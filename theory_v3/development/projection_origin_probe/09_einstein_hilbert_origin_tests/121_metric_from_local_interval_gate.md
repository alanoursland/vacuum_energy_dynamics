# Einstein-Hilbert Origin Test 121: Metric from Local Interval Gate

## Purpose

This report validates the algebraic gate:

```text
even local quadratic interval
  -> symmetric bilinear form
  -> metric candidate.
```

It does not prove that the vacuum ontology supplies such an interval. It proves
what follows once a local interval is the macroscopic observable.

## Validated Checks

- antisymmetric bilinear part drops out of interval: passed
- general quadratic interval equals symmetric part: passed
- interval Hessian recovers symmetric bilinear form: passed
- odd part of local expansion: passed
- even local interval forces zero linear term: passed
- explicit antisymmetric two-form gives zero interval: passed

## Quadratic Interval

Let a local interval be represented by:

```text
I(v) = v^T M v.
```

Every matrix decomposes as:

```text
M = S + A
S = (M + M^T)/2
A = (M - M^T)/2.
```

SymPy verifies:

```text
v^T A v = 0
v^T M v = v^T S v.
```

So only the symmetric part is visible to the interval.

## Hessian Recovery

SymPy verifies:

```text
(1/2) Hessian_v I = S.
```

The metric is therefore the second local derivative of the interval with
respect to displacement.

## Evenness

For a local expansion:

```text
I(v) = l_a v^a + M_ab v^a v^b,
```

the condition:

```text
I(v) = I(-v)
```

forces:

```text
l_a = 0.
```

## Interpretation

If the vacuum framework has a local, reversible, quadratic interval structure,
then the macroscopic configuration variable is naturally a symmetric metric.
The open physics question is whether the vacuum ontology forces that local
interval structure.
