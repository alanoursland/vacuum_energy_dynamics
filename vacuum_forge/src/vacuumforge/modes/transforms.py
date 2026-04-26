"""Scale-factor, logarithmic, and mode transformations.

Supports conversion between:
  (A, B)  <->  (a, b)  <->  (kappa, sigma)

where a = ln A, b = ln B, kappa = (a+b)/2, sigma = (a-b)/2.
"""

from __future__ import annotations

import sympy

from vacuumforge.core.simplify import vf_simplify


class TransformEngine:
    """Transforms expressions between scale, log, and mode representations."""

    def __init__(
        self,
        A: sympy.Basic,
        B: sympy.Basic,
        a: sympy.Basic,
        b: sympy.Basic,
        kappa: sympy.Basic,
        sigma: sympy.Basic,
    ) -> None:
        self.A = A
        self.B = B
        self.a = a
        self.b = b
        self.kappa = kappa
        self.sigma = sigma

    def to_log(self, expr: sympy.Basic) -> sympy.Basic:
        """Rewrite scale factors A, B in terms of log variables a, b."""
        result = expr.subs({
            self.A: sympy.exp(self.a),
            self.B: sympy.exp(self.b),
        })
        return vf_simplify(result)

    def to_scale(self, expr: sympy.Basic) -> sympy.Basic:
        """Rewrite log variables a, b in terms of scale factors A, B."""
        result = expr.subs({
            self.a: sympy.log(self.A),
            self.b: sympy.log(self.B),
        })
        return vf_simplify(result)

    def to_modes(self, expr: sympy.Basic) -> sympy.Basic:
        """Rewrite in terms of mode variables kappa, sigma."""
        # First ensure we're in log variables
        result = expr.subs({
            self.A: sympy.exp(self.a),
            self.B: sympy.exp(self.b),
        })
        # Then substitute log variables in terms of modes
        result = result.subs({
            self.a: self.kappa + self.sigma,
            self.b: self.kappa - self.sigma,
        })
        return vf_simplify(result)

    def from_modes(self, expr: sympy.Basic) -> sympy.Basic:
        """Rewrite mode variables kappa, sigma in terms of log variables a, b."""
        result = expr.subs({
            self.kappa: (self.a + self.b) / 2,
            self.sigma: (self.a - self.b) / 2,
        })
        return vf_simplify(result)

    def modes_to_scale(self, expr: sympy.Basic) -> sympy.Basic:
        """Rewrite mode variables directly in terms of scale factors A, B."""
        result = expr.subs({
            self.kappa: sympy.log(self.A * self.B) / 2,
            self.sigma: sympy.log(self.A / self.B) / 2,
        })
        return vf_simplify(result)

    def scale_to_modes(self, expr: sympy.Basic) -> sympy.Basic:
        """Rewrite scale factors directly in terms of modes."""
        result = expr.subs({
            self.A: sympy.exp(self.kappa + self.sigma),
            self.B: sympy.exp(self.kappa - self.sigma),
        })
        return vf_simplify(result)
