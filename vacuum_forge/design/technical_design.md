# VacuumForge Technical Design

## Purpose

This document describes how to implement VacuumForge.

VacuumForge is a Python and SymPy-based symbolic research workbench for exploring candidate mathematical structures in a vacuum-based theory of gravity. It is designed to represent symbolic variables, assumptions, source laws, energy functionals, mode decompositions, weak-field expansions, validation requirements, derivation dependencies, and human-readable reports.

This document covers implementation structure rather than scientific justification. It assumes the feature goals described in `feature_design.md`.

## Technical Goals

VacuumForge should be:

- symbolic-first;
- inspectable;
- reproducible;
- extensible;
- explicit about assumptions;
- explicit about dependencies;
- careful about exact versus perturbative results;
- able to distinguish assumed results from derived results;
- usable from scripts, notebooks, and eventually a command-line interface.

The first implementation should favor clarity over performance. The software is a theory-development tool, not a numerical solver.

## Technology Stack

VacuumForge will use Python as the primary language.

Core dependencies:

- `sympy` for symbolic algebra, simplification, solving, differentiation, series expansion, assumptions, and expression manipulation;
- `pydantic` or `dataclasses` for structured internal models;
- `networkx` for dependency graphs;
- `rich` for terminal output;
- `jinja2` for report generation;
- `pyyaml` or `tomli/tomli-w` for model/session serialization;
- `pytest` for automated tests.

Optional later dependencies:

- `pandas` for comparison tables;
- `matplotlib` for visualization of dependency graphs or candidate families;
- `hypothesis` for property-based testing;
- `sympy.physics.units` for dimensional checking;
- `lark` or `antlr` only if a custom input language becomes necessary.

The core should not depend on a web framework or UI framework. The initial interface should be Python API-first, with optional CLI wrappers.

## Repository Structure

A proposed repository layout:

```text
vacuumforge/
  pyproject.toml
  README.md
  design/
    overview.md
    feature_design.md
    technical_design.md
  src/
    vacuumforge/
      __init__.py
      core/
        symbols.py
        assumptions.py
        expressions.py
        transforms.py
        context.py
        status.py
      modes/
        scale_factors.py
        log_variables.py
        kappa_sigma.py
        source_decomposition.py
      metric/
        weak_field.py
        ppn.py
        expansion.py
        coordinates.py
      energy/
        functional.py
        positivity.py
        variation.py
        minimization.py
      sources/
        source.py
        exchange.py
        creation.py
        classification.py
      requirements/
        requirement.py
        validators.py
        result.py
        target_library.py
      search/
        candidate_family.py
        coefficient_solver.py
        counterexample.py
      ledger/
        ledger.py
        dependency_graph.py
        assumption_audit.py
      reports/
        markdown.py
        templates/
          derivation_report.md.j2
          validation_report.md.j2
          model_summary.md.j2
      persistence/
        session.py
        serialize.py
      cli/
        main.py
  tests/
    test_transforms.py
    test_reciprocal_scaling.py
    test_ppn_extraction.py
    test_source_decomposition.py
    test_energy_minimization.py
    test_dependency_tracking.py
```

## Core Architecture

VacuumForge should be organized around a central `TheoryContext`.

The `TheoryContext` stores:

- symbolic registry;
- assumptions;
- definitions;
- candidate equations;
- source laws;
- energy functionals;
- requirements;
- target results;
- derivation records;
- dependency graph;
- ledger entries.

The context is the main object passed to high-level APIs.

Example:

```python
from vacuumforge import TheoryContext

ctx = TheoryContext(name="equal_response_static_exchange")

ctx.symbols.define_constant("c", positive=True)
ctx.symbols.define_constant("G", positive=True)
ctx.symbols.define_constant("M", positive=True)
ctx.symbols.define_coordinate("r", positive=True)

ctx.modes.define_standard_scale_modes()
ctx.assumptions.add("A_redshift", ctx.A - sympy.exp(ctx.Phi / ctx.c**2))
```

The internal design should avoid global mutable state. Multiple contexts should be able to exist in the same Python process.

## Symbolic Registry

### Design

The symbolic registry should manage all named symbols, functions, and expressions.

Core classes:

```python
@dataclass
class SymbolRecord:
    name: str
    sympy_object: sympy.Basic
    kind: str
    description: str | None = None
    assumptions: dict[str, Any] = field(default_factory=dict)
    dimensions: str | None = None
    status: str = "definition"
```

```python
class SymbolRegistry:
    def define_symbol(...)
    def define_function(...)
    def define_constant(...)
    def define_coordinate(...)
    def get(name: str) -> sympy.Basic
    def record(name: str) -> SymbolRecord
    def list(kind: str | None = None) -> list[SymbolRecord]
```

The registry should support:

- symbols such as `c`, `G`, `M`, `gamma_v`, `beta`;
- coordinates such as `r`, `t`, `x`;
- functions such as `A(r)`, `B(r)`, `Phi(r)`, `kappa(r)`, `sigma(r)`;
- abstract sources such as `J_a`, `J_b`, `J_kappa`, `J_sigma`;
- coefficients such as `C_kappa`, `K_sigma`.

### SymPy Representation

For scale factors depending on radius, prefer SymPy functions applied to coordinates:

```python
r = sympy.Symbol("r", positive=True)
A = sympy.Function("A")(r)
B = sympy.Function("B")(r)
Phi = sympy.Function("Phi")(r)
```

For algebraic prototype models, also support coordinate-free symbols:

```python
A, B = sympy.symbols("A B", positive=True)
```

The context should allow both modes because many equal-response checks are algebraic, while field-equation work requires functions.

### Need for Namespaces

To avoid collisions, the registry should support named namespaces:

```text
metric.A
metric.B
modes.kappa
modes.sigma
sources.J_kappa
coefficients.C_kappa
```

The Python API can expose convenient attributes, but internal storage should keep full names.

## Assumption Management

### Design

Assumptions should be explicit records, not just SymPy assumptions embedded in symbols.

Core class:

```python
@dataclass
class AssumptionRecord:
    id: str
    expression: sympy.Basic | sympy.Relational
    description: str | None
    status: str = "assumption"
    dependencies: list[str] = field(default_factory=list)
```

The assumption manager should support:

```python
ctx.assumptions.add(id="A_exponential", expr=Eq(A, exp(Phi/c**2)))
ctx.assumptions.remove("A_exponential")
ctx.assumptions.active()
ctx.assumptions.contains_target(target_expr)
```

### Substitution Assumptions

Some assumptions are equations used as rewrite rules.

Example:

```math
A = e^{\Phi/c^2}
```

These should be represented as `sympy.Eq` plus a generated substitution map:

```python
{A: exp(Phi/c**2)}
```

The system should separate:

- logical assumptions;
- substitution definitions;
- inequalities;
- boundary conditions.

### Dependency Recording

Every operation using an assumption should record that usage in the derivation graph.

Example:

```python
result = ctx.derive("g00_expansion", operation=expand_metric, uses=["A_exponential"])
```

The output should know it depends on `A_exponential`.

## Expression Records

A central expression store should keep named symbolic expressions.

```python
@dataclass
class ExpressionRecord:
    id: str
    expr: sympy.Basic
    description: str | None = None
    status: str = "definition"
    dependencies: list[str] = field(default_factory=list)
    scope: str | None = None
    exactness: str = "exact"
```

Examples:

```text
metric.g00
metric.gij_factor
modes.mu
energy.E_config
requirements.reciprocal_condition
```

The expression store should allow inspection and reuse.

## Status System

VacuumForge needs a status vocabulary mirroring the research workflow.

Use an enum:

```python
class Status(str, Enum):
    DEFINITION = "definition"
    POSTULATE = "postulate"
    CANDIDATE_POSTULATE = "candidate_postulate"
    ASSUMPTION = "assumption"
    DERIVED = "derived"
    PROVISIONAL = "provisional"
    OBSERVATIONAL_CONSTRAINT = "observational_constraint"
    FAILED_DERIVATION = "failed_derivation"
    OPEN_QUESTION = "open_question"
    TARGET = "target"
```

Status should appear in the ledger, expression records, assumptions, and reports.

## Mode System

### Standard Mode Definitions

Implement a `ModeSystem` with helpers for defining the standard variables.

For algebraic mode:

```python
A, B = symbols("A B", positive=True)
a = log(A)
b = log(B)
kappa = (a + b)/2
sigma = (a - b)/2
```

For field mode:

```python
A = Function("A")(r)
B = Function("B")(r)
a = Function("a")(r)
b = Function("b")(r)
kappa = Function("kappa")(r)
sigma = Function("sigma")(r)
```

In field mode, relations should be recorded as equations rather than direct definitions:

```math
a(r)=\ln A(r)
```

```math
b(r)=\ln B(r)
```

```math
\kappa(r)=\frac{a(r)+b(r)}{2}
```

```math
\sigma(r)=\frac{a(r)-b(r)}{2}
```

### Transform Engine

Implement transformations among representations.

Core API:

```python
ctx.transforms.to_log(expr)
ctx.transforms.to_scale(expr)
ctx.transforms.to_modes(expr)
ctx.transforms.from_modes(expr)
```

Transform rules:

```python
a -> log(A)
b -> log(B)
kappa -> (a + b)/2
sigma -> (a - b)/2
a -> kappa + sigma
b -> kappa - sigma
A -> exp(kappa + sigma)
B -> exp(kappa - sigma)
```

The transform engine should track dependencies. If an expression is rewritten using mode definitions, the result should depend on those definitions.

### Simplification Strategy

SymPy simplification with logs and exponentials can be tricky. Use controlled simplification rather than calling `simplify` blindly everywhere.

Recommended utilities:

```python
sympy.expand_log(expr, force=True)
sympy.logcombine(expr, force=True)
sympy.powsimp(expr, force=True)
sympy.trigsimp(expr)
sympy.factor(expr)
sympy.cancel(expr)
```

Create a wrapper:

```python
def vf_simplify(expr, *, log=True, powers=True, factor=True):
    ...
```

This allows reproducible simplification behavior.

## Reciprocal Scaling Checks

### Equivalent Conditions

Implement a `ReciprocalScalingChecker`.

It should check whether an expression set implies:

```math
A B = 1
```

```math
a+b=0
```

```math
\kappa=0
```

```math
B=1/A
```

### Exact Check

Given definitions and assumptions, use substitution and simplification:

```python
def check_exact_reciprocal(ctx):
    expr = ctx.A * ctx.B - 1
    expr = ctx.apply_assumptions(expr)
    return simplify(expr) == 0
```

### Mode Check

If the model has `kappa`, check whether `kappa` is identically zero under equilibrium solution:

```python
def check_kappa_zero(solution):
    return simplify(solution[kappa]) == 0
```

### Perturbative Check

For weak-field expansions, expand `A*B - 1` in `epsilon = Phi/c**2` to requested order and check coefficients.

Represent perturbative result:

```python
@dataclass
class PerturbativeCheck:
    target: str
    order: int
    residual: sympy.Expr
    holds_to_order: bool
    first_failure_order: int | None
```

### Scope

The checker should report:

- exact;
- first order;
- second order;
- failed;
- undetermined.

## Weak-Field Expansion Engine

### Expansion Parameter

Define a canonical dimensionless expansion parameter:

```math
\epsilon = \Phi/c^2.
```

Because `Phi/c**2` is an expression, introduce a temporary dummy symbol:

```python
eps = sympy.Symbol("epsilon")
expr_eps = expr.subs(Phi/c**2, eps)
series = sympy.series(expr_eps, eps, 0, order+1).removeO()
result = series.subs(eps, Phi/c**2)
```

This works best when expressions are written explicitly in terms of `Phi/c**2`.

For functions `Phi(r)`, use the expression `Phi(r)/c**2`.

### API

```python
ctx.expansion.weak_field(expr, order=2, parameter=Phi/c**2)
ctx.expansion.coefficient(expr, parameter=Phi/c**2, power=1)
```

### Expansion Records

Expansion results should record:

- original expression;
- expansion parameter;
- order;
- resulting expression;
- residual if available;
- assumptions used.

## Metric Construction

### Metric Object

Implement a weak-field metric object:

```python
@dataclass
class WeakFieldMetric:
    A: sympy.Expr
    B: sympy.Expr
    coordinates: str = "isotropic_static_spherical"
    convention: str = "signature_minus_plus_plus_plus"

    @property
    def g00(self):
        return -self.A**2

    @property
    def gij_factor(self):
        return self.B**2
```

For the initial system, `gij` can be represented by its isotropic scalar factor rather than a full matrix:

```math
g_{ij}=B^2\delta_{ij}
```

Later, support full matrices.

### Metric Construction API

```python
metric = ctx.metric.from_scale_factors(A, B)
ctx.store("metric.g00", metric.g00)
ctx.store("metric.gij_factor", metric.gij_factor)
```

### Parameterized Target Metrics

Store target PPN-like forms:

```python
g00_target = -(1 + 2*Phi/c**2 + 2*beta*Phi**2/c**4)
gij_target = 1 - 2*gamma_v*Phi/c**2
```

Support comparison against these forms.

## PPN Parameter Extraction

### Gamma Extraction

Given:

```math
g_{ij}=1 - 2\gamma_v \Phi/c^2 + O(\Phi^2/c^4)
```

extract `gamma_v`.

Algorithm:

1. Expand `gij_factor` to first order in `epsilon = Phi/c**2`.
2. Compute coefficient of `epsilon`.
3. Solve:

```math
\text{coeff} = -2\gamma_v
```

So:

```python
gamma_value = -coeff / 2
```

Example:

```python
B = exp(-Phi/c**2)
gij = B**2 = exp(-2Phi/c**2)
coeff = -2
gamma_v = 1
```

### Beta Extraction

Given:

```math
g_{00}=-(1+2\Phi/c^2+2\beta\Phi^2/c^4)
```

extract `beta`.

Algorithm:

1. Compute `-g00`.
2. Expand to second order in `epsilon`.
3. Coefficient of `epsilon**2` equals `2*beta`.
4. `beta = coeff2/2`.

Example:

```python
A = exp(Phi/c**2)
g00 = -A**2
-g00 = exp(2epsilon)
coeff2 = 2
beta = 1
```

### API

```python
ctx.ppn.extract_gamma(metric)
ctx.ppn.extract_beta(metric)
ctx.ppn.extract_all(metric, order=2)
```

Return:

```python
@dataclass
class PPNResult:
    parameter: str
    value: sympy.Expr
    exactness: str
    dependencies: list[str]
    details: dict[str, Any]
```

## Source System

### Source Records

Represent source components as symbolic expressions or symbolic objects.

```python
@dataclass
class SourceRecord:
    id: str
    components: dict[str, sympy.Expr]
    source_type: str
    description: str | None = None
    assumptions: list[str] = field(default_factory=list)
```

Example components:

```python
{"J_a": Ja, "J_b": Jb}
```

or:

```python
{"J_kappa": 0, "J_sigma": Jsigma}
```

### Source Decomposition

Implement:

```python
def decompose_ab_to_modes(Ja, Jb):
    Jk = simplify(Ja + Jb)
    Js = simplify(Ja - Jb)
    return Jk, Js
```

Implement inverse:

```python
Ja = (Jk + Js)/2
Jb = (Jk - Js)/2
```

### Classification

A source classifier should return:

```python
class SourceClass(str, Enum):
    TRACE_FREE = "trace_free"
    PURE_TRACE = "pure_trace"
    MIXED = "mixed"
    ZERO = "zero"
    UNDETERMINED = "undetermined"
```

Classification rules:

- `J_kappa == 0` and `J_sigma != 0`: trace-free;
- `J_sigma == 0` and `J_kappa != 0`: pure trace;
- both nonzero: mixed;
- both zero: zero;
- cannot simplify: undetermined.

### Exchange Source Modeling

Provide helpers for common exchange source patterns.

Examples:

```python
Source.exchange_trace_free(Jsigma)
```

returns:

```math
J_\kappa=0,\quad J_\sigma=J_\sigma.
```

```python
Source.exchange_general(alpha, beta)
```

returns symbolic `J_a`, `J_b` with coefficients to test.

Important: the software must not assume exchange is trace-free unless the source model explicitly says so. Exchange source modeling should support both derived and assumed trace-free cases.

### Creation Source Modeling

Provide helpers:

```python
Source.creation_uniform(Jkappa)
```

returns:

```math
J_\kappa=J_c,\quad J_\sigma=0.
```

Localized creation can include profile functions:

```math
J_\kappa(r)=J_0 f(r)
```

The system should classify these as traceful unless additional shear terms are present.

## Exchange-Creation Separation Tests

Implement a validator:

```python
class ExchangeCreationSeparationValidator:
    def validate(exchange_source, creation_source) -> ValidationResult
```

Checks:

- exchange source has `J_kappa = 0`;
- creation source has `J_kappa != 0`;
- exchange source can source `sigma`;
- creation source is traceful;
- static gravity model uses exchange source;
- expansion model uses creation source.

Result should distinguish:

- satisfied by explicit assumption;
- satisfied by algebraic derivation;
- failed;
- undetermined.

To determine whether it is assumed or derived, inspect dependency records. If `J_kappa = 0` is a declared assumption, classify as assumed. If it follows from more primitive source equations after simplification, classify as derived.

## Energy Functional System

### Energy Functional Representation

Represent energy functionals symbolically.

For algebraic models:

```python
E = Ck*kappa**2 + Cs*sigma**2 - Jk*kappa - Js*sigma
```

For field models:

```python
density = Ck*kappa(r)**2 + Kk*diff(kappa(r), r)**2 + ...
E = Integral(density, (r, 0, oo))
```

Core class:

```python
@dataclass
class EnergyFunctional:
    id: str
    density: sympy.Expr | None
    expression: sympy.Expr
    variables: list[sympy.Basic]
    sources: list[str] = field(default_factory=list)
    description: str | None = None
```

For early work, algebraic energy functionals are enough. Field integrals can be represented without evaluating them.

### Energy Builder

Provide convenience methods:

```python
ctx.energy.quadratic_modes(Ck, Cs, cross=0)
ctx.energy.source_coupled(Ck, Cs, Jk, Js)
ctx.energy.mismatch(C, mu)
```

### Positivity Checks

Implement quadratic-form positivity.

For algebraic quadratic functionals in variables `[kappa, sigma]`:

1. Extract Hessian matrix:

```python
H = sympy.hessian(E, variables)
```

2. Check positive definiteness using principal minors under coefficient assumptions.

For two variables:

```math
H_{11}>0,\quad \det H>0
```

If coefficients have SymPy assumptions `positive=True`, this can often be resolved.

Return:

```python
@dataclass
class PositivityResult:
    status: Literal["positive", "semidefinite", "indefinite", "negative", "undetermined"]
    conditions: list[sympy.Relational]
    hessian: sympy.Matrix | None
    notes: list[str]
```

For non-quadratic expressions, use local Hessian analysis around equilibrium and report that global positivity is undetermined unless proven.

### Minimization

For algebraic models:

```python
equations = [Eq(diff(E, var), 0) for var in variables]
solutions = solve(equations, variables, dict=True)
```

For linear source-coupled quadratic energy:

```math
E=C_\kappa\kappa^2+C_\sigma\sigma^2-J_\kappa\kappa-J_\sigma\sigma
```

stationary solution:

```math
\kappa=\frac{J_\kappa}{2C_\kappa},\quad \sigma=\frac{J_\sigma}{2C_\sigma}.
```

If `J_kappa=0`, then `kappa=0`.

For field models, derive Euler-Lagrange equations using SymPy calculus of variations where possible, or implement a radial Euler-Lagrange helper:

For density:

```math
\mathcal{L}(q,q',r)
```

Euler-Lagrange:

```math
\frac{\partial \mathcal{L}}{\partial q} - \frac{d}{dr}\frac{\partial \mathcal{L}}{\partial q'}=0.
```

API:

```python
ctx.energy.stationary_conditions(E)
ctx.energy.solve_stationary(E, assumptions=...)
ctx.energy.euler_lagrange(density, fields=[kappa(r), sigma(r)], coord=r)
```

### Boundary Conditions

Represent boundary conditions:

```python
@dataclass
class BoundaryCondition:
    id: str
    expression: sympy.Relational
    location: str | sympy.Expr
    description: str | None
```

Examples:

```math
\kappa(\infty)=0
```

```math
\sigma(\infty)=0
```

For algebraic models, boundary conditions may be used as assumptions. For differential equations, full solution with boundary conditions may not be automated initially; the software should record them and use them in reports.

## Mismatch Energy Analysis

Implement a dedicated mismatch module.

Definitions:

```math
\mu = \ln A + \ln B = 2\kappa.
```

Provide:

```python
ctx.mismatch.define_mu()
ctx.mismatch.energy(C)
ctx.mismatch.check_minimum(E)
```

For energy:

```math
E_{\text{mismatch}} = C \mu^2
```

stationary condition:

```math
\frac{\partial E}{\partial \mu}=2C\mu=0
```

with `C>0` gives `mu=0`.

The module should warn if `mu=0` appears only because the energy was defined as a penalty centered at `mu=0`. This is not necessarily invalid, but it is a possible assumption leak.

## Candidate Equation Search

### Candidate Family Representation

Represent candidate families as symbolic templates with coefficients.

```python
@dataclass
class CandidateFamily:
    id: str
    expression_template: sympy.Expr
    coefficients: list[sympy.Symbol]
    variables: list[sympy.Basic]
    constraints: list[sympy.Relational] = field(default_factory=list)
```

Example:

```python
E = c1*kappa**2 + c2*sigma**2 + c3*kappa*sigma - c4*Jk*kappa - c5*Js*sigma
family = CandidateFamily("quadratic_mode_energy", E, [c1,c2,c3,c4,c5], [kappa,sigma])
```

### Constraint Solving

Requirements produce algebraic constraints on coefficients.

Example requirement: unsourced `kappa` relaxes to zero when `Jk=0`.

Procedure:

1. Compute stationary solution.
2. Substitute `Jk=0`.
3. Require solution for `kappa` is zero.
4. Solve resulting coefficient constraints.

Use `sympy.solve`, `sympy.reduce_inequalities`, and `sympy.solve_univariate_inequality` where possible.

For complex cases, return conditions rather than forcing complete solution.

### Search Output

Return candidate solutions:

```python
@dataclass
class CandidateSolution:
    substitutions: dict[sympy.Symbol, sympy.Expr]
    conditions: list[sympy.Relational]
    passes: list[str]
    fails: list[str]
    undetermined: list[str]
```

### Avoiding Black-Box Search

Candidate search should remain transparent. The software should report which equations were solved and which constraints produced each coefficient relation.

## Requirement Validation

### Requirement Objects

Define a base class:

```python
@dataclass
class Requirement:
    id: str
    description: str
    target: sympy.Expr | sympy.Relational | None
    exactness: str = "exact"
    scope: str | None = None

    def validate(self, ctx: TheoryContext) -> ValidationResult:
        ...
```

Core validation result:

```python
@dataclass
class ValidationResult:
    requirement_id: str
    status: Literal["pass", "fail", "undetermined", "assumed"]
    message: str
    evidence: list[sympy.Expr]
    dependencies: list[str]
    scope: str | None = None
```

### Built-In Requirements

Implement built-ins:

- `ReciprocalScalingRequirement`;
- `KappaZeroRequirement`;
- `GammaEqualsOneRequirement`;
- `BetaEqualsOneRequirement`;
- `TraceFreeExchangeRequirement`;
- `TracefulCreationRequirement`;
- `PositiveEnergyRequirement`;
- `UnsourcedKappaMinimizesToZeroRequirement`;
- `NonzeroSigmaResponseRequirement`.

### Validation Engine

The validation engine should run all requirements against a context or candidate model.

```python
results = ctx.requirements.validate_all()
```

It should output:

- pass;
- fail;
- assumed;
- undetermined.

The distinction between pass and assumed is essential.

## Dependency Tracking

### Graph Model

Use `networkx.DiGraph`.

Nodes represent:

- symbols;
- definitions;
- assumptions;
- expressions;
- source laws;
- energy functionals;
- operations;
- results;
- validations.

Edges represent "depends on."

Node data:

```python
{
  "id": "result.gamma_v",
  "kind": "result",
  "status": "derived",
  "expr": gamma_v_value,
}
```

### Derivation Records

Every operation should create a derivation record.

```python
@dataclass
class DerivationRecord:
    id: str
    operation: str
    inputs: list[str]
    outputs: list[str]
    assumptions: list[str]
    details: dict[str, Any]
```

Examples:

```text
operation: "weak_field_expand"
inputs: ["metric.g00"]
assumptions: ["A_exponential"]
outputs: ["metric.g00_expanded_order2"]
```

### Dependency Queries

API:

```python
ctx.dependencies.of("result.gamma_v")
ctx.dependencies.tree("result.gamma_v")
ctx.dependencies.uses_assumption("result.gamma_v", "reciprocal_scaling")
ctx.dependencies.contains_target_leak("result.gamma_v")
```

## Assumption Leak Detection

### Target Conditions

Define target expressions:

```math
AB-1=0
```

```math
\kappa=0
```

```math
\gamma_v-1=0
```

```math
J_\kappa=0
```

### Direct Leak Detection

Scan assumptions and definitions for exact target equivalents.

Example:

- If an active assumption is `B = 1/A`, then reciprocal scaling is assumed.
- If `kappa = 0` is declared, then reciprocal scaling is assumed in mode form.
- If source law is explicitly `J_kappa = 0`, trace-free exchange is assumed.

Use simplification:

```python
def equivalent_to_target(expr, target):
    return simplify(lhs_minus_rhs(expr) - lhs_minus_rhs(target)) == 0
```

### Near Leak Detection

Detect expressions that are mathematically equivalent after transformation.

Examples:

- `a + b = 0`;
- `log(A) + log(B) = 0`;
- `mu = 0`;
- `B*A - 1 = 0`.

The target library should include equivalent forms.

### Reporting

Leak reports should say:

```text
Result AB=1 is present as assumption reciprocal_scaling_B_inverse_A.
Derivation cannot classify reciprocal scaling as derived unless this assumption is removed.
```

Do not block the calculation; annotate the result.

## Exact Versus Perturbative Reasoning

### Exactness Metadata

Every expression and result should include exactness metadata:

```python
class Exactness(str, Enum):
    EXACT = "exact"
    FIRST_ORDER = "first_order"
    SECOND_ORDER = "second_order"
    ORDER_N = "order_n"
    UNDETERMINED = "undetermined"
```

### Perturbative Expressions

Represent perturbative expressions as:

```python
@dataclass
class PerturbativeExpression:
    expr: sympy.Expr
    parameter: sympy.Expr
    order: int
    big_o_dropped: bool = True
```

For display, include `O(epsilon**n)` optionally.

### Validation

A requirement can specify exactness:

```python
Requirement(id="reciprocal_first_order", exactness="first_order")
Requirement(id="reciprocal_exact", exactness="exact")
```

The validation engine should not report an exact pass when only a first-order pass was shown.

## Redshift Exponential Analysis

Implement an analysis helper:

```python
ctx.ansatz.redshift_exponential()
```

This declares or tests:

```math
A=e^{\Phi/c^2}.
```

Then:

```python
metric = ctx.metric.from_scale_factors(A=exp(Phi/c**2), B=SymbolicOrDerived)
beta = ctx.ppn.extract_beta(metric)
```

If reciprocal scaling is active or derived:

```math
B=e^{-\Phi/c^2}
```

Then extract `gamma_v`.

The module should output:

- `beta` from temporal ansatz;
- `gamma_v` if `B` is known;
- whether both come from one ansatz.

## Candidate Structure Comparison

Create a `ModelComparison` object.

```python
@dataclass
class ModelSummary:
    id: str
    assumptions: list[str]
    source_classification: dict[str, str]
    gamma_v: sympy.Expr | None
    beta: sympy.Expr | None
    reciprocal_status: str
    exchange_creation_status: str
    positivity_status: str
    failed_requirements: list[str]
    undetermined_requirements: list[str]
```

Comparison API:

```python
comparison = compare_models([ctx1, ctx2, ctx3], requirements=standard_requirements)
comparison.to_markdown()
```

## Theory Ledger

### Ledger Entry

```python
@dataclass
class LedgerEntry:
    id: str
    statement: str
    status: Status
    expression: sympy.Basic | None = None
    dependencies: list[str] = field(default_factory=list)
    notes: str | None = None
```

### Ledger API

```python
ctx.ledger.add_definition(...)
ctx.ledger.add_postulate(...)
ctx.ledger.add_candidate_postulate(...)
ctx.ledger.add_target(...)
ctx.ledger.add_open_question(...)
ctx.ledger.update_status(...)
```

The ledger should not duplicate every expression record, but important scientific statements should be entered into it.

## Reporting System

### Markdown Reports

Use Jinja2 templates to generate markdown.

Report types:

- derivation report;
- validation report;
- model summary;
- dependency report;
- failure report;
- comparison report.

### Derivation Report Structure

A derivation report should include:

```text
# Derivation: gamma_v from reciprocal scaling

## Inputs
...

## Assumptions Used
...

## Steps
...

## Result
...

## Dependency Notes
...

## Assumption Leak Audit
...
```

### Rendering SymPy to Markdown

Use `sympy.latex(expr)` for equations.

Helper:

```python
def md_math(expr):
    return f"```math\n{latex(expr)}\n```"
```

For inline math, use `$...$`.

### Report API

```python
ctx.reports.derivation("result.gamma_v").to_markdown(path)
ctx.reports.validation().to_markdown(path)
```

## Failure Reports

Validation failures should include structured reasons.

```python
@dataclass
class FailureReason:
    code: str
    message: str
    evidence: list[sympy.Expr]
    suggestion: str | None = None
```

Examples:

- `KAPPA_SOURCED`;
- `GAMMA_REMAINS_FREE`;
- `POSITIVITY_UNDETERMINED`;
- `TARGET_ASSUMED`;
- `ONLY_FIRST_ORDER`;
- `COORDINATE_SCOPE_LIMITED`.

Failure reports are generated from validation results.

## Boundary Conditions

Boundary conditions are records attached to contexts and equations.

```python
ctx.boundaries.add("A_infinity", Eq(limit(A, r, oo), 1))
ctx.boundaries.add("kappa_infinity", Eq(limit(kappa, r, oo), 0))
```

SymPy may not solve limits for arbitrary functions. The boundary system should primarily record conditions and allow manual use as assumptions.

For differential equations, boundary conditions should appear in reports and dependency trees even when not solved automatically.

## Coordinate Scope

### Scope Records

```python
@dataclass
class ScopeRecord:
    id: str
    description: str
    assumptions: list[str]
```

Examples:

```text
ppn_weak_field
static_spherical_isotropic
two_dimensional_time_space_slice
```

Expressions and results should carry a `scope`.

Validation should fail or warn if a requirement expects a broader scope than the result provides.

Example:

```text
Warning: Trace-free result shown only in 2D time-space slice. 3+1 generalization remains open.
```

## Dimensional Checks

### Initial Strategy

SymPy's unit system can be cumbersome. Start with lightweight dimension tags in the symbol registry.

Example:

```python
ctx.symbols.define_constant("c", dimensions="L/T")
ctx.symbols.define_function("Phi", dimensions="L^2/T^2")
```

Implement a simple dimensional algebra parser:

- multiplication adds exponents;
- division subtracts exponents;
- powers multiply exponents;
- addition requires matching dimensions;
- exponentials/logs require dimensionless arguments.

Core check:

```python
ctx.dimensions.check_dimensionless(Phi/c**2)
ctx.dimensions.check_expression(E, expected="energy")
```

This can be expanded later.

### Required Checks

- `Phi/c**2` dimensionless;
- `log(A)` requires `A` dimensionless;
- `exp(Phi/c**2)` valid;
- `gamma_v` and `beta` dimensionless;
- energy functional density and integration measure combine to energy where possible.

## Notation Profiles

Implement notation profiles as context-level conventions.

```python
@dataclass
class NotationProfile:
    potential_symbol: str
    potential_sign: Literal["Phi_negative_in_well", "U_positive"]
    metric_signature: str
    spatial_metric_convention: str
```

Provide built-ins:

```python
NotationProfile.framework_phi()
NotationProfile.ppn_U()
```

Transformation between `Phi` and `U`:

```math
U=-\Phi
```

Reports should state the active notation profile.

## Persistence and Reproducible Sessions

### Serialization

Use YAML or JSON for session metadata and SymPy `srepr` or string expressions for expressions.

Recommended approach:

```python
sympy.srepr(expr)
```

for robust expression serialization, plus a readable LaTeX field for humans.

Session file structure:

```yaml
name: equal_response_static_exchange
symbols:
  c:
    kind: constant
    assumptions:
      positive: true
assumptions:
  - id: A_exponential
    expr_srepr: ...
expressions:
  - id: metric.g00
    expr_srepr: ...
ledger:
  ...
dependencies:
  edges:
    - [assumption.A_exponential, result.beta]
```

Provide:

```python
ctx.save("session.yaml")
ctx = TheoryContext.load("session.yaml")
```

### Reproducibility

A loaded session should reproduce validation results. Tests should cover round-trip serialization.

## Interactive Exploration

The Python API should support quick mutation.

Example:

```python
for p in [0, sympy.Rational(1,2), 1, 2]:
    model = base.copy()
    model.assumptions.add("B_power", Eq(B, A**(-p)))
    print(p, model.ppn.extract_gamma())
```

Provide convenience functions:

```python
ctx.clone()
ctx.with_assumption(...)
ctx.with_source(...)
```

Do not mutate the original unless explicitly requested.

## Candidate Family Templates

Implement templates as Python functions.

### Reciprocal Power Family

```python
def reciprocal_power_family(p):
    A = exp(Phi/c**2)
    B = A**(-p)
    return A, B
```

Predictions:

```math
\gamma_v=p
```

when `A=e^{Phi/c^2}`.

This is a useful sanity test.

### Exponential Scale Family

```python
A = exp(alpha*Phi/c**2)
B = exp(-lambda_*Phi/c**2)
```

Extract:

```math
\beta=\alpha^2
```

depending on normalization, and

```math
\gamma_v=\lambda
```

when the temporal first-order coefficient is normalized to `alpha=1`.

The extraction code should determine this symbolically.

### Quadratic Mode Energy

```python
E = c1*kappa**2 + c2*sigma**2 + c3*kappa*sigma
```

Check positivity and cross coupling.

### Source-Coupled Mode Energy

```python
E = c1*kappa**2 + c2*sigma**2 - Jk*kappa - Js*sigma
```

Solve stationary response.

## Target Library

Create a target library.

```python
@dataclass
class Target:
    id: str
    expression: sympy.Basic | sympy.Relational
    equivalent_forms: list[sympy.Basic | sympy.Relational]
    description: str
    status: Status
```

Initial targets:

- `A_first_order`;
- `B_first_order_equal_response`;
- `reciprocal_scaling`;
- `kappa_zero`;
- `gamma_v_one`;
- `beta_one`;
- `g00_second_order`;
- `gij_first_order`.

Target library supports assumption leak detection and validation.

## Open Question Tracking

Add open questions to ledger.

```python
ctx.ledger.add_open_question(
    id="derive_Jkappa_zero",
    statement="What deeper structure derives J_kappa = 0 for exchange?"
)
```

Open questions can link to failed validations and candidate models.

## Model Status Classification

Implement classifier rules.

Examples:

- if reciprocal scaling passes and no leak detected: `derives_equal_response`;
- if reciprocal scaling passes but leak detected: `assumes_equal_response`;
- if gamma remains symbolic: `leaves_gamma_free`;
- if positivity fails: `fails_positivity`;
- if all standard requirements pass but exchange separation assumed: `algebraically_consistent_with_candidate_postulate`.

Status classification should be conservative. Prefer `undetermined` to overclaiming.

## Minimal Counterexample Search

Implement small symbolic counterexample tools.

### Counterexample to "Postulate 2 forbids kappa"

Represent a density definition:

```math
\rho = E_v / V_{\text{proper}}
```

Let a conformal scale `kappa` rescale both numerator and denominator:

```math
E_v' = e^{n\kappa} E_v
```

```math
V_{\text{proper}}' = e^{n\kappa} V
```

Then:

```math
\rho'=\rho
```

while `kappa != 0`.

The tool can produce this as an algebraic counterexample.

### Counterexample to "exchange implies trace-free"

Represent total energy conservation:

```math
\Delta E_m + \Delta E_v = 0
```

Let vacuum energy go into both modes:

```math
\Delta E_v = E_\kappa + E_\sigma
```

Total conservation does not require `E_kappa=0`.

The software can show symbolic degrees of freedom remain.

Counterexample generation should be template-based, not general automated theorem proving.

## Theorem Candidate Promotion

Represent theorem candidates:

```python
@dataclass
class TheoremCandidate:
    id: str
    statement: str
    scope: str
    assumptions: list[str]
    supporting_results: list[str]
    counterexamples: list[str]
    status: Status = Status.PROVISIONAL
```

A theorem candidate can be generated from repeated validation success or manually added.

Example:

```text
exchange_trace_free
Statement: Local vacuum exchange sources only sigma, not kappa.
Scope: 2D weak-field mode space.
```

## 3+1 Generalization Support

The early system should not hard-code only two variables everywhere.

Design mode decomposition utilities to support arbitrary spatial dimensions later.

General structure:

```python
spatial_logs = [b1, b2, b3]
time_log = a
```

Define traces:

```math
\text{spatial trace}=b_1+b_2+b_3
```

Possible 3+1 trace modes and shear modes can be added later.

For now, 2D helpers can be implemented separately, but core source and energy classes should allow variable lists of arbitrary length.

## CLI Design

Initial CLI commands:

```text
vacuumforge new SESSION_NAME
vacuumforge validate SESSION.yaml
vacuumforge report SESSION.yaml --out report.md
vacuumforge compare SESSION1.yaml SESSION2.yaml --out comparison.md
```

CLI is optional but useful.

The CLI should call the same Python API used in notebooks.

## Notebook Usage

VacuumForge should be notebook-friendly.

Provide readable display helpers:

```python
ctx.display.expressions()
ctx.display.ledger()
ctx.display.validation_results(results)
```

In notebooks, use SymPy pretty printing and LaTeX.

## Testing Strategy

### Unit Tests

Test core algebraic operations:

- scale/log/mode transformations;
- source decomposition;
- reciprocal scaling checks;
- weak-field expansion;
- metric construction;
- gamma extraction;
- beta extraction;
- energy minimization;
- positivity checks;
- dependency graph creation;
- assumption leak detection.

### Golden Tests

Create known model tests.

#### Model 1: Reciprocal Exponential

Inputs:

```math
A=e^{\Phi/c^2},\quad B=e^{-\Phi/c^2}
```

Expected:

```math
AB=1
```

```math
\gamma_v=1
```

```math
\beta=1
```

#### Model 2: Parallel Scaling

Inputs:

```math
A=e^{\Phi/c^2},\quad B=e^{\Phi/c^2}
```

Expected:

```math
AB\neq1
```

```math
A/B=1
```

```math
\gamma_v=-1
```

or equivalent failure depending on convention.

#### Model 3: Free Gamma

Inputs:

```math
A=e^{\Phi/c^2},\quad B=e^{-\gamma_v\Phi/c^2}
```

Expected:

```math
\gamma_v=\gamma_v
```

reciprocal scaling only when `gamma_v=1`.

#### Model 4: Quadratic Source Energy

Inputs:

```math
E=C_\kappa\kappa^2+C_\sigma\sigma^2-J_\kappa\kappa-J_\sigma\sigma
```

Expected:

```math
\kappa=J_\kappa/(2C_\kappa)
```

If `J_kappa=0`, then `kappa=0`.

### Regression Tests

Every bug related to symbolic simplification or assumptions should get a regression test.

## Example API Session

A minimal equal-response derivation under assumed trace-free exchange:

```python
import sympy as sp
from vacuumforge import TheoryContext

ctx = TheoryContext("trace_free_exchange_demo")
ctx.define_standard_symbols()

A, B, Phi, c = ctx.A, ctx.B, ctx.Phi, ctx.c
kappa, sigma = ctx.kappa, ctx.sigma
Ck, Cs = sp.symbols("C_kappa C_sigma", positive=True)
Jk, Js = sp.symbols("J_kappa J_sigma")

ctx.assumptions.add("A_redshift", sp.Eq(A, sp.exp(Phi/c**2)))
ctx.sources.add_modes("static_exchange", J_kappa=0, J_sigma=Js)

E = Ck*kappa**2 + Cs*sigma**2 - Jk*kappa - Js*sigma
ctx.energy.add("quadratic_mode_energy", E, variables=[kappa, sigma])

solution = ctx.energy.solve_stationary("quadratic_mode_energy")
ctx.assumptions.add("trace_free_exchange", sp.Eq(Jk, 0))

ctx.validate("kappa_zero")
ctx.validate("reciprocal_scaling")

ctx.assumptions.add("B_from_kappa_zero", sp.Eq(B, 1/A))
metric = ctx.metric.from_scale_factors(A, B)

ctx.ppn.extract_gamma(metric)
ctx.ppn.extract_beta(metric)
ctx.reports.validation().to_markdown("report.md")
```

The report should clearly say that `J_kappa=0` was assumed unless derived elsewhere.

## Implementation Priorities by Need

This document does not define milestones, but the implementation naturally depends on core needs.

The foundational need is an inspectable symbolic context with variables, assumptions, expressions, and dependencies.

The equal-response need requires mode transformations, source decomposition, energy minimization, reciprocal checks, and PPN extraction.

The honesty need requires assumption leak detection, dependency tracking, validation status, and failure reports.

The research-productivity need requires candidate templates, comparison, persistence, and markdown export.

The future field-equation need requires the energy functional and Euler-Lagrange design to be extensible beyond algebraic models.

## Risks and Mitigations

### Risk: SymPy Simplification Is Inconsistent

SymPy may not automatically prove two equivalent expressions are equal.

Mitigation:

- use controlled simplification pipelines;
- support manual rewrite rules;
- report undetermined rather than false;
- keep exact and perturbative checks separate.

### Risk: Hidden Assumptions Enter Through Substitution

Mitigation:

- every substitution rule must be an assumption or definition record;
- all results record dependency on used substitutions;
- target leak detection audits assumptions.

### Risk: Coordinate Scope Gets Overstated

Mitigation:

- every result has scope metadata;
- validation warns when scope is narrower than target;
- reports include scope sections.

### Risk: Positivity Claims Are Too Strong

Mitigation:

- implement only local quadratic positivity at first;
- label global positivity as undetermined unless proven;
- require coefficient assumptions.

### Risk: Tool Becomes Too Abstract

Mitigation:

- include built-in templates for the equal-response problem;
- maintain a target library;
- provide direct workflows for `gamma_v`, `beta`, `AB=1`, and `J_kappa`.

## Summary

VacuumForge should be implemented as a Python/SymPy symbolic workbench centered on a `TheoryContext`.

Its core technical capabilities are:

- symbolic registry;
- assumption management;
- scale/log/mode transformations;
- reciprocal scaling checks;
- weak-field expansion;
- metric construction;
- PPN parameter extraction;
- source decomposition;
- exchange and creation source modeling;
- energy functional definition;
- positivity and minimization analysis;
- candidate equation search;
- requirement validation;
- dependency tracking;
- assumption leak detection;
- markdown reporting;
- reproducible sessions.

The central implementation principle is that every symbolic result must carry its inputs, assumptions, scope, and exactness.

VacuumForge should make it easy to ask:

```text
Did this equation derive kappa = 0, or did we put kappa = 0 in by hand?
```

That question is the technical heart of the software.
