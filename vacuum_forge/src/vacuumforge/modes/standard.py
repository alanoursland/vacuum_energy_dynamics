"""Standard equal-response symbol definitions.

Provides ready-to-use variable sets for the equal-response problem:
  - Scale factors: A, B
  - Log variables: a, b
  - Mode variables: kappa, sigma
  - Mismatch: mu = a + b = 2*kappa
  - Sources: J_a, J_b, J_kappa, J_sigma
  - PPN parameters: gamma_v, beta
  - Physical constants: c, G, M
  - Potential: Phi
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy

from vacuumforge.modes.transforms import TransformEngine


@dataclass
class AlgebraicModeSymbols:
    """Coordinate-free algebraic symbols for the equal-response problem."""

    # Scale factors
    A: sympy.Symbol
    B: sympy.Symbol

    # Log variables
    a: sympy.Symbol
    b: sympy.Symbol

    # Mode variables
    kappa: sympy.Symbol
    sigma: sympy.Symbol

    # Mismatch
    mu: sympy.Symbol

    # Sources
    J_a: sympy.Symbol
    J_b: sympy.Symbol
    J_kappa: sympy.Symbol
    J_sigma: sympy.Symbol

    # PPN parameters
    gamma_v: sympy.Symbol
    beta: sympy.Symbol

    # Physical constants and potential
    c: sympy.Symbol
    G: sympy.Symbol
    M: sympy.Symbol
    Phi: sympy.Symbol

    # Coordinate
    r: sympy.Symbol

    # Stiffness coefficients
    C_kappa: sympy.Symbol
    C_sigma: sympy.Symbol

    # Transform engine
    transforms: TransformEngine


def create_algebraic_symbols() -> AlgebraicModeSymbols:
    """Create the standard algebraic symbol set for equal-response analysis."""

    A, B = sympy.symbols("A B", positive=True)
    a, b = sympy.symbols("a b", real=True)
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    mu = sympy.Symbol("mu", real=True)

    J_a, J_b = sympy.symbols("J_a J_b")
    J_kappa, J_sigma = sympy.symbols("J_kappa J_sigma")

    gamma_v = sympy.Symbol("gamma_v")
    beta = sympy.Symbol("beta")

    c = sympy.Symbol("c", positive=True)
    G = sympy.Symbol("G", positive=True)
    M = sympy.Symbol("M", positive=True)
    Phi = sympy.Symbol("Phi")
    r = sympy.Symbol("r", positive=True)

    C_kappa = sympy.Symbol("C_kappa", positive=True)
    C_sigma = sympy.Symbol("C_sigma", positive=True)

    transforms = TransformEngine(A=A, B=B, a=a, b=b, kappa=kappa, sigma=sigma)

    return AlgebraicModeSymbols(
        A=A, B=B, a=a, b=b, kappa=kappa, sigma=sigma, mu=mu,
        J_a=J_a, J_b=J_b, J_kappa=J_kappa, J_sigma=J_sigma,
        gamma_v=gamma_v, beta=beta,
        c=c, G=G, M=M, Phi=Phi, r=r,
        C_kappa=C_kappa, C_sigma=C_sigma,
        transforms=transforms,
    )


@dataclass
class FieldModeSymbols:
    """Function-valued symbols for radial field problems."""

    r: sympy.Symbol
    A: sympy.Basic  # A(r)
    B: sympy.Basic  # B(r)
    a: sympy.Basic  # a(r)
    b: sympy.Basic  # b(r)
    kappa: sympy.Basic  # kappa(r)
    sigma: sympy.Basic  # sigma(r)
    Phi: sympy.Basic  # Phi(r)
    c: sympy.Symbol
    G: sympy.Symbol
    M: sympy.Symbol


def create_field_symbols() -> FieldModeSymbols:
    """Create function-valued symbols for radial field equations."""
    r = sympy.Symbol("r", positive=True)
    c = sympy.Symbol("c", positive=True)
    G = sympy.Symbol("G", positive=True)
    M = sympy.Symbol("M", positive=True)

    A = sympy.Function("A")(r)
    B = sympy.Function("B")(r)
    a_func = sympy.Function("a")(r)
    b_func = sympy.Function("b")(r)
    kappa = sympy.Function("kappa")(r)
    sigma = sympy.Function("sigma")(r)
    Phi = sympy.Function("Phi")(r)

    return FieldModeSymbols(
        r=r, A=A, B=B, a=a_func, b=b_func,
        kappa=kappa, sigma=sigma, Phi=Phi,
        c=c, G=G, M=M,
    )
