# Field Equation Set — Current Licensed State and Constraint Architecture

## Purpose

This document records the current licensed state of the field-equation architecture. It states what is reconstructed, structural, constrained, rejected, unresolved, theorem-targeted, diagnostic, or not yet ready.

It is not a development log. It is not a proof of a completed covariant theory. It is a current progress snapshot whose central content is the constraint architecture: which equations, variables, insertions, recoveries, currents, projectors, and correction objects are presently licensed, blocked, provisional, or missing.

Audience: GR / relativistic field theory readers.

## Reading Rule

The main body is organized by current license status, not by discovery order. Historical audit labels and group-by-group development history are preserved only in the provenance appendix.

The main body answers:

```text
What is currently allowed?
What is currently derived?
What is currently structural only?
What is diagnostic only?
What is rejected?
What is theorem-targeted?
What is not ready?
What must not be smuggled in through recovery, boundary repair, source rerouting, or undefined operators?
```

## Section Pattern

Most sections use the following structure:

```text
Current role
Current status
Licensed use
Current constraints
Not licensed
Proof / witness status
Open obligations
```

---

# 1. Executive Snapshot

The strongest reconstructed branch is the reduced scalar mass-response sector, governed in the static spherical reduced setting by

\[
\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho.
\]

The reduced static spherical exterior gives

\[
A_{\rm ext}(r)=1-\frac{2GM}{c^2r}.
\]

The protected reduced ordinary exterior mass reference is the A-sector areal-flux charge

\[
F_A=4\pi r^2A'(r),
\qquad
M_A=\frac{c^2F_A}{8\pi G}.
\]

For the reduced exterior branch above, this gives \(M_A=M\). This is the current reduced mass coin for ordinary exterior audits. It is not a final covariant parent mass definition.

The reduced exterior relation

\[
B=\frac1A
\]

is recovered only in the static spherical exterior after the reduced areal diagnostic condition

\[
\kappa_{\rm areal}=0,
\qquad
\kappa_{\rm areal}=\frac12\ln(AB).
\]

This relation is a recovery check, not a general parent-theory construction rule.

The central unresolved burden is licensed metric recombination: deriving the scalar spatial response \(B_s/F_\zeta\), count-once scalar trace insertion, residual-kill or active no-overlap, boundary neutrality, scalar silence, source no-double-counting, and parent divergence safety without using recovery as construction or undefined objects as repair mechanisms.

Ordinary long-range gravitational radiation is TT-only. Ordinary scalar breathing radiation through \(A_{\rm rad}\), \(\zeta\), or \(\kappa\) is rejected.

No current \(J_V\), \(J_{\rm sub}\), \(J_{\rm exch}\), \(O\), \(H_{\rm curv}\), \(H_{\rm exch}\), or dark-sector label is licensed to repair mass leakage, boundary leakage, scalar trace double-counting, source double-counting, or parent closure by name.

The current parent equation is not ready.

---

# 2. Status and License System

## 2.1 Status Labels

The following labels are used throughout the current theory snapshot:

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
DEFERRED
NOT_READY
CLOSED
MISSING
UNFINISHED
UNRESOLVED
RISK
```

## 2.2 License Meanings

### DERIVED_REDUCED

A result has been derived in a reduced setting. It may be used inside that reduced domain and as a recovery or diagnostic anchor.

Not licensed: promotion to a final covariant parent law unless the parent derivation exists.

### STRUCTURAL

A form, split, variable, or equation shape is identified, but its full parent derivation, coefficient, normalization, source identity, or covariance status is missing.

Not licensed: treating the structure as a completed law.

### CONSTRAINED

The object or sector is allowed only under explicit restrictions. The restrictions are part of the current theory content, not secondary commentary.

Not licensed: using the object outside its constraint boundary.

### MATCHED

A coefficient, form, or behavior can be matched to a target but has not necessarily been derived from the parent theory.

Not licensed: claiming derivation from matching alone.

### RECOVERY_TARGET

A result must be recovered by a valid parent equation or structural mechanism.

Not licensed: copying the recovery target into the construction.

### THEOREM_TARGET

A law, identity, neutrality condition, operator, current, source relation, or support condition has been identified as required but is not derived.

Licensed use: naming the obligation.

Not licensed: inserting the target as if active.

### SAFE_IF

A convention or branch is conditionally safe if specified constraints are satisfied.

Not licensed: treating the condition as already proven.

### CANDIDATE

A possible variable, structure, role, or route has been identified.

Not licensed: treating the candidate as uniquely selected or derived.

### PROVISIONAL

The statement is the safest current convention but remains replaceable by a derived parent identity or theorem.

Not licensed: treating the convention as final.

### REJECTED

The route is currently disallowed by the theory’s consistency constraints.

Not licensed: reopening the route without explicitly discharging the reason for rejection.

### DEFERRED

The object or task is intentionally postponed until upstream obligations are solved.

Not licensed: using the deferred object as active machinery.

### NOT_READY

The construction lacks required definitions, identities, neutrality theorems, or source separation.

Not licensed: presenting it as a current field equation.

### CLOSED

A diagnostic audit or requirement inventory is complete at the current reduced or bookkeeping level.

Not licensed: interpreting a closed diagnostic audit as a completed parent theorem.

### MISSING

A necessary object, derivation, coefficient, source law, or identity is absent.

### UNFINISHED

The sector has partial structure but lacks required completion.

### UNRESOLVED

The object or relation remains open and cannot yet do active field-theory work.

### RISK

A route remains possible only with heavy theorem burdens or serious double-counting / leakage risks.

## 2.3 Proof and Witness Labels

The following labels describe support level:

```text
PROOF_AVAILABLE
PROOF_CAPSULE_AVAILABLE
DIAGNOSTIC_WITNESS_AVAILABLE
PARENT_PROOF_MISSING
REJECTED_BY_CONSTRAINT
```

A proof capsule is a short present-tense derivation sufficient to preserve why a known result is trusted, without turning the main body into a development history.

A diagnostic witness is a reduced equation or model calculation showing why a constraint is necessary. It is not a parent field law unless separately derived.

---

# 3. Object Registry and Current Field Content

## 3.1 Primary Fields

### \(A\)

Current role: scalar lapse / static mass-response field.

Current status:

```text
DERIVED_REDUCED in static spherical sector
STRUCTURAL beyond reduced sector
```

Licensed use:

```text
A-sector areal flux defines the current reduced ordinary exterior mass reference.
F_A = 4*pi*r^2 A'(r).
M_A = c^2 F_A/(8*pi*G).
For A = 1 - 2GM/(c^2 r), M_A = M.
```

Current constraint boundary:

```text
This is the protected reduced mass coin for ordinary exterior audits.
It is not a final covariant parent mass definition.
Non-A sectors may not shift this exterior mass by declaration.
```

Proof / witness status:

```text
PROOF_CAPSULE_AVAILABLE for reduced areal-flux law and exterior branch.
PARENT_PROOF_MISSING for final covariant mass definition.
```

### \(B_s\) or \(A_{\rm spatial}\)

Current role: scalar spatial response / spatial trace companion to the mass-response sector.

Current status:

```text
RECOVERY_TARGET / THEOREM_TARGET
NOT DERIVED
```

Licensed use:

```text
Target of acceptable parent recovery.
Possible insertion target for zeta-driven volume response.
```

Not licensed:

```text
copying from the GR metric form,
imposing by gamma_like = 1 tuning,
choosing from AB = 1,
choosing from B = 1/A,
choosing from Schwarzschild recovery,
choosing from areal kappa diagnostics,
opening parent closure from reduced recovery success.
```

Current insertion target:

\[
B_s=F_\zeta[A,\zeta,J_V,\Sigma_V,R_V].
\]

Status:

```text
THEOREM_TARGET
NOT DERIVED
```

### \(\zeta=\ln\sqrt{\gamma}\)

Current role: candidate vacuum-spacetime volume configuration variable.

Current status:

```text
CANDIDATE / GEOMETRICALLY MOTIVATED / FRAME-DEPENDENT
```

Licensed use:

```text
volume-form candidate;
possible B_s companion only under residual-kill or derived no-overlap.
```

Not licensed:

```text
independent residual metric trace after already entering B_s,
ordinary exterior scalar charge,
ordinary scalar breathing radiation,
source reservoir,
boundary repair field.
```

### \(\kappa\)

Current role: reduced trace / volume / interior relaxation diagnostic.

Reduced areal diagnostic relation:

\[
\kappa_{\rm areal}=\frac12\ln(AB).
\]

Current status:

```text
DIAGNOSTIC / NON-METRIC / SEPARATELY NEUTRAL UNLESS DERIVED
```

Licensed use:

```text
reduced areal-gauge diagnostic;
non-metric residual bookkeeping if kept inert;
possible relaxation/accounting variable only if it does not re-enter metric/source channels.
```

Not licensed:

```text
covariant physical scalar by assumption,
substitute scalar metric trace,
independent scalar gravity,
hidden residual-restoration path,
ordinary source reservoir,
back-door restoration of killed zeta residual trace.
```

### \(W_i\)

Current role: transverse vector current / frame-dragging candidate.

Current status:

```text
STRUCTURAL / NORMALIZATION UNKNOWN
```

Licensed use:

```text
transverse-current response shape;
frame-dragging structural sector.
```

Open obligations:

```text
alpha_W/K_c,
beta_W,
source convention factors,
gauge-invariant observable extraction.
```

### \(h_{ij}^{TT}\)

Current role: transverse-traceless tensor radiation field.

Current status:

```text
STRUCTURAL / ORDINARY RADIATIVE SECTOR
```

Licensed use:

```text
ordinary long-range gravitational radiation channel;
TT-only radiative sector.
```

Open obligations:

```text
tensor coupling,
source identity,
radiation flux coefficient,
parent derivation.
```

### \(A_{\rm rad}\)

Current role: scalar breathing/radiative hazard.

Current status:

```text
REJECTED as ordinary active long-range degree of freedom
```

Rejected because it would introduce ordinary scalar breathing radiation, scalar double-counting, far-zone scalar flux, secular orbital damping, or an exterior scalar channel not supported by the current theory.

### \(A_{\rm curv}\)

Current role: curvature admissibility / finite-admissibility diagnostic.

Current status:

```text
DIAGNOSTIC / BRANCH-FILTER THEOREM TARGET
NOT DYNAMICS
NOT A FIELD EQUATION
```

Licensed use:

```text
may flag or filter high-curvature / singular candidate branches if a finite-admissibility functional, domain, measure, and branch-kill rule are defined.
```

Not licensed:

```text
dynamical singularity avoidance,
bounce,
regular core,
current-based avoidance,
energy-based avoidance,
boundary-based avoidance,
H_curv correction avoidance.
```

## 3.2 Vacuum, Exchange, Projection, and Correction Objects

### \(J_V^\mu\)

Current role: candidate vacuum-volume flux / transport current needed to define a vacuum frame.

Current status:

```text
UNRESOLVED
```

Core rule:

```text
J_V is not defined by naming it.
J_V is not defined by the divergence equation alone.
J_V is not allowed to shift exterior mass while unresolved.
```

Mass/scalar/current neutrality burden:

```text
A J_V-induced scalar residue C_JV/r carries surface flux -4*pi*C_JV.
A far-zone current j^r = I/(4*pi*r^2) carries sphere flux I.
Ordinary-sector neutrality therefore requires C_JV = 0 and I_V = 0 unless a future current theorem derives a neutral transport interpretation.
```

### \(u_{\rm vac}^\mu\)

Candidate vacuum rest frame:

\[
u_{\rm vac}^\mu=\frac{J_V^\mu}{\sqrt{-J_V^2}}.
\]

Domain:

\[
D_V=\{J_V^2<0,\;J_V\neq0\}.
\]

Current status:

```text
THEOREM_TARGET / DOMAIN-LIMITED / UNRESOLVED
```

Current rule:

```text
No global u_vac follows from a domain-limited current.
Zero-current static equilibrium may protect neutrality, but it cannot define u_vac from J_V.
Spacelike redistribution currents may be spatial fluxes, but not vacuum clocks.
Equilibrium-frame fallback is deferred unless static regions require a frame.
```

### \(\Sigma_V\)

Current role: vacuum-volume source / creation / destruction side of exchange accounting.

Current status:

```text
ROLE-LEVEL ONLY / OPERATOR NOT DERIVED
```

### \(R_V\)

Current role: vacuum-volume relaxation / reconfiguration / return side of exchange accounting.

Current status:

```text
ROLE-LEVEL ONLY / OPERATOR NOT DERIVED
```

### \(J_{\rm sub}^\mu\)

Current role: neutral substrate / pure vacuum transport current.

Current status:

```text
THEOREM_TARGET
NOT DEFINED
```

Required:

```text
pure wind neutrality,
domain,
frame or frame-free law,
measure,
direction/orientation,
boundary behavior,
ordinary matter decoupling,
mass neutrality,
scalar-trace neutrality.
```

Forbidden:

```text
arbitrary preferred-frame wind,
circular definition from u_vac,
remainder-current definition,
pure wind gravitating by existence,
dark-sector convenience,
M_ext shift,
scalar trace source,
ordinary matter push,
boundary repair,
recovery role.
```

Current rule:

```text
Pure wind is not ordinary gravity.
```

### \(J_{\rm exch}^\mu\)

Current role: active exchange current.

Current status:

```text
THEOREM_TARGET
NOT DEFINED
```

Required:

```text
source side,
relaxation side,
Sigma/R distinction,
divergence/balance role,
domain,
direction/orientation,
boundary behavior,
ordinary matter decoupling,
mass neutrality,
scalar-trace guard.
```

Forbidden:

```text
repair current,
boundary repair,
recovery repair,
matter repair,
e_curv source reservoir,
H_exch shortcut,
ordinary matter rerouting,
scalar-tail cancellation,
boundary leakage fix,
M_ext tuning.
```

Current rule:

```text
Exchange is not repair.
```

### \(O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual},J_V]\)

Current role: no-overlap / projection-operator target for count-once recombination.

Current status:

```text
THEOREM_TARGET / DEFERRED
NO UNIVERSAL ACTIVE O DEFINED
ROLE-SPECIFIC PROJECTOR REQUIREMENTS EXPLICIT
DIAGNOSTIC-ONLY LABELS SAFE_IF
```

Current rule:

```text
O cannot be introduced by name.
Universal decorative O is rejected.
Role-specific projectors require independent domain/kernel/image/boundary/source/divergence laws.
Diagnostic-only labels are safe only if they do not alter equations.
```

Active \(O\) requires:

```text
domain,
codomain,
kernel,
image,
composition law,
measure or pairing if orthogonality is claimed,
derivative/divergence behavior,
boundary behavior,
source leakage controls,
mass leakage controls,
scalar leakage controls.
```

### \(J_{\rm curv}^\mu\)

Current role: candidate curvature current.

Current status:

```text
UNRESOLVED
NOT DEFINED
```

A real \(J_{\rm curv}\) requires:

```text
domain,
orientation / direction law,
measure,
covariance status,
admissibility relation,
boundary behavior,
matter separation,
mass neutrality.
```

Current consequence:

```text
current-based anti-singularity claims are deferred.
```

Far-zone neutrality burden:

```text
A far-zone curvature current j_curv^r = I_curv/(4*pi*r^2) carries sphere flux I_curv.
Ordinary-sector neutrality requires I_curv = 0 unless a future curvature-current law derives neutral transport.
```

### \(H_{\rm curv}\)

Current role: candidate curvature correction tensor.

Current status:

```text
NOT DEFINED
NOT INSERTABLE
THEOREM_TARGET / DIAGNOSTIC-ONLY AUDIT LABEL ONLY
```

Licensed use:

```text
curvature-correction theorem target;
diagnostic-only audit label.
```

Forbidden:

```text
anti-singularity patch,
finite-curvature insertion,
regular-core tuning,
e_curv source reservoir,
boundary counterterm,
insertion into a parent equation without independent definition.
```

### \(H_{\rm exch}\)

Current role: candidate exchange correction tensor.

Current status:

```text
NOT DEFINED
NOT INSERTABLE
THEOREM_TARGET / DIAGNOSTIC-ONLY AUDIT LABEL ONLY
```

Licensed use:

```text
exchange-correction theorem target;
diagnostic-only audit label.
```

Forbidden:

```text
exchange-continuity paint,
Sigma/R tuning tensor,
ordinary matter rerouting tensor,
dark-sector patch,
insertion into a parent equation without independent definition.
```

Correction tensor rule:

```text
H_curv is not a curvature rescue cloak.
H_exch is not exchange-continuity paint.
Bianchi-like language is not divergence safety.
Diagnostic-only means not inserted.
```

Future insertion requires:

```text
independent tensor definition,
independent source-side counterpart,
divergence safety,
ordinary matter separation,
A-sector mass neutrality,
scalar trace neutrality,
boundary neutrality,
far-zone flux neutrality,
no shell source,
no recovery tuning.
```

---

# 4. Reduced Reconstructed Core

## 4.1 A-Sector Areal-Flux Law

Primary reduced scalar equation:

\[
\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho.
\]

where

\[
\Delta_{\rm areal}A=\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dA}{dr}\right).
\]

Equivalent flux form:

\[
F_A(r)=4\pi r^2A'(r),
\]

\[
\frac{dF_A}{dr}=4\pi r^2\frac{8\pi G}{c^2}\rho(r).
\]

With

\[
M_{\rm enc}'(r)=4\pi r^2\rho(r),
\]

this gives

\[
F_A(r)=\frac{8\pi G}{c^2}M_{\rm enc}(r).
\]

Current status:

```text
DERIVED_REDUCED
```

Current role:

```text
strongest reconstructed sector;
ordinary reduced exterior mass-charge route.
```

Proof status:

```text
PROOF_CAPSULE_AVAILABLE
```

## 4.2 Exterior Vacuum Scalar Equation

For \(\rho=0\),

\[
\Delta_{\rm areal}A=0.
\]

Thus

\[
\frac{d}{dr}\left(r^2A'\right)=0,
\]

and

\[
A(r)=C_0+\frac{C_1}{r}.
\]

Asymptotic flatness sets

\[
C_0=1.
\]

Flux normalization by total mass \(M\) gives

\[
A(r)=1-\frac{2GM}{c^2r}.
\]

Current status:

```text
DERIVED_REDUCED
```

Proof status:

```text
PROOF_CAPSULE_AVAILABLE
```

## 4.3 Exterior Radial Factor

In the static spherical exterior, the reduced areal diagnostic condition is

\[
\kappa_{\rm areal}=0.
\]

With

\[
AB=e^{2\kappa_{\rm areal}},
\]

this gives

\[
AB=1,
\]

so

\[
B=\frac{1}{A}.
\]

Therefore

\[
B(r)=\left(1-\frac{2GM}{c^2r}\right)^{-1}.
\]

Current status:

```text
DERIVED_REDUCED / GAUGE-CONDITIONED / RECOVERY CHECK
```

Boundary of use:

```text
B = 1/A is not a general construction rule for the parent theory.
It is a recovered static spherical exterior relation.
It may audit a structurally fixed candidate in the reduced static exterior.
It may not choose F_zeta coefficients, seam data, residual-kill status, or parent closure.
```

Current recovery rule:

```text
Recovery may judge. Recovery may not forge.
```

## 4.4 Weak Multipole Scalar Extension

For weak fields,

\[
A\simeq1+\frac{2\Phi}{c^2}.
\]

The scalar field recovers the Newtonian potential structure:

\[
\nabla^2\Phi=4\pi G\rho.
\]

Exterior weak multipole expansion:

\[
\Phi(\mathbf{x})=-G\int\frac{\rho(\mathbf{x}')}{|\mathbf{x}-\mathbf{x}'|}\,d^3x'.
\]

Thus

\[
A(\mathbf{x})\simeq1+\frac{2\Phi(\mathbf{x})}{c^2}.
\]

Current status:

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

# 5. Metric Recombination and Count-Once Constraint

The recombination map is reduced bookkeeping, not a covariant parent derivation.

## 5.1 Safe Recombination Statement

```text
g_tt <- A

g_0i <- W_i

g_ij <- B_s / A_spatial scalar response
        + h_TT
        + killed, non-metric, or separately neutral residual bookkeeping
```

## 5.2 Unsafe Loose Form

```text
g_ij <- A_spatial + zeta_residual + kappa_residual + h_TT
```

Reason:

```text
This risks double-counting the scalar spatial trace.
```

## 5.3 Current Count-Once Rule

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

Current status:

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

## 5.4 Metric-Trace Load Ledger

Metric trace entries under \(B_s\) insertion:

```text
zeta_to_Bs
zeta_residual_metric
kappa_metric
epsilon_vac_metric
e_kappa_metric
```

Double-count load:

\[
L_{\rm double}
=
e_{\kappa,{\rm metric}}
+
\epsilon_{{\rm vac},{\rm metric}}
+
\kappa_{\rm metric}
+
\zeta_{{\rm residual},{\rm metric}}.
\]

Safe count-once target:

```text
T_safe = zeta_Bs
```

Current requirement:

```text
L_double must vanish or remain strictly inert, non-metric, and non-reentering.
Count-once recombination remains theorem-targeted.
```

## 5.5 \(B_s/F_\zeta\) Insertion Target

Current target:

\[
B_s=F_\zeta[A,\zeta,J_V,\Sigma_V,R_V].
\]

Current status:

```text
THEOREM_TARGET
NOT DERIVED
```

Coefficient-origin rule:

```text
Coefficient origin must be structural or theorem-targeted before recovery tests.
Recovery may not choose F_zeta form, coefficient, or zeta residual status.
Zeta enters metric trace only once through B_s.
```

Recovery diagnostics downstream of insertion:

```text
gamma_like_target
AB_target = 1
kappa_areal_target = 0
```

Current rule:

```text
A-sector exterior A_ext = 1 - 2GM/(c^2 r) is the recovery anchor,
not a spatial metric construction.
AB=1, B=1/A, gamma_like, and areal kappa are downstream diagnostics.
Count-once residual trace is the central unresolved burden.
No active O is available.
Parent equation remains not ready.
```

---

# 6. Zeta, Kappa, Residuals, and Vacuum-Volume Accounting

## 6.1 Vacuum-Volume Ontology

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

\[
\zeta=\ln\sqrt{\gamma}.
\]

Physical volume element:

\[
dV_{\rm phys}=\sqrt{\gamma}\,d^3x.
\]

Linear variation:

\[
\delta\zeta=\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

For TT perturbations,

\[
\gamma^{ij}h_{ij}^{TT}=0,
\]

so

\[
\delta\zeta|_{TT}=0.
\]

Interpretation:

```text
trace / volume modes change vacuum-spacetime amount,
TT modes are volume-preserving shear.
```

Proof / witness status:

```text
DIAGNOSTIC_WITNESS_AVAILABLE for TT volume preservation.
```

## 6.2 Conformal-Volume Split

Structural split:

```text
gamma_ij = exp(2 zeta / 3) * bar_gamma_ij
det(bar_gamma) = 1
```

Consistent with:

```text
zeta = ln sqrt(gamma)
```

In three spatial dimensions:

```text
det(gamma) = exp(2 zeta) det(bar_gamma) = exp(2 zeta)
```

Status:

```text
STRUCTURAL
NOT A FIELD LAW
```

Meaning:

```text
The split supports zeta as the spatial volume scalar.
It separates volume from unimodular shape/shear.
It does not derive B_s/F_zeta insertion.
It does not derive boundary safety.
It does not derive no-overlap O.
It does not derive residual-kill.
It does not derive recovery coefficients.
```

## 6.3 Current Role of \(\zeta\)

Current role:

```text
geometric vacuum-volume candidate,
possible B_s companion only under residual-kill or no-overlap.
```

Forbidden:

```text
zeta changes B_s and also remains independent residual metric trace.
```

## 6.4 Current Role of \(\kappa\)

Current best interpretation:

```text
kappa = reduced diagnostic / non-metric residual / separately neutral trace variable unless derived.
```

Areal-gauge diagnostic relation:

\[
\kappa_{\rm areal}=\frac12\ln(AB).
\]

Exterior Schwarzschild sector:

\[
\kappa_{\rm areal}=0.
\]

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

Areal-kappa rule:

```text
kappa_areal = (1/2)*ln(AB) is a reduced gauge-conditioned diagnostic.
Areal kappa may classify a structurally fixed candidate.
Areal kappa may not construct B_s or become a physical scalar insertion law.
kappa_areal = 0 in the reduced Schwarzschild exterior is an anchor, not a parent law.
e_kappa must not become an additional ordinary metric/source channel.
```

## 6.5 Residual-Kill Convention

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

Residual scalar-tail witness:

```text
zeta_tail = C_zeta/r gives F_zeta = -4*pi*C_zeta.
kappa_tail = C_kappa/r gives F_kappa = -4*pi*C_kappa.
```

Ordinary exterior scalar silence requires:

```text
C_zeta = 0,
C_kappa = 0,
```

unless residuals are strictly non-metric/diagnostic, killed/suppressed, compact-neutral, or routed through a future parent identity without double counting.

Not sufficient:

```text
C_zeta + C_kappa = 0
```

Cancellation by hand is not sector neutrality.

Diagnostic/non-metric residuals may survive only if they have:

```text
no metric trace effect,
no source role,
no boundary flux,
no far-zone tail,
no coefficient reservoir,
no later re-entry through H, O, dark labels, curvature, exchange, source projectors, or parent placeholders,
no recovery-selected status.
```

Non-metric vocabulary is not a no-overlap theorem.

Residual non-reentry through support/matching remains theorem-targeted.

Residual-kill and \(O\) remain the two routes to count-once insertion:

```text
residual-kill is provisional and must be fixed before recovery diagnostics are run;
O requires real operator structure before it can erase overlap.
```

## 6.6 Neutral Residual Alternative

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

Neutral residual survival requires:

```text
exterior scalar coefficient vanishing,
compact-neutral support with derived matching/no-shell behavior,
diagnostic residual non-reentry,
source-routing compatibility,
no repair route,
no recovery-selected status,
structural support origin,
value/slope matching,
distributional shell absence,
transition layer neutrality,
recovery independence,
source compatibility,
no residual re-entry through support or layer parameters.
```

Total cancellation across residual sectors is not neutral residual status.

## 6.7 Rejected Kappa / Zeta Interpretations

Rejected as ordinary propagating scalar gravity:

\[
\Box\kappa=\alpha S,
\]

\[
\Box\zeta=\alpha S.
\]

Rejected as ordinary exterior scalar channels:

```text
raw pressure trace Poisson kappa,
zeta exterior scalar charge,
kappa exterior scalar charge,
zeta/kappa independent scalar gravities,
kappa restoring killed residual metric trace,
zeta/kappa cancellation by hand,
nonzero zeta exterior 1/r tail,
nonzero kappa exterior 1/r tail,
residual relaxation repairing A-flux,
recovery-chosen residual status,
scalar silence by total cancellation,
O erasing zeta/kappa tails by name,
H canceling zeta/kappa tails,
boundary shell absorbing zeta/kappa leakage,
recovery-selected zeta/kappa coefficient zero,
diagnostic residual re-entering metric/source/boundary behavior.
```

## 6.8 Energy / Accounting Guardrail

Provisional vacuum-volume functional:

\[
\epsilon_{{\rm vac},{\rm config}}=
\frac12K_\zeta(\zeta-\zeta_{\min})^2+
\frac12L_\zeta|\nabla\zeta|^2.
\]

Separate kappa relaxation energy:

\[
e_\kappa=\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

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

### \(e_{\rm curv}\)

Current role: curvature energy diagnostic / accounting variable.

Current status:

```text
DIAGNOSTIC / ACCOUNTING ONLY
NOT A SOURCE
```

Licensed use:

```text
may measure curvature intensity,
may serve as finite-admissibility accounting,
may later seed H_curv only if a divergence-safe source structure is derived.
```

Forbidden:

```text
e_curv as source reservoir,
e_curv as bounce energy,
e_curv as regular-core tuning,
e_curv shifting M_ext independently of A,
e_curv defining J_curv by fiat.
```

---

# 7. Vacuum-Volume and Exchange Constraints

## 7.1 Exchange Continuity Target

Current exchange-continuity theorem target:

\[
\nabla_\mu J_V^\mu=\Sigma_V-R_V.
\]

Status:

```text
THEOREM_TARGET
NOT A LAW
```

Core reason:

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

Vacuum-current split refinement:

```text
Even if J_V is role-split into J_sub and J_exch,
the exchange-continuity equation remains theorem-target only.

Do not write:
  nabla_mu J_exch^mu = Sigma_exch - R_exch

as a law unless J_exch, Sigma_exch, R_exch,
domain, direction, measure, and boundary behavior are independently defined.
```

## 7.2 Curvature Balance Target

Candidate form:

\[
\nabla_\mu J_{\rm curv}^\mu=\Sigma_{\rm curv}-R_{\rm curv}.
\]

Status:

```text
THEOREM TARGET ONLY
NOT A LAW
```

Reason:

```text
J_curv, Sigma_curv, R_curv, domain, and measure are not defined.
```

Forbidden:

```text
decorative curvature continuity law,
repair balance,
recovery-tuned balance,
balance law used to claim bounce or regular core.
```

## 7.3 \(\Sigma/R\) Split

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

## 7.4 Flux Direction Constraint

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

Only the first can become ontology. The second may be useful diagnostically. The third is rejected.

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

## 7.5 Vacuum-Current Split

Current split:

\[
J_V=J_{\rm sub}+J_{\rm exch}.
\]

Status:

```text
SAFE_IF / ROLE-LEVEL ONLY
NOT OPERATOR-LEVEL
NOT A LAW
```

Interpretation:

```text
J_sub names the pure substrate / pure-wind role.
J_exch names the active exchange role.

This split is useful for bookkeeping,
but it does not define J_V,
J_sub,
J_exch,
u_vac,
Sigma_V,
R_V,
Sigma_exch,
or R_exch.
```

Ordinary-sector safest branches:

```text
zero-net exchange:
  Sigma_exch - R_exch = 0

zero creation:
  Sigma_exch = R_exch = 0

curvature-from-warping:
  curvature changes arise from constrained time/space warping,
  not net vacuum creation/destruction

latent exchange:
  Sigma/R exist as ontology/accounting,
  but vanish or balance in ordinary sector.
```

## 7.6 Timelike / Nonzero Domain

Candidate vacuum-frame definition:

\[
u_{\rm vac}^\mu=\frac{J_V^\mu}{\sqrt{-J_V^2}}.
\]

This only makes sense on:

\[
D_V=\{J_V^2<0,\;J_V\neq0\}.
\]

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

## 7.7 Static-Source Neutrality

Ordinary static sources must not create independent exterior scalar volume charge.

Allowed safety routes, all conditional:

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

Pure wind neutrality:

```text
REQUIRED
NOT DERIVED
```

Pure substrate flow must not gravitate merely because it flows.

Required:

```text
no M_ext shift,
no scalar trace,
no ordinary matter coupling,
no boundary repair,
no preferred-frame force,
no recovery role.
```

Failure:

```text
if J_sub shifts mass, sources scalar trace, pushes matter,
or repairs boundary behavior,
J_sub cannot be an ordinary-sector pure-wind current.
```

---

# 8. Boundary Neutrality, Scalar Silence, Matching, and Support

Boundary neutrality and exterior scalar silence are not derived. They are central current theorem targets.

## 8.1 Boundary Neutrality

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

## 8.2 Boundary / Scalar-Silence Target Ledger

Core target ledger:

```text
delta F_A|boundary,non-A = 0
C_zeta = 0
C_kappa = 0
C_JV = 0
C_Jsub = 0
C_Jexch = 0
C_curv = 0
C_Jcurv = 0
C_H = 0
C_boundary = 0
C_dark = 0
I_V = 0
I_sub = 0
I_exch = 0
I_curv = 0
I_H = 0
I_boundary = 0
I_dark = 0
no shell source
no recovery-tuned smoothing
no active O
no H insertion
```

Reduced witnesses:

```text
phi_i = C_i/r
F_i = -4*pi*C_i

j_i^r = I_i/(4*pi*r^2)
Phi_i = I_i

delta A_boundary = q/r
delta M_A = -c^2 q/(2G)
```

Interpretation:

```text
Every ordinary-sector residual scalar tail coefficient must vanish
or remain strictly inert, diagnostic, non-metric, compact-neutral with derived matching,
or future theorem-routed without double counting.

Every non-A far-zone current coefficient must vanish
or remain role-level / diagnostic / future theorem-routed as neutral transport.

Total cancellation is not sector silence.
Repair routes are not boundary neutrality.
Diagnostic/non-metric labels are not no-overlap theorems.
```

Status:

```text
CLOSED_DIAGNOSTIC / REQUIREMENTS EXPLICIT
BOUNDARY NEUTRALITY STILL THEOREM_TARGET
SCALAR SILENCE STILL THEOREM_TARGET
```

## 8.3 Mass-Neutrality Witnesses

Residual scalar tail:

```text
phi_tail = C/r
F_phi = 4*pi*r^2 phi_tail' = -4*pi*C
```

Therefore a residual ordinary-sector \(1/r\) scalar tail is not neutral unless \(C=0\), unless it is strictly non-metric/diagnostic, or unless a future parent theorem routes it without double counting.

Boundary A-tail:

```text
delta A_boundary = q/r
delta F_A = -4*pi*q
delta M_A = -c^2 q/(2G)
```

Therefore non-A boundary behavior must not leave a nonzero exterior A-tail.

Far-zone current flux:

```text
j^r = I/(4*pi*r^2)
Phi = 4*pi*r^2 j^r = I
```

Therefore non-A far-zone currents are neutral only if \(I=0\), unless a future current theorem derives a neutral transport interpretation.

Current status:

```text
DERIVED_REDUCED DIAGNOSTIC
```

These are reduced diagnostics and theorem burdens, not parent field equations.

## 8.4 Smooth Support / Matching-Law Requirements

Core matching/support obligation ledger:

```text
structural support origin,
value matching,
slope / no-flux matching,
distributional shell absence,
transition layer neutrality,
recovery independence,
source compatibility,
diagnostic residual non-reentry,
no repair route.
```

Reduced seam witnesses:

```text
phi(R),
phi'(R),
phi''(R),
F_R = 4*pi*R^2 phi'(R)
```

Cutoff profile witness:

```text
phi(r) = f(r) Theta(R-r)

d[f(r) Theta(R-r)]/dr
  = f'(r) Theta(R-r) - f(R) delta(R-r)
```

Transition-layer witnesses:

```text
F_layer = -4*pi*C_layer
delta M_A|layer = -c^2 q_layer/(2G)
Phi_layer = I_layer
```

Required transition-layer neutrality:

```text
C_layer = 0
q_layer = 0
I_layer = 0
sigma_layer = 0
alpha_recovery = 0
source_load = 0
layer origin is structural
```

Interpretation:

```text
Value matching alone is not enough.
Value+slope matching is a necessary diagnostic condition, not a support theorem.
Sharp cutoffs can create shell diagnostics.
Smooth transition layers cannot hide mass, scalar flux, current flux, shell/source load, recovery tuning, or source load.
Recovery is downstream audit, not construction.
Matching/support/layer laws must preserve ordinary A-sector source routing.
```

Status:

```text
CLOSED_DIAGNOSTIC / REQUIREMENTS EXPLICIT
COMPACT SUPPORT STILL THEOREM_TARGET
NO-SHELL MATCHING STILL THEOREM_TARGET
TRANSITION LAYER NEUTRALITY STILL THEOREM_TARGET
BOUNDARY / SCALAR SILENCE STILL NOT_READY
```

## 8.5 Curvature Boundary / Mass Neutrality

Status:

```text
REQUIRED
NOT DERIVED
```

Required:

```text
no M_ext shift independent of A-sector,
no boundary repair current,
no exterior scalar charge,
no far-zone hidden curvature/scalar flux,
no ordinary matter rerouting,
no recovery-tuned smoothing,
no boundary counterterm singularity avoidance.
```

Current safe fallback:

```text
curvature admissibility remains interior diagnostic / branch-filter only.
```

Curvature diagnostics and curvature-current labels must not rescue boundary or scalar leakage.

Required:

```text
C_curv = 0,
C_Jcurv = 0,
I_curv = 0,
```

unless a future curvature-current / curvature-admissibility theorem derives neutral behavior with no boundary repair, no scalar tail, no source rerouting, and no recovery tuning.

Curvature boundary rescue remains rejected.

## 8.6 Correction Tensor Boundary / Mass Neutrality

Status:

```text
REQUIRED
NOT DERIVED
```

\(H_{\rm curv}\) and \(H_{\rm exch}\) must not:

```text
shift M_ext,
act as boundary counterterms,
generate exterior scalar charge,
hide far-zone flux,
create shell sources,
smooth boundaries for recovery,
use dark-sector boundary patches,
claim anti-singularity by boundary behavior.
```

Required before any future \(H\) insertion:

```text
C_H = 0,
I_H = 0,
no H boundary counterterm,
no H scalar-tail cancellation,
no H M_ext correction,
no H repair of shell, boundary, or current leakage.
```

\(H\) boundary counterterms and \(H\) flux insertion remain rejected.

---

# 9. Source Routing, Projectors, and No-Double-Counting

## 9.1 Protected Source Route

Current source routing rule:

```text
ordinary rho / M_enc remains routed to the A-sector mass charge.
```

Protected route:

```text
rho / M_enc -> A-sector mass charge
```

Non-A duplicate source channels are not licensed.

## 9.2 Source Assignments

| Sector | Source | Status |
|---|---|---|
| \(A\) | \(\rho\), \(M_{\rm enc}\), scalar mass response | DERIVED_REDUCED / STRUCTURAL |
| \(B_s/A_{\rm spatial}\) | scalar spatial response companion | RECOVERY_TARGET / THEOREM_TARGET |
| \(W_i\) | \(j_T=P_T(\rho v)\) | STRUCTURAL / CONSTRAINED |
| \(\zeta\) | volume configuration / possible \(B_s\) companion | CANDIDATE / UNFINISHED |
| \(\kappa\) | diagnostic / non-metric residual unless derived | CONSTRAINED |
| \(h_{ij}^{TT}\) | trace-free quadrupole / \(P_{TT}T_{ij}\) | STRUCTURAL / COEFFICIENT MATCHED |
| \(A_{\rm rad}\) | ordinary long-range scalar radiation | REJECTED / CONSTRAINED |
| \(J_V\) | vacuum-volume current | UNRESOLVED |
| \(\Sigma_V\) | volume source / creation side | ROLE-LEVEL ONLY |
| \(R_V\) | relaxation / return side | ROLE-LEVEL ONLY |
| \(O\) | no-overlap / projection target | THEOREM_TARGET / DEFERRED |
| \(J_{\rm sub}\) | neutral substrate / pure-wind role | THEOREM_TARGET / NOT DEFINED |
| \(J_{\rm exch}\) | active exchange role | THEOREM_TARGET / NOT DEFINED |
| \(\Sigma_{\rm exch}/R_{\rm exch}\) | exchange source / relaxation sides | ROLE-LEVEL ONLY / NOT OPERATOR-LEVEL |
| dark-sector coupling | optional future coupling | NOT REQUIRED / DEFERRED |

## 9.3 Required Routing Constraints

```text
rho / scalar charge -> A only,

longitudinal current -> scalar continuity / density redistribution,

transverse current -> W_i,

TT stress -> h_ij^TT,

J_V-driven zeta -> B_s only if residual zeta/kappa metric trace is killed or non-metric,

residual zeta/kappa -> non-metric bookkeeping, diagnostic, or separately neutral unless O is derived,

ordinary scalar radiation -> rejected,

J_sub -> must not push ordinary matter, must not source scalar trace, must not shift M_ext,

J_exch -> must not reroute ordinary matter,
  must not define Sigma_exch from ordinary T_mu_nu by convenience,
  must not become boundary or curvature repair,

ordinary matter -> rho / scalar charge remains routed to A-sector
  unless a separate source theorem derives otherwise,

rho / M_enc -> A-sector mass charge,

non-A duplicate scalar tails -> rejected unless coefficient vanishes or future parent theorem routes without double counting,

non-A duplicate A-tails -> rejected unless q = 0 or future parent mass law derives the route,

pressure / trace -> diagnostic or non-metric kappa/zeta relaxation only if neutral,

curvature diagnostics -> not ordinary matter sources,

H_curv/H_exch -> not ordinary matter sinks or correction patches,

dark labels -> optional downstream only, not ordinary failure patches,

source cancellation ledgers -> not sector neutrality,

boundary/scalar silence -> requires source-routing compatibility,

ordinary source routing -> must not create boundary shell, scalar-tail, current-flux,
curvature, H, exchange, or dark repair channels,

diagnostic residuals -> must not re-enter source routing,

repair routes -> rejected as source-routing substitutes,

matching/support/layer laws -> must preserve ordinary A-sector source routing,

support/layer parameters -> must not carry ordinary source load,

boundary shell source -> rejected as matching/support law,

scalar tail source -> rejected as matching/support law,

current flux source -> rejected as matching/support law,

curvature/H/exchange/dark repair source -> rejected as matching/support law,

source compatibility -> requires sector-by-sector zero, not total cancellation.
```

## 9.4 Forbidden Duplicate Source Loads

Metric insertion must preserve ordinary source no-double-counting.

Forbidden duplicate source loads:

```text
rho_Bs_coeff
rho_zeta_residual
rho_kappa_residual
rho_support_layer
rho_curv
rho_H
rho_exch
rho_dark
rho_cancel
```

Current rule:

```text
B_s/F_zeta coefficients cannot carry ordinary source load.
Zeta/kappa residuals cannot become source channels.
Support/layer/boundary parameters cannot become source reservoirs.
Cancellation ledgers are not source compatibility.
Metric insertion source compatibility remains theorem-targeted.
```

## 9.5 No-Double-Counting Rules

```text
zeta cannot enter both B_s and residual metric trace,

kappa cannot restore killed zeta residual trace,

epsilon_vac_config and e_kappa cannot count killed residual as extra source energy,

J_V cannot shift M_ext independently of A-sector,

Sigma_V and R_V cannot be two names for one hidden tuning mechanism,

recovery checks cannot choose coefficients, boundary behavior, residual status, or overlap split,

ordinary T_mu_nu cannot be counted again in J_sub, J_exch, Sigma_exch, or R_exch,

Sigma_exch and R_exch cannot be two names for one hidden tuning mechanism,

J_sub cannot be defined as J_V - J_exch without a split criterion,

dark-sector coupling cannot relabel ordinary matter failure,

ordinary rho / M_enc cannot source a second ordinary exterior mass channel by declaration,

rho cannot also source kappa, zeta, curvature, H, exchange, or dark labels,

ordinary T_mu_nu cannot become Sigma_exch, J_exch, H_curv, or H_exch by convenience,

curvature diagnostics and accounting terms cannot become source reservoirs,

H tensors cannot absorb ordinary source mismatch or define their own source by divergence,

dark labels cannot patch ordinary source, boundary, scalar-tail, H, or recovery failure,

source-load cancellation across non-A labels is not sector-by-sector neutrality,

boundary shells cannot hide duplicate ordinary source load,

non-A scalar-tail coefficients cannot be canceled by total source ledgers,

non-A current-flux coefficients cannot be canceled by total flux ledgers,

diagnostic residual labels cannot re-enter through source projectors,

boundary/scalar repair mechanisms cannot be used to bypass source no-double-counting,

matching/support laws cannot duplicate A-sector source load,

support radius, smoothing width, and transition-layer coefficients cannot hide ordinary source load,

ordinary source cannot be rerouted into shell/scalar/current/repair seam pockets,

source-loaded support parameters are rejected,

source cancellation ledgers are not source compatibility,

B_s/F_zeta insertion coefficients cannot carry ordinary source load,

zeta/kappa residuals after insertion cannot become source channels,

support/layer/boundary parameters under insertion cannot carry ordinary source load,

curvature/H/exchange/dark repair labels cannot carry ordinary source load under insertion,

metric insertion duplicate source loads cancel only in sector-by-sector zero,
  not total cancellation.
```

Status:

```text
CONSTRAINED / NOT YET PARENT-DERIVED
```

## 9.6 Correction Tensor Source Separation

Status:

```text
REQUIRED
NOT DERIVED
```

Correction tensors must not double-count:

```text
ordinary matter,
A-sector mass source,
e_curv accounting,
A_curv diagnostic status,
undefined J_curv,
Sigma/R role labels,
J_V / J_exch role labels,
dark-sector labels,
residual trace,
boundary failure.
```

Current safe route:

```text
diagnostic-only H-like audit objects,
not inserted into field equations.
```

---

# 10. Radiation, Vector, and Tensor Sectors

## 10.1 Scalar Radiative Sector

An unconstrained scalar radiative perturbation would have the form

\[
A_{\rm rad}=a_0\cos(kx-\omega t),
\]

with wave condition

\[
\omega^2=c^2k^2.
\]

This would be a scalar breathing-type gravitational radiation channel.

Current rule:

\[
{\rm source}(A_{\rm rad}\ {\rm ordinary\ massless})=0.
\]

Rejected as ordinary scalar-radiation equations:

\[
\Box\kappa=\alpha S,
\]

\[
\Box\zeta=\alpha S.
\]

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

## 10.2 Vector Current / Frame-Dragging Sector

Matter continuity:

\[
\partial_t\rho+\nabla\cdot j=0,
\]

with

\[
j_i=\rho v_i.
\]

Decompose:

\[
j=j_T+j_L,
\]

with

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

Sector allocation:

\[
j_T\rightarrow W_i,
\]

\[
j_L\rightarrow A\text{ / scalar continuity}.
\]

Candidate vector energy:

\[
E_W=\int\left[K_c|\nabla\times W|^2+\alpha_W j_T\cdot W\right]d^3x.
\]

Variation gives:

\[
\nabla\times(\nabla\times W)=-\frac{\alpha_W}{2K_c}j_T.
\]

Under \(\nabla\cdot W=0\):

\[
\Delta W=\frac{\alpha_W}{2K_c}j_T.
\]

Status:

```text
STRUCTURAL / DERIVED_REDUCED SHAPE
NORMALIZATION UNKNOWN
```

Observable candidate:

\[
B_W=\nabla\times W,
\]

\[
\Omega_{\rm drag}=\beta_WB_W.
\]

Unknowns:

```text
alpha_W/K_c,
beta_W,
source convention factors,
gauge-invariant observable extraction.
```

## 10.3 Tensor Radiation Sector

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

Candidate tensor equation:

\[
\Box h_{ij}^{TT}=-\mathcal{C}_T S_{ij}^{TT}.
\]

GR target form:

\[
\Box h_{ij}^{TT}=-\frac{16\pi G}{c^4}T_{ij}^{TT}.
\]

Current status:

```text
TT structure: STRUCTURAL / RECOVERED SHAPE
wave equation form: STRUCTURAL
coefficient: MATCHED / UNKNOWN
source identity: UNFINISHED
```

Tensor energy flux scaling:

\[
F_T\sim K_T\langle\dot h_{ij}^{TT}\dot h_{ij}^{TT}\rangle.
\]

GR target:

\[
F_{\rm GR}=\frac{c^3}{32\pi G}\langle\dot h_{ij}^{TT}\dot h_{ij}^{TT}\rangle.
\]

Status:

```text
STRUCTURAL / MATCHED
COEFFICIENT NOT DERIVED
```

---

# 11. Curvature, Admissibility, and Correction Tensor Constraints

## 11.1 Curvature Admissibility

\(A_{\rm curv}\) remains a diagnostic / branch-filter theorem target, not a dynamical field equation.

Current role:

```text
may flag or filter high-curvature / singular candidate branches,
if a finite-admissibility functional, domain, measure, and branch-kill rule are defined.
```

Not licensed:

```text
dynamical singularity avoidance,
bounce,
regular core,
current-based avoidance,
energy-based avoidance,
boundary-based avoidance,
H_curv correction avoidance.
```

Anti-singularity claim ladder:

Currently licensed:

```text
diagnostic claim,
branch-filter / theorem-target claim.
```

Not currently licensed:

```text
dynamical singularity avoidance,
bounce,
regular core,
current-based avoidance,
energy-based avoidance,
boundary-based avoidance,
H_curv correction avoidance.
```

## 11.2 Curvature Current

\(J_{\rm curv}\) remains undefined. Current-based anti-singularity claims are deferred.

A real \(J_{\rm curv}\) requires:

```text
domain,
orientation / direction law,
measure,
covariance status,
admissibility relation,
boundary behavior,
matter separation,
mass neutrality.
```

Far-zone neutrality witness:

```text
j_curv^r = I_curv/(4*pi*r^2)
```

carries sphere flux \(I_{\rm curv}\). Ordinary-sector neutrality requires \(I_{\rm curv}=0\) unless a future curvature-current law derives neutral transport.

## 11.3 Curvature Energy

\(e_{\rm curv}\) is diagnostic / accounting only, not a source.

Allowed:

```text
measure curvature intensity,
serve as finite-admissibility accounting,
later seed H_curv only if a divergence-safe source structure is derived.
```

Forbidden:

```text
e_curv as source reservoir,
e_curv as bounce energy,
e_curv as regular-core tuning,
e_curv shifting M_ext independently of A,
e_curv defining J_curv by fiat.
```

## 11.4 Parent Correction Tensor Status

Current rule:

```text
H_curv is not a curvature rescue cloak.
H_exch is not exchange-continuity paint.
Bianchi-like language is not divergence safety.
Diagnostic-only means not inserted.
```

\(H_{\rm curv}\) status:

```text
NOT DEFINED
NOT INSERTABLE
THEOREM_TARGET / DIAGNOSTIC-ONLY AUDIT LABEL ONLY
```

\(H_{\rm exch}\) status:

```text
NOT DEFINED
NOT INSERTABLE
THEOREM_TARGET / DIAGNOSTIC-ONLY AUDIT LABEL ONLY
```

Future insertion requires:

```text
independent tensor definition,
independent source-side counterpart,
divergence safety,
ordinary matter separation,
A-sector mass neutrality,
scalar trace neutrality,
boundary neutrality,
far-zone flux neutrality,
no shell source,
no recovery tuning.
```

Correction tensor divergence safety:

```text
REQUIRED
NOT DERIVED
```

Allowed future routes:

```text
constructed divergence identity,
independently defined source-balance partner,
defined projection / constraint-propagation theorem,
diagnostic-only non-insertion.
```

Rejected:

```text
Bianchi-like language by itself,
decorative tensor closure,
source-by-divergence,
leakage-canceling divergence,
recovery-chosen divergence,
dark-patch divergence.
```

---

# 12. Constraint / Evolution Split

| Variable | Equation Type | Current Status | Licensed Role / Constraint |
|---|---|---|---|
| \(A\) | elliptic / scalar constraint | DERIVED_REDUCED | reduced scalar mass response |
| \(B_s/A_{\rm spatial}\) | scalar spatial response | RECOVERY_TARGET / NOT DERIVED | must be recovered, not copied |
| \(A_{\rm rad}\) | ordinary scalar radiation | REJECTED / CONSTRAINED | no ordinary scalar breathing channel |
| \(\zeta\) | volume configuration / possible \(B_s\) companion | CANDIDATE / FRAME-DEPENDENT | count-once only |
| \(\kappa\) | diagnostic / non-metric residual unless derived | CONSTRAINED | may not restore killed trace |
| \(J_V\) | vacuum-volume flux / transport current | UNRESOLVED | not defined by divergence alone |
| \(u_{\rm vac}\) | vacuum rest frame from \(J_V\), if domain exists | UNRESOLVED / DOMAIN-LIMITED | no global frame from unresolved current |
| \(\Sigma_V\) | volume source role | ROLE-LEVEL ONLY | not an operator |
| \(R_V\) | relaxation / return role | ROLE-LEVEL ONLY | not an operator |
| \(W_i\) | transverse vector response | STRUCTURAL | normalization unknown |
| \(h_{ij}^{TT}\) | hyperbolic tensor evolution | STRUCTURAL | TT-only ordinary radiation |
| source identities | continuity / Bianchi-like closure | MISSING | parent identity absent |
| recombination | count-once metric map | UNFINISHED | central unresolved burden |
| \(J_{\rm sub}\) | neutral substrate / pure-wind target | NOT DEFINED / THEOREM_TARGET | pure wind is not gravity |
| \(J_{\rm exch}\) | active exchange target | NOT DEFINED / THEOREM_TARGET | exchange is not repair |
| \(\Sigma_{\rm exch}\) | exchange source side | ROLE-LEVEL ONLY | not operator-level |
| \(R_{\rm exch}\) | exchange relaxation side | ROLE-LEVEL ONLY | not operator-level |
| dark-sector coupling | optional separated coupling | DEFERRED / NOT REQUIRED | not ordinary failure patch |

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

# 13. Current Minimal Candidate Field System

This section collects the current equations, diagnostics, candidates, theorem targets, and rejected forms by license level.

## 13.1 Derived Reduced Results

\[
\boxed{\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho}
\]

Status:

```text
DERIVED_REDUCED
```

\[
\boxed{A_{\rm ext}(r)=1-\frac{2GM}{c^2r}}
\]

Status:

```text
DERIVED_REDUCED
```

A-sector mass-charge reference:

\[
\boxed{M_A=\frac{c^2F_A}{8\pi G}}
\]

Status:

```text
CLOSED_REDUCED / AUDIT ANCHOR
```

Meaning:

```text
A-sector mass charge is the current reduced ordinary exterior reference.
It is not a final covariant parent mass definition.
```

Weak scalar limit:

\[
\boxed{A\simeq1+\frac{2\Phi}{c^2},\qquad \nabla^2\Phi=4\pi G\rho}
\]

Status:

```text
DERIVED_REDUCED / WEAK-FIELD
```

## 13.2 Reduced Diagnostics

\[
\boxed{AB=e^{2\kappa_{\rm areal}}}
\]

Status:

```text
DEFINITION / REDUCED AREAL-GAUGE DIAGNOSTIC
```

Exterior diagnostic condition:

\[
\boxed{\kappa_{\rm areal}=0}
\]

therefore:

\[
\boxed{B=\frac1A}
\]

Status:

```text
DERIVED_REDUCED in static spherical exterior
NOT GENERAL PARENT CONSTRUCTION
```

Residual scalar-tail witness:

```text
phi = C/r
F_phi = -4*pi*C
```

Status:

```text
DERIVED_REDUCED DIAGNOSTIC
```

Boundary A-tail witness:

```text
delta A_boundary = q/r
delta M_A = -c^2 q/(2G)
```

Far-zone current witness:

```text
j_i^r = I_i/(4*pi*r^2)
Phi_i = I_i
```

## 13.3 Structural / Candidate Forms

Volume-form candidate:

\[
\boxed{\zeta=\ln\sqrt{\gamma}}
\]

with

\[
\boxed{\delta\zeta=\frac12\gamma^{ij}\delta\gamma_{ij}},
\]

and

\[
\boxed{\delta\zeta|_{TT}=0.}
\]

Status:

```text
CANDIDATE / LINEAR STRUCTURAL
```

Vector response:

\[
\boxed{\nabla\times(\nabla\times W)=-\frac{\alpha_W}{2K_c}j_T}
\]

with

\[
j_T=P_Tj.
\]

Status:

```text
STRUCTURAL / COEFFICIENT UNKNOWN
```

Tensor radiation:

\[
\boxed{\Box h_{ij}^{TT}=-\mathcal{C}_T S_{ij}^{TT}}
\]

Status:

```text
STRUCTURAL / SOURCE AND COEFFICIENT UNFINISHED
```

## 13.4 Theorem Targets

Vacuum exchange theorem target:

\[
\boxed{\nabla_\mu J_V^\mu=\Sigma_V-R_V}
\]

Status:

```text
THEOREM_TARGET / NOT A LAW
```

Vacuum-current role split:

\[
\boxed{J_V=J_{\rm sub}+J_{\rm exch}}
\]

Status:

```text
ROLE-LEVEL BOOKKEEPING ONLY
NOT A FIELD LAW
NOT AN OPERATOR DECOMPOSITION
```

Pure-wind neutrality target:

\[
\boxed{\delta M_{\rm ext}|_{J_{\rm sub}}=0}
\]

\[
\boxed{J_{\rm sub}\text{ does not source }B_s/\zeta/\kappa\text{ scalar trace}}
\]

\[
\boxed{J_{\rm sub}\text{ does not couple to ordinary }T_{\mu\nu}}
\]

Status:

```text
THEOREM_TARGET / NOT DERIVED
```

Exchange-current source target:

\[
\boxed{\nabla_\mu J_{\rm exch}^\mu=\Sigma_{\rm exch}-R_{\rm exch}}
\]

Status:

```text
THEOREM_TARGET ONLY
NOT A LAW
```

Reason:

```text
J_exch, Sigma_exch, R_exch, domain, direction, measure,
and boundary behavior are not defined.
```

Vacuum-frame candidate:

\[
\boxed{u_{\rm vac}^\mu=\frac{J_V^\mu}{\sqrt{-J_V^2}}}
\]

only on:

\[
\boxed{D_V=\{J_V^2<0,\;J_V\neq0\}.}
\]

Status:

```text
THEOREM_TARGET / DOMAIN-LIMITED / UNRESOLVED
```

No-overlap theorem target:

\[
\boxed{O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual},J_V]=0}
\]

Status:

```text
THEOREM_TARGET / DEFERRED
NO UNIVERSAL ACTIVE O DEFINED
```

Residual-kill convention:

\[
\boxed{J_V\text{-driven }\zeta\rightarrow B_s
\quad\Rightarrow\quad
\zeta_{{\rm residual},{\rm metric}}=0,
\quad
\kappa_{{\rm residual},{\rm metric}}=0\text{ or non-metric}}
\]

Status:

```text
SAFE_IF / PROVISIONAL / NOT DERIVED
```

Parent equation theorem target:

\[
\boxed{E_{\rm parent}+H_{\rm curv}+H_{\rm exch}=\text{source side}}
\]

Status:

```text
THEOREM_TARGET ONLY
NOT A CURRENT FIELD EQUATION
NOT INSERTABLE
```

Reason:

```text
H_curv and H_exch are not defined;
divergence safety is not derived;
source separation is not derived;
boundary/mass neutrality is not derived.
```

No correction tensor is insertable into a parent equation yet. Diagnostic-only \(H\)-like audit objects are the only safe current route.

## 13.5 Rejected Forms

Rejected scalar-radiation equations:

\[
\boxed{\Box\kappa=\alpha S}
\]

\[
\boxed{\Box\zeta=\alpha S}
\]

Status:

```text
REJECTED as ordinary scalar gravity
```

Rejected by current constraints:

```text
ordinary scalar breathing radiation,
H insertion without independent definition,
O eraser by name,
boundary repair current,
R_V boundary cancellation,
J_exch repair,
curvature boundary rescue,
dark-sector patch,
recovery-tuned smoothing,
source cancellation ledger as sector neutrality,
parent equation opened from reduced recovery.
```

---

# 14. GR Recovery Audit

## 14.1 Real Reduced Reconstruction

Static spherical exterior:

\[
A=1-\frac{2GM}{c^2r},
\]

\[
B=\frac1A.
\]

Status:

```text
RECONSTRUCTED / DERIVED_REDUCED
```

This is the strongest current result.

## 14.2 Strong Reduced / Structural Support

Weak scalar multipole shape:

\[
A\simeq1+\frac{2\Phi}{c^2}.
\]

Status:

```text
RECONSTRUCTED AT WEAK ORDER
```

Reduced weak \(\gamma=1\) behavior:

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

## 14.3 Recovery Scorecard

| Result | Status |
|---|---|
| static spherical exterior \(A\) | DERIVED_REDUCED |
| exterior \(B=1/A\) once \(\kappa_{\rm areal}=0\) | DERIVED_REDUCED / GAUGE-CONDITIONED |
| weak scalar / Newtonian limit | DERIVED_REDUCED |
| weak spatial scalar response | RECOVERY_TARGET / NOT DERIVED |
| full PPN audit | MISSING |
| frame-dragging shape \(\sim J/r^3\) | DERIVED_REDUCED shape |
| frame-dragging normalization | MATCHED / UNKNOWN |
| tensor wave TT structure | STRUCTURAL |
| tensor coupling | MATCHED / UNKNOWN |
| tensor flux coefficient | MATCHED / UNKNOWN |
| no scalar breathing radiation | CONSTRAINED |
| \(\kappa\) non-radiative status | CONSTRAINED / UNFINISHED |
| \(J_V/u_{\rm vac}\) | UNRESOLVED |
| no-overlap \(O\) | UNRESOLVED |
| residual-kill | SAFE_IF / PROVISIONAL |
| parent conservation / Bianchi compatibility | MISSING |
| covariant metric recombination | UNFINISHED |

## 14.4 Recovery-Use Constraint

Recovery remains downstream.

Allowed recovery tests:

```text
gamma_like weak-field behavior,
AB exterior diagnostic,
areal kappa mismatch diagnostic,
Schwarzschild / GR-compatible exterior spatial behavior,
weak-field spatial curvature.
```

Rejected as construction:

```text
gamma_like coefficient fit,
B=1/A construction,
GR spatial metric copy,
areal kappa physical promotion,
recovery-tuned support / smoothing,
recovery-selected residual-kill,
J_V as recovery repair current,
F_zeta form or coefficient chosen from recovery target,
support radius chosen from Schwarzschild,
smoothing width or transition layer chosen from PPN/gamma/AB recovery,
residual-kill or nonmetric status chosen from recovery outcomes,
parent closure opened from recovery success.
```

Current rule:

```text
Recovery may test the branch.
Recovery may not build the branch.
Recovery may judge. Recovery may not forge.
```

---

# 15. Parent Readiness and Closure Gates

## 15.1 Parent Equation Status

The parent equation is not ready.

Status:

```text
NOT_READY
THEOREM_TARGET ONLY
NOT A CURRENT FIELD EQUATION
```

No correction tensor is currently insertable. No Bianchi-like phrase substitutes for divergence safety. No recovery success opens parent closure.

## 15.2 Closure Gates

Parent closure requires at least the following gates:

```text
Gate 1: A-sector reduced mass consistency.
Gate 2: B_s/F_zeta insertion law.
Gate 3: count-once scalar trace.
Gate 4: residual-kill or no-overlap derivation.
Gate 5: boundary neutrality / scalar silence.
Gate 6: smooth support / no-shell matching.
Gate 7: source no-double-counting.
Gate 8: correction tensor definition and divergence safety if correction tensors are used.
Gate 9: parent source identity / conservation compatibility.
```

## 15.3 Metric Insertion Closure Obligations

Metric insertion theorem obligations:

```text
O1: define B_s/F_zeta structurally, not by recovery.
O2: fix coefficient origin before recovery diagnostics.
O3: enforce count-once trace insertion.
O4: derive residual-kill or active no-overlap O.
O5: preserve boundary neutrality and exterior scalar silence.
O6: preserve smooth support and no-shell matching.
O7: preserve source no-double-counting.
O8: keep recovery diagnostics downstream.
O9: do not open parent equation before divergence/source identities are derived.
```

## 15.4 No Premature Closure Rule

```text
Reduced recovery success does not open parent closure.
Bianchi-like language does not prove divergence safety.
Diagnostic labels are not active field equations.
Theorem targets are not laws.
Undefined currents are not sources.
Undefined tensors are not insertable.
No repair route substitutes for a theorem.
```

---

# 16. Open Theorem Burdens and Unknowns

## 16.1 Core Missing Objects

```text
J_V^mu:
  physical vacuum-volume flux / transport current.

Sigma_V:
  volume source operator.

R_V:
  relaxation / return operator.

u_vac^mu:
  vacuum frame, definable from J_V only on a timelike / nonzero domain if J_V exists.

O[B_s, zeta_residual/kappa_residual, J_V]:
  no-overlap operator.

B_s/F_zeta:
  metric insertion law connecting volume response to scalar spatial trace.

alpha_W/K_c, beta_W, C_shape:
  vector normalization and observable coupling.

C_T, K_T:
  tensor coupling and radiation-energy coefficient.

K_zeta, L_zeta, zeta_min:
  volume-configuration stiffnesses and equilibrium configuration.

K_kappa, mu_kappa, lambda_kappa, chi_kappa:
  kappa relaxation parameters if a non-metric / relaxation branch survives.
```

## 16.2 Missing Projectors / Operators

```text
P_scalar,
P_TT,
P_trace,
P_relax,
P_boundary,
P_recombination,
P_coeff,
O no-overlap / projection operator,
O_metric,
O_source,
O_current,
O_divergence,
O_boundary.
```

## 16.3 Structural Unknowns

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
active no-overlap operator O,
role-specific projector derivations,
projector domain/kernel/image laws,
projector divergence and commutator laws,
projector boundary and exterior neutrality laws,
residual-kill derivation or parent identity,
kappa cleanup,
B_s/F_zeta insertion law,
coefficient action/stiffness principle,
formal A_curv finite-admissibility functional,
curvature invariant set / diagnostic scalar selection,
domain and physical measure,
branch-kill theorem,
e_curv diagnostic/accounting definition,
J_curv domain/orientation/measure/covariance status,
Sigma_curv and R_curv if curvature balance is reopened,
curvature boundary and mass neutrality theorem,
no exterior scalar charge theorem,
ordinary matter decoupling theorem,
relation to zeta/volume without reopening B_s/F_zeta or O,
future H_curv divergence-safe source structure,
explicit solutions before bounce or regular-core claims,
J_sub definition,
J_sub domain/frame/measure/direction law,
pure wind neutrality theorem,
J_exch definition,
J_exch source side,
J_exch relaxation side,
Sigma_exch / R_exch distinction and strength laws,
ordinary matter decoupling theorem for vacuum currents,
vacuum-current mass neutrality theorem,
vacuum-current scalar trace neutrality theorem,
vacuum-current boundary neutrality theorem,
zero-net exchange ordinary-sector condition,
zero-creation ordinary-sector condition,
curvature-from-warping parent relation,
latent vs active exchange regime condition,
dark-sector source separation if reopened,
H_exch divergence-safe audit,
H_curv tensor definition,
H_exch tensor definition,
correction tensor source origin,
projection class / sector split,
divergence identity or independent source-balance partner,
constraint propagation theorem if used,
ordinary matter separation theorem for correction tensors,
A-sector mass neutrality theorem for correction tensors,
scalar trace / no-overlap theorem for correction tensors,
boundary neutrality theorem for correction tensors,
far-zone flux neutrality for correction tensors,
shell-source absence for correction tensors,
coefficient origin for correction tensors,
recovery-independent construction of correction tensors,
parent divergence identity,
ordinary closed-regime mass-neutrality theorem,
boundary scalar-silence theorem,
non-A delta M_A = 0 theorem,
residual 1/r scalar coefficient vanishing theorem,
no-shell boundary matching law,
far-zone non-A current flux neutrality theorem,
ordinary source no-double-counting theorem,
correction tensor mass-neutrality and insertability theorem,
exterior scalar silence theorem,
compact support law,
value/slope boundary matching theorem,
distributional shell absence theorem,
sector scalar coefficient vanishing theorem,
sector current flux neutrality theorem,
neutral transport theorem,
diagnostic residual inertness theorem,
diagnostic residual non-reentry theorem,
recovery-independent boundary data theorem,
source-routing compatibility with boundary/scalar silence,
no-repair boundary theorem,
structural support origin theorem,
transition layer neutrality theorem,
recovery-independent support parameter theorem,
recovery-independent smoothing/layer theorem,
source-compatible matching law,
matching/support residual non-reentry theorem,
no-repair matching/support law,
compact-support admissibility theorem,
source-compatible transition-layer theorem,
F_zeta insertion law,
coefficient origin independent of recovery,
count-once recombination theorem,
residual-kill or no-overlap derivation,
gamma / AB recovery without diagnostic tuning,
boundary / scalar silence compatibility under metric insertion,
smooth support / matching compatibility under metric insertion,
source compatibility under metric insertion,
no-repair insertion,
metric insertion closure gate,
gamma-like recovery gate,
AB / B=1/A gate,
no-overlap / residual gate,
boundary/support/source gate under metric insertion,
parent equation gate under metric insertion.
```

---

# 17. Minimal Honest Claim

The current theory has:

```text
one real reduced reconstruction: the A-sector scalar mass-response branch;

a protected reduced ordinary exterior mass reference: M_A = c^2 F_A/(8*pi*G);

a recovered reduced static exterior: A = 1 - 2GM/(c^2 r), with B = 1/A only under the reduced areal diagnostic condition kappa_areal = 0;

structural vector and tensor sectors, with vector normalization and tensor coupling still missing;

a constrained radiation rule: ordinary long-range gravitational radiation is TT-only;

a candidate zeta/vacuum-volume architecture, with kappa kept diagnostic/non-metric unless derived;

a provisional residual-kill convention or future no-overlap route for count-once scalar trace insertion;

a sharpened boundary/scalar-silence and matching/support ledger;

a source-routing/no-double-counting ledger protecting the A-sector mass coin;

undefined vacuum currents and correction tensors that cannot yet do field-equation work;

a parent equation that remains not ready.
```

The current theory does not yet have:

```text
full covariant parent field equation,
B_s/F_zeta insertion law,
active no-overlap operator O,
derived residual-kill theorem,
J_V flux law,
Sigma_V/R_V operator laws,
J_sub pure-wind neutrality theorem,
J_exch active exchange theorem,
boundary neutrality theorem,
exterior scalar silence theorem,
no-shell matching theorem,
source no-double-counting theorem,
correction tensor insertability,
full PPN audit,
vector normalization,
tensor coupling and flux coefficient.
```

The central unfinished problem is not the reduced A-sector exterior. The central unfinished problem is licensed recombination: deriving \(B_s/F_\zeta\), count-once scalar trace insertion, boundary/scalar silence, support/matching neutrality, source no-double-counting, and parent divergence safety without using recovery as construction or undefined objects as repair mechanisms.

---

# 18. Recommended Next Technical Target

Do not immediately write a parent field equation.

The next technical target should be one of the following narrower routes:

```text
25_residual_kill_or_no_overlap_theorem
25_role_specific_boundary_projectors
25_source_compatible_boundary_laws
25_reduced_observational_audit
```

Recommended next group:

```text
25_residual_kill_or_no_overlap_theorem
```

Reason:

```text
Count-once recombination is the central unresolved burden.

The next step is to attack this core obstacle directly:

  derive residual-kill, meaning B_s insertion kills residual zeta/kappa metric trace,
  or derive active no-overlap O with full operator structure:
    domain, kernel, image, composition, pairing, divergence,
    boundary, source/mass/scalar leakage.

No shortcut through O by name is allowed.
No recovery-selected residual status is allowed.
```

Safe alternatives:

```text
25_role_specific_boundary_projectors:
  if the next step attempts actual projector routes with domain, kernel, image,
  divergence, boundary, and source compatibility.

25_source_compatible_boundary_laws:
  if the next step prioritizes boundary/support/source compatibility for insertion.

25_reduced_observational_audit:
  if no theorem route is ready and reduced consequences should be audited
  without claiming insertion or parent closure.
```

Known unresolved dependencies retained upstream of any parent equation:

```text
B_s/F_zeta insertion together with residual-kill or no-overlap,
without GR metric copying, gamma_like tuning, B=1/A construction,
areal-kappa promotion, or recovery-tuned boundary behavior.

J_V / J_sub / J_exch definition and ordinary matter decoupling.
```

---

# Appendix A — Proof Capsules for Derived Reduced Results

## A.1 A-Sector Areal-Flux Law

Claim:

\[
\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho.
\]

Proof capsule:

Using

\[
\Delta_{\rm areal}A=\frac1{r^2}\frac{d}{dr}\left(r^2A'\right),
\]

multiply by \(4\pi r^2\) and define

\[
F_A=4\pi r^2A'(r).
\]

Then

\[
\frac{dF_A}{dr}=4\pi r^2\frac{8\pi G}{c^2}\rho(r).
\]

With

\[
M_{\rm enc}'=4\pi r^2\rho,
\]

the flux is

\[
F_A=\frac{8\pi G}{c^2}M_{\rm enc}.
\]

Status:

```text
DERIVED_REDUCED
```

Limit:

```text
reduced scalar / areal sector;
not a final covariant parent proof.
```

## A.2 Exterior A-Solution

Claim:

\[
A_{\rm ext}=1-\frac{2GM}{c^2r}.
\]

Proof capsule:

For \(\rho=0\),

\[
\Delta_{\rm areal}A=0.
\]

Therefore

\[
\frac{d}{dr}(r^2A')=0.
\]

So

\[
A=C_0+\frac{C_1}{r}.
\]

Asymptotic flatness gives \(C_0=1\). Mass-flux normalization gives

\[
C_1=-\frac{2GM}{c^2}.
\]

Status:

```text
DERIVED_REDUCED
```

Limit:

```text
static spherical reduced exterior.
```

## A.3 Exterior Radial Factor

Claim:

\[
B=\frac1A
\]

in the reduced static spherical exterior.

Proof capsule:

Use the reduced areal diagnostic relation

\[
\kappa_{\rm areal}=\frac12\ln(AB).
\]

In the exterior diagnostic branch,

\[
\kappa_{\rm areal}=0.
\]

Therefore \(AB=1\), so \(B=1/A\).

Status:

```text
DERIVED_REDUCED / GAUGE-CONDITIONED / RECOVERY CHECK
```

Limit:

```text
not a general parent construction rule.
```

## A.4 Weak Scalar Limit

Claim:

\[
A\simeq1+\frac{2\Phi}{c^2},
\qquad
\nabla^2\Phi=4\pi G\rho.
\]

Proof capsule:

In the weak-field limit, identify the scalar lapse perturbation with the Newtonian potential by \(A\simeq1+2\Phi/c^2\). The reduced scalar equation recovers the Newtonian Poisson equation.

Status:

```text
DERIVED_REDUCED / WEAK-FIELD
```

Limit:

```text
not full nonlinear nonspherical field equation;
not full PPN audit.
```

## A.5 TT Volume Preservation

Claim:

\[
\delta\zeta|_{TT}=0.
\]

Proof capsule:

Since

\[
\zeta=\ln\sqrt\gamma,
\]

linear variation gives

\[
\delta\zeta=\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

For a TT perturbation,

\[
\gamma^{ij}h_{ij}^{TT}=0.
\]

Therefore TT perturbations are volume-preserving at this order.

Status:

```text
LINEAR STRUCTURAL / DIAGNOSTIC_WITNESS_AVAILABLE
```

---

# Appendix B — Diagnostic Witness Ledger

## B.1 Residual Scalar Tail

```text
phi = C/r
F_phi = 4*pi*r^2 phi' = -4*pi*C
```

Meaning:

```text
A residual ordinary-sector 1/r scalar tail is not neutral unless C = 0,
or unless it is strictly non-metric/diagnostic,
or unless a future parent theorem routes it without double counting.
```

## B.2 Boundary A-Tail

```text
delta A_boundary = q/r
delta F_A = -4*pi*q
delta M_A = -c^2 q/(2G)
```

Meaning:

```text
Non-A boundary behavior must not leave a nonzero exterior A-tail.
```

## B.3 Far-Zone Current Flux

```text
j^r = I/(4*pi*r^2)
Phi = 4*pi*r^2 j^r = I
```

Meaning:

```text
Non-A far-zone currents are neutral only if I = 0,
unless a future current theorem derives neutral transport.
```

## B.4 Sector Scalar-Tail Witness

```text
phi_i = C_i/r
F_i = -4*pi*C_i
```

Meaning:

```text
Every ordinary-sector residual scalar coefficient must vanish
or remain inert, non-metric, diagnostic, compact-neutral with derived matching,
or future theorem-routed without double counting.
```

## B.5 Sector Current-Flux Witness

```text
j_i^r = I_i/(4*pi*r^2)
Phi_i = I_i
```

Meaning:

```text
Every non-A far-zone current coefficient must vanish
or remain role-level, diagnostic, or future theorem-routed as neutral transport.
```

## B.6 Boundary Regularity Witness

```text
F_R = 4*pi*R^2 phi'(R)
```

Meaning:

```text
Value matching alone is insufficient.
Value+slope matching is necessary diagnostically, but not a support theorem.
```

## B.7 Cutoff Shell Witness

```text
phi(r) = f(r) Theta(R-r)

d[f(r) Theta(R-r)]/dr
  = f'(r) Theta(R-r) - f(R) delta(R-r)
```

Meaning:

```text
Sharp support and exterior zero do not prove no-shell behavior.
```

## B.8 Transition-Layer Witnesses

```text
F_layer = -4*pi*C_layer
delta M_A|layer = -c^2 q_layer/(2G)
Phi_layer = I_layer
```

Required:

```text
C_layer = 0
q_layer = 0
I_layer = 0
sigma_layer = 0
alpha_recovery = 0
source_load = 0
```

Meaning:

```text
Smoothness is not neutrality.
```

## B.9 Count-Once Trace Witness

\[
L_{\rm double}
=
e_{\kappa,{\rm metric}}
+
\epsilon_{{\rm vac},{\rm metric}}
+
\kappa_{\rm metric}
+
\zeta_{{\rm residual},{\rm metric}}.
\]

Meaning:

```text
L_double must vanish or remain strictly inert, non-metric, and non-reentering.
```

## B.10 Gamma / AB Diagnostic Witness

\[
AB-1=x\left(2\gamma_s+x(\beta_{AB}-4\gamma_s)-2\right).
\]

Meaning:

```text
gamma_s and beta_AB are diagnostic placeholders.
They must be structurally fixed before this diagnostic is interpreted.
Setting them from recovery is smuggling.
```

## B.11 Boundary / Support Compatibility Witness

\[
L_{\rm boundary/support}
=
C_{\rm ext}
+I_{\rm nonA}
+q_{A{\rm tail}}
+\sigma_{\rm shell}
+{\rm value\_jump}
+{\rm slope\_flux}
+{\rm layer\_load}
+{\rm recovery\_seam}
+{\rm repair\_route}.
\]

Meaning:

```text
Metric insertion is not licensed while any boundary/support load remains.
Boundary/support guardrails remain active for metric insertion.
```

## B.12 Source Compatibility Witness

\[
L_{\rm source\_dup}
=
\rho_{B_s{\rm coeff}}
+\rho_{\zeta{\rm residual}}
+\rho_{\kappa{\rm residual}}
+\rho_{\rm support/layer}
+\rho_{\rm curv}
+\rho_H
+\rho_{\rm exch}
+\rho_{\rm dark}
+\rho_{\rm cancel}.
\]

Meaning:

```text
Metric insertion must preserve source no-double-counting sector by sector.
Source coin stays in A. No metric pocket.
```

---

# Appendix C — Rejected Route Index

## C.1 Scalar Radiation Failures

```text
A_rad ordinary scalar radiation,
Box kappa = alpha S,
Box zeta = alpha S,
hidden breathing wave,
far-zone scalar flux,
secular orbital damping,
scalar conversion becoming ordinary radiation,
P_relax becoming Box zeta / Box kappa.
```

## C.2 Metric-Insertion Smuggling

```text
B_s copied from Schwarzschild / GR spatial metric,
B = 1/A used as general construction rule,
gamma_like coefficient fit,
AB = 1 used as parent insertion law,
areal kappa promoted to physical scalar,
zeta inserted into both B_s and residual metric trace,
kappa restores killed residual trace,
O erases overlap by name,
H or dark label patches insertion failure,
recovery target chooses F_zeta coefficients,
recovery target chooses seam data,
recovery target chooses residual-kill status,
support/smoothing/boundary/layer data chosen from recovery,
ordinary source hidden in B_s/F_zeta coefficient,
zeta residual becomes source channel after insertion,
kappa residual or e_kappa becomes source channel after insertion,
support/layer/boundary parameter carries ordinary source load,
curvature/H/exchange/dark label absorbs ordinary source load under insertion,
duplicate source loads cancel only in total,
source compatibility assumed from recovery success,
source compatibility assumed from boundary/support audit alone,
retest ledger treated as insertion theorem,
recovery diagnostics become metric insertion construction,
count-once convention treated as no-overlap theorem,
boundary/support audit licenses insertion,
source audit licenses insertion,
parent equation opened from metric insertion retest alone.
```

## C.3 Boundary Repair Routes

```text
surface counterterm,
boundary repair current,
R_V boundary cancellation,
J_exch repair,
curvature boundary rescue,
H boundary counterterm,
O boundary eraser,
dark boundary patch,
recovery-tuned smoothing,
sharp support hiding shell charge,
boundary counterterm,
source-gradient shell source,
zeta-gradient exterior tail without zero-charge theorem,
total scalar-tail cancellation,
total current-flux cancellation,
support by declaration,
exterior zero as support proof,
value+slope matching as full support theorem,
smoothness as neutrality,
finite-width shell disguise,
recovery-selected support,
recovery-selected smoothing,
AB-product tuning,
tail-suppression tuning,
boundary-load tuning,
parent-fit parameter,
source-loaded support parameter,
source cancellation ledger.
```

## C.4 Source-Routing Repairs

```text
ordinary rho/T rerouted into boundary shell,
ordinary rho/T rerouted into scalar-tail cancellation,
ordinary rho/T rerouted into non-A current flux,
ordinary rho/T rerouted into curvature boundary rescue,
ordinary rho/T rerouted into H counterterm,
ordinary rho/T rerouted into exchange repair,
ordinary rho/T rerouted into dark boundary patch,
ordinary source rerouted into support radius,
ordinary source rerouted into smoothing width,
ordinary source rerouted into layer coefficient,
source cancellation ledger treated as source compatibility,
boundary shells hiding duplicate ordinary source load,
non-A scalar-tail coefficients canceled by total source ledgers,
non-A current-flux coefficients canceled by total flux ledgers.
```

## C.5 Curvature Rescue Routes

```text
anti-singularity by declaration,
diagnostic called dynamics,
branch-kill called bounce,
bounded invariant called regular core,
e_curv as source reservoir,
e_curv as bounce money,
regular-core tuning by e_curv coefficient or cutoff,
J_curv as repair current,
J_curv as gradient-by-fiat,
decorative curvature balance law,
boundary counterterm singularity avoidance,
curvature object shifts M_ext independently of A,
ordinary matter coupling rerouted,
zeta/volume coupling reopens B_s/F_zeta or O,
H_curv introduced as patch,
recovery-tuned anti-singularity mechanism.
```

## C.6 Vacuum-Current Failures

```text
J_V assumed defined,
J_V as acausal repair current,
J_V as decorative flux,
J_V defined circularly from u_vac,
u_vac introduced as arbitrary preferred frame,
J_sub as arbitrary preferred-frame wind,
J_sub gravitating by existence,
J_sub pushing ordinary matter,
J_sub shifting M_ext,
J_sub sourcing scalar trace,
J_sub as remainder current,
J_exch as repair current,
Sigma_exch/R_exch as tuning knobs,
decorative exchange continuity law,
ordinary T_mu_nu as Sigma_exch by fiat,
matter-induced exchange by convenience,
boundary exchange as repair,
curvature admissibility as active repair source.
```

## C.7 Correction Tensor Failures

```text
H_curv as anti-singularity patch,
H_curv as finite-curvature insertion,
H_curv as regular-core tuning,
H_curv as e_curv source reservoir,
H_curv as boundary counterterm,
H_exch as exchange-continuity paint,
H_exch as Sigma/R tuning tensor,
H_exch as ordinary matter rerouting tensor,
H_exch as dark-sector patch,
H inserted by Bianchi-like language,
H and source defining each other,
source-by-divergence,
boundary leakage motivating insertion,
M_ext correction tensor,
scalar tail cancellation tensor,
shell-source hiding tensor,
recovery-fit correction,
undefined current/source insertion,
diagnostic-only object inserted into field equation,
theorem-target parent form treated as current law.
```

## C.8 No-Overlap Failures

```text
O by declaration,
O as residual eraser,
O as recovery projector,
O as boundary counterterm,
O as source separator by name,
O as tensor insertability patch,
O as Bianchi/divergence patch,
O as current repair,
O as shell source generator,
O as dark-sector patch,
O used to erase boundary/scalar leakage by name,
nonmetric vocabulary treated as no-overlap theorem,
neutral transport target treated as current law.
```

## C.9 Dark-Label Patches

```text
dark sector patching ordinary failure,
dark sector shifting ordinary M_ext,
dark scalar charge leak,
dark boundary patch,
dark source rerouting,
dark label used to patch ordinary boundary failure.
```

## C.10 Recovery-As-Construction Failures

```text
silent GR metric import,
recovery target used to select smoothing/support/boundary/current/residual data,
support radius chosen from Schwarzschild recovery,
smoothing width chosen from PPN/gamma_like recovery,
coefficient chosen to enforce AB=1 or B=1/A,
residual tail status chosen from scalar-tail failure,
boundary parameter chosen to cancel A-tail/current/shell/source load,
parent-fit parameter chosen to make a parent-looking equation close,
parent equation opened from recovery success.
```

---

# Appendix D — Operator / Projector Readiness Checklists

## D.1 Active No-Overlap Operator \(O\)

A real active \(O\) requires:

```text
domain,
codomain,
kernel,
image,
composition / idempotence law,
measure or pairing if orthogonality is claimed,
derivative behavior,
divergence behavior,
boundary behavior,
source leakage controls,
mass leakage controls,
scalar leakage controls,
compatibility with B_s/F_zeta insertion,
compatibility with residual-kill or residual survival,
compatibility with parent source identity.
```

## D.2 Role-Specific Projectors

Still missing or theorem-targeted:

```text
P_scalar,
P_TT,
P_trace,
P_relax,
P_boundary,
P_recombination,
P_coeff,
O_metric,
O_source,
O_current,
O_divergence,
O_boundary.
```

Each requires:

```text
independent domain,
image/kernel split,
composition law,
measure/pairing if orthogonality is claimed,
commutation or controlled non-commutation with derivatives,
boundary behavior,
source routing behavior,
mass neutrality behavior,
scalar trace behavior,
compatibility with recovery as audit only.
```

## D.3 Vacuum Current \(J_V\)

A real \(J_V\) requires:

```text
physical flux / transport law,
domain,
direction/orientation,
measure,
covariance status,
source relation,
relaxation relation,
ordinary matter decoupling,
static-source neutrality,
boundary neutrality,
scalar trace neutrality,
A-sector mass neutrality,
no far-zone scalar/current leakage,
no recovery repair role.
```

## D.4 Curvature Current \(J_{\rm curv}\)

A real \(J_{\rm curv}\) requires:

```text
domain,
orientation / direction law,
measure,
covariance status,
admissibility relation,
boundary behavior,
matter separation,
mass neutrality,
neutral transport theorem if far-zone flux exists.
```

## D.5 Correction Tensors \(H_{\rm curv}\), \(H_{\rm exch}\)

An insertable correction tensor requires:

```text
independent tensor definition,
independent source-side counterpart,
divergence safety,
ordinary matter separation,
A-sector mass neutrality,
scalar trace neutrality,
boundary neutrality,
far-zone flux neutrality,
no shell source,
coefficient origin independent of recovery,
no recovery tuning,
compatibility with parent identity.
```

---

# Appendix E — Symbol Index

```text
A:
  scalar lapse / static mass-response field.

B_s / A_spatial:
  scalar spatial response / spatial trace companion.

zeta:
  ln sqrt(gamma), candidate vacuum-spacetime volume variable.

kappa:
  reduced trace / volume / relaxation diagnostic.

kappa_areal:
  (1/2) ln(AB), reduced areal-gauge diagnostic.

W_i:
  transverse vector current / frame-dragging candidate.

h_ij^TT:
  transverse-traceless tensor radiation field.

A_rad:
  rejected ordinary scalar radiation / breathing channel.

A_curv:
  curvature admissibility / branch-filter diagnostic.

J_V:
  candidate vacuum-volume flux / transport current.

u_vac:
  vacuum frame from J_V only where J_V is timelike and nonzero.

Sigma_V:
  role-level vacuum-volume source / creation side.

R_V:
  role-level relaxation / return side.

J_sub:
  neutral substrate / pure-wind theorem target.

J_exch:
  active exchange theorem target.

Sigma_exch / R_exch:
  role-level exchange source / relaxation sides.

J_curv:
  undefined curvature current candidate.

H_curv:
  undefined, non-insertable curvature correction tensor target.

H_exch:
  undefined, non-insertable exchange correction tensor target.

O:
  no-overlap / projection theorem target.

epsilon_vac_config:
  provisional zeta configuration/accounting functional.

e_kappa:
  separate kappa relaxation/accounting energy.

e_curv:
  curvature diagnostic/accounting variable, not a source.

F_A:
  A-sector areal flux, 4*pi*r^2 A'(r).

M_A:
  reduced A-sector mass charge, c^2 F_A/(8*pi*G).

C_i:
  sector scalar-tail coefficient.

I_i:
  sector far-zone current coefficient.

q:
  boundary A-tail coefficient.

L_double:
  metric trace double-count load.

L_boundary/support:
  boundary/support compatibility load.

L_source_dup:
  duplicate source load.
```

---

# Appendix F — Provenance / Former Group Audit History

This appendix preserves the development provenance without letting historical chronology dominate the current-state architecture.

## F.1 Group 20 — No-Overlap / Projection Audit

Current outcome:

```text
O remains theorem-targeted and deferred.
No universal active projection operator is defined.
Role-specific projector requirements are explicit.
Diagnostic-only labels remain safe only without field-equation effect.
Divergence-compatible projection remains theorem-targeted.
Boundary/exterior-neutral projection remains theorem-targeted.
Parent equation forms remain not ready.
```

## F.2 Group 21 — Source-Routing / Mass-Neutrality Audit

Current outcome:

```text
A-sector mass charge is protected as the current reduced ordinary exterior reference.
M_A = c^2 F_A/(8*pi*G).
For A = 1 - 2GM/(c^2 r), M_A = M.
No non-A sector is licensed as an independent ordinary exterior mass carrier.
Residual 1/r scalar tails carry F = -4*pi*C.
Boundary A-tails q/r shift delta M_A = -c^2 q/(2G).
Zeta/kappa residuals must be killed, non-metric, compact-neutral, coefficient-zero, or theorem-targeted.
J_V remains unresolved.
J_sub/J_exch remain role-level.
Curvature accounting remains diagnostic/accounting.
H_curv/H_exch remain non-insertable.
Ordinary source routing is protected from duplicate non-A source channels.
Boundary neutrality and scalar silence remain the next bottleneck.
Parent equation remains not ready.
```

## F.3 Group 22 — Boundary-Neutrality / Scalar-Silence Requirements Audit

Current outcome:

```text
Boundary/scalar silence targets are explicit.
delta F_A|boundary,non-A = 0 is required.
Sector scalar-tail coefficients C_i must vanish or remain inert/nonmetric/diagnostic/compact-neutral/theorem-routed.
C_i/r tails carry F_i = -4*pi*C_i.
Non-A current coefficients I_i must vanish or remain role-level/diagnostic/theorem-routed.
I_i/(4*pi*r^2) current profiles carry Phi_i = I_i.
No shell source is allowed.
No recovery-tuned smoothing is allowed.
No active O is available.
No H insertion is allowed.
Value matching alone is insufficient.
C2/smooth compact toy profiles are diagnostics, not compact-support theorems.
Total scalar-tail cancellation is not sector silence.
Total current-flux cancellation is not sector current silence.
Repair routes remain rejected.
Diagnostic/non-metric residuals must remain inert and non-reentering.
Boundary neutrality and exterior scalar silence remain theorem-targeted.
Parent equation remains not ready.
```

## F.4 Group 23 — Smooth Support / Matching-Law Audit

Current outcome:

```text
Matching regularity ladder is explicit.
Value jump is rejected.
Value matching alone is risky.
Value+slope matching is necessary diagnostically but not a support theorem.
Cutoff profiles f(r) Theta(R-r) can create delta-shell diagnostics from f(R) and slope/flux diagnostics from f'(R).
Compact support requires structural origin, f(R)=0, f'(R)=0/no-flux, shell absence, recovery independence, no hidden tuning, no A-tail, no scalar tail, and source compatibility.
Smooth transition layers must have zero C_layer, q_layer, I_layer, sigma_layer, alpha_recovery, and source_load, with structural origin.
Recovery-selected support radius, smoothing width, AB/gamma coefficients, residual tail status, boundary data, and layer data remain rejected.
Matching/support/layer laws must preserve A-sector source routing and create no duplicate shell/scalar/current/repair/parameter source loads.
Real matching/support law still requires structural support origin, value matching, slope/no-flux matching, distributional shell absence, transition layer neutrality, recovery independence, source compatibility, residual non-reentry, and no repair route.
Compact support, no-shell matching, transition neutrality, boundary/scalar silence, and parent equation remain not ready.
```

## F.5 Group 24 — Metric-Insertion Retest and Requirements Audit

Current outcome:

```text
B_s/F_zeta insertion target clarified.
A-sector exterior is the recovery anchor, not a spatial metric construction.
AB=1, B=1/A, gamma_like, and areal kappa remain downstream recovery diagnostics.
Count-once trace burden is explicit:
  L_double = e_kappa_metric + epsilon_vac_metric + kappa_metric + zeta_residual_metric
  must vanish or remain strictly inert.
Gamma/AB diagnostics are classified as audit-only.
Boundary/support guardrails from Groups 22/23 remain active for metric insertion.
Source no-double-counting guardrails remain active for metric insertion.
Metric insertion theorem obligations are explicit.
B_s/F_zeta insertion remains not solved.
Count-once recombination remains the central unresolved burden.
Parent equation remains not ready.
```

---

# Appendix G — Compact Final Current Summary

```text
A-sector remains the strongest reduced branch.

A_spatial / B_s remains a recovery theorem target.

The conformal-volume split
  gamma_ij = exp(2 zeta/3) bar_gamma_ij,
  det bar_gamma = 1,
is structural and supports zeta as spatial volume scalar,
but it is not B_s dynamics.

B_s/F_zeta insertion remains a theorem target.

J_V / u_vac remains unresolved.

Exchange continuity remains a theorem target, not a law.

Sigma/R split is role-level only.

Flux direction is missing.

No-overlap O remains theorem-targeted and deferred.

Residual-kill / non-metric residual is the safest provisional convention.

Boundary safety is required and not derived:
  no exterior zeta/kappa charge,
  no far-zone scalar flux,
  no M_ext shift,
  no shell source,
  no boundary repair.

Recovery remains downstream:
  gamma_like, AB, areal kappa, and Schwarzschild-compatible exterior behavior
  may test the branch but may not construct it.

Kappa remains diagnostic / non-metric unless derived.

Curvature energy / finite admissibility status:
  curvature admissibility can diagnose or filter;
  e_curv can account but not source;
  J_curv is not defined;
  curvature balance law is theorem target only;
  boundary/mass neutrality is required but not derived;
  anti-singularity remains theorem target, not derived prediction.

Vacuum current split status:
  J_V remains unresolved;
  J_sub/J_exch split is role-level only;
  J_sub is pure-wind theorem target only;
  J_exch is active-exchange theorem target only;
  pure wind neutrality is required but not derived;
  ordinary matter decoupling is required but not derived;
  no ordinary-sector source side for J_exch is derived;
  zero-net exchange, zero creation, curvature-from-warping,
  and latent exchange remain safest ordinary-sector branches;
  no dark-sector coupling is required;
  H_exch/H_curv remain deferred.

Parent correction tensor status:
  H_curv is not defined;
  H_exch is not defined;
  neither correction tensor is insertable;
  divergence safety is required but not derived;
  source separation is required but not derived;
  boundary/mass neutrality is required but not derived;
  diagnostic-only H-like audit objects are the only safe current route;
  parent equation forms are theorem targets only;
  the final parent field equation is not ready.

The theory should not yet write a final parent equation.

The next honest target is:
  residual-kill or no-overlap theorem,
  role-specific boundary projectors,
  source-compatible boundary laws,
  or reduced observational audit,
not parent closure.
```

Compact closure rule:

```text
No correction tensor is earned.
No Bianchi-like language substitutes for divergence safety.
No parent equation gate opens without defined, separated, boundary-neutral tensors.
No boundary/scalar silence theorem is earned.
No compact-support theorem is earned.
No toy profile substitutes for no-shell matching.
No repair route substitutes for boundary neutrality.
No smooth-support theorem is earned.
No no-shell matching theorem is earned.
No transition-layer neutrality theorem is earned.
No recovery-independent seam construction is earned.
No source-compatible matching law is earned.
No metric insertion is earned.
No count-once recombination theorem is earned.
No residual-kill theorem is earned.
No active no-overlap operator is earned.
No gamma-like recovery is earned without smuggling.
No parent equation gate opens from reduced recovery or metric-insertion retest alone.
```

