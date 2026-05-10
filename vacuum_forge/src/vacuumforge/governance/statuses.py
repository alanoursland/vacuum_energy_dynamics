"""Governance status vocabulary."""

from enum import Enum


class GovernanceStatus(str, Enum):
    HEURISTIC = "heuristic"
    OPEN_RISK = "open_risk"
    POLICY_RULE = "policy_rule"
    UNPROVEN_EXCLUSION = "unproven_exclusion"
    UNRESOLVED_PROOF_OBLIGATION = "unresolved_proof_obligation"
    NOT_INSERTABLE_YET = "not_insertable_yet"
    DEFERRED_PENDING_PREREQUISITES = "deferred_pending_prerequisites"
    FAILED_BY_WITNESS = "failed_by_witness"
    KILLED_BY_CONTRADICTION = "killed_by_contradiction"
    CANDIDATE_ROUTE = "candidate_route"
    PROVISIONAL_CONVENTION = "provisional_convention"
    LICENSED_CLAIM = "licensed_claim"
    REJECTED_ROUTE = "rejected_route"
    SUPERSEDED = "superseded"
    SUPERSEDED_ROUTE = "superseded_route"
    UNVERIFIED = "unverified"
    ASSERTED_SATISFIED = "asserted_satisfied"
