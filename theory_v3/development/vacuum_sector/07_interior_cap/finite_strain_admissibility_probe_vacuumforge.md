# VacuumForge Finite-Strain Admissibility Probe

## Purpose

This report tests whether an interior cap scale is derived by a finite-strain
admissibility rule or imported as a cutoff. It does not prove a nonsingular
interior.

This report depends on:

```text
exterior_matching_lemma_026
```

It satisfies:

```text
finite_strain_admissibility_probe_required_026
```

## Symbolic Checks

Compactness:

```text
C = 2*G*M/(R_cap*c**2)
```

Finite-strain proxy:

```text
K_int = 1/(-2*G*M/(R_cap*c**2) + 1)
```

Cap radius from imposed `kappa_max`:

```text
R_cap = 2*G*M*kappa_max/(c**2*(kappa_max - 1))
```

Cap radius from a placeholder derived bound `K_ved`:

```text
R_cap = 2*G*K_ved*M/(c**2*(K_ved - 1))
```

Cap radius from observed compactness:

```text
R_cap = 2*G*M/(C_target*c**2)
```

The algebra shows where the missing object lives: a cap scale follows only
after a finite-strain bound is supplied. If that bound is imposed or inferred
from an observed target, the route is not a derivation.

## Finite-Strain Route Ledger

| route | route | strain quantity | bound route | cap scale route | observable face | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| unbounded_gr_interior | retain exterior GR and allow interior strain proxy to diverge | K_int = 1/(1 - C) | no finite bound | no cap scale | ordinary strong-interior incompletion | not a cap route | do not claim finite interior from exterior closure alone |
| imposed_strain_bound | set K_int <= kappa_max | K_int = 1/(1 - C) | kappa_max imposed | R_cap solved from imposed kappa_max | compactness/redshift cap | rejected as imported admissibility scale | derive kappa_max before use |
| derived_microphysical_bound | derive K_int <= K_ved from vacuum ontology | chosen finite-strain invariant | K_ved must be derived before observation | R_cap follows only after K_ved is derived | maximum compactness or redshift with exterior preserved | candidate only; missing derivation of K_ved | derive or reject finite-strain bound from ontology |
| observed_compactness_backsolve | infer cap scale from desired observed compactness | chosen after target | observed compactness supplies bound | R_cap from target compactness | fit to compact-object target | rejected as observed-value insertion | do not use as derivation |

## Readiness

| route | strain quantity | derives bound | derives scale | preserves exterior | live cap route |
| --- | --- | --- | --- | --- | --- |
| unbounded_gr_interior | True | False | False | True | False |
| imposed_strain_bound | True | False | False | True | False |
| derived_microphysical_bound | False | False | False | True | False |
| observed_compactness_backsolve | False | False | False | True | False |

## Current Conclusion

No finite-strain interior cap is licensed. The exterior matching lemma protects
the exterior only. It does not derive the interior admissibility bound,
cap scale, or nonsingularity rule.

The only possible live route is a future derived microphysical or ontological
bound, and that bound is not supplied here.

## Classification

```text
result type: finite-strain admissibility probe
scope: interior cap scale after exterior preservation
conclusion: no cap scale is derived; imposed cutoffs and observed-target backsolves fail
non-conclusion: no global no-go theorem against finite interiors
```

The next technical target is:

```text
global_boundary_topology_selector_rules_required_027
```
