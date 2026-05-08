"""Radial coordinate transformations registered as derivations.

Implements Milestones 45-47 from the validation-hardening technical design.

For a static spherical metric ds² = -A(r) dt² + B(r) dr² + r² dΩ²
and a transformation r = f(R):
  - Temporal: A_new(R) = A(f(R)).  No Jacobian factor.
  - Radial:  B_new(R) = B(f(R)) · (df/dR)².
  - Log modes: a_new = a(f(R)), b_new = b(f(R)) + 2·ln(df/dR).
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy

from vacuumforge.core.dependency import DerivationRecord
from vacuumforge.metric.weak_field import WeakFieldMetric


@dataclass
class CoordinateChange:
    """A radial coordinate transformation r = f(R)."""

    old_coord: sympy.Symbol
    new_coord: sympy.Symbol
    transform: sympy.Basic   # f(R), expressed in terms of new_coord
    inverse: sympy.Basic | None = None  # R(r), if known
    derivation_id: str | None = None    # set on registration

    def jacobian(self) -> sympy.Basic:
        """Return df/dR."""
        return sympy.diff(self.transform, self.new_coord)

    def transform_scale_factor(self, scale_factor: sympy.Basic, kind: str) -> sympy.Basic:
        """Transform a temporal or radial scale factor under r = f(R).

        Temporal:  A_new(R) = A(f(R))
        Radial:    B_new(R) = B(f(R)) · (df/dR)²
        """
        fp = self.jacobian()
        substituted = self._substitute_old_coord(scale_factor)
        if kind == "temporal":
            return sympy.simplify(substituted)
        if kind == "radial":
            return sympy.simplify(substituted * fp**2)
        raise ValueError(f"Unknown scale factor kind: {kind!r}")

    def transform_log_modes(
        self,
        a: sympy.Basic,
        b: sympy.Basic,
    ) -> tuple[sympy.Basic, sympy.Basic]:
        """Transform log modes under r = f(R).

        a_new = a(f(R))
        b_new = b(f(R)) + 2·ln(f'(R))
        """
        fp = self.jacobian()
        a_new = self._substitute_old_coord(a)
        b_new = self._substitute_old_coord(b) + 2 * sympy.log(fp)
        return sympy.simplify(a_new), sympy.simplify(b_new)

    def transform_metric(self, metric: WeakFieldMetric) -> WeakFieldMetric:
        """Transform a weak-field metric into the new radial coordinate."""
        return WeakFieldMetric(
            A=self.transform_scale_factor(metric.A, "temporal"),
            B=self.transform_scale_factor(metric.B, "radial"),
            coordinates=f"{metric.coordinates}; {self.old_coord}={self.transform}",
            convention=metric.convention,
        )

    def register(self, ctx, derivation_id: str) -> None:
        """Record this coordinate change in a TheoryContext dependency graph."""
        self.derivation_id = derivation_id
        ctx.dependencies.record_derivation(
            DerivationRecord(
                id=derivation_id,
                operation="coordinate_change_chain_rule",
                inputs=[str(self.old_coord), str(self.new_coord), str(self.transform)],
                outputs=[derivation_id],
                details={
                    "jacobian": str(self.jacobian()),
                    "inverse_known": self.inverse is not None,
                },
            )
        )

    def _substitute_old_coord(self, expr: sympy.Basic) -> sympy.Basic:
        """Substitute old_coord -> transform in *expr*.

        Handles both plain Symbol substitution and Function(old_coord) patterns.
        For ``sympy.Function('A')(r)`` the plain ``.subs(r, f(R))`` correctly
        produces ``A(f(R))`` in sympy, so no special ``replace`` is needed for
        the standard Function-of-Symbol case.
        """
        return expr.subs(self.old_coord, self.transform)
