"""Dependency tracking and derivation records for VacuumForge."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import networkx as nx


@dataclass
class DerivationRecord:
    """Records a derivation step with its inputs and outputs."""

    id: str
    operation: str
    inputs: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)


class DependencyGraph:
    """Tracks dependency relationships between theory objects."""

    def __init__(self) -> None:
        self._graph = nx.DiGraph()
        self._derivations: dict[str, DerivationRecord] = {}

    def add_node(self, id: str, kind: str, status: str = "definition", **data: Any) -> None:
        self._graph.add_node(id, kind=kind, status=status, **data)

    def add_dependency(self, target: str, depends_on: str, relation: str = "depends_on") -> None:
        """Record that `target` depends on `depends_on`."""
        # Ensure nodes exist
        if target not in self._graph:
            self._graph.add_node(target)
        if depends_on not in self._graph:
            self._graph.add_node(depends_on)
        self._graph.add_edge(depends_on, target, relation=relation)

    def record_derivation(self, record: DerivationRecord) -> None:
        """Record a derivation step and wire up dependencies."""
        self._derivations[record.id] = record
        self.add_node(record.id, kind="derivation", operation=record.operation)
        for inp in record.inputs:
            self.add_dependency(record.id, inp, relation="input")
        for assumption in record.assumptions:
            self.add_dependency(record.id, assumption, relation="assumes")
        for out in record.outputs:
            self.add_dependency(out, record.id, relation="derived_by")

    def of(self, id: str) -> list[str]:
        """Return direct dependencies of a node."""
        if id not in self._graph:
            return []
        return list(self._graph.predecessors(id))

    def tree(self, id: str) -> list[str]:
        """Return all transitive dependencies of a node."""
        if id not in self._graph:
            return []
        return list(nx.ancestors(self._graph, id))

    def dependents_of(self, id: str) -> list[str]:
        """Return everything that depends on a given node."""
        if id not in self._graph:
            return []
        return list(nx.descendants(self._graph, id))

    def uses_assumption(self, result_id: str, assumption_id: str) -> bool:
        """Check if a result transitively depends on a given assumption."""
        return assumption_id in self.tree(result_id)

    def get_derivation(self, id: str) -> DerivationRecord | None:
        return self._derivations.get(id)

    def node_data(self, id: str) -> dict[str, Any]:
        if id not in self._graph:
            return {}
        return dict(self._graph.nodes[id])

    def all_nodes(self, kind: str | None = None) -> list[str]:
        if kind is None:
            return list(self._graph.nodes)
        return [n for n, d in self._graph.nodes(data=True) if d.get("kind") == kind]

    def summary(self) -> str:
        lines = [f"Dependency Graph: {self._graph.number_of_nodes()} nodes, "
                 f"{self._graph.number_of_edges()} edges"]
        for deriv in self._derivations.values():
            lines.append(f"  [{deriv.id}] {deriv.operation}")
            if deriv.assumptions:
                lines.append(f"    assumes: {', '.join(deriv.assumptions)}")
            if deriv.inputs:
                lines.append(f"    inputs: {', '.join(deriv.inputs)}")
            if deriv.outputs:
                lines.append(f"    outputs: {', '.join(deriv.outputs)}")
        return "\n".join(lines)
