# Candidate Covariant Parent Modes

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full covariant field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the exploratory parent-mode study performed in:

```text
candidate_covariant_parent_modes.py
```

The script tested whether the reduced exterior variables \(\kappa\) and \(s\) can be interpreted as shadows of more general geometric modes.

The result is a working hypothesis:

```text
kappa is the reduced trace / conformal / determinant-like mode
of the temporal-radial exterior sector.

s is the reduced trace-free / shear mode that remains when
the source-free exterior suppresses kappa.
```

This is not yet a covariant definition. It is a reduced-sector interpretation that guides the next stage of development.

---

## Background

The reduced exterior mode program uses:

$$a=\ln A,$$

and:

$$b=\ln B.$$

Then:

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

Thus:

$$\kappa=0 \quad \Longleftrightarrow \quad AB=1.$$

When:

$$\kappa=0,$$

we have:

$$A=e^s,$$

and:

$$B=e^{-s}.$$

The exterior can then carry nonzero compensated distortion \(s\) while preserving reciprocal scaling.

The open question is:

```text
What are kappa and s shadows of in the full metric?
```

---

## Reduced Two-Sector Decomposition

The simplest reduced mode vector is:

$$v=\begin{pmatrix}a\\b\end{pmatrix}.$$

Using the definitions of \(\kappa\) and \(s\), we can write:

$$v=\kappa\begin{pmatrix}1\\1\end{pmatrix}+s\begin{pmatrix}1\\-1\end{pmatrix}.$$

That is:

$$\begin{pmatrix}a\\b\end{pmatrix} =
\kappa
\begin{pmatrix}1\\1\end{pmatrix}
+
s
\begin{pmatrix}1\\-1\end{pmatrix}.
$$

The two basis directions are orthogonal in the toy two-mode space:

$$\begin{pmatrix}1\\1\end{pmatrix}
\cdot
\begin{pmatrix}1\\-1\end{pmatrix}
=0.$$

This supports the reduced interpretation:

```text
kappa = trace-like direction
s     = shear-like direction
```

In this reduced two-sector algebra, \(\kappa\) is the common-mode distortion of \(a\) and \(b\), while \(s\) is the opposing-mode distortion.

---

## 3+1 Isotropic Spatial Reduction

The script also tested a 3+1 pre-mode reduction.

Let:

$$a=q_t,$$

and define the spatial average:

$$b=\frac{q_x+q_y+q_z}{3}.$$

Then:

$$\kappa=\frac{1}{2}\left(q_t+\frac{q_x+q_y+q_z}{3}\right),$$

and:

$$s=\frac{1}{2}\left(q_t-\frac{q_x+q_y+q_z}{3}\right).$$

The isotropic time-vs-space exchange direction:

$$\delta(q_t,q_x,q_y,q_z)=(-S,S,S,S)$$

gives:

$$\delta a=-S,$$

and:

$$\delta b=S.$$

Therefore:

$$\delta\kappa=\frac{\delta a+\delta b}{2}=0,$$

while:

$$\delta s=\frac{\delta a-\delta b}{2}=-S.$$

So this exchange lies in the \(\kappa\)-kernel and excites only the shear mode.

This supports the same reduced interpretation:

```text
trace/conformal imbalance is not excited,
but compensated time-vs-space shear is excited.
```

This is consistent with the earlier trace-kernel experiments, but now framed in parent-mode language.

---

## Linearized Trace Comparison

The script compared the reduced log modes to a simple linearized metric perturbation around Minkowski spacetime.

Use signature:

$$(-,+,+,+).$$

For the reduced diagonal sector:

$$g_{tt}=-e^a,$$

and:

$$g_{rr}=e^b.$$

Let:

$$a=\epsilon a_1,$$

and:

$$b=\epsilon b_1,$$

with \(\epsilon\) small.

Then to first order:

$$h_{tt}=-(e^{\epsilon a_1}-1)\approx-\epsilon a_1,$$

and:

$$h_{rr}=e^{\epsilon b_1}-1\approx\epsilon b_1.$$

The reduced temporal-radial trace contribution is:

$$-h_{tt}+h_{rr}.$$

Substituting gives:

$$-h_{tt}+h_{rr}=\epsilon(a_1+b_1).$$

But:

$$\kappa=\frac{\epsilon(a_1+b_1)}{2}.$$

Therefore:

$$-h_{tt}+h_{rr}=2\kappa.$$

This supports interpreting \(\kappa\) as half the reduced linearized trace contribution in the temporal-radial sector.

This is a useful clue, not a full covariant definition.

---

## Trace-Free Shear Check

For pure reduced shear, set:

$$\kappa=0.$$

Then:

$$a=s,$$

and:

$$b=-s.$$

In the linearized notation:

$$a=\epsilon s,$$

and:

$$b=-\epsilon s.$$

Then the first-order perturbations are:

$$h_{tt}\approx-\epsilon s,$$

and:

$$h_{rr}\approx-\epsilon s.$$

The reduced trace contribution is:

$$-h_{tt}+h_{rr}=0.$$

So pure reduced shear is trace-free to first order.

This supports interpreting \(s\) as the reduced trace-free temporal-radial shear mode.

---

## Determinant / Volume Caution

In static spherical areal-radius form:

$$ds^2=-A(r)c^2dt^2+B(r)dr^2+r^2d\Omega^2.$$

The determinant magnitude is:

$$|g|=A B r^4\sin^2\theta.$$

Therefore:

$$\sqrt{|g|}=\sqrt{AB}\,r^2\sin\theta.$$

Since:

$$AB=e^{2\kappa},$$

we have:

$$\sqrt{AB}=e^\kappa.$$

So:

$$\sqrt{|g|}=e^\kappa r^2\sin\theta.$$

Thus \(\kappa\) controls the temporal-radial determinant factor in areal-radius gauge.

This is important, but it must not be overinterpreted.

In areal-radius coordinates, the angular sector is fixed as:

$$r^2d\Omega^2.$$

Therefore \(\kappa\) controls the temporal-radial determinant factor in this gauge, not a fully coordinate-independent volume mode by itself.

A covariant parent must handle gauge and coordinate dependence carefully.

---

## Working Parent Interpretation

The current working interpretation is:

```text
kappa:
  reduced trace / conformal / determinant-like mode
  controls AB = exp(2 kappa)
  equals half the temporal-radial linearized trace contribution
  controls sqrt(|g|)'s temporal-radial factor in areal gauge

s:
  reduced trace-free temporal-radial shear mode
  preserves AB when kappa = 0
  carries compensated exterior distortion
```

In compact form:

$$\kappa \sim \text{reduced trace/conformal mode},$$

and:

$$s \sim \text{reduced trace-free/shear mode}.$$

The source-free exterior result:

$$\kappa=0,\qquad s\neq0$$

can then be interpreted as:

```text
the source-free exterior suppresses the reduced trace/conformal imbalance,
while allowing trace-free compensated shear.
```

---

## Relationship to the Reduced Exterior Action

The candidate reduced exterior action used:

$$L =
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
+
\alpha\rho s.$$

The parent-mode interpretation clarifies the meaning of this toy action.

The \(\kappa\) sector penalizes reduced trace/conformal imbalance:

$$K_\kappa|\nabla\kappa|^2+M_\kappa^2\kappa^2.$$

The \(s\) sector allows the trace-free shear mode to carry the exterior field:

$$K_s|\nabla s|^2+\alpha\rho s.$$

So the reduced action says, in parent-mode language:

```text
the source-free exterior resists trace/conformal imbalance,
while mass sources the trace-free shear channel.
```

This is still a reduced toy. The next challenge is to identify the corresponding covariant or gauge-aware structure.

---

## Relationship to the Slogan

The current slogan is:

```text
Gravity is the compensated shear left after the source-free vacuum suppresses imbalance.
```

In reduced mathematical language:

```text
imbalance = kappa
compensated shear = s
```

So:

$$\kappa=0$$

and:

$$s\neq0$$

is the reduced expression of that slogan.

The more formal version is:

```text
In the reduced exterior model, the vacuum suppresses the uncompensated mode kappa,
while mass sources the compensated shear mode s.
```

---

## What This Study Established

The parent-mode study established the following reduced results:

1. \([a,b]\) decomposes cleanly into a trace-like direction and a shear-like direction.
2. \(\kappa\) multiplies the trace-like direction \([1,1]\).
3. \(s\) multiplies the shear-like direction \([1,-1]\).
4. In a 3+1 isotropic spatial reduction, \((-S,S,S,S)\) excites \(s\) but not \(\kappa\).
5. In the reduced linearized temporal-radial sector, the trace contribution is \(2\kappa\).
6. Pure reduced shear is trace-free to first order.
7. In areal-radius gauge, \(\kappa\) controls the temporal-radial determinant factor.
8. \(\kappa\) and \(s\) are therefore good reduced parent-mode candidates.

---

## What This Study Did Not Establish

This study did not identify a fully covariant field variable.

It did not solve the gauge problem.

It did not prove that \(\kappa\) is a scalar invariant.

It did not prove that \(s\) is a covariant shear tensor component.

It did not generalize to arbitrary spacetimes.

It did not address nonspherical perturbations, rotating sources, time-dependent metrics, gravitational waves, or cosmology.

It did not derive the reduced exterior action from a covariant action.

It only supports a working reduced interpretation.

---

## The Main Caution

The main caution is coordinate dependence.

The variables \(\kappa\) and \(s\) are cleanly defined in the static spherical reduced sector, but they are not yet covariant objects.

In particular:

$$\sqrt{|g|}=e^\kappa r^2\sin\theta$$

holds in areal-radius gauge, where the angular sector is fixed.

A different coordinate choice may redistribute metric information between radial and angular components.

Therefore the next stage must not assume that \(\kappa\) itself is an invariant scalar.

Instead, the next stage should search for a gauge-aware or covariant decomposition whose static spherical reduction gives \(\kappa\) and \(s\).

---

## Next Development Target

The next development target is:

```text
Find a gauge-aware or covariant decomposition of metric variations
whose static spherical reduction gives kappa and s.
```

Possible directions include:

1. Trace / trace-free decomposition of metric perturbations.
2. ADM or 3+1 decomposition into lapse, spatial metric, trace, and shear components.
3. Decomposition relative to a preferred static observer congruence.
4. Areal-gauge reduction with explicit gauge limitations.
5. Conformal decomposition of spatial metric plus lapse response.
6. Comparison with scalar/vector/tensor perturbation theory.
7. Search for a covariant object whose reduced temporal-radial determinant factor becomes \(e^\kappa\).
8. Search for a shear-like tensor mode whose static spherical projection becomes \(s\).

A useful next script could be:

```text
candidate_gauge_dependence_modes.py
```

Its purpose would be to test how \(\kappa\) and \(s\) transform under simple radial coordinate changes.

This would help distinguish physical mode content from coordinate artifacts.

---

## Summary

The candidate parent-mode study supports the working hypothesis:

$$\kappa \rightarrow \text{reduced trace/conformal/determinant-like mode},$$

and:

$$s \rightarrow \text{reduced trace-free/shear mode}.$$

In the reduced static exterior sector:

$$\kappa=0$$

means reciprocal scaling:

$$AB=1.$$

The remaining mode:

$$s\neq0$$

carries compensated exterior distortion.

This supports the reduced picture:

```text
gravity is compensated shear left after the source-free vacuum suppresses imbalance.
```

The next step is not to treat \(\kappa\) and \(s\) as covariant fields immediately.

The next step is to find their gauge-aware or covariant parent structure.
