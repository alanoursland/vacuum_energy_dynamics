"""GPU validation of forge 058 (ordinary Maxwell, fork (a), on the 057 packing).

Sparse Bloch-twisted Whitney operators (gpu_maxwell.BlochComplex) on the
hash-verified 057 geometry; torus gates G3a-G3c with dense GPU linear
algebra (exact ranks, small at this size); the dispersion scan with a
gradient-projected complex LOBPCG (gpu_maxwell.lobpcg). Phase speeds are
compared with the committed 058_periodic_maxwell_calibration/dispersion_058.csv.
"""
from __future__ import annotations

import csv
import itertools as it
import math

import numpy as np
import torch

import gpu_common as gc
from gpu_maxwell import CT, BlochComplex, GradientProjector, lobpcg

DIRECTIONS = {"[100] box axis": (1, 0, 0), "[110] face diagonal": (1, 1, 0), "[111] body diagonal": (1, 1, 1)}
KA = (0.025, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7)
CPU_SECONDS = "~1.5 s per k, dense (058 report); this machine's CPU rerun of the whole module: 78.7 s"


def rank(A, rel=1e-9):
    s = torch.linalg.svdvals(A)
    return int((s > rel * s.max()).sum())


def main():
    print("GPU validation of 058:", gc.environment())
    chk = gc.Checks()
    arr, digest, ok = gc.load_packing("057_periodic_spring_control", "packing_057")
    chk("057 packing content hash verified (geometry fixed)", ok, digest[:16])
    with gc.Timer() as tb:
        cx = BlochComplex(arr["x"], float(arr["L"]), arr["T"], arr["O"])
    chi = cx.nV - cx.nE + cx.nF - cx.nT
    print(f"  V = {cx.nV}, E = {cx.nE}, F = {cx.nF}, T = {cx.nT}, chi = {chi} (built in {tb.dt:.2f} s)")
    chk("complex rebuilt: chi = 0, E matches 057, all volumes positive",
        chi == 0 and cx.nE == len(arr["I"]) and (cx.tet_vol > 0).all())
    err_w = cx.whitney_commutes()
    chk("Whitney forms commute with d: curl(W1 u) = W2(d1 u) at random interior points", err_w < 1e-10, f"{err_w:.1e}")
    kt = np.array([0.3, -0.2, 0.1])
    e01 = max(float((cx.d1(k) @ cx.d0(k).to_dense()).abs().max()) for k in (np.zeros(3), kt))
    chk("d1 d0 = 0 at k = 0 and under a twist", e01 < 1e-12, f"{e01:.1e}")
    K, M1 = cx.operators(kt)
    D1 = cx.d1(kt).to_dense()
    Kg = D1.conj().T @ (cx.M2(kt) @ D1)
    eK = float((K.to_dense() - Kg).abs().max() / Kg.abs().max())
    chk("locally assembled K equals d1^H M2 d1 (global) under a twist", eK < 1e-12, f"{eK:.1e}")

    # ---- G3a / G3b at k = 0 ------------------------------------------------------
    k0 = np.zeros(3)
    K0, M10 = cx.operators(k0)
    D0, D1 = cx.d0(k0).to_dense().real, cx.d1(k0).to_dense().real
    M1d = M10.to_dense().real
    m1min, m2min = float(torch.linalg.eigvalsh(M1d)[0]), float(torch.linalg.eigvalsh(cx.M2(k0).to_dense().real)[0])
    r0, nul1 = rank(D0), cx.nE - rank(D1)
    _, s, Vh = torch.linalg.svd(D1)
    Z = Vh[rank(D1):].T
    A0 = D0.T @ M1d @ D0
    Q = Z - D0 @ torch.linalg.lstsq(A0, D0.T @ M1d @ Z).solution
    hdim = rank(Q, 1e-8)
    print(f"  G3a: Whitney M1 min eig {m1min:.4e} (report 6.229e-02), M2 min eig {m2min:.4e} (report 2.834e-01); "
          f"rank d0 = {r0}, nullity d1 = {nul1}, harmonic dims = {hdim}")
    chk("G3a: rank d0 = V - 1, nullity d1 = V + 2, exactly 3 harmonic dimensions",
        r0 == cx.nV - 1 and nul1 == cx.nV + 2 and hdim == 3)
    chk("Whitney mass minimum eigenvalues match the report (6.229e-02, 2.834e-01)",
        abs(m1min - 6.229e-2) < 6e-6 and abs(m2min - 2.834e-1) < 6e-5)
    U = torch.as_tensor(cx.evec, device=gc.DEV, dtype=gc.DT)
    closed, cocl = float((D1 @ U).abs().max()), float((D0.T @ M1d @ U).abs().max())
    energy = (U.T @ M1d @ U / cx.L**3).cpu().numpy()
    u, sv, _ = torch.linalg.svd(Q, full_matrices=False)
    H = u[:, :hdim]

    def m1orth(A):
        w, v = torch.linalg.eigh(A.T @ M1d @ A)
        return A @ v / torch.sqrt(w)

    cos = torch.linalg.svdvals(m1orth(H).T @ M1d @ m1orth(U)).cpu().numpy()
    print(f"  G3b: |d1 U| = {closed:.1e}, |d0^T M1 U| = {cocl:.1e}, energy/Vol diag {np.round(np.diag(energy), 12)}, "
          f"principal cosines {np.round(cos, 12)}")
    chk("G3b: uniform fields closed, co-closed, energy = Vol I, span the harmonic subspace",
        closed < 1e-12 and cocl < 1e-10 and np.allclose(energy, np.eye(3), atol=1e-10) and (cos > 1 - 1e-10).all())

    # ---- G3c: twisted gate --------------------------------------------------------
    a = float(np.linalg.norm(cx.evec, axis=1).mean())
    nh = np.ones(3) / math.sqrt(3)
    g3c = []
    for ka in (0.05, 0.1):
        kv = nh * ka / a
        K, M1 = cx.operators(kv)
        G = cx.d0(kv)
        r0k = rank(G.to_dense())
        Lm = torch.linalg.cholesky(M1.to_dense())
        Li = torch.linalg.inv(Lm)
        wf = torch.linalg.eigvalsh(Li @ K.to_dense() @ Li.conj().T).cpu().numpy()
        nzero = int((np.abs(wf) < 1e-9).sum())
        w, X, info = lobpcg(K, M1, GradientProjector(G, M1), nwant=3, block=8, tol=1e-10)
        g3c.append({"ka": ka, "rank_d0": r0k, "nzero": nzero, "w": w.tolist(), "lobpcg_iters": info["iters"]})
        print(f"  G3c ka = {ka} [111]: rank d0(k) = {r0k}; full problem {nzero} zero modes; projected LOBPCG "
              f"omega^2 = {np.array2string(w, precision=6)} ({info['iters']} it)")
        chk(f"G3c(i) ka = {ka}: exactly V gradient zero modes", r0k == cx.nV and nzero == cx.nV)
        chk(f"G3c(ii) ka = {ka}: two small positive transverse modes, next > 50x",
            w[0] > 1e-6 and w[1] > 1e-6 and w[2] > 50 * w[1])
    chk("G3c(ii): transverse frequencies fall with k", g3c[0]["w"][1] < g3c[1]["w"][0])
    rep = {0.05: (0.002574, 0.002574, 1.982550), 0.1: (0.010292, 0.010293, 1.918653)}
    chk("G3c projected omega^2 match the report to printed precision",
        all(abs(gw - rw) < 6e-7 for r in g3c for gw, rw in zip(r["w"], rep[r["ka"]])))

    # ---- dispersion scan ----------------------------------------------------------
    ref = {(r["direction"], round(float(r["ka"]), 6)): r for r in
           csv.DictReader(open(gc.SECTOR / "058_periodic_maxwell_calibration" / "dispersion_058.csv"))}
    recip = [2 * math.pi / cx.L * np.array(g) for g in it.product((-1, 0, 1), repeat=3) if any(g)]
    rows, times = [], []
    for name, d in DIRECTIONS.items():
        dn = np.array(d, float) / np.linalg.norm(d)
        X = None
        for ka in KA:
            kv = dn * ka / a
            with gc.Timer() as tm:
                K, M1 = cx.operators(kv)
                proj = GradientProjector(cx.d0(kv), M1)
                w, X, info = lobpcg(K, M1, proj, nwant=4, block=8, X0=X, tol=1e-10)
            times.append(tm.dt)
            v = np.sqrt(w[:2]) / np.linalg.norm(kv)
            fold = min(float(np.linalg.norm(kv - G)) for G in recip)
            r_ = ref[(name, round(ka, 6))]
            row = {"direction": name, "ka": ka, "v_slow": float(v[0]), "v_fast": float(v[1]),
                   "gap_ratio": float(w[2] / w[1]), "folded_rel": float(np.sqrt(w[2:4]).mean() / fold - 1),
                   "dv_slow": float(v[0]) - float(r_["v_slow"]), "dv_fast": float(v[1]) - float(r_["v_fast"]),
                   "dgap_rel": float(w[2] / w[1]) / float(r_["gap_ratio"]) - 1,
                   "lobpcg_iters": info["iters"], "res_max": float(info["res"].max()), "time_s": tm.dt}
            row["div_max"] = float(info["div"].max())
            rows.append(row)
            print(f"  {name:<20} ka {ka:<5} v = {v[0]:.10f}, {v[1]:.10f}  dv vs CSV {row['dv_slow']:+.1e}, "
                  f"{row['dv_fast']:+.1e}; gap ratio rel diff {row['dgap_rel']:+.1e}; {info['iters']} it, {tm.dt:.2f} s")
    dvmax = max(max(abs(r["dv_slow"]), abs(r["dv_fast"])) for r in rows)
    chk("phase speeds match dispersion_058.csv to 1e-8 (all 27 points, both polarizations)", dvmax < 1e-8, f"max {dvmax:.1e}")
    chk("gap ratios (next mode / upper transverse) match the CSV to 1e-6 relative",
        max(abs(r["dgap_rel"]) for r in rows) < 1e-6)
    chk("every returned mode is divergence-free (|G^H M1 x| / |M1 x| < 1e-10)",
        max(r["div_max"] for r in rows) < 1e-10, f"max {max(r['div_max'] for r in rows):.1e}")
    out = {"module": "058", "environment": gc.environment(), "packing_sha256": digest,
           "cpu_reference_time": CPU_SECONDS, "a": a, "gates": {"r0": r0, "nul1": nul1, "hdim": hdim,
           "cos": cos, "M1min": m1min, "M2min": m2min, "g3c": g3c, "whitney_commute_err": err_w},
           "dispersion": rows, "time_per_k_mean_s": float(np.mean(times)), "max_dv": dvmax, "checks": chk.rows}
    print(f"  mean time per k (assembly + projector + LOBPCG): {np.mean(times):.3f} s")
    print("  wrote", gc.save_result("gpu_058", out))
    print("VERDICT:", "PASS" if not chk.failures else f"FAIL ({len(chk.failures)})")


if __name__ == "__main__":
    main()
