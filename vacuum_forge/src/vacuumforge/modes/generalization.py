"""3+1 generalization foundations (M34).

Prepare for higher-dimensional trace and shear decompositions
with one time variable and multiple spatial variables.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy


@dataclass
class GeneralModeDecomposition:
    """Mode decomposition for an arbitrary number of spatial log variables."""

    time_log: sympy.Symbol
    spatial_logs: list[sympy.Symbol]
    trace: sympy.Basic
    trace_free: list[sympy.Basic]
    n_spatial: int = 0
    is_experimental: bool = True
    warnings: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.n_spatial = len(self.spatial_logs)
        if self.n_spatial > 1:
            self.warnings.append(
                "3+1 mode decomposition is experimental. "
                "Results should be verified independently."
            )


def decompose_general(
    time_log: sympy.Symbol,
    spatial_logs: list[sympy.Symbol],
) -> GeneralModeDecomposition:
    """Compute trace and trace-free decomposition for general variable lists.

    For N spatial log variables b_1, ..., b_N and one time log a:
    - Total spatial trace: T = sum(b_i) / N
    - Total trace including time: T_full = (a + sum(b_i)) / (N+1)
    - Trace-free parts: b_i - T for each spatial b_i

    For the standard 2D case (a, b), this reduces to:
    - T = b
    - kappa = (a + b) / 2
    - sigma = (a - b) / 2
    """
    n = len(spatial_logs)
    spatial_sum = sum(spatial_logs)

    # Total trace-like mode (generalization of kappa)
    # In 2D: kappa = (a + b) / 2
    # In general: kappa_gen = (a + sum(b_i)) / (n + 1)
    trace = (time_log + spatial_sum) / (n + 1)

    # Trace-free parts
    spatial_mean = spatial_sum / n if n > 0 else sympy.Integer(0)
    trace_free = [b - spatial_mean for b in spatial_logs]

    return GeneralModeDecomposition(
        time_log=time_log,
        spatial_logs=spatial_logs,
        trace=trace,
        trace_free=trace_free,
    )


def decompose_2d(
    a: sympy.Symbol, b: sympy.Symbol,
) -> GeneralModeDecomposition:
    """Standard 2D decomposition for backward compatibility.

    Returns kappa = (a+b)/2 as trace and sigma = (a-b)/2 as trace-free.
    """
    kappa = (a + b) / 2
    sigma_val = (a - b) / 2

    result = GeneralModeDecomposition(
        time_log=a,
        spatial_logs=[b],
        trace=kappa,
        trace_free=[sigma_val],
    )
    result.is_experimental = False
    result.warnings = []
    return result


def decompose_3plus1(
    a: sympy.Symbol,
    b1: sympy.Symbol,
    b2: sympy.Symbol,
    b3: sympy.Symbol,
) -> GeneralModeDecomposition:
    """3+1 decomposition with one time and three spatial log variables.

    Trace: kappa_gen = (a + b1 + b2 + b3) / 4
    Trace-free spatial: b_i - (b1 + b2 + b3)/3 for each i
    """
    return decompose_general(a, [b1, b2, b3])
