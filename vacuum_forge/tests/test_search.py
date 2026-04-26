"""Tests for candidate equation search."""

import sympy
from vacuumforge.search.solver import search_energy_coefficients


def test_standard_source_coupled_search():
    """Standard source-coupled energy satisfies key requirements."""
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    Ck = sympy.Symbol("C_kappa", positive=True)
    Cs = sympy.Symbol("C_sigma", positive=True)
    Jk, Js = sympy.symbols("J_kappa J_sigma")

    E = Ck * kappa**2 + Cs * sigma**2 - Jk * kappa - Js * sigma

    result = search_energy_coefficients(
        E, [kappa, sigma], [Ck, Cs],
        requirements={
            "unsourced_kappa_zero": {
                "type": "equilibrium_zero",
                "variable": kappa,
                "source_zero": Jk,
            },
            "nonzero_sigma": {
                "type": "equilibrium_nonzero",
                "variable": sigma,
                "source_symbol": Js,
            },
            "positive_energy": {
                "type": "positivity",
            },
        },
    )

    assert "unsourced_kappa_zero" in result.passes
    assert "nonzero_sigma" in result.passes
    assert "positive_energy" in result.passes
    assert len(result.fails) == 0


def test_cross_coupled_search():
    """Cross-coupled energy with free c3."""
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    c1 = sympy.Symbol("c1", positive=True)
    c2 = sympy.Symbol("c2", positive=True)
    c3 = sympy.Symbol("c3")
    Jk, Js = sympy.symbols("J_kappa J_sigma")

    E = c1 * kappa**2 + c2 * sigma**2 + c3 * kappa * sigma - Jk * kappa - Js * sigma

    result = search_energy_coefficients(
        E, [kappa, sigma], [c1, c2, c3],
        requirements={
            "positive_energy": {"type": "positivity"},
        },
    )
    # c3 makes positivity undetermined
    assert "positive_energy" in result.undetermined or "positive_energy" in result.passes
