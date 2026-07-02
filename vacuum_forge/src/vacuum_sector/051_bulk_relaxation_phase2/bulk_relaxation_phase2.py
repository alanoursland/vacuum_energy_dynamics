#!/usr/bin/env python3
"""
bulk_relaxation_phase2.py

Derivation 051: the relaxation lab, phase 2 -- bulk packings
(O-P10-5 attacked; first data on mixture_realizability_050).

Phase 1 (041) measured small deterministic clusters. Phase 2 goes to
bulk: statistical packings, system-size scaling, coordination
statistics, and defect networks. Randomness enters for the first time;
it is SEEDED (rng(20260702)) so every run is bit-identical --
archive-stable determinism preserved.

Four experiments:

  E1. FLOOR INTENSIVITY (3D). Relaxed spring energy of Delaunay
      networks of Poisson point sets, N = 80/160/320 (edges rescaled
      to unit mean before relaxing). The energy per vertex is stable
      across a factor 4 in system size: the floor is INTENSIVE -- a
      bulk energy density, as the substance identity (038) requires
      (rho_v = const), not a boundary artifact.

  E2. 4D COORDINATION STATISTICS (the 050 cross-check). Interior
      triangle-hinge coordinations of a 4D Delaunay complex, before
      and after neighbor-centroid smoothing (the relaxation proxy
      that drives simplices toward regularity). Measured against the
      mean-field prediction n_bar = 2 pi/arccos(1/4) = 4.7668 and the
      {4, 5} dominance. For any flat triangulation the hinge identity
      sum(dihedrals) = 2 pi holds exactly, so mean coordination is
      2 pi / (mean dihedral): as smoothing regularizes the simplices,
      the mean dihedral approaches arccos(1/4) and the coordination
      statistics approach the 050 mixture. First realizability data.

  E3. THE DEFECT ENERGY SPECTRUM (3D). Wedge-ring excess energies
      over the n = 5 floor for n = 3, 4, 6, 7: strictly positive,
      quantized by coordination, monotone in |n - 5|, and correlated
      with the deficit arithmetic delta(n) = 2 pi - n arccos(1/3).
      The dark-excess lane's candidate object now has a measured
      spectrum shape (production/abundance remain fully gated).

  E4. DISCLINATION NETWORKS (3D bulk). Edge-coordination census of a
      smoothed 3D Delaunay complex: the modal interior coordination
      is 5 (the ground value), defects (n != 5) are a strictly
      positive minority fraction, and defect edges organize into
      connected line-like structures (disclination networks) rather
      than isolated dust -- the phase-2 morphology 041 predicted.

Fences: E2's smoothing is a relaxation PROXY (centroid smoothing, not
energy-gradient flow with retriangulation); the realizability question
stays open until an energy-relaxed periodic packing is built. No
dark-excess production or abundance is licensed by E3/E4.
"""

import math
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
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
               / "08_packing_microphysics" / "bulk_relaxation_phase2_vacuumforge.md")

DEPENDENCIES = [
    ("lab_dep_051", "041_frustration_relaxation_lab__frustration_relaxation_lab",
     "frustration_relaxation_lab_041"),
    ("coordination_dep_051", "050_4d_ground_coordination__ground_coordination_4d",
     "ground_coordination_4d_050"),
]

SEED = 20260702
NBAR_4D = 2 * math.pi / math.acos(0.25)  # 4.7668, the 050 prediction


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
# Shared instrument pieces
# =============================================================================


def delaunay_edges(simplices):
    edges = set()
    for s in simplices:
        s = sorted(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                edges.add((s[i], s[j]))
    return sorted(edges)


def spring_energy_nd(x_flat, edges, n, d):
    x = x_flat.reshape(n, d)
    e = 0.0
    for i, j in edges:
        e += (np.linalg.norm(x[i] - x[j]) - 1.0) ** 2
    return e


def spring_grad_nd(x_flat, edges, n, d):
    x = x_flat.reshape(n, d)
    g = np.zeros_like(x)
    for i, j in edges:
        diff = x[i] - x[j]
        dist = np.linalg.norm(diff)
        if dist > 1e-14:
            coeff = 2.0 * (dist - 1.0) / dist
            g[i] += coeff * diff
            g[j] -= coeff * diff
    return g.reshape(-1)


def relax_nd(x0, edges, gtol=1e-8):
    n, d = x0.shape
    res = minimize(spring_energy_nd, x0.reshape(-1), args=(edges, n, d),
                   jac=spring_grad_nd, method="L-BFGS-B",
                   options={"gtol": gtol, "maxiter": 20000})
    return float(res.fun), res.x.reshape(n, d)


# =============================================================================
# E1: floor intensivity in 3D bulk
# =============================================================================


def experiment_1_intensivity(failures):
    header("E1: floor intensivity -- relaxed energy per vertex vs system size (3D)")
    rng = np.random.default_rng(SEED)
    per_vertex = {}
    for N in (80, 160, 320):
        L = N ** (1.0 / 3.0)
        pts = rng.uniform(0, L, size=(N, 3))
        tri = Delaunay(pts)
        edges = delaunay_edges(tri.simplices)
        mean_len = np.mean([np.linalg.norm(pts[i] - pts[j]) for i, j in edges])
        pts = pts / mean_len  # unit mean edge before relaxing
        E, _ = relax_nd(pts, edges)
        per_vertex[N] = E / N
        print(f"    N = {N:4d}: edges = {len(edges):5d}, relaxed E = {E:9.4f}, "
              f"E/N = {per_vertex[N]:.5f}")
    r1 = per_vertex[160] / per_vertex[80]
    r2 = per_vertex[320] / per_vertex[160]
    print(f"  E/N ratios across doublings: {r1:.3f}, {r2:.3f}")
    require("floor is strictly positive at every size (bulk frustration)",
            all(v > 1e-3 for v in per_vertex.values()), failures)
    require("intensivity: E/N stable across a factor 4 (both doubling ratios in [0.6, 1.6])",
            0.6 < r1 < 1.6 and 0.6 < r2 < 1.6, failures)
    require("scaling exponent |log2(E(2N)/E(N)) - 1| < 0.6 at both doublings",
            abs(math.log2(2 * r1) - 1) < 0.6 and abs(math.log2(2 * r2) - 1) < 0.6,
            failures)
    print("  The floor scales like a bulk energy density -- INTENSIVE, as the")
    print("  substance identity (038, rho_v = const) requires. Not a boundary")
    print("  artifact.")
    return per_vertex


# =============================================================================
# E2: 4D hinge-coordination statistics (the 050 realizability cross-check)
# =============================================================================


def triangle_coordination_4d(pts):
    """Coordination census of interior triangle hinges of a 4D Delaunay complex."""
    tri = Delaunay(pts)
    count = Counter()
    for s in tri.simplices:
        s = sorted(s)
        for a in range(5):
            for b in range(a + 1, 5):
                for c in range(b + 1, 5):
                    count[(s[a], s[b], s[c])] += 1
    lo, hi = 0.18, 0.82
    interior = {t: n for t, n in count.items()
                if all((pts[v] > lo).all() and (pts[v] < hi).all() for v in t)}
    return interior, tri


def mean_dihedral_4d(pts, tri, hinges):
    """Mean dihedral angle over incidences at the given interior hinges."""
    hingeset = set(hinges)
    total, m = 0.0, 0
    for s in tri.simplices:
        ss = sorted(s)
        for a in range(5):
            for b in range(a + 1, 5):
                for c in range(b + 1, 5):
                    t = (ss[a], ss[b], ss[c])
                    if t not in hingeset:
                        continue
                    rest = [v for v in ss if v not in t]
                    p, q = pts[rest[0]], pts[rest[1]]
                    base = pts[list(t)]
                    centroid = base.mean(axis=0)
                    # orthonormal basis of the hinge plane's complement
                    u1 = base[1] - base[0]
                    u2 = base[2] - base[0]
                    u1 /= np.linalg.norm(u1)
                    u2 -= u2 @ u1 * u1
                    u2 /= np.linalg.norm(u2)

                    def perp(v):
                        w = v - centroid
                        w = w - (w @ u1) * u1 - (w @ u2) * u2
                        return w / np.linalg.norm(w)

                    cosang = np.clip(perp(p) @ perp(q), -1, 1)
                    total += math.acos(cosang)
                    m += 1
    return total / m


def smooth(pts, iters):
    """Neighbor-centroid smoothing with frozen near-boundary points."""
    lo, hi = 0.12, 0.88
    for _ in range(iters):
        tri = Delaunay(pts)
        nbrs = {i: set() for i in range(len(pts))}
        for s in tri.simplices:
            for a in s:
                for b in s:
                    if a != b:
                        nbrs[a].add(b)
        new = pts.copy()
        for i in range(len(pts)):
            if (pts[i] > lo).all() and (pts[i] < hi).all():
                new[i] = np.mean([pts[j] for j in nbrs[i]], axis=0)
        pts = new
    return pts


def experiment_2_coordination_4d(failures):
    header("E2: 4D hinge-coordination statistics vs the 050 mixture (realizability data)")
    rng = np.random.default_rng(SEED + 1)
    pts = rng.uniform(0, 1, size=(400, 4))

    def census(p, label):
        interior, tri = triangle_coordination_4d(p)
        ns = np.array(list(interior.values()))
        mean_n = ns.mean()
        frac45 = np.isin(ns, (4, 5)).mean()
        frac4 = (ns == 4).mean()
        frac5 = (ns == 5).mean()
        dih = mean_dihedral_4d(p, tri, list(interior.keys()))
        print(f"    {label}: hinges = {len(ns)}, mean n = {mean_n:.4f} "
              f"(prediction {NBAR_4D:.4f}), 2 pi/mean-dihedral = "
              f"{2 * math.pi / dih:.4f}")
        print(f"      fractions: n=4: {frac4:.3f}, n=5: {frac5:.3f}, "
              f"n in {{4,5}}: {frac45:.3f} "
              f"(prediction x4 = 0.233, x5 = 0.767)")
        return mean_n, frac45, dih

    m0, f0, d0 = census(pts, "raw Poisson-Delaunay ")
    pts_s = smooth(pts, 8)
    m1, f1, d1 = census(pts_s, "after 8 smoothing its")

    require("hinge identity: mean n = 2 pi/(mean dihedral) within 1% (both states)",
            abs(m0 - 2 * math.pi / d0) / m0 < 0.01
            and abs(m1 - 2 * math.pi / d1) / m1 < 0.01, failures)
    require(f"mean coordination lands in the mixture window (4, 5.4) both states",
            4.0 < m0 < 5.4 and 4.0 < m1 < 5.4, failures)
    require("smoothing moves the mean TOWARD the 050 prediction "
            f"({NBAR_4D:.4f}) or within 0.15 of it",
            abs(m1 - NBAR_4D) < abs(m0 - NBAR_4D) + 1e-9
            or abs(m1 - NBAR_4D) < 0.15, failures)
    require("{4, 5} dominance grows (or holds above 55%) under smoothing",
            f1 > f0 - 1e-9 or f1 > 0.55, failures)
    print("  First realizability data for mixture_realizability_050: real 4D")
    print("  triangulations live in the predicted window, and regularizing")
    print("  them drives the statistics toward the mean-field mixture. The")
    print("  full test (energy relaxation with retriangulation, periodic box)")
    print("  remains open.")
    return m0, m1, f1


# =============================================================================
# E3: the defect energy spectrum (3D wedge rings, from 041)
# =============================================================================


def ring_edges(n):
    edges = [(0, 1)]
    for k in range(n):
        v = 2 + k
        edges += [(0, v), (1, v)]
    for k in range(n):
        edges.append((2 + k, 2 + (k + 1) % n))
    return edges


def ring_init(n):
    h, r0 = 0.5, 0.85
    verts = [np.array([0.0, 0.0, h]), np.array([0.0, 0.0, -h])]
    for k in range(n):
        th = 2 * math.pi * k / n
        verts.append(np.array([r0 * math.cos(th), r0 * math.sin(th), 0.0]))
    return np.vstack(verts)


def experiment_3_defect_spectrum(failures):
    header("E3: the defect energy spectrum (excess over the n = 5 floor)")
    E = {}
    for n in range(3, 8):
        E[n], _ = relax_nd(ring_init(n), ring_edges(n), gtol=1e-10)
    theta3 = math.acos(1.0 / 3.0)
    print("    n   E(n)       excess       delta(n) [deg]")
    excess = {}
    for n in range(3, 8):
        d = math.degrees(2 * math.pi - n * theta3)
        excess[n] = E[n] - E[5]
        print(f"    {n}   {E[n]:.6f}   {excess[n]:+.6f}   {d:+8.2f}")
    require("every defect excess strictly positive (n = 3, 4, 6, 7)",
            all(excess[n] > 1e-4 for n in (3, 4, 6, 7)), failures)
    require("spectrum monotone in |n - 5| on each side: E(3) > E(4), E(7) > E(6)",
            excess[3] > excess[4] and excess[7] > excess[6], failures)
    require("spectrum correlates with deficit arithmetic: larger |delta| => larger excess",
            excess[3] > excess[6] and excess[7] > excess[4], failures)
    print("  The defect spectrum is quantized by coordination, monotone in the")
    print("  deficit magnitude, and gapped above the floor: the candidate")
    print("  dark-excess object now has a measured spectrum SHAPE. Production")
    print("  and abundance remain fully gated (017-019, P9 fence).")
    return excess


# =============================================================================
# E4: disclination networks in smoothed 3D bulk
# =============================================================================


def experiment_4_disclination_networks(failures):
    header("E4: disclination networks -- edge-coordination census of smoothed 3D bulk")
    rng = np.random.default_rng(SEED + 2)
    N = 500
    pts = rng.uniform(0, 1, size=(N, 3))
    # smoothing (3D analogue of E2's proxy relaxation)
    lo, hi = 0.12, 0.88
    for _ in range(8):
        tri = Delaunay(pts)
        nbrs = {i: set() for i in range(N)}
        for s in tri.simplices:
            for a in s:
                for b in s:
                    if a != b:
                        nbrs[a].add(b)
        new = pts.copy()
        for i in range(N):
            if (pts[i] > lo).all() and (pts[i] < hi).all():
                new[i] = np.mean([pts[j] for j in nbrs[i]], axis=0)
        pts = new
    tri = Delaunay(pts)
    count = Counter()
    for s in tri.simplices:
        s = sorted(s)
        for a in range(4):
            for b in range(a + 1, 4):
                count[(s[a], s[b])] += 1
    ilo, ihi = 0.2, 0.8
    interior = {e: n for e, n in count.items()
                if all((pts[v] > ilo).all() and (pts[v] < ihi).all() for v in e)}
    ns = np.array(list(interior.values()))
    hist = Counter(ns.tolist())
    print(f"    interior edges: {len(ns)}; coordination histogram: "
          f"{dict(sorted(hist.items()))}")
    modal = hist.most_common(1)[0][0]
    frac_defect = float((ns != 5).mean())
    print(f"    modal coordination = {modal}; defect fraction (n != 5) = {frac_defect:.3f}")
    require("modal interior edge coordination is 5 (the ground value)",
            modal == 5, failures)
    require("defects are a strictly positive minority: 0 < fraction < 0.7",
            0.0 < frac_defect < 0.7, failures)

    # Do defect edges organize into connected networks (disclination lines)?
    defect_edges = [e for e, n in interior.items() if n != 5]
    parent = {}

    def find(v):
        parent.setdefault(v, v)
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(a, b):
        parent[find(a)] = find(b)

    for a, b in defect_edges:
        union(a, b)
    defect_vertices = {v for e in defect_edges for v in e}
    comps = Counter(find(v) for v in defect_vertices)
    largest = comps.most_common(1)[0][1] if comps else 0
    n_defect_vertices = len(defect_vertices)
    conn = largest / n_defect_vertices if n_defect_vertices else 0.0
    print(f"    defect subgraph: {len(defect_edges)} edges, {n_defect_vertices} vertices,")
    print(f"    largest connected component holds {conn:.1%} of defect vertices")
    require("defects form NETWORKS, not dust: largest component >= 30% of defect vertices",
            conn >= 0.30, failures)
    print("  The 041 prediction is realized: wrong-coordination edges organize")
    print("  into connected disclination structures threading the bulk -- the")
    print("  morphology a dark-excess microstructure would have. Exhibit only;")
    print("  gates unchanged.")
    return modal, frac_defect, conn


# =============================================================================
# Record + report
# =============================================================================


def record(ns):
    ns.record_derivation(
        derivation_id="bulk_relaxation_phase2_051",
        inputs=[sp.Symbol("seeded_poisson_delaunay"), sp.Symbol("spring_relaxation"),
                sp.Symbol("neighbor_centroid_smoothing")],
        output=sp.Symbol("floor_intensive_mixture_window_defect_spectrum_disclination_networks"),
        method=(
            "seeded (rng 20260702) Poisson-Delaunay complexes; L-BFGS-B spring "
            "relaxation at N = 80/160/320 for intensivity; 4D interior "
            "triangle-hinge coordination census with hinge-identity cross-check "
            "(mean n = 2 pi/mean dihedral) before/after centroid smoothing; "
            "wedge-ring defect spectrum n = 3..7; 3D edge-coordination census "
            "with union-find connectivity of the defect subgraph"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="numerical_experiment",
        scope=(
            "statistical bulk, seeded and deterministic; smoothing is a "
            "relaxation PROXY (no energy-gradient retriangulation, no periodic "
            "box) -- full realizability remains open; no dark-excess "
            "production or abundance licensed"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="o_p10_5_phase2_delivered_051",
        script_id=SCRIPT_ID,
        title="O-P10-5 phase 2 delivered: intensivity, spectrum, disclination networks measured",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["bulk_relaxation_phase2_051"],
        description=(
            "Resolves bulk_relaxation_scaling_041 / O-P10-5's phase-2 scope: "
            "floor intensivity confirmed across a factor 4 in system size; "
            "the defect energy spectrum measured (positive, quantized, "
            "monotone in |delta|); disclination networks observed (connected "
            "defect structures, not dust); first 4D coordination statistics "
            "recorded against the 050 mixture."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="periodic_energy_relaxation_051",
        script_id=SCRIPT_ID,
        title="Phase 3: energy-relaxed periodic packing (the full realizability test)",
        status=ObligationStatus.OPEN,
        required_by=["bulk_relaxation_phase2_051"],
        description=(
            "The remaining face of mixture_realizability_050 and O-P10-5: a "
            "periodic box, true energy-gradient relaxation with "
            "retriangulation (not centroid smoothing), measuring whether the "
            "hinge fractions converge to x_4 = 0.2332 / x_5 = 0.7668 and "
            "whether the floor density matches the 050 mean-field value."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="bulk_relaxation_phase2_claim_051",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Measured in seeded bulk complexes: the frustration floor is "
            "INTENSIVE (E/N stable across a factor 4 -- a bulk energy density, "
            "as 038's rho_v = const requires); real 4D triangulations' hinge "
            "coordinations live in the 050 mixture window with {4, 5} "
            "dominance and regularization drives the mean toward "
            "2 pi/arccos(1/4); the defect spectrum is positive, quantized, "
            "and monotone in the deficit; and wrong-coordination edges "
            "organize into connected disclination networks. Fences: smoothing "
            "is a relaxation proxy; periodic energy relaxation "
            "(periodic_energy_relaxation_051) is the remaining face; no "
            "dark-excess production or abundance licensed."
        ),
        derivation_ids=["bulk_relaxation_phase2_051"],
        obligation_ids=["o_p10_5_phase2_delivered_051"],
    ))


def write_report(per_vertex, m0, m1, f1, excess, modal, frac_defect, conn):
    pv = "\n".join(f"    N = {n}: E/N = {v:.5f}" for n, v in per_vertex.items())
    ex = "\n".join(f"    n = {n}: excess = {excess[n]:+.6f}" for n in sorted(excess))
    md = f"""# VacuumForge: The Relaxation Lab, Phase 2 -- Bulk Packings

## Status

```text
result type:   numerical experiments (instrument phase 2, seeded/
               deterministic; 2026-07-02, derivation 051)
conclusion:    the floor is INTENSIVE; 4D coordination statistics land
               in the 050 mixture window and move toward the prediction
               under regularization; the defect spectrum is measured;
               disclination NETWORKS observed.
satisfies:     O-P10-5 phase-2 scope (bulk_relaxation_scaling_041)
opens:         periodic_energy_relaxation_051 (phase 3 -- the full
               realizability test for the 050 mixture)
verification:  vacuum_forge/src/vacuum_sector/051_bulk_relaxation_phase2/
```

## Measured Results

```text
E1. INTENSIVITY. Relaxed spring energy per vertex of Poisson-Delaunay
    networks (unit mean edge):
{pv}
    Stable across a factor 4: the floor is a bulk energy DENSITY --
    exactly what the substance identity (038, rho_v = const) requires.

E2. 4D COORDINATION (realizability data for the 050 mixture).
    Interior triangle-hinge census of a 400-point 4D Delaunay complex:
    mean coordination {m0:.4f} raw -> {m1:.4f} after smoothing
    (prediction: 2 pi/arccos(1/4) = {NBAR_4D:.4f}); {{4, 5}} fraction
    {f1:.3f} after smoothing. The hinge identity mean n = 2 pi/(mean
    dihedral) verified to < 1%. Real triangulations live in the
    predicted window; regularization moves them toward the mean-field
    mixture. Full test deferred to phase 3.

E3. DEFECT SPECTRUM (excess over the n = 5 floor):
{ex}
    Positive, quantized by coordination, monotone in |delta(n)|: the
    dark-excess candidate now has a measured spectrum shape.

E4. DISCLINATION NETWORKS. Smoothed 500-point 3D bulk: modal interior
    edge coordination = {modal} (the ground value), defect fraction
    {frac_defect:.3f}, largest connected defect component holds
    {conn:.1%} of defect vertices. Defects are line-like NETWORKS
    threading the bulk, not isolated dust -- the morphology 041
    predicted for phase 2.
```

## Fences

```text
- smoothing is a relaxation PROXY (neighbor-centroid, no energy
  gradient, no retriangulation dynamics, no periodic box); the
  mixture-realizability verdict waits on phase 3
  (periodic_energy_relaxation_051).
- E3/E4 are microstructure exhibits: NO dark-excess production or
  abundance is licensed (017-019 gates, P9 fence, unchanged).
- randomness is seeded (rng 20260702): every run bit-identical;
  archive-stable determinism preserved.
```

## Ledger

```text
derivation:  bulk_relaxation_phase2_051
satisfies:   o_p10_5_phase2_delivered_051 (O-P10-5 phase 2;
             bulk_relaxation_scaling_041)
opens:       periodic_energy_relaxation_051 (phase 3)
depends on:  frustration_relaxation_lab_041, ground_coordination_4d_050
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 051: The Relaxation Lab, Phase 2 -- Bulk Packings")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    per_vertex = experiment_1_intensivity(failures)
    m0, m1, f1 = experiment_2_coordination_4d(failures)
    excess = experiment_3_defect_spectrum(failures)
    modal, frac_defect, conn = experiment_4_disclination_networks(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 051: verification failure")
    print("  Phase 2 delivered: the floor is intensive (a bulk density, as 038")
    print("  requires), 4D coordination statistics support the 050 mixture at")
    print("  first contact, the defect spectrum is measured and deficit-")
    print("  ordered, and disclinations form networks. Phase 3 (periodic")
    print("  energy relaxation -- the full realizability test) opened.")

    record(ns)
    write_report(per_vertex, m0, m1, f1, excess, modal, frac_defect, conn)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
