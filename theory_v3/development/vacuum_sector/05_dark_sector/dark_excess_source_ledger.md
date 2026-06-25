# Dark Excess Source Ledger

# Claim

Vacuum-sector excess must be separated from the constant Lambda floor before
it can be treated as a dark-sector candidate.

# Scope

This ledger classifies source bookkeeping and equation-of-state faces. It does
not yet derive abundance, clustering, or a production mechanism.

# Inputs Used

```text
T_vac = T_floor + T_excess;
rho(a) scales as a^(-3(1+w));
w = -1, 0, 1/3, -1/3, -2/3.
```

# What Is Not Assumed

```text
observed dark matter abundance;
cluster formation;
particle dark matter;
constant Lambda derivation;
exchange law between floor and excess.
```

# Candidate Object

The candidate object is a source split:

```text
T_vac_ab = T_floor_ab + T_excess_ab.
```

The floor has:

```text
T_floor_ab = -rho_Lambda g_ab
w = -1
constant density
```

The excess must have its own equation of state, conservation or exchange law,
and clustering ledger.

# Symbolic / Variational / Ledger Check

The managed report checks:

```text
w = -1:
  rho is constant -> Lambda floor

w = 0:
  rho scales as a^-3 -> dustlike excess candidate

w = 1/3:
  rho scales as a^-4 -> radiationlike, not CDM-like

w = -1/3:
  rho scales as a^-2 -> stringlike defect candidate

w = -2/3:
  rho scales as a^-1 -> wall-like defect candidate
```

# Gate Results

```text
constant floor:
  route to Lambda baseline

dustlike excess:
  candidate only after clustering, conservation, and abundance gates

radiationlike or defectlike densities:
  not CDM-like without additional structure
```

# Current Classification

```text
result type: dark-sector source ledger
classification: source/equation-of-state inventory, not a live dark-sector model
```

# Non-Conclusions

This ledger does not:

```text
derive dark matter;
derive abundance;
prove clustering;
license source insertion;
modify the closed local metric equations.
```

# Satisfied Obligation

```text
dark_excess_source_ledger_required_016
```

# Newly Opened Obligation

```text
dark_excess_clustering_conservation_required_017
```
