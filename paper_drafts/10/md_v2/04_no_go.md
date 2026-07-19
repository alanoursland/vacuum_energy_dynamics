# 4. Static energy accounting and the conditional bound

The family derived in Sec. 2 contains the Schwarzschild exterior at

[
\lambda=-1,
]

but the assumptions used there do not select that value. One proposal is that gravitational field energy supplies the missing condition: gravitational binding energy is negative, and gravitational energy should gravitate with the same universal coupling as other forms of energy. The Nordtvedt effect tests anomalous coupling of gravitational binding energy (Nordtvedt 1968; Williams, Turyshev, and Boggs 2004), giving physical motivation for examining this proposal.

The total energy of a gravitating system may be well defined even when its division into matter and local field energy is not. Reading an energy density directly from the nonlinear source equation cannot determine (\lambda), because the proposed density already contains that coefficient. The convention-independent work required to assemble two spherical shells instead constrains a specified class of local matter–field assignments.

The resulting bound is conditional. It applies when the gravitational contribution is represented by the gradient-local density implied by the self-sourcing interpretation and when the matter assignment is restricted to a specified interval between local and asymptotic conventions. Within that class, static accounting confines

[
\lambda\in\left[-\frac14,\frac14\right]
]

and therefore excludes the Schwarzschild value.

The invariant assembly energy remains (E_{\rm int}=-U) throughout. The calculation is internally consistent, but within the stated localization and matter conventions it does not yield the Schwarzschild nonlinear coefficient. This is not a claim that general relativity violates energy conservation.

## 4.1 Why universal coupling does not determine (\lambda)

In the weak field, let

[
\epsilon_{\rm m}=\rho c^2
]

denote the matter energy density. The sourced equation for the logarithmic metric variable (s=\ln A) has the form

[
\Delta s
========

\frac{8\pi G}{c^4}\epsilon_{\rm m}.
]

The coupling per unit energy density is therefore

[
\frac{8\pi G}{c^4}.
]

In vacuum, the family equation is

[
\Delta s=\lambda(s')^2.
]

It is tempting to rewrite this equation as

[
\Delta s
========

\frac{8\pi G}{c^4}u_\lambda
]

by defining

[
u_\lambda
\equiv
\lambda
\frac{c^4(s')^2}{8\pi G}.
]

One may then say that the field energy (u_\lambda) gravitates with the same coupling as matter.

This statement does not constrain (\lambda). The density (u_\lambda) has been defined to be whatever quantity makes the vacuum equation take the universally coupled form. Substitution merely returns the original equation:

[
\frac{8\pi G}{c^4}u_\lambda
===========================

\lambda(s')^2.
]

The statement is therefore true by construction for every (\lambda), including

[
\lambda=0,
\qquad
u_0=0.
]

> **Self-consistency lemma.** A field-energy density defined by reading the nonlinear source term from the equation under examination cannot be used to determine the coefficient of that term.

To constrain (\lambda), the relevant energy must instead be determined independently, for example from an operational work budget.

## 4.2 Invariant assembly energy

The localization of gravitational energy is convention dependent. Even in Newtonian gravity, the density

[
-\frac{|\nabla\Phi|^2}{8\pi G}
]

may be exchanged, up to boundary terms and the field equation, for a matter-supported expression such as

[
\frac12\rho\Phi.
]

In general relativity the corresponding ambiguity appears in the use of gravitational pseudotensors and quasi-local energy constructions.

Although the local split is ambiguous, the total work required to assemble a weakly gravitating system is not.

Consider two concentric thin spherical shells with masses (m_1) and (m_2), at radii

[
a<b.
]

The shells are assumed to lie in the weak-field regime, where all members of the family have the same leading Newtonian behavior.

The outer shell is lowered quasi-statically from infinity to radius (b) in the gravitational field of the inner shell. The winch extracts the positive work

[
W=\frac{Gm_1m_2}{b}.
]

Because the process is quasi-static, this energy does not remain as kinetic energy of the shell. It leaves the two-shell system. Energy conservation therefore fixes the interaction contribution to the assembled system’s total energy:

[
E_{\rm int}
===========

-\frac{Gm_1m_2}{b}.
]

For later convenience, define

[
U\equiv\frac{Gm_1m_2}{b}>0.
]

Then

[
E_{\rm int}=-U.
]

This result is independent of how the interaction energy is divided between matter and field:

[
E_{\rm matter,cross}
+
E_{\rm field,cross}
===================

-U.
]

The total (-U) is operationally fixed. The two terms on the left depend on the chosen matter–field convention.

The use of two shells isolates the interaction term. Each shell’s self-energy is unchanged during the assembly and cancels when the initial and final configurations are compared.

## 4.3 Cross term of the gradient-local field density

The self-sourcing interpretation of Sec. 2 assigns the gravitational contribution to the gradient-local density

[
u_{\rm field}
=============

\lambda
\frac{c^4|\nabla s|^2}{8\pi G}.
]

At leading weak-field order,

[
s=\frac{2\Phi}{c^2}.
]

Let

[
s=s_1+s_2
]

be the superposition of the weak fields of the two shells. Then

[
|\nabla s|^2
============

|\nabla s_1|^2
+
|\nabla s_2|^2
+
2\nabla s_1\cdot\nabla s_2.
]

The first two terms are the separate self-energy terms of the shells. The interaction contribution is the cross term

[
2\nabla s_1\cdot\nabla s_2.
]

By the spherical shell theorem, the field of a thin shell vanishes everywhere inside that shell. Consequently:

[
r<a:
\qquad
\nabla s_1=\nabla s_2=0;
]

[
a<r<b:
\qquad
\nabla s_1\neq0,
\quad
\nabla s_2=0;
]

[
r>b:
\qquad
\nabla s_1\neq0,
\quad
\nabla s_2\neq0.
]

The cross term is therefore supported only in the region exterior to the outer shell.

For (r>b),

[
s_i(r)
======

-\frac{2Gm_i}{rc^2},
]

and hence

[
\nabla s_i
==========

\frac{2Gm_i}{r^2c^2}\,\hat{\mathbf r}.
]

The two gradients are parallel, so their scalar product is positive:

[
\nabla s_1\cdot\nabla s_2
=========================

\frac{4G^2m_1m_2}{r^4c^4}.
]

The field cross energy is

[
E_{\rm field,cross}
===================

\frac{\lambda c^4}{8\pi G}
\int_{r>b}
2\nabla s_1\cdot\nabla s_2\,dV.
]

Using

[
dV=4\pi r^2dr,
]

is sufficient at the order retained here. The proper-volume correction is (\sqrt{B}=1+O(G)); multiplying it by the quadratic weak-field cross term changes the integrated energy only at higher order.

We obtain

[
\begin{aligned}
E_{\rm field,cross}
&=
\frac{\lambda c^4}{8\pi G}
\int_b^\infty
2
\left(
\frac{4G^2m_1m_2}{r^4c^4}
\right)
4\pi r^2\,dr
[4pt]
&=
4\lambda Gm_1m_2
\int_b^\infty\frac{dr}{r^2}
[4pt]
&=
4\lambda\frac{Gm_1m_2}{b}.
\end{aligned}
]

Thus

[
\boxed{
E_{\rm field,cross}=4\lambda U
}.
]

Because the integral multiplying (\lambda) is positive, the sign of the assigned field interaction energy is the sign of (\lambda).

## 4.4 Matter conventions

The invariant assembly budget requires

[
E_{\rm matter,cross}
+
4\lambda U
==========

-U.
]

The remaining question is how much interaction energy has already been assigned to the matter.

Two limiting conventions are useful.

### Local rest-energy convention

The local convention records each shell at its locally measured rest energy. No interaction correction is assigned to the matter term:

[
E_{\rm matter,cross}=0.
]

The field must then contain the entire binding deficit:

[
4\lambda U=-U.
]

Therefore,

[
\boxed{
\lambda=-\frac14
}.
]

In this convention, all of the interaction energy is assigned to the field.

### Asymptotic redshift convention

The asymptotic convention records each shell after gravitational redshift relative to infinity is included.

At leading order, shell 1 receives the potential correction produced by shell 2, and shell 2 receives the correction produced by shell 1. Each contributes

[
-U
]

to the matter term, so together

[
E_{\rm matter,cross}=-2U.
]

This double entry does not mean that the physical interaction energy is (-2U). It is the result of assigning the same pair interaction once to each matter element. The field term must compensate so that the total remains the invariant value (-U):

[
-2U+4\lambda U=-U.
]

Hence

[
\boxed{
\lambda=+\frac14
}.
]

Here the matter term contains more negative interaction energy than the total system, and the field term supplies a positive correction.

### Interpolating convention

Introduce a parameter (f) by writing

[
E_{\rm matter,cross}=-2fU.
]

The local convention corresponds to

[
f=0,
]

and the asymptotic convention to

[
f=1.
]

The balance equation becomes

[
-2fU+4\lambda U=-U.
]

Dividing by (U) gives

[
-2f+4\lambda=-1,
]

and therefore

[
\boxed{
\lambda=\frac{2f-1}{4}
}.
]

If admissible matter conventions are restricted to fixed convex mixtures of these two assignments,

[
0\leq f\leq1,
]

then

[
\boxed{
-\frac14\leq\lambda\leq\frac14
}.
]

The midpoint convention

[
f=\frac12
]

gives

[
\lambda=0.
]

The Schwarzschild value

[
\lambda=-1
]

would require

[
-1=\frac{2f-1}{4},
]

or

[
\boxed{
f=-\frac32
}.
]

This would assign the matter cross term

[
E_{\rm matter,cross}=+3U.
]

The field term would then be

[
E_{\rm field,cross}=-4U,
]

and the total would still equal

[
+3U-4U=-U.
]

The invariant assembly energy cannot by itself exclude this assignment, because it measures only the total. The assignment instead falls outside the adopted matter convention: the matter term receives a positive interaction energy exceeding the local rest-energy assignment while the field contribution is represented separately by the gradient term.

Within the class adopted here, such a convention lies outside the interval between the local and asymptotic assignments.

The restriction

[
0\le f\le1
]

must therefore be recognized as part of the theorem’s assumptions. The invariant work budget fixes (-U), but it does not by itself prove that every conceivable matter–field decomposition must lie in this interval.

## 4.5 Conditional static-accounting bound

> **Conditional static-accounting bound.**
> Assume:
>
> 1. the metric family and constant nonlinear coefficient of Sec. 2;
> 2. a gradient-local gravitational density
>    [
>    u_{\rm field}
>    =============
>
>    \lambda
>    \frac{c^4|\nabla s|^2}{8\pi G};
>    ]
> 3. a matter cross-energy convention
>    [
>    E_{\rm matter,cross}=-2fU
>    ]
>    with
>    [
>    0\le f\le1;
>    ]
> 4. the invariant two-shell assembly energy
>    [
>    E_{\rm int}=-U.
>    ]
>
> Then
> [
> \lambda=\frac{2f-1}{4}
> ]
> and consequently
> [
> -\frac14\le\lambda\le\frac14.
> ]
> The Schwarzschild value
> [
> \lambda=-1
> ]
> is excluded.

Within the stated class, the interval lies near zero and does not contain the Schwarzschild value. The bound concerns the specified matter–field split, not energy conservation in general relativity.

## 4.6 Localization corollary: the factor-of-four coefficient

The Schwarzschild member has

[
\lambda=-1.
]

Its proposed gradient-local source density is therefore

[
u_{-1}
======

-\frac{c^4|\nabla s|^2}{8\pi G}.
]

In the weak field,

[
s=\frac{2\Phi}{c^2},
]

so

[
|\nabla s|^2
============

\frac{4|\nabla\Phi|^2}{c^4}.
]

Substitution gives

[
u_{-1}
======

-4
\frac{|\nabla\Phi|^2}{8\pi G}.
]

The standard Newtonian gradient-energy density is

[
u_{\rm N}
=========

-\frac{|\nabla\Phi|^2}{8\pi G}.
]

Hence

[
\boxed{
u_{-1}=4u_{\rm N}
}.
]

The statement concerns the coefficient of the proposed local gradient density. It does not mean that the observable gravitational binding energy of the two-shell system is four times its Newtonian value. That total remains

[
E_{\rm int}=-U.
]

Rather, the Schwarzschild source term, interpreted through this localization, assigns

[
-4U
]

to the field cross energy. To preserve the correct total, the matter term must then contribute

[
+3U.
]

Thus the Schwarzschild nonlinearity cannot be identified with the standard Newtonian gradient-energy density counted once. In this localization, its coefficient differs by a factor of four in magnitude.

## 4.7 Interpretation

Energy conservation determines the total interaction energy. Converting that invariant total into a self-coupling coefficient also requires the localization and matter-assignment choices stated in the theorem. Static assembly energy alone therefore leaves the nonlinear coefficient undetermined.

Related bootstrapped-Newtonian constructions introduce an explicit nonlinear coupling and fix it by matching the Schwarzschild post-Newtonian expansion. Such matching supplies dynamical information absent from the static accounting considered here.

A dynamics-based derivation may determine the coefficient through consistency of gravitational self-coupling, while observation may determine it through the post-Newtonian parameter (\beta). The latter route is developed in Sec. 5.
