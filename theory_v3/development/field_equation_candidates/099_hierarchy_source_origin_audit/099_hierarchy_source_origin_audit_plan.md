# 099_hierarchy_source_origin_audit — Plan

## Purpose

Group 099 follows Group 098's role audit.

Group 098 classified the determinant/Schur/parity hierarchy as:

```text
HIERARCHY_ROLE_AUXILIARY_ADMISSIBILITY_CANDIDATE
PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED
SOURCE_OR_FUNCTIONAL_ORIGIN_AUDIT_REQUIRED
```

The hierarchy remains mathematically valuable, but it is not yet physically assigned to `J_curv`, `H_curv`, `H_exch`, interface smoothing, total burden, a merger prediction, source law, or anti-singularity dynamics.

Group 099 asks the next necessary question:

```text
What source, variational, moment, projection, or boundary problem could produce the hierarchy matrix A_N?
```

This is not a full derivation. It is an origin audit. The goal is to identify which origin routes are plausible, which are currently unsupported, and what evidence would be required to upgrade the hierarchy from auxiliary admissibility to a physics-bearing object.

## Group Name

```text
099_hierarchy_source_origin_audit
```

## Central Question

```text
Is the hierarchy A_N currently traceable to a physical source/functional problem, or is its origin still unassigned?
```

## Starting State

Imported from Group 098:

```text
hierarchy role: auxiliary admissibility candidate;
physical ledger assignment deferred;
configuration-only assignment not licensed;
exchange-compensation assignment not licensed;
interface-smoothing assignment not licensed;
total-burden assignment not licensed;
source/functional origin audit required;
parent equation not ready;
recombination blocked.
```

Imported mathematical status from Groups 091–097:

```text
raw determinant positivity false;
determinant nonzero/invertibility target alive;
row-sign normalization works in tested range;
Schur complement route confirmed;
post-transition gap/ratio structure supported;
parity gap monotonicity and interlacing supported;
difference numerator positivity target identified.
```

## Candidate Origin Routes

Group 099 evaluates these possible origins:

### 1. Moment / Projection Origin

The hierarchy may arise from projecting a continuum response equation onto a basis of test functions or moments.

Evidence required:

```text
identified continuum residual R[y];
identified test/basis functions;
A_N entries derived as inner products or moment integrals;
right-hand side/source vector identified;
boundary conditions specified.
```

### 2. Variational Hessian Origin

The hierarchy may be the finite Hessian or Gram matrix of a quadratic expansion of a burden/configuration functional around a candidate minimum.

Evidence required:

```text
functional E[q] specified;
expansion variables q_i identified;
A_N = second variation / Hessian / Gram matrix;
positive/admissible sector defined;
source and constraints specified.
```

### 3. Interface Smoothing Origin

The hierarchy may encode finite-energy matching between a mass constraint and exterior source-free vacuum.

Evidence required:

```text
interior/interface/exterior domains identified;
matching conditions specified;
smoothness order specified;
A_N derived from interface basis constraints.
```

### 4. Exchange Compensation Origin

The hierarchy may encode substance/exchange compensation needed to make a configuration correction divergence-safe.

Evidence required:

```text
exchange current or density defined;
divergence equation written;
source separation from ordinary matter proved;
A_N derived from compensation conditions.
```

### 5. Total Burden Origin

The hierarchy may encode a combined ledger:

```text
J_curv + E_interface + E_exchange + ...
```

Evidence required:

```text
subledgers defined;
relative signs and units defined;
constraints specified;
A_N derived from total variation or balance equation.
```

### 6. Pure Auxiliary Origin

The hierarchy may currently be only a synthetic algebraic test system.

Evidence required:

```text
no physical derivation found;
objects remain useful as mathematical probes;
no physical claims attached.
```

## Expected Conservative Outcome

Likely safe result:

```text
MOMENT_PROJECTION_ORIGIN_PLAUSIBLE_BUT_UNDERDERIVED
VARIATIONAL_HESSIAN_ORIGIN_PLAUSIBLE_BUT_UNDERDERIVED
INTERFACE_ORIGIN_NOT_LICENSED
EXCHANGE_ORIGIN_NOT_LICENSED
TOTAL_BURDEN_ORIGIN_NOT_LICENSED
CURRENT_STATUS_ORIGIN_UNASSIGNED
HIERARCHY_REMAINS_AUXILIARY_ADMISSIBILITY_CANDIDATE
```

## What This Group May Do

Group 099 may:

```text
inspect the formula structure of A_N;
classify whether entries look like moment/projection integrals;
derive symbolic evidence for a moment-kernel reading;
build an evidence matrix for each origin route;
state minimum derivation requirements for physical upgrade;
recommend the next origin-building group.
```

## What This Group Must Not Do

Group 099 must not:

```text
claim A_N is derived from J_curv;
claim A_N is the Hessian of a real burden functional;
claim A_N is the exchange current equation;
claim A_N is an interface smoothing law;
claim determinant nonzero proves the physical field equation;
insert H_curv or H_exch;
write a parent equation;
claim merger-energy prediction;
claim anti-singularity dynamics;
open recombination.
```

## Recommended Script Batch

```text
candidate_source_origin_problem.py
candidate_hierarchy_formula_structure_inventory.py
candidate_origin_route_evidence_matrix.py
candidate_moment_projection_plausibility_probe.py
candidate_source_origin_decision_surface.py
candidate_group_099_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_source_origin_problem.py

Open Group 099 as a source/functional-origin audit.

### 2. candidate_hierarchy_formula_structure_inventory.py

Record the actual hierarchy matrix entry structure:

```text
A[k,j] = beta_moment(k+j) - ((2k-1)/(2k+3)) beta_moment(k+j-1)
beta_moment(s) = 768 / Π_{m=0..4}(2s+2m+1)
```

Classify the formula as moment-like, because entries depend on `k+j` and shifted `k+j-1`.

### 3. candidate_origin_route_evidence_matrix.py

Score each origin route against evidence requirements.

Expected:

```text
moment/projection: plausible structure but underderived;
variational Hessian: plausible only if symmetry/Gram/Hessian origin is shown;
interface: not licensed;
exchange: not licensed;
total burden: not licensed;
auxiliary admissibility: supported.
```

### 4. candidate_moment_projection_plausibility_probe.py

Try a purely formal moment-kernel interpretation.

Because:

```text
beta_moment(s) = 768 / Π(2s+odd constants)
```

looks like a Beta/Gamma-type moment sequence, attempt to solve for a simple integral representation of the form:

```text
beta_moment(s) = C ∫_0^1 x^(2s + a) (1-x^2)^b dx
```

or at least prove it has a moment-like rational structure.

This does not need to find the final physical measure. It should classify:

```text
MOMENT_STRUCTURE_SUPPORTED
PHYSICAL_MEASURE_NOT_DERIVED
```

### 5. candidate_source_origin_decision_surface.py

Classify the origin status:

```text
FORMULA_IS_MOMENT_LIKE
MOMENT_PROJECTION_ORIGIN_PLAUSIBLE_BUT_UNDERDERIVED
VARIATIONAL_HESSIAN_ORIGIN_NOT_YET_LICENSED
INTERFACE_ORIGIN_NOT_LICENSED
EXCHANGE_ORIGIN_NOT_LICENSED
TOTAL_BURDEN_ORIGIN_NOT_LICENSED
SOURCE_ORIGIN_REMAINS_OPEN
```

### 6. candidate_group_099_status_summary.py

Close the group and recommend next work.

Likely next groups:

```text
100_moment_projection_derivation_attempt
100_difference_numerator_factorization_attempt
100_burden_functional_minimum_requirements
```

## Key Success Criteria

Group 099 must produce:

```text
a formula inventory for A_N;
an origin-route evidence matrix;
a moment/projection plausibility test;
a conservative origin decision surface;
a concrete next recommendation.
```

## Recommended Next Group

If moment structure is supported:

```text
100_moment_projection_derivation_attempt
```

This would try to derive `A_N` from an explicit residual/projection problem.

If the user wants to continue pure math:

```text
100_difference_numerator_factorization_attempt
```

If physical formulation is prioritized:

```text
100_burden_functional_minimum_requirements
```

## Final Interpretation

Group 099 asks:

```text
Where did the matrix come from?
```

Goblin discipline:

```text
A key without a lock is still useful,
but a key with a known lock becomes a tool.
```
