# Lab Report: Trial D1 Depletion Budget vs the Dark Matter Requirement

## Experiment

**Script:** `vacuum_forge/src/field_equation_trials/004_trial_D_standing_frustration/trial_D1_depletion_budget.py`
**Experiment type:** Entry-gate ledger / kill test (armchair, parameter-free)
**Gate:** D-G1 (abundance) for the depletion-history mechanism
**Trial:** D (standing frustration ledger), mechanisms D-M1/D-M2 in P6-exchange form
**Status:** VERDICT REACHED -- mechanism KILLED
**Run environment:** `cd vacuum_forge/src; PYTHONPATH=. ; python field_equation_trials/004_trial_D_standing_frustration/trial_D1_depletion_budget.py`
**Run date:** 2026-06-11

## Purpose

Test the depletion-history-halo mechanism: vacuum destroyed by P6 exchange
during a galaxy's assembly leaves a $\Delta\rho<0$ residue gravitating
positively ($-2\Delta\rho$, the dark-bridge sign result). Does the
integrated budget land near the dark matter requirement (~5x baryonic)?

The budget is bound to kinetic energy by P6's own statement ("the energy
of the vacuum exchanged equals the kinetic energy change"), so the
calculation is parameter-free up to the sign-fork factor $\eta\in\{1,2\}$.

## Results

**Symbolic ratio (derived):**

$$\frac{E_{\rm budget}}{E_{\rm required}}
=\frac{\eta\,\tfrac12 M_b v^2}{\tfrac52 M_b c^2}
=\frac{\eta\,v^2}{5c^2}$$

(the 5/2 already includes the factor-2 dark-bridge generosity).

**Magnitudes ($\eta=2$, most generous):**

```text
dwarf galaxy  (v ~ 50 km/s):   1.1e-08   (shortfall 9.0e7 x)
Milky Way     (v ~ 200 km/s):  1.8e-07   (shortfall 5.6e6 x)
rich cluster  (v ~ 1000 km/s): 4.5e-06   (shortfall 2.2e5 x)
```

**Channel inventory at maximum generosity** (per unit baryonic rest
energy): virial assembly ~4e-7; cumulative SN kinetic ~1e-5; SMBH
accretion ~1e-4; compact-object binding (the most generous channel,
~0.1c^2 on ~1% of baryons) ~1e-3. Sum <= 1.1e-3 vs required 2.5:
**shortfall >= 2000x even with every channel maximized.**

**Shape failure:** the predicted "dark matter fraction" scales as
$(v/c)^2$; the observed ratio is ~5 and roughly flat from dwarfs to
clusters. Wrong magnitude and wrong shape.

**Counter-flow:** photons climbing out of wells CREATE vacuum under P6
(T1's ascent bookkeeping), partially refilling the depletion. The kill
margins above are lower bounds.

## Verdict

```text
Depletion-history halos (P6-exchange form of D-M1/D-M2):
KILLED at entry gate D-G1, parameter-free.
No parameter rescues it: scaling eta up by ~1e6 would violate P6's
exchange-equals-KE statement by definition.
```

This also retires, in its energy-bookkeeping form, the old notes'
assignment "dark matter = passive vacuum depletion at galactic scales"
(`notes/spatial_expansion.md` ledger table): depletion is real under P6
dynamics but ~six orders of magnitude too small to be the dark sector.

## Survivors (unaffected)

- **The excess/EoS branch** (Trial D's revised entry gate): a $w\approx0$
  transportable excess (gapped excitations / defect gas) whose abundance
  is set by PRODUCTION physics, not by P6 kinetic bookkeeping. This is
  now Trial D's only live dark-sector route, alongside
- **D-M3 (K_strain route)**: dark sector as a derived property of the
  strain functional.

## Threats to validity

1. Astronomical inputs are order-of-magnitude; the kill margin (>= 3
   orders at maximum generosity) dwarfs any plausible refinement.
2. The channel inventory could miss an energy reservoir -- but any
   rescue channel must deliver ~2.5 M_b c^2 of KINETIC-class energy
   through P6 exchange, i.e. bulk motions at ~0.7c during assembly,
   which is excluded by observed structure formation.
3. If P6's exchange were re-scoped to couple to something other than
   kinetic energy changes, the calculation would not apply -- but that
   would be a different postulate, and the current one is load-bearing
   for T1/T2.

## Relation to the trial program

Second sector kill (after A2) and third kill overall. The trials
scoreboard: B1 structural upgrade, C1 mechanism demotion, A2 sector
kill, C2 sign resolution + P9, C3 placement resolution + P7', D1
mechanism kill. The dark-sector question now funnels entirely into the
excess/EoS branch and the strain functional -- the same K_strain center
everything else points at.

## Next steps

1. Trial D2: equation of state and production of the frustration excess
   (the revised D-G1) -- requires giving the excess a seat in the
   dynamics first (P9 fence).
2. G03 radiative positivity (the remaining half of the sector-indefinite
   signature).
3. Layer-2 Yukawa conversion for the Casimir-sector data gate.
