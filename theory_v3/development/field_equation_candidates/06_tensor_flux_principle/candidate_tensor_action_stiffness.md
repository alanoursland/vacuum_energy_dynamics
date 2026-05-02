# Candidate Tensor Action Stiffness

## What This Document Is

This document is a development note for the tensor-flux program.

It is not a covariant action, not a derivation of general relativity, and not a complete theory of gravitational radiation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_tensor_action_stiffness.py
```

The guiding question was:

```text
Can a minimal tensor action/stiffness model support the TT wave equation and
explain the source-coupling normalization target?
```

The answer is yes at the reduced toy-model level.

The script showed that a quadratic action for plus/cross TT amplitudes gives the wave equation, keeps plus and cross decoupled at free quadratic order, supplies a positive quadratic energy proxy, and identifies the target source-coupling ratio:

$$
\frac{g_T}{K_T}\sim\frac{2G}{c^4}.
$$

This is the action-side version of the tensor amplitude target:

$$
h_{ij}^{TT}\sim\frac{2G}{c^4R}\ddot Q_{ij}^{TT}.
$$

Important caution:

```text
This is not yet a covariant derivation.
It is a reduced tensor-sector action toy.
```

---

## Background

The tensor-flux program has built the following sequence:

1. Scalar \(A\)-flux cannot produce gravitational waves.
2. The TT tensor basis supplies plus/cross polarizations.
3. The TT sector supports a vacuum wave equation:
   $$\Box h_{ij}^{TT}=0.$$
4. Trace-free quadrupole structure sources the tensor channel.
5. The target far-zone amplitude normalization is:
   $$h_{ij}^{TT}\sim\frac{2G}{c^4R}\ddot Q_{ij}^{TT}.$$
6. Tensor energy-flux scaling gives:
   $$P\sim\frac{G}{c^5}\dddot Q^2.$$
7. Scalar radiation must be absent, constrained, or suppressed.

The present study asks whether a simple action/stiffness model can support this tensor sector.

---

## Tensor Action / Stiffness Problem

The target tensor-sector behavior is:

$$\Box h_{ij}^{TT}=\text{source},$$

with far-zone scaling:

$$h\sim\frac{2G}{c^4R}\ddot Q,$$

and with a positive quadratic wave-energy structure.

The script tested a minimal quadratic action for the plus and cross amplitudes.

For a single polarization \(h(t,z)\), the free Lagrangian density was:

$$
L
=
\frac{K_T}{2c^2}\dot h^2
-
\frac{K_T}{2}h_z^2.
$$

Here \(K_T\) is a reduced tensor stiffness.

---

## Free Plus-Polarization Action

For the free single-polarization action:

$$
L
=
-\frac{K_T}{2}(\partial_z h)^2
+
\frac{K_T}{2c^2}(\partial_t h)^2,
$$

the Euler-Lagrange equation was:

$$
K_T\partial_z^2h
-
\frac{K_T}{c^2}\partial_t^2h
=
0.
$$

Dividing by \(K_T\):

$$
\partial_z^2h
-
\frac1{c^2}\partial_t^2h
=
0.
$$

Equivalently:

$$
\frac1{c^2}\partial_t^2h
-
\partial_z^2h
=
0.
$$

Thus:

$$\Box h=0.$$

The script confirmed:

```text
free action gives wave equation.
```

---

## Plus/Cross Decoupled Quadratic Action

For plus and cross polarizations, the free action used:

$$
L
=
\frac{K_T}{2c^2}
\left(
\dot h_+^2+\dot h_\times^2
\right)
-
\frac{K_T}{2}
\left(
h_+^{\prime 2}+h_\times^{\prime 2}
\right).
$$

The Euler-Lagrange equations were:

$$
K_T\partial_z^2h_+
-
\frac{K_T}{c^2}\partial_t^2h_+
=
0,
$$

and:

$$
K_T\partial_z^2h_\times
-
\frac{K_T}{c^2}\partial_t^2h_\times
=
0.
$$

Thus plus and cross each obey independent wave equations at free quadratic order.

The script confirmed:

```text
plus mode has independent wave equation;
cross mode has independent wave equation.
```

This is the expected behavior for two linear TT polarizations.

---

## Source Coupling and Driven Wave Equation

The source-coupled action used:

$$
L
=
\frac{K_T}{2c^2}\dot h^2
-
\frac{K_T}{2}h_z^2
+
g_T hS.
$$

The Euler-Lagrange expression was:

$$
K_T\partial_z^2h
-
\frac{K_T}{c^2}\partial_t^2h
+
g_TS
=
0.
$$

Rearranging:

$$
\frac1{c^2}\partial_t^2h
-
\partial_z^2h
=
\frac{g_T}{K_T}S.
$$

Thus the source coupling drives the tensor wave equation, with source strength controlled by:

$$
\frac{g_T}{K_T}.
$$

The script printed the correct Euler-Lagrange expression, but SymPy returned an empty list when solving directly for \(\Box h\). This produced a warning:

```text
[WARN] source coupling drives tensor wave equation
```

This is an implementation/solve-form issue, not a theory failure. The displayed Euler-Lagrange equation visibly contains the expected source term and rearranges directly into the driven wave equation.

---

## Stiffness/Coupling Ratio Controls Normalization

The key target is the far-zone tensor amplitude:

$$
h
\sim
\frac{2G}{c^4R}\ddot Q.
$$

A schematic Green-function solution of the driven wave equation has the form:

$$
h
\sim
\frac{g_T}{K_T}\frac{\text{source}}{R}.
$$

If the source is the quadrupole acceleration:

$$\text{source}\sim\ddot Q,$$

then matching requires:

$$
\frac{g_T}{K_T}
\sim
\frac{2G}{c^4}.
$$

The script identified this as the target tensor coupling/stiffness ratio.

---

## Green Scaling Analogy

The script tested the schematic Green scaling:

$$
h_{\rm green}
=
\frac{g_T}{K_T}\frac{\ddot Q}{R}.
$$

The target is:

$$
h_{\rm target}
=
\frac{2G}{c^4R}\ddot Q.
$$

Solving:

$$h_{\rm green}=h_{\rm target}$$

gives:

$$
\frac{g_T}{K_T}
=
\frac{2G}{c^4}.
$$

The script confirmed:

```text
Green scaling recovers target ratio.
```

This is the main normalization result.

---

## Energy Proxy From Quadratic Action

The Hamiltonian-like quadratic energy proxy from the action is:

$$
E
=
\frac{K_T}{2c^2}
\left(
\dot h_+^2+\dot h_\times^2
\right)
+
\frac{K_T}{2}
\left(
|\nabla h_+|^2+|\nabla h_\times|^2
\right).
$$

The script wrote this as:

$$
E
=
\frac{K_T}{2c^2}
\left[
c^2
\left(
\mathrm{grad}_\times^2+\mathrm{grad}_+^2
\right)
+
\dot h_\times^2+\dot h_+^2
\right].
$$

For:

$$K_T>0,$$

this is positive.

The script confirmed:

```text
quadratic action gives positive energy proxy for K_T>0.
```

This matches the earlier plus/cross quadratic energy-flux structure.

---

## What This Study Established

This study established:

1. A minimal quadratic tensor action gives the wave equation.
2. Plus and cross decouple at free quadratic order.
3. Source coupling gives a driven tensor wave equation.
4. The coupling/stiffness ratio controls amplitude normalization.
5. Matching:
   $$
   h\sim\frac{2G}{c^4R}\ddot Q
   $$
   requires:
   $$
   \frac{g_T}{K_T}\sim\frac{2G}{c^4}.
   $$
6. The quadratic action supplies a positive energy proxy when:
   $$K_T>0.$$

---

## What This Study Did Not Establish

This study did not derive a covariant action.

It did not derive general relativity.

It did not derive the tensor coupling from vacuum microphysics.

It did not derive the exact radiation-energy coefficient.

It did not include gauge constraints beyond the reduced TT setup.

It did not include full spatial dependence or arbitrary propagation directions.

It did not resolve the scalar \(A\) constraint/dynamics question.

It only shows that a reduced tensor-sector action toy can support the desired structural features.

---

## Current Best Interpretation

The current best interpretation is:

```text
A minimal tensor action can support the TT wave equation and provides a
stiffness/coupling interpretation for amplitude normalization.
```

The target ratio is:

$$
\frac{g_T}{K_T}
\sim
\frac{2G}{c^4}.
$$

This is the tensor-sector analogue of earlier scalar normalization work.

The difference is:

```text
scalar A-flux normalization matched the monopole field;
tensor stiffness/coupling normalization targets quadrupole radiation.
```

---

## Implementation Note

The only warning in the run occurred in the source-coupling case.

The script asked SymPy to solve directly for:

$$
\frac1{c^2}h_{tt}-h_{zz}.
$$

SymPy returned no direct solution list, but the printed Euler-Lagrange equation was:

$$
K_T h_{zz}
-
\frac{K_T}{c^2}h_{tt}
+
g_TS
=
0.
$$

This rearranges immediately to:

$$
\frac1{c^2}h_{tt}
-
h_{zz}
=
\frac{g_T}{K_T}S.
$$

So the warning should be treated as a script-solving artifact. A future patch can directly rearrange the expression instead of using `solve`.

---

## Next Development Targets

### 1. Patch the Driven Equation Solve

A small script update could replace the fragile solve step with explicit rearrangement:

```text
Box h = g_T S / K_T
```

### 2. Tensor Flux From Action

A next script could be:

```text
candidate_tensor_flux_from_action.py
```

Purpose:

```text
Use the tensor action normalization to recover the wave-energy flux scaling.
```

### 3. Scalar Constraint Mechanism

A next script could be:

```text
candidate_scalar_constraint_mechanism.py
```

Purpose:

```text
Decide whether A is elliptic/constraint-like rather than propagating in
ordinary radiation zones.
```

### 4. Tensor Action Covariant Parent

A later script could be:

```text
candidate_tensor_action_covariant_parent.py
```

Purpose:

```text
Ask whether the reduced TT action can be embedded in a covariant or
gauge-aware parent structure.
```

---

## Summary

The tensor action/stiffness study gives the first reduced action-side support for the tensor-flux program.

A quadratic action:

$$
L
=
\frac{K_T}{2c^2}\dot h^2
-
\frac{K_T}{2}h_z^2
+
g_T hS
$$

gives a driven wave equation:

$$
\Box h
=
\frac{g_T}{K_T}S.
$$

Matching the target far-zone quadrupole amplitude:

$$
h\sim\frac{2G}{c^4R}\ddot Q
$$

requires:

$$
\frac{g_T}{K_T}\sim\frac{2G}{c^4}.
$$

This is not yet a covariant derivation, but it is a coherent reduced tensor-sector action toy.
