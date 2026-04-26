"""Reciprocal scaling checks.

Checks whether a model implies A*B = 1 (equivalently kappa = 0).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy

from vacuumforge.core.simplify import is_zero
from vacuumforge.core.status import Exactness


@dataclass
class ReciprocalCheckResult:
    """Result of a reciprocal scaling check."""

    holds: bool | None  # True, False, or None (undetermined)
    exactness: Exactness
    status: str  # "pass", "fail", "assumed", "undetermined"
    residual: sympy.Basic | None = None
    message: str = ""
    dependencies: list[str] = field(default_factory=list)


def check_exact_reciprocal(A: sympy.Basic, B: sympy.Basic) -> ReciprocalCheckResult:
    """Check if A*B = 1 holds exactly."""
    residual = sympy.simplify(A * B - 1)
    result = is_zero(residual)

    if result is True:
        return ReciprocalCheckResult(
            holds=True, exactness=Exactness.EXACT,
            status="pass", residual=residual,
            message="A*B = 1 holds exactly.",
        )
    elif result is False:
        return ReciprocalCheckResult(
            holds=False, exactness=Exactness.EXACT,
            status="fail", residual=residual,
            message=f"A*B - 1 = {residual} (nonzero).",
        )
    else:
        return ReciprocalCheckResult(
            holds=None, exactness=Exactness.UNDETERMINED,
            status="undetermined", residual=residual,
            message=f"Cannot determine if A*B = 1. Residual: {residual}",
        )


def check_kappa_zero(kappa_value: sympy.Basic) -> ReciprocalCheckResult:
    """Check if kappa = 0 (equivalent to A*B = 1)."""
    result = is_zero(kappa_value)

    if result is True:
        return ReciprocalCheckResult(
            holds=True, exactness=Exactness.EXACT,
            status="pass", residual=kappa_value,
            message="kappa = 0 holds.",
        )
    elif result is False:
        return ReciprocalCheckResult(
            holds=False, exactness=Exactness.EXACT,
            status="fail", residual=kappa_value,
            message=f"kappa = {kappa_value} (nonzero).",
        )
    else:
        return ReciprocalCheckResult(
            holds=None, exactness=Exactness.UNDETERMINED,
            status="undetermined", residual=kappa_value,
            message=f"Cannot determine if kappa = 0. Value: {kappa_value}",
        )


def check_perturbative_reciprocal(
    A: sympy.Basic,
    B: sympy.Basic,
    Phi: sympy.Basic,
    c: sympy.Basic,
    order: int = 2,
) -> ReciprocalCheckResult:
    """Check if A*B = 1 holds perturbatively to a given order."""
    eps = sympy.Symbol("_vf_eps_recip")
    product = A * B
    product_eps = product.subs(Phi / c**2, eps)
    if product_eps.has(Phi):
        product_eps = product_eps.subs(Phi, eps * c**2)

    series = sympy.series(product_eps - 1, eps, 0, order + 1).removeO()

    if sympy.simplify(series) == 0:
        return ReciprocalCheckResult(
            holds=True,
            exactness=Exactness.EXACT,
            status="pass",
            residual=sympy.Integer(0),
            message=f"A*B = 1 holds to order {order}.",
        )

    # Find first nonzero order
    for n in range(order + 1):
        coeff = series.coeff(eps, n)
        if sympy.simplify(coeff) != 0:
            if n == 0:
                return ReciprocalCheckResult(
                    holds=False, exactness=Exactness.EXACT,
                    status="fail", residual=series.subs(eps, Phi / c**2),
                    message=f"A*B - 1 has nonzero zeroth-order term: {coeff}",
                )
            else:
                return ReciprocalCheckResult(
                    holds=False,
                    exactness=Exactness.FIRST_ORDER if n == 1 else Exactness.SECOND_ORDER,
                    status="fail",
                    residual=series.subs(eps, Phi / c**2),
                    message=f"A*B = 1 fails at order {n}. Coefficient: {coeff}",
                )

    return ReciprocalCheckResult(
        holds=True, exactness=Exactness.EXACT,
        status="pass", residual=sympy.Integer(0),
        message=f"A*B = 1 holds to order {order}.",
    )
