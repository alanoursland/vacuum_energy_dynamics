# 2. Explicit assumptions and the family they determine

The simple derivations considered in this paper use different combinations of a small number of recurring assumptions. To determine what these assumptions can establish, we formulate them in a common language and solve the resulting problem without imposing any additional dynamical condition.

We consider a static, spherically symmetric exterior written in areal coordinates,

[
ds^2
====

-A(r)c^2dt^2
+
B(r)dr^2
+
r^2d\Omega^2,
]

where

[
d\Omega^2=d\theta^2+\sin^2\theta\,d\phi^2.
]

The coordinate (r) is the areal radius: a sphere at fixed (r) has area (4\pi r^2). We restrict attention initially to a static branch on which (A(r)>0), and we impose asymptotic flatness,

[
A(r)\to1,
\qquad
B(r)\to1,
\qquad
r\to\infty.
]

The derivation uses three recurring ingredients and one closure condition.

## 2.1 Assumptions

### (I1) Newtonian weak-field condition

In the weak-field regime, clocks and orbits must reproduce Newtonian gravity with potential

[
\Phi(r)=-\frac{GM}{r}.
]

The time component of the metric therefore satisfies

[
A(r)
====

1+\frac{2\Phi}{c^2}
+
O\!\left(\frac{\Phi^2}{c^4}\right)
=================================

1-\frac{2GM}{rc^2}
+
O(r^{-2}).
]

We define

[
r_s\equiv\frac{2GM}{c^2},
\qquad
x\equiv\frac{r_s}{r},
]

so that

[
A(r)=1-x+O(x^2).
]

This assumption fixes both the mass scale (r_s) and the leading weak-field behavior. It does not determine the nonlinear terms in (A(r)).

### (I2) Areal-coordinate flux law

We investigate the consequences of requiring that there exist a monotonic function (V(A)) whose radial gradient obeys an exact Gauss-type law in the vacuum exterior:

[
\Delta V
\equiv
\frac{1}{r^2}\frac{d}{dr}
\left(
r^2\frac{dV}{dr}
\right)
=0.
]

Here (\Delta) denotes the ordinary radial flux operator constructed from the areal coordinate (r). It is not the spacetime wave operator or the Laplace–Beltrami operator of a curved spatial slice.

Equivalently,

[
4\pi r^2V'(r)=\text{constant}.
]

The factor (4\pi r^2) is the area of a sphere of areal radius (r). Thus (V'(r)) is the radial field strength associated with the chosen potential variable, while (4\pi r^2V'(r)) is its total flux through the sphere.

The flux is constant because every sphere in the vacuum exterior encloses the same source under the postulated flux law. The local field strength varies as

[
V'(r)\propto\frac{1}{r^2}.
]

Integration gives

[
V(r)=V_\infty-\frac{K}{r}.
]

Assumption (I1) fixes the weak-field normalization. We choose (V) so that

[
V(r)
====

1+\frac{2\Phi}{c^2}
+\cdots
=======

1-\frac{r_s}{r}
+\cdots.
]

The central freedom is that the flux law does not specify which function of the metric coefficient (A) should play the role of (V). An exact flux law for (A), for (\ln A), and for (1/A) produces different nonlinear metrics even though all choices agree at Newtonian order after normalization.

The areal-coordinate flux law is a postulate of the construction. It is not asserted as a covariant vacuum field equation or a general consequence of the Einstein equations.

### (I3) Reciprocal metric condition

We impose

[
A(r)B(r)=1.
]

Equivalently,

[
g_{tt}g_{rr}=-1
]

in the coordinates used here. The radial metric coefficient is therefore fixed once (A(r)) is known:

[
B(r)=\frac{1}{A(r)}.
]

This relation holds for the Schwarzschild exterior and appears either as an assumption or as the result of an auxiliary argument in the simple derivations under consideration. Kassner (2015) discusses its status in detail, and Jacobson (2007) gives a general condition under which it holds.

It is not a consequence of static spherical symmetry alone. Here it is an explicit assumption defining the metric class under study.

The condition expresses a reciprocal relation between the time and radial coefficients. For a stationary clock,

[
d\tau=\sqrt{A(r)}\,dt,
]

whereas a radial proper-distance element at fixed time is

[
d\ell=\sqrt{B(r)}\,dr
=\frac{dr}{\sqrt{A(r)}}.
]

A reduction in the clock-rate factor is therefore accompanied by an inverse increase in the radial-distance factor.

The condition also fixes the time–radial contribution to the metric determinant. It does not imply that ordinary three-dimensional spatial volume is unchanged.

Every member derived below satisfies (AB=1). The condition reduces the number of unknown metric functions but cannot select one member of the family over another.

### (I4) Constant nonlinear coefficient

Assumption (I2) leaves an unrestricted choice of the potential variable (V(A)). We reduce this freedom by requiring that, when the flux equation is rewritten in a fixed metric variable, the coefficient of the nonlinear squared-gradient term be a constant of the theory rather than a function of the local field strength.

Conditions (I1)–(I3) do not restrict the functional choice of (V(A)). To obtain a definite and auditable class, we impose the additional closure condition that the nonlinear coefficient be constant.

The assumption does not require the nonlinear coefficient to be nonzero. It permits

[
\lambda=0,
]

corresponding to no squared-gradient nonlinearity in the chosen metric variable. It requires only that

[
\lambda=\text{constant},
]

rather than (\lambda=\lambda(A)).

The completeness result below is relative to assumptions (I1)–(I4), not a classification of all possible static, spherically symmetric metrics.

## 2.2 Logarithmic metric variable

Define

[
s(r)\equiv\ln A(r).
]

This is a change of variable, not a new independent field. Since

[
A=e^s,
\qquad
B=e^{-s},
]

the complete time–radial metric is determined by (s(r)).

The variable (s) is particularly useful because it reduces to a dimensionless Newtonian potential in the weak field. When (A=1+\epsilon) with (|\epsilon|\ll1),

[
s=\ln A=\epsilon+O(\epsilon^2),
]

and hence

[
s
=

\frac{2\Phi}{c^2}
+\cdots
=======

-\frac{r_s}{r}
+\cdots.
]

## 2.3 Complete potential class under constant closure

Let the potential variable be an arbitrary monotonic function

[
V=F(s),
]

with

[
F'(s)\neq0
]

on the branch of interest. The chain rule gives

[
\Delta V
========

F'(s)\Delta s
+
F''(s)(s')^2.
]

Imposing

[
\Delta V=0
]

and dividing by (F'(s)) yields

[
\Delta s
========

-\frac{F''(s)}{F'(s)}(s')^2.
]

The effective nonlinear coefficient is therefore

[
\lambda(s)
==========

-\frac{F''(s)}{F'(s)}.
]

For a general function (F), this coefficient depends on (s) and therefore on the local field strength. Assumption (I4) requires

[
-\frac{F''(s)}{F'(s)}=\lambda,
]

where (\lambda) is constant. Hence

[
F''(s)=-\lambda F'(s).
]

The flux equation is then

[
\boxed{
\Delta s=\lambda(s')^2
},
\qquad
\Delta s=s''+\frac{2}{r}s'.
]

This equation establishes the nonlinear term and its constant coefficient. Interpreting ((s')^2) as a gravitational energy density requires the additional accounting choices in Sec. 4.

For (\lambda\neq0), the solution is

[
F(s)=C_0+C_1e^{-\lambda s}.
]

Since (A=e^s),

[
F(s)=C_0+C_1A^{-\lambda}.
]

The constants (C_0) and (C_1\neq0) amount only to an additive shift and multiplicative normalization of the potential and do not alter the vacuum equation. The essential variable is therefore

[
V\propto A^{-\lambda}.
]

For (\lambda=0),

[
F''(s)=0,
]

so

[
F(s)=C_0+C_1s,
]

and the essential variable is

[
V\propto\ln A.
]

The power-law variables, together with the logarithmic limiting case, form the complete class allowed by assumptions (I2) and (I4).

## 2.4 Direct integration and classification theorem

Section 2.3 showed that, for (\lambda\neq0), the essential potential variable is (A^{-\lambda}). Assumption (I2) therefore gives

[
\Delta\!\left(A^{-\lambda}\right)=0.
]

The asymptotically flat spherical solution has the form

[
A^{-\lambda}=C_0+\frac{C_1}{r}.
]

Asymptotic flatness fixes (C_0=1). The Newtonian expansion

[
A(r)=1-\frac{r_s}{r}+O(r^{-2})
]

implies

[
A^{-\lambda}
================

1+\lambda\frac{r_s}{r}+O(r^{-2}),
]

so (C_1=\lambda r_s). Hence

[
\boxed{
A_\lambda(r)
============

\left(
1+\lambda\frac{r_s}{r}
\right)^{-1/\lambda}
},
\qquad
\boxed{
B_\lambda(r)=A_\lambda(r)^{-1}
}.
]

For (\lambda=0), the essential potential variable is (s=\ln A), and the flux equation becomes

[
\Delta s=0.
]

The Newtonian and asymptotic conditions give

[
s(r)=-\frac{r_s}{r},
\qquad
A_0(r)=e^{-r_s/r}.
]

This is also the continuous limit

[
\lim_{\lambda\to0}
\left(
1+\lambda\frac{r_s}{r}
\right)^{-1/\lambda}
====================

e^{-r_s/r}.
]

> **Classification theorem.** Consider a connected, static, spherically symmetric, asymptotically flat exterior branch with (A>0), written in areal coordinates. Impose the Newtonian weak-field condition (I1), the areal-coordinate flux law for a monotonic variable (V=F(\ln A)) (I2), the reciprocal metric condition (AB=1) (I3), and the constant-coefficient closure condition (-F''/F'=\lambda) (I4). Then
> [
> \Delta s=\lambda(s')^2,
> \qquad
> s=\ln A,
> ]
> and the boundary conditions determine
> [
> A_\lambda(r)
> =============
>
> \left(1+\lambda\frac{r_s}{r}\right)^{-1/\lambda},
> \qquad
> B_\lambda(r)=A_\lambda(r)^{-1},
> ]
> with (A_0=e^{-r_s/r}) by continuity. Conversely, every constant-(\lambda) member satisfies (I1)–(I4) on its static domain. The family is complete relative to these assumptions; they do not determine (\lambda).

## 2.5 Distinguished members

Three members provide useful reference points:

| (\lambda) | Exact-flux variable | (A_\lambda(r))   | Description   |
| --------: | ------------------- | ---------------- | ------------- |
|      (-1) | (A)                 | (1-r_s/r)        | Schwarzschild |
|       (0) | (\ln A)             | (e^{-r_s/r})     | exponential   |
|      (+1) | (1/A)               | ((1+r_s/r)^{-1}) | reciprocal    |

For

[
\lambda=-1,
]

the exact Gauss law is obeyed by (A) itself:

[
\Delta A=0.
]

The solution is

[
A_{-1}(r)=1-\frac{r_s}{r},
]

which gives the Schwarzschild exterior.

For

[
\lambda=0,
]

the exact Gauss law is obeyed by (s=\ln A):

[
\Delta(\ln A)=0,
]

giving

[
A_0(r)=e^{-r_s/r}.
]

For

[
\lambda=+1,
]

the exact Gauss law is obeyed by (1/A), giving

[
A_{+1}(r)=\frac{1}{1+r_s/r}.
]

The closed-form expression has appeared previously. Shuler (2018) exhibited the Schwarzschild metric and two alternatives in the common single-parameter form

[
g_{tt}
======

-\left(
1+n\frac{GM}{rc^2}
\right)^{-2/n},
]

with

[
n=2\lambda.
]

The values (n=-2,-1,+1) correspond to

[
\lambda=-1,-\frac12,+\frac12.
]

The three values displayed by Shuler are members of the continuous class derived above. Kassner (2019) later reviewed these metrics and showed that only the Schwarzschild member satisfies a standard relativistic generalization of Newton’s law. The result here derives the continuous class and establishes its completeness under (I1)–(I4), with (\lambda) identified as the constant squared-gradient coefficient. These assumptions leave (\lambda) undetermined.

## 2.6 Weak-field degeneracy

Expanding the family in

[
x=\frac{r_s}{r},
]

we obtain

[
A_\lambda
=========

1-x+\frac{1+\lambda}{2}x^2+O(x^3).
]

The first-order term,

[
-x=-\frac{r_s}{r},
]

is independent of (\lambda), as required by the Newtonian weak-field condition. The family members first differ at order (x^2), where the coefficient is

[
\frac{1+\lambda}{2}.
]

For the Schwarzschild member,

[
\lambda=-1,
]

this coefficient vanishes:

[
A_{-1}=1-x.
]

In areal coordinates, the Schwarzschild expansion terminates at first order. This termination is a coordinate-dependent statement; the invariant content is that the members differ in their nonlinear post-Newtonian behavior.

The weak-field degeneracy has immediate observational consequences. Experiments sensitive only to the leading gravitational redshift cannot determine (\lambda), because every member has

[
A_\lambda=1-x+O(x^2).
]

Likewise, assumption (I3) enforces a common first-order relation between the time and radial metric coefficients. As shown explicitly after transformation to isotropic coordinates in Sec. 5, this gives

[
\gamma=1
]

for every member. Light bending and radar time delay, whose leading PPN dependence is controlled by (\gamma), therefore do not distinguish the family.

The remaining freedom appears in the nonlinear PPN parameter (\beta). Perihelion precession is sensitive to this coefficient and can therefore discriminate among metrics that agree in the Newtonian limit and in (\gamma).

The family agrees in the (\gamma)-controlled part of the 1PN metric while leaving the (\beta)-controlled nonlinear coefficient undetermined; its members do not first diverge beyond 1PN order.

![Figure 1](figure_1_family.png)

*Figure 1. The metric function (A_\lambda(r)) for (\lambda\in{-1,-1/4,0,+1}). All members share the Newtonian limit and first differ at quadratic order in (r_s/r). For negative (\lambda), the plotted static branch reaches (A_\lambda=0) at (r=-\lambda r_s); this occurs at (r=r_s) for Schwarzschild and at (r=r_s/4) for (\lambda=-1/4). Members with (\lambda\geq0) remain positive for every finite (r>0). Source: `src_fig/figure_1_family.py`.*
