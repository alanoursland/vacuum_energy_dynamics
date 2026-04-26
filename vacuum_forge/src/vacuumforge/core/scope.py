"""Coordinate scope annotation (M30).

Tracks the coordinate/gauge scope of results so that
narrow-scope results are not over-claimed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class ScopeLevel(str, Enum):
    ALGEBRAIC = "algebraic_prototype"
    TWO_D_SLICE = "2d_time_space_slice"
    STATIC_ISOTROPIC = "static_spherical_isotropic"
    PPN_WEAK_FIELD = "ppn_weak_field"
    GENERAL_3_PLUS_1 = "general_3+1"


# Scope hierarchy: broader scopes contain narrower ones
_SCOPE_ORDER = [
    ScopeLevel.ALGEBRAIC,
    ScopeLevel.TWO_D_SLICE,
    ScopeLevel.STATIC_ISOTROPIC,
    ScopeLevel.PPN_WEAK_FIELD,
    ScopeLevel.GENERAL_3_PLUS_1,
]


@dataclass
class ScopeRecord:
    """Scope metadata for a result or expression."""

    scope: ScopeLevel
    description: str = ""
    warnings: list[str] = field(default_factory=list)


@dataclass
class ScopeMismatch:
    """Warning about scope mismatch."""

    result_scope: ScopeLevel
    requirement_scope: ScopeLevel
    message: str
    is_warning: bool = True


def scope_index(scope: ScopeLevel) -> int:
    """Return the breadth index of a scope (higher = broader)."""
    return _SCOPE_ORDER.index(scope)


def check_scope_compatibility(
    result_scope: ScopeLevel,
    requirement_scope: ScopeLevel,
) -> ScopeMismatch | None:
    """Check if a result's scope is sufficient for a requirement.

    Returns None if compatible, or a ScopeMismatch warning if the
    result's scope is narrower than the requirement's scope.
    """
    r_idx = scope_index(result_scope)
    req_idx = scope_index(requirement_scope)

    if r_idx < req_idx:
        return ScopeMismatch(
            result_scope=result_scope,
            requirement_scope=requirement_scope,
            message=(
                f"Result derived in {result_scope.value} scope "
                f"but requirement expects {requirement_scope.value}. "
                "This result may not generalize."
            ),
        )
    return None


class ScopeManager:
    """Manages scope annotations for a theory context."""

    def __init__(self) -> None:
        self._default: ScopeLevel = ScopeLevel.ALGEBRAIC
        self._result_scopes: dict[str, ScopeRecord] = {}

    @property
    def default(self) -> ScopeLevel:
        return self._default

    @default.setter
    def default(self, scope: ScopeLevel) -> None:
        self._default = scope

    def annotate(
        self,
        result_id: str,
        scope: ScopeLevel | None = None,
        description: str = "",
    ) -> ScopeRecord:
        """Annotate a result with scope metadata."""
        s = scope or self._default
        record = ScopeRecord(scope=s, description=description)
        self._result_scopes[result_id] = record
        return record

    def get(self, result_id: str) -> ScopeRecord | None:
        return self._result_scopes.get(result_id)

    def check(
        self,
        result_id: str,
        requirement_scope: ScopeLevel,
    ) -> ScopeMismatch | None:
        """Check if a result's scope matches a requirement scope."""
        record = self._result_scopes.get(result_id)
        if record is None:
            return ScopeMismatch(
                result_scope=self._default,
                requirement_scope=requirement_scope,
                message=(
                    f"Result '{result_id}' has no scope annotation "
                    f"(default: {self._default.value}). "
                    f"Requirement expects {requirement_scope.value}."
                ),
            )
        return check_scope_compatibility(record.scope, requirement_scope)

    def list(self) -> dict[str, ScopeRecord]:
        return dict(self._result_scopes)

    def summary(self) -> str:
        lines = [f"Scope (default: {self._default.value}):"]
        for rid, rec in self._result_scopes.items():
            lines.append(f"  {rid}: {rec.scope.value}")
        return "\n".join(lines)
