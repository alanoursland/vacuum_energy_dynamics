# Finite-Strain Admissibility Probe

## Claim

An exterior-preserving interior cap is not licensed unless the vacuum ontology
derives the finite-strain bound or admissibility scale that sets the cap.

## Scope

This probe follows the exterior matching lemma. It assumes the exterior can be
held fixed at the contract level and asks whether that also supplies an
interior cap. It does not.

## Symbolic Probe

Use compactness:

```text
C = 2GM / (c^2 R_cap)
```

and a finite-strain placeholder:

```text
K_int = 1 / (1 - C)
```

If a bound is imposed:

```text
K_int = kappa_max
```

then:

```text
R_cap = 2GM kappa_max / (c^2 (kappa_max - 1))
```

The cap radius depends on `kappa_max`. Unless `kappa_max` is derived, the cap
scale is imported.

If a placeholder ontological bound is supplied:

```text
K_int = K_ved
R_cap = 2GM K_ved / (c^2 (K_ved - 1))
```

the missing object is now `K_ved`.

## Route Classification

```text
unbounded GR-like interior:
    not a cap route

imposed strain bound:
    rejected as imported admissibility scale

derived microphysical/ontological bound:
    possible but deferred until the ontology derives the bound

observed compactness backsolve:
    rejected as observed-value insertion
```

## Current Classification

The VacuumForge probe records:

```text
derivation: finite_strain_admissibility_probe_027
obligation satisfied: finite_strain_admissibility_probe_required_026
new obligation: global_boundary_topology_selector_rules_required_027
```

Current conclusion:

```text
No finite-strain interior cap is licensed.
```

The exterior matching lemma protects the exterior only. It does not derive the
interior admissibility bound, cap scale, or nonsingularity rule.
