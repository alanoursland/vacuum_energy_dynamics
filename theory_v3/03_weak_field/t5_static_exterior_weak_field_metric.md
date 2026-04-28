# T5: Static Exterior Weak-Field Metric

## What This Theorem Establishes

In a static, source-free exterior weak field around a localized mass constraint, the framework recovers the standard one-post-Newtonian weak-field metric structure with

$$\gamma=1,$$

and

$$\beta=1.$$

In PPN-compatible weak-field coordinates, with positive Newtonian potential magnitude

$$U(r)=\frac{GM}{r},$$

and with $U/c^2 \ll 1$, the exterior metric takes the form

$$ds^2 
-\left(1-\frac{2U}{c^2}+2\frac{U^2}{c^4}\right)c^2dt^2
+
\left(1+2\frac{U}{c^2}\right)d\vec{x}^{,2}
+
O(c^{-6})*{tt}+O(c^{-4})*{ij}.$$

Equivalently,

$$-g_{tt}
1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}),$$

and

$$g_{ij}
\left(1+2\frac{U}{c^2}\right)\delta_{ij}+O(c^{-4}).$$

This is the weak-field exterior metric form used by the classical solar-system tests: light deflection, Shapiro delay, and perihelion precession.

The theorem does not introduce new physics. It assembles previously established framework results into the metric form needed for downstream weak-field proofs.

---

## Why This Theorem Is Needed

The framework now has separate pieces of weak-field recovery.

T1 establishes gravitational redshift in the weak-field limit.

T2 establishes gravitational time dilation from T1.

T3 establishes reciprocal exterior scaling in static source-free exteriors, giving the framework's spatial-response result

$$\gamma=1.$$

T4 establishes second-order temporal self-coupling in static source-free exteriors, giving the temporal nonlinear result

$$\beta=1.$$

Each result is individually important, but the downstream weak-field proofs need a single metric statement to invoke. Light deflection, Shapiro delay, perihelion precession, and the weak-field equations of motion should not each reassemble the metric from scratch.

T5 performs that assembly.

It states exactly what static exterior weak-field geometry the framework has earned from its postulates and earlier theorems. Downstream proofs can then cite this theorem rather than importing a metric ansatz independently.

---

## The Setup

Consider a static, source-free exterior vacuum configuration around a localized mass constraint.

The assumptions are:

1. **Staticity:** the exterior configuration is unchanging in time.
2. **Exterior region:** the theorem applies outside the matter source or localized constraint.
3. **Source-free vacuum:** the exterior region contains no matter source of its own.
4. **Weak-field regime:** the potential satisfies $U/c^2 \ll 1$.
5. **Asymptotic flatness:** far from the source, the metric approaches Minkowski form.
6. **PPN-compatible coordinates:** the metric is expressed in weak-field coordinates suitable for comparison with the standard PPN expansion.
7. **Localized source limit:** for the point-mass exterior, the weak-field potential magnitude is $U=GM/r$.

The theorem is not a source-law derivation. It does not derive $U=GM/r$ from the framework's mass-as-constraint dynamics. It uses the Newtonian exterior potential as the weak-field source profile, as standard weak-field metric derivations do.

---

## Convention Note: Metric Coefficients, Scale Factors, and Coordinates

There are three related but distinct pieces of notation that must not be confused.

First, in T3's static spherical exterior convention, the metric is written in areal-radius form as

$$ds^2=-A(r)c^2dt^2+B(r)dr^2+r^2d\Omega^2,$$

and T3 establishes

$$A(r)B(r)=1.$$

That relation is a statement about reciprocal temporal-radial scaling in the static source-free exterior. In weak-field language, it gives the spatial-response condition

$$\gamma=1.$$

Second, in T4, the temporal scale factor is written as

$$\alpha(r)=\sqrt{-g_{tt}(r)}.$$

T4 derives the temporal metric coefficient through second order:

$$-g_{tt}=1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}).$$

Third, the present theorem states the assembled metric in PPN-compatible weak-field coordinates. These are the natural coordinates for comparing the framework with standard PPN parameters and for deriving the usual weak-field tests.

The important invariant content is not the naming convention for $A$, $B$, or $\alpha$. The important content is:

* the first-order spatial coefficient has $\gamma=1$,
* the second-order temporal coefficient has $\beta=1$,
* the metric approaches Minkowski form at infinity,
* and the result is restricted to static source-free exterior weak fields.

---

## Inputs from Earlier Theorems

### Temporal first-order structure

T1 and T2 establish the leading temporal mapping. In weak-field exterior notation, the temporal scale factor has the first-order form

$$\alpha=1-\frac{U}{c^2}+O(c^{-4}),$$

where

$$\alpha=\sqrt{-g_{tt}}.$$

Squaring gives the first-order temporal metric coefficient

$$-g_{tt}=1-\frac{2U}{c^2}+O(c^{-4}).$$

This is the temporal side of weak-field gravity established by redshift and time dilation.

### Spatial first-order structure

T3 establishes reciprocal exterior scaling from P7. In weak-field PPN language, this fixes the spatial-response parameter:

$$\gamma=1.$$

The standard PPN spatial metric is

$$g_{ij}=\left(1+2\gamma\frac{U}{c^2}\right)\delta_{ij}+O(c^{-4}).$$

With

$$\gamma=1,$$

this becomes

$$g_{ij}=\left(1+2\frac{U}{c^2}\right)\delta_{ij}+O(c^{-4}).$$

This is the spatial side of weak-field gravity supplied by exterior compensation.

### Temporal second-order structure

T4 establishes temporal self-coupling from P8. It gives

$$-g_{tt}=1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}).$$

In PPN language, this is

$$\beta=1.$$

This is the second-order temporal side of weak-field gravity supplied by exterior temporal self-coupling.

---

## The Derivation

The standard PPN-compatible weak-field metric for a static exterior field can be written as

$$ds^2
-\left(1-\frac{2U}{c^2}+2\beta\frac{U^2}{c^4}\right)c^2dt^2
+
\left(1+2\gamma\frac{U}{c^2}\right)d\vec{x}^{,2}
+
O(c^{-6})*{tt}+O(c^{-4})*{ij}.$$

Here $U$ is the positive Newtonian potential magnitude, with $U\to0$ at infinity.

By T3,

$$\gamma=1.$$

By T4,

$$\beta=1.$$

Substituting these values gives

$$ds^2
-\left(1-\frac{2U}{c^2}+2\frac{U^2}{c^4}\right)c^2dt^2
+
\left(1+2\frac{U}{c^2}\right)d\vec{x}^{,2}
+
O(c^{-6})*{tt}+O(c^{-4})*{ij}.$$

Therefore,

$$-g_{tt}
1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}),$$

and

$$g_{ij}
\left(1+2\frac{U}{c^2}\right)\delta_{ij}+O(c^{-4}).$$

This is the framework's assembled static exterior weak-field metric.

---

## Relation to General Relativity

In standard general relativity, the exterior weak-field metric of a nonrotating mass has the same one-post-Newtonian form:

$$-g_{tt}
1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}),$$

and

$$g_{ij}
\left(1+2\frac{U}{c^2}\right)\delta_{ij}+O(c^{-4}).$$

In PPN language, GR predicts

$$\gamma=1,$$

and

$$\beta=1.$$

The framework reaches the same weak-field exterior metric through different conceptual machinery.

The spatial response comes from P7/T3: static exterior vacuum compensation.

The second-order temporal response comes from P8/T4: static exterior temporal self-coupling.

This is important. The framework is not importing the Schwarzschild metric wholesale. It is assembling the weak-field exterior form from separately stated framework commitments. Those commitments are restricted exterior principles and are meant to be design constraints for the future field equation.

---

## Why This Is Not a Full Schwarzschild Derivation

T5 does not derive the full Schwarzschild solution.

It derives the weak-field exterior metric through the orders needed for one-post-Newtonian recovery. This is weaker than deriving the exact strong-field metric.

Specifically, T5 does not derive an exact expression for $g_{tt}$ at all orders. T4 fixes the second-order temporal coefficient, not the full temporal function.

T5 does not derive an exact expression for the radial metric coefficient at all orders. T3 supplies reciprocal exterior scaling in its static spherical exterior setting, and in weak-field PPN language this fixes $\gamma=1$, but the full strong-field radial structure remains future work.

T5 does not derive the source profile from the framework's configuration-energy functional. It uses the Newtonian exterior potential $U=GM/r$ in the weak-field limit.

T5 therefore establishes one-post-Newtonian exterior agreement, not full strong-field equivalence.

---

## Why This Is Not a Scalar Metric Ansatz

The assembled metric is controlled by the same weak-field potential $U$ because the theorem is restricted to static, source-free exterior weak fields around a localized mass. In that regime, the exterior field has one Newtonian potential profile.

This does not mean the framework has adopted a universal scalar metric.

The spatial coefficient comes from P7/T3. The temporal second-order coefficient comes from P8/T4. These are separate structural commitments with separate roles. They should not be collapsed into a single all-orders scalar exponential ansatz.

The theorem does not say that every metric component in every regime is generated by one scalar function. It does not address rotating sources, gravitational radiation, nonspherical configurations, cosmology, interior solutions, or strong fields. Those require the future field equation and the directional structure already anticipated by P3a and P4.

T5 is an exterior weak-field assembly theorem, not a general metric postulate.

---

## What This Theorem Enables

T5 is the gateway theorem for the remaining weak-field proofs.

Once the framework has the assembled static exterior weak-field metric, the downstream classical tests can be derived without re-importing general relativity.

The expected downstream theorem sequence is:

* weak-field equations of motion,
* light deflection,
* Shapiro delay,
* perihelion precession.

The light-deflection and Shapiro-delay proofs primarily use the spatial-response coefficient

$$\gamma=1.$$

The perihelion-precession proof uses both

$$\gamma=1$$

and

$$\beta=1.$$

Thus T5 packages the required metric information into one auditable result. Later proofs can depend on T5 rather than each separately invoking T3 and T4.

---

## Scope and Limitations

T5 applies only to static, source-free exterior weak fields.

It does not apply to cosmology. Cosmic expansion is not static exterior vacuum behavior.

It does not apply inside matter. Interior solutions require source terms and cannot be obtained from the source-free exterior assumptions.

It does not apply automatically to rotating bodies. Rotation introduces off-diagonal metric terms and frame-dragging structure not addressed here.

It does not apply automatically to radiating or time-dependent systems. Gravitational waves and dynamical fields require the future field equation.

It does not apply automatically to nonspherical systems beyond the standard weak-field PPN approximation. Directional and tensor-like structure remain open framework work.

It does not establish strong-field agreement with GR. It establishes weak-field exterior agreement through one-post-Newtonian order.

---

## Status of the Result

T5 is a theorem conditional on P7 and P8 through T3 and T4.

Given:

* the first-order temporal mapping from T1/T2,
* the spatial-response result $\gamma=1$ from T3,
* the temporal nonlinear result $\beta=1$ from T4,
* asymptotic flatness,
* the static source-free exterior weak-field setting,
* and the Newtonian exterior potential profile $U$,

then the framework's assembled weak-field exterior metric is

$$ds^2
-\left(1-\frac{2U}{c^2}+2\frac{U^2}{c^4}\right)c^2dt^2
+
\left(1+2\frac{U}{c^2}\right)d\vec{x}^{,2}
+
O(c^{-6})*{tt}+O(c^{-4})*{ij}.$$

This is the same metric structure used by standard one-post-Newtonian weak-field tests.

If P7 or P8 is later derived from a deeper field equation, T5 becomes downstream of that deeper structure. Until then, T5's status is conditional on the exterior structural postulates that supply $\gamma=1$ and $\beta=1$.

---

## Imports and Dependencies

This theorem invokes:

* SR3: Spacetime Interval and Minkowski Structure, for the flat metric limit and interpretation of metric coefficients.
* SR9: Local Validity of SR in Inertial Frames, for local clock and ruler interpretation.

It depends on:

* P1: Vacuum-Energy Equivalence, as part of the ontology underlying vacuum configuration.
* P2: Vacuum-Spacetime Identity, as part of the ontology identifying vacuum configuration with spacetime geometry.
* P3a: Spatial Differential is Curvature, for the framework's curvature vocabulary.
* P4: Curvature Contains Energy, for the configuration-energy status of curved vacuum.
* P5: Vacuum Seeks Minimum Energy Configuration, for the static exterior as a constrained minimum configuration.
* P7: Static Exterior Vacuum Compensation, inherited through T3.
* P8: Static Exterior Temporal Self-Coupling, inherited through T4.
* T1: Gravitational Redshift, for the first-order temporal mapping.
* T2: Gravitational Time Dilation, for the clock-rate interpretation of the first-order temporal mapping.
* T3: Reciprocal Exterior Scaling, for $\gamma=1$.
* T4: Second-Order Temporal Self-Coupling, for $\beta=1$.

---

## Summary

T5 assembles the framework's static exterior weak-field metric.

T3 gives

$$\gamma=1.$$

T4 gives

$$\beta=1.$$

Substituting these into the PPN-compatible static weak-field metric gives

$$ds^2
-\left(1-\frac{2U}{c^2}+2\frac{U^2}{c^4}\right)c^2dt^2
+
\left(1+2\frac{U}{c^2}\right)d\vec{x}^{,2}
+
O(c^{-6})*{tt}+O(c^{-4})*{ij}.$$

This theorem does not introduce a new metric postulate. It assembles previous framework results into the form needed for downstream weak-field proofs.

T5 is therefore the bridge between the postulate-level recovery structure and the observational weak-field theorems: equations of motion, light deflection, Shapiro delay, and perihelion precession.
