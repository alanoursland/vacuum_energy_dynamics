# candidate_mixed_source_signature_scan — Analysis Note

## Result

`candidate_mixed_source_signature_scan.py` scans:

```text
S_pq(x)=x^(2q)(1-x^2)^p
```

for:

```text
p=0..4
q=0..6
k=1..12.
```

Class counts:

```text
ALL_NEGATIVE:
  8

LEADING_POSITIVE_THEN_NEGATIVE:
  12

MULTI_OR_MIXED_FLIP_1:
  13

MULTI_OR_MIXED_FLIP_2:
  2
```

Clean signatures include:

```text
ALL_NEGATIVE:
  (p,q) = (0,0), (1,0), (2,0), (2,1),
          (3,0), (3,1), (4,0), (4,1)

LEADING_POSITIVE_THEN_NEGATIVE:
  (0,1), (0,2), (1,2), (2,2), (2,3),
  (3,2), (3,3), (3,4),
  (4,2), (4,3), (4,4), (4,5).
```

Higher `q` values tend to lengthen the initial positive run, while larger `p` values pull the source back toward all-negative or shorter leading-positive behavior.

## Interpretation

This is the most informative scan in Group 102.

The mixed family shows that source signatures are governed by a balance between two tendencies:

```text
x^(2q):
  pushes the source toward x=1,
  creating leading positive entries.

(1-x^2)^p:
  suppresses the endpoint,
  favoring all-negative or shorter leading-positive signatures.
```

This is exactly the kind of classification the group was supposed to produce.

It gives the next boundary/source-origin group a concrete structure to test. A boundary condition that concentrates source weight near `x=1` should correspond to larger `q` behavior. A boundary condition that suppresses the endpoint should correspond to larger `p` behavior.

## What It Does Not Prove

Clean signatures are not source selection.

No `(p,q)` pair is physical yet.

## Carry-forward status

```text
MIXED_SOURCE_SIGNATURES_CLASSIFIED
ALL_NEGATIVE_MIXED_CLASSES_IDENTIFIED
LEADING_POSITIVE_THEN_NEGATIVE_CLASSES_IDENTIFIED
ENDPOINT_SUPPRESSION_VS_ENDPOINT_CONCENTRATION_TENSION_IDENTIFIED
PHYSICAL_SOURCE_NOT_SELECTED
```
