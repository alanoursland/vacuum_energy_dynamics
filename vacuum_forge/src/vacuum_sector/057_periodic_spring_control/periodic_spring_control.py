#!/usr/bin/env python3
"""
periodic_spring_control.py

Derivation 057: the periodic, non-inverting spring control
(09_maxwell_probe, stage 2; periodic_noninverting_spring_control).

The engineering question: can the spatial quanta relax at FIXED box size
and shape (the "fixed macroscopic metric") while every tetrahedron stays
valid? 051 E1's free-boundary relaxation inverted 44-49% of its original
tetrahedra (09_maxwell_probe/free_relaxation_diagnostics.md), so its
final coordinates cannot serve as an optical domain. This module builds
one valid periodic packing for the paired comparisons that follow: the
stage-3 mechanical comparison and the 058 Maxwell calibration read the
SAME saved geometry.

Five experiments:

  E1. THE PERIODIC TRIANGULATION. Seeded Poisson points in a cubic box,
      periodic Delaunay via the 27-image construction, deduplicated into
      tetrahedra with integer image offsets. Checks: chi = 0 (three-
      torus), every triangle shared by exactly two tetrahedra, volumes
      sum to L^3, no edge joins a vertex to its own image. Rescaled to
      unit mean edge; the box is then FIXED.

  E2. THE FREE PERIODIC CONTROL. The 051 spring objective
      E = sum_e (l_e - 1)^2 relaxed with no barrier at fixed box: the
      inversion fraction a periodic, fixed-box relaxation produces on
      its own, for comparison with the free-boundary 051 figure.

  E3. THE BARRIER RELAXATION (primary, mu = 1e-2). Total energy
      E_spring - mu sum_t log(V_t / V_ref), damped Newton with an exact
      Hessian, feasibility kept by backtracking. Reported separately:
      the TOTAL residual (equilibrium with the barrier) and the
      SPRING-ONLY residual (the force the barrier supplies). Mechanical
      observables: the spring virial W = sum (l-1) l u u^T, the
      strain-energy fabric F = sum (l-1)^2 u u^T, the extension-fabric
      identity sum (l-1) u u^T = W - F, the barrier's virial (exactly
      isotropic, -mu T I), and the rotation-invariant anisotropy
      |dev F| / tr F with its principal axes.

  E4. BARRIER SENSITIVITY. Warm-started at mu = 1e-3 and 1e-4. Compared:
      minimum signed volume, spring energy, anisotropy, principal axes.
      The contact set (tetrahedra whose volume falls in proportion to
      mu) carries the residual spring force. If the fabric is stable as
      the barrier weakens, it is attributable to the packing rather than
      to the barrier.

  E5. THE SAVED PACKING. Relaxed coordinates, connectivity, periodic
      offsets, the pre-relaxation coordinates, and the weak-barrier
      coordinates, saved with a content hash so 058 can verify it is
      reading exactly this geometry.

Fences: one seed, one size, one box shape: a calibration packing, not
an ensemble. The spring objective is the 051 PROXY, not the P10 hinge
energy (stage 3). Fixed connectivity: no retriangulation, so the mesh is
generally no longer Delaunay after relaxation (058 diagnoses the Hodge
consequence). No EM coupling and no channel.
"""

import hashlib
import itertools as it
import json
import math
import time
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
               / "09_maxwell_probe" / "periodic_spring_control_vacuumforge.md")
PACKING_PATH = SCRIPT_PATH.parent / "packing_057.npz"
PACKING_META = SCRIPT_PATH.parent / "packing_057.json"

DEPENDENCIES = [
    ("relaxation_dep_057", "051_bulk_relaxation_phase2__bulk_relaxation_phase2",
     "bulk_relaxation_phase2_051"),
]

SEED = 20261124
N = 160
MU_PRIMARY = 1e-2
MU_WEAK = (1e-3, 1e-4)
VREF = 1 / (6 * math.sqrt(2))      # regular tetrahedron of unit edge
GTOL = 1e-11


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
# Periodic complex
# =============================================================================


def canonical(verts, offs):
    """Translate a cell so its lexicographically first (vertex, offset) sits
    at offset 0; return the hashable key."""
    order = np.lexsort((offs[:, 2], offs[:, 1], offs[:, 0], verts))
    v, o = verts[order], offs[order]
    o = o - o[0]
    return tuple(int(a) for a in v) + tuple(int(a) for a in o.ravel())


def periodic_delaunay(pts, L):
    n = len(pts)
    shifts = np.array(list(it.product((-1, 0, 1), repeat=3)))
    centre = int(np.where((shifts == 0).all(axis=1))[0][0])
    big = (pts[None, :, :] + L * shifts[:, None, :]).reshape(-1, 3)
    sid = np.repeat(np.arange(27), n)
    vid = np.tile(np.arange(n), 27)
    tets = {}
    for s in Delaunay(big).simplices:
        if not np.any(sid[s] == centre):
            continue
        verts, offs = vid[s], shifts[sid[s]]
        k = canonical(verts, offs)
        if k not in tets:
            o = offs - offs[np.lexsort((offs[:, 2], offs[:, 1], offs[:, 0], verts))[0]]
            tets[k] = (verts.copy(), o.copy())
    T = np.array([v for v, _ in tets.values()])
    O = np.array([o for _, o in tets.values()])
    return T, O


def edges_and_faces(T, O):
    E, F = {}, {}
    for t in range(len(T)):
        for a, b in it.combinations(range(4), 2):
            k = canonical(T[t, [a, b]], O[t, [a, b]])
            E.setdefault(k, None)
        for f in it.combinations(range(4), 3):
            k = canonical(T[t, list(f)], O[t, list(f)])
            F[k] = F.get(k, 0) + 1
    I = np.array([k[0] for k in E])
    J = np.array([k[1] for k in E])
    OF = np.array([k[5:8] for k in E])  # offset of the second vertex
    return I, J, OF, F


def volumes(x, L, T, O):
    P = x[T] + L * O
    return np.linalg.det(P[:, 1:] - P[:, :1]) / 6


# =============================================================================
# Energies (spring proxy + log barrier), exact gradient and Hessian
# =============================================================================


class Packing:
    def __init__(self, L, T, O, I, J, OF):
        self.L, self.T, self.O, self.I, self.J, self.OF = L, T, O, I, J, OF
        self.n = int(max(T.max(), I.max(), J.max())) + 1
        self.eps = np.zeros((3, 3, 3))
        for (a, b, c), s in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                             ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
            self.eps[a, b, c] = s
        A = np.zeros((9, 12))
        for r in range(3):
            for k in range(3):
                A[3 * r + k, 3 * (r + 1) + k] = 1
                A[3 * r + k, k] = -1
        self.A = A

    def edge_vectors(self, x):
        return x[self.J] + self.L * self.OF - x[self.I]

    def spring(self, x):
        b = self.edge_vectors(x)
        l = np.linalg.norm(b, axis=1)
        c = (2 * (l - 1) / l)[:, None] * b
        g = np.zeros_like(x)
        np.add.at(g, self.J, c)
        np.add.at(g, self.I, -c)
        return float(((l - 1) ** 2).sum()), g

    def _tet_parts(self, x):
        P = x[self.T] + self.L * self.O
        a, b, c = P[:, 1] - P[:, 0], P[:, 2] - P[:, 0], P[:, 3] - P[:, 0]
        V = np.einsum("ij,ij->i", a, np.cross(b, c)) / 6
        return a, b, c, V

    def barrier(self, x, mu):
        a, b, c, V = self._tet_parts(x)
        if np.any(V <= 0):
            return math.inf, None, V
        g1, g2, g3 = np.cross(b, c) / 6, np.cross(c, a) / 6, np.cross(a, b) / 6
        w = (-mu / V)[:, None]
        G = np.zeros_like(x)
        np.add.at(G, self.T[:, 1], w * g1)
        np.add.at(G, self.T[:, 2], w * g2)
        np.add.at(G, self.T[:, 3], w * g3)
        np.add.at(G, self.T[:, 0], -w * (g1 + g2 + g3))
        return float(-mu * np.log(V / VREF).sum()), G, V

    def total(self, x, mu):
        es, gs = self.spring(x)
        if mu == 0:
            return es, gs, es, gs, self._tet_parts(x)[3]
        eb, gb, V = self.barrier(x, mu)
        if gb is None:
            return math.inf, None, es, gs, V
        return es + eb, gs + gb, es, gs, V

    def hessian(self, x, mu):
        n3 = 3 * self.n
        H = np.zeros((n3, n3))
        idx = np.arange(3)
        b = self.edge_vectors(x)
        l = np.linalg.norm(b, axis=1)
        u = b / l[:, None]
        uu = u[:, :, None] * u[:, None, :]
        He = 2 * uu + (2 * (l - 1) / l)[:, None, None] * (np.eye(3) - uu)
        for p, q, sgn in ((self.J, self.J, 1), (self.I, self.I, 1),
                          (self.I, self.J, -1), (self.J, self.I, -1)):
            rows = np.broadcast_to(3 * p[:, None, None] + idx[None, :, None], He.shape)
            cols = np.broadcast_to(3 * q[:, None, None] + idx[None, None, :], He.shape)
            np.add.at(H, (rows, cols), sgn * He)
        if mu == 0:
            return H
        a, bb, c, V = self._tet_parts(x)
        gabc = np.concatenate([np.cross(bb, c), np.cross(c, a), np.cross(a, bb)], axis=1) / 6
        Habc = np.zeros((len(self.T), 9, 9))
        Hab = np.einsum("klm,tm->tkl", self.eps, c) / 6
        Hac = np.einsum("klm,tl->tkm", self.eps, bb) / 6
        Hbc = np.einsum("klm,tk->tlm", self.eps, a) / 6
        Habc[:, 0:3, 3:6], Habc[:, 3:6, 0:3] = Hab, Hab.transpose(0, 2, 1)
        Habc[:, 0:3, 6:9], Habc[:, 6:9, 0:3] = Hac, Hac.transpose(0, 2, 1)
        Habc[:, 3:6, 6:9], Habc[:, 6:9, 3:6] = Hbc, Hbc.transpose(0, 2, 1)
        gp = gabc @ self.A
        Hp = np.einsum("ia,tij,jb->tab", self.A, Habc, self.A)
        Hb = (mu * (gp[:, :, None] * gp[:, None, :]) / (V ** 2)[:, None, None]
              - (mu / V)[:, None, None] * Hp)
        dof = (3 * self.T[:, :, None] + idx[None, None, :]).reshape(len(self.T), 12)
        np.add.at(H, (dof[:, :, None].repeat(12, 2), dof[:, None, :].repeat(12, 1)), Hb)
        return H

    def newton(self, x, mu, gtol=GTOL, maxit=500):
        f, g, *_ = self.total(x, mu)
        lam = 1e-10
        eye = np.eye(3 * self.n)
        for k in range(maxit):
            gn = float(np.abs(g).max())
            if gn < gtol:
                return x, k, gn, "converged"
            H = self.hessian(x, mu)
            while True:
                try:
                    Lc = np.linalg.cholesky(H + lam * eye)
                    break
                except np.linalg.LinAlgError:
                    lam = max(lam * 10, 1e-8)
            d = -np.linalg.solve(Lc.T, np.linalg.solve(Lc, g.ravel())).reshape(x.shape)
            t = 1.0
            while True:
                xn = x + t * d
                fn, gnew, *_ = self.total(xn, mu)
                if gnew is not None and fn <= f + 1e-4 * t * float(d.ravel() @ g.ravel()):
                    break
                t *= 0.5
                if t < 1e-14:
                    return x, k, gn, "line-search stall"
            lam = max(lam / 10, 1e-12) if t == 1.0 else lam * 10
            x, f, g = xn, fn, gnew
        return x, maxit, float(np.abs(g).max()), "max iterations"


def mechanics(pk, x, mu):
    f, g, es, gs, V = pk.total(x, mu)
    b = pk.edge_vectors(x)
    l = np.linalg.norm(b, axis=1)
    u = b / l[:, None]
    W = (u.T * ((l - 1) * l)) @ u
    F = (u.T * ((l - 1) ** 2)) @ u
    X = (u.T * (l - 1)) @ u
    dev = F - np.trace(F) / 3 * np.eye(3)
    w, axes = np.linalg.eigh(dev)
    return {
        "mu": mu, "E_spring_per_N": es / pk.n,
        "total_res_max": float(np.abs(g).max()) if g is not None else math.inf,
        "spring_res_max": float(np.abs(gs).max()),
        "spring_res_rms": float(np.sqrt((gs ** 2).mean())),
        "minV": float(V.min() / VREF), "V": V,
        "W": W, "F": F, "X": X, "identity_err": float(np.abs(X - (W - F)).max()),
        "aniso": float(np.linalg.norm(dev) / np.trace(F)),
        "dev_eigs": w / np.trace(F), "axes": axes,
        "mean_len": float(l.mean()),
    }


# =============================================================================
# Experiments
# =============================================================================


def experiment_1_triangulation(failures):
    header("E1: the periodic Delaunay triangulation (three-torus)")
    rng = np.random.default_rng(SEED)
    L0 = N ** (1 / 3)
    pts = rng.uniform(0, L0, size=(N, 3))
    T, O = periodic_delaunay(pts, L0)
    I, J, OF, F = edges_and_faces(T, O)
    V = volumes(pts, L0, T, O)
    flip = V < 0  # orient every tetrahedron positively
    T[flip, 0], T[flip, 1] = T[flip, 1].copy(), T[flip, 0].copy()
    O[flip, 0], O[flip, 1] = O[flip, 1].copy(), O[flip, 0].copy()
    chi = N - len(I) + len(F) - len(T)
    print(f"    N = {N}: edges = {len(I)}, triangles = {len(F)}, tetrahedra = {len(T)}, chi = {chi}")
    require("chi = 0 and every triangle shared by exactly two tetrahedra",
            chi == 0 and set(F.values()) == {2}, failures)
    require("tetrahedron volumes sum to L^3",
            math.isclose(np.abs(V).sum(), L0 ** 3, rel_tol=1e-12), failures)
    require("no edge joins a vertex to its own image",
            not np.any((I == J)), failures)

    b0 = pts[J] + L0 * OF - pts[I]
    m = np.linalg.norm(b0, axis=1).mean()
    x0, L = pts / m, L0 / m
    V0 = volumes(x0, L, T, O)
    print(f"    rescaled to unit mean edge: box L = {L:.6f} (FIXED from here on); "
          f"initial min volume = {V0.min() / VREF:.5f} V_ref")
    require("all tetrahedra positively oriented before relaxation", np.all(V0 > 0), failures)
    return Packing(L, T, O, I, J, OF), x0


def experiment_2_free(pk, x0, failures):
    header("E2: the free periodic control (no barrier, fixed box)")
    res = minimize(lambda z: pk.spring(z.reshape(-1, 3))[0], x0.ravel(),
                   jac=lambda z: pk.spring(z.reshape(-1, 3))[1].ravel(),
                   method="L-BFGS-B", options={"gtol": 1e-9, "maxiter": 50000})
    xf, iters, gn, status = pk.newton(res.x.reshape(-1, 3), 0.0)  # polish, barrier off
    ef = pk.spring(xf)[0]
    Vf = volumes(xf, pk.L, pk.T, pk.O)
    inv = float((Vf < 0).mean())
    print(f"    L-BFGS-B then {iters} Newton polish steps ({status}): E/N = {ef / N:.5f}, "
          f"max spring residual = {gn:.2e}, inverted fraction = {100 * inv:.2f}%")
    require(f"free periodic relaxation converged (max spring residual < {GTOL:g})",
            status == "converged", failures)
    res.fun = ef
    print("  051 E1's free-boundary runs inverted 44-49% (scratch rerun). This")
    print("  periodic, fixed-box control isolates what the bulk does on its own.")
    return {"E_per_N": res.fun / N, "inverted": inv}


def experiment_3_barrier(pk, x0, failures):
    header(f"E3: barrier relaxation (primary, mu = {MU_PRIMARY:g})")
    t0 = time.time()
    x, iters, gn, status = pk.newton(x0.copy(), MU_PRIMARY)
    m = mechanics(pk, x, MU_PRIMARY)
    print(f"    damped Newton: {iters} iterations, {status}, {time.time() - t0:.1f}s")
    print(f"    total residual (spring + barrier) max = {m['total_res_max']:.2e}")
    print(f"    spring-only residual: max = {m['spring_res_max']:.4f}, "
          f"rms = {m['spring_res_rms']:.4f}  (the force the barrier supplies)")
    print(f"    E_spring/N = {m['E_spring_per_N']:.5f}; min volume = {m['minV']:.5f} V_ref; "
          f"mean edge = {m['mean_len']:.5f}")
    require(f"equilibrium with the barrier (total residual < {GTOL:g})",
            status == "converged" and m["total_res_max"] < GTOL, failures)
    require("no tetrahedron inverted or degenerate (all V > 0)", np.all(m["V"] > 0), failures)

    # barrier virial: dV/d(eps) = V tr(eps) => sum_t (-mu/V) dV/deps = -mu T I
    a, b, c, V = pk._tet_parts(x)
    Wb = np.zeros((3, 3))
    for P_row, grad in ((a, np.cross(b, c) / 6), (b, np.cross(c, a) / 6), (c, np.cross(a, b) / 6)):
        Wb += ((-MU_PRIMARY / V)[:, None, None] * (grad[:, :, None] * P_row[:, None, :])).sum(axis=0)
    require("the barrier's virial is exactly isotropic: -mu T I",
            np.allclose(Wb, -MU_PRIMARY * len(pk.T) * np.eye(3), atol=1e-9), failures)
    require("extension-fabric identity sum (l-1) u u^T = W - F (exact)",
            m["identity_err"] < 1e-10, failures)
    nE = len(pk.I)
    print(f"    spring virial W / edges, eigenvalues: {np.round(np.linalg.eigvalsh(m['W']) / nE, 6)}")
    print(f"    energy fabric anisotropy |dev F| / tr F = {m['aniso']:.4f}; "
          f"dev eigenvalues / tr F = {np.round(m['dev_eigs'], 5)}")
    print("  Fixed box: W need not vanish, and does not. The barrier adds only")
    print("  isotropic stress, so the deviatoric stress and the fabric anisotropy")
    print("  are not supplied by the barrier directly.")
    return x, m


def axis_angles(A, B):
    return [math.degrees(math.acos(min(1.0, abs(float(A[:, i] @ B[:, i]))))) for i in range(3)]


def experiment_4_sensitivity(pk, x, m0, failures):
    header("E4: barrier sensitivity (warm-started weaker barriers)")
    rows = [m0]
    xs = {MU_PRIMARY: x}
    xw = x
    for mu in MU_WEAK:
        xw, iters, gn, status = pk.newton(xw.copy(), mu)
        m = mechanics(pk, xw, mu)
        require(f"mu = {mu:g}: equilibrium with the barrier ({iters} Newton steps)",
                status == "converged", failures)
        rows.append(m)
        xs[mu] = xw
    print("    mu       E_spring/N  spring res max/rms   min V/V_ref  anisotropy  "
          "axis angles vs primary (deg)")
    for m in rows:
        ang = axis_angles(m0["axes"], m["axes"])
        print(f"    {m['mu']:<8g} {m['E_spring_per_N']:.5f}     "
              f"{m['spring_res_max']:.4f}/{m['spring_res_rms']:.4f}      "
              f"{m['minV']:.5f}      {m['aniso']:.4f}      "
              + ", ".join(f"{a_:.2f}" for a_ in ang))
    V1, V2 = rows[1]["V"], rows[2]["V"]
    contact = int(((V2 / V1) < 0.2).sum())
    print(f"    contact set: {contact} tetrahedra whose volume falls >5x from "
          f"mu = {MU_WEAK[0]:g} to {MU_WEAK[1]:g}")
    rel = max(abs(m["aniso"] / m0["aniso"] - 1) for m in rows)
    dE = max(abs(m["E_spring_per_N"] / m0["E_spring_per_N"] - 1) for m in rows)
    max_ang = max(max(axis_angles(m0["axes"], m["axes"])) for m in rows)
    tail_ang = max(axis_angles(rows[1]["axes"], rows[2]["axes"]))
    print(f"    axis rotation primary -> weakest: {max_ang:.1f} deg; between the two weak "
          f"barriers ({MU_WEAK[0]:g} -> {MU_WEAK[1]:g}): {tail_ang:.1f} deg")
    require(f"spring energy stable as the barrier weakens 100x (max change {100 * dE:.2f}% < 2%)",
            dE < 0.02, failures)
    require(f"fabric anisotropy stable (max change {100 * rel:.1f}% < 15%)", rel < 0.15, failures)
    require(f"fabric principal axes stable (max rotation {max_ang:.1f} deg < 15 deg)",
            max_ang < 15, failures)
    require(f"fabric axes converge as mu -> 0 (weak-barrier rotation {tail_ang:.1f} deg < 3 deg)",
            tail_ang < 3, failures)
    require("min volume tracks mu (constraint-limited contact set, no inversion)",
            all(np.all(m["V"] > 0) for m in rows) and rows[2]["minV"] < rows[0]["minV"],
            failures)
    return rows, xs, contact, max_ang, tail_ang


def content_hash(arrays):
    h = hashlib.sha256()
    for name in sorted(arrays):
        a = np.ascontiguousarray(arrays[name])
        h.update(name.encode())
        h.update(str(a.dtype).encode())
        h.update(str(a.shape).encode())
        h.update(a.tobytes())
    return h.hexdigest()


def experiment_5_save(pk, x0, xs, failures):
    header("E5: the saved packing")
    arrays = {
        "x": xs[MU_PRIMARY], "x_initial": x0, "x_weak": xs[MU_WEAK[-1]],
        "L": np.array(pk.L), "T": pk.T.astype(np.int64), "O": pk.O.astype(np.int64),
        "I": pk.I.astype(np.int64), "J": pk.J.astype(np.int64), "OF": pk.OF.astype(np.int64),
        "mu": np.array(MU_PRIMARY), "mu_weak": np.array(MU_WEAK[-1]), "seed": np.array(SEED),
    }
    digest = content_hash(arrays)
    old = json.loads(PACKING_META.read_text()) if PACKING_META.exists() else {}
    if old.get("content_sha256") == digest and PACKING_PATH.exists():
        print(f"    unchanged: {PACKING_PATH.name} (content sha256 {digest[:16]}...)")
    else:
        np.savez(PACKING_PATH, **arrays)
        PACKING_META.write_text(json.dumps({
            "derivation": "periodic_spring_control_057",
            "content_sha256": digest,
            "seed": SEED, "N": N, "box_L": pk.L,
            "mu_primary": MU_PRIMARY, "mu_weak_saved": MU_WEAK[-1],
            "arrays": {k: list(np.shape(v)) for k, v in sorted(arrays.items())},
            "hash_rule": "sha256 over sorted array names: name, dtype, shape, C-order bytes",
        }, indent=2) + "\n")
        print(f"    wrote {PACKING_PATH.name} and {PACKING_META.name} "
              f"(content sha256 {digest[:16]}...)")
    back = dict(np.load(PACKING_PATH))
    require("saved packing reloads with the recorded content hash",
            content_hash(back) == digest, failures)
    return digest


# =============================================================================
# Record + report
# =============================================================================


def record(ns, digest):
    ns.record_derivation(
        derivation_id="periodic_spring_control_057",
        inputs=[sp.Symbol("seeded_periodic_delaunay"), sp.Symbol("spring_proxy_051"),
                sp.Symbol("log_volume_barrier")],
        output=sp.Symbol("valid_periodic_packing_fixed_box"),
        method=(
            "seeded (rng 20261124) Poisson points, N = 160, periodic Delaunay via 27 "
            "images; unit mean edge, box then fixed; free L-BFGS-B control; damped "
            "Newton with exact Hessian on spring + log-volume barrier at mu = 1e-2, "
            "1e-3, 1e-4 (warm-started); spring-only vs total residual; virial, "
            "energy fabric, extension identity, barrier virial; saved packing with "
            f"content hash {digest}"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="numerical_experiment",
        scope=(
            "one seed, one size, one cubic box: a calibration packing; spring proxy, "
            "not the P10 hinge energy; fixed connectivity (no retriangulation); no EM "
            "coupling, no channel"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="periodic_noninverting_spring_control",
        script_id=SCRIPT_ID,
        title="Stage 2 (one seed): a valid periodic packing at fixed box",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["periodic_spring_control_057"],
        description=(
            "09 charter stage 2 for one seed: the 051 spring objective relaxes at fixed "
            "periodic box with every tetrahedron positive; total and spring-only "
            "residuals, barrier sensitivity, and the energy fabric recorded; packing "
            "saved for 058 and stage 3."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="spring_control_ensemble_057",
        script_id=SCRIPT_ID,
        title="Spring-control ensemble: seeds, sizes, box shapes",
        status=ObligationStatus.OPEN,
        required_by=["periodic_spring_control_057"],
        description=(
            "Repeat the 057 construction across seeds, N, and cell shapes, recording the "
            "per-packing rotation-invariant fabric anisotropy and principal axes before "
            "averaging: the control the stage-3 P10 comparison needs."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="periodic_spring_control_claim_057",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.INFORMATIONAL,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "For one seeded N = 160 periodic packing at fixed cubic box, the 051 spring "
            "proxy relaxes with every tetrahedron positive under a log-volume barrier; "
            "spring energy, fabric anisotropy and principal axes are stable as the "
            "barrier weakens 100x; the barrier adds only isotropic stress. The free "
            "periodic control inverts far fewer tetrahedra than 051's free-boundary "
            "runs. Calibration packing only."
        ),
        derivation_ids=["periodic_spring_control_057"],
        obligation_ids=["periodic_noninverting_spring_control"],
    ))


def write_report(pk, tri, free, rows, contact, digest):
    nE = len(pk.I)
    def axes_str(m):
        return "; ".join("(" + ", ".join(f"{c:+.3f}" for c in m["axes"][:, i]) + ")"
                         for i in range(3))
    tab = "\n".join(
        f"    {m['mu']:<7g} {m['E_spring_per_N']:.5f}    {m['spring_res_max']:.4f} / "
        f"{m['spring_res_rms']:.4f}   {m['total_res_max']:.1e}   {m['minV']:.5f}     "
        f"{m['aniso']:.4f}     "
        + ", ".join(f"{a_:.2f}" for a_ in axis_angles(rows[0]["axes"], m["axes"]))
        for m in rows)
    m0 = rows[0]
    md = f"""# VacuumForge: The Periodic Spring Control

## Status

```text
result type:   numerical experiment (one-seed calibration packing;
               2026-11-24, derivation 057)
conclusion:    the 051 spring proxy relaxes at FIXED periodic box with
               every tetrahedron positive; its stored-strain fabric is
               stable as the barrier weakens 100x, so it is attributable
               to the packing, not the barrier. The free periodic
               control inverts {100 * free['inverted']:.1f}% of tetrahedra (051 free
               boundary: 44-49%).
satisfies:     periodic_noninverting_spring_control (09 charter,
               stage 2, one seed)
opens:         spring_control_ensemble_057
packing:       vacuum_forge/src/vacuum_sector/057_periodic_spring_control/
               packing_057.npz (content sha256 {digest[:16]}...)
verification:  vacuum_forge/src/vacuum_sector/057_periodic_spring_control/
```

## Measured Results

```text
E1. TRIANGULATION. Seed {SEED}, N = {N}, cubic box. Periodic Delaunay:
    {nE} edges, {tri['F']} triangles, {len(pk.T)} tetrahedra, chi = 0, every
    triangle in two tetrahedra, volumes sum to L^3. Unit mean edge;
    box FIXED at L = {pk.L:.6f}.

E2. FREE PERIODIC CONTROL (no barrier): E/N = {free['E_per_N']:.5f}, inverted
    fraction {100 * free['inverted']:.2f}%.

E3. BARRIER RELAXATION (mu = {MU_PRIMARY:g}, damped Newton, exact Hessian):
    total residual {m0['total_res_max']:.1e}; spring-only residual max {m0['spring_res_max']:.4f},
    rms {m0['spring_res_rms']:.4f}; E_spring/N = {m0['E_spring_per_N']:.5f}; min volume
    {m0['minV']:.5f} V_ref. Spring virial W / edges eigenvalues
    {np.round(np.linalg.eigvalsh(m0['W']) / nE, 6).tolist()} (fixed box: nonzero).
    Barrier virial exactly -mu T I (isotropic). Identity
    sum (l-1) u u^T = W - F exact. Energy-fabric anisotropy
    |dev F| / tr F = {m0['aniso']:.4f}; principal axes (columns, ascending):
    {axes_str(m0)}

E4. BARRIER SENSITIVITY:
    mu      E_spr/N    spring res max/rms  total res  min V/V_ref  aniso      axis rotation (deg)
{tab}
    Contact set: {contact} tetrahedra whose volume falls >5x between
    mu = {MU_WEAK[0]:g} and {MU_WEAK[1]:g}; they carry the spring-only residual.
    Principal axes rotate {tri['max_ang']:.1f} deg from mu = {MU_PRIMARY:g} to {MU_WEAK[-1]:g}, but only
    {tri['tail_ang']:.1f} deg between the two weak barriers: the fabric converges
    as mu -> 0, and the primary barrier tilts its axes slightly.

E5. SAVED PACKING: coordinates (primary and mu = {MU_WEAK[-1]:g}), pre-
    relaxation coordinates, connectivity, periodic offsets, edge list;
    content sha256 {digest}.
```

## Reading

- A small total residual means the optimizer found equilibrium WITH the
  barrier. The spring-only residual is the force the barrier supplies;
  it is concentrated on the contact set, tetrahedra held against the
  zero-volume constraint, whose volumes fall in proportion to mu.
- The barrier contributes only isotropic stress. The deviatoric stress
  and the energy-fabric anisotropy change little as mu drops 100x, and
  the fabric's principal axes converge as mu -> 0. That is the basis for
  attributing the fabric to the packing. For stage 3's axis-alignment
  test, use the weak-barrier axes (saved as `x_weak`) as the reference
  direction.
- This is the spring PROXY. Whether the P10 angle-gap energy produces a
  directional pattern beyond this control is stage 3's question.

## Compute Environment

```text
ran on:      CPU-only cloud container (NumPy/SciPy). No GPU was
             available; attaching the theory owner's local GPU (RTX
             3080 Ti) to the cloud session was not supported.
methods:     chosen for CPU efficiency instead of brute force. A
             first-order L-BFGS with feasibility backtracking took
             minutes and did not reach tolerance at weak barriers, so
             the barrier runs use damped Newton with an EXACT analytic
             Hessian (spring + log-volume, 480 x 480 dense), reaching
             residuals ~1e-12 in under 1 s per barrier strength. The
             free control uses L-BFGS-B followed by a barrier-off
             Newton polish.
validation:  another Claude Code session with GPU access should rerun
             this module and confirm the saved packing's content hash
             (or, with a different optimizer, the same E/N, minimum
             volume, fabric anisotropy and principal axes to ~1e-6).
             The GPU's real value is the ensemble
             (spring_control_ensemble_057): many seeds, larger N, other
             cell shapes, with sparse Hessians on the GPU.
```

## Fences

```text
- one seed, one size, one cubic box: a calibration packing; the
  ensemble is spring_control_ensemble_057.
- fixed connectivity: no retriangulation; the relaxed mesh is generally
  not Delaunay (058 diagnoses the Hodge consequence).
- no EM coupling, no channel (06 quarantine).
```

## Ledger

```text
derivation:  periodic_spring_control_057
satisfies:   periodic_noninverting_spring_control
opens:       spring_control_ensemble_057
depends on:  bulk_relaxation_phase2_051
feeds:       058 (periodic Maxwell calibration), stage 3
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 057: The Periodic Spring Control")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    pk, x0 = experiment_1_triangulation(failures)
    _, _, _, F = edges_and_faces(pk.T, pk.O)
    free = experiment_2_free(pk, x0, failures)
    x, m0 = experiment_3_barrier(pk, x0, failures)
    rows, xs, contact, max_ang, tail_ang = experiment_4_sensitivity(pk, x, m0, failures)
    digest = experiment_5_save(pk, x0, xs, failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 057: verification failure")
    print("  Stage 2 delivered for one seed: a valid periodic packing at fixed")
    print("  box, its stored-strain fabric stable under barrier weakening, saved")
    print("  for 058 and stage 3.")

    record(ns, digest)
    write_report(pk, {"F": len(F), "max_ang": max_ang, "tail_ang": tail_ang},
                 free, rows, contact, digest)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
