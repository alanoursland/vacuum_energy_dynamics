# Matter Source Origin Gate 15: Gauge Invariance Source Conservation

## Purpose

This proof records the linearized source-consistency gate:

```text
gauge/diffeomorphism consistency requires conserved source.
```

The proof is written as a one-dimensional integration-by-parts witness for the
standard tensor statement.

## Validated Checks

- T xi' = d(T xi)/dx - T' xi: passed
- if T' = 0, gauge variation is boundary-only: passed
- nonzero source divergence leaves a bulk gauge-variation witness: passed

## Model Identity

For a source coupling, the gauge variation contains terms of the form:

```text
T xi'.
```

SymPy verifies:

```text
T xi' = d(T xi)/dx - T' xi.
```

So the variation is boundary-only if:

```text
T' = 0.
```

The tensor version is:

```text
delta h_mu_nu = partial_mu xi_nu + partial_nu xi_mu
```

and the source coupling is gauge-compatible only when:

```text
partial_mu T^mu_nu = 0.
```

## Gate Interpretation

This is a source-origin constraint, not a new field equation. Any candidate
matter, residual, or projection source coupled to the metric lift must satisfy
the appropriate conservation/no-leak condition.
