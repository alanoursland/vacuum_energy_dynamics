"""Record-kind vocabulary for governance-aware archives."""

from enum import Enum


class RecordKind(str, Enum):
    DERIVATION = "derivation"
    SAMPLE_DERIVATION = "sample_derivation"
    COUNTEREXAMPLE = "counterexample"
    DIAGNOSTIC_EXAMPLE = "diagnostic_example"
    COMPATIBILITY_EXAMPLE = "compatibility_example"
    INVENTORY_MARKER = "inventory_marker"
    MEMO_STATEMENT = "memo_statement"
    MEMO_RECORD = "memo_record"
    GOVERNANCE_CLAIM = "governance_claim"
    EVIDENCE_OBJECT = "evidence_object"
    PROOF_OBLIGATION = "proof_obligation"
    BRANCH_DECISION = "branch_decision"
    ROUTE_RECORD = "route_record"
    HANDOFF_IMPORT = "handoff_import"
    SUMMARY_CLAIM = "summary_claim"
    SCRIPT_METADATA = "script_metadata"
    SUPERSEDED_RECORD = "superseded_record"
    UNARCHIVED_FOUNDATION = "unarchived_foundation"


class DerivationRecordQuality(str, Enum):
    CONTENTFUL = "contentful"
    PLACEHOLDER = "placeholder"
    INVENTORY_MARKER = "inventory_marker"
    SAMPLE = "sample"
    DIAGNOSTIC = "diagnostic"
    COMPATIBILITY = "compatibility"
    UNKNOWN = "unknown"
