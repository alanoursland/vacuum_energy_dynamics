# Lab Report: Exp01 Short-Range Gravity Anchors vs UFFT Crossover

## Experiment

**Script:** `src_exp/dataexp/experiments/exp01_short_range_anchors.py`
**Experiment type:** Data confrontation (Layer 3, data gate protocol)
**Gate:** G25 (short-range gravity at 10-100 microns)
**Trial:** A (UFFT), opening data gate
**Status:** Anchor-level confrontation; quantitative constraint surface deferred
**Run environment:** `cd src_exp; PYTHONPATH=. ; python dataexp/experiments/exp01_short_range_anchors.py`
**Dataset:** `dataexp/datasets/short_range_gravity.py`, version v1
**Run date:** 2026-06-11

## Purpose

First confrontation of a trial candidate with published observational data
under the data gate protocol
(`theory_v3/development/field_equation_trials/01_data_gate_protocol.md`).

Two questions:

1. Does the dataexp pipeline (dataset module -> cached artifacts with
   provenance -> loader -> experiment) run end to end, with no constraint
   value typed outside the dataset module?

2. Where does UFFT's predicted crossover scale sit relative to the verified
   short-range-gravity exclusion anchors?

The UFFT crossover is the separation at which ideal-Casimir energy density
equals the dark-energy density:

$$a_\Lambda=\left(\frac{\pi^2\hbar c}{720\,\rho_\Lambda}\right)^{1/4}.$$

The UFFT memo proposes this as the scale where laboratory confinement begins
to probe the vacuum sector responsible for cosmic acceleration; boundary
relaxation effects (the $-V(\chi_\ast)$ offset and $-\gamma\chi_\ast^2/a^2$
terms in the trial-A pressure spectrum) become competitive there.

## Data

Yukawa parameterization used by the experiments:

$$V(r)=-\frac{Gm_1m_2}{r}\left(1+\alpha\,e^{-r/\lambda}\right).$$

Verified scalar anchors (all values live in the dataset module only;
verification = read from the paper's abstract on 2026-06-11):

| anchor | result | confidence | status |
|---|---|---|---|
| Lee et al. 2020, PRL 124, 101101 (arXiv:2002.11761) | $\|\alpha\|=1$ excluded for $\lambda\ge38.6\,\mu$m; separations tested 52 $\mu$m - 3.0 mm | 95% CL | VERIFIED_FROM_ABSTRACT |
| Tan et al. 2020, PRL 124, 051301 (HUST) | $\|\alpha\|\le1$ holds down to $\lambda=48\,\mu$m; strongest bounds 40-350 $\mu$m | 95% CL | VERIFIED_FROM_ABSTRACT (independent group) |
| Kapner et al. 2007, PRL 98, 021101 (hep-ph/0611184) | $\|\alpha\|=1$ excluded for $\lambda\ge56\,\mu$m | 95% CL | SUPERSEDED by Lee 2020 |

Artifact cache status at run time:

```text
OK  remote  lee2020_abs.html       (provenance snapshot, auto-downloaded)
OK  remote  kapner2007_abs.html    (provenance snapshot, auto-downloaded)
--  manual  lee2020_alpha_lambda_95cl.csv   MISSING (digitization declared, not done)
--  manual  tan2020_alpha_lambda_95cl.csv   MISSING (digitization declared, not done)
```

Physical inputs to the crossover formula: $\hbar=1.054571817\times10^{-34}$ J s,
$c=2.99792458\times10^8$ m/s, $\rho_\Lambda=5.4\times10^{-10}$ J/m$^3$
(the UFFT memo's dark-energy density value).

## Results

```text
best live |alpha| = 1 exclusion crossing : 38.6 um   (Lee 2020)
UFFT crossover a_Lambda                  : 29.9 um

UFFT crossover below the exclusion crossing: TRUE
```

The candidate's predicted scale sits in the unexcluded window below the
gravitational-strength crossing, a factor of about 1.3 from the current
experimental frontier.

Independent-group consistency: the two live anchors (Eot-Wash 38.6 $\mu$m,
HUST 48 $\mu$m) agree on the exclusion ordering; the more sensitive
experiment sets the live crossing.

## Interpretation

1. **Gate G25 is not an instant kill for UFFT.** Had $a_\Lambda$ landed above
   38.6 $\mu$m, any gravitational-strength boundary-relaxation force at the
   crossover would already be excluded and Trial A would face an immediate
   quantitative kill. Instead the predicted scale lands in the last
   unexcluded corner of the $|\alpha|\ge1$ parameter space.

2. **This is the correct epistemic position for a falsifiable candidate:**
   alive, cornered, and directly addressable by the next generation of
   short-range experiments, which are pushing into exactly this window.

3. **The confrontation is anchor-level only.** Converting it into a
   constraint surface on UFFT's parameters $(\gamma,\alpha_0,\beta,\lambda)$
   requires both declared follow-ups:
   the digitized $\alpha(\lambda)$ exclusion curves (manual artifacts with
   instructions and sanity anchors in the dataset module), and the Layer-2
   forge derivation converting the UFFT pressure spectrum
   $\Delta P(a)=-V(\chi_\ast,a)-\gamma\chi_\ast^2/a^2-3C/a^4$ into effective
   Yukawa (or explicitly non-Yukawa) language.

## Negative-space record

Per protocol rule D6:

- These anchors do NOT exclude $|\alpha|>1$ below $\sim38.6\,\mu$m.
- These anchors do NOT directly constrain non-Yukawa-shaped signatures
  (the UFFT offset term and $a^{-2}$ term are not Yukawa-shaped); the
  Layer-2 conversion must be done before the bounds apply at all.
- The torsion-balance experiments use shaped test masses, not parallel
  plates; geometry-dependent couplings (the memo's material-sensitive
  $\gamma$ branch) are constrained differently than universal couplings.

## Threats to validity

1. Anchor values are verified from abstracts, not full texts or figures
   (VERIFIED_FROM_ABSTRACT). The 38.6 $\mu$m and 48 $\mu$m crossings are
   stated in the abstracts directly, so risk is low, but full-text
   verification is the declared upgrade path.
2. $\rho_\Lambda=5.4\times10^{-10}$ J/m$^3$ is the memo's value; the
   crossover scales as $\rho_\Lambda^{-1/4}$, so even a factor-2 revision
   moves $a_\Lambda$ only by ~19%. The qualitative conclusion (below the
   crossing) is robust to any plausible $\rho_\Lambda$.
3. $a_\Lambda$ is a crossover scale, not a sharp UFFT prediction; the
   actual transition separations $a_{\rm disc}>a_{\rm co}>a_{\rm sp}$
   depend on $(\gamma,\alpha_0,\beta,\lambda)$ and may sit elsewhere.
   The anchor comparison is a positioning result, not a survival proof.
4. Newer bounds may exist (anchors retrieved 2026-06-11); protocol rule D5
   handles updates through the dataset module only.

## Conclusions

```text
pipeline: end-to-end PASS (dataset -> cache+manifest -> loader -> experiment)
G25 anchor confrontation: UFFT NOT killed; predicted scale in the
  unexcluded window (29.9 um < 38.6 um)
trial A status: OPEN; quantitative constraint surface pending
  (curve digitization + Layer-2 pressure-to-Yukawa conversion)
```

## Next steps

1. Digitize the Lee 2020 and Tan 2020 $\alpha(\lambda)$ 95%-CL curves per
   the dataset module instructions (sanity anchors: curves must pass
   $|\alpha|=1$ at 38.6 $\mu$m and 48 $\mu$m respectively).
2. Forge script (Layer 2): derive the plane-geometry pressure of a Yukawa
   interaction symbolically and the mapping from UFFT's
   $\Delta P(a)$ terms onto $(\alpha,\lambda)$ space, flagging the
   non-Yukawa components explicitly.
3. Re-run the confrontation as a constraint-surface computation over
   $(\gamma,\alpha_0,\beta,\lambda)$; record excluded and surviving regions.
