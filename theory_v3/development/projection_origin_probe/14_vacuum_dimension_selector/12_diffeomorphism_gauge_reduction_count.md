# Vacuum Dimension Selector 12: Diffeomorphism Gauge Reduction Count

## Purpose

This proof records the standard massless spin-2 degree count used by the
weak-field GR lift.

## Validated Checks

- symmetric components minus gauge/constraint count reduces to `D(D-3)/2`:
  passed
- `D=4` gives two propagating degrees of freedom: passed
- `D=3` gives zero local spin-2 degrees of freedom: passed
- `D=5` gives five propagating degrees of freedom: passed

## Computation

```text
D(D+1)/2 - 2D = D*(D - 3)/2
```

So:

```text
N_spin2(D) = D*(D - 3)/2
N_spin2(4) = 2
N_spin2(3) = 0
N_spin2(5) = 5
```

## Interpretation

This is imported weak-field spin-2 bookkeeping. It is valid under the assumption
of a local massless spin-2 metric lift with diffeomorphism-type gauge freedom.
