"""Weak-field expansion engine.

Expands expressions in powers of epsilon = Phi/c^2.
Uses a dummy variable substitution strategy for reliable series expansion.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy

from vacuumforge.core.status import Exactness


@dataclass
class ExpansionResult:
    """Result of a weak-field expansion."""

    original: sympy.Basic
    expanded: sympy.Basic
    parameter: sympy.Basic
    order: int
    exactness: Exactness = Exactness.UNDETERMINED


class ExpansionEngine:
    """Expands expressions in powers of a weak-field parameter."""

    def __init__(self, Phi: sympy.Basic, c: sympy.Basic) -> None:
        self.Phi = Phi
        self.c = c
        self._eps = sympy.Symbol("_vf_epsilon")

    @property
    def epsilon(self) -> sympy.Basic:
        """The expansion parameter Phi/c^2."""
        return self.Phi / self.c**2

    def weak_field(self, expr: sympy.Basic, order: int = 2) -> ExpansionResult:
        """Expand expression in powers of Phi/c^2 to given order."""
        eps = self._eps
        # Substitute Phi/c^2 -> eps
        expr_eps = expr.subs(self.Phi / self.c**2, eps)

        # Also handle Phi -> eps * c^2 for expressions not already in Phi/c^2 form
        if expr_eps.has(self.Phi):
            expr_eps = expr_eps.subs(self.Phi, eps * self.c**2)

        series = sympy.series(expr_eps, eps, 0, order + 1).removeO()
        # Substitute back
        result = series.subs(eps, self.Phi / self.c**2)

        return ExpansionResult(
            original=expr,
            expanded=result,
            parameter=self.epsilon,
            order=order,
        )

    def coefficient(self, expr: sympy.Basic, power: int = 1) -> sympy.Basic:
        """Extract the coefficient of (Phi/c^2)^power from an expression."""
        eps = self._eps
        expr_eps = expr.subs(self.Phi / self.c**2, eps)
        if expr_eps.has(self.Phi):
            expr_eps = expr_eps.subs(self.Phi, eps * self.c**2)

        poly = sympy.Poly(sympy.series(expr_eps, eps, 0, power + 2).removeO(), eps)
        return poly.nth(power)

    def expand_and_collect(self, expr: sympy.Basic, order: int = 2) -> dict[int, sympy.Basic]:
        """Expand and return coefficients by order."""
        eps = self._eps
        expr_eps = expr.subs(self.Phi / self.c**2, eps)
        if expr_eps.has(self.Phi):
            expr_eps = expr_eps.subs(self.Phi, eps * self.c**2)

        series = sympy.series(expr_eps, eps, 0, order + 1).removeO()
        coeffs = {}
        for n in range(order + 1):
            coeff = series.coeff(eps, n)
            if coeff != 0:
                coeffs[n] = coeff
        return coeffs
