# Matter Source Origin Gate 31: Polarization Interval Uniqueness

## Purpose

This proof records the mathematical uniqueness gate behind operational interval
measurements.

If the vacuum state supplies a local quadratic interval:

```text
Q(v) = g(v,v),
```

then the full symmetric bilinear form is determined by the interval data.

## Validated Checks

- quadratic interval determines the symmetric bilinear form: passed
- basis and sum interval measurements recover all 2D metric components: passed
- two symmetric forms with same interval data are identical: passed

## Polarization

For a symmetric bilinear form `B` with quadratic interval `Q(v)=B(v,v)`:

```text
B(x,y) = (Q(x+y)-Q(x-y))/4.
```

SymPy verifies this identity for a general 2D symmetric matrix:

```text
M = [[a,b],[b,c]].
```

## Component Recovery

From interval measurements:

```text
Q(e1)
Q(e2)
Q(e1+e2)
```

one recovers:

```text
a = Q(e1)
c = Q(e2)
b = (Q(e1+e2)-Q(e1)-Q(e2))/2.
```

## Gate Interpretation

If operational rods/clocks determine one local quadratic interval for all
directions, then the corresponding metric candidate is unique. The remaining
physical question is whether the vacuum ontology forces matter probes to read
that one interval.
