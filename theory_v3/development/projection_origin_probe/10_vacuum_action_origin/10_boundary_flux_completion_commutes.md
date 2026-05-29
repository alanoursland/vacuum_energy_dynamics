# Vacuum Action Origin 10: Boundary Completion and Flux Sources Commute

## Purpose

This report validates a one-dimensional analogue of the EH/GHY boundary
bookkeeping with boundary flux sources included.

The question is whether two operations are compatible:

```text
1. complete a curvature-like second-derivative density by a boundary term;
2. add boundary source terms that impose flux conditions.
```

## Validated Checks

- curvature completion equals strain: passed
- right derivative-of-variation cancellation: passed
- left derivative-of-variation cancellation: passed
- completed boundary source variation: passed
- completed action yields flux conditions: passed

## Boundary Completion

Use:

```text
L_curv = -(1/2) q q''
L_boundary = (1/2) d(q q')/dx
L_strain = (1/2)(q')^2.
```

SymPy verifies:

```text
L_curv + L_boundary = L_strain.
```

The derivative-of-variation boundary terms cancel at both endpoints.

## Boundary Flux Sources

After completion, add:

```text
E_source = -Q_R q(R) + Q_L q(L).
```

The boundary variation becomes:

```text
(q'(R)-Q_R)eta_R + (-q'(L)+Q_L)eta_L.
```

For arbitrary boundary variations:

```text
q'(R)=Q_R
q'(L)=Q_L.
```

## Interpretation

The boundary completion required for a well-posed variational principle is
compatible with boundary-flux source bookkeeping. This is the toy-model bridge
toward understanding the EH/GHY boundary term as the nonlinear geometric
version of the boundary-flux source structure.
