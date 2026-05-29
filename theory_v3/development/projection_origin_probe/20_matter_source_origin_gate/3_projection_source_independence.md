# Matter Source Origin Gate 3: Projection Source Independence

## Purpose

This proof checks the formal projection source vector:

```text
b_k(S) = 2 integral_0^1 psi_k S a^4 dx.
```

It shows that `b_k(S)` is not an ordinary mass/monopole functional by itself.
It can detect variations that have zero simple monopole.

## Validated Checks

- zero unweighted monopole can still have nonzero projection source: passed
- zero a^4-weighted monopole can still have nonzero projection source: passed
- contact cancellation does not mean zero projection response: passed

## Witness 1: Zero Unweighted Monopole

Let:

```text
S = x^2 - 1/3.
```

Then:

```text
integral_0^1 S dx = 0,
```

but:

```text
b_1(S) = 1024/32175.
```

## Witness 2: Zero a^4-Weighted Monopole

Let:

```text
S = x^2 - 1/11.
```

Then:

```text
integral_0^1 S a^4 dx = 0,
```

but:

```text
b_1(S) = 1024/99099.
```

## Witness 3: Contact Cancellation Is Not Projection Silence

For:

```text
psi_1 = x^2 - 1/5,
```

the contact moment cancels:

```text
integral_0^1 a psi_1 dx = 0.
```

But the projection self-pairing is nonzero:

```text
2 integral_0^1 psi_1^2 a^4 dx = 2048/102375.
```

## Gate Interpretation

The formal projection source vector is a real linear diagnostic, but it is not
licensed as ordinary matter mass. A later source-origin theorem must explain
how `b_k(S)` is routed, or else keep it in the formal admissibility layer.
