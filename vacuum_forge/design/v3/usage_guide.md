# VacuumForge v3 Script Update Usage Guide

## Purpose

This guide tells AI agents how to update scripts under:

```text
vacuum_forge/src/scripts_v3/
```

for the v3 governance-validation features.

The goal is not to make scripts sound more formal. The goal is to make every important script output machine-visible as the right kind of record:

```text
derivation
sample derivation
diagnostic example
compatibility example
inventory marker
evidence object
proof obligation
governance claim
branch decision
route record
handoff import
summary claim
```

When updating scripts, preserve the physics intent of the script. Do not strengthen claims, invent derivations, or convert prose requirements into theorem claims. If a script only has a warning, route idea, theorem target, or unresolved prerequisite, record that honestly.

## Core Rule

Do not use one placeholder `record_derivation(..._marker)` to stand for a whole script if the script contains more specific results.

Use the narrowest truthful record type:

| Script content | Archive record to use |
| --- | --- |
| SymPy identity, residual, variation, metric check, algebraic equality | `record_derivation(..., record_kind=RecordKind.DERIVATION)` |
| Toy profile, illustrative parameter choice, non-general numerical/symbolic sample | `record_derivation(..., record_kind=RecordKind.SAMPLE_DERIVATION)` |
| Diagnostic-only computation | `record_derivation(..., record_kind=RecordKind.DIAGNOSTIC_EXAMPLE)` |
| Compatibility check that does not derive mechanism | `record_derivation(..., record_kind=RecordKind.COMPATIBILITY_EXAMPLE)` |
| Inventory/audit table with no computation | `ClaimRecord`, `ProofObligationRecord`, `RouteRecord`, `BranchDecisionRecord`, or `HandoffImportRecord` |
| "Requires X", "unless X is derived", "missing theorem", "not yet closed" | `ProofObligationRecord` |
| Counterexample, contradiction, overlap witness, failed boundary check | `EvidenceRecord` |
| "This branch is killed/rejected/deferred" | `BranchDecisionRecord`, backed by evidence or obligations |
| "This route is candidate/provisional/licensed" | `RouteRecord` or `ClaimRecord` |
| Group summary imports assumptions into next group | `HandoffImportRecord` |

## Standard Imports

Use explicit governance imports in migrated scripts:

```python
from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    EvidenceRecord,
    EvidenceType,
    GovernanceStatus,
    HandoffImportRecord,
    ObligationStatus,
    ProofObligationRecord,
    ReasonCode,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)
```

Only import what the script uses.

## Script Metadata Header

New or migrated scripts should carry metadata comments near the top of the file.

Use this instead of stale `# Suggested location:` comments:

```python
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   DERIVATION
```

Common script types:

```text
DERIVATION
SAMPLE
DIAGNOSTIC
INVENTORY
AUDIT
SUMMARY
MEMO
SIEVE
REQUIREMENTS
```

Guidance:

- A script that computes identities or residuals is usually `DERIVATION`.
- A script that lists route statuses is usually `AUDIT` or `INVENTORY`.
- A group-ending script with handoff rows is usually `SUMMARY`.
- An audit script should include a controlled-failure section such as `case_6_good_failure()`.
- Do not label an inventory or summary as a derivation just because it records an archive marker.

## Output Discipline

Replace per-script `status_line()` helpers with `ScriptOutput`.

Old pattern:

```python
def status_line(label: str, status: str, detail: str = "") -> None:
    ...

status_line("boundary neutrality", "MISSING")
```

New pattern:

```python
out = ScriptOutput()

with out.derived_results():
    out.line("curl-curl transverse identity residual", StatusMark.PASS, "residual simplifies to 0")

with out.governance_assessments():
    out.line("boundary neutrality theorem", StatusMark.DEFER, "required before insertion")

with out.unresolved_obligations():
    out.line("derive boundary neutrality", StatusMark.OBLIGATION, "open proof obligation recorded")
```

Use `StatusMark.FAIL` for real failures. Do not collapse failures into `WARN`.

Recommended block mapping:

| Output block | Use for |
| --- | --- |
| `derived_results()` | computed derivations and residual checks |
| `sample_results()` | toy examples and sample-only support |
| `counterexamples()` | witnesses, contradictions, failed checks |
| `governance_assessments()` | route status, policy rules, branch decisions |
| `unresolved_obligations()` | missing theorem/source law/coefficient/prerequisite |

## Recording Contentful Derivations

If a script computes a real expression, archive the expression.

Example:

```python
residual = sp.simplify(P_T * P_T - P_T)

ns.record_derivation(
    derivation_id="transverse_projector_idempotence_residual",
    inputs=[P_T],
    output=residual,
    method="simplify(P_T*P_T - P_T)",
    status=Status.DERIVED,
    record_kind=RecordKind.DERIVATION,
    result_type="identity_residual",
)
```

Do not replace this with:

```python
ns.record_derivation(
    derivation_id="projector_script_marker",
    inputs=[],
    output=sp.Symbol("projector_identities_stated"),
    method="projector_inventory",
    status=Status.DERIVED,
)
```

That marker may be acceptable only for a pure inventory script, and then it should usually be:

```python
record_kind=RecordKind.INVENTORY_MARKER
is_placeholder=True
```

## Recording Samples And Diagnostics

Toy models and selected examples are useful, but they must not masquerade as general derivations.

Use `SAMPLE_DERIVATION` when the script evaluates a chosen profile, parameter value, ansatz, or special case:

```python
ns.record_derivation(
    derivation_id="constant_weight_joint_minimum_sample",
    inputs=[eq],
    output=sp.simplify(eq.lhs),
    method="constant-weight toy Euler-Lagrange reduction",
    status=Status.DERIVED,
    record_kind=RecordKind.SAMPLE_DERIVATION,
    scope="constant weights only",
)
```

Use `DIAGNOSTIC_EXAMPLE` when the output is a test or measurement definition rather than a mechanism derivation:

```python
ns.record_derivation(
    derivation_id="near_boundary_deviation_diagnostic",
    inputs=[f_joint, f_reference],
    output=sp.simplify(f_joint - f_reference),
    method="define diagnostic delta = f_joint - f_reference",
    status=Status.DERIVED,
    record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
)
```

Use `COMPATIBILITY_EXAMPLE` when a result shows that a construction is compatible with a target but does not derive the construction:

```python
ns.record_derivation(
    derivation_id="reciprocal_metric_compatibility_check",
    inputs=[A_value, B_value],
    output=sp.simplify(A_value * B_value),
    method="ConcreteMetricCheck reciprocal_scaling",
    status=Status.DERIVED,
    record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
)
```

## Recording Proof Obligations

Any prose of this shape must become a proof obligation:

```text
requires X
unless X is derived
missing X
X remains theorem target
cannot proceed until X
not insertable until X
coefficient origin missing
boundary neutrality not derived
parent identity missing
```

Example:

```python
obligation = ProofObligationRecord(
    obligation_id="derive_boundary_neutrality_theorem",
    script_id=SCRIPT_ID,
    title="Derive boundary neutrality theorem",
    status=ObligationStatus.OPEN,
    required_by=["B_s_insertion_route"],
    description=(
        "Show that the insertion creates no exterior scalar charge, "
        "far-zone flux, shell source, boundary repair, or independent M_ext shift."
    ),
)
ns.record_obligation(obligation)
```

When later satisfied:

```python
ns.update_obligation_status(
    "derive_boundary_neutrality_theorem",
    ObligationStatus.SATISFIED,
    by="script_id:derivation_id",
)
```

Do not mark an obligation satisfied from prose, memo records, or summary restatement.

## Recording Evidence

Use evidence for concrete witnesses and checks.

Example counterexample or failed check:

```python
evidence = EvidenceRecord(
    evidence_id="exterior_scalar_charge_witness",
    script_id=SCRIPT_ID,
    evidence_type=EvidenceType.EXTERIOR_SCALAR_CHARGE_WITNESS,
    challenges=["B_s_boundary_safe_route"],
    reason_code=ReasonCode.EXTERIOR_SCALAR_CHARGE,
    expression=scalar_charge_expr,
    expected=sp.Integer(0),
    observed=observed_charge,
    residual=sp.simplify(observed_charge),
    description="The proposed insertion leaves a nonzero exterior scalar charge.",
)
ns.record_evidence(evidence)
```

Evidence can support or challenge claims:

```python
EvidenceRecord(
    evidence_id="overlap_residual_nonzero",
    script_id=SCRIPT_ID,
    evidence_type=EvidenceType.OVERLAP_WITNESS,
    supports=["kill_double_counted_trace_branch"],
    challenges=["neutral_residual_metric_trace_route"],
)
```

## Recording Governance Claims

Use `ClaimRecord` for statements that guide interpretation but are not ordinary derivations.

Example policy rule:

```python
claim = ClaimRecord(
    claim_id="recovery_targets_downstream_only",
    script_id=SCRIPT_ID,
    claim_kind=RecordKind.GOVERNANCE_CLAIM,
    tier=ClaimTier.CONSTRAINED,
    status=GovernanceStatus.POLICY_RULE,
    statement=(
        "Gamma-like behavior, AB behavior, and Schwarzschild recovery are downstream tests, "
        "not construction rules for B_s/F_zeta insertion."
    ),
    reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
    evidence_ids=["recovery_precedes_origin_check"],
)
ns.record_claim(claim)
```

Example summary claim:

```python
summary_claim = ClaimRecord(
    claim_id="group_16_insertion_not_licensed",
    script_id=SCRIPT_ID,
    claim_kind=RecordKind.SUMMARY_CLAIM,
    tier=ClaimTier.CONSTRAINED,
    status=GovernanceStatus.NOT_INSERTABLE_YET,
    statement="Group 16 does not license B_s/F_zeta insertion into the metric sector.",
    obligation_ids=["derive_boundary_neutrality_theorem", "derive_no_overlap_operator"],
    source_claim_ids=["B_s_boundary_safety_required", "O_operator_unresolved"],
)
ns.record_claim(summary_claim)
```

Claim-strength rule:

- `HEURISTIC`, `OPEN_RISK`, and `UNVERIFIED` are weak.
- `CANDIDATE_ROUTE` is stronger than heuristic.
- `PROVISIONAL_CONVENTION` means usable as a visible convention, not a theorem.
- `LICENSED_CLAIM` requires strong support.
- A summary must not upgrade an upstream claim without new evidence or derivation.

If support is missing, archive validation may downgrade the claim.

## Recording Branch Decisions

Use `BranchDecisionRecord` when a branch is deferred, rejected, or killed.

A branch kill needs evidence. A missing theorem usually means defer, not kill.

Good deferred branch:

```python
decision = BranchDecisionRecord(
    decision_id="defer_B_s_insertion",
    script_id=SCRIPT_ID,
    branch_id="B_s_metric_insertion",
    status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
    tier=ClaimTier.CONSTRAINED,
    reason_code=ReasonCode.MISSING_BOUNDARY_NEUTRALITY_THEOREM,
    obligation_ids=["derive_boundary_neutrality_theorem", "derive_no_overlap_operator"],
    description="The insertion branch remains open but cannot be licensed yet.",
)
ns.record_branch_decision(decision)
```

Good killed branch:

```python
decision = BranchDecisionRecord(
    decision_id="kill_recovery_tuned_B_s_branch",
    script_id=SCRIPT_ID,
    branch_id="recovery_tuned_B_s",
    status=GovernanceStatus.KILLED_BY_CONTRADICTION,
    tier=ClaimTier.EXCLUSION,
    reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
    evidence_ids=["gamma_coefficient_fit_witness"],
    description="The branch chooses its coefficient from the recovery target.",
)
ns.record_branch_decision(decision)
```

Bad pattern:

```python
RecoveryAuditEntry(status="BRANCH_KILLED", missing="boundary theorem")
```

That is not a valid branch kill. Missing support should usually be an open obligation or deferred branch.

## Recording Routes

Use `RouteRecord` for candidate, provisional, rejected, or licensed routes.

```python
route = RouteRecord(
    route_id="compact_support_zero_flux_boundary_route",
    script_id=SCRIPT_ID,
    name="Compact support with structural zero-flux boundary",
    status=GovernanceStatus.CANDIDATE_ROUTE,
    tier=ClaimTier.CONSTRAINED,
    required_obligations=["derive_boundary_neutrality_theorem"],
    activation_conditions=[
        "support is compact",
        "boundary flux vanishes structurally",
        "no exterior scalar charge appears",
    ],
)
ns.record_route(route)
```

Use `PROVISIONAL_CONVENTION` when a route may be used as an explicit convention while its theorem remains open:

```python
RouteRecord(
    route_id="residual_kill_nonmetric_convention",
    script_id=SCRIPT_ID,
    name="Residual kill / non-metric residual convention",
    status=GovernanceStatus.PROVISIONAL_CONVENTION,
    tier=ClaimTier.CONSTRAINED,
    required_obligations=["derive_no_overlap_operator_or_parent_identity"],
)
```

Do not call a route licensed until obligations and evidence actually support it.

## Dependencies

Prefer dependency checks that verify content, kind, and status.

Weak dependency:

```python
ns.declare_dependency(
    dependency_id="upstream_marker",
    upstream_script_id="10_kappa_trace_response__candidate_kappa_joint_minimum_spline_model",
    upstream_derivation_id="kappa_joint_minimum_spline_model_marker",
)
```

Stronger dependency:

```python
ns.declare_dependency(
    dependency_id="upstream_constant_weight_el_equation",
    upstream_script_id="10_kappa_trace_response__candidate_kappa_joint_minimum_energy_functional",
    upstream_derivation_id="constant_weight_joint_minimum_sample",
    expected_status=Status.DERIVED.value,
    expected_record_kind=RecordKind.SAMPLE_DERIVATION,
)
```

If the exact symbolic output is stable, include `expected_output`.

```python
ns.declare_dependency(
    dependency_id="projector_idempotence",
    upstream_script_id="09_vacuum_identity_and_source_coupling__candidate_vector_current_projection_operator",
    upstream_derivation_id="transverse_projector_idempotence_residual",
    expected_output=sp.zeros(3),
    expected_status=Status.DERIVED.value,
    expected_record_kind=RecordKind.DERIVATION,
)
```

## Handoff Imports

Group-ending summaries should record what the next group may import.

Use `HandoffImportRecord` for all assumptions, claims, obligations, and route statuses that a downstream group may rely on or must preserve.

```python
handoff = HandoffImportRecord(
    handoff_id="group_16_metric_insertion_handoff",
    script_id=SCRIPT_ID,
    imported_as=RecordKind.SUMMARY_CLAIM,
    status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
    imported_record_refs=[
        "claim:group_16_insertion_not_licensed",
        "obligation:derive_boundary_neutrality_theorem",
        "route:residual_kill_nonmetric_convention",
    ],
    description="Inputs that Group 17/19 may import from Group 16.",
)
ns.record_handoff_import(handoff)
```

The handoff must distinguish:

- derived results;
- samples;
- open obligations;
- provisional conventions;
- rejected routes;
- branch kills;
- theorem targets.

Do not hide an open obligation inside a general "handoff complete" marker.

## Summary Scripts

Summary scripts should query the archive rather than restating status from memory where possible.

Use `GovernanceSummaryBuilder` for archive-backed summaries:

```python
from vacuumforge.governance import GovernanceSummaryBuilder

summary = GovernanceSummaryBuilder(archive).build([
    "16_metric_insertion_and_no_overlap__candidate_B_s_insertion_recovery_audit",
    "16_metric_insertion_and_no_overlap__candidate_metric_insertion_group_status_summary",
])

for obligation in summary.open_obligations:
    ...
for claim in summary.claims:
    ...
for counterexample in summary.counterexamples:
    ...
for handoff in summary.handoff_imports:
    ...
```

A summary may add interpretation, but interpretation must remain separate from upstream derivation status.

Do not upgrade:

```text
candidate route -> provisional convention
provisional convention -> licensed claim
open obligation -> satisfied obligation
sample support -> general derivation
```

unless the summary records new evidence or a new derivation.

## Updating Common Script Shapes

### Group 09 Style: Symbolic Algebra Plus Placeholder Marker

Observed pattern:

- real SymPy matrices, residuals, source expressions, or identities;
- local `status_line`;
- final marker derivation with `inputs=[]`;
- missing coefficients or source laws printed as prose.

Update pattern:

1. Add script metadata.
2. Replace local output helper with `ScriptOutput`.
3. Record each real residual or identity as a contentful derivation.
4. Record coefficient/source-law gaps as proof obligations.
5. Record recovery-target or no-smuggling statements as governance claims.
6. Keep an inventory marker only if useful, with `RecordKind.INVENTORY_MARKER` and `is_placeholder=True`.

Example obligations likely to appear:

```text
derive alpha_W/K_c
derive beta_W observable coupling
derive global boundary normalization
derive vector source identity
```

### Group 10 Style: Toy Variational Or Diagnostic Models

Observed pattern:

- useful symbolic Euler-Lagrange computations;
- toy assumptions such as constant weights;
- diagnostic definitions for possible deviations;
- open scale/weight/coefficient questions.

Update pattern:

1. Record the Euler-Lagrange expression as a derivation if it follows from the stated toy functional.
2. Mark constant-weight or hand-chosen profiles as `SAMPLE_DERIVATION`.
3. Mark deviation definitions as `DIAGNOSTIC_EXAMPLE`.
4. Record weights, transition widths, observability, and coefficient origins as obligations.
5. Do not treat a toy minimizer as a physical prediction.

### Group 11 Style: Field-Equation Closure Inventory And GR Audit

Observed pattern:

- dataclass ledgers with statuses like `DERIVED_REDUCED`, `STRUCTURAL`, `MATCHED`, `MISSING`, `RISK`;
- some real concrete metric checks;
- no controlled failure in older audit scripts;
- summary language that can outrank upstream records.

Update pattern:

1. Convert ledger rows into `ClaimRecord`s and `ProofObligationRecord`s.
2. Record actual concrete metric checks as contentful derivations or compatibility examples.
3. Add `case_6_good_failure()` to audit scripts that lack controlled failure.
4. Use `SUMMARY_CLAIM` only for claims backed by source claims, evidence, derivations, or obligations.
5. Avoid treating `MATCHED` as derived. It is usually a governance claim plus an obligation for coefficient origin.

### Groups 15-19 Style: Governance-Heavy Audits And Group Summaries

Observed pattern:

- dataclass rows with `status`, `consequence`, and `handoff`;
- statuses such as `SAFE_IF`, `REQUIRED`, `THEOREM_TARGET`, `RECOVERY_TARGET`, `BRANCH_KILLED`, `DEFER`, `CLOSED`;
- explicit `case_6_good_failure()` in newer audits;
- group summaries containing rich handoff material.

Update pattern:

1. Map each row to a claim, route, branch decision, or obligation.
2. Treat `SAFE_IF` as `CANDIDATE_ROUTE` or `PROVISIONAL_CONVENTION`, depending on whether the script says it may be used as a convention.
3. Treat `THEOREM_TARGET`, `REQUIRED`, and `MISSING` as obligations.
4. Treat `RECOVERY_TARGET` as a policy/governance claim, not a construction rule.
5. Treat `BRANCH_KILLED` as a branch decision only if evidence exists.
6. Turn `handoff` fields into `HandoffImportRecord`s in group-ending summaries.

## Status Mapping

Many existing scripts use local status strings. Migrate them conservatively.

| Existing string | Usually means | v3 record/status |
| --- | --- | --- |
| `DERIVED` | computed derivation | `Status.DERIVED`, `RecordKind.DERIVATION` |
| `DERIVED_REDUCED` | reduced/symmetric/special-case derivation | `Status.DERIVED` plus `scope=...`; sometimes `SAMPLE_DERIVATION` |
| `STRUCTURAL` | architecture-level support, not derivation | `GovernanceStatus.HEURISTIC` or `CANDIDATE_ROUTE` |
| `CONSTRAINED`, `CONSTRAINED_BY_IDENTITY` | restricted by existing identity or policy | `GovernanceStatus.POLICY_RULE` or `CANDIDATE_ROUTE` with provenance |
| `MATCHED` | target known but coefficient/mechanism imported | claim plus obligation; not derivation |
| `MISSING` | required item absent | `ProofObligationRecord(status=OPEN)` |
| `UNRESOLVED` | open prerequisite | `ProofObligationRecord(status=OPEN)` or deferred branch |
| `REQUIRED` | prerequisite/theorem target | `ProofObligationRecord(status=OPEN)` |
| `THEOREM_TARGET` | desired theorem not yet proved | `ProofObligationRecord(status=OPEN)` plus optional claim |
| `RECOVERY_TARGET` | downstream test | `GovernanceStatus.POLICY_RULE` or `HEURISTIC` |
| `SAFE_IF` | conditional route | `CANDIDATE_ROUTE` or `PROVISIONAL_CONVENTION` |
| `CANDIDATE` | candidate route | `GovernanceStatus.CANDIDATE_ROUTE` |
| `DEFER` | not licensed pending prerequisites | `DEFERRED_PENDING_PREREQUISITES` |
| `REJECTED` | rejected route | `REJECTED_ROUTE`, preferably with evidence/reason |
| `BRANCH_KILLED` | branch exclusion | `KILLED_BY_CONTRADICTION` only with evidence |
| `CLOSED` | group script completed | run metadata or summary claim; not proof by itself |
| `RISK` | unresolved risk | `OPEN_RISK` or obligation |
| `FORBIDDEN` | policy rule | `POLICY_RULE` with reason code |

When uncertain, choose the weaker status and record an obligation.

## Lint Expectations

The linter is meant to catch common AI-authored failure modes. Avoid these patterns:

```text
stale "# Suggested location:" header
hand-rolled boolean pass/warn status helper
strong branch-kill language without local evidence/provenance
Status.DERIVED marker in a script that only prints inventory prose
real symbolic computation followed only by a placeholder marker
audit script without controlled-failure case
summary language that upgrades upstream status without archive query/evidence
versioned script pair without supersession metadata
```

Expected practices:

- Use `ScriptOutput`.
- Add metadata headers.
- Record actual symbolic results.
- Record proof obligations.
- Attach evidence to exclusions.
- Make summary handoffs explicit.
- Keep metadata JSON-safe.

## Verification After Updating A Script

For one updated script:

```powershell
C:\Users\alano\anaconda3\python.exe vacuum_forge\src\scripts_v3\<group>\<script>.py
C:\Users\alano\anaconda3\python.exe -m vacuumforge.cli archive list --root vacuum_forge\src\scripts_v3\.vacuumforge_archive
C:\Users\alano\anaconda3\python.exe -m vacuumforge.cli archive verify --root vacuum_forge\src\scripts_v3\.vacuumforge_archive
```

For tests:

```powershell
C:\Users\alano\anaconda3\python.exe -m pytest -q
```

If running lint directly, prefer the repository's lint entrypoint or tests around `tools/vf_lint`.

## Migration Checklist

Before editing:

- Read the whole script.
- Identify whether it is derivation, sample, diagnostic, audit, inventory, summary, memo, or sieve.
- Identify all real computed expressions.
- Identify all governance statements.
- Identify all missing prerequisites.
- Identify all branch decisions and route decisions.
- Identify downstream handoff material.

During editing:

- Add metadata header.
- Replace local output helper with `ScriptOutput`.
- Record contentful derivations with actual inputs and outputs.
- Mark samples and diagnostics as samples or diagnostics.
- Convert missing prerequisites to obligations.
- Convert governance rows to claims/routes/branch decisions.
- Attach evidence to branch kills and rejected routes.
- Strengthen dependencies when stable.
- Preserve final run metadata.

After editing:

- Run the script.
- Inspect archive files for derivations, claims, obligations, evidence, branches, routes, and handoffs.
- Run tests.
- Run lint or lint tests.
- Check that no open obligation was treated as satisfied.
- Check that no summary claim outranks its support.

## Final Discipline

When in doubt, do less but record it accurately.

A script that says "this remains a theorem target" should create an open obligation, not a theorem.

A script that finds a special-case identity should record the scope, not generalize it.

A script that rejects a branch for policy reasons should say policy rule, not contradiction.

A group summary should make the next group's assumptions visible, including which assumptions are only provisional.
