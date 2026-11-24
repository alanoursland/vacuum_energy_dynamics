#!/usr/bin/env python3
"""
periodic_maxwell_calibration.py

Derivation 058: ordinary vacuum Maxwell on the saved 057 packing
(09_maxwell_probe; maxwell_torus_calibration_056 and the first
stage-4 dispersion run, fork (a), one seed).

The question: can we keep the packing's measured strain and still
recover ordinary long-wavelength light propagation on the very same
geometry? The packing is read from 057's saved file and verified by
content hash, so a later change of Maxwell solver is known to leave the
geometry fixed.

Five experiments:

  E1. THE SAVED GEOMETRY. Load packing_057.npz, verify the content hash
      recorded by 057, rebuild the periodic complex (vertices, edges,
      triangles, tetrahedra with image offsets), check chi = 0 and
      d1 d0 = 0 with and without a Bloch twist.

  E2. THE HODGE CHOICE (diagnosed, not assumed). Signed circumcentric
      weights are assembled on the relaxed mesh and on the original
      (pre-relaxation) Delaunay mesh. Individual signed contributions
      can be negative even when an assembled weight is positive; what
      matters is the assembled weight. On the Delaunay mesh the
      circumcentric dual is the Voronoi diagram, so every assembled
      weight is non-negative; relaxation at fixed connectivity breaks
      the Delaunay property, and some assembled weights go negative.
      The uniform-field energy identity sum_e *1_e b_e b_e^T = Vol I
      still holds exactly with signed weights. Decision rule: if any
      assembled weight is zero or negative, use Whitney mass matrices,
      and keep that discretization for all paired comparisons.

  E3. TORUS GATES AT k = 0 (G3a, G3b; fork (a)). Whitney M1, M2 are
      positive definite. G3a: nullity of d1 is V - 1 + 3; removing the
      gradient subspace in the M1 inner product leaves exactly three
      dimensions. G3b: those three dimensions span the sampled uniform
      E fields (principal angles), which are closed, co-closed, and
      carry exactly the metric energy.

  E4. THE TWISTED GATE (G3c). Under a nontrivial Bloch twist:
      (i) the full curl-curl problem has exactly V gradient zero modes;
      (ii) after projecting gradients out, the two lowest transverse
      modes have small POSITIVE frequencies, well separated from the
      next mode, and they fall toward zero with k.

  E5. THE DISPERSION RUN. Phase speeds omega / (c |k|) of the two
      transverse branches along a box axis [100], a face diagonal [110]
      and a body diagonal [111], for ka inside the supercell Brillouin
      zone (a = mean edge length). Reported: each polarization, their
      mean, their splitting, and a fit 1 - v = alpha (ka)^2. Ordinary
      flat vacuum is the target: both curves approach 1 in every
      direction. The finite-ka spread is the apparent optical effect
      this mesh and solver produce on their own: the baseline for any
      later fork-(b) run.

Fences: fork (a) only (ordinary vacuum coefficients; no strain coupling).
One seed, one size, one cubic box: the result describes this packing
repeated periodically. Whitney discretization fixed for paired
comparisons. No claim that spatial quanta produce EM; no channel.
"""

import csv
import hashlib
import itertools as it
import json
import math
import time
from pathlib import Path

import numpy as np
from scipy.linalg import eigh, null_space

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
PROBE_DIR = REPO_ROOT / "theory_v3" / "development" / "vacuum_sector" / "09_maxwell_probe"
REPORT_PATH = PROBE_DIR / "periodic_maxwell_calibration_vacuumforge.md"
PLOT_PATH = PROBE_DIR / "periodic_maxwell_dispersion_058.png"
CSV_PATH = SCRIPT_PATH.parent / "dispersion_058.csv"
PACKING_DIR = SCRIPT_PATH.parents[1] / "057_periodic_spring_control"
PACKING_PATH = PACKING_DIR / "packing_057.npz"
PACKING_META = PACKING_DIR / "packing_057.json"

DEPENDENCIES = [
    ("packing_dep_058", "057_periodic_spring_control__periodic_spring_control",
     "periodic_spring_control_057"),
    ("benchmark_dep_058", "056_maxwell_regular_mesh__maxwell_regular_mesh",
     "maxwell_regular_mesh_056"),
]

DIRECTIONS = {"[100] box axis": (1, 0, 0), "[110] face diagonal": (1, 1, 0),
              "[111] body diagonal": (1, 1, 1)}
KA = (0.025, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7)
EDGES_L = list(it.combinations(range(4), 2))
FACES_L = list(it.combinations(range(4), 3))


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


def content_hash(arrays):
    """Same rule as 057: sha256 over sorted names: name, dtype, shape, bytes."""
    h = hashlib.sha256()
    for name in sorted(arrays):
        a = np.ascontiguousarray(arrays[name])
        h.update(name.encode())
        h.update(str(a.dtype).encode())
        h.update(str(a.shape).encode())
        h.update(a.tobytes())
    return h.hexdigest()


# =============================================================================
# The periodic complex with Bloch phases
# =============================================================================


def canon(v, o):
    order = np.lexsort((o[:, 2], o[:, 1], o[:, 0], v))
    vs, os_ = v[order], o[order]
    par = 1
    perm = list(order)
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                par = -par
    key = tuple(int(a) for a in vs) + tuple(int(a) for a in (os_ - os_[0]).ravel())
    return key, vs, os_ - os_[0], os_[0], par


class Complex:
    """Periodic simplicial complex; cochains are Bloch-periodic with phase
    exp(i k . L n) on the image translated by the integer vector n."""

    def __init__(self, x, L, T, O):
        self.x, self.L, self.T, self.O = x, L, T, O
        self.nV, self.nT = len(x), len(T)
        E, F = {}, {}
        self.loc_e = np.zeros((self.nT, 6), int)
        self.sgn_e = np.zeros((self.nT, 6))
        self.tr_e = np.zeros((self.nT, 6, 3))
        self.loc_f = np.zeros((self.nT, 4), int)
        self.sgn_f = np.zeros((self.nT, 4))
        self.tr_f = np.zeros((self.nT, 4, 3))
        for t in range(self.nT):
            for n, (a, b) in enumerate(EDGES_L):
                k, v, o, n0, par = canon(T[t, [a, b]], O[t, [a, b]])
                if k not in E:
                    E[k] = (len(E), v, o)
                self.loc_e[t, n], self.sgn_e[t, n], self.tr_e[t, n] = E[k][0], par, n0
            for n, f in enumerate(FACES_L):
                k, v, o, n0, par = canon(T[t, list(f)], O[t, list(f)])
                if k not in F:
                    F[k] = (len(F), v, o)
                self.loc_f[t, n], self.sgn_f[t, n], self.tr_f[t, n] = F[k][0], par, n0
        self.E, self.F = E, F
        self.nE, self.nF = len(E), len(F)
        self.Ev = [None] * self.nE
        for _, (i, v, o) in E.items():
            self.Ev[i] = (v, o)
        self.Fv = [None] * self.nF
        for _, (i, v, o) in F.items():
            self.Fv[i] = (v, o)
        self.evec = np.array([x[v[1]] + L * o[1] - x[v[0]] for v, o in self.Ev])
        self._whitney_local()

    def phase(self, kv, n):
        return np.exp(1j * self.L * (np.asarray(n) @ kv))

    def d0(self, kv):
        D = np.zeros((self.nE, self.nV), complex)
        for e, (v, o) in enumerate(self.Ev):
            D[e, v[0]] -= 1
            D[e, v[1]] += self.phase(kv, o[1])
        return D

    def d1(self, kv):
        D = np.zeros((self.nF, self.nE), complex)
        for f, (v, o) in enumerate(self.Fv):
            for a, b in ((0, 1), (1, 2), (2, 0)):
                k, _, _, n0, par = canon(np.array([v[a], v[b]]), np.array([o[a], o[b]]))
                D[f, self.E[k][0]] += par * self.phase(kv, n0)
        return D

    def _whitney_local(self):
        P = self.x[self.T] + self.L * self.O
        Mx = np.concatenate([P, np.ones((self.nT, 4, 1))], axis=2)
        G = np.transpose(np.linalg.inv(Mx)[:, :3, :], (0, 2, 1))  # grad lambda_a
        V = np.linalg.det(P[:, 1:] - P[:, :1]) / 6
        self.tet_vol = V

        def ill(i, j):
            return (1 + (i == j)) / 20  # int lambda_i lambda_j / V

        M1 = np.zeros((self.nT, 6, 6))
        for p, (a, b) in enumerate(EDGES_L):
            for q, (c, d) in enumerate(EDGES_L):
                dot = lambda u, w: np.einsum("ti,ti->t", G[:, u], G[:, w])
                M1[:, p, q] = V * (ill(a, c) * dot(b, d) - ill(a, d) * dot(b, c)
                                   - ill(b, c) * dot(a, d) + ill(b, d) * dot(a, c))

        def comps(f):
            a, b, c = f
            return [(a, np.cross(G[:, b], G[:, c])), (b, np.cross(G[:, c], G[:, a])),
                    (c, np.cross(G[:, a], G[:, b]))]

        M2 = np.zeros((self.nT, 4, 4))
        for p, f in enumerate(FACES_L):
            for q, g in enumerate(FACES_L):
                val = 0
                for i, ci in comps(f):
                    for j, cj in comps(g):
                        val = val + ill(i, j) * np.einsum("ti,ti->t", ci, cj)
                M2[:, p, q] = 4 * V * val
        self.M1loc, self.M2loc = M1, M2

    def whitney_mass(self, kv):
        M1 = np.zeros((self.nE, self.nE), complex)
        M2 = np.zeros((self.nF, self.nF), complex)
        for t in range(self.nT):
            r1 = self.sgn_e[t] * np.exp(1j * self.L * (self.tr_e[t] @ kv))
            r2 = self.sgn_f[t] * np.exp(1j * self.L * (self.tr_f[t] @ kv))
            M1[np.ix_(self.loc_e[t], self.loc_e[t])] += np.conj(r1)[:, None] * self.M1loc[t] * r1[None, :]
            M2[np.ix_(self.loc_f[t], self.loc_f[t])] += np.conj(r2)[:, None] * self.M2loc[t] * r2[None, :]
        return M1, M2


def circumcenter(P):
    p0 = P[0]
    A = P[1:] - p0
    G = A @ A.T
    return p0 + np.linalg.solve(G, 0.5 * np.diag(G)) @ A


def circumcentric_weights(cx):
    """Signed circumcentric *1 (per edge) and *2 (per face), assembled."""
    s1, s2 = np.zeros(cx.nE), np.zeros(cx.nF)
    neg, tot = 0, 0
    for t in range(cx.nT):
        P = cx.x[cx.T[t]] + cx.L * cx.O[t]
        ct = circumcenter(P)
        for nf, f in enumerate(FACES_L):
            opp = [i for i in range(4) if i not in f][0]
            Pf = P[list(f)]
            cf = circumcenter(Pf)
            nrm = np.cross(Pf[1] - Pf[0], Pf[2] - Pf[0])
            area = np.linalg.norm(nrm) / 2
            nrm /= np.linalg.norm(nrm)
            htf = float((ct - cf) @ nrm) * float(np.sign((P[opp] - Pf[0]) @ nrm))
            s2[cx.loc_f[t, nf]] += htf / area
            for a, b in it.combinations(range(3), 2):
                c3 = 3 - a - b
                pa, pb, pc = Pf[a], Pf[b], Pf[c3]
                m = (pa + pb) / 2
                ed = (pb - pa) / np.linalg.norm(pb - pa)
                perp = (cf - m) - ((cf - m) @ ed) * ed
                hfe = float(np.linalg.norm(perp)) * (float(np.sign((pc - m) @ perp))
                                                     if np.linalg.norm(perp) > 0 else 1.0)
                contrib = 0.5 * htf * hfe
                tot += 1
                neg += contrib < 0
                ne = EDGES_L.index(tuple(sorted((f[a], f[b]))))
                s1[cx.loc_e[t, ne]] += contrib / np.linalg.norm(pb - pa)
    return s1, s2, neg, tot


def local_delaunay_violations(cx):
    """Interior faces whose neighbouring tetrahedron's far vertex lies inside
    the circumsphere of the other (non-locally-Delaunay faces)."""
    owners = {}
    for t in range(cx.nT):
        for nf, f in enumerate(FACES_L):
            owners.setdefault(cx.loc_f[t, nf], []).append((t, nf))
    bad = 0
    for f, ((t1, f1), (t2, f2)) in owners.items():
        P1 = cx.x[cx.T[t1]] + cx.L * cx.O[t1]
        P2 = cx.x[cx.T[t2]] + cx.L * cx.O[t2]
        c1 = circumcenter(P1)
        r1 = np.linalg.norm(P1[0] - c1)
        opp2 = [i for i in range(4) if i not in FACES_L[f2]][0]
        # align t2 to t1's image frame through the shared face's first vertex
        v1 = [cx.T[t1, i] for i in FACES_L[f1]]
        shift = None
        for i in FACES_L[f2]:
            for j in FACES_L[f1]:
                if cx.T[t2, i] == cx.T[t1, j]:
                    shift = (cx.O[t1, j] - cx.O[t2, i])
                    break
            if shift is not None:
                break
        q = P2[opp2] + cx.L * shift
        bad += np.linalg.norm(q - c1) < r1 * (1 - 1e-9)
        del v1
    return bad, len(owners)


# =============================================================================
# Experiments
# =============================================================================


def experiment_1_geometry(failures):
    header("E1: the saved 057 geometry")
    meta = json.loads(PACKING_META.read_text())
    arrays = dict(np.load(PACKING_PATH))
    digest = content_hash(arrays)
    print(f"    {PACKING_PATH.name}: content sha256 {digest[:16]}... "
          f"(recorded {meta['content_sha256'][:16]}...)")
    require("packing content hash matches 057's record (geometry fixed)",
            digest == meta["content_sha256"], failures)
    x, L, T, O = arrays["x"], float(arrays["L"]), arrays["T"], arrays["O"]
    cx = Complex(x, L, T, O)
    chi = cx.nV - cx.nE + cx.nF - cx.nT
    print(f"    V = {cx.nV}, E = {cx.nE}, F = {cx.nF}, T = {cx.nT}, chi = {chi}; L = {L:.6f}")
    require("complex rebuilt: chi = 0, edge count matches 057's edge list",
            chi == 0 and cx.nE == len(arrays["I"]), failures)
    require("all tetrahedra positively oriented", np.all(cx.tet_vol > 0), failures)
    kt = np.array([0.3, -0.2, 0.1])
    err = max(float(np.abs(cx.d1(k) @ cx.d0(k)).max()) for k in (np.zeros(3), kt))
    require(f"d1 d0 = 0 at k = 0 and under a twist (max {err:.1e})", err < 1e-12, failures)
    return cx, arrays, digest


def experiment_2_hodge(cx, arrays, failures):
    header("E2: the Hodge choice -- signed circumcentric weights, diagnosed")
    out = {}
    for label, xx in (("relaxed", arrays["x"]), ("pre-relaxation Delaunay", arrays["x_initial"])):
        c = Complex(xx, cx.L, cx.T, cx.O)
        s1, s2, neg, tot = circumcentric_weights(c)
        ident = (c.evec.T * s1) @ c.evec / c.L ** 3
        bad, nf = local_delaunay_violations(c)
        out[label] = dict(n1=int((s1 <= 0).sum()), n2=int((s2 <= 0).sum()), min1=float(s1.min()),
                          min2=float(s2.min()), neg=neg, tot=tot, ident=ident, bad=bad, nf=nf)
        print(f"    {label}: negative elementary contributions {neg}/{tot}; assembled "
              f"*1 <= 0: {out[label]['n1']}/{c.nE} (min {s1.min():.3e}); "
              f"*2 <= 0: {out[label]['n2']}/{c.nF} (min {s2.min():.3e}); "
              f"non-locally-Delaunay faces {bad}/{nf}")
        require(f"{label}: uniform-field identity sum *1 b b^T = Vol I holds (signed)",
                np.allclose(ident, np.eye(3), atol=1e-9), failures)
    d = out["pre-relaxation Delaunay"]
    require("pre-relaxation Delaunay mesh: all assembled weights >= 0 (Voronoi dual) "
            "although some elementary contributions are negative",
            d["n1"] == 0 and d["n2"] == 0 and d["min1"] > -1e-12 and d["neg"] > 0
            and d["bad"] == 0, failures)
    r = out["relaxed"]
    use_whitney = r["n1"] > 0 or r["n2"] > 0
    print(f"    decision: {'WHITNEY mass matrices' if use_whitney else 'circumcentric'} "
          "for this calibration and all paired comparisons that follow")
    require("relaxation at fixed connectivity broke the Delaunay property "
            "(diagnosis of the non-positive assembled weights)",
            (not use_whitney) or r["bad"] > 0, failures)
    return out, use_whitney


def experiment_3_torus(cx, failures):
    header("E3: torus gates at k = 0 (G3a, G3b; fork (a), Whitney)")
    k0 = np.zeros(3)
    D0, D1 = cx.d0(k0).real, cx.d1(k0).real
    M1, M2 = (m.real for m in cx.whitney_mass(k0))
    e1, e2 = np.linalg.eigvalsh(M1).min(), np.linalg.eigvalsh(M2).min()
    print(f"    Whitney M1 min eigenvalue {e1:.4e}, M2 min eigenvalue {e2:.4e}")
    require("Whitney mass matrices positive definite", e1 > 0 and e2 > 0, failures)
    s0 = np.linalg.svd(D0, compute_uv=False)
    s1 = np.linalg.svd(D1, compute_uv=False)
    r0 = int((s0 > 1e-9 * s0.max()).sum())
    nul1 = cx.nE - int((s1 > 1e-9 * s1.max()).sum())
    Z = null_space(D1)
    Q = Z - D0 @ np.linalg.lstsq(D0.T @ M1 @ D0, D0.T @ M1 @ Z, rcond=None)[0]
    u, sv, _ = np.linalg.svd(Q, full_matrices=False)
    hdim = int((sv > 1e-8 * sv.max()).sum())
    print(f"    rank d0 = {r0} (V - 1 = {cx.nV - 1}); nullity d1 = {nul1} (V + 2 = {cx.nV + 2}); "
          f"dimensions left after removing gradients = {hdim}")
    require("G3a: nullity of d1 is V - 1 + 3 and exactly three harmonic dimensions remain",
            r0 == cx.nV - 1 and nul1 == cx.nV + 2 and hdim == 3, failures)
    H = u[:, :hdim]
    U = cx.evec  # columns: the sampled uniform E fields along x, y, z
    closed = float(np.abs(D1 @ U).max())
    coclosed = float(np.abs(D0.T @ M1 @ U).max())
    energy = U.T @ M1 @ U / cx.L ** 3

    def m1orth(A):
        w, v = np.linalg.eigh(A.T @ M1 @ A)
        return A @ v / np.sqrt(w)

    cos = np.linalg.svd(m1orth(H).T @ M1 @ m1orth(U), compute_uv=False)
    print(f"    uniform fields: |d1 U| = {closed:.1e}, |d0^T M1 U| = {coclosed:.1e}, "
          f"energy / Vol = diag {np.round(np.diag(energy), 10).tolist()}")
    print(f"    principal-angle cosines (harmonic subspace vs uniform fields): "
          f"{np.round(cos, 12).tolist()}")
    require("G3b: uniform fields closed, co-closed, carry the metric energy exactly, and span "
            "the harmonic subspace",
            closed < 1e-12 and coclosed < 1e-10 and np.allclose(energy, np.eye(3), atol=1e-10)
            and np.all(cos > 1 - 1e-10), failures)
    return {"r0": r0, "nul1": nul1, "hdim": hdim, "cos": cos, "M1min": e1, "M2min": e2}


def transverse(cx, kv, nlow=3, full=False):
    D0, D1 = cx.d0(kv), cx.d1(kv)
    M1, M2 = cx.whitney_mass(kv)
    K = D1.conj().T @ M2 @ D1
    res = {}
    if full:
        s0 = np.linalg.svd(D0, compute_uv=False)
        res["rank_d0"] = int((s0 > 1e-9 * s0.max()).sum())
        res["w_full"] = eigh(K, M1, eigvals_only=True, subset_by_index=[0, cx.nV + 2])
    Z = null_space(D0.conj().T @ M1)
    w = eigh(Z.conj().T @ K @ Z, Z.conj().T @ M1 @ Z, eigvals_only=True,
             subset_by_index=[0, nlow - 1])
    res["w"] = w
    return res


def experiment_4_twist(cx, a, failures):
    header("E4: the twisted gate (G3c)")
    out = []
    for ka in (0.05, 0.1):
        nh = np.ones(3) / math.sqrt(3)
        r = transverse(cx, nh * ka / a, full=True)
        wf = r["w_full"]
        nzero = int((np.abs(wf) < 1e-9).sum())
        w = r["w"]
        print(f"    ka = {ka} along [111]: rank d0(k) = {r['rank_d0']}; full problem: "
              f"{nzero} zero modes, next omega^2 = {wf[cx.nV]:.4e}; projected: omega^2 = "
              f"{np.array2string(w, precision=6)}")
        require(f"G3c(i) ka = {ka}: exactly V = {cx.nV} gradient zero modes "
                "(no harmonic classes; gradients gain one dimension)",
                r["rank_d0"] == cx.nV and nzero == cx.nV, failures)
        require(f"G3c(ii) ka = {ka}: two small POSITIVE transverse frequencies, "
                "well separated from the next mode",
                w[0] > 1e-6 and w[1] > 1e-6 and w[2] > 50 * w[1], failures)
        out.append((ka, w))
    require("G3c(ii): the transverse frequencies fall toward zero with k",
            out[0][1][1] < out[1][1][0], failures)
    return out


def experiment_5_dispersion(cx, a, failures):
    header("E5: the dispersion run -- transverse phase speeds vs ka (fork (a))")
    bz = math.pi * a / cx.L
    print(f"    a = mean edge length = {a:.5f}; supercell zone edge along [100] at ka = {bz:.4f}")
    rows = []
    recip = [2 * math.pi / cx.L * np.array(g) for g in it.product((-1, 0, 1), repeat=3) if any(g)]
    for name, d in DIRECTIONS.items():
        nh = np.array(d, float) / np.linalg.norm(d)
        for ka in KA:
            kv = nh * ka / a
            assert np.all(np.abs(kv) <= math.pi / cx.L + 1e-12), "k outside the supercell zone"
            w = transverse(cx, kv, nlow=4)["w"]
            v = np.sqrt(w[:2]) / np.linalg.norm(kv)
            fold = min(float(np.linalg.norm(kv - G)) for G in recip)
            rows.append({"direction": name, "ka": ka, "v_slow": float(v[0]), "v_fast": float(v[1]),
                         "v_mean": float(v.mean()), "splitting": float(v[1] - v[0]),
                         "gap_ratio": float(w[2] / w[1]),
                         "folded_rel": float(np.sqrt(w[2:4]).mean() / fold - 1),
                         "unfolded": bool(np.linalg.norm(kv) < fold)})
        r_ = [r for r in rows if r["direction"] == name]
        print(f"    {name}:")
        for r in r_:
            print(f"      ka = {r['ka']:<5}  v = {r['v_slow']:.6f}, {r['v_fast']:.6f}  "
                  f"mean {r['v_mean']:.6f}  splitting {r['splitting']:.2e}")
    fits = {}
    for name in DIRECTIONS:
        r_ = [r for r in rows if r["direction"] == name]
        k2 = np.array([r["ka"] ** 2 for r in r_])
        dv = np.array([1 - r["v_mean"] for r in r_])
        alpha = float((k2 @ dv) / (k2 @ k2))
        sp_ = np.array([r["splitting"] for r in r_])
        beta = float((k2 @ sp_) / (k2 @ k2))
        fits[name] = (alpha, beta, float(np.abs(dv - alpha * k2).max()))
        print(f"    fit {name}: 1 - v_mean = {alpha:.5f} (ka)^2 (max residual {fits[name][2]:.1e}); "
              f"splitting ~ {beta:.5f} (ka)^2")
    smallest = [r for r in rows if r["ka"] == KA[0]]
    dev0 = max(max(abs(1 - r["v_slow"]), abs(1 - r["v_fast"])) for r in smallest)
    require(f"both polarizations approach c in every direction (|1 - v| = {dev0:.1e} "
            f"< 1e-4 at ka = {KA[0]})", dev0 < 1e-4, failures)
    worst_gap = min(r["gap_ratio"] for r in rows)
    worst_fold = max(abs(r["folded_rel"]) for r in rows)
    print(f"    next mode pair = the transverse branch folded from k - G: frequency within "
          f"{100 * worst_fold:.1f}% of c min|k - G|; smallest omega^2 gap ratio {worst_gap:.2f} "
          "(at the zone edge, where the folded branch meets)")
    require("the tracked pair is the unfolded branch (|k| < min |k - G|) and stays below "
            "the next mode across the scan",
            all(r["unfolded"] for r in rows) and worst_gap > 1.05, failures)
    require("the next mode pair is the folded transverse branch (within 5% of c min|k - G|), "
            "not a mesh-scale mode", worst_fold < 0.05, failures)
    alphas = [f[0] for f in fits.values()]
    print(f"    direction spread of the (ka)^2 coefficient: "
          f"{min(alphas):.5f} .. {max(alphas):.5f}")
    return rows, fits, bz


# =============================================================================
# Plot, record, report
# =============================================================================


def write_plot(rows, a):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    surface, ink, ink2, grid = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3de"
    slow_c, fast_c = "#2a78d6", "#eb6834"  # categorical slots 1, 2 (validated)
    plt.rcParams.update({"font.size": 10, "axes.edgecolor": ink2, "axes.labelcolor": ink2,
                         "xtick.color": ink2, "ytick.color": ink2, "text.color": ink})
    fig, axs = plt.subplots(2, 3, figsize=(11, 6.2), sharex=True,
                            gridspec_kw={"height_ratios": [2.2, 1]})
    fig.patch.set_facecolor(surface)
    names = list(DIRECTIONS)
    vmin = min(min(r["v_slow"] for r in rows), 0.996)
    smax = max(r["splitting"] for r in rows)
    for j, name in enumerate(names):
        r_ = [r for r in rows if r["direction"] == name]
        ka = [r["ka"] for r in r_]
        ax = axs[0, j]
        ax.set_facecolor(surface)
        ax.axhline(1.0, color=ink2, lw=1, ls=(0, (4, 3)), zorder=1)
        ax.plot(ka, [r["v_slow"] for r in r_], color=slow_c, lw=2, marker="o", ms=5,
                label="slower polarization", zorder=3)
        ax.plot(ka, [r["v_fast"] for r in r_], color=fast_c, lw=2, marker="o", ms=5,
                label="faster polarization", zorder=3)
        ax.set_ylim(vmin - 0.0004, 1.0006)
        ax.set_title(name, color=ink, fontsize=11)
        ax.grid(True, color=grid, lw=0.8)
        ax.set_axisbelow(True)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        if j == 0:
            ax.set_ylabel("phase speed  ω / (c|k|)")
            ax.text(0.02, 1.0002, "flat-vacuum target", color=ink2, fontsize=9, va="bottom")
        ax2 = axs[1, j]
        ax2.set_facecolor(surface)
        ax2.plot(ka, [1e3 * r["splitting"] for r in r_], color=ink2, lw=2, marker="o", ms=5)
        ax2.set_ylim(0, 1e3 * smax * 1.15)
        ax2.grid(True, color=grid, lw=0.8)
        ax2.set_axisbelow(True)
        for s in ("top", "right"):
            ax2.spines[s].set_visible(False)
        ax2.set_xlabel("k a   (a = mean edge length)")
        if j == 0:
            ax2.set_ylabel("splitting  ×10³")
    h, l_ = axs[0, 0].get_legend_handles_labels()
    fig.legend(h, l_, loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.0))
    fig.suptitle("Transverse phase speeds on the 057 packing, ordinary vacuum Maxwell (Whitney)",
                 y=1.045, color=ink, fontsize=12)
    fig.tight_layout()
    fig.savefig(PLOT_PATH, dpi=150, bbox_inches="tight", facecolor=surface,
                metadata={"Software": None, "CreationDate": None})
    plt.close(fig)
    print(f"[INFO] plot written: {PLOT_PATH}")


def write_csv(rows):
    with CSV_PATH.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        for r in rows:
            w.writerow({k: (f"{v:.10f}" if isinstance(v, float) else v) for k, v in r.items()})
    print(f"[INFO] data written: {CSV_PATH}")


def record(ns, digest):
    ns.record_derivation(
        derivation_id="periodic_maxwell_calibration_058",
        inputs=[sp.Symbol("packing_057"), sp.Symbol("whitney_forms"), sp.Symbol("bloch_twist")],
        output=sp.Symbol("periodic_maxwell_baseline_fork_a"),
        method=(
            f"057 packing (content sha256 {digest}); signed circumcentric weights "
            "diagnosed on relaxed and pre-relaxation meshes; Whitney M1/M2; torus "
            "nullity and harmonic-subspace principal angles at k = 0; Bloch-twisted "
            "gradient count and gradient-projected transverse modes; phase speeds along "
            "[100], [110], [111] for ka in the supercell zone"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="numerical_benchmark",
        scope=(
            "fork (a) only; one seed, one size, one cubic box (the packing repeated "
            "periodically); Whitney discretization fixed for paired comparisons; no EM "
            "coupling to strain; no channel"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="maxwell_torus_calibration_056",
        script_id=SCRIPT_ID,
        title="Periodic-solver calibration: torus gates G3a-G3c",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["periodic_maxwell_calibration_058"],
        description=(
            "On the 057 packing with Whitney mass matrices: G3a nullity V - 1 + 3 with "
            "three harmonic dimensions; G3b they span the uniform E fields; G3c exactly "
            "V twisted gradient zero modes and two small positive transverse frequencies."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="maxwell_packing_sweep",
        script_id=SCRIPT_ID,
        title="Stage 4: Maxwell sweep across packings (ensemble; fork (b) once specified)",
        status=ObligationStatus.OPEN,
        required_by=["periodic_maxwell_calibration_058"],
        description=(
            "058 is the one-seed fork-(a) calibration. Remaining: the same measurement "
            "across seeds, sizes and cell shapes; the P10 packings from stage 3; axis "
            "alignment with the stage-3 fabric; and fork (b) on the same packings once "
            "a strain coupling is specified."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="periodic_maxwell_calibration_claim_058",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.INFORMATIONAL,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "On the saved 057 packing, ordinary vacuum Maxwell with Whitney forms passes "
            "the torus gates and recovers c in every tested direction as ka -> 0; the "
            "finite-ka departures (quadratic in ka, small polarization splitting) are "
            "the mesh-and-solver baseline for later strain-coupled comparisons. "
            "Calibration only."
        ),
        derivation_ids=["periodic_maxwell_calibration_058"],
        obligation_ids=["maxwell_torus_calibration_056"],
    ))


def write_report(cx, digest, hodge, torus, twist, rows, fits, bz, a):
    r, d = hodge["relaxed"], hodge["pre-relaxation Delaunay"]
    disp = []
    for name in DIRECTIONS:
        disp.append(f"    {name}")
        for row in [x for x in rows if x["direction"] == name]:
            disp.append(f"      ka {row['ka']:<5}  {row['v_slow']:.6f}  {row['v_fast']:.6f}  "
                        f"mean {row['v_mean']:.6f}  splitting {row['splitting']:.2e}")
    disp = "\n".join(disp)
    fit = "\n".join(f"    {n:<22} 1 - v_mean = {f[0]:.5f} (ka)^2   splitting ~ {f[1]:.5f} (ka)^2"
                    for n, f in fits.items())
    tw = "\n".join(f"    ka = {ka} [111]: projected omega^2 = "
                   + ", ".join(f"{x:.6f}" for x in w) for ka, w in twist)
    md = f"""# VacuumForge: Ordinary Maxwell on the Periodic Spring Packing

## Status

```text
result type:   numerical calibration (fork (a), one seed; 2026-11-24,
               derivation 058)
conclusion:    on the exact 057 geometry, ordinary vacuum Maxwell
               (Whitney forms) passes the torus gates and recovers c
               in every tested direction as ka -> 0. The finite-ka
               departures are quadratic in ka and small: the
               mesh-and-solver baseline for later strain-coupled runs.
satisfies:     maxwell_torus_calibration_056 (gates G3a-G3c)
opens:         maxwell_packing_sweep (stage 4 proper)
geometry:      057 packing, content sha256 {digest[:16]}...
verification:  vacuum_forge/src/vacuum_sector/058_periodic_maxwell_calibration/
```

![Transverse phase speeds](periodic_maxwell_dispersion_058.png)

Top row: the two transverse phase speeds ω/(c|k|) against ka along a
box axis, a face diagonal, and a body diagonal; the dashed line is the
flat-vacuum target. Bottom row: their splitting (faster − slower),
×10³. Numbers below; data in
`vacuum_forge/src/vacuum_sector/058_periodic_maxwell_calibration/dispersion_058.csv`.

## Measured Results

```text
E1. GEOMETRY. 057 packing reloaded, content hash verified. V = {cx.nV},
    E = {cx.nE}, F = {cx.nF}, T = {cx.nT}, chi = 0, all tetrahedra positive;
    d1 d0 = 0 with and without a Bloch twist.

E2. HODGE CHOICE (signed circumcentric weights, assembled):
    pre-relaxation Delaunay: *1 <= 0 on {d['n1']}/{cx.nE} edges, *2 <= 0 on
      {d['n2']}/{cx.nF} faces, although {d['neg']}/{d['tot']} elementary
      contributions are negative; {d['bad']} non-locally-Delaunay faces.
    relaxed: *1 <= 0 on {r['n1']}/{cx.nE} edges (min {r['min1']:.3e}), *2 <= 0 on
      {r['n2']}/{cx.nF} faces (min {r['min2']:.3e}); {r['bad']}/{r['nf']} faces no
      longer locally Delaunay.
    The identity sum *1 b b^T = Vol I holds exactly on both (signed).
    Diagnosis: relaxation at fixed connectivity broke the Delaunay
    property. Decision: Whitney mass matrices, kept for all paired
    comparisons.

E3. TORUS GATES (k = 0, Whitney; M1 min eig {torus['M1min']:.3e}, M2 min eig
    {torus['M2min']:.3e}):
    G3a  rank d0 = {torus['r0']} = V - 1; nullity d1 = {torus['nul1']} = V + 2; {torus['hdim']}
         dimensions remain after removing gradients.
    G3b  uniform E fields closed, co-closed, energy = Vol I exactly;
         principal-angle cosines with the harmonic subspace = 1, 1, 1.

E4. TWISTED GATE (G3c): exactly V = {cx.nV} gradient zero modes in the full
    problem; after projection, two small positive transverse
    frequencies, far below the next mode:
{tw}

E5. DISPERSION (fork (a); a = mean edge = {a:.5f}; supercell zone edge
    along [100] at ka = {bz:.4f}). Columns: slower, faster phase speed:
{disp}
    Quadratic fits:
{fit}
```

## Reading

- Both polarizations approach c in every tested direction as ka -> 0.
  The packing keeps its stored spring strain (057) while ordinary
  long-wavelength light propagation is recovered on the same geometry.
- At finite ka the speeds fall below c quadratically, with a small
  polarization splitting. Both numbers are this mesh and solver's own
  apparent optical effect: the baseline a fork-(b) run on the same
  packing must exceed.
- Near the supercell zone edge the next pair of modes is the same
  transverse branch folded back from k − G. It is a consequence of the
  periodic repetition, not a mesh-scale mode, and it limits how far in
  ka one box can be scanned.
- The quadratic coefficient varies little between the three
  directions at this size. Whether that spread is a property of the
  packing, of the cubic supercell, or of finite size needs the
  ensemble (maxwell_packing_sweep).

## Compute Environment

```text
ran on:      CPU-only cloud container (NumPy/SciPy). No GPU was
             available; attaching the theory owner's local GPU (RTX
             3080 Ti) to the cloud session was not supported.
methods:     chosen for CPU efficiency at this size. Whitney mass
             matrices assembled per tetrahedron; Bloch-twisted
             operators built once per k; the gradient subspace removed
             by an explicit null-space projection so only the lowest
             few transverse modes are computed (dense complex
             Hermitian eigensolves, ~1078 unknowns, ~1.5 s per k). The
             torus gates use exact ranks and principal angles.
validation:  another Claude Code session with GPU access should rerun
             this module on the same 057 packing (hash-verified) and
             confirm the gates and the phase speeds to ~1e-8. A GPU is
             what makes the next step practical: larger packings
             (smaller ka at the zone edge), many seeds and cell shapes
             (maxwell_packing_sweep), with sparse Whitney operators and
             a GPU shift-invert or LOBPCG eigensolver replacing the
             dense solves.
```

## Fences

```text
- fork (a) only: ordinary vacuum coefficients, no strain coupling.
- one seed, one size, one cubic box: the packing repeated
  periodically; ka is limited by the supercell zone.
- Whitney discretization, chosen by the E2 rule; keep it fixed for
  paired comparisons.
- no claim that spatial quanta produce EM; no channel (06 quarantine).
```

## Ledger

```text
derivation:  periodic_maxwell_calibration_058
satisfies:   maxwell_torus_calibration_056
opens:       maxwell_packing_sweep
depends on:  periodic_spring_control_057, maxwell_regular_mesh_056
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 058: Ordinary Maxwell on the Periodic Spring Packing")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    cx, arrays, digest = experiment_1_geometry(failures)
    a = float(np.linalg.norm(cx.evec, axis=1).mean())
    hodge, use_whitney = experiment_2_hodge(cx, arrays, failures)
    torus = experiment_3_torus(cx, failures)
    twist = experiment_4_twist(cx, a, failures)
    rows, fits, bz = experiment_5_dispersion(cx, a, failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 058: verification failure")
    print("  Calibration delivered: the torus gates pass on the exact 057 geometry,")
    print("  both transverse polarizations approach c in every tested direction,")
    print("  and the finite-ka spread is recorded as the mesh-and-solver baseline.")

    record(ns, digest)
    write_csv(rows)
    write_plot(rows, a)
    write_report(cx, digest, hodge, torus, twist, rows, fits, bz, a)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
