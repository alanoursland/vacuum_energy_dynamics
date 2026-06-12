# Vacuum Field Equations — Status of Record

**Updated:** 2026-06-12 (field equation trials program)
**Supersedes:** the Groups 01–96 snapshot previously in this file (preserved
below as a historical appendix). The "All-Order Parity Gap Theorem"
bottleneck described there was dissolved: the projection hierarchy was
solved in full ($r_k=(2k-1)/(2k+3)$ identified as the $R=0$
boundary/admissibility coefficient, $m=2$ proved, the regularity ladder
$r_{R,k}=(2k-1)/(2k+2R+3)$ derived, and the $\det(A_N)\neq 0$ puzzle
explained by cross-Gram invertibility — positivity fails at $N=11$ because
the cross-Gram is not a Gram, and invertibility never needed positivity).
See `projection_origin_probe/` and `field_equation_candidates/proof_chain_seam_map.md`.

***

## Abstract

The static sector of the theory is now **derived, not matched**. From the
adopted postulate set (P1–P6, P7′, P9) the trials program derived the
exterior field equation, its self-coupling structure, the sign and
stability architecture of every sector, and the first parameter-free
deviation prediction. The remaining center of gravity is one object: the
**covariant strain functional $K_{\text{strain}}$** — the parent equation
whose reduced limits are now all theorem-shaped.

## 1. The adopted postulate set

| Postulate | Status |
|---|---|
| P1–P6 | Ontological core (vacuum = energy = spacetime; constant density; curvature = spatial differential; curvature carries energy; minimum-energy; P6 exchange) |
| **P7′** (static frame indifference) | **Adopted 2026-06-11**, defined at the limit: exact as $H\to 0$; real exteriors carry $AB-1 = O(H_0 r/c)$ |
| P7 ($AB=1$) | Demoted to P7′'s metric shadow |
| P8 (temporal self-coupling) | A 1PN **theorem** under P9 (formal rewrite pending) |
| **P9** (configuration energy gravitates) | **Adopted 2026-06-11**, fenced: source status is earned by presence in the adopted dynamical law, counted exactly once |

**Zero recovery-shaped postulates remain.** Nothing in the set was
adopted to force agreement with GR; agreement is an output.

## 2. The static sector — derived complete (reduced level)

Reduced variables: $\kappa=\tfrac12\ln(AB)$ (trace), $s=\tfrac12\ln(A/B)$
(shear); under P7′, $\kappa\to 0$ and $A=e^s$.

**The areal-flux law (the field equation):**
$$\Delta_{\text{areal}}\,A \;=\; \frac{8\pi G}{c^2}\,\rho,
\qquad A=e^{s}$$

**Its self-coupling content (Trial C2 bootstrap identity):**
$$\Delta_{\text{areal}}\,s \;=\; -(s')^2 \;+\; \text{source},
\qquad u_{\text{field}} \;=\; -\frac{c^4 (s')^2}{8\pi G}$$

The linearizing exponential is not a trick: it is P9's count-once
placement, with the field's own (negative) configuration energy as the
nonlinear source. The one-parameter family $A_\lambda=(1+\lambda
r_s/r)^{-1/\lambda}$ is closed by the bootstrap selector to $\lambda=-1$:
$$A \;=\; 1-\frac{2GM}{c^2 r}$$
— the Schwarzschild exterior, derived. Trial C3 proved
$G^t{}_t-G^r{}_r=-(\ln AB)'/(rB)$, so P7′ ⟺ radial-boost invariance of
the source, and killed the explicit-scalar-source placement of the
configuration energy: the count-once placement is **geometry-side,
forced**.

## 3. Sector-indefinite signature — complete (reduced level)

| Sector | Sign | Character | Established by |
|---|---|---|---|
| Temporal ($s$, static) | **Negative** | Non-propagating (forced), source-slaved | C2 + P9; ghost exclusion (G03/T2); uniqueness $A\equiv 1$ at zero source (G02) |
| Radiative (TT) | **Positive** | Propagating, outward flux | G03: sum-of-squares energy density; sign anchored by binary-pulsar spin-down |

This is the architecture by which GR survives its conformal-factor
problem — here it is *derived*: the scalar sector **must** be a
constraint because the alternative is a ghost draining into the TT
sector. The negative reservoir cannot be mined except by moving sources
through the positive channel.

## 4. Other sectors

* **Radiative coupling $K_T$:** **DERIVED** (2026-06-12, radiative
  bootstrap, group 008): $K_T = c^4/16\pi G$ per polarization, forced
  by P9 self-sourcing at the static sector's own normalization
  $N=c^4/8\pi G$. The quadrupole chain closes with no free constants —
  amplitude coefficient $2G/c^4$, projector average $2/5$,
  $P=(G/5c^5)\langle\dddot Q_{ij}\dddot Q_{ij}\rangle$ — and the
  binary-pulsar anchor passes as a kill condition, not a calibration.
  **Zero matched coefficients remain in the reduced theory.**
* **Vector / frame-dragging ($W_i$):** structural; sourced by transverse
  matter current via the continuity identity. Normalization not yet
  derived.
* **Trace ($\kappa$):** no longer "must be strictly killed" — under P7′
  at the limit it is a **predicted channel**: the κ-leak
  $$AB-1 \;=\; O\!\left(\frac{H_0 r}{c}\right) \;\sim\; 10^{-15}
  \text{ at 1 AU}$$
  — the theory's first parameter-free deviation from GR.

## 5. Trial scoreboard

| Trial | Result |
|---|---|
| B1 (measure bridge) | Probe energy = physical Dirichlet energy under forced $\nu=2$, $\kappa_\omega=3$ ($w=a^4=3+3-2$); structural upgrade |
| C1 (burden reduction, long range) | **KILLED** — positive branch repulsive, interface separation-blind |
| C2 (self-coupling bootstrap) | Sign resolved negative; Schwarzschild selected; → P9 adoption |
| C3 (spatial bootstrap) | Placement resolved geometry-side; → P7′ adoption |
| A2 (UFFT tidal sector, TVN) | **KILLED** at G26 (up-set theorem, $4.7\times10^{33}$ hierarchy) — memo §15–19 only; the Casimir-gap core survives |
| D1 (depletion-history halos) | **KILLED** parameter-free: budget/requirement $=\eta v^2/5c^2\sim10^{-7}$, shortfall ≥2000× at maximum generosity |
| G02/G03 | **PASS** — sector signature complete |
| 008 (radiative bootstrap) | **SUCCESS** — $K_T$ derived; zero matched coefficients remain |
| E1 (sharp-source gate) | **UNDERDETERMINED** (constraint-recording): reduced VED = GR at boundaries; smooth-boundary intuition ⟺ $\beta\neq0$ in $K_{\text{strain}}$, $\ell^*=\sqrt{\beta}$ |
| E2 (observable face of $\ell^*$) | Boundary smoothing ⟺ bench-top Yukawa (exact identity): $\ell^*<38.6\,\mu$m at $\|\alpha\|=1$ today; NS-tidal/GW channel **KILLED** (shortfall $\ge 3\times10^7$); window coincides with the UFFT squeeze |
| G20 (β health) | **Scalaron class PASSES, Weyl class KILLED**: unique ghost-safe realization $aR^2$ ($a>0$) + Gauss-Bonnet; $\alpha=+1/3$ exactly (positive sign), $\ell^*=\sqrt{6a}$, $\gamma_{\rm eff}=1/2$ inside $\ell^*$; radiative sector untouched |
| E3 (P7′ vs scalaron) | **Smooth-boundary route KILLED_BY_CONTRADICTION**: scalaron hair has $AB\neq1$ in static vacuum and is mandatory for $a\neq0$; P7′ ⟹ $a=0$. **K_strain ≤4-derivative sector CLOSED** = EH + Λ + GB exactly. Trial E resolved: VED boundaries = GR. Appeal path (P7′ re-scope) documented, default kill stands |

**Data gates:** the 3-layer protocol is operational with verified
anchors (Lee 2020, Tan 2020). Layer-2 Yukawa conversion done. Standing
quantitative squeeze on UFFT's Casimir sector:
$$29.9\,\mu\text{m} \;<\; a_{\text{disc}} \;<\; 38.6\,\mu\text{m}$$
(crossover below the $|\alpha|=1$ exclusion crossing — alive but cornered).

## 6. What is open

Ordered by centrality:

1. **The covariant $K_{\text{strain}}$ parent — local sector now
   CLOSED at ≤4 derivatives (E3):**
   $$K_{\text{strain}}\ (\le4\ \text{derivatives}) = \frac{c^4}{16\pi G}(R-2\Lambda) + \text{Gauss-Bonnet, exactly.}$$
   Chain: 008 forced the two-derivative normalizations; G20 reduced the
   four-derivative freedom to $aR^2$ ($a>0$); E3 showed P7′ forces
   $a=0$ (scalaron hair has $AB\neq1$ in static vacuum and is mandatory
   for $a\neq0$). All local gravitational physics of VED = GR. What
   remains open of the parent is its *non-EH* content: the B2 measure
   structure, the matter-coupling sector, Λ's origin, and the
   $H\neq0$ (κ-leak) branch — this is now where the program's novelty
   lives.
2. ~~Radiative bootstrap for $K_T$~~ — **CLOSED 2026-06-12** (group
   008); residual coefficient-free obligations: in-house
   closure-uniqueness proof (Deser 1970 currently cited), averaging
   rigor in the covariant lift.
3. **Covariant lifts** of the reduced theorems; nonlinear stability.
4. **Source-law origin** — why $8\pi G/c^2$ couples to $\rho$ (P6's
   exchange gives the structure; the constant is anchored, not derived).
5. **Interior behavior** — finite-admissibility cap; what replaces the
   singularity (quarantined as an engineering seam, but a physics
   obligation).
6. **Vector-sector normalization** ($\alpha_W$).
7. **Dark sector** — funneled entirely into Trial D2: equation of state
   and production of the $w\approx 0$ frustration excess (needs a seat
   in the dynamics first, per the P9 fence); plus D-M3, dark sector as a
   derived property of $K_{\text{strain}}$.
8. **Cosmology branch** — the κ-leak's large-scale counterpart;
   expansion-as-creation bookkeeping under P7′ at the limit.
9. **Data program** — α(λ) curve digitization (manual artifacts with
   instructions in `src_exp/dataexp`) — **promoted to top priority by
   E2**: the curves now constrain both $a_{\text{disc}}$ (UFFT squeeze)
   and $\ell^*$ (the α=1/3 reading of the boundary-smoothing bound);
   template reanalysis for non-Yukawa pressure shapes.
10. **Housekeeping** — P8/T4 formal rewrite as theorems; UFFT remaining
    gates (G04 χ scalar safety; G20 Weyl² ghost check if a covariant
    coupling is retained).

**Engineering seams** (quarantined, standing rules in
`ontology_and_mechanism/engineering_seams.md`): P7′ current seam (κ
channel), Casimir/boundary sector, interior cap, substance creation
regime. None may be built into the theory.

***

## Historical appendix — superseded snapshot (Groups 01–96)

*Retained for the record. Its bottleneck framing is obsolete: the parity
gap / Schur structure was explained by cross-Gram invertibility, and the
parent-equation obstruction migrated into the $K_{\text{strain}}$
program above.*

### Abstract (historical)
This document summarizes the current state of the reduced vacuum response theory of gravity. After 96 development iterations, the theory has transitioned from a scalar toy model into a strict multi-sector architecture. The framework definitively rules out unsuppressed scalar radiation and unstructured metric insertions. The parent field equation is currently blocked by a covariant divergence anomaly at the boundary layer, which has been mathematically reduced to a moment-suppression hierarchy. The survival of the theory rests on proving the all-order invertibility of the associated Schur gap matrix system.

### 1. The Multi-Sector Architecture (historical)
The theory relies on a "Count-Once" ontology, strictly segregating the physical payload to avoid double-counting mass or generating non-physical breathing modes. The active sectors are constrained as follows:

* **Scalar / Monopole Sector ($A_{\text{constraint}}$):** Handles static mass response and the Newtonian potential. Sourced entirely by ordinary density $\rho$. Generates the exact areal-flux Schwarzschild exterior:
  $$F_A = 4\pi r^2 A' = \frac{8\pi G}{c^2}M_{\text{enc}} \quad \implies \quad A_{\text{ext}} = 1 - \frac{2GM}{rc^2}$$
* **Tensor / Quadrupole Sector ($h_{ij}^{TT}$):** Handles long-range gravitational radiation. Radiative scalar components ($A_{\text{rad}}$) are suppressed by vacuum absorption.
* **Vector / Current Sector ($W_i$):** Handles frame dragging. Sourced by the transverse matter current $j_T$ via the vacuum continuity identity:
  $$\nabla \times (\nabla \times W) = -\frac{\alpha_W}{2K_c}j_T$$
* **Trace / Interior Sector ($\kappa, \zeta$):** Handles non-inertial trace and volume relaxation. To prevent double-counting, any residual $\zeta$ or $\kappa$ trace must be strictly killed or demoted to non-metric bookkeeping (the *Residual-Kill* convention). *(Superseded: under P7′ the κ trace is now a predicted, limit-suppressed channel — see §4 above.)*

### 2. The Parent Equation Obstruction (historical)
The assembly of the unified parent field equation is formally blocked. Pure geometry and conservation identities cannot automatically erase residual scalar traces, and "repair currents" have been rejected as unphysical.

The core obstruction is the **Covariant Divergence Identity**. To achieve covariant conservation, the bulk covariant lift and boundary transition layer must exactly cancel:
$$D_{\text{lift}} + D_{\text{boundary}} = 0$$

Expanded to its physical components, this requires the following target to evaluate to zero:
$$L_{\text{bulk}} + L_{\text{gauge}} + L_{\text{boundary}} + D_{\text{jump}} + D_{\text{layer}} + D_{\text{tail}} = 0$$

Currently, the matching theorem yields a non-zero physical remainder, $\rho$. If $\rho$ carries any physical payload (source, trace, mass), covariant conservation fails.

### 3. The Boundary Layer Moment Hierarchy (historical)
To neutralize the boundary layer remainder ($\rho$) without utilizing arbitrary "repair" mathematics, the exactness operator must suppress local payload moments.

A concrete weighted exactness geometry derived from measure-gradient orthogonality requires a specific skew ($c = \frac{3\ell}{2R}$). However, linear skew fails to suppress quadratic payloads. The math structurally forces a richer finite hierarchy of shape profiles.

The minimal working profile (the $N=2$ case) is the unique, zero-action even quartic:
$$P(y) = 1 - 12y^2 + 51y^4$$
This profile successfully kills the first block of local payload moments ($M_2, M_4$).

### 4. The Schur Gap Bottleneck (historical — dissolved)
The moment-suppression hierarchy generalizes to a Beta-function linear system for any degree $N$:
$$A_N a = b_N$$
For the hierarchy to hold at all orders (neutralizing $\rho$ universally), the determinant of the generator matrix must never vanish: $\det(A_N) \neq 0$.

Raw determinant positivity fails at $N=11$. However, the system survives via a **parity-split Schur gap structure**. The matrix is invertible if the Schur gap remains strictly positive. The final mathematical bottleneck to unlock the parent field equation was framed as the **All-Order Parity Gap Theorem**.

*Resolution:* the projection-origin probe identified $A_N$ as a
**cross-Gram** matrix between two admissibility bases; invertibility
follows from the regularity-admissibility ladder without any positivity
requirement, and the sign failure at $N=11$ is exactly what a cross-Gram
(as opposed to a Gram) is allowed to do. The bottleneck was an artifact
of asking a Gram-shaped question of a cross-Gram object.
