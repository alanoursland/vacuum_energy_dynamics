# Candidate Tensor Radiation Energy Flux

## What This Document Is

This document is a development note for the tensor-flux program.

It is not a derivation of gravitational-wave energy flux, not a covariant stress tensor, and not a complete radiation theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_tensor_radiation_energy_flux.py
```

The guiding question was:

```text
Does the tensor branch connect the far-zone amplitude scaling
h ~ 2G Qdd/(c^4 R) to the expected radiated-power scaling
P ~ G Qddd²/c^5?
```

The answer is yes at the scaling level.

The run confirms:

```text
TT flux is quadratic in hdot_plus and hdot_cross.
Substituting h ~ 2G Qdd/(c^4 R) gives flux scaling
F ~ G Omega^6 Q0²/(R² c^5).
Multiplying by area gives total power scaling
P ~ G Omega^6 Q0²/c^5.
This matches the Qdddot² power-scaling class.
```

Important caution:

```text
Numerical coefficients are not derived here.
```

The run produced one warning because two cases used different numerical coefficient conventions for the same scaling proxy. That is not a conceptual failure; it is a normalization bookkeeping issue. The safe claim is the scaling class, not the exact coefficient.

---

## Background

The tensor-flux program has established the following sequence:

1. Scalar \(A\)-flux cannot produce tensor gravitational waves.
2. A tensor \(h_{ij}^{TT}\) sector is needed.
3. Plus/cross TT modes provide the two tensor polarizations.
4. The TT sector supports a vacuum wave equation:
   $$\Box h_{ij}^{TT}=0.$$
5. Trace-free quadrupole structure projects onto plus/cross channels.
6. The target amplitude normalization is:
   $$h_{ij}^{TT}\sim\frac{2G}{c^4R}\ddot Q_{ij}^{TT}.$$

The present study asks whether this amplitude scaling leads to the expected energy-flux / power scaling.

---

## Target Flux Proxy

The target TT wave energy-flux proxy is:

$$
F_{TT}
\sim
\frac{c^3}{32\pi G}
\left\langle
\dot h_+^2+\dot h_\times^2
\right\rangle.
$$

This has the expected structure:

```text
quadratic in wave time derivatives,
quadratic in plus/cross polarizations,
scaled by c³/G.
```

This expression is used as a target proxy.

It is not derived in this script.

---

## Plus/Cross Wave Flux Proxy

For wave amplitudes \(H_+\) and \(H_\times\), the averaged derivative squares are:

$$
\langle \dot h_+^2\rangle=\frac12H_+^2\omega^2,
$$

and:

$$
\langle \dot h_\times^2\rangle=\frac12H_\times^2\omega^2.
$$

Therefore:

$$
F
=
\frac{c^3\omega^2}{64\pi G}
\left(
H_+^2+H_\times^2
\right).
$$

The script confirmed:

```text
plus/cross flux proxy is quadratic in amplitudes.
```

This is the correct structural behavior for a tensor wave energy-flux proxy.

---

## Substitute Quadrupole Amplitude Normalization

The quadrupole coupling normalization target is:

$$
h
\sim
\frac{2G}{c^4R}\ddot Q.
$$

For the rotating quadrupole proxy:

$$Q_+=Q_0\cos(2\Omega t),$$

and:

$$Q_\times=Q_0\sin(2\Omega t),$$

we have:

$$|\ddot Q|\sim 4\Omega^2Q_0.$$

Thus the wave amplitude scale is:

$$
H
=
\frac{8G\Omega^2Q_0}{c^4R}.
$$

The wave frequency is:

$$\omega=2\Omega.$$

Substituting into the flux proxy gives:

$$
F_{TT}
\sim
\frac{G\Omega^6Q_0^2}{R^2c^5}.
$$

The run gave:

$$
F_{TT}
=
\frac{8G\Omega^6Q_0^2}{\pi R^2c^5}
$$

in Case 2.

A later comparison case used:

$$
F
=
\frac{4G\Omega^6Q_0^2}{\pi R^2c^5}.
$$

This produced a warning in the script because the expected coefficient did not match the computed coefficient.

Interpretation:

```text
The scaling is correct.
The numerical coefficient is not settled in this reduced proxy.
```

This is acceptable for this stage because the script explicitly says it is a scaling diagnostic, not a derivation of the exact angular-pattern coefficient.

---

## Total Power Scaling

Radiation flux through a sphere scales like:

$$P\sim4\pi R^2F.$$

Since:

$$F\sim\frac{G\Omega^6Q_0^2}{R^2c^5},$$

the total power scales as:

$$P\sim\frac{G\Omega^6Q_0^2}{c^5}.$$

The observer radius cancels.

The script confirmed:

```text
total power scaling cancels observer radius R;
power scales as G Omega^6 Q0²/c^5.
```

This is the central result.

---

## Compare to Third-Derivative Quadrupole Proxy

The quadrupole third-derivative proxy is:

$$
\dddot Q_+^2+\dddot Q_\times^2
=
64\Omega^6Q_0^2.
$$

A GR-like power scaling has the form:

$$
P
\sim
\frac{G}{5c^5}
\left\langle
\dddot Q_{ij}\dddot Q_{ij}
\right\rangle.
$$

The script confirmed that the power proxy uses:

$$
\frac{G}{c^5}\dddot Q^2.
$$

Thus the tensor radiation energy-flux proxy connects correctly to the third-derivative quadrupole scaling class.

---

## No-Radiation Controls

The script checked two no-radiation controls.

For a static quadrupole:

$$Q=Q_0,$$

we have:

$$\dddot Q=0.$$

For a linearly changing quadrupole:

$$Q=Q_0+Vt,$$

we also have:

$$\dddot Q=0.$$

The script confirmed:

```text
static quadrupole has no power proxy;
linearly changing quadrupole has no third-derivative power proxy.
```

This is a useful guardrail: not every nonzero quadrupole radiates.

Radiation is tied to sufficiently time-varying quadrupole structure.

---

## Scalar and Tensor Radiation Distinction

The script explicitly keeps scalar and tensor channels separate.

Scalar \(A\) channel:

```text
monopole/static Newtonian response;
not the TT radiation channel.
```

Tensor \(h_{ij}^{TT}\) channel:

```text
plus/cross polarizations;
quadrupole time variation;
energy flux quadratic in hdot.
```

A viable theory must avoid large unwanted scalar radiation.

This motivates the next guardrail script:

```text
candidate_no_unwanted_scalar_radiation.py
```

---

## What This Study Established

This study established:

1. The TT wave flux proxy is quadratic in:
   $$\dot h_+,$$
   and:
   $$\dot h_\times.$$

2. Substituting:
   $$h\sim\frac{2G\ddot Q}{c^4R}$$
   gives:
   $$F\sim\frac{G\Omega^6Q_0^2}{R^2c^5}.$$

3. Multiplying by area gives:
   $$P\sim\frac{G\Omega^6Q_0^2}{c^5}.$$

4. This matches the:
   $$\frac{G}{c^5}\dddot Q^2$$
   scaling class.

5. Static and linearly changing quadrupoles do not radiate in this proxy.

6. Scalar \(A\) remains separate from tensor radiation.

---

## What This Study Did Not Establish

This study did not derive the exact numerical radiation coefficient.

It did not derive a gravitational-wave stress tensor.

It did not derive angular radiation patterns.

It did not derive radiation reaction.

It did not derive the tensor action or stiffness.

It did not prove equivalence to GR’s quadrupole formula.

It only established scaling consistency.

---

## Coefficient Warning

The run produced one warning:

```text
[WARN] flux scales as G Omega^6 Q0^2/(R^2 c^5)
```

This happened because Case 2 computed a coefficient of:

$$
\frac{8G\Omega^6Q_0^2}{\pi R^2c^5},
$$

while the expected expression in the script used:

$$
\frac{4G\Omega^6Q_0^2}{\pi R^2c^5}.
$$

This should be fixed in the script by aligning the expected coefficient with the chosen assumptions about plus/cross amplitudes and averaging.

The physics conclusion is unchanged:

```text
the scaling class is correct;
the exact coefficient is not derived here.
```

---

## Current Best Interpretation

The current best interpretation is:

```text
The tensor-flux branch now has:
  TT basis,
  wave propagation,
  quadrupole source structure,
  target amplitude normalization,
  radiation-power scaling.

It still lacks:
  exact coefficient derivation,
  tensor action/stiffness,
  angular pattern integration,
  no-unwanted-scalar-radiation proof.
```

---

## Next Development Targets

### 1. No Unwanted Scalar Radiation

A direct next script:

```text
candidate_no_unwanted_scalar_radiation.py
```

Purpose:

```text
Ensure the scalar A channel does not predict large scalar radiation from
binary systems.
```

### 2. Tensor Radiation Coefficient Cleanup

A later script or patch:

```text
candidate_tensor_radiation_coefficient_cleanup.py
```

Purpose:

```text
Align plus/cross amplitudes, averaging conventions, angular pattern factors,
and total-power coefficients.
```

### 3. Tensor Action / Stiffness

A later script:

```text
candidate_tensor_action_stiffness.py
```

Purpose:

```text
Try to derive the amplitude and flux coefficients from a tensor-field action.
```

---

## Summary

The tensor radiation energy-flux study passes at the scaling level.

Using:

$$
h\sim\frac{2G\ddot Q}{c^4R},
$$

and:

$$
F_{TT}
\sim
\frac{c^3}{32\pi G}
\left\langle
\dot h_+^2+\dot h_\times^2
\right\rangle,
$$

gives:

$$
P\sim\frac{G}{c^5}\dddot Q^2.
$$

This is the expected tensor-radiation scaling class.

The numerical coefficient remains a future normalization problem.

The next guardrail is to ensure scalar \(A\) does not produce forbidden large scalar radiation.
