"""Minimal counterexample generation.

Template-based counterexamples for common failed derivation claims.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy


@dataclass
class Counterexample:
    """A symbolic counterexample to a proposed claim."""

    claim: str
    construction: str
    symbols: dict[str, sympy.Basic]
    verification: sympy.Basic
    conclusion: str


def density_with_nonzero_kappa() -> Counterexample:
    """Counterexample: Postulate 2 (constant density) does NOT forbid kappa.

    If density = E_v / V_proper, and a conformal rescaling scales both
    numerator and denominator equally, density is unchanged while kappa != 0.
    """
    kappa = sympy.Symbol("kappa", real=True)
    n = sympy.Symbol("n", positive=True)
    E_v, V = sympy.symbols("E_v V", positive=True)

    rho = E_v / V
    E_v_prime = sympy.exp(n * kappa) * E_v
    V_prime = sympy.exp(n * kappa) * V
    rho_prime = E_v_prime / V_prime

    verification = sympy.simplify(rho_prime - rho)

    return Counterexample(
        claim="Constant vacuum density (Postulate 2) forbids kappa != 0",
        construction=(
            "Let rho = E_v/V_proper. Under conformal rescaling by exp(n*kappa), "
            "both E_v and V_proper scale by the same factor. "
            "Then rho' = rho even though kappa != 0."
        ),
        symbols={"kappa": kappa, "rho": rho, "rho_prime": rho_prime},
        verification=verification,
        conclusion=(
            f"rho' - rho = {verification}. "
            "Density constancy does not by itself forbid nonzero kappa."
        ),
    )


def exchange_with_nonzero_trace() -> Counterexample:
    """Counterexample: Total energy conservation does NOT imply trace-free exchange.

    If Delta_E_matter + Delta_E_vacuum = 0 and vacuum energy goes into
    both kappa and sigma modes, J_kappa can be nonzero while total
    energy is still conserved.
    """
    E_kappa, E_sigma = sympy.symbols("E_kappa E_sigma")
    Delta_Em = sympy.Symbol("Delta_E_m")

    total_conservation = sympy.Eq(Delta_Em + E_kappa + E_sigma, 0)
    # Solving for Delta_Em: matter loses what vacuum gains
    Delta_Em_val = sympy.solve(total_conservation, Delta_Em)[0]

    return Counterexample(
        claim="Local energy exchange implies trace-free sourcing (J_kappa = 0)",
        construction=(
            "Let Delta_E_m + E_kappa + E_sigma = 0 (total conservation). "
            "This constrains Delta_E_m = -(E_kappa + E_sigma), "
            "but places no constraint on E_kappa individually. "
            "E_kappa != 0 is compatible with total conservation."
        ),
        symbols={
            "total_conservation": total_conservation,
            "Delta_E_m": Delta_Em_val,
            "E_kappa": E_kappa,
        },
        verification=Delta_Em_val + E_kappa + E_sigma,
        conclusion=(
            "Total energy conservation is satisfied for any E_kappa. "
            "Trace-free exchange (E_kappa = 0) requires an additional principle."
        ),
    )


def parallel_scaling_failure() -> Counterexample:
    """Counterexample: Parallel scaling A = B fails reciprocal scaling.

    A = exp(Phi/c^2), B = exp(Phi/c^2).
    A*B = exp(2*Phi/c^2) != 1.
    gamma_v = -1.
    """
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(Phi / c**2)

    product = sympy.simplify(A * B)
    ratio = sympy.simplify(A / B)

    return Counterexample(
        claim="Any exponential metric ansatz gives reciprocal scaling",
        construction=(
            "Let A = B = exp(Phi/c^2) (parallel scaling). "
            f"Then A*B = {product}, A/B = {ratio}."
        ),
        symbols={"A": A, "B": B, "A*B": product, "A/B": ratio},
        verification=sympy.simplify(A * B - 1),
        conclusion=(
            f"A*B = {product} != 1. "
            "Parallel scaling gives gamma_v = -1, not 1. "
            "Reciprocal scaling requires a specific relationship between A and B."
        ),
    )


ALL_COUNTEREXAMPLES = {
    "density_allows_kappa": density_with_nonzero_kappa,
    "exchange_allows_trace": exchange_with_nonzero_trace,
    "parallel_scaling_fails": parallel_scaling_failure,
}
