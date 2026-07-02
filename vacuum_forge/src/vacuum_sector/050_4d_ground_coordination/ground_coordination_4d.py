#!/usr/bin/env python3
"""
ground_coordination_4d.py

Derivation 050: the 4D ground coordination (O-P10-2 attacked).

O-P10-2 asked: around a triangle hinge in 4D, n = 4 and n = 5
coordinations carry opposite-sign deficits (+57.91 deg / -17.61 deg).
Which does the ground state select?

The answer this derivation establishes, at mean-field level:

  NEITHER PURELY -- THE FLAT GROUND STATE IS FORCED TO MIX.

  (1) The deficit ladder is exact: delta(n) = 2 pi - n arccos(1/4),
      positive for n <= 4, negative for n >= 5, zero for no integer.
      |delta(5)| < |delta(4)| < everything else: n = 5 is the softest
      single coordination, exactly as in 3D.
  (2) For ANY wedge energy increasing in |delta| the per-hinge ranking
      puts n = 5 first -- but a pure n = 5 packing carries strictly
      negative total deficit and CANNOT be flat.
  (3) P10's flat ground state (the 037/041 result: the ground state is
      flat and frustrated) therefore imposes the zero-mean-deficit
      constraint, which fixes the {4, 5} mixture exactly:
          x_4 = 5 - 2 pi/theta = 0.2332...   (theta = arccos(1/4))
          x_5 = 2 pi/theta - 4 = 0.7668...
      i.e. mean coordination n_bar = 2 pi/theta = 4.7668... -- an
      exact, parameter-free structural number of the 4D vacuum.
  (4) The mixed floor is strictly positive (frustration survives the
      mixture): for the quadratic witness, E/hinge = x4 delta4^2 +
      x5 delta5^2 > 0. 4D frustration is unavoidable AND quantified.
  (5) The 4D wedge-ring lab (scipy, the 041 pattern lifted one
      dimension): relaxed spring energy E(n) of n 4-simplices sharing
      a triangle hinge has its strict minimum at n = 5 with a positive
      residual -- the numerical face of (1)-(2).

Honesty fence: (3) is a MEAN-FIELD statement -- it treats hinge
deficits as independently assignable, ignoring the combinatorial
constraints of an actual triangulation (which hinge fractions are
realizable is a Delaunay-combinatorics question). The remaining face
of O-P10-2 -- realizing the mixture in a periodic 4D packing and
confirming the floor is intensive -- folds into O-P10-5 (bulk
relaxation phase 2). The (3+1) relationship note: the SPATIAL packing
(3D, edge hinges, arccos(1/3), Delta_0 > 0, positive ground deficits)
and the Euclidean-4D packing (triangle hinges, arccos(1/4), mixed-sign
ground deficits) are different objects; which one the Lorentzian
vacuum instantiates is part of O-P10-4's initial-value question and is
NOT settled here.
"""

from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import minimize

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
)


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"

DEPENDENCIES = [
    ("lift_dep_050", "043_lorentzian_4d_lift__lorentzian_4d_lift",
     "lorentzian_4d_lift_043"),
    ("lab_dep_050", "041_frustration_relaxation_lab__frustration_relaxation_lab",
     "frustration_relaxation_lab_041"),
    ("adoption_dep_050", "044_p10_adoption__p10_adoption",
     "p10_adoption_record_044"),
]

THETA = sp.acos(sp.Rational(1, 4))  # the regular 4-simplex dihedral


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def require(label: str, condition: bool, failures: list) -> None:
    mark = "PASS" if condition else "FAIL"
    print(f"  [{mark}] {label}")
    if not condition:
        failures.append(label)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in DEPENDENCIES:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
        )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def check_1_deficit_ladder(failures):
    header("Check 1: the exact 4D deficit ladder at a triangle hinge")
    deltas = {n: sp.simplify(2 * sp.pi - n * THETA) for n in range(3, 8)}
    print(f"  theta = arccos(1/4) = {float(THETA.evalf(50)):.6f} rad "
          f"= {float((THETA * 180 / sp.pi).evalf(50)):.4f} deg")
    for n, d in deltas.items():
        print(f"    n = {n}: delta = {float(d.evalf(50)):+.6f} rad "
              f"= {float((d * 180 / sp.pi).evalf(50)):+.4f} deg")
    require("sign flip between n = 4 and n = 5 (positive <= 4, negative >= 5)",
            all(float(deltas[n].evalf(50)) > 0 for n in (3, 4))
            and all(float(deltas[n].evalf(50)) < 0 for n in (5, 6, 7)), failures)
    require("no integer coordination is deficit-free (50-digit witness, n = 3..7)",
            all(abs(float(d.evalf(50))) > 1e-40 for d in deltas.values()), failures)
    require("headline values: delta(4) = +57.91 deg, delta(5) = -17.61 deg",
            abs(float((deltas[4] * 180 / sp.pi).evalf(50)) - 57.9066) < 5e-3
            and abs(float((deltas[5] * 180 / sp.pi).evalf(50)) + 17.6124) < 5e-3,
            failures)
    return deltas


def check_2_single_coordination_ranking(deltas, failures):
    header("Check 2: per-hinge ranking -- n = 5 is the softest single coordination")
    mags = {n: abs(float(d.evalf(50))) for n, d in deltas.items()}
    require("|delta(5)| < |delta(4)| < |delta(3)|",
            mags[5] < mags[4] < mags[3], failures)
    require("|delta(5)| < |delta(6)| < |delta(7)|",
            mags[5] < mags[6] < mags[7], failures)
    print("  For ANY wedge energy f increasing in |delta| (f(0) = 0), the")
    print("  per-hinge cost ranks n = 5 first: the same selection as 3D (041 E2).")
    print("  But a pure n = 5 packing has strictly negative deficit at every")
    print("  hinge -- by the Regge encoding (039) it is a negatively curved")
    print("  configuration, NOT the flat ground state (037/041).")


def check_3_flatness_mixture(deltas, failures):
    header("Check 3: the flat ground state's forced {4, 5} mixture (mean-field)")
    x = sp.Symbol("x", positive=True)
    sol = sp.solve(sp.Eq(x * deltas[4] + (1 - x) * deltas[5], 0), x)
    x4 = sp.simplify(sol[0])
    x4_closed = sp.simplify(5 - 2 * sp.pi / THETA)
    require("zero-mean-deficit fraction: x_4 = 5 - 2 pi/arccos(1/4) exactly",
            sp.simplify(x4 - x4_closed) == 0, failures)
    x4_num = float(x4.evalf(50))
    require("x_4 in (0, 1): the mixture is genuinely mixed", 0 < x4_num < 1, failures)
    nbar = sp.simplify(2 * sp.pi / THETA)
    print(f"  x_4 = {x4_num:.6f}, x_5 = {1 - x4_num:.6f}")
    print(f"  mean coordination n_bar = 2 pi/arccos(1/4) = {float(nbar.evalf(50)):.6f}")
    require("mean coordination n_bar = 2 pi/theta, and 4 < n_bar < 5",
            4 < float(nbar.evalf(50)) < 5, failures)

    # The mixed floor is strictly positive (quadratic witness).
    floor = sp.simplify(x4 * deltas[4] ** 2 + (1 - x4) * deltas[5] ** 2)
    floor_num = float(floor.evalf(50))
    require("mixed frustration floor > 0 (quadratic witness): E/hinge = "
            f"{floor_num:.6f} rad^2", floor_num > 0, failures)
    # Sanity: mixture beats pure n = 4 but pays more than (non-flat) pure n = 5.
    d4sq = float((deltas[4] ** 2).evalf(50))
    d5sq = float((deltas[5] ** 2).evalf(50))
    require("floor ordering: delta5^2 < mixed floor < delta4^2 (flatness costs energy)",
            d5sq < floor_num < d4sq, failures)
    print("  The flat vacuum PAYS for flatness: the zero-curvature constraint")
    print("  forces ~23.3% of hinges up to the expensive n = 4 coordination.")
    print("  Both the mixture fractions and the floor are exact functions of")
    print("  arccos(1/4) alone -- parameter-free structural numbers of the")
    print("  4D vacuum (mean-field; realizability folds into O-P10-5).")
    return x4, nbar, floor


def relaxed_wedge_energy(n: int) -> float:
    """Relaxed spring energy of n regular 4-simplices sharing a triangle hinge.

    Fixed unit equilateral triangle (v0, v1, v2) in the e1-e2 plane; n outer
    vertices w_i in R^4; cell i = (v0, v1, v2, w_i, w_{i+1 mod n}). Springs
    (|e| - 1)^2 on every triangle-to-outer and consecutive outer-outer edge.
    Initial condition: outer vertices on the dihedral circle of radius
    sqrt(2/3) about the triangle centroid in the e3-e4 plane.
    """
    tri = np.array([
        [0.0, 0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0, 0.0],
        [0.5, np.sqrt(3.0) / 2.0, 0.0, 0.0],
    ])
    centroid = tri.mean(axis=0)
    rho = np.sqrt(2.0 / 3.0)
    phis = 2.0 * np.pi * np.arange(n) / n
    w0 = np.array([centroid + rho * (np.cos(p) * np.array([0, 0, 1, 0])
                                     + np.sin(p) * np.array([0, 0, 0, 1]))
                   for p in phis])

    def energy(flat):
        w = flat.reshape(n, 4)
        e = 0.0
        for i in range(n):
            for v in tri:
                e += (np.linalg.norm(w[i] - v) - 1.0) ** 2
            e += (np.linalg.norm(w[i] - w[(i + 1) % n]) - 1.0) ** 2
        return e

    res = minimize(energy, w0.ravel(), method="BFGS",
                   options={"gtol": 1e-12, "maxiter": 20000})
    return float(res.fun)


def check_4_wedge_ring_lab(failures):
    header("Check 4: the 4D wedge-ring relaxation lab (numerical, 041 pattern)")
    energies = {}
    for n in range(3, 8):
        energies[n] = relaxed_wedge_energy(n)
        print(f"    n = {n}: relaxed E = {energies[n]:.6f}")
    emin = min(energies, key=energies.get)
    require("strict minimum of relaxed E(n) at n = 5", emin == 5
            and all(energies[5] < energies[n] for n in energies if n != 5),
            failures)
    require("positive residual at the minimum (4D frustration is real): E(5) > 1e-4",
            energies[5] > 1e-4, failures)
    print("  The lifted lab confirms the exact ladder: five 4-simplices around")
    print("  a triangle hinge is the softest wedge, and even it cannot relax to")
    print("  zero -- 4D frustration, measured.")
    return energies


def record(ns, x4, nbar, floor, energies):
    ns.record_derivation(
        derivation_id="ground_coordination_4d_050",
        inputs=[sp.Symbol("theta_arccos_quarter"), sp.Symbol("flat_ground_state_constraint"),
                sp.Symbol("wedge_ring_lab_4d")],
        output=sp.Symbol("flat_4d_ground_is_mixed_x4_5_minus_2pi_over_theta"),
        method=(
            "exact symbolic deficit ladder delta(n) = 2 pi - n arccos(1/4); "
            "generic monotone-energy ranking; zero-mean-deficit flatness "
            "constraint solved exactly for the {4, 5} mixture (mean-field); "
            "positive mixed floor (quadratic witness); scipy BFGS relaxation "
            "of the 4D wedge ring confirming the strict n = 5 minimum with "
            "positive residual"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="ground_state_structure_theorem",
        scope=(
            "mean-field: hinge deficits treated as independently assignable; "
            "realizability of the mixture in a periodic 4D triangulation and "
            "floor intensivity fold into O-P10-5; the (3+1)-vs-Euclidean-4D "
            "instantiation question stays with O-P10-4"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="o_p10_2_resolved_meanfield_050",
        script_id=SCRIPT_ID,
        title="O-P10-2 resolved at mean-field: the flat 4D ground state is MIXED {4, 5}",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["ground_coordination_4d_050"],
        description=(
            "The ground state selects NEITHER pure coordination: n = 5 is the "
            "softest wedge (exact ladder + 4D lab) but pure n = 5 is negatively "
            "curved; the flat ground state (037/041) forces the exact mixture "
            "x_4 = 5 - 2 pi/arccos(1/4) = 0.2332, x_5 = 0.7668, mean "
            "coordination 2 pi/arccos(1/4) = 4.7668 -- parameter-free. Mixed "
            "floor strictly positive. Remaining face (realizability, "
            "intensivity) transferred to O-P10-5."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="mixture_realizability_050",
        script_id=SCRIPT_ID,
        title="Realize the {4, 5} hinge mixture in a periodic 4D triangulation",
        status=ObligationStatus.OPEN,
        required_by=["ground_coordination_4d_050"],
        description=(
            "Mean-field fractions x_4 = 0.2332 / x_5 = 0.7668 must be shown "
            "realizable (or corrected) by an actual periodic 4D simplicial "
            "packing; joint with O-P10-5 bulk relaxation phase 2. Known "
            "cross-check target: which fractions Delaunay triangulations of "
            "dense 4D point sets actually achieve."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="ground_coordination_claim_050",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "O-P10-2's question 'which coordination does the 4D ground state "
            "select' has answer: a forced mixture. n = 5 is the softest wedge "
            "but cannot tile flat space alone (net negative deficit); the flat "
            "frustrated ground state must promote x_4 = 5 - 2 pi/arccos(1/4) "
            "of its triangle hinges to n = 4, giving mean coordination "
            "2 pi/arccos(1/4) = 4.7668 and a strictly positive, exactly "
            "computable frustration floor. Flatness is BOUGHT with frustration "
            "energy -- the 4D vacuum pays for being flat, which is the "
            "substance-energy story (038) in its sharpest form yet. Mean-field "
            "fence recorded; realizability open (mixture_realizability_050)."
        ),
        derivation_ids=["ground_coordination_4d_050"],
        obligation_ids=["o_p10_2_resolved_meanfield_050"],
    ))


def write_report(x4, nbar, floor, energies) -> Path:
    repo_root = SCRIPT_PATH.parents[4]
    report_path = (repo_root / "theory_v3" / "development" / "vacuum_sector"
                   / "08_packing_microphysics"
                   / "ground_coordination_4d_vacuumforge.md")
    x4n = float(x4.evalf(50))
    nbarn = float(nbar.evalf(50))
    floorn = float(floor.evalf(50))
    elines = "\n".join(f"    n = {n}:  E = {e:.6f}" for n, e in energies.items())
    report = f"""# The 4D Ground Coordination (O-P10-2) -- VacuumForge Record

## Status

```text
result type:   ground-state structure theorem, mean-field (2026-07-02,
               derivation 050)
conclusion:    the flat 4D ground state selects NEITHER n = 4 nor n = 5
               purely -- it is a FORCED MIXTURE with exact fractions
               x_4 = 5 - 2 pi/arccos(1/4) = {x4n:.6f}
               x_5 = 2 pi/arccos(1/4) - 4 = {1 - x4n:.6f}
               mean coordination n_bar = 2 pi/arccos(1/4) = {nbarn:.6f}
               -- parameter-free structural numbers of the 4D vacuum.
fence:         MEAN-FIELD (deficits treated as independently assignable);
               realizability in a periodic triangulation is opened as
               mixture_realizability_050, joint with O-P10-5.
verification:  vacuum_forge/src/vacuum_sector/050_4d_ground_coordination/
```

## The Question and the Answer's Shape

O-P10-2 asked which coordination the 4D ground state selects, given
that n = 4 and n = 5 around a triangle hinge carry opposite-sign
deficits. The question presupposed a single winner. The answer is that
the flatness of the ground state (037/041) makes a single winner
impossible:

```text
delta(n) = 2 pi - n arccos(1/4):
    n = 3: +133.44 deg     n = 5:  -17.61 deg
    n = 4:  +57.91 deg     n = 6:  -93.13 deg

- n = 5 is the SOFTEST wedge (smallest |delta|; confirmed by the 4D
  relaxation lab below) -- the same selection as 3D.
- but every hinge of a pure n = 5 packing carries negative deficit:
  by the Regge encoding (039) that configuration is negatively
  curved, not flat.
- the flat ground state must therefore mix, and zero mean deficit
  fixes the mixture EXACTLY: x_4 delta(4) + x_5 delta(5) = 0.
```

## The Payoff: Flatness Is Bought

The mixed floor is strictly positive and exactly computable
(quadratic witness): E/hinge = x_4 delta_4^2 + x_5 delta_5^2 =
{floorn:.6f} rad^2, sitting strictly between the pure-n=5 and
pure-n=4 costs. The vacuum pays ~23% expensive n = 4 hinges as the
price of zero curvature. This is the substance-energy identity (038)
in its sharpest form: the frustration floor is not incidental to
flatness -- it is flatness's PRICE, and both the price and the
mixture are functions of arccos(1/4) alone.

## The 4D Wedge-Ring Lab (numerical face)

Relaxed spring energy of n regular 4-simplices sharing a fixed unit
triangle hinge (scipy BFGS, the 041 pattern lifted to R^4):

```text
{elines}
```

Strict minimum at n = 5 with positive residual: 4D frustration is
real and measured, one dimension up from 041 E2.

## What This Does NOT Settle

```text
- realizability: which hinge fractions actual periodic 4D
  triangulations achieve (mixture_realizability_050; the natural
  cross-check is the coordination statistics of 4D Delaunay
  complexes) -- joint with O-P10-5.
- the (3+1) question: the SPATIAL 3D packing (edge hinges,
  arccos(1/3), all-positive ground deficits at n = 5) and the
  Euclidean-4D packing (triangle hinges, arccos(1/4), mixed-sign
  ground hinges) are different objects; which the Lorentzian vacuum
  instantiates belongs to O-P10-4.
- no observable moves: the mixture is a structural (sub-Planckian)
  statement; its long-wavelength shadow is exactly the flat, EH-
  responding vacuum already derived.
```

## Ledger

```text
derivation:  ground_coordination_4d_050
satisfies:   o_p10_2_resolved_meanfield_050 (O-P10-2 at mean-field)
opens:       mixture_realizability_050 (joint with O-P10-5)
depends on:  lorentzian_4d_lift_043, frustration_relaxation_lab_041,
             p10_adoption_record_044
watch:       ground-state isotropy (guards 049's selector closure):
             the mixture must not order anisotropically -- a face for
             the O-P10-5 lab.
```
"""
    report_path.write_text(report)
    return report_path


def main() -> None:
    header("Derivation 050: The 4D Ground Coordination (O-P10-2)")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    deltas = check_1_deficit_ladder(failures)
    check_2_single_coordination_ranking(deltas, failures)
    x4, nbar, floor = check_3_flatness_mixture(deltas, failures)
    energies = check_4_wedge_ring_lab(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 050: FAILED")
    print("  O-P10-2 RESOLVED AT MEAN-FIELD: the flat 4D ground state is a")
    print("  forced {4, 5} mixture -- x_4 = 5 - 2 pi/arccos(1/4) = 0.2332,")
    print("  mean coordination 4.7668, exact and parameter-free. Flatness is")
    print("  bought with frustration energy (the 038 identity, sharpest form).")
    print("  Opened: mixture_realizability_050 (joint with O-P10-5).")

    record(ns, x4, nbar, floor, energies)
    report_path = write_report(x4, nbar, floor, energies)
    print(f"[INFO] report written: {report_path}")
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
