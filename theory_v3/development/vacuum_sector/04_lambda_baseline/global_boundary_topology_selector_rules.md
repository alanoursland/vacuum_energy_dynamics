# Global/Boundary/Topology Selector Rules

## Claim

Global, boundary, topology, and admissibility data can restrict sectors or
allowed classes, but they do not set dimensionful local values unless the
missing scale is also derived.

## Scope

This rule applies across:

```text
Lambda baseline selectors
topology and global constraints
boundary/admissibility selectors
measure identities
finite-strain interior caps
```

It does not kill any of those selector families. It blocks only the move from
sector selection to value selection without a derived scale.

## Symbolic Checks

Two-dimensional topology relation:

```text
integral R dA = 4*pi*chi
R = 4*pi*chi / A
```

The value of `R` needs the area `A`.

Four-dimensional constant-curvature Gauss-Bonnet proxy:

```text
integral E dV = 32*pi^2 chi
E = (8/3) Lambda^2
Lambda^2 = 12*pi^2 chi / V
```

The value of `Lambda^2` needs the volume `V`, plus a sign/branch selector.

Interior finite-strain caps obey the same pattern:

```text
R_cap = 2GM K_ved / (c^2 (K_ved - 1))
```

The cap scale needs the admissibility bound `K_ved`.

## Rule Ledger

```text
topology only:
    constrains sectors, does not derive dimensionful values

topology plus measure:
    candidate only if the measure/volume is derived

boundary/admissibility scale:
    candidate only if the boundary or admissibility scale is selected by the
    ontology

observed-value backsolve:
    rejected as value insertion
```

## Current Classification

The VacuumForge consolidation records:

```text
derivation: global_boundary_topology_selector_rules_028
obligation satisfied: global_boundary_topology_selector_rules_required_027
new obligation: vacuum_sector_program_checkpoint_required_028
```

Current conclusion:

```text
Sector selection is not value selection without a derived scale.
```

The next useful step is a program checkpoint before opening new mechanism
branches.
