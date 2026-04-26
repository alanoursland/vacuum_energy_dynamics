"""Theory ledger for classifying statements by status."""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy

from vacuumforge.core.status import Status


@dataclass
class LedgerEntry:
    """A theory statement with its scientific status."""

    id: str
    statement: str
    status: Status
    expression: sympy.Basic | None = None
    dependencies: list[str] = field(default_factory=list)
    notes: str | None = None


class TheoryLedger:
    """Classifies theory statements as definitions, postulates, assumptions, etc."""

    def __init__(self) -> None:
        self._entries: dict[str, LedgerEntry] = {}

    def add(
        self,
        id: str,
        statement: str,
        status: Status,
        expression: sympy.Basic | None = None,
        dependencies: list[str] | None = None,
        notes: str | None = None,
    ) -> LedgerEntry:
        entry = LedgerEntry(
            id=id,
            statement=statement,
            status=status,
            expression=expression,
            dependencies=dependencies or [],
            notes=notes,
        )
        self._entries[id] = entry
        return entry

    def add_definition(self, id: str, statement: str, **kwargs) -> LedgerEntry:
        return self.add(id, statement, Status.DEFINITION, **kwargs)

    def add_postulate(self, id: str, statement: str, **kwargs) -> LedgerEntry:
        return self.add(id, statement, Status.POSTULATE, **kwargs)

    def add_candidate_postulate(self, id: str, statement: str, **kwargs) -> LedgerEntry:
        return self.add(id, statement, Status.CANDIDATE_POSTULATE, **kwargs)

    def add_assumption(self, id: str, statement: str, **kwargs) -> LedgerEntry:
        return self.add(id, statement, Status.ASSUMPTION, **kwargs)

    def add_target(self, id: str, statement: str, **kwargs) -> LedgerEntry:
        return self.add(id, statement, Status.TARGET, **kwargs)

    def add_derived(self, id: str, statement: str, **kwargs) -> LedgerEntry:
        return self.add(id, statement, Status.DERIVED, **kwargs)

    def add_open_question(self, id: str, statement: str, **kwargs) -> LedgerEntry:
        return self.add(id, statement, Status.OPEN_QUESTION, **kwargs)

    def get(self, id: str) -> LedgerEntry:
        return self._entries[id]

    def has(self, id: str) -> bool:
        return id in self._entries

    def update_status(self, id: str, new_status: Status, notes: str | None = None) -> None:
        entry = self._entries[id]
        entry.status = new_status
        if notes:
            entry.notes = notes

    def by_status(self, status: Status) -> list[LedgerEntry]:
        return [e for e in self._entries.values() if e.status == status]

    def all(self) -> list[LedgerEntry]:
        return list(self._entries.values())

    def summary(self) -> str:
        lines = ["Theory Ledger:"]
        for status in Status:
            entries = self.by_status(status)
            if entries:
                lines.append(f"  {status.value}:")
                for e in entries:
                    lines.append(f"    [{e.id}] {e.statement}")
        return "\n".join(lines)
