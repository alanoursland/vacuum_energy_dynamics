# Development Status Map

## Purpose

This document is a top-level status map for the `theory_v3/development/` tree.

It is not a postulate, theorem, proof, or field equation. It is an organizational document.

Its purpose is to track:

```text
what has been explored,
what the current result/status is,
where the supporting files live,
what depends on what,
and what the next useful move appears to be.
```

The development tree currently organizes work into:

```text
background_geometry/
field_equation_candidates/
intuition_models/
lab_reports/
ontology_and_mechanism/
```

This map cuts across those folders.

---

## Status Legend

```text
stable reduced result:
  internally consistent reduced-sector result supported by forge/script work

candidate:
  plausible mechanism or interpretation, not yet proven

negative result:
  useful failed derivation or reframing

gauge-warning:
  result constraining how reduced variables may be interpreted

open:
  unresolved target or future work
```

---

## Current Main Development Branch

The current main branch is the reduced static-spherical exterior program.

The chain is:

```text
log-scale mode decomposition
  -> kappa controls reciprocal scaling
  -> kappa suppression allows AB = 1
  -> shear mode s carries compensated exterior distortion
  -> shear source law gives weak-field 1/r profile
  -> reduced exterior action unifies kappa suppression and shear sourcing
  -> gauge studies clarify that kappa and s are areal-gauge reduced variables
  -> regime studies classify exchange, creation/destruction, and relaxation
```

In equations:

$$a=\ln A,$$

$$b=\ln B,$$

$$\kappa=\frac{a+b}{2},$$

$$s=\frac{a-b}{2},$$

and:

$$AB=e^{2\kappa}.$$

Thus, in static spherical areal gauge:

$$\kappa=0\quad\Longleftrightarrow\quad AB=1.$$

The reduced exterior target is:

$$\kappa=0,\qquad s\neq0.$$

The candidate shear source law is:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

For a spherical source:

$$s(r)=-\frac{2GM}{rc^2}.$$

Then:

$$A=e^s\approx1-\frac{2GM}{rc^2},$$

and:

$$B=e^{-s}\approx1+\frac{2GM}{rc^2}.$$

This is the best-developed reduced branch so far.

---

## Folder Map

### `background_geometry/`

Current files:

```text
lorentzian_manifold_as_formal_home.md
```

Status:

```text
background / formal home
```

Role:

This folder provides the general geometric setting for the theory. It is not yet tightly integrated with the reduced exterior mode program.

Current need:

The reduced variables \(\kappa\) and \(s\) need a gauge-aware or covariant parent. That future work should eventually connect back to this folder.

---

### `field_equation_candidates/`

Current visible candidate files include:

```text
candidate_areal_gauge_kappa_condition.py
candidate_covariant_parent_modes.md
candidate_exchange_creation_relaxation_regimes.md
candidate_exterior_shear_source_law.md
candidate_gauge_dependence_modes.py
candidate_reduced_exterior_action.md
candidate_regime_map_observations.md
log_scale_modes_candidate.md
```

Status:

```text
active candidate branch
```

Role:

This folder contains the active speculative mechanisms and candidate field-equation structures.

Current note:

Several scripts are listed here. If the repo policy is to keep scripts in `scripts_v3/`, then the `.py` files may eventually need either to move or to be represented here by `.md` notes that reference the scripts.

---

### `lab_reports/`

Current visible lab reports include:

```text
candidate_exchange_creation_distinction_lab_report.md
kappa_suppression_lab_report.md
log_scale_modes_lab_report.md
log_scale_modes_v2_lab_report.md
p3_volume_preservation_lab_report.md
reduced_exterior_mode_program_summary.md
shear_profile_source_law_lab_report.md
```

Status:

```text
evidence / experiment record
```

Role:

This folder records forge/script results, including positive tests, negative tests, and summary conclusions.

Current note:

The lab reports are the evidence layer. Candidate notes should not overclaim beyond what these reports support.

---

### `ontology_and_mechanism/`

Current files:

```text
gravity_as_vacuum_burden_reduction.md
merger_energy_scale_check.md
```

Status:

```text
ontology / interpretation
```

Role:

This folder appears to hold conceptual mechanism notes rather than reduced field-equation candidates.

Current need:

The exchange/creation/relaxation regime work may eventually belong here if promoted from field-equation candidate classification into ontology architecture.

---

### `intuition_models/`

Current files:

```text
informal_continuum_graph_model.md
```

Status:

```text
intuition / metaphor / informal model
```

Role:

This folder holds informal models. It should remain separated from formal candidate claims.

Current note:

The slogan:

```text
Gravity is the compensated shear left after the source-free vacuum suppresses imbalance.
```

belongs at the intuition level unless explicitly tied to reduced equations.

---

## Candidate Status Table

| Candidate / report | Current status | Key result | Main caveat | Next action |
|---|---|---|---|---|
| `log_scale_modes_candidate.md` | stable reduced result | \(\kappa=(\ln A+\ln B)/2\) controls \(AB=e^{2\kappa}\) | static spherical reduced sector | keep as foundation of reduced branch |
| `log_scale_modes_lab_report.md` | evidence | first log-scale test established the mode split | superseded/refined by v2 | preserve as history |
| `log_scale_modes_v2_lab_report.md` | evidence | clarified tautology/leak controls and trace-kernel behavior | reduced toy only | preserve as stronger report |
| `kappa_suppression_lab_report.md` | stable reduced result | source-free toys suppress \(\kappa\) while allowing \(s\neq0\) | not covariant, not source law | use as basis for exterior compensation |
| `candidate_exterior_shear_source_law.md` | candidate | \(\nabla^2s=8\pi G\rho/c^2\) gives \(s=-2GM/(rc^2)\) | assumes source law and flux normalization | connect to reduced action |
| `shear_profile_source_law_lab_report.md` | evidence | forge confirmed radial Laplace/flux chain | does not derive the equation | preserve as support |
| `candidate_reduced_exterior_action.md` | strongest reduced action candidate | one toy action gives \(\kappa\)-suppression and shear source law | non-covariant areal-gauge toy | next: covariant/gauge-aware parent |
| `candidate_covariant_parent_modes.md` | candidate / parent-mode reconnaissance | \(\kappa\) resembles reduced trace/conformal mode; \(s\) resembles reduced trace-free shear | not covariant yet | continue with gauge-aware formulation |
| `candidate_gauge_dependence_modes.py` | gauge-warning script | naive \(\kappa,s\) shift under \(r=f(R)\) | script not a final note | keep result in gauge warning docs |
| `candidate_areal_gauge_kappa_condition.py` | gauge-fixed formulation script | \(\kappa_{\rm areal}=0\) becomes \(TQ=(S')^2\) | static spherical only | preserve as gauge-safe formulation |
| `candidate_areal_gauge_kappa_condition.md` | stable gauge-fixed result | \(\kappa=0\) is safe as areal-gauge condition, not invariant scalar | not nonspherical | use language consistently |
| `p3_volume_preservation_lab_report.md` | negative result | P1+P3 equate energy and volume, but do not define exchange | does not close equal-response gap | motivates regime distinction |
| `candidate_exchange_creation_relaxation_regimes.md` | candidate ontology/classification | separates exchange, creation/destruction, relaxation | not derived from postulates | test and map to observations |
| `candidate_exchange_creation_distinction_lab_report.md` | evidence / stable classification test | exchange gives \(J_\kappa=0\), creation/destruction source \(\kappa\) | does not prove nature uses regimes | use for regime map |
| `candidate_regime_map_observations.md` | reality-facing candidate map | maps regimes to static gravity, cosmology, waves, collapse, deviations | no quantitative constraints yet | next: kappa-leak deviation script |
| `reduced_exterior_mode_program_summary.md` | branch summary | connects log-scale, \(\kappa\)-suppression, shear source law, weak-field metric | needs updates as branch grows | keep as branch overview |

---

## Current Stable Reduced Results

### 1. Log-scale mode split

Status:

```text
stable reduced result
```

Result:

$$\kappa=\frac{\ln A+\ln B}{2},$$

$$s=\frac{\ln A-\ln B}{2},$$

and:

$$AB=e^{2\kappa}.$$

Interpretation:

```text
kappa = reduced imbalance / trace-like mode
s = reduced compensated shear mode
```

Caveat:

This is static spherical reduced language.

---

### 2. Kappa suppression

Status:

```text
stable reduced result
```

Result:

Source-free exterior toy functionals can suppress:

$$\kappa=0$$

while allowing:

$$s\neq0.$$

Interpretation:

```text
source-free exterior resists imbalance while allowing compensated shear
```

Caveat:

The mechanism is still reduced and not covariant.

---

### 3. Shear source law

Status:

```text
candidate supported by forge
```

Result:

If:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho,$$

then for spherical mass:

$$s(r)=-\frac{2GM}{rc^2}.$$

This gives the weak-field exterior metric coefficients when \(\kappa=0\).

Caveat:

The source law is not yet derived from deeper postulates.

---

### 4. Reduced exterior action

Status:

```text
strongest reduced action candidate
```

Candidate density:

$$L
=
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
+
\alpha\rho s.$$

With:

$$\alpha=\frac{16\pi G K_s}{c^2},$$

the variation gives the desired reduced equations.

Caveat:

This is not a covariant action.

---

### 5. Gauge correction

Status:

```text
stable gauge-warning / gauge-fixed result
```

Naive modes shift under radial reparameterization:

$$\kappa\rightarrow\kappa+\ln f'(R),$$

$$s\rightarrow s-\ln f'(R).$$

Therefore \(\kappa\) and \(s\) are not raw invariant scalar fields.

Safe formulation:

For:

$$ds^2=-T(R)c^2dt^2+Q(R)dR^2+S(R)^2d\Omega^2,$$

define areal radius:

$$r_{\rm areal}=S(R).$$

Then:

$$\kappa_{\rm areal}
=
\frac12\ln\left(\frac{T(R)Q(R)}{[S'(R)]^2}\right).$$

The compensation condition is:

$$\kappa_{\rm areal}=0,$$

equivalently:

$$T(R)Q(R)=[S'(R)]^2.$$

Caveat:

Static spherical only.

---

### 6. Exchange / creation / relaxation regimes

Status:

```text
stable reduced classification, not yet ontology proof
```

Exchange:

$$J_a=S,\qquad J_b=-S.$$

Then:

$$J_\kappa=0,\qquad J_s=S.$$

Creation/destruction:

$$J_a=\pm C,\qquad J_b=\pm C.$$

Then:

$$J_\kappa=\pm C.$$

Interpretation:

```text
exchange supplies compensated shear
creation/destruction source traceful kappa
relaxation drives imbalance toward zero
```

Caveat:

The theory has not derived the exchange/creation distinction from postulates.

---

## Main Open Questions

### 1. Covariant parent

Current question:

```text
What full geometric/covariant structure reduces to kappa and s in static spherical areal gauge?
```

Status:

```text
open
```

Likely next work:

```text
candidate_orbit_space_modes.py
candidate_orbit_space_modes.md
```

or:

```text
candidate_covariant_parent_modes_v2.md
```

---

### 2. Reduced action derivation

Current question:

```text
Can the reduced exterior action be derived from deeper ontology or variational principles?
```

Status:

```text
open
```

Key issue:

The reduced action works algebraically, but its coefficients and coupling structure are not derived.

---

### 3. Exchange/creation distinction

Current question:

```text
Is exchange vs creation/destruction derived from existing postulates, or does it need to become a structural principle?
```

Status:

```text
open
```

Current result:

P1+P3 identify energy and volume, but they do not classify process type.

---

### 4. Kappa-leak deviations

Current question:

```text
If kappa is small but nonzero, what observable deviations appear?
```

Status:

```text
next quantitative target
```

Proposed script:

```text
candidate_kappa_leak_deviation.py
```

Reason:

This is the first likely route toward falsifiable deviations from GR-like weak-field behavior.

---

### 5. Cosmological creation

Current question:

```text
Can expansion be modeled as traceful vacuum creation?
```

Status:

```text
speculative / future
```

Recommendation:

Do not prioritize until kappa-leak weak-field consequences are clearer.

---

### 6. Dynamic shear and gravitational waves

Current question:

```text
What is the time-dependent tensorial parent of the shear mode?
```

Status:

```text
future
```

Recommendation:

Do after static/gauge/covariant parent work.

---

## Recommended Next Work

### Immediate next quantitative script

```text
candidate_kappa_leak_deviation.py
```

Purpose:

Test a small nonzero \(\kappa\) mode:

$$\kappa(r)=\varepsilon_\kappa(r),$$

with the usual shear profile:

$$s(r)=-\frac{2GM}{rc^2}.$$

Then:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Compute weak-field deviations in:

```text
A coefficient
B coefficient
AB product
gamma-like response
possible PPN-style deviation proxy
```

Reason:

The regime map identified mixed shear + traceful leakage as the first natural deviation channel.

---

### Immediate next conceptual note

```text
candidate_kappa_leak_deviation.md
```

or after the script:

```text
kappa_leak_deviation_lab_report.md
```

Purpose:

Record whether small \(\kappa\)-leak is observationally plausible or already tightly constrained.

---

### Medium-term work

```text
candidate_orbit_space_modes.py
```

Purpose:

Express static spherical geometry in terms of a 2D orbit space plus areal-radius scalar, and see whether \(\kappa_{\rm areal}\) and \(s\) can be represented in a more gauge-aware way.

---

## Candidate Dependency Graph

```text
log_scale_modes_candidate
  -> log_scale_modes_lab_report
  -> log_scale_modes_v2_lab_report
  -> kappa_suppression_lab_report
  -> reduced_exterior_mode_program_summary

kappa_suppression_lab_report
  -> candidate_exterior_shear_source_law
  -> shear_profile_source_law_lab_report
  -> candidate_reduced_exterior_action

candidate_reduced_exterior_action
  -> candidate_covariant_parent_modes
  -> candidate_gauge_dependence_modes
  -> candidate_areal_gauge_kappa_condition

p3_volume_preservation_lab_report
  -> candidate_exchange_creation_relaxation_regimes
  -> candidate_exchange_creation_distinction_lab_report
  -> candidate_regime_map_observations

candidate_regime_map_observations
  -> candidate_kappa_leak_deviation.py
```

---

## Current Best One-Paragraph Summary

The reduced exterior development branch has produced a coherent static-spherical areal-gauge toy program. The log-scale split identifies \(\kappa\) as the reciprocal-scaling control mode and \(s\) as the compensated shear mode. Kappa-suppression toys show that source-free exteriors can relax to \(\kappa=0\) while allowing \(s\neq0\). A candidate shear source law gives \(s(r)=-2GM/(rc^2)\), recovering the weak-field exterior metric when \(\kappa=0\). A reduced action unifies these two mechanisms. Gauge studies show that \(\kappa\) and \(s\) are not invariant scalar fields but are meaningful as areal-gauge reduced variables. Regime studies distinguish conservative exchange, traceful creation/destruction, and relaxation, identifying mixed \(\kappa\)-leak as a possible deviation channel. The next quantitative target is to compute observational consequences of small nonzero \(\kappa\).

---

## Status Snapshot

```text
Most stable reduced result:
  log-scale kappa/s split and AB = exp(2 kappa)

Strongest mechanism candidate:
  reduced exterior action

Most important caution:
  kappa and s are areal-gauge reduced variables, not raw invariant fields

Most important negative result:
  P1+P3 do not derive exchange; they only equate energy preservation and volume preservation

Most promising deviation channel:
  small kappa-leak / mixed exchange+creation

Best next script:
  candidate_kappa_leak_deviation.py

Best next long-term theory goal:
  covariant/gauge-aware parent of kappa and s
```
