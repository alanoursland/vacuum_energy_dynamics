# Matter Source Origin Gate 27: Particle Current Weak Conservation

## Purpose

This proof records the weak conservation law behind source consistency.

For a moving point source:

```text
rho = m delta(x-q(t))
j = m q'(t) delta(x-q(t)).
```

Rather than manipulating distributions directly, the proof uses test-function
pairings.

## Validated Checks

- d/dt <rho,test> equals <j,test'> for a moving point source: passed
- constant test function gives conserved total mass: passed
- linear test detects the particle current m v: passed

## Weak Continuity

Let the test function be:

```text
test(x) = a0 + a1 x + a2 x^2.
```

Then:

```text
<rho,test> = m test(q).
```

Taking `q'(t)=v`:

```text
d/dt <rho,test> = m v test'(q).
```

The current pairing is:

```text
<j,test'> = m v test'(q).
```

So:

```text
d/dt <rho,test> = <j,test'>.
```

This is the weak form of:

```text
partial_t rho + partial_x j = 0.
```

## Gate Interpretation

The matter source produced by proper-time particles is not just a static mass
density. It carries the conservation structure required by the gauge/source
consistency gate.
