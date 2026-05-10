"""Shared status-output helpers for governance-aware scripts."""

from __future__ import annotations

from dataclasses import dataclass
from contextlib import contextmanager
from enum import Enum
import warnings


class StatusMark(str, Enum):
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"
    INFO = "INFO"
    OPEN = "OPEN"
    DEFER = "DEFER"
    MEMO = "MEMO"
    EVIDENCE = "EVIDENCE"
    OBLIGATION = "OBLIGATION"
    UNSUPPORTED = "UNSUPPORTED"
    UNDETERMINED = "UNDETERMINED"


@dataclass
class OutputEvent:
    label: str
    mark: StatusMark
    detail: str = ""
    block: str | None = None


def status_line(label: str, mark: StatusMark | str, detail: str = "") -> str:
    status = mark if isinstance(mark, StatusMark) else StatusMark(str(mark))
    suffix = f" -- {detail}" if detail else ""
    line = f"[{status.value}] {label}{suffix}"
    print(line)
    return line


def pass_warn_line(label: str, ok: bool, detail: str = "") -> str:
    warnings.warn(
        "pass_warn_line is deprecated because it cannot emit FAIL; use status_line.",
        DeprecationWarning,
        stacklevel=2,
    )
    return status_line(label, StatusMark.PASS if ok else StatusMark.WARN, detail)


class ScriptOutput:
    """Collect and print script output in governance-aware blocks."""

    def __init__(self) -> None:
        self.events: list[OutputEvent] = []
        self._current_block: str | None = None

    @contextmanager
    def block(self, name: str):
        previous = self._current_block
        self._current_block = name
        print(f"\n[{name}]")
        try:
            yield self
        finally:
            self._current_block = previous

    def derived_results(self):
        return self.block("derived_results")

    def governance_assessments(self):
        return self.block("governance_assessments")

    def unresolved_obligations(self):
        return self.block("unresolved_obligations")

    def sample_results(self):
        return self.block("sample_results")

    def counterexamples(self):
        return self.block("counterexamples")

    def line(self, label: str, mark: StatusMark | str, detail: str = "") -> str:
        status = mark if isinstance(mark, StatusMark) else StatusMark(str(mark))
        self.events.append(OutputEvent(label, status, detail, self._current_block))
        return status_line(label, status, detail)
