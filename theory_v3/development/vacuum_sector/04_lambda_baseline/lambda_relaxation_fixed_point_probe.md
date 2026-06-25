# Lambda Relaxation/Fixed-Point Probe

# Claim

Relaxation dynamics can select `Lambda = 0` without an extra scale. Nonzero
fixed points require a target, domain length, kernel scale, or coefficient
ratio, and become derived only if that scale is itself derived.

# Scope

This probe tests relaxation/fixed-point dynamics as Lambda selectors. It does
not test microphysical floor derivations.

# Inputs Used

```text
dLambda/dt = -gamma Lambda;
dLambda/dt = -gamma (Lambda - Lambda_star);
dLambda/dt = -gamma (Lambda - sigma/L^2);
dLambda/dt = -gamma Lambda + beta Lambda^2.
```

# What Is Not Assumed

```text
observed Lambda value;
derived target Lambda_star;
derived domain length L;
derived coefficient ratio gamma/beta;
microphysical floor.
```

# Candidate Object

The candidate selector object is a relaxation or fixed-point equation for
`Lambda`.

# Symbolic / Variational / Ledger Check

The managed report checks:

```text
scale-free damping -> Lambda = 0;
target relaxation -> Lambda_star;
domain-scale relaxation -> sigma/L^2;
nonlinear fixed point -> 0 or gamma/beta.
```

# Gate Results

```text
zero relaxation:
  selects Lambda = 0

target relaxation:
  imports the target

domain-scale relaxation:
  imports L

nonlinear fixed point:
  imports coefficient ratio unless coefficients are derived
```

# Current Classification

```text
result type: Lambda relaxation/fixed-point probe
classification: deferred pending derived scale or coefficient route
```

# Non-Conclusions

This probe does not:

```text
derive nonzero Lambda;
derive a target value;
derive a domain length;
derive a microphysical floor;
license dark-sector excess.
```

# Satisfied Obligation

```text
lambda_relaxation_fixed_point_probe_required_014
```

# Newly Opened Obligation

```text
lambda_frustration_floor_microphysics_probe_required_015
```
