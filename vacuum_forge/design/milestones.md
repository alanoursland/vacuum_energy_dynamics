# VacuumForge Milestones

## Purpose

This document breaks the VacuumForge technical design into implementation milestones.

The milestones are organized by dependency and need. Each milestone should leave the software in a usable state, even if narrow. The goal is to build from a reliable symbolic core toward a full research workbench for the equal-response problem and, later, broader vacuum field-equation exploration.

VacuumForge should remain useful throughout development. Early milestones should already help answer simple symbolic questions such as:

```text
Does this model assume AB = 1 or derive it?
```

Later milestones should support richer candidate equation search, reporting, persistence, and field-equation exploration.

## Milestone 1: Project Skeleton and Core Context

### Goal

Create the basic Python package structure and the central `TheoryContext` object.

This milestone establishes the foundation on which all symbolic, reporting, and validation features depend.

### Deliverables

- Python package structure under `src/vacuumforge`.
- `pyproject.toml` with project metadata and dependencies.
- Basic test setup using `pytest`.
- Initial `TheoryContext` class.
- Core namespaces attached to the context:
  - symbols;
  - assumptions;
  - expressions;
  - ledger;
  - dependencies.
- Minimal documentation explaining how to create a context.

### Required Capabilities

The user can create a context:

```python
from vacuumforge import TheoryContext

ctx = TheoryContext("equal_response_demo")
```

The context can store a name, metadata, and empty registries.

The package can be imported and tested.

### Completion Criteria

- `pytest` runs successfully.
- `TheoryContext` can be instantiated.
- Context namespaces exist.
- A minimal smoke test passes.

### Notes

Do not implement symbolic physics yet. This milestone is infrastructure.

## Milestone 2: Symbol Registry

### Goal

Implement the symbolic variable registry.

VacuumForge needs a reliable way to define, inspect, and retrieve symbols, functions, constants, coordinates, coefficients, and sources.

### Deliverables

- `SymbolRecord`.
- `SymbolRegistry`.
- Methods for defining:
  - constants;
  - coordinates;
  - scalar symbols;
  - coefficients;
  - functions of coordinates;
  - source symbols.
- Assumption support for SymPy symbols, such as `positive=True`.
- Registry inspection methods.

### Required Capabilities

The user can define:

```python
c = ctx.symbols.define_constant("c", positive=True)
G = ctx.symbols.define_constant("G", positive=True)
M = ctx.symbols.define_constant("M", positive=True)
r = ctx.symbols.define_coordinate("r", positive=True)
Phi = ctx.symbols.define_function("Phi", args=[r])
```

The user can retrieve records by name.

The registry tracks:

- name;
- SymPy object;
- kind;
- assumptions;
- description;
- optional dimension tag;
- status.

### Completion Criteria

- Symbols and functions can be created and retrieved.
- Duplicate symbol names are handled intentionally.
- Tests cover constants, coordinates, functions, and assumptions.
- Registry display/summary works in plain text.

## Milestone 3: Assumptions and Expression Store

### Goal

Represent assumptions and named expressions explicitly.

This milestone prevents hidden assumptions from entering calculations without records.

### Deliverables

- `AssumptionRecord`.
- `AssumptionManager`.
- `ExpressionRecord`.
- `ExpressionStore`.
- Support for equality assumptions, inequalities, definitions, and substitution rules.
- Ability to apply active substitution assumptions to expressions.
- Status metadata on expressions and assumptions.

### Required Capabilities

The user can write:

```python
ctx.assumptions.add("A_exponential", Eq(A, exp(Phi/c**2)))
ctx.expressions.add("metric.g00", -A**2)
```

The system can apply substitution assumptions where appropriate.

The user can inspect active assumptions.

### Completion Criteria

- Assumptions can be added, listed, and removed.
- Named expressions can be stored and retrieved.
- Substitution from equality assumptions works.
- Tests cover assumption application and expression storage.
- No derivation result is produced without an expression record.

## Milestone 4: Dependency Graph and Ledger

### Goal

Track what each result depends on.

This milestone is central to VacuumForge’s honesty requirement: every result must know whether it depended on a postulate, assumption, definition, or candidate law.

### Deliverables

- Dependency graph using `networkx`.
- `DerivationRecord`.
- `LedgerEntry`.
- `TheoryLedger`.
- Methods to add entries with statuses:
  - definition;
  - postulate;
  - candidate postulate;
  - assumption;
  - target;
  - derived result;
  - provisional result;
  - failed derivation;
  - open question.
- Dependency query API.

### Required Capabilities

The user can ask:

```python
ctx.dependencies.of("result.gamma_v")
ctx.ledger.add_target("reciprocal_scaling", "AB = 1")
```

The graph records that an expression or result depends on specific assumptions or definitions.

### Completion Criteria

- Dependencies can be added and queried.
- Ledger entries can be created and updated.
- Tests verify dependency chains.
- Reports can list direct dependencies for a stored result, even before full report generation exists.

## Milestone 5: Standard Equal-Response Symbols

### Goal

Provide built-in helpers for the main variables used in the equal-response problem.

This is the first milestone where VacuumForge becomes recognizably useful for the theory.

### Deliverables

- Helper to define standard algebraic variables:
  - `A`, `B`;
  - `a`, `b`;
  - `kappa`, `sigma`;
  - `mu`;
  - `J_a`, `J_b`, `J_kappa`, `J_sigma`;
  - `gamma_v`, `beta`;
  - `Phi`, `c`.
- Helper to define standard field variables as functions of `r`.
- Built-in definitions:
  - `a = log(A)`;
  - `b = log(B)`;
  - `kappa = (a+b)/2`;
  - `sigma = (a-b)/2`;
  - `mu = a+b = 2*kappa`.

### Required Capabilities

The user can write:

```python
ctx.define_equal_response_algebraic_symbols()
```

and receive a ready-to-use symbolic context.

### Completion Criteria

- Standard variables are created consistently.
- Standard definitions are stored as expression records or assumptions.
- Tests verify all definitions.
- Both algebraic and radial-function modes are supported at least minimally.

## Milestone 6: Scale, Log, and Mode Transformations

### Goal

Implement transformations among scale-factor variables, logarithmic variables, and mode variables.

### Deliverables

- Transform engine.
- Rewrite methods:
  - `to_log`;
  - `to_scale`;
  - `to_modes`;
  - `from_modes`.
- Controlled simplification utilities for logs and exponentials.
- Tests for round-trip transformations.

### Required Capabilities

The software can transform:

```math
A=e^{\kappa+\sigma}
```

```math
B=e^{\kappa-\sigma}
```

and

```math
\kappa=\frac{\ln A+\ln B}{2}.
```

The user can take an expression in `A, B` and rewrite it in `kappa, sigma`.

### Completion Criteria

- `A*B` rewrites to `exp(2*kappa)`.
- `A/B` rewrites to `exp(2*sigma)`.
- `kappa=0` rewrites to `AB=1` where appropriate.
- Tests cover exact transformations and simplification behavior.

## Milestone 7: Reciprocal Scaling Checker

### Goal

Implement direct checks for reciprocal scaling and equivalent forms.

### Deliverables

- `ReciprocalScalingChecker`.
- Exact checks for:
  - `A*B = 1`;
  - `a+b = 0`;
  - `kappa = 0`;
  - `B = 1/A`;
  - `mu = 0`.
- Result classification:
  - pass;
  - fail;
  - assumed;
  - undetermined.
- Basic dependency integration.

### Required Capabilities

The user can ask:

```python
ctx.checks.reciprocal_scaling()
```

The checker should detect reciprocal scaling in multiple equivalent forms.

### Completion Criteria

- Reciprocal exponential model passes.
- Free-gamma model remains undetermined or fails unless gamma is set to one.
- Parallel scaling model fails.
- If `B = 1/A` is declared as an assumption, the result is marked as assumed, not derived.

## Milestone 8: Weak-Field Expansion Engine

### Goal

Support perturbative expansion in powers of `Phi/c^2`.

### Deliverables

- Weak-field expansion utility.
- Coefficient extraction by order.
- Exactness metadata for first-order and second-order results.
- Expansion parameter substitution using a dummy variable.
- Tests for exponential expansions.

### Required Capabilities

The user can expand:

```math
e^{2\Phi/c^2}
```

to second order.

The user can ask for the first-order coefficient of a metric expression.

### Completion Criteria

- `exp(Phi/c**2)` expands correctly.
- `exp(2*Phi/c**2)` expands correctly.
- Expansion order is recorded.
- Tests distinguish exact identity from first-order equality.

## Milestone 9: Weak-Field Metric Construction

### Goal

Construct weak-field metric components from scale factors.

### Deliverables

- `WeakFieldMetric`.
- Metric construction from `A` and `B`.
- Expressions:
  - `g00 = -A**2`;
  - `gij_factor = B**2`.
- Support for isotropic static weak-field coordinate scope.
- Stored metric expressions in context.

### Required Capabilities

The user can write:

```python
metric = ctx.metric.from_scale_factors(A, B)
```

and inspect:

```python
metric.g00
metric.gij_factor
```

### Completion Criteria

- Metric expressions are correct.
- Metric expressions can be expanded weak-field.
- Scope metadata is attached.
- Tests cover exponential and parameterized metrics.

## Milestone 10: PPN Parameter Extraction

### Goal

Extract `gamma_v` and `beta` from candidate metric expressions.

### Deliverables

- `PPNResult`.
- `extract_gamma`.
- `extract_beta`.
- Standard target metric forms.
- Comparison against `gamma_v = 1` and `beta = 1`.

### Required Capabilities

Given:

```math
A=e^{\Phi/c^2},\quad B=e^{-\lambda\Phi/c^2},
```

VacuumForge extracts:

```math
\gamma_v=\lambda.
```

Given:

```math
A=e^{\alpha\Phi/c^2},
```

VacuumForge extracts the corresponding second-order time coefficient and reports the implied `beta` under the active normalization.

### Completion Criteria

- Reciprocal exponential gives `gamma_v = 1`.
- Temporal exponential gives `beta = 1` when normalized to the framework’s redshift coefficient.
- Parameterized spatial exponential leaves `gamma_v` symbolic.
- Tests verify coefficient extraction and sign conventions.

## Milestone 11: Source Decomposition and Classification

### Goal

Represent source components and classify trace/shear content.

### Deliverables

- `SourceRecord`.
- Source decomposition:
  - from `J_a, J_b` to `J_kappa, J_sigma`;
  - from `J_kappa, J_sigma` to `J_a, J_b`.
- Source classifier:
  - trace-free;
  - pure trace;
  - mixed;
  - zero;
  - undetermined.
- Source summary display.

### Required Capabilities

The user can define:

```python
ctx.sources.add_ab("static_source", Ja, Jb)
ctx.sources.classify("static_source")
```

or:

```python
ctx.sources.add_modes("exchange", J_kappa=0, J_sigma=Js)
```

### Completion Criteria

- Trace-free source is identified correctly.
- Pure-trace source is identified correctly.
- Mixed source is identified correctly.
- Tests cover symbolic simplification and undetermined cases.

## Milestone 12: Exchange and Creation Source Models

### Goal

Add domain-specific helpers for exchange and creation source modeling.

### Deliverables

- Exchange source helpers:
  - assumed trace-free exchange;
  - general exchange with free trace component;
  - parameterized exchange source.
- Creation source helpers:
  - uniform creation;
  - localized creation profile;
  - pure-trace creation.
- Source metadata identifying whether trace-free behavior is assumed or derived.
- Initial exchange-creation separation validator.

### Required Capabilities

The user can create:

```python
exchange = ctx.sources.exchange_trace_free(J_sigma=Js)
creation = ctx.sources.creation_uniform(J_kappa=Jc)
```

The system can check whether the model satisfies the candidate separation principle.

### Completion Criteria

- Exchange source with `J_kappa=0` validates as trace-free but marked assumed if directly declared.
- General exchange source does not automatically validate.
- Creation source validates as traceful.
- Tests verify assumed versus derived classification where possible.

## Milestone 13: Energy Functional Core

### Goal

Represent algebraic energy functionals over modes.

### Deliverables

- `EnergyFunctional`.
- Energy builder for:
  - quadratic mode energy;
  - source-coupled quadratic energy;
  - mismatch energy.
- Store energy functionals in context.
- Inspect which variables and sources appear in an energy.

### Required Capabilities

The user can define:

```math
E=C_\kappa\kappa^2+C_\sigma\sigma^2-J_\kappa\kappa-J_\sigma\sigma.
```

The software records variables, coefficients, and dependencies.

### Completion Criteria

- Algebraic energy functionals can be created and retrieved.
- Variables are detected or supplied.
- Source couplings are identified.
- Tests cover common energy forms.

## Milestone 14: Energy Minimization

### Goal

Derive stationary conditions and solve simple algebraic equilibrium problems.

### Deliverables

- Partial derivative stationary equations.
- Algebraic solver for stationary points.
- Equilibrium result records.
- Detection of whether unsourced `kappa` minimizes to zero.
- Boundary-condition records for algebraic use.

### Required Capabilities

For

```math
E=C_\kappa\kappa^2+C_\sigma\sigma^2-J_\kappa\kappa-J_\sigma\sigma,
```

VacuumForge derives:

```math
\kappa=\frac{J_\kappa}{2C_\kappa},
```

```math
\sigma=\frac{J_\sigma}{2C_\sigma}.
```

Then, under `J_kappa=0`, it derives `kappa=0`.

### Completion Criteria

- Stationary conditions are correct.
- Solutions are stored with dependencies.
- `J_kappa=0 => kappa=0` is derived from the energy model and source assumption.
- If `J_kappa` is not zero, `kappa` does not falsely vanish.
- Tests cover sourced and unsourced modes.

## Milestone 15: Positivity Checks

### Goal

Check local quadratic positivity of candidate energy functionals.

### Deliverables

- Hessian-based positivity checker.
- Positive-definite, semidefinite, indefinite, and undetermined statuses.
- Coefficient condition reporting.
- Integration with validation requirements.

### Required Capabilities

For

```math
E=C_\kappa\kappa^2+C_\sigma\sigma^2,
```

with positive coefficients, VacuumForge reports positive energy.

For cross-coupled forms, it reports determinant conditions.

### Completion Criteria

- Quadratic positive forms are identified.
- Indefinite forms are flagged.
- Undetermined coefficient cases remain undetermined.
- Tests cover two-variable quadratic forms.

## Milestone 16: Requirement System

### Goal

Implement requirement-based validation.

### Deliverables

- `Requirement`.
- `ValidationResult`.
- Built-in requirements:
  - reciprocal scaling;
  - `kappa = 0`;
  - `gamma_v = 1`;
  - `beta = 1`;
  - trace-free exchange;
  - traceful creation;
  - positive energy;
  - unsourced kappa minimizes to zero;
  - nonzero sigma response.
- Validation engine.

### Required Capabilities

The user can define or load a standard requirement set and run:

```python
results = ctx.requirements.validate_all()
```

The report distinguishes:

- pass;
- fail;
- assumed;
- undetermined.

### Completion Criteria

- Requirements validate against current context.
- Built-in equal-response requirements work.
- Assumed target results are not mislabeled as derived.
- Tests cover pass/fail/assumed/undetermined statuses.

## Milestone 17: Target Library

### Goal

Create a library of target results and equivalent forms.

### Deliverables

Targets for:

- `A ≈ 1 + Phi/c^2`;
- `B ≈ 1 - Phi/c^2`;
- `AB = 1`;
- `kappa = 0`;
- `mu = 0`;
- `gamma_v = 1`;
- `beta = 1`;
- weak-field `g00`;
- weak-field `gij`.

Each target includes:

- expression;
- equivalent forms;
- description;
- status;
- exactness scope.

### Required Capabilities

The reciprocal scaling checker and leak detector can query the target library.

### Completion Criteria

- Targets can be listed and retrieved.
- Equivalent forms are recognized.
- Requirements can reference targets.
- Tests verify target equivalence for reciprocal scaling.

## Milestone 18: Assumption Leak Detection

### Goal

Detect when a target result has been inserted into assumptions or definitions.

### Deliverables

- Direct leak detection.
- Equivalent-form leak detection.
- Leak audit reports.
- Integration with validation statuses.

### Required Capabilities

If the user assumes:

```math
B=1/A
```

and then validates `AB=1`, VacuumForge reports:

```text
reciprocal scaling is assumed, not derived
```

If the user assumes:

```math
J_\kappa=0
```

VacuumForge reports trace-free exchange as assumed unless derived from deeper source equations.

### Completion Criteria

- Direct target assumptions are detected.
- Equivalent forms such as `a+b=0` and `kappa=0` are detected.
- Validation results downgrade from pass to assumed where appropriate.
- Tests cover common leak patterns.

## Milestone 19: Exact vs Perturbative Validation

### Goal

Make all checks explicit about order of validity.

### Deliverables

- `Exactness` metadata.
- Perturbative validation mode.
- First-order and second-order reciprocal checks.
- Exact versus perturbative report fields.

### Required Capabilities

The software can say:

```text
AB = 1 holds to first order but not second order.
```

or:

```text
AB = 1 holds exactly under this ansatz.
```

### Completion Criteria

- First-order checks do not claim exact proof.
- Second-order residuals are reported.
- Exact reciprocal exponential is recognized as exact.
- Tests cover exact, first-order-only, and failed cases.

## Milestone 20: Candidate Family Templates

### Goal

Provide reusable symbolic templates for common candidate structures.

### Deliverables

Templates for:

- reciprocal power family: `B=A^{-p}`;
- exponential scale family:
  - `A=exp(alpha Phi/c^2)`;
  - `B=exp(-lambda Phi/c^2)`;
- quadratic mode energy;
- source-coupled mode energy;
- mismatch energy;
- general exchange source with trace parameter.

### Required Capabilities

The user can instantiate a candidate family and immediately validate it.

### Completion Criteria

- Templates produce valid contexts or model objects.
- Standard validations can run on template outputs.
- Tests verify expected predictions for common parameter values.

## Milestone 21: Candidate Equation Search

### Goal

Search coefficient families for structures satisfying requirements.

### Deliverables

- `CandidateFamily`.
- Coefficient constraint solver.
- Candidate solution records.
- Requirement-driven search over algebraic families.
- Transparent constraint reporting.

### Required Capabilities

Given a family such as:

```math
E=c_1\kappa^2+c_2\sigma^2+c_3\kappa\sigma-J_\kappa\kappa-J_\sigma\sigma,
```

VacuumForge can derive conditions under which:

- energy is positive;
- unsourced kappa relaxes to zero;
- sigma responds to source;
- reciprocal scaling follows if trace-free exchange is present.

### Completion Criteria

- Search returns symbolic coefficient constraints.
- Search output explains why a candidate passes.
- Underdetermined searches are reported honestly.
- Tests cover simple coefficient-family searches.

## Milestone 22: Minimal Counterexample Tools

### Goal

Help test proposed derivations by constructing symbolic counterexamples.

### Deliverables

Counterexample templates for:

- “Postulate 2 forbids kappa”;
- “total energy exchange implies trace-free sourcing”;
- “local Lorentz invariance forces gamma_v = 1” in a simplified metric setting;
- “parallel scaling is observationally viable.”

### Required Capabilities

The user can generate a counterexample report showing why a proposed derivation does not close.

### Completion Criteria

- Counterexample for density-per-proper-volume with nonzero kappa and constant density works.
- Counterexample for total exchange with nonzero `J_kappa` works.
- Parallel scaling failure report shows `A/B=1`.
- Tests verify counterexample algebra.

## Milestone 23: Markdown Report Generation

### Goal

Generate human-readable reports for derivations, validations, failures, and model summaries.

### Deliverables

- Markdown report module.
- Jinja2 templates.
- LaTeX rendering helper.
- Report types:
  - derivation report;
  - validation report;
  - failure report;
  - model summary;
  - dependency report.

### Required Capabilities

The user can write:

```python
ctx.reports.validation().to_markdown("validation.md")
```

The report includes:

- assumptions;
- definitions;
- derived results;
- validation status;
- dependencies;
- leak audit;
- scope;
- exactness.

### Completion Criteria

- Reports are readable markdown.
- Equations render as LaTeX blocks.
- Validation reports include pass/fail/assumed/undetermined.
- Tests compare generated reports to expected structural content.

## Milestone 24: Failure Reports

### Goal

Make failed derivations useful.

### Deliverables

- `FailureReason`.
- Standard failure codes:
  - `KAPPA_SOURCED`;
  - `GAMMA_REMAINS_FREE`;
  - `POSITIVITY_UNDETERMINED`;
  - `TARGET_ASSUMED`;
  - `ONLY_FIRST_ORDER`;
  - `COORDINATE_SCOPE_LIMITED`;
  - `TRACE_FREE_NOT_DERIVED`.
- Failure report generation.

### Required Capabilities

When a model fails, VacuumForge explains the reason symbolically.

### Completion Criteria

- Failed reciprocal scaling reports why it failed.
- Free gamma reports gamma remains symbolic.
- Positivity ambiguity reports needed coefficient conditions.
- Tests cover failure code generation.

## Milestone 25: Persistence and Reproducible Sessions

### Goal

Save and load VacuumForge sessions.

### Deliverables

- YAML or JSON session serialization.
- SymPy expression serialization using `srepr` or equivalent.
- Session load/save API.
- Round-trip tests.
- Version metadata.

### Required Capabilities

The user can save a context:

```python
ctx.save("equal_response_session.yaml")
```

and reload it:

```python
ctx = TheoryContext.load("equal_response_session.yaml")
```

Validation results should be reproducible after loading.

### Completion Criteria

- Symbols, assumptions, expressions, sources, energy functionals, ledger entries, and dependencies survive round-trip.
- Tests cover save/load of a nontrivial equal-response model.
- Session files include VacuumForge version metadata.

## Milestone 26: Model Comparison

### Goal

Compare candidate structures side by side.

### Deliverables

- `ModelSummary`.
- `ModelComparison`.
- Comparison report.
- Standard comparison fields:
  - assumptions;
  - source classification;
  - reciprocal status;
  - `gamma_v`;
  - `beta`;
  - positivity status;
  - exchange-creation status;
  - failed requirements;
  - undetermined requirements.

### Required Capabilities

The user can compare:

- reciprocal exponential;
- free gamma;
- parallel scaling;
- trace-free exchange model;
- mixed-source model.

### Completion Criteria

- Comparison table is generated.
- Models are classified conservatively.
- Tests verify expected statuses for known models.

## Milestone 27: Model Status Classification

### Goal

Automatically classify candidate models by scientific status.

### Deliverables

Statuses such as:

- exploratory;
- algebraically consistent;
- derives equal-response;
- assumes equal-response;
- fails positivity;
- leaves gamma free;
- predicts wrong weak-field limit;
- requires new postulate;
- candidate for deeper development.

### Required Capabilities

The classifier uses validation results and leak audits.

### Completion Criteria

- Reciprocal scaling by assumption is classified as assumes equal-response.
- Trace-free exchange plus minimization can classify as derives equal-response only if trace-free source was derived, not assumed.
- Free gamma classified as leaves gamma free.
- Tests verify conservative classification.

## Milestone 28: Dimensional Checks

### Goal

Add lightweight dimensional validation.

### Deliverables

- Dimension tags in symbol registry.
- Dimension algebra for simple expressions.
- Checks for:
  - `Phi/c^2` dimensionless;
  - logs and exponentials have dimensionless arguments;
  - `gamma_v` and `beta` dimensionless;
  - basic energy expression consistency where possible.

### Required Capabilities

The user can run:

```python
ctx.dimensions.check(Phi/c**2)
```

and receive a dimensionless result.

### Completion Criteria

- Dimensionless weak-field parameter is verified.
- Invalid exponential arguments are flagged.
- Tests cover simple dimensional expressions.

## Milestone 29: Notation Profiles and Sign Conventions

### Goal

Make sign and notation conventions explicit.

### Deliverables

- `NotationProfile`.
- Built-in profiles:
  - framework `Phi < 0` in wells;
  - PPN `U > 0`.
- Conversion relation `U = -Phi`.
- Report annotation of active notation profile.

### Required Capabilities

The user can switch or declare potential convention.

### Completion Criteria

- PPN extraction respects active convention or reports required convention.
- Reports state convention.
- Tests cover sign convention consistency.

## Milestone 30: Coordinate Scope Annotation

### Goal

Track the coordinate/gauge scope of results.

### Deliverables

- `ScopeRecord`.
- Built-in scopes:
  - PPN-compatible weak-field coordinates;
  - static spherical isotropic coordinates;
  - 2D time-space slice;
  - algebraic prototype.
- Scope metadata on expressions, validations, and reports.
- Scope warnings.

### Required Capabilities

A result derived in a 2D slice is not reported as a full 3+1 theorem.

### Completion Criteria

- Scope appears in validation results.
- Scope mismatch warnings work.
- Tests cover narrow-scope result used for broad requirement.

## Milestone 31: CLI Interface

### Goal

Provide a basic command-line interface.

### Deliverables

Commands:

```text
vacuumforge new SESSION_NAME
vacuumforge validate SESSION.yaml
vacuumforge report SESSION.yaml --out report.md
vacuumforge compare SESSION1.yaml SESSION2.yaml --out comparison.md
```

### Required Capabilities

Users can validate and report saved sessions without writing Python code.

### Completion Criteria

- CLI commands run.
- CLI output is readable.
- Tests or smoke tests cover CLI entry points.

## Milestone 32: Notebook-Friendly Display

### Goal

Improve interactive research use in notebooks.

### Deliverables

- Pretty display helpers.
- Summary tables.
- LaTeX display helpers.
- Validation result display.

### Required Capabilities

The user can call:

```python
ctx.display.ledger()
ctx.display.assumptions()
ctx.display.validation_results(results)
```

### Completion Criteria

- Notebook displays are readable.
- Plain terminal fallback works.
- No core functionality depends on notebook display.

## Milestone 33: Euler-Lagrange Field Support

### Goal

Extend energy functional analysis from algebraic mode models to simple field models.

### Deliverables

- Radial field density support.
- Euler-Lagrange equation derivation for fields depending on one coordinate.
- Support for gradient terms:
  - `(diff(kappa(r), r))**2`;
  - `(diff(sigma(r), r))**2`.
- Boundary-condition records included in field reports.

### Required Capabilities

Given a density:

```math
\mathcal{L}=K_\kappa(\kappa')^2+C_\kappa\kappa^2-J_\kappa\kappa,
```

VacuumForge derives the corresponding symbolic Euler-Lagrange equation.

### Completion Criteria

- Euler-Lagrange equations are correct for simple radial fields.
- Source-free positive massive field shows relaxation structure symbolically.
- Tests cover one-field and two-field densities.

## Milestone 34: 3+1 Generalization Foundations

### Goal

Prepare for higher-dimensional trace and shear decompositions.

### Deliverables

- General variable-list mode decomposition utilities.
- Support for one time log variable and multiple spatial log variables.
- Basic trace and trace-free decomposition in higher-dimensional linearized mode space.
- 3+1 scope marker.

### Required Capabilities

The user can define:

```math
a,\quad b_1,\quad b_2,\quad b_3
```

and compute total trace and trace-free components.

### Completion Criteria

- 2D system remains unchanged.
- 3+1 prototype decomposition works.
- Reports warn that 3+1 physics is experimental.
- Tests cover trace decomposition algebra.

## Milestone 35: Theorem Candidate System

### Goal

Support promotion of repeated symbolic results into theorem candidates.

### Deliverables

- `TheoremCandidate`.
- Supporting result links.
- Known counterexample links.
- Scope and assumption tracking.
- Report export.

### Required Capabilities

The user can create:

```text
Theorem candidate: Local exchange is trace-free.
```

with supporting models and counterexamples.

### Completion Criteria

- Theorem candidates can be created and inspected.
- Dependencies and counterexamples are linked.
- Reports summarize theorem candidate status.

## Milestone 36: Standard Equal-Response Workbench

### Goal

Package the main equal-response investigation into a ready-to-use workbench.

### Deliverables

- Prebuilt context template for the equal-response problem.
- Standard targets loaded.
- Standard requirements loaded.
- Common candidate families available.
- Common reports available.
- Example notebooks or scripts.

### Required Capabilities

The user can run:

```python
ctx = vacuumforge.workbenches.equal_response()
```

and immediately explore:

- reciprocal scaling;
- trace-free exchange;
- mismatch energy;
- gamma extraction;
- beta extraction;
- assumption leak audit.

### Completion Criteria

- The workbench can reproduce the known core examples:
  - reciprocal exponential;
  - parallel scaling failure;
  - free gamma;
  - trace-free exchange plus quadratic energy.
- Documentation explains the workflow.
- Tests cover workbench creation and standard validations.

## Milestone 37: Documentation Set

### Goal

Produce usable documentation for researchers and future developers.

### Deliverables

- User guide.
- API guide.
- Equal-response tutorial.
- Candidate model tutorial.
- Reporting tutorial.
- Developer architecture notes.
- Glossary of theory variables.

### Required Capabilities

A new user can understand how to:

- create a context;
- define variables;
- declare assumptions;
- build a metric;
- extract `gamma_v` and `beta`;
- validate reciprocal scaling;
- generate a report.

### Completion Criteria

- Documentation examples run successfully.
- Glossary includes all major symbols.
- Docs distinguish scientific concepts from software implementation.

## Milestone 38: Quality Hardening

### Goal

Make the software reliable enough for serious theory work.

### Deliverables

- Expanded test coverage.
- Regression tests for symbolic simplification issues.
- Type hints across core modules.
- Static checking with `mypy` or `pyright`.
- Formatting with `ruff` or equivalent.
- Error messages improved.
- Performance review of common operations.

### Required Capabilities

The system should fail clearly and conservatively when it cannot prove something.

### Completion Criteria

- Tests cover all core modules.
- Type checking passes for core modules.
- Known symbolic edge cases are documented.
- Ambiguous results are reported as undetermined rather than incorrectly passing or failing.

## Milestone 39: Research Examples Library

### Goal

Provide a library of example models that demonstrate the tool’s value.

### Deliverables

Example sessions for:

- reciprocal exponential scaling;
- parallel scaling failure;
- free gamma metric;
- mismatch energy with assumed penalty;
- trace-free exchange plus minimization;
- mixed source showing nonzero kappa;
- creation source exciting kappa;
- counterexample to “exchange implies trace-free”;
- counterexample to “density constancy forbids kappa.”

### Required Capabilities

Each example produces a validation report.

### Completion Criteria

- Examples run reproducibly.
- Reports are generated.
- Each example has a short explanation of what it demonstrates.

## Milestone 40: Release Candidate

### Goal

Prepare VacuumForge for first real use as a research tool.

### Deliverables

- Stable Python API for core workflows.
- CLI for validation and reports.
- Documentation and examples.
- Test suite.
- Versioned release.
- Known limitations document.

### Required Capabilities

The tool can support actual framework research on the equal-response problem.

The user can:

1. define candidate source laws;
2. define energy functionals;
3. derive stationary conditions;
4. check reciprocal scaling;
5. extract `gamma_v` and `beta`;
6. detect assumption leaks;
7. generate markdown reports;
8. compare candidate models;
9. save and reload sessions.

### Completion Criteria

- Standard equal-response workbench is usable end-to-end.
- Known examples produce expected reports.
- Documentation is sufficient for self-use.
- The software can answer the core audit question:

```text
Did this model derive kappa = 0, or did it assume it?
```

## Dependency Map

Some milestones depend strongly on earlier ones.

Core foundation:

```text
1 → 2 → 3 → 4
```

Equal-response algebra:

```text
5 → 6 → 7
```

Weak-field metric and PPN:

```text
8 → 9 → 10
```

Sources and exchange/creation:

```text
11 → 12
```

Energy and minimization:

```text
13 → 14 → 15
```

Validation and target auditing:

```text
16 → 17 → 18 → 19
```

Candidate exploration:

```text
20 → 21 → 22
```

Reports and reproducibility:

```text
23 → 24 → 25 → 26 → 27
```

Research hardening and future extension:

```text
28 → 29 → 30 → 31 → 32 → 33 → 34 → 35
```

End-to-end usability:

```text
36 → 37 → 38 → 39 → 40
```

## Recommended Build Order

The recommended order is the milestone order above. It builds from core infrastructure to symbolic algebra, then to validation, reporting, persistence, and higher-dimensional extensions.

The first major usable checkpoint is Milestone 10. At that point, VacuumForge can already define scale factors, construct weak-field metrics, and extract `gamma_v` and `beta`.

The second major usable checkpoint is Milestone 18. At that point, VacuumForge can distinguish derived reciprocal scaling from assumed reciprocal scaling.

The third major usable checkpoint is Milestone 24. At that point, VacuumForge can produce useful validation and failure reports.

The fourth major usable checkpoint is Milestone 36. At that point, VacuumForge becomes a coherent equal-response research workbench.

The first release candidate is Milestone 40.

## What Not to Delay

Several capabilities are important enough that they should not be postponed too far:

- dependency tracking;
- assumption leak detection;
- exact versus perturbative distinction;
- failure reporting;
- source classification.

These are not polish features. They are core to the scientific purpose of the tool.

VacuumForge is not just an algebra calculator. Its value is in preserving the distinction between assumption, derivation, failure, and open question.

## Summary

VacuumForge should be built in layers.

First, create the symbolic context and registries.

Second, implement the equal-response variable system.

Third, add reciprocal scaling, weak-field expansion, metric construction, and PPN extraction.

Fourth, add source modeling and energy minimization.

Fifth, add validation, target tracking, assumption leak detection, and reports.

Sixth, add persistence, comparison, counterexamples, and field-equation extensions.

The core question guiding every milestone is:

```text
Can this tool help determine whether kappa = 0 follows from the model, or was put in by hand?
```
