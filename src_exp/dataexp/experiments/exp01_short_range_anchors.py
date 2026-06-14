"""Experiment 01: short-range gravity anchors vs the UFFT crossover scale.

Smoke test of the dataexp pipeline plus the first quantitative geometric
fact for Trial A: where does UFFT's predicted crossover scale sit relative
to the verified short-range-gravity exclusion anchors?

Run from vacuum_forge/src:

    PYTHONPATH=. python dataexp/experiments/exp01_short_range_anchors.py

This is a Layer-3 confrontation consuming Layer-1 data only through the
dataset loader (protocol rule D2: no number typed twice).
"""

from __future__ import annotations

import math

from dataexp.datasets.short_range_gravity import ShortRangeGravity, VerificationStatus


HBAR = 1.054571817e-34   # J s   (CODATA, exact-derived)
C = 2.99792458e8         # m/s   (exact)
RHO_LAMBDA = 5.4e-10     # J/m^3 (dark energy density; UFFT memo's value)


def ufft_crossover_m() -> float:
    """a_Lambda = (pi^2 hbar c / (720 rho_Lambda))^(1/4); charter case 2e."""
    return (math.pi**2 * HBAR * C / (720 * RHO_LAMBDA)) ** 0.25


def main() -> None:
    print("=" * 100)
    print("exp01: short-range gravity anchors vs UFFT crossover")
    print("=" * 100)

    ds = ShortRangeGravity()
    print(ds.describe())
    data = ds.load()

    print("\n[file statuses]")
    for st in data["file_statuses"]:
        mark = "OK " if st.present else "-- "
        print(f"  {mark} {st.kind:6s} {st.filename}  {st.note}")

    print("\n[verified anchors]")
    for a in data["anchors"]:
        sup = f"  (superseded by {a.superseded_by})" if a.superseded_by else ""
        print(f"  {a.key}: lambda = {a.lambda_m*1e6:.1f} um @ |alpha| <= {a.alpha_bound}"
              f" [{a.confidence}, {a.verification.value}]{sup}")

    if data["curves"]:
        print("\n[validated curves]")
        for curve in data["curves"].values():
            a13 = ds.curve_crossing_m(curve, 1.0 / 3.0)
            a13_msg = f", alpha=1/3 crossing = {a13*1e6:.2f} um" if a13 else ""
            print(
                f"  {curve.key}: {len(curve.points)} points "
                f"[{curve.verification.value}], anchor crossing = "
                f"{curve.validation_crossing_m*1e6:.2f} um "
                f"(rel. error {curve.validation_relative_error*100:.2f}%){a13_msg}"
            )

        print("\n[curve-derived binding crossings]")
        for target, label in [(1.0, "|alpha|=1"), (1.0 / 3.0, "alpha=1/3")]:
            crossings = [
                (ds.curve_crossing_m(curve, target), curve.key)
                for curve in data["curves"].values()
            ]
            crossings = [(value, key) for value, key in crossings if value is not None]
            if crossings:
                value, key = min(crossings, key=lambda item: item[0])
                print(f"  {label}: lambda >= {value*1e6:.2f} um ({key})")

    crossing = ds.best_alpha1_crossing_m()
    a_lambda = ufft_crossover_m()

    print("\n[confrontation]")
    print(f"  best live |alpha|=1 exclusion crossing : {crossing*1e6:.1f} um")
    print(f"  UFFT crossover a_Lambda                : {a_lambda*1e6:.1f} um")

    in_window = a_lambda < crossing
    print(f"\n  UFFT crossover below the exclusion crossing: {in_window}")
    if in_window:
        print("  => The candidate's predicted scale sits in the unexcluded window")
        print("     below the gravitational-strength crossing. The G25 gate is a")
        print("     QUANTITATIVE constraint-surface computation, not an instant kill.")
        print("     Required next: the UFFT pressure -> effective Yukawa conversion")
        print("     (Layer 2, to be derived in the forge), evaluated against these")
        print("     validated alpha(lambda) curves.")
    else:
        print("  => The candidate's predicted scale is inside the excluded region")
        print("     at gravitational strength; Trial A faces an immediate")
        print("     quantitative kill test.")

    print("\n[negative-space record]")
    print("  NOT excluded by these anchors: |alpha| > 1 below ~38.6 um;")
    print("  any non-Yukawa-shaped signature (offset or a^-2 terms) needs the")
    print("  Layer-2 conversion before these bounds apply at all.")

    print("\nexp01 complete.")


if __name__ == "__main__":
    main()
