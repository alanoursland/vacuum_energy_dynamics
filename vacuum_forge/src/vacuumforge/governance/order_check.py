"""Validate scripts_v3 group order files."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from vacuumforge.governance.lint_models import parse_script_metadata


@dataclass
class OrderCheckResult:
    group_dir: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def check_group_order(group_dir: str | Path) -> OrderCheckResult:
    group = Path(group_dir)
    result = OrderCheckResult(group)
    order_file = group / "order.txt"
    scripts = sorted(p.name for p in group.glob("*.py"))
    if not order_file.exists():
        result.errors.append("missing order.txt")
        return result
    entries: list[str] = []
    for raw_line in order_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if not line.endswith(".py"):
            line += ".py"
        entries.append(line)
    for entry in entries:
        if entry not in scripts:
            result.errors.append(f"order entry points to missing file: {entry}")
    for script in scripts:
        if entries.count(script) == 0:
            result.errors.append(f"script is missing from order.txt: {script}")
        if entries.count(script) > 1:
            result.errors.append(f"script appears more than once in order.txt: {script}")
    if entries:
        summary_entries = [e for e in entries if "summary" in e.lower()]
        if summary_entries and entries[-1] not in summary_entries:
            result.warnings.append("summary script is not last")
    stems = {}
    for script in scripts:
        stem = script.removesuffix(".py")
        base = stem[:-3] if stem.endswith("_v2") else stem
        stems.setdefault(base, []).append(script)
    for versions in stems.values():
        if len(versions) > 1:
            for script in versions:
                meta = parse_script_metadata(group / script)
                if not meta.superseded_by and meta.canonical is not False:
                    result.warnings.append(f"versioned script lacks supersession metadata: {script}")
    return result
