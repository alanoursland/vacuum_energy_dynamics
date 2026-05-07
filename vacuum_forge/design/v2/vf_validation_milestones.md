# VacuumForge Validation Hardening Milestones

## Purpose

This document breaks the validation-hardening technical design into implementation milestones. It extends the main VacuumForge milestone series with four new features:

- `vf-lint`: discipline-enforcement linting (standalone tool).
- `CoordinateChange`: coordinate-transformation derivations registered in VacuumForge's dependency graph.
- `ConcreteMetricCheck`: leak-aware classification of known-metric requirement validation.
- `ProjectArchive`: cross-script dependency tracking with persistent storage.

The milestones continue the numbering from the main milestones document. They follow the same section structure (Goal, Deliverables, Required Capabilities, Completion Criteria, Notes) and the same discipline: each milestone should leave the software in a usable state, even if narrow.

The four features have minimal interdependencies. The recommended implementation order matches the priority order from the technical design: linting first, then `CoordinateChange`, then `ConcreteMetricCheck`, then `ProjectArchive`. Within each feature, milestones are ordered so that early ones produce useful artifacts even if later ones are deferred.

A reader who is committed to building all four features should expect this series to take roughly four to six developer-weeks, depending on test depth and integration choices. A reader who plans to stop after the first two features (the recommended minimum viable set) should expect roughly two developer-weeks.

## Milestone 41: vf-lint Project Skeleton

### Goal

Create the standalone `vf-lint` tool's project structure with a working but empty CLI.

This milestone establishes that vf-lint is a separate tool from VacuumForge proper, and gives it a place to grow.

### Deliverables

- Project directory at `tools/vf_lint/` with the structure described in the technical design.
- `pyproject.toml` or equivalent for the standalone tool, declaring no VacuumForge dependency.
- Working `argparse`-based CLI that accepts a list of file paths and prints "OK" for each (placeholder behavior).
- Initial test setup using `pytest`.
- Test fixture directory at `tools/vf_lint/tests/fixtures/` containing two starter files: a copy of `candidate_log_scale_modes_test.py` (known-good) and a copy of the parent-correction-tensor closure script (known-bad).

### Required Capabilities

The user can run:

```bash
$ vf-lint candidate_log_scale_modes_test.py
candidate_log_scale_modes_test.py: OK
```

The tool exits 0 for any file. Real classification logic comes in the next milestone.

The user can run the test suite:

```bash
$ cd tools/vf_lint && pytest
```

The smoke test passes.

### Completion Criteria

- The CLI is invokable on a Python file and produces output.
- The package structure matches the technical design.
- Tests run.
- The tool does not import VacuumForge.

### Notes

The fixture directory is critical. Subsequent milestones depend on having canonical good and bad scripts available without external file dependencies. The fixtures should be exact copies, not symlinks.

The tool's CLI exit codes (0/1/2 for OK/WARN/FAIL) should be wired up in this milestone but always return 0 until the rule logic is implemented. This ensures the exit-code contract is established before it carries meaning.

## Milestone 42: vf-lint AST Walker and Pattern Detection

### Goal

Implement the AST analysis core that finds verdict-emitting sites in a script.

This milestone produces no classifications yet — it only locates the patterns that future milestones will classify.

### Deliverables

- AST walker that visits every `Call` node in a script.
- Pattern matchers for the three cases identified in the technical design: `print("[PASS] ...")` calls, `status_line(label, ok, ...)` calls, and dataclass instantiations with verdict-like string fields.
- A `VerdictSite` dataclass capturing each match: file path, line number, column, the AST node, and the matched pattern.
- Unit tests asserting that the walker finds the expected sites in each fixture.

### Required Capabilities

The walker correctly identifies all PASS-emitting sites in the known-good fixture.

The walker correctly identifies all dataclass-literal verdicts in the known-bad fixture.

The walker does not crash on syntactically invalid Python (it reports the syntax error and continues with the next file).

### Completion Criteria

- All three pattern types are detected on hand-crafted test inputs.
- The known-good fixture produces approximately the right number of `VerdictSite` entries (assert at least 5 for the foundation script; do not over-specify).
- The known-bad closure-summary fixture produces a `VerdictSite` for every `Group19StatusEntry` constructor call.
- Unit tests cover the dataclass-literal pattern explicitly, since this is the closure-summary failure mode.

### Notes

Use Python's standard `ast` module. Resist the temptation to pull in `libcst` or other source-preserving parsers — `ast` is sufficient for verdict-site detection, and adding dependencies to a linting tool reduces its portability.

The walker's design should be open to new pattern types. Each pattern matcher is a function `(ast.Call) -> VerdictSite | None`. Future milestones may add patterns; the walker should accept a list of matchers as configuration.

## Milestone 43: vf-lint Trace-Back Analysis

### Goal

For each verdict site, determine whether the verdict is gated on a real computation.

This is the milestone where vf-lint becomes useful. After this milestone, the tool can distinguish the closure-summary script from the foundation scripts.

### Deliverables

- Trace-back algorithm that, given a `VerdictSite`, walks the AST backward to find the gating condition.
- Logic that distinguishes "gated on a literal" from "gated on a computation."
- Recognition of sympy and vacuumforge calls as evidence of real computation.
- A `VerdictClassification` dataclass extending `VerdictSite` with one of `"OK"`, `"WARN"`, or `"FAIL"` plus an explanation string.
- The CLI reports classifications per file and exits with the maximum severity.

### Required Capabilities

The user can run:

```bash
$ vf-lint candidate_log_scale_modes_test.py
candidate_log_scale_modes_test.py: OK (12 PASS verdicts, all gated on real computation)
$ vf-lint candidate_parent_correction_tensor_group_status_summary.py
candidate_parent_correction_tensor_group_status_summary.py: FAIL
  Line 247: PASS in dataclass constructor (Group19StatusEntry status="CLOSED")
  ... [more violations]
  No sympy or vacuumforge imports detected.
```

The exit code is 0 for the foundation script and 2 for the closure-summary script.

### Completion Criteria

- All Group 01 foundation scripts classify as OK.
- The closure-summary script classifies as FAIL.
- A hand-crafted "unconditional PASS" test fixture classifies as WARN.
- A hand-crafted "PASS gated on `if True`" test fixture classifies as WARN.
- A hand-crafted "PASS gated on `if my_func()` where `my_func` returns a literal" test fixture classifies as WARN.
- A hand-crafted "PASS gated on `if is_zero(expr)`" test fixture classifies as OK.

### Notes

The trace-back algorithm should bound recursion at five levels. If the trace exits the function scope, default to OK rather than WARN. False negatives are preferable to false positives for this tool — the goal is catching the egregious cases, not perfecting nuanced edge cases.

The recognition of "sympy or vacuumforge call" is import-aware: the walker should track which names refer to sympy or vacuumforge symbols based on the script's imports. A script that does `import sympy as sp` and uses `sp.simplify` should have `sp.simplify` recognized; a script that does `from sympy import simplify` should have `simplify` recognized. This is straightforward but easy to miss.

This milestone is where vf-lint earns its keep. After this, the remaining milestones add polish and edge cases.

## Milestone 44: vf-lint Rule Configuration and Output Formatting

### Goal

Make the rule set configurable and improve output for human readers.

### Deliverables

- A `rules.py` module with rules as `(name, matcher, severity)` tuples.
- The starting rule set described in the technical design.
- Configuration via a `vf_lint.toml` file at the project root, allowing rule disable/enable and severity override.
- Output formatters: human-readable (default), JSON (for CI integration), and quiet mode (for hooks).
- Coverage of all rule types in the test fixtures.

### Required Capabilities

The user can disable a rule:

```toml
# vf_lint.toml
[rules.unconditional_pass_print]
severity = "INFO"
```

The user can request JSON output:

```bash
$ vf-lint --format=json script.py
{"file": "script.py", "classification": "OK", "violations": []}
```

The user can run vf-lint in quiet mode (output only on FAIL):

```bash
$ vf-lint --quiet good_script.py bad_script.py
bad_script.py: FAIL
  ...
```

### Completion Criteria

- All rule severities are configurable.
- JSON output is well-formed and machine-parseable.
- Quiet mode produces no output for OK or WARN.
- Test fixtures exist for every rule the tool emits.

### Notes

Configuration is the place where vf-lint can drift if not careful. A user can disable a rule that catches their actual failure mode. The default configuration should be strict; disabling rules should be a deliberate choice. Document the rules and their severities in a user-facing file.

After this milestone, vf-lint is feature-complete for the validation-hardening goals stated in the technical design. Subsequent improvements (catching helper-function indirection, better trace-back across modules) are deferred.

## Milestone 45: CoordinateChange Module Skeleton

### Goal

Create the `vacuumforge.coordinates` package with stubs for the public API.

This milestone gives the new module a place to live and validates that it integrates with the existing VacuumForge structure.

### Deliverables

- New module directory at `src/vacuumforge/coordinates/`.
- `__init__.py` exposing the planned public API (with NotImplementedError stubs).
- `transform.py` with the `CoordinateChange` dataclass and method stubs.
- `invariants.py` with the `_validate_coordinate_invariance` function stub.
- Tests directory at `src/vacuumforge/coordinates/tests/`.
- A smoke test asserting that the module imports and that `CoordinateChange` can be instantiated with the canonical example (radial reparameterization).

### Required Capabilities

The user can run:

```python
from vacuumforge.coordinates import CoordinateChange
import sympy

R = sympy.Symbol("R", positive=True)
r = sympy.Symbol("r", positive=True)
f = sympy.Function("f")(R)

change = CoordinateChange(
    old_coord=r,
    new_coord=R,
    transform=f,
)
```

The instantiation succeeds. Method calls raise `NotImplementedError` with informative messages.

### Completion Criteria

- The package imports cleanly.
- `CoordinateChange` is instantiable.
- The smoke test passes.
- The existing VacuumForge test suite still passes.

### Notes

This milestone is deliberately small. It exists to validate the module's place in the package layout before any logic is written. Skipping it and going straight to implementation is possible but tends to result in import-path issues that surface late.

## Milestone 46: CoordinateChange Core Transformation Methods

### Goal

Implement the three core transformation methods: `transform_scale_factor`, `transform_log_modes`, `transform_metric`.

### Deliverables

- Working implementations of all three methods, with the algorithms described in the technical design.
- Handling of both `sympy.Symbol` and `sympy.Function` substitution patterns.
- A `jacobian` property returning `df/dR`.
- Unit tests covering: scaling transformation `r = λR`, infinitesimal transformation `r = R + ε·ξ(R)`, and symbolic transformation `r = f(R)`.
- Reconstruction tests: apply a transformation, apply its inverse, assert round-trip equivalence.

### Required Capabilities

The user can transform a scale factor:

```python
A_R = change.transform_scale_factor(A_r, kind="temporal")
B_R = change.transform_scale_factor(B_r, kind="radial")
```

The transformed expressions are correct sympy expressions, simplified.

The user can transform log modes:

```python
a_R, b_R = change.transform_log_modes(a_r, b_r)
```

The result matches the formula from `gauge_dependence_modes.py` Case 1: `a_R = a(f(R))`, `b_R = b(f(R)) + 2 log(f'(R))`.

### Completion Criteria

- All three transformation methods produce correct outputs for the canonical examples.
- Round-trip tests pass for invertible transformations.
- The script `gauge_dependence_modes.py` Case 1 can be reproduced using the new API, with the result matching (after simplification) the script's hand-derived value.

### Notes

The `transform_scale_factor` method needs to handle two kinds of inputs: a `sympy.Symbol` representing a free variable, and a `sympy.Function` call representing an unevaluated function. Both forms appear in the existing scripts. Use `sympy.subs` for the Symbol case and `sympy.replace` for the Function case. Branch on the input type rather than trying to handle both with one mechanism.

The `transform_metric` method may be deferred to Milestone 47 if `WeakFieldMetric`'s API is unclear at this point. The other two methods are sufficient to demonstrate the feature's value.

## Milestone 47: CoordinateChange Registration and Validator

### Goal

Wire `CoordinateChange` into VacuumForge's dependency graph and implement the coordinate-invariance validator.

### Deliverables

- `CoordinateChange.register(ctx, derivation_id)` method that records the change in the context's dependency graph.
- The registration uses `Status.DERIVED` and method `"chain_rule"`.
- `_validate_coordinate_invariance(ctx, req_id, quantity, change)` returning a `ValidationResult`.
- A helper for adding the validator to the requirement manager when needed.
- Tests verifying that registered coordinate changes appear in the dependency graph.
- Tests for the validator: a known-invariant scalar passes, a known-non-invariant scalar fails with the expected residual.

### Required Capabilities

The user can register a coordinate change:

```python
change = CoordinateChange(...)
change.register(ctx, derivation_id="g19_radial_reparam")
```

The dependency graph contains a node with that ID and the chain-rule method tag.

The user can validate a quantity's invariance:

```python
result = _validate_coordinate_invariance(
    ctx, req_id="kappa_invariance", quantity=kappa, change=change
)
assert result.status == "fail"
assert "log(f'" in str(result.evidence[0])
```

### Completion Criteria

- Registration appears in the dependency graph.
- The validator returns `pass`/`fail`/`undetermined` mirroring `is_zero`'s three-way return.
- The Group 01 script `gauge_dependence_modes.py` Case 1 can be expressed entirely through `CoordinateChange` plus the validator, producing the same conclusion ("κ shifts by log(f'), is not invariant").

### Notes

`Status.DERIVED` is the right marker because coordinate transformations are calculus identities, not theory-specific assumptions. Do not use `Status.ASSUMPTION` here, even if the user has not yet proven the chain rule explicitly — the chain rule is part of sympy, not part of the theory under test.

This milestone closes out `CoordinateChange`. After it, the three Group 01 scripts that currently use raw sympy for coordinate transformations can be rewritten to use the new API. That rewrite is not part of this milestone — it is downstream cleanup work that depends on the team's appetite for retroactive refactoring.

## Milestone 48: ConcreteMetricCheck Implementation

### Goal

Implement leak-aware classification of known-metric requirement validation as a single working module.

This feature is small enough to fit in one milestone. Splitting it across milestones would impose more overhead than the implementation itself.

### Deliverables

- New module at `src/vacuumforge/metric/concrete_check.py`.
- `ConcreteMetricCheckResult` dataclass.
- `check_concrete_metric(ctx, A_value, B_value, requirement_ids)` function.
- The four-way classification logic: `satisfied_independently`, `satisfied_by_construction`, `failed`, `undetermined`.
- Tests covering each classification: Schwarzschild (satisfied_by_construction), trace-kernel-derived (satisfied_independently), no-spatial-response (failed), incomplete-metric (undetermined).

### Required Capabilities

The user can check a known metric:

```python
from vacuumforge.metric.concrete_check import check_concrete_metric

results = check_concrete_metric(
    ctx,
    A_value=1 - 2*G*M / (r * c**2),
    B_value=1 / (1 - 2*G*M / (r * c**2)),
)
```

For Schwarzschild, the `reciprocal_scaling` result has `status == "satisfied_by_construction"` and a non-None `leak_report` identifying the metric definition as the leaked-via assumption.

For an independently-derived metric where `AB = 1` follows from energy equilibrium, the result has `status == "satisfied_independently"` and `leak_report.leaked == False`.

### Completion Criteria

- All four classifications are reachable from the test inputs.
- The Schwarzschild test produces `satisfied_by_construction`.
- The trace-kernel-derived test produces `satisfied_independently`.
- The function does not modify the caller's context (uses `ctx.clone()` internally).
- `orbit_space_modes.py` Case 7 can be rewritten to use this function, producing a machine-classifiable verdict instead of a hand check.

### Notes

The four-way classification is the substantive content of this feature. The rest is infrastructure. Resist the urge to add a fifth classification ("partially satisfied" or similar) without a concrete use case.

The feature inherits the leak detector's limitations. If the metric definition encodes the target in a form not present in `equivalent_forms`, the leak will be missed. Document this clearly. A future milestone could extend the equivalent-forms list as new patterns are observed; that is not part of this milestone.

## Milestone 49: ProjectArchive Storage Layer

### Goal

Implement the on-disk storage layer for derivation records and dependency declarations.

This is the first of several milestones for the archive feature, which is the largest of the four features. The archive is decomposed into milestones because each layer (storage, recording, verification, invalidation, CLI) can be tested independently.

### Deliverables

- New module at `src/vacuumforge/archive/`.
- `archive.py` with the `ProjectArchive` and `ScriptNamespace` classes (storage methods only, no verification logic).
- `records.py` with `DerivationRecord`, `DependencyDeclaration`, and `DependencyCheckResult` dataclasses.
- `serialization.py` with sympy-to-JSON and JSON-to-sympy round-trip functions.
- The directory layout described in the technical design (`.vacuumforge_archive/<script_id>/derivations/*.json`, etc.).
- Atomic-write logic using `os.rename`.
- Tests covering: round-trip serialization for common sympy expression types, record-and-retrieve, atomic-write integrity.

### Required Capabilities

The user can record a derivation:

```python
archive = ProjectArchive(pathlib.Path(".vacuumforge_archive"))
ns = archive.script_namespace("my_script")
ns.record_derivation(
    derivation_id="kappa_zero_from_trace_kernel",
    inputs=[J_kappa, J_sigma],
    output=sympy.Eq(kappa, 0),
    method="energy_equilibrium",
    status=Status.DERIVED,
)
```

The derivation is written to `.vacuumforge_archive/my_script/derivations/kappa_zero_from_trace_kernel.json`.

The user can retrieve it:

```python
record = ns.get_derivation("kappa_zero_from_trace_kernel")
assert check_equal(record.output, sympy.Eq(kappa, 0))
```

### Completion Criteria

- All sympy expression classes used in Group 01 round-trip through serialization (Symbol, Integer, Rational, Add, Mul, Pow, exp, log, Eq, Derivative, Function).
- Round-trip tests assert `check_equal` (algebraic equivalence), not structural identity.
- Atomic writes are used for all file operations.
- Records can be retrieved after being written and after the process restarts.
- The existing VacuumForge test suite still passes.

### Notes

The choice of JSON over pickle is deliberate. JSON files are diff-friendly and can be checked into version control. Pickle is faster but produces opaque files that cannot be reviewed. For a tool whose value is auditability, JSON wins.

`sympy.srepr` is the right serialization function for most expressions, but it has known issues with custom Symbol assumptions. The serialization tests must specifically verify that Symbols with `positive=True`, `real=True`, and similar assumptions round-trip correctly. If they do not, the serialization layer needs supplementary handling.

This milestone produces a working storage layer with no semantic content. Verification logic comes in Milestone 50.

## Milestone 50: ProjectArchive Verification and Invalidation

### Goal

Implement dependency verification and source-change invalidation.

This is the milestone where the archive becomes useful. Without verification, recorded entries are write-only data.

### Deliverables

- `ScriptNamespace.declare_dependency()` writing to `dependencies.json`.
- `ScriptNamespace.verify_dependencies(ctx)` returning a list of `DependencyCheckResult`.
- The four verification statuses: `dependency_satisfied`, `dependency_changed`, `dependency_missing`, `dependency_cycle`.
- Source-hash invalidation: each script computes its source hash and the namespace clears entries on hash mismatch.
- Tests for each status: matching dependency, modified upstream, missing upstream, cyclic dependency, source change.

### Required Capabilities

The user can declare a dependency:

```python
ns_b = archive.script_namespace("script_b")
ns_b.declare_dependency(
    dependency_id="uses_kappa_zero_derivation",
    upstream_script_id="script_a",
    upstream_derivation_id="kappa_zero_from_trace_kernel",
    expected_output=sympy.Eq(kappa, 0),
)
```

The user can verify:

```python
results = ns_b.verify_dependencies(ctx)
for r in results:
    if r.status != "dependency_satisfied":
        raise RuntimeError(f"Dependency check failed: {r.message}")
```

When the upstream output changes, the next verification reports `dependency_changed`.

### Completion Criteria

- All four verification statuses are reachable from test inputs.
- Cycle detection works on a hand-crafted two-script cycle.
- Source-hash invalidation correctly clears entries when the script source changes.
- The end-to-end test runs two real Group 01 scripts in sequence with a declared dependency, and the dependency verifies cleanly.

### Notes

The `expected_output` field is the load-bearing one. Without it, verification reduces to existence checking, which catches missing entries but not changed ones. Strongly encourage users to declare expected outputs whenever possible.

Cycle detection should use NetworkX (which the existing `DependencyGraph` already depends on). Build a directed graph from the dependency declarations and run `networkx.is_directed_acyclic_graph`. Cycles are reported with the cycle path included in the message.

Source-hash invalidation is conservative — any change to the script source clears all derivation entries. This catches false negatives (stale entries surviving real changes) at the cost of false positives (clearing entries when the change does not affect derivations). The latter is cheap; the former is dangerous.

## Milestone 51: ProjectArchive CLI

### Goal

Provide a command-line interface for archive inspection and maintenance.

### Deliverables

- New CLI subcommand `vf archive` with subcommands: `list`, `verify`, `invalidate`, `doctor`.
- `vf archive list <script_id>` showing all derivations and dependencies for a script.
- `vf archive verify <script_id>` running dependency verification and printing results.
- `vf archive invalidate <script_id>` clearing a script's archive entries.
- `vf archive doctor` scanning the archive for corruption and reporting issues.
- Tests for each subcommand on a populated test archive.

### Required Capabilities

The CLI commands described in the technical design all work as documented:

```bash
$ vf archive list candidate_log_scale_modes_test
Derivations (2): ...
$ vf archive verify candidate_covariant_parent_modes
Checking 2 dependencies... ...
$ vf archive doctor
Scanning archive for inconsistencies... ...
```

### Completion Criteria

- All four subcommands produce useful output on a populated archive.
- `vf archive doctor` correctly identifies a hand-crafted corrupted entry.
- The CLI integrates with the existing `vf` command structure (does not require a separate binary).
- Documentation for the new subcommands exists in the user-facing CLI reference.

### Notes

The CLI is the user's primary interface to the archive when something goes wrong. It should produce output that is actionable: not just "verification failed" but "dependency `X` expected output `Y` but found `Z`; re-run script `A` to update or run `vf archive invalidate A` to clear stale entries."

After this milestone, the archive feature is complete. The remaining work is documentation, examples, and ongoing maintenance discipline.

## Milestone 52: Documentation and Migration Guide

### Goal

Produce user-facing documentation for all four validation-hardening features and a migration guide for existing scripts.

### Deliverables

- A user guide for each feature in `docs/`.
- A migration guide for retrofitting existing scripts to use the new tools.
- Examples showing the same validation expressed three ways: raw sympy (current Group 01 style), VacuumForge-only (current v1/v2 style), and validation-hardened (using the new features).
- Updated overview document mentioning the new capabilities.
- Updated milestones document (this one) marked as complete or in-progress per milestone.

### Required Capabilities

A new contributor reading the documentation can:

- Run `vf-lint` on a candidate script and understand the output.
- Use `CoordinateChange` to register a radial reparameterization derivation.
- Use `ConcreteMetricCheck` to classify a known metric's relationship to target requirements.
- Use `ProjectArchive` to record derivations and declare dependencies (only if Milestones 49–51 were completed).

### Completion Criteria

- Each feature has at least one worked example in the documentation.
- The migration guide covers retrofitting at least one Group 01 script to the new API.
- The overview document is updated.
- All examples in the documentation actually run (verify with a documentation test).

### Notes

The migration guide is the most valuable single document. Users will be tempted to leave existing scripts as-is rather than refactor them, which means the new features only see use on new scripts. The migration guide should include explicit before-and-after examples and an honest assessment of when retrofitting is worthwhile (for scripts whose outputs are still load-bearing) and when it is not (for one-off explorations whose conclusions have already been absorbed).

## Implementation order and parallelism

The recommended order is: Milestones 41–44 (vf-lint), then Milestones 45–47 (CoordinateChange), then Milestone 48 (ConcreteMetricCheck), then Milestones 49–51 (ProjectArchive), then Milestone 52 (documentation).

Parallelism is possible:

- Milestones 41–44 (vf-lint) can be implemented entirely in parallel with the others, since vf-lint has no VacuumForge dependencies.
- Milestone 48 (ConcreteMetricCheck) can be implemented in parallel with Milestones 45–47 (CoordinateChange), since the two features touch disjoint VacuumForge modules.
- Milestones 49–51 (ProjectArchive) should be sequenced after CoordinateChange, since the archive's end-to-end test benefits from having `CoordinateChange`-produced derivations to record.

A team of two developers could complete the validation-hardening series in roughly three to four weeks. A single developer should expect five to seven weeks.

## Stop conditions

Each feature has a natural stop condition where further investment yields diminishing returns. The team should not feel obligated to complete the entire series.

- After Milestones 41–44 (vf-lint) and 45–47 (CoordinateChange): the minimum viable hardening. Most of the validation-discipline value is captured. This is the recommended stopping point if maintenance bandwidth is constrained.
- After Milestone 48 (ConcreteMetricCheck): adds Schwarzschild-style classification. Useful but optional.
- After Milestones 49–51 (ProjectArchive): adds cross-script dependency tracking. Useful only if the team commits to maintaining the archive as a load-bearing artifact. A neglected archive is worse than no archive.

The decision to build Milestones 49–51 should be revisited after Milestones 41–48 are in production use. If the team finds itself wishing for cross-script dependency tracking after using the other features, build the archive. If not, do not build it speculatively.

## Risks specific to the milestone schedule

The technical design identified four risks: feature creep, theatrical validation, maintenance burden, and design assumptions about VacuumForge internals. The milestone schedule introduces two additional risks specific to incremental delivery.

**Risk: a milestone produces working code that is never used.** vf-lint after Milestone 44 is fully functional, but if no one actually runs it on candidate scripts, the failure mode it was built to catch will recur. Mitigation: integrate vf-lint into the project's CI pipeline as part of Milestone 44, not as an afterthought.

**Risk: a half-completed feature becomes a permanent half-completed feature.** ProjectArchive after Milestone 49 has a working storage layer but no verification. If the team stops there, the archive becomes a write-only sink that gives the appearance of recording derivations without doing any validation. Mitigation: do not start Milestone 49 unless the team commits to completing at least Milestone 50. The storage layer alone has no value.

These risks suggest that the validation-hardening effort is not just a series of discrete milestones but a continuous discipline. The milestones provide structure, but the underlying commitment is to use the tools after they are built.
