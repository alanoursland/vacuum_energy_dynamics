# Field Equation Trials: Introduction and Starting State

## What This Folder Is

This folder is the successor to `field_equation_candidates/` (archived) and the
constructive continuation of `projection_origin_probe/` (internally closed).

It inverts the failed search's polarity. The archived search was structurally
subtractive: constrain, exclude, defer. Its postmortem found that the best
mathematics arrived only after a concrete object was forced onto the table
(Rule 1: no object, no theorem attempt). This folder therefore starts from
concrete candidate functionals and runs them through the gate stack the
previous two campaigns built.

The working unit is a **trial**: one named candidate functional, stated boldly
enough to be killable, fed through the gates in order of cheapest kill first.

```text
field_equation_candidates:  built the filter, found no candidates.
projection_origin_probe:    closed the formal mysteries, localized the gap.
field_equation_trials:      feeds candidates to the filter.
```

Tiny goblin charter:

```text
Bring objects, not labels.
The gates eat first.
What survives gets a coefficient.
```

---

## 1. Starting State (What Is Already Established)

### 1.1 The theory layer

Postulates P1–P8 plus SR imports. Theorems T1–T9 recover the static exterior
weak field through one post-Newtonian order: T1/T2 (redshift, time dilation)
unconditional from P1–P6; T3 (`AB = 1`, hence gamma = 1) conditional on P7;
T4 (`d ln alpha = -dU/c^2`, hence beta = 1) conditional on P8; T5–T9 assemble
the metric and the classical tests. P7 and P8 are explicit recovery postulates:
**any trial functional must derive them in the static source-free exterior
limit, or it fails.**

### 1.2 The localization result

Two independent campaigns (the FEC search and the probe chain) converged on
the same diagnosis: all remaining dynamics live in one object,

```text
S_vac[X] = integral ( V_local(X) + K_strain(X, grad X, ...) ),

K_strain = K_GR + epsilon * K_residual.
```

The local part is strongly constrained (quadratic directional response ->
metric as Hessian). The strain part is unspecified. Outcomes per trial:

```text
epsilon = 0 forced:      ontology-based rederivation of GR.
epsilon != 0 derived:    candidate extension of GR with named residual.
underdetermined:         the candidate does not supply the missing axiom.
killed by a gate:        negative result; record and archive.
```

All four outcomes are deliverables.

### 1.3 The solved formal layer

The projection hierarchy is internally finished and available as a **test**,
not a mystery:

```text
r_k = (2k-1)/(2k+3)        closed: R=0 moment-kernel coefficient.
m = 2                      closed: selected by bounded-response admissibility
                           (f = u/a^3 bounded) and by boundary flux silence
                           (m=1 fails derivative silence).
A[k,j]                     cross-Gram of two bases of ker C_0 under positive
                           pairing; invertible for all N.
u = a^3 f                  transforms the weighted energy
                           E[f] = (1/2)<Lf,Lf>_w - <S,f>_w,  w = (1-x^2)^4,
                           L[f] = (1-x^2)f' - 6xf
                           into ordinary Dirichlet form: -u'' = aS.
```

The one external residue: why this energy functional, this chart, this weight
— physically. Trials may answer it; Trial B below targets it directly.

---

## 2. Candidate Roster

### Trial A: UFFT (Unified Frustration Field Theory)

Source: `ontology_and_mechanism/unified_frustration_field_theory_memo.md`.

Classification: elastic-medium + relaxation branch of the K_strain families,
with an **explicitly routed extra field** — the legal form of an epsilon != 0
candidate under the probe's "no un-routed fields" gate. Unifies the two free
ends of the GR-branch closure (epsilon and Lambda) in one mechanism.

Fields:

```text
phi   bulk frustration order parameter (sets Lambda)
chi   dimensional-relaxation phase coordinate, chi in [0,1]
```

Bulk sector:

```text
V_phi(phi) = rho_0 + (1/2) m_f^2 phi^2 + (lambda_phi/4) phi^4

phi_star = sqrt(-m_f^2 / lambda_phi)          (m_f^2 < 0)

rho_f = rho_0 - m_f^4/(4 lambda_phi)

T_munu^(f) = -rho_f g_munu   =>   Lambda_f = (8 pi G / c^4) rho_f
```

Relaxation sector (mechanical boundary form):

```text
V(chi, a) = (1/2) alpha(a) chi^2 - (1/3) beta chi^3 + (lambda/4) chi^4

alpha(a) = alpha_0 - gamma / a^2

chi_star(a) = [beta + sqrt(beta^2 - 4 lambda alpha(a))] / (2 lambda)
```

First-order phase structure (decreasing a):

```text
a_disc = sqrt( gamma / (alpha_0 - beta^2/(4 lambda)) )    minimum appears
a_co   = sqrt( gamma / (alpha_0 - 2 beta^2/(9 lambda)) )  coexistence
a_sp   = sqrt( gamma / alpha_0 )                          spinodal
```

Laboratory pressure spectrum (the core CDR equation):

```text
Delta P(a) = -V(chi_star, a) - gamma chi_star^2 / a^2 - 3C/a^4,
C = pi^2 hbar c / 720
```

Crossover scale where Casimir density meets dark energy:

```text
a_Lambda = (pi^2 hbar c / (720 rho_Lambda))^(1/4)  ~  30 microns
```

Tidal sector (Newtonian):

```text
alpha_eff(x) = alpha_0 - kappa E_ij E^ij,    E_ij = d_i d_j Phi

midpoint of equal-mass pair:  E_ij E^ij = 1536 G^2 M^2 / d^6

d_c = (1536 kappa G^2 M^2 / (alpha_0 - alpha_c))^(1/6)  ~  M^(1/3)
```

Covariant action and field equation:

```text
S = integral sqrt(-g) [ (c^4/16 pi G) R - rho_f(phi_star)
      - (1/2) M_f^2 g^munu grad_mu chi grad_nu chi
      - V_eff(chi, g) ] + S_m

V_eff(chi, g) = (1/2)(alpha_0 - kappa_W C^2) chi^2
                - (1/3) beta chi^3 + (lambda/4) chi^4,
C^2 = C_munurhosigma C^munurhosigma   (Weyl invariant)

M_f^2 Box_g chi = (alpha_0 - kappa_W C^2) chi - beta chi^2 + lambda chi^3

nucleation:  kappa_W C^2 > alpha_0 - alpha_c
```

Hysteresis/memory (thin wall):

```text
R_c = 3 sigma_chi / Delta rho
B   = 27 pi^2 sigma_chi^4 / (2 (Delta rho)^3)
Gamma/V ~ xi^-4 exp(-B/hbar)
```

Dark-bridge sign result: a relaxed region with Delta rho < 0 has

```text
Delta(rho + 3P) = -2 Delta rho > 0
```

so a vacuum-energy deficit gravitates as a positive effective source.

Parameter ledger (all currently free; each is a kill surface):

```text
alpha_0, beta, lambda      chi-potential shape
gamma                      mechanical boundary coupling (universal vs
                           material-sensitive: undecided)
kappa, kappa_W, kappa_K    tidal / Weyl / Kretschmann couplings
M_f                        chi gradient stiffness (healing length xi)
m_f^2, lambda_phi, rho_0   bulk frustration sector (fix rho_f, Lambda_f)
```

### Trial B: Measure-Conversion Bridge (1D toy -> projection chart)

Source: `intuition_models/1d_scalar_dissipation.md`.

The toy's bending energy is curvature-squared in physical measure:

```text
ds = e^phi dx,   D_s = e^-phi d_x,   kappa = e^-2phi q,
q = u_xx - phi_x u_x,
B/2 e^-3phi q^2 = B/2 e^phi kappa^2   (kappa^2 ds)
```

with exponential measure ladder e^-3phi -> e^-phi -> e^+phi structurally
parallel to the probe's a^2 -> a^3 -> a^4 -> a^5 ladder, and a
weighted-divergence first-order operator parallel to L[f] = a^-2 d(a^3 f)/dx.

Hypothesis to test: **the probe weights are measure-conversion factors between
coordinate and physical span, with the field's tensor weight setting the
exponent.** Concretely: restrict the toy to static profiles with phi(x) fixed
by a compactification profile and check whether the energy reduces to
(1/2)<Lf, Lf>_w with w = a^4. Either outcome is decisive for the chart
question (the probe's last external gap).

Secondary asset: the toy's reservoir field implements the relaxation
accounting identity the FEC chain demanded, by construction:

```text
d_t(e^phi R) = e^phi [eta_u u_t^2 + eta_phi phi_t^2 + Lambda H_eps(phi_t) phi_t^2]

d/dt [ E[u, phi] + integral e^phi R dx ] = 0     (no bottomless bucket)
```

### Trial C: Burden Decomposition (the sign fork, settled by calculation)

Sources: `ontology_and_mechanism/positive_curvature_energy_J_curv.md`,
`radius_scaling_positive_curvature_energy_j_curv.md`,
`gravity_as_vacuum_burden_reduction.md`,
`p4_sign_fork_infall_ledger.md`.

The candidate burden:

```text
E_burden = J_curv + E_interface + E_substance/exchange + ...
```

Established Newtonian-limit anchors:

```text
J_curv,ext(m, R) = G m^2 / (2R)                          positive
J_curv,total(uniform) = 3 G M^2 / (5R) = |U_self|
J_curv(m, lambda R) = (1/lambda) J_curv(m, R)            1/R scaling
J(m1) + J(m2) - J(m1+m2) = -G m1 m2 / R                  cross-term = U_grav
R -> 0  =>  J_curv -> infinity                           anti-singularity
```

The fork, sharpened: J_curv is superadditive (combining wells stores MORE
curvature energy; under positive-J accounting, infall must be funded:
substance destroyed = Delta_KE + Delta_J = 2 Delta_KE, the traceful branch
with P6 as payer). The interface toy (J ~ GM/R^2 ~ M^(1/3) at fixed density)
is subadditive (the traceless burden-reduction branch). The question is no
longer which sign — both components exist with known signs — but **which term
dominates the two-body ledger**, and that is a calculation:

```text
1. per-term two-body ledger (J_curv, interface, substance) vs separation;
2. check each dominance pattern against the merger-energy gate and the
   kappa-leak bound;
3. note: anti-singularity survives only where J_curv dominates admissibility.
```

---

### Trial D: Standing Frustration Ledger (registered post-A2)

Source: `ontology_and_mechanism/standing_frustration_ledger.md`.

The author's dark-sector intuition, distinguished from the memo's tidal
nucleation (killed at G26, Trial A2): the dark sector as the standing
energy cost of maintaining 3D structure — a ledger entry, no phase
transition, no tidal trigger. Entry gate D-G1: a uniform standing cost is
Lambda, not dark matter, so the candidate must first produce a mechanism
making the frustration cost cluster like halos (candidate mechanisms
D-M1..D-M4 in the note). The TVN-killing profile gate applies to this
candidate with full force.

### Trial E: Boundary Admissibility (registered 2026-06-12)

Source: theory-owner intuition, surfaced in discussion — "curvature at
mass boundaries must be smooth in VED because of curvature energy,
whereas GR allows but does not require non-smooth curvature."

Status of the intuition at registration: NOT a theorem of the trials.
The derived reduced static law is pointwise-algebraic in the source and
therefore transcribes source jumps into curvature jumps exactly as GR
does. The old transition-layer machinery (groups 052–065) was
quarantined diagnostic-only and never derived a forced layer. Trial E
exists to either earn the intuition as a property of K_strain or kill
it at a gate.

Entry gates:

- **E-G1 (sharp-source admissibility, reduced):** does the derived
  static sector admit step sources without pathology? (Expected: yes —
  the honest baseline that the intuition is not yet in the theory.)
- **E-G2 (GR control):** verify the conditional response handles the
  sharp boundary via standard junction behavior, so any later VED
  difference is real and not an artifact.
- **E-G3 (mechanism classification):** what structure in the parent
  would FORCE boundary smoothing, at what cost, and with what derived
  smoothing scale. Higher-curvature terms raise the equation order and
  force curvature continuity with a derived layer width — but face the
  Ostrogradsky/G20 ghost gate.

Prediction shape if the intuition survives: a minimum smoothing scale at
matter boundaries, where GR transcribes the source profile exactly — a
deviation in the kappa-leak family. Forecast verdict class:
UNDERDETERMINED at reduced level (constraint-recording), since the
decision lives in K_strain's higher-curvature content.

## 3. Gate Inventory (The Filter Stack)

Every trial faces these, cheapest kills first. A gate failure is a recorded
result, not a tuning opportunity. Recovery targets audit; they never construct.

### 3.1 Cheap discriminators (run first, toy-level)

```text
G1  two-body cross-term sign X(r) of the candidate's configuration energy
    (decides traceless/traceful infall; p4 sign fork)
G2  flat-vacuum stability (P5 ground state survives; no spontaneous curdling)
G3  gravitational-wave energy sign (binary pulsar spin-down is positive)
G4  scalar-radiation safety (no unsuppressed long-range breathing mode;
    monopole/dipole protected by conservation, quadrupole must be killed
    by mass gap, conversion, or projection)
```

### 3.2 Recovery gates (reduced, forge-scripted)

```text
G5  static exterior: derive P7 (AB = 1) — not assume it
G6  static exterior: derive P8 (d ln alpha = -dU/c^2 through O(c^-4))
G7  Newtonian limit with correct coefficient (areal flux F_A = 8 pi G M/c^2)
G8  scalar-sector admissibility: the candidate's static scalar reduction
    must reproduce the bounded-response problem -u'' = aS — ideally
    DERIVING the chart and w = a^4 (Trial B is the direct attack)
```

### 3.3 Fortress gates (inherited from field_equation_candidates)

```text
G9   mass coin: delta M_A = 0 for every non-A sector
     (M_A = c^2 F_A / (8 pi G); a q/r A-tail shifts M_A by -c^2 q/(2G))
G10  scalar-tail silence: any C/r sector tail carries flux -4 pi C; C = 0
     sector-by-sector (total cancellation does not count)
G11  count-once trace: L_double = 0; zeta enters the metric once
G12  source no-double-counting: rho routes to the A-sector only
G13  boundary no-shell: value AND slope matching (C1 value-match still
     carries flux -4 pi R phi_0); smoothness is not neutrality
G14  no-repair: no counterterms, repair currents, O-by-name, dark patches,
     or recovery-tuned parameters
```

### 3.4 Probe gates (covariant structure)

```text
G15  quadratic/parallelogram response -> metric (nonquadratic residual must
     be routed explicitly as Finsler/medium/constitutive epsilon)
G16  calibration-coherent transport -> Levi-Civita (torsion/nonmetricity
     need explicit defect ledgers)
G17  shared-metric matter coupling -> stress tensor route
G18  no un-routed extra fields (routed fields legal; UFFT's chi qualifies)
G19  Weyl/TT sector: tensor radiation present, scalar ladder rank-deficiency
     respected (no scalar completion of the tensor sector)
G20  D=4 Lovelock/locality/boundary-differentiability bookkeeping vs the
     candidate's action terms (Weyl^2 couplings: check ghosts/instabilities)
```

### 3.5 Observational gates (numbers, not vibes)

```text
G21  Cassini: |gamma - 1| < 2.3e-5  (kappa-leak budget)
G22  perihelion/LLR: beta = 1
G23  binary pulsar: orbital decay matches GR quadrupole (bridge hysteresis
     and any chi-sector drag must hide under this)
G24  LIGO: merger energy ~ few % of M c^2 with chirp-mass scaling
     (merger_energy_scale_check.md is the spec)
G25  short-range gravity: torsion-balance / microcantilever bounds at
     10-100 microns (UFFT's a_Lambda ~ 30 micron crossover sits exactly
     here — likely the cheapest UFFT kill or first survival)
G26  solar-system Weyl screening: kappa_W C^2 below nucleation threshold
     for Sun/planets, or a derived screening mechanism
G27  equivalence principle: composition-independent coupling (P6 per-energy)
G28  cosmology (deferred until statics pass): expansion history, structure
     growth, CMB, no early-universe transition catastrophe
```

### 3.6 Discipline gates (process)

```text
G29  status vocabulary: DERIVED / CONDITIONAL / MATCHED / DIAGNOSTIC /
     THEOREM_TARGET / KILLED — no candidate advertised above its status
G30  compatibility-vs-origin: a value solved-for is not a value derived
     (the c = 3 ell/(2R) standard: derive it from structure or label it)
G31  every trial ends in a verdict document, including kills
```

---

## 4. Trial Protocol

1. One folder per trial: `01_ufft/`, `02_measure_bridge/`, `03_burden_ledger/`.
2. Scripts follow the probe convention: `make_N_name.py` (sympy) emits
   `N_name.md`; claims in the md are backed by validated checks in the py.
   Record actual symbolic content, not archive markers
   (see `field_equation_candidates/marker_to_derivation.md`).
3. Gates are run cheapest-first; a kill stops the trial and produces the
   verdict document immediately. No candidate hoarding: a trial survives
   only while it has a live theorem target or an unrun gate.
4. Parameters may be *bounded* by gates; they may never be *selected* by
   recovery (G30). A parameter chosen to pass a gate demotes the result
   to MATCHED.
5. The trichotomy verdict (epsilon = 0 / epsilon != 0 / underdetermined /
   KILLED) is stated explicitly at the end of every trial.

## 5. Opening Schedule

```text
Trial A (UFFT):    A1 short-range gravity bounds at the 30-micron crossover
                   A2 chi scalar-radiation safety (mass gap from alpha_0)
                   A3 solar-system Weyl screening estimate
                   A4 flat-vacuum stability and ghost check of Weyl^2 coupling
                   A5 binary-pulsar / merger gates
                   A6 static exterior recovery (G5-G8)

Trial B (bridge):  B1 static reduction of the 1D toy under compactification
                      profiles; target: derive (or kill) w = a^4
                   B2 if derived: physical identification of x, f, S
                      (lifting the probe's last external gap)

Trial C (burden):  C1 per-term two-body ledger vs separation
                   C2 dominance patterns vs merger gate and kappa-leak bound
                   C3 anti-singularity status per branch
```

Trials A and B are independent and can run in parallel. Trial C feeds both
(its verdict constrains which energy bookkeeping A and B are allowed to use).

## 6. What Would Count as Winning

Smallest win: one candidate killed cleanly (the machine works on real ore).

Middle win: Trial B derives the chart — the projection hierarchy becomes
physics and the probe closes entirely.

Large win: a candidate passes G1–G27 with epsilon != 0 and a named,
observationally live residual. That residual is the theory's first
genuine prediction beyond GR — and the first entry in the spacetime
engineering catalog.

Honest expectation: kills. Kills are the system working.

```text
The forge is lit.
First ingot on the anvil.
```
