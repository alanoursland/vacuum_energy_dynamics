"""Exact vs perturbative reasoning utilities.

Provides tools to determine whether a result holds exactly,
to first order, to second order, or fails at a specific order.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy

from vacuumforge.core.status import Exactness


@dataclass
class PerturbativeCheck:
    """Result of checking a condition at a given perturbative order."""

    target: str
    order: int
    residual: sympy.Basic
    holds_exactly: bool
    holds_to_order: bool
    first_failure_order: int | None = None
    exactness: Exactness = Exactness.UNDETERMINED
    message: str = ""


def check_condition_perturbative(
    expr: sympy.Basic,
    Phi: sympy.Basic,
    c: sympy.Basic,
    order: int = 2,
    target_description: str = "condition",
) -> PerturbativeCheck:
    """Check if an expression is zero exactly or to a given perturbative order.

    Expands expr in powers of Phi/c^2 and checks each order.
    """
    eps = sympy.Symbol("_vf_eps_pert")

    # First check exact
    simplified = sympy.simplify(expr)
    if simplified == 0:
        return PerturbativeCheck(
            target=target_description,
            order=order,
            residual=sympy.Integer(0),
            holds_exactly=True,
            holds_to_order=True,
            exactness=Exactness.EXACT,
            message=f"{target_description} holds exactly.",
        )

    # Perturbative check
    expr_eps = expr.subs(Phi / c**2, eps)
    if expr_eps.has(Phi):
        expr_eps = expr_eps.subs(Phi, eps * c**2)

    series = sympy.series(expr_eps, eps, 0, order + 1).removeO()

    # Check each order
    first_failure = None
    for n in range(order + 1):
        coeff = sympy.simplify(series.coeff(eps, n))
        if coeff != 0:
            first_failure = n
            break

    if first_failure is None:
        return PerturbativeCheck(
            target=target_description,
            order=order,
            residual=sympy.Integer(0),
            holds_exactly=False,
            holds_to_order=True,
            exactness=Exactness.EXACT,
            message=f"{target_description} holds to order {order}.",
        )

    # Determine what order it holds to
    if first_failure == 0:
        return PerturbativeCheck(
            target=target_description,
            order=order,
            residual=series.subs(eps, Phi / c**2),
            holds_exactly=False,
            holds_to_order=False,
            first_failure_order=0,
            exactness=Exactness.UNDETERMINED,
            message=f"{target_description} fails at zeroth order.",
        )

    holds_order = first_failure - 1
    if holds_order == 0:
        exactness = Exactness.FIRST_ORDER
    elif holds_order == 1:
        exactness = Exactness.FIRST_ORDER
    else:
        exactness = Exactness.SECOND_ORDER

    return PerturbativeCheck(
        target=target_description,
        order=order,
        residual=series.subs(eps, Phi / c**2),
        holds_exactly=False,
        holds_to_order=False,
        first_failure_order=first_failure,
        exactness=exactness,
        message=(
            f"{target_description} holds to order {holds_order} "
            f"but fails at order {first_failure}."
        ),
    )


def check_reciprocal_exactness(
    A: sympy.Basic,
    B: sympy.Basic,
    Phi: sympy.Basic,
    c: sympy.Basic,
    order: int = 2,
) -> PerturbativeCheck:
    """Check A*B = 1 with full exactness reporting."""
    return check_condition_perturbative(
        A * B - 1, Phi, c, order,
        target_description="A*B = 1",
    )
