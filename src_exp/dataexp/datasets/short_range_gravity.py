"""Short-range gravity (inverse-square-law) constraints: gate G25.

Yukawa parameterization used by the experiments:

    V(r) = -(G m1 m2 / r) * (1 + alpha * exp(-r / lambda))

Anchors below were verified against paper abstracts on 2026-06-11 (see
verification field per constraint). The full alpha(lambda) exclusion curves
require digitization from published figures and are declared as manual
artifacts with instructions.
"""

from __future__ import annotations

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
            filename="lee2020_alpha_lambda_95cl.csv",
            instructions=(
                "Digitize the 95%-CL alpha(lambda) exclusion curve from Fig. 5 of "
                "Lee et al., PRL 124, 101101 (arXiv:2002.11761), lambda from ~10 um "
                "to ~1 mm, log-log. Use a plot digitizer; sample >= 30 points per "
                "decade; record both axes in SI units. The curve must pass through "
                "|alpha| = 1 at lambda = 38.6e-6 m (the abstract's anchor) -- use "
                "that as the digitization sanity check."
            ),
            schema="CSV header: lambda_m,alpha_limit  (floats, SI units, 95% CL upper bound on |alpha|)",
        ),
        ManualFile(
            filename="tan2020_alpha_lambda_95cl.csv",
            instructions=(
                "Digitize the 95%-CL alpha(lambda) exclusion curve from Tan et al., "
                "PRL 124, 051301, lambda ~40-350 um. Sanity anchor: |alpha| = 1 "
                "crossing at lambda = 48e-6 m."
            ),
            schema="CSV header: lambda_m,alpha_limit",
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
                rows = []
                for line in path.read_text().splitlines()[1:]:
                    if line.strip():
                        lam, al = line.split(",")
                        rows.append((float(lam), float(al)))
                curves[mf.filename] = rows
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
