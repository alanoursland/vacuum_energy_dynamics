# Field Equation Set — Current Reconstruction Status

## Scope

This document presents the current field-equation architecture as if it were a candidate finished system, while explicitly marking incomplete or unknown pieces.

Audience: GR / relativistic field theory readers.

Status labels:

```text
DERIVED_REDUCED
CONSTRAINED
STRUCTURAL
UNKNOWN
UNFINISHED
PHENOMENOLOGICAL_IF_USED
```

---

# 1. Variables and Sector Split

Current field variables:

\[
A
\]

scalar lapse / static mass-response field.

\[
\kappa
\]

trace / volume / interior response candidate.

\[
W_i
\]

vector current / frame-dragging candidate.

\[
h_{ij}^{TT}
\]

transverse-traceless tensor radiation field.

Auxiliary or controlled scalar-radiative variable:

\[
A_{\rm rad}
\]

scalar breathing/radiative hazard; not an ordinary active long-range degree of freedom unless a suppression/relaxation mechanism is specified.

Current weak-field recombination map:

\[
g_{tt}\sim -A c^2,
\]

\[
g_{ti}\sim W_i,
\]

\[
g_{ij}\sim \text{scalar trace/}\kappa\text{ sector}+h_{ij}^{TT}.
\]

Status:

```text
STRUCTURAL / UNFINISHED
```

The recombination map is not yet a covariant parent derivation.

---

# 2. Scalar Static / Monopole Sector

## 2.1 Areal-Flux Law

Primary reduced scalar equation:

\[
\Delta_{\rm areal}A =
\frac{8\pi G}{c^2}\rho.
\]

where:

\[
\Delta_{\rm areal}A =
\frac{1}{r^2}\frac{d}{dr}
\left(
r^2\frac{dA}{dr}
\right).
\]

Equivalent flux form:

\[
F_A(r)=4\pi r^2 A'(r),
\]

\[
\frac{dF_A}{dr} =
4\pi r^2
\frac{8\pi G}{c^2}\rho(r).
\]

With:

\[
M_{\rm enc}'(r)=4\pi r^2\rho(r),
\]

this gives:

\[
F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).
\]

Status:

```text
DERIVED_REDUCED
```

This is the strongest reconstructed sector.

---

## 2.2 Exterior Vacuum Scalar Equation

For:

\[
\rho=0,
\]

\[
\Delta_{\rm areal}A=0.
\]

Thus:

\[
\frac{d}{dr}\left(r^2A'\right)=0,
\]

and:

\[
A(r)=C_0+\frac{C_1}{r}.
\]

Asymptotic flatness:

\[
C_0=1.
\]

Flux normalization by total mass \(M\):

\[
4\pi r^2A'=\frac{8\pi GM}{c^2}.
\]

Therefore:

\[
A(r)=1-\frac{2GM}{c^2r}.
\]

Status:

```text
DERIVED_REDUCED
```

---

## 2.3 Reciprocal Exterior Radial Factor

In the static spherical exterior, impose:

\[
\kappa=0.
\]

With the areal-gauge relation:

\[
AB=e^{2\kappa},
\]

this gives:

\[
AB=1,
\]

so:

\[
B=\frac{1}{A}.
\]

Therefore:

\[
B(r)=\left(1-\frac{2GM}{c^2r}\right)^{-1}.
\]

Status:

```text
DERIVED_REDUCED / GAUGE-CONDITIONED
```

This recovers the Schwarzschild exterior metric factors in the static spherical sector.

---

# 3. Weak Multipole Scalar Extension

For weak fields:

\[
A\simeq 1+\frac{2\Phi}{c^2}.
\]

The scalar field recovers the Newtonian potential structure:

\[
\nabla^2\Phi=4\pi G\rho.
\]

Exterior weak multipole expansion:

\[
\Phi(\mathbf{x}) =
-G\int
\frac{\rho(\mathbf{x}')}{|\mathbf{x}-\mathbf{x}'|}
\,d^3x'.
\]

Thus:

\[
A(\mathbf{x})
\simeq
1+\frac{2\Phi(\mathbf{x})}{c^2}.
\]

Spatial reconstruction at weak order gives the GR-like \(\gamma=1\) structure when the scalar spatial response is tied to the same potential.

Status:

```text
DERIVED_REDUCED / WEAK-FIELD
```

Limit:

```text
Not yet full nonlinear nonspherical field equation.
```

---

# 4. Scalar Radiative Sector

An unconstrained scalar radiative perturbation would have the form:

\[
A_{\rm rad}=a_0\cos(kx-\omega t),
\]

with wave condition:

\[
\omega^2=c^2k^2.
\]

This would be a scalar breathing-type gravitational radiation channel.

Current policy:

\[
A_{\rm rad}
\quad
\text{is absent, constrained, damped, relaxed, massive, or otherwise suppressed.}
\]

Candidate relaxation law:

\[
\frac{dA_{\rm rad}}{d\tau} =
-\Gamma\mu^2 A_{\rm rad}.
\]

Solution:

\[
A_{\rm rad}(\tau) =
A_{\rm rad}(0)e^{-\Gamma\mu^2\tau}.
\]

Status:

```text
CONSTRAINED / UNFINISHED
```

Required condition:

\[
A_{\rm constraint}
\text{ survives as static long-range field, while }
A_{\rm rad}
\text{ does not become an unsuppressed scalar wave.}
\]

Unknown:

```text
Mechanism separating static scalar constraint from scalar radiation.
```

---

# 5. Vacuum-Substance Balance Identity

Candidate ontology-native balance law:

\[
\partial_t q_v+\nabla\cdot J_v =
\Sigma_{\rm exchange} +
\Sigma_{\rm creation} -
\Gamma_{\rm relax}.
\]

Interpretation:

\[
q_v
\]

vacuum charge/density proxy.

\[
J_v
\]

vacuum transport current proxy.

\[
\Sigma_{\rm exchange}
\]

matter/vacuum exchange source.

\[
\Sigma_{\rm creation}
\]

nonconservative creation/destruction term.

\[
\Gamma_{\rm relax}
\]

relaxation toward vacuum minimum.

Status:

```text
STRUCTURAL / UNFINISHED
```

Known projection hints:

\[
\rho
\rightarrow
\Sigma_{\rm exchange}^{(0)}
\rightarrow
A.
\]

\[
j_i=\rho v_i
\rightarrow
\Sigma_{\rm exchange}^{(1)}
\rightarrow
W_i.
\]

\[
\text{trace/stress}
\rightarrow
\Sigma_{\rm exchange}^{\rm trace}
\rightarrow
\kappa.
\]

\[
\text{trace-free quadrupole/shear}
\rightarrow
\Sigma_{\rm exchange}^{TT}
\rightarrow
h_{ij}^{TT}.
\]

Unknown:

```text
Definition of q_v.
Closure identity.
Relation to stress-energy conservation.
Bianchi-like parent identity.
```

---

# 6. Vector Current / Frame-Dragging Sector

## 6.1 Source From Continuity

Matter continuity:

\[
\partial_t\rho+\nabla\cdot j=0.
\]

With:

\[
j_i=\rho v_i.
\]

If \(\rho\) sources scalar exchange, then \(j_i\) is the natural vector/current source.

Status:

```text
CONSTRAINED
```

---

## 6.2 Transverse Current Projection

Decompose:

\[
j=j_T+j_L.
\]

with:

\[
\nabla\cdot j_T=0,
\]

\[
\nabla\times j_L=0.
\]

Fourier-space projector:

\[
P_T(k)=I-\frac{kk^T}{k^2}.
\]

\[
P_L(k)=\frac{kk^T}{k^2}.
\]

Thus:

\[
j_T=P_Tj,
\]

\[
j_L=P_Lj.
\]

Sector allocation:

\[
j_T\rightarrow W_i,
\]

\[
j_L\rightarrow A\text{ / scalar continuity}.
\]

Status:

```text
DERIVED_REDUCED for k^2 != 0
```

Caveat:

```text
k=0/global rotation requires boundary treatment.
```

---

## 6.3 Curl-Energy Vector Action

Candidate vector energy:

\[
E_W =
\int
\left[
K_c|\nabla\times W|^2+\alpha_W j_T\cdot W
\right]d^3x.
\]

Variation gives:

\[
2K_c\nabla\times(\nabla\times W)+\alpha_W j_T=0.
\]

Therefore:

\[
\nabla\times(\nabla\times W) =
-\frac{\alpha_W}{2K_c}j_T.
\]

Using:

\[
\nabla\times(\nabla\times W) =
\nabla(\nabla\cdot W)-\Delta W,
\]

and imposing:

\[
\nabla\cdot W=0,
\]

gives:

\[
\Delta W =
\frac{\alpha_W}{2K_c}j_T.
\]

Status:

```text
STRUCTURAL / DERIVED_REDUCED
```

Unknown coefficient:

\[
\frac{\alpha_W}{2K_c}.
\]

Status of coefficient:

```text
UNKNOWN
```

---

## 6.4 Vector Observable Candidate

Raw \(W_i\) is gauge-sensitive.

Define:

\[
B_W=\nabla\times W.
\]

A symbolic precession/frame-dragging relation is:

\[
\Omega_{\rm drag} =
\beta_W B_W.
\]

Status:

```text
STRUCTURAL / UNFINISHED
```

Unknown:

\[
\beta_W.
\]

---

## 6.5 Global Rotation Boundary Data

Angular momentum:

\[
J=\int r\times j\,d^3x.
\]

For a uniformly rotating solid sphere:

\[
M=\frac{4\pi R^3\rho}{3},
\]

\[
J=\frac{2}{5}MR^2\Omega.
\]

Exterior symbolic axial vector ansatz:

\[
W_\phi(r,\theta) =
\frac{C_JJ\sin\theta}{r^2}.
\]

Curl components:

\[
(\nabla\times W)_r =
\frac{2C_JJ\cos\theta}{r^3},
\]

\[
(\nabla\times W)_\theta =
\frac{C_JJ\sin\theta}{r^3}.
\]

Thus:

\[
B_W\sim\frac{J}{r^3}.
\]

Status:

```text
DERIVED_REDUCED shape
```

Normalization chain:

\[
C_J
\sim
C_{\rm shape}
\frac{\alpha_W}{8\pi K_c}.
\]

Observable:

\[
\Omega_{\rm drag}
\sim
\beta_W
C_{\rm shape}
\frac{\alpha_W}{8\pi K_c}
\frac{J}{r^3}.
\]

Unknowns:

```text
alpha_W/K_c
C_shape
beta_W
```

Status:

```text
NORMALIZATION UNKNOWN
```

---

# 7. Kappa Trace / Interior Sector

## 7.1 Current Role

Current intended role:

\[
\kappa
\]

is no longer best treated as an ordinary scalar field.

Current best interpretation:

```text
kappa = constrained non-inertial trace / volume relaxation response.
```

It describes local vacuum-curvature equilibration:

```text
matter trace or pressure shifts a local vacuum-curvature minimum;
kappa relaxes toward that minimum;
the relaxation has no independent momentum channel;
therefore kappa does not overshoot, slosh, or propagate as an ordinary
breathing wave.
```

Areal-gauge diagnostic relation:

\[
AB=e^{2\kappa}.
\]

Thus:

\[
\kappa=\frac12\ln(AB).
\]

Exterior Schwarzschild sector:

\[
\kappa=0.
\]

Status:

```text
CONSTRAINED / STRUCTURAL
```

The areal-gauge diagnostic relation is reduced-derived, but the covariant physical status of \(\kappa\) remains unfinished.

---

## 7.2 Rejected Kappa Interpretations

Raw density \(\rho\) as the primary \(\kappa\) source is rejected.

Reason:

```text
rho already sources the A-sector mass / monopole response.
```

A raw pressure trace Poisson source:

\[
S_{\rm trace}=3p
\]

is also rejected as a final unscreened source, because for ordinary positive pressure:

\[
Q_\kappa=\int 3p\,d^3x\neq0,
\]

which would produce a massless exterior tail:

\[
\kappa_{\rm ext}\sim\frac{1}{r}.
\]

An ordinary massless wave equation:

\[
\Box\kappa=\alpha S
\]

is rejected because it introduces a scalar breathing-radiation channel.

Status:

```text
REJECTED as ordinary propagating scalar gravity.
```

---

## 7.3 Non-Inertial Relaxation Candidate

The preferred candidate is first-order local relaxation toward a shifted minimum:

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa
(\kappa-\kappa_{\min}).
\]

For fixed \(\kappa_{\min}\):

\[
\kappa(t)-\kappa_{\min}
=
[\kappa(0)-\kappa_{\min}]
e^{-\mu_\kappa K_\kappa t}.
\]

This gives:

```text
no oscillation,
no overshoot,
no slosh,
no independent kappa momentum channel,
no ordinary breathing radiation.
```

Candidate minimum shift:

\[
\kappa_{\min}
=
\chi_\kappa S_{\rm trace,effective}.
\]

Interpretation:

```text
trace / pressure shifts the local equilibrium configuration;
kappa relaxes toward it;
trace is not treated as a radiative scalar charge.
```

Status:

```text
STRUCTURAL / UNFINISHED
```

Unknown:

```text
K_kappa,
mu_kappa,
chi_kappa,
S_trace_effective,
covariant origin.
```

---

## 7.4 Exterior Suppression and Boundary Flux

Exterior vacuum target:

\[
S_{\rm trace}=0,
\]

\[
\kappa_{\min}=0,
\]

\[
\kappa\to0.
\]

Boundary flux diagnostic:

\[
F_\kappa(R)=4\pi R^2\kappa'(R).
\]

Exterior safety requires:

\[
F_\kappa(R+)=0.
\]

Compact interior profiles can satisfy:

\[
\kappa(R)=0,
\]

\[
\kappa'(R)=0,
\]

and therefore:

\[
F_\kappa(R)=0.
\]

A smoother C2 compact profile:

\[
\kappa(r)=
\kappa_0
\left(
1-\frac{r^2}{R^2}
\right)^3
\]

also satisfies:

\[
\kappa''(R)=0,
\]

removing the toy hidden second-derivative shell-stress trap.

Status:

```text
DERIVED_REDUCED toy boundary control
```

Unknown:

```text
physical interface law,
source compatibility,
required smoothness from true action.
```

---

## 7.5 Compensated / Projected Trace Logic

A compensated source:

\[
P_0S=S-\langle S\rangle
\]

satisfies:

\[
\int P_0S\,d^3x=0.
\]

This removes massless exterior monopole \(\kappa\)-charge.

Status:

```text
CONSTRAINED
```

Caveat:

```text
P_0 is nonlocal over the support region.
It is acceptable only as a constraint/projection identity or boundary balance,
not as an ordinary local scalar source.
```

---

## 7.6 Near-Boundary Joint Minimum

Group 10 suggests that the interior profile may not be exactly the naive Newtonian/parabolic curve near a material boundary.

A mass source can create an interior quadratic tendency:

\[
f_{\rm int}=a_0+a_2r^2,
\]

while the exterior vacuum favors a reciprocal tendency:

\[
f_{\rm ext}=1-\frac{M}{r}.
\]

A toy joint-minimum energy is:

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

For constant weights, the schematic minimizer is:

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

This may imply a near-boundary deviation from naive GR/Newtonian interior matching.

Deviation diagnostics:

\[
\delta_f=f_{\rm joint}-f_{\rm GR,ref},
\]

\[
\delta_g=-\frac{d\delta_f}{dr},
\]

\[
\delta_{\rm curv}=\frac{d^2\delta_f}{dr^2}.
\]

Status:

```text
PLAUSIBLE / DIAGNOSTIC ONLY
```

No magnitude or measurement claim is justified until:

```text
weights are derived,
transition width is derived,
recombination map is fixed,
observable is selected.
```



# 8. Tensor Radiation Sector

## 8.1 TT Field

Tensor radiation variable:

\[
h_{ij}^{TT}.
\]

Conditions:

\[
\partial_i h_{ij}^{TT}=0,
\]

\[
\delta^{ij}h_{ij}^{TT}=0.
\]

For propagation along \(z\):

\[
h_{ij}^{TT} =
\begin{pmatrix}
h_+ & h_\times & 0\\
h_\times & -h_+ & 0\\
0&0&0
\end{pmatrix}.
\]

Status:

```text
DERIVED_REDUCED / STRUCTURAL
```

---

## 8.2 Tensor Wave Equation

Candidate tensor equation:

\[
\Box h_{ij}^{TT} =
-\mathcal{C}_T S_{ij}^{TT}.
\]

GR target would be:

\[
\Box h_{ij}^{TT} =
-\frac{16\pi G}{c^4}T_{ij}^{TT}
\]

or in far-zone quadrupole form:

\[
h_{ij}^{TT}
\sim
\frac{2G}{c^4R}
\frac{d^2Q_{ij}^{TT}}{dt^2}.
\]

Current reconstruction status:

```text
TT structure: DERIVED_REDUCED / STRUCTURAL
wave equation form: STRUCTURAL
coefficient: MATCHED / UNKNOWN
source identity: UNFINISHED
```

Unknown:

\[
\mathcal{C}_T.
\]

The coefficient \(2G/c^4\) has not been derived from the vacuum ontology.

---

## 8.3 Tensor Radiation Energy Flux

Candidate energy-flux scaling:

\[
F_T
\sim
K_T
\left\langle
\dot{h}_{ij}^{TT}\dot{h}_{ij}^{TT}
\right\rangle.
\]

GR target form:

\[
F_{\rm GR} =
\frac{c^3}{32\pi G}
\left\langle
\dot{h}_{ij}^{TT}\dot{h}_{ij}^{TT}
\right\rangle.
\]

Current status:

```text
STRUCTURAL / MATCHED
```

Unknown:

```text
K_T from vacuum action/stiffness.
```

---

# 9. Source Coupling Summary

Current source assignments:

| Sector | Source | Status |
|---|---|---|
| \(A\) | \(\rho\), \(M_{\rm enc}\) | DERIVED_REDUCED |
| \(W_i\) | \(j_T=P_T(\rho v)\) | STRUCTURAL / CONSTRAINED |
| \(\kappa\) | pressure / stress trace shifts \(\kappa_{\min}\); constrained trace / volume relaxation | STRUCTURAL / UNFINISHED |
| \(h_{ij}^{TT}\) | trace-free quadrupole / \(T_{ij}^{TT}\) | STRUCTURAL / COEFFICIENT MATCHED |
| \(A_{\rm rad}\) | scalar radiative deviation | SUPPRESSED / UNFINISHED |
| \(\Sigma_{\rm creation}\) | nonconservative creation regime | SPECIAL / RISK |

---

# 10. Constraint / Evolution Split

Current best split:

| Variable | Equation Type | Status |
|---|---|---|
| \(A\) | elliptic / constraint | DERIVED_REDUCED |
| \(A_{\rm rad}\) | absent, damped, or constrained | UNFINISHED |
| \(\kappa\) | first-order non-inertial trace relaxation / constrained variable | STRUCTURAL / UNFINISHED |
| \(W_i\) | elliptic transverse vector response, at least stationary | STRUCTURAL |
| \(h_{ij}^{TT}\) | hyperbolic tensor evolution | STRUCTURAL |
| gauge modes | projected / fixed | UNFINISHED |
| source identities | continuity / Bianchi-like closure | UNKNOWN |

---

# 11. Current Candidate Field System

A compact presentation of the current system is:

\[
\boxed{
\Delta_{\rm areal}A =
\frac{8\pi G}{c^2}\rho
}
\]

Status:

```text
DERIVED_REDUCED
```

\[
\boxed{
AB=e^{2\kappa}
}
\]

Status:

```text
DEFINITION / GAUGE-CONDITIONED
```

Exterior condition:

\[
\boxed{
\kappa=0
}
\]

Status:

```text
DERIVED_REDUCED in static spherical exterior
```

\[
\boxed{
\nabla\times(\nabla\times W) =
-\frac{\alpha_W}{2K_c}j_T
}
\]

with:

\[
j_T=P_Tj,
\]

\[
P_T=I-\frac{kk^T}{k^2}.
\]

Status:

```text
STRUCTURAL / COEFFICIENT UNKNOWN
```

Under:

\[
\nabla\cdot W=0,
\]

\[
\boxed{
\Delta W =
\frac{\alpha_W}{2K_c}j_T
}
\]

Status:

```text
STRUCTURAL / COEFFICIENT UNKNOWN
```

\[
\boxed{
\dot{\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min})
}
\]

with:

\[
\kappa_{\min}
=
\chi_\kappa S_{\rm trace,effective}
\]

and exterior/boundary conditions:

\[
\kappa\to0,
\qquad
\kappa_{\min}\to0,
\qquad
F_\kappa(R+)=0.
\]

Status:

```text
STRUCTURAL / UNFINISHED
```

Rejected:

\[
\Box\kappa=\alpha S
\]

as an ordinary massless scalar breathing-wave equation.

\[
\boxed{
\Box h_{ij}^{TT} =
-\mathcal{C}_T S_{ij}^{TT}
}
\]

Status:

```text
STRUCTURAL / SOURCE AND COEFFICIENT UNFINISHED
```

\[
\boxed{
\partial_t q_v+\nabla\cdot J_v =
\Sigma_{\rm exchange}
+
\Sigma_{\rm creation}
-
\Gamma_{\rm relax}
}
\]

Status:

```text
ONTOLOGY-NATIVE / UNFINISHED
```

---

# 12. What Is Genuinely Reconstructed

## Static Spherical Exterior

\[
A=1-\frac{2GM}{c^2r},
\]

\[
B=\frac{1}{A}.
\]

Status:

```text
RECONSTRUCTED
```

## Weak Scalar Multipole Shape

\[
A\simeq 1+\frac{2\Phi}{c^2}.
\]

Status:

```text
RECONSTRUCTED AT WEAK ORDER
```

## Vector Current Structure

\[
j_i=\rho v_i,
\]

\[
j_T=P_Tj,
\]

\[
\nabla\times\nabla\times W\sim j_T,
\]

\[
B_W=\nabla\times W,
\]

\[
B_W\sim\frac{J}{r^3}.
\]

Status:

```text
STRUCTURE RECONSTRUCTED
NORMALIZATION NOT RECONSTRUCTED
```

## Tensor TT Shape

\[
h_{ij}^{TT}
\]

with plus/cross polarizations and quadrupole source form.

Status:

```text
STRUCTURE RECONSTRUCTED
COUPLING NOT RECONSTRUCTED
```

---

# 13. Major Unknowns

\[
\frac{\alpha_W}{K_c}
\]

vector source/stiffness ratio.

\[
\beta_W
\]

precession / observable coupling.

\[
C_{\rm shape}
\]

vector source convention factor.

\[
K_\kappa,\;\mu_\kappa,\;\chi_\kappa
\]

kappa stiffness, mobility, and trace-minimum coupling.

\[
S_{\rm trace,effective}
\]

effective trace / pressure / volume source shifting \(\kappa_{\min}\).

\[
\sigma
\]

near-boundary joint-minimum transition width, if used.

\[
W_{\rm int},\;W_{\rm ext},\;\lambda_1,\;\lambda_2
\]

joint-minimum energy weights / smoothing coefficients, if used.

\[
\mathcal{C}_T
\]

tensor coupling coefficient.

\[
K_T
\]

tensor action stiffness / radiation energy coefficient.

\[
q_v,\;J_v,\;\Sigma_{\rm exchange},\;\Sigma_{\rm creation},\;\Gamma_{\rm relax}
\]

parent ontology variables and balance terms.

Bianchi-like closure identity:

\[
\text{UNKNOWN}.
\]

Gauge-invariant observable set:

\[
\text{UNFINISHED}.
\]

---

# 14. Minimal Honest Claim

The current field-equation status is:

```text
A-sector:
  real reduced reconstruction.

Vector sector:
  source/projection/action/shape reconstructed,
  normalization missing.

Kappa sector:
  role identified as constrained non-inertial trace / volume relaxation,
  first-order structural candidate written,
  coefficients, source law, boundary physics, and covariant origin missing.

Tensor sector:
  TT structure identified,
  coupling and source identity missing.

Parent conservation:
  ontology-native balance proposed,
  closure missing.
```

The candidate system is therefore not yet a finished covariant theory.

It is a partially reconstructed field-equation architecture with one fully successful reduced exterior sector.
