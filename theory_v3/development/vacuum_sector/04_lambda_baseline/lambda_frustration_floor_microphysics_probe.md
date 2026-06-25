# Lambda Frustration-Floor Microphysics Probe

# Claim

Microphysical potential shape can supply minima, excitation scales, and a
constant-floor ledger. It does not derive a nonzero `Lambda` baseline unless it
derives the absolute constant offset before observation is used.

# Scope

This probe tests microphysical/frustration floor candidates as Lambda
selectors. It does not develop the dark-sector excess ledger.

# Inputs Used

```text
V(phi) = lambda_f (phi^2 - v^2)^2 / 4 + V0;
constant floor stress p = -rho;
fluctuations around the minimum.
```

# What Is Not Assumed

```text
observed Lambda value;
derived V0;
derived abundance of excitations;
non-clustering proof;
dark-sector dynamics.
```

# Candidate Object

The candidate selector object is a microphysical floor:

```text
microstate variable -> coarse-grained potential -> absolute constant floor.
```

# Symbolic / Variational / Ledger Check

The managed report checks:

```text
potential minima occur at +/-v;
minimum value is V0;
V0 = 0 gives zero floor;
V0 = rho_obs inserts the target;
p + rho = 0 for a constant floor;
fluctuations around the minimum are excitation/excess content, not Lambda.
```

# Gate Results

```text
potential shape:
  not enough to derive Lambda

absolute offset:
  must be derived before observation

constant floor:
  has the right w = -1 ledger but still needs scale/sign derivation

excitations:
  route to dark-sector or defect ledger
```

# Current Classification

```text
result type: Lambda frustration-floor microphysics probe
classification: candidate route only after absolute floor derivation
```

# Non-Conclusions

This probe does not:

```text
derive nonzero Lambda;
derive V0;
license dark-sector excess;
prove non-clustering;
modify the closed local metric equations.
```

# Satisfied Obligation

```text
lambda_frustration_floor_microphysics_probe_required_015
```

# Newly Opened Obligation

```text
dark_excess_source_ledger_required_016
```
