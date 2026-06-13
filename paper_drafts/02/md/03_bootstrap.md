# 3. Static Bootstrap: Why the Scalar/Static Energy Is Negative

The sign problem enters before any wave equation is written down. In a
static, spherically symmetric exterior, let

$$
ds^2=-c^2 A(r)\,dt^2+B(r)\,dr^2+r^2d\Omega^2 ,
$$

and introduce the shear variable

$$
s(r)=\frac{1}{2}\ln\frac{A(r)}{B(r)} .
$$

In the compensated static exterior considered here, $A B=1$, so
$s=\ln A$ and $A=e^s$. The areal radial operator is

$$
\Delta_{\rm ar} f=\frac{1}{r^2}\frac{d}{dr}\left(r^2 f'\right).
$$

The static flux law is linear in the distortion variable $A$:

$$
\Delta_{\rm ar} A = \frac{8\pi G}{c^2}\rho .
$$

Outside the source, this reduces to

$$
\Delta_{\rm ar} A =0.
$$

The key point is that linearity in $A$ is not linearity in $s$. For any
radial function $s$,

$$
\Delta_{\rm ar}(e^s)
=e^s\left(\Delta_{\rm ar}s+(s')^2\right).
$$

Therefore the source-free exterior equation $\Delta_{\rm ar}A=0$ is
equivalent to

$$
\Delta_{\rm ar}s=-(s')^2 .
$$

The nonlinear term has the form of a self-source. If field/configuration
energy gravitates at the same universal coupling as matter, and is counted
once, the right-hand side fixes the static field-energy density:

$$
u_{\rm stat}=-\frac{c^4}{8\pi G}(s')^2 .
$$

The sign is the result. It is not inserted by convention and it is not a
choice made after comparing with radiation. It follows from asking for the
static flux law to be linear in the variable that already incorporates its
own accumulated temporal distortion.

Equivalently, one may write the family of possible self-coupled exterior
solutions as

$$
A_\lambda(r)=\left(1+\lambda\frac{r_s}{r}\right)^{-1/\lambda},
$$

where $\lambda$ is the coefficient of the quadratic self-source in

$$
\Delta_{\rm ar}s=\lambda(s')^2 .
$$

The weak-field limit does not distinguish the members of this family. The
self-coupling ledger does. The value $\lambda=-1$ is the member for which
the nonlinear term is exactly the field's own static energy counted at the
universal coupling, giving

$$
A(r)=1-\frac{r_s}{r}
=1-\frac{2GM}{c^2r}.
$$

The alternatives have clear interpretations. The limit $\lambda\to0$
corresponds to no self-coupling in the logarithmic variable, while
$\lambda=+1$ gives the opposite sign. The static bootstrap therefore
selects the negative-energy branch.

This is the first half of the stability puzzle. A negative-energy sector
has appeared, and it is not optional. The rest of the paper explains why
this does not make the theory unstable.

For provenance, the algebraic identity, the one-parameter family, and the
selection of $\lambda=-1$ are verified in
`trial_C2_self_coupling_bootstrap.py`. The exclusion of an explicit
positive scalar-source placement, which breaks the static compensated
sector by introducing $T^t{}_t\ne T^r{}_r$, is verified in
`trial_C3_spatial_bootstrap.py`.
