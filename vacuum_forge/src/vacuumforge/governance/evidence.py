"""Evidence and reason-code vocabulary."""

from enum import Enum


class EvidenceType(str, Enum):
    COUNTEREXAMPLE = "counterexample"
    DEPENDENCY_LEAK = "dependency_leak"
    OVERLAP_WITNESS = "overlap_witness"
    BOUNDARY_VIOLATION = "boundary_violation"
    EXTERIOR_SCALAR_CHARGE_WITNESS = "exterior_scalar_charge_witness"
    TARGET_SELECTED_PARAMETER = "target_selected_parameter"
    RECOVERY_PRECEDES_ORIGIN = "recovery_precedes_origin"
    FAILED_CONSERVATION_CHECK = "failed_conservation_check"
    FAILED_BOUNDARY_NEUTRALITY_CHECK = "failed_boundary_neutrality_check"
    DUPLICATE_DEGREE_OF_FREEDOM_WITNESS = "duplicate_degree_of_freedom_witness"
    CONTRADICTION_RECORD = "contradiction_record"
    STALE_DEPENDENCY = "stale_dependency"
    SUPERSEDED_DEPENDENCY = "superseded_dependency"
    SAMPLE_ONLY_SUPPORT = "sample_only_support"


class ReasonCode(str, Enum):
    RECOVERY_SELECTED_PARAMETER = "recovery_selected_parameter"
    GR_COPY_CONSTRUCTION = "gr_copy_construction"
    BOUNDARY_REPAIR_AFTER_FAILURE = "boundary_repair_after_failure"
    DOUBLE_COUNTING_WITHOUT_OVERLAP_WITNESS = "double_counting_without_overlap_witness"
    EXTERIOR_SCALAR_CHARGE = "exterior_scalar_charge"
    UNRESOLVED_OVERLAP = "unresolved_overlap"
    MISSING_BOUNDARY_NEUTRALITY_THEOREM = "missing_boundary_neutrality_theorem"
    MISSING_COEFFICIENT_ORIGIN = "missing_coefficient_origin"
    UNRESOLVED_SOURCE_IDENTITY = "unresolved_source_identity"
    UNRESOLVED_PARENT_IDENTITY = "unresolved_parent_identity"
    STALE_DEPENDENCY = "stale_dependency"
    SUPERSEDED_DEPENDENCY = "superseded_dependency"
    SAMPLE_ONLY_SUPPORT = "sample_only_support"
