# Vacuum Action Origin 7: Lorentzian Propagation Signature Gate

## Purpose

This report tests the signature gate for propagating vacuum disturbances.

It does not derive Lorentzian signature from first principles. It proves the
conditional statement:

```text
real finite-speed wave propagation
  -> hyperbolic principal form
  -> Lorentzian sign split.
```

## Validated Checks

- Lorentzian dispersion: passed
- Euclidean elliptic dispersion: passed
- Lorentzian group velocity: passed
- Lorentzian principal determinant: passed
- Euclidean principal determinant: passed
- canonical momentum: passed
- positive wave Hamiltonian density: passed

## Principal Symbols

For a Lorentzian wave operator:

```text
P_L = -omega^2 + c^2 k^2.
```

SymPy verifies:

```text
P_L = 0 -> omega^2 = c^2 k^2.
```

So real nonzero `k` gives real propagation frequency and group velocity:

```text
domega/dk = c.
```

For a Euclidean elliptic operator:

```text
P_E = omega^2 + c^2 k^2.
```

SymPy verifies:

```text
P_E = 0 -> omega^2 = -c^2 k^2.
```

So nonzero real `k` does not give real oscillatory propagation.

## Stable Energy

The Lorentzian wave Lagrangian:

```text
L = (1/2)[q_t^2 - c^2 q_x^2]
```

has canonical momentum:

```text
pi = q_t.
```

SymPy verifies the Hamiltonian density:

```text
H = (1/2)[pi^2 + c^2 q_x^2].
```

Thus Lorentzian spacetime signature is compatible with positive propagation
energy.

## Interpretation

If the vacuum supports real local propagating disturbances, the local interval
cannot be purely positive definite in the propagation variables. A Lorentzian
sign split is the minimal principal structure that gives finite-speed
hyperbolic evolution while preserving positive Hamiltonian energy.
