"""Source-change invalidation for the project archive.

On every run a script computes a hash of its own source and compares
against the hash stored in the archive.  On mismatch the script's
archive entries are cleared before new derivations are recorded.

This is conservative: any source change triggers full invalidation,
even changes that do not affect derivations (e.g. comment edits).
False invalidations are cheap; missed invalidations are dangerous.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


def compute_source_hash(script_path: str | Path) -> str:
    """Return a hex digest of the script's source file content."""
    data = Path(script_path).read_bytes()
    return hashlib.sha256(data).hexdigest()


def read_stored_hash(namespace_path: Path) -> str | None:
    """Read the previously stored source hash, or None if absent."""
    hash_file = namespace_path / "source_hash.json"
    if not hash_file.exists():
        return None
    try:
        data = json.loads(hash_file.read_text(encoding="utf-8"))
        return data.get("sha256")
    except (json.JSONDecodeError, KeyError):
        return None


def write_source_hash(namespace_path: Path, hash_value: str) -> None:
    """Write the source hash to the namespace directory."""
    hash_file = namespace_path / "source_hash.json"
    namespace_path.mkdir(parents=True, exist_ok=True)
    tmp = hash_file.with_suffix(".json.tmp")
    tmp.write_text(
        json.dumps({"sha256": hash_value}, indent=2),
        encoding="utf-8",
    )
    os.replace(tmp, hash_file)


def check_and_invalidate(
    namespace_path: Path,
    script_path: str | Path,
    derivations_path: Path,
) -> bool:
    """Compare source hash and invalidate if changed.

    Returns True if invalidation occurred, False if the hash matched
    or no previous hash was stored.
    """
    current_hash = compute_source_hash(script_path)
    stored_hash = read_stored_hash(namespace_path)

    if stored_hash is not None and stored_hash != current_hash:
        # Source changed — clear all derivation entries.
        for path in derivations_path.glob("*.json"):
            path.unlink()
        write_source_hash(namespace_path, current_hash)
        return True

    # Store the current hash (first run or unchanged).
    write_source_hash(namespace_path, current_hash)
    return False
