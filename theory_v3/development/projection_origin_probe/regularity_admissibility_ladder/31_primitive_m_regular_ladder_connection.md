# Synthesis Proof 31: Primitive Power and Regularity Ladder

## Purpose

This report connects the generalized regularity rows to the primitive-power
family.

## Validated Checks

- regularity level R corresponds to primitive power m=R+2: passed
- primitive derivative identity verified for R=0..6: passed

## Main Relation

The row family adapted to regularity level `R` has ratio:

```text
(2k-1)/(2k+2R+3).
```

The primitive-power family has ratio:

```text
(2k-1)/(2k+2m-1).
```

These match when:

```text
m = R + 2.
```

## Table

```text
R=0: m=2, ratio=(2k-1)/(2k+3)
R=1: m=3, ratio=(2k-1)/(2k+5)
R=2: m=4, ratio=(2k-1)/(2k+7)
R=3: m=5, ratio=(2k-1)/(2k+9)
R=4: m=6, ratio=(2k-1)/(2k+11)
R=5: m=7, ratio=(2k-1)/(2k+13)
R=6: m=8, ratio=(2k-1)/(2k+15)
```

## Interpretation

The observed hierarchy has:

```text
m = 2.
```

Therefore it is the `R=0` member of the regularity ladder: the row family
adapted to boundedness of `f=u/a^3`.

Higher regularity levels would naturally shift the primitive power:

```text
R=1 -> m=3
R=2 -> m=4
...
```

This gives the primitive-power family a new interpretation:

```text
m labels regularity level plus 2.
```
