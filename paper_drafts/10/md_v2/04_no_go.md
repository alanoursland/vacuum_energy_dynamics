# 4. What static energy accounting can and cannot determine

The family derived in Sec. 2 contains the Schwarzschild exterior at

[
\lambda=-1,
]

but the assumptions used there do not select that value. A natural proposal is that gravitational field energy supplies the missing condition: gravitational binding energy is negative, and gravitational energy should gravitate with the same universal coupling as other forms of energy. Experimental tests of the Nordtvedt effect strongly constrain anomalous coupling of gravitational binding energy, so the proposal has a plausible physical motivation.

The difficulty is that the total energy of a gravitating system may be well defined even when its division into matter energy and local field energy is not. This section separates those two issues.

We first show that identifying an energy density directly from the nonlinear source equation is circular and therefore cannot determine (\lambda). We then use the convention-independent work required to assemble two spherical shells to constrain a particular class of local energy bookkeeping schemes.

The resulting no-go statement is conditional. It applies when the gravitational contribution is represented by the gradient-local density implied by the self-sourcing interpretation and when the matter ledger is restricted to a specified interval between local and asymptotic energy audits. Within that class, static accounting confines

[
\lambda\in\left[-\frac14,\frac14\right]
]

and therefore excludes the Schwarzschild value.

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

This gives the following elementary lemma.

> **Self-consistency lemma.** A field-energy density defined by reading the nonlinear source term from the equation under examination cannot be used to determine the coefficient of that term.

To constrain (\lambda), the relevant energy must instead be determined independently, for example from an operational work budget.

## 4.2 The invariant part of the energy ledger

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

The total (-U) is operationally fixed. The two terms on the left are bookkeeping assignments.

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

\frac{2Gm_i}{r^2c^2},\hat{\mathbf r}.
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
2\nabla s_1\cdot\nabla s_2,dV.
]

Using

[
dV=4\pi r^2dr,
]

we obtain

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
4\pi r^2,dr
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

### Local matter audit

A local audit records each shell at its locally measured rest energy. No interaction correction is entered in the matter column:

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

### Asymptotic matter audit

An asymptotic audit records each shell according to the energy associated with it after gravitational redshift relative to infinity is included.

At leading order, shell 1 receives the potential correction produced by shell 2, and shell 2 receives the correction produced by shell 1. Each contributes

[
-U
]

to the matter ledger, so together

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

Here the matter column contains more negative interaction energy than the total system possesses, and the field column supplies a positive correction.

### Interpolating convention

Introduce a parameter (f) by writing

[
E_{\rm matter,cross}=-2fU.
]

The local audit corresponds to

[
f=0,
]

and the asymptotic audit to

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

If admissible matter conventions are restricted to fixed convex mixtures of the local and asymptotic audits,

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

The invariant assembly energy cannot by itself exclude this ledger, because it measures only the total. The objection is instead to its interpretation: the matter column is credited with a positive interaction energy that exceeds the locally measured rest-energy assignment, while the field contribution is already represented separately by the gradient term.

Within the bookkeeping framework adopted here, such a convention lies outside the interval between the local and asymptotic audits.

The restriction

[
0\le f\le1
]

must therefore be recognized as part of the theorem’s assumptions. The invariant work budget fixes (-U), but it does not by itself prove that every conceivable matter–field decomposition must lie in this interval.

## 4.5 Conditional no-go result

The calculation establishes the following result.

> **Conditional static-accounting no-go.**
> Assume:
>
> 1. the metric family and constant self-sourcing coefficient of Sec. 2;
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

The result is stronger than the statement that static bookkeeping leaves (\lambda) undetermined. Under the specified localization and convention class, it selects values near zero rather than the Schwarzschild value.

It is not a theorem that every conceivable static energy argument fails. Such a universal statement would require proving that all admissible localizations and matter conventions reduce to the class above. The invariant assembly process fixes the total energy, but the matter–field division remains an additional structural choice.

## 4.6 The factor-of-four mismatch

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

to the field cross energy. To preserve the correct total, the matter ledger must then contribute

[
+3U.
]

Thus the Schwarzschild nonlinearity cannot be identified with the standard Newtonian gradient-energy density counted once. Within the present bookkeeping scheme, its coefficient differs by a factor of four in magnitude.

## 4.7 Interpretation

The two-shell assembly exposes the distinction between energy conservation and dynamical self-coupling.

Energy conservation determines the total interaction energy:

[
E_{\rm int}=-U.
]

It does not uniquely determine the local gravitational energy density or its division from matter energy. Once a particular gradient-local density and a restricted matter convention are imposed, the resulting coefficient lies in

[
\left[-\frac14,\frac14\right].
]

The Schwarzschild coefficient

[
\lambda=-1
]

therefore does not emerge from that static ledger.

This identifies the obstruction more precisely than the statement that Newtonian and special-relativistic reasoning cannot determine the second-order metric. Within the family, the missing information is one coefficient. Static accounting constrains that coefficient only after additional localization choices are made, and the resulting range does not include the general-relativistic value.

Related bootstrapped-Newtonian constructions introduce an explicit nonlinear coupling and select its value by matching the Schwarzschild post-Newtonian expansion. The analysis above explains why such matching is not replaced by the static accounting considered here: the desired coupling is dynamical information, not a consequence of the invariant assembly energy alone.

A dynamics-based derivation may determine the coefficient through consistency of gravitational self-coupling, while observation may determine it through the post-Newtonian parameter (\beta). The latter route is developed in Sec. 5.
