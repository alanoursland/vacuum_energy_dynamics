"""Notation profiles and sign conventions (M29).

Makes sign and notation conventions explicit so that
potential convention mismatches are caught early.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy


@dataclass
class NotationProfile:
    """A named set of sign and notation conventions."""

    name: str
    description: str
    conventions: dict[str, str] = field(default_factory=dict)
    sign_rules: dict[str, int] = field(default_factory=dict)

    def potential_sign(self) -> int:
        """Return the sign convention for the gravitational potential.

        +1: U > 0 (PPN convention, potential is positive)
        -1: Phi < 0 in wells (framework convention)
        """
        return self.sign_rules.get("potential", -1)

    def convert_potential(
        self, expr: sympy.Basic, to_profile: NotationProfile,
    ) -> sympy.Basic:
        """Convert an expression from this profile's convention to another."""
        my_sign = self.potential_sign()
        their_sign = to_profile.potential_sign()
        if my_sign == their_sign:
            return expr
        # U = -Phi conversion
        Phi = sympy.Symbol("Phi")
        U = sympy.Symbol("U")
        if my_sign == -1 and their_sign == 1:
            return expr.subs(Phi, -U)
        elif my_sign == 1 and their_sign == -1:
            return expr.subs(U, -Phi)
        return expr


# --- Built-in profiles ---

FRAMEWORK_PROFILE = NotationProfile(
    name="framework",
    description="Framework convention: Phi < 0 in gravitational wells.",
    conventions={
        "potential": "Phi < 0 in wells",
        "metric_signature": "(-,+,+,+)",
        "expansion_parameter": "Phi/c^2",
    },
    sign_rules={"potential": -1},
)

PPN_PROFILE = NotationProfile(
    name="ppn",
    description="PPN convention: U > 0 (U = -Phi).",
    conventions={
        "potential": "U > 0",
        "metric_signature": "(-,+,+,+)",
        "expansion_parameter": "U/c^2",
    },
    sign_rules={"potential": 1},
)


BUILT_IN_PROFILES = {
    "framework": FRAMEWORK_PROFILE,
    "ppn": PPN_PROFILE,
}


def get_profile(name: str) -> NotationProfile:
    """Retrieve a built-in notation profile."""
    if name not in BUILT_IN_PROFILES:
        raise ValueError(f"Unknown profile: {name}. Available: {list(BUILT_IN_PROFILES.keys())}")
    return BUILT_IN_PROFILES[name]
