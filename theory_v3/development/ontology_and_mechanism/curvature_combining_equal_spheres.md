# Curvature Combining for Two Identical Spherical Masses

## Status

This is a development note. Its purpose is to show one specific mechanism:
the kinetic energy gained in gravitational infall is exactly the energy
difference produced when two initially separate curvature fields become one
combined curvature configuration. It does not postulate or require vacuum
creation or destruction.

The calculation is exact within its stated weak-field assumptions. Its
interpretation in terms of vacuum curvature belongs to the framework. The
calculation does not provide a covariant local gravitational-energy density,
a microscopic transfer current, or a strong-field merger solution.

## 1. Central Claim

Two isolated spherical masses do not carry two immutable gravitational wells
whose energies can be added independently at every separation. As the masses
approach, their fields form one combined configuration. Because the energy is
quadratic in the field, the energy of the sum is not the sum of the separate
energies. The difference is a separation-dependent cross-term.

For two identical masses, that physical interaction term is

$$
U_{12}(d)=-\frac{Gm^2}{d}.
$$

As the separation decreases, $U_{12}$ becomes more negative. In the
nonradiative Newtonian ledger, the decrease is exactly the increase in the
total kinetic energy of the two bodies:

$$
\Delta K=-\Delta U_{12}.
$$

The framework interpretation is that potential curvature is being combined
and reorganized into kinetic energy. Nothing in this identity requires a
change in vacuum amount. It is configuration conversion, not vacuum
destruction.

The complete infall ledger is therefore

$$
\boxed{
E_{\mathrm{combined}}(d)-E_1-E_2
=-\frac{Gm^2}{d}
=-K_{\mathrm{gained}}(d)
}.
$$

This equality, rather than the later material-merger model, is the central
result of the note.

## 2. Setup and Scope

Consider two identical, nonrotating spherical bodies. Each has:

```text
mass:    m
radius:  r
```

Let $d$ be their center-to-center separation. Before contact,

$$
d\geq 2r.
$$

Assume:

1. weak compactness, $Gm/(rc^2)\ll 1$;
2. slow motion compared with $c$;
3. spherical symmetry of each body before contact;
4. negligible radiation during the idealized infall ledger;
5. asymptotic flatness, with each potential vanishing at infinity.

For the merger endpoint calculation only, also assume that each initial body
is a uniform sphere and that the final body is a uniform sphere with mass
$2m$ and radius $r$. The final body therefore has twice the initial mean
density. These extra assumptions are not needed for the non-overlap
interaction term.

The Newtonian potentials satisfy

$$
\nabla^2\Phi_i=4\pi G\rho_i,
\qquad
\Phi_i\rightarrow 0\quad\text{at infinity},
$$

and the weak-field solution superposes:

$$
\Phi=\Phi_1+\Phi_2.
$$

Here $\Phi$ is a weak-field metric and constraint-sector proxy. Calling its
configuration a curvature well is framework language; $\nabla\Phi$ is not
itself the four-dimensional Riemann tensor.

## 3. Stored Strain Is Not the Reduced Interaction

A positive quadratic strain functional can be written as

$$
J[\Phi]=\frac{1}{8\pi G}\int |\nabla\Phi|^2\,d^3x.
$$

For $\Phi=\Phi_1+\Phi_2$, this contains a positive cross-term:

$$
J_{12}=\frac{1}{4\pi G}
\int\nabla\Phi_1\mathbin{\cdot}\nabla\Phi_2\,d^3x
=+\frac{Gm^2}{d}.
$$

Taken by itself, this term would give repulsion. It is therefore not the
physical mechanical interaction energy.

The source-coupled functional is

$$
E[\Phi;\rho]
=\frac{1}{8\pi G}\int|\nabla\Phi|^2\,d^3x
+\int\rho\Phi\,d^3x.
$$

Its stationary equation is Poisson's equation. Eliminating the stationary
field gives the reduced energy

$$
E_{\mathrm{red}}[\rho]
=\frac12\int\rho\Phi\,d^3x
=-\frac{1}{8\pi G}\int|\nabla\Phi|^2\,d^3x.
$$

Thus the positive stored-strain term and the source coupling must be counted
together. Their on-shell combination gives a negative interaction between
positive masses. This is the sign distinction established by the
source-coupled reduced-action work:

```text
positive stored strain + source coupling = negative reduced interaction
```

## 4. The Two-Sphere Cross-Term

Expanding the reduced field energy gives

$$
E_{\mathrm{red}}=U_1+U_2+U_{12},
$$

where $U_1$ and $U_2$ are the separation-independent self terms and

$$
U_{12}
=-\frac{1}{4\pi G}
\int\nabla\Phi_1\mathbin{\cdot}\nabla\Phi_2\,d^3x.
$$

Integration by parts, with the boundary term vanishing at infinity, gives

$$
U_{12}
=\int\rho_1\Phi_2\,d^3x
=\int\rho_2\Phi_1\,d^3x.
$$

For non-overlapping spherical bodies, the shell theorem makes each body act
on the other as though its mass were concentrated at its center. Therefore

$$
\boxed{U_{12}(d)=-\frac{Gm^2}{d}},
\qquad d\geq 2r.
$$

This result is independent of the bodies' radial density profiles while they
remain spherical and non-overlapping.

The generalized force associated with the separation coordinate is

$$
F_d=-\frac{dU_{12}}{dd}
=-\frac{Gm^2}{d^2}.
$$

The negative sign means that the force acts toward decreasing separation.
This is the Newtonian attractive force.

## 5. Infall From Infinity

At infinite separation,

$$
U_{12}(\infty)=0.
$$

At separation $d$,

$$
\Delta U_{12}
=U_{12}(d)-U_{12}(\infty)
=-\frac{Gm^2}{d}.
$$

If the bodies begin at rest and radiation is neglected, conservation of the
reduced mechanical energy gives

$$
\boxed{K_{\mathrm{total}}(d)=\frac{Gm^2}{d}}.
$$

Both bodies contribute to this total kinetic energy. In the center-of-mass
frame they have equal speeds $v$, so

$$
K_{\mathrm{total}}=2\left(\frac12mv^2\right)=mv^2,
$$

and hence

$$
v^2=\frac{Gm}{d}.
$$

The ledger closes with one conversion:

```text
decrease of reduced potential-curvature energy
                        ->
increase of matter kinetic energy
```

There is no second payer and no residual that needs to be assigned to vacuum
substance.

## 6. First Contact

The spheres first touch at

$$
d=2r.
$$

The interaction energy is then

$$
U_{12}(2r)=-\frac{Gm^2}{2r},
$$

and the kinetic energy gained from rest at infinity is

$$
K_{\mathrm{contact}}=\frac{Gm^2}{2r}.
$$

Each sphere has

$$
v^2=\frac{Gm}{2r}
$$

in the center-of-mass frame under the idealized nonradiative assumptions.

For uniform spheres, each self-energy is

$$
U_{\mathrm{self}}(m,r)=-\frac{3Gm^2}{5r}.
$$

The total configuration energy just before contact is therefore

$$
U_{\mathrm{touch}}
=2U_{\mathrm{self}}+U_{12}(2r)
=-\frac{17}{10}\frac{Gm^2}{r}.
$$

The self terms were already present at infinity. The energy released during
the approach is only the change in the interaction term, not the self-energy
of each pre-existing body.

## 7. The Fixed-Radius Combination Identity

The same cross-term can be displayed by comparing two spherical exterior
fields with one combined exterior field at the same radius $r$.

For the negative potential-sector energy,

$$
U_{\mathrm{ext}}(m,r)=-\frac{Gm^2}{2r}.
$$

The two separate exterior configurations have

$$
U_{\mathrm{sep,ext}}
=2U_{\mathrm{ext}}(m,r)
=-\frac{Gm^2}{r}.
$$

The combined exterior configuration of mass $2m$ and radius $r$ has

$$
U_{\mathrm{comb,ext}}
=U_{\mathrm{ext}}(2m,r)
=-\frac{2Gm^2}{r}.
$$

Therefore

$$
\boxed{
U_{\mathrm{comb,ext}}-U_{\mathrm{sep,ext}}
=-\frac{Gm^2}{r}
},
$$

and the positive magnitude of the curvature-combination difference is

$$
\boxed{K_{\mathrm{gained}}=\frac{Gm^2}{r}}.
$$

This is the equal-mass, fixed-radius form of the general interaction identity
$K_{\mathrm{gained}}=Gm^2/d$, with the comparison scale set to $d=r$.

The equality is an exterior-field ledger. It isolates the cross-term that
accounts for infall kinetic energy. It should not be confused with the full
self-energy of matter inside the radius, which depends on the density profile
and introduces additional compression bookkeeping.

## 8. Full Uniform-Sphere Endpoint

Suppose the two uniform spheres combine and settle into one uniform sphere
with mass $2m$ and radius $r$. The final volume is the volume of either
initial sphere, so its mean density is

$$
\rho_f=2\rho_i.
$$

The final self-energy is

$$
U_f
=-\frac{3G(2m)^2}{5r}
=-\frac{12}{5}\frac{Gm^2}{r}.
$$

The initial self-energy at infinite separation was

$$
U_i=2U_{\mathrm{self}}
=-\frac65\frac{Gm^2}{r}.
$$

The total configuration-energy change from separated bodies at infinity to
the settled merged sphere is

$$
\Delta U_{\mathrm{merge}}
=U_f-U_i
=-\frac65\frac{Gm^2}{r}.
$$

Thus the total decrease in gravitational configuration energy is

$$
\boxed{
E_{\mathrm{release}}
=\frac65\frac{Gm^2}{r}
}.
$$

This release has two stages in the endpoint ledger:

$$
E_{\mathrm{approach}}=\frac12\frac{Gm^2}{r},
$$

from infinity to first contact, and

$$
E_{\mathrm{settling}}
=\frac7{10}\frac{Gm^2}{r},
$$

from first contact to the final fixed-radius sphere. The two contributions
sum to

$$
\frac12\frac{Gm^2}{r}+\frac7{10}\frac{Gm^2}{r}
=\frac65\frac{Gm^2}{r}.
$$

This is the gravitational configuration-energy release. Compressing twice
the mass into the original radius generally raises the matter's internal
energy, so the energy available to escape as radiation or ejecta can be less
than this amount. The endpoint calculation does not supply an equation of
state or determine the partition. Depending on the bodies and dynamics, the
released gravitational energy can remain as bulk motion or be converted into
compression energy, oscillation, heat, ejecta, electromagnetic radiation, or
gravitational radiation. Without pressure support and dissipative channels,
the merged body need not settle into the assumed final state.

## 9. What "Curvature Combining" Means

The phrase has a precise limited meaning in this model.

At infinite separation, the total configuration contains two self terms and
no interaction term. At finite separation, the fields overlap and the
configuration functional produces a cross-term. As separation decreases,
that cross-term becomes increasingly negative. After merger, the original
decomposition into two self fields ceases to be natural; there is one new
configuration sourced by the combined mass distribution.

Therefore:

```text
two separated curvature configurations
                 ->
one separation-dependent combined configuration
                 ->
one reorganized merged configuration
```

The kinetic and radiative energy released during this process is balanced by
the change in the combined configuration energy.

This does not mean that curvature is a material fluid flowing from the field
into the bodies. It means that the matter and gravitational configuration are
one coupled system whose reduced energy changes as its configuration changes.

It also does not mean that a positive local strain cost decreases everywhere.
The integrand

$$
-\frac{1}{4\pi G}
\nabla\Phi_1\mathbin{\cdot}\nabla\Phi_2
$$

is spatially distributed and is not sign-definite point by point. The robust
statement is about the integrated interaction term.

## 10. No Vacuum Destruction

Nothing in the calculation changes the amount of vacuum or spacetime. The
following quantities change:

```text
the matter separation,
the combined weak-field metric configuration,
the interaction cross-term,
the bodies' kinetic energy,
and, in a dynamical treatment, radiative curvature.
```

These changes are sufficient to close the energy ledger. Identifying the
negative interaction term with destroyed vacuum would add an ontological
claim that the calculation neither needs nor proves.

The conservative framework statement is:

```text
Infall converts potential-curvature configuration energy into kinetic and,
when present, radiative energy. Vacuum substance remains intact.
```

## 11. Locality and Relativistic Limits

The Newtonian cross-term has a distributed field representation, but its
integral depends on the complete two-body configuration. This note does not
derive a unique local transfer current telling where each increment of matter
kinetic energy came from.

That limitation becomes more important in general relativity, where a unique
gauge-invariant local gravitational-energy density is not generally
available. A relativistic completion must formulate the conversion through
the adopted covariant dynamics and its boundary or flux ledger without
counting the same interaction twice.

The fixed-radius uniform merged endpoint is not a model of black-hole merger,
neutron-star merger, or relativistic collapse. Those problems require the
full nonlinear field equations, matter dynamics, radiation, and possibly
strong-field interior physics.

## 12. Established and Not Established

### Established in the stated model

```text
U_12(d) = -Gm^2/d for non-overlapping spherical bodies.
F_d = -Gm^2/d^2.
K_total(d) = Gm^2/d for nonradiative infall from rest at infinity.
For the fixed-radius exterior comparison,
U_comb,ext(2m,r) - 2 U_ext(m,r) = -Gm^2/r = -K_gained.
K_contact = Gm^2/(2r).
For the uniform fixed-radius endpoint,
the gravitational configuration release is 6Gm^2/(5r) from infinity to the
settled merged sphere.
No vacuum-substance term is required to close these ledgers.
```

### Not established

```text
A covariant local density for the interaction energy.
A local microscopic current from curvature configuration to matter motion.
The time-dependent overlap calculation after the spheres make contact.
The partition of released energy among kinetic, thermal, material, and
radiative channels.
The strong-field merger energy or waveform.
Any change in vacuum amount.
```

## 13. Relationship to Earlier Burden Language

The earlier `gravity_as_vacuum_burden_reduction.md` proposed that attraction
might result from a lower total burden for combined mass constraints. That
idea was useful but did not distinguish positive stored strain from the full
source-coupled reduced energy.

The present result keeps the defensible core and removes the ambiguity:

```text
Not established:
  every positive curvature or interface cost decreases as masses approach.

Established in the Newtonian model:
  the full reduced interaction energy decreases as the two curvature
  configurations combine.
```

This is the sense in which curvature combining supplies the infall ledger.
