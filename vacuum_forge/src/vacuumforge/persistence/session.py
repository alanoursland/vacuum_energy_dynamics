"""Session persistence for VacuumForge.

Saves and loads TheoryContext sessions to/from YAML,
using sympy.srepr for expression serialization.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import yaml
import sympy

if TYPE_CHECKING:
    from vacuumforge.core.context import TheoryContext


def _serialize_expr(expr: sympy.Basic) -> dict[str, str]:
    """Serialize a SymPy expression to a dict with srepr and latex."""
    return {
        "srepr": sympy.srepr(expr),
        "latex": sympy.latex(expr),
    }


def _deserialize_expr(data: dict[str, str]) -> sympy.Basic:
    """Deserialize a SymPy expression from srepr."""
    return sympy.sympify(data["srepr"])


def save_session(ctx: TheoryContext, path: str) -> None:
    """Save a TheoryContext to a YAML file."""
    data: dict[str, Any] = {
        "vacuumforge_version": "0.1.0",
        "name": ctx.name,
        "symbols": {},
        "assumptions": [],
        "expressions": [],
        "sources": [],
        "energy_functionals": [],
        "ledger": [],
    }

    # Symbols
    for rec in ctx.symbols.list():
        data["symbols"][rec.name] = {
            "kind": rec.kind,
            "description": rec.description,
            "assumptions": rec.assumptions,
            "dimensions": rec.dimensions,
            "status": rec.status,
            "namespace": rec.namespace,
        }

    # Assumptions
    for rec in ctx.assumptions.active():
        data["assumptions"].append({
            "id": rec.id,
            "expression": _serialize_expr(rec.expression),
            "description": rec.description,
            "status": rec.status,
            "dependencies": rec.dependencies,
            "assumption_type": rec.assumption_type,
        })

    # Expressions
    for rec in ctx.expressions.list():
        data["expressions"].append({
            "id": rec.id,
            "expression": _serialize_expr(rec.expr),
            "description": rec.description,
            "status": rec.status,
            "dependencies": rec.dependencies,
            "scope": rec.scope,
            "exactness": rec.exactness,
        })

    # Sources
    for rec in ctx.sources.list():
        src_data = {
            "id": rec.id,
            "source_type": rec.source_type,
            "description": rec.description,
            "classification": rec.classification.value,
            "assumed_trace_free": rec.assumed_trace_free,
        }
        if rec.J_kappa is not None:
            src_data["J_kappa"] = _serialize_expr(rec.J_kappa)
        if rec.J_sigma is not None:
            src_data["J_sigma"] = _serialize_expr(rec.J_sigma)
        data["sources"].append(src_data)

    # Energy functionals
    for func in ctx.energy.list():
        data["energy_functionals"].append({
            "id": func.id,
            "expression": _serialize_expr(func.expression),
            "variables": [sympy.srepr(v) for v in func.variables],
            "description": func.description,
        })

    # Ledger
    for entry in ctx.ledger.all():
        entry_data = {
            "id": entry.id,
            "statement": entry.statement,
            "status": entry.status.value,
            "dependencies": entry.dependencies,
            "notes": entry.notes,
        }
        if entry.expression is not None:
            entry_data["expression"] = _serialize_expr(entry.expression)
        data["ledger"].append(entry_data)

    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def load_session(path: str) -> TheoryContext:
    """Load a TheoryContext from a YAML file."""
    from vacuumforge.core.context import TheoryContext
    from vacuumforge.core.status import Status

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    ctx = TheoryContext(data.get("name", "loaded_session"))

    # Rebuild symbols — for now, use define_equal_response if standard symbols present
    if "A" in data.get("symbols", {}) and "kappa" in data.get("symbols", {}):
        ctx.define_equal_response_algebraic_symbols()

    # Rebuild assumptions
    for a_data in data.get("assumptions", []):
        expr = _deserialize_expr(a_data["expression"])
        ctx.assumptions.add(
            id=a_data["id"],
            expression=expr,
            description=a_data.get("description"),
            status=a_data.get("status", "assumption"),
            dependencies=a_data.get("dependencies", []),
            assumption_type=a_data.get("assumption_type"),
        )

    # Rebuild sources
    for s_data in data.get("sources", []):
        J_kappa = _deserialize_expr(s_data["J_kappa"]) if "J_kappa" in s_data else sympy.Integer(0)
        J_sigma = _deserialize_expr(s_data["J_sigma"]) if "J_sigma" in s_data else sympy.Integer(0)
        ctx.sources.add_modes(
            id=s_data["id"],
            J_kappa=J_kappa,
            J_sigma=J_sigma,
            source_type=s_data.get("source_type", "general"),
            description=s_data.get("description"),
        )

    # Rebuild energy functionals
    for e_data in data.get("energy_functionals", []):
        expr = _deserialize_expr(e_data["expression"])
        variables = [sympy.sympify(v) for v in e_data.get("variables", [])]
        ctx.energy.add(
            id=e_data["id"],
            expression=expr,
            variables=variables,
            description=e_data.get("description"),
        )

    # Rebuild ledger
    for l_data in data.get("ledger", []):
        expr = _deserialize_expr(l_data["expression"]) if "expression" in l_data else None
        ctx.ledger.add(
            id=l_data["id"],
            statement=l_data["statement"],
            status=Status(l_data["status"]),
            expression=expr,
            dependencies=l_data.get("dependencies", []),
            notes=l_data.get("notes"),
        )

    return ctx
