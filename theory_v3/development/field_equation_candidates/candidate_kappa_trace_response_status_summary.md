# Kappa Trace Response Status Summary

## Group

```text
10_kappa_trace_response
```

## One-Line Result

\[
\kappa
\]

is best interpreted as a constrained, non-inertial trace / vacuum-volume relaxation variable, not as an ordinary propagating scalar field.

It may describe local vacuum-curvature equilibration inside or near matter, but it must not become long-range breathing radiation.

---

## Why This Group Was Needed

Before this group, \(\kappa\) had too many possible jobs:

```text
trace response,
volume response,
interior correction,
exterior suppression variable,
scalar-radiation safety mechanism,
possible relaxation field.
```

That was dangerous.

A variable with too many jobs becomes a repair knob.

This group forced \(\kappa\) into a narrower role.

---

## Current Best Interpretation

The current best interpretation is:

```text
kappa = constrained non-inertial trace / volume relaxation response.
```

More explicitly:

```text
matter trace or pressure shifts a local vacuum-curvature minimum;
kappa relaxes toward that minimum;
the relaxation has no independent momentum channel;
therefore kappa does not overshoot, slosh, or propagate as an ordinary
breathing wave.
```

The preferred equation type is not:

\[
\Box\kappa=\text{source}.
\]

The preferred equation type is closer to first-order local relaxation:

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa
(\kappa-\kappa_{\min}).
\]

For fixed \(\kappa_{\min}\), this gives:

\[
\kappa(t)-\kappa_{\min}
=
[\kappa(0)-\kappa_{\min}]
e^{-\mu_\kappa K_\kappa t}.
\]

So:

```text
no oscillation,
no overshoot,
no slosh,
no ordinary breathing radiation.
```

---

## What Was Rejected

### Raw Density as Primary Source

Raw density \(\rho\) was rejected as the primary \(\kappa\) source.

Reason:

```text
rho already sources the A-sector mass/monopole response.
```

If \(\rho\) also directly sourced \(\kappa\), the theory would risk double-counting the scalar mass field.

---

### Raw Pressure Trace as Final Poisson Source

A raw pressure trace source such as:

\[
S_{\rm trace}=3p
\]

was plausible as an interior hint, but not as a final unscreened Poisson source.

Reason:

\[
Q_\kappa=\int 3p\,d^3x\neq0
\]

for ordinary positive pressure.

A massless \(\kappa\) Poisson equation would then create:

\[
\kappa_{\rm ext}\sim\frac{1}{r}.
\]

That is forbidden.

---

### Ordinary Massless Hyperbolic Kappa

An ordinary wave equation:

\[
\Box\kappa=\alpha S
\]

was rejected.

Reason:

```text
it creates a propagating scalar / breathing-wave channel.
```

The theory’s radiation rule remains:

```text
ordinary long-range gravitational radiation is TT-only unless extra modes are
separately derived and controlled.
```

For \(\kappa\), no such propagating mode has been justified.

---

## What Was Kept

### Trace / Pressure as Minimum Shift

Pressure or trace can still matter, but not as an ordinary radiative scalar charge.

The better interpretation is:

\[
\kappa_{\min}
=
\chi_\kappa S_{\rm trace,effective}.
\]

That is:

```text
matter trace shifts the local equilibrium configuration;
kappa relaxes toward the shifted minimum.
```

This is not the same as:

\[
\Delta\kappa \sim S_{\rm trace}.
\]

This distinction is important.

---

### Compensated / Projected Source Logic

A compensated source:

\[
P_0S
=
S-\langle S\rangle
\]

removes net monopole \(\kappa\)-charge:

\[
\int P_0S\,d^3x=0.
\]

This works algebraically.

But it is nonlocal over the support region and therefore must be interpreted as a constraint/projection identity, not as an ordinary local scalar source.

---

### Boundary-Confined Kappa

A compact interior profile can satisfy:

\[
\kappa(R)=0,
\]

\[
\kappa'(R)=0,
\]

and:

\[
F_\kappa(R)=4\pi R^2\kappa'(R)=0.
\]

Therefore interior \(\kappa\) can exist without exporting exterior scalar flux.

A smoother C2 profile:

\[
\kappa
=
\kappa_0
\left(
1-\frac{r^2}{R^2}
\right)^3
\]

also removes the second-derivative jump at toy level.

---

## Boundary Layer Result

The boundary-layer work found:

```text
C1 compact profile:
  value and first derivative match,
  but second derivative jumps.

C2 compact profile:
  value, first derivative, and second derivative match,
  boundary flux vanishes,
  net effective source vanishes.
```

The C2 profile is mathematically cleaner.

But its elliptic effective source:

\[
S_{\rm eff}\sim\Delta\kappa
\]

is compensated/sign-changing.

That means raw pressure cannot directly produce it as a simple Poisson source.

This pushed the interpretation toward minimum-shift relaxation rather than Poisson sourcing.

---

## Non-Inertial Relaxation Result

The non-inertial model gave the cleanest conceptual result.

Let:

\[
E_{\rm vac-curv}
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Then:

\[
\dot{\kappa}
=
-\mu_\kappa
\frac{\delta E}{\delta\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

The energy in the explicit imbalance decreases:

\[
\frac{dE}{dt}
=
-\mu_\kappa K_\kappa^2(\kappa-\kappa_{\min})^2.
\]

This can be interpreted as conversion into vacuum configuration/restoration energy, not destruction of energy.

Key point:

```text
no independent kappa momentum channel.
```

This is why local trace relaxation does not become a propagating breathing wave.

---

## Joint Minimum / Near-Boundary Result

Late in the group, the picture broadened.

Interior curvature may not be exactly the naive Newtonian parabola near the surface.

The mass may create an interior quadratic tendency, while the exterior vacuum prefers a reciprocal \(1/r\)-type tendency.

A joint-minimum model allows both tendencies to co-solve one smooth curve.

Toy energy:

\[
E[f]
=
\int
\left[
W_{\rm int}(r)(f-f_{\rm int})^2
+
W_{\rm ext}(r)(f-f_{\rm ext})^2
+
\lambda_1(f')^2
+
\lambda_2(f'')^2
\right]dr.
\]

The resulting schematic minimizer is:

\[
\lambda_2 f''''
-
\lambda_1 f''
+
(W_i+W_e)f
=
W_if_{\rm int}
+
W_ef_{\rm ext}.
\]

This suggests a possible near-boundary deviation from naive GR/Newtonian matching.

But no magnitude claim is justified yet.

---

## Near-Boundary Diagnostic Result

The group defined deviation diagnostics:

\[
\delta_f
=
f_{\rm joint}
-
f_{\rm GR,ref},
\]

\[
\delta_g
=
-\frac{d\delta_f}{dr},
\]

\[
\delta_{\rm curv}
=
\frac{d^2\delta_f}{dr^2}.
\]

For a lapse-like deviation:

\[
\frac{\delta z}{z}
\sim
\frac{\delta_A}{2A_{\rm ref}}
\]

in the linearized limit.

Scaling with transition width \(\sigma\):

\[
\delta_f\sim\epsilon,
\]

\[
\delta_g\sim\frac{\epsilon}{\sigma},
\]

\[
\delta_{\rm curv}\sim\frac{\epsilon}{\sigma^2}.
\]

This means curvature-like deviations are most sensitive to narrow transition layers.

But:

```text
epsilon is not derived,
sigma is not derived,
observable mapping is not fixed.
```

So this is diagnostic only.

---

## Theory Naming Note

This group also clarified naming.

Names that fit the current theory better than the original repo name include:

```text
Vacuum Exchange Dynamics
Vacuum Curvature Dynamics
Dynamical Vacuum Gravity
Vacuum Minimum Gravity
Vacuum Flux Gravity
```

The strongest current candidates are:

```text
Vacuum Exchange Dynamics
Vacuum Curvature Dynamics
```

Why:

```text
Vacuum Exchange Dynamics:
  emphasizes exchange between vacuum configuration, curvature, trace response,
  flux, and relaxation.

Vacuum Curvature Dynamics:
  emphasizes the vacuum-curvature minimum and the geometric/gravity target.
```

The simplest broad name is:

```text
Dynamical Vacuum
```

but as an acronym, `DV` is less distinctive.

The name should probably not lock too hard onto only flux, because the theory has moved beyond scalar flux into tensor, vector, trace, constraint, and exchange sectors.

---

## Current Status of Kappa

Status:

```text
STRUCTURALLY CONSTRAINED
NOT DERIVED COVARIANTLY
NOT FINAL
```

What is strong:

```text
ordinary scalar-wave kappa is rejected;
raw density source is rejected;
raw pressure Poisson source is rejected as final;
non-inertial relaxation gives a coherent control model;
boundary-confined profiles can avoid exterior flux;
near-boundary deviation diagnostics are defined.
```

What remains missing:

```text
K_kappa,
mu_kappa,
chi_kappa,
S_trace_effective,
transition width sigma,
parent covariant identity,
recombination map into the metric,
observational magnitude.
```

---

## Current Best Field Picture for Kappa

The best current picture is:

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa
(\kappa-\kappa_{\min}),
\]

with:

\[
\kappa_{\min}
=
\chi_\kappa S_{\rm trace,effective},
\]

and with exterior conditions:

\[
\kappa_{\min}\to0,
\]

\[
\kappa\to0,
\]

\[
F_\kappa(R+)=0.
\]

This is not final.

But it is far better than treating \(\kappa\) as a free scalar repair field.

---

## Group 10 Conclusion

Group 10 turned \(\kappa\) from a vague correction into a disciplined constrained sector.

The conclusion is:

```text
kappa is allowed as local trace / volume relaxation,
but not as propagating scalar gravity.
```

It may alter interior or near-boundary curvature as part of a joint vacuum-curvature minimum.

But any such deviation must be handled through diagnostics first, not claimed as a prediction.

---

## Recommended Next Group

Group 10 has reached a natural stopping point.

The next group should probably not add more \(\kappa\) mechanisms.

The next group should step back and ask:

```text
How do all sectors recombine into a coherent field-equation system?
```

Possible group name:

```text
11_sector_recombination_and_closure
```

or:

```text
11_field_equation_closure
```

Recommended:

```text
11_field_equation_closure
```

Purpose:

```text
Recombine A, W_i, h_ij^TT, and kappa into one disciplined current field-equation
status, with derived / structural / missing labels.
```

The next artifact could be:

```text
field_equation_closure_plan.md
```

or:

```text
candidate_field_equation_closure_inventory.py
```
