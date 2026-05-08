"""Fixture: various status_line patterns for testing."""
import sympy
from vacuumforge.core.simplify import is_zero


def status_line(label, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}: {detail}")


r = sympy.Symbol("r", positive=True)

# Gated on real computation — OK
status_line("zero_check", is_zero(r - r), "should be zero")

# Literal condition — WARN
status_line("literal_true", True, "hardcoded")

# Non-validation function — WARN
status_line("other_call", len([1, 2]) == 2, "not a validation call")
