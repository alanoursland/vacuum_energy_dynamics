# Boundary Flux Field Bridge 42: Attraction Sign Bookkeeping

## Purpose

This report isolates the sign issue in the scalar boundary-flux bridge.

The minimal Dirichlet cross term has the form:

```text
E_cross(d) = K Q1 Q2 / d.
```

That is Coulomb-like. Same-sign scalar charges repel unless an additional sign
choice or interpretation is introduced.

## Validated Checks

- separation force from signed interaction: passed
- positive cross energy gives repulsive separation force: passed
- negative interaction gives attractive separation force: passed
- opposite scalar charges attract: passed

## Separation Force Convention

Let:

```text
E(d) = s K M1 M2 / d
```

with positive `K`, `M1`, and `M2`.

The force on the separation coordinate is:

```text
F_d = -dE/dd = s K M1 M2 / d^2.
```

Under this convention:

```text
F_d > 0  means increasing separation, repulsion
F_d < 0  means decreasing separation, attraction
```

## Consequence

For same-sign positive masses:

```text
E = +K M1 M2/d  -> repulsive
E = -K M1 M2/d  -> attractive
```

Therefore a gravitational interpretation must supply one of the following:

```text
1. physical interaction energy is the negative of the scalar cross-strain;
2. positive mass maps to opposite scalar boundary charges in the relevant
   interaction channel;
3. the scalar model is only a magnitude model and the tensor/nonlinear theory
   supplies the attractive sign.
```

## Interpretation

The inverse-square scaling is established by the previous bridge scripts, but
the attractive sign is not automatic. It is an independent physical requirement
that must be derived, not assumed.
