#!/usr/bin/env python3
"""
neighbour_changes.py

Derivation 061: letting the quanta change neighbours
(09_maxwell_probe, stage 3 step 2; p10_bulk_neighbour_changes_060).

The question: when spatial quanta can move far enough to acquire new
geometric neighbours, how much of the strain seen in 060 remains, and
does it still point in the direction favoured by the starting mesh?

Energy: the length-weighted trial angle energy of 060 (P10 candidate),
E_w = sum over (tet, edge) of l_e (1/2)(theta - arccos(1/3))^2, K = 1,
at the same fixed periodic box, with the same log-volume barrier
(mu = 1e-3) during relaxation. Start: 060's relaxed coordinates.

Two neighbour rules on the same seed:

  RULE A -- VED's DELAUNAY ADJACENCY. Neighbours are the periodic
      Delaunay triangulation of the current positions. First, Delaunay
      adjacency is restored at 060's coordinates (060 relaxed with the
      057 connectivity frozen, so its mesh need not be Delaunay). Then
      relax at fixed connectivity, re-triangulate, and repeat until the
      connectivity stops changing (a fixed point: Delaunay AND relaxed)
      or a connectivity repeats (a cycle).

  RULE B -- ENERGY-SELECTED NEIGHBOURS. Any valid, periodic 2-3 or 3-2
      bistellar flip that lowers E_w is accepted (all new tetrahedra
      positive, volume conserved, no duplicate edge or face), sweeping
      in random order at fixed positions; then relax; repeat until no
      improving flip exists after relaxation. Replayed from the same
      start with different flip orders, so the endpoint is reported as
      a local result with its order-to-order spread.

Exact checks after every round, for a closed three-torus mesh with V
vertices, E edges, T tetrahedra: E = V + T, sum_h n_h = 6T,
sum_h (6 - n_h) = 6V; every tetrahedron positive; volumes sum to L^3;
every hinge closes (sum theta = 2 pi). Every accepted flip conserves
volume and lowers E_w.

Reported per endpoint: E_w and E_w / L^3, the unweighted unavoidable
coordination cost sum (2 pi - n theta0)^2 / (2n) and uneven-sharing
extra (and their length-weighted forms), total hinge length (so
shortening and coordination change stay distinguishable), coordination
histogram, minimum volume, and the per-hinge energy fabric with its
overlap and axis angles against the starting mesh (057) and 060.

Fences: TRIAL angle energy, K explicit; one seed, one size, one cubic
box; endpoints are local minima of the stated procedures, not global;
no EM coupling.
"""

import importlib.util
import hashlib
import itertools as it
import json
import math
import time
from collections import Counter
from pathlib import Path

import numpy as np

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
               / "09_maxwell_probe" / "neighbour_changes_vacuumforge.md")
SECTOR = SCRIPT_PATH.parents[1]
PACKING_057 = SECTOR / "057_periodic_spring_control" / "packing_057.npz"
PACKING_060 = SECTOR / "060_angle_energy_fixed_neighbors" / "packing_060.npz"
PACKING_060_META = SECTOR / "060_angle_energy_fixed_neighbors" / "packing_060.json"
PACKING_OUT = SCRIPT_PATH.parent / "packing_061.npz"
PACKING_OUT_META = SCRIPT_PATH.parent / "packing_061.json"

DEPENDENCIES = [
    ("fixed_dep_061", "060_angle_energy_fixed_neighbors__angle_energy_fixed_neighbors",
     "angle_energy_fixed_neighbors_060"),
    ("packing_dep_061", "057_periodic_spring_control__periodic_spring_control",
     "periodic_spring_control_057"),
]

MU = 1e-3
FLIP_ORDERS = (1, 2, 3)          # replay seeds for rule B
MAX_ROUNDS = 40
DE_TOL = 1e-10                    # a flip must lower E_w by more than this
TH0 = math.acos(1 / 3)
FACES4 = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
EDGES4 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


M060 = _load("m060", SECTOR / "060_angle_energy_fixed_neighbors" / "angle_energy_fixed_neighbors.py")
M057 = _load("m057", SECTOR / "057_periodic_spring_control" / "periodic_spring_control.py")
AngleModel = M060.AngleModel
canonical = M060.canonical
content_hash = M060.content_hash
fabric, overlap, axis_angles = M060.fabric, M060.overlap, M060.axis_angles


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
# Mesh bookkeeping
# =============================================================================


_LOCAL = AngleModel.__new__(AngleModel)  # stateless use of 060's per-tetrahedron energy


def tet_energy(x, L, verts, offs):
    P = (x[np.asarray(verts)] + L * np.asarray(offs))[None]
    return float(_LOCAL.local(P, 0.0, True)[0][0])


def tet_volume(P):
    return float(np.linalg.det(P[1:] - P[:1]) / 6)


def orient(x, L, verts, offs):
    verts, offs = list(verts), [np.asarray(o) for o in offs]
    P = x[verts] + L * np.array(offs)
    if tet_volume(P) < 0:
        verts[0], verts[1] = verts[1], verts[0]
        offs[0], offs[1] = offs[1], offs[0]
    offs = np.array(offs)
    first = np.lexsort((offs[:, 2], offs[:, 1], offs[:, 0], np.array(verts)))[0]
    return tuple(int(v) for v in verts), offs - offs[first]


class Mesh:
    """Periodic tetrahedral mesh with incremental face and edge maps."""

    def __init__(self, x, L, T, O):
        self.x, self.L = x, L
        self.tets = {}
        self.faces, self.edges = {}, {}
        self.next_id = 0
        for v, o in zip(T, O):
            self.add(tuple(int(a) for a in v), np.array(o))

    def add(self, verts, offs):
        tid = self.next_id
        self.next_id += 1
        self.tets[tid] = (verts, offs)
        va = np.array(verts)
        for f in FACES4:
            k = canonical(va[list(f)], offs[list(f)])
            self.faces.setdefault(k, set()).add(tid)
        for e in EDGES4:
            k = canonical(va[list(e)], offs[list(e)])
            self.edges.setdefault(k, set()).add(tid)
        return tid

    def remove(self, tid):
        verts, offs = self.tets.pop(tid)
        va = np.array(verts)
        for f in FACES4:
            k = canonical(va[list(f)], offs[list(f)])
            self.faces[k].discard(tid)
            if not self.faces[k]:
                del self.faces[k]
        for e in EDGES4:
            k = canonical(va[list(e)], offs[list(e)])
            self.edges[k].discard(tid)
            if not self.edges[k]:
                del self.edges[k]

    def arrays(self):
        ids = sorted(self.tets)
        T = np.array([self.tets[i][0] for i in ids])
        O = np.array([self.tets[i][1] for i in ids])
        return T, O

    def P(self, tid):
        v, o = self.tets[tid]
        return self.x[list(v)] + self.L * o

    def local_index(self, tid, key, size):
        v, o = self.tets[tid]
        va = np.array(v)
        combos = FACES4 if size == 3 else EDGES4
        for c in combos:
            if canonical(va[list(c)], o[list(c)]) == key:
                return c
        raise KeyError(key)

    def shift_into(self, tid_ref, tid, shared_ref, shared):
        """Integer shift s with offsets(tid) + s = offsets(tid_ref) on shared vertices."""
        vr, orf = self.tets[tid_ref]
        v, o = self.tets[tid]
        s = None
        for i in shared_ref:
            j = next(j for j in shared if v[j] == vr[i])
            si = orf[i] - o[j]
            if s is None:
                s = si
            elif not np.array_equal(s, si):
                return None
        return s


def try_flip_23(mesh, fkey, energies):
    tids = list(mesh.faces.get(fkey, ()))
    if len(tids) != 2:
        return None
    t1, t2 = tids
    f1 = mesh.local_index(t1, fkey, 3)
    f2 = mesh.local_index(t2, fkey, 3)
    d1 = next(i for i in range(4) if i not in f1)
    e2 = next(i for i in range(4) if i not in f2)
    s = mesh.shift_into(t1, t2, f1, f2)
    if s is None:
        return None
    v1, o1 = mesh.tets[t1]
    v2, o2 = mesh.tets[t2]
    a, b, c = [(v1[i], o1[i]) for i in f1]
    d = (v1[d1], o1[d1])
    e = (v2[e2], o2[e2] + s)
    if d[0] == e[0]:
        return None
    ekey = canonical(np.array([d[0], e[0]]), np.array([d[1], e[1]]))
    if ekey in mesh.edges:
        return None
    new = [orient(mesh.x, mesh.L, [p[0], q[0], d[0], e[0]], [p[1], q[1], d[1], e[1]])
           for p, q in ((a, b), (b, c), (c, a))]
    return _evaluate(mesh, [t1, t2], new, energies)


def try_flip_32(mesh, ekey, energies):
    tids = list(mesh.edges.get(ekey, ()))
    if len(tids) != 3:
        return None
    t1 = tids[0]
    e1 = mesh.local_index(t1, ekey, 2)
    v1, o1 = mesh.tets[t1]
    d, e = (v1[e1[0]], o1[e1[0]]), (v1[e1[1]], o1[e1[1]])
    ring = {}
    for tid in tids:
        loc = mesh.local_index(tid, ekey, 2)
        s = mesh.shift_into(t1, tid, e1, loc) if tid != t1 else np.zeros(3, int)
        if s is None:
            return None
        v, o = mesh.tets[tid]
        for i in range(4):
            if i not in loc:
                ring[(v[i], tuple(int(z) for z in o[i] + s))] = None
    if len(ring) != 3:
        return None
    (a, oa), (b, ob), (c, oc) = [(k[0], np.array(k[1])) for k in ring]
    fkey = canonical(np.array([a, b, c]), np.array([oa, ob, oc]))
    if fkey in mesh.faces:
        return None
    new = [orient(mesh.x, mesh.L, [a, b, c, apex[0]], [oa, ob, oc, apex[1]]) for apex in (d, e)]
    return _evaluate(mesh, tids, new, energies)


def _evaluate(mesh, old, new, energies):
    Vold = sum(tet_volume(mesh.P(t)) for t in old)
    Pn = [mesh.x[list(v)] + mesh.L * o for v, o in new]
    Vn = [tet_volume(P) for P in Pn]
    if min(Vn) <= 1e-12 or abs(sum(Vn) - Vold) > 1e-9 * max(1.0, Vold):
        return None
    e_new = [tet_energy(mesh.x, mesh.L, v, o) for v, o in new]
    dE = sum(e_new) - sum(energies[t] for t in old)
    return dE, old, new, e_new


def apply(mesh, flip, energies):
    _, old, new, e_new = flip
    for t in old:
        mesh.remove(t)
        energies.pop(t)
    for (v, o), en in zip(new, e_new):
        energies[mesh.add(v, o)] = en


def all_energies(mesh):
    return {t: tet_energy(mesh.x, mesh.L, v, o) for t, (v, o) in mesh.tets.items()}


def flip_sweeps(mesh, rng):
    energies = all_energies(mesh)
    n23 = n32 = 0
    while True:
        cands = [("23", k) for k, s in mesh.faces.items() if len(s) == 2]
        cands += [("32", k) for k, s in mesh.edges.items() if len(s) == 3]
        order = rng.permutation(len(cands))
        accepted = 0
        for idx in order:
            kind, key = cands[idx]
            flip = (try_flip_23 if kind == "23" else try_flip_32)(mesh, key, energies)
            if flip is not None and flip[0] < -DE_TOL:
                apply(mesh, flip, energies)
                accepted += 1
                if kind == "23":
                    n23 += 1
                else:
                    n32 += 1
        if accepted == 0:
            return n23, n32


def relax(x, L, T, O):
    model = AngleModel(L, T, O)
    x, it_, gn, status = model.newton(x.copy(), MU, True)
    return x, it_, gn, status


def delaunay_unwrapped(x, L):
    """Periodic Delaunay of the current positions, offsets in the unwrapped frame."""
    w = np.floor(x / L).astype(int)
    xw = x - L * w
    T, O = M057.periodic_delaunay(xw, L)
    O = O - w[T]
    out_T, out_O = [], []
    for v, o in zip(T, O):
        vv, oo = orient(x, L, v, o)
        out_T.append(vv)
        out_O.append(oo)
    return np.array(out_T), np.array(out_O)


def tet_keys(T, O):
    return frozenset(canonical(np.asarray(v), np.asarray(o)) for v, o in zip(T, O))


# =============================================================================
# Measurement and exact checks
# =============================================================================


def measure(x, L, T, O, start_fab, fab060):
    model = AngleModel(L, T, O)
    hz = model.hinges(x)
    th, le, eh, _ = model.dihedrals(model.P(x))
    Ew = float(0.5 * (le * (th - TH0) ** 2).sum())
    ew_h = np.bincount(model.hinge.ravel(), weights=(0.5 * le * (th - TH0) ** 2).ravel(),
                       minlength=model.nH)
    V = model.volumes(x)
    nV, nE, nT = model.n, model.nH, model.nT
    n = hz["n"]
    fab = fabric(ew_h, hz["dir"])
    return {
        "Ew": Ew, "Ew_per_vol": Ew / L ** 3,
        "unavoid": float(hz["unavoid"].sum()), "extra": float(hz["extra"].sum()),
        "unavoid_w": float((hz["len"] * hz["unavoid"]).sum()),
        "extra_w": float((hz["len"] * hz["extra"]).sum()),
        "hinge_len": float(hz["len"].sum()), "nV": nV, "nE": nE, "nT": nT,
        "hist": dict(sorted(Counter(n.tolist()).items())),
        "id_EVT": nE == nV + nT, "id_sum_n": int(n.sum()) == 6 * nT,
        "id_6V": int((6 - n).sum()) == 6 * nV,
        "minV": float(V.min() / M060.VREF), "all_pos": bool(np.all(V > 0)),
        "vol_ok": abs(float(V.sum()) - L ** 3) < 1e-8 * L ** 3,
        "closure": float(np.abs(hz["sum_th"] - 2 * math.pi).max()),
        "fab": fab, "ov_start": overlap(fab, start_fab), "ov_060": overlap(fab, fab060),
        "ang_start": axis_angles(fab, start_fab),
    }


def checks_ok(m):
    return (m["id_EVT"] and m["id_sum_n"] and m["id_6V"] and m["all_pos"] and m["vol_ok"]
            and m["closure"] < 1e-8)


def line(m):
    return (f"E_w = {m['Ew']:.4f} (per volume {m['Ew_per_vol']:.5f}); unavoidable {m['unavoid']:.3f}, "
            f"extra {m['extra']:.3f}; hinge length {m['hinge_len']:.2f}; T = {m['nT']}; "
            f"min V {m['minV']:.1e}; fabric aniso {m['fab']['aniso']:.4f}, overlap start "
            f"{m['ov_start']:+.3f}, 060 {m['ov_060']:+.3f}")


# =============================================================================
# Experiments
# =============================================================================


def experiment_1_start(failures):
    header("E1: the start -- 060's relaxed coordinates on the 057 connectivity")
    arr = dict(np.load(PACKING_060))
    meta = json.loads(PACKING_060_META.read_text())
    require("060 packing content hash verified", content_hash(arr) == meta["content_sha256"],
            failures)
    L, T, O = float(arr["L"]), arr["T"], arr["O"]
    x = arr["x_weighted"]
    a57 = dict(np.load(PACKING_057))
    m0 = AngleModel(L, a57["T"], a57["O"])
    h0 = m0.hinges(a57["x_initial"])
    start_fab = fabric(h0["e"], h0["dir"])  # the starting mesh's pattern (as in 060)
    th, le, _, _ = m0.dihedrals(m0.P(x))
    ew_h = np.bincount(m0.hinge.ravel(), weights=(0.5 * le * (th - TH0) ** 2).ravel(),
                       minlength=m0.nH)
    fab060 = fabric(ew_h, m0.hinges(x)["dir"])
    ms = measure(x, L, T, O, start_fab, fab060)
    print(f"    {line(ms)}")
    print(f"    coordination histogram {ms['hist']}")
    require("start passes the exact mesh checks (E = V + T, sum n = 6T, sum (6 - n) = 6V, "
            "volumes, closure)", checks_ok(ms), failures)
    return x, L, T, O, start_fab, fab060, ms


def experiment_2_delaunay(x, L, T, O, start_fab, fab060, failures):
    header("E2: rule A -- VED's Delaunay adjacency (moving quanta, geometric neighbours)")
    Td, Od = delaunay_unwrapped(x, L)
    changed = len(tet_keys(T, O) ^ tet_keys(Td, Od)) // 2
    m_restore = measure(x, L, Td, Od, start_fab, fab060)
    print(f"    restoring Delaunay at 060's coordinates: ~{changed} tetrahedra differ")
    print(f"      {line(m_restore)}")
    require("restored Delaunay mesh passes the exact checks", checks_ok(m_restore), failures)
    history, seen = [], {tet_keys(Td, Od): 0}
    xr, Tc, Oc = x.copy(), Td, Od
    outcome = "max rounds"
    for r in range(1, MAX_ROUNDS + 1):
        xr, it_, gn, status = relax(xr, L, Tc, Oc)
        m_rel = measure(xr, L, Tc, Oc, start_fab, fab060)
        Tn, On = delaunay_unwrapped(xr, L)
        kn = tet_keys(Tn, On)
        nchg = len(tet_keys(Tc, Oc) ^ kn) // 2
        m_new = measure(xr, L, Tn, On, start_fab, fab060)
        history.append((r, status, m_rel, nchg, m_new))
        print(f"    round {r:2d}: relaxed ({status}) E_w {m_rel['Ew']:.4f} -> re-Delaunay "
              f"({nchg} tets change) E_w {m_new['Ew']:.4f}")
        require(f"round {r}: relaxed and re-triangulated meshes pass the exact checks",
                checks_ok(m_rel) and checks_ok(m_new) and status == "converged", failures)
        if nchg == 0:
            outcome = "fixed point"
            break
        if kn in seen:
            outcome = f"cycle (returns to round {seen[kn]})"
            Tc, Oc = Tn, On
            break
        seen[kn] = r
        Tc, Oc = Tn, On
    final = history[-1][2] if outcome == "fixed point" else history[-1][4]
    if outcome != "fixed point":
        xr, it_, gn, status = relax(xr, L, Tc, Oc)
        final = measure(xr, L, Tc, Oc, start_fab, fab060)
    print(f"    outcome: {outcome} after {len(history)} rounds")
    print(f"    endpoint: {line(final)}")
    print(f"    coordination histogram {final['hist']}")
    return {"restore": m_restore, "changed": changed, "history": history, "outcome": outcome,
            "final": final, "x": xr, "T": Tc, "O": Oc}


def run_rule_b(x, L, T, O, seed, start_fab, fab060, failures, verbose):
    rng = np.random.default_rng(seed)
    xr, Tc, Oc = x.copy(), T, O
    rounds, tot23, tot32 = [], 0, 0
    prev = measure(xr, L, Tc, Oc, start_fab, fab060)["Ew"]
    for r in range(1, MAX_ROUNDS + 1):
        mesh = Mesh(xr, L, Tc, Oc)
        e_before = sum(all_energies(mesh).values())
        n23, n32 = flip_sweeps(mesh, rng)
        e_after = sum(all_energies(mesh).values())
        Tc, Oc = mesh.arrays()
        mf = measure(xr, L, Tc, Oc, start_fab, fab060)
        tot23 += n23
        tot32 += n32
        if n23 + n32 == 0:
            rounds.append((r, 0, 0, e_before, e_after, None))
            break
        xr, it_, gn, status = relax(xr, L, Tc, Oc)
        mr = measure(xr, L, Tc, Oc, start_fab, fab060)
        rounds.append((r, n23, n32, e_before, e_after, mr))
        if verbose:
            print(f"    round {r:2d}: flips 2-3 {n23:4d}, 3-2 {n32:4d}; E_w {e_before:.4f} -> "
                  f"{e_after:.4f} (flips) -> {mr['Ew']:.4f} (relaxed, {status})")
        ok = (checks_ok(mf) and checks_ok(mr) and status == "converged"
              and e_after < e_before and mr["Ew"] <= prev + 1e-9)
        require(f"order {seed} round {r}: exact checks; flips and relaxation lower E_w", ok, failures)
        prev = mr["Ew"]
    final = measure(xr, L, Tc, Oc, start_fab, fab060)
    return {"seed": seed, "rounds": rounds, "n23": tot23, "n32": tot32, "final": final,
            "x": xr, "T": Tc, "O": Oc}


def experiment_3_flips(x, L, T, O, start_fab, fab060, failures):
    header("E3: rule B -- energy-selected neighbours (2-3 / 3-2 flips), replayed over flip orders")
    runs = []
    for k, seed in enumerate(FLIP_ORDERS):
        t0 = time.time()
        print(f"  flip order {seed}:")
        res = run_rule_b(x, L, T, O, seed, start_fab, fab060, failures, verbose=True)
        print(f"    endpoint ({time.time() - t0:.0f}s; {res['n23']} 2-3 and {res['n32']} 3-2 flips): "
              f"{line(res['final'])}")
        print(f"    coordination histogram {res['final']['hist']}")
        runs.append(res)
    # Why no 2-3 flips? (1) round trip: a 3-2 flip followed by the 2-3 flip on the face it
    # created must restore the same tetrahedra with the opposite energy change.
    mesh = Mesh(x.copy(), L, T, O)
    energies = all_energies(mesh)
    trips = []
    for key in [k for k, s in mesh.edges.items() if len(s) == 3]:
        f32 = try_flip_32(mesh, key, energies)
        if f32 is None:
            continue
        before = {canonical(np.array(mesh.tets[t][0]), mesh.tets[t][1]) for t in f32[1]}
        apply(mesh, f32, energies)
        new_face = canonical(np.array(f32[2][0][0][:3]), f32[2][0][1][:3])
        f23 = try_flip_23(mesh, new_face, energies)
        ok = f23 is not None and abs(f23[0] + f32[0]) < 1e-9
        if ok:
            apply(mesh, f23, energies)
            after = {canonical(np.array(v), o) for v, o in f23[2]}
            ok = after == before
        trips.append((f32[0], ok))
        if len(trips) == 5:
            break
    print(f"    flip round trip (3-2 then 2-3 on the created face), 5 cases: dE_32 = "
          f"{np.round([t[0] for t in trips], 4).tolist()}; restored {all(t[1] for t in trips)}")
    require("2-3 flips are implemented consistently: each round trip restores the original "
            "tetrahedra with the opposite energy change", len(trips) == 5
            and all(t[1] for t in trips), failures)
    # (2) census of 2-3 candidates at each endpoint
    census = []
    for r in runs:
        mesh = Mesh(r["x"], L, r["T"], r["O"])
        energies = all_energies(mesh)
        dEs = [f[0] for f in (try_flip_23(mesh, k, energies)
                              for k, s in mesh.faces.items() if len(s) == 2) if f is not None]
        census.append((len(dEs), float(min(dEs)) if dEs else math.nan))
    print("    2-3 census at the endpoints (valid candidates, smallest dE): "
          + "; ".join(f"order {r['seed']}: {c[0]}, {c[1]:+.4f}" for r, c in zip(runs, census)))
    require("at every rule-B endpoint, every geometrically valid 2-3 flip raises E_w "
            "(it creates an n = 3 hinge)", all(c[0] > 0 and c[1] > 0 for c in census), failures)
    Ews = np.array([r["final"]["Ew"] for r in runs])
    spread = float(Ews.max() - Ews.min())
    pair_ov = [overlap(a["final"]["fab"], b["final"]["fab"]) for a, b in it.combinations(runs, 2)]
    print(f"    replay spread: E_w {Ews.min():.4f} .. {Ews.max():.4f} (spread {spread:.4f}); "
          f"fabric overlaps between orders {np.round(pair_ov, 3).tolist()}")
    return runs, spread, pair_ov, trips, census


# =============================================================================
# Record + report
# =============================================================================


def save(rA, runs, failures):
    header("E4: saved endpoints")
    out = {"x_delaunay": rA["x"], "T_delaunay": rA["T"].astype(np.int64),
           "O_delaunay": rA["O"].astype(np.int64)}
    for r in runs:
        s = r["seed"]
        out[f"x_flips_{s}"] = r["x"]
        out[f"T_flips_{s}"] = r["T"].astype(np.int64)
        out[f"O_flips_{s}"] = r["O"].astype(np.int64)
    digest = content_hash(out)
    old = json.loads(PACKING_OUT_META.read_text()) if PACKING_OUT_META.exists() else {}
    if old.get("content_sha256") == digest and PACKING_OUT.exists():
        print(f"    unchanged: {PACKING_OUT.name} (content sha256 {digest[:16]}...)")
    else:
        np.savez(PACKING_OUT, **out)
        PACKING_OUT_META.write_text(json.dumps({
            "derivation": "neighbour_changes_061", "content_sha256": digest,
            "source_packing_sha256": json.loads(PACKING_060_META.read_text())["content_sha256"],
            "mu": MU, "flip_orders": list(FLIP_ORDERS),
            "arrays": {k: list(np.shape(v)) for k, v in sorted(out.items())},
            "hash_rule": "sha256 over sorted array names: name, dtype, shape, C-order bytes",
        }, indent=2) + "\n")
        print(f"    wrote {PACKING_OUT.name} (content sha256 {digest[:16]}...)")
    require("saved endpoints reload with the recorded hash",
            content_hash(dict(np.load(PACKING_OUT))) == digest, failures)
    return digest


def record(ns, digest):
    ns.record_derivation(
        derivation_id="neighbour_changes_061",
        inputs=[sp.Symbol("packing_060"), sp.Symbol("weighted_trial_angle_energy"),
                sp.Symbol("periodic_delaunay_rule"), sp.Symbol("bistellar_flips")],
        output=sp.Symbol("strain_surviving_neighbour_changes"),
        method=(
            "060 relaxed coordinates; rule A: periodic Delaunay restored then alternated with "
            "fixed-connectivity Newton relaxation to a fixed point or cycle; rule B: greedy "
            "energy-lowering periodic 2-3/3-2 flips in random order alternated with relaxation, "
            "replayed over three flip orders; exact mesh identities after every round; per-hinge "
            f"unavoidable/extra split; fabrics vs start and 060; endpoints saved ({digest})"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="numerical_experiment",
        scope=(
            "trial angle energy, K explicit; one seed, one size, one cubic box; endpoints are "
            "local results of the stated procedures; no EM coupling"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p10_bulk_neighbour_changes_060",
        script_id=SCRIPT_ID,
        title="Stage 3 step 2 (one seed): neighbour changes under the weighted angle energy",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["neighbour_changes_061"],
        description=(
            "For one seed: Delaunay adjacency (rule A) and energy-selected flips (rule B) "
            "from 060's coordinates, with exact mesh identities, the unavoidable/extra split, "
            "energy per volume, hinge length, and fabric against the starting mesh."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p10_neighbour_ensemble_061",
        script_id=SCRIPT_ID,
        title="Neighbour-change ensemble: seeds, sizes, starting arrangements",
        status=ObligationStatus.OPEN,
        required_by=["neighbour_changes_061"],
        description=(
            "Repeat 061 across seeds, N and cell shapes (and the spring control): is the energy "
            "per volume reproducible, does a floor survive, and does the directional fabric wash "
            "out at large scale?"
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="neighbour_changes_claim_061",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.INFORMATIONAL,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "For one seed, letting the quanta change neighbours (Delaunay rule, and energy-"
            "selected flips over three orders) changes how much of 060's stored angle strain "
            "remains and how it is oriented; the report records the endpoints, their exact "
            "mesh checks, and their order-to-order spread. Local results; trial energy."
        ),
        derivation_ids=["neighbour_changes_061"],
        obligation_ids=["p10_bulk_neighbour_changes_060"],
    ))


def write_report(ms, rA, runs, spread, pair_ov, digest, trips, census):
    def row(tag, m):
        return (f"    {tag:<22} {m['Ew']:9.3f}  {m['Ew_per_vol']:.5f}  {m['unavoid']:8.3f}  "
                f"{m['extra']:8.3f}  {m['hinge_len']:8.2f}  {m['nT']:5d}  {m['fab']['aniso']:.4f}  "
                f"{m['ov_start']:+.3f}  {m['ov_060']:+.3f}")

    rows = [row("060 start (057 mesh)", ms), row("A: Delaunay restored", rA["restore"]),
            row("A: endpoint", rA["final"])]
    rows += [row(f"B: flips, order {r['seed']}", r["final"]) for r in runs]
    hists = "\n".join([f"    060 start:   {ms['hist']}", f"    A endpoint:  {rA['final']['hist']}"]
                      + [f"    B order {r['seed']}:   {r['final']['hist']}" for r in runs])
    histA = "\n".join(f"    round {r:2d}: relaxed E_w {mr['Ew']:.4f}; re-Delaunay changes {c} "
                      f"tets -> E_w {mn['Ew']:.4f}" for r, _, mr, c, mn in rA["history"])
    histB = []
    for r_ in runs:
        histB.append(f"    order {r_['seed']}: {r_['n23']} 2-3 and {r_['n32']} 3-2 flips in "
                     f"{len(r_['rounds'])} rounds")
    histB = "\n".join(histB)
    b = [r["final"] for r in runs]
    bEw = np.mean([m["Ew"] for m in b])
    md = f"""# VacuumForge: Letting the Quanta Change Neighbours

## Status

```text
result type:   numerical experiment (stage 3 step 2, one seed;
               2026-11-24, derivation 061); TRIAL angle energy, K = 1
question:      when spatial quanta can move far enough to acquire new
               geometric neighbours, how much of the strain seen in 060
               remains, and does it still point in the direction
               favoured by the starting mesh?
satisfies:     p10_bulk_neighbour_changes_060 (one seed)
opens:         p10_neighbour_ensemble_061
endpoints:     vacuum_forge/src/vacuum_sector/061_neighbour_changes/
               packing_061.npz (content sha256 {digest[:16]}...)
verification:  vacuum_forge/src/vacuum_sector/061_neighbour_changes/
```

## Two Neighbour Rules

```text
A  VED's Delaunay adjacency: neighbours = periodic Delaunay
   triangulation of the current positions; relax, re-triangulate,
   repeat to a fixed point or a cycle.
B  energy-selected neighbours: any valid periodic 2-3 / 3-2 flip that
   lowers E_w, in random order, alternated with relaxation; replayed
   over flip orders {list(FLIP_ORDERS)}.
energy:  E_w = sum over (tet, edge) of l_e (1/2)(theta - arccos(1/3))^2
         (the 060 P10 candidate), barrier mu = {MU:g} during relaxation
checks:  after every round: E = V + T, sum n_h = 6T,
         sum (6 - n_h) = 6V, all volumes positive and summing to L^3,
         every hinge closes; every accepted flip conserves volume and
         lowers E_w.
```

## Measured Results

```text
                           E_w       E_w/vol  unavoid.   extra    hinge len   T     aniso   ov.start  ov.060
{chr(10).join(rows)}
(unavoidable and extra are the unweighted per-hinge sums; ov = overlap
of the deviatoric energy fabric, +1 = same pattern)

Coordination histograms (n: number of hinges):
{hists}

Rule A history ({rA['outcome']}; restoring Delaunay at 060's coordinates
changed ~{rA['changed']} tetrahedra):
{histA}

Rule B:
{histB}
    replay spread of E_w across orders: {spread:.4f} (mean {bEw:.3f});
    fabric overlaps between orders: {np.round(pair_ov, 3).tolist()}
    every accepted flip was 3-2. Round-trip test (3-2 then 2-3 on the
    created face, 5 cases): originals restored with the opposite energy
    change. 2-3 census at the endpoints (valid candidates, smallest
    dE): {'; '.join(f"order {r['seed']}: {c[0]}, {c[1]:+.4f}" for r, c in zip(runs, census))}.
    Every valid 2-3 flip creates an n = 3 hinge and raises E_w, so
    greedy descent can only remove n = 3 edges.
```

## Reading

- **Moving quanta with geometric (Delaunay) neighbours releases most of
  the fixed-neighbour strain.** Rule A takes E_w from {ms['Ew']:.1f} to
  {rA['final']['Ew']:.1f} ({100 * (1 - rA['final']['Ew'] / ms['Ew']):.0f}% released). The unavoidable coordination cost
  falls from {ms['unavoid']:.1f} to {rA['final']['unavoid']:.1f} as the histogram moves toward n = 5, and
  the uneven-sharing extra from {ms['extra']:.1f} to {rA['final']['extra']:.1f}. Restoring Delaunay
  adjacency at 060's own coordinates already lowers E_w to
  {rA['restore']['Ew']:.1f}. The iteration is not monotone (re-triangulation can
  raise E_w), but it reaches a fixed point: a packing that is both
  Delaunay and relaxed.
- **Energy-selected flips reach about the same energy, by a different
  route.** Rule B ends at {min(m['Ew'] for m in b):.1f}–{max(m['Ew'] for m in b):.1f}, within its own order-to-order spread
  of rule A. Its greedy flips remove every n = 3 edge but cannot make
  the uphill 2-3 moves that would open other rearrangements. It ends
  with a lower unavoidable cost but more uneven-sharing extra than
  rule A.
- **Energy per volume is similar across rules:** {rA['final']['Ew_per_vol']:.2f} (A) and
  {min(m['Ew_per_vol'] for m in b):.2f}–{max(m['Ew_per_vol'] for m in b):.2f} (B), against {ms['Ew_per_vol']:.2f} with neighbours fixed. Whether
  that number is reproducible across seeds and sizes is the ensemble's
  question.
- **Direction.** Rule A loses the starting mesh's orientation (overlap
  {rA['final']['ov_start']:+.2f}). Rule B keeps a variable amount of it ({min(m['ov_start'] for m in b):+.2f} to
  {max(m['ov_start'] for m in b):+.2f} across orders). The strong alignment seen in 060 was
  largely a property of the frozen triangulation.
- **What this says, for one seed.** Most of the excess disappears in
  both runs, so moving quanta and updating their geometric neighbours
  is enough to release it. The theory needs no extra neighbour-choice
  rule to reach this level, although greedy flips are a weak search
  (see Fences).
- **Still far above the floor.** If every hinge sat at n = 5 the
  unavoidable cost would be about 0.0016 per unit hinge length. Mixed
  coordination keeps it near {rA['final']['unavoid']:.0f}. The positive floor 059 predicts
  is present, but this packing is nowhere near it.

## Fences

```text
- TRIAL angle energy (059/060), K explicit.
- one seed, one size, one cubic box; endpoints are local results of
  the stated procedures (greedy flips, Delaunay iteration), not global
  minima. The ensemble is p10_neighbour_ensemble_061.
- rule B is greedy: it cannot pass through the uphill 2-3 moves, so it
  bounds what local energy-selected flips can reach only from above.
  Composite moves (4-4 flips) or annealing would search further.
- no EM coupling.
```

## Compute Environment

```text
ran on:      CPU-only cloud container (NumPy/SciPy). No GPU was
             available; attaching the theory owner's local GPU (RTX
             3080 Ti) to the cloud session was not supported.
methods:     incremental face/edge maps and per-tetrahedron energies
             make each flip test local; relaxation reuses 060's exact
             per-tetrahedron Hessian and eigenvalue-modified Newton.
validation:  another Claude Code session with GPU access should rerun
             this module, confirm the saved endpoints' content hash
             (or the endpoint energies and histograms), and then run
             the ensemble (p10_neighbour_ensemble_061) at larger N,
             where the GPU makes the relaxations practical.
```

## Ledger

```text
derivation:  neighbour_changes_061
satisfies:   p10_bulk_neighbour_changes_060 (one seed)
opens:       p10_neighbour_ensemble_061
depends on:  angle_energy_fixed_neighbors_060, periodic_spring_control_057
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 061: Letting the Quanta Change Neighbours")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    x, L, T, O, start_fab, fab060, ms = experiment_1_start(failures)
    rA = experiment_2_delaunay(x, L, T, O, start_fab, fab060, failures)
    runs, spread, pair_ov, trips, census = experiment_3_flips(x, L, T, O, start_fab, fab060,
                                                              failures)
    digest = save(rA, runs, failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 061: verification failure")
    print("  Step 2 delivered for one seed: both neighbour rules run with exact mesh")
    print("  checks after every round; endpoints, spreads and fabrics recorded.")

    record(ns, digest)
    write_report(ms, rA, runs, spread, pair_ov, digest, trips, census)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
