# Interior Cap

This folder is for strong-field and compact-interior admissibility work. The
closed weak-field, exterior, and radiative sectors can remain GR while the
vacuum-sector ontology still owes an interior completion rule.

This folder is not a shortcut for:

```text
changing the tested exterior metric without residual gates
inserting a cap radius by hand
claiming nonsingularity before matching and scale derivation
reusing dark-sector or Lambda bookkeeping as an interior rule
```

## Current Result

The first contract is recorded in:

```text
interior_cap_contract.md
interior_cap_admissibility_contract_vacuumforge.md
exterior_matching_lemma.md
exterior_matching_lemma_vacuumforge.md
finite_strain_admissibility_probe.md
finite_strain_admissibility_probe_vacuumforge.md
```

Current conclusion:

```text
UPDATED (2026-07-03, derivation 055): the admissibility scale is now
DERIVED at mean-field from P10's compression limits -- the bound the
finite-strain probe (027) said was "possible but absent" was the
coordination floor all along. An interior hinge carries >= 3 cells, so
the near-regular deficit is capped at delta_max = 2 pi - 3 arccos(1/3)
= 2.590 rad, giving R_max = 2 c_e delta_max/a^2 = 51.67/a^2 and a
capped core at r_cap = 0.406 (r_s a^2)^(1/3) -- the Planck-star
scaling with a derived coefficient, exact in arccos(1/3). The cap sits
~26 orders inside a stellar-mass horizon: exteriors exactly GR, NO
echoes predicted at any astrophysical mass (register A4's caveat
resolves to a null), Planck-mass endpoint marker at ~0.1 M_P.
See interior_cap_scale_vacuumforge.md.

STILL OPEN (cap_junction_dynamics_055): the capped interior METRIC,
junction/source bookkeeping, collapse dynamics, and the fence's
energetics (the near-regular bound vs the degenerate-cell trade).
The contract below remains the gate for all of it.
```

Imported cutoff radii and untracked exterior deviations are rejected.
The exterior matching lemma licenses only fixed-charge exterior preservation:
if the exterior equations and charges are unchanged, the exterior proxy is
unchanged at this contract level. Charge shifts, Lambda shifts, and residual
leaks reroute to their own ledgers.
The finite-strain admissibility probe shows that exterior preservation does not
derive an interior cap scale. Imposed strain bounds and observed compactness
backsolves fail; a derived microphysical or ontological bound remains possible
but absent.

## Required Contract

Every interior-cap branch must state:

```text
what exterior data are preserved;
what matching or junction rule is used;
what interior strain quantity is bounded;
what finite-strain admissibility rule supplies the bound;
what scale or compactness threshold is derived;
what observable face remains after exterior preservation;
what failure route kills or reroutes the branch.
```

## Next Work

The next obligation is:

```text
global_boundary_topology_selector_rules_required_027
```

That rule set should consolidate the missing-scale lesson across Lambda,
interiors, topology, boundary data, and admissibility selectors.
