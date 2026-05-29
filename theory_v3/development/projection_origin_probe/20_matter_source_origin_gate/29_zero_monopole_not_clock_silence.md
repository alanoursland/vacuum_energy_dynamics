# Matter Source Origin Gate 29: Zero Monopole Is Not Clock Silence

## Purpose

This proof separates two safety concepts:

```text
zero exterior mass monopole
```

and:

```text
zero local clock-rate effect.
```

The first does not imply the second.

## Validated Checks

- H has zero routed ordinary monopole: passed
- the same H gives a nonzero local clock-force witness if coupled to clocks: passed
- clock decoupling alpha=0 silences the local clock effect: passed

## Witness Shape

Use:

```text
H(r) = r^2 - (3/5)R^2.
```

It has zero ordinary radial monopole:

```text
4*pi integral_0^R H r^2 dr = 0.
```

So it does not shift exterior A-sector mass if routed only through the
ordinary monopole ledger.

## Clock-Coupled Failure

If the same shape changes clock rate:

```text
d tau/dt -> d tau/dt + alpha H,
```

then the local clock-force witness is:

```text
-c^2 d(alpha H)/dr = -2*alpha*c**2*r.
```

This is not zero.

## Gate Interpretation

Zero monopole is enough for exterior mass neutrality, but not enough for local
clock neutrality. Auxiliary projection/residual structures must either remain
outside the clock coupling or be given a physical interpretation as local
clock-rate effects.
