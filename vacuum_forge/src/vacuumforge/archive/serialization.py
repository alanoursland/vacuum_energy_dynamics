"""JSON-safe SymPy serialization helpers."""

from __future__ import annotations

import sympy


def serialize_expr(expr: sympy.Basic) -> dict[str, str]:
    return {"srepr": sympy.srepr(expr), "latex": sympy.latex(expr)}


def deserialize_expr(data: dict[str, str]) -> sympy.Basic:
    return sympy.sympify(data["srepr"])

