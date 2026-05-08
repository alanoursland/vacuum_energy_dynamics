"""Fixture: a script with verdict-like strings in dataclass constructors."""
from dataclasses import dataclass


@dataclass
class Result:
    name: str
    status: str


r1 = Result(name="check_1", status="PASS")
r2 = Result(name="check_2", status="DERIVED")
r3 = Result(name="check_3", status="FAIL")
