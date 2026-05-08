"""Fixture: a script that hardcodes verdicts in dataclass constructors."""
from dataclasses import dataclass


@dataclass
class GroupStatusEntry:
    group: str
    status: str
    note: str


entries = [
    GroupStatusEntry(group="Group01", status="CLOSED", note="Foundation validated"),
    GroupStatusEntry(group="Group02", status="PASS", note="Trace modes confirmed"),
    GroupStatusEntry(group="Group03", status="DERIVED", note="Orbit space done"),
    GroupStatusEntry(group="Group04", status="DEFER", note="Pending review"),
]

for entry in entries:
    print(f"[{entry.status}] {entry.group}: {entry.note}")
