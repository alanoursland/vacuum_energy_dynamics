"""Target library for the equal-response problem.

Stores target results and their equivalent forms for
leak detection and validation.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy

from vacuumforge.core.simplify import check_equal
from vacuumforge.core.status import Status


@dataclass
class Target:
    """A target result the theory attempts to derive."""

    id: str
    expression: sympy.Basic
    equivalent_forms: list[sympy.Basic] = field(default_factory=list)
    description: str = ""
    status: Status = Status.TARGET
    exactness: str = "exact"


class TargetLibrary:
    """Library of target results for validation and leak detection."""

    def __init__(self) -> None:
        self._targets: dict[str, Target] = {}

    def add(self, target: Target) -> None:
        self._targets[target.id] = target

    def get(self, id: str) -> Target:
        return self._targets[id]

    def has(self, id: str) -> bool:
        return id in self._targets

    def all(self) -> list[Target]:
        return list(self._targets.values())

    def matches_any_target(self, expr: sympy.Basic) -> list[str]:
        """Check if an expression matches any target or equivalent form."""
        matches = []
        for target in self._targets.values():
            if _expression_matches_target(expr, target):
                matches.append(target.id)
        return matches


def _expression_matches_target(expr: sympy.Basic, target: Target) -> bool:
    """Check if an expression is equivalent to a target or any of its forms."""
    all_forms = [target.expression] + target.equivalent_forms
    for form in all_forms:
        if _exprs_equivalent(expr, form):
            return True
    return False


def _exprs_equivalent(a: sympy.Basic, b: sympy.Basic) -> bool:
    """Check equivalence, handling Eq objects."""
    if isinstance(a, sympy.Eq) and isinstance(b, sympy.Eq):
        return check_equal(a.lhs - a.rhs, b.lhs - b.rhs)
    if isinstance(a, sympy.Eq):
        return check_equal(a.lhs - a.rhs, b)
    if isinstance(b, sympy.Eq):
        return check_equal(a, b.lhs - b.rhs)
    return check_equal(a, b)


def build_standard_targets(
    A: sympy.Basic,
    B: sympy.Basic,
    a: sympy.Basic,
    b: sympy.Basic,
    kappa: sympy.Basic,
    sigma: sympy.Basic,
    mu: sympy.Basic,
    gamma_v: sympy.Basic,
    beta: sympy.Basic,
    Phi: sympy.Basic,
    c: sympy.Basic,
) -> TargetLibrary:
    """Build the standard target library for the equal-response problem."""
    lib = TargetLibrary()

    lib.add(Target(
        id="reciprocal_scaling",
        expression=sympy.Eq(A * B, 1),
        equivalent_forms=[
            sympy.Eq(a + b, 0),
            sympy.Eq(kappa, 0),
            sympy.Eq(mu, 0),
            sympy.Eq(B, 1 / A),
            sympy.Eq(sympy.log(A) + sympy.log(B), 0),
        ],
        description="Reciprocal scaling: A*B = 1",
    ))

    lib.add(Target(
        id="kappa_zero",
        expression=sympy.Eq(kappa, 0),
        equivalent_forms=[
            sympy.Eq(A * B, 1),
            sympy.Eq(a + b, 0),
            sympy.Eq(mu, 0),
        ],
        description="Conformal mode vanishes",
    ))

    lib.add(Target(
        id="gamma_v_one",
        expression=sympy.Eq(gamma_v, 1),
        description="PPN spatial response parameter equals 1",
    ))

    lib.add(Target(
        id="beta_one",
        expression=sympy.Eq(beta, 1),
        description="PPN second-order temporal parameter equals 1",
    ))

    lib.add(Target(
        id="trace_free_exchange",
        expression=sympy.Eq(sympy.Symbol("J_kappa"), 0),
        description="Exchange source is trace-free",
    ))

    return lib
