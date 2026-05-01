# Candidate Interior A Source Model

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full interior relativistic solution. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_interior_A_source_model.py
```

The guiding question was:

```text
Does the areal-flux source law behave sensibly inside a finite spherical source,
or is it only an exterior trick?
```

The answer is qualified but positive.

For a constant-density sphere, the reduced areal-flux law gives:

```text
regular interior A(r),
smooth matching of A and A' at the surface,
continuous areal flux,
the correct exterior Schwarzschild coefficient,
and the standard weak-field Newtonian interior potential.
```

But the model is not the full GR interior Schwarzschild solution.

It is the interior solution of the reduced areal-flux law.

---

## Background

The exact static spherical exterior branch uses:

$$A=e^s,$$

with source law:

$$\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho.$$

The areal radial operator is:

$$\Delta_{\rm areal}A =
\frac1{r^2}\frac{d}{dr}(r^2A').$$

Equivalently, define the areal flux:

$$F_A(r)=4\pi r^2A'(r).$$

Then the flux law is:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

Outside the source:

$$M_{\rm enc}(r)=M,$$

so:

$$F_A=\frac{8\pi GM}{c^2}.$$

This gives:

$$A(r)=1-\frac{2GM}{rc^2}.$$

With exterior compensation:

$$\kappa=0,$$

we get:

$$B=\frac1A.$$

Thus the exact Schwarzschild exterior metric factors are recovered in areal gauge.

The present study asks what happens inside a finite source.

---

## Constant-Density Source

Take a spherical source of radius \(R\) and constant density:

$$\rho(r)=\rho_0,$$

for:

$$0\le r\le R.$$

The enclosed mass is:

$$M_{\rm enc}(r) =
\frac{4\pi}{3}\rho_0 r^3.$$

Differentiating:

$$M_{\rm enc}'(r)=4\pi r^2\rho_0.$$

This matches the spherical volume element, so the enclosed-mass bookkeeping is consistent.

The total mass is:

$$M=M_{\rm enc}(R) =
\frac{4\pi}{3}\rho_0R^3.$$

---

## Interior A Equation

The areal-flux law is:

$$F_A(r)=4\pi r^2A'(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

Substitute:

$$M_{\rm enc}(r)=\frac{4\pi}{3}\rho_0r^3.$$

Then:

$$4\pi r^2A' =
\frac{8\pi G}{c^2}
\left(
\frac{4\pi}{3}\rho_0r^3
\right).$$

Divide by \(4\pi r^2\):

$$A'(r)=\frac{8\pi G\rho_0}{3c^2}r.$$

Integrating:

$$A_{\rm in}(r)=C+\frac{4\pi G\rho_0}{3c^2}r^2.$$

The script confirmed directly that:

$$\Delta_{\rm areal}A_{\rm in} =
\frac{8\pi G\rho_0}{c^2}.$$

Thus the interior solution satisfies the reduced areal source equation.

---

## Matching to the Exterior

The exterior solution is:

$$A_{\rm out}(r)=1-\frac{2GM}{c^2r}.$$

Using:

$$M=\frac{4\pi}{3}\rho_0R^3,$$

this becomes:

$$A_{\rm out}(r) =
1-\frac{8\pi G\rho_0R^3}{3c^2r}.$$

At the boundary \(r=R\):

$$A_{\rm out}(R) =
1-\frac{8\pi G\rho_0R^2}{3c^2}.$$

The interior value at \(R\) is:

$$A_{\rm in}(R) =
C+\frac{4\pi G\rho_0R^2}{3c^2}.$$

Set:

$$A_{\rm in}(R)=A_{\rm out}(R).$$

Then:

$$C+\frac{4\pi G\rho_0R^2}{3c^2} =
1-\frac{8\pi G\rho_0R^2}{3c^2}.$$

So:

$$C=1-\frac{4\pi G\rho_0R^2}{c^2}.$$

Therefore the matched interior solution is:

$$A_{\rm in}(r) =
1-\frac{4\pi G\rho_0R^2}{c^2}
+
\frac{4\pi G\rho_0r^2}{3c^2}.
$$

The script confirmed that this value of \(C\) enforces continuity of \(A\) at \(r=R\).

---

## Derivative Matching

The interior derivative is:

$$A_{\rm in}'(r)=\frac{8\pi G\rho_0}{3c^2}r.$$

At \(r=R\):

$$A_{\rm in}'(R)=\frac{8\pi G\rho_0R}{3c^2}.$$

The exterior derivative is:

$$A_{\rm out}'(r) =
\frac{2GM}{c^2r^2}.$$

Using:

$$M=\frac{4\pi}{3}\rho_0R^3,$$

at \(r=R\):

$$A_{\rm out}'(R) =
\frac{2G}{c^2R^2}
\left(
\frac{4\pi}{3}\rho_0R^3
\right) =
\frac{8\pi G\rho_0R}{3c^2}.
$$

Therefore:

$$A_{\rm in}'(R)=A_{\rm out}'(R).$$

The script confirmed that \(A'\) matches at the source boundary.

---

## Flux Continuity

The areal flux is:

$$F_A(r)=4\pi r^2A'(r).$$

For the interior solution:

$$F_{\rm in}(r) =
4\pi r^2
\left(
\frac{8\pi G\rho_0}{3c^2}r
\right) =
\frac{32\pi^2G\rho_0r^3}{3c^2}.
$$

At \(r=R\):

$$F_{\rm in}(R) =
\frac{32\pi^2G\rho_0R^3}{3c^2}.
$$

The exterior flux is:

$$F_{\rm out} =
\frac{8\pi GM}{c^2}.
$$

Using:

$$M=\frac{4\pi}{3}\rho_0R^3,$$

we get:

$$F_{\rm out} =
\frac{8\pi G}{c^2}
\left(
\frac{4\pi}{3}\rho_0R^3
\right) =
\frac{32\pi^2G\rho_0R^3}{3c^2}.
$$

Therefore:

$$F_{\rm in}(R)=F_{\rm out}(R).$$

The script confirmed both flux continuity and mass normalization.

---

## Regularity at the Origin

The matched interior solution is:

$$A_{\rm in}(r) =
1-\frac{4\pi G\rho_0R^2}{c^2}
+
\frac{4\pi G\rho_0r^2}{3c^2}.
$$

At the origin:

$$A_{\rm in}(0) =
1-\frac{4\pi G\rho_0R^2}{c^2}.
$$

This is finite.

The derivative is:

$$A_{\rm in}'(r)=\frac{8\pi G\rho_0}{3c^2}r.$$

Thus:

$$A_{\rm in}'(0)=0.$$

The flux is:

$$F_A(r)=4\pi r^2A'(r)\propto r^3.$$

Thus:

$$F_A(0)=0.$$

The script confirmed that the interior solution is regular at the origin.

---

## Interior B from Kappa Equals Zero

If the model imposes:

$$\kappa=0$$

inside the matter source as well as outside, then:

$$AB=1.$$

Thus:

$$B_{\rm in}=\frac1{A_{\rm in}}.$$

So:

$$B_{\rm in} =
\left(
1-\frac{4\pi G\rho_0R^2}{c^2}
+
\frac{4\pi G\rho_0r^2}{3c^2}
\right)^{-1}.
$$

The script confirmed:

$$A_{\rm in}B_{\rm in}=1.$$

However, this is a modeling assumption. It may not be appropriate inside matter.

The script explicitly warns:

```text
This is the reciprocal interior metric implied by the reduced model.
It is not the GR interior Schwarzschild solution.
```

---

## Weak-Field Newtonian Interior Potential

In weak field:

$$A\approx1+\frac{2\Phi}{c^2}.$$

Thus:

$$\Phi=\frac{c^2}{2}(A-1).$$

Using the interior solution:

$$A_{\rm in} =
1-\frac{4\pi G\rho_0R^2}{c^2}
+
\frac{4\pi G\rho_0r^2}{3c^2},
$$

we get:

$$\Phi_{\rm in} =
-2\pi G\rho_0R^2
+
\frac{2\pi G\rho_0}{3}r^2.
$$

This is the standard Newtonian potential inside a uniform-density sphere, with \(\Phi(\infty)=0\).

The script confirmed that the interior \(A(r)\) matches the weak-field Newtonian interior potential normalization.

---

## Difference from the GR Interior Schwarzschild Solution

This interior model is not the full GR interior Schwarzschild solution.

Reasons:

```text
pressure is not included;
stress-energy is not fully represented;
the GR interior solution has a different exact lapse structure;
the current model enforces kappa=0 / B=1/A even inside;
the current source law uses only rho, not pressure or relativistic stress.
```

The model should be understood as:

```text
the interior solution of the reduced areal-flux source law.
```

It is useful because it tests the source law across a finite body.

It is not a replacement for the relativistic interior solution.

---

## What This Study Established

This study established:

1. For constant density:
   $$M_{\rm enc}(r)=\frac{4\pi}{3}\rho_0r^3.$$

2. The areal-flux law gives:
   $$A'(r)=\frac{2GM_{\rm enc}(r)}{c^2r^2}.$$

3. Therefore:
   $$A_{\rm in}(r)=C+\frac{4\pi G\rho_0}{3c^2}r^2.$$

4. Matching to the exterior fixes:
   $$C=1-\frac{4\pi G\rho_0R^2}{c^2}.$$

5. The matched interior solution is:
   $$A_{\rm in}(r)
   =
   1-\frac{4\pi G\rho_0R^2}{c^2}
   +
   \frac{4\pi G\rho_0r^2}{3c^2}.
   $$

6. \(A\) is continuous at \(R\).

7. \(A'\) is continuous at \(R\).

8. Areal flux is continuous at \(R\).

9. \(A\) is finite at the origin.

10. \(A'\) vanishes at the origin.

11. The weak-field Newtonian interior potential is recovered.

12. The result is not the full GR interior Schwarzschild solution.

---

## What This Study Did Not Establish

This study did not derive the areal-flux law from deeper principles.

It did not prove that \(\kappa=0\) should hold inside matter.

It did not include pressure.

It did not include relativistic stress.

It did not derive the GR interior Schwarzschild solution.

It did not address stability.

It did not address horizons or compactness bounds.

It did not address nonspherical sources.

It did not address time dependence.

It only tested whether the reduced areal-flux law has a sensible constant-density interior continuation.

---

## Relationship to the Areal-Flux Principle

The areal-flux principle states:

$$F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).$$

The interior test confirms that this principle behaves naturally for a finite source.

Inside matter, the flux grows with enclosed mass.

At the boundary, the flux equals the exterior mass flux.

Outside matter, the flux is conserved.

This is exactly the behavior expected of a Gauss-law-like source principle.

---

## Relationship to Exterior Schwarzschild Recovery

The exterior recovery remains:

$$A_{\rm out}(r)=1-\frac{2GM}{rc^2}.$$

The interior solution matches it smoothly at \(r=R\).

Thus the finite-source model supports the exterior Schwarzschild coefficient rather than only imposing it by hand.

The chain is:

```text
rho(r) -> M_enc(r) -> F_A(r) -> A'(r) -> A(r) -> exterior coefficient
```

This is stronger than using only exterior boundary assumptions.

---

## Current Best Interpretation

The current best interpretation is:

```text
The areal-flux law is internally consistent for a finite constant-density
source at the reduced level.

It reproduces the Newtonian interior potential in weak field and matches
smoothly to the exact exterior Schwarzschild A factor.

But the relativistic interior is incomplete because pressure, stress, and
possibly nonzero interior kappa are not yet modeled.
```

---

## Next Development Targets

### 1. Interior Kappa Question

A possible next script:

```text
candidate_interior_kappa_response.py
```

Purpose:

```text
Test whether kappa=0 should be enforced inside matter or only in the
source-free exterior.
```

### 2. Pressure / Stress Source Extension

A possible next note:

```text
candidate_pressure_stress_source_extension.md
```

Purpose:

```text
Ask how pressure and relativistic stress should modify the areal-flux source law.
```

### 3. Compare to GR Interior Schwarzschild

A possible next script:

```text
candidate_compare_gr_interior_schwarzschild.py
```

Purpose:

```text
Compare the reduced interior A(r), B(r) to the exact GR constant-density
interior metric and identify which missing terms correspond to pressure/stress.
```

### 4. Boundary Flux Action

A possible next script:

```text
candidate_boundary_flux_action.py
```

Purpose:

```text
Test whether areal flux can be derived from a boundary/interface action.
```

---

## Summary

The interior \(A\)-source model passed its reduced consistency checks.

For a constant-density sphere:

$$M_{\rm enc}(r)=\frac{4\pi}{3}\rho_0r^3.$$

The areal-flux law gives:

$$A_{\rm in}(r) =
1-\frac{4\pi G\rho_0R^2}{c^2}
+
\frac{4\pi G\rho_0r^2}{3c^2}.
$$

This matches smoothly to:

$$A_{\rm out}(r)=1-\frac{2GM}{rc^2},$$

with:

$$M=\frac{4\pi}{3}\rho_0R^3.$$

The model has continuous \(A\), continuous \(A'\), continuous areal flux, and regular origin behavior.

In weak field, it reproduces the Newtonian potential inside a uniform sphere.

But it is not the full GR interior Schwarzschild solution.

The next major question is whether \(\kappa=0\) is valid inside matter, and how pressure/stress should enter the source law.
