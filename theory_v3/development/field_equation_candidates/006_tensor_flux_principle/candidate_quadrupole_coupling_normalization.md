# Candidate Quadrupole Coupling Normalization

## What This Document Is

This document is a development note for the tensor-flux program.

It is not a derivation of the gravitational-wave amplitude formula, not a tensor action, and not a full radiation theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_quadrupole_coupling_normalization.py
```

The guiding question was:

```text
What normalization should map a changing trace-free quadrupole source into
far-zone h_ij^TT wave amplitude?
```

The answer is a target normalization:

$$
h_{ij}^{TT}
\sim
\frac{2G}{c^4R}\ddot Q_{ij}^{TT}.
$$

This is treated as a target to reproduce, not as a derivation.

The result is important because it separates:

```text
scalar monopole normalization:
  GM/(c²R)

tensor quadrupole amplitude normalization:
  G Qdd/(c⁴R)

tensor radiated-power normalization:
  G Qddd²/c⁵
```

These are related but distinct steps.

---

## Background

The tensor-flux principle established the multi-channel architecture:

```text
A-flux -> scalar monopole channel
h_ij^TT -> tensor quadrupole radiative channel
```

The quadrupole tensor-flux study established the source-side structure:

$$Q_{ij}^{TF}\rightarrow h_{ij}^{TT}.$$

For propagation along \(z\), the plus and cross source projections are:

$$Q_+=\frac{Q_{xx}-Q_{yy}}{2},$$

and:

$$Q_\times=Q_{xy}.$$

The next question is the coefficient relating the quadrupole motion to the far-zone wave amplitude.

---

## Target Far-Zone Amplitude Law

The target far-zone relation is:

$$
h_{ij}^{TT}
\sim
C_Q\ddot Q_{ij}^{TT}.
$$

The GR-like weak far-zone coefficient is:

$$
C_Q=\frac{2G}{c^4R},
$$

where \(R\) is the distance to the observer.

Therefore:

$$
h_+
=
\frac{2G}{c^4R}\ddot Q_+,
$$

and:

$$
h_\times
=
\frac{2G}{c^4R}\ddot Q_\times.
$$

The script stated this normalization directly and treated it as the target.

It did not derive the coefficient from a tensor action.

---

## Rotating Quadrupole Scaling

The script used a rotating quadrupole proxy:

$$Q_+(t)=Q_0\cos(2\Omega t),$$

and:

$$Q_\times(t)=Q_0\sin(2\Omega t).$$

Then:

$$\ddot Q_+=-4\Omega^2Q_0\cos(2\Omega t),$$

and:

$$\ddot Q_\times=-4\Omega^2Q_0\sin(2\Omega t).$$

Using:

$$h=\frac{2G}{c^4R}\ddot Q,$$

gives:

$$
h_+
=
-\frac{8G\Omega^2Q_0}{c^4R}\cos(2\Omega t),
$$

and:

$$
h_\times
=
-\frac{8G\Omega^2Q_0}{c^4R}\sin(2\Omega t).
$$

The squared amplitude sum is:

$$
h_+^2+h_\times^2
=
\frac{64G^2\Omega^4Q_0^2}{R^2c^8}.
$$

Thus the tensor amplitude scales as:

$$
h\sim\frac{G\Omega^2Q_0}{c^4R}.
$$

The script confirmed this scaling.

---

## Dimensional Consistency

The dimensions are:

```text
[G] = L³ / (M T²)
[Q] = M L²
[Qdd] = M L² / T²
[c⁴ R] = L⁵ / T⁴
```

Therefore:

$$
\left[
\frac{G\ddot Q}{c^4R}
\right]
=
\frac{L^3}{MT^2}
\frac{ML^2}{T^2}
\frac{T^4}{L^5}
=
1.
$$

So the far-zone strain amplitude is dimensionless, as required.

This is a sanity check, not a derivation.

---

## Amplitude Versus Power Normalization

The script kept the amplitude and power normalizations distinct.

The second-derivative amplitude-source proxy is:

$$
\ddot Q_+^2+\ddot Q_\times^2
=
16\Omega^4Q_0^2.
$$

The third-derivative power-source proxy is:

$$
\dddot Q_+^2+\dddot Q_\times^2
=
64\Omega^6Q_0^2.
$$

A GR-like power proxy uses a coefficient of the form:

$$
\frac{G}{5c^5}.
$$

So the schematic power proxy is:

$$
P\sim
\frac{64G\Omega^6Q_0^2}{5c^5}.
$$

Interpretation:

```text
Amplitude normalization uses G/c⁴.
Power normalization uses G/c⁵.
They are related but not the same step.
```

This distinction must be preserved in future tensor-radiation work.

---

## Scalar Versus Tensor Normalization

The scalar monopole amplitude at distance \(R\) is:

$$
\delta A
\sim
-\frac{2GM}{c^2R}.
$$

The tensor quadrupole amplitude is:

$$
h_{TT}
\sim
\frac{2G\ddot Q}{c^4R}.
$$

Thus:

```text
scalar mass channel uses GM/(c²R);
tensor quadrupole channel uses GQdd/(c⁴R).
```

This confirms that the scalar and tensor couplings are distinct.

The tensor channel should not be normalized by reusing the scalar \(A\)-flux coefficient blindly.

---

## What This Study Established

This study established:

1. A GR-like far-zone tensor amplitude has coefficient:
   $$
   \frac{2G}{c^4R}.
   $$

2. This coefficient is dimensionally consistent.

3. Rotating quadrupole amplitudes scale as:
   $$
   \Omega^2Q_0.
   $$

4. Radiated-power proxies scale as:
   $$
   \Omega^6Q_0^2.
   $$

5. Scalar monopole normalization:
   $$
   \frac{GM}{c^2R}
   $$
   is distinct from tensor quadrupole normalization:
   $$
   \frac{G\ddot Q}{c^4R}.
   $$

6. The coefficient is a target normalization, not yet derived.

---

## What This Study Did Not Establish

This study did not derive the coefficient:

$$\frac{2G}{c^4R}.$$

It did not derive a tensor action.

It did not derive a tensor stiffness parameter.

It did not derive the far-zone approximation.

It did not derive the radiation power formula.

It did not derive energy flux from first principles.

It only identified the normalization a successful tensor-flux theory should reproduce.

---

## Current Best Interpretation

The current best interpretation is:

```text
The tensor-flux theory now has a target amplitude normalization.

A successful tensor action or tensor-stiffness model should reproduce:

  h_ij^TT ~ (2G/(c⁴R)) Qdd_ij^TT.
```

This is analogous to how the scalar \(A\)-flux branch had to reproduce:

$$
F_A=\frac{8\pi GM}{c^2}.
$$

But the scalar and tensor coefficients are different because they map different source moments into different field sectors.

---

## Next Development Targets

### 1. Tensor Radiation Energy Flux

A direct next script:

```text
candidate_tensor_radiation_energy_flux.py
```

Purpose:

```text
Connect plus/cross wave amplitudes to a quadratic energy-flux proxy and
compare it with the third-derivative quadrupole power scaling.
```

### 2. Tensor Action / Stiffness

A later script:

```text
candidate_tensor_action_stiffness.py
```

Purpose:

```text
Ask whether the target 2G/(c⁴R) coefficient can arise from a tensor-field
action with a stiffness parameter.
```

### 3. No Unwanted Scalar Radiation

A later script:

```text
candidate_no_unwanted_scalar_radiation.py
```

Purpose:

```text
Check that the scalar A channel does not produce forbidden large scalar
radiation from binaries.
```

---

## Summary

The quadrupole coupling normalization study establishes the target far-zone tensor amplitude scaling:

$$
h_{ij}^{TT}
\sim
\frac{2G}{c^4R}\ddot Q_{ij}^{TT}.
$$

For a rotating quadrupole:

$$
h\sim
\frac{G\Omega^2Q_0}{c^4R}.
$$

Radiated-power proxies scale instead as:

$$
\frac{G\Omega^6Q_0^2}{c^5}.
$$

This keeps amplitude normalization and power normalization distinct.

The next step is tensor radiation energy flux.
