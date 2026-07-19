# 6. Michell’s radius and the Painlevé–Gullstrand condition

In 1784, Michell combined the Newtonian escape relation

[
\frac12v^2=\frac{GM}{r}
]

with the condition (v=c) and obtained

[
r=\frac{2GM}{c^2}=r_s.
]

Laplace later gave the same argument. The numerical result is the Schwarzschild radius, although the calculation predates general relativity by more than a century and applies Newtonian mechanics outside its domain of validity. The nonrelativistic kinetic-energy formula is not valid at (v=c), and Newtonian gravity supplies neither a spacetime metric nor a causal horizon.

Michell’s premises do not determine the Schwarzschild geometry, but the dimensional observation alone does not account for the exact coefficient. Every member of the family can be written on its static exterior in a Painlevé–Gullstrand-type form. Exact agreement of the radial shift with the Newtonian profile at every radius holds only for Schwarzschild.

Throughout this section, the Painlevé–Gullstrand construction is understood on the branch (A>0). For Schwarzschild, the coordinates extend regularly through (A=0).

## 6.1 Painlevé–Gullstrand form of the family

The coordinate form used here is due to Painlevé (1921) and Gullstrand (1922).

Begin with

[
ds^2
====

-A(r)c^2dt^2
+
\frac{dr^2}{A(r)}
+
r^2d\Omega^2.
]

Introduce a new time coordinate (T) through

[
dt
==

dT
-
\frac{\sqrt{1-A(r)}}{cA(r)}\,dr.
]

Substitution gives

[
ds^2
====

-c^2dT^2
+
\left[
dr+v(r)dT
\right]^2
+
r^2d\Omega^2,
]

where

[
\boxed{
v(r)=c\sqrt{1-A(r)}
}.
]

Expanding the square,

[
ds^2
====

-\left(c^2-v^2\right)dT^2
+
2v\,dr\,dT
+
dr^2
+
r^2d\Omega^2.
]

The spatial geometry on a surface of constant (T) is

[
d\ell^2
=======

dr^2+r^2d\Omega^2,
]

the metric of flat Euclidean space in spherical coordinates. The gravitational geometry has not disappeared. It is encoded partly in the mixed term

[
2v\,dr\,dT,
]

which couples radial position to time and tilts the radial light cones.

The function (v(r)) is often described as a river velocity (Hamilton and Lisle 2008). This is a representation of the coordinate shift, not the velocity of a material substance.

For the family

[
A_\lambda(r)
============

\left(
1+\lambda\frac{r_s}{r}
\right)^{-1/\lambda},
]

the corresponding profile is

[
\boxed{
v_\lambda(r)
============

c\sqrt{
1-
\left(
1+\lambda\frac{r_s}{r}
\right)^{-1/\lambda}
}
}.
]

All members therefore admit the same flat-slice form; they differ in the radial profile (v_\lambda(r)).

Painlevé–Gullstrand-type coordinates alone do not select a member. Exact equality with the Newtonian velocity profile at every radius selects Schwarzschild.

## 6.2 The unique Newtonian profile

The Newtonian speed of a particle falling from rest at infinity satisfies

[
\frac12v_{\rm N}^2=\frac{GM}{r}.
]

Using

[
r_s=\frac{2GM}{c^2},
]

this may be written as

[
\frac{v_{\rm N}^2}{c^2}
=======================

\frac{r_s}{r}.
]

The Painlevé–Gullstrand relation gives

[
\frac{v_\lambda^2}{c^2}
=======================

1-A_\lambda(r).
]

Exact agreement with the Newtonian profile at every radius therefore requires

[
1-A_\lambda(r)
==============

\frac{r_s}{r}.
]

Equivalently,

[
A_\lambda(r)
============

1-\frac{r_s}{r}.
]

This is precisely the member

[
\boxed{
\lambda=-1
}.
]

Thus

[
\boxed{
v_{-1}(r)
=========

\sqrt{\frac{2GM}{r}}
}
]

holds exactly throughout the Schwarzschild exterior.

The uniqueness can also be seen from the weak-field expansion:

[
1-A_\lambda
===========

x-\frac{1+\lambda}{2}x^2+O(x^3),
\qquad
x=\frac{r_s}{r}.
]

Every member reproduces the Newtonian profile at leading order,

[
\frac{v_\lambda^2}{c^2}=x+O(x^2),
]

but the quadratic correction vanishes only when

[
1+\lambda=0.
]

This is a dynamical or slicing condition stronger than the Newtonian limit. The Newtonian weak-field condition requires agreement only when (r_s/r\ll1); the condition above imposes the Newtonian velocity law at every radius.

## 6.3 Radial light propagation

The Painlevé–Gullstrand metric makes the causal significance of the profile transparent.

For radial light,

[
ds^2=0,
\qquad
d\Omega=0.
]

Therefore,

[
0
=

-c^2dT^2
+
\left(
dr+v\,dT
\right)^2.
]

Taking the two square-root branches gives

[
dr+v\,dT=\pm c\,dT,
]

and hence

[
\boxed{
\frac{dr}{dT}=-v\pm c
}.
]

The outward and inward radial coordinate velocities are

[
\left(
\frac{dr}{dT}
\right)_{\rm out}
=================

c-v,
]

and

[
\left(
\frac{dr}{dT}
\right)_{\rm in}
================

-c-v.
]

At a surface where

[
v=c,
]

outward-directed light satisfies

[
\left(
\frac{dr}{dT}
\right)_{\rm out}=0.
]

For (v>c), even the outward branch has

[
\frac{dr}{dT}<0.
]

This causal behavior is not Newtonian. It follows from the mixed space–time term in the relativistic metric. The velocity profile may have a Newtonian form, but the geometry in which it appears does not.

For the Schwarzschild member,

[
v^2=\frac{2GM}{r}.
]

The condition (v=c) therefore gives

[
c^2=\frac{2GM}{r},
]

or

[
\boxed{
r=r_s
}.
]

The same equation used by Michell consequently identifies the Schwarzschild horizon radius when interpreted through the independently selected Schwarzschild geometry.

## 6.4 Logical role of Michell’s calculation

Michell’s calculation supplies neither the radial metric component nor the mixed space–time structure of Painlevé–Gullstrand coordinates. Its Newtonian premises therefore do not determine the Schwarzschild member or the causal behavior of light at (r_s).

The valid logical direction is

[
\text{dynamics or observation}
\longrightarrow
\lambda=-1,
]

followed by

[
\lambda=-1
\longrightarrow
v^2=\frac{2GM}{r}
\quad\text{in Painlevé--Gullstrand form},
]

and therefore

[
v=c
\longrightarrow
r=r_s.
]

The Newtonian velocity relation is exact for the Painlevé–Gullstrand shift of the independently selected Schwarzschild member. This accounts for the numerical coefficient without treating the Newtonian argument as a metric derivation.

## 6.5 Why the time coefficient is insufficient

Pairing the temporal coefficient (A=1-r_s/r) with a static Euclidean spatial metric gives (\gamma=0) and half the leading general-relativistic light deflection. Flat Painlevé–Gullstrand slices do not have this defect because the full metric contains the mixed term (2v\,dr\,dT). Michell’s velocity relation becomes physically meaningful only after the remaining metric structure has been supplied.

![Figure 3](figure_3_river_ledger.png)

*Figure 3. Painlevé–Gullstrand profiles (v_\lambda(r)/c=\sqrt{1-A_\lambda(r)}), compared with the Newtonian infall profile (\sqrt{r_s/r}). The Schwarzschild member (\lambda=-1) coincides with the Newtonian curve at every radius. All other members agree at leading order for (r\gg r_s) and depart at nonlinear order. Source: `src_fig/figure_3_river_ledger.py`.*
