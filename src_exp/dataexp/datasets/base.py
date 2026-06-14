"""Dataset base machinery for data experiments.

Data is treated like ML datasets: a dataset module declares its provenance,
its remote artifacts (auto-downloadable) and manual artifacts (with
digitization/acquisition instructions), and provides a deterministic loader.
Artifacts cache under dataexp/.data/<name>/<version>/ with a manifest.

Run everything from vacuum_forge/src with PYTHONPATH=.
"""

from __future__ import annotations

import hashlib
import json
import urllib.request
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import List, Optional


DATA_ROOT = Path(__file__).resolve().parents[1] / ".data"


class VerificationStatus(str, Enum):
    VERIFIED_FROM_ABSTRACT = "verified_from_abstract"
    VERIFIED_FROM_FULL_TEXT = "verified_from_full_text"
    AUTHOR_PROVIDED_TABLE = "author_provided_table"
    DIGITIZED_FROM_FIGURE = "digitized_from_figure"
    VECTOR_EXTRACTED_FROM_ARXIV_PDF = "vector_extracted_from_arxiv_pdf"
    FROM_MEMORY_UNVERIFIED = "from_memory_unverified"  # forbidden in confrontations
    SUPERSEDED = "superseded"


@dataclass
class Citation:
    key: str
    authors: str
    title: str
    journal_ref: str
    year: int
    arxiv: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None


@dataclass
class RemoteFile:
    """An artifact that can be fetched automatically."""

    filename: str
    url: str
    sha256: Optional[str] = None  # None: content not hash-pinned (e.g. HTML)
    note: str = ""


@dataclass
class ManualFile:
    """An artifact that requires manual acquisition (e.g. figure digitization).

    The instructions must be detailed enough that a future worker can produce
    the file without further context. schema describes the expected format.
    """

    filename: str
    instructions: str
    schema: str
    sha256: Optional[str] = None  # pin once produced


@dataclass
class FileStatus:
    filename: str
    present: bool
    sha256: Optional[str]
    verified: Optional[bool]  # None when no pin declared
    kind: str  # "remote" | "manual"
    note: str = ""


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


class Dataset:
    """Base class. Subclasses set name, version, citations, remote_files,
    manual_files and implement load()."""

    name: str = "unnamed"
    version: str = "v0"
    citations: List[Citation] = []
    remote_files: List[RemoteFile] = []
    manual_files: List[ManualFile] = []

    @property
    def root(self) -> Path:
        return DATA_ROOT / self.name / self.version

    # ------------------------------------------------------------------
    # acquisition
    # ------------------------------------------------------------------

    def ensure(self, offline_ok: bool = True) -> List[FileStatus]:
        """Download missing remote artifacts; report status of everything.

        Never raises on network failure when offline_ok (the experiment then
        decides what it can run without). Writes/updates manifest.json.
        """
        self.root.mkdir(parents=True, exist_ok=True)
        statuses: List[FileStatus] = []

        for rf in self.remote_files:
            path = self.root / rf.filename
            note = rf.note
            if not path.exists():
                try:
                    req = urllib.request.Request(
                        rf.url, headers={"User-Agent": "vacuumforge-dataexp/1.0"}
                    )
                    with urllib.request.urlopen(req, timeout=60) as resp:
                        path.write_bytes(resp.read())
                    note = (note + " | downloaded").strip(" |")
                except Exception as exc:  # offline / blocked / 404
                    statuses.append(FileStatus(rf.filename, False, None, None,
                                               "remote", f"download failed: {exc}"))
                    if not offline_ok:
                        raise
                    continue
            digest = sha256_of(path)
            verified = None if rf.sha256 is None else (digest == rf.sha256)
            statuses.append(FileStatus(rf.filename, True, digest, verified, "remote", note))

        for mf in self.manual_files:
            path = self.root / mf.filename
            if path.exists():
                digest = sha256_of(path)
                verified = None if mf.sha256 is None else (digest == mf.sha256)
                statuses.append(FileStatus(mf.filename, True, digest, verified, "manual"))
            else:
                statuses.append(FileStatus(mf.filename, False, None, None, "manual",
                                           "MISSING -- see instructions in dataset module"))

        self._write_manifest(statuses)
        return statuses

    def _write_manifest(self, statuses: List[FileStatus]) -> None:
        manifest = {
            "dataset": self.name,
            "version": self.version,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "citations": [asdict(c) for c in self.citations],
            "files": [asdict(s) for s in statuses],
        }
        (self.root / "manifest.json").write_text(json.dumps(manifest, indent=2))

    # ------------------------------------------------------------------
    # loading
    # ------------------------------------------------------------------

    def load(self):  # pragma: no cover - abstract
        raise NotImplementedError

    def describe(self) -> str:
        lines = [f"dataset {self.name} {self.version}"]
        for c in self.citations:
            ar = f" arXiv:{c.arxiv}" if c.arxiv else ""
            lines.append(f"  [{c.key}] {c.authors} ({c.year}), {c.journal_ref}{ar}")
        return "\n".join(lines)
