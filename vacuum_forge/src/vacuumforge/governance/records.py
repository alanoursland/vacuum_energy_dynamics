"""Governance record dataclasses and derivation-quality helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

import sympy

from vacuumforge.core.status import Status
from vacuumforge.governance.evidence import EvidenceType, ReasonCode
from vacuumforge.governance.kinds import DerivationRecordQuality, RecordKind
from vacuumforge.governance.statuses import GovernanceStatus
from vacuumforge.governance.tiers import ClaimTier


class ObligationStatus(str, Enum):
    OPEN = "open"
    SATISFIED = "satisfied"
    FAILED = "failed"
    SUPERSEDED = "superseded"
    ABANDONED = "abandoned"
    DEFERRED = "deferred"


@dataclass
class ArchiveRecordBase:
    record_id: str
    record_kind: RecordKind
    script_id: str
    created_at: str = ""
    description: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class EvidenceRecord:
    evidence_id: str
    evidence_type: EvidenceType
    script_id: str
    supports: list[str] = field(default_factory=list)
    challenges: list[str] = field(default_factory=list)
    reason_code: ReasonCode | None = None
    expression: sympy.Basic | None = None
    expected: sympy.Basic | None = None
    observed: sympy.Basic | None = None
    residual: sympy.Basic | None = None
    source_records: list[str] = field(default_factory=list)
    status: str = "active"
    created_at: str = ""
    description: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ProofObligationRecord:
    obligation_id: str
    script_id: str
    title: str
    status: ObligationStatus
    required_by: list[str] = field(default_factory=list)
    satisfied_by: list[str] = field(default_factory=list)
    failed_by: list[str] = field(default_factory=list)
    superseded_by: str | None = None
    created_at: str = ""
    description: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ClaimRecord:
    claim_id: str
    script_id: str
    claim_kind: RecordKind
    tier: ClaimTier
    status: GovernanceStatus | Status | str
    statement: str
    reason_code: ReasonCode | None = None
    evidence_ids: list[str] = field(default_factory=list)
    derivation_ids: list[str] = field(default_factory=list)
    obligation_ids: list[str] = field(default_factory=list)
    source_claim_ids: list[str] = field(default_factory=list)
    supersedes: list[str] = field(default_factory=list)
    superseded_by: str | None = None
    created_at: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class BranchDecisionRecord:
    decision_id: str
    script_id: str
    branch_id: str
    status: GovernanceStatus
    tier: ClaimTier
    reason_code: ReasonCode | None = None
    evidence_ids: list[str] = field(default_factory=list)
    obligation_ids: list[str] = field(default_factory=list)
    activation_conditions: list[str] = field(default_factory=list)
    superseded_by: str | None = None
    created_at: str = ""
    description: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class RouteRecord:
    route_id: str
    script_id: str
    name: str
    status: GovernanceStatus
    tier: ClaimTier
    witness_ids: list[str] = field(default_factory=list)
    activation_conditions: list[str] = field(default_factory=list)
    required_obligations: list[str] = field(default_factory=list)
    created_at: str = ""
    description: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class HandoffImportRecord:
    handoff_id: str
    script_id: str
    imported_as: RecordKind
    status: GovernanceStatus | Status | str
    source_record_ref: str = ""
    imported_record_refs: list[str] = field(default_factory=list)
    created_at: str = ""
    description: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.source_record_ref and self.source_record_ref not in self.imported_record_refs:
            self.imported_record_refs.append(self.source_record_ref)


@dataclass
class ClaimValidationResult:
    requested_status: str
    effective_status: str
    supported: bool
    messages: list[str] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)


def classify_derivation_record(record: Any) -> DerivationRecordQuality:
    """Classify whether an archive derivation carries mathematical content."""
    record_kind = getattr(record, "record_kind", RecordKind.DERIVATION)
    if isinstance(record_kind, str):
        try:
            record_kind = RecordKind(record_kind)
        except ValueError:
            record_kind = RecordKind.DERIVATION

    if record_kind == RecordKind.SAMPLE_DERIVATION:
        return DerivationRecordQuality.SAMPLE
    if record_kind == RecordKind.DIAGNOSTIC_EXAMPLE:
        return DerivationRecordQuality.DIAGNOSTIC
    if record_kind == RecordKind.COMPATIBILITY_EXAMPLE:
        return DerivationRecordQuality.COMPATIBILITY
    if record_kind == RecordKind.INVENTORY_MARKER:
        return DerivationRecordQuality.INVENTORY_MARKER
    if getattr(record, "is_placeholder", False):
        return DerivationRecordQuality.PLACEHOLDER

    inputs = list(getattr(record, "inputs", []) or [])
    output = getattr(record, "output", None)
    if not inputs and isinstance(output, sympy.Symbol):
        name = str(output)
        if name.endswith("_stated") or name.endswith("_marker") or "stated" in name:
            return DerivationRecordQuality.PLACEHOLDER

    method = str(getattr(record, "method", "")).lower()
    if "inventory" in method or "marker" in method:
        return DerivationRecordQuality.INVENTORY_MARKER
    if inputs and output is not None:
        return DerivationRecordQuality.CONTENTFUL
    return DerivationRecordQuality.UNKNOWN
