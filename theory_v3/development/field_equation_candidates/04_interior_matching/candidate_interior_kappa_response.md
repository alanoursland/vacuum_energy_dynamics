# Candidate Interior Kappa Response

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full matter model. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_interior_kappa_response.py
```

The guiding question was:

```text
Should kappa=0 be enforced inside matter, or should kappa=0 be treated
only as a source-free exterior condition?
```

The answer is:

```text
kappa=0 is safest as an exterior/source-free condition.
Interior matter may source kappa without necessarily spoiling the exterior,
provided kappa relaxes to zero at or outside the boundary.
```

This matters because the reduced exterior branch depends on:

$$\kappa=0,$$

which gives:

$$AB=1.$$

But the GR interior Schwarzschild comparison shows that \(AB=1\) generally does not hold inside matter. This suggests that matter may produce a traceful interior response.

---

## Background

The reduced mode split is:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Therefore:

$$AB=e^{2\kappa}.$$

If:

$$\kappa=0,$$

then:

$$AB=1.$$

So:

$$B=\frac1A.$$

This works in the source-free Schwarzschild exterior.

The question is whether it should also be forced inside the matter source.

---

## Case 1: Forced Interior Compensation

The reduced constant-density interior \(A\)-solution is:

$$A_{\rm in}
=
1-\frac{4\pi G\rho_0R^2}{c^2}
+
\frac{4\pi G\rho_0r^2}{3c^2}.
$$

If we force:

$$\kappa_{\rm in}=0,$$

then:

$$B_{\rm in}=\frac1{A_{\rm in}}.$$

Thus:

$$A_{\rm in}B_{\rm in}=1.$$

This is the simplest interior extension.

But it may be too strong because it excludes traceful matter response.

In particular, it makes the interior reciprocal in the same way as the exterior, while known GR interior behavior does not generally preserve \(AB=1\) inside matter.

---

## Case 2: Generic Traceful Kappa Source Inside Matter

The script tested a simple traceful interior profile:

$$\kappa_{\rm in}
=
\frac{G\eta\rho_0}{c^2}(R^2-r^2).
$$

This profile is regular at the origin:

$$\kappa_{\rm in}'(0)=0.$$

It vanishes at the boundary:

$$\kappa_{\rm in}(R)=0.$$

Thus it can match to an exterior with:

$$\kappa_{\rm ext}=0.$$

But its boundary derivative is:

$$\kappa_{\rm in}'(R)
=
-\frac{2G\eta\rho_0R}{c^2}.
$$

So unless an interface layer handles the derivative, there may be a boundary derivative jump.

The product becomes:

$$A_{\rm in}B_{\rm in}=e^{2\kappa_{\rm in}}.$$

Thus a nonzero interior \(\kappa\) breaks reciprocal interior scaling generically, while still allowing the exterior to remain reciprocal if \(\kappa\) vanishes at the boundary.

---

## Case 3: Smooth Boundary Kappa Profile

The script also tested a smoother profile:

$$\kappa_{\rm in}
=
\frac{G\eta\rho_0}{c^2R^2}(R^2-r^2)^2.
$$

This satisfies:

$$\kappa_{\rm in}(R)=0,$$

and:

$$\kappa_{\rm in}'(R)=0.$$

It is also regular at the origin:

$$\kappa_{\rm in}'(0)=0.$$

This demonstrates that a nonzero interior trace response can coexist smoothly with exterior compensation:

$$\kappa_{\rm ext}=0.$$

Thus nonzero interior \(\kappa\) is not automatically fatal.

---

## Case 4: Interior Kappa Energy Penalty

The script used a local algebraic toy energy:

$$E=C_\kappa\kappa^2-J_\kappa\kappa.$$

Stationarity gives:

$$2C_\kappa\kappa-J_\kappa=0.$$

Thus:

$$\kappa=\frac{J_\kappa}{2C_\kappa}.$$

If:

$$J_\kappa\neq0$$

inside matter, then \(\kappa\) responds.

If:

$$J_\kappa=0$$

outside matter, then \(\kappa\) relaxes to zero.

This supports a natural interior/exterior split:

```text
matter may source kappa inside;
source-free exterior suppresses kappa.
```

---

## Case 5: Exterior Matching Classification

The script identified four possible regimes.

### A. Kappa Equals Zero Everywhere

```text
simplest;
reciprocal interior;
not GR interior.
```

This is clean but probably too restrictive.

### B. Kappa Sourced Inside, Kappa(R) = 0

```text
exterior remains compensated;
interior can carry traceful matter response;
boundary derivative may need interface physics.
```

This is plausible.

### C. Kappa Sourced Inside, Kappa(R) Nonzero

```text
exterior begins with nonzero kappa;
reciprocal exterior may fail unless relaxation layer suppresses it.
```

This creates exterior deviation risk.

### D. Smooth Interior Kappa with Kappa(R)=Kappa'(R)=0

```text
cleanest coexistence of interior trace response and exterior compensation.
```

This is the best toy class found by the script.

---

## Case 6: Exterior Kappa Leakage

If interior \(\kappa\) leaks into the exterior as:

$$\kappa_{\rm ext}=\lambda_\kappa\epsilon,$$

with:

$$s_{\rm ext}=-2\epsilon,$$

then:

$$A\approx1+(\lambda_\kappa-2)\epsilon,$$

and:

$$B\approx1+(\lambda_\kappa+2)\epsilon.$$

Also:

$$AB\approx1+2\lambda_\kappa\epsilon.$$

Thus exterior \(\kappa\)-leak modifies weak-field observables.

This reuses the earlier kappa-leak conclusion:

```text
exterior kappa leak is observationally dangerous.
```

So the theory must suppress exterior \(\kappa\) strongly in ordinary weak-field regions.

---

## What This Study Established

This study established:

1. Forcing \(\kappa=0\) inside matter is possible but restrictive.
2. Nonzero interior \(\kappa\) breaks reciprocal interior scaling.
3. Nonzero interior \(\kappa\) can still match to \(\kappa=0\) exterior.
4. Smooth profiles can satisfy:
   $$\kappa(R)=0,\qquad \kappa'(R)=0.$$
5. A traceful matter source can produce:
   $$\kappa=J_\kappa/(2C_\kappa).$$
6. Exterior \(\kappa\)-leak is observationally dangerous.
7. The most plausible interpretation is:
   ```text
   kappa=0 is an exterior/source-free relaxation condition,
   not necessarily an interior matter condition.
   ```

---

## What This Study Did Not Establish

This study did not derive the interior \(\kappa\) source law.

It did not determine whether matter actually sources \(\kappa\).

It did not include pressure or stress explicitly.

It did not provide a full boundary layer model.

It did not solve the full interior metric.

It did not derive GR interior Schwarzschild behavior.

It only showed that interior \(\kappa\)-response is plausible and not automatically fatal.

---

## Relationship to GR Interior Comparison

The GR interior comparison shows that the exact GR constant-density interior generally does not have:

$$AB=1.$$

That means GR has an effective interior \(\kappa\)-like deviation:

$$\kappa_{\rm GR}=\frac12\ln(A_{\rm GR}B_{\rm GR})\neq0$$

inside matter.

But at the exterior boundary:

$$A_{\rm GR}B_{\rm GR}=1.$$

Thus the GR comparison supports the same structural lesson:

```text
kappa=0 is naturally exterior/source-free;
inside matter, traceful response may appear.
```

This does not mean the reduced model must copy GR exactly. It means the reduced model should not blindly force \(\kappa=0\) inside matter.

---

## Current Best Interpretation

The current best interpretation is:

```text
The exterior source-free region suppresses kappa.

The interior matter region may source kappa.

A viable source model must prevent kappa leak into ordinary exterior weak fields.

Boundary/interface physics may convert traceful interior response into
compensated exterior flux.
```

This gives the reduced model more flexibility without sacrificing the exact exterior recovery.

---

## Next Development Targets

### 1. Boundary Kappa Relaxation Layer

A possible script:

```text
candidate_boundary_kappa_relaxation_layer.py
```

Purpose:

```text
Model how an interior kappa response can relax to exterior kappa=0 across
a finite boundary layer.
```

### 2. Pressure / Stress Source Extension

A possible note:

```text
candidate_pressure_stress_source_extension.md
```

Purpose:

```text
Identify whether pressure/stress should source kappa, A-flux, or both.
```

### 3. Compare to GR Interior Residual

A possible follow-up:

```text
candidate_gr_interior_residual_source_terms.py
```

Purpose:

```text
Interpret the difference between the reduced interior and GR interior as
missing pressure/stress/kappa terms.
```

---

## Summary

The interior \(\kappa\)-response study suggests that \(\kappa=0\) should not be assumed everywhere.

It is safest to treat:

$$\kappa=0$$

as a source-free exterior compensation condition.

Inside matter, \(\kappa\) may respond to traceful source content.

This can coexist with exact exterior compensation if \(\kappa\) vanishes at the boundary or relaxes through an interface layer.

The theory must still explain the interior source law and prevent exterior \(\kappa\)-leak.
