"""In-memory governance manager for TheoryContext workflows."""

from __future__ import annotations

from vacuumforge.governance.records import (
    BranchDecisionRecord,
    ClaimRecord,
    EvidenceRecord,
    ProofObligationRecord,
    RouteRecord,
)
from vacuumforge.governance.statuses import GovernanceStatus
from vacuumforge.governance.validation import validate_branch_decision, validate_claim_support, validate_route


class GovernanceManager:
    """Small in-memory store for governance records.

    Persistent cross-script workflows should use ``ProjectArchive``.  This
    manager exists for notebooks, tests, and single-context experiments.
    """

    def __init__(self) -> None:
        self.evidence: dict[str, EvidenceRecord] = {}
        self.obligations: dict[str, ProofObligationRecord] = {}
        self.claims: dict[str, ClaimRecord] = {}
        self.branches: dict[str, BranchDecisionRecord] = {}
        self.routes: dict[str, RouteRecord] = {}

    def record_evidence(self, record: EvidenceRecord) -> EvidenceRecord:
        self.evidence[record.evidence_id] = record
        return record

    def record_obligation(self, record: ProofObligationRecord) -> ProofObligationRecord:
        self.obligations[record.obligation_id] = record
        return record

    def record_claim(self, record: ClaimRecord) -> ClaimRecord:
        validation = validate_claim_support(record, resolver=self)
        record.metadata["validation"] = validation.__dict__
        if not validation.supported:
            record.status = GovernanceStatus(validation.effective_status)
        self.claims[record.claim_id] = record
        return record

    def record_branch_decision(self, record: BranchDecisionRecord) -> BranchDecisionRecord:
        validation = validate_branch_decision(record, resolver=self)
        record.metadata["validation"] = validation.__dict__
        if not validation.supported:
            record.status = GovernanceStatus(validation.effective_status)
        self.branches[record.decision_id] = record
        return record

    def record_route(self, record: RouteRecord) -> RouteRecord:
        validation = validate_route(record, resolver=self)
        record.metadata["validation"] = validation.__dict__
        if not validation.supported:
            record.status = validation.effective_status
        self.routes[record.route_id] = record
        return record

    def has_evidence(self, evidence_id: str) -> bool:
        return evidence_id in self.evidence

    def has_derivation(self, derivation_id: str) -> bool:
        return False
