# Vacuum Interval Directional Probe Origin 21: Single Scale Field Origin

## Purpose

This proof records the positive origin of the common-scale gate.

If all local interval measurements are scaled by one local field `beta`, then
all non-null calibrations share one conformal factor automatically.

## Validated Checks

- `m1/q1 = beta`: passed
- `m2/q2 = beta`: passed
- `mp/qp = beta`: passed
- cross-calibration consistency equations vanish: passed

## Model

Let baseline interval probes be:

```text
q1, q2, qp
```

and measured probes be:

```text
m1 = beta q1
m2 = beta q2
mp = beta qp.
```

Then:

```text
m1/q1 = m2/q2 = mp/qp = beta.
```

Equivalently:

```text
m1 q2 - m2 q1 = 0
mp q1 - m1 qp = 0.
```

## Interpretation

A single local clock/interval scale field is sufficient to explain the common
conformal calibration required by the metric branch. Independent per-direction
scale factors would be a different tensor or auxiliary channel.
