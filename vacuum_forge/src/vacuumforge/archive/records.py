"""Archive record types."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy

from vacuumforge.core.status import Status
from vacuumforge.governance.kinds import RecordKind


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
    record_kind: RecordKind = RecordKind.DERIVATION
    scope: str | None = None
    claim_tier: str | None = None
    result_type: str | None = None
    superseded_by: str | None = None
    is_placeholder: bool = False


@dataclass
class DependencyDeclaration:
    dependency_id: str
    upstream_script_id: str
    upstream_derivation_id: str
    expected_output: sympy.Basic | None = None
    expected_status: str | None = None
    expected_record_kind: RecordKind | None = None
    allow_superseded: bool = False
    declared_at: str = ""


@dataclass
class DependencyCheckResult:
    dependency: DependencyDeclaration
    status: str
    message: str
    expected_output: sympy.Basic | None = None
    actual_output: sympy.Basic | None = None
    residual: sympy.Basic | None = None
