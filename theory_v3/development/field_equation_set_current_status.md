# Field Equation Set — Current Reconstruction Status

## Scope

This document presents the current field-equation architecture as if it were a candidate finished system, while explicitly marking incomplete or unknown pieces.

Audience: GR / relativistic field theory readers.

Status labels:

```text
DERIVED_REDUCED
STRUCTURAL
CONSTRAINED
MATCHED
REJECTED
MISSING
UNFINISHED
RISK
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
\zeta=\ln\sqrt{\gamma}
\]

candidate vacuum-spacetime volume configuration variable.

\[
\kappa
\]

trace / volume / interior relaxation candidate; currently kept separate from \(\zeta\)-volume configuration until the \(\kappa\)-\(\zeta\) map is derived.

\[
W_i
\]

transverse vector current / frame-dragging candidate.

\[
h_{ij}^{TT}
\]

transverse-traceless tensor radiation field.

Auxiliary or controlled scalar-radiative variable:

\[
A_{\rm rad}
\]

scalar breathing/radiative hazard; rejected as an ordinary active long-range degree of freedom.

Vacuum-substance / vacuum-spacetime accounting variables:

\[
\epsilon_{\rm vac,config},
\qquad
E_{\rm vac,config},
\qquad
q_v,
\qquad
J_v.
\]

Current best interpretation from group 13:

```text
epsilon_vac_config is geometric, not a generic reservoir.
It is provisionally a zeta-volume configuration density.
q_v/J_v are optional bookkeeping variables, only allowed if tied to geometry.
```

Current provisional vacuum-volume functional:

\[
\epsilon_{\rm vac,config}=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2.
\]

Separate \(\kappa\)-relaxation energy:

\[
e_\kappa=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Provisional exchange accounting:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}=
0.
\]

Current reduced recombination map:

\[
g_{tt}\leftarrow A,
\]

\[
g_{0i}\leftarrow W_i,
\]

\[
g_{ij}\leftarrow
\text{scalar spatial response}(A)
+
\kappa_{\rm trace}
+
h_{ij}^{TT}.
\]

No-double-counting requirements:

```text
rho -> A only,
trace / pressure -> kappa_min or zeta-volume sector only through projectors,
kappa_ext = 0,
zeta_ext = 0,
h_ij^TT trace-free,
W_i transverse,
source(A_rad ordinary massless)=0,
delta M_ext|kappa/zeta relaxation=0,
epsilon_vac_config excludes A_flux and M_ext,
e_kappa is kept outside epsilon_vac_config until the kappa-zeta map is derived.
```

Status:

```text
STRUCTURAL / UNFINISHED
```

The recombination map is reduced bookkeeping, not a covariant parent derivation.

Group 13 result:

```text
vacuum-substance accounting is now geometric enough to state provisionally,
but the kappa-zeta map and projectors remain unresolved.
```


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

Current rule:

\[
{\rm source}(A_{\rm rad}\ {\rm ordinary\ massless})=0.
\]

Also rejected as ordinary massless scalar radiation equations:

\[
\Box\kappa=\alpha S,
\]

\[
\Box\zeta=\alpha S.
\]

Group 13 interpretation:

```text
scalar / trace disturbances are conversion-limited,
not friction-damped waves.
```

They are not currently modeled as:

\[
\phi_{tt}+\gamma\phi_t+\omega^2\phi=0.
\]

Reason:

```text
no scalar inertia / momentum channel has been derived.
```

Current scalar / trace conversion skeleton:

\[
P_{\rm trace}[\text{source/geometry}]
\rightarrow
\delta\zeta.
\]

\[
\zeta=\ln\sqrt{\gamma}.
\]

\[
\kappa\sim\zeta-\zeta_{\min}
\]

as a constraint target only, not yet a derived identity.

Interpretation:

```text
trace / scalar disturbance changes the spacetime-volume configuration.
It does not become an ordinary far-zone scalar wave.
```

Ordinary radiation rule:

```text
ordinary long-range gravitational radiation is TT-only.
```

The static scalar \(A\)-sector survives as a constraint / mass-response field. The scalar-radiative residue does not become an ordinary active long-range wave channel.

Status:

```text
REJECTED / CONSTRAINED
```

Unknown:

```text
Parent mechanism proving static scalar constraint cannot become ordinary scalar radiation.
Trace/volume conversion operator P_trace.
Binary scalar-conversion safety theorem.
Nonlinear/covariant volume-form theorem.
```

Failure if violated:

```text
breathing radiation,
scalar double-counting,
far-zone scalar flux,
secular orbital damping,
or an exterior scalar channel not supported by the current theory.
```


# 5. Vacuum-Substance / Vacuum-Spacetime Balance Target

Corrected ontology carried into group 13:

```text
vacuum is spacetime.
creating vacuum creates spacetime.
changing local spacetime creates curvature.
```

Therefore:

```text
vacuum accounting is geometric accounting,
not generic reservoir bookkeeping.
```

Candidate volume-form variable:

\[
\zeta=\ln\sqrt{\gamma}.
\]

Physical volume element:

\[
dV_{\rm phys}=\sqrt{\gamma}\,d^3x.
\]

Linear variation:

\[
\delta\zeta=
\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

For TT perturbations:

\[
\gamma^{ij}h_{ij}^{TT}=0,
\]

so:

\[
\delta\zeta|_{TT}=0.
\]

Interpretation:

```text
trace / volume modes change vacuum-spacetime amount,
TT modes are volume-preserving shear.
```

Candidate vacuum-accounting balance skeleton:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

Ordinary closed conditions:

\[
\Sigma_{\rm creation}=0,
\]

\[
\oint J_v\cdot dS=0,
\]

\[
Q_{\rm volume}=0,
\]

\[
\delta M_{\rm ext}=0,
\]

\[
F_{\rm scalar,far}=0.
\]

Provisional \(\epsilon_{\rm vac,config}\) functional:

\[
\epsilon_{\rm vac,config}=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2.
\]

Separate \(\kappa\)-relaxation energy:

\[
e_\kappa=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Provisional exchange accounting:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}=
0.
\]

No \(K_{\rm lock}\) energy is currently counted.

Constraint target only:

\[
\kappa\sim\zeta-\zeta_{\min}.
\]

Group 12 parent template v2 remains:

\[
{\rm Div}\,
E_{\rm parent}
[
A,W,h_{TT},\kappa;
P_{\rm scalar},P_T,P_{TT},P_{\rm trace},P_{\rm boundary}
]=
B_{\rm closed}[T]
+
B_{\rm relax}[\Gamma_{\rm relax},E_{\rm vac,config}].
\]

Status:

```text
CANDIDATE / SCAFFOLD ONLY
```

The group-13 balance is more concrete than the group-12 balance language, but it is still not closure.

Allowed \(J_v\) classes:

```text
J_v = 0 / local exchange,
compact-support J_v,
constraint redistribution J_v with zero exterior flux,
causal transport J_v only if separately derived.
```

Forbidden \(J_v\) classes:

```text
acausal repair current,
far-zone scalar-energy current,
coefficient tuning current,
exterior mass-changing current,
unlabeled nonlocal transport.
```

Unknown:

```text
Definition of E_parent.
Definition of B_closed.
Definition of B_relax.
Definition of epsilon_vac_config from a parent action.
Definition of zeta_min.
Definition of q_v and J_v, if needed.
Definition of Sigma_exchange.
Definition of Gamma_relax sign convention.
Definition of u^mu / frame / foliation.
Closure identity.
Relation to stress-energy conservation.
Bianchi-like parent identity.
Covariant recombination map.
Scalar constraint propagation.
Coefficient action / stiffness principle.
Kappa-zeta map.
```


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

Group 13 added the volume-form variable:

\[
\zeta=\ln\sqrt{\gamma}.
\]

Current constraint target:

\[
\kappa\sim\zeta-\zeta_{\min}.
\]

Status:

```text
CONSTRAINED / STRUCTURAL
```

The areal-gauge diagnostic relation is reduced-derived, but the covariant physical relation between \(\kappa\) and \(\zeta\) remains unfinished.

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

Ordinary massless wave equations:

\[
\Box\kappa=\alpha S,
\]

\[
\Box\zeta=\alpha S
\]

are rejected because they introduce scalar breathing-radiation channels.

Status:

```text
REJECTED as ordinary propagating scalar gravity.
```

---

## 7.3 Non-Inertial Relaxation Candidate

The reduced candidate is first-order local relaxation toward a shifted minimum:

\[
\dot{\kappa}=
-\mu_\kappa K_\kappa
(\kappa-\kappa_{\min}).
\]

Group 12 frame-compatible candidate:

\[
u^\mu\nabla_\mu\kappa=
-\lambda_\kappa(\kappa-\kappa_{\min}).
\]

where:

\[
\lambda_\kappa=\mu_\kappa K_\kappa.
\]

Candidate minimum shift:

\[
\kappa_{\min}=
\chi_\kappa S_{\rm trace,effective}.
\]

For fixed \(\kappa_{\min}\):

\[
\kappa(t)-\kappa_{\min}=
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

Status:

```text
STRUCTURAL / UNFINISHED
```

Unknown:

```text
u^mu,
K_kappa,
mu_kappa,
lambda_kappa,
chi_kappa,
S_trace_effective,
covariant origin,
kappa-zeta map.
```

---

## 7.4 Kappa / Zeta Energy Accounting

Group 13 provisional convention:

\[
\epsilon_{\rm vac,config}=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2.
\]

Separate kappa relaxation energy:

\[
e_\kappa=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Provisional exchange accounting:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}=
0.
\]

Constraint target:

\[
\kappa\sim\zeta-\zeta_{\min}.
\]

but:

```text
no K_lock energy is counted until derived.
```

Reason:

```text
the kappa-zeta map is not derived,
so combining kappa mismatch energy into epsilon_vac_config risks double-counting.
```

Status:

```text
CANDIDATE / PROVISIONAL
```

Unknown:

```text
zeta_min,
kappa-zeta map,
whether e_kappa is truly separate or later absorbed,
K_zeta,
L_zeta,
K_kappa,
volume measure,
total balance law.
```

---

## 7.5 Exterior Suppression and Boundary Flux

Exterior vacuum target:

\[
S_{\rm trace}=0,
\]

\[
\kappa_{\min}=0,
\]

\[
\zeta_{\min}=0,
\]

\[
\kappa\to0,
\]

\[
\zeta\to0.
\]

Boundary flux diagnostics:

\[
F_\kappa(R)=4\pi R^2\kappa'(R),
\]

\[
F_\zeta(R)=4\pi R^2\zeta'(R).
\]

Exterior safety requires:

\[
F_\kappa(R+)=0,
\]

\[
F_\zeta(R+)=0.
\]

Exterior charge conditions:

\[
Q_\kappa=0,
\]

\[
Q_{\rm volume}=0.
\]

Boundary mass preservation requires:

\[
\delta M_{\rm ext}\big|_{\kappa/\zeta{\rm\ reconfiguration}}=0.
\]

Compact interior profiles can satisfy:

\[
\kappa(R)=0,
\qquad
\kappa'(R)=0,
\]

and similarly:

\[
\zeta(R)=0,
\qquad
\zeta'(R)=0.
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
\kappa''(R)=0.
\]

Analogous compact \(\zeta\) profiles may be used only as toy boundary diagnostics.

Status:

```text
DERIVED_REDUCED toy boundary control / CONSTRAINED
```

Unknown:

```text
physical interface law,
source compatibility,
required smoothness from true action,
boundary mass preservation theorem,
P_boundary P_trace origin.
```

---

## 7.6 Compensated / Projected Trace and Volume Logic

A compensated source:

\[
P_0S=S-\langle S\rangle
\]

satisfies:

\[
\int P_0S\,d^3x=0.
\]

This removes massless exterior monopole \(\kappa\)- or \(\zeta\)-charge.

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

## 7.7 Near-Boundary Joint Minimum

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
E[f]=
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
(W_i+W_e)f=
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
observable is selected,
boundary mass preservation theorem is established,
kappa-zeta map is derived.
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

# 9. Source Coupling, Projectors, and No-Double-Counting Summary

Current source assignments:

| Sector | Source | Status |
|---|---|---|
| \(A\) | \(\rho\), \(M_{\rm enc}\), \(P_{\rm scalar}T\) | DERIVED_REDUCED / STRUCTURAL PROJECTOR |
| \(W_i\) | \(j_T=P_T(\rho v)\) | STRUCTURAL / CONSTRAINED |
| \(\zeta\) | trace / volume configuration through \(P_{\rm trace}\) | CANDIDATE / UNFINISHED |
| \(\kappa\) | pressure / stress trace shifts \(\kappa_{\min}\); constrained trace / volume relaxation | STRUCTURAL / UNFINISHED |
| \(h_{ij}^{TT}\) | trace-free quadrupole / \(P_{TT}T_{ij}\) | STRUCTURAL / COEFFICIENT MATCHED |
| \(A_{\rm rad}\) | ordinary long-range scalar radiative deviation | REJECTED / CONSTRAINED |
| \(\epsilon_{\rm vac,config}\) | \(\zeta\)-volume configuration density | CANDIDATE / PROVISIONAL |
| \(e_\kappa\) | separate \(\kappa\)-relaxation energy | CANDIDATE / PROVISIONAL |
| \(J_v\) | optional local / compact / constrained vacuum configuration current | STRUCTURAL / OPTIONAL |
| \(\Sigma_{\rm creation}\) | nonconservative creation regime | SPECIAL / RISK; excluded from ordinary closed gravity |

Projector routing required by groups 12–13:

```text
rho / scalar charge
  -> P_scalar
  -> A

longitudinal current
  -> P_L
  -> scalar continuity

transverse current
  -> P_T
  -> W_i

TT stress
  -> P_TT
  -> h_ij^TT

trace / pressure / volume source
  -> P_trace
  -> zeta, zeta_min, kappa_min

kappa imbalance
  -> P_relax
  -> first-order relaxation and exchange with epsilon_vac_config

boundary data
  -> P_boundary
  -> M_ext preservation and kappa/zeta exterior safety

active-regime terms
  -> P_closed
  -> Sigma_creation=0 in ordinary regime

sector fields
  -> P_recombination
  -> geometry without double-counting
```

No-double-counting rules:

\[
S_\kappa[\rho]=0
\]

as an independent long-range scalar source.

\[
S_\zeta[\rho]=0
\]

as an independent exterior scalar charge.

\[
Q_\kappa=\int S_\kappa\,d^3x=0.
\]

\[
Q_{\rm volume}=0.
\]

\[
{\rm source}(W_i)=P_Tj.
\]

\[
P_Lj
\rightarrow
\text{scalar continuity / density redistribution}.
\]

\[
{\rm source}(h_{TT})=P_{TT}S_{ij}.
\]

\[
{\rm source}(A_{\rm rad}\ {\rm ordinary\ massless})=0.
\]

\[
{\rm source}(\Box\zeta)=0
\]

in ordinary gravity.

\[
{\rm source}(\Box\kappa)=0
\]

in ordinary gravity.

\[
\Gamma_{\rm relax}[A_{\rm mass\ flux}]=0.
\]

\[
\delta M_{\rm ext}\big|_{\kappa/\zeta\ {\rm boundary\ smoothing}}=0.
\]

\[
\epsilon_{\rm vac,config}
\not\rightarrow
A\text{-sector exterior mass charge}.
\]

\[
\epsilon_{\rm vac,config}
\not\rightarrow
\Sigma_{\rm creation}
\]

in ordinary closed gravity.

\[
e_\kappa
\]

is counted separately from \(\epsilon_{\rm vac,config}\) until the \(\kappa\)-\(\zeta\) map is derived.

Main rule:

```text
one source may participate in total stress-energy,
but it must not become multiple independent gravity sources unless a parent
identity forces the split.
```

Status:

```text
CONSTRAINED / NOT YET PARENT-DERIVED
```


# 10. Constraint / Evolution Split

Current best split:

| Variable | Equation Type | Status |
|---|---|---|
| \(A\) | elliptic / scalar constraint | DERIVED_REDUCED |
| \(B\) | reduced gauge-conditioned companion to \(A\) | DERIVED_REDUCED / UNFINISHED COVARIANTLY |
| \(A_{\rm rad}\) | ordinary scalar radiation rejected | REJECTED / CONSTRAINED |
| \(\zeta\) | volume-form configuration variable; no scalar wave equation | CANDIDATE / FRAME-DEPENDENT |
| \(\epsilon_{\rm vac,config}\) | \(\zeta\)-volume configuration density | CANDIDATE / PROVISIONAL |
| \(\kappa\) | first-order non-inertial trace relaxation / constrained variable | STRUCTURAL / UNFINISHED |
| \(e_\kappa\) | separate kappa relaxation energy | CANDIDATE / PROVISIONAL |
| \(q_v,J_v\) | optional vacuum-substance density/current bookkeeping | STRUCTURAL / OPTIONAL |
| \(W_i\) | transverse vector response; stationary constraint-like sector, possible retarded response dynamically | STRUCTURAL |
| \(h_{ij}^{TT}\) | hyperbolic tensor evolution | STRUCTURAL |
| gauge modes | projected / fixed | UNFINISHED |
| source identities | continuity / Bianchi-like closure | MISSING |

Radiation rule:

```text
ordinary long-range gravitational radiation is TT-only.
```

Allowed:

```text
h_ij^TT propagates.
```

Constrained or rejected:

```text
A_rad ordinary scalar radiation is rejected.
kappa breathing radiation is rejected.
zeta scalar radiation is rejected.
W_i free vector radiation is not currently derived.
```

Scalar / trace conversion rule:

```text
scalar / trace disturbances are conversion-limited,
not friction-damped waves.
```

Relaxation rule:

```text
Gamma_relax is exchange / restoration, not energy destruction.
```

Provisional exchange:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}=
0.
\]

Vacuum-accounting balance skeleton:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

Ordinary constraints:

\[
\Sigma_{\rm creation}=0,
\]

\[
\oint J_v\cdot dS=0,
\]

\[
Q_{\rm volume}=0,
\]

\[
\delta M_{\rm ext}=0,
\]

\[
F_{\rm scalar,far}=0.
\]

Status:

```text
CONSTRAINED / STRUCTURAL
```

Parent identity still required:

```text
how constraints propagate consistently,
why TT modes alone carry ordinary radiation,
why scalar trace converts but does not radiate,
why vector current response is transverse,
how energy/source conservation is maintained,
how epsilon_vac_config is derived,
how e_kappa and epsilon_vac_config avoid double-counting,
how recombination avoids double-counting.
```


# 11. Current Minimal Candidate Field System

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
A_{\rm ext}(r)=1-\frac{2GM}{c^2r}
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

therefore:

\[
\boxed{
B=\frac{1}{A}
}
\]

Status:

```text
DERIVED_REDUCED in static spherical exterior
```

Weak scalar limit:

\[
\boxed{
A\simeq1+\frac{2\Phi}{c^2},
\qquad
\nabla^2\Phi=4\pi G\rho
}
\]

Status:

```text
DERIVED_REDUCED / WEAK-FIELD
```

Volume-form candidate:

\[
\boxed{
\zeta=\ln\sqrt{\gamma}
}
\]

with:

\[
\boxed{
\delta\zeta=
\frac12\gamma^{ij}\delta\gamma_{ij}
}
\]

and for TT perturbations:

\[
\boxed{
\delta\zeta|_{TT}=0.
}
\]

Status:

```text
CANDIDATE / LINEAR STRUCTURAL
```

Vector response:

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

Kappa trace relaxation:

\[
\boxed{
u^\mu\nabla_\mu\kappa=
-\lambda_\kappa(\kappa-\kappa_{\min})
}
\]

with:

\[
\kappa_{\min}=
\chi_\kappa S_{\rm trace,effective}.
\]

Reduced form:

\[
\dot{\kappa}=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

Exterior/boundary conditions:

\[
\kappa\to0,
\qquad
\zeta\to0,
\qquad
\kappa_{\min}\to0,
\qquad
\zeta_{\min}\to0,
\]

\[
Q_\kappa=0,
\qquad
Q_{\rm volume}=0,
\]

\[
F_\kappa(R+)=0,
\qquad
F_\zeta(R+)=0,
\]

\[
\delta M_{\rm ext}\big|_{\kappa/\zeta{\rm\ reconfiguration}}=0.
\]

Status:

```text
STRUCTURAL / UNFINISHED
```

Vacuum-volume configuration density:

\[
\boxed{
\epsilon_{\rm vac,config}=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2
}
\]

Status:

```text
CANDIDATE / PROVISIONAL
```

Separate kappa relaxation energy:

\[
\boxed{
e_\kappa=
\frac12K_\kappa(\kappa-\kappa_{\min})^2
}
\]

Status:

```text
CANDIDATE / PROVISIONAL
```

Provisional exchange:

\[
\boxed{
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}=
0
}
\]

Status:

```text
CANDIDATE / PROVISIONAL
```

Vacuum-accounting balance skeleton:

\[
\boxed{
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}
}
\]

with ordinary constraints:

\[
\boxed{
\Sigma_{\rm creation}=0,
\qquad
\oint J_v\cdot dS=0,
\qquad
Q_{\rm volume}=0,
\qquad
\delta M_{\rm ext}=0,
\qquad
F_{\rm scalar,far}=0.
}
\]

Status:

```text
CANDIDATE / SCAFFOLD ONLY
```

Rejected:

\[
\Box\kappa=\alpha S,
\]

\[
\Box\zeta=\alpha S,
\]

as ordinary massless scalar breathing-wave equations.

Tensor radiation:

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

Tensor energy flux scaling:

\[
\boxed{
F_T
\sim
K_T
\left\langle
\dot h_{ij}^{TT}
\dot h_{ij}^{TT}
\right\rangle
}
\]

Status:

```text
MATCHED / COEFFICIENT UNFINISHED
```

Scalar-radiation rejection:

\[
\boxed{
{\rm source}(A_{\rm rad}\ {\rm ordinary\ massless})=0
}
\]

Status:

```text
REJECTED / CONSTRAINED
```

Parent closure target v2:

\[
\boxed{
{\rm Div}\,
E_{\rm parent}
[
A,W,h_{TT},\kappa;
P_{\rm scalar},P_T,P_{TT},P_{\rm trace},P_{\rm boundary}
]=
B_{\rm closed}[T]
+
B_{\rm relax}[\Gamma_{\rm relax},E_{\rm vac,config}]
}
\]

Status:

```text
MISSING / TEMPLATE ONLY
```

This is not closure.


# 12. What Is Genuinely Reconstructed / GR Recovery Audit

## Real Reduced Reconstruction

### Static Spherical Exterior

\[
A=1-\frac{2GM}{c^2r},
\]

\[
B=\frac{1}{A}.
\]

Status:

```text
RECONSTRUCTED / DERIVED_REDUCED
```

This is the strongest current result.

---

## Strong Reduced / Structural Support

### Weak Scalar Multipole Shape

\[
A\simeq 1+\frac{2\Phi}{c^2}.
\]

Status:

```text
RECONSTRUCTED AT WEAK ORDER
```

Limit:

```text
not a full nonlinear nonspherical theory.
```

### Reduced \(\gamma=1\)

The exterior weak reciprocal relation supports the GR-like \(\gamma=1\) structure in the reduced weak exterior.

Status:

```text
DERIVED_REDUCED / NOT FULL PPN AUDIT
```

### Vector Current Shape

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

### Tensor TT Shape

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

## Matched or Missing

Matched / not yet derived:

```text
vector normalization,
tensor coupling,
tensor radiation flux coefficient.
```

Missing:

```text
Bianchi-like parent closure,
covariant recombination,
full nonlinear nonspherical scalar equation,
full PPN audit,
kappa covariant source law,
boundary mass theorem.
```

Constrained:

```text
no scalar radiation,
no kappa breathing mode,
no independent long-range kappa scalar,
no Sigma_creation in ordinary closed gravity.
```

---

## Recovery Scorecard

| Result | Status |
|---|---|
| static spherical exterior \(A\) | DERIVED_REDUCED |
| exterior \(B=1/A\) once \(\kappa=0\) | DERIVED_REDUCED |
| weak scalar / Newtonian limit | DERIVED_REDUCED |
| reduced weak \(\gamma=1\) | DERIVED_REDUCED / not full PPN |
| frame-dragging shape \(\sim J/r^3\) | DERIVED_REDUCED shape |
| frame-dragging normalization | MATCHED / UNKNOWN |
| tensor wave TT structure | STRUCTURAL |
| tensor coupling | MATCHED / UNKNOWN |
| tensor flux coefficient | MATCHED / UNKNOWN |
| no scalar breathing radiation | CONSTRAINED |
| \(\kappa\) non-radiative trace behavior | STRUCTURAL / UNFINISHED |
| parent conservation / Bianchi compatibility | MISSING |
| covariant metric recombination | UNFINISHED |


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
K_\kappa,\;\mu_\kappa,\;\lambda_\kappa,\;\chi_\kappa
\]

kappa stiffness, mobility, relaxation rate, and trace-minimum coupling.

\[
K_\zeta,\;L_\zeta
\]

volume-configuration displacement and gradient/interface stiffness.

\[
u^\mu
\]

frame / flow field defining covariant kappa relaxation and vacuum-accounting derivative.

\[
\zeta_{\min}
\]

local vacuum-volume equilibrium configuration.

\[
S_{\rm trace,effective}
\]

effective trace / pressure / volume source shifting \(\kappa_{\min}\) and/or \(\zeta_{\min}\).

\[
\epsilon_{\rm vac,config}
\]

vacuum-spacetime configuration density; provisionally a \(\zeta\)-volume functional.

\[
E_{\rm vac,config}
\]

integrated vacuum-spacetime configuration functional.

\[
q_v,\;J_v
\]

optional vacuum-substance density/current bookkeeping variables.

\[
\Sigma_{\rm exchange},\;\Sigma_{\rm creation},\;\Gamma_{\rm relax}
\]

vacuum-accounting source / active-regime / relaxation terms.

\[
Q_{\rm volume},\;S_{\rm volume}
\]

volume charge and volume source variables needed for exterior neutrality.

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

Projectors:

\[
P_{\rm scalar},
\quad
P_{TT},
\quad
P_{\rm trace},
\quad
P_{\rm relax},
\quad
P_{\rm boundary},
\quad
P_{\rm recombination},
\quad
P_{\rm coeff}.
\]

Kappa-zeta relation:

\[
\kappa\stackrel{?}{=}\zeta-\zeta_{\min}.
\]

or:

\[
\kappa=P_{\rm trace}[\zeta-\zeta_{\min}].
\]

or:

\[
\kappa=\frac12\ln(AB)
\]

as only a reduced areal-gauge diagnostic.

Status:

```text
UNRESOLVED
```

Bianchi-like closure identity:

\[
\text{UNKNOWN}.
\]

Gauge-invariant observable set:

\[
\text{UNFINISHED}.
\]

Coefficient action / stiffness principle:

\[
\text{MISSING}.
\]

Boundary mass preservation theorem:

\[
\text{MISSING}.
\]

Scalar constraint propagation identity:

\[
\text{MISSING}.
\]

Covariant recombination map:

\[
\text{UNFINISHED}.
\]

Nonlinear / covariant volume-form theorem:

\[
\text{MISSING}.
\]

Binary scalar-conversion safety theorem:

\[
\text{MISSING}.
\]


# 14. Minimal Honest Claim

The current field-equation status is:

```text
A-sector:
  real reduced reconstruction.

Vector sector:
  source/projection/action/shape reconstructed,
  normalization missing.

Tensor sector:
  TT structure identified,
  coupling and source identity missing.

Scalar radiation:
  ordinary long-range scalar radiation rejected / constrained,
  parent mechanism still missing.

Zeta / vacuum-volume sector:
  zeta = ln sqrt(gamma) identified as leading geometric volume-form candidate,
  epsilon_vac_config provisionally written as zeta-volume displacement plus gradient/interface energy,
  frame, measure, stiffnesses, and parent origin missing.

Kappa sector:
  role identified as constrained non-inertial trace / volume relaxation,
  first-order structural candidate written,
  e_kappa kept separate from epsilon_vac_config to avoid double-counting,
  kappa-zeta map, frame field, coefficients, source law, boundary theorem, and covariant origin missing.

Vacuum-substance accounting:
  balance skeleton written,
  J_v constrained to absent/local/compact/constraint/causal-if-derived classes,
  q_v/J_v optional bookkeeping,
  Sigma_creation excluded from ordinary regime.

Parent conservation:
  parent template v2 proposed,
  parent closure identity still missing.

Metric recombination:
  reduced bookkeeping map stated,
  scalar double-counting constraints added,
  covariant parent recombination missing.
```

The candidate system is therefore not yet a finished covariant theory.

It is a partially reconstructed field-equation architecture with one fully successful reduced exterior sector and a much more constrained scalar/vector/tensor/vacuum accounting structure.

---

# 15. Closure Failure Modes

Fatal closure failures:

```text
decorative parent identity,
scalar double-counting,
hidden breathing wave,
boundary smoothing tunes measured mass,
sector ledger mistaken for closure,
epsilon_vac_config becomes a repair reservoir,
kappa/zeta energy counted twice.
```

Major closure risks:

```text
silent GR metric import,
kappa repair knob,
zeta exterior scalar charge,
tensor coupling matched but claimed derived,
vector normalization matched but claimed derived,
active-regime leakage,
relaxation as energy loss,
near-boundary deviation overclaim,
coefficient tuning through vacuum reservoir,
J_v as acausal repair current,
scalar conversion becoming orbital damping.
```

Current controls:

```text
scalar double-counting constrained,
hidden breathing wave constrained,
active-regime leakage constrained,
near-boundary prediction overclaim controlled by diagnostic-before-prediction rule,
relaxation energy interpreted as vacuum-spacetime configuration exchange,
epsilon_vac_config excluded from A-sector mass and Sigma_creation,
J_v forbidden as far-zone scalar current or coefficient tuning knob,
e_kappa kept separate from epsilon_vac_config until kappa-zeta map is derived.
```

Still unresolved:

```text
parent identity derivation,
scalar constraint propagation,
tensor coupling,
vector normalization,
covariant recombination,
boundary mass theorem,
epsilon_vac_config parent derivation,
q_v/J_v meaning,
kappa-zeta map,
P_trace / P_boundary / P_recombination,
coefficient action/stiffness principle.
```

---

# 16. Group 12 Parent-Identity Constraints

Group 12 excluded false parent identities.

The parent identity cannot be:

```text
a decorative Bianchi restatement,
an ordinary scalar A wave,
Box kappa,
rho double-sourced into kappa,
nonzero exterior kappa charge,
trace contamination of TT,
longitudinal current sourcing W_i,
boundary smoothing changing exterior mass,
Sigma_creation in ordinary closure,
GR coefficients inserted as derivation,
metric recombination copied from GR.
```

Group 13 extends the exclusions to:

```text
Box zeta,
far-zone scalar zeta flux,
zeta exterior scalar charge,
epsilon_vac_config as repair reservoir,
J_v as acausal transport,
J_v as coefficient tuning current,
e_kappa double-counting inside epsilon_vac_config.
```

Any surviving parent identity must be:

```text
projector-routed,
scalar-safe,
TT-radiative,
kappa-first-order,
zeta-volume-geometric,
vacuum-spacetime-exchange-accounted,
boundary-mass-preserving,
recombination-safe,
coefficient-honest.
```

Template v2:

\[
{\rm Div}\,
E_{\rm parent}
[
A,W,h_{TT},\kappa;
P_{\rm scalar},P_T,P_{TT},P_{\rm trace},P_{\rm boundary}
]=
B_{\rm closed}[T]
+
B_{\rm relax}[\Gamma_{\rm relax},E_{\rm vac,config}].
\]

Status:

```text
CANDIDATE / SCAFFOLD ONLY
```

---

# 17. Vacuum-Substance Accounting Status

Best current interpretation:

```text
epsilon_vac_config:
  local vacuum-spacetime volume-configuration density

zeta:
  zeta = ln sqrt(gamma)

q_v, J_v:
  optional ontology-native density / current bookkeeping variables

E_boundary_config:
  possible interface contribution, diagnostic only
```

Excluded from \(\epsilon_{\rm vac,config}\):

```text
A-sector exterior mass charge,
Sigma_creation in ordinary regime,
coefficient tuning reservoir,
scalar kinetic wave term,
kappa mismatch energy until the kappa-zeta map is derived.
```

Provisional \(\epsilon_{\rm vac,config}\):

\[
\epsilon_{\rm vac,config}=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2.
\]

Separate \(\kappa\)-relaxation energy:

\[
e_\kappa=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Provisional exchange:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}=
0.
\]

Vacuum-accounting balance skeleton:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config} +
\nabla_\mu J_v^\mu =
\Sigma_{\rm exchange} - \Gamma_{\rm relax}.
\]

Ordinary constraints:

\[
\Sigma_{\rm creation}=0,
\]

\[
\oint J_v\cdot dS=0,
\]

\[
Q_{\rm volume}=0,
\]

\[
\delta M_{\rm ext}=0,
\]

\[
F_{\rm scalar,far}=0.
\]

Status:

```text
CANDIDATE / NOT DERIVED
```

---

# 18. Group 13 Vacuum-Substance Accounting Results

Group 13 established:

1. \(E_{\rm vac,config}\) should be geometric, not a generic reservoir.
2. \(\zeta=\ln\sqrt{\gamma}\) is the leading geometric candidate.
3. Trace modes change \(\zeta\); TT modes preserve \(\zeta\) at linear order.
4. Scalar / trace behavior should be treated as conversion, not ordinary damping.
5. Raw reduced coupling terms are dangerous until proven conservative.
6. Binary safety requires no far-zone scalar flux or secular scalar damping.
7. Local volume reconfiguration must have zero exterior charge.
8. \(J_v\) is optional and tightly constrained.
9. The first vacuum-accounting balance skeleton is now explicit.
10. \(\epsilon_{\rm vac,config}\) has a provisional \(\zeta\)-volume functional form.
11. \(e_\kappa\) remains separate for now to avoid double-counting.

Group 13 did not derive:

```text
u^mu,
zeta_min,
K_zeta,
L_zeta,
K_kappa,
Sigma_exchange,
Gamma_relax sign convention,
P_trace,
P_boundary,
P_recombination,
P_TT,
J_v transport law,
Q_volume,
S_volume,
boundary mass theorem,
binary scalar-safety theorem,
parent identity embedding,
kappa-zeta map.
```

---

# 19. Current Best Summary After Group 14

The current reduced field-equation system is coherent enough to present.

It is not closed.

Strongest result:

```text
Schwarzschild exterior from the A-sector.
```

Strongest structural result:

```text
a controlled sector split:
  scalar constraint,
  vector current response,
  TT tensor radiation,
  zeta volume-form configuration,
  non-radiative kappa trace relaxation,
  vacuum-spacetime exchange accounting.
```

Group 13 result:

```text
It made vacuum-substance accounting geometric enough to stop being a bucket.
It did not close the theory.
It revealed the next central problem: what exactly is kappa relative to zeta?
```

Group 14 result:

```text
Group 14 is closed.

It did not derive A_spatial.

It reduced the spatial-trace origin problem to J_V/u_vac.

Final bottleneck:
  define a real vacuum-volume current J_V^mu,
  or keep acceleration-gradient volume creation as a theorem target only.
```

Most important current missing relation is no longer only:

```text
kappa-zeta map.
```

The sharper current bottleneck is now:

```text
J_V / u_vac definition for vacuum-volume exchange.
```

Interpretation:

```text
A_spatial remains a recovery theorem target unless
a real vacuum-volume exchange current J_V can be defined.
```

Group 14 also established a useful negative result:

```text
do not continue ratio/frame relocation loops inside the kappa-zeta group.
```

The attempted chain was:

```text
A_spatial from local closure
  -> q

q from coupled stiffness
  -> c_x/c_s

q from conservation current
  -> a/b

q from parent balance
  -> E_parent ratio

volume exchange
  -> zeta status

zeta companion
  -> F_zeta

F_zeta
  -> Sigma_V

Sigma_V
  -> frame field u^mu

vacuum frame
  -> J_V

J_V
  -> not yet defined
```

This means Group 14 did not fail by wandering. It exposed the repeated hidden move:

```text
candidate mechanisms kept relocating the missing coefficient or clock.
```

The surviving non-decorative next problem is therefore:

```text
Can a real exchange continuity law define J_V?
```

---

# 20. Group 14 Closure Results

Group 14 closed the following questions.

## 20.1 What Group 14 Was Trying To Determine

Original purpose:

```text
map kappa/zeta/projector responsibilities and prevent scalar double-counting.
```

Sharpened purpose:

```text
determine whether A_spatial / spatial trace can be derived without:
  GR smuggling,
  gamma tuning,
  scalar double-counting,
  exterior scalar charge,
  or hidden scalar radiation.
```

Status:

```text
CLOSED AS SEARCH GROUP
```

It did not produce a final field equation for \(A_{\rm spatial}\).

It did produce a much narrower bottleneck.

---

## 20.2 Group 14 Closure Ledger

| Entry | Finding | Status | Consequence |
|---|---|---|---|
| G14-1: original group purpose | map kappa/zeta/projector responsibilities and prevent scalar double-counting | STRUCTURAL | projector accounting was sharpened into spatial-trace origin search |
| G14-2: \(A_{\rm spatial}\) origin target | derive \(A_{\rm spatial}\) / spatial trace without GR smuggling or gamma tuning | THEOREM_TARGET | became the central field-equation narrowing problem of the group |
| G14-3: local differential closure | local closure produces \(q\) but does not derive \(q\) | DEFER | coefficient origin became the bottleneck |
| G14-4: coupled stiffness route | coupled stiffness yields \(q=-c_x/c_s\) | DEFER | moved coefficient problem to stiffness ratio |
| G14-5: conservation-current route | minimal gradient current yields \(q=-a/b\) | DEFER | moved coefficient problem to current ratio |
| G14-6: parent balance route | parent balance requires explicit \(E_{\rm parent}\) and otherwise relocates ratio | DEFER | decorative balance and GR rewrite were rejected |
| G14-7: volume-exchange route | volume exchange is ontology-native but requires explicit \(V[A,B_s,\zeta]\) | CANDIDATE | forced zeta companion-versus-residual decision |
| G14-8: zeta status | \(\zeta\) cannot be both \(B_s\) companion and independent residual trace | REQUIRED | companion branch requires residual \(\zeta\) trace killed or non-metric |
| G14-9: \(F_\zeta\) map | algebraic \(F_\zeta\) maps are high-risk; source-driven maps need \(\Sigma_V[A,T]\) | DEFER | moved live branch to source-driven volume creation |
| G14-10: source-driven volume creation | best candidate is \(\Sigma_V\sim\chi\rho a^\mu\nabla_\mu A\) | CANDIDATE | requires frame/projection, \(\chi\)-origin, neutrality, and no-overlap |
| G14-11: frame field | matter frame is concrete but risky; vacuum frame is ontology-native but undefined | DEFER | moved live branch to \(u_{\rm vac}\) definition |
| G14-12: vacuum current | \(u_{\rm vac}\) best candidate is normalized \(J_V\), but \(J_V\) is not defined | UNRESOLVED | final surviving bottleneck is \(J_V/u_{\rm vac}\) |
| G14-13: closure decision | Group 14 should stop rather than continue ratio/frame relocation loops | CLOSED | promote \(J_V/u_{\rm vac}\) and exchange continuity to next group |

---

## 20.3 Branches Killed Or Rejected By Group 14

Rejected under the current ordinary-regime target constraints:

```text
free q chosen from gamma_like or AB

copy GR spatial metric or impose B=1/A by decree

raw kappa / Box kappa / Box zeta scalar radiation branches

zeta as both B_s companion and residual metric trace

coordinate velocity rho v dot grad A as parent source law

arbitrary preferred vacuum frame

decorative J_V or decorative Div E_parent

J_V = n_V u_vac used to define u_vac circularly
```

Interpretation:

```text
these are not metaphysical impossibilities;
they are forbidden under the current no-smuggling and ordinary-sector safety discipline.
```

---

## 20.4 Provisional Conventions Carried Forward

Group 14 carries forward these conventions:

```text
A_spatial remains a recovery theorem target, not a derived equation.

zeta may become B_s companion only if residual zeta trace is killed or non-metric.

if zeta remains residual, it does not solve A_spatial/q-origin.

kappa remains diagnostic/non-metric unless later branch proves otherwise.

gamma_like and AB are recovery checks, not construction tools.

boundary neutrality and no-overlap remain mandatory.

J_V/u_vac is the next-group bottleneck.
```

---

## 20.5 Final Bottleneck From Group 14

The surviving bottleneck is:

\[
J_V^\mu.
\]

Needed for:

\[
u_{\rm vac}^\mu
=
\frac{J_V^\mu}{\sqrt{-J_V^2}}.
\]

Strongest possible structure:

\[
\nabla_\mu J_V^\mu
=
\Sigma_V
-
R_V.
\]

Still missing:

```text
Sigma_V complete source law
R_V relaxation / exchange term
flux / transport direction
timelike / nonzero domain
boundary neutrality
no-overlap / residual-kill theorem
sign / orientation
chi-origin
```

Status:

```text
UNRESOLVED / NEXT-GROUP BOTTLENECK
```

---

# 21. Recommended Next Group

Recommended next group:

```text
15_vacuum_current_and_exchange_continuity
```

Locked door:

```text
Can a real exchange continuity law define J_V?
```

First script:

```text
candidate_exchange_continuity_law_for_volume.py
```

Purpose:

```text
test whether the strongest surviving structure from Group 14 can become a real law:
  nabla_mu J_V^mu = Sigma_V - R_V.
```

The continuity equation is not enough by itself.

A real exchange-continuity law must provide:

```text
J_V flux direction / transport law

Sigma_V source creation law

R_V relaxation / exchange law

timelike / nonzero domain for J_V

static-source neutrality

boundary neutrality

no-overlap / residual-kill theorem

sign / orientation convention

recovery checks downstream
```

Current Group 15 starter result:

```text
exchange continuity is the right next locked door,
but it is not yet a law.

J_V needs a flux direction,
not only a divergence equation.

Sigma_V and R_V must be defined separately.

static neutrality,
boundary neutrality,
and no-overlap remain mandatory.
```

Recommended next Group 15 script:

```text
candidate_sigma_R_split_for_volume_exchange.py
```

Purpose:

```text
split Sigma_V and R_V roles before claiming exchange continuity.
```

Reason:

```text
the continuity equation cannot define J_V until the source and relaxation/exchange terms are split and named.
```

---

# 22. Updated Minimal Honest Claim

The current field-equation status is:

```text
A-sector:
  real reduced reconstruction.

Vector sector:
  source/projection/action/shape reconstructed,
  normalization missing.

Tensor sector:
  TT structure identified,
  coupling and source identity missing.

Scalar radiation:
  ordinary long-range scalar radiation rejected / constrained,
  parent mechanism still missing.

Zeta / vacuum-volume sector:
  zeta = ln sqrt(gamma) identified as leading geometric volume-form candidate,
  epsilon_vac_config provisionally written as zeta-volume displacement plus gradient/interface energy,
  frame, measure, stiffnesses, and parent origin missing.

Kappa sector:
  role identified as constrained non-inertial trace / volume relaxation,
  e_kappa kept separate from epsilon_vac_config to avoid double-counting,
  kappa-zeta map remains unresolved but no longer the only central bottleneck.

A_spatial / spatial-trace origin:
  not derived.
  reduced to the J_V/u_vac bottleneck through Group 14.

Vacuum-current / exchange-continuity sector:
  J_V is the best current route to u_vac,
  but J_V is not defined.
  strongest candidate structure is nabla_mu J_V^mu = Sigma_V - R_V,
  with Sigma_V, R_V, and flux direction still missing.

Parent conservation:
  parent template v2 proposed,
  parent closure identity still missing.

Metric recombination:
  reduced bookkeeping map stated,
  scalar double-counting constraints added,
  covariant parent recombination missing.
```

The candidate system is therefore not yet a finished covariant theory.

It is a partially reconstructed field-equation architecture with:

```text
one fully successful reduced exterior sector,

a controlled scalar/vector/tensor/vacuum accounting structure,

and a newly identified next bottleneck:
  exchange continuity for J_V/u_vac.
```

---

# 23. Updated Closure Failure Modes

Fatal closure failures:

```text
decorative parent identity,
decorative exchange continuity,
decorative J_V,
scalar double-counting,
hidden breathing wave,
boundary smoothing tunes measured mass,
sector ledger mistaken for closure,
epsilon_vac_config becomes a repair reservoir,
kappa/zeta energy counted twice,
u_vac introduced as arbitrary preferred frame,
J_V defined circularly from u_vac.
```

Major closure risks:

```text
silent GR metric import,
kappa repair knob,
zeta exterior scalar charge,
tensor coupling matched but claimed derived,
vector normalization matched but claimed derived,
active-regime leakage,
relaxation as energy loss,
near-boundary deviation overclaim,
coefficient tuning through vacuum reservoir,
J_V as acausal repair current,
J_V as decorative flux,
scalar conversion becoming orbital damping,
exchange continuity written before Sigma_V/R_V are defined.
```

Current controls:

```text
scalar double-counting constrained,
hidden breathing wave constrained,
active-regime leakage constrained,
near-boundary prediction overclaim controlled by diagnostic-before-prediction rule,
relaxation energy interpreted as vacuum-spacetime configuration exchange,
epsilon_vac_config excluded from A-sector mass and Sigma_creation,
J_V/J_v forbidden as far-zone scalar current or coefficient tuning knob,
e_kappa kept separate from epsilon_vac_config until kappa-zeta map is derived,
u_vac not promoted without a non-circular J_V definition,
Group 14 closed to prevent further ratio/frame relocation loops.
```

Still unresolved:

```text
parent identity derivation,
scalar constraint propagation,
tensor coupling,
vector normalization,
covariant recombination,
boundary mass theorem,
epsilon_vac_config parent derivation,
q_v/J_v/J_V meaning,
vacuum-current flux law,
Sigma_V source law,
R_V relaxation/exchange law,
u_vac definition,
kappa-zeta map,
P_trace / P_boundary / P_recombination,
coefficient action/stiffness principle.
```
