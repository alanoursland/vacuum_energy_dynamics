# Einstein-Hilbert Origin Test 105: EH Linearizes to Fierz-Pauli Action

## Purpose

This report validates that the Gamma-Gamma part of the Einstein-Hilbert action
linearizes to the Fierz-Pauli / linearized Einstein quadratic action.

## Validated Checks

- Gamma-Gamma quadratic equals Fierz-Pauli action: passed
- Gamma-Gamma quadratic varies to linearized Einstein operator: passed

## Identity

Using a plane-wave/momentum-space substitution:

```text
partial_c h_ab -> k_c H_ab,
```

SymPy verifies:

```text
L_GG^(2) = 1/2 h^ab G_ab[h].
```

It also verifies that varying the quadratic Gamma-Gamma density with respect to
the independent symmetric components gives the linearized Einstein operator.

## Interpretation

This proves the direct action bridge:

```text
Einstein-Hilbert
  -> Gamma-Gamma connection strain
  -> Fierz-Pauli quadratic action
  -> linearized Einstein equations.
```
