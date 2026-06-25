# Dark Excess Abundance/Production Probe

# Claim

A pressureless vacuum-sector excess is not a dark-sector model until its
production or formation mechanism computes an abundance before the observed
dark matter density is inserted.

# Scope

This probe tests abundance bookkeeping. It does not build a halo model or a
specific particle/defect microphysics.

# Inputs Used

```text
rho_today = rho_form (a_form/a_0)^3;
rho_today = m Y s_0;
Omega proxy proportional to 1/<sigma v>;
rho_today = f_form rho_tot,form (a_form/a_0)^3.
```

# What Is Not Assumed

```text
observed dark matter density as input;
particle identity;
cross section;
formation fraction;
initial yield;
halo phenomenology.
```

# Candidate Object

The candidate object is an abundance route:

```text
production/formation law -> conserved number or energy density -> present
abundance.
```

# Symbolic / Variational / Ledger Check

The managed report checks:

```text
observed-value insertion solves for the required initial density;
yield route needs m and Y;
freezeout proxy needs <sigma v>;
formation route needs f_form and formation epoch;
all routes need microphysics or formation data before becoming predictions.
```

# Gate Results

```text
observed insertion:
  rejected as fitting

yield route:
  candidate only after Y is derived

freezeout-like route:
  candidate only after interaction/cross-section route exists

formation-fraction route:
  candidate only after formation dynamics derive f_form
```

# Current Classification

```text
result type: dark-excess abundance/production probe
classification: no abundance route licensed without production microphysics
```

# Non-Conclusions

This probe does not:

```text
derive dark matter abundance;
identify the excess;
derive a cross section;
derive a formation fraction;
prove halo phenomenology.
```

# Satisfied Obligation

```text
dark_excess_abundance_production_required_018
```

# Newly Opened Obligation

```text
non_grav_channel_quarantine_required_019
```
