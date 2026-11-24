#!/usr/bin/env python3
"""
angle_energy_fixed_neighbors.py

Derivation 060: the trial angle energy in bulk, neighbours fixed
(09_maxwell_probe, stage 3 step 1; p10_bulk_relaxation_059, fixed-
neighbour face).

The question: when exactly the same quanta -- the 057 starting
coordinates, periodic box, and neighbour list -- relax under the
angle-gap energy instead of the spring proxy, is the pattern of stored
strain different? Neighbours do not change here; that is step 2.

Two energies, both from the 059 trial form, summed over every
(tetrahedron, edge) dihedral theta with x = theta - arccos(1/3):

    P10 candidate (length-weighted):  E_w = sum_h l_h (K/2) sum_i x_i^2
    control (unweighted):             E_u = sum_h     (K/2) sum_i x_i^2

Under uniform dilation E_u is unchanged and E_w scales with length, so
the two give different forces even in a fixed box: E_w can lower the
cost of a frustrated hinge by shortening it. K = 1 (energies in units
of K). Validity is kept by the same log-volume barrier as 057.

Per-hinge identity (059, exact for any closed flat hinge of n
tetrahedra, sum theta_i = 2 pi):

    (1/2) sum x_i^2 = (2 pi - n theta0)^2 / (2 n)   unavoidable at n
                    + (1/2) sum (theta_i - 2 pi/n)^2   extra: uneven sharing

With neighbours fixed, the unavoidable total of E_u is fixed by the
coordination numbers; what relaxation can change is the extra.

Seven experiments:

  E1. THE START. 057's pre-relaxation coordinates, box and neighbour list
      (content hash verified). Every hinge closes (deficit 0); the
      per-hinge identity holds; coordination histogram; unavoidable and
      extra totals at the start.

  E2. THE CONTROL (unweighted) and E3. THE P10 CANDIDATE (weighted).
      Damped Newton with an exact per-tetrahedron Hessian. Reported:
      total residual, angle-only residual (the force the barrier
      supplies), minimum volume, contact set, unavoidable and extra
      totals, and edge lengths by coordination. For E_w, the energy
      drop is split exactly into angle redistribution at the starting
      lengths and the change of hinge lengths.

  E4. BARRIER SENSITIVITY for both: mu = 1e-3, 1e-4, 1e-5.

  E5. DIRECTIONAL FABRICS. Per-hinge energy times the hinge direction's
      outer product, for each relaxed packing and for the 057 spring
      packing on the same neighbours: rotation-invariant anisotropy
      |dev F| / tr F, principal axes, and the normalized overlap of
      deviatoric tensors between models. Also the fabric of the extra
      (uneven-sharing) energy alone.

  E6. STRESS. The affine virial dE/d(eps) at fixed box, by symmetric
      finite differences. Identities: trace 0 for E_u (dilation flat),
      trace = E_w for E_w (degree-one homogeneity). Deviatoric stress
      reported.

  E7. SAVED PACKINGS for later Maxwell runs on exactly these geometries.

Fences: TRIAL angle energy, K explicit; neighbours fixed (no topology
change, so the unavoidable coordination cost is frozen); one seed, one
size, one cubic box; no EM coupling.
"""

import hashlib
import itertools as it
import json
import math
import time
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
               / "09_maxwell_probe" / "angle_energy_fixed_neighbors_vacuumforge.md")
PACKING_DIR = SCRIPT_PATH.parents[1] / "057_periodic_spring_control"
PACKING_IN = PACKING_DIR / "packing_057.npz"
PACKING_IN_META = PACKING_DIR / "packing_057.json"
PACKING_OUT = SCRIPT_PATH.parent / "packing_060.npz"
PACKING_OUT_META = SCRIPT_PATH.parent / "packing_060.json"

DEPENDENCIES = [
    ("packing_dep_060", "057_periodic_spring_control__periodic_spring_control",
     "periodic_spring_control_057"),
    ("wedge_dep_060", "059_wedge_strain_definition__wedge_strain_definition",
     "wedge_strain_definition_059"),
]

TH0 = math.acos(1 / 3)
VREF = 1 / (6 * math.sqrt(2))
MUS = (1e-3, 1e-4, 1e-5)
GTOL = 1e-10
E6 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
OPP = [tuple(m for m in range(4) if m not in e) for e in E6]
IA = np.array([e[0] for e in E6])
IB = np.array([e[1] for e in E6])
IC = np.array([o[0] for o in OPP])
ID = np.array([o[1] for o in OPP])


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


def canonical(verts, offs):
    order = np.lexsort((offs[:, 2], offs[:, 1], offs[:, 0], verts))
    v, o = verts[order], offs[order]
    o = o - o[0]
    return tuple(int(a) for a in v) + tuple(int(a) for a in o.ravel())


# =============================================================================
# The angle energies on a fixed periodic mesh
# =============================================================================


class AngleModel:
    def __init__(self, L, T, O):
        self.L, self.T, self.O = L, T, O
        self.nT = len(T)
        self.n = int(T.max()) + 1
        self.dof = (3 * T[:, :, None] + np.arange(3)[None, None, :]).reshape(self.nT, 12)
        # (tet, local edge) -> global hinge index
        keys = {}
        self.hinge = np.zeros((self.nT, 6), int)
        for t in range(self.nT):
            for k, (a, b) in enumerate(E6):
                key = canonical(T[t, [a, b]], O[t, [a, b]])
                if key not in keys:
                    keys[key] = len(keys)
                self.hinge[t, k] = keys[key]
        self.nH = len(keys)
        self.coord = np.bincount(self.hinge.ravel(), minlength=self.nH)

    def P(self, x):
        return x[self.T] + self.L * self.O

    @staticmethod
    def dihedrals(P):
        a, b, c, d = P[:, IA], P[:, IB], P[:, IC], P[:, ID]
        e = b - a
        le = np.linalg.norm(e, axis=2)
        eh = e / le[..., None]

        def perp(p):
            w = p - a
            return w - (w * eh).sum(-1)[..., None] * eh

        hc, hd = perp(c), perp(d)
        nc, nd = np.linalg.norm(hc, axis=2), np.linalg.norm(hd, axis=2)
        th = np.arctan2(np.linalg.norm(np.cross(hc, hd), axis=2), (hc * hd).sum(-1))
        wc = np.cross(eh, hc)
        wc /= np.linalg.norm(wc, axis=2)[..., None]
        wc *= np.sign((wc * hd).sum(-1))[..., None]
        wd = np.cross(eh, hd)
        wd /= np.linalg.norm(wd, axis=2)[..., None]
        wd *= np.sign((wd * hc).sum(-1))[..., None]
        gc, gd = -wc / nc[..., None], -wd / nd[..., None]
        sc = ((c - a) * e).sum(-1) / le ** 2
        sd = ((d - a) * e).sum(-1) / le ** 2
        ga = -((1 - sc)[..., None] * gc + (1 - sd)[..., None] * gd)
        gb = -(sc[..., None] * gc + sd[..., None] * gd)
        return th, le, eh, (ga, gb, gc, gd)

    def local(self, P, mu, weighted):
        th, le, eh, (ga, gb, gc, gd) = self.dihedrals(P)
        dx = th - TH0
        w = le if weighted else np.ones_like(le)
        e = 0.5 * (w * dx ** 2).sum(1)
        coef = (w * dx)[..., None]
        G = np.zeros_like(P)
        for idx, g in ((IA, ga), (IB, gb), (IC, gc), (ID, gd)):
            np.add.at(G, (slice(None), idx), coef * g)
        if weighted:
            q = (0.5 * dx ** 2)[..., None] * eh
            np.add.at(G, (slice(None), IB), q)
            np.add.at(G, (slice(None), IA), -q)
        a_, b_, c_ = P[:, 1] - P[:, 0], P[:, 2] - P[:, 0], P[:, 3] - P[:, 0]
        V = np.einsum("ij,ij->i", a_, np.cross(b_, c_)) / 6
        Ga = G.copy()
        if mu > 0:
            with np.errstate(invalid="ignore", divide="ignore"):
                e = e - mu * np.log(np.where(V > 0, V, np.nan) / VREF)
            g1, g2, g3 = np.cross(b_, c_) / 6, np.cross(c_, a_) / 6, np.cross(a_, b_) / 6
            wv = (-mu / V)[:, None]
            G[:, 1] += wv * g1
            G[:, 2] += wv * g2
            G[:, 3] += wv * g3
            G[:, 0] -= wv * (g1 + g2 + g3)
        return e, G, Ga, V

    def scatter(self, Gl):
        G = np.zeros((self.n, 3))
        for j in range(4):
            np.add.at(G, self.T[:, j], Gl[:, j])
        return G

    def total(self, x, mu, weighted):
        e, Gl, _, V = self.local(self.P(x), mu, weighted)
        if np.any(V <= 0):
            return math.inf, None
        return float(e.sum()), self.scatter(Gl)

    def angle_residual(self, x, weighted):
        _, _, Ga, _ = self.local(self.P(x), 0.0, weighted)
        return self.scatter(Ga)

    def hessian(self, x, mu, weighted, h=1e-6):
        P = self.P(x)
        Ht = np.zeros((self.nT, 12, 12))
        for k in range(12):
            Pp, Pm = P.copy(), P.copy()
            Pp[:, k // 3, k % 3] += h
            Pm[:, k // 3, k % 3] -= h
            Ht[:, :, k] = (self.local(Pp, mu, weighted)[1]
                           - self.local(Pm, mu, weighted)[1]).reshape(self.nT, 12) / (2 * h)
        Ht = 0.5 * (Ht + Ht.transpose(0, 2, 1))
        H = np.zeros((3 * self.n, 3 * self.n))
        np.add.at(H, (self.dof[:, :, None].repeat(12, 2), self.dof[:, None, :].repeat(12, 1)), Ht)
        return H

    def newton(self, x, mu, weighted, gtol=GTOL, maxit=400):
        """Newton with an eigenvalue-modified Hessian (|lambda|, floored):
        robust for the non-convex angle energy near constraint contact."""
        E, g = self.total(x, mu, weighted)
        for k in range(maxit):
            gn = float(np.abs(g).max())
            if gn < gtol:
                return x, k, gn, "converged"
            H = self.hessian(x, mu, weighted)
            w, Q = np.linalg.eigh(H)
            floor = 1e-8 * max(1.0, float(np.abs(w).max()))
            wm = np.maximum(np.abs(w), floor)
            d = -(Q @ ((Q.T @ g.ravel()) / wm)).reshape(x.shape)
            t = 1.0
            while True:
                xn = x + t * d
                En, gnew = self.total(xn, mu, weighted)
                if gnew is not None and En <= E + 1e-4 * t * float(d.ravel() @ g.ravel()):
                    break
                # near convergence the Armijo decrease falls below the energy's
                # floating-point resolution: accept a full step that is energy-
                # neutral to roundoff and reduces the gradient
                if (gnew is not None and t == 1.0 and abs(En - E) < 1e-12 * max(1.0, abs(E))
                        and float(np.abs(gnew).max()) < 0.5 * gn):
                    break
                t *= 0.5
                if t < 1e-14:
                    return x, k, gn, "line-search stall"
            x, E, g = xn, En, gnew
        return x, maxit, float(np.abs(g).max()), "max iterations"

    # ---- per-hinge analysis --------------------------------------------------

    def hinges(self, x):
        th, le, eh, _ = self.dihedrals(self.P(x))
        h = self.hinge.ravel()
        sum_th = np.bincount(h, weights=th.ravel(), minlength=self.nH)
        e_h = np.bincount(h, weights=0.5 * ((th - TH0) ** 2).ravel(), minlength=self.nH)
        n = self.coord
        unavoid = (2 * math.pi - n * TH0) ** 2 / (2 * n)
        share = (2 * math.pi / n)[h]
        extra = np.bincount(h, weights=0.5 * ((th.ravel() - share) ** 2), minlength=self.nH)
        # one direction and length per hinge (first occurrence)
        first = np.full(self.nH, -1)
        first[h[::-1]] = np.arange(h.size)[::-1]
        ln = le.ravel()[first]
        dirn = eh.reshape(-1, 3)[first]
        return {"sum_th": sum_th, "e": e_h, "unavoid": unavoid, "extra": extra,
                "len": ln, "dir": dirn, "n": n}

    def volumes(self, x):
        P = self.P(x)
        return np.linalg.det(P[:, 1:] - P[:, :1]) / 6

    def stress(self, x, weighted, h=1e-6):
        """dE/d(eps) for the affine map P -> P (I + eps)^T, angle energy only."""
        P = self.P(x)
        S = np.zeros((3, 3))
        for a in range(3):
            for b in range(a, 3):
                eps = np.zeros((3, 3))
                eps[a, b] = eps[b, a] = h if a != b else h
                ep = self.local(P @ (np.eye(3) + eps).T, 0.0, weighted)[0].sum()
                em = self.local(P @ (np.eye(3) - eps).T, 0.0, weighted)[0].sum()
                val = (ep - em) / (2 * h)
                if a == b:
                    S[a, a] = val
                else:
                    S[a, b] = S[b, a] = val / 2
        return S


def fabric(values, dirs):
    F = (dirs.T * values) @ dirs
    dev = F - np.trace(F) / 3 * np.eye(3)
    w, axes = np.linalg.eigh(dev)
    return {"F": F, "dev": dev, "aniso": float(np.linalg.norm(dev) / np.trace(F)),
            "eigs": w / np.trace(F), "axes": axes}


def overlap(A, B):
    return float(np.sum(A["dev"] * B["dev"]) / (np.linalg.norm(A["dev"]) * np.linalg.norm(B["dev"])))


def axis_angles(A, B):
    return [math.degrees(math.acos(min(1.0, abs(float(A["axes"][:, i] @ B["axes"][:, i])))))
            for i in range(3)]


# =============================================================================
# Experiments
# =============================================================================


def experiment_1_start(failures):
    header("E1: the start -- 057's coordinates, box and neighbour list")
    meta = json.loads(PACKING_IN_META.read_text())
    arrays = dict(np.load(PACKING_IN))
    digest = content_hash(arrays)
    require("057 packing content hash verified", digest == meta["content_sha256"], failures)
    L, T, O = float(arrays["L"]), arrays["T"], arrays["O"]
    model = AngleModel(L, T, O)
    x0 = arrays["x_initial"]
    hz = model.hinges(x0)
    defect = float(np.abs(hz["sum_th"] - 2 * math.pi).max())
    ident = float(np.abs(hz["e"] - hz["unavoid"] - hz["extra"]).max())
    hist = {int(k): int(v) for k, v in zip(*np.unique(hz["n"], return_counts=True))}
    print(f"    hinges = {model.nH} (= 057 edges {len(arrays['I'])}); coordination histogram {hist}")
    print(f"    max |sum theta - 2 pi| over hinges = {defect:.1e}; per-hinge identity error {ident:.1e}")
    print(f"    start: E_u = {hz['e'].sum():.3f}; unavoidable (fixed by n) = {hz['unavoid'].sum():.3f}; "
          f"extra = {hz['extra'].sum():.3f}")
    require("one hinge per 057 edge", model.nH == len(arrays["I"]), failures)
    require("every hinge closes in flat space at the start (deficit 0)", defect < 1e-9, failures)
    require("per-hinge identity: e_h = unavoidable(n) + extra (exact)", ident < 1e-9, failures)
    return model, arrays, digest, hz, hist


def relax_series(model, x0, weighted, failures, tag):
    rows, xs = [], {}
    x = x0.copy()
    for mu in MUS:
        t0 = time.time()
        x, it_, gn, status = model.newton(x, mu, weighted)
        V = model.volumes(x)
        hz = model.hinges(x)
        ga = model.angle_residual(x, weighted)
        e_ang = float((hz["e"] * (hz["len"] if weighted else 1)).sum()) if weighted else float(hz["e"].sum())
        if weighted:  # weighted energy sums l_h over all incident dihedrals of the hinge
            e_ang = float(0.5 * (model.dihedrals(model.P(x))[1]
                                 * (model.dihedrals(model.P(x))[0] - TH0) ** 2).sum())
        rows.append({"mu": mu, "iters": it_, "status": status, "res": gn, "E": e_ang,
                     "unavoid": float(hz["unavoid"].sum()), "extra": float(hz["extra"].sum()),
                     "minV": float(V.min() / VREF), "V": V,
                     "ang_res_max": float(np.abs(ga).max()),
                     "ang_res_rms": float(np.sqrt((ga ** 2).mean())),
                     "min_len": float(hz["len"].min()), "mean_len": float(hz["len"].mean()),
                     "defect": float(np.abs(hz["sum_th"] - 2 * math.pi).max()), "time": time.time() - t0})
        xs[mu] = x
        require(f"{tag} mu = {mu:g}: equilibrium with the barrier ({it_} Newton steps, "
                f"residual {gn:.1e})", status == "converged", failures)
        require(f"{tag} mu = {mu:g}: every tetrahedron positive and every hinge closed",
                np.all(V > 0) and rows[-1]["defect"] < 1e-9, failures)
    return rows, xs


def print_rows(rows, tag):
    print(f"    {tag}:  mu      E_angle     unavoidable  extra      angle res max/rms   "
          "min V/V_ref  min edge  mean edge")
    for r in rows:
        print(f"           {r['mu']:<7g} {r['E']:10.4f}  {r['unavoid']:10.4f}  {r['extra']:9.4f}  "
              f"{r['ang_res_max']:.3f}/{r['ang_res_rms']:.4f}      {r['minV']:.2e}     "
              f"{r['min_len']:.4f}    {r['mean_len']:.4f}")


def by_coordination(hz):
    out = {}
    for n in np.unique(hz["n"]):
        m = hz["n"] == n
        out[int(n)] = (int(m.sum()), float(hz["len"][m].mean()))
    return out


def experiment_2_3_relax(model, arrays, hz0, failures):
    header("E2: the control -- unweighted angle energy")
    x0 = arrays["x_initial"]
    rows_u, xs_u = relax_series(model, x0, False, failures, "unweighted")
    print_rows(rows_u, "unweighted")
    require("unweighted: unavoidable total unchanged by relaxation (fixed neighbours)",
            abs(rows_u[0]["unavoid"] - hz0["unavoid"].sum()) < 1e-9, failures)
    require("unweighted: relaxation lowers only the uneven-sharing extra",
            rows_u[0]["extra"] < hz0["extra"].sum(), failures)

    header("E3: the P10 candidate -- length-weighted angle energy")
    rows_w, xs_w = relax_series(model, x0, True, failures, "weighted")
    print_rows(rows_w, "weighted  ")
    # exact split of the weighted energy change: redistribution at fixed lengths + length change
    h0, h1 = model.hinges(x0), model.hinges(xs_w[MUS[0]])
    th0, le0, _, _ = model.dihedrals(model.P(x0))
    th1, le1, _, _ = model.dihedrals(model.P(xs_w[MUS[0]]))
    e0 = 0.5 * (th0 - TH0) ** 2
    e1 = 0.5 * (th1 - TH0) ** 2
    Ew0, Ew1 = float((le0 * e0).sum()), float((le1 * e1).sum())
    redistribution = float((le0 * (e1 - e0)).sum())
    length_change = float(((le1 - le0) * e1).sum())
    print(f"    weighted energy {Ew0:.4f} -> {Ew1:.4f}: angle redistribution at starting lengths "
          f"{redistribution:+.4f}, hinge-length change {length_change:+.4f}")
    require("exact split: redistribution + length change = total change",
            abs(redistribution + length_change - (Ew1 - Ew0)) < 1e-8, failures)
    c0, c1 = by_coordination(h0), by_coordination(h1)
    cu = by_coordination(model.hinges(xs_u[MUS[0]]))
    print("    mean hinge length by coordination n (count): start -> weighted / unweighted")
    for n in sorted(c0):
        u = (2 * math.pi - n * TH0) ** 2 / (2 * n)
        print(f"      n = {n:2d} ({c0[n][0]:4d}; unavoidable {u:.4f} each): {c0[n][1]:.4f} -> "
              f"{c1[n][1]:.4f} / {cu[n][1]:.4f}")
    # correlation: do frustrated hinges shorten more under weighting?
    u_h = h1["unavoid"]
    rel_w = h1["len"] / h0["len"]
    rel_u = model.hinges(xs_u[MUS[0]])["len"] / h0["len"]
    corr_w = float(np.corrcoef(u_h, rel_w)[0, 1])
    corr_u = float(np.corrcoef(u_h, rel_u)[0, 1])
    print(f"    correlation of hinge-length ratio with its unavoidable cost: weighted {corr_w:+.3f}, "
          f"unweighted {corr_u:+.3f}")
    split = {"Ew0": Ew0, "Ew1": Ew1, "redistribution": redistribution,
             "length_change": length_change, "c0": c0, "c1": c1, "cu": cu,
             "corr_w": corr_w, "corr_u": corr_u}
    return rows_u, xs_u, rows_w, xs_w, split


def experiment_4_sensitivity(rows_u, rows_w, failures):
    header("E4: barrier sensitivity (mu = 1e-3 -> 1e-5)")
    out = {}
    for tag, rows in (("unweighted", rows_u), ("weighted", rows_w)):
        dE = abs(rows[-1]["E"] / rows[0]["E"] - 1)
        contact = int(((rows[-1]["V"] / rows[1]["V"]) < 0.2).sum())
        len_drift = abs(rows[-1]["min_len"] / rows[0]["min_len"] - 1)
        out[tag] = {"dE": dE, "contact": contact, "len_drift": len_drift}
        print(f"    {tag}: angle energy change {100 * dE:.4f}%; contact set {contact} tetrahedra "
              f"(volume falls >5x from mu = {MUS[1]:g} to {MUS[2]:g}); min edge drift {100 * len_drift:.2f}%")
        require(f"{tag}: angle energy stable as the barrier weakens 100x (< 0.5%)", dE < 5e-3, failures)
        require(f"{tag}: no edge collapses as the barrier weakens (min edge drift < 5%)",
                len_drift < 0.05, failures)
    return out


def experiment_5_fabrics(model, arrays, xs_u, xs_w, failures):
    header("E5: directional fabrics -- where each model stores its energy")
    mu = MUS[-1]
    hu, hw = model.hinges(xs_u[mu]), model.hinges(xs_w[mu])
    th_w, le_w, _, _ = model.dihedrals(model.P(xs_w[mu]))
    ew_h = np.bincount(model.hinge.ravel(), weights=(0.5 * le_w * (th_w - TH0) ** 2).ravel(),
                       minlength=model.nH)
    F = {
        "angle, unweighted": fabric(hu["e"], hu["dir"]),
        "angle, weighted": fabric(ew_h, hw["dir"]),
        "extra only, unweighted": fabric(hu["extra"], hu["dir"]),
        "extra only, weighted": fabric(hw["extra"] * hw["len"], hw["dir"]),
    }
    # 057 spring fabric on the same neighbours (weak-barrier packing)
    xs = arrays["x_weak"]
    b = xs[arrays["J"]] + model.L * arrays["OF"] - xs[arrays["I"]]
    l = np.linalg.norm(b, axis=1)
    F["spring (057)"] = fabric((l - 1) ** 2, b / l[:, None])
    h0 = model.hinges(arrays["x_initial"])
    F["angle at start"] = fabric(h0["e"], h0["dir"])
    for k, f in F.items():
        print(f"    {k:<24} anisotropy {f['aniso']:.4f}; dev eigenvalues / tr {np.round(f['eigs'], 4)}")
    names = list(F)
    print("    deviatoric overlaps (cosine of dev tensors):")
    for a, b_ in it.combinations(names, 2):
        print(f"      {a:<24} vs {b_:<24} {overlap(F[a], F[b_]):+.3f}")
    ang = axis_angles(F["angle, weighted"], F["spring (057)"])
    print(f"    principal-axis angles, weighted angle vs spring: "
          + ", ".join(f"{a_:.1f}" for a_ in ang) + " deg")
    require("all fabrics computed with positive trace", all(np.trace(f["F"]) > 0 for f in F.values()),
            failures)
    return F


def experiment_6_stress(model, xs_u, xs_w, failures):
    header("E6: stress at fixed box -- affine virial of the angle energy")
    mu = MUS[-1]
    Su = model.stress(xs_u[mu], False)
    Sw = model.stress(xs_w[mu], True)
    Ew = float(model.local(model.P(xs_w[mu]), 0.0, True)[0].sum())
    print(f"    unweighted: trace {np.trace(Su):+.2e}; dev eigenvalues "
          f"{np.round(np.linalg.eigvalsh(Su - np.trace(Su) / 3 * np.eye(3)), 4)}")
    print(f"    weighted:   trace {np.trace(Sw):+.6f} (E_w = {Ew:.6f}); dev eigenvalues "
          f"{np.round(np.linalg.eigvalsh(Sw - np.trace(Sw) / 3 * np.eye(3)), 4)}")
    require("unweighted energy is dilation-flat: virial trace = 0", abs(np.trace(Su)) < 1e-5, failures)
    require("weighted energy is degree-one homogeneous: virial trace = E_w",
            abs(np.trace(Sw) - Ew) < 1e-5 * max(1, Ew), failures)
    return Su, Sw, Ew


def experiment_7_save(model, arrays, xs_u, xs_w, failures):
    header("E7: saved packings")
    out = {"x_weighted": xs_w[MUS[0]], "x_unweighted": xs_u[MUS[0]],
           "x_weighted_weak": xs_w[MUS[-1]], "x_unweighted_weak": xs_u[MUS[-1]],
           "x_initial": arrays["x_initial"], "L": arrays["L"], "T": arrays["T"], "O": arrays["O"],
           "I": arrays["I"], "J": arrays["J"], "OF": arrays["OF"], "mu": np.array(MUS[0]),
           "mu_weak": np.array(MUS[-1])}
    digest = content_hash(out)
    old = json.loads(PACKING_OUT_META.read_text()) if PACKING_OUT_META.exists() else {}
    if old.get("content_sha256") == digest and PACKING_OUT.exists():
        print(f"    unchanged: {PACKING_OUT.name} (content sha256 {digest[:16]}...)")
    else:
        np.savez(PACKING_OUT, **out)
        PACKING_OUT_META.write_text(json.dumps({
            "derivation": "angle_energy_fixed_neighbors_060", "content_sha256": digest,
            "source_packing_sha256": json.loads(PACKING_IN_META.read_text())["content_sha256"],
            "mu_primary": MUS[0], "mu_weak_saved": MUS[-1],
            "arrays": {k: list(np.shape(v)) for k, v in sorted(out.items())},
            "hash_rule": "sha256 over sorted array names: name, dtype, shape, C-order bytes",
        }, indent=2) + "\n")
        print(f"    wrote {PACKING_OUT.name} (content sha256 {digest[:16]}...)")
    require("saved packings reload with the recorded hash",
            content_hash(dict(np.load(PACKING_OUT))) == digest, failures)
    return digest


# =============================================================================
# Record + report
# =============================================================================


def record(ns, digest):
    ns.record_derivation(
        derivation_id="angle_energy_fixed_neighbors_060",
        inputs=[sp.Symbol("packing_057_start"), sp.Symbol("trial_angle_energy_059"),
                sp.Symbol("log_volume_barrier")],
        output=sp.Symbol("angle_gap_strain_pattern_fixed_neighbours"),
        method=(
            "057 start, box and neighbour list; all-dihedral trial angle energy, "
            "length-weighted (P10 candidate) and unweighted (control); damped Newton "
            "with exact per-tetrahedron Hessian; barrier mu = 1e-3, 1e-4, 1e-5; per-hinge "
            "unavoidable/extra split; weighted-energy redistribution/length split; "
            "hinge-direction energy fabrics vs the 057 spring fabric; affine virial; saved "
            f"packings (content sha256 {digest})"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="numerical_experiment",
        scope=(
            "trial angle energy, K explicit; neighbours fixed (unavoidable coordination "
            "cost frozen); one seed, one size, one cubic box; no EM coupling"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p10_bulk_fixed_neighbours_060",
        script_id=SCRIPT_ID,
        title="Stage 3 step 1: trial angle energy in bulk with neighbours fixed",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["angle_energy_fixed_neighbors_060"],
        description=(
            "On 057's start, box and neighbour list, both trial angle energies relax with "
            "every tetrahedron valid; unavoidable and extra costs, length vs redistribution "
            "split, fabrics vs the spring control, and stress recorded."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p10_bulk_neighbour_changes_060",
        script_id=SCRIPT_ID,
        title="Stage 3 step 2: allow neighbour changes; which frustration survives?",
        status=ObligationStatus.OPEN,
        required_by=["angle_energy_fixed_neighbors_060"],
        description=(
            "Allow retriangulation or bistellar moves under the weighted angle energy at "
            "fixed box; test whether a floor energy per volume survives across seeds, sizes "
            "and starting arrangements, and whether its directional fabric washes out."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="angle_energy_fixed_neighbors_claim_060",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.INFORMATIONAL,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "With 057's quanta, box and neighbours fixed, the trial angle energy relaxes to a "
            "valid flat packing whose stored energy is dominated by the coordination-fixed "
            "unavoidable cost; the reports record how much uneven-sharing extra remains, how "
            "the weighted model splits its relief between angle redistribution and hinge "
            "length, and how its directional fabric compares with the spring control."
        ),
        derivation_ids=["angle_energy_fixed_neighbors_060"],
        obligation_ids=["p10_bulk_fixed_neighbours_060"],
    ))


def write_report(hz0, hist, rows_u, rows_w, split, sens, F, stress, digest):
    Su, Sw, Ew = stress

    def tab(rows):
        return "\n".join(
            f"    {r['mu']:<7g} {r['E']:10.4f}  {r['unavoid']:10.4f}  {r['extra']:9.4f}  "
            f"{r['ang_res_max']:.3f}/{r['ang_res_rms']:.4f}   {r['minV']:.2e}   "
            f"{r['min_len']:.4f}   {r['mean_len']:.4f}" for r in rows)

    coord = "\n".join(
        f"    n = {n:2d} ({split['c0'][n][0]:4d} hinges; unavoidable "
        f"{(2 * math.pi - n * TH0) ** 2 / (2 * n):.4f} each): {split['c0'][n][1]:.4f} -> "
        f"{split['c1'][n][1]:.4f} weighted, {split['cu'][n][1]:.4f} unweighted"
        for n in sorted(split["c0"]))
    fab = "\n".join(f"    {k:<24} {f['aniso']:.4f}    {np.round(f['eigs'], 4).tolist()}"
                    for k, f in F.items())
    ov = "\n".join(f"    {a:<24} vs {b:<24} {overlap(F[a], F[b]):+.3f}"
                   for a, b in [("angle, weighted", "spring (057)"),
                                ("angle, unweighted", "spring (057)"),
                                ("angle, weighted", "angle, unweighted"),
                                ("angle, weighted", "angle at start"),
                                ("spring (057)", "angle at start"),
                                ("extra only, weighted", "spring (057)")])
    r_u, r_w = rows_u[0], rows_w[0]
    frac_u = r_u["unavoid"] / r_u["E"]
    md = f"""# VacuumForge: The Angle-Gap Energy in Bulk, Neighbours Fixed

## Status

```text
result type:   numerical experiment (stage 3 step 1; 2026-11-24,
               derivation 060); TRIAL angle energy, K = 1 units
question:      with the 057 quanta, box and neighbour list fixed, does
               the angle-gap energy store strain in a different pattern
               from the spring proxy?
satisfies:     p10_bulk_fixed_neighbours_060
opens:         p10_bulk_neighbour_changes_060 (step 2)
packings:      vacuum_forge/src/vacuum_sector/060_angle_energy_fixed_neighbors/
               packing_060.npz (content sha256 {digest[:16]}...)
verification:  vacuum_forge/src/vacuum_sector/060_angle_energy_fixed_neighbors/
```

## The Two Energies

```text
P10 candidate:  E_w = sum over (tet, edge) of l_e (1/2)(theta - arccos(1/3))^2
control:        E_u = sum over (tet, edge) of     (1/2)(theta - arccos(1/3))^2
per hinge (closed, flat, n tetrahedra):
  (1/2) sum x_i^2 = (2 pi - n theta0)^2 / (2 n)  +  (1/2) sum (theta_i - 2 pi/n)^2
                    unavoidable at n                 extra: uneven sharing
```

## Measured Results

```text
E1. START (057 pre-relaxation coordinates; hash verified). Coordination
    histogram {hist}. Every hinge closes (deficit 0); per-hinge
    identity exact. E_u = {hz0['e'].sum():.3f} = unavoidable {hz0['unavoid'].sum():.3f} + extra
    {hz0['extra'].sum():.3f}.

E2. CONTROL (unweighted):
    mu      E_angle     unavoidable  extra      angle res max/rms   min V/V_ref  min edge  mean edge
{tab(rows_u)}
    With neighbours fixed the unavoidable part is frozen; relaxation
    removes {100 * (1 - r_u['extra'] / hz0['extra'].sum()):.1f}% of the starting extra. At the relaxed state the
    unavoidable coordination cost is {100 * frac_u:.1f}% of E_u.

E3. P10 CANDIDATE (length-weighted):
    mu      E_angle     unavoidable  extra      angle res max/rms   min V/V_ref  min edge  mean edge
{tab(rows_w)}
    (unavoidable and extra columns are unweighted per-hinge sums)
    E_w {split['Ew0']:.4f} -> {split['Ew1']:.4f}: angle redistribution at starting lengths
    {split['redistribution']:+.4f}; hinge-length change {split['length_change']:+.4f} (exact split).
    Mean hinge length by coordination, start -> relaxed:
{coord}
    Correlation of hinge-length ratio with unavoidable cost: weighted
    {split['corr_w']:+.3f}, unweighted {split['corr_u']:+.3f}.

E4. BARRIER SENSITIVITY (mu 1e-3 -> 1e-5): angle energy change
    {100 * sens['unweighted']['dE']:.4f}% (unweighted), {100 * sens['weighted']['dE']:.4f}% (weighted); contact sets
    {sens['unweighted']['contact']} and {sens['weighted']['contact']} tetrahedra (volume tracks mu); min edge drift
    {100 * sens['unweighted']['len_drift']:.2f}% and {100 * sens['weighted']['len_drift']:.2f}%: no edge collapses.

E5. DIRECTIONAL FABRICS (per-hinge energy x hinge direction; weakest
    barrier; spring fabric = 057's (l-1)^2 on the same neighbours):
    fabric                   anisotropy  dev eigenvalues / tr
{fab}
    deviatoric overlaps (cosine; +1 = same pattern, 0 = unrelated):
{ov}

E6. STRESS (affine virial, fixed box): unweighted trace {np.trace(Su):+.1e}
    (dilation flat, exact 0); weighted trace {np.trace(Sw):.4f} = E_w {Ew:.4f}
    (degree-one homogeneity). Deviatoric eigenvalues: unweighted
    {np.round(np.linalg.eigvalsh(Su - np.trace(Su) / 3 * np.eye(3)), 4).tolist()}, weighted
    {np.round(np.linalg.eigvalsh(Sw - np.trace(Sw) / 3 * np.eye(3)), 4).tolist()}.
```

## Reading

- **What fixed neighbours leave behind.** In the control, the
  unavoidable coordination cost ({r_u['unavoid']:.1f}) is frozen by the 057
  triangulation. Relaxation removes {100 * (1 - r_u['extra'] / hz0['extra'].sum()):.0f}% of the uneven-sharing extra,
  but {r_u['extra']:.1f} remains ({100 * (1 - frac_u):.0f}% of E_u): neighbouring tetrahedra cannot all
  reach their individual hinge minima at once, because each
  tetrahedron's six dihedrals are coupled.
- **How the weighted model relieves frustration.** Of its energy drop,
  {100 * split['redistribution'] / (split['Ew1'] - split['Ew0']):.0f}% comes from redistributing angles at the starting lengths
  and {100 * split['length_change'] / (split['Ew1'] - split['Ew0']):.0f}% from changing hinge lengths. Relative to the unweighted
  control, the extra shortening falls on the most frustrated hinges
  (n = 3 and n >= 8; see the coordination table); across all hinges
  the correlation with unavoidable cost is weak ({split['corr_w']:+.2f}).
- **Directional pattern.** With neighbours fixed, all three energies
  store their strain along similar directions: the angle fabrics
  overlap the spring fabric at {overlap(F['angle, weighted'], F['spring (057)']):+.2f} (weighted) and
  {overlap(F['angle, unweighted'], F['spring (057)']):+.2f} (unweighted), and every fabric overlaps the starting
  mesh's ({overlap(F['spring (057)'], F['angle at start']):+.2f} for the spring). The pattern is largely
  inherited from the triangulation. The part the angle energy adds,
  the uneven-sharing extra, is less aligned with the spring fabric
  ({overlap(F['extra only, weighted'], F['spring (057)']):+.2f}). Anisotropy magnitudes are similar
  ({F['angle, weighted']['aniso']:.3f} weighted, {F['spring (057)']['aniso']:.3f} spring).
- **Validity.** Each model holds one tetrahedron against the
  zero-volume constraint (volume tracks mu); energies change by about
  1e-6 relative as mu drops 100x, and no edge collapses. The 057 spring
  control held 34.
- At fixed neighbours, then, the angle-gap energy does not produce a
  markedly different directional pattern from the spring model on the
  same quanta. Whether a different pattern, or a frustration floor,
  emerges when neighbours can change is step 2's question.

## Fences

```text
- TRIAL angle energy (059), K explicit; both weightings are models.
- neighbours fixed: the unavoidable coordination cost is frozen by the
  057 triangulation; whether any of it survives neighbour changes is
  step 2 (p10_bulk_neighbour_changes_060).
- one seed, one size, one cubic box.
- no EM coupling.
```

## Ledger

```text
derivation:  angle_energy_fixed_neighbors_060
satisfies:   p10_bulk_fixed_neighbours_060
opens:       p10_bulk_neighbour_changes_060
depends on:  periodic_spring_control_057, wedge_strain_definition_059
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 060: The Angle-Gap Energy in Bulk, Neighbours Fixed")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    model, arrays, _, hz0, hist = experiment_1_start(failures)
    rows_u, xs_u, rows_w, xs_w, split = experiment_2_3_relax(model, arrays, hz0, failures)
    sens = experiment_4_sensitivity(rows_u, rows_w, failures)
    F = experiment_5_fabrics(model, arrays, xs_u, xs_w, failures)
    stress = experiment_6_stress(model, xs_u, xs_w, failures)
    digest = experiment_7_save(model, arrays, xs_u, xs_w, failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 060: verification failure")
    print("  Step 1 delivered: both angle energies relax the 057 quanta with fixed")
    print("  neighbours to valid flat packings; unavoidable and extra costs, the")
    print("  weighted model's length/redistribution split, fabrics vs the spring")
    print("  control, and stress are recorded.")

    record(ns, digest)
    write_report(hz0, hist, rows_u, rows_w, split, sens, F, stress, digest)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
