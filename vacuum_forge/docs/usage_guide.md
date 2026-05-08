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

VacuumForge is not intended to replace physical judgment. It does not decide which theory is true. It helps make the mathematical consequences of candidate structures explicit.

The most important habit when using VacuumForge is this:

> Treat every result as a dependency question.

Do not ask only, “Did I get the desired result?” Ask, “What did I have to assume in order to get it?”

---

## 2. The Core Scientific Problem

The weak-field metric language uses two scale factors:

```math
A(r)=\sqrt{-g_{00}},
```

```math
B(r)=\sqrt{g_{ii}}.
```

The temporal response is constrained by redshift/time-dilation reasoning:

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

VacuumForge works with logarithmic variables:

```math
a = \ln A,
```

```math
b = \ln B,
```

and mode variables:

```math
\kappa = \frac{a+b}{2},
```

```math
\sigma = \frac{a-b}{2}.
```

In this representation, reciprocal scaling becomes the simple condition:

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

## 3. Mental Model of the VacuumForge Pipeline

A typical VacuumForge investigation follows this chain:

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

Not every project uses every step. Early explorations may only classify sources. A more mature candidate may pass through the entire chain.

Think of VacuumForge as a sequence of filters:

1. Can the structure be represented symbolically?
2. Does exchange induce `J_kappa = 0`?
3. Does creation induce `J_kappa != 0`?
4. Does unsourced `kappa` relax to zero?
5. Does this imply `A B = 1`?
6. Does the resulting metric recover `gamma_v = 1`?
7. Does the temporal sector recover `beta = 1`?
8. Which of these results were assumptions, and which were derived?

The dependency answer is as important as the numerical or algebraic answer.

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

The registry is there so symbols remain inspectable. Do not create too many anonymous SymPy symbols outside the context unless you are doing temporary scratch work.

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

Named expressions make reports and dependency chains easier to inspect.

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

A directly declared `J_kappa = 0` exchange source is useful as a control, but it should usually be considered assumed unless it was produced by an upstream structure-search projection.

### Energy Manager

Use the energy system to test whether a candidate functional drives the desired equilibrium.

A simple algebraic source-coupled energy might have the form:

```math
E = C_\kappa \kappa^2 + C_\sigma \sigma^2 - J_\kappa\kappa - J_\sigma\sigma.
```

VacuumForge can derive stationary conditions and check whether `J_kappa = 0` implies `kappa = 0`.

### Requirement Manager

The requirement system validates a context against target conditions.

Typical requirements include:

* reciprocal scaling;
* `gamma_v = 1`;
* `beta = 1`;
* positive energy;
* trace-free exchange;
* traceful creation.

Run all active requirements with:

```python
results = ctx.requirements.validate_all()
```

The result statuses matter. A pass that depends on a target assumption is not the same as a derived pass.

### Reports

Reports convert the symbolic context into human-readable output.

Use them to create validation summaries, model summaries, and comparison material:

```python
report = ctx.reports.validation()
print(report.to_markdown())
```

Reports are especially useful for paper notes, research logs, and debugging hidden assumptions.

---

## 5. Recommended Workflow for a New Candidate Model

### Step 1: Name the candidate clearly

Start with a context whose name describes the idea being tested.

```python
ctx = TheoryContext("antisymmetric_exchange_projection")
ctx.define_equal_response_algebraic_symbols()
```

Good names help later comparison.

Prefer names like:

```text
reciprocal_exponential_control
parallel_scaling_failure
trace_free_exchange_minimization
mixed_source_nonzero_kappa
symmetric_antisymmetric_structure
```

Avoid vague names like:

```text
test1
new_thing
maybe_good
```

### Step 2: Declare only the assumptions you truly intend

Before adding assumptions, decide whether they are:

* definitions;
* provisional assumptions;
* physical postulates;
* candidate postulates;
* target results;
* boundary conditions;
* normalization choices.

The most common mistake is accidentally declaring the target result.

Dangerous assumptions include:

```math
B = 1/A,
```

```math
A B = 1,
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

These assumptions are allowed, but they must be interpreted correctly.

If you are using them as controls, label them as controls. If you are trying to prove them, do not insert them.

### Step 3: Define the candidate source or structure

For a direct source-level model, define the source components and classify them.

```python
ctx.sources.add_ab("candidate_exchange", Ja, Jb)
classification = ctx.sources.classify("candidate_exchange")
```

For an upstream structure-search model, define pre-mode variables, a projection map, and source operators. Then let `StructureSearch` compute induced `J_a`, `J_b`, `J_kappa`, and `J_sigma`.

This distinction is important:

```text
source-level model:
  assumes or proposes a source law directly

structure-level model:
  derives a mode-space source law from deeper variables and projection
```

The second is usually more valuable for the equal-response problem.

### Step 4: Check exchange and creation separately

A candidate should not merely make exchange trace-free. It should also preserve a meaningful distinction between exchange and creation.

For static gravity, the desired result is:

```math
J_\kappa^{exchange}=0,
```

```math
J_\sigma^{exchange}\neq0.
```

For creation or expansion-like behavior, the desired result is:

```math
J_\kappa^{creation}\neq0.
```

A structure that makes both exchange and creation trace-free may fail to distinguish the physical mechanisms.

A structure that makes exchange mixed, with nonzero `J_kappa`, usually fails the equal-response goal unless another mechanism cancels the trace mode.

### Step 5: Add an energy functional

Once source behavior is known, add a candidate energy functional.

The simplest useful form is a positive quadratic mode energy with source couplings:

```math
E = C_\kappa \kappa^2 + C_\sigma \sigma^2 - J_\kappa\kappa - J_\sigma\sigma.
```

This lets VacuumForge test whether unsourced `kappa` relaxes to zero.

If the model requires a mismatch term such as

```math
E_{mismatch} = C_\mu \mu^2,
```

be careful. A mismatch penalty may be useful, but it may also restate the reciprocal-scaling target rather than derive it from deeper structure.

### Step 6: Validate requirements

Run the standard validation set.

```python
results = ctx.requirements.validate_all()
```

Inspect not just pass/fail, but status and dependencies.

Useful statuses include:

```text
passed
failed
assumed
derived
conditional
undetermined
```

A result marked `assumed` may still be useful, but it has not solved the derivation problem.

### Step 7: Generate a report

Create a validation report for the research record.

```python
report = ctx.reports.validation()
markdown = report.to_markdown()
```

A good report should show:

* active assumptions;
* source classifications;
* energy functionals;
* validation results;
* failures;
* undetermined conditions;
* dependencies.

### Step 8: Compare against benchmark models

Compare the candidate against known controls and failures.

Useful benchmark classes include:

* reciprocal exponential model;
* parallel scaling failure;
* free-gamma model;
* assumed reciprocal model;
* trace-free exchange minimization;
* mixed source nonzero-kappa model;
* creation source model;
* counterexamples with nonzero trace.

The goal is not merely to find one working model. The goal is to understand the landscape of what works, what fails, and why.

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

### Core idea

Given variables

```math
q_1, q_2, \ldots, q_n,
```

and projection

```math
a = f_a(q_1,\ldots,q_n),
```

```math
b = f_b(q_1,\ldots,q_n),
```

an operator

```math
\delta q_i
```

induces

```math
J_a = \sum_i \frac{\partial a}{\partial q_i}\delta q_i,
```

```math
J_b = \sum_i \frac{\partial b}{\partial q_i}\delta q_i.
```

Then

```math
J_\kappa = J_a + J_b,
```

```math
J_\sigma = J_a - J_b.
```

A strong candidate structure makes `J_kappa = 0` for exchange as an identity, while allowing creation to be traceful.

### Good StructureSearch questions

Ask questions like:

* Does this projection make antisymmetric exchange trace-free?
* Is trace-free behavior automatic or conditional?
* What coefficient constraints are required?
* Does creation remain traceful?
* Is this merely the direct mode basis in disguise?
* Does this structure leak source terms into `kappa`?
* Does it produce a useful counterexample?

### How to interpret StructureSearch results

A result can fall into several categories.

#### Structurally trace-free

Exchange produces

```math
J_\kappa = 0
```

without extra assumptions.

This is the best case.

#### Conditionally trace-free

Exchange produces

```math
J_\kappa = 0
```

only if coefficient constraints are imposed.

Example:

```math
J_\kappa = (\alpha + \beta)S
```

requires

```math
\alpha + \beta = 0.
```

This is not a failure. It may reveal a candidate symmetry or conservation law.

#### Tautological

The structure is just the desired mode split written in another basis.

This can be useful as a control, but it does not explain equal response deeply.

#### Failed

Exchange generically sources `kappa`.

This is still useful. It may become a counterexample or show which assumptions are necessary.

#### Undetermined

SymPy simplification or symbolic solving cannot decide.

Undetermined is not the same as failure. It means the structure needs more assumptions, simplification rules, or mathematical analysis.

---

## 7. Common Candidate Families

### Reciprocal exponential control

Assume:

```math
A = e^{\Phi/c^2},
```

```math
B = e^{-\Phi/c^2}.
```

Then

```math
A B = 1.
```

This recovers the target behavior, but it should usually be treated as a control because reciprocal scaling is built in.

Use it to verify sign conventions, weak-field expansion, and PPN extraction.

### Parallel scaling failure

Assume:

```math
A = e^{\Phi/c^2},
```

```math
B = e^{\Phi/c^2}.
```

Then

```math
A B \neq 1.
```

This is a useful failure case. It shows that temporal and spatial scale factors cannot simply respond in parallel if the goal is reciprocal scaling.

### Free-gamma model

Use a parameterized spatial response:

```math
B = e^{-\lambda \Phi/c^2}.
```

Then VacuumForge should extract

```math
\gamma_v = \lambda.
```

This model is useful for checking whether `gamma_v = 1` follows or remains free.

### Assumed trace-free exchange

Declare:

```math
J_\kappa = 0,
```

```math
J_\sigma = S.
```

This is useful for verifying the downstream chain:

```text
J_kappa = 0
-> kappa = 0
-> A B = 1
-> gamma_v = 1
```

But it does not explain why exchange is trace-free.

### Mixed source failure

Let exchange produce both trace and shear:

```math
J_\kappa \neq 0,
```

```math
J_\sigma \neq 0.
```

This tests whether the model incorrectly excites the conformal mode during static exchange.

### Creation source model

Use a pure trace source:

```math
J_\kappa = C,
```

```math
J_\sigma = 0.
```

This is useful for distinguishing static gravitational exchange from expansion-like creation.

---

## 8. Interpreting Validation Results

### `passed`

The requirement appears satisfied under the active model and assumptions.

Always inspect dependencies before celebrating.

### `derived`

The result followed from prior structure rather than being directly assumed.

This is the most valuable status for theory development.

### `assumed`

The result was explicitly inserted or depended directly on a target-equivalent assumption.

This is not bad for a control model, but it does not solve the derivation problem.

### `conditional`

The result holds if certain coefficient constraints, symmetries, or side conditions are imposed.

Conditional results are often valuable. They may point toward deeper principles.

### `failed`

The model contradicts the requirement or produces a nonzero residual.

Failures are useful when recorded clearly.

### `undetermined`

VacuumForge could not decide.

This may happen because of symbolic complexity, missing assumptions, insufficient simplification, or genuinely ambiguous structure.

Do not convert `undetermined` into `passed` by hand. Either refine the model or record the open question.

---

## 9. How to Avoid Fooling Yourself

### Do not assume the target result unless you are building a control

The target-equivalent assumptions are:

```math
A B = 1,
```

```math
B = 1/A,
```

```math
a+b=0,
```

```math
\kappa=0,
```

```math
\mu=0.
```

For source-level equal response, also beware:

```math
J_\kappa=0.
```

This may be the result you are trying to derive.

### Check exact and perturbative results separately

A relation may hold exactly, to first order, or to second order only under additional assumptions.

For example:

```math
\gamma_v = 1
```

is a first-order spatial metric result, while

```math
\beta = 1
```

depends on second-order temporal structure.

Do not treat first-order success as full weak-field recovery.

### Separate source selection from energy relaxation

Energy minimization can show that unsourced `kappa` relaxes to zero.

It does not by itself explain why exchange leaves `kappa` unsourced.

The deeper question is source selection:

```text
Why does static exchange imply J_kappa = 0?
```

Use `StructureSearch` for that question.

### Treat mismatch energy carefully

A mismatch energy term can force reciprocal scaling, but it may simply encode the desired result.

Ask:

* Why does this term exist?
* Is it derived from a deeper structure?
* Does it forbid creation-like trace behavior?
* Does it make reciprocal scaling an input rather than an output?

### Preserve failures

Do not delete failed candidates. Label them.

A failed candidate may become:

* a regression test;
* a counterexample;
* evidence for a missing principle;
* a boundary marker for viable structures.

A good failure report is a theory-development asset.

---

## 10. Good Research Patterns

### Pattern 1: Control, candidate, counterexample

For every major claim, maintain three model types:

```text
control model:
  known to pass because the desired behavior is inserted

candidate model:
  intended to derive the behavior

counterexample model:
  similar-looking but fails
```

This makes the claim sharper.

### Pattern 2: Assumption removal

Start with a working model, then remove assumptions one by one.

Ask which result breaks first.

This helps identify which assumption is actually carrying the derivation.

### Pattern 3: Minimal assumption search

Try to find the smallest assumption set that yields the target chain:

```text
trace-free exchange
-> kappa relaxation
-> reciprocal scaling
-> gamma_v = 1
```

The smaller and more physically interpretable the assumption set, the stronger the model.

### Pattern 4: Conditional result mining

When a model is conditional, do not discard it immediately.

Coefficient constraints like

```math
\alpha + \beta = 0
```

may indicate:

* antisymmetry;
* conservation;
* trace cancellation;
* a hidden projection symmetry;
* a deeper invariant.

Conditional results can become theorem candidates.

### Pattern 5: Failure atlas

Maintain a collection of failed models grouped by failure type:

```text
sources kappa
fails creation tracefulness
assumes reciprocal scaling
has indefinite energy
fails gamma_v
fails beta
only works perturbatively
requires unnatural coefficient tuning
```

A failure atlas prevents repeated dead ends.

---

## 11. Suggested Research Notebook Template

For each candidate, record the following.

### Candidate name

A short descriptive name.

### Motivation

What idea is being tested?

### Primitive variables

List scale variables, log variables, mode variables, or pre-mode variables.

### Projection map

If using `StructureSearch`, record how pre-mode variables map to `a` and `b`.

### Exchange operator

Record the proposed exchange source or pre-mode operator.

### Creation operator

Record the creation source or pre-mode operator.

### Energy functional

Record the proposed energy expression and coefficient assumptions.

### Target requirements

List which requirements the model is meant to satisfy.

### Validation results

Record pass/fail/assumed/derived/conditional/undetermined statuses.

### Dependency notes

Record which assumptions were used for key results.

### Failure or success interpretation

Explain what the result teaches about the theory.

### Next action

Examples:

```text
promote to theorem candidate
search nearby family
look for counterexample
remove target assumption
add creation test
check beta
try nonlinear projection
```

---

## 12. Example Investigation Sketch

Suppose you want to test whether an antisymmetric internal exchange variable can derive trace-free exchange.

Start by defining a candidate structure with two pre-mode variables:

```math
q_+,
```

```math
q_-.
```

Use projection:

```math
a = q_+ + q_-,
```

```math
b = q_+ - q_-.
```

Define exchange:

```math
\delta q_+ = 0,
```

```math
\delta q_- = S.
```

Define creation:

```math
\delta q_+ = C,
```

```math
\delta q_- = 0.
```

VacuumForge computes induced exchange:

```math
J_a = S,
```

```math
J_b = -S,
```

so

```math
J_\kappa = J_a + J_b = 0,
```

```math
J_\sigma = J_a - J_b = 2S.
```

Creation gives:

```math
J_a = C,
```

```math
J_b = C,
```

so

```math
J_\kappa = 2C,
```

```math
J_\sigma = 0.
```

This structure cleanly separates exchange and creation.

The next question is whether it is a deep derivation or just the direct `kappa/sigma` mode basis renamed. That is not a purely algebraic question. VacuumForge can expose the equivalence; the theory developer must decide whether the pre-mode interpretation adds genuine ontology.

---

## 13. Practical CLI Patterns

VacuumForge also includes command-line workflows for common operations.

Typical commands may include:

```bash
vacuumforge new model.yaml
```

```bash
vacuumforge validate model.yaml
```

```bash
vacuumforge report model.yaml
```

```bash
vacuumforge compare model_a.yaml model_b.yaml
```

```bash
vacuumforge summary model.yaml
```

Use the CLI for repeatable checks and reports. Use notebooks or scripts for exploratory symbolic development.

A good pattern is:

```text
notebook:
  explore and prototype

saved session:
  preserve candidate model

CLI validation:
  run repeatable checks

markdown report:
  record result in research notes
```

---

## 14. What VacuumForge Can and Cannot Tell You

### VacuumForge can tell you

* whether a symbolic relation simplifies to zero;
* whether a source decomposes into trace, shear, mixed, or zero components;
* whether a candidate energy has simple quadratic positivity;
* whether stationary conditions imply `kappa = 0` under a source assumption;
* whether reciprocal scaling follows exactly or perturbatively;
* whether weak-field metric coefficients imply `gamma_v` or `beta`;
* whether a result depends on an explicit assumption;
* whether a structure is a useful counterexample.

### VacuumForge cannot tell you by itself

* whether the physical ontology is correct;
* whether a symbolic candidate is the unique explanation;
* whether a coordinate convention is physically preferred;
* whether a conditional coefficient relation has a real physical basis;
* whether a mathematically viable structure is empirically true;
* whether an elegant-looking model is conceptually justified.

VacuumForge makes theory claims harder to hide and easier to test. It does not replace theory judgment.

---

## 15. Development Priorities for Theory Users

When extending VacuumForge, prioritize features that improve scientific honesty.

High-value improvements include:

1. Better dependency tracking.
2. Better assumed-versus-derived classification.
3. More structure-search families.
4. More counterexample generation.
5. More robust conditional solving.
6. Clearer report output.
7. Exact versus perturbative status tracking.
8. Better source-leak detection.
9. Better positivity-condition reporting.
10. Saved comparison tables across candidate models.

Avoid adding complexity that makes the system less inspectable. VacuumForge should remain a transparent symbolic workbench, not a black box.

---

## 16. Recommended Standards for Claims

When writing research notes based on VacuumForge, use precise claim labels.

### Strong claim

```text
This structure derives trace-free exchange as an algebraic identity under the stated primitive projection and operator definitions.
```

### Conditional claim

```text
This structure derives trace-free exchange if the coefficient constraint alpha + beta = 0 is imposed.
```

### Control claim

```text
This model recovers reciprocal scaling because B = 1/A was assumed. It is useful as a downstream validation control.
```

### Failure claim

```text
This model fails the equal-response requirement because exchange induces nonzero J_kappa.
```

### Undetermined claim

```text
VacuumForge could not determine whether J_kappa vanishes under the current assumptions. Additional simplification rules or structural constraints are needed.
```

Precise labels prevent accidental overclaiming.

---

## 17. The Most Important Use Case

The central use case is not merely recovering `gamma_v = 1`.

The central use case is determining whether the theory can earn this chain:

```text
local static exchange
-> structurally trace-free source
-> J_kappa = 0
-> positive unsourced kappa relaxes to zero
-> kappa = 0
-> A B = 1
-> gamma_v = 1
```

The strongest VacuumForge result would be a candidate vacuum structure where the first arrow is derived rather than assumed.

That is the equal-response wall.

VacuumForge exists to chip at that wall without losing track of which stones were actually removed and which were painted to look like openings.

---

## 18. Quick Checklist Before Trusting a Candidate

Before treating a candidate as promising, ask:

* Did I assume `AB = 1`, `B = 1/A`, `a+b=0`, `mu=0`, or `kappa=0`?
* Did I assume `J_kappa = 0` directly?
* If exchange is trace-free, was it derived from a projection/operator structure?
* Does creation remain traceful?
* Does the energy functional actually make unsourced `kappa` relax to zero?
* Is the energy positive or at least locally stable under stated coefficient conditions?
* Does the model recover `gamma_v = 1`?
* Does it also recover or constrain `beta = 1`?
* Are results exact or perturbative?
* Are there hidden sign convention issues?
* Are dependencies visible in the report?
* Is there a nearby counterexample?
* Is the result physically interpretable, not just algebraically convenient?

If the answer to any of these is unclear, the candidate should remain provisional.

---

## 19. Final Advice

Use VacuumForge like a suspicious collaborator.

Let it question every simplification, every target result, every source decomposition, and every assumption. The point is not to make candidate structures look successful. The point is to find out which ones survive explicit symbolic pressure.

The best VacuumForge session ends with one of three outcomes:

1. A result was genuinely derived.
2. A hidden assumption was exposed.
3. A failure revealed a sharper condition for the next model.

All three are progress.
