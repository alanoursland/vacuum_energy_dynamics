# Time-Dependent Vector Sector

## Purpose

This directory holds Phase 3 of the targeted covariant-lift program:
the general linear time-dependent vector sector extending the stationary
012 frame-dragging closure.

Current status: completed at linear reduced/covariant-lift level. See
`vector_time_dependent_note.md` and the forge script:

```text
vacuum_forge/src/field_equation_trials/017_vector_time_dependent/vector_time_dependent.py
```

## Scope

012 derived the stationary vector equation and Lense-Thirring
normalization:

$$
\Delta w_i = {16\pi G\over c^2}\rho v_i .
$$

This lift allows \(w_i=w_i(t,\mathbf x)\) in transverse gauge
\(\partial_i w_i=0\). The linearized closed parent gives:

$$
G_{ti}^{(1)}=-{1\over2}\Delta w_i ,
$$

and

$$
G_{ij}^{(1)}
=
-{1\over 2c^2}
\left(\partial_i\dot w_j+\partial_j\dot w_i\right).
$$

The first equation remains an elliptic constraint. The second is the
time-dependent consistency/evolution condition, sourced by vector
anisotropic stress when present. In source-free vacuum, regular boundary
conditions force \(w_i=0\); there is no independent vector radiation
mode.

## Forge Proof

The forge script validates:

1. the time-dependent linearized Einstein tensor for a transverse stream
   witness \(w=\nabla\times(\chi \hat z)\);
2. recovery of the 012 stationary constraint and normalization;
3. the Fourier-mode vacuum result: for \(k\ne0\), the constraint forces
   transverse vector amplitudes to zero, with no dispersion relation;
4. the stationary limit \(\dot w_i=0\) kills the \(G_{ij}\) vector
   components and reduces exactly to 012.

Archive result:

```text
vector_time_dependent_lift_017
```

This retires the 012 vector time-dependence subpiece of the covariant
lift debt. Nonlinear stability remains separate.

