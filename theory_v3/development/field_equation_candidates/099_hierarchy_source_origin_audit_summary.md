# Group 099 Summary: Hierarchy Source Origin Audit

## Purpose

Group 099 followed the Group 098 role audit.

Group 098 concluded that the determinant/Schur hierarchy is currently an:

```text
AUXILIARY_ADMISSIBILITY_CANDIDATE
```

and that physical ledger assignment is deferred.

Group 099 asked:

```text
What source, variational, moment, projection, or boundary problem could produce A_N?
```

## Main Result

Group 099 is successful as a source-origin audit.

Stable result:

```text
A_N formula is moment-like;

beta_moment has a beta-type moment-integral structure;

moment/projection origin is plausible but underderived;

variational Hessian origin is not licensed;

interface origin is not licensed;

exchange origin is not licensed;

total burden origin is not licensed;

source origin remains open;

hierarchy remains auxiliary admissibility candidate;

parent equation remains not ready;

recombination remains blocked.
```

## Important Archive Caveat

The Group 099 output includes dependency warnings for:

```text
g098_summary
```

This appears to be caused by the transition from two-digit to three-digit group naming. It should be treated as an archive/rename dependency issue, not as a substantive failure of the Group 099 scripts.

The substantive Group 099 dependencies among `g099_*` scripts are satisfied.

## What We Actually Learned

The strongest result is the beta-integral identity.

The hierarchy uses:

```text
beta_moment(s)
=
768 / [(2s+1)(2s+3)(2s+5)(2s+7)(2s+9)].
```

Group 099 shows:

```text
beta_moment(s)
=
2 ∫_0^1 x^(2s) (1-x^2)^4 dx.
```

So the hierarchy is not merely “kind of moment-like.” Its base sequence is literally a weighted even-moment sequence.

The matrix entries also simplify to:

```text
A[k,j]
=
1536(4j - 6k + 3)
/
[
(2k+3)
(2j+2k-1)
(2j+2k+1)
(2j+2k+3)
(2j+2k+5)
(2j+2k+7)
(2j+2k+9)
].
```

This gives the next derivation attempt a concrete object to explain.

## Script-Level Analysis

### 1. Source Origin Problem

The opener correctly asks where `A_N` comes from.

It blocks premature assignments:

```text
A_N as J_curv;
A_N as H_exch;
A_N as total burden;
parent equation jump.
```

### 2. Formula Structure Inventory

The script records the explicit `beta_moment` and `A[k,j]` formula.

It finds:

```text
A_N is moment-like;
A_N is not symmetric in raw form.
```

The raw asymmetry blocks a naive Hessian/Gram interpretation unless additional structure is found.

### 3. Origin Route Evidence Matrix

The script classifies:

```text
MOMENT_PROJECTION:
  PLAUSIBLE_BUT_UNDERDERIVED

AUXILIARY_ADMISSIBILITY:
  SUPPORTED
```

and rejects or defers:

```text
VARIATIONAL_HESSIAN;
INTERFACE_SMOOTHING;
EXCHANGE_COMPENSATION;
TOTAL_BURDEN.
```

This is the correct conservative result.

### 4. Moment Projection Plausibility Probe

The script proves the strongest positive clue:

```text
beta_moment(s)
=
2 ∫_0^1 x^(2s) (1-x^2)^4 dx.
```

This supports a moment/projection origin as mathematically plausible, but it does not derive the physical residual, basis, source vector, or boundary conditions.

### 5. Source Origin Decision Surface

The classifier records the right final status:

```text
FORMULA_IS_MOMENT_LIKE
BETA_MOMENT_INTEGRAL_STRUCTURE_SUPPORTED
MOMENT_PROJECTION_ORIGIN_PLAUSIBLE_BUT_UNDERDERIVED
SOURCE_ORIGIN_REMAINS_OPEN
HIERARCHY_REMAINS_AUXILIARY_ADMISSIBILITY_CANDIDATE
```

### 6. Group Status Summary

The summary is accurate and recommends the right next routes.

## Final Status Ledger

```text
formula_structure:
  MOMENT_LIKE

beta_moment_integral:
  SUPPORTED

candidate_weight:
  (1-x^2)^4 on [0,1]

moment_projection_origin:
  PLAUSIBLE_BUT_UNDERDERIVED

continuum_residual:
  NOT_DERIVED

test_basis:
  NOT_DERIVED

source_vector:
  NOT_DERIVED

boundary_conditions:
  NOT_DERIVED

variational_hessian_origin:
  NOT_LICENSED

raw_A_symmetry:
  FAILS

interface_origin:
  NOT_LICENSED

exchange_origin:
  NOT_LICENSED

total_burden_origin:
  NOT_LICENSED

source_origin:
  OPEN

hierarchy_role:
  AUXILIARY_ADMISSIBILITY_CANDIDATE

physical_ledger_assignment:
  DEFERRED

parent_equation:
  NOT_READY

recombination:
  BLOCKED
```

## Rejected Overclaims

Group 099 rejects:

```text
A_N is J_curv;
A_N is H_curv;
A_N is H_exch;
A_N is total burden;
A_N is a source law;
A_N is a field equation;
A_N is a merger prediction;
moment representation is physical derivation;
moment representation is burden ledger assignment.
```

## Strategic Interpretation

Group 099 is more productive than a pure bookkeeping group.

It finds the first concrete clue about the origin of the hierarchy:

```text
weighted even moments with weight (1-x^2)^4.
```

That suggests the next physical/mathematical bridge should try to derive `A_N` from a projection problem.

A plausible target is something like:

```text
choose basis functions x^(2j) or related powers;
choose test functions involving row-dependent differential/weight operators;
derive A[k,j] as an integral against (1-x^2)^4;
identify the residual and source vector.
```

The row-dependent factor:

```text
(2k-1)/(2k+3)
```

and the simplified numerator:

```text
4j - 6k + 3
```

are the goblin scratches that the next group should inspect.

## Recommended Next Group

Best next group:

```text
100_moment_projection_derivation_attempt
```

Purpose:

```text
try to derive A[k,j] from the beta-integral representation by constructing candidate basis/test functions or a residual projection.
```

Alternative:

```text
100_difference_numerator_factorization_attempt
```

if the project wants to finish the current admissibility theorem trail first.

My recommendation:

```text
100_moment_projection_derivation_attempt
```

because Group 099 found a concrete origin clue.

## Final Interpretation

Group 099 found a scent trail.

```text
The matrix is not yet physical.
But it smells like moments.

The weight is visible.
The powers are visible.
The row operator is hiding.

Next goblin job:
find the operator that made the matrix.
```
