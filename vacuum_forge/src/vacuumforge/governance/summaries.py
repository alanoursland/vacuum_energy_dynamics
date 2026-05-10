"""Archive-backed governance summaries and claim-upgrade checks."""

from __future__ import annotations

from dataclasses import dataclass, field

from vacuumforge.archive.archive import ProjectArchive
from vacuumforge.governance.kinds import RecordKind
from vacuumforge.governance.records import (
    BranchDecisionRecord,
    ClaimRecord,
    EvidenceRecord,
    HandoffImportRecord,
    ProofObligationRecord,
)
from vacuumforge.governance.evidence import EvidenceType
from vacuumforge.governance.statuses import GovernanceStatus


_STRENGTH = {
    "unverified": 0,
    "heuristic": 1,
    "open_risk": 2,
    "unresolved_proof_obligation": 2,
    "candidate_route": 3,
    "not_insertable_yet": 3,
    "deferred_pending_prerequisites": 3,
    "policy_rule": 3,
    "provisional_convention": 4,
    "unproven_exclusion": 4,
    "rejected_route": 5,
    "failed_by_witness": 6,
    "killed_by_contradiction": 7,
    "licensed_claim": 7,
    "derived": 8,
}


@dataclass
class UpgradeCheckResult:
    claim_id: str
    upgraded: bool
    message: str


@dataclass
class GovernanceSummary:
    script_ids: list[str]
    derived_results: list[str] = field(default_factory=list)
    sample_results: list[str] = field(default_factory=list)
    evidence: list[EvidenceRecord] = field(default_factory=list)
    counterexamples: list[EvidenceRecord] = field(default_factory=list)
    claims: list[ClaimRecord] = field(default_factory=list)
    branch_decisions: list[BranchDecisionRecord] = field(default_factory=list)
    handoff_imports: list[HandoffImportRecord] = field(default_factory=list)
    open_obligations: list[ProofObligationRecord] = field(default_factory=list)
    superseded_records: list[str] = field(default_factory=list)
    unsupported_claims: list[ClaimRecord] = field(default_factory=list)
    upgrade_warnings: list[UpgradeCheckResult] = field(default_factory=list)

    def to_markdown(self) -> str:
        lines = ["# Governance Summary", ""]
        lines.append(f"Scripts: {', '.join(self.script_ids) if self.script_ids else '(none)'}")
        lines.append("")
        lines.append(f"- Derived results: {len(self.derived_results)}")
        lines.append(f"- Sample results: {len(self.sample_results)}")
        lines.append(f"- Evidence objects: {len(self.evidence)}")
        lines.append(f"- Counterexamples: {len(self.counterexamples)}")
        lines.append(f"- Claims: {len(self.claims)}")
        lines.append(f"- Branch decisions: {len(self.branch_decisions)}")
        lines.append(f"- Handoff imports: {len(self.handoff_imports)}")
        lines.append(f"- Open obligations: {len(self.open_obligations)}")
        lines.append(f"- Superseded records: {len(self.superseded_records)}")
        lines.append(f"- Unsupported claims: {len(self.unsupported_claims)}")
        lines.append(f"- Upgrade warnings: {len(self.upgrade_warnings)}")
        return "\n".join(lines)


def _status_value(status) -> str:
    return status.value if hasattr(status, "value") else str(status)


def _strength(status) -> int:
    return _STRENGTH.get(_status_value(status), 0)


def check_claim_strength_upgrade(claim: ClaimRecord, upstream_claims: list[ClaimRecord]) -> UpgradeCheckResult:
    if not claim.source_claim_ids or claim.evidence_ids or claim.derivation_ids:
        return UpgradeCheckResult(claim.claim_id, False, "No unsupported upgrade detected.")
    upstream = [c for c in upstream_claims if c.claim_id in claim.source_claim_ids]
    if not upstream:
        return UpgradeCheckResult(claim.claim_id, False, "No referenced upstream claims found.")
    max_upstream = max(_strength(c.status) for c in upstream)
    current = _strength(claim.status)
    if current > max_upstream:
        return UpgradeCheckResult(
            claim.claim_id,
            True,
            f"Claim strength {_status_value(claim.status)} exceeds upstream support.",
        )
    return UpgradeCheckResult(claim.claim_id, False, "No unsupported upgrade detected.")


class GovernanceSummaryBuilder:
    """Build a structured summary from one or more archive namespaces."""

    def __init__(self, archive: ProjectArchive) -> None:
        self.archive = archive

    def build(self, script_ids: list[str] | None = None) -> GovernanceSummary:
        namespaces = (
            [self.archive.script_namespace(s) for s in script_ids]
            if script_ids is not None
            else self.archive._namespaces()
        )
        summary = GovernanceSummary(script_ids=[ns.script_id for ns in namespaces])
        all_claims: list[ClaimRecord] = []
        for ns in namespaces:
            for path in ns.derivations_path.glob("*.json"):
                record = ns.get_derivation(path.stem)
                if record is None:
                    continue
                if record.record_kind == RecordKind.SAMPLE_DERIVATION:
                    summary.sample_results.append(f"{ns.script_id}:{record.derivation_id}")
                elif record.record_kind == RecordKind.DERIVATION:
                    summary.derived_results.append(f"{ns.script_id}:{record.derivation_id}")
                if record.superseded_by:
                    summary.superseded_records.append(f"{ns.script_id}:{record.derivation_id}")
            summary.evidence.extend(ns.list_evidence())
            summary.counterexamples.extend(
                ev for ev in ns.list_evidence()
                if ev.evidence_type == EvidenceType.COUNTEREXAMPLE
            )
            summary.branch_decisions.extend(ns.list_branch_decisions())
            summary.handoff_imports.extend(ns.list_handoff_imports())
            summary.open_obligations.extend(ns.list_obligations())
            claims = ns.list_claims()
            all_claims.extend(claims)
            summary.claims.extend(claims)
            summary.unsupported_claims.extend(
                c for c in claims if not c.metadata.get("validation", {}).get("supported", True)
            )
        for claim in all_claims:
            result = check_claim_strength_upgrade(claim, all_claims)
            if result.upgraded:
                summary.upgrade_warnings.append(result)
        summary.open_obligations = [
            o for o in summary.open_obligations if o.status.value == "open"
        ]
        return summary
