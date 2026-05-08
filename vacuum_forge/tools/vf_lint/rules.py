"""Lint rule definitions for vf-lint.

Each rule is a (name, pattern_matcher, severity) tuple. Pattern matchers
receive a VerdictClassification and return True if the rule applies.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .analyzer import VerdictClassification


@dataclass
class Rule:
    name: str
    description: str
    severity: str  # "FAIL", "WARN", "INFO"
    enabled: bool = True


# Default rule set from the technical design.
DEFAULT_RULES: list[Rule] = [
    Rule(
        name="verdict_in_dataclass_literal",
        description="Verdict-like string in a dataclass or constructor status field.",
        severity="FAIL",
    ),
    Rule(
        name="unconditional_pass_print",
        description="PASS verdict in a print statement with no enclosing conditional.",
        severity="WARN",
    ),
    Rule(
        name="status_line_with_literal",
        description="status_line call whose condition argument is a literal.",
        severity="WARN",
    ),
    Rule(
        name="status_line_with_no_computation",
        description="status_line call whose condition is not traceable to validation.",
        severity="WARN",
    ),
    Rule(
        name="missing_validation_imports",
        description="Script emits verdicts but imports neither sympy nor vacuumforge.",
        severity="INFO",
    ),
]


def get_rule(name: str) -> Rule | None:
    for rule in DEFAULT_RULES:
        return_rule = rule if rule.name == name else None
        if return_rule is not None:
            return return_rule
    return None


def build_rule_index() -> dict[str, Rule]:
    return {rule.name: rule for rule in DEFAULT_RULES}
