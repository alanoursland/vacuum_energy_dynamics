# Quadratic Response Selector 22: Metric Stress Variation Gate

## Purpose

This proof checks the algebraic form of a symmetric metric variation coupling.
It is not a matter-origin proof; it only records what becomes available after a
symmetric metric variable exists.

## Computation

For the symmetric contraction

```text
L = 1/2 (T00 h00 + 2 T01 h01 + T11 h11),
```

SymPy computes:

```text
dL/dh00 = T00/2
dL/dh01 = T01
dL/dh11 = T11/2
```

## Interpretation

Standard stress coupling presupposes a symmetric metric variable. It is
downstream of the quadratic response gate, not upstream of it.
