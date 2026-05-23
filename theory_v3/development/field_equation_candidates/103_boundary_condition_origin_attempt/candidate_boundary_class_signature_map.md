# candidate_boundary_class_signature_map — Analysis Note

## Result

`candidate_boundary_class_signature_map.py` maps formal boundary classes to source-vector signatures for:

```text
p=0..4
q=0..6.
```

Important class-map counts include:

```text
B0_FINITE_ORIGIN:
  ALL_NEGATIVE: 8
  LEADING_POSITIVE_THEN_NEGATIVE: 13
  MULTI_OR_MIXED_FLIP_1: 13
  MULTI_OR_MIXED_FLIP_0: 1

B1_CENTER_SUPPRESSED:
  LEADING_POSITIVE_THEN_NEGATIVE: 13
  MULTI_OR_MIXED_FLIP_1: 13
  MULTI_OR_MIXED_FLIP_0: 1
  ALL_NEGATIVE: 3

B3_ENDPOINT_VANISHING:
  ALL_NEGATIVE: 7
  MULTI_OR_MIXED_FLIP_0: 1
  LEADING_POSITIVE_THEN_NEGATIVE: 11
  MULTI_OR_MIXED_FLIP_1: 9

B6_P_GE_Q:
  ALL_NEGATIVE: 8
  MULTI_OR_MIXED_FLIP_0: 1
  LEADING_POSITIVE_THEN_NEGATIVE: 6

B7_P_GE_Q_MINUS_1:
  ALL_NEGATIVE: 8
  LEADING_POSITIVE_THEN_NEGATIVE: 11
  MULTI_OR_MIXED_FLIP_0: 1.
```

Governance records:

```text
boundary class map:
  built

signature trend:
  endpoint suppression classes favor cleaner negative signatures

physical boundary:
  not selected.
```

## Interpretation

This is one of the main results of Group 103.

The map shows that endpoint behavior does not uniquely determine a signature, but it strongly biases the signature class.

The strongest trend is:

```text
balanced or endpoint-suppressed classes
  produce more all-negative or simple signatures.
```

The `p>=q` class is especially useful:

```text
B6_P_GE_Q:
  no multi-flip-1 cases
  all-negative and leading-positive-then-negative dominate.
```

That suggests that balanced endpoint suppression may be a useful formal selector if the future physical boundary problem wants a clean right-hand side.

## What It Does Not Prove

This is not physical selection.

A boundary class count is not enough to say which source profile is correct.

## Carry-forward status

```text
BOUNDARY_CLASS_SIGNATURE_MAP_BUILT
BALANCED_SUPPRESSION_CLASSES_TRACKED
ENDPOINT_SUPPRESSION_FAVORS_CLEANER_SIGNATURES
P_GE_Q_CLASS_AVOIDS_MULTI_FLIP_1_IN_TESTED_RANGE
PHYSICAL_BOUNDARY_NOT_SELECTED
```
