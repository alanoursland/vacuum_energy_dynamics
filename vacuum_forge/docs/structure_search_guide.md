# StructureSearch User Guide

## What StructureSearch Does

The existing VacuumForge pipeline verifies a conditional chain:

```text
J_kappa = 0  =>  kappa = 0  =>  A B = 1  =>  gamma_v = 1
```

That chain works, but it starts from an assumed source rule. The `structure_search` module addresses the harder upstream question:

```text
What mathematical structure makes local exchange produce J_kappa = 0
as a consequence, rather than as an imposed rule?
```

StructureSearch represents candidate vacuum configurations as **pre-mode variables** with a **projection map** into metric scale variables. It applies **exchange and creation operators**, computes induced mode sources via Jacobian projection, and classifies whether trace-free exchange is **derived**, **assumed**, **conditional**, **failed**, **tautological**, or **undetermined**.

When it derives trace-free exchange, it feeds the result into the existing VacuumForge pipeline for full downstream validation.

## Core Concepts

### Pre-Mode Variables

Pre-mode variables are the internal degrees of freedom of a candidate vacuum structure. They are not `a`, `b`, `kappa`, or `sigma` — they are deeper variables that *produce* metric response after projection.

Examples: `q_t, q_x` (temporal and spatial channels), `q_+, q_-` (symmetric and antisymmetric modes), or abstract `q_1, ..., q_n`.

### Projection Map

A projection map defines how pre-mode variables determine the log scale factors:

```math
a = f_a(q_1, ..., q_n)
```

```math
b = f_b(q_1, ..., q_n)
```

Both linear and nonlinear projections are supported. The module uses the Jacobian to compute induced sources.

### Source Operators

A source operator defines how a physical process (exchange or creation) changes the pre-mode variables:

```text
Exchange: delta q_t = S, delta q_x = -S   (antisymmetric)
Creation: delta q_t = C, delta q_x = C    (symmetric)
```

These pre-mode perturbations become metric sources only after projection.

### Induced Mode Sources

Given a projection map and a source operator, the module computes:

```math
J_a = sum_i (da/dq_i) * delta q_i
```

```math
J_b = sum_i (db/dq_i) * delta q_i
```

then decomposes:

```math
J_kappa = J_a + J_b
```

```math
J_sigma = J_a - J_b
```

and classifies the result.

### Status Categories

Every analysis result is classified into one of six statuses:

| Status | Meaning |
|---|---|
| **derived** | J_kappa = 0 follows structurally from the projection and operator. |
| **assumed** | J_kappa = 0 is present because it was directly imposed. |
| **conditional** | J_kappa = 0 follows only if coefficient constraints are satisfied. |
| **failed** | Exchange generically produces nonzero J_kappa. |
| **tautological** | The structure is a relabeling of (kappa, sigma) or directly zeroes the trace variable. |
| **undetermined** | The algebra cannot decide. |

## Tutorial: Five Structures in Five Minutes

This section walks through five candidate structures, from tautological control to genuine derivation to failure.

### Setup

```python
import sympy as sp
from vacuumforge import TheoryContext
from vacuumforge.structure_search import (
    VacuumStructure,
    ProjectionMap,
    SourceOperator,
    StructureAnalyzer,
)
from vacuumforge.structure_search.families import (
    direct_mode_basis,
    two_channel_exchange,
    general_linear_projection,
    conserved_volume_family,
    mixed_exchange_family,
)
```

### 1. Tautological Control (Direct Mode Basis)

This structure defines exchange as `delta kappa = 0` directly. It should be classified as tautological — trace-free exchange is assumed, not derived.

```python
structure = direct_mode_basis()
analyzer = StructureAnalyzer()
result = analyzer.analyze(structure)

print(result.summary_status)
# StructureStatus.TAUTOLOGICAL

print(result.leak_warnings)
# ['LEAK WARNING: Exchange operator explicitly zeroes all
#   trace-contributing variables. ...']
```

The module detects that the exchange operator explicitly assigns zero to the only variable that contributes to J_kappa. This is not a deep derivation.

**Why this matters:** Any structure that directly names kappa and sets its exchange perturbation to zero is restating the target. StructureSearch catches this.

### 2. Two-Channel Antisymmetric Exchange (The Minimal Nontrivial Model)

Two pre-mode channels `q_t` and `q_x` with a direct projection. Exchange is antisymmetric; creation is symmetric.

```python
structure = two_channel_exchange()
result = analyzer.analyze(structure)

print(result.summary_status)
# StructureStatus.DERIVED

print(result.derived_trace_free_exchange)
# True

print(result.derived_traceful_creation)
# True
```

Inspect the induced sources:

```python
ex = result.exchange_results[0]
print(f"J_kappa = {ex.J_kappa}")   # 0
print(f"J_sigma = {ex.J_sigma}")   # 2*S

cr = result.creation_results[0]
print(f"J_kappa = {cr.J_kappa}")   # 2*C
print(f"J_sigma = {cr.J_sigma}")   # 0
```

The structure derives trace-free exchange from antisymmetric channel exchange. It also derives traceful creation from symmetric channel creation. The remaining open question is:

```text
Why is local exchange antisymmetric in q_t, q_x?
```

The module names this as the new missing principle rather than hiding it.

### 3. General Linear Projection (Coefficient Constraint Discovery)

This family uses symbolic coefficients and lets the module solve for the conditions under which exchange is trace-free.

```python
structure = general_linear_projection(n_vars=2)
result = analyzer.analyze(structure)

print(result.summary_status)
# StructureStatus.CONDITIONAL

print(result.conditions)
# [Eq(alpha_1*e_1 + alpha_2*e_2 + beta_1*e_1 + beta_2*e_2, 0)]
# i.e., sum (alpha_i + beta_i) * e_i = 0
```

The module reveals that trace-free exchange is not automatic for a general linear projection. It requires a specific algebraic relationship between the projection coefficients and the exchange direction vector.

### 4. Conserved-Volume Family

Tests whether `delta(a+b) = 0` (volume conservation) produces trace-free exchange.

```python
structure = conserved_volume_family()
result = analyzer.analyze(structure)

print(result.summary_status)
# StructureStatus.DERIVED

print(result.derived_trace_free_exchange)
# True
```

This succeeds because the antisymmetric exchange operator `(S, -S)` conserves `a + b`. The question then becomes whether "conservation" is a physical principle or just a restatement.

### 5. Mixed Exchange (A Failure)

Exchange acts on only one channel. This should fail.

```python
structure = mixed_exchange_family()
result = analyzer.analyze(structure)

print(result.summary_status)
# StructureStatus.FAILED

print(result.failures)
# ["Exchange operator 'one_sided_exchange': mixed"]

ex = result.exchange_results[0]
print(f"J_kappa = {ex.J_kappa}")   # S
print(f"J_sigma = {ex.J_sigma}")   # S
```

The exchange sources both kappa and sigma. Reciprocal scaling cannot follow. This is a useful negative result — it shows that one-sided exchange is insufficient.

## Building Custom Structures

To test your own candidate structure, construct the three components manually.

### Step 1: Define Pre-Mode Variables

```python
u, v = sp.symbols("u v", real=True)
S, C = sp.symbols("S C")
```

### Step 2: Define a Projection Map

```python
projection = ProjectionMap(
    id="my_projection",
    variables=[u, v],
    a_expr=u + v,        # a = u + v
    b_expr=u - v,        # b = u - v
)
```

Check properties:

```python
print(projection.is_linear())
# True

print(projection.jacobian())
# Matrix([[1, 1], [1, -1]])
```

### Step 3: Define Source Operators

```python
exchange = SourceOperator(
    id="my_exchange",
    kind="exchange",
    deltas={u: S, v: -S},
    source_symbols=[S],
)

creation = SourceOperator(
    id="my_creation",
    kind="creation",
    deltas={u: C, v: C},
    source_symbols=[C],
)
```

### Step 4: Assemble the Structure

```python
structure = VacuumStructure(
    id="my_custom_structure",
    variables=[u, v],
    projection=projection,
    exchange_operators=[exchange],
    creation_operators=[creation],
    description="Custom test structure",
)
```

### Step 5: Analyze

```python
analyzer = StructureAnalyzer()
result = analyzer.analyze(structure)

print(result.summary())
```

### Nonlinear Projections

For nonlinear projections, the module uses Jacobian-based source computation automatically:

```python
q1, q2 = sp.symbols("q1 q2", positive=True)

projection = ProjectionMap(
    id="log_projection",
    variables=[q1, q2],
    a_expr=sp.log(q1 * q2),     # a = ln(q1 * q2)
    b_expr=sp.log(q1 / q2),     # b = ln(q1 / q2)
)

print(projection.is_linear())
# False

print(projection.jacobian())
# Matrix([[1/q1, 1/q2], [1/q1, -1/q2]])
```

## Using the Search Engine

The `StructureSearchEngine` is available directly on the `TheoryContext` as `ctx.structure_search`, or can be instantiated standalone.

### Single Structure Analysis

```python
ctx = TheoryContext("my_search")
ctx.define_equal_response_algebraic_symbols()

structure = two_channel_exchange()
result = ctx.structure_search.analyze(structure)

print(result.summary())
```

### Family Search with Coefficient Solving

```python
family = general_linear_projection(n_vars=2)
fam_result = ctx.structure_search.search_family(family)

print(fam_result.summary())
# Shows conditions required for trace-free exchange
```

### Sign-Pattern Enumeration

Exhaustively tests all 2D exchange sign patterns `{-1, 0, +1}`:

```python
fam_result = ctx.structure_search.enumerate_sign_patterns(n_vars=2)

print(f"Total tested: {fam_result.candidates_analyzed}")      # 8
print(f"Trace-free derived: {len(fam_result.trace_free_derived)}")  # 2
print(f"Failed: {len(fam_result.failed)}")                     # 6
```

Only the antisymmetric patterns `(+1, -1)` and `(-1, +1)` derive trace-free exchange. All others fail.

### Reviewing All Results

```python
print(ctx.structure_search.summary())
```

## Downstream Integration

When StructureSearch derives trace-free exchange, it can feed the result into the full VacuumForge pipeline. Pass the `TheoryContext` to the `analyze` call:

```python
ctx = TheoryContext("full_chain")
ms = ctx.define_equal_response_algebraic_symbols()

# Analyze structure with downstream integration
structure = two_channel_exchange()
result = ctx.structure_search.analyze(structure, ctx)

# A derived source is now registered in the context
source_id = f"derived_exchange_from_{structure.id}"
src = ctx.sources.get(source_id)
print(src.assumed_trace_free)  # False — it was derived, not assumed
```

You can then continue the standard VacuumForge workflow:

```python
# Define energy functional
ctx.energy.source_coupled(
    C_kappa=ms.C_kappa, C_sigma=ms.C_sigma,
    J_kappa=ms.J_kappa, J_sigma=ms.J_sigma,
    kappa=ms.kappa, sigma=ms.sigma,
)

# Solve with J_kappa = 0
sol = ctx.energy.solve_stationary(
    "source_coupled_energy",
    extra_subs={ms.J_kappa: 0},
)
print(sol.solutions[0][ms.kappa])  # 0

# Set up metric assumptions
ctx.assumptions.add("A_redshift", sp.Eq(ms.A, sp.exp(ms.Phi / ms.c**2)))
ctx.assumptions.add("B_reciprocal", sp.Eq(ms.B, 1 / ms.A))

# Check reciprocal scaling
check = ctx.checks.reciprocal_scaling()
print(check.status)  # "pass"

# Extract PPN parameters
A_val = ctx.assumptions.apply(ms.A)
B_val = ctx.assumptions.apply(ms.B)
metric = ctx.metric.from_scale_factors(A_val, B_val)

gamma = ctx.ppn.extract_gamma(metric)
beta = ctx.ppn.extract_beta(metric)
print(f"gamma_v = {gamma.value}")  # 1
print(f"beta = {beta.value}")      # 1
```

The full chain is:

```text
candidate structure
-> Jacobian projection
-> J_kappa = 0 (derived)
-> energy minimization: kappa = 0
-> reciprocal scaling: A B = 1
-> gamma_v = 1, beta = 1
```

## Generating Reports

```python
from vacuumforge.structure_search.reports import generate_structure_report

structure = two_channel_exchange()
analyzer = StructureAnalyzer()
result = analyzer.analyze(structure)

report = generate_structure_report(structure, result)

# Write to file
with open("structure_report.md", "w") as f:
    f.write(report)
```

The report includes:

- Pre-mode variables
- Projection map (with linearity check)
- Exchange and creation operators with their delta definitions
- Induced sources J_a, J_b, J_kappa, J_sigma for each operator
- Classification and status for each operator
- Conditions required (if conditional)
- Leak warnings (if tautological)
- Overall summary

## Understanding Leak Detection

StructureSearch applies three levels of leak detection to prevent disguised assumptions from being mislabeled as derivations.

### Level 1: Projection Enforces a + b = 0

If the projection map itself enforces `a + b = 0` (a constant), then reciprocal scaling is built into the projection. Any exchange operator would trivially produce `J_kappa = 0`.

### Level 2: Jacobian Sum Row Is Zero

If the sum of the Jacobian rows is the zero vector, then `a + b` is independent of all pre-mode variables. No source of any kind can change `a + b`, making `J_kappa = 0` structurally guaranteed for any operator.

### Level 3: Exchange Zeroes All Trace Contributors

The module computes which variables contribute to J_kappa through the Jacobian sum row. If the exchange operator explicitly sets `delta = 0` for every variable that contributes to J_kappa, trace-free exchange is assumed through the operator definition, not derived from deeper structure.

**Example:** The direct mode basis has projection `a = kappa + sigma`, `b = kappa - sigma`. The Jacobian sum row is `[2, 0]`. Only `kappa` contributes to J_kappa. The exchange operator sets `delta kappa = 0` directly. This is classified as **tautological**.

**Counter-example:** The two-channel basis has projection `a = q_t`, `b = q_x`. The Jacobian sum row is `[1, 1]`. Both variables contribute to J_kappa. The exchange operator sets `delta q_t = S`, `delta q_x = -S` — neither is zero. The cancellation `S + (-S) = 0` is a genuine structural consequence.

## Built-In Families Reference

| Family | Function | Variables | Projection | Exchange | Expected Status |
|---|---|---|---|---|---|
| Direct mode basis | `direct_mode_basis()` | kappa, sigma | a = kappa + sigma, b = kappa - sigma | delta kappa = 0 | tautological |
| Sym/antisym pair | `symmetric_antisymmetric_pair()` | q_+, q_- | a = q_+ + q_-, b = q_+ - q_- | delta q_+ = 0 | tautological |
| Two-channel | `two_channel_exchange()` | q_t, q_x | a = q_t, b = q_x | delta q_t = S, delta q_x = -S | derived |
| General linear | `general_linear_projection(n)` | q_1...q_n | a = sum alpha_i q_i, b = sum beta_i q_i | delta q_i = e_i * S | conditional |
| Conserved volume | `conserved_volume_family()` | q_t, q_x | a = q_t, b = q_x | delta q_t = S, delta q_x = -S | derived |
| Mixed exchange | `mixed_exchange_family()` | q_t, q_x | a = q_t, b = q_x | delta q_t = S, delta q_x = 0 | failed |

## API Reference

### Key Classes

**`ProjectionMap(id, variables, a_expr, b_expr)`**
- `.jacobian()` — returns 2xN Jacobian matrix
- `.is_linear()` — checks for linearity
- `.induced_source(deltas)` — returns `(J_a, J_b)` tuple

**`SourceOperator(id, kind, deltas, source_symbols)`**
- `kind`: `"exchange"`, `"creation"`, `"mixed"`, or `"unknown"`
- `deltas`: dict mapping variable symbols to perturbation expressions

**`VacuumStructure(id, variables, projection, exchange_operators, creation_operators)`**
- Container combining variables, projection, and operators

**`StructureAnalyzer()`**
- `.analyze(structure, ctx=None)` — returns `StructureAnalysisResult`

**`StructureSearchEngine()`** (also at `ctx.structure_search`)
- `.analyze(structure, ctx=None)` — analyze single structure
- `.search_family(family)` — solve for coefficient conditions
- `.enumerate_sign_patterns(n_vars=2)` — exhaustive sign-pattern search
- `.summary()` — text summary of all results

### Result Objects

**`InducedModeSource`** — one operator's projection result
- `.J_a`, `.J_b`, `.J_kappa`, `.J_sigma` — induced sources
- `.classification` — `"trace_free"`, `"pure_trace"`, `"mixed"`, `"zero"`, `"conditional_trace_free"`, `"undetermined"`
- `.status` — `StructureStatus` enum value
- `.conditions` — list of required coefficient constraints
- `.notes` — explanatory notes

**`StructureAnalysisResult`** — full structure analysis
- `.exchange_results`, `.creation_results` — lists of `InducedModeSource`
- `.summary_status` — overall `StructureStatus`
- `.derived_trace_free_exchange` — bool
- `.derived_traceful_creation` — bool
- `.conditions`, `.failures`, `.leak_warnings`, `.notes`
- `.summary()` — human-readable text summary

**`FamilySearchResult`** — family-level search result
- `.trace_free_derived`, `.conditional`, `.failed`, `.tautological` — categorized results
- `.conditions_for_trace_free` — extracted conditions
- `.summary()` — text summary

## What StructureSearch Does Not Do

StructureSearch does not prove that a candidate structure is physically correct. A result like

```text
exchange is trace-free because exchange is antisymmetric in two channels
```

moves the question to:

```text
why is exchange antisymmetric in those channels?
```

That is still progress. The module's purpose is to move the wall, name the remaining assumption, and prevent hidden circularity. It operates in weak-field 2D time-space mode space. A full theory will eventually need 3+1-dimensional, coordinate-aware generalization.

The most valuable outcome is not necessarily finding the final structure. The valuable outcome is narrowing the search space and identifying what kind of deeper physical principle would be needed to close the remaining gap.
