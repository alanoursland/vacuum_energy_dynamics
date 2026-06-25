# Lambda Boundary/Admissibility Probe

# Claim

Boundary/admissibility data can select allowed `Lambda` families and can
convert a supplied boundary scale into a `Lambda` relation. It does not derive
a nonzero value unless the boundary scale itself is selected by the vacuum
ontology.

# Scope

This probe tests boundary data as a Lambda selector. It does not modify the
closed local metric equations and does not derive the observed cosmological
constant.

# Inputs Used

```text
asymptotically flat finite scalar flux;
de Sitter radius L;
anti-de Sitter radius L;
compact constant-curvature 4D volume V and Euler characteristic chi;
horizon/domain radius R_b.
```

# What Is Not Assumed

```text
observed Lambda value;
derived boundary length;
derived compact volume;
derived sign selector;
local strain residual.
```

# Candidate Object

The candidate selector object is explicit boundary/admissibility data:

```text
asymptotic class;
boundary radius;
compact volume/topology pair;
horizon or domain scale.
```

# Symbolic / Variational / Ledger Check

The managed report checks:

```text
finite flat flux -> Lambda = 0;
de Sitter radius L -> Lambda = +3/L^2;
anti-de Sitter radius L -> Lambda = -3/L^2;
constant-curvature Gauss-Bonnet -> Lambda^2 = 12*pi^2*chi/V;
horizon/domain radius R_b -> Lambda = 3/R_b^2.
```

# Gate Results

```text
asymptotic flatness:
  selects Lambda = 0 in the scalar boundary-flux bridge

de Sitter / anti-de Sitter / horizon data:
  convert supplied boundary scale into Lambda

compact topology plus volume:
  constrains Lambda^2, but imports V and still needs a sign selector
```

# Current Classification

```text
result type: Lambda boundary/admissibility selector probe
classification: deferred pending boundary-scale selector
```

# Non-Conclusions

This probe does not:

```text
derive a nonzero Lambda value;
derive the boundary scale;
derive the compact volume;
select the sign in the compact topology case;
license a dark-sector excess;
modify local GR equations.
```

# Satisfied Obligation

```text
lambda_boundary_admissibility_probe_required_011
```

# Newly Opened Obligation

```text
lambda_topology_global_constraint_probe_required_012
```
