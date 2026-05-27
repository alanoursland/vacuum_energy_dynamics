# Matter Source Origin Gate 21: Nonmetric Clock Channel Exclusion

## Purpose

This proof checks what happens if an independent nonmetric channel changes
clock rate.

## Validated Checks

- independent clock channel with 1/r tail produces inverse-square acceleration: passed
- for arbitrary nonzero tail, silence requires alpha=0: passed
- zero exterior tail also silences the nonmetric clock channel: passed
- constant exterior shift is not a force but remains a background-clock datum: passed

## Setup

Let the clock rate contain an extra channel:

```text
d tau/dt = 1 + Phi/c^2 + alpha zeta.
```

For a source-free exterior scalar:

```text
zeta = C0 + C1/r.
```

The additional acceleration is:

```text
a_extra = -c^2 d(alpha zeta)/dr
        = alpha c^2 C1/r^2.
```

## Silence Routes

For an arbitrary nonzero exterior tail, silence requires:

```text
alpha = 0.
```

Alternatively, if the channel is allowed but must be exterior-silent:

```text
C1 = 0.
```

The remaining constant mode does not produce a force, but it is still a
background-clock datum that must be fixed or interpreted.

## Gate Interpretation

Nonmetric residual/projection channels cannot be allowed to alter clock rate
with a `1/r` tail. They either remain outside the clock coupling, have zero
exterior tail, or require an explicit new routing theorem.
