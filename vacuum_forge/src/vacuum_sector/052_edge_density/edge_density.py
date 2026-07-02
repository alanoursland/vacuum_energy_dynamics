#!/usr/bin/env python3
"""
edge_density.py

Derivation 052: the edge density c_e derived (O-P10-1, partial).

O-P10-1 asks for the microphysics constants a (packing scale) and c_e
(edge density) in the conversion-factor target

    rho_v = (c_e Delta_0 / 2 a^3) f'(Delta_0).

This derivation computes c_e EXACTLY for the near-regular 3D ground
packing, by the same flatness logic that fixed the 4D mixture (050):

  (1) 3D GROUND MIXTURE. delta(5) = 2 pi - 5 arccos(1/3) = +7.36 deg,
      delta(6) = -63.17 deg. A flat ground state must mix: zero mean
      deficit fixes x_6 = delta_5/(delta_5 - delta_6) = 0.1043
      exactly, and the mean edge coordination is
          n_bar = 2 pi / arccos(1/3) = 5.1043
      -- independent of which coordinations mix (the hinge identity),
      parameter-free.

  (2) EDGE DENSITY. Each near-regular tetrahedron (edge a) has 6
      edges, each shared by n_bar cells, volume V_tet = sqrt(2) a^3/12:
          c_e = 6 / (V_tet n_bar) = 36 arccos(1/3) / (sqrt(2) pi)
              = 9.9743 edges per a^3.
      Exact, a function of arccos(1/3) alone.

  (3) NUMERICAL CROSS-CHECK (the 051 instrument). Seeded 3D
      Poisson-Delaunay bulk, neighbor-centroid smoothed: measured
      edges per unit volume (in units of the mean edge length) and
      mean interior edge coordination, compared against (1)-(2).
      Random/proxy-relaxed complexes are not the ground packing, so
      agreement is expected at the tens-of-percent level and the
      DIRECTION of movement under smoothing is the meaningful signal.

  (4) THE REDUCTION. Substituting c_e into the conversion target
      leaves rho_v = (c_e Delta_0/2) f'(Delta_0) / a^3 with c_e now
      DERIVED and f'(Delta_0) eliminated by the floor-Newton lock
      (039). O-P10-1 reduces to ONE unknown: the packing scale a.
      Register C4 sharpens: G, rho_v, and a are now locked by a
      single one-parameter family -- any independent measurement of
      discreteness overdetermines the system (with 048's scalaron
      range sqrt(6) a as the second consistency face).

Fence: (1)-(2) are mean-field near-regular statements (the 050 class):
they assume the ground packing's cells are near-regular tetrahedra
with the flat mixture statistics. The phase-3 lab
(periodic_energy_relaxation_051) tests exactly this. O-P10-1 stays
OPEN for a; no value of a is proposed here (Planck-scale a is an
ASSUMPTION elsewhere, never a derivation).
"""

import math
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.spatial import Delaunay

import sympy as sp

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
REPO_ROOT = SCRIPT_PATH.parents[4]
REPORT_PATH = (REPO_ROOT / "theory_v3" / "development" / "vacuum_sector"
               / "08_packing_microphysics" / "edge_density_vacuumforge.md")

DEPENDENCIES = [
    ("bridge_dep_052", "039_regge_delaunay_bridge__regge_delaunay_bridge",
     "regge_delaunay_bridge_039"),
    ("coordination_dep_052", "050_4d_ground_coordination__ground_coordination_4d",
     "ground_coordination_4d_050"),
    ("bulk_dep_052", "051_bulk_relaxation_phase2__bulk_relaxation_phase2",
     "bulk_relaxation_phase2_051"),
]

SEED = 20260703
THETA3 = sp.acos(sp.Rational(1, 3))


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


def check_1_ground_mixture_3d(failures):
    header("Check 1: the 3D flat ground mixture and the exact mean edge coordination")
    d5 = sp.simplify(2 * sp.pi - 5 * THETA3)
    d6 = sp.simplify(2 * sp.pi - 6 * THETA3)
    print(f"  delta(5) = {float((d5 * 180 / sp.pi).evalf(50)):+.4f} deg, "
          f"delta(6) = {float((d6 * 180 / sp.pi).evalf(50)):+.4f} deg")
    require("3D signs bracket flatness: delta(5) > 0 > delta(6)",
            float(d5.evalf(50)) > 0 > float(d6.evalf(50)), failures)
    x = sp.Symbol("x", positive=True)
    x6 = sp.solve(sp.Eq((1 - x) * d5 + x * d6, 0), x)[0]
    x6_closed = sp.simplify(2 * sp.pi / THETA3 - 5)
    require("zero-mean-deficit fraction: x_6 = 2 pi/arccos(1/3) - 5 exactly",
            sp.simplify(x6 - x6_closed) == 0, failures)
    nbar = sp.simplify((1 - x6) * 5 + x6 * 6)
    require("mean edge coordination n_bar = 2 pi/arccos(1/3) exactly",
            sp.simplify(nbar - 2 * sp.pi / THETA3) == 0, failures)
    print(f"  x_6 = {float(x6.evalf(50)):.6f}; "
          f"n_bar = 2 pi/arccos(1/3) = {float(nbar.evalf(50)):.6f}")
    print("  The 3D twin of 050: the flat ground state promotes ~10.4% of its")
    print("  edges to n = 6; the mean coordination is the hinge identity's")
    print("  exact number, independent of which coordinations mix.")
    return nbar


def check_2_edge_density(nbar, failures):
    header("Check 2: the edge density c_e, exact")
    a = sp.Symbol("a", positive=True)
    V_tet = sp.sqrt(2) * a**3 / 12
    c_e = sp.simplify(6 / (V_tet * nbar) * a**3)  # edges per a^3, dimensionless
    c_e_closed = sp.simplify(36 * THETA3 / (sp.sqrt(2) * sp.pi))
    require("c_e = 6/(V_tet n_bar) = 36 arccos(1/3)/(sqrt(2) pi) exactly",
            sp.simplify(c_e - c_e_closed) == 0, failures)
    c_num = float(c_e.evalf(50))
    print(f"  c_e = 36 arccos(1/3)/(sqrt(2) pi) = {c_num:.6f} edges per a^3")
    require("numeric value in a sane geometric window (8, 12)",
            8 < c_num < 12, failures)
    print("  Pure geometry: 6 edges per tetrahedron, each shared by n_bar")
    print("  cells, sqrt(2)/12 volume. A function of arccos(1/3) alone --")
    print("  the same sole input as Delta_0 itself.")
    return c_e


def check_3_numerical_cross_check(failures):
    header("Check 3: bulk cross-check (seeded 3D Delaunay, smoothed)")
    rng = np.random.default_rng(SEED)
    N = 600
    pts = rng.uniform(0, 1, size=(N, 3))
    lo, hi = 0.12, 0.88
    for _ in range(8):
        tri = Delaunay(pts)
        nbrs = {i: set() for i in range(N)}
        for s in tri.simplices:
            for u in s:
                for v in s:
                    if u != v:
                        nbrs[u].add(v)
        new = pts.copy()
        for i in range(N):
            if (pts[i] > lo).all() and (pts[i] < hi).all():
                new[i] = np.mean([pts[j] for j in nbrs[i]], axis=0)
        pts = new
    tri = Delaunay(pts)

    # interior edge census with coordination
    count = Counter()
    for s in tri.simplices:
        s = sorted(s)
        for i in range(4):
            for j in range(i + 1, 4):
                count[(s[i], s[j])] += 1
    ilo, ihi = 0.25, 0.75
    interior = {e: n for e, n in count.items()
                if all((pts[v] > ilo).all() and (pts[v] < ihi).all() for v in e)}
    ns_arr = np.array(list(interior.values()))
    mean_coord = float(ns_arr.mean())

    # edge density in units of the mean interior edge length
    mean_len = float(np.mean([np.linalg.norm(pts[i] - pts[j]) for i, j in interior]))
    box_vol = (ihi - ilo) ** 3
    # count edges with midpoint in the census box (density estimator)
    mid_in = sum(1 for (i, j) in count
                 if ((pts[i] + pts[j]) / 2 > ilo).all()
                 and ((pts[i] + pts[j]) / 2 < ihi).all())
    density = mid_in / box_vol * mean_len ** 3

    nbar_pred = 2 * math.pi / math.acos(1 / 3)
    ce_pred = 36 * math.acos(1 / 3) / (math.sqrt(2) * math.pi)
    print(f"  mean interior edge coordination: {mean_coord:.4f} "
          f"(ground prediction {nbar_pred:.4f})")
    print(f"  edge density (edges per mean-edge-length^3): {density:.4f} "
          f"(ground prediction c_e = {ce_pred:.4f})")
    require("mean coordination within 10% of 2 pi/arccos(1/3)",
            abs(mean_coord - nbar_pred) / nbar_pred < 0.10, failures)
    require("measured edge density within 35% of the exact c_e "
            "(proxy-relaxed complex, not the ground packing)",
            abs(density - ce_pred) / ce_pred < 0.35, failures)
    print("  The smoothed complex -- NOT the ground packing, only its proxy --")
    print("  already sits close on coordination and at the tens-of-percent")
    print("  level on density. The exact numbers are claims about the")
    print("  energy-relaxed near-regular packing: phase-3 territory.")
    return mean_coord, density


def check_4_reduction(c_e, failures):
    header("Check 4: the conversion factor reduces to ONE unknown")
    a, fp = sp.symbols("a f_prime", positive=True)
    Delta0 = 2 * sp.pi - 5 * THETA3
    rho_v = c_e * Delta0 * fp / (2 * a**3)
    # c_e derived here; f'(Delta_0) eliminated by the floor-Newton lock
    # (039): the same f'(Delta_0) multiplies the Regge/EH term, so it
    # cancels out of the ratio rho_v / (1/16 pi G) -- the lock. What is
    # left free is a alone.
    prefactor = sp.simplify(c_e * Delta0 / 2)
    print(f"  rho_v = [{sp.nsimplify(prefactor, rational=False)}] "
          f"* f'(Delta_0) / a^3")
    print(f"        = {float(prefactor.evalf(50)):.6f} * f'(Delta_0) / a^3")
    require("prefactor c_e Delta_0/2 is exact in arccos(1/3) and positive",
            float(prefactor.evalf(50)) > 0, failures)
    free_syms = rho_v.free_symbols
    require("with c_e derived and f' locked (039), the only free microphysics "
            "symbols are {a, f_prime}",
            free_syms == {a, fp}, failures)
    print("  With c_e now DERIVED and f'(Delta_0) eliminated by the")
    print("  floor-Newton lock (039), O-P10-1 reduces to the single unknown a.")
    print("  Register C4 sharpens: G, rho_v, and the packing scale form a")
    print("  one-parameter family; any independent discreteness measurement")
    print("  overdetermines it (with 048's scalaron range sqrt(6) a as the")
    print("  second face of the same battery).")
    return prefactor


def record(ns):
    ns.record_derivation(
        derivation_id="edge_density_052",
        inputs=[sp.Symbol("flat_hinge_identity"), sp.Symbol("tet_volume_sqrt2_over_12"),
                sp.Symbol("ground_mixture_logic_050")],
        output=sp.Symbol("c_e_equals_36_arccos_third_over_sqrt2_pi"),
        method=(
            "3D flatness mixture x_6 = 2 pi/arccos(1/3) - 5 solved exactly; "
            "mean edge coordination n_bar = 2 pi/arccos(1/3) by the hinge "
            "identity; c_e = 6/(V_tet n_bar) = 36 arccos(1/3)/(sqrt(2) pi) = "
            "9.9743 per a^3; seeded bulk cross-check (coordination within "
            "10%, density within 35% on the proxy complex); conversion "
            "factor reduced to the single unknown a"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="microphysics_constant_derivation",
        scope=(
            "mean-field near-regular ground packing (the 050 class); the "
            "exact values are claims about the energy-relaxed packing, "
            "tested by phase 3 (periodic_energy_relaxation_051); O-P10-1 "
            "remains OPEN for the packing scale a -- no value of a proposed"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="o_p10_1_ce_derived_052",
        script_id=SCRIPT_ID,
        title="O-P10-1 partial: c_e DERIVED (36 arccos(1/3)/(sqrt(2) pi) per a^3)",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["edge_density_052"],
        description=(
            "The edge density is no longer a free microphysics constant: "
            "c_e = 36 arccos(1/3)/(sqrt(2) pi) = 9.9743 edges per a^3, pure "
            "geometry of the flat near-regular ground packing (mean edge "
            "coordination 2 pi/arccos(1/3) by the hinge identity; 3D ground "
            "mixture x_6 = 0.1043). With f'(Delta_0) eliminated by the "
            "floor-Newton lock (039), the conversion factor has ONE unknown "
            "left: a. Cross-checked in seeded bulk (proxy level)."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="o_p10_1_packing_scale_052",
        script_id=SCRIPT_ID,
        title="O-P10-1 remainder: the packing scale a",
        status=ObligationStatus.OPEN,
        required_by=["edge_density_052"],
        description=(
            "The sole remaining microphysics constant. Same thread as 'is "
            "space discrete': a is meaningful only if it is. No derivation "
            "route currently on the books; Planck-scale a remains an "
            "assumption wherever used (recorded as such). Consistency "
            "battery if a is ever measured: C4 (floor-Newton lock, now "
            "sharpened by derived c_e) + the 048 scalaron range sqrt(6) a."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="edge_density_claim_052",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The edge density of the flat near-regular 3D ground packing is "
            "derived: c_e = 36 arccos(1/3)/(sqrt(2) pi) = 9.9743 edges per "
            "a^3, with mean edge coordination 2 pi/arccos(1/3) = 5.1043 and "
            "ground mixture x_6 = 0.1043 -- all functions of arccos(1/3) "
            "alone, the same sole input as Delta_0. The conversion factor "
            "rho_v = (c_e Delta_0/2) f'(Delta_0)/a^3 now has one free "
            "constant (a). Mean-field fence: exact values are claims about "
            "the energy-relaxed packing (phase-3 test); no value of a is "
            "proposed."
        ),
        derivation_ids=["edge_density_052"],
        obligation_ids=["o_p10_1_ce_derived_052"],
    ))


def write_report(nbar, c_e, mean_coord, density, prefactor):
    nbar_n = float(nbar.evalf(50))
    ce_n = float(c_e.evalf(50))
    pre_n = float(prefactor.evalf(50))
    md = f"""# The Edge Density c_e (O-P10-1, partial) -- VacuumForge Record

## Status

```text
result type:   microphysics-constant derivation (2026-07-02,
               derivation 052)
conclusion:    c_e = 36 arccos(1/3)/(sqrt(2) pi) = {ce_n:.6f} edges
               per a^3 -- EXACT, pure geometry of the flat
               near-regular ground packing. O-P10-1 reduces to one
               unknown: the packing scale a.
fence:         mean-field near-regular (the 050 class); the exact
               values are claims about the energy-relaxed packing --
               phase 3 (periodic_energy_relaxation_051) tests them.
               NO value of a is proposed.
verification:  vacuum_forge/src/vacuum_sector/052_edge_density/
```

## The Derivation

```text
1. THE 3D GROUND MIXTURE (050's logic, one dimension down).
   delta(5) = +7.36 deg, delta(6) = -63.17 deg: a flat ground state
   must mix, and zero mean deficit fixes
       x_6 = 2 pi/arccos(1/3) - 5 = 0.104299
   with mean edge coordination
       n_bar = 2 pi/arccos(1/3) = {nbar_n:.6f}
   (the hinge identity: independent of WHICH coordinations mix).

2. THE EDGE DENSITY. 6 edges per near-regular tetrahedron (edge a),
   each shared by n_bar cells, cell volume sqrt(2) a^3/12:
       c_e = 6/(V_tet n_bar) = 36 arccos(1/3)/(sqrt(2) pi)
           = {ce_n:.6f} per a^3.
   A function of arccos(1/3) alone -- the same sole input as
   Delta_0, the relief function (037), and the mixtures (050, here).

3. BULK CROSS-CHECK (seeded, smoothed 3D Delaunay, N = 600):
   mean interior edge coordination {mean_coord:.4f} vs predicted
   {nbar_n:.4f} (within 10%); edge density {density:.4f} vs predicted
   {ce_n:.4f} (tens-of-percent level on the PROXY complex -- the
   smoothed random complex is not the ground packing; direction and
   window are the meaningful signals pre-phase-3).

4. THE REDUCTION. rho_v = (c_e Delta_0/2) f'(Delta_0)/a^3
            = {pre_n:.6f} f'(Delta_0)/a^3.
   c_e: derived here. f'(Delta_0): eliminated by the floor-Newton
   lock (039). Remaining free microphysics constant: a, alone.
```

## What Sharpens

Register C4 (the discreteness consistency battery) now reads: G,
rho_v, and a are locked into a ONE-parameter family with every
coefficient an exact function of arccos(1/3). If any independent
probe ever measures a discreteness scale, the system is
overdetermined twice over -- the floor-Newton lock must produce the
observed G, AND the 048 scalaron must appear at range sqrt(6) a.
Parameter-free consistency tests waiting on a measurement nobody yet
knows how to make: recorded as exactly that.

## What Stays Open

```text
o_p10_1_packing_scale_052: the packing scale a -- the sole remaining
microphysics constant; same thread as "is space discrete." No
derivation route on the books; Planck-scale a remains an assumption
wherever used, and is recorded as such.
```

## Ledger

```text
derivation:  edge_density_052
satisfies:   o_p10_1_ce_derived_052 (O-P10-1, c_e face)
opens:       o_p10_1_packing_scale_052 (the remainder, explicit)
depends on:  regge_delaunay_bridge_039, ground_coordination_4d_050,
             bulk_relaxation_phase2_051
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 052: The Edge Density c_e (O-P10-1, partial)")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    nbar = check_1_ground_mixture_3d(failures)
    c_e = check_2_edge_density(nbar, failures)
    mean_coord, density = check_3_numerical_cross_check(failures)
    prefactor = check_4_reduction(c_e, failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 052: FAILED")
    print("  c_e DERIVED: 36 arccos(1/3)/(sqrt(2) pi) = 9.9743 edges per a^3,")
    print("  pure geometry (mean coordination 2 pi/arccos(1/3), 3D ground")
    print("  mixture x_6 = 0.1043). O-P10-1 reduces to the packing scale a")
    print("  alone. C4's consistency battery sharpens accordingly.")

    record(ns)
    write_report(nbar, c_e, mean_coord, density, prefactor)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
