# Boundary Flux Field Bridge 46: Source-Coupled Reduced Action Sign

## Purpose

This report resolves the scalar sign bookkeeping gap left by proof `42`.

The important distinction is:

```text
stored strain energy
```

versus:

```text
source-coupled reduced action after the field has been eliminated.
```

## Validated Checks

- stationary field in quadratic source-coupled action: passed
- reduced quadratic action is negative: passed
- positive stored strain cross term: passed
- source coupling cross term: passed
- negative reduced interaction cross term: passed
- reduced action gives attractive separation derivative: passed
- stored strain alone gives repulsive derivative: passed

## Quadratic Prototype

For a positive quadratic operator `A`, the source-coupled action has the finite
dimensional form:

```text
E[u] = 1/2 <u,Au> - <J,u>.
```

The stationary field satisfies:

```text
Au = J.
```

Substituting the stationary field back into the action gives:

```text
E_red[J] = -1/2 <J,A^-1 J>.
```

The minus sign is forced by completing the square.

## Two-Source Interaction

For two positive boundary/source strengths:

```text
G(d) = 1/(4*pi*d).
```

The stored strain cross term is:

```text
E_strain,cross = +Q1*Q2*G(d).
```

The source coupling contributes:

```text
E_source,cross = -2*Q1*Q2*G(d).
```

Therefore the reduced interaction is:

```text
E_red,cross = -Q1*Q2*G(d)
            = -Q1*Q2/(4*pi*d).
```

## Force Sign

Using the convention that the separation force is:

```text
F_d = -dE/dd,
```

the reduced interaction gives:

```text
F_d = -Q1*Q2/(4*pi*d^2).
```

For same-sign positive sources this is attractive.

## Interpretation

The scalar bridge does not need same-sign charges to repel. Repulsion only
appears if one treats the positive stored strain cross term as the full
effective interaction energy.

The source-coupled reduced action supplies the attractive sign:

```text
positive stored strain + source coupling -> negative reduced interaction.
```
