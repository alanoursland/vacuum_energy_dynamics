# Field Equation Set — Current Reconstruction Status

## Scope

This document is a snapshot of the current field-equation architecture. It records what is reconstructed, what is only structural, what is constrained, what is rejected, and what remains unknown.

It is not a development log and not a proof of a completed covariant theory.

Audience: GR / relativistic field theory readers.

Status labels used below:

```text
DERIVED_REDUCED
STRUCTURAL
CONSTRAINED
MATCHED
RECOVERY_TARGET
THEOREM_TARGET
SAFE_IF
CANDIDATE
PROVISIONAL
REJECTED
MISSING
UNFINISHED
UNRESOLVED
RISK
```

---

# 1. Current Variables and Sector Split

## 1.1 Primary Fields

$$
A
$$

Scalar lapse / static mass-response field.

Status:

```text
DERIVED_REDUCED in static spherical sector
STRUCTURAL beyond reduced sector
```

$$
B_s \quad \text{or} \quad A_{\rm spatial}
$$

Scalar spatial response / spatial trace companion to the mass-response sector.

Status:

```text
RECOVERY_TARGET / THEOREM_TARGET
NOT DERIVED
```

It must be recovered by an acceptable parent equation, not copied from the GR metric form or imposed by $\gamma_{\rm like}=1$ tuning.

$$
\zeta=\ln\sqrt{\gamma}
$$

Candidate vacuum-spacetime volume configuration variable.

Status:

```text
CANDIDATE / GEOMETRICALLY MOTIVATED / FRAME-DEPENDENT
```

$$
\kappa
$$

Reduced trace / volume / interior relaxation diagnostic. The areal relation

$$
\kappa_{\rm areal}=\frac12\ln(AB)
$$

is a reduced areal-gauge diagnostic, not a covariant physical scalar unless later derived.

Status:

```text
DIAGNOSTIC / NON-METRIC / SEPARATELY NEUTRAL UNLESS DERIVED
```

$$
W_i
$$

Transverse vector current / frame-dragging candidate.

Status:

```text
STRUCTURAL / NORMALIZATION UNKNOWN
```

$$
h_{ij}^{TT}
$$

Transverse-traceless tensor radiation field.

Status:

```text
STRUCTURAL / ORDINARY RADIATIVE SECTOR
```

$$
A_{\rm rad}
$$

Scalar breathing/radiative hazard.

Status:

```text
REJECTED as ordinary active long-range degree of freedom
```

---

## 1.2 Vacuum-Volume / Exchange Variables

$$
J_V^\mu
$$

Candidate vacuum-volume flux / transport current needed to define a vacuum frame.

Status:

```text
UNRESOLVED
```

It is not defined by naming it and is not defined by the divergence equation alone.

$$
u_{\rm vac}^\mu = \frac{J_V^\mu}{\sqrt{-J_V^2}}
$$

Candidate vacuum rest frame, valid only where $J_V$ is timelike and nonzero.

Domain condition:

$$
D_V=\{J_V^2<0,\;J_V\neq0\}.
$$

Status:

```text
THEOREM_TARGET / DOMAIN-LIMITED / UNRESOLVED
```

$$
\Sigma_V
$$

Vacuum-volume source / creation / destruction side of exchange accounting.

Status:

```text
ROLE-LEVEL ONLY / OPERATOR NOT DERIVED
```

$$
R_V
$$

Vacuum-volume relaxation / reconfiguration / return side of exchange accounting.

Status:

```text
ROLE-LEVEL ONLY / OPERATOR NOT DERIVED
```

$$
O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual},J_V]
$$

No-overlap operator target for count-once recombination.

Status:

```text
UNRESOLVED CENTRAL BOTTLENECK
```

---

# 2. Current Recombination Constraint

The recombination map is reduced bookkeeping, not a covariant parent derivation.

Current safe recombination statement:

```text
g_tt <- A

g_0i <- W_i

g_ij <- B_s / A_spatial scalar response
        + h_TT
        + killed, non-metric, or separately neutral residual bookkeeping
```

Unsafe loose form:

```text
g_ij <- A_spatial + zeta_residual + kappa_residual + h_TT
```

Reason:

```text
This risks double-counting the scalar spatial trace.
```

Current count-once rule:

```text
J_V-driven zeta may enter ordinary metric scalar trace only through B_s,
with residual zeta/kappa metric trace killed or made non-metric,
unless a real no-overlap operator O is later derived.
```

Residual-kill convention:

```text
If J_V-driven zeta enters B_s,
then residual zeta/kappa metric trace is killed or made non-metric.
```

Status:

```text
SAFE_IF / PROVISIONAL
NOT DERIVED
```

Revisit triggers:

```text
explicit no-overlap operator O is derived,
neutral residual branch becomes structurally safe,
B_s/F_zeta insertion law changes,
kappa obtains separately derived no-overlap status,
parent identity derives residual-kill or residual survival,
real J_V flux law changes recombination structure.
```

---

# 3. Scalar Static / Monopole Sector

## 3.1 Areal-Flux Law

Primary reduced scalar equation:

$$
\Delta_{\rm areal}A =
\frac{8\pi G}{c^2}\rho.
$$

where:

$$
\Delta_{\rm areal}A =
\frac{1}{r^2}\frac{d}{dr}
\left(r^2\frac{dA}{dr}\right).
$$

Equivalent flux form:

$$
F_A(r)=4\pi r^2 A'(r),
$$

$$
\frac{dF_A}{dr}=4\pi r^2\frac{8\pi G}{c^2}\rho(r).
$$

With:

$$
M_{\rm enc}'(r)=4\pi r^2\rho(r),
$$

this gives:

$$
F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).
$$

Status:

```text
DERIVED_REDUCED
```

This is the strongest reconstructed sector.

---

## 3.2 Exterior Vacuum Scalar Equation

For $\rho=0$,

$$
\Delta_{\rm areal}A=0.
$$

Thus:

$$
\frac{d}{dr}\left(r^2A'\right)=0,
$$

and:

$$
A(r)=C_0+\frac{C_1}{r}.
$$

Asymptotic flatness sets:

$$
C_0=1.
$$

Flux normalization by total mass $M$ gives:

$$
A(r)=1-\frac{2GM}{c^2r}.
$$

Status:

```text
DERIVED_REDUCED
```

---

## 3.3 Exterior Radial Factor

In the static spherical exterior, the reduced areal diagnostic condition is:

$$
\kappa_{\rm areal}=0.
$$

With:

$$
AB=e^{2\kappa_{\rm areal}},
$$

this gives:

$$
AB=1,
$$

so:

$$
B=\frac{1}{A}.
$$

Therefore:

$$
B(r)=\left(1-\frac{2GM}{c^2r}\right)^{-1}.
$$

Status:

```text
DERIVED_REDUCED / GAUGE-CONDITIONED / RECOVERY CHECK
```

Important boundary:

```text
B=1/A is not a general construction rule for the parent theory.
It is a recovered static spherical exterior relation.
```

---

# 4. Weak Multipole Scalar Extension

For weak fields:

$$
A\simeq1+\frac{2\Phi}{c^2}.
$$

The scalar field recovers the Newtonian potential structure:

$$
\nabla^2\Phi=4\pi G\rho.
$$

Exterior weak multipole expansion:

$$
\Phi(\mathbf{x})=
-G\int\frac{\rho(\mathbf{x}')}{|\mathbf{x}-\mathbf{x}'|}\,d^3x'.
$$

Thus:

$$
A(\mathbf{x})\simeq1+\frac{2\Phi(\mathbf{x})}{c^2}.
$$

The spatial response must recover GR-compatible weak-field scalar spatial curvature, but the mechanism producing $B_s/A_{\rm spatial}$ is not derived.

Status:

```text
A weak scalar shape: DERIVED_REDUCED / WEAK-FIELD
B_s / gamma-like response: RECOVERY_TARGET / NOT DERIVED
```

Limit:

```text
Not yet full nonlinear nonspherical field equation.
Not yet full PPN audit.
```

---

# 5. Scalar Radiative Sector

An unconstrained scalar radiative perturbation would have the form:

$$
A_{\rm rad}=a_0\cos(kx-\omega t),
$$

with wave condition:

$$
\omega^2=c^2k^2.
$$

This would be a scalar breathing-type gravitational radiation channel.

Current rule:

$$
{\rm source}(A_{\rm rad}\ {\rm ordinary\ massless})=0.
$$

Rejected as ordinary scalar-radiation equations:

$$
\Box\kappa=\alpha S,
$$

$$
\Box\zeta=\alpha S.
$$

Interpretation:

```text
Scalar / trace disturbances are conversion-limited,
not ordinary far-zone scalar waves.
```

Ordinary radiation rule:

```text
ordinary long-range gravitational radiation is TT-only.
```

Status:

```text
REJECTED / CONSTRAINED
```

Failure if violated:

```text
breathing radiation,
scalar double-counting,
far-zone scalar flux,
secular orbital damping,
or an exterior scalar channel not supported by the current theory.
```

---

# 6. Vacuum-Volume / Exchange-Continuity Sector

## 6.1 Ontology

Current ontology:

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

$$
\zeta=\ln\sqrt{\gamma}.
$$

Physical volume element:

$$
dV_{\rm phys}=\sqrt{\gamma}\,d^3x.
$$

Linear variation:

$$
\delta\zeta=\frac12\gamma^{ij}\delta\gamma_{ij}.
$$

For TT perturbations:

$$
\gamma^{ij}h_{ij}^{TT}=0,
$$

so:

$$
\delta\zeta|_{TT}=0.
$$

Interpretation:

```text
trace / volume modes change vacuum-spacetime amount,
TT modes are volume-preserving shear.
```

---

## 6.2 Exchange Continuity Target

Current exchange-continuity theorem target:

$$
\nabla_\mu J_V^\mu=\Sigma_V-R_V.
$$

Status:

```text
THEOREM_TARGET
NOT A LAW
```

Reason:

```text
A divergence equation constrains a current.
It does not define the current.
```

A real exchange-continuity law still requires:

```text
J_V physical flux / transport law,
Sigma_V source operator,
R_V relaxation / return operator,
flux direction,
timelike / nonzero domain,
static-source neutrality,
boundary neutrality,
no-overlap or residual-kill theorem,
sign / orientation convention,
recovery checks downstream.
```

---

## 6.3 Sigma/R Split

Current split:

```text
Sigma_V:
  source / creation / destruction side

R_V:
  relaxation / reconfiguration / return side
```

Status:

```text
STRUCTURAL / ROLE-LEVEL ONLY
NOT OPERATOR-LEVEL
```

Guardrail:

```text
Sigma_V and R_V must not become two names for one hidden tuning mechanism.
```

Rejected:

```text
R_V tuned to erase exterior scalar charge,
Sigma_V chosen from gamma_like or AB recovery,
Sigma_V and R_V double-counting the same volume change,
Sigma/R balancing by definition with no mechanism.
```

---

## 6.4 Flux Direction

Key result:

```text
Sigma_V - R_V supplies divergence strength,
not vector direction.
```

Status:

```text
REQUIRED GUARDRAIL
```

Distinctions:

```text
physical flux law:
  derived direction / transport mechanism

diagnostic elliptic completion:
  solve div J_V = Sigma_V - R_V after the fact as an audit

forbidden repair current:
  choose J_V nonlocally to cancel exterior scalar charge
```

Only the first can become ontology.

The second may be useful diagnostically.

The third is rejected.

Candidate direction families remain:

```text
exchange-potential flux,
causal first-order transport current,
compact-support redistribution,
zeta-gradient flux,
source-gradient flux,
relaxation-gradient flux.
```

None is derived.

Causal transport remains dangerous unless it avoids:

```text
Box zeta,
Box kappa,
ordinary scalar radiation.
```

---

## 6.5 Timelike / Nonzero Domain

Candidate vacuum-frame definition:

$$
u_{\rm vac}^\mu=\frac{J_V^\mu}{\sqrt{-J_V^2}}.
$$

This only makes sense on:

$$
D_V=\{J_V^2<0,\;J_V\neq0\}.
$$

Status:

```text
THEOREM_TARGET / DOMAIN-LIMITED
```

Implications:

```text
No global u_vac follows from a domain-limited current.

Zero-current static equilibrium may protect neutrality,
but it cannot define u_vac from J_V.

Spacelike redistribution currents may be spatial fluxes,
but not vacuum clocks.

Equilibrium-frame fallback is deferred unless static regions require a frame.
```

---

## 6.6 Static-Source Neutrality

Ordinary static sources must not create independent exterior scalar volume charge.

Allowed safety routes, all still conditional:

```text
static zero-current equilibrium,
pointwise Sigma_V = R_V balance,
compact-support J_V with zero boundary flux.
```

Forbidden:

```text
ordinary static mass creates exterior zeta/kappa/J_V scalar charge,
R_V is tuned to cancel that charge,
source-gradient creates shell scalar charge,
zeta-gradient current produces far-zone scalar tail,
acceleration-gradient source treats static support as scalar source without neutrality theorem,
J_V shifts M_ext independently of A-sector.
```

Status:

```text
REQUIRED / NOT DERIVED
```

Failure condition:

```text
static scalar charge kills the current family for ordinary gravity.
```

---

## 6.7 Boundary Neutrality

Surviving current families must satisfy:

```text
zero exterior J_V flux,
zero exterior zeta/kappa charge,
no far-zone scalar flux,
no M_ext shift.
```

Status:

```text
REQUIRED / NOT DERIVED
```

Forbidden boundary moves:

```text
nonlocal boundary repair current,
R_V boundary counterterm tuned to cancel leakage,
surface term hiding residual trace overlap,
shell-source created by sharp support,
recovery checks choosing boundary conditions.
```

---

# 7. Kappa / Zeta / Residual Sector

## 7.1 Current Role of Kappa

Current best interpretation:

```text
kappa = reduced diagnostic / non-metric residual / separately neutral trace variable unless derived.
```

Areal-gauge diagnostic relation:

$$
\kappa_{\rm areal}=\frac12\ln(AB).
$$

Exterior Schwarzschild sector:

$$
\kappa_{\rm areal}=0.
$$

Status:

```text
STRUCTURAL / DIAGNOSTIC
```

Guardrail:

```text
kappa must not restore killed zeta residual trace.
```

Forbidden:

```text
kappa as substitute scalar metric trace,
kappa as independent scalar gravity,
kappa as hidden residual-restoration path,
e_kappa as physical source reservoir before derivation.
```

---

## 7.2 Current Role of Zeta

$$
\zeta=\ln\sqrt{\gamma}
$$

is the leading volume-form candidate.

Current role:

```text
geometric vacuum-volume candidate,
possible B_s companion only under residual-kill or no-overlap.
```

Forbidden:

```text
zeta changes B_s and also remains independent residual metric trace.
```

---

## 7.3 Residual-Kill Convention

Current provisional convention:

```text
If J_V-driven zeta enters B_s,
residual zeta/kappa metric trace is killed or made non-metric.
```

Meaning:

```text
zeta_residual_metric = 0 after B_s insertion,

kappa_residual_metric = 0
  or kappa remains diagnostic / non-metric / separately neutral,

zeta/kappa residual may remain as bookkeeping,
  but not as direct metric scalar trace,

P_relax-only residual may survive only if first-order,
  non-radiative,
  boundary-neutral,
  and not Box zeta / Box kappa.
```

Status:

```text
SAFE_IF / PROVISIONAL
NOT DERIVED
```

---

## 7.4 Neutral Residual Alternative

The theorem-heavy alternative is:

```text
neutral residual metric trace,
allowed only if O, boundary neutrality, no A-sector mass overlap,
and no exterior scalar charge are all derived.
```

Status:

```text
RISK / THEOREM-HEAVY
```

---

## 7.5 Rejected Kappa / Zeta Interpretations

Rejected as ordinary propagating scalar gravity:

$$
\Box\kappa=\alpha S,
$$

$$
\Box\zeta=\alpha S.
$$

Rejected as ordinary exterior scalar channels:

```text
raw pressure trace Poisson kappa,
zeta exterior scalar charge,
kappa exterior scalar charge,
zeta/kappa independent scalar gravities,
kappa restoring killed residual metric trace.
```

---

## 7.6 Energy / Accounting Guardrail

Provisional vacuum-volume functional:

$$
\epsilon_{\rm vac,config}=
\frac12K_\zeta(\zeta-\zeta_{\min})^2+
\frac12L_\zeta|\nabla\zeta|^2.
$$

Separate kappa relaxation energy:

$$
e_\kappa=\frac12K_\kappa(\kappa-\kappa_{\min})^2.
$$

Guardrail:

```text
epsilon_vac_config / e_kappa cannot count killed residual as extra source energy.
```

Allowed:

```text
diagnostic bookkeeping,
configuration accounting,
count-once recombination if a mechanism is derived.
```

Forbidden:

```text
killed residual reappears as physical energy source,
energy term becomes coefficient reservoir,
vacuum accounting shifts M_ext independently,
e_kappa restores scalar trace through the back door.
```

Status:

```text
CANDIDATE / PROVISIONAL / NOT DERIVED
```

---

# 8. Vector Current / Frame-Dragging Sector

Matter continuity:

$$
\partial_t\rho+\nabla\cdot j=0,
$$

with:

$$
j_i=\rho v_i.
$$

Decompose:

$$
j=j_T+j_L,
$$

with:

$$
\nabla\cdot j_T=0,
$$

$$
\nabla\times j_L=0.
$$

Fourier-space projector:

$$
P_T(k)=I-\frac{kk^T}{k^2}.
$$

Sector allocation:

$$
j_T\rightarrow W_i,
$$

$$
j_L\rightarrow A\text{ / scalar continuity}.
$$

Candidate vector energy:

$$
E_W=\int\left[K_c|\nabla\times W|^2+\alpha_W j_T\cdot W\right]d^3x.
$$

Variation gives:

$$
\nabla\times(\nabla\times W)=-\frac{\alpha_W}{2K_c}j_T.
$$

Under $\nabla\cdot W=0$:

$$
\Delta W=\frac{\alpha_W}{2K_c}j_T.
$$

Status:

```text
STRUCTURAL / DERIVED_REDUCED SHAPE
NORMALIZATION UNKNOWN
```

Observable candidate:

$$
B_W=\nabla\times W,
$$

$$
\Omega_{\rm drag}=\beta_W B_W.
$$

Unknowns:

```text
alpha_W/K_c,
beta_W,
source convention factors,
gauge-invariant observable extraction.
```

---

# 9. Tensor Radiation Sector

Tensor radiation variable:

$$
h_{ij}^{TT}.
$$

Conditions:

$$
\partial_i h_{ij}^{TT}=0,
$$

$$
\delta^{ij}h_{ij}^{TT}=0.
$$

Candidate tensor equation:

$$
\Box h_{ij}^{TT}=-\mathcal{C}_T S_{ij}^{TT}.
$$

GR target form:

$$
\Box h_{ij}^{TT}=-\frac{16\pi G}{c^4}T_{ij}^{TT}.
$$

Current status:

```text
TT structure: STRUCTURAL / RECOVERED SHAPE
wave equation form: STRUCTURAL
coefficient: MATCHED / UNKNOWN
source identity: UNFINISHED
```

Tensor energy flux scaling:

$$
F_T\sim K_T\langle\dot h_{ij}^{TT}\dot h_{ij}^{TT}\rangle.
$$

GR target:

$$
F_{\rm GR}=\frac{c^3}{32\pi G}\langle\dot h_{ij}^{TT}\dot h_{ij}^{TT}\rangle.
$$

Status:

```text
STRUCTURAL / MATCHED
COEFFICIENT NOT DERIVED
```

---

# 10. Source Coupling, Projectors, and No-Double-Counting

Current source assignments:

| Sector                | Source                                          | Status                           |
| --------------------- | ----------------------------------------------- | -------------------------------- |
| $A$                   | $\rho$, $M_{\rm enc}$, scalar mass response     | DERIVED_REDUCED / STRUCTURAL     |
| $B_s/A_{\rm spatial}$ | scalar spatial response companion               | RECOVERY_TARGET / THEOREM_TARGET |
| $W_i$                 | $j_T=P_T(\rho v)$                               | STRUCTURAL / CONSTRAINED         |
| $\zeta$               | volume configuration / possible $B_s$ companion | CANDIDATE / UNFINISHED           |
| $\kappa$              | diagnostic / non-metric residual unless derived | CONSTRAINED                      |
| $h_{ij}^{TT}$         | trace-free quadrupole / $P_{TT}T_{ij}$          | STRUCTURAL / COEFFICIENT MATCHED |
| $A_{\rm rad}$         | ordinary long-range scalar radiation            | REJECTED / CONSTRAINED           |
| $J_V$                 | vacuum-volume current                           | UNRESOLVED                       |
| $\Sigma_V$            | volume source / creation side                   | ROLE-LEVEL ONLY                  |
| $R_V$                 | relaxation / return side                        | ROLE-LEVEL ONLY                  |
| $O$                   | no-overlap operator                             | UNRESOLVED                       |

Required routing constraints:

```text
rho / scalar charge -> A only,

longitudinal current -> scalar continuity / density redistribution,

transverse current -> W_i,

TT stress -> h_ij^TT,

J_V-driven zeta -> B_s only if residual zeta/kappa metric trace is killed or non-metric,

residual zeta/kappa -> non-metric bookkeeping, diagnostic, or separately neutral unless O is derived,

ordinary scalar radiation -> rejected.
```

No-double-counting rules:

```text
zeta cannot enter both B_s and residual metric trace,

kappa cannot restore killed zeta residual trace,

epsilon_vac_config and e_kappa cannot count killed residual as extra source energy,

J_V cannot shift M_ext independently of A-sector,

Sigma_V and R_V cannot be two names for one hidden tuning mechanism,

recovery checks cannot choose coefficients, boundary behavior, residual status, or overlap split.
```

Status:

```text
CONSTRAINED / NOT YET PARENT-DERIVED
```

---

# 11. Constraint / Evolution Split

Current best split:

| Variable              | Equation Type                                   | Status                        |
| --------------------- | ----------------------------------------------- | ----------------------------- |
| $A$                   | elliptic / scalar constraint                    | DERIVED_REDUCED               |
| $B_s/A_{\rm spatial}$ | scalar spatial response                         | RECOVERY_TARGET / NOT DERIVED |
| $A_{\rm rad}$         | ordinary scalar radiation                       | REJECTED / CONSTRAINED        |
| $\zeta$               | volume configuration / possible $B_s$ companion | CANDIDATE / FRAME-DEPENDENT   |
| $\kappa$              | diagnostic / non-metric residual unless derived | CONSTRAINED                   |
| $J_V$                 | vacuum-volume flux / transport current          | UNRESOLVED                    |
| $u_{\rm vac}$         | vacuum rest frame from $J_V$, if domain exists  | UNRESOLVED / DOMAIN-LIMITED   |
| $\Sigma_V$            | volume source role                              | ROLE-LEVEL ONLY               |
| $R_V$                 | relaxation / return role                        | ROLE-LEVEL ONLY               |
| $W_i$                 | transverse vector response                      | STRUCTURAL                    |
| $h_{ij}^{TT}$         | hyperbolic tensor evolution                     | STRUCTURAL                    |
| source identities     | continuity / Bianchi-like closure               | MISSING                       |
| recombination         | count-once metric map                           | UNFINISHED                    |

Radiation rule:

```text
ordinary long-range gravitational radiation is TT-only.
```

Constrained or rejected:

```text
A_rad ordinary scalar radiation,
kappa breathing radiation,
zeta scalar radiation,
free vector radiation not currently derived.
```

---

# 12. Current Minimal Candidate Field System

A compact presentation of the current system is:

$$
\boxed{\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho}
$$

Status:

```text
DERIVED_REDUCED
```

$$
\boxed{A_{\rm ext}(r)=1-\frac{2GM}{c^2r}}
$$

Status:

```text
DERIVED_REDUCED
```

$$
\boxed{AB=e^{2\kappa_{\rm areal}}}
$$

Status:

```text
DEFINITION / REDUCED AREAL-GAUGE DIAGNOSTIC
```

Exterior diagnostic condition:

$$
\boxed{\kappa_{\rm areal}=0}
$$

therefore:

$$
\boxed{B=\frac{1}{A}}
$$

Status:

```text
DERIVED_REDUCED in static spherical exterior
NOT GENERAL PARENT CONSTRUCTION
```

Weak scalar limit:

$$
\boxed{A\simeq1+\frac{2\Phi}{c^2},\qquad \nabla^2\Phi=4\pi G\rho}
$$

Status:

```text
DERIVED_REDUCED / WEAK-FIELD
```

Volume-form candidate:

$$
\boxed{\zeta=\ln\sqrt{\gamma}}
$$

with:

$$
\boxed{\delta\zeta=\frac12\gamma^{ij}\delta\gamma_{ij}},
$$

and:

$$
\boxed{\delta\zeta|_{TT}=0.}
$$

Status:

```text
CANDIDATE / LINEAR STRUCTURAL
```

Vector response:

$$
\boxed{\nabla\times(\nabla\times W)=-\frac{\alpha_W}{2K_c}j_T}
$$

with:

$$
j_T=P_Tj.
$$

Status:

```text
STRUCTURAL / COEFFICIENT UNKNOWN
```

Vacuum exchange theorem target:

$$
\boxed{\nabla_\mu J_V^\mu=\Sigma_V-R_V}
$$

Status:

```text
THEOREM_TARGET / NOT A LAW
```

Vacuum-frame candidate:

$$
\boxed{u_{\rm vac}^\mu=\frac{J_V^\mu}{\sqrt{-J_V^2}}}
$$

only on:

$$
\boxed{D_V=\{J_V^2<0,\;J_V\neq0\}.}
$$

Status:

```text
THEOREM_TARGET / DOMAIN-LIMITED / UNRESOLVED
```

No-overlap theorem target:

$$
\boxed{O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual},J_V]=0}
$$

Status:

```text
UNRESOLVED
```

Residual-kill convention:

$$
\boxed{J_V\text{-driven }\zeta\rightarrow B_s
\quad\Rightarrow\quad
\zeta_{\rm residual,metric}=0,
\quad
\kappa_{\rm residual,metric}=0\text{ or non-metric}}
$$

Status:

```text
SAFE_IF / PROVISIONAL / NOT DERIVED
```

Tensor radiation:

$$
\boxed{\Box h_{ij}^{TT}=-\mathcal{C}_T S_{ij}^{TT}}
$$

Status:

```text
STRUCTURAL / SOURCE AND COEFFICIENT UNFINISHED
```

Rejected scalar-radiation equations:

$$
\boxed{\Box\kappa=\alpha S}
$$

$$
\boxed{\Box\zeta=\alpha S}
$$

Status:

```text
REJECTED as ordinary scalar gravity
```

Parent closure target:

$$
\boxed{\text{Div}\,E_{\rm parent}[\cdots]=B_{\rm closed}[T]+B_{\rm relax}[\cdots]}
$$

Status:

```text
MISSING / TEMPLATE ONLY
```

This is not closure.

---

# 13. GR Recovery Audit

## Real Reduced Reconstruction

Static spherical exterior:

$$
A=1-\frac{2GM}{c^2r},
$$

$$
B=\frac{1}{A}.
$$

Status:

```text
RECONSTRUCTED / DERIVED_REDUCED
```

This is the strongest current result.

---

## Strong Reduced / Structural Support

Weak scalar multipole shape:

$$
A\simeq1+\frac{2\Phi}{c^2}.
$$

Status:

```text
RECONSTRUCTED AT WEAK ORDER
```

Reduced weak $\gamma=1$ behavior:

```text
RECOVERY_TARGET / REDUCED SUPPORT
NOT FULL PPN AUDIT
NOT A CONSTRUCTION RULE
```

Vector current shape:

```text
j_i = rho v_i,
j_T = P_T j,
B_W = curl W,
B_W ~ J/r^3.
```

Status:

```text
STRUCTURE RECONSTRUCTED
NORMALIZATION NOT RECONSTRUCTED
```

Tensor TT structure:

```text
plus/cross TT modes and quadrupole source form.
```

Status:

```text
STRUCTURE RECONSTRUCTED
COUPLING NOT RECONSTRUCTED
```

---

## Recovery Scorecard

| Result                                       | Status                              |
| -------------------------------------------- | ----------------------------------- |
| static spherical exterior $A$                | DERIVED_REDUCED                     |
| exterior $B=1/A$ once $\kappa_{\rm areal}=0$ | DERIVED_REDUCED / GAUGE-CONDITIONED |
| weak scalar / Newtonian limit                | DERIVED_REDUCED                     |
| weak spatial scalar response                 | RECOVERY_TARGET / NOT DERIVED       |
| full PPN audit                               | MISSING                             |
| frame-dragging shape $\sim J/r^3$            | DERIVED_REDUCED shape               |
| frame-dragging normalization                 | MATCHED / UNKNOWN                   |
| tensor wave TT structure                     | STRUCTURAL                          |
| tensor coupling                              | MATCHED / UNKNOWN                   |
| tensor flux coefficient                      | MATCHED / UNKNOWN                   |
| no scalar breathing radiation                | CONSTRAINED                         |
| $\kappa$ non-radiative status                | CONSTRAINED / UNFINISHED            |
| $J_V/u_{\rm vac}$                            | UNRESOLVED                          |
| no-overlap $O$                               | UNRESOLVED                          |
| residual-kill                                | SAFE_IF / PROVISIONAL               |
| parent conservation / Bianchi compatibility  | MISSING                             |
| covariant metric recombination               | UNFINISHED                          |

---

# 14. Major Unknowns

Core missing objects:

$$
J_V^\mu
$$

physical vacuum-volume flux / transport current.

$$
\Sigma_V
$$

volume source operator.

$$
R_V
$$

relaxation / return operator.

$$
u_{\rm vac}^\mu
$$

vacuum frame, definable from $J_V$ only on a timelike / nonzero domain if $J_V$ exists.

$$
O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual},J_V]
$$

no-overlap operator.

$$
B_s/F_\zeta
$$

metric insertion law connecting volume response to scalar spatial trace.

$$
\frac{\alpha_W}{K_c},\;\beta_W,\;C_{\rm shape}
$$

vector normalization and observable coupling.

$$
\mathcal{C}_T,\;K_T
$$

tensor coupling and radiation-energy coefficient.

$$
K_\zeta,\;L_\zeta,\;\zeta_{\min}
$$

volume-configuration stiffnesses and equilibrium configuration.

$$
K_\kappa,\;\mu_\kappa,\;\lambda_\kappa,\;\chi_\kappa
$$

kappa relaxation parameters if a non-metric / relaxation branch survives.

Projectors / operators still missing or unresolved:

```text
P_scalar,
P_TT,
P_trace,
P_relax,
P_boundary,
P_recombination,
P_coeff,
O no-overlap operator.
```

Structural unknowns:

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
timelike/nonzero active domain,
equilibrium-frame fallback,
static-source neutrality theorem,
boundary neutrality theorem,
no-overlap operator O,
residual-kill derivation or parent identity,
kappa cleanup,
B_s/F_zeta insertion law,
coefficient action/stiffness principle.
```

---

# 15. Minimal Honest Claim

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
  role identified as diagnostic / non-metric / constrained trace residual unless derived,
  e_kappa kept separate from epsilon_vac_config to avoid double-counting,
  kappa-zeta map remains unresolved,
  kappa must not restore killed zeta residual trace.

A_spatial / B_s spatial-trace origin:
  not derived,
  remains a recovery theorem target,
  J_V-driven zeta may enter ordinary metric trace only through B_s,
  with residual zeta/kappa metric trace killed or non-metric,
  unless a real no-overlap operator O is later derived.

Vacuum-current / exchange-continuity sector:
  J_V remains undefined,
  u_vac remains unresolved / domain-limited,
  strongest candidate structure is nabla_mu J_V^mu = Sigma_V - R_V,
  but this is a theorem target, not a law,
  Sigma_V and R_V are split only at role level,
  flux direction is missing.

Parent conservation:
  parent template proposed,
  parent closure identity still missing.

Metric recombination:
  reduced bookkeeping map stated,
  scalar double-counting constraints sharpened,
  no-overlap O unresolved,
  residual-kill / non-metric residual is the safest provisional convention.
```

The candidate system is therefore not yet a finished covariant theory.

It is a partially reconstructed field-equation architecture with:

```text
one fully successful reduced exterior sector,

a controlled scalar/vector/tensor/vacuum accounting structure,

and a sharpened current bottleneck:
  real J_V + no-overlap / residual-kill mechanism.
```

---

# 16. Closure Failure Modes

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
J_V defined circularly from u_vac,
residual-kill treated as derived,
zeta enters both B_s and residual metric trace.
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
exchange continuity written before Sigma_V/R_V are defined,
neutral residual assumed without O,
P_relax becoming Box zeta / Box kappa.
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
residual-kill marked provisional,
O marked unresolved.
```

---

# 17. Recommended Next Technical Target

Do not immediately write a parent field equation.

The next technical target should be framed as a known unknown, not a completed equation:

```text
Can J_V-driven zeta enter B_s through a concrete metric insertion law
while residual zeta/kappa metric trace is killed or non-metric?
```

Equivalent bottleneck:

```text
derive B_s/F_zeta insertion,
or derive a parent identity for no-overlap / residual-kill,
or keep J_V-driven zeta out of the ordinary metric scalar sector.
```

Candidate next artifact title, if needed:

```text
candidate_B_s_F_zeta_insertion_law.py
```

or:

```text
candidate_parent_identity_for_residual_kill.py
```

---

# 18. Final Current Summary

After the current update, the field-equation status is:

```text
A-sector remains the strongest reduced branch.

A_spatial / B_s remains a recovery theorem target.

J_V / u_vac remains unresolved.

Exchange continuity remains a theorem target, not a law.

Sigma/R split is role-level only.

Flux direction is missing.

No-overlap O remains unresolved.

Residual-kill / non-metric residual is the safest provisional convention.

Kappa remains diagnostic / non-metric unless derived.

The theory should not yet write a final parent equation.
```
