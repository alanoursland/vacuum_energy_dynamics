"""Script metadata parsing helpers for governance tooling."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass
class ScriptMetadata:
    group: str | None = None
    script_type: str | None = None
    canonical: bool | None = None
    superseded_by: str | None = None
    archive_script_id: str | None = None


_FIELD_MAP = {
    "group": "group",
    "script type": "script_type",
    "canonical": "canonical",
    "superseded by": "superseded_by",
    "archive script id": "archive_script_id",
}


def parse_script_metadata_text(text: str) -> ScriptMetadata:
    metadata = ScriptMetadata()
    for line in text.splitlines()[:40]:
        match = re.match(r"\s*#\s*([^:]+):\s*(.+?)\s*$", line)
        if not match:
            continue
        key = match.group(1).strip().lower()
        value = match.group(2).strip()
        attr = _FIELD_MAP.get(key)
        if attr is None:
            continue
        if attr == "canonical":
            setattr(metadata, attr, value.lower() == "true")
        else:
            setattr(metadata, attr, value)
    return metadata


def parse_script_metadata(path: str | Path) -> ScriptMetadata:
    return parse_script_metadata_text(Path(path).read_text(encoding="utf-8"))
