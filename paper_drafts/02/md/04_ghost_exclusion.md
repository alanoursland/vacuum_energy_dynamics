# 4. Ghost Exclusion: Why the Negative Sector Cannot Propagate

The negative sign derived in Sec. 3 is not by itself fatal. It becomes
fatal only if the corresponding sector is allowed to propagate as an
independent hyperbolic degree of freedom.

To see this, suppose the static shear $s$ were promoted to a wave-like
field while keeping the sign of its energy. A schematic wrong-sign
Hamiltonian density would have the form

$$
{\cal H}_s
=-\frac{K_s}{2}\left(\frac{\dot{s}^2}{c^2}+|\nabla s|^2\right),
\qquad K_s>0 .
$$

For any compact nonzero configuration $s$, scaling the amplitude by a
constant $\lambda$ gives

$$
H[\lambda s]=\lambda^2 H[s].
$$

Since $H[s]<0$ for a nontrivial witness, the energy is unbounded below:

$$
H[\lambda s]\rightarrow-\infty
\qquad\text{as}\qquad
\lambda\rightarrow\infty .
$$

Such a mode is a ghost. Coupled to any positive-energy radiative sector,
it would allow the vacuum to decay by producing positive-energy radiation
while the ghost sector runs to increasingly negative energy. Stability
therefore forbids the hyperbolic promotion.

The conclusion is not that the negative sector is harmless in every
formulation. The conclusion is sharper:

$$
\text{negative static energy}+\text{stability}
\quad\Longrightarrow\quad
\text{non-propagating constraint sector}.
$$

Thus the static scalar/conformal sector must be elliptic. Its value is
solved from the source configuration; it is not evolved as an independent
radiative field.

This is the structural move that makes the indefinite signature stable.
The same wrong-sign sector that would be pathological as a propagating
field is acceptable as a constraint. In standard GR language, this is the
role played by the Hamiltonian constraint in removing the dangerous
conformal propagation. Here the constraint assignment is reached from the
static self-coupling sign plus the stability requirement.

The reduced theorem is verified in `gate_G03_radiative_positivity.py`,
where it appears as the ghost-exclusion result: hyperbolic promotion of
the negative temporal/static sector has a Hamiltonian unbounded below and
is therefore excluded.
