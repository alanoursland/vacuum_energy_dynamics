# VacuumForge Governance Validation Technical Design

## Companion Documents

This document is the implementation-level companion to:

```text
overview.md
feature_design.md
```

The overview explains why this development phase exists. The feature design specifies behavioral requirements. This document describes how to implement those behaviors in the current VacuumForge codebase.

This is not a physics design document. It does not add new gravitational assumptions, field equations, source laws, or recovery targets. It extends VacuumForge so that AI-authored scripts can make machine-visible distinctions among derivations, evidence, governance claims, proof obligations, branch decisions, samples, inventories, and summaries.

## Current Codebase Integration Points

The dehydrated code shows that VacuumForge already has the following relevant infrastructure:

```text
src/vacuumforge/core/context.py
src/vacuumforge/core/dependency.py
src/vacuumforge/core/ledger.py
src/vacuumforge/core/status.py
src/vacuumforge/archive/archive.py
src/vacuumforge/archive/records.py
src/vacuumforge/archive/serialization.py
src/vacuumforge/archive/invalidation.py
src/vacuumforge/archive/cli.py
src/vacuumforge/requirements/validators.py
src/vacuumforge/requirements/leak_detection.py
src/vacuumforge/metric/concrete_check.py
src/vacuumforge/coordinates/transform.py
src/vacuumforge/structure_search/
src/vacuumforge/theorems/candidates.py
```

The current archive already supports `ProjectArchive`, per-script `ScriptNamespace`, `record_derivation`, `declare_dependency`, `verify_dependencies`, cycle detection, invalidation, run metadata, CLI listing, CLI verification, CLI invalidation, and archive doctor checks.

The current `TheoryContext` already carries a dependency graph, ledger, requirement manager, source manager, energy manager, theorem registry, structure-search engine, concrete metric checks, coordinate transformations, and report generation.

This phase should build on those pieces. It should not replace them.

The main gap is that the existing archive is derivation-centered. It can record that a script produced a derivation-like marker, but it does not yet express the different epistemic kinds that now matter:

```text
derivation
sample derivation
counterexample
diagnostic example
inventory marker
governance claim
proof obligation
evidence object
branch decision
handoff import
summary claim
script metadata
```

The implementation should therefore add a governance layer above the archive while preserving the current derivation API.

## Design Goals

The technical design should satisfy these goals.

1. Preserve the existing algebra-validation system.
2. Extend the archive without breaking existing scripts.
3. Make claim kind and claim strength explicit.
4. Require evidence for strong governance claims.
5. Track unresolved proof obligations as first-class records.
6. Let summaries query archive state rather than restating it from memory.
7. Detect unsupported claim-strength upgrades.
8. Distinguish real derivations from samples, diagnostics, inventories, and memos.
9. Make branch decisions machine-readable.
10. Give linting enough structure to catch validation theater and governance theater.

## Non-Goals

This phase should not attempt to:

```text
validate undefined physics objects;
derive a covariant parent theory;
prove GR recovery;
turn every heuristic into a theorem;
auto-discover all equivalent target forms;
replace SymPy or the existing requirement validators;
force every script to be a derivation script.
```

The goal is not to prevent exploratory work. The goal is to label it correctly.

## Proposed Package Structure

Add a new package:

```text
src/vacuumforge/governance/
    __init__.py
    kinds.py
    tiers.py
    statuses.py
    records.py
    evidence.py
    obligations.py
    claims.py
    branches.py
    routes.py
    validation.py
    summaries.py
    output.py
    lint_models.py
```

Add governance-aware archive extensions in:

```text
src/vacuumforge/archive/records.py
src/vacuumforge/archive/archive.py
src/vacuumforge/archive/serialization.py
src/vacuumforge/archive/cli.py
src/vacuumforge/archive/invalidation.py
```

Add standalone lint tooling:

```text
tools/vf_lint/
    __init__.py
    cli.py
    analyzer.py
    rules.py
    traces.py
    governance_rules.py
    archive_rules.py
    output.py
    tests/
```

Add runner/order utilities if the script runner is inside the repository:

```text
tools/vf_runner_checks/
    order_check.py
    result_check.py
```

If runner code is already elsewhere, put these checks next to the existing runner instead of creating a new tool package.

## Core Type System

### Record Kind

Create an enum in `vacuumforge/governance/kinds.py`:

```python
from enum import Enum

class RecordKind(str, Enum):
    DERIVATION = "derivation"
    SAMPLE_DERIVATION = "sample_derivation"
    COUNTEREXAMPLE = "counterexample"
    DIAGNOSTIC_EXAMPLE = "diagnostic_example"
    COMPATIBILITY_EXAMPLE = "compatibility_example"
    INVENTORY_MARKER = "inventory_marker"
    MEMO_STATEMENT = "memo_statement"
    GOVERNANCE_CLAIM = "governance_claim"
    EVIDENCE_OBJECT = "evidence_object"
    PROOF_OBLIGATION = "proof_obligation"
    BRANCH_DECISION = "branch_decision"
    ROUTE_RECORD = "route_record"
    HANDOFF_IMPORT = "handoff_import"
    SUMMARY_CLAIM = "summary_claim"
    SCRIPT_METADATA = "script_metadata"
```

This must be separate from the existing `Status` enum. `RecordKind` says what kind of object is being recorded. `Status` or governance statuses say what state that object is in.

Existing `DerivationRecord` instances should be treated as `RecordKind.DERIVATION` by default unless they explicitly declare another kind.

### Claim Tier

Create `vacuumforge/governance/tiers.py`:

```python
from enum import Enum

class ClaimTier(str, Enum):
    INFORMATIONAL = "informational"      # Tier 1
    CONSTRAINED = "constrained"          # Tier 2
    EXCLUSION = "exclusion"              # Tier 3
    LICENSING = "licensing"              # Tier 3
```

`LICENSING` is technically Tier 3 because claiming a route is safe for downstream use can be as strong as killing a route. It should require derivation/evidence support.

### Governance Status

Create `vacuumforge/governance/statuses.py`:

```python
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
    UNVERIFIED = "unverified"
    ASSERTED_SATISFIED = "asserted_satisfied"
```

Do not add these values to the existing derivation `Status` enum unless absolutely necessary. Mixing derivation status and governance status recreates the problem this phase is trying to solve.

### Evidence Type

Create `vacuumforge/governance/evidence.py`:

```python
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
```

### Reason Code

Create `vacuumforge/governance/evidence.py` or `reasons.py`:

```python
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
```

Reason codes are not evidence by themselves. They classify why a claim or decision exists. Strong decisions still need evidence records.

## Archive Record Extensions

The existing `archive.records` module should be extended. If it already contains `DerivationRecord`, `DependencyDeclaration`, and `DependencyCheckResult`, keep those intact and add new dataclasses.

### Base Archive Record

Add a lightweight base dataclass that all new record types can share:

```python
@dataclass(frozen=True)
class ArchiveRecordBase:
    record_id: str
    record_kind: RecordKind
    script_id: str
    created_at: str
    description: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
```

Do not force existing `DerivationRecord` to inherit from this immediately if that creates migration risk. A compatibility adapter can treat derivations as base records when queried.

### DerivationRecord Additions

Extend `DerivationRecord` with optional fields:

```python
record_kind: RecordKind = RecordKind.DERIVATION
scope: str | None = None
claim_tier: ClaimTier | None = None
result_type: str | None = None
superseded_by: str | None = None
is_placeholder: bool = False
```

`record_kind` allows a script to record `SAMPLE_DERIVATION` or `DIAGNOSTIC_EXAMPLE` without using a separate dataclass.

`is_placeholder` should be computed or explicitly set. A derivation with `inputs=[]` and output like `Symbol("..._stated")` should be considered a placeholder unless the method explicitly declares it an inventory marker.

Backwards compatibility rule:

```text
Old derivation records without record_kind load as DERIVATION.
Old derivation records with empty inputs remain valid but may emit lint warnings.
```

### EvidenceRecord

Add:

```python
@dataclass(frozen=True)
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
```

`expression`, `expected`, `observed`, and `residual` should be serialized with the existing SymPy serialization helpers. They are optional because not every witness is a single expression.

Examples:

```text
Evidence: target_selected_parameter
  parameter = q
  target = gamma_like = 1
  source_records = [coefficient_choice_record, recovery_check_record]

Evidence: overlap_witness
  role = scalar_trace
  carriers = [B_s, zeta]
  residual = nonzero overlap expression
```

### ProofObligationRecord

Add:

```python
class ObligationStatus(str, Enum):
    OPEN = "open"
    SATISFIED = "satisfied"
    FAILED = "failed"
    SUPERSEDED = "superseded"
    ABANDONED = "abandoned"
    DEFERRED = "deferred"

@dataclass(frozen=True)
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
```

An obligation should never be represented only as prose. If a script says “unless X is derived,” record X here.

### ClaimRecord

Add:

```python
@dataclass(frozen=True)
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
```

`ClaimRecord` is the generic record for governance assessments and summary claims. Branch decisions should either use `BranchDecisionRecord` or a `ClaimRecord` with `claim_kind=BRANCH_DECISION`. The stronger option is a separate branch dataclass.

### BranchDecisionRecord

Add:

```python
@dataclass(frozen=True)
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
```

### RouteRecord

Add:

```python
@dataclass(frozen=True)
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
```

Named safe routes should be route records. If no minimal witness exists, the route should stay `CANDIDATE_ROUTE` or `HEURISTIC`.

## Archive Storage Layout

The current archive layout appears to use per-script namespaces with derivation JSON files and dependency metadata. Extend each script namespace as follows:

```text
.vacuumforge_archive/
  <script_id>/
    derivations/
      <derivation_id>.json
    evidence/
      <evidence_id>.json
    obligations/
      <obligation_id>.json
    claims/
      <claim_id>.json
    branches/
      <decision_id>.json
    routes/
      <route_id>.json
    dependencies.json
    run_metadata.json
    source_hash.json
```

Use separate directories instead of one mixed `records/` directory. This keeps CLI inspection simple and avoids breaking existing derivation tooling.

The existing `ScriptNamespace.__init__` should create these directories lazily or eagerly.

Recommended attributes:

```python
self.derivations_path = self.namespace_path / "derivations"
self.evidence_path = self.namespace_path / "evidence"
self.obligations_path = self.namespace_path / "obligations"
self.claims_path = self.namespace_path / "claims"
self.branches_path = self.namespace_path / "branches"
self.routes_path = self.namespace_path / "routes"
```

## Archive API Extensions

Extend `ScriptNamespace` with methods. Keep existing names unchanged.

### Evidence Methods

```python
def record_evidence(self, evidence: EvidenceRecord) -> EvidenceRecord: ...
def get_evidence(self, evidence_id: str) -> EvidenceRecord | None: ...
def list_evidence(self) -> list[EvidenceRecord]: ...
```

Convenience wrappers:

```python
def record_counterexample(...): ...
def record_overlap_witness(...): ...
def record_dependency_leak(...): ...
def record_target_selected_parameter(...): ...
```

Convenience wrappers should be thin. They should populate `EvidenceRecord` and call `record_evidence`.

### Proof Obligation Methods

```python
def record_obligation(self, obligation: ProofObligationRecord) -> ProofObligationRecord: ...
def get_obligation(self, obligation_id: str) -> ProofObligationRecord | None: ...
def update_obligation_status(self, obligation_id: str, status: ObligationStatus, *, by: str | None = None) -> ProofObligationRecord: ...
def list_obligations(self, status: ObligationStatus | None = None) -> list[ProofObligationRecord]: ...
```

Obligation updates should be immutable in spirit. Either overwrite the JSON record with updated status and append history metadata, or write event records. Simpler first version: overwrite plus `metadata["history"]` list.

### Claim Methods

```python
def record_claim(self, claim: ClaimRecord) -> ClaimRecord: ...
def get_claim(self, claim_id: str) -> ClaimRecord | None: ...
def list_claims(self, *, tier: ClaimTier | None = None, status: str | None = None) -> list[ClaimRecord]: ...
def validate_claim(self, claim: ClaimRecord) -> ClaimValidationResult: ...
```

`record_claim` should call `validate_claim` before writing. It should not necessarily reject unsupported claims, because exploratory scripts may need to record unsupported claims. Instead, it should downgrade or annotate them according to the rules below.

### Branch Methods

```python
def record_branch_decision(self, decision: BranchDecisionRecord) -> BranchDecisionRecord: ...
def get_branch_decision(self, decision_id: str) -> BranchDecisionRecord | None: ...
def list_branch_decisions(self, branch_id: str | None = None) -> list[BranchDecisionRecord]: ...
```

`record_branch_decision` should enforce Tier 3 evidence requirements.

### Route Methods

```python
def record_route(self, route: RouteRecord) -> RouteRecord: ...
def get_route(self, route_id: str) -> RouteRecord | None: ...
def list_routes(self, status: GovernanceStatus | None = None) -> list[RouteRecord]: ...
```

### Generic Query Methods

Add to `ProjectArchive`:

```python
def find_record(self, record_ref: str) -> ArchiveRecordBase | DerivationRecord | None: ...
def query_claims(self, *, status=None, tier=None, reason_code=None) -> list[ClaimRecord]: ...
def query_obligations(self, *, status=None) -> list[ProofObligationRecord]: ...
def query_evidence(self, *, evidence_type=None, supports=None, challenges=None) -> list[EvidenceRecord]: ...
def query_branch_decisions(self, *, status=None, branch_id=None) -> list[BranchDecisionRecord]: ...
```

`find_record` should accept either:

```text
<script_id>:<record_id>
```

or separate script/record arguments in an overload/helper.

## Serialization Updates

The current serialization code has `serialize_expr` and `deserialize_expr` using `sympy.srepr`, `sympy.latex`, and `sympy.sympify`. Extend it with helper functions:

```python
def serialize_optional_expr(expr: sympy.Basic | None) -> dict | None: ...
def deserialize_optional_expr(data: dict | None) -> sympy.Basic | None: ...
def serialize_enum(value: Enum | str | None) -> str | None: ...
def deserialize_enum(enum_cls, value, default=None): ...
def serialize_record_ref_list(refs: list[str]) -> list[str]: ...
```

Do not attempt to serialize arbitrary Python objects in metadata. Metadata must be JSON-safe. If a script needs symbolic content, use explicit symbolic fields.

Each record type should have `_to_json` and `_from_json` helpers in `archive/archive.py` or a new `archive/json_records.py`. To avoid bloating `archive.py`, create:

```text
src/vacuumforge/archive/json_records.py
```

with:

```python
def record_to_json(record): ...
def record_from_json(kind, data): ...
```

Existing `_record_to_json` and `_record_from_json` for derivations can delegate to this module after migration.

## Claim Validation Logic

Create `vacuumforge/governance/validation.py`.

### ClaimValidationResult

```python
@dataclass(frozen=True)
class ClaimValidationResult:
    claim_id: str
    original_status: str
    effective_status: str
    tier: ClaimTier
    supported: bool
    downgraded: bool
    messages: list[str] = field(default_factory=list)
    missing_evidence: list[str] = field(default_factory=list)
    missing_obligations: list[str] = field(default_factory=list)
    evidence_ids: list[str] = field(default_factory=list)
```

### Validation Rules

Implement:

```python
def validate_claim_support(claim: ClaimRecord, resolver: RecordResolver) -> ClaimValidationResult: ...
def validate_branch_decision(decision: BranchDecisionRecord, resolver: RecordResolver) -> ClaimValidationResult: ...
def validate_route(route: RouteRecord, resolver: RecordResolver) -> ClaimValidationResult: ...
```

`RecordResolver` can be a protocol implemented by `ScriptNamespace` or `ProjectArchive`:

```python
class RecordResolver(Protocol):
    def get_evidence_ref(self, ref: str) -> EvidenceRecord | None: ...
    def get_derivation_ref(self, ref: str) -> DerivationRecord | None: ...
    def get_obligation_ref(self, ref: str) -> ProofObligationRecord | None: ...
```

### Tier Rules

Tier 1:

```text
No evidence required.
If evidence is attached, preserve it.
Cannot support Tier 3 decisions downstream unless explicitly referenced as context only.
```

Tier 2:

```text
Requires reason_code or description.
Requires at least one provenance pointer: source_claim_ids, derivation_ids, obligation_ids, or evidence_ids.
If missing, effective_status becomes UNVERIFIED or HEURISTIC.
```

Tier 3 exclusion:

```text
Requires at least one active evidence_id or derivation_id.
If status is KILLED_BY_CONTRADICTION, evidence must include CONTRADICTION_RECORD or COUNTEREXAMPLE.
If status is FAILED_BY_WITNESS, evidence must include any witness type.
If status is REJECTED_ROUTE, evidence or a failed/superseded obligation is required.
If missing, effective_status becomes UNPROVEN_EXCLUSION.
```

Tier 3 licensing:

```text
Requires at least one derivation_id or evidence_id that supports the licensed claim.
If the only support is SAMPLE_DERIVATION, DIAGNOSTIC_EXAMPLE, or COMPATIBILITY_EXAMPLE, effective_status becomes CANDIDATE_ROUTE or SAMPLE_ONLY_SUPPORT warning.
```

### Downgrade Function

Implement a pure function:

```python
def downgrade_unsupported_status(status: GovernanceStatus, tier: ClaimTier, reason: str) -> GovernanceStatus:
    ...
```

Mapping:

```text
KILLED_BY_CONTRADICTION -> UNPROVEN_EXCLUSION
FAILED_BY_WITNESS -> UNPROVEN_EXCLUSION
REJECTED_ROUTE -> UNPROVEN_EXCLUSION
LICENSED_CLAIM -> CANDIDATE_ROUTE
FORBIDDEN-like policy claims -> OPEN_RISK or POLICY_RULE
DERIVED-like missing computation -> UNVERIFIED
```

If a script requests a strong status and the support is missing, record both requested and effective status. Reports should show both.

## Expected Output Dependency Verification

The current dependency verification appears to check existence and source invalidation. It also has `expected_output` support in the design docs but may not fully enforce it. Implement or strengthen it.

### DependencyDeclaration Additions

Extend `DependencyDeclaration`:

```python
expected_output: sympy.Basic | None = None
expected_status: str | None = None
expected_record_kind: RecordKind | None = None
allow_superseded: bool = False
```

### Verification Rules

`ScriptNamespace.verify_dependencies` should:

1. Detect cycles as it already does.
2. Load the upstream record.
3. Fail as `dependency_missing` if absent.
4. Fail or warn as `dependency_superseded` if the upstream record is superseded and `allow_superseded=False`.
5. Compare expected status when provided.
6. Compare expected record kind when provided.
7. Compare expected output when provided, using `vacuumforge.core.simplify.check_equal` or `is_equivalent`.
8. Report `dependency_changed` if expected output does not match.
9. Report `dependency_satisfied` only if all declared constraints pass.

### DependencyCheckResult Additions

Extend:

```python
actual_output: sympy.Basic | None = None
expected_output: sympy.Basic | None = None
actual_status: str | None = None
expected_status: str | None = None
actual_record_kind: str | None = None
expected_record_kind: str | None = None
residual: sympy.Basic | None = None
```

This lets downstream scripts say, “I depend on `P_T^2 = P_T`, not merely on `vector_projection_script_marker` existing.”

## Placeholder Derivation Detection

A major current gap is that scripts can perform symbolic work and record only a marker.

Add a function:

```python
def classify_derivation_record(record: DerivationRecord) -> DerivationRecordQuality: ...
```

Where:

```python
class DerivationRecordQuality(str, Enum):
    CONTENTFUL = "contentful"
    PLACEHOLDER = "placeholder"
    INVENTORY_MARKER = "inventory_marker"
    SAMPLE = "sample"
    UNKNOWN = "unknown"
```

Heuristics:

```text
inputs == [] and output is Symbol ending in _stated -> PLACEHOLDER
inputs == [] and method contains inventory -> INVENTORY_MARKER
record_kind == INVENTORY_MARKER -> INVENTORY_MARKER
record_kind == SAMPLE_DERIVATION -> SAMPLE
inputs nonempty and output non-placeholder -> CONTENTFUL
```

This classification should appear in archive CLI output and reports.

Do not reject placeholders globally. Inventory scripts may need them. But scripts that compute real algebra should be linted if they only record placeholders.

## Governance-Aware Script Output Helper

Create `vacuumforge/governance/output.py`.

Current scripts hand-roll `status_line(label, ok: bool, detail="")`, often limiting output to PASS/WARN. Replace this with a shared helper.

### StatusMark

```python
class StatusMark(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARN = "WARN"
    INFO = "INFO"
    MEMO = "MEMO"
    OPEN = "OPEN"
    DEFER = "DEFER"
    EVIDENCE = "EVIDENCE"
    OBLIGATION = "OBLIGATION"
```

### OutputEvent

```python
@dataclass(frozen=True)
class OutputEvent:
    label: str
    mark: StatusMark
    detail: str = ""
    claim_id: str | None = None
    record_ref: str | None = None
    tier: ClaimTier | None = None
    kind: RecordKind | None = None
```

### Helper Function

```python
def status_line(label: str, mark: StatusMark | str, detail: str = "", *, claim_id=None, record_ref=None, tier=None, kind=None) -> OutputEvent:
    event = OutputEvent(...)
    print(format_event(event))
    return event
```

The helper must not accept `ok: bool` as the primary interface. For compatibility, provide:

```python
def pass_warn_line(label: str, ok: bool, detail: str = "") -> OutputEvent:
    warnings.warn("pass_warn_line cannot emit FAIL; use status_line", DeprecationWarning)
    return status_line(label, StatusMark.PASS if ok else StatusMark.WARN, detail)
```

Scripts should migrate away from `pass_warn_line`.

### Derived/Governance/Obligation Blocks

Add a simple block helper:

```python
class ScriptOutput:
    def derived_results(self): ...
    def governance_assessments(self): ...
    def unresolved_obligations(self): ...
```

Usage:

```python
out = ScriptOutput(script_id)
with out.derived_results():
    status_line("projection idempotent", "PASS", ...)
with out.governance_assessments():
    status_line("route deferred", "DEFER", ...)
with out.unresolved_obligations():
    status_line("derive q-origin", "OPEN", ...)
```

This is not required for the archive to work, but it makes output regular enough for humans and linting.

## Summary Generation And Claim-Strength Upgrade Detection

Create `vacuumforge/governance/summaries.py`.

### Summary Builder

```python
@dataclass
class SummarySpec:
    script_id: str
    upstream_scripts: list[str]
    include_derivations: bool = True
    include_claims: bool = True
    include_obligations: bool = True
    include_branch_decisions: bool = True
```

```python
class GovernanceSummaryBuilder:
    def __init__(self, archive: ProjectArchive): ...
    def build(self, spec: SummarySpec) -> GovernanceSummary: ...
```

`GovernanceSummary` should contain:

```text
derived_results
sample_results
counterexamples
governance_claims
branch_decisions
open_obligations
failed_obligations
superseded_records
unsupported_claims
claim_strength_upgrades
```

### Claim-Strength Upgrade Check

A group summary should not upgrade upstream claims without new evidence.

Implement:

```python
def check_claim_strength_upgrade(summary_claim: ClaimRecord, upstream_claims: list[ClaimRecord]) -> UpgradeCheckResult: ...
```

Define a strength ordering:

```text
memo/open question < heuristic < candidate_route < provisional_convention < licensed_claim/derived
open_risk < unproven_exclusion < failed_by_witness < killed_by_contradiction
unresolved_obligation < satisfied_obligation
sample_derivation < derivation
```

If a summary claim is stronger than every upstream source claim it references and has no new evidence/derivation, flag:

```text
claim_strength_upgrade
```

The archive should record this as an evidence or warning record, not silently pass it.

### Handoff Imports

Add:

```python
@dataclass(frozen=True)
class HandoffImportRecord:
    import_id: str
    script_id: str
    imported_record_refs: list[str]
    import_status: str
    created_at: str
    notes: list[str] = field(default_factory=list)
```

A group-ending summary should emit handoff imports for what the next group may assume.

If an imported record is a sample, open obligation, or unsupported claim, the handoff should report it as such.

## Integration With TheoryContext

The current `TheoryContext` has:

```python
self.ledger
self.dependencies
self.theorems
self.scope
```

Add a governance manager:

```python
from vacuumforge.governance.manager import GovernanceManager

self.governance = GovernanceManager(self)
```

Create:

```text
src/vacuumforge/governance/manager.py
```

With:

```python
class GovernanceManager:
    def __init__(self, ctx: TheoryContext): ...
    def claim(...): ...
    def evidence(...): ...
    def obligation(...): ...
    def branch_decision(...): ...
    def route(...): ...
    def validate_claim(...): ...
```

This manager is for in-session work. It should not replace `ProjectArchive`. Scripts that use a persistent archive should call `ScriptNamespace` methods. The manager can help notebooks or smaller examples produce governance records in memory.

Potential future bridge:

```python
ctx.governance.export_to_archive(ns)
```

Do not implement that bridge until a clear use case appears.

## Integration With Existing Ledger

The current `TheoryLedger` supports entries like definitions, postulates, assumptions, targets, derived results, and open questions. Do not overload it with all governance records.

Recommended use:

```text
Ledger: human-facing theory notes inside a TheoryContext.
Archive: persistent cross-script record store.
Governance: structured claim/evidence/obligation layer.
```

A ledger entry may reference an archive record, but should not be the source of truth for branch decisions.

Add optional fields to `LedgerEntry` only if needed:

```python
archive_ref: str | None = None
claim_tier: ClaimTier | None = None
record_kind: RecordKind | None = None
```

## Integration With Theorem Candidates

The current `TheoremCandidate` supports supporting models and counterexamples. It can remain lightweight.

Add optional references:

```python
supporting_record_refs: list[str]
counterexample_record_refs: list[str]
obligation_refs: list[str]
```

`add_support` and `add_counterexample` should accept either strings or archive refs.

Do not make theorem candidates enforce governance by themselves. They are useful working objects, but archive records should remain the persistent source of truth.

## `vf-lint` Technical Design

The existing codebase does not show a `vf-lint` package. Add it as a standalone tool under `tools/vf_lint/`.

### Goals

`vf-lint` catches syntactic and structural patterns that indicate validation theater or governance theater.

It does not prove script semantics. It catches cases where the script shape is already suspicious.

### CLI

```bash
vf-lint path/to/script.py
vf-lint scripts_v3/**/*.py
vf-lint --format=json path/to/script.py
vf-lint --quiet path/to/script.py
```

Exit codes:

```text
0 = OK or INFO only
1 = WARN present
2 = FAIL present
```

### Analyzer Phases

1. Parse with `ast`.
2. Collect imports.
3. Collect function definitions.
4. Collect calls and dataclass constructor sites.
5. Detect verdict-emitting sites.
6. Trace verdicts back to computation where possible.
7. Detect governance language and strong status strings.
8. Detect archive record calls.
9. Detect symbolic computation calls.
10. Apply rules.

### Existing Validation-Theater Rules

From prior design:

```text
print("[PASS] ...") outside computation -> WARN
status_line(..., True, ...) -> WARN
dataclass status="PASS" or "DERIVED" without provenance -> FAIL or WARN
missing sympy/vacuumforge imports in verdict script -> INFO/WARN
```

### New Governance-Theater Rules

Add `tools/vf_lint/governance_rules.py`.

Rules:

```text
branch_kill_without_evidence
forbidden_without_evidence
rejected_without_evidence
licensed_without_derivation_or_evidence
hardcoded_derivation_status_without_provenance
hardcoded_governance_status_without_claim_tier
status_field_without_evidence_columns
summary_claim_upgrade_language_without_archive_query
optional_branch_latent_language
not_insertable_reported_as_killed
```

Detection patterns:

Strong words in string literals:

```text
"BRANCH_KILLED"
"KILLED"
"FORBIDDEN"
"REJECTED"
"NO_VIABLE_ROUTE"
"LICENSED"
"DERIVED"
"SATISFIED_REDUCED"
```

Branch-kill prose:

```text
"kill the branch"
"branch is killed"
"ruled out"
"forbidden"
"no viable route"
```

Evidence calls that satisfy a rule:

```text
record_evidence(...)
record_counterexample(...)
record_branch_decision(... evidence_ids=[...])
record_claim(... evidence_ids=[...])
record_overlap_witness(...)
record_dependency_leak(...)
```

If a file contains strong words but no evidence-recording call, emit WARN or FAIL depending on context.

### Archive Marker Rules

Add `tools/vf_lint/archive_rules.py`.

Rules:

```text
placeholder_derivation_after_symbolic_work
record_derivation_empty_inputs_after_simplify
record_derivation_placeholder_symbol_output
expected_output_missing_for_dependency_on_math_result
superseded_pair_without_marker
```

Detect symbolic work calls:

```text
sp.simplify
sympy.simplify
is_zero
check_equal
sp.solve
sympy.solve
sp.diff
sympy.diff
euler_lagrange_1d
check_quadratic_positivity
ConcreteMetricCheck
check_concrete_metric
CoordinateChange
StructureSearchEngine.analyze
```

If the script uses symbolic work and only calls:

```python
record_derivation(inputs=[], output=sp.Symbol("..._stated"), ...)
```

emit:

```text
WARN placeholder derivation after symbolic work
```

If method contains `inventory` or record kind is `INVENTORY_MARKER`, reduce severity to INFO.

### Dataclass Provenance Rule

Detect dataclass definitions with fields named:

```text
status
verdict
classification
claim_status
```

Then detect instantiations where those fields are string literals like:

```text
DERIVED
SATISFIED_REDUCED
FORBIDDEN
REJECTED
BRANCH_KILLED
CLOSED
LICENSED
```

Require one of:

```text
evidence_script
evidence_derivation
evidence_ids
derivation_ids
claim_tier
claim_kind
record_kind
```

If missing, emit WARN or FAIL.

Suggested severity:

```text
DERIVED/FORBIDDEN/BRANCH_KILLED without provenance -> FAIL
SATISFIED_REDUCED/PARTIAL/MISSING without provenance -> WARN
HEURISTIC/OPEN_RISK without provenance -> OK or INFO
```

### Boolean Status Helper Rule

Detect functions like:

```python
def status_line(label: str, ok: bool, detail: str = ""):
    mark = "PASS" if ok else "WARN"
```

Emit WARN:

```text
boolean status_line cannot emit FAIL; use governance.output.status_line
```

This rule is important for early scripts where definitive computed failures appear as WARN.

### Stale Header Rule

Detect:

```text
# Suggested location:
```

Emit INFO:

```text
replace Suggested location with Group metadata
```

This is low severity but useful for cleanup.

## Runner And Result File Checks

If `run_scripts_v3.py` is maintained in the repository, update it.

### Script Failure Sentinel

When a script exits nonzero, the result file should start with:

```text
[SCRIPT_FAILED]
exit_code=<code>
```

Then include stdout/stderr.

The console summary should show `[FAIL]` for nonzero exits.

### Archive Marker Cross-Check

After running a script, optionally check whether expected archive markers were written.

This requires either:

```text
script metadata declares expected archive writes
```

or a loose check:

```text
if script imports prepare_archive or ProjectArchive but no records changed, warn
```

Do not make the loose check fatal.

### Result Linting

Add a result-file scanner:

```text
result file contains [stderr] or traceback -> WARN/FAIL
result file contains [SCRIPT_FAILED] -> FAIL
result file exists but archive marker absent -> WARN if archive expected
```

## `order.txt` Coverage Checker

Create a tool:

```bash
vf-order-check theory_v3/development/field_equation_candidates/NN_group/
```

Behavior:

1. Read `order.txt`.
2. List `*.py` files in the group.
3. Ensure every `.py` file appears exactly once unless explicitly ignored.
4. Ensure every order entry exists.
5. Warn if summary scripts are not last unless marked otherwise.
6. Warn if versioned scripts both appear without `SUPERSEDED_BY` metadata.
7. Optionally check dependency declarations against prior scripts.

Script metadata comments:

```python
# Group: 09_vacuum_identity_and_source_coupling
# Script type: DERIVATION
# SUPERSEDED_BY: candidate_parent_identity_template_v2.py
```

The checker should parse these comments with regex, not Python import execution.

## Script Metadata Standard

Add a tiny metadata parser in `vacuumforge/governance/lint_models.py` or the lint tool.

Recommended header fields:

```text
# Group: 11_field_equation_closure
# Script type: DERIVATION | SAMPLE | INVENTORY | AUDIT | REQUIREMENTS | SUMMARY | MEMO | SIEVE
# Canonical: true | false
# Superseded by: <script_id>
# Archive script id: <script_id>
```

Only `Group` and `Script type` are required for new scripts.

The archive can store this as `SCRIPT_METADATA` records via:

```python
ns.write_run_metadata(...)
```

or a new:

```python
ns.record_script_metadata(...)
```

## Archive CLI Extensions

The current archive CLI supports list, verify, invalidate, and doctor. Extend it.

### List

```bash
vf archive list --root .vacuumforge_archive --script SCRIPT_ID
```

Should show counts for:

```text
derivations
evidence
obligations
claims
branches
routes
dependencies
```

For derivations, show quality:

```text
contentful
placeholder
inventory_marker
sample
```

### Verify

`vf archive verify` should verify dependencies and claim support.

New options:

```bash
vf archive verify --claims
vf archive verify --obligations
vf archive verify --branches
vf archive verify --strict
```

Strict mode should exit nonzero for unsupported Tier 3 claims.

### Doctor

Extend doctor checks:

```text
invalid JSON
missing source hashes
cycle detection
claims referencing missing evidence
branch decisions without evidence
open obligations marked satisfied without satisfying derivation
summary claims stronger than upstream support
placeholder derivations in scripts with run metadata indicating derivation script type
superseded records still used by dependencies
```

### Query

Add:

```bash
vf archive query obligations --status open
vf archive query claims --tier exclusion
vf archive query evidence --type overlap_witness
vf archive query branches --status rejected_route
```

This is useful for summary scripts and human review.

## Migration Plan

### Phase 1: Schema And Archive Compatibility

Implement:

```text
RecordKind
ClaimTier
GovernanceStatus
EvidenceType
ReasonCode
EvidenceRecord
ProofObligationRecord
ClaimRecord
BranchDecisionRecord
RouteRecord
serialization helpers
new archive directories
record/get/list methods
```

Completion criteria:

```text
Existing archive tests still pass.
Old derivation records load.
New record types can round-trip to JSON.
Archive list shows new record counts.
```

### Phase 2: Claim Validation And Downgrade Rules

Implement:

```text
ClaimValidationResult
validate_claim_support
validate_branch_decision
validate_route
downgrade_unsupported_status
```

Completion criteria:

```text
Tier 1 claim records without evidence pass as informational.
Tier 2 claims without provenance downgrade to HEURISTIC/UNVERIFIED.
Tier 3 branch kill without evidence downgrades to UNPROVEN_EXCLUSION.
Tier 3 branch kill with counterexample remains KILLED_BY_CONTRADICTION.
Licensed claim with only sample support downgrades to CANDIDATE_ROUTE.
```

### Phase 3: Expected Output Dependencies

Implement:

```text
expected_output
expected_status
expected_record_kind
allow_superseded
residual reporting
```

Completion criteria:

```text
Dependency satisfied when expected output matches.
Dependency changed when expected output differs.
Dependency superseded when upstream is superseded and not allowed.
Existing dependency declarations without expected_output still work.
```

### Phase 4: Script Output Helpers

Implement:

```text
governance.output.status_line
ScriptOutput blocks
Deprecation helper for pass/warn boolean output
```

Completion criteria:

```text
New helper can emit PASS/WARN/FAIL/INFO/OPEN/DEFER.
Boolean helper emits deprecation warning.
Sample script uses derived/governance/obligation blocks.
```

### Phase 5: Archive CLI Expansion

Implement:

```text
list counts for new record types
verify --claims
verify --branches
verify --obligations
doctor governance checks
query commands
```

Completion criteria:

```text
CLI reports unsupported Tier 3 claims.
CLI reports open obligations.
CLI reports branch decisions and evidence links.
Doctor catches missing evidence references.
```

### Phase 6: vf-lint Governance Rules

Implement standalone lint tool or extend existing planned tool:

```text
AST verdict detection
hardcoded dataclass status rules
branch kill without evidence rules
placeholder derivation rules
boolean status_line rule
stale header rule
```

Completion criteria:

```text
Known good script passes.
Hardcoded BRANCH_KILLED dataclass without evidence fails.
Placeholder derivation after sp.simplify warns.
Boolean status_line warns.
Strong branch-kill prose without record_evidence warns/fails.
```

### Phase 7: Runner And Order Checks

Implement:

```text
SCRIPT_FAILED sentinel
console failure visibility
result-file failure scan
order.txt coverage check
superseded version check
```

Completion criteria:

```text
Failed script result begins with [SCRIPT_FAILED].
order checker catches missing and duplicate entries.
Versioned scripts without supersession metadata warn.
```

### Phase 8: Retrofit High-Value Scripts

Do not retrofit every script at once. Start with groups where the governance and marker problems are visible.

Suggested order:

```text
Group 09 vector sector scripts with real symbolic checks.
Group 10 kappa trace response scripts with real symbolic checks.
Group 11 field-equation closure scripts.
Group 08 covariant parent audit scripts.
Groups 01-07 foundation scripts only after the new pattern stabilizes.
```

For each script:

```text
replace placeholder derivation markers with actual inputs/outputs;
add script metadata header;
replace boolean status_line with shared helper;
record proof obligations where prose says “unless X is derived”;
record branch decisions with reason codes and evidence;
tag samples as SAMPLE_DERIVATION or COMPATIBILITY_EXAMPLE;
add expected_output to downstream dependencies where appropriate.
```

## Testing Strategy

### Unit Tests

Add tests for:

```text
record serialization round-trip for every new record type;
claim validation downgrade rules;
branch decision evidence requirements;
proof obligation status transitions;
expected_output dependency matching;
placeholder derivation classification;
archive query filters;
summary upgrade detection;
output helper formatting.
```

### Integration Tests

Create small fixture scripts in a test directory:

```text
good_derivation_script.py
placeholder_marker_script.py
unsupported_branch_kill_script.py
supported_branch_kill_script.py
open_obligation_script.py
summary_upgrade_script.py
sample_only_license_script.py
```

Each fixture should run against a temporary archive.

Expected results:

```text
good_derivation_script: contentful derivation, no warnings
placeholder_marker_script: placeholder warning
unsupported_branch_kill_script: downgraded to UNPROVEN_EXCLUSION
supported_branch_kill_script: KILLED_BY_CONTRADICTION accepted
open_obligation_script: obligation listed as OPEN
summary_upgrade_script: upgrade warning
sample_only_license_script: LICENSED_CLAIM downgraded to CANDIDATE_ROUTE
```

### CLI Tests

Use `pytest` with `tmp_path`.

Test:

```text
vf archive list
vf archive verify --claims
vf archive verify --branches
vf archive query obligations --status open
vf archive doctor
vf-lint fixture.py
vf-order-check fixture_group/
```

### Backward Compatibility Tests

Use old-style derivation records.

Ensure:

```text
old derivation JSON loads;
old dependency declarations verify;
old archive list works;
old scripts do not fail merely because governance records are absent;
missing governance metadata produces warnings, not hard failures, unless strict mode is requested.
```

## Backward Compatibility And Strictness Policy

Default mode should be permissive but explicit.

```text
Unsupported strong claim -> record with downgrade/warning.
Strict mode -> nonzero exit or exception for unsupported Tier 3 claim.
Old derivation record -> accepted.
Old placeholder marker -> accepted with warning.
Old boolean status_line -> lint warning, not runtime failure.
```

Strictness should be controlled by:

```text
archive CLI --strict
vf-lint severity configuration
possibly environment variable VF_STRICT_GOVERNANCE=1
```

Do not make the first migration pass block all old scripts.

## Example Workflows

### Recording A Real Symbolic Derivation

```python
residual = sp.simplify(P_T * P_T - P_T)
assert is_zero(residual)

ns.record_derivation(
    derivation_id="transverse_projector_idempotence",
    inputs=[P_T],
    output=residual,
    method="symbolic_matrix_simplification",
    status=Status.DERIVED,
    record_kind=RecordKind.DERIVATION,
)
```

This is contentful because it records the actual input and output.

### Recording A Sample Derivation

```python
ns.record_derivation(
    derivation_id="compact_support_c2_profile_zero_flux_sample",
    inputs=[kappa_profile, boundary_radius],
    output=boundary_flux,
    method="symbolic_boundary_check",
    status=Status.DERIVED,
    record_kind=RecordKind.SAMPLE_DERIVATION,
    scope="toy_profile",
)
```

Reports should not treat this as a theorem-level mechanism derivation.

### Recording A Proof Obligation

```python
ns.record_obligation(ProofObligationRecord(
    obligation_id="derive_boundary_neutrality_theorem",
    script_id=SCRIPT_ID,
    title="Derive boundary neutrality theorem",
    status=ObligationStatus.OPEN,
    required_by=["kappa_boundary_safety_route"],
    description="Needed before compact-support boundary smoothing can be licensed as a mechanism.",
))
```

### Recording An Unsupported Branch Kill

If a script tries:

```python
ns.record_branch_decision(BranchDecisionRecord(
    decision_id="kill_residual_trace_route",
    branch_id="residual_trace_route",
    status=GovernanceStatus.KILLED_BY_CONTRADICTION,
    tier=ClaimTier.EXCLUSION,
    evidence_ids=[],
))
```

The system should either downgrade or return a validation result:

```text
requested_status = KILLED_BY_CONTRADICTION
effective_status = UNPROVEN_EXCLUSION
missing_evidence = [counterexample or contradiction_record required]
```

### Recording A Supported Branch Kill

```python
ev = ns.record_evidence(EvidenceRecord(
    evidence_id="residual_trace_exports_scalar_charge",
    evidence_type=EvidenceType.EXTERIOR_SCALAR_CHARGE_WITNESS,
    script_id=SCRIPT_ID,
    observed=scalar_charge_expr,
    expected=sp.Integer(0),
    residual=sp.simplify(scalar_charge_expr),
    reason_code=ReasonCode.EXTERIOR_SCALAR_CHARGE,
))

ns.record_branch_decision(BranchDecisionRecord(
    decision_id="kill_residual_trace_route",
    branch_id="residual_trace_route",
    status=GovernanceStatus.FAILED_BY_WITNESS,
    tier=ClaimTier.EXCLUSION,
    reason_code=ReasonCode.EXTERIOR_SCALAR_CHARGE,
    evidence_ids=[ev.evidence_id],
))
```

This may remain a strong exclusion if the evidence record is active and not superseded.

### Recording A Candidate Route Without Witness

```python
ns.record_route(RouteRecord(
    route_id="projected_trace_separation_route",
    name="Projected trace separation",
    status=GovernanceStatus.CANDIDATE_ROUTE,
    tier=ClaimTier.INFORMATIONAL,
    description="Possible route; no witness yet.",
))
```

This is allowed. It must not be reported as licensed.

## Known Limitations

This design cannot prove that a script uses its declared dependencies correctly. It can only verify that the declared dependencies exist, match expected outputs, and are not stale or unsupported.

This design cannot tell whether a reason code is scientifically adequate. It can only require that reason codes and evidence exist for strong claims.

This design cannot prevent a bad symbolic computation from being recorded as evidence. That remains the job of the algebra validators, tests, and review.

This design cannot automatically classify all prose. Linting can catch common governance-theater patterns, but scripts can still evade static checks. The archive API should therefore make the disciplined path easier than the undisciplined path.

This design intentionally allows memo and sieve scripts. The goal is not to ban exploratory judgment. The goal is to prevent exploratory judgment from masquerading as derivation or exclusion.

## Final Implementation Principle

Do not make the cave look cleaner by hiding the bones.

The next VacuumForge iteration should expose what each script actually did:

```text
computed result;
sample result;
counterexample;
policy rule;
open risk;
unresolved obligation;
branch decision;
summary interpretation;
placeholder marker.
```

Once those are separate, downstream scripts can depend on the right things and refuse the wrong ones. That is the purpose of this development phase.
