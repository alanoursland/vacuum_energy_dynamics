"""Source operators for candidate vacuum structures."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

import sympy


@dataclass
class SourceOperator:
    """Defines how a source changes pre-mode variables.

    Exchange and creation are represented as different source operators.
    The deltas dict maps each pre-mode variable to its perturbation.

    Example exchange operator (antisymmetric):
        deltas = {q_t: S, q_x: -S}
        source_symbols = [S]

    Example creation operator (symmetric):
        deltas = {q_t: C, q_x: C}
        source_symbols = [C]
    """

    id: str
    kind: Literal["exchange", "creation", "mixed", "unknown"]
    deltas: dict[sympy.Symbol, sympy.Expr]
    source_symbols: list[sympy.Symbol] = field(default_factory=list)
    constraints: list[sympy.Basic] = field(default_factory=list)
    description: str | None = None
    status: str = "candidate"
