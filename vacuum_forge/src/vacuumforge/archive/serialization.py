"""JSON-safe SymPy serialization helpers."""

from __future__ import annotations

import sympy
from enum import Enum


def serialize_expr(expr: sympy.Basic) -> dict[str, str]:
    return {"srepr": sympy.srepr(expr), "latex": sympy.latex(expr)}


def deserialize_expr(data: dict[str, str]) -> sympy.Basic:
    return sympy.sympify(data["srepr"])


def serialize_optional_expr(expr: sympy.Basic | None) -> dict[str, str] | None:
    return serialize_expr(expr) if expr is not None else None


def deserialize_optional_expr(data: dict[str, str] | None) -> sympy.Basic | None:
    return deserialize_expr(data) if isinstance(data, dict) else None


def serialize_enum(value: Enum | str | None) -> str | None:
    if value is None:
        return None
    return value.value if isinstance(value, Enum) else str(value)


def deserialize_enum(enum_cls, value, default=None):
    if value is None:
        return default
    if isinstance(value, enum_cls):
        return value
    try:
        return enum_cls(value)
    except ValueError:
        return default if default is not None else value
