# Lambda Measure Identity Probe

# Claim

A measure identity can be a Lambda selector only if it supplies a derived,
covariantly conserved, constant floor before observation is used. Dimensional
fits import a scale, and transportable or clustered densities belong to the
dark-sector ledger rather than the constant Lambda baseline.

# Scope

This probe tests measure identities as Lambda selectors. It does not test
relaxation dynamics or microphysical floor derivations.

# Inputs Used

```text
Lambda = kappa rho;
rho(a) scaling for w = -1, w = 0, and defectlike equations of state;
dimensional fit Lambda = C/L^2.
```

# What Is Not Assumed

```text
observed Lambda value;
derived rho0;
derived length L;
dark-sector abundance;
energy exchange law for variable Lambda.
```

# Candidate Object

The candidate selector object is a covariant measure identity:

```text
measure identity -> conserved density rho0 -> Lambda = kappa rho0.
```

# Symbolic / Variational / Ledger Check

The managed report checks:

```text
dim(kappa rho) = dim(Lambda);
w = -1 gives a constant floor;
w = 0 gives dustlike a^-3 scaling;
defectlike equations of state vary with scale factor;
Lambda = C/L^2 imports L unless L is derived.
```

# Gate Results

```text
conserved w = -1 floor:
  candidate only after rho0 is derived

dimensional fit:
  not a derivation unless L is derived

w != -1 density:
  route to dark-sector or defect ledger, not Lambda
```

# Current Classification

```text
result type: Lambda measure identity probe
classification: candidate route only for a derived conserved floor
```

# Non-Conclusions

This probe does not:

```text
derive rho0;
derive nonzero Lambda;
license dark-sector excess;
provide a relaxation law;
modify the closed local metric equations.
```

# Satisfied Obligation

```text
lambda_measure_identity_probe_required_013
```

# Newly Opened Obligation

```text
lambda_relaxation_fixed_point_probe_required_014
```
