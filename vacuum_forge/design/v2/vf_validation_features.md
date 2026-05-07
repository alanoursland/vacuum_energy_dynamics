# VacuumForge Validation Hardening: Technical Design

## Companion document

This document specifies implementation detail for the four features proposed in `vf_validation_features.md`. The feature design doc explains why each feature exists and what it does. This document explains how to build them.

The features, in implementation priority order:

1. `vf-lint`: discipline-enforcement linting (standalone tool).
2. `CoordinateChange`: coordinate-transformation derivations registered as VacuumForge derivations.
3. `ConcreteMetricCheck`: leak-aware classification of known-metric requirement validation.
4. `ProjectArchive`: cross-script dependency tracking with persistent storage.

Each section below covers: dependencies on existing code, module structure, public API, internal logic, edge cases, testing strategy, and known limitations.

---

## Feature 1: vf-lint

### Position in the codebase

This is a standalone tool, not a VacuumForge module. It lives outside `src/vacuumforge/` entirely. Recommended location:

```
tools/vf_lint/
    __init__.py
    cli.py
    analyzer.py
    rules.py
    tests/
        test_known_good_scripts.py
        test_known_bad_scripts.py
        fixtures/
            good_v1_log_scale_modes.py
            bad_closure_summary.py
            mixed_partial_validation.py
```

The reason for the separation: `vf-lint` analyzes scripts that may or may not import VacuumForge. It must not depend on VacuumForge being installed in the analyzed script's environment. It also targets a different audience (the script author at lint time) than VacuumForge itself (the script at run time).

### Dependencies on existing code

None. The tool uses only `ast` from the standard library and a small CLI framework (suggest `argparse`; resist the temptation to pull in click/typer for a tool this small).

### Public API

```python
# tools/vf_lint/cli.py

def main(argv: list[str] | None = None) -> int:
    """Entry point. Returns 0 if all files pass, 1 if any warn, 2 if any fail."""
```

```bash
$ vf-lint candidate_log_scale_modes_test.py
candidate_log_scale_modes_test.py: OK (12 PASS verdicts, all gated on real computation)

$ vf-lint candidate_parent_correction_tensor_group_status_summary.py
candidate_parent_correction_tensor_group_status_summary.py: FAIL
  Line 247: PASS in dataclass constructor (Group19StatusEntry status="CLOSED")
  Line 251: PASS in dataclass constructor (Group19StatusEntry status="DEFER")
  ... 10 more violations
  No sympy or vacuumforge imports detected.
```

### Internal logic

The analyzer walks the AST looking for verdict-emitting patterns. The patterns to detect:

**Pattern A**: `print("[PASS] ...")` or `print(f"[PASS] ...")` calls.
**Pattern B**: `status_line(label, ok, ...)` calls where `ok` is the second argument.
**Pattern C**: Dataclass instantiations where a `status` field is set to a verdict-like string literal (`"PASS"`, `"CLOSED"`, `"DERIVED"`, `"DEFER"`, `"BRANCH_KILLED"`, etc.).

For each verdict-emitting site, trace backward to determine whether it is gated on a computation:

1. If the verdict is a literal inside a constructor call (Pattern C), report FAIL. This is the closure-summary pattern. There is no gating — the verdict is the input.
2. If the verdict is in a print statement (Pattern A), find the enclosing `if` statement. If none, report WARN (unconditional verdict). If the `if` condition is a literal, report WARN.
3. If the verdict is a `status_line` call (Pattern B), inspect the second argument:
   - If it is a literal `True`/`False`, WARN.
   - If it is a function call, check whether the function is one of: `is_zero`, `check_equal`, `simplify(...) == 0`, or any `vacuumforge.*` call. If yes, OK. If no, WARN.
   - If it is a comparison expression, check whether either side traces back to a sympy or vacuumforge operation. If yes, OK. If no, WARN.

The "trace back" step uses simple AST analysis: walk from the call argument up to its definition in the same scope, recursively. Bound the recursion at 5 levels to avoid pathological cases. If the trace exits the function scope (refers to a parameter or a module-level name), conservatively assume OK rather than WARN — false negatives are preferable to false positives for a linting tool.

### Rule definitions

Rules live in `rules.py` as a list of (name, pattern_matcher, severity) tuples. This makes adding new rules trivial. The starting rule set:

```python
RULES = [
    Rule("verdict_in_dataclass_literal", _detect_verdict_in_dataclass, severity="FAIL"),
    Rule("unconditional_pass_print", _detect_unconditional_pass, severity="WARN"),
    Rule("status_line_with_literal", _detect_status_line_with_literal, severity="WARN"),
    Rule("status_line_with_no_computation", _detect_status_line_no_compute, severity="WARN"),
    Rule("missing_validation_imports", _detect_no_validation_imports, severity="INFO"),
]
```

The `INFO` severity for missing validation imports is intentional: a script that imports neither sympy nor vacuumforge but produces verdicts should be flagged, but it is not necessarily a failure (the closure-summary script is a failure for other reasons; a pure prose script with verdict labels is borderline). The combination of FAIL on dataclass literals + INFO on missing validation imports correctly classifies the closure-summary script as FAIL.

### Edge cases

**Generated tests with hardcoded PASS labels.** A unit test fixture might legitimately contain `print("[PASS]")` literals. Distinguish by file path: `tools/vf_lint/tests/fixtures/` is exempt from analysis when running on itself.

**Verdicts produced by helper functions.** A script might define `def my_status(label, condition): print(f"[{'PASS' if condition else 'FAIL'}] {label}")`. The analyzer should recognize this pattern — verdict ternaries inside function definitions count as gated on the condition.

**Vacuumforge calls that return non-boolean values.** `analyzer.analyze(structure)` returns a result object; the script then accesses `.summary_status.value` and compares it to a string. The trace should follow attribute access and method calls. Bound the trace, but be generous about what counts as a vacuumforge-rooted computation.

**Scripts that import vacuumforge but use it only superficially.** A script could import `from vacuumforge.core.context import TheoryContext`, instantiate a context, and never call any validation method on it, while printing PASS for unrelated reasons. The current rules would not catch this. This is a known gap. A more sophisticated rule could check whether vacuumforge calls actually appear in the trace lineage of each verdict, but the false-positive rate would be high. Defer.

### Testing strategy

A test fixture directory contains known-good and known-bad scripts. The known-good scripts include the actual Group 01 foundation scripts (copied as fixtures, not symlinked). The known-bad scripts include a copy of the closure-summary script and a few hand-crafted variants:

- `unconditional_pass.py`: a script with `print("[PASS]")` not inside any `if`.
- `dataclass_verdict.py`: a script with `MyClass(status="PASS")` literals.
- `partial_validation.py`: a script that has some real validation and some hardcoded verdicts (should produce mixed warnings, not a uniform classification).

The test asserts that vf-lint produces the expected classifications. Snapshot tests are appropriate here — diff the full output against a recorded expected output.

A separate test confirms that vf-lint runs against every script in `scripts/` and produces some classification (no crashes, no missing files). This is a regression test against the tool itself, not a correctness test against the scripts.

### Known limitations

vf-lint does not catch scripts whose verdicts come from real computation but whose computation is wrong. It is a syntactic check, not a semantic one. A script that computes `is_zero(0)` and gates a PASS on it will pass the lint check, regardless of whether the underlying claim is meaningful. This is fine — semantic correctness is what VacuumForge itself addresses. vf-lint catches the failure mode where the syntactic shape of validation is missing entirely.

vf-lint also cannot catch the case where a script delegates verdicts to an LLM-generated string template that happens to use the right syntactic patterns. If a future LLM produces dataclass instantiations with `status` fields populated by `_compute_status()` calls that are themselves literal-returning functions, the lint check would pass. Adding a rule that distinguishes "computation that returns a literal" from "computation that performs work" is possible but expensive and low-priority.

Estimated implementation: 300-500 lines of source plus 100-200 lines of test fixtures and assertions. One developer-week including the fixture set.

---

## Feature 2: CoordinateChange

### Position in the codebase

```
src/vacuumforge/coordinates/
    __init__.py
    transform.py        # CoordinateChange class
    invariants.py       # _validate_coordinate_invariance
    tests/
        test_radial_reparameterization.py
        test_areal_gauge_reconstruction.py
        test_jacobian_consistency.py
```

The new module is parallel to `metric/`, `modes/`, etc. It depends on `core` (for `TheoryContext`, `is_zero`, dependency graph) and `metric` (for `WeakFieldMetric`).

### Dependencies on existing code

- `vacuumforge.core.context.TheoryContext`: register the coordinate change in the context's dependency graph.
- `vacuumforge.core.dependency.DependencyGraph.record_derivation`: store the transformation as a derivation record.
- `vacuumforge.core.simplify.is_zero` and `check_equal`: equivalence checks for the validator.
- `vacuumforge.metric.weak_field.WeakFieldMetric`: input and output type for `transform_metric`.
- `vacuumforge.requirements.validators.Requirement` and `ValidationResult`: the new validator integrates with the existing validation system.

The `ProjectionMap.jacobian` method in `structure_search/projection.py` is the right pattern to follow for the Jacobian computation. Do not import it directly — the projection map operates on multi-variable spaces, while `CoordinateChange` operates on a single radial coordinate. Mirror the pattern, do not reuse.

### Public API

```python
# vacuumforge/coordinates/transform.py

@dataclass
class CoordinateChange:
    """A radial coordinate transformation r = f(R)."""

    old_coord: sympy.Symbol
    new_coord: sympy.Symbol
    transform: sympy.Basic   # f(R), expressed in terms of new_coord
    inverse: sympy.Basic | None = None  # R(r), if known
    derivation_id: str | None = None    # set on registration

    def jacobian(self) -> sympy.Basic:
        """Return df/dR."""
        return sympy.diff(self.transform, self.new_coord)

    def transform_scale_factor(
        self,
        scale_factor: sympy.Basic,
        kind: str,  # "temporal" or "radial"
    ) -> sympy.Basic: ...

    def transform_log_modes(
        self,
        a: sympy.Basic,  # ln A in old coordinate
        b: sympy.Basic,  # ln B in old coordinate
    ) -> tuple[sympy.Basic, sympy.Basic]: ...

    def transform_metric(
        self,
        metric: WeakFieldMetric,
    ) -> WeakFieldMetric: ...

    def register(self, ctx: TheoryContext, derivation_id: str) -> None:
        """Register this coordinate change as a derivation in the context."""
```

```python
# vacuumforge/coordinates/invariants.py

def _validate_coordinate_invariance(
    ctx: TheoryContext,
    req_id: str,
    quantity: sympy.Basic,
    change: CoordinateChange,
) -> ValidationResult:
    """Check whether a registered scalar is invariant under a coordinate change."""
```

The validator is parameterized rather than registered as a standard requirement. This is intentional: coordinate invariance is a per-quantity, per-transformation check, not a global requirement that applies to a context. Add it to the requirement manager only when used for a specific quantity.

### Internal logic

#### `transform_scale_factor`

For a static spherical metric `ds² = -A(r) dt² + B(r) dr² + r² dΩ²` and a transformation `r = f(R)`:

- Temporal: `A_new(R) = A(f(R))`. No Jacobian factor.
- Radial: `B_new(R) = B(f(R)) · (df/dR)²`.

Implementation:

```python
def transform_scale_factor(self, scale_factor, kind):
    fp = self.jacobian()
    substituted = scale_factor.subs(self.old_coord, self.transform)
    if kind == "temporal":
        return sympy.simplify(substituted)
    elif kind == "radial":
        return sympy.simplify(substituted * fp**2)
    else:
        raise ValueError(f"Unknown scale factor kind: {kind}")
```

Edge case: the input `scale_factor` may be an unevaluated `sympy.Function` like `A(r)`. The `subs` call must handle both `sympy.Symbol` substitution (`r → f(R)`) and `sympy.Function` substitution (`A(r) → A(f(R))`). The implementation should detect which case applies and use the appropriate sympy mechanism. For Function objects, use `expr.replace(Function('A')(self.old_coord), Function('A')(self.transform))`. For Symbol objects, plain `subs` works.

#### `transform_log_modes`

Given `a = ln A` and `b = ln B` in the old coordinate:

```python
def transform_log_modes(self, a, b):
    fp = self.jacobian()
    a_new = a.subs(self.old_coord, self.transform)
    b_new = b.subs(self.old_coord, self.transform) + 2 * sympy.log(fp)
    return sympy.simplify(a_new), sympy.simplify(b_new)
```

This is the formula derived in `gauge_dependence_modes.py` Case 1. The implementation mirrors the script's manual derivation, but registered in the dependency graph as a derived result rather than printed.

#### `register`

```python
def register(self, ctx, derivation_id):
    self.derivation_id = derivation_id
    ctx.dependencies.record_derivation(
        node_id=derivation_id,
        node_kind="coordinate_change",
        inputs=[self.old_coord, self.new_coord, self.transform],
        method="chain_rule",
        status=Status.DERIVED,
        metadata={
            "jacobian": str(self.jacobian()),
            "inverse_known": self.inverse is not None,
        },
    )
```

The `Status.DERIVED` marker is correct: a coordinate transformation is a calculus identity, not a theory-specific assumption. The dependency graph node represents the *act* of transforming, not the *result* of transformation. Specific transformed quantities (a transformed metric, a transformed log mode) are registered as separate derivations downstream, with this node as an input.

#### `_validate_coordinate_invariance`

```python
def _validate_coordinate_invariance(ctx, req_id, quantity, change):
    transformed = quantity.subs(change.old_coord, change.transform)
    transformed = sympy.simplify(transformed)
    residual = sympy.simplify(quantity - transformed)
    if is_zero(residual) is True:
        return ValidationResult(
            req_id, "pass",
            f"{quantity} is invariant under {change.old_coord} = {change.transform}",
            evidence=[residual],
        )
    elif is_zero(residual) is False:
        return ValidationResult(
            req_id, "fail",
            f"{quantity} shifts by {residual} under coordinate change",
            evidence=[residual, transformed],
        )
    else:
        return ValidationResult(
            req_id, "undetermined",
            "Could not determine invariance",
        )
```

Note the three-way return mirroring `is_zero`'s behavior. This matches the existing validator pattern.

### Edge cases

**Symbolic transformations.** The transformation `r = f(R)` may use a symbolic `f` rather than a concrete function. `sympy.diff(sympy.Function('f')(R), R)` produces `Derivative(f(R), R)`, which is correct but produces unwieldy expressions. The implementation should not assume `f` is concrete. The Group 01 scripts use both concrete (`f = λR`, `f = R + ε·ξ(R)`) and symbolic (`f = sympy.Function("f")(R)`) forms. Both must work.

**Infinitesimal transformations.** `gauge_dependence_modes.py` Case 3 uses `f = R + ε·ξ(R)` and series-expands to first order. The current `CoordinateChange` does not perform series expansion — it produces exact transformed expressions. To handle infinitesimal cases, the script should compose a `CoordinateChange` with a separate series expansion step using `ctx.expansion.weak_field`. This is the right factoring: coordinate changes are exact, expansions are approximate, and combining them happens at the script level.

**Non-radial transformations.** The current API is radial-only. This is a deliberate limitation. The Group 01 scripts only need radial transformations. Generalization to time or angular transformations is possible but should wait for a use case.

**Composed transformations.** A user might want to apply two coordinate changes in sequence. The current API does not support composition directly. Workaround: apply the first transformation to get intermediate quantities, then construct a second `CoordinateChange` from the intermediate to the final. If composition becomes a common pattern, add a `CoordinateChange.compose(other)` method. Defer.

### Testing strategy

Tests live in `vacuumforge/coordinates/tests/`. Test categories:

**Unit tests on `CoordinateChange` mechanics.** For a fixed simple transformation (`r = λR`), verify that `transform_scale_factor`, `transform_log_modes`, and `transform_metric` produce the expected outputs. These tests use concrete sympy expressions and assert structural equality (after simplification).

**Reconstruction tests.** Apply a transformation, then apply its inverse, and verify the round-trip recovers the original. This catches sign errors and Jacobian factor mistakes.

**Reproduction of script results.** Reproduce the key results from `gauge_dependence_modes.py` and `areal_gauge_kappa_condition.py` using `CoordinateChange`. The reproduced results should be identical (after simplification) to the script's hand-derived values. This is the highest-value test set: it confirms that the new feature produces the same answers as the validated sympy work it replaces.

**Validator tests.** Build a context with a known-invariant scalar (e.g., the areal radius itself) and verify `_validate_coordinate_invariance` reports `pass`. Build a context with a known-non-invariant scalar (e.g., naive κ) and verify it reports `fail` with the expected residual.

### Known limitations

`CoordinateChange` operates on expressions, not on the metric definition itself. If a user has a `WeakFieldMetric` registered and applies a `CoordinateChange`, the resulting transformed metric is a new `WeakFieldMetric` object, not a modification of the original. Downstream validators need to be told which metric to use. This is consistent with the existing pattern for metric ansatz updates and should not require new infrastructure.

Estimated implementation: 400-600 lines of source plus 200-300 lines of tests. One to two developer-weeks.

---

## Feature 3: ConcreteMetricCheck

### Position in the codebase

```
src/vacuumforge/metric/
    concrete_check.py     # new file
    tests/
        test_concrete_check.py
        test_schwarzschild_classification.py
```

This is a small addition to the existing `metric` module. It does not warrant its own subdirectory.

### Dependencies on existing code

- `vacuumforge.core.context.TheoryContext`: clone the context for non-destructive substitution.
- `vacuumforge.core.context.TheoryContext.clone`: already exists per the dehydrated dump.
- `vacuumforge.requirements.leak_detection.detect_leaks`: leak detection.
- `vacuumforge.requirements.validators.RequirementManager.validate`: per-requirement validation.
- `vacuumforge.requirements.targets.TargetLibrary.has`: check whether a target exists for the requirement.

### Public API

```python
# vacuumforge/metric/concrete_check.py

@dataclass
class ConcreteMetricCheckResult:
    requirement_id: str
    status: str  # "satisfied_independently", "satisfied_by_construction", "failed", "undetermined"
    message: str
    leak_report: LeakReport | None
    underlying_validation: ValidationResult


def check_concrete_metric(
    ctx: TheoryContext,
    A_value: sympy.Basic,
    B_value: sympy.Basic,
    requirement_ids: list[str] | None = None,
) -> list[ConcreteMetricCheckResult]:
    """Check a concrete metric against requirements, classifying leaks."""
```

### Internal logic

```python
def check_concrete_metric(ctx, A_value, B_value, requirement_ids=None):
    # Clone the context to avoid polluting the caller's state
    test_ctx = ctx.clone()

    # Inject the concrete metric values as assumptions
    ms = test_ctx._mode_symbols
    test_ctx.assumptions.add(
        id="concrete_metric_A",
        expression=sympy.Eq(ms.A, A_value),
        status="assumption",
    )
    test_ctx.assumptions.add(
        id="concrete_metric_B",
        expression=sympy.Eq(ms.B, B_value),
        status="assumption",
    )

    # Default to all standard requirements if none specified
    if requirement_ids is None:
        requirement_ids = [r.id for r in test_ctx.requirements.list()]

    results = []
    for req_id in requirement_ids:
        validation = test_ctx.requirements.validate(req_id, test_ctx)

        # Determine leak status
        leak = None
        if validation.status == "pass" and test_ctx._targets.has(req_id):
            leak = detect_leaks(req_id, test_ctx.assumptions, test_ctx._targets)

        # Classify
        if validation.status == "fail":
            status = "failed"
            message = validation.message
        elif validation.status == "undetermined":
            status = "undetermined"
            message = validation.message
        elif validation.status == "pass" and leak is not None and leak.leaked:
            status = "satisfied_by_construction"
            message = (
                f"{req_id} is satisfied, but the target form is present "
                f"in the metric definition. {leak.message}"
            )
        elif validation.status == "pass":
            status = "satisfied_independently"
            message = f"{req_id} is satisfied without the target form being assumed."
        else:
            # validation.status == "assumed" — already a leak case
            status = "satisfied_by_construction"
            message = validation.message
            if leak is None:
                # Validator already caught the leak before we did
                leak = LeakReport(
                    target_id=req_id, leaked=True,
                    leaked_via=validation.dependencies,
                    message=validation.message,
                )

        results.append(ConcreteMetricCheckResult(
            requirement_id=req_id,
            status=status,
            message=message,
            leak_report=leak,
            underlying_validation=validation,
        ))

    return results
```

The key insight is in the classification logic: a `pass` from the underlying validator combined with a `leaked=True` from the leak detector is reclassified as `satisfied_by_construction`, not as a failure. This is the new vocabulary the feature introduces.

### Edge cases

**Metrics that fail multiple requirements with overlapping leak patterns.** A metric defined as `A = exp(s), B = exp(-s)` (the trace-free shear case) satisfies `AB = 1` by construction. The leak detector flags this for `reciprocal_scaling`. But `gamma_v_one` is also satisfied — does that count as `satisfied_independently` or `satisfied_by_construction`? Strictly speaking, `gamma_v_one` is implied by `reciprocal_scaling`, so satisfying `gamma_v_one` while leaking on `reciprocal_scaling` is a chain that the user might want to know about. The current API does not expose this transitive leak structure. Defer.

**Metrics that the validator cannot evaluate.** If `A_value` contains free symbols beyond the standard ones, the validator may return `undetermined`. The classification correctly reports `undetermined`. The user should reduce the metric to a concrete form before running the check.

**Cloning side effects.** The `clone()` method on `TheoryContext` performs a deepcopy. If the context contains large objects (a huge dependency graph, many cached expressions), this is expensive. For the Group 01 scripts, contexts are small and the cost is negligible. If `ConcreteMetricCheck` is called in a loop over many candidate metrics, consider exposing a non-cloning variant that takes responsibility for state management. Defer.

### Testing strategy

**Schwarzschild test.** The canonical test: register the standard target library, build a context, call `check_concrete_metric` with `A = 1 - 2GM/(rc²)`, `B = 1/A`. Assert that `reciprocal_scaling` returns `satisfied_by_construction` with a leak report identifying `concrete_metric_B` as the leaked-via assumption.

**Independent-derivation test.** Build a context where `AB = 1` is derived from a trace-kernel exchange via energy equilibrium (mirroring v1 Section 4 Fork TC). Call `check_concrete_metric` with the resulting `A` and `B` values. Assert that `reciprocal_scaling` returns `satisfied_independently`. This test demonstrates that the classification correctly distinguishes the two cases.

**Failure test.** Call with `A = 1 + Φ/c²`, `B = 1` (no spatial response). Assert that `reciprocal_scaling` returns `failed` with a nonzero residual.

### Known limitations

`ConcreteMetricCheck` inherits all limitations of the leak detector. If the metric definition encodes the target in a form not present in `equivalent_forms`, the leak will be missed and the result will be misclassified as `satisfied_independently` when it should be `satisfied_by_construction`. The mitigation is to maintain the equivalent-forms list as new patterns are observed.

Estimated implementation: 150-250 lines of source plus 100-150 lines of tests. Three to five developer-days.

---

## Feature 4: ProjectArchive

### Position in the codebase

```
src/vacuumforge/archive/
    __init__.py
    archive.py            # ProjectArchive class
    records.py            # DerivationRecord, DependencyDeclaration
    serialization.py      # sympy ↔ JSON-safe form
    invalidation.py       # source-change detection
    cli.py                # vf-archive subcommand
    tests/
        test_record_and_retrieve.py
        test_dependency_verification.py
        test_invalidation.py
        test_serialization_roundtrip.py
```

This is the largest new module. It includes its own CLI subcommand for archive inspection.

### Dependencies on existing code

- `vacuumforge.core.dependency.DependencyGraph`: the in-memory dependency graph already exists. The archive persists a superset of this graph across script invocations.
- `vacuumforge.core.simplify.check_equal`: the verification step uses the existing equivalence check.
- `vacuumforge.core.context.TheoryContext`: archive operations are scoped to a context.
- `vacuumforge.cli`: the new `vf archive` subcommand integrates with the existing CLI module.

### Storage layout

The archive is a directory tree. Each script gets its own subdirectory. Each derivation is a JSON file:

```
.vacuumforge_archive/
    candidate_log_scale_modes_test/
        derivations/
            section_3_trace_kernel_derivation.json
            section_4_fork_tc_kappa_zero.json
        dependencies.json
        last_run_metadata.json
        source_hash.json
    candidate_covariant_parent_modes/
        derivations/
            case_2_structural_trace_kernel.json
            case_2b_anisotropic_trace_kernel.json
        dependencies.json
        ...
```

The choice of JSON over pickle is deliberate: JSON is human-readable, diff-friendly, and version-controllable. The tradeoff is that sympy expressions need to be serialized to a JSON-safe form (specifically, sympy's `srepr` or `dumps` format).

### Public API

```python
# vacuumforge/archive/archive.py

class ProjectArchive:
    def __init__(self, root_path: pathlib.Path) -> None: ...

    def script_namespace(self, script_id: str) -> ScriptNamespace: ...


class ScriptNamespace:
    def record_derivation(
        self,
        derivation_id: str,
        inputs: list[sympy.Basic],
        output: sympy.Basic,
        method: str,  # "structural", "algebraic", "coordinate_transform", "energy_equilibrium"
        status: Status,
        metadata: dict[str, Any] | None = None,
    ) -> DerivationRecord: ...

    def get_derivation(self, derivation_id: str) -> DerivationRecord | None: ...

    def declare_dependency(
        self,
        dependency_id: str,
        upstream_script_id: str,
        upstream_derivation_id: str,
        expected_output: sympy.Basic | None = None,
    ) -> DependencyDeclaration: ...

    def verify_dependencies(
        self,
        ctx: TheoryContext,
    ) -> list[DependencyCheckResult]: ...

    def invalidate(self) -> None:
        """Mark this script's archive entries as stale (e.g., on source change)."""
```

### Internal logic

#### Recording derivations

A derivation record contains:

- `derivation_id`: unique within the script.
- `inputs`: list of input expressions, serialized.
- `output`: the derived expression, serialized.
- `method`: a tag describing how the derivation was performed.
- `status`: one of the existing `Status` enum values.
- `metadata`: arbitrary additional fields.
- `recorded_at`: timestamp.
- `vacuumforge_version`: for forward compatibility.

When `record_derivation` is called, the namespace serializes the inputs and output, writes the JSON file, and adds an entry to the in-memory dependency graph for the current run. If a record with the same `derivation_id` already exists, it is overwritten — the assumption is that re-running the script produces the canonical version of the derivation.

#### Declaring dependencies

A dependency declaration is stored in the script's `dependencies.json` file. It contains:

- `dependency_id`: unique within the script.
- `upstream_script_id`: the script that produced the dependency.
- `upstream_derivation_id`: the derivation within that script.
- `expected_output`: serialized form of the expected output (optional but recommended).
- `declared_at`: timestamp.

The `expected_output` field is the load-bearing one. Without it, "verifying a dependency" reduces to "checking that the upstream derivation still exists." With it, verification can check that the upstream output still equals what the downstream script was written to expect.

#### Verifying dependencies

```python
def verify_dependencies(self, ctx):
    results = []
    for dep in self._load_dependencies():
        upstream = self._archive.script_namespace(dep.upstream_script_id)
        record = upstream.get_derivation(dep.upstream_derivation_id)

        if record is None:
            results.append(DependencyCheckResult(
                dep, status="dependency_missing",
                message=f"Upstream derivation '{dep.upstream_derivation_id}' "
                        f"not found in archive for script '{dep.upstream_script_id}'.",
            ))
            continue

        if dep.expected_output is None:
            # No expected output declared; can only check existence
            results.append(DependencyCheckResult(
                dep, status="dependency_satisfied",
                message=f"Upstream derivation exists; output not verified "
                        f"(no expected_output declared).",
            ))
            continue

        # Verify the output still matches
        if check_equal(record.output, dep.expected_output):
            results.append(DependencyCheckResult(
                dep, status="dependency_satisfied",
                message=f"Upstream derivation matches expected output.",
            ))
        else:
            results.append(DependencyCheckResult(
                dep, status="dependency_changed",
                message=f"Upstream derivation output has changed. "
                        f"Expected: {dep.expected_output}; Found: {record.output}.",
            ))

    return results
```

The `check_equal` call uses VacuumForge's existing simplification machinery, so it correctly handles algebraic equivalence (not just structural string equality). This is essential — a re-run that produces `2*kappa` instead of the previously-recorded `kappa + kappa` should not be flagged as a change.

#### Source-change invalidation

A script's entries should be invalidated when the script's source changes. The archive stores a hash of the script source in `source_hash.json`. On every run, the script computes its own source hash (via `inspect.getsource(__main__)` or by reading `sys.argv[0]`) and compares against the stored hash. On mismatch, the script's archive entries are cleared before new derivations are recorded.

This is a safety mechanism against the failure mode where a script is modified but the archive still contains stale derivations from the old version. It is conservative — any source change triggers full invalidation, even changes that do not affect derivations (e.g., comment edits). This is acceptable. False invalidations are cheap; missed invalidations are dangerous.

### Edge cases

**Concurrent script runs.** If two scripts run simultaneously and write to the same archive directory, file-level conflicts are possible. JSON files are small and writes are atomic on most filesystems, but this is not guaranteed. Mitigation: use `os.rename` for atomic writes (write to `derivation.json.tmp`, then rename to `derivation.json`). Document that the archive is not designed for concurrent multi-process use.

**Sympy expression serialization.** `sympy.srepr` produces a string that round-trips through `sympy.sympify`. This works for almost all expressions but has known issues with custom Symbols (those with assumptions like `positive=True`) — the `srepr` output preserves the assumptions, and `sympify` on the output reconstructs them, but the resulting Symbol is *not* identical to the original (sympy considers two Symbols with the same name and same assumptions to be equal but not identical). For the archive's purposes, equality (not identity) is sufficient, but tests should verify this assumption.

**Cycles in the dependency graph.** If script A depends on script B and script B depends on script A, the archive's verification step needs to avoid infinite loops. The simplest mitigation: detect cycles when building the verification queue and report them as a separate error class (`dependency_cycle`).

**Archive corruption.** A partially-written JSON file or a malformed entry should not crash the entire verification step. Each load should be wrapped in a try/except that reports the corruption and continues with the next entry. Corrupted entries should be reported in a `vf archive doctor` subcommand.

### CLI integration

```bash
$ vf archive list candidate_log_scale_modes_test
Derivations (2):
  section_3_trace_kernel_derivation [DERIVED, structural]
  section_4_fork_tc_kappa_zero [DERIVED, energy_equilibrium]

Dependencies (0):
  (none declared)

Last run: 2025-...
Source hash: ...

$ vf archive verify candidate_covariant_parent_modes
Checking 2 dependencies...
  uses_v1_trace_kernel_result [SATISFIED]
  uses_v1_log_mode_algebra [CHANGED — expected output differs]

1 of 2 dependencies failed verification.

$ vf archive doctor
Scanning archive for inconsistencies...
  candidate_orbit_space_modes/derivations/case_3.json: malformed JSON, skipping
  candidate_areal_gauge_kappa_condition: source hash mismatch, entries should be invalidated

Run 'vf archive invalidate <script_id>' to clear stale entries.
```

### Testing strategy

**Round-trip serialization tests.** For each sympy expression class commonly used in VacuumForge (Symbol, Integer, Rational, exp, log, Eq, Function, Derivative, etc.), assert that `serialize(deserialize(serialize(expr))) == serialize(expr)` and that the deserialized expression `check_equal`'s the original.

**Record-and-retrieve tests.** Record a derivation, retrieve it, assert equality. Record multiple derivations, retrieve a subset by ID, assert no cross-contamination.

**Dependency verification tests.** Set up a two-script archive: script A records a derivation, script B declares a dependency on it. Verify the dependency. Modify script A's recorded output. Verify the dependency again, assert `dependency_changed`.

**Invalidation tests.** Record entries, modify the source hash, assert that the next run with a different hash invalidates the entries.

**End-to-end test.** Run two real Group 01 scripts in sequence, with the second declaring a dependency on the first. Assert the dependency verifies cleanly. Modify the first script's output (artificially, by editing the archive), re-run the second, assert `dependency_changed`.

### Known limitations

The archive does not capture the *reasoning* behind a derivation, only its inputs and outputs. If a script's logic for computing the output changes but the output itself happens to be the same, the verification will pass. This is by design: the archive is checking the contract between scripts (output A flows into input B), not the implementation of either script.

The `expected_output` field can become stale if the user copies the output from a script run without updating the dependency declaration. There is no automatic mechanism to keep `expected_output` synchronized with the upstream's actual output. This is intentional — automatic synchronization would silently mask the very drift the archive is meant to detect.

The archive is the feature most likely to be neglected in practice. A half-maintained archive (entries recorded but not verified, or verified but not invalidated) is worse than no archive. Before implementing this feature, the team should commit to: (1) running `vf archive verify` as part of every script invocation, (2) treating verification failures as build failures, (3) running `vf archive doctor` periodically to catch corruption.

If that commitment is not realistic, do not build this feature. The other three features provide most of the validation hardening value at a fraction of the maintenance cost.

Estimated implementation: 1500-2000 lines of source plus 500-700 lines of tests. Two to three developer-weeks for the initial build. Ongoing maintenance is the larger cost.

---

## Cross-feature integration

### Order of implementation

The four features have minimal interdependencies. The recommended order:

1. `vf-lint` first. Standalone, addresses the actual observed failure mode, useful immediately.
2. `CoordinateChange` second. Improves three Group 01 scripts directly.
3. `ConcreteMetricCheck` third. Small addition, useful for orbit_space Case 7 and any future known-metric tests.
4. `ProjectArchive` last. Largest investment, contingent on commitment to maintenance.

`vf-lint` and `ConcreteMetricCheck` could be implemented in parallel by different developers. `CoordinateChange` and `ProjectArchive` should be sequenced — `ProjectArchive`'s integration tests benefit from having `CoordinateChange` available as a source of derivations to record.

### Compatibility with existing tests

The existing VacuumForge test suite (per the design doc, located at `tests/`) should not need modification. The new features add new test files but do not change existing module APIs. The one exception: if `CoordinateChange.register` modifies the dependency graph in ways that affect other tests, those tests need review. Suggested mitigation: write the registration to use a clearly-namespaced node ID prefix (`coordinate_change_*`) so existing tests can filter it out.

### Documentation updates

Each feature requires:

- Module docstring with usage examples.
- An entry in the milestones document (extending the existing 40-milestone list).
- An entry in the user-facing overview document if the feature changes the recommended workflow.

The overview document currently describes VacuumForge as a "reduced field-equation laboratory." `vf-lint` and `ProjectArchive` are infrastructure rather than laboratory features. The overview should be extended with a section on validation infrastructure that distinguishes these from the symbolic-research core.

---

## Risks and mitigations

**Risk: feature creep.** Each feature has obvious extensions. `CoordinateChange` could grow to handle non-radial transformations, finite diffeomorphisms, gauge transformations. `ConcreteMetricCheck` could grow to handle source operators, energy functionals, full theory comparisons. `ProjectArchive` could grow to handle distributed teams, conflict resolution, version-controlled derivations.

Mitigation: the feature design doc explicitly lists out-of-scope capabilities. This technical design follows the same discipline. Resist requests to extend any feature beyond its stated scope without a corresponding update to the feature design.

**Risk: theatrical validation.** A new feature, however carefully designed, could be misused to produce verdicts that look rigorous without being well-founded. The closure-summary script that initiated this audit is the canonical example.

Mitigation: each feature's verdicts must trace back to a real computation on a real expression. The technical design has been written with this constraint in mind — every PASS/FAIL/satisfied/leaked verdict is the result of an `is_zero`, `check_equal`, or equivalent call. There are no hardcoded verdicts in the design.

**Risk: maintenance burden.** Four new features add roughly 2500-3500 lines of source code plus 1000-1500 lines of tests. The total surface increase is significant.

Mitigation: implement in priority order. Stop after `CoordinateChange` if maintenance bandwidth is constrained. The first two features (`vf-lint` and `CoordinateChange`) deliver most of the validation hardening value. `ConcreteMetricCheck` is a pure win at small cost. `ProjectArchive` is the marginal call.

**Risk: design assumptions about VacuumForge internals.** This design has been written based on the dehydrated source dump and the design documents. Some implementation details — the exact API of `TheoryContext.clone`, the structure of `AssumptionRecord`, the semantics of `Status.DERIVED` — are inferred rather than known.

Mitigation: before implementing each feature, read the actual source for the modules it depends on. If the inferred APIs are wrong, the design will need adjustment. The risk is contained because the dependencies are localized — a mistake in inferred `TheoryContext.clone` semantics affects `ConcreteMetricCheck` only, not the other features.

---

## What this design intentionally does not address

This design does not propose:

- A unified validation report format spanning all features. Reports are per-feature for now. A unified format can be designed once the per-feature outputs have been used in practice.
- Automatic generation of equivalent forms for the target library. Mentioned in the feature design as deferred; still deferred here.
- Integration with the counterexample-search module. The counterexample module exists but has not been audited. Integration should wait until the module's actual capabilities are confirmed.
- A higher-level "is this script's claims trustworthy?" meta-tool. The closest thing is `vf-lint`, which catches syntactic absence of validation. Semantic trustworthiness is the job of VacuumForge's existing tools, not a new meta-tool.

These deferrals are not arbitrary. Each represents a place where the value of the feature is unclear or where the right design depends on information not yet available. Building features speculatively, without that information, is exactly the failure mode the validation hardening effort is meant to recover from.