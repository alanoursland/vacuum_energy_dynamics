# Appendix D. Linear Underdetermination of the Radiative Normalization

This appendix gives the scaling argument behind Sec. 7.

Consider a reduced linear wave equation

$$
K_T\Box h=J,
$$

where $J$ is fixed by the source and $K_T$ is the kinetic normalization.
The retarded solution scales as

$$
h\propto\frac{J}{K_T}.
$$

The wave energy flux has the schematic form

$$
{\cal F}\propto K_T\dot{h}^2.
$$

Substituting the linear solution gives

$$
{\cal F}
\propto
K_T\left(\frac{\dot{J}}{K_T}\right)^2
\propto
\frac{\dot{J}^2}{K_T}.
$$

The radiation reaction work done on the source has the same scaling:

$$
P_{\rm work}\propto J\dot{h}
\propto
\frac{J\dot{J}}{K_T}.
$$

With the detailed retarded solution, the time-averaged work and flux
match for every value of $K_T$. Thus linear energy balance is not a
normalization condition. It confirms conservation after a normalization
has been chosen; it does not choose that normalization.

The missing information is supplied by self-coupling. The static sector
fixes the response normalization

$$
N=\frac{c^4}{8\pi G}.
$$

The wave's own second-order energy must source the background through the
same response. Reading the second-order effective stress of a TT wave
therefore fixes

$$
K_T=\frac{c^4}{16\pi G}.
$$

This is the reduced radiative bootstrap: the normalization that cannot be
determined at linear order is determined when the wave's own energy is
included in the source ledger.

The corresponding verification script is
`vacuum_forge/src/field_equation_trials/008_radiative_bootstrap/radiative_bootstrap_KT.py`.
