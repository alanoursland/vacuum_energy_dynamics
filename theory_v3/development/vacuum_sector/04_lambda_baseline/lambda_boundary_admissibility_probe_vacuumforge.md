# VacuumForge Lambda Boundary/Admissibility Probe

## Purpose

This report tests whether boundary/admissibility data can select a nonzero
`Lambda` baseline without observed-value insertion or local-equation
modification. It does not derive the observed cosmological constant.

This report depends on:

```text
lambda_variational_minimum_probe_011
```

It satisfies:

```text
lambda_boundary_admissibility_probe_required_011
```

## Symbolic Checks

For the asymptotically flat scalar bridge:

```text
Phi = -Lambda*r**2/6 - M/r
F_r = Lambda*r/3 - M/r**2
r^2 F_r = Lambda*r**3/3 - M
d(r^2 F_r)/dr = Lambda*r**2
finite-flux Lambda = 0
```

For supplied constant-curvature boundary scales:

```text
de Sitter radius L:      Lambda = 3/L**2
anti-de Sitter radius L: Lambda = -3/L**2
horizon/domain R_b:      Lambda = 3/R_b**2
```

For a compact constant-curvature 4D topology/volume ledger:

```text
Gauss-Bonnet density E = 8*Lambda**2/3
Lambda^2 from E V = 32 pi^2 chi:
  Lambda^2 = 12*pi**2*chi/V
```

## Probe Ledger

| probe | boundary data | relation | selected quantity | source of scale | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
| asymptotically_flat_finite_flux | finite radius-independent scalar flux at infinity | d(r^2 F)/dr = Lambda*r**2 | Lambda = 0 | no nonzero background scale supplied | selects Lambda = 0 within the asymptotically flat scalar bridge | do not infer observed nonzero Lambda from this sector |
| de_sitter_radius_boundary | asymptotic de Sitter radius L | 1 - Lambda L^2 / 3 = 0 | Lambda = 3/L**2 | boundary radius L | converts supplied L into positive Lambda | derive L before claiming derived nonzero Lambda |
| anti_de_sitter_radius_boundary | asymptotic anti-de Sitter radius L | curvature scale sign supplied by AdS boundary class | Lambda = -3/L**2 | boundary radius L and AdS sign class | converts supplied L and sign class into negative Lambda | derive L and sign class before claiming derived Lambda |
| compact_constant_curvature_gb | compact constant-curvature 4D topology and volume | (8/3) Lambda^2 V = 32 pi^2 chi | Lambda^2 = 12*pi**2*chi/V | volume V; sign still unselected | constrains magnitude when V and chi are supplied | derive volume and sign selector before claiming a value |
| horizon_domain_radius_boundary | domain or horizon radius R_b | 1 - Lambda R_b^2 / 3 = 0 | Lambda = 3/R_b**2 | boundary radius R_b | converts supplied boundary radius into Lambda | derive R_b from vacuum admissibility before claiming selection |

## Current Conclusion

Boundary/admissibility data can select allowed `Lambda` families and can
convert a supplied boundary length, radius, volume, or asymptotic class into a
`Lambda` relation. It does not derive a nonzero value unless the boundary scale
or volume is itself selected by the vacuum ontology.

The clean split is:

```text
asymptotically flat finite-flux data:
  Lambda = 0

de Sitter / anti-de Sitter / horizon data:
  nonzero Lambda inherits a supplied length or radius

compact constant-curvature topology:
  Lambda^2 V is constrained, but V and sign still require selection
```

## Classification

```text
result type: Lambda boundary/admissibility selector probe
scope: boundary data as source of Lambda baseline relations
conclusion: boundary data can convert supplied scales into Lambda, but does not derive the scale
non-conclusion: no nonzero Lambda value is derived; topology/global constraints are not yet fully tested
```

The next technical target is:

```text
lambda_topology_global_constraint_probe_required_012
```
