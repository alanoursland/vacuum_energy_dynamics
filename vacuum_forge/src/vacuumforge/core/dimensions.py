"""Lightweight dimensional validation (M28).

Provides dimension tags, algebra, and checks for expressions
commonly used in the vacuum field-equation framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

import sympy


class Dimension(str, Enum):
    DIMENSIONLESS = "dimensionless"
    LENGTH = "length"
    TIME = "time"
    MASS = "mass"
    VELOCITY = "velocity"
    ACCELERATION = "acceleration"
    POTENTIAL = "potential"  # velocity^2
    ENERGY = "energy"
    UNKNOWN = "unknown"


# Standard dimension assignments for equal-response symbols
STANDARD_DIMENSIONS: dict[str, Dimension] = {
    "c": Dimension.VELOCITY,
    "G": Dimension.UNKNOWN,  # G has composite dimensions
    "M": Dimension.MASS,
    "r": Dimension.LENGTH,
    "Phi": Dimension.POTENTIAL,
    "A": Dimension.DIMENSIONLESS,
    "B": Dimension.DIMENSIONLESS,
    "a": Dimension.DIMENSIONLESS,
    "b": Dimension.DIMENSIONLESS,
    "kappa": Dimension.DIMENSIONLESS,
    "sigma": Dimension.DIMENSIONLESS,
    "mu": Dimension.DIMENSIONLESS,
    "gamma_v": Dimension.DIMENSIONLESS,
    "beta": Dimension.DIMENSIONLESS,
    "C_kappa": Dimension.UNKNOWN,
    "C_sigma": Dimension.UNKNOWN,
}


@dataclass
class DimensionCheckResult:
    """Result of a dimensional check."""

    expression: sympy.Basic
    dimension: Dimension
    is_valid: bool
    message: str
    notes: list[str] = field(default_factory=list)


class DimensionChecker:
    """Checks dimensional consistency of expressions."""

    def __init__(self) -> None:
        self._dimensions: dict[str, Dimension] = dict(STANDARD_DIMENSIONS)

    def set_dimension(self, symbol_name: str, dim: Dimension) -> None:
        self._dimensions[symbol_name] = dim

    def get_dimension(self, symbol_name: str) -> Dimension:
        return self._dimensions.get(symbol_name, Dimension.UNKNOWN)

    def check(self, expr: sympy.Basic) -> DimensionCheckResult:
        """Check if an expression is dimensionless.

        This is a lightweight check — it examines known ratios
        like Phi/c^2 rather than doing full dimensional algebra.
        """
        notes = []

        # Check for known dimensionless combinations
        if self._is_known_dimensionless(expr):
            return DimensionCheckResult(
                expr, Dimension.DIMENSIONLESS, True,
                "Expression is dimensionless.",
            )

        # Check exp/log arguments are dimensionless
        for func in expr.atoms(sympy.exp, sympy.log):
            arg = func.args[0]
            if not self._is_known_dimensionless(arg):
                notes.append(f"Argument of {func.func}: {arg}")
                if self._could_be_dimensionless(arg):
                    notes.append("  -> appears dimensionless by known ratios")
                else:
                    return DimensionCheckResult(
                        expr, Dimension.UNKNOWN, False,
                        f"Cannot verify argument of {func.func} is dimensionless.",
                        notes,
                    )

        # If all function arguments check out, expression is likely valid
        if notes:
            return DimensionCheckResult(
                expr, Dimension.DIMENSIONLESS, True,
                "Function arguments are dimensionless.", notes,
            )

        return DimensionCheckResult(
            expr, Dimension.UNKNOWN, True,
            "No dimensional inconsistencies detected (limited check).",
            notes,
        )

    def check_ratio(
        self,
        numerator_sym: str,
        denominator_sym: str,
    ) -> DimensionCheckResult:
        """Check if a ratio of two named symbols is dimensionless."""
        n_dim = self.get_dimension(numerator_sym)
        d_dim = self.get_dimension(denominator_sym)

        if n_dim == d_dim and n_dim != Dimension.UNKNOWN:
            return DimensionCheckResult(
                sympy.Symbol(numerator_sym) / sympy.Symbol(denominator_sym),
                Dimension.DIMENSIONLESS, True,
                f"{numerator_sym}/{denominator_sym} is dimensionless (same dimension: {n_dim.value}).",
            )

        # Known valid ratios
        valid_ratios = {
            ("Phi", "c"): "Phi/c^2 is the weak-field expansion parameter",
        }
        key = (numerator_sym, denominator_sym)
        if key in valid_ratios:
            return DimensionCheckResult(
                sympy.Symbol(numerator_sym) / sympy.Symbol(denominator_sym),
                Dimension.DIMENSIONLESS, True,
                valid_ratios[key],
            )

        return DimensionCheckResult(
            sympy.Symbol(numerator_sym) / sympy.Symbol(denominator_sym),
            Dimension.UNKNOWN, False,
            f"Cannot verify {numerator_sym}/{denominator_sym} is dimensionless.",
        )

    def _is_known_dimensionless(self, expr: sympy.Basic) -> bool:
        """Check if expression is a known dimensionless form."""
        free = expr.free_symbols
        names = {s.name for s in free}

        # Pure numeric
        if not free:
            return True

        # All symbols dimensionless
        if all(
            self._dimensions.get(n) == Dimension.DIMENSIONLESS
            for n in names
        ):
            return True

        return False

    def _could_be_dimensionless(self, expr: sympy.Basic) -> bool:
        """Heuristic: check if expression looks like Phi/c^2 or similar."""
        free = expr.free_symbols
        names = {s.name for s in free}

        # Phi/c^2 pattern
        if names <= {"Phi", "c"}:
            return True

        # All dimensionless symbols
        if all(
            self._dimensions.get(n, Dimension.UNKNOWN) == Dimension.DIMENSIONLESS
            for n in names
        ):
            return True

        return False
