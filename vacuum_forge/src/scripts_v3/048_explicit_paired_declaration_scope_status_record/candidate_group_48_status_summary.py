from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    ScriptOutput,
    StatusMark,
)

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"

SCRIPT_LABEL = "Candidate Group 48 Status Summary"
MARKER_ID = "g48_summary"
DEPENDENCIES = [
    ("g48_recon", "048_explicit_paired_declaration_scope_status_record__candidate_paired_scope_status_record_batch_reconciliation", "g48_recon"),
    ("g48_integrity_sieve", "048_explicit_paired_declaration_scope_status_record__candidate_scope_status_record_integrity_sieve", "g48_integrity_sieve"),
    ("g48_caveat_record", "048_explicit_paired_declaration_scope_status_record__candidate_downstream_caveat_and_rejected_broadening_record", "g48_caveat_record"),
    ("g48_assumption_domain", "048_explicit_paired_declaration_scope_status_record__candidate_assumption_domain_and_numeric_d_condition_record", "g48_assumption_domain"),
    ("g48_status_field", "048_explicit_paired_declaration_scope_status_record__candidate_status_field_and_nonactive_branch_record", "g48_status_field"),
    ("g48_schema", "048_explicit_paired_declaration_scope_status_record__candidate_paired_scope_record_schema", "g48_schema"),
    ("g48_problem", "048_explicit_paired_declaration_scope_status_record__candidate_paired_scope_status_record_problem", "g48_problem"),
    ("g47_summary", "047_normalization_declaration_scope_closure_audit__candidate_group_47_status_summary", "g47_summary"),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    topic: str
    status: str
    conclusion: str
    boundary: str


@dataclass(frozen=True)
class GapEntry:
    name: str
    status: str
    gap: str
    discipline: str


@dataclass(frozen=True)
class HandoffEntry:
    name: str
    status: str
    route: str
    caution: str


@dataclass(frozen=True)
class RejectedUpgrade:
    name: str
    upgrade: str
    reason: str


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def subheader(title: str) -> None:
    print()
    print("-" * 120)
    print(title)
    print("-" * 120)


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=RecordKind.INVENTORY_MARKER,
        )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def mark(status: str) -> StatusMark:
    return {
        "PASS": StatusMark.PASS,
        "MATCHED_EXPECTATION": StatusMark.PASS,
        "PAIRED_SCOPE_STATUS_RECORD": StatusMark.INFO,
        "SCOPE_STATUS_RECORD": StatusMark.INFO,
        "STATUS_FIELD": StatusMark.INFO,
        "DOMAIN_FIELD": StatusMark.INFO,
        "ASSUMPTION_FIELD": StatusMark.INFO,
        "CAVEAT_FIELD": StatusMark.INFO,
        "CLOSED_FOR_REVIEW": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "NON_ACTIVE": StatusMark.INFO,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "SCOPE_REQUIRED": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"POLICY_RULE", "SCOPE_REQUIRED", "NUMERIC_D_CONDITION"}:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, symbol_name: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=scope,
    )


def record_claim(ns, claim_id: str, marker_id: str, status: str, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=governance_status(status),
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, statement: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry(
            "G48-1: paired scope/status artifact instantiated",
            "explicit artifact requested by Group 47",
            "PAIRED_SCOPE_STATUS_RECORD",
            "Group 48 instantiated the paired declaration-scope/status record surface rather than repeating the scope audit.",
            "The artifact is pre-declaration infrastructure, not trace-normalization declaration.",
        ),
        StatusEntry(
            "G48-2: schema fields stated",
            "identity, domain, status, assumptions, caveats, and handoff fields",
            "SCOPE_STATUS_RECORD",
            "The record schema is explicit enough to be carried forward without hiding assumptions or caveats.",
            "Schema completeness is container integrity, not equation installation.",
        ),
        StatusEntry(
            "G48-3: status and non-active branch discipline",
            "pre-declaration status and paired branch status",
            "STATUS_FIELD",
            "The record explicitly says trace normalization remains not declared and both B_s_metric and b_s_scale remain non-active paired candidates.",
            "No metric branch, scale branch, or Package B status is chosen or adopted.",
        ),
        StatusEntry(
            "G48-4: assumptions and numeric-d condition",
            "paired domain, shared zeta, symbolic d, numeric-d condition, and factor-of-two preservation",
            "ASSUMPTION_FIELD",
            "The paired record domain, shared record-local zeta, shared symbolic d, and numeric-d condition are explicit.",
            "Numeric d is not fixed, and dimension handling cannot erase the factor-of-two burden.",
        ),
        StatusEntry(
            "G48-5: downstream caveats attached",
            "non-insertion, no active O, no safety theorem, and no parent-facing use",
            "CAVEAT_FIELD",
            "The record carries its own negative boundary: no B_s/F_zeta insertion, no active O, no residual/source theorem, no recombination, and no parent use.",
            "Negative caveats are not positive theorem support.",
        ),
        StatusEntry(
            "G48-6: rejected broadening preserved",
            "neutral-law, insertion-facing, parent-facing, active-O, and safety-proof broadening routes",
            "REJECTED_ROUTE",
            "Broadening the scope/status record into neutral law, insertion machinery, active projector, safety proof, or parent-facing trace scope remains rejected.",
            "The record cannot become downstream field-equation machinery by summary prose.",
        ),
        StatusEntry(
            "G48-7: integrity result",
            "assembled record coherence",
            "PAIRED_SCOPE_STATUS_RECORD",
            "The assembled record is coherent as pre-declaration infrastructure and can be carried forward as the artifact Group 47 requested.",
            "Integrity validation is not declaration readiness or Package B adoption.",
        ),
        StatusEntry(
            "G48-8: batch reconciliation",
            "actual batch outputs reconciled before summary",
            "MATCHED_EXPECTATION",
            "Outputs matched the expected shape: explicit paired scope/status record instantiated, assumptions visible, caveats attached, no declaration or downstream route opened.",
            "Reconciliation is not group closure by itself, branch choice, declaration completion, adoption, theorem proof, or insertion.",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry(
            "G1: trace-normalization declaration",
            "NOT_DECLARED",
            "The paired scope/status record is now instantiated, but trace normalization remains undeclared.",
            "A separate declaration record is required before any candidate expression becomes declared trace-normalization content.",
        ),
        GapEntry(
            "G2: declaration-review decision",
            "DEFERRED_WITH_TARGET",
            "The next route is review for a possible parallel trace-normalization declaration attempt, not automatic declaration.",
            "Do not jump from artifact integrity to equation installation.",
        ),
        GapEntry(
            "G3: numeric d condition",
            "SCOPE_REQUIRED",
            "Numeric d remains conditioned on explicit scope/declaration support and is not fixed by the record.",
            "Do not set d by recovery, aesthetics, or factor-of-two erasure.",
        ),
        GapEntry(
            "G4: branch choice",
            "NOT_CHOSEN",
            "B_s_metric and b_s_scale remain paired non-active candidates.",
            "The scope/status artifact cannot select one branch or activate both.",
        ),
        GapEntry(
            "G5: Package B adoption",
            "NOT_ADOPTED",
            "Record instantiation is not Package B adoption or recommendation.",
            "Adoption remains a separate explicit theory decision.",
        ),
        GapEntry(
            "G6: downstream safety and parent routes",
            "NOT_READY",
            "B_s/F_zeta insertion, active O, residual/source safety, recombination, and parent closure remain closed.",
            "The record is not scalar-response law, projector construction, safety theorem, or parent identity.",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: declaration-readiness review",
            "DEFERRED_WITH_TARGET",
            "Evaluate whether the instantiated paired scope/status record plus existing assumptions are sufficient to attempt a separate parallel trace-normalization declaration record.",
            "This review is not the declaration itself and must be allowed to say no.",
        ),
        HandoffEntry(
            "H2: parallel trace-normalization declaration attempt",
            "NOT_DECLARED",
            "Attempt only if a later review accepts the scope/status record, numeric-d condition, non-active branch status, and caveats as adequate for a declaration route.",
            "Declaration must be a separate explicit record, not a summary upgrade.",
        ),
        HandoffEntry(
            "H3: explicit branch-choice route",
            "NOT_CHOSEN",
            "Use only if the project leaves the paired route and deliberately chooses metric or scale in a daylight-labeled choice record.",
            "The paired record cannot choose for us.",
        ),
        HandoffEntry(
            "H4: residual/source safety theorem route",
            "NOT_DERIVED",
            "Continue theorem work if declaration review depends on safety support before any physical use.",
            "Record caveats do not prove safety.",
        ),
        HandoffEntry(
            "H5: insertion or parent route",
            "NOT_READY",
            "Not available from Group 48.",
            "Requires separate scalar-response law, safety gates, active-projector construction if needed, and parent identity support.",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade("R1: record as declaration", "Treat the instantiated scope/status record as completed trace-normalization declaration", "Record instantiation is pre-declaration infrastructure."),
        RejectedUpgrade("R2: schema as equation", "Treat schema completeness as equation installation", "A schema is a container, not a field equation."),
        RejectedUpgrade("R3: paired status as branch choice", "Use paired status to choose metric, scale, or both branches", "Both branch records remain non-active candidates."),
        RejectedUpgrade("R4: numeric d leak", "Quietly fix numeric d inside the record", "Numeric d remains scope-conditioned."),
        RejectedUpgrade("R5: record as insertion", "Use scope/status clarity to insert B_s/F_zeta", "Insertion requires a separate scalar-response law and safety gates."),
        RejectedUpgrade("R6: record as active O", "Treat scope/status fields as projector machinery", "Fields are not operators."),
        RejectedUpgrade("R7: caveats as theorems", "Treat negative caveats as residual/source safety proofs", "Safety theorems remain separate."),
        RejectedUpgrade("R8: record as adoption", "Treat artifact completion as Package B adoption", "Adoption remains a separate explicit theory decision."),
        RejectedUpgrade("R9: record as parent-ready", "Call the record parent-facing or parent-ready", "Parent-facing use requires identity and safety support."),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 48 establish by instantiating the explicit paired")
    print("  declaration-scope/status record requested by Group 47?\n")
    print("Discipline:\n")
    print("  This script summarizes Group 48 after reviewing the batch outputs.")
    print("  It preserves record-instantiated status while keeping trace normalization")
    print("  undeclared. It chooses no branch, adopts nothing, inserts nothing,")
    print("  constructs no active O, and opens no parent gate.")
    with out.governance_assessments():
        out.line("Group 48 status summary opened", StatusMark.PASS, "closing paired scope/status record instantiation while preserving no-declaration / no-insertion boundary")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 48 summary boundary ledger")
    ledger = [
        ("paired scope/status record", "PAIRED_SCOPE_STATUS_RECORD", "explicit paired declaration-scope/status record surface instantiated"),
        ("schema fields", "SCOPE_STATUS_RECORD", "identity, domain, status, assumptions, caveats, and handoff fields explicit"),
        ("status discipline", "STATUS_FIELD", "pre-declaration / not declared status carried on the record"),
        ("branch status", "NON_ACTIVE", "B_s_metric and b_s_scale remain paired non-active candidates"),
        ("assumptions", "ASSUMPTION_FIELD", "paired domain, shared zeta, symbolic d, and numeric-d condition visible"),
        ("numeric d", "NUMERIC_D_CONDITION", "numeric d remains conditioned, not fixed"),
        ("downstream caveats", "CAVEAT_FIELD", "no insertion, active O, residual/source theorem, recombination, or parent use"),
        ("rejected broadening", "REJECTED_ROUTE", "neutral-law, insertion-facing, parent-facing, active-O, and safety-proof broadening rejected"),
        ("trace declaration", "NOT_DECLARED", "trace normalization remains undeclared"),
        ("downstream gates", "NOT_READY", "adoption, insertion, active O, residual control, recombination, and parent closure remain closed"),
    ]
    for subject, status, text in ledger:
        with out.governance_assessments():
            out.line(subject, mark(status), f"{status}: {text}")


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 48 status entries")
    for entry in entries:
        subheader(entry.name)
        print(f"Topic: {entry.topic}")
        with out.governance_assessments():
            out.line(entry.name, mark(entry.status), f"{entry.status}: {entry.conclusion} Boundary: {entry.boundary}")
    with out.governance_assessments():
        out.line("Group 48 status entries stated", StatusMark.PASS, f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for gap in gaps:
        subheader(gap.name)
        with out.unresolved_obligations():
            out.line(gap.name, mark(gap.status), f"{gap.status}: {gap.gap} Discipline: {gap.discipline}")
    with out.unresolved_obligations():
        out.line("Group 48 final gaps stated", StatusMark.PASS, f"{len(gaps)} gaps remain open, conditioned, not chosen, not declared, not adopted, not derived, or not ready")


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for handoff in handoffs:
        subheader(handoff.name)
        with out.governance_assessments():
            out.line(handoff.name, mark(handoff.status), f"{handoff.status}: {handoff.route} Caution: {handoff.caution}")
    with out.governance_assessments():
        out.line("Group 48 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; declaration-readiness review is the next non-looping target")


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.reason}")
    with out.governance_assessments():
        out.line("Group 48 summary upgrades rejected", StatusMark.PASS, f"{len(rejected)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 48 conclusions")
    conclusions = [
        ("C1: Group 48 result", "PAIRED_SCOPE_STATUS_RECORD", "Group 48 instantiated the explicit paired declaration-scope/status record"),
        ("C2: record integrity", "PAIRED_SCOPE_STATUS_RECORD", "the record is coherent as pre-declaration infrastructure"),
        ("C3: status result", "STATUS_FIELD", "status, non-active branch clauses, assumptions, numeric-d condition, and caveats are explicit"),
        ("C4: declaration status", "NOT_DECLARED", "trace normalization is not declared"),
        ("C5: branch/adoption status", "NOT_ADOPTED", "no branch is chosen and Package B is not adopted"),
        ("C6: downstream status", "NOT_READY", "B_s/F_zeta insertion, active O, recombination, and parent equation remain not ready"),
    ]
    for name, status, text in conclusions:
        subheader(name)
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {text}")
    with out.governance_assessments():
        out.line("Group 48 status summary conclusion stated", StatusMark.PASS, "paired scope/status record instantiated; no declaration, adoption, insertion, active O, recombination, or parent route opened")
    header("Final interpretation")
    print("Group 48 status summary result:\n")
    print("  Group 48 instantiated the explicit paired declaration-scope/status record requested by Group 47.")
    print("  The record names its identity, paired-record domain, status, assumptions, numeric-d condition, branch status, caveats, and handoff route.")
    print("  The domain is the paired non-active B_s_metric / b_s_scale record surface, not a physical insertion domain.")
    print("  Shared zeta and symbolic d are inherited for record use; numeric d remains conditioned and not fixed.")
    print("  B_s_metric and b_s_scale remain paired, labeled, non-active, and not chosen.")
    print("  The record carries no-insertion, no-active-O, no-residual/source-theorem, no-recombination, and no-parent caveats.")
    print("  Broadening into neutral law, insertion-facing scope, parent-facing scope, active O, or safety proof remains rejected.")
    print("  No trace-normalization declaration is completed.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, source protection, recombination, and parent equation remain not ready.\n")
    print("Possible next step:")
    print("  declaration-readiness review for a possible parallel trace-normalization declaration attempt, then only later a separate declaration record if assumptions remain acceptable\n")
    print("Forbidden immediate next step:")
    print("  Package B adoption, B_s/F_zeta insertion, active O, recombination, or parent closure")


def record_governance(
    ns,
    entries: List[StatusEntry],
    gaps: List[GapEntry],
    handoffs: List[HandoffEntry],
    rejected: List[RejectedUpgrade],
) -> None:
    record_marker(ns, MARKER_ID, "g48_paired_scope_status_record", "Group 48 status summary marker: paired scope/status record instantiated only")
    for idx, entry in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, entry.status, f"{entry.name}: {entry.conclusion} Boundary: {entry.boundary}")
    for idx, gap in enumerate(gaps, 1):
        oid = f"{MARKER_ID}_gap{idx}"
        record_obligation(ns, oid, f"{gap.name}: {gap.gap} Discipline: {gap.discipline}", gap.status)
        record_claim(ns, f"{MARKER_ID}_gap_claim{idx}", MARKER_ID, gap.status, f"{gap.name}: {gap.gap}")
    for idx, handoff in enumerate(handoffs, 1):
        record_claim(ns, f"{MARKER_ID}_h{idx}", MARKER_ID, handoff.status, f"{handoff.name}: {handoff.route} Caution: {handoff.caution}")
    for idx, item in enumerate(rejected, 1):
        record_claim(ns, f"{MARKER_ID}_r{idx}", MARKER_ID, "POLICY_RULE", f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_status_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rejected = build_rejected_upgrades()
    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, gaps)
    case_4(out, handoffs)
    case_5(out, rejected)
    case_6(out)
    record_governance(ns, entries, gaps, handoffs, rejected)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
