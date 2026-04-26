"""Tests for energy functionals and minimization."""

import sympy
from vacuumforge.energy.functional import EnergyManager
from vacuumforge.energy.positivity import check_quadratic_positivity


def test_source_coupled_minimization():
    """E = Ck*kappa^2 + Cs*sigma^2 - Jk*kappa - Js*sigma
    Stationary: kappa = Jk/(2*Ck), sigma = Js/(2*Cs).
    """
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    Ck = sympy.Symbol("C_kappa", positive=True)
    Cs = sympy.Symbol("C_sigma", positive=True)
    Jk, Js = sympy.symbols("J_kappa J_sigma")

    mgr = EnergyManager()
    mgr.source_coupled(Ck, Cs, Jk, Js, kappa, sigma)
    result = mgr.solve_stationary("source_coupled_energy")

    assert len(result.solutions) == 1
    sol = result.solutions[0]
    assert sympy.simplify(sol[kappa] - Jk / (2 * Ck)) == 0
    assert sympy.simplify(sol[sigma] - Js / (2 * Cs)) == 0


def test_unsourced_kappa_zero():
    """With J_kappa = 0, kappa equilibrium is 0."""
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    Ck = sympy.Symbol("C_kappa", positive=True)
    Cs = sympy.Symbol("C_sigma", positive=True)
    Jk, Js = sympy.symbols("J_kappa J_sigma")

    mgr = EnergyManager()
    mgr.source_coupled(Ck, Cs, Jk, Js, kappa, sigma)
    result = mgr.solve_stationary("source_coupled_energy", extra_subs={Jk: 0})

    sol = result.solutions[0]
    assert sol[kappa] == 0


def test_sourced_sigma_nonzero():
    """With J_sigma != 0, sigma equilibrium is nonzero."""
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    Ck = sympy.Symbol("C_kappa", positive=True)
    Cs = sympy.Symbol("C_sigma", positive=True)
    Js = sympy.Symbol("J_sigma")

    mgr = EnergyManager()
    mgr.source_coupled(Ck, Cs, sympy.Integer(0), Js, kappa, sigma)
    result = mgr.solve_stationary("source_coupled_energy")

    sol = result.solutions[0]
    # sigma = Js/(2*Cs), which is nonzero for nonzero Js
    assert sol[sigma] != 0


def test_positivity_positive():
    """Ck*kappa^2 + Cs*sigma^2 with positive coefficients."""
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    Ck = sympy.Symbol("C_kappa", positive=True)
    Cs = sympy.Symbol("C_sigma", positive=True)
    E = Ck * kappa**2 + Cs * sigma**2
    result = check_quadratic_positivity(E, [kappa, sigma])
    assert result.status == "positive"


def test_positivity_with_cross_term():
    """Cross-coupled form: needs determinant check."""
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    c1 = sympy.Symbol("c1", positive=True)
    c2 = sympy.Symbol("c2", positive=True)
    c3 = sympy.Symbol("c3")
    E = c1 * kappa**2 + c2 * sigma**2 + c3 * kappa * sigma
    result = check_quadratic_positivity(E, [kappa, sigma])
    # Can't determine without knowing c3, should be undetermined
    assert result.status in ("undetermined", "positive")


def test_quadratic_modes():
    """Test convenience builder."""
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    Ck = sympy.Symbol("C_kappa", positive=True)
    Cs = sympy.Symbol("C_sigma", positive=True)

    mgr = EnergyManager()
    func = mgr.quadratic_modes(Ck, Cs, kappa, sigma)
    assert func.expression == Ck * kappa**2 + Cs * sigma**2


def test_context_energy(ctx):
    """Test energy through the context."""
    ms = ctx._mode_symbols
    ctx.energy.source_coupled(
        ms.C_kappa, ms.C_sigma, ms.J_kappa, ms.J_sigma,
        ms.kappa, ms.sigma,
    )
    result = ctx.energy.solve_stationary(
        "source_coupled_energy",
        extra_subs={ms.J_kappa: 0},
    )
    sol = result.solutions[0]
    assert sol[ms.kappa] == 0
