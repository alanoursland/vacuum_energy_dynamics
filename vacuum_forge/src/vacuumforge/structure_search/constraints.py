"""Constraint solving for structure search.

Finds coefficient conditions under which J_kappa = 0 for exchange
or J_kappa != 0 for creation.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy

from vacuumforge.core.simplify import is_zero


@dataclass
class ConstraintResult:
    """Result of solving for trace-free or traceful conditions."""

    target: str  # "trace_free_exchange" or "traceful_creation"
    solvable: bool
    conditions: list[sympy.Basic] = field(default_factory=list)
    free_symbols: list[sympy.Symbol] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def solve_trace_free_conditions(
    J_kappa: sympy.Expr,
    source_symbols: list[sympy.Symbol],
    coefficient_symbols: list[sympy.Symbol] | None = None,
) -> ConstraintResult:
    """Find conditions on coefficients such that J_kappa = 0 for all source values.

    Algorithm:
    1. Expand J_kappa.
    2. Collect by source symbols.
    3. Extract coefficient of each independent source symbol.
    4. Set each coefficient to zero.
    5. Solve for structure coefficients.
    """
    J_kappa = sympy.expand(J_kappa)

    # If already zero, no conditions needed
    if is_zero(J_kappa) is True:
        return ConstraintResult(
            target="trace_free_exchange",
            solvable=True,
            notes=["J_kappa is identically zero."],
        )

    # Collect coefficients of source symbols
    equations = []
    if source_symbols:
        for s in source_symbols:
            coeff = J_kappa.coeff(s)
            if coeff != 0:
                equations.append(sympy.Eq(coeff, 0))

        # Also check constant term (term without any source symbol)
        constant = J_kappa
        for s in source_symbols:
            constant = constant.coeff(s, 0)
        if constant != 0 and constant != J_kappa:
            equations.append(sympy.Eq(constant, 0))
    else:
        # No source symbols — J_kappa itself must be zero
        equations.append(sympy.Eq(J_kappa, 0))

    if not equations:
        return ConstraintResult(
            target="trace_free_exchange",
            solvable=True,
            notes=["All source coefficients in J_kappa are zero."],
        )

    # Determine what to solve for
    if coefficient_symbols is None:
        # Find all free symbols that aren't source symbols
        all_free = set()
        for eq in equations:
            all_free.update(eq.free_symbols)
        coefficient_symbols = sorted(
            all_free - set(source_symbols),
            key=lambda s: str(s),
        )

    if not coefficient_symbols:
        # Equations must hold as identities — check if they do
        all_hold = all(
            is_zero(eq.lhs - eq.rhs) is True
            for eq in equations
        )
        if all_hold:
            return ConstraintResult(
                target="trace_free_exchange",
                solvable=True,
                notes=["Trace-free condition holds identically."],
            )
        return ConstraintResult(
            target="trace_free_exchange",
            solvable=False,
            conditions=equations,
            notes=["Trace-free condition requires constraints that cannot be resolved."],
        )

    # Try to solve
    try:
        solutions = sympy.solve(
            [eq.lhs - eq.rhs for eq in equations],
            coefficient_symbols,
            dict=True,
        )
    except Exception:
        return ConstraintResult(
            target="trace_free_exchange",
            solvable=False,
            conditions=equations,
            free_symbols=coefficient_symbols,
            notes=["SymPy could not solve the constraint equations."],
        )

    if solutions:
        # Convert solutions back to conditions
        conditions = []
        for sol in solutions:
            for var, val in sol.items():
                conditions.append(sympy.Eq(var, val))
        return ConstraintResult(
            target="trace_free_exchange",
            solvable=True,
            conditions=conditions,
            free_symbols=coefficient_symbols,
            notes=[f"Trace-free exchange requires: {conditions}"],
        )

    # No solutions found — the equations are unsatisfiable
    return ConstraintResult(
        target="trace_free_exchange",
        solvable=False,
        conditions=equations,
        free_symbols=coefficient_symbols,
        notes=["No coefficient values satisfy the trace-free condition."],
    )


def check_traceful_condition(
    J_kappa: sympy.Expr,
    source_symbols: list[sympy.Symbol],
) -> ConstraintResult:
    """Check whether J_kappa is generically nonzero (traceful).

    For creation sources, the desired result is J_kappa != 0.
    """
    J_kappa = sympy.expand(J_kappa)

    zero_check = is_zero(J_kappa)

    if zero_check is True:
        return ConstraintResult(
            target="traceful_creation",
            solvable=False,
            notes=["J_kappa is zero — creation is not traceful. "
                   "Creation cannot be distinguished from exchange."],
        )

    if zero_check is False:
        return ConstraintResult(
            target="traceful_creation",
            solvable=True,
            notes=["J_kappa is generically nonzero — creation is traceful."],
        )

    # Undetermined — check if nonzero for generic source values
    if source_symbols:
        test_subs = {s: sympy.Rational(3, 2) for s in source_symbols}
        test_val = sympy.simplify(J_kappa.subs(test_subs))
        if test_val != 0:
            return ConstraintResult(
                target="traceful_creation",
                solvable=True,
                notes=["J_kappa is nonzero for generic source values — creation is traceful."],
            )

    return ConstraintResult(
        target="traceful_creation",
        solvable=False,
        notes=["Cannot determine whether J_kappa is generically nonzero."],
    )
