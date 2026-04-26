# VacuumForge Feature Design

## Purpose

VacuumForge is a symbolic research workbench for exploring candidate mathematical structures in a vacuum-based theory of gravity.

The software exists to help formalize, test, and compare candidate equations, mode decompositions, source laws, and energy functionals. It is designed for theory development: the user proposes symbolic structures, expresses postulates as constraints, and asks what follows.

VacuumForge does not decide which physical theory is true. It helps determine whether a proposed mathematical structure actually implies the consequences it is claimed to imply.

The immediate scientific need is the equal-response problem: determining whether the reciprocal scale relation

```math
A(r)B(r)=1
```

can be derived from vacuum exchange, source structure, and configuration-energy minimization rather than assumed.

## Core Concepts

VacuumForge should treat the following as first-class conceptual objects.

### Scale Factors

VacuumForge should support symbolic scale factors such as

```math
A(r)=\sqrt{-g_{00}},
```

```math
B(r)=\sqrt{g_{ii}}.
```

These represent temporal and spatial metric response in a weak-field, PPN-compatible coordinate setting.

The software should allow scale factors to be defined abstractly, expanded perturbatively, related to potentials, and transformed into other variable systems.

### Logarithmic Variables

VacuumForge should support logarithmic scale variables

```math
a=\ln A,
```

```math
b=\ln B.
```

These are useful because reciprocal scaling becomes linear:

```math
A B = 1
```

is equivalent to

```math
a+b=0.
```

The software should allow users to move cleanly between scale-factor form and logarithmic form.

### Mode Variables

VacuumForge should support the mode decomposition

```math
\kappa=\frac{a+b}{2},
```

```math
\sigma=\frac{a-b}{2}.
```

Here `kappa` represents the conformal cell mode, while `sigma` represents the reciprocal time-space shear mode.

The software should treat this decomposition as a central working representation for the equal-response problem.

### Sources

VacuumForge should support symbolic source components such as

```math
J_a, \quad J_b,
```

and their mode decompositions

```math
J_\kappa = J_a + J_b,
```

```math
J_\sigma = J_a - J_b.
```

The tool should distinguish source structures that are trace-free from source structures that are traceful.

### Energy Functionals

VacuumForge should support symbolic energy functionals over vacuum modes. These may include terms involving fields, gradients, potentials, source couplings, and mode-mismatch penalties.

The software should support asking whether a proposed energy functional is positive, whether a mode is sourced or unsourced, and whether minimization drives specific modes to zero.

### Candidate Laws

VacuumForge should allow users to define candidate laws, assumptions, constraints, and postulates as symbolic statements.

These may include:

- reciprocal scaling;
- trace-free exchange;
- traceful creation;
- positivity of configuration energy;
- local density constancy;
- source conservation;
- exchange-creation separation;
- weak-field recovery conditions;
- PPN parameter targets.

Candidate laws should be testable against symbolic structures rather than merely recorded as prose.

## Feature: Symbolic Variable Registry

VacuumForge should provide a way to define and organize symbolic variables used in a theory model.

The user should be able to define variables such as:

- coordinates: `r`, `t`, `x`, `theta`, `phi`;
- constants: `c`, `G`, `M`;
- potentials: `Phi(r)`;
- scale factors: `A(r)`, `B(r)`;
- log variables: `a(r)`, `b(r)`;
- modes: `kappa(r)`, `sigma(r)`;
- sources: `J_a`, `J_b`, `J_kappa`, `J_sigma`;
- coefficients: `gamma_v`, `beta`, stiffness constants, coupling constants.

The registry should track what each variable represents mathematically and conceptually.

A user should be able to inspect the current variable set and see definitions, assumptions, dependencies, and physical interpretation notes.

## Feature: Assumption Management

VacuumForge should allow assumptions to be declared explicitly.

Examples include:

```math
c>0,
```

```math
G>0,
```

```math
M>0,
```

```math
|\Phi|/c^2 \ll 1.
```

It should also support theory-specific assumptions, such as:

```math
A=e^{\Phi/c^2},
```

```math
B=1/A,
```

```math
J_\kappa=0.
```

Assumptions should be visible, inspectable, and removable.

The software should make it clear when a result depends on an assumption. If a user derives `gamma_v = 1`, the tool should be able to report whether that result followed from a source law, an energy functional, a boundary condition, or an explicit assumption that already contained the result.

The purpose of assumption management is to prevent hidden assumptions from entering derivations unnoticed.

## Feature: Scale-Factor Transformations

VacuumForge should support transformations among the main weak-field variable systems.

The user should be able to convert between:

```math
(A,B)
```

```math
(a,b)
```

```math
(\kappa,\sigma).
```

The software should know that:

```math
a = \ln A,
```

```math
b = \ln B,
```

```math
\kappa = \frac{a+b}{2},
```

```math
\sigma = \frac{a-b}{2},
```

and the inverse relations:

```math
a = \kappa + \sigma,
```

```math
b = \kappa - \sigma,
```

```math
A = e^{\kappa+\sigma},
```

```math
B = e^{\kappa-\sigma}.
```

The user should be able to enter an expression in one representation and ask VacuumForge to rewrite it in another.

This is essential for seeing whether a candidate law is really about `A` and `B`, about `a` and `b`, or about the modes `kappa` and `sigma`.

## Feature: Reciprocal Scaling Checks

VacuumForge should provide built-in checks for reciprocal scaling.

The software should be able to determine whether a candidate structure implies any of the equivalent conditions:

```math
A B = 1,
```

```math
\ln A + \ln B = 0,
```

```math
a+b=0,
```

```math
\kappa=0,
```

```math
B=1/A.
```

The user should be able to ask:

- Does this source law imply reciprocal scaling?
- Does this energy functional minimize at reciprocal scaling?
- Does reciprocal scaling follow only after imposing a boundary condition?
- Does reciprocal scaling follow only because it was assumed?
- Does the result hold exactly or only to first order?
- Does the result survive second-order expansion?

The output should clearly distinguish exact identities from perturbative results.

## Feature: Weak-Field Expansion

VacuumForge should support weak-field expansions in powers of

```math
\epsilon = \Phi/c^2.
```

The user should be able to expand scale factors, metric components, source laws, and energy functionals to a requested order.

Examples:

```math
A=e^{\Phi/c^2}
```

expands as

```math
A = 1 + \frac{\Phi}{c^2} + \frac{1}{2}\frac{\Phi^2}{c^4}+\cdots.
```

```math
g_{00}=-A^2=-e^{2\Phi/c^2}
```

expands as

```math
g_{00}= -\left(1+2\frac{\Phi}{c^2}+2\frac{\Phi^2}{c^4}+\cdots\right).
```

VacuumForge should allow users to specify expansion order and compare coefficients.

This feature is needed to extract weak-field parameters such as `gamma_v` and `beta`.

## Feature: Metric Construction

VacuumForge should construct weak-field metric components from scale factors.

Given `A` and `B`, the tool should produce:

```math
g_{00} = -A^2,
```

```math
g_{ij} = B^2\delta_{ij}
```

in the isotropic weak-field setting.

The user should be able to inspect metric components exactly or in weak-field expansion.

The software should also support parameterized metric forms such as:

```math
g_{00}\approx -\left(1+2\frac{\Phi}{c^2}+2\beta\frac{\Phi^2}{c^4}\right),
```

```math
g_{ij}\approx \left(1-2\gamma_v\frac{\Phi}{c^2}\right)\delta_{ij}.
```

VacuumForge should compare constructed metrics against these target forms and solve for parameters where possible.

## Feature: PPN Parameter Extraction

VacuumForge should extract weak-field PPN-style parameters from candidate metric expressions.

At minimum, it should identify:

```math
\gamma_v
```

from the first-order spatial metric response, and

```math
\beta
```

from the second-order temporal metric response.

The user should be able to ask:

- What `gamma_v` does this candidate structure predict?
- What `beta` does this candidate structure predict?
- Are the predicted values exact or perturbative?
- Which assumptions were required to obtain them?
- Does the candidate reproduce `gamma_v = 1`?
- Does the candidate reproduce `beta = 1`?
- Are `gamma_v = 1` and `beta = 1` consequences of one shared ansatz?

This feature should make the relationship between reciprocal exponential scaling and weak-field GR recovery explicit.

## Feature: Source Decomposition

VacuumForge should support source decomposition in scale and mode variables.

Given source components

```math
J_a, \quad J_b,
```

the software should compute:

```math
J_\kappa = J_a + J_b,
```

```math
J_\sigma = J_a - J_b.
```

It should classify sources as:

- trace-free if `J_kappa = 0`;
- pure trace if `J_sigma = 0`;
- mixed if both components are nonzero.

The user should be able to define candidate source laws and ask how they decompose.

This is a core feature because the equal-response problem becomes the question of whether static gravitational exchange sources `sigma` without sourcing `kappa`.

## Feature: Exchange Source Modeling

VacuumForge should allow users to define candidate exchange source laws.

Exchange sources represent local redistribution between matter energy and vacuum configuration energy. They are not assumed automatically to be trace-free unless the user imposes or derives that condition.

The software should support questions such as:

- Does this exchange source imply `J_kappa = 0`?
- Does this exchange source conserve total energy?
- Does this exchange source conserve any channel-like quantity?
- Does this exchange source deposit energy into `sigma`, `kappa`, or both?
- Does this source require an additional trace-free assumption?
- Is trace-free exchange an input or an output?

The tool should help identify whether a proposed exchange model genuinely derives Exchange-Creation Separation or merely restates it.

## Feature: Creation Source Modeling

VacuumForge should allow users to define candidate creation source laws.

Creation sources represent new vacuum content rather than local exchange. The software should support uniform creation, localized creation, and parameterized creation profiles.

The user should be able to ask:

- Does this creation source excite `kappa`?
- Is the creation traceful?
- Does the source preserve local density if applied uniformly?
- Does localized creation violate a declared constant-density condition?
- How does creation differ structurally from exchange?

This feature is needed to model the distinction between static gravity and cosmic expansion.

## Feature: Exchange-Creation Separation Tests

VacuumForge should provide direct tests for the candidate principle:

```math
\text{exchange} \Rightarrow J_\kappa=0,
```

```math
\text{creation} \Rightarrow J_\kappa\neq0.
```

The user should be able to evaluate whether a proposed model satisfies:

- local exchange is trace-free;
- creation is traceful;
- static gravity is represented by exchange;
- cosmic expansion is represented by creation;
- reciprocal scaling follows for static gravity;
- traceful expansion remains allowed.

The software should report which parts are derived and which parts are imposed.

This feature is central to determining whether Exchange-Creation Separation should become a postulate, a theorem, or remain an observationally motivated closure.

## Feature: Energy Functional Definition

VacuumForge should allow users to define symbolic configuration-energy functionals.

These may include terms such as:

```math
C_\kappa \kappa^2,
```

```math
C_\sigma \sigma^2,
```

```math
K_\kappa (\nabla\kappa)^2,
```

```math
K_\sigma (\nabla\sigma)^2,
```

```math
J_\kappa \kappa,
```

```math
J_\sigma \sigma.
```

The user should be able to build energy functionals in mode variables or scale variables.

The software should support inspecting what modes appear, whether terms are positive under declared assumptions, and whether source couplings are trace-free, traceful, or mixed.

## Feature: Positivity Checks

VacuumForge should help check whether a candidate configuration-energy expression is positive or bounded below under stated assumptions.

The software should support questions such as:

- Is the `kappa` energy positive?
- Is the `sigma` energy positive?
- Are there cross terms that make the energy indefinite?
- Does the energy have a minimum at `kappa = 0`?
- Does the energy have flat directions?
- Does the functional permit runaway behavior?
- What coefficient assumptions are required for positivity?

This feature is important because Postulate 4 requires non-flat configurations to carry positive configuration energy.

VacuumForge should not claim global mathematical positivity where it cannot prove it. It should distinguish between local quadratic positivity, assumed positivity, and proven positivity under specified coefficient constraints.

## Feature: Minimization and Stationary Conditions

VacuumForge should derive stationary conditions from candidate energy functionals.

For algebraic models, the software should compute partial derivatives such as:

```math
\frac{\partial E}{\partial \kappa}=0,
```

```math
\frac{\partial E}{\partial \sigma}=0.
```

For field models, it should express Euler-Lagrange-style conditions symbolically.

The user should be able to ask:

- What equations follow from minimizing this energy?
- What is the equilibrium value of `kappa`?
- What is the equilibrium value of `sigma`?
- Does unsourced `kappa` relax to zero?
- Does sourced `sigma` remain nonzero?
- What boundary conditions are needed?
- Are there multiple extrema?
- Which extrema are stable?

This feature connects Postulate 4 and Postulate 5 to symbolic equations.

## Feature: Mismatch Energy Analysis

VacuumForge should specifically support mismatch-energy analysis for the reciprocal-scaling target.

The mismatch variable is

```math
\mu = \ln A + \ln B = 2\kappa.
```

The software should allow candidate terms such as:

```math
E_{\text{mismatch}} = \int C(r)\mu(r)^2\,d^3x,
```

or equivalent `kappa` terms.

The user should be able to ask:

- Does this mismatch term force `mu = 0`?
- Is the mismatch term independent or derived from another energy structure?
- Does it simply encode reciprocal scaling by hand?
- What happens if a source term couples to `mu`?
- What happens if creation sources `mu` uniformly?
- What coefficient assumptions are required?

The goal is to determine whether mismatch energy is an explanatory structure or just a restatement of the desired outcome.

## Feature: Candidate Equation Search

VacuumForge should support structured search over families of candidate equations.

The user should be able to define a family such as:

```math
E = c_1\kappa^2 + c_2\sigma^2 + c_3\kappa\sigma + c_4 J_\kappa\kappa + c_5J_\sigma\sigma.
```

The software should solve for coefficient constraints under requirements such as:

- positive energy;
- no unsourced `kappa`;
- nonzero `sigma` response to static exchange;
- reciprocal scaling;
- traceful creation response;
- weak-field recovery.

The tool should return candidate coefficient families that satisfy the constraints, along with assumptions needed.

Candidate search should be constrained and transparent. It should not produce uninterpretable equation lists without showing why they satisfy the requirements.

## Feature: Requirement-Based Validation

VacuumForge should allow users to define requirements that candidate structures must satisfy.

Examples:

```text
R1: Static exchange must imply J_kappa = 0.
R2: Unsourced kappa must minimize to zero.
R3: Nonzero J_sigma must produce nonzero sigma.
R4: The relaxed static solution must imply A B = 1.
R5: The weak-field metric must give gamma_v = 1.
R6: The second-order time metric must give beta = 1.
R7: Uniform creation may source kappa.
```

The user should be able to run a candidate model against a set of requirements and receive a pass/fail/undetermined report.

Each result should include supporting symbolic reasoning.

If a requirement is satisfied only because it was assumed, the report should say so.

## Feature: Dependency Tracking

VacuumForge should track dependency chains.

If a result is derived, the software should record what definitions, assumptions, source laws, equations, boundary conditions, and simplification rules were used.

For example:

```text
Result: gamma_v = 1
Depends on:
- A = exp(Phi/c^2)
- exchange source rule J_kappa = 0
- positive kappa energy
- boundary condition kappa(infinity)=0
- minimization of unsourced kappa
```

The user should be able to inspect dependency trees for important results.

This feature is essential because the framework distinguishes derived results, provisional assumptions, and observational closures.

## Feature: Assumption Leak Detection

VacuumForge should help detect when a desired result has been inserted into a candidate model under another name.

Examples of possible assumption leaks:

- defining `B = 1/A` and then claiming reciprocal scaling was derived;
- defining a mismatch energy with an unexplained minimum at `AB = 1`;
- imposing `J_kappa = 0` while claiming trace-free exchange was derived;
- using a metric already equivalent to `gamma_v = 1`;
- choosing coefficient constraints that secretly encode the desired result.

The software should flag direct and near-direct restatements of target conditions when possible.

This feature should not accuse the user of error. It should present an audit trail: which inputs already contain the target structure, and which results follow independently.

## Feature: Exact vs Perturbative Reasoning

VacuumForge should clearly distinguish exact identities from perturbative approximations.

For example:

```math
A B = 1
```

may hold exactly, while

```math
A B \approx 1
```

may hold only to first order in `Phi/c^2`.

The user should be able to specify whether a requirement is exact, first-order, second-order, or all-orders under a given ansatz.

The software should report results with their perturbative scope.

This is important because the framework's first-order `gamma_v` problem and second-order `beta` problem may be connected but are not identical unless an all-order ansatz is assumed or derived.

## Feature: Redshift Exponential Analysis

VacuumForge should support analysis of the redshift exponential ansatz:

```math
A=e^{\Phi/c^2}.
```

The user should be able to inspect consequences of this ansatz for:

```math
g_{00}=-A^2,
```

```math
\beta,
```

and, if reciprocal scaling is added or derived,

```math
B=e^{-\Phi/c^2},
```

```math
g_{ij}=B^2\delta_{ij}.
```

The software should help determine whether `beta = 1` follows from the temporal ansatz and whether `gamma_v = 1` follows only with reciprocal scaling.

This feature supports the possible unification of the two provisional weak-field assumptions.

## Feature: Comparison of Candidate Structures

VacuumForge should allow multiple candidate models to be compared.

For each candidate, the software should show:

- variables used;
- source rules;
- energy functional;
- assumptions;
- derived equilibrium equations;
- predicted `gamma_v`;
- predicted `beta`;
- whether reciprocal scaling follows;
- whether exchange-creation separation is derived or assumed;
- which requirements pass, fail, or remain undetermined.

This comparison should help the user decide which mathematical structures are worth developing further.

## Feature: Theory Ledger

VacuumForge should maintain a theory ledger that classifies statements by status.

Possible statuses include:

- definition;
- postulate;
- candidate postulate;
- assumption;
- derived result;
- provisional result;
- observational constraint;
- failed derivation;
- open question.

The ledger should make it clear whether a statement is being used as an input or obtained as an output.

For example:

```text
AB = 1
Status: target result

J_kappa = 0 for exchange
Status: candidate postulate or derived result, depending on model

gamma_v = 1
Status: derived if AB = 1 follows; otherwise observational constraint
```

This feature mirrors the framework's document taxonomy and helps prevent conceptual drift.

## Feature: Human-Readable Derivation Reports

VacuumForge should generate human-readable reports for symbolic derivations.

A report should explain:

- what was assumed;
- what was derived;
- what transformations were used;
- where the result depends on a candidate law;
- whether the target was derived, assumed, or left undetermined.

The reports should be suitable for inclusion in theory notes, process documents, or README-style explanations.

They should avoid implementation details and focus on the mathematical reasoning.

## Feature: Failure Reports

VacuumForge should treat failed derivations as valuable outputs.

When a candidate structure fails, the software should report why.

Examples:

```text
Failure: kappa does not relax to zero because the energy functional contains a nonzero J_kappa source.
```

```text
Failure: reciprocal scaling holds only to first order; second-order terms leave AB != 1.
```

```text
Failure: positivity requires C_kappa > 0, but the candidate constraints allow C_kappa < 0.
```

```text
Failure: gamma_v remains free.
```

Failure reports should help guide theory development by narrowing the search space.

## Feature: Boundary Condition Handling

VacuumForge should allow users to declare boundary conditions relevant to weak-field static problems.

Examples:

```math
A(\infty)=1,
```

```math
B(\infty)=1,
```

```math
\kappa(\infty)=0,
```

```math
\sigma(\infty)=0.
```

The software should distinguish between results that follow from local equations and results that require boundary conditions.

This is especially important for statements like:

```math
J_\kappa=0 \Rightarrow \kappa=0.
```

That implication generally requires both positive energy and appropriate boundary behavior.

## Feature: Coordinate Scope Annotation

VacuumForge should allow users to mark a calculation's coordinate or gauge scope.

For early work, many calculations live in PPN-compatible weak-field coordinates. The software should make that explicit.

A result should be annotated as applying to a scope such as:

```text
PPN-compatible weak-field coordinates
```

or

```text
static spherically symmetric isotropic coordinates
```

or

```text
2D time-space slice
```

This prevents a result from being mistaken for a fully coordinate-invariant theorem before the theory has earned that level of generality.

## Feature: Dimensional and Unit Checks

VacuumForge should support basic dimensional checks for expressions involving physical quantities.

It should help verify that expressions such as

```math
\Phi/c^2
```

are dimensionless, that energy functionals have units of energy, and that source terms have compatible dimensions.

This feature is useful for catching invalid candidate equations early.

## Feature: Notation Profiles

VacuumForge should allow notation conventions to be defined and reused.

For example, the framework may use:

```math
\Phi<0
```

inside a gravitational well, with

```math
\Phi=-GM/r.
```

Other contexts may use

```math
U=GM/r>0.
```

The software should help avoid sign errors by allowing a model to declare its potential convention.

This is important because weak-field expansions and PPN comparisons are sensitive to sign conventions.

## Feature: Documentation Export

VacuumForge should support exporting definitions, assumptions, derivations, and validation reports into markdown.

The exported material should be suitable for project documentation.

Outputs may include:

- symbolic definitions;
- mode decompositions;
- candidate source laws;
- energy functionals;
- derivation summaries;
- requirement validation tables;
- dependency lists;
- open questions.

This feature supports the framework's document-driven research style.

## Feature: Interactive Exploration

VacuumForge should support interactive theory exploration.

A user should be able to change a source rule, coefficient, or assumption and immediately see how derived results change.

Example questions:

- What happens if exchange has a small `kappa` component?
- What happens if `B = A^{-p}`?
- What value of `p` gives `gamma_v = 1`?
- What value of `p` gives `beta = 1`?
- Does a cross term `kappa sigma` destabilize the minimum?
- Does uniform creation source only `kappa`?

The goal is to make mathematical exploration fast enough that the user can follow conceptual threads without getting bogged down in manual algebra.

## Feature: Candidate Family Templates

VacuumForge should provide reusable templates for common candidate families.

Examples:

### Reciprocal Power Family

```math
B=A^{-p}.
```

This family allows the user to test how different reciprocal strengths affect `gamma_v`.

### Exponential Scale Family

```math
A=e^{\alpha \Phi/c^2},
```

```math
B=e^{-\lambda \Phi/c^2}.
```

This family allows comparison of temporal and spatial response coefficients.

### Quadratic Mode Energy

```math
E=c_1\kappa^2+c_2\sigma^2+c_3\kappa\sigma.
```

This family tests positivity and mode coupling.

### Source-Coupled Mode Energy

```math
E=c_1\kappa^2+c_2\sigma^2-J_\kappa\kappa-J_\sigma\sigma.
```

This family tests equilibrium response to trace and shear sources.

Templates should be starting points, not fixed theories.

## Feature: Target Library

VacuumForge should maintain a library of target results the theory may attempt to derive.

Initial targets include:

```math
A \approx 1+\Phi/c^2,
```

```math
B \approx 1-\Phi/c^2,
```

```math
A B = 1,
```

```math
\kappa = 0,
```

```math
\gamma_v = 1,
```

```math
\beta = 1,
```

```math
g_{00}\approx -\left(1+2\Phi/c^2+2\Phi^2/c^4\right),
```

```math
g_{ij}\approx \left(1-2\Phi/c^2\right)\delta_{ij}.
```

The library should also store whether each target is currently treated as derived, assumed, provisional, or observationally required.

## Feature: Open Question Tracking

VacuumForge should allow open questions to be attached to models and results.

Examples:

- What deeper structure derives `J_kappa = 0` for exchange?
- Is `kappa` physical or gauge in this formulation?
- What is the 3+1-dimensional generalization of trace-free exchange?
- Does the candidate source law suppress scalar gravitational wave modes?
- Does the same structure derive both `gamma_v = 1` and `beta = 1`?
- What boundary conditions are physically justified?

Open-question tracking helps keep the research program honest about what remains unresolved.

## Feature: Model Status Classification

VacuumForge should classify candidate models by their scientific status.

Possible statuses include:

- exploratory;
- algebraically consistent;
- satisfies equal-response;
- derives equal-response;
- assumes equal-response;
- fails positivity;
- leaves `gamma_v` free;
- predicts wrong weak-field limit;
- requires new postulate;
- candidate for deeper development.

This classification helps distinguish models that merely reproduce desired outputs from models that explain them.

## Feature: Reproducible Sessions

VacuumForge should make symbolic sessions reproducible.

A user should be able to save:

- variable definitions;
- assumptions;
- candidate equations;
- requirements;
- derivation steps;
- results;
- reports.

A saved session should allow the same symbolic reasoning to be revisited later.

This matters because the theory is document-driven and evolves over time. Results need to remain auditable.

## Feature: Error and Ambiguity Reporting

VacuumForge should report ambiguity rather than hide it.

Examples:

```text
Cannot determine whether expression is positive without assumptions on C_kappa.
```

```text
Cannot decide whether kappa is unsourced because J_kappa has not been defined.
```

```text
gamma_v remains symbolic.
```

```text
Result depends on coordinate scope.
```

```text
Expression simplifies to target only at first order.
```

Ambiguity reports should be treated as useful guidance.

## Feature: Minimal Counterexample Search

VacuumForge should help find counterexamples to proposed derivations.

For example, if the user claims that Postulate 2 forbids `kappa`, the software should help construct a symbolic case where `kappa != 0` while local density remains constant under a specified density definition.

If the user claims exchange implies trace-free sourcing, the software should help construct a source that conserves total energy while still producing nonzero `J_kappa`.

This feature is important because failed derivations often reveal exactly what new principle is needed.

## Feature: Theorem Candidate Promotion

VacuumForge should support promoting a repeated symbolic result into a theorem candidate.

For example, if many candidate structures satisfying a deeper rule also produce `J_kappa = 0`, the user may mark:

```text
Exchange sources are trace-free.
```

as a theorem candidate.

The software should store:

- statement;
- scope;
- required assumptions;
- supporting models;
- known counterexamples;
- unresolved issues.

This helps the framework distinguish promising structural results from one-off algebraic coincidences.

## Feature: Support for Future 3+1 Generalization

Although the initial equal-response problem is naturally expressed in a 2D time-space slice, VacuumForge should be conceptually prepared for 3+1 generalization.

The software should eventually support:

- three spatial scale factors;
- trace and trace-free decompositions in higher dimensions;
- isotropic and anisotropic spatial response;
- tensor-mode decomposition;
- scalar/breathing mode identification;
- comparison to gravitational-wave polarization expectations.

The early design should avoid hard-coding assumptions that make 3+1 extension impossible.

## Feature: User Workflow

A typical VacuumForge workflow should look like this:

1. Define the symbolic context.
2. Declare variables and assumptions.
3. Choose a coordinate or mode representation.
4. Define source rules.
5. Define an energy functional.
6. Derive equilibrium equations.
7. Apply boundary conditions.
8. Check reciprocal scaling.
9. Extract weak-field parameters.
10. Validate requirements.
11. Inspect dependencies.
12. Export a derivation report.
13. Record open questions.

The tool should support this workflow without requiring the user to prematurely commit to a final theory.

## Success Criteria

VacuumForge is successful if it helps answer questions of the following form:

- Does this candidate equation derive `AB = 1`, or assume it?
- What extra principle is needed to make `J_kappa = 0` follow?
- Can exchange and creation be distinguished mathematically?
- Which energy functionals make `kappa` an unsourced positive-energy mode?
- Does one ansatz explain both `gamma_v = 1` and `beta = 1`?
- Which candidate structures fail, and why?
- What is the minimal mathematical structure needed to turn the current provisional weak-field recovery into a derivation?

The software is valuable even when it disproves candidate paths. A clean failure can be as important as a successful derivation, because it tells the theory where new structure is genuinely required.

## Non-Goals

VacuumForge should not attempt to do everything at once.

It is not intended to be:

- a complete general relativity package;
- a numerical relativity simulator;
- a cosmology simulator;
- an automatic physics-discovery engine;
- a replacement for human judgment;
- a proof assistant for full formal mathematics;
- a final arbiter of physical truth.

Its role is narrower and more useful: symbolic exploration and validation of candidate vacuum field structures.

## Summary

VacuumForge is a tool for making speculative theory-building mathematically disciplined.

It gives the framework a place to test candidate source laws, energy functionals, and mode equations against the equal-response problem and related weak-field targets.

Its central question is:

```text
What mathematical structure makes static vacuum exchange source sigma but not kappa?
```

If VacuumForge can help answer that question, it will help move the framework from provisional weak-field compatibility toward genuine field equations.
