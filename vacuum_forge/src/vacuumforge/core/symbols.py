"""Symbolic variable registry for VacuumForge."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy


@dataclass
class SymbolRecord:
    """Record for a registered symbolic variable."""

    name: str
    sympy_object: sympy.Basic
    kind: str
    description: str | None = None
    assumptions: dict[str, Any] = field(default_factory=dict)
    dimensions: str | None = None
    status: str = "definition"
    namespace: str | None = None

    @property
    def full_name(self) -> str:
        if self.namespace:
            return f"{self.namespace}.{self.name}"
        return self.name


class SymbolRegistry:
    """Manages all named symbols, functions, and expressions."""

    def __init__(self) -> None:
        self._records: dict[str, SymbolRecord] = {}

    def define_symbol(
        self,
        name: str,
        kind: str = "symbol",
        description: str | None = None,
        namespace: str | None = None,
        dimensions: str | None = None,
        status: str = "definition",
        **sympy_assumptions: Any,
    ) -> sympy.Symbol:
        sym = sympy.Symbol(name, **sympy_assumptions)
        record = SymbolRecord(
            name=name,
            sympy_object=sym,
            kind=kind,
            description=description,
            assumptions=sympy_assumptions,
            dimensions=dimensions,
            status=status,
            namespace=namespace,
        )
        self._store(record)
        return sym

    def define_constant(
        self,
        name: str,
        description: str | None = None,
        dimensions: str | None = None,
        **sympy_assumptions: Any,
    ) -> sympy.Symbol:
        return self.define_symbol(
            name,
            kind="constant",
            description=description,
            namespace="constants",
            dimensions=dimensions,
            **sympy_assumptions,
        )

    def define_coordinate(
        self,
        name: str,
        description: str | None = None,
        dimensions: str | None = None,
        **sympy_assumptions: Any,
    ) -> sympy.Symbol:
        return self.define_symbol(
            name,
            kind="coordinate",
            description=description,
            namespace="coordinates",
            dimensions=dimensions,
            **sympy_assumptions,
        )

    def define_coefficient(
        self,
        name: str,
        description: str | None = None,
        **sympy_assumptions: Any,
    ) -> sympy.Symbol:
        return self.define_symbol(
            name,
            kind="coefficient",
            description=description,
            namespace="coefficients",
            **sympy_assumptions,
        )

    def define_function(
        self,
        name: str,
        args: list[sympy.Basic] | None = None,
        description: str | None = None,
        namespace: str | None = None,
        dimensions: str | None = None,
        status: str = "definition",
    ) -> sympy.Basic:
        """Define a symbolic function, optionally applied to arguments."""
        func_class = sympy.Function(name)
        if args:
            applied = func_class(*args)
        else:
            applied = func_class
        record = SymbolRecord(
            name=name,
            sympy_object=applied,
            kind="function",
            description=description,
            dimensions=dimensions,
            status=status,
            namespace=namespace or "functions",
        )
        self._store(record)
        return applied

    def define_source(
        self,
        name: str,
        description: str | None = None,
        **sympy_assumptions: Any,
    ) -> sympy.Symbol:
        return self.define_symbol(
            name,
            kind="source",
            description=description,
            namespace="sources",
            **sympy_assumptions,
        )

    def _store(self, record: SymbolRecord) -> None:
        self._records[record.name] = record

    def get(self, name: str) -> sympy.Basic:
        """Retrieve the SymPy object by name."""
        return self._records[name].sympy_object

    def record(self, name: str) -> SymbolRecord:
        """Retrieve the full record by name."""
        return self._records[name]

    def has(self, name: str) -> bool:
        return name in self._records

    def list(self, kind: str | None = None) -> list[SymbolRecord]:
        """List records, optionally filtered by kind."""
        if kind is None:
            return list(self._records.values())
        return [r for r in self._records.values() if r.kind == kind]

    def names(self, kind: str | None = None) -> list[str]:
        return [r.name for r in self.list(kind)]

    def summary(self) -> str:
        lines = ["Symbol Registry:"]
        for kind in ["constant", "coordinate", "coefficient", "function", "source", "symbol"]:
            records = self.list(kind)
            if records:
                lines.append(f"  {kind}s:")
                for r in records:
                    desc = f" — {r.description}" if r.description else ""
                    lines.append(f"    {r.name}{desc}")
        return "\n".join(lines)
