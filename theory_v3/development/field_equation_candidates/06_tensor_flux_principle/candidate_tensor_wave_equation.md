# Candidate Tensor Wave Equation

## What This Document Is

This document is a development note for the tensor-flux program.

It is not a full theory of gravitational radiation, not a postulate, and not a covariant derivation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_tensor_wave_equation.py
```

The guiding question was:

```text
Once the transverse-traceless tensor basis is defined, can it support a
minimal linear wave equation with plus/cross polarizations?
```

The answer is yes.

The TT tensor sector can support the vacuum wave equation:

$$\Box h_{ij}^{TT}=0.$$

Plane-wave plus and cross modes satisfy this equation when:

$$\omega^2=c^2k^2.$$

The trace-free and transverse constraints are preserved during propagation.

This is the first constructive tensor-wave result in the tensor-flux program.

---

## Background

The scalar-flux no-wave failure control established that scalar \(A\)-flux cannot produce gravitational waves.

The tensor-flux basis study then defined the minimal TT basis for a wave propagating along \(z\):

$$
e_+
=
\begin{pmatrix}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 0
\end{pmatrix},
$$

and:

$$
e_\times
=
\begin{pmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

A general TT tensor wave is:

$$h_{ij}^{TT}=h_+e_+ + h_\times e_\times.$$

The present study asks whether this TT sector can propagate as a wave.

---

## Plane-Wave TT Tensor

The script used:

$$h_+(t,z)=H_+\cos(kz-\omega t),$$

and:

$$h_\times(t,z)=H_\times\cos(kz-\omega t).$$

Then:

$$
H_{TT}
=
\begin{pmatrix}
H_+\cos(kz-\omega t) & H_\times\cos(kz-\omega t) & 0 \\
H_\times\cos(kz-\omega t) & -H_+\cos(kz-\omega t) & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

This is the standard plus/cross TT structure for propagation along \(z\).

---

## Wave Operator on Polarizations

The script used the wave operator:

$$\Box=\frac1{c^2}\partial_t^2-\partial_z^2.$$

For the plus mode:

$$\Box h_+
=
\frac{H_+}{c^2}(c^2k^2-\omega^2)\cos(kz-\omega t).
$$

For the cross mode:

$$\Box h_\times
=
\frac{H_\times}{c^2}(c^2k^2-\omega^2)\cos(kz-\omega t).
$$

Both vanish when:

$$\omega^2=c^2k^2.$$

Equivalently:

$$\omega=ck$$

for positive frequency and wavenumber.

The script confirmed that plus and cross have the same wave dispersion coefficient:

$$k^2-\frac{\omega^2}{c^2}.$$

---

## Wave Operator on the Full Tensor

The full TT tensor wave satisfies:

$$\Box H_{TT}=0$$

component by component when:

$$\omega^2=c^2k^2.$$

The script showed that every nonzero component of:

$$\Box H_{TT}$$

is proportional to:

$$c^2k^2-\omega^2.$$

Therefore the full TT tensor wave vanishes on the dispersion relation.

This confirms that the tensor-basis object is compatible with a minimal linear wave equation.

---

## TT Conditions Are Preserved

The trace of the tensor is:

$$\mathrm{Tr}(H_{TT})=0.$$

For wave vector:

$$k^i=(0,0,k),$$

transversality requires:

$$k^iH_{ij}=0.$$

The script confirmed:

$$k^iH_{ij}^{TT}=0.$$

These conditions hold for all \(t\) and \(z\).

Therefore the wave equation does not spoil the TT constraints for this plane wave.

This is important because the tensor sector must propagate without leaking into scalar trace or longitudinal modes.

---

## Quadratic Energy Proxy

The script also formed a simple positive quadratic diagnostic:

$$E_{\rm proxy}
\sim
\frac{\dot h_+^2+\dot h_\times^2}{c^2}
+
h_+^{\prime 2}
+
h_\times^{\prime 2}.
$$

For the plane wave, this becomes:

$$
E_{\rm proxy}
=
\frac{
H_\times^2\omega^2
+
H_+^2\omega^2
+
c^2k^2(H_\times^2+H_+^2)
}{c^2}
\sin^2(kz-\omega t).
$$

This is quadratic in both tensor polarizations.

Caution:

```text
This is only a positive quadratic diagnostic.
It is not a derived GR stress tensor or radiation flux.
```

The result is still useful because it shows the tensor branch admits a natural wave-energy-like quadratic quantity.

---

## Scalar A Remains Separate

The script explicitly separated the scalar and tensor channels.

Scalar channel:

```text
A = 1 + 2 Phi/c²
mass / density source
monopole and weak scalar multipoles
```

Tensor channel:

```text
h_ij^TT
plus/cross polarizations
quadrupole/radiative source candidate
```

The tensor wave equation is not supplied by scalar \(A\).

This preserves the failure-control result:

```text
A-flux is not secretly the wave sector.
```

The tensor wave equation is a separate sector.

---

## What This Study Established

This study established:

1. Plus and cross amplitudes can satisfy a linear wave equation.
2. The dispersion relation is:
   $$\omega^2=c^2k^2.$$
3. The full \(h_{ij}^{TT}\) tensor satisfies:
   $$\Box h_{ij}^{TT}=0$$
   component by component.
4. Trace-free and transverse constraints are preserved.
5. A quadratic energy proxy can be formed from plus/cross derivatives.
6. This is a tensor sector, not scalar \(A\)-flux.

---

## What This Study Did Not Establish

This study did not derive the tensor wave equation from a covariant action.

It did not derive the source term.

It did not derive quadrupole radiation.

It did not compute real gravitational-wave power.

It did not prove that the tensor sector emerges from the vacuum ontology.

It did not connect the tensor sector to binary inspiral observations.

It only showed that a minimal TT tensor sector can support linear plane waves with the expected two-polarization structure and speed \(c\).

---

## Current Best Interpretation

The current best interpretation is:

```text
The tensor sector can support a minimal linear wave equation.

This makes h_ij^TT a viable candidate carrier of quadrupole radiative
vacuum response.

A remains the scalar/monopole channel.
h_ij^TT becomes the tensor/radiative channel.
```

This supports the emerging architecture:

```text
A-flux:
  monopole scalar flow

W_i:
  vector current / frame-dragging flow

h_ij^TT:
  tensor quadrupole radiation flow
```

---

## Next Development Targets

### 1. Quadrupole Tensor Flux

A direct next script:

```text
candidate_quadrupole_tensor_flux.py
```

Purpose:

```text
Connect h_ij^TT to trace-free quadrupole source structure.
```

### 2. Tensor Flux Principle

A later note:

```text
candidate_tensor_flux_principle.md
```

Purpose:

```text
State the analogy between scalar A-flux as monopole flow and tensor TT
radiation as quadrupole flow.
```

### 3. Wave Energy / Radiation Proxy

A later script:

```text
candidate_tensor_radiation_energy_flux.py
```

Purpose:

```text
Develop a more meaningful tensor energy flux proxy and compare with the
expected quadratic plus/cross structure.
```

---

## Summary

The tensor wave equation study gives the first constructive propagation result for the tensor-flux program.

The TT tensor:

$$h_{ij}^{TT}=h_+e_+ + h_\times e_\times$$

supports the wave equation:

$$\Box h_{ij}^{TT}=0.$$

Plane waves:

$$h_+=H_+\cos(kz-\omega t),$$

and:

$$h_\times=H_\times\cos(kz-\omega t)$$

propagate when:

$$\omega^2=c^2k^2.$$

The trace-free and transverse conditions are preserved.

This does not yet derive radiation from sources, but it establishes the propagation side of the tensor channel.

The next question is how quadrupole source structure feeds \(h_{ij}^{TT}\).
