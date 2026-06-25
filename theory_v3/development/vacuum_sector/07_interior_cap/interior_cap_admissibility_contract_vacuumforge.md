# VacuumForge Interior-Cap Admissibility Contract

## Purpose

This report opens the strong-field/interior admissibility workstream. It does
not prove a finite interior, a nonsingular compact object, or a new equation of
state.

This report depends on:

```text
substance_frame_bounds_sieve_024
```

It satisfies:

```text
interior_cap_admissibility_contract_required_024
```

## Symbolic Checks

Compactness proxy:

```text
C = 2*G*M/(R_cap*c**2)
1 - C = -2*G*M/(R_cap*c**2) + 1
R_cap at C = 1 -> 2*G*M/c**2
```

Finite-strain placeholder:

```text
K_int = 1/(-2*G*M/(R_cap*c**2) + 1)
R_cap from K_int = kappa_max -> 2*G*M*kappa_max/(c**2*(kappa_max - 1))
```

Exterior potential proxy:

```text
Phi_ext = -G*M/r
d(Phi_ext)/dR_cap = 0
```

The check is intentionally narrow. The exterior proxy depends on exterior mass
and radius, not the cap radius, when exterior charges are preserved. A finite
strain cap still imports a bound or admissibility scale unless that scale is
derived.

## Interior Route Ledger

| route | route | exterior condition | interior rule | scale route | observable face | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exterior_preserving_interior_rule | modify only interior admissibility while preserving exterior GR matching | same exterior mass M and Lambda; no exterior residual | finite-strain cap rule not yet supplied | cap scale not yet derived | compactness/redshift/interior-EOS face with no exterior deviation | contracted candidate only | prove exterior matching lemma before finite-strain cap claims |
| surface_layer_matching_route | allow a surface layer or transition shell | must satisfy junction bookkeeping and conserve exterior charges | surface stress or transition law not yet supplied | shell/cap radius not derived | surface redshift, merger, echo, or compactness signature | deferred pending matching and source ledger | write junction/source ledger before use |
| imported_cutoff_radius | insert cap radius by hand | may preserve exterior by construction | cutoff imposed, not derived | imported length or compactness threshold | chosen cap phenomenology | rejected as imported scale | derive cap scale from admissibility before use |
| untracked_exterior_deviation | alter interior and let exterior change without residual gates | fails: tested exterior is no longer protected | not enough | not enough | untracked weak-field or radiative deviation | rejected as wrong ledger | return to residual gates before exterior modification |

## Readiness

| route | preserves exterior | matching rule | finite-strain rule | derives scale | live cap route |
| --- | --- | --- | --- | --- | --- |
| exterior_preserving_interior_rule | True | False | False | False | False |
| surface_layer_matching_route | True | False | False | False | False |
| imported_cutoff_radius | True | False | False | False | False |
| untracked_exterior_deviation | False | False | False | False | False |

## Current Conclusion

No interior-cap route is live. Exterior-preserving interior modification is a
candidate contract only. A cap or finite-strain rule needs exterior matching,
junction/source bookkeeping, and a derived admissibility scale before it can be
used.

Imported cutoff radii and untracked exterior deviations are rejected.

## Classification

```text
result type: interior-cap admissibility contract
scope: strong-field interiors with tested exterior sector preserved
conclusion: no finite-strain cap is licensed without matching and scale derivation
non-conclusion: no nonsingularity theorem; no global no-go theorem against interiors
```

The next technical target is:

```text
exterior_matching_lemma_required_025
```
