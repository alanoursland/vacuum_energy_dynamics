#!/usr/bin/env python3
"""
wedge_strain_definition.py

Derivation 059: how the angle gap becomes stored strain in a flat
wedge (09_maxwell_probe, stage 3 prerequisite; p10_wedge_strain_definition).

Trial energy (authorized 2026-11-24 for the wedge; K explicit, NOT
fitted). For a hinge h with incident dihedral angles theta_i,

    x_i = theta_i - arccos(1/3)          (change from the preferred angle)
    E_h = (K / 2) sum_i x_i^2            (at fixed hinge length)

Flat closure of an interior hinge requires sum_i theta_i = 2 pi, i.e.
for five tetrahedra sum_i x_i = Delta_0 = 2 pi - 5 arccos(1/3). Then,
exactly,

    E_h = K Delta_0^2 / 10 + (K / 2) sum_i (x_i - Delta_0 / 5)^2 .

Two quantities are kept distinct throughout:
    Delta_0  the mismatch of the PREFERRED arrangement (a constant);
    delta_h  the Regge deficit 2 pi - sum of ACTUAL dihedrals.
Every closed ring below has delta_h = 0 exactly, yet stores energy.

Six experiments, all on explicit 3D coordinates (angles are MEASURED
from the geometry, not assigned):

  E1. THE OPEN RING. Five regular unit tetrahedra glued around a unit
      hinge: every hub dihedral is arccos(1/3), E_h = 0, and the last
      face misses the first by exactly Delta_0.

  E2. THE SYMMETRIC CLOSED RING. Closing the ring in flat space: every
      hub dihedral is 72 deg, the Regge deficit is 0, and
      E_h = K Delta_0^2 / 10 > 0. The gap has left the space around the
      edge; its cost is in the shapes of the five tetrahedra.

  E3. REDISTRIBUTED CLOSED RINGS (the decisive test). Closed rings with
      angle shifted between tetrahedra: deficit 0 for all, energy
      raised by exactly (K/2) sum (x_i - Delta_0/5)^2. Any function of
      the total deficit alone, f(delta_h), assigns every one of them the
      same value f(0); the trial energy distinguishes them.

  E4. THE MINIMUM. Over all closed rings, E_h is minimized by equal
      sharing (x_i = Delta_0 / 5), by convexity; checked by constrained
      minimization from random starts.

  E5. THE SPRING COMPARISON (no fit). 041's relaxed five-ring spring
      network (E_spring = 0.000649) is re-relaxed; its measured hub
      dihedrals are evaluated in the trial energy, in units of K. K is
      NOT fitted to the spring number: the two models are compared by
      where they put the strain, not by a matched constant.

  E6. EXTENSION: ALL SIX DIHEDRALS (shape-only). In a bulk packing every
      edge is a hinge, so each tetrahedron's six dihedrals all carry
      energy. Minimizing (K/2) sum over all 30 (tetrahedron, edge)
      dihedrals of the closed ring, hinge fixed, shows how much the
      hinge-only value underestimates and how the strain spreads into
      the other edges. Also recorded: the exact per-hinge lower bound
      K delta(n)^2 / (2n) for an interior hinge of coordination n.

Fences: a TRIAL f, adopted for this test; the bulk form and K remain
theory-owner choices. Hinge energy is per unit hinge length; E6 is
shape-only (unweighted). No bulk packing here: the bulk relaxation with
neighbour changes is the next obligation. No EM coupling.
"""

import math
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

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
               / "09_maxwell_probe" / "wedge_strain_definition_vacuumforge.md")

DEPENDENCIES = [
    ("lab_dep_059", "041_frustration_relaxation_lab__frustration_relaxation_lab",
     "frustration_relaxation_lab_041"),
    ("packing_dep_059", "057_periodic_spring_control__periodic_spring_control",
     "periodic_spring_control_057"),
]

THETA0 = math.acos(1 / 3)
DELTA0 = 2 * math.pi - 5 * THETA0
SEED = 20261124
TOL = 1e-12
EDGES6 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


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


# =============================================================================
# Geometry
# =============================================================================


def dihedral(a, b, c, d):
    """Interior dihedral angle of tetrahedron (a, b, c, d) at edge ab."""
    e = (b - a) / np.linalg.norm(b - a)
    u = (c - a) - ((c - a) @ e) * e
    v = (d - a) - ((d - a) @ e) * e
    return math.atan2(np.linalg.norm(np.cross(u, v)), float(u @ v))


def tet_dihedrals(P):
    """The six dihedrals of a tetrahedron, one per edge (EDGES6 order)."""
    out = []
    for i, j in EDGES6:
        k, l = [m for m in range(4) if m not in (i, j)]
        out.append(dihedral(P[i], P[j], P[k], P[l]))
    return np.array(out)


A = np.array([0.0, 0.0, -0.5])
B = np.array([0.0, 0.0, 0.5])
R_REG = math.sqrt(3) / 2      # ring radius making the spokes unit length


def ring_vertices(azimuths, radius=R_REG):
    return [np.array([radius * math.cos(p), radius * math.sin(p), 0.0]) for p in azimuths]


def hub_angles(ring, closed=True):
    n = len(ring) if closed else len(ring) - 1
    return np.array([dihedral(A, B, ring[i], ring[(i + 1) % len(ring)]) for i in range(n)])


def hinge_energy_over_K(theta):
    x = np.asarray(theta) - THETA0
    return 0.5 * float(x @ x)


def predicted_over_K(theta):
    x = np.asarray(theta) - THETA0
    return DELTA0 ** 2 / 10 + 0.5 * float(((x - DELTA0 / 5) ** 2).sum())


def regge_deficit(theta):
    return 2 * math.pi - float(np.sum(theta))


# =============================================================================
# Experiments
# =============================================================================


def experiment_1_open(failures):
    header("E1: the open ring -- five regular tetrahedra around a unit hinge")
    az = [i * THETA0 for i in range(6)]
    ring = ring_vertices(az)
    edges_ok = True
    for i in range(5):
        P = [A, B, ring[i], ring[i + 1]]
        lens = [np.linalg.norm(P[a] - P[b]) for a, b in EDGES6]
        edges_ok &= np.allclose(lens, 1.0, atol=TOL)
    theta = hub_angles(ring, closed=False)
    gap = dihedral(A, B, ring[5], ring[0])
    gap = 2 * math.pi - float(theta.sum())
    print(f"    hub dihedrals: {np.round(np.degrees(theta), 10).tolist()} deg")
    print(f"    E_h / K = {hinge_energy_over_K(theta):.3e}; open gap = "
          f"{math.degrees(gap):.10f} deg (Delta_0 = {math.degrees(DELTA0):.10f} deg)")
    require("all five tetrahedra regular (every edge unit length)", edges_ok, failures)
    require("every hub dihedral = arccos(1/3); E_h = 0",
            np.allclose(theta, THETA0, atol=TOL) and hinge_energy_over_K(theta) < TOL, failures)
    require("the last face misses the first by exactly Delta_0",
            abs(gap - DELTA0) < TOL and np.linalg.norm(ring[5] - ring[0]) > 0.1, failures)
    return theta, gap


def experiment_2_symmetric(failures):
    header("E2: the symmetric closed ring -- flat closure, zero deficit, stored strain")
    ring = ring_vertices([2 * math.pi * i / 5 for i in range(5)])
    theta = hub_angles(ring)
    e = hinge_energy_over_K(theta)
    print(f"    hub dihedrals: {np.round(np.degrees(theta), 10).tolist()} deg")
    print(f"    Regge deficit at the hub = {regge_deficit(theta):.2e}")
    print(f"    E_h / K = {e:.12f}; K Delta_0^2 / 10 / K = {DELTA0 ** 2 / 10:.12f}")
    require("every hub dihedral = 72 deg (each tetrahedron opens by Delta_0 / 5)",
            np.allclose(theta, 2 * math.pi / 5, atol=TOL), failures)
    require("Regge deficit at the hub is exactly 0 (the space around the edge is flat)",
            abs(regge_deficit(theta)) < TOL, failures)
    require("E_h = K Delta_0^2 / 10 > 0: the gap is stored in the tetrahedra's shapes",
            abs(e - DELTA0 ** 2 / 10) < TOL and e > 0, failures)
    return e


def closed_ring_from_shifts(eps, radii=None):
    theta = 2 * math.pi / 5 + np.asarray(eps)
    az = np.concatenate([[0.0], np.cumsum(theta)[:-1]])
    radii = [R_REG] * 5 if radii is None else radii
    return [np.array([r * math.cos(p), r * math.sin(p), z])
            for p, (r, z) in zip(az, [(r, 0.0) if np.isscalar(r) else r for r in radii])]


def experiment_3_redistributed(failures):
    header("E3: redistributed closed rings -- same zero deficit, different stored energy")
    rng = np.random.default_rng(SEED)
    rows = []
    for trial in range(8):
        eps = rng.uniform(-0.15, 0.15, 5)
        eps -= eps.mean()                       # keep the ring closed
        radii = [(rng.uniform(0.6, 1.1), rng.uniform(-0.3, 0.3)) for _ in range(5)]
        ring = closed_ring_from_shifts(eps, radii)
        theta = hub_angles(ring)
        rows.append((regge_deficit(theta), hinge_energy_over_K(theta), predicted_over_K(theta),
                     float(np.max(np.abs(theta - 2 * math.pi / 5 - eps)))))
    print("    trial  Regge deficit   E_h/K (measured)   prediction      f(total deficit)")
    for n, (d, e, p, _) in enumerate(rows):
        print(f"    {n}      {d:+.1e}        {e:.12f}     {p:.12f}   f(0) (same for all)")
    require("every redistributed ring is closed: Regge deficit 0 (to 1e-12)",
            all(abs(r[0]) < TOL for r in rows), failures)
    require("measured hub angles equal the construction (angles read from coordinates)",
            all(r[3] < 1e-10 for r in rows), failures)
    require("E_h = K Delta_0^2/10 + (K/2) sum (x_i - Delta_0/5)^2 exactly",
            all(abs(r[1] - r[2]) < TOL for r in rows), failures)
    require("energy rises above the symmetric value whenever angle is redistributed",
            all(r[1] > DELTA0 ** 2 / 10 + 1e-6 for r in rows), failures)
    spread = max(r[1] for r in rows) - min(r[1] for r in rows)
    require(f"zero-deficit rings store different energies (spread {spread:.3e} K): no function "
            "of the total deficit alone can represent them", spread > 1e-4, failures)
    return rows


def experiment_4_minimum(failures):
    header("E4: the minimum over closed rings is equal sharing")
    rng = np.random.default_rng(SEED + 1)
    best = []
    for _ in range(6):
        x0 = rng.uniform(-0.5, 0.5, 5) + THETA0
        res = minimize(hinge_energy_over_K, x0,
                       constraints=[{"type": "eq", "fun": lambda t: float(np.sum(t)) - 2 * math.pi}],
                       method="SLSQP", options={"ftol": 1e-15, "maxiter": 500})
        best.append(res.x)
    spread = max(float(np.max(np.abs(b - 2 * math.pi / 5))) for b in best)
    emin = min(hinge_energy_over_K(b) for b in best)
    print(f"    constrained minima: max |theta_i - 72 deg| = {math.degrees(spread):.2e} deg; "
          f"E_min / K = {emin:.12f}")
    require("from random starts, the closed-ring minimum shares the gap equally",
            spread < 1e-6 and abs(emin - DELTA0 ** 2 / 10) < 1e-12, failures)
    # symbolic: Lagrange condition gives x_i = Delta_0 / 5
    xs = sp.symbols("x1:6")
    lam, D = sp.symbols("lambda Delta_0")
    Lg = sum(x ** 2 for x in xs) / 2 - lam * (sum(xs) - D)
    sol = sp.solve([sp.diff(Lg, x) for x in xs] + [sum(xs) - D], list(xs) + [lam], dict=True)[0]
    emin_sym = sp.simplify(sum(sol[x] ** 2 for x in xs) / 2)
    print(f"    Lagrange: x_i = {sol[xs[0]]}, E_min / K = {emin_sym}")
    require("symbolic Lagrange solution: x_i = Delta_0/5, E_min = K Delta_0^2/10",
            all(sp.simplify(sol[x] - D / 5) == 0 for x in xs)
            and sp.simplify(emin_sym - D ** 2 / 10) == 0, failures)
    return emin


def spring_ring_relax():
    """041's five-ring spring network, re-relaxed with its own conventions."""
    n = 5
    edges = [(0, 1)] + [(0, 2 + k) for k in range(n)] + [(1, 2 + k) for k in range(n)] \
        + [(2 + k, 2 + (k + 1) % n) for k in range(n)]
    h, r0 = 0.5, 0.85
    x0 = np.vstack([[0, 0, h], [0, 0, -h]]
                   + [[r0 * math.cos(2 * math.pi * k / n), r0 * math.sin(2 * math.pi * k / n), 0]
                      for k in range(n)]).astype(float)

    def f(z):
        x = z.reshape(-1, 3)
        return sum((np.linalg.norm(x[i] - x[j]) - 1) ** 2 for i, j in edges)

    def g(z):
        x = z.reshape(-1, 3)
        out = np.zeros_like(x)
        for i, j in edges:
            d = x[i] - x[j]
            l = np.linalg.norm(d)
            c = 2 * (l - 1) / l * d
            out[i] += c
            out[j] -= c
        return out.ravel()

    res = minimize(f, x0.ravel(), jac=g, method="BFGS", options={"gtol": 1e-10, "maxiter": 20000})
    return float(res.fun), res.x.reshape(-1, 3), edges


def experiment_5_spring(failures):
    header("E5: the spring comparison (041 five-ring; K NOT fitted)")
    E, x, edges = spring_ring_relax()
    a, b = x[0], x[1]
    theta = np.array([dihedral(a, b, x[2 + k], x[2 + (k + 1) % 5]) for k in range(5)])
    lens = np.array([np.linalg.norm(x[i] - x[j]) for i, j in edges])
    others = []
    for k in range(5):
        others += list(tet_dihedrals([a, b, x[2 + k], x[2 + (k + 1) % 5]])[1:])
    others = np.array(others)
    print(f"    spring energy E = {E:.6f} (041 E2: 0.000649); edge lengths "
          f"{lens.min():.5f} .. {lens.max():.5f}")
    print(f"    hub dihedrals: {np.round(np.degrees(theta), 8).tolist()} deg; deficit "
          f"{regge_deficit(theta):.1e}")
    print(f"    trial hinge energy of the spring configuration: E_h / K = "
          f"{hinge_energy_over_K(theta):.10f} (= Delta_0^2/10 = {DELTA0 ** 2 / 10:.10f})")
    print(f"    the other 25 dihedrals depart from arccos(1/3) by "
          f"{math.degrees(np.abs(others - THETA0).min()):.3f} .. "
          f"{math.degrees(np.abs(others - THETA0).max()):.3f} deg")
    require("041 spring ring reproduced (E = 0.000649 to 6 decimals)",
            abs(E - 0.000649) < 5e-7, failures)
    require("the spring ring is closed and flat at the hub (deficit 0) and shares the gap "
            "equally (72 deg each)",
            abs(regge_deficit(theta)) < 1e-9 and np.allclose(theta, 2 * math.pi / 5, atol=1e-8),
            failures)
    print("  Both models put the hub at 72 deg. The spring model stores the gap in")
    print("  edge-length changes; the trial angle energy stores it in the hinge")
    print("  angles. Matching their totals would require fitting K, which is not")
    print("  done: the comparison is kept as a test, not spent as a calibration.")
    return E, theta, others


def experiment_6_all_dihedrals(failures):
    header("E6: extension -- all six dihedrals of each tetrahedron (shape-only)")

    def energy(z):
        ring = z.reshape(5, 3)
        tot = 0.0
        for k in range(5):
            th = tet_dihedrals([A, B, ring[k], ring[(k + 1) % 5]])
            tot += 0.5 * float(((th - THETA0) ** 2).sum())
        return tot

    z0 = np.array(ring_vertices([2 * math.pi * i / 5 for i in range(5)])).ravel()
    e_sym = energy(z0)
    res = minimize(energy, z0, method="BFGS", options={"gtol": 1e-11, "maxiter": 20000})
    ring = res.x.reshape(5, 3)
    theta = hub_angles(list(ring))
    per = [tet_dihedrals([A, B, ring[k], ring[(k + 1) % 5]]) for k in range(5)]
    hub_share = 0.5 * float(((theta - THETA0) ** 2).sum())
    radius = float(np.linalg.norm(ring[:, :2], axis=1).mean())
    print(f"    start (radius sqrt(3)/2, symmetric): E_all / K = {e_sym:.8f}")
    print(f"    minimum: E_all / K = {res.fun:.8f}; hub part {hub_share:.8f} "
          f"(hinge-only value Delta_0^2/10 = {DELTA0 ** 2 / 10:.8f}); ring radius {radius:.5f}")
    print(f"    hub dihedrals at the minimum: {np.round(np.degrees(theta), 6).tolist()} deg; "
          f"deficit {regge_deficit(theta):.1e}")
    print(f"    each tetrahedron's six dihedrals (deg): "
          f"{np.round(np.degrees(per[0]), 4).tolist()}")
    require("all-dihedral minimum is a closed flat ring (hub deficit 0) with equal 72 deg hubs",
            abs(regge_deficit(theta)) < 1e-9 and np.allclose(theta, 2 * math.pi / 5, atol=1e-6),
            failures)
    require("counting all six dihedrals raises the stored energy above the hinge-only value",
            res.fun > DELTA0 ** 2 / 10 * 1.01, failures)

    header("E6b: per-hinge lower bound by coordination (exact)")
    rows = []
    for n in range(3, 8):
        gap = 2 * math.pi - n * THETA0
        rows.append((n, gap, gap ** 2 / (2 * n)))
        print(f"    n = {n}: preferred gap 2 pi - n arccos(1/3) = {math.degrees(gap):+9.4f} deg; "
              f"min E_h / K = {gap ** 2 / (2 * n):.8f}")
    require("n = 5 has the smallest per-hinge lower bound (the ground coordination)",
            min(rows, key=lambda r: r[2])[0] == 5, failures)
    return res.fun, hub_share, per[0], rows


# =============================================================================
# Record + report
# =============================================================================


def record(ns):
    ns.record_derivation(
        derivation_id="wedge_strain_definition_059",
        inputs=[sp.Symbol("trial_f_quadratic_dihedral"), sp.Symbol("Delta_0"),
                sp.Symbol("five_tetrahedron_wedge")],
        output=sp.Symbol("angle_gap_stored_as_strain_in_flat_wedge"),
        method=(
            "explicit 3D wedges with angles measured from coordinates: open regular ring, "
            "symmetric closed ring, random redistributed closed rings (random radii and "
            "heights), constrained minimization and symbolic Lagrange solution, the 041 "
            "spring ring re-relaxed and evaluated in units of K, and an all-six-dihedral "
            "shape-only extension; per-hinge coordination bound"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="exact_identity_and_numerical_witness",
        scope=(
            "TRIAL f = (K/2) sum (theta_i - arccos(1/3))^2 per hinge, K explicit and not "
            "fitted; single wedge; E6 shape-only; no bulk packing, no neighbour changes, no "
            "EM coupling"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p10_wedge_strain_definition",
        script_id=SCRIPT_ID,
        title="How the preferred angle gap becomes stored strain (wedge, trial f)",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["wedge_strain_definition_059"],
        description=(
            "With the trial per-hinge energy (K/2) sum x_i^2, flat closure forces "
            "sum x_i = Delta_0 and stores at least K Delta_0^2/10 per five-fold hinge at zero "
            "Regge deficit; redistributed zero-deficit rings store more, exactly as "
            "predicted, which no function of the total deficit alone can represent."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p10_bulk_relaxation_059",
        script_id=SCRIPT_ID,
        title="Stage 3: bulk relaxation with the trial angle energy, against the 057 control",
        status=ObligationStatus.OPEN,
        required_by=["wedge_strain_definition_059"],
        description=(
            "Relax periodic packings with the all-dihedral trial energy at fixed box, "
            "matched to the 057 spring control (same starts); then allow neighbour changes "
            "(retriangulation or bistellar moves) and test whether a floor energy per "
            "volume survives across seeds, sizes and starting arrangements, and whether its "
            "directional fabric washes out at large scale."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="wedge_strain_definition_claim_059",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "In a five-tetrahedron wedge closed in flat space, the Regge deficit at the hinge "
            "is zero while the trial angle energy stores K Delta_0^2/10 at minimum, attained "
            "by equal sharing; rings with the same zero deficit but redistributed angles "
            "store exactly (K/2) sum (x_i - Delta_0/5)^2 more. An energy depending only on "
            "the total deficit cannot represent this. Trial f; K not fitted."
        ),
        derivation_ids=["wedge_strain_definition_059"],
        obligation_ids=["p10_wedge_strain_definition"],
    ))


def write_report(open_gap, e_sym, rows3, emin, spring, ext):
    E_sp, theta_sp, others_sp = spring
    e_all, hub_share, per, bound = ext
    tab3 = "\n".join(f"    {n}      {d:+.1e}      {e:.10f}     {p:.10f}"
                     for n, (d, e, p, _) in enumerate(rows3))
    tabb = "\n".join(f"    n = {n}: gap {math.degrees(g):+9.4f} deg   min E_h / K = {b:.8f}"
                     for n, g, b in bound)
    md = f"""# VacuumForge: How the Angle Gap Becomes Stored Strain (the Wedge)

## Status

```text
result type:   exact identity + numerical witnesses (2026-11-24,
               derivation 059); TRIAL energy, K explicit, not fitted
conclusion:    closing five tetrahedra around an edge in flat space
               removes the gap from the space (Regge deficit 0) but
               not from the tetrahedra: the trial angle energy stores
               at least K Delta_0^2 / 10, and zero-deficit rings with
               redistributed angles store exactly the predicted extra.
satisfies:     p10_wedge_strain_definition (09 charter, stage 3
               prerequisite)
opens:         p10_bulk_relaxation_059
verification:  vacuum_forge/src/vacuum_sector/059_wedge_strain_definition/
```

## The Trial Energy

For a hinge h with incident dihedral angles theta_i (angles measured
from coordinates throughout):

```text
x_i  = theta_i - arccos(1/3)          change from the preferred angle
E_h  = (K / 2) sum_i x_i^2            at fixed hinge length, K > 0
flat closure (5 tetrahedra):  sum_i x_i = Delta_0 = {math.degrees(DELTA0):.6f} deg
=>   E_h = K Delta_0^2 / 10 + (K / 2) sum_i (x_i - Delta_0 / 5)^2
```

Delta_0 is the mismatch of the preferred arrangement; the Regge
deficit delta_h = 2 pi - sum theta_i is a property of the actual
configuration. Every closed ring below has delta_h = 0.

## Measured Results

```text
E1. OPEN RING. Five regular unit tetrahedra: hub dihedrals all
    arccos(1/3), E_h = 0, open gap {math.degrees(open_gap):.10f} deg = Delta_0.

E2. SYMMETRIC CLOSED RING. Hub dihedrals all 72 deg; Regge deficit 0;
    E_h / K = {e_sym:.12f} = Delta_0^2 / 10.

E3. REDISTRIBUTED CLOSED RINGS (random azimuth shifts, radii, heights):
    trial  deficit      E_h / K          prediction
{tab3}
    All closed and flat at the hub; all agree with the prediction to
    1e-12; all store more than the symmetric ring. A function of the
    total deficit alone gives every one of them the same value f(0).

E4. MINIMUM. Constrained minimization from random starts and the
    symbolic Lagrange solution: x_i = Delta_0 / 5, E_min / K =
    {emin:.12f}.

E5. SPRING COMPARISON (041 five-ring, re-relaxed; K NOT fitted).
    E_spring = {E_sp:.6f}. Its hub dihedrals are 72 deg each (closed, flat,
    equal sharing), so its trial hinge energy is K Delta_0^2/10. The
    spring model holds the gap in edge-length changes; its other 25
    dihedrals depart from arccos(1/3) by
    {math.degrees(np.abs(others_sp - THETA0).min()):.3f} .. {math.degrees(np.abs(others_sp - THETA0).max()):.3f} deg.

E6. EXTENSION: ALL SIX DIHEDRALS (shape-only, hinge fixed). Minimum
    E_all / K = {e_all:.8f}, of which the hub carries {hub_share:.8f}
    (hinge-only value {DELTA0 ** 2 / 10:.8f}). Hubs stay at 72 deg with
    zero deficit; the rest of the strain spreads into the other five
    edges of each tetrahedron. Dihedrals of one tetrahedron at the
    minimum (deg): {np.round(np.degrees(per), 4).tolist()}.
    Per-hinge lower bound for an interior hinge of coordination n:
{tabb}
```

## Reading

- The gap disappears from the space around the edge and reappears in
  the shapes of the five tetrahedra. A surveyor measuring curvature at
  the hub finds zero; the trial energy finds K Delta_0^2 / 10.
- The decisive test is E3: equal zero deficits, unequal energies. Any
  P10 energy written as f(delta_h) of the actual deficit cannot hold
  flat-space strain; the energy has to read the individual angles (or
  an equivalent per-cell shape variable).
- In a bulk packing every edge is a hinge. A tetrahedron's six
  dihedrals are not independent, so opening the hub angle to 72 deg
  pulls the other five below arccos(1/3). E6 shows that counting all
  six raises the stored energy to {e_all / (DELTA0 ** 2 / 10):.2f}x the hinge-only count for
  this wedge. The bulk form should therefore sum over all
  (tetrahedron, edge) dihedrals, weighted by hinge length.
- The spring value 0.000649 is kept as a comparison point. Fitting K
  to it would spend the comparison.

## Fences

```text
- TRIAL f, authorized for this test; the bulk form and K remain the
  theory owner's choices.
- single wedge; E6 is shape-only (unweighted by edge length).
- no bulk packing and no neighbour changes yet:
  p10_bulk_relaxation_059.
- no EM coupling.
```

## Ledger

```text
derivation:  wedge_strain_definition_059
satisfies:   p10_wedge_strain_definition
opens:       p10_bulk_relaxation_059
depends on:  frustration_relaxation_lab_041, periodic_spring_control_057
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 059: How the Angle Gap Becomes Stored Strain (the Wedge)")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    _, open_gap = experiment_1_open(failures)
    e_sym = experiment_2_symmetric(failures)
    rows3 = experiment_3_redistributed(failures)
    emin = experiment_4_minimum(failures)
    spring = experiment_5_spring(failures)
    ext = experiment_6_all_dihedrals(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 059: verification failure")
    print("  The wedge test passes: the angle gap leaves flat space and is stored in")
    print("  the tetrahedra's shapes; the trial energy distinguishes zero-deficit")
    print("  rings that any deficit-only energy would equate. Bulk relaxation next.")

    record(ns)
    write_report(open_gap, e_sym, rows3, emin, spring, ext)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
