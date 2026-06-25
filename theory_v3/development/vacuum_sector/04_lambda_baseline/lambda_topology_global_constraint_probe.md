# Lambda Topology/Global Constraint Probe

# Claim

Topology and global constraints can restrict allowed sectors and relate
`Lambda` to supplied area, volume, length, or measure data. Topology alone does
not derive a dimensionful `Lambda` value.

# Scope

This probe tests topology/global data as Lambda selectors. It does not test
measure identities, relaxation dynamics, or microphysical floors.

# Inputs Used

```text
Euler characteristic chi;
2D area A;
4D constant-curvature volume V;
dimensionless sector label q;
length scale L.
```

# What Is Not Assumed

```text
observed Lambda value;
derived area or volume;
derived sign selector;
measure identity;
dark-sector excess.
```

# Candidate Object

The candidate selector object is a global/topological constraint:

```text
Euler characteristic;
Gauss-Bonnet relation;
global sector label;
constant-curvature compactness relation.
```

# Symbolic / Variational / Ledger Check

The managed report checks:

```text
dim(chi) = L^0 while dim(Lambda) = L^-2;
2D Gauss-Bonnet gives R = 4*pi*chi/A;
4D constant-curvature Gauss-Bonnet gives Lambda^2 = 12*pi^2*chi/V;
global quantization gives Lambda = q/L^2 only after L is supplied.
```

# Gate Results

```text
topology alone:
  dimension mismatch for Lambda

topology plus area:
  can set curvature from supplied area

topology plus volume:
  can constrain Lambda magnitude from supplied volume

topology plus length:
  can label sectors after a scale is supplied
```

# Current Classification

```text
result type: Lambda topology/global constraint probe
classification: deferred pending measure/scale selector
```

# Non-Conclusions

This probe does not:

```text
derive a nonzero Lambda value;
derive compact volume;
derive a sign selector;
kill topology/global constraints as sector restrictions;
test measure identities.
```

# Satisfied Obligation

```text
lambda_topology_global_constraint_probe_required_012
```

# Newly Opened Obligation

```text
lambda_measure_identity_probe_required_013
```
