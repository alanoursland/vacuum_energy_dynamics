# 101_residual_source_reconstruction_attempt — Plan

## Purpose

Group 101 follows Group 100.

Group 100 derived the hierarchy matrix as a formal weighted projection:

```text
A[k,j] = 2 ∫_0^1 psi_k(x) phi_j(x) w(x) dx
w(x) = (1-x^2)^4
phi_j(x) = x^(2j)
psi_k(x) = x^(2k) - r_k x^(2k-2)
r_k = (2k-1)/(2k+3)
```

Group 100 upgraded the mathematical origin to:

```text
FORMAL_WEIGHTED_PROJECTION_DERIVED
```

but kept open:

```text
PHYSICAL_RESIDUAL_NOT_DERIVED
SOURCE_VECTOR_NOT_DERIVED
BOUNDARY_CONDITIONS_NOT_DERIVED
PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED
```

Group 101 attempts to reconstruct what residual/source equation could generate this projection matrix.

This is not allowed to declare a physical field equation. It is a formal reconstruction attempt.

## Group Name

```text
101_residual_source_reconstruction_attempt
```

## Central Question

```text
Given the formal projection matrix, what residual operator or source structure could produce A c = b?
```

## Core Setup

Let an unknown finite profile be:

```text
f_N(x) = Σ_j c_j phi_j(x)
       = Σ_j c_j x^(2j).
```

The matrix entries imply:

```text
A[k,j] = 2 ∫ psi_k(x) phi_j(x) w(x) dx.
```

Therefore the projected unknown profile satisfies:

```text
Σ_j A[k,j] c_j
=
2 ∫ psi_k(x) f_N(x) w(x) dx.
```

So the left-hand side corresponds to projection of `f_N` itself against sign-changing tests. This suggests the simplest formal residual:

```text
R[f](x) = f(x) - S(x)
```

with equations:

```text
2 ∫ psi_k(x) [f(x)-S(x)] w(x) dx = 0.
```

Then the source vector would be:

```text
b_k = 2 ∫ psi_k(x) S(x) w(x) dx.
```

But `S(x)` is not yet physically known.

## What This Group Should Do

Group 101 should:

```text
derive the projected profile equation LHS_k = 2∫psi_k f_N w dx;
classify the minimal formal residual R[f]=f-S;
test candidate simple source profiles S(x);
derive what b_k would look like for simple sources;
classify whether any source choice is physically licensed;
identify the missing boundary/domain meaning.
```

## Candidate Source Profiles

Test formal candidate sources, not physical claims:

```text
S(x)=1
S(x)=x^2
S(x)=1-x^2
S(x)=(1-x^2)^p
S(x)=delta-like endpoint proxy not actually inserted
```

The group should not choose one as physical. It should classify what each produces and whether it looks structurally compatible.

## What This Group Must Not Do

Group 101 must not:

```text
claim R[f]=f-S is the physical field equation;
claim S(x) is mass, density, J_curv, H_exch, or total burden;
claim boundary conditions are derived;
claim source vector is physically known;
insert H_curv or H_exch;
claim parent divergence identity;
claim recombination;
claim merger prediction;
claim anti-singularity dynamics.
```

## Recommended Script Batch

```text
candidate_residual_reconstruction_problem.py
candidate_projected_profile_identity.py
candidate_minimal_residual_family.py
candidate_candidate_source_vector_probe.py
candidate_residual_origin_classifier.py
candidate_group_101_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_residual_reconstruction_problem.py

Open Group 101 as a formal residual/source reconstruction attempt.

### 2. candidate_projected_profile_identity.py

Prove:

```text
Σ_j A[k,j] c_j = 2∫psi_k f_N w dx.
```

This identifies what the matrix does to coefficient vectors.

### 3. candidate_minimal_residual_family.py

Define formal residual family:

```text
R_S[f] = f - S.
```

Then:

```text
A c = b(S)
b_k(S)=2∫psi_k S w dx.
```

Classify as formal only.

### 4. candidate_candidate_source_vector_probe.py

Compute exact `b_k` for simple formal sources:

```text
S=1
S=x^2
S=1-x^2
S=(1-x^2)^2
```

Look for sign patterns and finite structure.

### 5. candidate_residual_origin_classifier.py

Classify:

```text
PROJECTED_PROFILE_IDENTITY_DERIVED
MINIMAL_RESIDUAL_FAMILY_FORMAL
SOURCE_VECTOR_FORMULA_DERIVED
SIMPLE_SOURCE_PROBES_COMPLETED
PHYSICAL_SOURCE_NOT_IDENTIFIED
BOUNDARY_CONDITIONS_NOT_DERIVED
PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED
```

### 6. candidate_group_101_status_summary.py

Close the group.

## Key Success Criteria

Group 101 must earn at least one:

```text
derive matrix action as projected profile;
derive formal source-vector formula;
show simple source probes;
classify why physical source remains open.
```

## Recommended Next Group

If Group 101 succeeds:

```text
102_source_vector_structure_selection
```

or:

```text
102_boundary_condition_origin_attempt
```

If returning to pure admissibility:

```text
102_difference_numerator_factorization_attempt
```

## Final Interpretation

Group 101 asks:

```text
We found the projection loom.
What cloth equation could it be weaving?
```

Goblin discipline:

```text
Do not call a shadow a source.
But trace the shadow back toward the fire.
```
