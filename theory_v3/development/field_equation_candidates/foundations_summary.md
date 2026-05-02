# Foundations Summary

## What This Document Is

This document summarizes the `01_foundations/` development group for the reduced exterior mode program.

It is not a postulate, theorem, proof, full field equation, or complete gravitational theory. It is a foundation-level development summary whose purpose is to consolidate the static spherical reduced-variable language, its gauge limitations, and its best current geometric reformulation.

This summary is based primarily on the Markdown development notes:

```text
candidate_log_scale_modes.md
candidate_covariant_parent_modes.md
candidate_orbit_space_modes.md
```

The accompanying scripts on gauge dependence and areal-gauge reconstruction support the same conclusions, but the conceptual source for this summary is the Markdown note set.

The most important result of this foundation group is:

```text
The reduced exterior variables kappa and s are useful static-spherical mode diagnostics,
but they are not raw coordinate-invariant scalar fields.
```

The best current geometric form is:

$$
\kappa=\frac12\ln\left(\frac{A}{|\nabla R|^2}\right),
$$

and:

$$
s=\frac12\ln\left(A|\nabla R|^2\right).
$$

The corresponding exterior compensation condition is:

$$
\kappa=0
\quad\Longleftrightarrow\quad
A=|\nabla R|^2.
$$

In areal gauge, where:

$$
|\nabla R|^2=\frac1B,
$$

this reduces to:

$$
AB=1.
$$

This is the foundation-level bridge from the raw areal-gauge identity to a gauge-aware spherical-reduction statement.

---

## Source Scope

This group covers the first foundation layer of the reduced exterior mode program.

It establishes:

```text
1. log-scale variables for the static spherical exterior,
2. compensated and uncompensated mode combinations,
3. a reduced parent-mode interpretation,
4. gauge dependence of the naive areal-gauge variables,
5. the areal-radius repair,
6. the orbit-space reformulation.
```

It does not establish:

```text
1. the weak shear source law as a derived field equation,
2. the exact A-flux source law as a foundation result,
3. a covariant action,
4. nonspherical gravity,
5. rotation,
6. gravitational waves,
7. full strong-field dynamics.
```

The foundation group should therefore be read as the reduced-variable and geometry-preparation group, not as the source-law or full-theory group.

---

## Static Spherical Setup

The starting point is the static spherical exterior metric in areal-radius form:

$$
ds^2=-A(r)c^2dt^2+B(r)dr^2+r^2d\Omega^2.
$$

Here:

```text
A(r) is the temporal metric coefficient.
B(r) is the radial metric coefficient.
r is the areal radius.
```

The areal-radius condition means that symmetry spheres have area:

$$
\text{Area}=4\pi r^2.
$$

This gauge choice matters. The variables defined below are clean in this reduced form, but they are not automatically invariant under arbitrary radial reparameterizations.

---

## Log-Scale Variables

The first foundation note introduced temporal and radial log-scale variables:

$$
\psi=\frac12\ln A,
$$

and:

$$
\chi=\frac12\ln B.
$$

Equivalently:

$$
A=e^{2\psi},
$$

and:

$$
B=e^{2\chi}.
$$

In this notation, exterior reciprocal compensation:

$$
AB=1
$$

becomes:

$$
\psi+\chi=0.
$$

This motivates two reduced modes:

$$
\sigma=\psi+\chi,
$$

and:

$$
\eta=\psi-\chi.
$$

The uncompensated mode is \(\sigma\). The compensated exterior distortion mode is \(\eta\).

In this language, the static source-free exterior target is:

$$
\sigma=0,
\qquad
\eta\neq0.
$$

This gives a clean reduced interpretation of exterior compensation:

```text
The source-free static exterior suppresses the uncompensated temporal-radial mode,
while allowing a compensated distortion mode to remain.
```

---

## Translation to kappa and s

The later reduced exterior summaries use the equivalent notation:

$$
a=\ln A,
$$

and:

$$
b=\ln B.
$$

Then:

$$
\kappa=\frac{a+b}{2},
$$

and:

$$
s=\frac{a-b}{2}.
$$

Since:

$$
a=2\psi,
\qquad
b=2\chi,
$$

we have:

$$
\kappa=\psi+\chi=\sigma,
$$

and:

$$
s=\psi-\chi=\eta.
$$

Thus the two notations describe the same reduced mode split.

The inverse relations are:

$$
a=\kappa+s,
$$

and:

$$
b=\kappa-s.
$$

Therefore:

$$
A=e^{\kappa+s},
$$

and:

$$
B=e^{\kappa-s}.
$$

Multiplying gives the core identity:

$$
AB=e^{2\kappa}.
$$

So:

$$
\kappa=0
\quad\Longleftrightarrow\quad
AB=1.
$$

When \(\kappa=0\), the reduced exterior sector becomes:

$$
A=e^s,
$$

and:

$$
B=e^{-s}.
$$

The mode \(s\) can remain nonzero while reciprocal compensation is preserved.

---

## Parent-Mode Interpretation

The covariant-parent development note did not find a full covariant definition of \(\kappa\) and \(s\). It did establish a useful reduced interpretation.

In the two-component log-space vector:

$$
v=\begin{pmatrix}a\\b\end{pmatrix},
$$

the decomposition is:

$$
\begin{pmatrix}a\\b\end{pmatrix}
=
\kappa
\begin{pmatrix}1\\1\end{pmatrix}
+
s
\begin{pmatrix}1\\-1\end{pmatrix}.
$$

Thus:

```text
kappa follows the common-mode / trace-like direction.
s follows the opposing-mode / shear-like direction.
```

In the reduced linearized temporal-radial sector, \(\kappa\) behaves like half the relevant trace contribution, while pure \(s\) is trace-free to first order.

The working interpretation is therefore:

```text
kappa:
  reduced trace / conformal / determinant-like imbalance mode

s:
  reduced trace-free / compensated shear-like mode
```

In areal-radius gauge, \(\kappa\) also controls the temporal-radial determinant factor because:

$$
\sqrt{|g|}=e^\kappa r^2\sin\theta.
$$

This determinant statement is gauge-limited. It should not be interpreted as saying that \(\kappa\) is a full invariant spacetime volume scalar.

A useful foundation-level slogan is:

```text
Gravity is the compensated shear left after the source-free exterior suppresses imbalance.
```

The safer formal version is:

```text
In the static spherical reduced exterior, the source-free sector suppresses kappa,
and the remaining exterior distortion is carried by s.
```

---

## Gauge Status

The foundation files explicitly warn against treating \(\kappa\) and \(s\) as raw invariant fields.

Under a radial reparameterization:

$$
r=f(R),
$$

the radial metric coefficient picks up a Jacobian factor:

$$
B_{new}(R)=B(f(R))[f'(R)]^2.
$$

If one naively recomputes the temporal-radial log modes using only the new \(A_{new}\) and \(B_{new}\), then:

$$
\kappa\rightarrow\kappa+\ln f'(R),
$$

and:

$$
s\rightarrow s-\ln f'(R).
$$

This does not mean the physical geometry changed. It means the naive reduced variables were computed after leaving areal gauge while ignoring the angular sector.

The safe statement is:

```text
kappa and s are reduced variables defined after static spherical reduction and gauge control.
They are not general coordinate-invariant scalar fields by themselves.
```

---

## Areal-Gauge Repair

The areal radius is not an arbitrary coordinate. In spherical symmetry it is defined geometrically by sphere area:

$$
R=\sqrt{\frac{\text{Area}}{4\pi}}.
$$

For a general static spherical metric in an arbitrary radial coordinate \(X\):

$$
ds^2=-T(X)c^2dt^2+Q(X)dX^2+S(X)^2d\Omega^2,
$$

the areal radius is:

$$
R=S(X).
$$

Transforming to areal radius gives:

$$
A_{areal}=T(X),
$$

and:

$$
B_{areal}=\frac{Q(X)}{[S'(X)]^2}.
$$

Therefore the areal-gauge imbalance mode is:

$$
\kappa_{areal}
=
\frac12\ln\left(\frac{T(X)Q(X)}{[S'(X)]^2}\right).
$$

The areal-gauge compensation condition is:

$$
\kappa_{areal}=0,
$$

or:

$$
T(X)Q(X)=[S'(X)]^2.
$$

This is the arbitrary-radial-coordinate form of the areal-gauge condition \(AB=1\).

---

## Orbit-Space Reformulation

The orbit-space note gives the cleanest current geometric form.

A general spherically symmetric geometry can be written as:

$$
ds^2=h_{AB}(x)dx^A dx^B+R(x)^2d\Omega^2.
$$

Here:

```text
h_AB is the two-dimensional temporal-radial orbit-space metric.
R(x) is the areal-radius scalar.
```

The orbit-space norm of the areal-radius gradient is:

$$
|\nabla R|^2=h^{AB}\partial_A R\partial_B R.
$$

In the static diagonal sector:

$$
|\nabla R|^2=\frac{[S'(X)]^2}{Q(X)}.
$$

In areal gauge this becomes:

$$
|\nabla R|^2=\frac1B.
$$

Thus the reduced modes can be written as:

$$
\kappa=
\frac12\ln\left(\frac{A}{|\nabla R|^2}\right),
$$

and:

$$
s=
\frac12\ln\left(A|\nabla R|^2\right).
$$

The compensation condition is then:

$$
\kappa=0
\quad\Longleftrightarrow\quad
A=|\nabla R|^2.
$$

This is stronger and cleaner than saying only \(AB=1\). The expression \(AB=1\) is the areal-gauge version of the orbit-space condition.

This remains a spherical-reduction result. It does not make \(\kappa\) or \(s\) full spacetime scalar fields.

---

## Schwarzschild Check

For Schwarzschild exterior in areal coordinates:

$$
A=1-\frac{2GM}{rc^2},
$$

and:

$$
B=\frac1A.
$$

Therefore:

$$
AB=1,
$$

so:

$$
\kappa=0.
$$

Also, in areal gauge:

$$
|\nabla R|^2=\frac1B=A.
$$

Thus Schwarzschild satisfies:

$$
A=|\nabla R|^2.
$$

This is an important consistency check. It shows that the reduced compensation condition is aligned with the exact static spherical exterior relation in GR.

It does not, by itself, derive Schwarzschild, derive the field equation, or derive the mass-source law.

---

## Relationship to the Two Reduced Exterior Summaries

This foundation group sits between the earlier and later reduced exterior program summaries.

The earlier reduced exterior summary correctly used the log-scale split and the compensated sector:

$$
\kappa=0
\quad\Rightarrow\quad
A=e^s,
\qquad
B=e^{-s},
\qquad
AB=1.
$$

It also treated:

$$
\nabla^2s=\frac{8\pi G}{c^2}\rho
$$

as the candidate shear source law. In the foundation documents, this should be treated only as a weak-field target or toy source-law direction, not as an established foundation result.

The later v2 reduced exterior summary correctly incorporates the gauge and orbit-space improvement:

$$
\kappa=\frac12\ln\left(\frac{A}{|\nabla R|^2}\right),
\qquad
s=\frac12\ln\left(A|\nabla R|^2\right),
$$

with exterior compensation:

$$
A=|\nabla R|^2.
$$

The v2 summary also introduces the stronger exact static spherical candidate:

$$
\nabla^2A=\frac{8\pi G}{c^2}\rho,
\qquad
A=e^s.
$$

That exact source-law candidate is not established by the `01_foundations` Markdown files themselves. The foundation files point toward exact Schwarzschild recovery as a next target, especially after the orbit-space Schwarzschild check, but they do not yet derive or validate the exact \(A\)-law.

So the correct foundation-level position is:

```text
Established here:
  log-scale split, kappa/s interpretation, gauge limitation, areal repair,
  orbit-space compensation A=|∇R|², Schwarzschild consistency check.

Not established here:
  exact A-flux law, full source law, covariant action, full nonspherical theory.
```

---

## What This Foundation Group Establishes

The stable foundation results are:

1. The static spherical exterior metric can be rewritten in log-scale variables.

2. Exterior compensation becomes the vanishing of an uncompensated mode:

   $$
   \sigma=\psi+\chi=0.
   $$

3. In the later notation:

   $$
   \kappa=\sigma,
   \qquad
   s=\eta.
   $$

4. The core areal-gauge identity is:

   $$
   AB=e^{2\kappa}.
   $$

5. Therefore:

   $$
   \kappa=0
   \quad\Longleftrightarrow\quad
   AB=1.
   $$

6. The compensated sector has:

   $$
   A=e^s,
   \qquad
   B=e^{-s}.
   $$

7. \(\kappa\) is a reduced trace/conformal/determinant-like imbalance mode.

8. \(s\) is a reduced trace-free/shear-like compensated mode.

9. \(\kappa\) and \(s\) are gauge-sensitive if computed naively outside areal gauge.

10. The areal radius repairs the radial-coordinate ambiguity in spherical symmetry.

11. The orbit-space expression is:

    $$
    \kappa=\frac12\ln\left(\frac{A}{|\nabla R|^2}\right),
    $$

    and:

    $$
    s=\frac12\ln\left(A|\nabla R|^2\right).
    $$

12. The cleanest compensation condition is:

    $$
    A=|\nabla R|^2.
    $$

13. Schwarzschild exterior satisfies this condition exactly.

---

## What This Foundation Group Does Not Establish

This group does not establish a full field equation.

It does not derive P7 or P8 from a deeper covariant variational principle.

It does not derive the weak-field Laplace or Poisson equation for \(s\).

It does not derive the exact candidate law:

$$
\nabla^2A=\frac{8\pi G}{c^2}\rho.
$$

It does not derive the mass/interface flux condition.

It does not define \(\kappa\) and \(s\) as full spacetime covariant fields.

It does not generalize to nonspherical, rotating, time-dependent, cosmological, or radiative regimes.

It does not solve frame dragging or gravitational waves.

It does not produce the final configuration-energy action.

---

## Current Best Interpretation

The best current foundation-level interpretation is:

```text
The static spherical exterior admits a reduced mode split.

The imbalance mode kappa measures failure of temporal-radial compensation.
The compensated mode s carries the remaining static exterior distortion.

However, kappa and s are not standalone scalar gravitational fields.
They are gauge-aware spherical-reduction diagnostics built from the metric,
the areal-radius scalar, and the static temporal coefficient.
```

In the cleanest geometric form:

$$
\kappa=0
\quad\Longleftrightarrow\quad
A=|\nabla R|^2.
$$

In areal gauge this becomes:

$$
AB=1.
$$

The foundation group therefore justifies using \(\kappa\) and \(s\) as reduced diagnostic variables, while also warning against promoting them prematurely to fundamental scalar fields.

---

## Recommended Next Work

The natural next development target is not another raw areal-gauge identity. It is an action or field-equation candidate written in gauge-aware spherical-reduction variables.

Recommended next artifact:

```text
candidate_orbit_space_action.md
```

or:

```text
candidate_orbit_space_action.py
```

Purpose:

```text
Test whether a reduced exterior action can be written in terms of h_AB, R, A,
and |∇R|², with kappa and s appearing as derived spherical diagnostics rather
than independent scalar fields.
```

A second useful target is:

```text
candidate_static_spherical_exact_recovery.md
```

Purpose:

```text
Determine whether the orbit-space compensation condition A=|∇R|², together
with an appropriate source law, can recover the exact Schwarzschild exterior
rather than only the weak-field exterior.
```

The exact \(A=e^s\) source-law candidate should be developed there or in a later source-law group, not treated as already established by this foundation group.

---

## One-Paragraph Summary

The `01_foundations/` group establishes the reduced static spherical mode language for the exterior program. Starting from log-scale variables for the temporal and radial metric factors, it identifies an uncompensated mode \(\kappa\) and a compensated shear-like mode \(s\), with \(AB=e^{2\kappa}\) in areal gauge. The source-free exterior target is \(\kappa=0\), leaving \(s\) to carry the compensated distortion. The parent-mode study supports interpreting \(\kappa\) as a reduced trace/conformal/determinant-like imbalance and \(s\) as a reduced trace-free/shear-like mode. The gauge studies warn that these are not raw invariant scalar fields. The orbit-space reformulation gives the best current geometric expression: \(\kappa=\frac12\ln(A/|\nabla R|^2)\), \(s=\frac12\ln(A|\nabla R|^2)\), and exterior compensation \(A=|\nabla R|^2\), which reduces to \(AB=1\) in areal gauge and is satisfied by Schwarzschild exterior. The group does not yet derive a source law, exact \(A\)-flux equation, covariant action, or nonspherical theory.

---

## Status Snapshot

```text
Group role:
  foundation / reduced-variable geometry

Stable areal-gauge identity:
  AB = exp(2 kappa)

Stable areal-gauge compensation:
  kappa = 0 <=> AB = 1

Best geometric compensation:
  A = |∇R|²

Best interpretation of kappa:
  reduced trace / conformal / determinant-like imbalance diagnostic

Best interpretation of s:
  reduced compensated shear-like diagnostic

Main warning:
  kappa and s are not raw coordinate-invariant scalar fields

Schwarzschild status:
  exact exterior satisfies the compensation condition

Source-law status:
  not derived in this group

Exact A-law status:
  promising later candidate, not a foundation result

Best next target:
  candidate_orbit_space_action.md or candidate_static_spherical_exact_recovery.md
```
