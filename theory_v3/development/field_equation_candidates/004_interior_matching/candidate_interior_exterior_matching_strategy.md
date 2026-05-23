# Candidate Interior / Exterior Matching Strategy

## What This Document Is

This document is a synthesis note.

It summarizes the current best strategy for connecting interior matter, boundary/interface physics, and the exact compensated exterior branch.

It is not a postulate, theorem, proof, or field equation.

It is based on the current candidate studies:

```text
candidate_interior_A_source_model.md
candidate_boundary_flux_action.md
candidate_interior_kappa_response.md
candidate_compare_gr_interior_schwarzschild.md
candidate_gr_residual_as_kappa_response.md
candidate_boundary_kappa_relaxation_layer.md
```

The central conclusion is:

```text
A-flux carries the exterior mass field.
Kappa may carry traceful interior response.
The boundary/interface restores compensated exterior geometry.
```

---

## Current Exterior Branch

The source-free exterior branch is the strongest current result.

It uses:

$$\kappa=0,$$

so:

$$AB=1.$$

Thus:

$$B=\frac1A.$$

The exact source variable is:

$$A=e^s.$$

The exterior mass field is carried by areal flux:

$$F_A(r)=4\pi r^2A'(r).$$

For total mass \(M\):

$$F_A=\frac{8\pi GM}{c^2}.$$

Therefore:

$$A=1-\frac{2GM}{rc^2}.$$

Then:

$$B=\frac1{1-2GM/(rc^2)}.$$

This recovers exact Schwarzschild exterior metric factors in areal gauge.

Current exterior statement:

```text
source-free exterior suppresses kappa;
mass fixes A-flux;
compensation gives B=1/A.
```

---

## Current Interior A-Flux Picture

The areal-flux law inside a finite source is:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

For constant density:

$$M_{\rm enc}(r)=\frac{4\pi}{3}\rho_0r^3.$$

This gives:

$$A_{\rm in}(r)
=
1-\frac{4\pi G\rho_0R^2}{c^2}
+
\frac{4\pi G\rho_0r^2}{3c^2}.
$$

This interior \(A\) is regular, matches \(A\) and \(A'\) to the exterior, and reproduces the weak-field Newtonian interior potential.

But it is not the full GR interior Schwarzschild solution.

This means:

```text
A-flux alone captures mass sourcing and weak-field interior behavior,
but not complete relativistic interior structure.
```

---

## Current Interior Kappa Picture

The evidence now suggests that forcing:

$$\kappa=0$$

inside matter is too restrictive.

The GR interior Schwarzschild diagnostic has:

$$A_{\rm GR}B_{\rm GR}\neq1$$

inside matter.

Thus:

$$\kappa_{\rm GR}=\frac12\ln(A_{\rm GR}B_{\rm GR})\neq0$$

inside matter.

But at the exterior boundary:

$$A_{\rm GR}B_{\rm GR}=1,$$

so:

$$\kappa_{\rm GR}=0.$$

The leading weak-field diagnostic shape is:

$$\kappa_{\rm GR}
=
-\frac{3u}{4}(1-x^2)+O(u^2),
$$

where:

$$x=\frac{r}{R},\qquad u=\frac{r_s}{R}.$$

This supports:

```text
kappa=0 should be treated as an exterior/source-free condition,
not an everywhere-inside-matter condition.
```

---

## Boundary / Interface Role

The boundary-flux action study showed that the reduced radial action:

$$L_{\rm bulk}=K_A r^2(A')^2$$

has a boundary variation:

$$2K_A r^2A'\delta A.$$

Thus:

$$r^2A'$$

is the boundary momentum conjugate to \(A\).

A boundary/source coupling:

$$E_{\rm boundary}=-qA(R)$$

fixes:

$$2K_AR^2A'(R)=q.$$

With:

$$q_M=\frac{4K_AGM}{c^2},$$

this gives:

$$4\pi R^2A'(R)=\frac{8\pi GM}{c^2}.$$

So the boundary/interface can be interpreted as converting matter content into exterior \(A\)-flux.

The boundary \(\kappa\)-relaxation study showed that \(\kappa\) can be nonzero inside and still vanish smoothly at the surface.

The cleanest reduced condition is:

$$\kappa(R)=0,$$

and:

$$\kappa'(R)=0.$$

This prevents exterior \(\kappa\)-leak.

---

## Current Matching Strategy

The current best matching strategy is:

### 1. Interior Matter Region

Inside matter:

```text
A is sourced by enclosed mass through the areal-flux law.
kappa may be nonzero because matter is traceful.
pressure/stress/interior self-field effects likely live in kappa or corrections to A.
```

Symbolically:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r),$$

and possibly:

$$\kappa_{\rm in}(r)\neq0.$$

### 2. Boundary / Interface

At the boundary:

```text
matter fixes the exterior A-flux;
kappa relaxes to zero;
boundary/interface conditions prevent exterior kappa leak.
```

Conditions:

$$F_A(R)=\frac{8\pi GM}{c^2},$$

$$\kappa(R)=0,$$

and ideally:

$$\kappa'(R)=0.$$

### 3. Exterior Source-Free Region

Outside matter:

```text
A-flux is conserved;
kappa is suppressed;
B is determined by compensation.
```

So:

$$F_A=\frac{8\pi GM}{c^2},$$

$$A=1-\frac{2GM}{rc^2},$$

$$\kappa=0,$$

$$B=\frac1A.$$

---

## Why This Strategy Matters

This strategy prevents two mistakes.

### Mistake 1: Forcing Kappa Zero Everywhere

If \(\kappa=0\) is forced inside matter, then:

$$B=\frac1A$$

inside matter.

But the GR interior Schwarzschild solution generally does not have:

$$AB=1$$

inside matter.

Therefore forcing \(\kappa=0\) everywhere likely removes necessary interior physics.

### Mistake 2: Treating A as a Curved-Space Harmonic Scalar

The exact source law is not ordinary curved-spatial harmonicity.

It is currently best stated as an areal-flux law:

$$F_A=4\pi r^2A'.$$

The boundary action supports this interpretation because \(r^2A'\) appears naturally as boundary momentum.

---

## Current Best Physical Picture

The best current reduced picture is:

```text
Matter does two different things.

First, its total mass fixes the exterior A-flux.

Second, its interior trace/stress content may excite kappa inside.

The source-free exterior suppresses kappa, leaving only compensated A/B
reciprocal geometry.
```

In slogan form:

```text
Exterior gravity is compensated A-flux.
Interior matter may carry traceful kappa response.
The boundary turns matter content into exterior flux and restores compensation.
```

---

## Open Problems

### 1. Source of Kappa

What matter quantity sources interior \(\kappa\)?

Possibilities:

```text
density trace,
pressure,
stress,
relativistic self-energy,
boundary/interface stress.
```

### 2. Boundary Conditions

What principle enforces:

$$\kappa(R)=0$$

or:

$$\kappa'(R)=0$$

at the boundary?

### 3. Source Coupling Normalization

Why does the boundary coupling have normalization:

$$q_M=\frac{4K_AGM}{c^2}?$$

### 4. Pressure / Stress

How do pressure and stress modify the source law?

Do they source:

```text
A-flux,
kappa,
or both?
```

### 5. Covariant Parent

What covariant or geometric principle reduces to this interior/exterior structure?

---

## Recommended Next Work

### 1. Candidate GR Residual as Source Terms

```text
candidate_gr_residual_source_terms.py
```

Purpose:

```text
Decompose the GR interior residual into possible pressure/stress/kappa source terms.
```

### 2. Candidate Pressure / Stress Source Extension

```text
candidate_pressure_stress_source_extension.py
```

Purpose:

```text
Test simple pressure contributions to A-flux and kappa response.
```

### 3. Candidate Boundary Kappa Action

```text
candidate_boundary_kappa_action.py
```

Purpose:

```text
Try to derive kappa boundary relaxation from an action.
```

### 4. Candidate Interior / Exterior Master Summary

```text
interior_exterior_matching_summary.md
```

Purpose:

```text
Update the overall program architecture after pressure/stress tests.
```

---

## Summary

The current matching strategy is:

```text
Interior:
  A-flux follows enclosed mass.
  Kappa may be nonzero.

Boundary:
  matter fixes exterior A-flux.
  kappa relaxes to zero.

Exterior:
  A-flux is conserved.
  kappa=0.
  B=1/A.
```

This reconciles the exact Schwarzschild exterior recovery with the fact that realistic matter interiors need not satisfy \(AB=1\).

The next major target is to identify the source law for interior \(\kappa\), likely involving pressure, stress, or relativistic self-energy.
