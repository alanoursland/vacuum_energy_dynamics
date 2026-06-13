# Appendix B. Ghost-Exclusion Witness

This appendix gives the minimal instability witness for a propagating
negative sector.

Assume a scalar/static mode $s$ is promoted to a hyperbolic field while
retaining the negative energy sign derived in the static bootstrap. A
schematic Hamiltonian is

$$
H_s
=-\frac{K_s}{2}
\int
\left(
\frac{\dot{s}^2}{c^2}+|\nabla s|^2
\right)d^3x,
\qquad K_s>0 .
$$

Let $s_0$ be any smooth compact field configuration with nonzero
derivatives. Then

$$
H_s[s_0]<0 .
$$

For $\lambda s_0$,

$$
H_s[\lambda s_0]
=\lambda^2 H_s[s_0].
$$

Since $H_s[s_0]$ is negative,

$$
\lim_{\lambda\to\infty}H_s[\lambda s_0]=-\infty .
$$

The Hamiltonian has no lower bound. If this mode is coupled to a positive
radiative sector, the total energy can remain conserved while positive
radiation is produced and the negative sector runs downward without
limit. That is the standard ghost instability.

The only stable assignment for this negative sector is therefore
non-propagating. In the static problem this means elliptic/constraint
character: the scalar/static mode is solved from boundary conditions and
sources rather than evolved as an independent wave.

The corresponding verification script is
`vacuum_forge/src/field_equation_trials/006_gate_G03_radiative_positivity/gate_G03_radiative_positivity.py`.
