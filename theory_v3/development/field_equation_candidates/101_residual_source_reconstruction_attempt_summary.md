# Group 101 Summary: Residual Source Reconstruction Attempt

## Purpose

Group 101 followed Group 100.

Group 100 derived the hierarchy matrix as a formal weighted projection:

```text
A[k,j] = 2∫psi_k(x) phi_j(x) w(x) dx.
```

Group 101 asked:

```text
Given this projection matrix, what formal residual/source equation could produce A c = b?
```

## Main Result

Group 101 succeeds as a formal residual/source reconstruction group.

Stable result:

```text
projected profile identity derived;

minimal formal residual family R_S[f]=f-S defined;

source-vector formula b_k(S)=2∫psi_k S w dx derived;

simple formal source probes completed;

physical source not identified;

boundary conditions not derived;

physical ledger assignment deferred;

hierarchy remains auxiliary admissibility candidate;

parent equation not ready;

recombination blocked.
```

## What We Actually Learned

Let:

```text
f_N(x) = Σ_j c_j x^(2j).
```

Group 101 verifies:

```text
Σ_j A[k,j] c_j
=
2∫psi_k(x) f_N(x) w(x) dx.
```

So `A` maps coefficients to weighted test projections of the finite profile.

Then the formal residual family:

```text
R_S[f](x)=f(x)-S(x)
```

gives:

```text
2∫psi_k(x)[f_N(x)-S(x)]w(x)dx = 0
```

or:

```text
A c = b(S)
```

where:

```text
b_k(S)=2∫psi_k(x)S(x)w(x)dx.
```

This is a clean formal source-vector reconstruction.

## Script-Level Analysis

### 1. Residual Reconstruction Problem

The opener correctly asks what residual/source equation could produce `A c=b`.

It blocks:

```text
R[f]=f-S as physical field equation;
S as mass/source/burden;
boundary conditions as derived.
```

### 2. Projected Profile Identity

The script verifies:

```text
Σ_j A[k,j]c_j = 2∫psi_k f_N w dx
```

with no failures for `N<=6`.

This identifies the matrix action.

### 3. Minimal Residual Family

The script defines:

```text
R_S[f]=f-S
```

and derives:

```text
b_k(S)=2∫psi_k S w dx.
```

This gives a formal but not physical residual/source family.

### 4. Candidate Source Vector Probe

The script computes `b_k(S)` for simple candidate sources.

Most tested sources produce all-negative signs through `k=8`, while `S=x^2` gives:

```text
[1, -1, -1, -1, -1, -1, -1, -1].
```

This shows that source-vector signatures depend strongly on source profile and test-function roots.

### 5. Residual Origin Classifier

The classifier preserves the correct status:

```text
PHYSICAL_SOURCE_NOT_IDENTIFIED
BOUNDARY_CONDITIONS_NOT_DERIVED
PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED
```

### 6. Group Status Summary

The final summary is accurate and recommends source-vector selection, boundary-origin work, or returning to numerator factorization.

## Final Status Ledger

```text
projected_profile_identity:
  DERIVED

matrix_action:
  A maps coefficients to weighted test projections of f_N

minimal_residual_family:
  FORMAL

source_vector_formula:
  DERIVED

simple_source_probes:
  COMPLETED

simple_source_signatures:
  COMPUTED

physical_source:
  NOT_IDENTIFIED

boundary_conditions:
  NOT_DERIVED

physical_ledger_assignment:
  DEFERRED

hierarchy_role:
  AUXILIARY_ADMISSIBILITY_CANDIDATE

parent_equation:
  NOT_READY

recombination:
  BLOCKED
```

## Rejected Overclaims

Group 101 rejects:

```text
R_S[f]=f-S as a physical field equation;
S(x) as mass/source/burden by declaration;
b_k(S) as ordinary matter source;
simple source profiles as physically selected;
boundary conditions as derived;
projection as ledger assignment;
parent equation insertion;
recombination opening.
```

## Strategic Interpretation

Group 101 is useful because it reconstructs the right-hand-side layer of the hierarchy.

Before Group 101, we had:

```text
A_N is a formal weighted projection matrix.
```

After Group 101, we have:

```text
A c = b(S)
```

with a precise formal source-vector map.

That is not the final physical theory, but it gives the next group a concrete choice:

```text
study possible source-vector structures,
or derive boundary/domain conditions that select S(x).
```

## Recommended Next Group

Best next group:

```text
102_source_vector_structure_selection
```

Purpose:

```text
study what formal source profiles S(x) produce source vectors compatible with the desired hierarchy behavior, without calling any source physical yet.
```

Alternative:

```text
102_boundary_condition_origin_attempt
```

Purpose:

```text
try to derive S(x) or b_k from a boundary/domain problem instead of choosing it.
```

If the project wants to return to the admissibility proof:

```text
102_difference_numerator_factorization_attempt.
```

## Final Interpretation

Group 101 found the formal shadow of the source.

```text
The matrix tests the profile.
The right side tests the target.

But the target is still a ghost.

Next goblin task:
learn what kind of ghost casts the right shadow.
```
