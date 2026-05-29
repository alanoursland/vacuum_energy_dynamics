# Vacuum Dimension Selector 8: Zero Time Channel Obstruction

## Purpose

This proof checks the opposite failure mode from the multiple-time branch. If no
time channel is present, the wave operator loses its hyperbolic dispersion
structure.

## Validated Checks

- plane-wave symbol of `-d_t^2 + d_x^2` is `omega^2 - k^2`: passed
- plane-wave symbol of the spatial-only operator is `-k^2`: passed
- the spatial-only symbol contains no `omega`: passed

## Computation

For:

```text
u = exp(i(k x - omega t))
```

the wave operator gives:

```text
(-d_t^2 + d_x^2)u / u = -k**2 + omega**2
```

The spatial-only operator gives:

```text
d_x^2 u / u = -k**2
```

## Interpretation

Without a clock channel, the lift is static or elliptic rather than a dynamical
wave theory. This is a gate result, not an ontology derivation: a time channel
must be supplied by the parent theory if the lift is to reproduce wave-like
weak-field behavior.
