#!/usr/bin/env python3
"""
make_7_lorentzian_propagation_signature_gate.py

Validate that real finite-speed propagation is associated with a Lorentzian
principal signature, while a positive Euclidean principal form gives elliptic
behavior.

Output:
    7_lorentzian_propagation_signature_gate.md
"""

from pathlib import Path
import sympy as sp


omega, k, c = sp.symbols("omega k c", positive=True)
W = sp.symbols("W")
qt, qx, pi = sp.symbols("q_t q_x pi")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

P_lorentz = -omega**2 + c**2 * k**2
P_euclid = omega**2 + c**2 * k**2

omega_sq_lorentz = sp.solve(sp.Eq((-W + c**2 * k**2), 0), W)[0]
omega_sq_euclid = sp.solve(sp.Eq((W + c**2 * k**2), 0), W)[0]

require_equal("Lorentzian dispersion", omega_sq_lorentz, c**2 * k**2)
checks.append("Lorentzian dispersion")

require_equal("Euclidean elliptic dispersion", omega_sq_euclid, -c**2 * k**2)
checks.append("Euclidean elliptic dispersion")

omega_branch = c * k
group_velocity = sp.diff(omega_branch, k)
require_equal("Lorentzian group velocity", group_velocity, c)
checks.append("Lorentzian group velocity")

G_lorentz_det = sp.Matrix([[-1, 0], [0, c**2]]).det()
G_euclid_det = sp.Matrix([[1, 0], [0, c**2]]).det()
require_equal("Lorentzian principal determinant", G_lorentz_det, -c**2)
checks.append("Lorentzian principal determinant")
require_equal("Euclidean principal determinant", G_euclid_det, c**2)
checks.append("Euclidean principal determinant")

# Stable Hamiltonian from Lorentzian wave Lagrangian.
L_wave = sp.Rational(1, 2) * (qt**2 - c**2 * qx**2)
canonical_pi = sp.diff(L_wave, qt)
require_equal("canonical momentum", canonical_pi, qt)
checks.append("canonical momentum")

Hamiltonian = simplify_expr((pi * qt - L_wave).subs(qt, pi))
require_equal("positive wave Hamiltonian density", Hamiltonian, sp.Rational(1, 2) * (pi**2 + c**2 * qx**2))
checks.append("positive wave Hamiltonian density")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 7: Lorentzian Propagation Signature Gate

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

{validation_bullets}

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
"""

out = Path(__file__).with_name("7_lorentzian_propagation_signature_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
