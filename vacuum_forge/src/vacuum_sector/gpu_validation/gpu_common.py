"""Shared GPU (PyTorch, float64) machinery for the Maxwell-probe validation.

These scripts are an INDEPENDENT check of forges 057, 058, 060 and 061. They
read the forges' saved, hash-verified packings, but do not import the
forges' energy, gradient, Hessian, optimizer or eigensolver code. Everything
numerical here is written from the formulas stated in the forge reports:

  spring proxy (057)   E = sum_e (l_e - 1)^2
  barrier              -mu sum_t log(V_t / V_ref),  V_ref = 1 / (6 sqrt 2)
  angle energy (060)   E = sum_(tet, edge) w (1/2)(theta - arccos(1/3))^2,
                       w = l_e (weighted, P10 candidate) or 1 (control)

Gradients come from autograd. Hessians are assembled SPARSE on the GPU from
per-term local Hessians (torch.func.vmap of torch.func.hessian), and the
optimizer is a trust-region Newton-CG (Steihaug-Toint) with a 3x3
block-Jacobi preconditioner. The forges use dense Cholesky / eigenvalue-
modified Newton with line search; the two methods share no code and differ
in globalization.

Roundoff: near convergence the predicted decrease of a step falls below the
energy's floating-point resolution, so the trust-region ratio is noise. In
that regime a step is accepted if it is feasible and reduces max|g| (the
same idea as 060's roundoff rule, implemented independently). This is
reported in each script's output.
"""
from __future__ import annotations

import hashlib
import itertools as it
import json
import math
import time
from pathlib import Path

import numpy as np
import torch
from scipy.spatial import Delaunay

SECTOR = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
RESULTS = Path(__file__).resolve().parent / "results"
DEV = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DT = torch.float64
TH0 = math.acos(1 / 3)
VREF = 1 / (6 * math.sqrt(2))
E6 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
OPP6 = [tuple(m for m in range(4) if m not in e) for e in E6]


# =============================================================================
# Environment, I/O
# =============================================================================


def environment() -> dict:
    env = {"torch": torch.__version__, "torch_cuda": torch.version.cuda,
           "numpy": np.__version__, "device": str(DEV)}
    if DEV.type == "cuda":
        p = torch.cuda.get_device_properties(0)
        env.update(gpu=p.name, gpu_mem_GB=round(p.total_memory / 2**30, 2))
    return env


def sync():
    if DEV.type == "cuda":
        torch.cuda.synchronize()


class Timer:
    def __enter__(self):
        sync()
        self.t0 = time.perf_counter()
        return self

    def __exit__(self, *a):
        sync()
        self.dt = time.perf_counter() - self.t0


def content_hash(arrays: dict) -> str:
    """The forges' hash rule: sha256 over sorted names: name, dtype, shape, bytes."""
    h = hashlib.sha256()
    for name in sorted(arrays):
        a = np.ascontiguousarray(arrays[name])
        h.update(name.encode())
        h.update(str(a.dtype).encode())
        h.update(str(a.shape).encode())
        h.update(a.tobytes())
    return h.hexdigest()


def load_packing(folder: str, stem: str) -> tuple[dict, str, bool]:
    d = SECTOR / folder
    arrays = dict(np.load(d / f"{stem}.npz"))
    meta = json.loads((d / f"{stem}.json").read_text())
    digest = content_hash(arrays)
    return arrays, digest, digest == meta["content_sha256"]


def save_result(name: str, payload: dict) -> Path:
    RESULTS.mkdir(exist_ok=True)
    p = RESULTS / f"{name}.json"

    def conv(o):
        if isinstance(o, (np.floating, np.integer, np.bool_)):
            return o.item()
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, torch.Tensor):
            return o.detach().cpu().tolist()
        raise TypeError(type(o))

    p.write_text(json.dumps(payload, indent=2, default=conv) + "\n")
    return p


class Checks:
    def __init__(self):
        self.rows = []

    def __call__(self, label, ok, detail=""):
        ok = bool(ok)
        self.rows.append({"check": label, "pass": ok, "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  ({detail})" if detail else ""))
        return ok

    @property
    def failures(self):
        return [r for r in self.rows if not r["pass"]]


# =============================================================================
# Periodic meshes (own implementation: canonical keys, hinges, Delaunay)
# =============================================================================


def canon_key(verts, offs):
    """Canonical key of a periodic simplex given its vertices and integer image
    offsets: sort by (vertex, offset), translate so the first sits at offset 0.
    Returns (key, sorted vertices, translated offsets, translation, parity)."""
    items = sorted(range(len(verts)), key=lambda i: (int(verts[i]),) + tuple(int(c) for c in offs[i]))
    n0 = np.asarray(offs[items[0]], dtype=np.int64)
    sv = [int(verts[i]) for i in items]
    so = [tuple(int(c) for c in (np.asarray(offs[i]) - n0)) for i in items]
    inv = sum(1 for a in range(len(items)) for b in range(a + 1, len(items)) if items[a] > items[b])
    return tuple(sv) + tuple(c for o in so for c in o), sv, so, n0, (-1) ** inv


def hinge_index(T, O):
    """(tet, local edge) -> global hinge id, plus coordination numbers."""
    keys, hid = {}, np.zeros((len(T), 6), np.int64)
    for t in range(len(T)):
        for k, (a, b) in enumerate(E6):
            key = canon_key([T[t, a], T[t, b]], [O[t, a], O[t, b]])[0]
            hid[t, k] = keys.setdefault(key, len(keys))
    return hid, len(keys)


def periodic_delaunay(x, L, margin=None):
    """Periodic Delaunay triangulation of points x in a cubic box of side L,
    with tetrahedra as (vertices, integer offsets), positively oriented.
    margin=None uses all 26 neighbouring images; otherwise only image points
    within `margin` of the box (fast for large N). x may be unwrapped; the
    returned offsets are in the frame of x."""
    x = np.asarray(x, float)
    n = len(x)
    w = np.floor(x / L).astype(np.int64)
    xw = x - L * w
    shifts = np.array(list(it.product((-1, 0, 1), repeat=3)), np.int64)
    pts, sid, vid = [], [], []
    for s_i, s in enumerate(shifts):
        p = xw + L * s
        if margin is not None and s.any():
            keep = np.all((p > -margin) & (p < L + margin), axis=1)
        else:
            keep = np.ones(n, bool)
        pts.append(p[keep])
        sid.append(np.full(keep.sum(), s_i))
        vid.append(np.nonzero(keep)[0])
    pts, sid, vid = np.concatenate(pts), np.concatenate(sid), np.concatenate(vid)
    centre = int(np.nonzero((shifts == 0).all(1))[0][0])
    simp = Delaunay(pts).simplices
    simp = simp[(sid[simp] == centre).any(1)]
    V_ = vid[simp]
    Off = shifts[sid[simp]] - w[V_]                     # offsets in x's frame
    P = x[V_] + L * Off
    vol = np.linalg.det(P[:, 1:] - P[:, :1]) / 6
    neg = vol < 0
    V_[neg, 0], V_[neg, 1] = V_[neg, 1].copy(), V_[neg, 0].copy()
    Off[neg, 0], Off[neg, 1] = Off[neg, 1].copy(), Off[neg, 0].copy()
    tets = {}
    for v, o in zip(V_, Off):
        key = canon_key(v, o)[0]
        if key not in tets:
            # translate so the canonical-first vertex has offset (its x-frame) 0 shift
            first = min(range(4), key=lambda i: (int(v[i]),) + tuple(int(c) for c in o[i]))
            tets[key] = (v.copy(), o - o[first])
    T = np.array([a for a, _ in tets.values()], np.int64)
    O = np.array([b for _, b in tets.values()], np.int64)
    return T, O


def tet_keyset(T, O):
    return frozenset(canon_key(v, o)[0] for v, o in zip(T, O))


def mesh_identities(x, L, T, O):
    """Exact checks used by 061: E = V + T, sum n = 6T, sum(6 - n) = 6V,
    all volumes positive and summing to L^3."""
    hid, nH = hinge_index(T, O)
    n = np.bincount(hid.ravel(), minlength=nH)
    nV, nT = len(x), len(T)
    P = x[T] + L * O
    vol = np.linalg.det(P[:, 1:] - P[:, :1]) / 6
    return {"EVT": nH == nV + nT, "sum_n": int(n.sum()) == 6 * nT,
            "6V": int((6 - n).sum()) == 6 * nV, "all_pos": bool((vol > 0).all()),
            "vol_sum": abs(vol.sum() - L**3) < 1e-8 * L**3}


# =============================================================================
# Local energy terms (batched over [..., k, 3])
# =============================================================================


def tet_volume(P):
    a, b, c = P[..., 1, :] - P[..., 0, :], P[..., 2, :] - P[..., 0, :], P[..., 3, :] - P[..., 0, :]
    return (a * torch.linalg.cross(b, c, dim=-1)).sum(-1) / 6


def dihedrals(P):
    """Interior dihedral angles of a tetrahedron at its six edges, from the
    angle between the two face normals e x (c - a) and e x (d - a)."""
    ia = [e[0] for e in E6]; ib = [e[1] for e in E6]
    ic = [o[0] for o in OPP6]; id_ = [o[1] for o in OPP6]
    A, B, C, D = P[..., ia, :], P[..., ib, :], P[..., ic, :], P[..., id_, :]
    e = B - A
    n1 = torch.linalg.cross(e, C - A, dim=-1)
    n2 = torch.linalg.cross(e, D - A, dim=-1)
    th = torch.atan2(torch.linalg.norm(torch.linalg.cross(n1, n2, dim=-1), dim=-1), (n1 * n2).sum(-1))
    return th, torch.linalg.norm(e, dim=-1)


def spring_term(P):          # P [..., 2, 3]
    l = torch.linalg.norm(P[..., 1, :] - P[..., 0, :], dim=-1)
    return (l - 1) ** 2


def make_barrier_term(mu):
    def f(P):
        V = tet_volume(P)
        return -mu * torch.log(V / VREF)
    return f


def make_angle_term(weighted, mu):
    def f(P):
        th, le = dihedrals(P)
        w = le if weighted else torch.ones_like(le)
        e = 0.5 * (w * (th - TH0) ** 2).sum(-1)
        if mu > 0:
            e = e - mu * torch.log(tet_volume(P) / VREF)
        return e
    return f


class TermSet:
    """sum over a batch of local terms phi(x[idx] + L * off)."""

    def __init__(self, idx, off, L, fn, n):
        self.idx = torch.as_tensor(np.asarray(idx), device=DEV, dtype=torch.long)
        self.off = torch.as_tensor(np.asarray(off), device=DEV, dtype=DT)
        self.L, self.fn, self.n = float(L), fn, n
        k = self.idx.shape[1]
        self.k = k
        self.dof = (3 * self.idx[:, :, None] + torch.arange(3, device=DEV)).reshape(-1, 3 * k)
        self._h = torch.func.vmap(torch.func.hessian(lambda p: fn(p.reshape(k, 3)).sum()))

    def P(self, x):
        return x[self.idx] + self.L * self.off

    def energy(self, x):
        return self.fn(self.P(x)).sum()

    def local_hessians(self, x):
        return self._h(self.P(x).reshape(-1, 3 * self.k))      # [m, 3k, 3k]


class Objective:
    def __init__(self, terms, n):
        self.terms, self.n = terms, n

    def energy(self, x):
        return sum(t.energy(x) for t in self.terms)

    def fg(self, x):
        """Energy and gradient; (inf, None) if infeasible or non-finite."""
        xx = x.detach().requires_grad_(True)
        f = self.energy(xx)
        if not torch.isfinite(f):
            return math.inf, None
        (g,) = torch.autograd.grad(f, xx)
        return float(f), g.detach()

    def hessian(self, x):
        """Sparse CSR Hessian assembled from per-term local Hessians."""
        rows, cols, vals = [], [], []
        for t in self.terms:
            Hl = t.local_hessians(x.detach())
            d = t.dof
            rows.append(d[:, :, None].expand_as(Hl).reshape(-1))
            cols.append(d[:, None, :].expand_as(Hl).reshape(-1))
            vals.append(Hl.reshape(-1))
        N3 = 3 * self.n
        H = torch.sparse_coo_tensor(torch.stack([torch.cat(rows), torch.cat(cols)]),
                                    torch.cat(vals), (N3, N3)).coalesce()
        return H.to_sparse_csr()


def block_jacobi(H, n):
    """3x3 vertex blocks of H, made SPD by |eigenvalue| with a floor; returns
    (apply M^{-1}, apply M)."""
    Hc = H.to_sparse_coo().coalesce()
    r, c = Hc.indices()
    v = Hc.values()
    m = (r // 3) == (c // 3)
    B = torch.zeros(n, 3, 3, dtype=DT, device=DEV)
    B[r[m] // 3, r[m] % 3, c[m] % 3] = v[m]
    w, Q = torch.linalg.eigh(0.5 * (B + B.transpose(1, 2)))
    wa = w.abs()
    wa = torch.clamp(wa, min=1e-10 * float(wa.max()))
    Minv = Q @ torch.diag_embed(1 / wa) @ Q.transpose(1, 2)
    Mb = Q @ torch.diag_embed(wa) @ Q.transpose(1, 2)
    return (lambda z: torch.einsum("nij,nj->ni", Minv, z.reshape(n, 3)).reshape(-1),
            lambda z: torch.einsum("nij,nj->ni", Mb, z.reshape(n, 3)).reshape(-1))


def remove_translation(v, n):
    v = v.reshape(n, 3)
    return (v - v.mean(0, keepdim=True)).reshape(-1)


def steihaug(H, g, Minv, Mmv, delta, tol, maxit, n):
    """Preconditioned Steihaug-Toint CG for min g.s + s.Hs/2, ||s||_M <= delta.
    Vectors are kept orthogonal to rigid translations (exact zero modes)."""
    z = torch.zeros_like(g)
    r = g.clone()
    y = remove_translation(Minv(r), n)
    d = -y
    ry = float(r @ y)
    gn0 = float(torch.linalg.norm(r))
    if gn0 < tol:
        return z, 0, "tol"

    def to_boundary(z, d):
        Mz, Md = Mmv(z), Mmv(d)
        a, b, c = float(d @ Md), 2 * float(z @ Md), float(z @ Mz) - delta**2
        tau = (-b + math.sqrt(max(b * b - 4 * a * c, 0.0))) / (2 * a)
        return z + tau * d

    for j in range(maxit):
        Hd = H @ d
        dHd = float(d @ Hd)
        if dHd <= 0:
            return to_boundary(z, d), j + 1, "negative curvature"
        alpha = ry / dHd
        zn = z + alpha * d
        if math.sqrt(max(float(zn @ Mmv(zn)), 0.0)) >= delta:
            return to_boundary(z, d), j + 1, "boundary"
        r = r + alpha * Hd
        if float(torch.linalg.norm(r)) < tol:
            return zn, j + 1, "tol"
        y = remove_translation(Minv(r), n)
        ryn = float(r @ y)
        d = -y + (ryn / ry) * d
        ry, z = ryn, zn
    return z, maxit, "maxit"


def tr_newton(obj, x0, gtol, maxit=500, delta0=0.5, verbose=False):
    """Trust-region Newton-CG. Returns x, info dict."""
    n = obj.n
    x = torch.as_tensor(np.asarray(x0), device=DEV, dtype=DT).clone()
    f, g = obj.fg(x)
    assert g is not None, "infeasible start"
    g = remove_translation(g.reshape(-1), n).reshape(n, 3)
    delta = delta0
    info = {"iters": 0, "cg": 0, "roundoff_accepts": 0, "rejects": 0, "status": "max iterations"}
    for k in range(maxit):
        gmax = float(g.abs().max())
        if gmax < gtol:
            info.update(status="converged", iters=k)
            break
        H = obj.hessian(x)
        Minv, Mmv = block_jacobi(H, n)
        gv = g.reshape(-1)
        gnorm = float(torch.linalg.norm(gv))
        tol = min(0.1, math.sqrt(gnorm)) * gnorm
        s, ncg, why = steihaug(H, gv, Minv, Mmv, delta, tol, 4 * 3 * n, n)
        info["cg"] += ncg
        pred = -(float(gv @ s) + 0.5 * float(s @ (H @ s)))
        xn = x + s.reshape(n, 3)
        fn, gn = obj.fg(xn)
        snorm = math.sqrt(max(float(s @ Mmv(s)), 0.0))
        if gn is None:
            delta = 0.25 * snorm
            info["rejects"] += 1
            continue
        gn = remove_translation(gn.reshape(-1), n).reshape(n, 3)
        roundoff = pred < 1e-13 * max(1.0, abs(f))
        if roundoff:
            accept = float(gn.abs().max()) < gmax
            if accept:
                info["roundoff_accepts"] += 1
            else:
                delta = 0.5 * snorm
        else:
            rho = (f - fn) / pred
            accept = rho > 1e-4
            if rho < 0.25:
                delta = 0.25 * snorm
            elif rho > 0.75 and why in ("boundary", "negative curvature"):
                delta = 2 * delta
        if accept:
            x, f, g = xn, fn, gn
        else:
            info["rejects"] += 1
        if verbose:
            print(f"      it {k:3d} f {f:.12f} |g| {gmax:.2e} cg {ncg:4d} ({why}) "
                  f"delta {delta:.2e} {'acc' if accept else 'rej'}{' roundoff' if roundoff else ''}")
        if delta < 1e-30:
            info.update(status="trust region collapsed", iters=k)
            break
    else:
        info["iters"] = maxit
    info["gmax"] = float(g.abs().max())
    info["E"] = f
    return x.detach().cpu().numpy(), info


def fire(obj, x0, ftol, max_steps=400000, dt0=1e-3, dtmax=2e-2):
    """FIRE (Bitzek et al. 2006): damped molecular-dynamics descent, close to
    the gradient-flow path. Unit masses; a step that inverts a tetrahedron is
    undone with dt halved and the velocity zeroed. Stops at max|g| < ftol."""
    n = obj.n
    x = torch.as_tensor(np.asarray(x0), device=DEV, dtype=DT).clone()
    v = torch.zeros_like(x)
    f, g = obj.fg(x)
    dt, alpha, npos = dt0, 0.1, 0
    for step in range(max_steps):
        F = -remove_translation(g.reshape(-1), n).reshape(n, 3)
        if float(F.abs().max()) < ftol:
            return x.cpu().numpy(), {"status": "converged", "steps": step, "gmax": float(F.abs().max()), "E": f}
        P = float((F * v).sum())
        if P > 0:
            vn, Fn = torch.linalg.norm(v), torch.linalg.norm(F)
            v = (1 - alpha) * v + alpha * F * (vn / Fn)
            npos += 1
            if npos > 5:
                dt, alpha = min(dt * 1.1, dtmax), alpha * 0.99
        else:
            v.zero_()
            dt, alpha, npos = dt * 0.5, 0.1, 0
        v = v + dt * F
        xn = x + dt * v
        fn, gn = obj.fg(xn)
        if gn is None:
            v.zero_()
            dt *= 0.5
            continue
        x, f, g = xn, fn, gn
    return x.cpu().numpy(), {"status": "max steps", "steps": max_steps,
                             "gmax": float(g.abs().max()), "E": f}


# =============================================================================
# Objectives for the three forge energies
# =============================================================================


def spring_objective(L, T, O, I, J, OF, mu):
    n = int(max(T.max(), I.max(), J.max())) + 1
    eidx = np.stack([I, J], 1)
    eoff = np.stack([np.zeros_like(OF), OF], 1)
    terms = [TermSet(eidx, eoff, L, spring_term, n)]
    if mu > 0:
        terms.append(TermSet(T, O, L, make_barrier_term(mu), n))
    return Objective(terms, n)


def angle_objective(L, T, O, weighted, mu):
    n = int(T.max()) + 1
    return Objective([TermSet(T, O, L, make_angle_term(weighted, mu), n)], n)


# =============================================================================
# Measurements (numpy, own code)
# =============================================================================


def np_dihedrals(P):
    with torch.no_grad():
        th, le = dihedrals(torch.as_tensor(P, dtype=DT))
    return th.numpy(), le.numpy()


def fabric(values, dirs):
    F = (dirs.T * values) @ dirs
    dev = F - np.trace(F) / 3 * np.eye(3)
    w, axes = np.linalg.eigh(dev)
    return {"F": F, "dev": dev, "aniso": float(np.linalg.norm(dev) / np.trace(F)),
            "eigs": w / np.trace(F), "axes": axes}


def overlap(A, B):
    return float(np.sum(A["dev"] * B["dev"]) / (np.linalg.norm(A["dev"]) * np.linalg.norm(B["dev"])))


def axis_angles(A, B):
    return [math.degrees(math.acos(min(1.0, abs(float(A[:, i] @ B[:, i]))))) for i in range(3)]


def spring_measure(x, L, T, O, I, J, OF):
    b = x[J] + L * OF - x[I]
    l = np.linalg.norm(b, axis=1)
    P = x[T] + L * O
    vol = np.linalg.det(P[:, 1:] - P[:, :1]) / 6
    fab = fabric((l - 1) ** 2, b / l[:, None])
    return {"E_per_N": float(((l - 1) ** 2).sum() / len(x)), "minV": float(vol.min() / VREF),
            "aniso": fab["aniso"], "axes": fab["axes"], "fab": fab, "dev_eigs": fab["eigs"]}


def angle_measure(x, L, T, O, hid=None, nH=None):
    """E_w, E_u, unavoidable and extra (unweighted per-hinge sums), fabrics."""
    if hid is None:
        hid, nH = hinge_index(T, O)
    P = x[T] + L * O
    th, le = np_dihedrals(P)
    n = np.bincount(hid.ravel(), minlength=nH)
    h = hid.ravel()
    e_u = np.bincount(h, weights=(0.5 * (th - TH0) ** 2).ravel(), minlength=nH)
    e_w = np.bincount(h, weights=(0.5 * le * (th - TH0) ** 2).ravel(), minlength=nH)
    share = (2 * math.pi / n)[h]
    extra = np.bincount(h, weights=0.5 * (th.ravel() - share) ** 2, minlength=nH)
    unavoid = (2 * math.pi - n * TH0) ** 2 / (2 * n)
    sum_th = np.bincount(h, weights=th.ravel(), minlength=nH)
    first = np.full(nH, -1)
    first[h[::-1]] = np.arange(h.size)[::-1]
    t_, k_ = np.divmod(first, 6)
    a_ = np.array([e[0] for e in E6])[k_]
    b_ = np.array([e[1] for e in E6])[k_]
    ev = P[t_, b_] - P[t_, a_]
    ln = np.linalg.norm(ev, axis=1)
    dirs = ev / ln[:, None]
    vol = np.linalg.det(P[:, 1:] - P[:, :1]) / 6
    hist = dict(zip(*[a.tolist() for a in np.unique(n, return_counts=True)]))
    return {"E_w": float(e_w.sum()), "E_u": float(e_u.sum()), "unavoid": float(unavoid.sum()),
            "extra": float(extra.sum()), "closure": float(np.abs(sum_th - 2 * math.pi).max()),
            "minV": float(vol.min() / VREF), "hist": hist, "hinge_len": float(ln.sum()),
            "fab_u": fabric(e_u, dirs), "fab_w": fabric(e_w, dirs),
            "fab_extra_u": fabric(extra, dirs), "fab_extra_w": fabric(extra * ln, dirs),
            "nT": len(T), "min_len": float(ln.min()), "mean_len": float(ln.mean())}


def nonrigid_diff(a, b):
    d = np.asarray(a) - np.asarray(b)
    return float(np.abs(d - d.mean(0)).max())
