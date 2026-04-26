"""PPN parameter extraction from weak-field metrics.

Extracts gamma_v from spatial metric and beta from temporal metric:
  g_ij ~ (1 - 2*gamma_v*Phi/c^2) delta_ij
  g_00 ~ -(1 + 2*Phi/c^2 + 2*beta*Phi^2/c^4)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy

from vacuumforge.core.status import Exactness
from vacuumforge.metric.expansion import ExpansionEngine
from vacuumforge.metric.weak_field import WeakFieldMetric


@dataclass
class PPNResult:
    """Result of PPN parameter extraction."""

    parameter: str
    value: sympy.Basic
    exactness: Exactness
    dependencies: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)


def extract_gamma(
    metric: WeakFieldMetric,
    expansion: ExpansionEngine,
) -> PPNResult:
    """Extract gamma_v from the spatial metric factor.

    The spatial metric factor B^2 is expanded as:
      B^2 ~ 1 - 2*gamma_v*(Phi/c^2) + ...

    So gamma_v = -(first-order coefficient)/2.
    """
    gij = metric.gij_factor
    coeff1 = expansion.coefficient(gij, power=1)
    gamma_value = sympy.simplify(-coeff1 / 2)

    return PPNResult(
        parameter="gamma_v",
        value=gamma_value,
        exactness=Exactness.FIRST_ORDER,
        details={"gij_first_order_coeff": coeff1},
    )


def extract_beta(
    metric: WeakFieldMetric,
    expansion: ExpansionEngine,
) -> PPNResult:
    """Extract beta from the temporal metric component.

    We work with -g00 = A^2, expanded as:
      A^2 ~ 1 + 2*(Phi/c^2) + 2*beta*(Phi/c^2)^2 + ...

    So beta = (second-order coefficient)/2.
    """
    neg_g00 = metric.neg_g00
    coeff2 = expansion.coefficient(neg_g00, power=2)
    beta_value = sympy.simplify(coeff2 / 2)

    return PPNResult(
        parameter="beta",
        value=beta_value,
        exactness=Exactness.SECOND_ORDER,
        details={"neg_g00_second_order_coeff": coeff2},
    )


def extract_all(
    metric: WeakFieldMetric,
    expansion: ExpansionEngine,
) -> dict[str, PPNResult]:
    """Extract both gamma_v and beta."""
    return {
        "gamma_v": extract_gamma(metric, expansion),
        "beta": extract_beta(metric, expansion),
    }
