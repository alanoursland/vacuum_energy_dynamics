# General Time-Dependent Vector Sector

## Statement

Work in a local flat background with metric perturbation

$$
g_{ti}=w_i(t,\mathbf x),
\qquad
\partial_i w_i=0,
$$

and no scalar or TT tensor components in this sector. The closed parent
linearized about the zero-source state gives

$$
\boxed{
G_{ti}^{(1)}=-{1\over2}\Delta w_i
}
$$

and

$$
\boxed{
G_{ij}^{(1)}
=
-{1\over 2c^2}
\left(\partial_i\dot w_j+\partial_j\dot w_i\right)
}.
$$

The first equation is the vector constraint. With the normalization
already derived in 008 and used in 012,

$$
N={c^4\over 8\pi G},
$$

and with slow matter momentum

$$
T_{ti}=-\rho c^2 v_i,
$$

the constraint gives

$$
\Delta w_i={16\pi G\over c^2}\rho v_i^T,
$$

where the transverse part is selected by the gauge condition.

## Relation to 012

For \(\dot w_i=0\), the spatial vector equation vanishes:

$$
G_{ij}^{(1)}=0.
$$

The only remaining vector equation is the elliptic constraint above,
which is exactly the stationary 012 equation. The 012 Lense-Thirring
solution is therefore the stationary limit of the general vector sector,
not a separate assumption.

## No Source-Free Vector Radiation

For a transverse Fourier mode

$$
w_i=W_i e^{i(kz-\Omega t)},\qquad k_iW_i=0,
$$

the vacuum constraint gives

$$
G_{ti}^{(1)}={1\over2}k^2 W_i e^{i(kz-\Omega t)}=0.
$$

For \(k\ne0\), this forces

$$
W_i=0.
$$

The spatial equation contains \(\Omega k W_i\), but the constraint has
already killed the amplitude. There is no vector dispersion relation and
no independent vector radiative degree of freedom. This matches the
massless spin-2 sector architecture: only TT modes propagate.

## What This Retires

This retires the vector time-dependence subpiece of the covariant lift
debt. It does not address nonlinear stability, and it does not replace
the broader covariant statics lift for C2/C3.

