"""Euler-Lagrange field support (M33).

Extends energy analysis from algebraic mode models to
simple field models depending on one coordinate.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy


@dataclass
class EulerLagrangeResult:
    """Result of deriving Euler-Lagrange equations."""

    density: sympy.Basic
    coordinate: sympy.Basic
    fields: list[sympy.Basic]
    equations: dict[sympy.Basic, sympy.Basic]
    boundary_conditions: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def euler_lagrange_1d(
    density: sympy.Basic,
    fields: list[sympy.Function],
    coordinate: sympy.Symbol,
    boundary_conditions: list[str] | None = None,
) -> EulerLagrangeResult:
    """Derive Euler-Lagrange equations for fields depending on one coordinate.

    For a density L(f, f', r) with field f(r), the equation is:
        dL/df - d/dr(dL/df') = 0

    Parameters
    ----------
    density : sympy.Basic
        The Lagrangian density as a SymPy expression.
    fields : list
        Applied functions like [kappa(r), sigma(r)].
    coordinate : sympy.Symbol
        The independent coordinate (e.g. r).
    boundary_conditions : list, optional
        String descriptions of boundary conditions.
    """
    equations = {}
    for f_applied in fields:
        # f_applied is e.g. kappa(r)
        f_prime = sympy.diff(f_applied, coordinate)

        # dL/df
        dL_df = sympy.diff(density, f_applied)

        # dL/df' and d/dr(dL/df')
        dL_dfp = sympy.diff(density, f_prime)
        d_dr_dL_dfp = sympy.diff(dL_dfp, coordinate)

        # Euler-Lagrange equation: dL/df - d/dr(dL/df') = 0
        el_eq = sympy.simplify(dL_df - d_dr_dL_dfp)
        equations[f_applied] = el_eq

    return EulerLagrangeResult(
        density=density,
        coordinate=coordinate,
        fields=list(fields),
        equations=equations,
        boundary_conditions=boundary_conditions or [],
    )


def radial_mode_density(
    K_kappa: sympy.Basic,
    K_sigma: sympy.Basic,
    C_kappa: sympy.Basic,
    C_sigma: sympy.Basic,
    J_kappa: sympy.Basic,
    J_sigma: sympy.Basic,
    kappa_r: sympy.Basic,
    sigma_r: sympy.Basic,
    r: sympy.Symbol,
) -> sympy.Basic:
    """Build a standard radial mode field density.

    L = K_kappa * (kappa')^2 + K_sigma * (sigma')^2
        + C_kappa * kappa^2 + C_sigma * sigma^2
        - J_kappa * kappa - J_sigma * sigma
    """
    kappa_prime = sympy.diff(kappa_r, r)
    sigma_prime = sympy.diff(sigma_r, r)

    return (K_kappa * kappa_prime**2 + K_sigma * sigma_prime**2
            + C_kappa * kappa_r**2 + C_sigma * sigma_r**2
            - J_kappa * kappa_r - J_sigma * sigma_r)
