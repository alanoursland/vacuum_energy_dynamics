# StructureSearch Module Design

## Purpose

`StructureSearch` is a new upstream VacuumForge module for searching candidate mathematical structures that make local vacuum exchange inherently trace-free.

The existing VacuumForge pipeline can already verify the conditional chain:

```text
J_kappa = 0
=> kappa = 0
=> A B = 1
=> gamma_v = 1
```

That is a verification problem.

`StructureSearch` addresses the harder search problem:

```text
What mathematical structure for vacuum configuration makes
local exchange produce J_kappa = 0 as a consequence,
rather than as an imposed source rule?
```

The module is designed to sit upstream of the existing source, energy, metric, PPN, and requirement-validation systems. It generates or receives candidate vacuum structures, projects their source operators into `(kappa, sigma)` mode space, and determines whether trace-free exchange follows structurally.

## Why This Module Is Needed

VacuumForge currently answers questions like:

```text
Given J_kappa = 0, does kappa relax to zero?
```

It does not yet answer:

```text
Why should exchange have J_kappa = 0?
```

The missing theory step is not energy minimization. VacuumForge already verifies that unsourced positive-energy `kappa` relaxes to zero.

The missing step is source selection:

```text
static local exchange -> J_kappa = 0
```

`StructureSearch` exists to explore whether that implication can be derived from deeper mathematical structure.

## Module Name

The module should be named:

```text
vacuumforge.structure_search
```

This name is explicit and honest. The module does not merely classify existing sources. It searches over candidate structures that may produce source classifications.

Alternative names considered:

- `structures`
- `source_search`
- `pregeometry`
- `structure_forge`
- `operator_search`

`structure_search` is preferred because the scientific task is broader than source search alone. The module must represent candidate vacuum degrees of freedom, projection maps, source operators, constraints, and induced mode sources.

## Core Question

The module is organized around one central question:

```text
Given a candidate vacuum configuration structure, do exchange-type source
operators project into metric mode space with J_kappa = 0?
```

More formally:

Given pre-mode variables

```math
q_1, q_2, \ldots, q_n,
```

a projection map

```math
P: q_i \mapsto (a,b),
```

and an exchange operator

```math
S_{\text{exchange}},
```

compute the induced source components

```math
J_a,\quad J_b,
```

then decompose:

```math
J_\kappa = J_a + J_b,
```

```math
J_\sigma = J_a - J_b.
```

The desired structural result is:

```math
J_\kappa = 0
```

for exchange-type sources, while creation-type sources have

```math
J_\kappa \neq 0.
```

## Relationship to Existing VacuumForge Modules

`StructureSearch` does not replace the existing modules. It feeds them.

Existing pipeline:

```text
source classification
-> energy minimization
-> reciprocal scaling
-> metric construction
-> PPN extraction
-> validation/reporting
```

New pipeline:

```text
candidate vacuum structure
-> source operator projection
-> induced source classification
-> existing VacuumForge pipeline
```

If `StructureSearch` finds that a candidate structure derives trace-free exchange, it should pass the derived source result into the existing validation system with status:

```text
derived
```

If trace-free exchange is imposed manually, the status remains:

```text
assumed
```

If trace-free exchange holds only under coefficient constraints, the status should be:

```text
conditional
```

If it fails, the status should be:

```text
failed
```

## Package Layout

Suggested package structure:

```text
vacuumforge/
  structure_search/
    __init__.py
    structure.py
    variables.py
    projection.py
    operators.py
    families.py
    analyzer.py
    constraints.py
    results.py
    search.py
    reports.py
```

Optional later additions:

```text
    symmetries.py
    invariants.py
    examples.py
    heuristics.py
```

## Key Concepts

### Vacuum Structure

A `VacuumStructure` represents a candidate mathematical structure for the vacuum before it is reduced to ordinary metric mode variables.

It contains:

- a set of pre-mode degrees of freedom;
- a projection map into metric scale variables;
- optional internal constraints;
- optional symmetry rules;
- source operator families;
- creation operator families;
- metadata about physical interpretation.

Example:

```text
Structure:
  variables: q1, q2
  projection:
    a = q1 + q2
    b = q1 - q2
  exchange operator:
    delta q1 = 0
    delta q2 = S
  creation operator:
    delta q1 = C
    delta q2 = 0
```

This structure would project exchange into shear and creation into trace, if the algebra supports it.

### Pre-Mode Variables

Pre-mode variables are the internal variables of a candidate vacuum structure.

They are not necessarily `a`, `b`, `kappa`, or `sigma`.

Examples:

```math
q
```

```math
q_t,\quad q_x
```

```math
u,\quad v
```

```math
\rho,\quad \chi
```

```math
s,\quad \eta
```

The goal is to see whether some deeper variable basis naturally separates exchange and creation.

### Projection Map

A projection map defines how pre-mode variables determine metric scale variables.

Example:

```math
a = f_a(q_1,\ldots,q_n)
```

```math
b = f_b(q_1,\ldots,q_n)
```

The projection map is the bridge from candidate vacuum structure to VacuumForge’s existing `(a,b,kappa,sigma)` mode system.

The module must support linear and nonlinear projection maps.

### Source Operators

A source operator defines how a source changes the pre-mode variables.

Exchange and creation are represented as different source operators.

Example exchange operator:

```math
\delta q_1 = S
```

```math
\delta q_2 = -S
```

Example creation operator:

```math
\delta q_1 = C
```

```math
\delta q_2 = C
```

These are not yet metric sources. They become metric sources only after projection.

### Induced Metric Sources

Given a projection map and source operator, the module computes induced source components:

```math
J_a = \delta a
```

```math
J_b = \delta b
```

For nonlinear projections, this may require a Jacobian:

```math
J_a = \sum_i \frac{\partial a}{\partial q_i}\delta q_i
```

```math
J_b = \sum_i \frac{\partial b}{\partial q_i}\delta q_i.
```

Then:

```math
J_\kappa = J_a + J_b
```

```math
J_\sigma = J_a - J_b.
```

The module classifies the result.

### Structural Trace-Free Result

A source operator is structurally trace-free if

```math
J_\kappa = 0
```

as an identity after applying the projection map and structure constraints.

It is conditionally trace-free if

```math
J_\kappa = 0
```

only when coefficient constraints are imposed.

It is not trace-free if

```math
J_\kappa
```

is generically nonzero.

## Data Models

### VacuumStructure

```python
@dataclass
class VacuumStructure:
    id: str
    variables: list[sympy.Symbol]
    projection: ProjectionMap
    exchange_operators: list[SourceOperator]
    creation_operators: list[SourceOperator]
    constraints: list[sympy.Relational] = field(default_factory=list)
    symmetries: list[str] = field(default_factory=list)
    description: str | None = None
    status: str = "candidate"
```

### ProjectionMap

```python
@dataclass
class ProjectionMap:
    id: str
    a_expr: sympy.Expr
    b_expr: sympy.Expr
    variables: list[sympy.Symbol]
    description: str | None = None
```

Required methods:

```python
def jacobian(self) -> sympy.Matrix
def induced_sources(self, operator: SourceOperator) -> InducedModeSource
```

### SourceOperator

```python
@dataclass
class SourceOperator:
    id: str
    kind: Literal["exchange", "creation", "mixed", "unknown"]
    deltas: dict[sympy.Symbol, sympy.Expr]
    source_symbols: list[sympy.Symbol]
    constraints: list[sympy.Relational] = field(default_factory=list)
    description: str | None = None
    status: str = "candidate"
```

Example:

```python
SourceOperator(
    id="antisymmetric_exchange",
    kind="exchange",
    deltas={q1: S, q2: -S},
    source_symbols=[S],
)
```

### InducedModeSource

```python
@dataclass
class InducedModeSource:
    structure_id: str
    operator_id: str
    J_a: sympy.Expr
    J_b: sympy.Expr
    J_kappa: sympy.Expr
    J_sigma: sympy.Expr
    classification: str
    conditions: list[sympy.Relational]
    dependencies: list[str]
```

### StructureAnalysisResult

```python
@dataclass
class StructureAnalysisResult:
    structure_id: str
    exchange_results: list[InducedModeSource]
    creation_results: list[InducedModeSource]
    summary_status: str
    derived_trace_free_exchange: bool
    derived_traceful_creation: bool
    conditions: list[sympy.Relational]
    failures: list[str]
    notes: list[str]
```

## Core Algorithms

### Algorithm 1: Induced Source Projection

Input:

- projection map `a(q), b(q)`;
- source operator `delta q_i`.

Steps:

1. Build vector:

```math
q = (q_1,\ldots,q_n)
```

2. Build source vector:

```math
\delta q = (\delta q_1,\ldots,\delta q_n)
```

3. Compute Jacobian:

```math
J_P =
\begin{pmatrix}
\partial a/\partial q_1 & \cdots & \partial a/\partial q_n \\
\partial b/\partial q_1 & \cdots & \partial b/\partial q_n
\end{pmatrix}
```

4. Compute:

```math
\begin{pmatrix}
J_a \\
J_b
\end{pmatrix}
=
J_P \delta q
```

5. Compute:

```math
J_\kappa = J_a + J_b
```

```math
J_\sigma = J_a - J_b
```

6. Simplify results.

7. Classify.

Output:

`InducedModeSource`.

### Algorithm 2: Source Classification

Input:

```math
J_\kappa,\quad J_\sigma.
```

Steps:

1. Simplify both.
2. If `J_kappa == 0` and `J_sigma != 0`, classify as trace-free.
3. If `J_sigma == 0` and `J_kappa != 0`, classify as pure trace.
4. If both nonzero, classify as mixed.
5. If both zero, classify as zero.
6. If symbolic uncertainty remains, attempt conditional solve.
7. If conditions are found, classify as conditionally trace-free or conditionally traceful.
8. Otherwise classify as undetermined.

### Algorithm 3: Conditional Trace-Free Solve

Input:

```math
J_\kappa(q,c_i,S_j)
```

and coefficient list.

Goal:

Find conditions on coefficients such that:

```math
J_\kappa = 0
```

for arbitrary source symbols.

Steps:

1. Expand `J_kappa`.
2. Collect by source symbols.
3. Extract coefficients of independent source symbols.
4. Set each coefficient equal to zero.
5. Solve the resulting equations for structure coefficients.
6. Return conditions.

Example:

```math
J_\kappa = (\alpha+\beta)S
```

returns:

```math
\alpha+\beta=0.
```

This means trace-free exchange is not automatic but follows if the structure satisfies an antisymmetry condition.

### Algorithm 4: Creation Trace Test

Creation should be traceful.

Input:

```math
J_\kappa^{creation}.
```

Steps:

1. Simplify.
2. Check whether it is generically nonzero.
3. If nonzero, classify as traceful.
4. If zero, creation fails to distinguish itself from exchange.
5. If conditional, report required conditions.

The desired result is:

```math
J_\kappa^{creation} \neq 0.
```

For practical symbolic work, nonzero detection may use structural simplification plus optional generic sampling, as existing VacuumForge checks already do.

### Algorithm 5: Full Chain Validation

If a structure derives trace-free exchange, feed the induced source into the existing VacuumForge pipeline:

1. Create source record with derived `J_kappa = 0`.
2. Use existing energy minimization module.
3. Derive `kappa = 0`.
4. Derive reciprocal scaling.
5. Construct metric.
6. Extract `gamma_v`.
7. Extract `beta` if a temporal ansatz is present.
8. Generate a full validation result.

This produces the final research answer:

```text
This candidate structure derives trace-free exchange and therefore derives reciprocal scaling.
```

or:

```text
This candidate structure requires condition alpha + beta = 0 to derive trace-free exchange.
```

or:

```text
This candidate structure fails because exchange sources kappa.
```

## Candidate Structure Families

The module should include reusable structure families.

### Family 1: Direct Mode Basis

Variables:

```math
q_1=\kappa,\quad q_2=\sigma.
```

Projection:

```math
a=\kappa+\sigma
```

```math
b=\kappa-\sigma
```

Exchange:

```math
\delta\kappa = 0,\quad \delta\sigma=S.
```

Creation:

```math
\delta\kappa=C,\quad \delta\sigma=0.
```

This family is useful as a control. It assumes the desired separation and should be classified as assumed or tautological, not as a deep derivation.

### Family 2: Symmetric/Antisymmetric Pair Basis

Variables:

```math
q_+,\quad q_-.
```

Projection:

```math
a=q_+ + q_-
```

```math
b=q_+ - q_-.
```

Exchange:

```math
\delta q_+ = 0,\quad \delta q_- = S.
```

Creation:

```math
\delta q_+ = C,\quad \delta q_- = 0.
```

This is mathematically equivalent to the mode basis but may represent a more primitive physical split between common-mode and differential-mode response.

The module should identify whether this is merely a relabeling of `(kappa, sigma)` or whether additional structure gives it independent meaning.

### Family 3: Two-Channel Exchange Basis

Variables:

```math
q_t,\quad q_x.
```

Projection:

```math
a=\alpha_t q_t + \alpha_x q_x
```

```math
b=\beta_t q_t + \beta_x q_x.
```

Exchange:

```math
\delta q_t=S
```

```math
\delta q_x=-S.
```

Creation:

```math
\delta q_t=C
```

```math
\delta q_x=C.
```

The module should solve for coefficient conditions under which exchange is trace-free and creation is traceful.

This family is likely to reveal whether a time-space antisymmetry or conservation law is sufficient.

### Family 4: General Linear Projection Family

Variables:

```math
q_1,\ldots,q_n.
```

Projection:

```math
a=\sum_i \alpha_i q_i
```

```math
b=\sum_i \beta_i q_i.
```

Exchange operator:

```math
\delta q_i = e_i S.
```

Creation operator:

```math
\delta q_i = c_i C.
```

Trace-free exchange condition:

```math
\sum_i (\alpha_i+\beta_i)e_i = 0.
```

Traceful creation condition:

```math
\sum_i (\alpha_i+\beta_i)c_i \neq 0.
```

This family is important because it exposes the general algebraic condition for exchange trace-freeness.

### Family 5: Nonlinear Projection Family

Variables:

```math
q_1,\ldots,q_n.
```

Projection examples:

```math
a=\ln f(q_i)
```

```math
b=\ln g(q_i)
```

or

```math
A=f(q_i)
```

```math
B=g(q_i).
```

The module should use Jacobian projection to analyze infinitesimal source response.

This family is needed because the eventual vacuum structure may not be linear in scale factors.

### Family 6: Conserved-Volume or Conserved-Measure Families

These families test whether a conservation principle can derive trace-free exchange.

Examples:

```math
\delta(a+b)=0
```

or

```math
\delta(AB)=0
```

or

```math
\delta(\sqrt{-g})=0.
```

The module should clearly distinguish:

- deriving trace-free exchange from a conservation principle;
- merely restating trace-free exchange as a conservation principle.

This family is useful for auditing possible hidden circularity.

### Family 7: Representation-Theoretic Families

Later, the module may include structures based on symmetry representations.

Example idea:

- exchange transforms as a traceless representation;
- creation transforms as a scalar representation.

This may become relevant for deriving scalar-mode suppression and gravitational-wave polarization structure.

The first version can leave this as a placeholder.

## Search Modes

### Manual Candidate Evaluation

The user defines one candidate structure and asks for analysis.

Example:

```python
result = ctx.structure_search.analyze(structure)
```

Output:

- induced exchange source;
- induced creation source;
- trace classification;
- conditions;
- full chain validation if applicable.

### Family Parameter Search

The user defines a family with symbolic coefficients.

The module solves for coefficient conditions that make exchange trace-free and creation traceful.

Example output:

```text
Exchange trace-free condition:
  alpha_t + beta_t - alpha_x - beta_x = 0

Creation traceful condition:
  alpha_t + beta_t + alpha_x + beta_x != 0
```

### Candidate Enumeration

The module generates a finite set of candidate structures from templates.

Examples:

- all sign patterns for two-channel exchange;
- all simple linear projections with coefficients in `{-1,0,1}`;
- all two-variable source operators with one exchange parameter.

It then classifies candidates.

This is not intended as blind discovery. It is a way to map a small symbolic design space.

### Counterexample Search

The module should look for structures that satisfy some proposed principle but fail trace-free exchange.

Example:

```text
Structure satisfies total energy conservation but exchange still has J_kappa != 0.
```

This helps test whether proposed derivations are too weak.

## Integration with Existing VacuumForge

### Integration with Sources

If a structure derives an induced source, it should create a normal VacuumForge source record.

Example:

```python
ctx.sources.add_modes(
    id="derived_exchange_from_structure_X",
    J_kappa=result.J_kappa,
    J_sigma=result.J_sigma,
    status="derived",
    dependencies=[structure.id, operator.id],
)
```

### Integration with Requirements

The existing requirement system should validate:

- trace-free exchange;
- traceful creation;
- reciprocal scaling;
- gamma;
- beta;
- positivity;
- assumption leaks.

`StructureSearch` should add new requirements:

- exchange trace-free derived from structure;
- creation traceful derived from structure;
- exchange not trace-free by assumption;
- creation not traceful by assumption;
- structure not merely a relabeling of `(kappa, sigma)` unless allowed.

### Integration with Reports

Reports should include a new section:

```text
Structure Search Analysis
```

with:

- structure variables;
- projection map;
- exchange operator;
- creation operator;
- induced sources;
- classification;
- coefficient conditions;
- whether trace-free exchange was derived, assumed, conditional, or failed;
- downstream equal-response validation.

### Integration with Theorem Candidates

If multiple independent structures produce trace-free exchange from the same deeper condition, the module should allow promotion to a theorem candidate.

Example:

```text
Theorem candidate:
  Exchange is trace-free when exchange operators lie in the kernel of the trace projection.
```

This statement is close to tautological mathematically, so the real theorem would need a physical reason why exchange operators lie in that kernel.

The theorem candidate system should track that distinction.

## Status Categories

The module should classify results using these statuses.

### Derived

Trace-free exchange follows from the candidate structure without assuming `J_kappa = 0` or equivalent target forms.

### Assumed

Trace-free exchange is present because the structure directly defines exchange as `delta kappa = 0` or `J_kappa = 0`.

### Conditional

Trace-free exchange follows only if coefficient constraints or symmetry constraints are imposed.

Example:

```math
\alpha+\beta=0.
```

### Failed

Exchange generically produces nonzero `J_kappa`.

### Undetermined

The algebra cannot decide whether `J_kappa` vanishes.

### Tautological

The structure is merely a reparameterization of the `(kappa, sigma)` basis and defines exchange in that basis.

This is not useless, but it should not be mistaken for a deep derivation.

## Assumption Leak Detection for Structure Search

Existing leak detection should be extended.

The module should flag when a structure contains the target in disguised form.

Potential leaks:

- projection directly defines one variable as `kappa`;
- exchange operator directly sets `delta kappa = 0`;
- projection map enforces `a+b=0`;
- source operator imposes `J_a + J_b = 0`;
- coefficient constraints are equivalent to trace-free exchange;
- creation/exchange distinction is defined purely as trace-free/traceful without deeper content.

Leak detection should not reject these models. It should classify them honestly.

A control model may intentionally assume separation. But it should be labeled as such.

## Minimal Successful Result

A minimal successful `StructureSearch` result would look like this:

```text
Candidate Structure: two_channel_antisymmetric_exchange

Variables:
  q_t, q_x

Projection:
  a = q_t
  b = q_x

Exchange:
  delta q_t = S
  delta q_x = -S

Creation:
  delta q_t = C
  delta q_x = C

Induced exchange:
  J_a = S
  J_b = -S
  J_kappa = 0
  J_sigma = 2S

Induced creation:
  J_a = C
  J_b = C
  J_kappa = 2C
  J_sigma = 0

Classification:
  exchange trace-free: derived from antisymmetric exchange operator
  creation traceful: derived from symmetric creation operator

Downstream:
  kappa = 0
  AB = 1
  gamma_v = 1
```

However, this still raises the physical question:

```text
Why is local exchange antisymmetric in q_t, q_x?
```

The module should therefore report the deeper unresolved assumption:

```text
The structure derives trace-free exchange from antisymmetric channel exchange.
The physical origin of antisymmetric channel exchange remains open.
```

This is a good outcome. It moves the wall one level deeper and names the new missing principle.

## Search Targets

The module should search for structures that satisfy:

### Required

- exchange induces `J_kappa = 0`;
- exchange induces nonzero `J_sigma`;
- creation induces nonzero `J_kappa`;
- creation is distinguishable from exchange;
- downstream reciprocal scaling follows through existing VacuumForge pipeline.

### Preferred

- trace-free exchange follows from a symmetry or conservation law;
- creation tracefulness follows from uniform/common-mode operation;
- the structure is not a trivial relabeling of `(kappa, sigma)`;
- coefficient constraints are simple;
- the structure generalizes to 3+1 dimensions;
- the structure suggests scalar-mode suppression in waves.

### Rejected or Flagged

- exchange trace-free only because `J_kappa=0` was directly assumed;
- projection map already imposes `AB=1`;
- creation also trace-free;
- exchange also traceful;
- kappa is removed entirely rather than unsourced;
- conditions conflict with known weak-field requirements.

## Example API

### Manual Structure

```python
import sympy as sp
from vacuumforge import TheoryContext
from vacuumforge.structure_search import VacuumStructure, ProjectionMap, SourceOperator

ctx = TheoryContext("structure_search_demo")

q_t, q_x, S, C = sp.symbols("q_t q_x S C")

projection = ProjectionMap(
    id="direct_tx_projection",
    variables=[q_t, q_x],
    a_expr=q_t,
    b_expr=q_x,
)

exchange = SourceOperator(
    id="antisymmetric_exchange",
    kind="exchange",
    deltas={q_t: S, q_x: -S},
    source_symbols=[S],
)

creation = SourceOperator(
    id="symmetric_creation",
    kind="creation",
    deltas={q_t: C, q_x: C},
    source_symbols=[C],
)

structure = VacuumStructure(
    id="two_channel_exchange_creation",
    variables=[q_t, q_x],
    projection=projection,
    exchange_operators=[exchange],
    creation_operators=[creation],
)

result = ctx.structure_search.analyze(structure)
print(result.summary())
```

Expected output:

```text
exchange: trace_free
creation: pure_trace
downstream reciprocal scaling: pass
status: derived from structure, conditional on antisymmetric exchange operator
```

### Family Search

```python
family = ctx.structure_search.families.general_linear_two_channel()
results = ctx.structure_search.search_family(
    family,
    require_exchange_trace_free=True,
    require_creation_traceful=True,
)
```

Expected output:

```text
Found conditions:
  (alpha_t + beta_t)*e_t + (alpha_x + beta_x)*e_x = 0
  (alpha_t + beta_t)*c_t + (alpha_x + beta_x)*c_x != 0
```

## Tests

The module should include tests for:

### Projection Tests

- linear projection computes correct induced sources;
- nonlinear projection uses Jacobian correctly;
- missing delta variables default to zero or raise clear errors.

### Classification Tests

- antisymmetric exchange is trace-free;
- symmetric creation is pure trace;
- mixed operator is mixed;
- zero operator is zero;
- symbolic condition returns conditional.

### Leak Detection Tests

- direct `delta kappa = 0` is classified as assumed or tautological;
- projection imposing `a+b=0` is flagged;
- `J_a + J_b = 0` imposed directly is flagged.

### Family Search Tests

- general two-channel family returns correct trace-free condition;
- free coefficients remain conditional;
- known failing family fails.

### Downstream Integration Tests

- derived trace-free source feeds into energy minimization;
- derived `kappa=0` feeds into reciprocal scaling;
- derived reciprocal scaling gives `gamma_v=1`.

### Counterexample Tests

- total conservation alone does not force trace-free exchange;
- density constancy alone does not force `kappa=0`;
- local Lorentz-compatible projection does not necessarily force `gamma_v=1`.

## Documentation

The module should have documentation explaining:

- difference between validation and structure search;
- what a candidate vacuum structure is;
- how projection maps work;
- how source operators induce metric-mode sources;
- why trace-free exchange is the target;
- how to interpret derived, assumed, conditional, failed, and tautological results;
- how downstream validation connects to existing VacuumForge results.

A tutorial should walk through:

1. direct mode basis as a tautological control;
2. two-channel antisymmetric exchange as a minimal nontrivial model;
3. general linear family search;
4. failed mixed source model;
5. downstream recovery of reciprocal scaling.

## Known Limitations

The first version of `StructureSearch` will not solve the full physics problem.

It can show that a candidate structure makes exchange trace-free.

It cannot, by itself, prove that the candidate structure is physically correct.

A result such as:

```text
exchange is trace-free because exchange is antisymmetric in two channels
```

moves the question to:

```text
why is exchange antisymmetric in those channels?
```

That is still progress. The software's job is to move the wall, name the remaining assumption, and prevent hidden circularity.

The module also begins in weak-field 2D time-space mode space. A full theory will need 3+1-dimensional, coordinate-aware, and possibly gauge-aware generalization.

## Scientific Success Criteria

`StructureSearch` succeeds if it can produce results like:

```text
This candidate structure derives J_kappa = 0 from antisymmetric exchange.
```

or:

```text
This candidate structure requires alpha + beta = 0 for exchange to be trace-free.
```

or:

```text
This candidate structure fails because exchange sources both kappa and sigma.
```

or:

```text
This candidate merely assumes the target by defining exchange as delta kappa = 0.
```

The most valuable outcome is not necessarily finding the final structure immediately. The valuable outcome is narrowing the search space and identifying what kind of deeper physical principle would be needed.

## Summary

`StructureSearch` is the next major VacuumForge module.

It addresses the problem VacuumForge cannot yet answer:

```text
What minimal mathematical structure for vacuum configuration makes local exchange inherently trace-free?
```

It does this by representing candidate pre-mode variables, projection maps, exchange and creation operators, and induced metric-mode sources.

It then classifies whether exchange is trace-free as a derived, assumed, conditional, failed, tautological, or undetermined result.

When successful, it feeds the derived source classification into the existing VacuumForge pipeline to verify the full chain:

```text
derived trace-free exchange
-> kappa = 0
-> A B = 1
-> gamma_v = 1
```

This module turns VacuumForge from a verifier of proposed source classifications into a search tool for the structures that might produce those classifications.
