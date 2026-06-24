# Lab Report: Exp01 Short-Range Gravity Anchors vs UFFT Crossover

## Experiment

**Script:** `src_exp/dataexp/experiments/exp01_short_range_anchors.py`
**Experiment type:** Data confrontation (Layer 3, data gate protocol)
**Gate:** G25 (short-range gravity at 10-100 microns)
**Trial:** A (UFFT), opening data gate
**Status:** Curve-level confrontation; Lee 2020 and Tan 2020 curves wired in
**Run environment:** `cd src_exp; PYTHONPATH=. python dataexp/experiments/exp01_short_range_anchors.py`
**Dataset:** `dataexp/datasets/short_range_gravity.py`, version v1
**Run date:** 2026-06-14

## Experimentalist-Facing Summary

This run evaluates the Lee and Tan short-range gravity exclusion curves at a
nonstandard but physically motivated Yukawa coupling, $\alpha=1/3$. That
number is not chosen for convenience: in the healthy local $R+aR^2$
extension of GR, equivalently the scalaron sector of $f(R)$ gravity, the
Newtonian potential acquires a scalar Yukawa correction with fixed relative
strength $\alpha=1/3$ and range $\lambda=\sqrt{6a}$. Reading the exclusion
curve on this slice directly bounds the scalaron range.

From the validated Lee 2020 supplemental table, $\alpha=1/3$ is excluded for
$\lambda\ge54.03\,\mu$m; the independent vector extraction gives
$54.05\,\mu$m. From the Tan 2020 author-provided table, the same slice crosses
at $57.29\,\mu$m. Lee is currently the binding dataset on this scalaron-coupling
readout.

Separately, the UFFT/Casimir-vacuum crossover scale computed from the ideal
Casimir energy density equals the dark-energy density at
$a_\Lambda=29.9\,\mu$m. That scale lies below the current
gravitational-strength benchmark frontier ($|\alpha|=1$ at $38.6\,\mu$m) and
below the $\alpha=1/3$ scalaron frontier ($54.03\,\mu$m). A next factor-of-two
improvement in reach would therefore begin testing a model-motivated range,
not just extending a generic exclusion plot.

Short external version: the Lee and Tan curves imply scalaron-coupling bounds
near $\lambda<54$-$57\,\mu$m, while an independent vacuum-sector scale points
to $\sim30\,\mu$m as the next interesting target.

## Purpose

First confrontation of a trial candidate with published short-range gravity
data under the data gate protocol
(`theory_v3/development/field_equation_trials/01_data_gate_protocol.md`).

Two questions:

1. Does the dataexp pipeline run end to end with cached artifacts,
   provenance, loader validation, and no constraint value typed outside the
   dataset module?
2. Where does UFFT's predicted crossover scale sit relative to the validated
   short-range-gravity Yukawa exclusion curves?
3. What do the same data imply on the $\alpha=1/3$ Yukawa slice motivated by
   the scalaron sector of $R+aR^2$ gravity?

The UFFT crossover is the separation at which ideal-Casimir energy density
equals the dark-energy density:

$$a_\Lambda=\left(\frac{\pi^2\hbar c}{720\,\rho_\Lambda}\right)^{1/4}.$$

The UFFT memo proposes this as the scale where laboratory confinement begins
to probe the vacuum sector responsible for cosmic acceleration.

## Data

Yukawa parameterization:

$$V(r)=-\frac{Gm_1m_2}{r}\left(1+\alpha\,e^{-r/\lambda}\right).$$

Verified scalar anchors:

| anchor | result | confidence | status |
|---|---|---|---|
| Lee et al. 2020 [Lee et al., 2020], PRL 124, 101101 | $\|\alpha\|=1$ excluded for $\lambda\ge38.6\,\mu$m; separations tested 52 $\mu$m - 3.0 mm | 95% CL | VERIFIED_FROM_ABSTRACT |
| Tan et al. 2020 [Tan et al., 2020], PRL 124, 051301 | $\|\alpha\|\le1$ holds down to $\lambda=48\,\mu$m | 95% CL | VERIFIED_FROM_ABSTRACT |
| Kapner et al. 2007, PRL 98, 021101 | $\|\alpha\|=1$ excluded for $\lambda\ge56\,\mu$m | 95% CL | SUPERSEDED by Lee 2020 |

Validated curve artifacts:

| curve | source artifact | points | validation |
|---|---|---:|---|
| Lee 2020 | `lee2020_chi_squared_vs_lambda.csv` from validated `suppMaterial1.pdf` text extraction | 66 | $\|\alpha\|=1$ crossing 38.63 $\mu$m; 0.08% from abstract anchor |
| Tan 2020 | `tan2020_alpha_lambda_95cl.txt` from author-provided `PRL2020-AlphaLambda.txt` | 25 | $\|\alpha\|=1$ crossing 47.74 $\mu$m; 0.55% from abstract anchor |

The $\alpha=1/3$ readout is reported because it is the fixed scalar Yukawa
coupling of the ghost-safe $R+aR^2$ sector. It gives an experimentalist-facing
translation from each exclusion curve into a scalaron range bound.

Artifact cache status at run time:

```text
OK  remote  lee2020_abs.html
OK  remote  kapner2007_abs.html
OK  manual  lee2020_chi_squared_vs_lambda.csv
OK  manual  tan2020_alpha_lambda_95cl.txt
```

Physical inputs to the crossover formula: 
$\hbar=1.054571817\times10^{-34}$ J s,
$c=2.99792458\times10^8$ m/s, 
$\rho_\Lambda=5.4\times10^{-10}$ J/m$^3$.

## Results

Experimental readout:

| slice | Lee 2020 crossing | Tan 2020 crossing | binding dataset |
|---|---:|---:|---|
| $|\alpha|=1$ benchmark | 38.63 $\mu$m | 47.74 $\mu$m | Lee 2020 |
| $\alpha=1/3$ scalaron coupling | 54.03 $\mu$m | 57.29 $\mu$m | Lee 2020 |

Validated curve readouts:

```text
Lee 2020:
  |alpha|=1 crossing: 38.63 um
  alpha=1/3 crossing: 54.03 um

Tan 2020:
  |alpha|=1 crossing: 47.74 um
  alpha=1/3 crossing: 57.29 um

Binding curve-derived crossings:
  |alpha|=1: lambda >= 38.63 um (Lee 2020)
  alpha=1/3: lambda >= 54.03 um (Lee 2020)
```

UFFT positioning:

```text
best live |alpha| = 1 exclusion crossing : 38.6 um
UFFT crossover a_Lambda                  : 29.9 um
UFFT crossover below the exclusion crossing: TRUE
```

The candidate's predicted scale sits in the unexcluded window below the
gravitational-strength crossing, about a factor of 1.29 below the Lee 2020
frontier.

## Interpretation

1. **The most portable result is the $\alpha=1/3$ slice.** Lee 2020 implies
   $\lambda<54.03\,\mu$m for a scalaron-coupling Yukawa correction, while
   Tan 2020 gives the independent check $\lambda<57.29\,\mu$m. This is the
   part of the analysis most likely to be useful to Lee/Tan, because it reads
   their curves at a physically motivated coupling rather than only at the
   conventional $|\alpha|=1$ benchmark.
2. **Gate G25 is not an instant kill for UFFT.** Had $a_\Lambda$ landed above
   the Lee 2020 crossing, any gravitational-strength boundary-relaxation
   force at the crossover would already be excluded. Instead the scale lands
   below the current $|\alpha|=1$ exclusion crossing.
3. **The next reach target is close.** The $\sim30\,\mu$m crossover sits below
   present reach, but not far below it: 38.63/29.9 = 1.29 on the
   gravitational-strength benchmark, and 54.03/29.9 = 1.81 on the
   scalaron-coupling slice.
4. **Lee 2020 is the binding curve in the window of interest.** Tan 2020 is an
   independent check and is weaker at both $|\alpha|=1$ and $\alpha=1/3$.
5. **The confrontation is now curve-level, not anchor-only.** The remaining
   missing step is not data acquisition; it is the Layer-2 forge conversion
   from the UFFT pressure spectrum into effective Yukawa or explicitly
   non-Yukawa observables.

## Negative-Space Record

Per protocol rule D6:

- These curves do NOT exclude $|\alpha|>1$ below $\sim38.6\,\mu$m.
- These curves do NOT directly constrain non-Yukawa-shaped signatures
  (the UFFT offset term and $a^{-2}$ term are not Yukawa-shaped); the
  Layer-2 conversion must be done before the bounds apply at all.
- The torsion-balance experiments use shaped test masses, not parallel
  plates; geometry-dependent couplings are constrained differently than
  universal Yukawa couplings.

## Threats To Validity

1. The Lee 2020 supplemental table was extracted from a PDF text/copy-paste
   workflow and validated by Alan, not received as a clean official CSV.
   It is strongly cross-validated by the prior vector-path extraction:
   38.63/54.03 $\mu$m here versus 38.61/54.05 $\mu$m from the vector path.
2. The Tan 2020 table is author-provided, but the loader validation is still
   anchor-based. The $|\alpha|=1$ crossing lands within 0.55% of the 48 $\mu$m
   abstract anchor.
3. $\rho_\Lambda=5.4\times10^{-10}$ J/m$^3$ is the memo's value; the
   crossover scales as $\rho_\Lambda^{-1/4}$, so even a factor-2 revision
   moves $a_\Lambda$ only by about 19%.
4. $a_\Lambda$ is a crossover scale, not a sharp UFFT prediction; the actual
   transition separations depend on trial parameters and may sit elsewhere.

## Conclusions

```text
pipeline: end-to-end PASS
curve validation: PASS for Lee 2020 and Tan 2020
binding |alpha|=1 crossing: 38.63 um (Lee 2020)
binding alpha=1/3 crossing: 54.03 um (Lee 2020)
G25 confrontation: UFFT NOT killed at crossover scale
trial A status: OPEN; Layer-2 pressure-to-Yukawa conversion pending
```

## Next Steps

1. Forge script (Layer 2): derive the plane-geometry pressure of a Yukawa
   interaction symbolically and map UFFT's $\Delta P(a)$ terms onto
   $(\alpha,\lambda)$ space, flagging non-Yukawa components explicitly.
2. Re-run the confrontation as a constraint-surface computation over UFFT
   parameters; record excluded and surviving regions.
3. Preserve `src_exp/external_data/` as the received-source/provenance folder
   for the Lee and Tan files.
