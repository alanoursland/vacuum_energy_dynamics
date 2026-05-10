"""Claim-support and downgrade rules."""

from __future__ import annotations

from typing import Protocol

from vacuumforge.core.status import Status
from vacuumforge.governance.kinds import RecordKind
from vacuumforge.governance.records import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimValidationResult,
    RouteRecord,
)
from vacuumforge.governance.statuses import GovernanceStatus
from vacuumforge.governance.tiers import ClaimTier


class GovernanceResolver(Protocol):
    def has_evidence(self, evidence_id: str) -> bool: ...
    def has_derivation(self, derivation_id: str) -> bool: ...


def _status_value(status: GovernanceStatus | Status | str) -> str:
    return status.value if hasattr(status, "value") else str(status)


def _has_support(evidence_ids: list[str], derivation_ids: list[str], resolver=None) -> bool:
    if not evidence_ids and not derivation_ids:
        return False
    if resolver is None:
        return True
    return any(resolver.has_evidence(e) for e in evidence_ids) or any(
        resolver.has_derivation(d) for d in derivation_ids
    )


def downgrade_unsupported_status(
    status: GovernanceStatus | Status | str,
    tier: ClaimTier,
) -> GovernanceStatus | Status | str:
    """Return the strongest allowed status when support is missing."""
    value = _status_value(status)
    if tier == ClaimTier.EXCLUSION:
        if value in {
            GovernanceStatus.KILLED_BY_CONTRADICTION.value,
            GovernanceStatus.FAILED_BY_WITNESS.value,
            GovernanceStatus.REJECTED_ROUTE.value,
            "branch_killed",
            "forbidden",
            "rejected",
        }:
            return GovernanceStatus.UNPROVEN_EXCLUSION
    if tier == ClaimTier.LICENSING:
        if value in {GovernanceStatus.LICENSED_CLAIM.value, "licensed", "derived"}:
            return GovernanceStatus.CANDIDATE_ROUTE
    if isinstance(status, Status) and status == Status.DERIVED:
        return GovernanceStatus.UNVERIFIED
    return status


def validate_claim_support(claim: ClaimRecord, resolver=None) -> ClaimValidationResult:
    requested = _status_value(claim.status)
    messages: list[str] = []
    missing: list[str] = []

    if claim.tier == ClaimTier.INFORMATIONAL:
        return ClaimValidationResult(requested, requested, True)

    if claim.tier == ClaimTier.CONSTRAINED:
        if claim.reason_code or claim.evidence_ids or claim.derivation_ids or claim.obligation_ids:
            return ClaimValidationResult(requested, requested, True)
        effective = GovernanceStatus.HEURISTIC.value
        messages.append("Tier 2 claim lacks reason, provenance, evidence, or obligation links.")
        missing.append("reason_or_provenance")
        return ClaimValidationResult(requested, effective, False, messages, missing)

    supported = _has_support(claim.evidence_ids, claim.derivation_ids, resolver)
    if supported:
        return ClaimValidationResult(requested, requested, True)

    effective = _status_value(downgrade_unsupported_status(claim.status, claim.tier))
    messages.append("Tier 3 claim lacks structured evidence or derivation support.")
    missing.append("evidence_or_derivation")
    return ClaimValidationResult(requested, effective, False, messages, missing)


def validate_branch_decision(decision: BranchDecisionRecord, resolver=None) -> ClaimValidationResult:
    claim = ClaimRecord(
        claim_id=decision.decision_id,
        script_id=decision.script_id,
        claim_kind=RecordKind.BRANCH_DECISION,
        tier=decision.tier,
        status=decision.status,
        statement=decision.description or decision.branch_id,
        reason_code=decision.reason_code,
        evidence_ids=decision.evidence_ids,
        derivation_ids=[],
        obligation_ids=decision.obligation_ids,
    )
    return validate_claim_support(claim, resolver=resolver)


def validate_route(route: RouteRecord, resolver=None) -> ClaimValidationResult:
    claim = ClaimRecord(
        claim_id=route.route_id,
        script_id=route.script_id,
        claim_kind=RecordKind.ROUTE_RECORD,
        tier=route.tier,
        status=route.status,
        statement=route.description or route.name,
        evidence_ids=route.witness_ids,
        obligation_ids=route.required_obligations,
    )
    return validate_claim_support(claim, resolver=resolver)
