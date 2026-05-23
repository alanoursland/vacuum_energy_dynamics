# Mechanics Summary

## What This Document Is

This document summarizes the `02_mechanics/` development group.

It is a development summary. It is not a postulate, theorem, proof, full covariant action, or complete field equation.

The role of this group is to connect the foundation-level reduced exterior variables to concrete source-law and variational candidates. The main development arc is:

```text
weak shear source law
  -> reduced exterior action
  -> exact static spherical recovery using A = exp(s)
  -> reduced A-action
  -> geometry/operator check
  -> areal-flux interpretation
```

The current safest conclusion is:

```text
In the reduced static spherical areal-gauge sector, exterior compensation sets kappa = 0, so B = 1/A. If the exact source variable A = exp(s) obeys a mass-sourced areal-flux law, then the exterior solution recovers the exact Schwarzschild metric factors in areal gauge.
```

The main caveat is:

```text
The successful source operator is not yet a standard covariant geometric Laplacian. It is currently best understood as a reduced areal-flux / flat-radial operator.
```

---

## Directory Scope

This group contains the mechanics-level studies that follow from the `01_foundations/` mode definitions and gauge/orbit-space clarifications.

The relevant files are:

```text
candidate_exterior_shear_source_law.md
candidate_reduced_exterior_action.md
candidate_static_spherical_exact_recovery.md
candidate_orbit_space_action.md
candidate_exact_source_law_geometry_check.md
candidate_areal_flux_principle.md
mechanics_status_summary.md
```

These files should be read as one development sequence rather than as independent final claims.

---

## Foundation Imported from 01_foundations

The mechanics group assumes the reduced static spherical metric in areal gauge:

$$ds^2=-A(r)c^2dt^2+B(r)dr^2+r^2d\Omega^2.$$

Define:

$$a=\ln A,$$

and:

$$b=\ln B.$$

The reduced modes are:

$$\kappa=\frac{a+b}{2},$$

and:

$$s=\frac{a-b}{2}.$$

Equivalently:

$$a=\kappa+s,$$

and:

$$b=\kappa-s.$$

Therefore:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Multiplying gives:

$$AB=e^{2\kappa}.$$

So:

$$\kappa=0\quad\Longleftrightarrow\quad AB=1.$$

The compensated exterior sector is:

$$\kappa=0,$$

with:

$$s\neq0.$$

Then:

$$A=e^s,$$

and:

$$B=e^{-s}=\frac1A.$$

The mechanics group asks what source law or action determines the remaining compensated mode.

---

## Stage 1: Weak Exterior Shear Source Law

The first mechanics candidate treated the compensated shear mode itself as the sourced variable.

The candidate weak source law was:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

In source-free exterior:

$$\nabla^2s=0.$$

In spherical symmetry:

$$\nabla^2s=\frac1{r^2}\frac{d}{dr}\left(r^2\frac{ds}{dr}\right).$$

The exterior solution is:

$$s(r)=C_0+\frac{C_1}{r}.$$

Asymptotic flatness sets:

$$C_0=0.$$

The candidate mass/interface flux condition was:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}.$$

For:

$$s(r)=\frac{C_1}{r},$$

this fixes:

$$C_1=-\frac{2GM}{c^2}.$$

Thus:

$$s(r)=-\frac{2GM}{rc^2}.$$

With:

$$\kappa=0,$$

we get:

$$A=e^s=e^{-2GM/(rc^2)},$$

and:

$$B=e^{-s}=e^{2GM/(rc^2)}.$$

To first order:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

So the weak shear source law recovers the correct first-order exterior metric structure.

Current interpretation:

```text
The direct s-source law is the weak-field linearized mechanics.
```

It is no longer the best exact static spherical law.

---

## Stage 2: Reduced Exterior Action

The next mechanics step asked whether kappa suppression and the weak shear source law could come from one reduced variational toy.

The candidate action density was:

$$L=
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
+
\alpha\rho s.$$

Varying with respect to \(\kappa\) gives:

$$-2K_\kappa\nabla^2\kappa+2M_\kappa^2\kappa=0.$$

In a source-free exterior with suitable boundary data, the relaxed solution is:

$$\kappa=0.$$

This gives:

$$AB=1.$$

Varying with respect to \(s\) gives:

$$-2K_s\nabla^2s+\alpha\rho=0,$$

or:

$$\nabla^2s=\frac{\alpha}{2K_s}\rho.$$

To match the weak shear source law, choose:

$$\alpha=\frac{16\pi G K_s}{c^2}.$$

Then:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

This action therefore unifies, at the reduced weak-field level:

```text
kappa suppression
+
linear shear sourcing
```

Current interpretation:

```text
This is a useful weak-field reduced action, but it is superseded in the exact static spherical branch by an action/source law in A = exp(s).
```

---

## Stage 3: Exact Static Spherical Recovery

The exact recovery study found that the weak shear profile:

$$s_{\rm weak}=-\frac{r_s}{r},$$

where:

$$r_s=\frac{2GM}{c^2},$$

only gives:

$$A=e^{-r_s/r}.$$

This agrees with Schwarzschild only at first order.

Exact Schwarzschild in areal gauge has:

$$A=1-\frac{r_s}{r},$$

and:

$$B=\frac1{1-r_s/r}.$$

Since:

$$AB=1,$$

this lies in the compensated sector:

$$\kappa=0.$$

The exact shear is therefore:

$$s_{\rm exact}=\ln A=\ln\left(1-\frac{r_s}{r}\right).$$

This implies:

$$A=e^s$$

is the cleaner exact variable.

The exact source-free candidate is:

$$\nabla^2A=0,$$

or:

$$\nabla^2e^s=0.$$

Using:

$$\nabla^2e^s=e^s(\nabla^2s+|\nabla s|^2),$$

this becomes:

$$\nabla^2s+|\nabla s|^2=0.$$

In weak field, the nonlinear term is second order, so:

$$\nabla^2s\approx0.$$

Thus the earlier shear law is the linearized limit of the exact candidate.

The exact source law becomes:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho,$$

or:

$$\nabla^2e^s=\frac{8\pi G}{c^2}\rho.$$

For the exterior solution:

$$A=1-\frac{r_s}{r},$$

we have:

$$A'=\frac{r_s}{r^2}.$$

The flux is:

$$4\pi r^2A'=4\pi r_s.$$

Setting:

$$4\pi r_s=\frac{8\pi GM}{c^2}$$

gives:

$$r_s=\frac{2GM}{c^2}.$$

So the exact candidate recovers:

$$A=1-\frac{2GM}{rc^2},$$

and, with \(\kappa=0\):

$$B=\frac1A=\frac1{1-2GM/(rc^2)}.$$

This is the strongest positive result of the mechanics group.

---

## Stage 4: Exact Reduced A-Action

The exact recovery motivates replacing the weak action in \(s\) with an action in:

$$A=e^s.$$

The reduced exact candidate action is:

$$E_A=\int\left[K_A|\nabla A|^2+\beta\rho A\right]d^3x.$$

Variation gives:

$$\nabla^2A=\frac{\beta}{2K_A}\rho.$$

To match:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho,$$

choose:

$$\beta=\frac{16\pi G K_A}{c^2}.$$

Under:

$$A=e^s,$$

this becomes the nonlinear \(s\)-action:

$$E_s^{\rm exact}=\int\left[K_Ae^{2s}|\nabla s|^2+\beta\rho e^s\right]d^3x.$$

The exact action can be combined with kappa suppression:

$$E=\int
\left[
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_A|\nabla A|^2
+
\beta\rho A
\right]d^3x.$$

The intended reduced structure is:

```text
kappa is suppressed;
A = exp(s) is sourced;
when kappa = 0, B = 1/A.
```

This gives exact static spherical metric recovery in areal gauge.

Current caveat:

```text
This is still a reduced action. Its operator and measure are not yet derived from a full covariant geometry.
```

---

## Stage 5: Geometry Check of the Source Operator

The exact source-law geometry check asked what the symbol \(\nabla^2\) actually means in the successful exact law.

For Schwarzschild exterior:

$$A=1-\frac{r_s}{r},$$

and:

$$B=\frac1A.$$

The flat areal radial operator is:

$$\Delta_{\rm areal}A=\frac1{r^2}\frac{d}{dr}\left(r^2A'\right).$$

For Schwarzschild:

$$r^2A'=r_s,$$

so:

$$\Delta_{\rm areal}A=0.$$

Equivalently, the areal flux:

$$F_A=4\pi r^2A'$$

is conserved outside the source.

However, the study also checked the ordinary curved spatial Laplacian of the spatial metric:

$$dl^2=B(r)dr^2+r^2d\Omega^2.$$

For Schwarzschild \(A\), this does not vanish. The curved spatial Laplacian gives a nonzero result.

The study also checked the scalar operator of the two-dimensional orbit-space metric:

$$h_{AB}dx^A dx^B=-A(r)c^2dt^2+B(r)dr^2.$$

That operator also does not make \(A\) harmonic.

Therefore the exact recovery is not based on:

```text
ordinary curved-space scalar harmonicity of A.
```

The successful operator is specifically:

```text
areal-flux / flat-radial reduced operator.
```

This is the main precision correction of the mechanics group.

---

## Stage 6: Areal-Flux Principle

The areal-flux principle rewrites the exact source law in the safest current form.

Define:

$$F_A(r)=4\pi r^2A'(r).$$

The candidate flux law is:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

Equivalently:

$$\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho,$$

where:

$$\Delta_{\rm areal}A=\frac1{r^2}\frac{d}{dr}(r^2A').$$

Outside the source:

$$M_{\rm enc}(r)=M,$$

so:

$$F_A(r)=\frac{8\pi GM}{c^2}.$$

Then:

$$4\pi r^2A'=\frac{8\pi GM}{c^2},$$

so:

$$A'=\frac{2GM}{c^2r^2}.$$

Integrating gives:

$$A(r)=C_0-\frac{2GM}{c^2r}.$$

Asymptotic flatness sets:

$$C_0=1.$$

Thus:

$$A(r)=1-\frac{2GM}{rc^2}.$$

With:

$$\kappa=0,$$

we get:

$$B=\frac1A=\frac1{1-2GM/(rc^2)}.$$

This recovers exact Schwarzschild exterior metric factors in areal gauge.

The areal-flux phrasing also supports shell and boundary interpretations:

```text
mass changes the areal flux of A across the source/interface.
```

This is currently safer than saying that \(A\) is a standard curved-space harmonic scalar.

---

## Current Mechanics Claim

The strongest safe mechanics claim is:

```text
In the reduced static spherical areal-gauge sector, exterior compensation suppresses kappa, giving B = 1/A. The exact static spherical source variable is A = exp(s), not s itself. If mass sources the areal flux F_A = 4pi r^2 A', then the exterior solution is A = 1 - 2GM/(rc^2), and compensation gives B = 1/A. This recovers the exact Schwarzschild exterior metric factors in areal gauge.
```

In equations:

$$\kappa=0,$$

$$A=e^s,$$

$$B=e^{-s}=\frac1A,$$

$$F_A=4\pi r^2A',$$

$$F_A=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

For exterior vacuum:

$$F_A=\frac{8\pi GM}{c^2}.$$

Therefore:

$$A=1-\frac{2GM}{rc^2},$$

and:

$$B=\frac1{1-2GM/(rc^2)}.$$

---

## Current Interpretation of Each File

### `candidate_exterior_shear_source_law.md`

This is the linearized weak-field mechanics note.

It establishes that:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho$$

gives:

$$s=-\frac{2GM}{rc^2},$$

and therefore recovers the first-order exterior metric factors when \(\kappa=0\).

Current status:

```text
valid as weak-field linearization;
not exact static spherical mechanics.
```

### `candidate_reduced_exterior_action.md`

This is the weak-field reduced action note.

It unifies:

```text
kappa suppression
+
linear s-source law
```

using:

$$K_\kappa|\nabla\kappa|^2+M_\kappa^2\kappa^2+K_s|\nabla s|^2+\alpha\rho s.$$

Current status:

```text
valid as weak-field reduced action toy;
superseded by A-action in exact static spherical branch.
```

### `candidate_static_spherical_exact_recovery.md`

This is the strongest exact recovery result.

It shows that exact Schwarzschild recovery requires:

$$A=e^s,$$

with:

$$A=1-\frac{r_s}{r},$$

and:

$$s=\ln\left(1-\frac{r_s}{r}\right).$$

Current status:

```text
strongest positive mechanics result;
exact in reduced static spherical areal gauge.
```

### `candidate_orbit_space_action.md`

This is the exact reduced action candidate.

It shows that:

$$E_A=\int[K_A|\nabla A|^2+\beta\rho A]d^3x$$

with:

$$\beta=\frac{16\pi G K_A}{c^2}$$

produces:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

Current status:

```text
successful reduced A-action toy;
not yet a covariant/geometric action.
```

### `candidate_exact_source_law_geometry_check.md`

This is the operator caution note.

It shows that the successful exact source operator is not the curved spatial Laplacian and not the orbit-space scalar operator.

Current status:

```text
main caveat / open wound;
forces the areal-flux interpretation.
```

### `candidate_areal_flux_principle.md`

This is the safest current formulation of the exact mechanics law.

It states:

$$F_A(r)=4\pi r^2A'(r),$$

and:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

Current status:

```text
best current mechanics statement.
```

### `mechanics_status_summary.md`

This is an organizational status summary of the branch.

It correctly classifies the weak \(s\)-law and weak action as linearized, and identifies the exact branch as an \(A=e^s\) areal-flux branch.

Current status:

```text
already close to the correct group-level summary;
this document expands it into a consolidated mechanics summary.
```

---

## What This Group Establishes

This group establishes the following reduced results:

1. The direct shear source law works as a weak-field linearized law.
2. A reduced action can unify kappa suppression with linear shear sourcing.
3. Exact Schwarzschild recovery requires the source variable \(A=e^s\), not \(s\).
4. The exact shear is:
   $$s=\ln(1-r_s/r).$$
5. The exact source-free equation in \(s\) is nonlinear:
   $$\Delta_{\rm areal}s+|\nabla s|^2=0.$$
6. The exact source law can be represented as:
   $$\Delta_{\rm areal}A=8\pi G\rho/c^2.$$
7. The corresponding flux law is:
   $$F_A=4\pi r^2A'=8\pi GM_{\rm enc}/c^2.$$
8. Exterior flux conservation gives:
   $$A=1-2GM/(rc^2).$$
9. Kappa compensation gives:
   $$B=1/A.$$
10. Together these recover exact Schwarzschild exterior metric factors in areal gauge.
11. The successful source operator is areal-flux / flat-radial, not a standard curved spatial scalar Laplacian.

---

## What This Group Does Not Establish

This group does not establish a full covariant field equation.

It does not derive the areal-flux law from deeper postulates.

It does not prove that the flat areal radial operator is fundamental.

It does not explain why mass sources the areal flux of \(A=e^s\).

It does not derive the source/interface coupling from vacuum burden, mass-as-constraint, or configuration energy.

It does not handle pressure, stress, or relativistic sources.

It does not generalize to nonspherical geometries.

It does not handle rotation, frame dragging, gravitational waves, or time dependence.

It does not prove that the reduced A-action is the true action.

It only establishes a strong reduced static spherical mechanics candidate.

---

## Main Open Questions

### 1. What is the geometric parent of the areal-flux law?

The core open problem is:

```text
Why should the exact static spherical source law use the areal-flux operator rather than the curved spatial scalar Laplacian?
```

### 2. What action produces the areal-flux operator geometrically?

The reduced A-action works formally, but its gradient and measure behave like flat areal-coordinate objects.

Open question:

```text
Can a deeper geometric or constrained variational principle reduce to this areal-flux action?
```

### 3. Why does mass source A-flux?

The current law says:

$$F_A=\frac{8\pi G}{c^2}M_{\rm enc}.$$

Open question:

```text
What source/interface principle makes mass control the areal flux of A = exp(s)?
```

### 4. How do interiors work?

The exterior recovery is strong, but interiors remain unresolved.

Open question:

```text
What interior density, pressure, and boundary conditions produce the exterior A-flux law consistently?
```

### 5. What survives beyond spherical symmetry?

The mechanics branch is static and spherical.

Open question:

```text
How does the scalar A-flux law generalize to weak nonspherical multipoles, and where must additional vector/tensor sectors enter?
```

---

## Recommended Next Work

The next work should focus on the origin of the areal-flux operator.

Likely next targets:

```text
candidate_areal_flux_variational_origin.md
candidate_mass_interface_flux_source.md
candidate_interior_areal_flux_matching.md
candidate_operator_parent_comparison.md
candidate_reduced_bianchi_or_constraint_origin.md
```

The key guardrail is:

```text
Do not call the exact source law an ordinary curved-space scalar Laplacian.
```

The right current language is:

```text
mass-sourced areal flux of A = exp(s).
```

---

## One-Paragraph Current Summary

The `02_mechanics/` group develops the reduced static spherical source mechanics built on the foundation modes \(\kappa\) and \(s\). The first weak candidate sourced the shear mode directly through \(\nabla^2s=8\pi G\rho/c^2\), producing \(s=-2GM/(rc^2)\) and the correct first-order metric factors when \(\kappa=0\). A reduced action then unified \(\kappa\)-suppression with this linear shear law. The exact recovery studies refined the picture: the exact static spherical source variable is not \(s\) but \(A=e^s\). The exact branch uses an areal-flux law \(F_A=4\pi r^2A'=8\pi GM_{\rm enc}/c^2\), giving \(A=1-2GM/(rc^2)\), and compensation gives \(B=1/A\). This recovers exact Schwarzschild exterior metric factors in areal gauge. The main unresolved issue is that the successful operator is an areal-flux / flat-radial reduced operator, not yet a covariant geometric Laplacian or full field equation.

---

## Status Snapshot

```text
Best weak-field variable:
  s

Weak-field law:
  ∇²s = 8πGρ/c²

Best exact static spherical variable:
  A = exp(s)

Best exact mechanics law:
  F_A = 4πr²A' = 8πG M_enc / c²

Equivalent reduced operator:
  Δ_areal A = (1/r²)(r²A')' = 8πGρ/c²

Exterior compensation:
  kappa = 0

Metric consequence:
  B = 1/A

Exact exterior result:
  A = 1 - 2GM/(rc²)
  B = 1 / [1 - 2GM/(rc²)]

Main success:
  exact Schwarzschild exterior metric factors in areal gauge

Main caveat:
  areal-flux operator not yet derived from a covariant/geometric parent

Best current slogan:
  Mass sources the areal flux of A = exp(s).
```
