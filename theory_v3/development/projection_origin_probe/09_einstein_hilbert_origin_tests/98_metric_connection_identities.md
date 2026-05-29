# Einstein-Hilbert Origin Test 98: Metric Connection Identities

## Purpose

This report validates the basic nonlinear Levi-Civita connection identities on
a nontrivial diagonal metric:

```text
g = diag(A(x,y), B(x,y)).
```

## Validated Checks

- Christoffel lower-index symmetry: passed
- metric compatibility: passed
- contracted connection / volume identity: passed

## Results

The Christoffel symbol:

```text
Gamma^a_bc =
  1/2 g^ad(
    partial_b g_dc
    + partial_c g_db
    - partial_d g_bc
  )
```

is torsion-free:

```text
Gamma^a_bc = Gamma^a_cb.
```

It is metric-compatible:

```text
nabla_c g_ab = 0.
```

The contracted connection satisfies the volume identity:

```text
Gamma^a_ac = partial_c log(sqrt(g)).
```

## Interpretation

This establishes the nonlinear connection object used by the
Einstein-Hilbert/Gamma-Gamma action tests. It is the candidate geometric
version of configuration strain.
