"""Pre-mode variable definitions for candidate vacuum structures."""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy


@dataclass
class PreModeVariable:
    """A pre-mode degree of freedom in a candidate vacuum structure.

    Pre-mode variables are the internal variables of a candidate structure.
    They are not necessarily a, b, kappa, or sigma. They become metric
    variables only after projection.
    """

    symbol: sympy.Symbol
    description: str | None = None
    assumptions: dict[str, bool] = field(default_factory=dict)

    @staticmethod
    def create(name: str, description: str | None = None, **kwargs) -> PreModeVariable:
        """Create a pre-mode variable with SymPy assumptions."""
        sym = sympy.Symbol(name, **kwargs)
        return PreModeVariable(symbol=sym, description=description, assumptions=kwargs)
