# Dark Excess Clustering/Conservation Probe

# Claim

A dustlike vacuum-sector excess becomes a dark-sector candidate only if it has
a conservation or exchange law, negligible pressure support, a clustering face,
and source-ledger separation from the Lambda floor.

# Scope

This probe tests clustering/conservation readiness. It does not derive
abundance or a production mechanism.

# Inputs Used

```text
rho_dust = rho0 a^-3;
continuity residual d rho / d ln a + 3(1+w) rho;
pressure perturbation term c_s^2 k^2/a^2;
matter-era growth equation in ln a.
```

# What Is Not Assumed

```text
observed dark matter abundance;
production mechanism;
particle identity;
exchange law with Lambda;
modification of closed local GR equations.
```

# Candidate Object

The candidate object is a conserved, pressureless excess component:

```text
w = 0;
c_s^2 = 0;
nabla^a T_excess_ab = 0
```

or an explicitly routed exchange law:

```text
nabla^a T_excess_ab = J_b,
nabla^a T_floor_ab = -J_b.
```

# Symbolic / Variational / Ledger Check

The managed report checks:

```text
rho0 a^-3 satisfies dust conservation;
pressure support vanishes only when c_s^2 = 0;
matter-era delta proportional to a solves the dust growth proxy;
nonzero exchange residual requires an explicit exchange ledger.
```

# Gate Results

```text
conserved pressureless dustlike excess:
  clustering candidate, but abundance still missing

pressure-supported excess:
  not CDM-like without a small-sound-speed route

exchange with floor:
  requires explicit two-ledger conservation

ordinary matter insertion:
  rejected as source double-counting
```

# Current Classification

```text
result type: dark-excess clustering/conservation probe
classification: candidate route only after production and abundance gates
```

# Non-Conclusions

This probe does not:

```text
derive dark matter abundance;
derive a production mechanism;
prove halo phenomenology;
identify a particle;
modify the closed local metric equations.
```

# Satisfied Obligation

```text
dark_excess_clustering_conservation_required_017
```

# Newly Opened Obligation

```text
dark_excess_abundance_production_required_018
```
