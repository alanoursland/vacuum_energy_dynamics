"""Candidate family templates for systematic exploration.

Provides reusable symbolic templates for common candidate structures
in the equal-response problem.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy

from vacuumforge.core.status import Exactness


@dataclass
class CandidateFamily:
    """A parameterized family of candidate structures."""

    id: str
    expression_template: sympy.Basic
    coefficients: list[sympy.Symbol]
    variables: list[sympy.Basic] = field(default_factory=list)
    constraints: list[sympy.Basic] = field(default_factory=list)
    description: str = ""


@dataclass
class CandidateResult:
    """Result of evaluating a specific candidate within a family."""

    family_id: str
    parameter_values: dict[sympy.Symbol, Any]
    A: sympy.Basic
    B: sympy.Basic
    gamma_v: sympy.Basic | None = None
    beta: sympy.Basic | None = None
    reciprocal: bool | None = None
    notes: list[str] = field(default_factory=list)


# --- Built-in families ---

def reciprocal_power_family(
    Phi: sympy.Basic, c: sympy.Basic, p: sympy.Basic | None = None,
) -> tuple[sympy.Basic, sympy.Basic, sympy.Basic]:
    """B = A^(-p) family.

    A = exp(Phi/c^2), B = exp(-p*Phi/c^2).
    Predictions: gamma_v = p, beta = 1.
    Reciprocal scaling when p = 1.

    Returns (A, B, p).
    """
    if p is None:
        p = sympy.Symbol("p")
    A = sympy.exp(Phi / c**2)
    B = A**(-p)
    return A, B, p


def exponential_scale_family(
    Phi: sympy.Basic, c: sympy.Basic,
    alpha: sympy.Basic | None = None,
    lam: sympy.Basic | None = None,
) -> tuple[sympy.Basic, sympy.Basic, sympy.Basic, sympy.Basic]:
    """A = exp(alpha*Phi/c^2), B = exp(-lambda*Phi/c^2).

    Predictions: gamma_v = lambda (when alpha normalized to 1),
    beta = alpha^2.

    Returns (A, B, alpha, lambda).
    """
    if alpha is None:
        alpha = sympy.Symbol("alpha")
    if lam is None:
        lam = sympy.Symbol("lambda")
    A = sympy.exp(alpha * Phi / c**2)
    B = sympy.exp(-lam * Phi / c**2)
    return A, B, alpha, lam


def quadratic_mode_energy_family(
    kappa: sympy.Basic,
    sigma: sympy.Basic,
    J_kappa: sympy.Basic,
    J_sigma: sympy.Basic,
) -> tuple[sympy.Basic, list[sympy.Symbol]]:
    """E = c1*kappa^2 + c2*sigma^2 + c3*kappa*sigma - c4*J_kappa*kappa - c5*J_sigma*sigma.

    Returns (E, [c1, c2, c3, c4, c5]).
    """
    c1, c2, c3, c4, c5 = sympy.symbols("c1 c2 c3 c4 c5")
    E = (c1 * kappa**2 + c2 * sigma**2 + c3 * kappa * sigma
         - c4 * J_kappa * kappa - c5 * J_sigma * sigma)
    return E, [c1, c2, c3, c4, c5]


def source_coupled_energy_family(
    kappa: sympy.Basic,
    sigma: sympy.Basic,
    J_kappa: sympy.Basic,
    J_sigma: sympy.Basic,
    C_kappa: sympy.Basic | None = None,
    C_sigma: sympy.Basic | None = None,
) -> tuple[sympy.Basic, sympy.Basic, sympy.Basic]:
    """Standard source-coupled energy: E = Ck*kappa^2 + Cs*sigma^2 - Jk*kappa - Js*sigma.

    Returns (E, C_kappa, C_sigma).
    """
    if C_kappa is None:
        C_kappa = sympy.Symbol("C_kappa", positive=True)
    if C_sigma is None:
        C_sigma = sympy.Symbol("C_sigma", positive=True)
    E = (C_kappa * kappa**2 + C_sigma * sigma**2
         - J_kappa * kappa - J_sigma * sigma)
    return E, C_kappa, C_sigma


def mismatch_energy(
    kappa: sympy.Basic,
    C: sympy.Basic | None = None,
) -> tuple[sympy.Basic, sympy.Basic]:
    """Mismatch energy: E = C * (2*kappa)^2 = 4*C*kappa^2.

    Returns (E, C).
    """
    if C is None:
        C = sympy.Symbol("C_mu", positive=True)
    mu = 2 * kappa
    E = C * mu**2
    return E, C


def scan_power_family(
    Phi: sympy.Basic,
    c: sympy.Basic,
    p_values: list,
    expansion_engine=None,
) -> list[CandidateResult]:
    """Scan the reciprocal power family B = A^(-p) over a list of p values.

    Returns gamma_v and reciprocal status for each p.
    """
    from vacuumforge.metric.ppn import extract_gamma
    from vacuumforge.metric.reciprocal import check_exact_reciprocal
    from vacuumforge.metric.weak_field import WeakFieldMetric

    results = []
    for p_val in p_values:
        A, B, _ = reciprocal_power_family(Phi, c, p=p_val)
        metric = WeakFieldMetric(A, B)

        recip = check_exact_reciprocal(A, B)
        gamma = None
        if expansion_engine:
            gamma_result = extract_gamma(metric, expansion_engine)
            gamma = gamma_result.value

        results.append(CandidateResult(
            family_id="reciprocal_power",
            parameter_values={"p": p_val},
            A=A, B=B,
            gamma_v=gamma,
            reciprocal=recip.holds,
            notes=[recip.message],
        ))
    return results
