# Candidate Kappa Joint Minimum Energy Functional

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final physical derivation, not an observational claim, and not a completed replacement for GR interior matching. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_joint_minimum_energy_functional.py
```

The guiding question was:

```text
Can the interior/exterior spline be interpreted as the minimizer of a joint
vacuum-curvature energy rather than hand smoothing?
```

The answer is:

```text
Yes, as a variational toy model.

A variational joint-minimum model can make the spline idea less ad hoc.

It suggests the largest deviation from naive GR/Newtonian interior matching
would occur near the material boundary.

But no measurement claim is justified yet.
```

Needed next:

```text
define concrete deviation diagnostics,
then estimate magnitude only after weights/scale are specified.
```

---

## Why This Study Matters

The previous spline model showed that an interior quadratic tendency and exterior reciprocal tendency can be blended smoothly.

But a spline alone is dangerous because it may be only curve fitting.

This study moves the idea toward a variational model: instead of choosing a transition curve by hand, the curve should minimize a joint vacuum-curvature energy.

The key idea is:

```text
interior tendency,
exterior tendency,
and smoothness penalty
compete to form one minimum configuration.
```

This is where a near-boundary deviation from naive GR/Newtonian matching could arise.

---

## Toy Energy Density

The toy energy density is:

\[
L
=
W_{\rm int}(r)(f-f_{\rm int})^2
+
W_{\rm ext}(r)(f-f_{\rm ext})^2
+
\lambda_1(f')^2
+
\lambda_2(f'')^2.
\]

Interpretation:

```text
W_int:
  anchors the profile to the interior tendency

W_ext:
  anchors the profile to the exterior tendency

lambda_1:
  penalizes slope strain

lambda_2:
  penalizes curvature jumps / sharp bending
```

Status:

```text
PLAUSIBLE — weights not derived.
```

This is not yet the real action. It is a toy variational structure.

---

## Euler-Lagrange Structure

For a functional depending on:

\[
f,\qquad f',\qquad f'',
\]

the Euler-Lagrange equation is:

\[
\frac{\partial L}{\partial f}
-
\frac{d}{dr}
\left(
\frac{\partial L}{\partial f'}
\right)
+
\frac{d^2}{dr^2}
\left(
\frac{\partial L}{\partial f''}
\right)
=
0.
\]

The script found the structure:

\[
-2\lambda_1 f''
+
2\lambda_2 f''''
+
2(f-f_{\rm ext})W_{\rm ext}
+
2(f-f_{\rm int})W_{\rm int}
=
0.
\]

Status:

```text
DERIVED_REDUCED — toy variational structure only.
```

The \(\lambda_2\) term makes the minimizer fourth-order.

That is expected for curvature-smoothing energy.

It also means boundary conditions must be handled carefully.

---

## Constant-Weight Schematic Equation

For constant weights, the schematic minimizer equation is:

\[
W_e(f-f_{\rm ext})
+
W_i(f-f_{\rm int})
-
\lambda_1 f''
+
\lambda_2 f''''
=
0.
\]

Equivalently:

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

Status:

```text
DERIVED_REDUCED — still toy model.
```

This shows the minimizer is pulled toward both interior and exterior tendencies while smoothness terms distribute the mismatch.

---

## Interior / Exterior Tendencies

The toy interior tendency is:

\[
f_{\rm int}=a_0+a_2r^2.
\]

The toy exterior tendency is:

\[
f_{\rm ext}=1-\frac{M}{r}.
\]

In the energy model, these are not manually spliced.

They are competing attractors/minima with radial weights.

Status:

```text
PLAUSIBLE — physical identification still open.
```

---

## Smooth Weight Functions

A smooth model needs radial weights such as:

```text
W_int(r):
  large inside, fades near/outside surface

W_ext(r):
  small inside, dominates outside
```

A possible transition coordinate is:

\[
x=\frac{r-R}{\sigma}.
\]

A possible logistic weight is:

\[
W_{\rm ext}
=
\frac{1}{1+e^{-x}},
\]

and:

\[
W_{\rm int}
=
1-W_{\rm ext}.
\]

This avoids a hard seam but introduces:

\[
\sigma.
\]

The parameter \(\sigma\) would control the near-boundary deviation width.

Status:

```text
PLAUSIBLE — sigma / weights not derived.
```

---

## Near-Boundary Deviation Diagnostic

The script defined a near-boundary deviation diagnostic:

\[
\delta_{\rm GR-like}(r)
=
f_{\rm joint}(r)
-
f_{\rm GR,ref}(r).
\]

Possible derived diagnostics later include:

```text
delta_f,
delta_f',
delta_f'',
deviation in local acceleration,
deviation in redshift / time dilation.
```

Status:

```text
CONSTRAINED_BY_IDENTITY — no magnitude prediction yet.
```

This is the correct discipline.

Before claiming a measurable deviation, the theory must define what observable deviates.

---

## Measurement Caution

A near-boundary deviation is plausible in the toy model, but not yet an observational prediction.

Reasons:

```text
no derived energy weights,
no derived transition width,
no selected observable,
no magnitude estimate,
interior curvature is hard to measure directly,
exterior far field must remain GR-like / 1/r.
```

Likely location of largest deviation:

```text
near the material surface / interface.
```

Likely status:

```text
theoretical effect first,
possible niche experimental target later.
```

Status:

```text
CONSTRAINED_BY_IDENTITY — do not overclaim.
```

---

## GR-Deviation Hierarchy

The script produced this hierarchy:

| Region | Expected deviation status |
|---|---|
| deep interior | possible, model-dependent |
| near boundary / interface | most likely largest deviation |
| exterior near surface | possible small smoothing correction |
| far exterior | should recover \(1/r\) / GR-like behavior |
| radiation sector | no breathing wave from \(\kappa\) |

Status:

```text
PLAUSIBLE — requires quantitative model.
```

This hierarchy keeps the model from claiming broad GR violation.

---

## Failure Controls

The variational joint-minimum model fails if:

1. Weights are arbitrary curve-fitting.
2. Far exterior \(1/r\) behavior is spoiled.
3. Transition width \(\sigma\) is unconstrained.
4. Predicted deviations conflict with existing tests.
5. \(\kappa\) and \(A\) variables are mixed without a recombination rule.
6. Fourth-order smoothing introduces unphysical boundary modes.
7. Near-boundary deviation is claimed without observable definition.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| energy density template | PLAUSIBLE |
| Euler-Lagrange structure | DERIVED_REDUCED |
| fourth-order smoothing equation | DERIVED_REDUCED toy result |
| radial weights | PLAUSIBLE / not derived |
| transition width \(\sigma\) | MISSING |
| near-boundary deviation diagnostic | CONSTRAINED_BY_IDENTITY |
| observability | UNKNOWN |
| final prediction | UNFINISHED |

---

## What This Study Established

This study established:

1. The spline idea can be written as a variational toy model.
2. The Euler-Lagrange equation contains a fourth-order smoothing term if \(f''\) is penalized.
3. The minimizer is pulled toward both interior and exterior tendencies.
4. Smooth radial weights can make the boundary a transition region rather than a hard seam.
5. A near-boundary deviation diagnostic can be defined.
6. No magnitude or measurement claim is justified yet.

---

## What This Study Did Not Establish

This study did not derive \(W_{\rm int}\).

It did not derive \(W_{\rm ext}\).

It did not derive \(\lambda_1\).

It did not derive \(\lambda_2\).

It did not derive \(\sigma\).

It did not identify the observable.

It did not quantify any GR deviation.

It did not prove that the deviation has not been measured.

It only made the spline model variational at toy level.

---

## Current Best Interpretation

A variational joint-minimum model can make the spline idea less ad hoc.

It suggests the largest deviation from naive GR/Newtonian interior matching would occur near the material boundary.

But no measurement claim is justified yet.

Needed next:

```text
define concrete deviation diagnostics,
then estimate magnitude only after weights/scale are specified.
```

---

## Next Development Target

The next script should be:

```text
candidate_kappa_near_boundary_deviation_diagnostic.py
```

Purpose:

```text
Define concrete acceleration / redshift / curvature deviation diagnostics.
```

Reason:

```text
If deviation from GR is possible, define what would deviate before claiming
magnitude or measurability.
```

Expected result:

```text
A list of candidate observables and symbolic diagnostics:
  potential deviation,
  acceleration deviation,
  curvature deviation,
  redshift deviation,
  interface width dependence.
```

---

## Summary

The variational toy model says:

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

This is a joint minimum, not just a hand spline.

It may imply near-boundary deviation from GR.

But the next rule is strict:

```text
diagnostic before prediction.
```
