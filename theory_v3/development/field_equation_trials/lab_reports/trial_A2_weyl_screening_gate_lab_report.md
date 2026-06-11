# Lab Report: Trial A2 Weyl-Screening Gate (G26) vs Minimal Tidal Vacuum Nucleation

## Experiment

**Script:** `vacuum_forge/src/field_equation_trials/003_trial_A_ufft_gates/trial_A2_weyl_screening_gate.py`
**Experiment type:** Gate confrontation / structural kill test (armchair; no external data)
**Gate:** G26 (solar-system Weyl screening)
**Trial:** A (UFFT), tidal-nucleation sector
**Status:** VERDICT REACHED -- minimal TVN sector KILLED for the dark-sector role
**Run environment:** `cd vacuum_forge/src; PYTHONPATH=. ; python field_equation_trials/003_trial_A_ufft_gates/trial_A2_weyl_screening_gate.py`
**Run date:** 2026-06-11

## Purpose

UFFT's Tidal Vacuum Nucleation (TVN) sector proposes that tidal curvature
lowers the cost of pseudo-2D vacuum relaxation:

$$\alpha_{\rm eff}=\alpha_0-\kappa\,E_{ij}E^{ij}\quad\text{(Newtonian)},
\qquad
\alpha_{\rm eff}=\alpha_0-\kappa_W C^2\quad\text{(covariant)},$$

with nucleation when $\alpha_{\rm eff}<\alpha_c$, i.e. when the invariant
exceeds a threshold $I_c$. The intended phenomenology is dark-matter-like
vacuum bridges between galaxy pairs (the relaxed region's
$\Delta(\rho+3P)=-2\,\Delta\rho>0$ acts as a positive source).

Gate G26 asks whether this can avoid triggering in the solar system. The
UFFT memo itself flags the need for "screening, thresholds, or scale
dependence" (danger zone). This experiment tests whether the minimal
threshold form can have it both ways.

## Method

Pure computation, no data files. Astronomical inputs (G, M_sun, AU, kpc)
are order-of-magnitude stage props, not precision data.

1. Derive the point-mass tidal invariant symbolically (sympy Hessian).
2. Reuse the charter's midpoint invariant for a mass pair
   ($1536\,G^2M^2/d^6$, archived witness, dependency-checked).
3. Compute the curvature hierarchy between solar-system and
   galactic-bridge environments.
4. State the monotone-threshold (up-set) theorem.
5. Check the relaxation-amplitude profile against the dark-matter
   spatial requirement.

## Results

**Point-mass invariant (derived, trace-free verified):**

$$E_{ij}E^{ij}=\frac{6\,G^2M^2}{r^6}$$

(eigenvalues $(-2,1,1)\,GM/r^3$; the covariant counterpart is Schwarzschild's
$C^2=48\,G^2M^2/(c^4r^6)$ -- same $r^{-6}$ profile).

**Hierarchy witness (2 x $10^{12}M_\odot$ galaxies at 50 kpc vs the Sun):**

```text
I(Sun, 1 AU)       = 9.43e-27 s^-4
I(Sun, Saturn)     = 1.21e-32 s^-4
I(bridge midpoint) = 2.01e-60 s^-4

I_1AU / I_bridge   = 4.7e+33      (~34 orders of magnitude)
equal-invariant radius around the Sun: 6.1e16 m = 4.1e5 AU = 1.98 pc
```

**Up-set theorem:** $\alpha_{\rm eff}(I)$ is strictly decreasing, so the
nucleation set $\{I>I_c\}$ is an up-set in the invariant: if any
galactic-bridge midpoint nucleates, every region of higher invariant
nucleates -- which includes the entire planetary system, Kuiper belt and
Oort cloud (everything within ~2 pc of the Sun), and a comparable bubble
around every star in the galaxy.

**Profile inversion:** in the minimal quartic the relaxation amplitude
grows with the invariant ($\chi_\ast\sim\sqrt{\alpha_{\rm excess}/\lambda}$,
verified by sympy limit; the memo's $\chi\in[0,1]$ is an unenforced intent,
its own danger zone 2). Growing or clamped, the induced source is largest
(or saturated) in high-curvature regions:

```text
predicted extra source:        max near stars,  min at halo outskirts
required by rotation curves:   min near stars,  dominant at outskirts
```

The spatial profile is inverted relative to the dark-matter role, for
every value of $\kappa_W$.

## Verdict

```text
Minimal TVN sector: KILLED (FAILED_BY_WITNESS) for the dark-sector role.
The kill is structural and parameter-free:
  (1) up-set theorem + 34-order hierarchy witness;
  (2) profile inversion.
```

Survival routes recorded as obligations (burden on UFFT):

- **S1 Trigger inversion:** relaxation favored by LOW curvature; must then
  explain why laboratory confinement still triggers relaxation while
  stellar tides do not.
- **S2 Derived screening:** replace the local curvature threshold
  (environment-dependent $\alpha_0$, gradient/nonlocal terms).
- **S3 Retreat:** drop the dark-sector claim; keep the boundary/Casimir
  sector ($\gamma/a^2$ coupling, independent -- NOT killed here) and the
  bulk-frustration $\to\Lambda$ sector.

## Scope and threats to validity

1. The kill targets the **minimal threshold form** stated in the memo
   (sections 15-17). It does not touch the Casimir/boundary sector, the
   bulk-$\Lambda$ sector, or any future screened/inverted variant.
2. Astronomical inputs are order-of-magnitude; the conclusion survives any
   plausible refinement because the margin is ~34 orders and the structural
   arguments (up-set, profile sign) carry no parameters at all.
3. The Newtonian invariant is used as the scaling proxy for $C^2$; for the
   exterior environments compared here (vacuum regions around point-like
   masses) the two have identical $r^{-6}$ structure.
4. Hysteresis/memory (memo section 19) does not rescue the minimal form:
   memory retains nucleated regions, and the up-set theorem says the
   solar-system region nucleates first and strongest.

## Relation to the trial program

- First **sector kill** inside a trial (Trial C1's was a mechanism
  demotion). The gate stack is functioning as designed: G26 was scheduled
  as a cheap armchair gate precisely because the memo flagged the screening
  problem, and it produced a verdict in one script.
- Trial A continues with the surviving sectors. Live gates: G25
  (quantitative, pending curve digitization + Layer-2 conversion), G04
  (chi scalar safety), G02 (flat stability), G20 (Weyl-squared ghost check,
  now relevant only if the covariant coupling is retained for a revived
  tidal sector), G23/G24.
- The UFFT memo's own "danger zones" list anticipated this: the experiment
  converts danger zone 3 (solar-system constraints) from a worry into a
  theorem with witnesses.

## Next steps

1. Trial A3: chi scalar-radiation safety (G04) -- does the mass gap from
   $\alpha_0>0$ keep the chi sector out of the long-range scalar channel?
2. Trial A4: Weyl-squared ghost check (G20) if the covariant coupling is
   retained for any revived tidal sector.
3. Layer-2 forge derivation (Yukawa plane-pressure conversion) feeding the
   quantitative G25 confrontation for the surviving Casimir sector.
