"""Sparse Bloch-twisted Whitney Maxwell operators and a gradient-projected
complex LOBPCG eigensolver on the GPU (PyTorch). Independent of forge 058's
dense implementation: own simplex bookkeeping, own Whitney assembly (per
tetrahedron, stiffness built locally as C^T M2_t C), sparse CSR operators,
and an iterative eigensolver instead of dense null-space projection.

Bloch convention: a cochain on the image of a simplex translated by the
integer vector n carries the phase exp(i k . L n). Local values on a
tetrahedron are r * (global value) with r = orientation sign * phase.
"""
from __future__ import annotations

import itertools as it
import math

import numpy as np
import torch

from gpu_common import DEV, DT, canon_key

CT = torch.complex128
EL = list(it.combinations(range(4), 2))        # local edges (a < b)
FL = list(it.combinations(range(4), 3))        # local faces (a < b < c)


class BlochComplex:
    def __init__(self, x, L, T, O):
        self.x, self.L, self.T, self.O = np.asarray(x), float(L), np.asarray(T), np.asarray(O)
        nT = len(T)
        E, F = {}, {}
        self.e_id = np.zeros((nT, 6), np.int64); self.e_sg = np.zeros((nT, 6)); self.e_n0 = np.zeros((nT, 6, 3))
        self.f_id = np.zeros((nT, 4), np.int64); self.f_sg = np.zeros((nT, 4)); self.f_n0 = np.zeros((nT, 4, 3))
        for t in range(nT):
            for i, (a, b) in enumerate(EL):
                key, sv, so, n0, par = canon_key([T[t, a], T[t, b]], [O[t, a], O[t, b]])
                if key not in E:
                    E[key] = (len(E), sv, so)
                self.e_id[t, i], self.e_sg[t, i], self.e_n0[t, i] = E[key][0], par, n0
            for i, f in enumerate(FL):
                key, sv, so, n0, par = canon_key([T[t, j] for j in f], [O[t, j] for j in f])
                if key not in F:
                    F[key] = (len(F), sv, so)
                self.f_id[t, i], self.f_sg[t, i], self.f_n0[t, i] = F[key][0], par, n0
        self.nV, self.nE, self.nF, self.nT = len(x), len(E), len(F), nT
        self.edges = [None] * self.nE
        for _, (i, sv, so) in E.items():
            self.edges[i] = (sv, so)
        self.faces = [None] * self.nF
        for _, (i, sv, so) in F.items():
            self.faces[i] = (sv, so)
        self.Ekeys = E
        # uniform-field samples on edges: E . (edge vector)
        self.evec = np.array([self.x[v[1]] + self.L * np.array(o[1]) - self.x[v[0]] for v, o in self.edges])
        self._local()

    # ---- local Whitney matrices -------------------------------------------
    def _local(self):
        P = torch.as_tensor(self.x[self.T] + self.L * self.O, device=DEV, dtype=DT)
        Mx = torch.cat([P, torch.ones(self.nT, 4, 1, device=DEV, dtype=DT)], 2)
        G = torch.linalg.inv(Mx)[:, :3, :].transpose(1, 2)            # [t, a, 3] = grad lambda_a
        V = torch.linalg.det(P[:, 1:] - P[:, :1]) / 6
        self.tet_vol = V.cpu().numpy()
        Ill = lambda i, j: (1 + (i == j)) / 20
        dot = lambda u, w: (G[:, u] * G[:, w]).sum(-1)
        M1 = torch.zeros(self.nT, 6, 6, device=DEV, dtype=DT)
        for p, (a, b) in enumerate(EL):
            for q, (c, d) in enumerate(EL):
                M1[:, p, q] = V * (Ill(a, c) * dot(b, d) - Ill(a, d) * dot(b, c)
                                   - Ill(b, c) * dot(a, d) + Ill(b, d) * dot(a, c))
        cr = lambda u, w: torch.linalg.cross(G[:, u], G[:, w], dim=-1)

        def comps(f):
            a, b, c = f
            return [(a, cr(b, c)), (b, cr(c, a)), (c, cr(a, b))]

        M2 = torch.zeros(self.nT, 4, 4, device=DEV, dtype=DT)
        for p, f in enumerate(FL):
            for q, g in enumerate(FL):
                acc = 0
                for i, ci in comps(f):
                    for j, cj in comps(g):
                        acc = acc + Ill(i, j) * (ci * cj).sum(-1)
                M2[:, p, q] = 4 * V * acc
        C = torch.zeros(4, 6, device=DEV, dtype=DT)                    # local d1: face <- edges
        for p, (a, b, c) in enumerate(FL):
            C[p, EL.index((b, c))] += 1
            C[p, EL.index((a, c))] -= 1
            C[p, EL.index((a, b))] += 1
        self.Cloc, self.G = C, G
        self.M1loc, self.M2loc = M1, M2
        self.Kloc = C.T @ M2 @ C

    def whitney_commutes(self, nsamp=5, seed=0):
        """Max error of curl(W1 u) = W2(d1 u) at random points of every tet."""
        rng = np.random.default_rng(seed)
        G = self.G
        u = torch.as_tensor(rng.standard_normal((self.nT, 6)), device=DEV, dtype=DT)
        curl = sum(u[:, p, None] * 2 * torch.linalg.cross(G[:, a], G[:, b], dim=-1) for p, (a, b) in enumerate(EL))
        c = u @ self.Cloc.T
        err = 0.0
        for _ in range(nsamp):
            lam = torch.as_tensor(rng.dirichlet(np.ones(4), self.nT), device=DEV, dtype=DT)
            w2 = 0
            for p, (a, b, cc) in enumerate(FL):
                W = 2 * (lam[:, a, None] * torch.linalg.cross(G[:, b], G[:, cc], dim=-1)
                         + lam[:, b, None] * torch.linalg.cross(G[:, cc], G[:, a], dim=-1)
                         + lam[:, cc, None] * torch.linalg.cross(G[:, a], G[:, b], dim=-1))
                w2 = w2 + c[:, p, None] * W
            err = max(err, float((w2 - curl).abs().max() / curl.abs().max()))
        return err

    # ---- Bloch-twisted global operators -------------------------------------
    def _phase(self, kv, n0):
        return torch.exp(1j * self.L * torch.as_tensor(n0 @ np.asarray(kv, float), device=DEV, dtype=DT))

    def _assemble(self, loc, ids, sg, n0, kv, n):
        r = torch.as_tensor(sg, device=DEV, dtype=DT) * self._phase(kv, n0)   # [t, m]
        vals = r.conj()[:, :, None] * loc.to(CT) * r[:, None, :]
        I = torch.as_tensor(ids, device=DEV)
        rows = I[:, :, None].expand_as(vals).reshape(-1)
        cols = I[:, None, :].expand_as(vals).reshape(-1)
        return torch.sparse_coo_tensor(torch.stack([rows, cols]), vals.reshape(-1), (n, n)).coalesce().to_sparse_csr()

    def operators(self, kv):
        """(K, M1) sparse CSR on the edges, K = d1^H M2 d1 assembled locally."""
        K = self._assemble(self.Kloc, self.e_id, self.e_sg, self.e_n0, kv, self.nE)
        M1 = self._assemble(self.M1loc, self.e_id, self.e_sg, self.e_n0, kv, self.nE)
        return K, M1

    def M2(self, kv):
        return self._assemble(self.M2loc, self.f_id, self.f_sg, self.f_n0, kv, self.nF)

    def d0(self, kv):
        rows, cols, vals = [], [], []
        for e, (v, o) in enumerate(self.edges):
            rows += [e, e]; cols += [v[0], v[1]]
            vals += [-1.0, complex(np.exp(1j * self.L * (np.array(o[1]) @ np.asarray(kv, float))))]
        return torch.sparse_coo_tensor(torch.tensor([rows, cols], device=DEV),
                                       torch.tensor(vals, device=DEV, dtype=CT), (self.nE, self.nV)).coalesce().to_sparse_csr()

    def d1(self, kv):
        rows, cols, vals = [], [], []
        for f, (v, o) in enumerate(self.faces):
            for (a, b), s in (((1, 2), 1), ((0, 2), -1), ((0, 1), 1)):
                key, _, _, n0, par = canon_key([v[a], v[b]], [o[a], o[b]])
                rows.append(f); cols.append(self.Ekeys[key][0])
                vals.append(s * par * complex(np.exp(1j * self.L * (n0 @ np.asarray(kv, float)))))
        return torch.sparse_coo_tensor(torch.tensor([rows, cols], device=DEV),
                                       torch.tensor(vals, device=DEV, dtype=CT), (self.nF, self.nE)).coalesce().to_sparse_csr()


# =============================================================================
# Gradient projector and LOBPCG
# =============================================================================


class GradientProjector:
    """P v = v - G A0^{-1} G^H M1 v,  A0 = G^H M1 G: the M1-orthogonal
    projector onto the discrete divergence-free edge cochains. A0 is solved
    densely (Cholesky) or by Jacobi-preconditioned block CG."""

    def __init__(self, G, M1, mode="dense", cg_tol=1e-13, cg_maxit=5000):
        self.G, self.M1, self.mode = G, M1, mode
        self.GH = G.to_sparse_coo().transpose(0, 1).conj().coalesce().to_sparse_csr()
        self.cg_tol, self.cg_maxit, self.cg_iters = cg_tol, cg_maxit, 0
        if mode == "dense":
            A0 = (self.GH @ (M1 @ G.to_dense()))
            A0 = 0.5 * (A0 + A0.conj().T)
            self.Lc = torch.linalg.cholesky(A0)
        else:
            nV = G.shape[1]
            diag = torch.zeros(nV, device=DEV, dtype=CT)
            Gd = G.to_sparse_coo().coalesce()
            # diag(A0) = sum_e |G_ev|^2 (M1)_ee
            M1d = torch.zeros(M1.shape[0], device=DEV, dtype=CT)
            Mc = M1.to_sparse_coo().coalesce()
            r_, c_ = Mc.indices()
            m = r_ == c_
            M1d[r_[m]] = Mc.values()[m]
            r, c = Gd.indices()
            diag.index_add_(0, c, (Gd.values().abs() ** 2) * M1d[r])
            self.dinv = (1 / diag.real).to(CT)[:, None]

    def _solve(self, B):
        if self.mode == "dense":
            return torch.cholesky_solve(B, self.Lc)
        A = lambda Y: self.GH @ (self.M1 @ (self.G @ Y))
        X = torch.zeros_like(B)
        R = B.clone()
        Z = self.dinv * R
        Pd = Z.clone()
        rz = (R.conj() * Z).sum(0).real
        bn = torch.linalg.norm(B, dim=0)
        for j in range(self.cg_maxit):
            AP = A(Pd)
            alpha = rz / (Pd.conj() * AP).sum(0).real
            X = X + alpha * Pd
            R = R - alpha * AP
            if float((torch.linalg.norm(R, dim=0) / bn).max()) < self.cg_tol:
                break
            Z = self.dinv * R
            rzn = (R.conj() * Z).sum(0).real
            Pd = Z + (rzn / rz) * Pd
            rz = rzn
        self.cg_iters += j + 1
        return X

    def __call__(self, Vb):
        return Vb - self.G @ self._solve(self.GH @ (self.M1 @ Vb))

    def shift_term(self, Vb):
        """M1 G A0^{-1} G^H M1 v: adding s times this to K moves every gradient
        mode G phi to omega^2 = s exactly and leaves divergence-free modes
        (G^H M1 e = 0) unchanged."""
        return self.M1 @ (self.G @ self._solve(self.GH @ (self.M1 @ Vb)))

    def divergence(self, Vb):
        """Relative size of G^H M1 v (zero for an exact transverse mode)."""
        return torch.linalg.norm(self.GH @ (self.M1 @ Vb), dim=0) / torch.linalg.norm(self.M1 @ Vb, dim=0)


def _morth(S, Mmv, drop=1e-12):
    """M-orthonormalize the columns of S (SVQB, twice); drops dependent directions."""
    for _ in range(2):
        BS = Mmv(S)
        Gm = S.conj().T @ BS
        Gm = 0.5 * (Gm + Gm.conj().T)
        d = 1 / torch.sqrt(torch.clamp(torch.diagonal(Gm).real, min=1e-300))
        th, Vv = torch.linalg.eigh(d[:, None] * Gm * d[None, :])
        keep = th > drop * th.max()
        S = S @ (d[:, None] * Vv[:, keep] / torch.sqrt(th[keep])[None, :])
    return S


def lobpcg(K, M1, proj, nwant=4, block=8, X0=None, tol=1e-9, maxit=3000, sigma=1.0, seed=0, shift=10.0):
    """Lowest eigenpairs of the gradient-removed problem K x = w M1 x,
    G^H M1 x = 0. Solved as (K + shift * M1 G A0^{-1} G^H M1) x = w M1 x:
    gradients sit at w = shift exactly, so eigenvalues below `shift` are those
    of the projected problem. Search directions are also projected.
    Returns (w, X, info)."""
    n = K.shape[0]
    Mmv = lambda V: M1 @ V
    Kmv = lambda V: K @ V + shift * proj.shift_term(V)
    dK = torch.zeros(n, device=DEV, dtype=CT)     # Jacobi preconditioner: diag(K + sigma M1)
    for A_, s in ((K, 1.0), (M1, sigma)):
        Ac = A_.to_sparse_coo().coalesce()
        r, c = Ac.indices()
        m = r == c
        dK.index_add_(0, r[m], s * Ac.values()[m])
    prec = lambda R: R / dK.real[:, None]
    g = torch.Generator(device="cpu").manual_seed(seed)
    if X0 is None or X0.shape[1] < block:
        Xr = torch.randn(n, block, generator=g, dtype=DT) + 1j * torch.randn(n, block, generator=g, dtype=DT)
        Xr = Xr.to(DEV)
        if X0 is not None:
            Xr[:, :X0.shape[1]] = X0
        X0 = Xr
    X = _morth(proj(X0), Mmv)
    AX = Kmv(X)
    w, C = torch.linalg.eigh(0.5 * ((X.conj().T @ AX) + (X.conj().T @ AX).conj().T))
    X, AX = X @ C, AX @ C
    BX = Mmv(X)
    Pd = None
    for itn in range(1, maxit + 1):
        R = AX - BX * w[None, :]
        res = torch.linalg.norm(R, dim=0) / (torch.linalg.norm(AX, dim=0) + w.abs() * torch.linalg.norm(BX, dim=0))
        if float(res[:nwant].max()) < tol:
            break
        Wd = proj(prec(R))
        S = torch.cat([X, Wd] + ([Pd] if Pd is not None else []), 1)
        S = _morth(S, Mmv)
        AS = Kmv(S)
        A = S.conj().T @ AS
        wa, Ca = torch.linalg.eigh(0.5 * (A + A.conj().T))
        m = X.shape[1]
        Cx = Ca[:, :m]
        Xn = S @ Cx
        # implicit conjugate direction: the part of the new X outside the old X
        Pd = Xn - X @ (X.conj().T @ Mmv(Xn))
        X, AX, w = Xn, AS @ Cx, wa[:m]
        BX = Mmv(X)
    info = {"iters": itn, "res": res[:nwant].cpu().numpy(),
            "div": proj.divergence(X[:, :nwant]).cpu().numpy()}
    assert float(w[nwant - 1].real) < shift, "wanted eigenvalues reach the gradient shift; raise it"
    return w[:nwant].real.cpu().numpy(), X, info
