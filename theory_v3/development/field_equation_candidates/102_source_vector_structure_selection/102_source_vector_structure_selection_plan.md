# 102_source_vector_structure_selection — Plan

## Purpose

Group 102 follows Group 101.

Group 101 derived the formal source-vector layer behind the projection system:

```text
A c = b(S)
b_k(S) = 2∫_0^1 psi_k(x) S(x) w(x) dx
w(x) = (1-x^2)^4
psi_k(x)=x^(2k)-r_k x^(2k-2)
r_k=(2k-1)/(2k+3)
```

It also tested a few simple source profiles:

```text
S=1
S=x^2
S=1-x^2
S=(1-x^2)^2
```

and found distinct sign signatures. But no physical source was selected.

Group 102 tries to make real progress by classifying source-vector structure more systematically.

This group does **not** choose a physical source. It asks which formal source families produce source vectors with stable, simple, or target-compatible signatures.

## Group Name

```text
102_source_vector_structure_selection
```

## Central Question

```text
What formal source profiles S(x) produce structurally useful source-vector signatures b_k(S)?
```

## Starting State

Imported from Group 101:

```text
projected profile identity derived;
minimal formal residual family R_S[f]=f-S defined;
source-vector formula b_k(S)=2∫psi_k S w dx derived;
simple formal source probes completed;
physical source not identified;
boundary conditions not derived;
physical ledger assignment deferred;
hierarchy remains auxiliary admissibility candidate.
```

## Formal Identity to Exploit

Because:

```text
psi_k(x)=x^(2k-2)(x^2-r_k)
```

the source vector is:

```text
b_k(S)=2∫x^(2k-2)(x^2-r_k)S(x)(1-x^2)^4 dx.
```

So the sign of `b_k(S)` compares the weighted source mass above and below the row root:

```text
x_k = sqrt(r_k).
```

This suggests that source-vector signs are not arbitrary; they encode where `S(x)` sits relative to the moving row test roots.

## What This Group Should Do

Group 102 should:

```text
derive source-vector formula for monomial sources S=x^(2q);
derive source-vector formula for endpoint-weight sources S=(1-x^2)^p;
scan finite q,p families for sign patterns;
identify whether any family yields all-positive, all-negative, single-flip, or parity-like signatures;
classify useful formal source classes and reject physical selection.
```

## Candidate Formal Source Families

### Monomial even powers

```text
S_q(x)=x^(2q), q=0..8.
```

### Endpoint weights

```text
S_p(x)=(1-x^2)^p, p=0..6.
```

### Mixed profile

```text
S_{p,q}(x)=x^(2q)(1-x^2)^p
```

for small `p,q`.

## What This Group Must Not Do

Group 102 must not:

```text
claim any S(x) is physical source;
claim S(x) is mass density;
claim S(x) is J_curv, H_exch, interface energy, or total burden;
claim boundary conditions are derived;
claim source separation from ordinary matter;
insert parent equation terms;
claim recombination.
```

## Recommended Script Batch

```text
candidate_source_structure_problem.py
candidate_monomial_source_signature_scan.py
candidate_endpoint_weight_source_signature_scan.py
candidate_mixed_source_signature_scan.py
candidate_source_structure_classifier.py
candidate_group_102_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_source_structure_problem.py

Open Group 102 as a formal source-vector structure selection group.

### 2. candidate_monomial_source_signature_scan.py

Derive and scan:

```text
S_q=x^(2q)
```

for `q=0..8`, `k=1..12`.

Classify sign patterns:

```text
all negative
all positive
single leading positive then negative
multi-flip
```

### 3. candidate_endpoint_weight_source_signature_scan.py

Scan:

```text
S_p=(1-x^2)^p
```

for `p=0..6`, `k=1..12`.

### 4. candidate_mixed_source_signature_scan.py

Scan:

```text
S_{p,q}=x^(2q)(1-x^2)^p
```

for small `p,q`.

Look for clean classes.

### 5. candidate_source_structure_classifier.py

Classify:

```text
SOURCE_VECTOR_STRUCTURE_SCANNED
MONOMIAL_SOURCE_CLASSES_IDENTIFIED
ENDPOINT_WEIGHT_CLASSES_IDENTIFIED
MIXED_SOURCE_CLASSES_IDENTIFIED
PHYSICAL_SOURCE_NOT_SELECTED
BOUNDARY_ORIGIN_REQUIRED
```

### 6. candidate_group_102_status_summary.py

Close the group and recommend next step.

## Key Success Criteria

Group 102 must produce at least one:

```text
closed-form or exact finite source-vector scan;
classification of sign signatures;
identification of source families with simple patterns;
or a negative result showing simple families do not provide useful selection.
```

## Recommended Next Group

If useful source classes are found:

```text
103_boundary_condition_origin_attempt
```

because boundary/domain origin should decide which class is physical.

If source classes are messy:

```text
103_difference_numerator_factorization_attempt
```

or:

```text
103_residual_operator_origin_attempt
```

## Final Interpretation

Group 102 asks:

```text
What kind of formal target casts a clean projection shadow?
```

Goblin discipline:

```text
Do not crown the shadow.
Sort the shadows first.
```
