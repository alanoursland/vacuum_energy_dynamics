# Vacuum Action Origin 1: Response Reciprocity to Metric Candidate

## Purpose

This report validates the first action-origin gate:

```text
smooth local response cost
  + zero self-cost
  + reciprocity under displacement reversal
  -> symmetric quadratic leading term.
```

That symmetric quadratic leading term is the metric candidate.

## Validated Checks

- self-response normalization: passed
- zero self-response removes constant term: passed
- reciprocity odd part: passed
- reciprocity removes linear term: passed
- antisymmetric part invisible to quadratic interval: passed
- quadratic interval equals symmetric part: passed
- Hessian recovers symmetric response metric: passed
- explicit antisymmetric response gives zero interval: passed

## Local Response Expansion

Write the local response cost for a small displacement `d` as:

```text
C(d) = c0 + l_a d^a + (1/2) M_ab d^a d^b + higher terms.
```

Zero self-cost gives:

```text
C(0) = 0 -> c0 = 0.
```

Reciprocity means:

```text
C(d) = C(-d).
```

SymPy verifies that the odd part is:

```text
C(d) - C(-d) = 2 l_a d^a.
```

So reciprocity forces:

```text
l_a = 0.
```

## Metric Candidate

Every matrix decomposes as:

```text
M = S + A
S = (M + M^T)/2
A = (M - M^T)/2.
```

SymPy verifies:

```text
d^T A d = 0
d^T M d = d^T S d.
```

The Hessian of the quadratic response is:

```text
partial_a partial_b C = S_ab.
```

## Interpretation

If vacuum response supplies a smooth reciprocal local cost between nearby
states, the leading nontrivial local observable is necessarily a symmetric
bilinear form. This does not yet determine signature or dynamics, but it gives
the metric as the natural macroscopic configuration variable.
