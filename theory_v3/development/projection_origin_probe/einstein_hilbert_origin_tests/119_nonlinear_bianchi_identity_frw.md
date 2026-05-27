# Einstein-Hilbert Origin Test 119: Nonlinear Bianchi Identity on FRW

## Purpose

This report validates the contracted Bianchi identity on a nonlinear metric:

```text
ds^2 = -dt^2 + a(t)^2(dx^2 + dy^2 + dz^2).
```

## Validated Checks

- contracted Bianchi identity on flat-FRW metric: passed
- FRW G_00 component: passed
- FRW spatial Einstein components: passed

## Einstein Tensor Components

SymPy computes:

```text
G_00 = 3(a')^2/a^2
G_ii = -2aa'' - (a')^2
```

for each spatial diagonal component.

## Contracted Bianchi Identity

Using the mixed tensor:

```text
G^a_b = g^ac G_cb,
```

SymPy verifies all four components of:

```text
nabla_a G^a_b = 0.
```

## Interpretation

This is a nonlinear consistency check on the action-to-source gate. The EH
field tensor has the covariant divergence identity required by
diffeomorphism-invariant source coupling.
