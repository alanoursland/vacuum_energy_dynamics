# VacuumForge Usage Guide

## A Guide for Theory Developers

VacuumForge is a symbolic research workbench for developing, testing, comparing, and auditing candidate mathematical structures in a vacuum-based theory of gravity.

It is designed for theory developers who need to know not only whether a candidate structure produces a desired result, but how that result was obtained: derived, assumed, conditionally derived, failed, or still undetermined.

VacuumForge is especially focused on the equal-response problem: whether the reciprocal-scale relation

```math
A(r)B(r)=1
```

or equivalently

```math
\kappa = 0
```

can be derived from vacuum structure, exchange-source rules, and energy minimization rather than inserted as an assumption.

The purpose of this guide is to explain what VacuumForge can do, how to use it effectively, and how to avoid common theory-development mistakes.

---

## 1. What VacuumForge Is For

VacuumForge is useful when a proposed structure can be written symbolically.

It helps answer questions such as:

* Does this candidate model derive reciprocal scaling?
* Does it merely assume reciprocal scaling?
* Does exchange source the shear mode while leaving the conformal mode unsourced?
* Does creation source the conformal mode?
* Does a proposed energy functional make unsourced `kappa` relax to zero?
* Does the weak-field metric recover `gamma_v = 1`?
* Does the temporal sector recover `beta = 1`?
* Which assumptions were required for those results?
* Which candidate structures fail, and why?
* Which failures are useful counterexamples?

VacuumForge does not decide which theory is true. It makes the mathematical consequences of candidate structures explicit and inspectable.

The most important habit when using VacuumForge is this:

> Treat every result as a dependency question.

Do not ask only, "Did I get the desired result?" Ask, "What did I have to assume in order to get it?"

---

## 2. The Core Scientific Problem

The weak-field metric language uses two scale factors:

```math
A(r)=\sqrt{-g_{00}},
```

```math
B(r)=\sqrt{g_{ii}}.
```

The temporal response is constrained by redshift and time-dilation reasoning:

```math
A(r) \approx 1 + \frac{\Phi(r)}{c^2}.
```

The spatial response can be written as

```math
B(r) \approx 1 - \gamma_v\frac{\Phi(r)}{c^2}.
```

Observation requires

```math
\gamma_v = 1.
```

In the preferred formulation, this is equivalent to reciprocal scaling:

```math
A(r)B(r)=1.
```

VacuumForge works with logarithmic variables

```math
a = \ln A,
```

```math
b = \ln B,
```

and mode variables

```math
\kappa = \frac{a+b}{2},
```

```math
\sigma = \frac{a-b}{2}.
```

In this representation, reciprocal scaling becomes the simple condition

```math
\kappa = 0.
```

The main theoretical goal is to show that static gravitational exchange sources `sigma` but not `kappa`:

```math
J_\kappa = 0,
```

```math
J_\sigma \neq 0.
```

If positive-energy dynamics then relax unsourced `kappa` to zero, reciprocal scaling follows.

---

## 3. Mental Model of the Workflow

A typical investigation follows this chain:

```text
candidate vacuum structure
-> induced source projection
-> source classification
-> energy functional or equilibrium rule
-> reciprocal scaling check
-> weak-field metric construction
-> PPN parameter extraction
-> validation report
-> model comparison
```

Not every project uses every step. Early explorations may only classify sources. Mature candidates may pass through the entire chain.

The validation-hardening features added in v2 sit at the seams where a research workflow can drift:

* `vf-lint`: are verdict scripts actually validation artifacts?
* `CoordinateChange`: are coordinate or gauge derivations tracked as derivations?
* `ConcreteMetricCheck`: does a known metric satisfy a target independently or by construction?
* `ProjectArchive`: do downstream scripts really depend on current upstream derivations?

Think of VacuumForge as a sequence of filters:

1. Can the structure be represented symbolically?
2. Does exchange induce `J_kappa = 0`?
3. Does creation induce `J_kappa != 0`?
4. Does unsourced `kappa` relax to zero?
5. Does this imply `AB = 1`?
6. Does the resulting metric recover `gamma_v = 1`?
7. Does the temporal sector recover `beta = 1`?
8. Which of these results were assumptions, and which were derived?

The dependency answer is as important as the algebraic answer.

---

## 4. Main Objects You Will Use

### `TheoryContext`

`TheoryContext` is the central workbench.

It holds the symbolic registry, assumptions, expressions, sources, energy functionals, requirements, reports, dependency graph, ledger, theorem candidates, and structure-search tools.

A typical session begins by creating a context:

```python
from vacuumforge import TheoryContext

ctx = TheoryContext("equal_response_candidate")
```

For equal-response work, initialize the standard algebraic variables:

```python
ctx.define_equal_response_algebraic_symbols()
```

This prepares the common symbols and relations involving `A`, `B`, `a`, `b`, `kappa`, `sigma`, `mu`, source symbols, `Phi`, `c`, `gamma_v`, and `beta`.

### Symbol Registry

Use the symbol registry when you need named constants, coordinates, functions, sources, or coefficients.

Examples:

```python
c = ctx.symbols.define_constant("c", positive=True)
r = ctx.symbols.define_coordinate("r", positive=True)
Ck = ctx.symbols.define_coefficient("C_kappa", positive=True)
S = ctx.symbols.define_source("S")
```

The registry is there so symbols remain inspectable. Avoid creating too many anonymous SymPy symbols outside the context unless you are doing temporary scratch work.

### Assumption Manager

Use assumptions for declared relations, definitions, boundary conditions, or provisional closures.

Examples:

```python
ctx.assumptions.add("A_exponential", Eq(A, exp(Phi/c**2)))
ctx.assumptions.add("B_reciprocal", Eq(B, 1/A))
```

Be careful: an assumption like `B = 1/A` directly inserts reciprocal scaling. VacuumForge can still use it, but it should be treated as assumed, not derived.

### Expression Store

Use expressions for named intermediate or final symbolic objects.

Examples:

```python
ctx.expressions.add("metric.g00", -A**2)
ctx.expressions.add("modes.mu", a + b)
```

### Source Manager

Use sources to represent how a candidate law excites temporal/spatial or trace/shear modes.

You can define sources in `a,b` form:

```python
ctx.sources.add_ab("candidate_exchange", Ja, Jb)
```

or directly in mode form:

```python
ctx.sources.add_modes("trace_free_exchange", J_kappa=0, J_sigma=Js)
```

A directly declared `J_kappa = 0` exchange source is useful as a control, but it should usually be considered assumed unless it was produced by upstream structure-search logic.

### Energy Manager

Use the energy system to test whether a candidate functional drives the desired equilibrium.

A simple algebraic source-coupled energy might have the form

```math
E = C_\kappa \kappa^2 + C_\sigma \sigma^2 - J_\kappa\kappa - J_\sigma\sigma.
```

VacuumForge can derive stationary conditions and check whether `J_kappa = 0` implies `kappa = 0`.

### Requirement Manager

The requirement system validates a context against target conditions.

Typical requirements include:

* reciprocal scaling
* `gamma_v = 1`
* `beta = 1`
* positive energy
* trace-free exchange

Run all active requirements with:

```python
results = ctx.requirements.validate_all(ctx)
```

The basic validation statuses are:

* `pass`
* `fail`
* `assumed`
* `undetermined`

Structure-level classifications such as derived, conditional, tautological, or failed are usually produced by `StructureSearch` or by explicit review of dependency chains and leak reports.

### Reports

Reports convert the symbolic context into human-readable output.

Examples:

```python
handle = ctx.reports.validation()
markdown = handle.to_markdown()
```

Reports are useful for research notes, debugging hidden assumptions, and preserving failure cases.

---

## 5. Recommended Workflow for a New Candidate Model

### Step 1: Name the candidate clearly

```python
ctx = TheoryContext("antisymmetric_exchange_projection")
ctx.define_equal_response_algebraic_symbols()
```

Good names are specific:

```text
reciprocal_exponential_control
parallel_scaling_failure
trace_free_exchange_minimization
mixed_source_nonzero_kappa
symmetric_antisymmetric_structure
```

### Step 2: Declare only the assumptions you truly intend

The most dangerous assumptions are target-equivalent assumptions:

```math
B = 1/A,
```

```math
AB = 1,
```

```math
a + b = 0,
```

```math
\kappa = 0,
```

```math
J_\kappa = 0.
```

These are allowed as controls. They are not acceptable if the point of the model is to derive them.

### Step 3: Define the candidate source or structure

For a direct source-level model:

```python
ctx.sources.add_ab("candidate_exchange", Ja, Jb)
classification = ctx.sources.classify("candidate_exchange")
```

For an upstream structure-level model, define pre-mode variables, a projection map, and source operators, then let `StructureSearch` compute induced `J_a`, `J_b`, `J_kappa`, and `J_sigma`.

### Step 4: Check exchange and creation separately

For static gravity, the desired result is:

```math
J_\kappa^{exchange}=0,
```

```math
J_\sigma^{exchange}\neq0.
```

For creation or expansion-like behavior:

```math
J_\kappa^{creation}\neq0.
```

### Step 5: Add an energy functional

The simplest useful form is a positive quadratic mode energy with source couplings:

```math
E = C_\kappa \kappa^2 + C_\sigma \sigma^2 - J_\kappa\kappa - J_\sigma\sigma.
```

This lets VacuumForge test whether unsourced `kappa` relaxes to zero.

### Step 6: Validate requirements

```python
results = ctx.requirements.validate_all(ctx)
```

Inspect not just pass or fail, but also leak reports, assumptions, and source provenance.

### Step 7: Generate a report

```python
handle = ctx.reports.validation()
markdown = handle.to_markdown()
```

### Step 8: Compare against benchmark models

Useful controls and failures include:

* reciprocal exponential model
* parallel scaling failure
* free-gamma model
* assumed reciprocal model
* trace-free exchange minimization
* mixed-source nonzero-kappa model
* creation-source model

---

## 6. How to Use StructureSearch Effectively

`StructureSearch` is for exploring whether trace-free exchange follows from deeper mathematical structure.

Instead of starting with `J_kappa = 0`, start with:

```text
pre-mode variables q_i
projection map q_i -> (a,b)
exchange operator on q_i
creation operator on q_i
```

Then let VacuumForge compute the induced mode sources.

Core algebra:

```math
J_a = \sum_i \frac{\partial a}{\partial q_i}\delta q_i,
```

```math
J_b = \sum_i \frac{\partial b}{\partial q_i}\delta q_i,
```

```math
J_\kappa = J_a + J_b,
```

```math
J_\sigma = J_a - J_b.
```

A strong candidate makes `J_kappa = 0` for exchange as an identity while allowing creation to remain traceful.

Interpret results carefully:

* structurally trace-free
* conditionally trace-free
* tautological
* failed
* undetermined

`StructureSearch` is documented in more detail in [structure_search_guide.md](/E:/Projects/vacuum_energy_dynamics/vacuum_forge/docs/structure_search_guide.md).

---

## 7. Validation-Hardening Features

These features were added to harden the research workflow around real failure modes that occur outside the core symbolic algebra.

### `vf-lint`

`vf-lint` is a standalone AST linter for scripts that emit verdict-style output.

Use it before trusting a script that prints PASS, FAIL, CLOSED, DERIVED, or similar verdicts:

```bash
python -m tools.vf_lint script.py
```

or, if installed:

```bash
vf-lint script.py
```

It looks for three patterns:

* `print("[PASS] ...")` or similar output
* `status_line(...)` verdict helpers
* dataclass-style or constructor-style `status="PASS"` literals

It then traces back through imports, calls, and simple assignment chains to decide whether the verdict is gated on real `sympy` or `vacuumforge` computation.

Interpret the result as:

* `OK`: verdict sites are gated on real computation
* `WARN`: verdict sites exist, but some are unconditional or gated on literals
* `FAIL`: hardcoded verdict structure; do not treat the script as a validation artifact

If you use local rule overrides, keep them in an untracked `vf_lint.toml`.

### `CoordinateChange`

Use `CoordinateChange` when a derivation depends on radial reparameterization or gauge-form comparison and you want the transformation itself tracked in the dependency graph.

Example:

```python
import sympy as sp
from vacuumforge import TheoryContext
from vacuumforge.coordinates import CoordinateChange, validate_coordinate_invariance

ctx = TheoryContext("radial_reparam")
r, R, lam = sp.symbols("r R lambda", positive=True)
change = CoordinateChange(old_coord=r, new_coord=R, transform=lam * R)
change.register(ctx, "radial_reparameterization")
```

Then transform the relevant quantities:

```python
A_R = change.transform_scale_factor(A_r, "temporal")
B_R = change.transform_scale_factor(B_r, "radial")
a_R, b_R = change.transform_log_modes(a_r, b_r)
metric_R = change.transform_metric(metric_r)
```

The current validation-hardening implementation follows the convention used in the v2 work:

* radial scale factors transform with `(df/dR)^2`
* radial log modes pick up `2 * log(f')`

If a script claims that a quantity is invariant or not invariant under the transformation, use the validator instead of leaving the claim as prose:

```python
result = validate_coordinate_invariance(ctx, "kappa_invariance", kappa_expr, change)
```

### `ConcreteMetricCheck`

Use `ConcreteMetricCheck` when you substitute a fully specified metric or ansatz and want honest vocabulary about what the check means.

```python
from vacuumforge.metric.concrete_check import check_concrete_metric

results = check_concrete_metric(
    ctx,
    A_value=A_known,
    B_value=B_known,
    requirement_ids=["reciprocal_scaling", "gamma_v_one"],
)
```

Each result is classified as:

* `satisfied_independently`
* `satisfied_by_construction`
* `failed`
* `undetermined`

This distinction matters. A known metric may satisfy a target, but that does not mean the target was derived from deeper structure.

Use the additional fields when you need the raw details:

* `leak_report`
* `underlying_validation`

### `ProjectArchive`

Use `ProjectArchive` when later scripts depend on earlier derivations and you want that continuity checked mechanically.

Example:

```python
import sympy as sp
from vacuumforge import ProjectArchive, Status

archive = ProjectArchive(".vacuumforge_archive")
ns = archive.script_namespace("candidate_log_scale_modes_test")

ns.record_derivation(
    derivation_id="trace_kernel_condition",
    inputs=[sp.Symbol("J_kappa")],
    output=sp.Eq(sp.Symbol("J_kappa"), 0),
    method="algebraic",
    status=Status.DERIVED,
)
```

Downstream:

```python
dep_ns = archive.script_namespace("candidate_covariant_parent_modes")
dep_ns.declare_dependency(
    dependency_id="uses_trace_kernel_condition",
    upstream_script_id="candidate_log_scale_modes_test",
    upstream_derivation_id="trace_kernel_condition",
    expected_output=sp.Eq(sp.Symbol("J_kappa"), 0),
)

results = dep_ns.verify_dependencies()
```

Operational guidance:

* record derivations every run
* verify dependencies before trusting downstream verdicts
* use source-hash invalidation when scripts change
* treat dependency failures as real failures

The CLI mirrors that workflow:

```bash
vacuumforge archive list SCRIPT_ID
vacuumforge archive verify SCRIPT_ID
vacuumforge archive invalidate SCRIPT_ID
vacuumforge archive doctor
```

---

## 8. Common Candidate Families

Useful model families include:

* reciprocal exponential control
* parallel scaling failure
* free-gamma model
* assumed trace-free exchange
* mixed-source failure
* pure-trace creation model

These are useful because they force you to separate control models, genuine candidates, and counterexamples.

---

## 9. Interpreting Results Honestly

### `pass`

The requirement appears satisfied under the active model and assumptions.

### `assumed`

The result is present directly or through a target-equivalent assumption.

### `fail`

The requirement does not hold or produces a nonzero residual.

### `undetermined`

VacuumForge could not decide under the current assumptions or simplification rules.

### Structure-level statuses

For `StructureSearch` and some validation-hardening workflows, also think in terms of:

* derived
* conditional
* tautological
* satisfied by construction

Those distinctions are often the real scientific content.

---

## 10. How to Avoid Fooling Yourself

### Do not assume the target result unless you are building a control

Target-equivalent assumptions include:

```math
AB = 1,
```

```math
B = 1/A,
```

```math
a+b=0,
```

```math
\mu=0,
```

```math
\kappa=0,
```

```math
J_\kappa=0.
```

### Check exact and perturbative results separately

`gamma_v = 1` is a first-order spatial metric result. `beta = 1` depends on second-order temporal structure. Do not collapse them into one success criterion.

### Separate source selection from energy relaxation

Energy minimization can show that unsourced `kappa` relaxes to zero.

It does not explain why exchange leaves `kappa` unsourced. That is a source-selection problem.

### Treat mismatch energy carefully

A mismatch penalty may be useful, but it may also just encode the target.

### Preserve failures

Do not delete failed candidates. They often become regression tests, counterexamples, or evidence for a missing principle.

### Use the hardening tools where they belong

If a script emits verdicts, run `vf-lint`.

If a claim depends on coordinate transformation, track it with `CoordinateChange`.

If a known metric is being checked, classify it with `ConcreteMetricCheck`.

If one script builds on another, verify that dependency through `ProjectArchive`.

---

## 11. Practical CLI Patterns

VacuumForge includes command-line workflows for common operations:

```bash
vacuumforge new model_name --out model.yaml
```

```bash
vacuumforge validate model.yaml
```

```bash
vacuumforge report model.yaml --out report.md
```

```bash
vacuumforge compare model_a.yaml model_b.yaml --out comparison.md
```

```bash
vacuumforge summary model.yaml
```

For archive-backed script chains:

```bash
vacuumforge archive list candidate_log_scale_modes_test
```

```bash
vacuumforge archive verify candidate_covariant_parent_modes
```

```bash
vacuumforge archive doctor
```

Use the CLI for repeatable checks and reports. Use notebooks or scripts for exploratory symbolic development.

---

## 12. Quick Checklist Before Trusting a Candidate

Ask:

* Did I assume `AB = 1`, `B = 1/A`, `a+b = 0`, `mu = 0`, or `kappa = 0`?
* Did I assume `J_kappa = 0` directly?
* If exchange is trace-free, was it derived from a projection or operator structure?
* Does creation remain traceful?
* Does the energy functional actually make unsourced `kappa` relax to zero?
* Are the results exact or merely perturbative?
* Does the model recover `gamma_v = 1`?
* Does it also recover or constrain `beta = 1`?
* If verdict scripts exist, does `vf-lint` classify them as real validation artifacts?
* If the derivation depends on coordinate transformation, is it tracked through `CoordinateChange`?
* If a known metric is being used, is it classified independently or by construction?
* If the script depends on earlier scripts, does `ProjectArchive` verify those dependencies cleanly?
* Is there a nearby counterexample?
* Is the result physically interpretable, not just algebraically convenient?

If any of these answers are unclear, the candidate should remain provisional.

---

## 13. Final Advice

Use VacuumForge like a suspicious collaborator.

Let it question every simplification, every target result, every source decomposition, and every assumption. The point is not to make candidate structures look successful. The point is to find out which ones survive explicit symbolic pressure.

The best session ends with one of three outcomes:

1. A result was genuinely derived.
2. A hidden assumption was exposed.
3. A failure revealed a sharper condition for the next model.

All three are progress.
