# Interior / Exterior Matching Summary

## What This Summary Is

This document summarizes the `04_interior_matching/` development group.

This group connects the reduced exterior mechanics to finite matter sources, interior response, pressure/stress corrections, source-coupling normalization, and boundary/interface matching. It does not provide a full relativistic matter theory, a covariant action, or a derivation of Einstein's equations. It is a reduced static spherical matching program.

The central conclusion is:

```text
A-flux carries the exterior mass field.
Kappa may carry traceful interior matter response.
Pressure/stress likely belong to interior correction channels.
The boundary/interface fixes exterior A-flux and restores compensated exterior geometry.
```

In compact form:

```text
Interior:
  A is sourced by enclosed mass.
  kappa may be nonzero.
  pressure/stress may source kappa or boundary-smooth A corrections.

Boundary:
  matter fixes exterior A-flux.
  the boundary/source charge normalization is fixed by weak-field matching.
  kappa relaxes to zero.

Exterior:
  A-flux is conserved.
  kappa = 0.
  B = 1/A.
```

This group prevents an important overreach: the condition \(\kappa=0\) should not be imposed everywhere. It is safest as a relaxed source-free exterior condition.

---

## Files in This Group

```text
candidate_interior_A_source_model.md
candidate_compare_gr_interior_schwarzschild.md
candidate_gr_residual_as_kappa_response.md
candidate_interior_kappa_response.md
candidate_boundary_flux_action.md
candidate_source_coupling_normalization.md
candidate_pressure_stress_source_extension.md
candidate_boundary_kappa_relaxation_layer.md
candidate_interior_exterior_matching_strategy.md
```

The group should be read as an interior/exterior consistency and matching layer between the exact exterior mechanics branch and future pressure/stress source modeling.

---

## Exterior Branch Being Matched

The exterior branch inherited from the mechanics group is:

\[
\kappa=0,
\]

so:

\[
AB=1,
\]

and therefore:

\[
B=\frac1A.
\]

The exact static spherical source variable is:

\[
A=e^s.
\]

The exterior mass field is carried by the areal flux:

\[
F_A(r)=4\pi r^2A'(r).
\]

For total mass \(M\):

\[
F_A=\frac{8\pi GM}{c^2}.
\]

Thus:

\[
A(r)=1-\frac{2GM}{rc^2},
\]

and:

\[
B(r)=\frac1{1-2GM/(rc^2)}.
\]

This recovers the exact Schwarzschild exterior metric factors in areal gauge.

The interior-matching question is not whether this exterior branch works. The question is what kind of matter interior, pressure/stress correction, and boundary/interface behavior can feed it without incorrectly forcing exterior assumptions inside matter.

---

## Interior A-Flux Source Model

The finite-source extension uses the areal-flux law inside matter:

\[
F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).
\]

For a constant-density sphere of radius \(R\),

\[
M_{\rm enc}(r)=\frac{4\pi}{3}\rho_0r^3.
\]

Then:

\[
4\pi r^2 A'(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r),
\]

so:

\[
A'(r)=\frac{8\pi G\rho_0}{3c^2}r.
\]

Integrating and matching to the exterior gives:

\[
A_{\rm in}(r)
=
1-\frac{4\pi G\rho_0R^2}{c^2}
+
\frac{4\pi G\rho_0r^2}{3c^2}.
\]

This interior solution is regular at the origin, has \(A'(0)=0\), has zero flux at the center, and matches both \(A\) and \(A'\) to the exterior at \(r=R\).

It also reproduces the standard Newtonian weak-field interior potential, using:

\[
A\approx1+\frac{2\Phi}{c^2}.
\]

So the areal-flux law is not merely an exterior trick. It has a sensible reduced finite-source continuation.

However, this is not the full GR interior Schwarzschild solution. It includes density through enclosed mass, but not pressure, relativistic stress, nonlinear interior self-field structure, or a dynamical \(\kappa\)-source.

---

## Comparison with GR Interior Schwarzschild

The group compares the reduced constant-density interior \(A\)-model to the GR interior Schwarzschild solution.

Use dimensionless variables:

\[
x=\frac{r}{R},
\]

and:

\[
u=\frac{r_s}{R}=\frac{2GM}{c^2R}.
\]

The reduced interior lapse factor is:

\[
A_{\rm red}(x)=1-\frac{3u}{2}+\frac{ux^2}{2}.
\]

The GR interior Schwarzschild lapse factor is:

\[
A_{\rm GR}(x)
=
\frac14
\left(
3\sqrt{1-u}
-
\sqrt{1-ux^2}
\right)^2.
\]

At the surface:

\[
A_{\rm red}(1)=A_{\rm GR}(1)=1-u.
\]

Their derivatives also match at the boundary:

\[
A_{\rm red}'(1)=A_{\rm GR}'(1)=u.
\]

Their weak-field expansions agree through first order in compactness. The leading residual is second order:

\[
A_{\rm GR}-A_{\rm red}
=
\frac{3u^2}{16}(1-x^2)^2+O(u^3).
\]

This residual vanishes at the boundary and is largest at the center. That strongly suggests the missing structure is interior-supported: pressure, stress, relativistic self-field response, interior \(\kappa\), or boundary/interface corrections.

The most important structural difference is in the radial factor. If the reduced model forces \(\kappa=0\) inside matter, then:

\[
B_{\rm red}=\frac1{A_{\rm red}}.
\]

But the GR interior Schwarzschild radial factor is:

\[
B_{\rm GR}=\frac1{1-ux^2}.
\]

These are not generally equal. Equivalently, GR generally has:

\[
A_{\rm GR}B_{\rm GR}\neq1
\]

inside matter, even though:

\[
A_{\rm GR}B_{\rm GR}=1
\]

at the exterior boundary.

This supports the main refinement:

```text
kappa = 0 is an exterior/source-free condition, not an interior matter condition.
```

---

## Interior Kappa Response

The group defines the reduced diagnostic:

\[
\kappa=\frac12\ln(AB).
\]

For the GR interior Schwarzschild solution:

\[
\kappa_{\rm GR}
=
\frac12\ln(A_{\rm GR}B_{\rm GR}).
\]

This is generally nonzero inside matter, but returns to zero at the surface:

\[
\kappa_{\rm GR}(1)=0.
\]

The leading weak-field shape is:

\[
\kappa_{\rm GR}
=
-\frac{3u}{4}(1-x^2)+O(u^2).
\]

It is regular at the center, negative inside for positive compactness, and vanishes at the boundary.

A simple toy profile captures this leading behavior:

\[
\kappa_{\rm toy}
=
-\frac{3u}{4}(1-x^2).
\]

The lesson is not that the reduced theory must copy GR interiors exactly. The lesson is that a nonzero interior \(\kappa\)-diagnostic is natural and useful. Matter can carry traceful interior response while the source-free exterior remains compensated.

---

## Pressure / Stress Source Extension

The pressure/stress source-extension study asks whether pressure and stress should:

```text
source A-flux directly,
source interior kappa,
or appear as boundary-smooth second-order A corrections.
```

The current best answer is:

```text
Pressure/stress most likely belong to the interior problem,
not to the ordinary exterior mass-flux law.
```

For the GR constant-density interior, the pressure profile has leading weak-field form:

\[
\frac{p}{\rho c^2}
\approx
\frac{u}{4}(1-x^2).
\]

This begins at order \(u\) and vanishes at the boundary.

The GR lapse residual relative to the reduced \(A\)-model is:

\[
A_{\rm GR}-A_{\rm red}
=
\frac{3u^2}{16}(1-x^2)^2+O(u^3).
\]

If:

\[
P_{\rm lead}
=
\frac{u}{4}(1-x^2),
\]

then:

\[
3P_{\rm lead}^2
=
\frac{3u^2}{16}(1-x^2)^2.
\]

So the leading \(A\)-residual has a pressure/self-field-like shape. This does not prove pressure is the source, but it strongly suggests that the missing relativistic interior structure is boundary-contained and pressure/stress-like.

The study considers two source-channel hypotheses.

### Hypothesis 1: Pressure as Direct A-Flux Source

One possibility is:

\[
\Delta_{\rm areal}A
=
\frac{8\pi G}{c^2}
\left(
\rho+\chi\frac{p}{c^2}
\right).
\]

This would let pressure contribute directly to \(A\)-flux.

This is possible, but dangerous, because if pressure contributes directly to exterior flux then the theory must explain how that relates to observed gravitational mass and exterior Schwarzschild normalization.

### Hypothesis 2: Pressure / Stress as Kappa Source

A cleaner current hypothesis is that pressure and stress source interior \(\kappa\). A toy trace-like source is:

\[
J_\kappa=a\rho c^2+bp.
\]

With local energy:

\[
E=C_\kappa\kappa^2-J_\kappa\kappa,
\]

stationarity gives:

\[
\kappa_{\rm eq}
=
\frac{a\rho c^2+bp}{2C_\kappa}.
\]

If the source vanishes or is suppressed outside matter, exterior \(\kappa\) relaxes to zero.

This fits the interior/exterior split:

```text
density / total mass fixes exterior A-flux;
pressure / stress may source interior kappa;
source-free exterior suppresses kappa and conserves A-flux.
```

The boundary behavior also supports this. The leading pressure shape, leading \(\kappa\) shape, and leading \(A\)-residual all vanish at \(x=1\), while the \(A\)-residual has vanishing derivative at the boundary. This lets pressure/stress corrections remain interior-contained.

---

## General Interior Kappa Models

The interior \(\kappa\)-response study tested whether nonzero interior \(\kappa\) is compatible with exact exterior compensation.

The simplest traceful interior profile is:

\[
\kappa_{\rm in}
=
\frac{G\eta\rho_0}{c^2}(R^2-r^2).
\]

This is regular at the center and satisfies:

\[
\kappa_{\rm in}(R)=0.
\]

However, its boundary derivative is generally nonzero, so an interface layer or boundary condition may be needed.

A smoother profile is:

\[
\kappa_{\rm in}
=
\frac{G\eta\rho_0}{c^2R^2}(R^2-r^2)^2.
\]

This satisfies:

\[
\kappa_{\rm in}(R)=0,
\]

and:

\[
\kappa_{\rm in}'(R)=0.
\]

It is regular at the center and can match cleanly to:

\[
\kappa_{\rm ext}=0.
\]

The cleanest toy class is therefore:

```text
kappa nonzero inside,
kappa(R)=0,
kappa'(R)=0,
kappa=0 outside.
```

This permits interior trace response without exterior \(\kappa\)-leak.

---

## Boundary Flux Action

The boundary-flux action study asks whether the areal flux law can arise as a boundary/interface condition.

The reduced radial bulk action is:

\[
L_{\rm bulk}=K_A r^2(A')^2.
\]

Its Euler-Lagrange equation gives:

\[
\frac{d}{dr}(r^2A')=0.
\]

This is the source-free areal-flux equation.

The variation produces the boundary term:

\[
2K_A r^2A'\delta A.
\]

Thus \(r^2A'\) is the boundary momentum conjugate to \(A\). Since:

\[
F_A=4\pi r^2A',
\]

the same object is the flux carrier.

A boundary/source coupling:

\[
E_{\rm boundary}=-qA(R)
\]

gives the stationarity condition:

\[
2K_A R^2A'(R)=q.
\]

Then:

\[
F_A=4\pi R^2A'(R)=\frac{2\pi q}{K_A}.
\]

This gives a reduced mechanism:

```text
matter fixes the boundary momentum r²A';
that boundary momentum is the areal flux of A;
the exterior carries conserved A-flux.
```

The boundary action does not yet derive the source coupling from deeper principles, but it identifies the quantity the source must fix.

---

## Source Coupling Normalization

The source-coupling normalization study asks whether the boundary/source charge \(q\) is arbitrary.

At the reduced matching level, it is not arbitrary.

For conserved exterior flux:

\[
4\pi r^2A'=F,
\]

asymptotic flatness gives:

\[
A(r)=1-\frac{F}{4\pi r}.
\]

Weak-field Newtonian matching requires:

\[
A(r)=1+\frac{2\Phi}{c^2}
=
1-\frac{2GM}{c^2r}.
\]

Therefore:

\[
F=\frac{8\pi GM}{c^2}.
\]

But the boundary action gives:

\[
F_A=\frac{2\pi q}{K_A}.
\]

Matching these gives:

\[
q_M=\frac{4K_AGM}{c^2}.
\]

The same flux normalization gives the Schwarzschild radius coefficient:

\[
F_A=4\pi r_s=\frac{8\pi GM}{c^2},
\]

so:

\[
r_s=\frac{2GM}{c^2}.
\]

The boundary/source charge is also additive in mass:

\[
q(M_1+M_2)=q(M_1)+q(M_2).
\]

Thus:

```text
matched normalization: achieved;
first-principles derivation: still open.
```

The reduced model fixes the coefficient required for Newtonian and Schwarzschild matching. It does not yet explain why matter couples through:

\[
E_{\rm boundary}=-qA(R)
\]

or why the reduced stiffness \(K_A\) has its deeper value.

---

## Boundary Kappa Relaxation

The boundary \(\kappa\)-relaxation study asks whether interior \(\kappa\) can vanish before entering the ordinary exterior weak-field region.

A sharp cutoff,

```text
kappa = k0 inside,
kappa = 0 outside,
```

enforces exterior compensation but requires interface stress or a resolved transition.

A smooth interior profile,

\[
\kappa_{\rm in}(r)=k_0\left(1-\frac{r^2}{R^2}\right)^2,
\]

satisfies:

\[
\kappa(R)=0,
\]

\[
\kappa'(R)=0,
\]

and:

\[
\kappa'(0)=0.
\]

This is the cleanest reduced profile class.

The study also considers exterior exponential or massive relaxation tails. These can suppress \(\kappa\) asymptotically, but they create an exterior \(\kappa\)-leak channel. That is observationally dangerous because a weak exterior leak of the form:

\[
\kappa_{\rm ext}=\lambda_\kappa\epsilon,
\qquad
s_{\rm ext}=-2\epsilon,
\]

changes the weak-field coefficients:

\[
A\approx1+(\lambda_\kappa-2)\epsilon,
\]

\[
B\approx1+(\lambda_\kappa+2)\epsilon,
\]

and:

\[
AB\approx1+2\lambda_\kappa\epsilon.
\]

Therefore viable ordinary exteriors should strongly suppress \(\kappa\)-leak.

---

## Current Matching Strategy

The best reduced matching strategy is:

### Interior

Inside matter:

\[
F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).
\]

The \(A\)-field tracks enclosed mass and reproduces the Newtonian interior potential at weak field.

Meanwhile:

\[
\kappa_{\rm in}(r)\neq0
\]

may be allowed, because matter can carry traceful response.

Pressure, stress, relativistic self-energy, and interior self-field corrections likely enter through:

```text
interior kappa,
boundary-smooth A residuals,
or both.
```

### Boundary

At the matter boundary:

\[
F_A(R)=\frac{8\pi GM}{c^2}.
\]

A reduced boundary/source action can impose this by fixing:

\[
2K_A R^2A'(R)=q_M,
\]

with:

\[
q_M=\frac{4K_AGM}{c^2}.
\]

The preferred \(\kappa\) matching conditions are:

\[
\kappa(R)=0,
\]

and ideally:

\[
\kappa'(R)=0.
\]

These prevent exterior \(\kappa\)-leak.

### Exterior

Outside matter:

\[
F_A=\frac{8\pi GM}{c^2},
\]

so:

\[
A=1-\frac{2GM}{rc^2}.
\]

The source-free exterior suppresses:

\[
\kappa=0.
\]

Therefore:

\[
B=\frac1A.
\]

This gives the exact Schwarzschild exterior metric factors in areal gauge.

---

## Why This Group Matters

This group corrects three possible mistakes.

### Mistake 1: Forcing Kappa Zero Everywhere

The exact exterior uses \(\kappa=0\), but the interior need not. GR itself has an effective nonzero interior \(\kappa\)-diagnostic for the constant-density solution while restoring \(AB=1\) at the surface.

Thus:

```text
Do not force kappa=0 inside matter.
```

The safer statement is:

```text
The source-free exterior relaxes to kappa=0.
```

### Mistake 2: Treating A-Flux as a Complete Interior Matter Theory

The areal-flux law works well for density/enclosed mass and weak-field interior behavior, but it does not include pressure or relativistic stress. It matches the exterior and first-order interior behavior, but not the full GR interior Schwarzschild solution.

Thus:

```text
A-flux is the mass/enclosed-flux channel.
Interior relativistic structure likely requires kappa and stress/pressure terms.
```

### Mistake 3: Treating Boundary Coupling Normalization as Arbitrary

The boundary/source charge is not free once Newtonian and Schwarzschild matching are required.

The required reduced normalization is:

\[
q_M=\frac{4K_AGM}{c^2}.
\]

But this is a matching result, not yet a first-principles derivation.

---

## Current Best Statement

The safest current statement is:

```text
In the reduced static spherical model, A-flux gives a sensible finite-source
mass channel and matches smoothly to the exact exterior Schwarzschild A factor.
However, matter interiors should not be forced into kappa=0. Interior matter
may source traceful kappa response, while pressure/stress likely produce
interior-contained corrections. The boundary/interface fixes exterior A-flux
with a normalization fixed by weak-field matching, while relaxing kappa to
zero so the source-free exterior remains compensated, with B=1/A.
```

In slogan form:

```text
Exterior gravity is compensated A-flux.
Interior matter may carry traceful kappa response.
Pressure/stress are interior correction channels.
The boundary turns matter content into exterior flux and restores compensation.
```

---

## Open Questions

1. What physical matter quantity sources interior \(\kappa\)?

Candidates include density trace, pressure, stress, relativistic self-energy, or boundary/interface stress.

2. How do pressure and relativistic stress enter?

They may modify \(A\)-flux, source \(\kappa\), produce boundary-smooth \(A\)-residuals, or some combination.

3. What principle enforces \(\kappa(R)=0\) and possibly \(\kappa'(R)=0\)?

This is currently a matching strategy, not a derived law.

4. Why does the boundary source coupling have the form:

\[
E_{\rm boundary}=-qA(R)?
\]

5. Why does the matched boundary charge use:

\[
q_M=\frac{4K_AGM}{c^2}?
\]

The coefficient is fixed by weak-field matching, but the source action is not yet derived.

6. What is the physical meaning or deeper normalization of \(K_A\)?

7. What covariant or geometric parent reduces to this interior/exterior structure?

8. How does this generalize to nonspherical, rotating, time-dependent, or strong-field matter?

---

## Recommended Next Work

The next natural group should focus on pressure/stress source terms and boundary-source derivation.

Possible artifacts:

```text
candidate_pressure_kappa_source_model.py
candidate_A_residual_source_reconstruction.py
candidate_pressure_boundary_matching.py
candidate_boundary_source_coupling_origin.md
candidate_A_stiffness_normalization.py
candidate_boundary_kappa_action.py
candidate_interior_exterior_master_summary.md
```

The most important near-term tasks are:

```text
decompose the GR interior residual into pressure/stress/kappa source terms;
derive or motivate the boundary coupling E_boundary = -qA(R);
determine whether pressure/stress modifies A-flux, kappa, or both.
```

---

## One-Paragraph Summary

The `04_interior_matching/` group shows how the exact compensated exterior branch can coexist with finite matter interiors. The areal-flux law gives a regular constant-density interior \(A(r)\), continuous \(A\), continuous \(A'\), continuous flux, the Newtonian interior potential, and the exact exterior Schwarzschild coefficient. But comparison with the GR interior Schwarzschild solution shows that the reduced \(A\)-only interior is incomplete beyond first order and that \(AB=1\) should not be forced inside matter. GR itself has an effective nonzero interior \(\kappa=\frac12\ln(AB)\) that vanishes at the boundary. Pressure/stress analysis suggests the missing interior structure is boundary-contained and pressure/self-field-like, while source-coupling normalization fixes the reduced boundary charge \(q_M=4K_AGM/c^2\) by Newtonian and Schwarzschild matching. The current best strategy is therefore: \(A\)-flux carries mass/enclosed-source information, interior matter may source traceful \(\kappa\), pressure/stress provide interior corrections, and the boundary/interface fixes exterior \(A\)-flux while relaxing \(\kappa\) to zero so the source-free exterior remains compensated.
