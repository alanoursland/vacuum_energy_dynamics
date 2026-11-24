"""Capacity probe: GPU memory and per-call cost vs N for the three heavy
kernels, on synthetic Poisson packings (periodic Delaunay, unit mean edge,
NO relaxation). Measures, does not solve: the numbers feed the N / ensemble
estimates in gpu_validation.md. Iteration counts to convergence are taken
from the N = 160 validation runs and are an assumption at larger N.
"""
from __future__ import annotations

import math
import sys

import numpy as np
import torch

import gpu_common as gc
from gpu_maxwell import BlochComplex, GradientProjector, lobpcg


def packing(N, seed=1):
    rng = np.random.default_rng(seed)
    L0 = N ** (1 / 3)
    x = rng.uniform(0, L0, (N, 3))
    with gc.Timer() as td:
        T, O = gc.periodic_delaunay(x, L0, margin=3.0)
    ident = gc.mesh_identities(x, L0, T, O)
    assert all(ident.values()), ident
    return x, L0, T, O, td.dt


def peak(fn, reps=3):
    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats()
    base = torch.cuda.memory_allocated()
    fn()
    with gc.Timer() as t:
        for _ in range(reps):
            fn()
    return t.dt / reps, (torch.cuda.max_memory_allocated() - base) / 2**20


def main(sizes=(1000, 4000, 16000), maxwell_sizes=(1000, 4000)):
    print("capacity probe:", gc.environment())
    out = []
    for N in sizes:
        x, L, T, O, tdel = packing(N)
        hid, nH = gc.hinge_index(T, O)
        I = np.array([0]); J = np.array([0]); OF = np.zeros((1, 3), int)
        # edge list for the spring term from the hinge map (first occurrence)
        first = np.full(nH, -1)
        h = hid.ravel()
        first[h[::-1]] = np.arange(h.size)[::-1]
        t_, k_ = np.divmod(first, 6)
        a_ = np.array([e[0] for e in gc.E6])[k_]; b_ = np.array([e[1] for e in gc.E6])[k_]
        I, J, OF = T[t_, a_], T[t_, b_], O[t_, b_] - O[t_, a_]
        m = np.linalg.norm(x[J] + L * OF - x[I], axis=1).mean()
        x, L = x / m, L / m
        row = {"N": N, "T": len(T), "E": nH, "delaunay_s": tdel}
        xt = torch.as_tensor(x, device=gc.DEV, dtype=gc.DT)
        for name, obj in (("spring+barrier", gc.spring_objective(L, T, O, I, J, OF, 1e-3)),
                          ("angle_weighted", gc.angle_objective(L, T, O, True, 1e-3))):
            t_fg, m_fg = peak(lambda: obj.fg(xt))
            t_h, m_h = peak(lambda: obj.hessian(xt), reps=2)
            H = obj.hessian(xt)
            v = torch.randn(3 * N, device=gc.DEV, dtype=gc.DT)
            t_mv, _ = peak(lambda: H @ v, reps=20)
            row[name] = {"fg_s": t_fg, "fg_MB": m_fg, "hess_s": t_h, "hess_MB": m_h, "spmv_s": t_mv,
                         "hess_nnz": int(H.values().numel())}
            print(f"  N = {N} (T = {len(T)}) {name}: grad {t_fg*1e3:.1f} ms / {m_fg:.0f} MB; sparse Hessian "
                  f"{t_h*1e3:.0f} ms / {m_h:.0f} MB (nnz {row[name]['hess_nnz']}); SpMV {t_mv*1e3:.2f} ms", flush=True)
            del H
        if N in maxwell_sizes:
            with gc.Timer() as tb:
                cx = BlochComplex(x, L, T, O)
            a = float(np.linalg.norm(cx.evec, axis=1).mean())
            kv = np.array([1.0, 1, 1]) / math.sqrt(3) * 0.1 / a

            def build():
                K, M1 = cx.operators(kv)
                return K, M1, GradientProjector(cx.d0(kv), M1, mode="cg", cg_tol=1e-12)

            torch.cuda.reset_peak_memory_stats(); base = torch.cuda.memory_allocated()
            with gc.Timer() as to:
                K, M1, proj = build()
            with gc.Timer() as tl:
                w, X, info = lobpcg(K, M1, proj, nwant=4, block=8, maxit=20, tol=0.0)
            mem = (torch.cuda.max_memory_allocated() - base) / 2**20
            row["maxwell"] = {"nE": cx.nE, "complex_build_s": tb.dt, "operators_s": to.dt,
                              "lobpcg_iter_s": tl.dt / info["iters"], "cg_iters_per_projection":
                              proj.cg_iters / max(1, 2 * info["iters"]), "peak_MB": mem}
            print(f"  N = {N} Maxwell: nE = {cx.nE}; complex build {tb.dt:.1f} s (CPU Python), operators "
                  f"{to.dt:.2f} s; LOBPCG {tl.dt / info['iters'] * 1e3:.0f} ms/iteration with CG projector "
                  f"(~{row['maxwell']['cg_iters_per_projection']:.0f} CG its per projection); peak {mem:.0f} MB", flush=True)
            del K, M1, proj, X
        out.append(row)
        torch.cuda.empty_cache()
    print("  wrote", gc.save_result("gpu_capacity", {"environment": gc.environment(), "rows": out}))


if __name__ == "__main__":
    main()
