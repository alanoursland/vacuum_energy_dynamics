"""Short-range gravity (inverse-square-law) constraints: gate G25.

Yukawa parameterization used by the experiments:

    V(r) = -(G m1 m2 / r) * (1 + alpha * exp(-r / lambda))

Anchors below were verified against paper abstracts on 2026-06-11 (see
verification field per constraint). The full alpha(lambda) exclusion curves
require digitization from published figures and are declared as manual
artifacts with instructions.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from dataexp.datasets.base import (
    Citation,
    Dataset,
    ManualFile,
    RemoteFile,
    VerificationStatus,
)


@dataclass
class YukawaAnchor:
    """A single scalar anchor from a paper (not a full curve)."""

    key: str
    statement: str
    lambda_m: float            # the lambda value the statement refers to (meters)
    alpha_bound: float         # |alpha| bound at that lambda
    confidence: str
    separations_tested_m: Optional[tuple]
    verification: VerificationStatus
    superseded_by: Optional[str] = None


@dataclass
class YukawaCurve:
    """A validated alpha(lambda) exclusion curve."""

    key: str
    filename: str
    points: List[tuple[float, float]]
    verification: VerificationStatus
    validation_anchor_key: str
    validation_crossing_m: float
    validation_relative_error: float


class ShortRangeGravity(Dataset):
    name = "short_range_gravity"
    version = "v1"

    citations = [
        Citation(
            key="lee2020",
            authors="J.G. Lee, E.G. Adelberger, T.S. Cook, S.M. Fleischer, B.R. Heckel",
            title="New Test of the Gravitational 1/r^2 Law at Separations down to 52 um",
            journal_ref="Phys. Rev. Lett. 124, 101101",
            year=2020,
            arxiv="2002.11761",
            doi="10.1103/PhysRevLett.124.101101",
            url="https://arxiv.org/abs/2002.11761",
        ),
        Citation(
            key="tan2020",
            authors="W.-H. Tan et al. (HUST)",
            title="Improvement for Testing the Gravitational Inverse-Square Law at the Submillimeter Range",
            journal_ref="Phys. Rev. Lett. 124, 051301",
            year=2020,
            doi="10.1103/PhysRevLett.124.051301",
        ),
        Citation(
            key="kapner2007",
            authors="D.J. Kapner et al. (Eot-Wash)",
            title="Tests of the Gravitational Inverse-Square Law below the Dark-Energy Length Scale",
            journal_ref="Phys. Rev. Lett. 98, 021101",
            year=2007,
            arxiv="hep-ph/0611184",
            doi="10.1103/PhysRevLett.98.021101",
        ),
    ]

    remote_files = [
        RemoteFile(
            filename="lee2020_abs.html",
            url="https://arxiv.org/abs/2002.11761",
            note="provenance cache of the primary anchor's abstract page",
        ),
        RemoteFile(
            filename="kapner2007_abs.html",
            url="https://arxiv.org/abs/hep-ph/0611184",
            note="provenance cache of the historical anchor's abstract page",
        ),
    ]

    manual_files = [
        ManualFile(
            filename="lee2020_chi_squared_vs_lambda.csv",
            instructions=(
                "Validated copy/paste extraction from Lee et al. supplemental "
                "material, Section 3 chi^2 vs lambda table. Use lambda_mm and "
                "alpha_95_absolute as the 95%-CL |alpha|(lambda) curve. Validate "
                "by log-log interpolation: |alpha| = 1 should cross at lambda = "
                "38.6e-6 m within 2%."
            ),
            schema=(
                "CSV header includes: lambda_mm,alpha_95_absolute. lambda_mm is "
                "converted to meters by the loader."
            ),
        ),
        ManualFile(
            filename="tan2020_alpha_lambda_95cl.txt",
            instructions=(
                "Author-provided table from Tan et al., PRL 124, 051301. Place the "
                "received PRL2020-AlphaLambda.txt file here. Validate by log-log "
                "interpolation: |alpha| = 1 should cross at lambda = 48e-6 m within "
                "2%."
            ),
            schema="Whitespace-delimited text: lambda_m alpha_limit",
        ),
    ]

    # ------------------------------------------------------------------
    # verified scalar anchors (typed once, here, with provenance)
    # ------------------------------------------------------------------

    ANCHORS: List[YukawaAnchor] = [
        YukawaAnchor(
            key="lee2020_alpha1_crossing",
            statement="gravitational-strength Yukawa (|alpha|=1) excluded for lambda >= 38.6 um",
            lambda_m=38.6e-6,
            alpha_bound=1.0,
            confidence="95% CL",
            separations_tested_m=(52e-6, 3.0e-3),
            verification=VerificationStatus.VERIFIED_FROM_ABSTRACT,
        ),
        YukawaAnchor(
            key="tan2020_alpha1_crossing",
            statement="|alpha| <= 1 holds down to lambda = 48 um (independent group)",
            lambda_m=48e-6,
            alpha_bound=1.0,
            confidence="95% CL",
            separations_tested_m=None,
            verification=VerificationStatus.VERIFIED_FROM_ABSTRACT,
        ),
        YukawaAnchor(
            key="kapner2007_alpha1_crossing",
            statement="|alpha| = 1 excluded for lambda >= 56 um (historical)",
            lambda_m=56e-6,
            alpha_bound=1.0,
            confidence="95% CL",
            separations_tested_m=None,
            verification=VerificationStatus.SUPERSEDED,
            superseded_by="lee2020_alpha1_crossing",
        ),
    ]

    def load(self) -> dict:
        """Return anchors plus any digitized curves present in the cache."""
        statuses = self.ensure()
        curves = {}
        for mf in self.manual_files:
            path = self.root / mf.filename
            if path.exists():
                rows = self._read_curve(path)
                curves[mf.filename] = self._validated_curve(path.name, rows)
        return {
            "anchors": self.ANCHORS,
            "curves": curves,
            "file_statuses": statuses,
            "primary_anchor": self.ANCHORS[0],
        }

    # convenience for experiments
    def best_alpha1_crossing_m(self) -> float:
        live = [a for a in self.ANCHORS
                if a.verification != VerificationStatus.SUPERSEDED and a.alpha_bound == 1.0]
        return min(a.lambda_m for a in live)

    def curve_crossing_m(self, curve: YukawaCurve, alpha_target: float) -> Optional[float]:
        """Log-log interpolate the lambda crossing for a target alpha."""
        return self._crossing_m(curve.points, alpha_target)

    def _validated_curve(self, filename: str, rows: List[tuple[float, float]]) -> YukawaCurve:
        if filename.startswith("lee2020"):
            anchor = self._anchor("lee2020_alpha1_crossing")
            verification = VerificationStatus.VERIFIED_FROM_FULL_TEXT
        elif filename.startswith("tan2020"):
            anchor = self._anchor("tan2020_alpha1_crossing")
            verification = VerificationStatus.AUTHOR_PROVIDED_TABLE
        else:
            raise ValueError(f"unknown curve source for {filename}")

        crossing = self._crossing_m(rows, anchor.alpha_bound)
        if crossing is None:
            raise ValueError(f"{filename}: curve does not cross alpha={anchor.alpha_bound}")
        rel = abs(crossing - anchor.lambda_m) / anchor.lambda_m
        if rel > 0.02:
            raise ValueError(
                f"{filename}: anchor validation failed; crossing={crossing:.6e} m, "
                f"expected={anchor.lambda_m:.6e} m, rel={rel:.3%}"
            )
        return YukawaCurve(
            key=filename.rsplit(".", 1)[0],
            filename=filename,
            points=rows,
            verification=verification,
            validation_anchor_key=anchor.key,
            validation_crossing_m=crossing,
            validation_relative_error=rel,
        )

    def _anchor(self, key: str) -> YukawaAnchor:
        for anchor in self.ANCHORS:
            if anchor.key == key:
                return anchor
        raise KeyError(key)

    @staticmethod
    def _read_curve(path: Path) -> List[tuple[float, float]]:
        if path.suffix.lower() == ".csv":
            csv_rows = list(csv.DictReader(path.read_text().splitlines()))
            if csv_rows and "lambda_mm" in csv_rows[0] and "alpha_95_absolute" in csv_rows[0]:
                rows = [
                    (float(row["lambda_mm"]) * 1e-3, float(row["alpha_95_absolute"]))
                    for row in csv_rows
                ]
                rows.sort(key=lambda pair: pair[0])
                return rows
            if csv_rows and "lambda_m" in csv_rows[0] and "alpha_limit" in csv_rows[0]:
                rows = [
                    (float(row["lambda_m"]), float(row["alpha_limit"]))
                    for row in csv_rows
                ]
                rows.sort(key=lambda pair: pair[0])
                return rows

        rows: List[tuple[float, float]] = []
        for line in path.read_text().splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            parts = stripped.replace(",", " ").split()
            if len(parts) < 2:
                continue
            try:
                lam, alpha = float(parts[0]), float(parts[1])
            except ValueError:
                continue
            rows.append((lam, alpha))
        rows.sort(key=lambda pair: pair[0])
        if len(rows) < 2:
            raise ValueError(f"{path.name}: expected at least two curve points")
        return rows

    @staticmethod
    def _crossing_m(rows: List[tuple[float, float]], alpha_target: float) -> Optional[float]:
        for (l1, a1), (l2, a2) in zip(rows, rows[1:]):
            if (a1 - alpha_target) * (a2 - alpha_target) <= 0 and a1 != a2:
                t = (
                    (math.log10(alpha_target) - math.log10(a1))
                    / (math.log10(a2) - math.log10(a1))
                )
                return 10 ** (math.log10(l1) + t * (math.log10(l2) - math.log10(l1)))
        return None
