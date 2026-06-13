# 6. Radiative Positivity: What Is Allowed to Propagate

The previous two sections removed the dangerous possibility: the
negative-energy scalar/static sector cannot be a propagating field and has
no independent source-free reservoir. The remaining question is what
sector does propagate.

In the weak-field radiative regime, the physical wave content is the
transverse-traceless part of the metric perturbation,

$$
h_{ij}^{\rm TT}.
$$

For the two TT polarizations, the reduced quadratic energy density has the
sum-of-squares form

$$
u_{\rm TT}
=\frac{c^2}{32\pi G}
\left\langle
\dot{h}_{ij}^{\rm TT}\dot{h}_{ij}^{\rm TT}
\right\rangle ,
$$

with the usual averaging understood over several wavelengths or periods.
For an outgoing wave, the corresponding flux is outward and null:

$$
{\cal F}_{\rm TT}=c\,u_{\rm TT}.
$$

Thus the sector that propagates is positive. This is the complement of
the ghost-exclusion theorem. The negative scalar/static sector is
forbidden from propagating; the positive TT sector is precisely the sector
that may carry radiation.

In a stripped-down one-dimensional model for either TT polarization, the
quadratic Lagrangian may be written schematically as

$$
L_{\rm TT}
=\frac{K_T}{2}
\left(\frac{\dot{h}^2}{c^2}-h_z^2\right).
$$

The energy density is then

$$
u_{\rm TT}
=\frac{K_T}{2}
\left(\frac{\dot{h}^2}{c^2}+h_z^2\right),
$$

which is positive for $K_T>0$. For an outgoing wave
$h=F(z-ct)$, one has $\dot{h}=-c h_z$, so

$$
u_{\rm TT}=K_T h_z^2,
\qquad
{\cal F}_{\rm TT}=cK_T h_z^2.
$$

The sign of $K_T$ is therefore not a harmless convention. Positive
outward energy loss in binary systems fixes the radiative sector to the
positive branch. Once the normalization is derived, this same sign gives
the standard gravitational-wave energy flux.

The sum-of-squares and outward-flux statements are verified in
`gate_G03_radiative_positivity.py`. The coefficient
$c^2/(32\pi G)$ is fixed in the later radiative bootstrap,
`radiative_bootstrap_KT.py`.
