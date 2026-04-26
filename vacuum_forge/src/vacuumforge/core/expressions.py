"""Named expression store for VacuumForge."""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy


@dataclass
class ExpressionRecord:
    """A named symbolic expression with metadata."""

    id: str
    expr: sympy.Basic
    description: str | None = None
    status: str = "definition"
    dependencies: list[str] = field(default_factory=list)
    scope: str | None = None
    exactness: str = "exact"


class ExpressionStore:
    """Stores named symbolic expressions."""

    def __init__(self) -> None:
        self._records: dict[str, ExpressionRecord] = {}

    def add(
        self,
        id: str,
        expr: sympy.Basic,
        description: str | None = None,
        status: str = "definition",
        dependencies: list[str] | None = None,
        scope: str | None = None,
        exactness: str = "exact",
    ) -> ExpressionRecord:
        record = ExpressionRecord(
            id=id,
            expr=expr,
            description=description,
            status=status,
            dependencies=dependencies or [],
            scope=scope,
            exactness=exactness,
        )
        self._records[id] = record
        return record

    def get(self, id: str) -> ExpressionRecord:
        return self._records[id]

    def expr(self, id: str) -> sympy.Basic:
        return self._records[id].expr

    def has(self, id: str) -> bool:
        return id in self._records

    def remove(self, id: str) -> None:
        self._records.pop(id, None)

    def list(self) -> list[ExpressionRecord]:
        return list(self._records.values())

    def ids(self) -> list[str]:
        return list(self._records.keys())

    def summary(self) -> str:
        lines = ["Expressions:"]
        for record in self._records.values():
            desc = f" — {record.description}" if record.description else ""
            lines.append(f"  [{record.id}] {sympy.pretty(record.expr)}{desc}")
        return "\n".join(lines)
