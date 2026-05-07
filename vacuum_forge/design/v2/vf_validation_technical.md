# VacuumForge Feature Design: Group 01 Validation Hardening

## Purpose

This document specifies feature additions to VacuumForge intended to address gaps observed during the Group 01 audit. The audit identified three classes of work that VacuumForge does not currently support but could support without compromising its discipline:

1. Coordinate-transformation derivations (currently sympy-only in `gauge_dependence_modes`, `areal_gauge_kappa_condition`, and `orbit_space_modes`).

2. Concrete-metric requirement validation that distinguishes "satisfies the target" from "satisfies the target by construction" (currently impossible to express; relevant to Schwarzschild-style checks in `orbit_space_modes` Case 7 and any future known-metric tests).

3. Cross-script dependency tracking, so that later scripts can build on earlier derivations with machine-checked rather than prose-only continuity.

This document does not propose features that would expand VacuumForge's scope into territory the theory has not yet earned. Specifically, it does not propose validators for parent correction tensors, divergence safety, source separation, or any other Group 10+ topic where the underlying objects are not yet defined. Building validators for undefined objects produces verdicts with the visual register of rigor but no substance, which is the failure mode the Group 01 audit was undertaken to catch.

A fourth proposal, discipline-enforcement linting, addresses the failure mode at the artifact level rather than the tool level. It is included because it is the highest-value addition for preventing recurrence, even though it is not strictly a VacuumForge feature.

## Out of scope

The following capabilities are explicitly excluded from this design:

- Validators for objects the theory has not defined (H_curv, H_exch, parent correction tensors).
- Auto-classification of scripts as "validated" or "not validated" by meta-analysis.
- Verdicts about interpretive prose claims (e.g., "is kappa a trace-like parent mode in the covariant sense").
- Equivalent-form auto-discovery for the target library (deferred until manual maintenance has identified which forms recur as missing).
- Counterexample-search integration with the requirement validators (deferred as hardening, dependent on knowing the existing counterexample module's actual capabilities).

These exclusions are not because the capabilities are useless. They are because, in the current state of the theory and tool, building them risks producing output that resembles validation without performing it. The exclusion list should be revisited if and when the underlying objects become well-defined enough to validate.

## Feature 1: CoordinateChange

### Motivation

The scripts `gauge_dependence_modes`, `areal_gauge_kappa_condition`, and `orbit_space_modes` all perform coordinate-transformation derivations using raw sympy. The derivations are correct, but their results are not registered with VacuumForge's dependency tracking, which means downstream scripts that claim to build on these results cannot machine-verify the dependency.

Examples of derivations these scripts produce:

- Under `r = f(R)`, naive κ shifts by `log(f')` and naive s shifts by `−log(f')`.
- The areal-gauge compensation condition `kappa_areal = 0` is equivalent in arbitrary radial coordinates to `T(R)Q(R) = S'(R)²`.
- Under `r = f(R)`, an areal-gauge metric with `AB = 1` produces a transformed naive `T(R)Q(R) = f'(R)²` rather than 1.

Each of these derivations is a verifiable algebraic identity. Each is currently a print statement.

### API

A new module `vacuumforge.coordinates` provides:

```python
class CoordinateChange:
    """A radial coordinate transformation r = f(R)."""

    def __init__(
        self,
        old_coord: sympy.Symbol,
        new_coord: sympy.Symbol,
        transform: sympy.Basic,
        ctx: TheoryContext,
    ) -> None: ...

    def transform_metric(
        self,
        metric: WeakFieldMetric,
    ) -> WeakFieldMetric: ...

    def transform_scale_factor(
        self,
        scale_factor: sympy.Basic,
        kind: str,  # "temporal" or "radial"
    ) -> sympy.Basic: ...

    def transformed_log_modes(
        self,
        a: sympy.Basic,
        b: sympy.Basic,
    ) -> tuple[sympy.Basic, sympy.Basic]: ...
```

A `CoordinateChange` records itself in the context's dependency graph as a derivation, with the input metric or scale factors as inputs and the transformed metric or scale factors as outputs. The status of the derivation is `Status.DERIVED` because it follows from the chain rule, which is not a theory-specific assumption.

### Validator

A new validator `_validate_coordinate_invariance` checks whether a registered scalar quantity is invariant under a registered coordinate change. This is the right tool for claims like "the areal radius is geometrically invariant" — a claim the current scripts make in prose but do not check.

### What this catches

- A script that claims `kappa` is invariant under reparameterization. The validator computes the transformed kappa and reports the residual; if nonzero, it fails.
- A script that claims a particular gauge-fixed condition is the arbitrary-coordinate form of an areal-gauge condition. The validator transforms the areal-gauge form and checks equivalence with the claimed arbitrary-coordinate form.

### What this does not catch

- Whether a particular gauge choice is "physically meaningful" in the broader sense. That is interpretation, not algebra.
- Whether the chosen transformation `r = f(R)` is the right transformation to test. That is the user's responsibility.

### Implementation notes

The Jacobian computation already exists in `ProjectionMap`. The `is_zero` machinery already handles the core equivalence checks. The new code is mostly bookkeeping: register inputs, compute transforms via `sympy.diff`, store outputs as derivation records.

Estimated size: 200–400 lines of source plus tests.

## Feature 2: ConcreteMetricCheck

### Motivation

The Group 01 audit identified that `orbit_space_modes` Case 7 (Schwarzschild) instantiates a concrete metric (`A = 1 − 2GM/rc²`, `B = 1/A`) and checks that it satisfies `AB = 1`, `kappa = 0`, and other targets. This is currently done with hand checks. Routing it through the requirement validators would correctly flag the leak (because `B = 1/A` is in the assumption ledger), but the resulting "leaked" verdict is not the right vocabulary: Schwarzschild *does* satisfy `AB = 1`; it just satisfies it by construction rather than by independent derivation.

The right vocabulary distinguishes:

- **Satisfied independently**: the metric satisfies the target and the target is not present in the assumption ledger as an equivalent form.
- **Satisfied by construction**: the metric satisfies the target and the target *is* present in the assumption ledger (or is implied by the metric definition itself).
- **Failed**: the metric does not satisfy the target.

This three-way classification is what makes Schwarzschild-style checks comparable across scripts. Without it, every Schwarzschild check looks identical to a structural derivation, or every Schwarzschild check looks identical to a leaked tautology, depending on which way you bias the validator.

### API

A new module `vacuumforge.metric.concrete_check` provides:

```python
@dataclass
class ConcreteMetricCheckResult:
    requirement_id: str
    status: str  # "satisfied_independently", "satisfied_by_construction", "failed", "undetermined"
    message: str
    leak_report: LeakReport | None
    evidence: list[sympy.Basic]


def check_concrete_metric(
    ctx: TheoryContext,
    A_value: sympy.Basic,
    B_value: sympy.Basic,
    requirement_ids: list[str] | None = None,
) -> list[ConcreteMetricCheckResult]:
    """Check a concrete metric against requirements with leak-aware classification."""
```

The function:

1. Substitutes A_value and B_value into the context (without modifying the original).
2. Runs each requested requirement validator.
3. For each PASS verdict, runs `detect_leaks` against the corresponding target.
4. Classifies the result:
   - PASS + no leak → `satisfied_independently`
   - PASS + leak → `satisfied_by_construction`
   - FAIL → `failed`
   - other → `undetermined`

### What this catches

- A script that claims a known metric "derives" `AB = 1` when in fact the metric was constructed to satisfy it. The leak detector flags it; this wrapper translates the leak into the right classification rather than treating it as a failure.

### What this does not catch

- Whether the construction of the concrete metric was itself principled. A sufficiently obfuscated metric definition could hide its relationship to the target form, and the leak detector might miss it. This is the same limitation the leak detector already has; this feature inherits it.

### Implementation notes

This feature is mostly a thin wrapper around existing validators and the leak detector. The new logic is the four-way classification of validator output. The risk of the feature is interpretive: if a script using this wrapper reports "satisfied_by_construction" for a case that the user expected to be "satisfied_independently," the report is correct but might be misread. Documentation should be explicit that "satisfied_by_construction" is not a failure — it is a true and useful classification.

Estimated size: 100–200 lines of source plus tests.

## Feature 3: ProjectArchive

### Motivation

The Group 01 audit traced the dependency chain among the foundation scripts:

- `log_scale_modes_test_v2` builds on v1.
- `covariant_parent_modes` builds on v1/v2's trace-kernel result.
- `gauge_dependence_modes` builds on `covariant_parent_modes`.
- `areal_gauge_kappa_condition` builds on `gauge_dependence_modes`.
- `orbit_space_modes` builds on `areal_gauge_kappa_condition`.

Each "builds on" relationship is currently expressed in prose: a comment block at the top of the script saying "Previous result: ...". If the previous result changes — because the upstream script was modified, or because a re-run produced different output — the prose does not detect the change, and the downstream script may produce verdicts that are no longer consistent with its inputs.

This is the precise failure mode the Group 10+ drift exemplifies, scaled down. The Group 19 closure script claimed to depend on Group 17 and Group 18 results without machine-checking that those results still held.

### API

A new module `vacuumforge.archive` provides:

```python
class ProjectArchive:
    """Persistent storage of derivation records across scripts."""

    def __init__(self, root_path: pathlib.Path) -> None: ...

    def record_derivation(
        self,
        script_id: str,
        derivation_id: str,
        inputs: list[sympy.Basic],
        output: sympy.Basic,
        method: str,  # "structural", "algebraic", "coordinate_transform", "energy_equilibrium"
        status: Status,
    ) -> None: ...

    def get_derivation(self, script_id: str, derivation_id: str) -> DerivationRecord: ...

    def declare_dependency(
        self,
        downstream_script_id: str,
        upstream_script_id: str,
        upstream_derivation_id: str,
    ) -> DependencyDeclaration: ...

    def verify_dependency(
        self,
        dep: DependencyDeclaration,
        ctx: TheoryContext,
    ) -> DependencyCheckResult: ...
```

A `DependencyCheckResult` reports either:

- `dependency_satisfied`: the upstream derivation exists and produces the expected output.
- `dependency_changed`: the upstream derivation exists but produces a different output than when the dependency was declared.
- `dependency_missing`: the upstream derivation is no longer in the archive.

### Workflow

1. A script's first run registers its derivations in the archive.
2. A downstream script declares dependencies on specific upstream derivations.
3. On subsequent runs, the downstream script verifies its dependencies before producing verdicts. If any dependency has changed or gone missing, the script halts with an explicit error rather than producing potentially-stale verdicts.

### What this catches

- A script that claims to build on an upstream result that no longer holds. Verification fails before the script produces output.
- A script that claims to build on an upstream result that was never actually registered. Verification fails because the dependency is missing.
- Silent drift between scripts where upstream changes were not propagated downstream.

### What this does not catch

- Whether the dependency declaration itself is *meaningful* — that is, whether the downstream script actually uses the upstream result in the way it claims. The declaration is a user-asserted contract; the tool checks that the upstream output matches what was recorded, not that the downstream logic correctly consumes it.

### Implementation notes

This is the largest feature in this document. It requires:

- Persistent storage (probably JSON or pickle, sympy expressions serialize to either).
- A canonical form for derivation records that lets the archive recognize "the same derivation" across runs.
- A protocol for invalidating archive entries when the source script changes.

The risk is that the archive becomes its own source of drift: if entries are recorded but never re-verified, the archive accumulates stale data and the dependency checks become a different kind of theatrical rigor. Mitigation: every script that uses the archive should re-run its own derivations on every invocation, not just verify dependencies.

Estimated size: 600–1000 lines of source plus tests, plus a CLI surface for inspecting archive state.

This feature is the most expensive and the most ambitious. It should not be undertaken unless there is commitment to maintaining the archive as a load-bearing artifact. A half-built ProjectArchive is worse than no ProjectArchive, because it produces verification verdicts that are no longer trustworthy.

## Feature 4: Discipline-enforcement linting (not a VacuumForge feature)

### Motivation

The closure-summary script that initiated the Group 01 audit was not a VacuumForge failure. It was a script that produced PASS verdicts without ever calling sympy or VacuumForge. Nothing in the existing tooling prevents this. A new VacuumForge feature, no matter how rigorous, cannot prevent it either, because the failure mode is at the artifact level: a script that does not import the validation tools cannot be saved by improvements to the validation tools.

The right response to this failure mode is a separate linting tool that scans candidate scripts for the specific pattern: PASS-style output that is not preceded by a real computation.

### API

A standalone tool `vf-lint`:

```bash
vf-lint script.py
```

reports:

- Each `print("[PASS] ...")` (or status_line PASS) call.
- Whether the call is reached only via a conditional that depends on a computed value.
- Whether the computed value comes from a sympy or vacuumforge call (not just a string literal).

Output is one of:

- `OK`: every PASS in the script is gated on a real computation.
- `WARN`: at least one PASS is unconditional or gated on a literal.
- `FAIL`: the script has the closure-summary structure (PASS verdicts in dataclass constructors or hardcoded strings).

### Implementation notes

The tool is a static analyzer. It uses Python's `ast` module to parse the script and trace data flow from PASS-emitting calls back to their gating conditions. It does not need to be perfect — even a tool with significant false-positive and false-negative rates would have caught the closure-summary script, because that script's failure was unmistakable at the AST level.

This is a small tool. Estimated size: 200–400 lines, plus a test suite of known-good and known-bad scripts.

The reason this is the highest-value addition: it addresses the failure mode that actually happened, not a hypothetical failure mode. Every other feature in this document hardens VacuumForge against errors it could in principle catch. This tool catches the specific error class that Group 10+ produced, which the existing VacuumForge could not catch.

## Implementation priority

Recommended order, in decreasing value-to-effort ratio:

1. **vf-lint** (Feature 4). Smallest scope, addresses the actual observed failure mode, useful immediately.

2. **CoordinateChange** (Feature 1). Moderate scope, well-defined, directly improves three Group 01 scripts. Low risk because the underlying primitives (Jacobians, `is_zero`) already exist and are trusted.

3. **ConcreteMetricCheck** (Feature 2). Small scope, mostly a wrapper. Useful for Schwarzschild-style checks and would extend cleanly to other known-metric tests.

4. **ProjectArchive** (Feature 3). Largest scope, highest risk. Should be undertaken only with commitment to maintenance. A useful test of commitment: would the archive be re-built and re-verified on every script run? If not, the feature will drift and become its own source of theatrical rigor.

## What this design does not propose, and why

A reader checking this document for completeness might expect proposals for:

- A H_curv or H_exch validator. Not proposed because the underlying objects are not defined; building a validator for an undefined object produces theatrical verdicts.
- An automatic Group-N closure summary generator. Not proposed because the closure summaries were the failure mode.
- A natural-language interpretation checker. Not proposed because interpretation is not algebra.
- A unified "VacuumForge score" for a candidate theory. Not proposed because the design's discipline is to produce specific verdicts about specific claims, not aggregate quality scores.

The absence of these features is intentional. The design's goal is to extend VacuumForge's capabilities in directions where the verdicts the new tools produce are well-founded, and to leave undefined territory undefined until the theory earns its way into it.

## Calibration note

This document is a feature design, not a commitment. Each feature has a real implementation cost and a real maintenance cost. Building all four would expand VacuumForge's surface significantly and would require corresponding investment in tests, documentation, and discipline. If the immediate goal is to recover from the Group 10+ drift and re-establish confidence in the Group 01 base, the minimum viable set is `vf-lint` plus `CoordinateChange`. The other two features can wait until there is concrete evidence they are needed.
