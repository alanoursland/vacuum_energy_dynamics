"""Weak-field metric construction and expansion."""

from __future__ import annotations

from dataclasses import dataclass

import sympy


@dataclass
class WeakFieldMetric:
    """Isotropic weak-field metric built from scale factors A, B.

    Convention: ds^2 = -A^2 c^2 dt^2 + B^2 (dx^2 + dy^2 + dz^2)
    So g_00 = -A^2, g_ij = B^2 delta_ij.
    """

    A: sympy.Basic
    B: sympy.Basic
    coordinates: str = "isotropic_static_spherical"
    convention: str = "signature_minus_plus_plus_plus"

    @property
    def g00(self) -> sympy.Basic:
        return -self.A**2

    @property
    def gij_factor(self) -> sympy.Basic:
        """Scalar factor for spatial metric: g_ij = gij_factor * delta_ij."""
        return self.B**2

    @property
    def neg_g00(self) -> sympy.Basic:
        """Returns -g00 = A^2, useful for PPN extraction."""
        return self.A**2
