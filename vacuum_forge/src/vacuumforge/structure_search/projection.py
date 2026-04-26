"""Projection maps from pre-mode variables to metric scale variables."""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy


@dataclass
class ProjectionMap:
    """Defines how pre-mode variables determine metric scale variables.

    Maps pre-mode variables q_i to log scale variables (a, b) via:
        a = f_a(q_1, ..., q_n)
        b = f_b(q_1, ..., q_n)

    Supports both linear and nonlinear projections.
    """

    id: str
    variables: list[sympy.Symbol]
    a_expr: sympy.Expr
    b_expr: sympy.Expr
    description: str | None = None

    def jacobian(self) -> sympy.Matrix:
        """Compute the Jacobian matrix of the projection.

        Returns a 2xN matrix:
            [[da/dq_1, ..., da/dq_n],
             [db/dq_1, ..., db/dq_n]]
        """
        rows = []
        for expr in [self.a_expr, self.b_expr]:
            rows.append([sympy.diff(expr, q) for q in self.variables])
        return sympy.Matrix(rows)

    def is_linear(self) -> bool:
        """Check if the projection is linear in the variables."""
        for expr in [self.a_expr, self.b_expr]:
            for q in self.variables:
                # Second derivatives should be zero for linearity
                if sympy.diff(expr, q, q) != 0:
                    return False
                # Cross derivatives should be zero for linearity
                for q2 in self.variables:
                    if q2 != q and sympy.diff(expr, q, q2) != 0:
                        return False
        return True

    def induced_source(
        self,
        deltas: dict[sympy.Symbol, sympy.Expr],
    ) -> tuple[sympy.Expr, sympy.Expr]:
        """Compute induced metric sources (J_a, J_b) from pre-mode deltas.

        For a source operator with deltas {q_i: delta_q_i}, computes:
            J_a = sum_i (da/dq_i) * delta_q_i
            J_b = sum_i (db/dq_i) * delta_q_i

        Returns (J_a, J_b).
        """
        jac = self.jacobian()
        delta_vec = sympy.Matrix([deltas.get(q, sympy.Integer(0)) for q in self.variables])
        result = jac * delta_vec
        J_a = sympy.simplify(result[0])
        J_b = sympy.simplify(result[1])
        return J_a, J_b
