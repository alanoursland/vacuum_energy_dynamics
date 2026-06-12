# Lab Report: Trial E2 -- The Observable Face of ell*

## Experiment

**Script:** `vacuum_forge/src/field_equation_trials/009_trial_E_boundary_admissibility/trial_E2_ellstar_observable_face.py`
**Experiment type:** Derivation + Layer-3 data confrontation (verified anchors) + channel kill
**Trial:** E (boundary admissibility), continuation of E1
**Status:** VERDICT REACHED -- claim half right, dataset inverted; **GW channel KILLED**, bench-top bound established
**Run environment:** `cd vacuum_forge/src; PYTHONPATH=. ; python field_equation_trials/009_trial_E_boundary_admissibility/trial_E2_ellstar_observable_face.py`
**Run date:** 2026-06-12
**Dependencies verified:** E1 beta-smoothing mechanism.

## Claim under test

Theory owner (after external-AI discussion): *"ell\* is plausibly the most
testable number, more so than the kappa-leak, because its observable face
sits in existing data -- the neutron-star phase-transition edge perturbs
tidal deformability measured in GW inspirals."*

## Results

**T1 (the static face -- exact).** The same $\beta(s'')^2$ term that
smooths boundaries necessarily modifies the static potential. Exact
propagator identity:
$$\frac{1}{k^2+\beta k^4} \;=\; \frac{1}{k^2} - \frac{1}{k^2+1/\beta},$$
position-space Green identity verified for $(1-e^{-r/\ell^*})/r$. So
$$V(r) = -\frac{Gm}{r}\Big[1 - e^{-r/\ell^*}\Big]
\qquad (\text{naive scalar reduction: } \alpha=-1).$$
**Boundary smoothing and a gravitational-strength short-range Yukawa are
one parameter.** You cannot have one without the other. (The degenerate
f(R)-class realization gives $\alpha=+1/3$; the exact $\alpha$ -- even
its sign -- is owed by the covariant parent and is itself a
discriminator.)

**T2 (the existing bound).** The Lee 2020 verified anchor
($|\alpha|=1$ excluded for $\lambda \ge 38.6\,\mu$m) therefore caps,
today, before any parent functional is written:
$$\ell^* < 38.6\,\mu\text{m}\quad(|\alpha|=1),
\qquad \beta < 1.5\times10^{-9}\,\text{m}^2.$$
The $\alpha=1/3$ reading needs the $\alpha(\lambda)$ curve digitization
already registered in `src_exp/dataexp` -- now doubly load-bearing.

**T3 (the GW channel dies by hierarchy).** With $\ell^*$ capped at tens
of microns, smoothing a density discontinuity inside a neutron star
perturbs the tidal deformability by
$$\frac{\delta\Lambda}{\Lambda} \sim \frac{\ell^*}{R_{NS}}\times O(1)
\;\lesssim\; 3\times10^{-9},$$
against GW measurement precision no better than $\sim10^{-1}$:
**shortfall $\ge 3\times10^{7}$ at maximum generosity.** For NS tidal
data to see $\ell^*$ it would need $\ell^*\sim$ meters-to-kilometers,
excluded by bench-top gravity by $\ge 8$ orders. Recorded as
FAILED_BY_WITNESS.

## Verdict

```text
The claim's insight SURVIVES: ell* is data-active today, unlike the
kappa-leak -- it is the program's most immediately testable parameter.
The claim's dataset INVERTS: the active data is Eot-Wash/Casimir-class
bench-top gravity, not gravitational waves. NS tidal channel KILLED.
```

**Convergence recorded:** the testable face of $\ell^*$ lands in the
same micron window as the UFFT squeeze
($29.9\,\mu\text{m} < a_{\text{disc}} < 38.6\,\mu\text{m}$). Two
independent program parameters now funnel into one experimental window;
the $\alpha(\lambda)$ digitization is promoted to the data program's top
priority.

**E1's conclusion sharpened into a two-faced signature:** if
$K_{\text{strain}}$ has $\beta\neq0$, VED predicts a micron-or-smaller
boundary-smoothing scale *and* a bench-top Yukawa deviation at the same
range. If future $|\alpha|\sim O(1)$ exclusions push far below the
parent's natural $\ell^*$, then $\beta=0$ is forced and the
smooth-boundary intuition dies by data.

## Threats to validity

1. The NS response factor and GW precision are order-of-magnitude
   (precision FROM_MEMORY, flagged per protocol); the kill margin
   ($\ge7$ orders) dwarfs both.
2. T2 assumes the deviation couples to ordinary matter at gravitational
   strength -- which T1's derivation gives it; an exotically screened
   realization would need to be exhibited, not presumed.
3. A rescue of the GW channel needs an NS observable with
   $\ell^*$-sensitivity amplified by $\ge10^7$ over tidal deformability;
   none is known.

## Relation to the program

Fourth kill overall (TVN, burden-reduction, depletion-history, now the
NS-tidal channel for $\ell^*$) and the second time a kill protected the
program from spending effort on a channel that arithmetic forecloses.
The trial also produced the program's tightest *prospective* link
between the unwritten parent and running experiments: $\beta$ is bounded
by bench-top data before being defined by theory.

## Next steps

1. $\alpha(\lambda)$ digitization (manual artifacts, instructions in
   `src_exp/dataexp/datasets/short_range_gravity.py`) -- top data
   priority; constrains both $a_{\text{disc}}$ and $\ell^*$.
2. When candidate parents are written: evaluate $\beta$ and its
   $\alpha$ (sign included) first.
3. G20/Ostrogradsky health check for any $\beta\neq0$ candidate.
