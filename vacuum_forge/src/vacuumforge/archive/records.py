"""Archive record types."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy

from vacuumforge.core.status import Status


@dataclass
class DerivationRecord:
    derivation_id: str
    inputs: list[sympy.Basic]
    output: sympy.Basic
    method: str
    status: Status
    metadata: dict[str, Any] = field(default_factory=dict)
    recorded_at: str = ""
    vacuumforge_version: str = "0.1.0"


@dataclass
class DependencyDeclaration:
    dependency_id: str
    upstream_script_id: str
    upstream_derivation_id: str
    expected_output: sympy.Basic | None = None
    declared_at: str = ""


@dataclass
class DependencyCheckResult:
    dependency: DependencyDeclaration
    status: str
    message: str

