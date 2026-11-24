"""GPU validation of forge 060 (trial angle energy, neighbours fixed).

On the 057 quanta, box and neighbour list (hash-verified), relax the
length-weighted angle energy (P10 candidate) and its unweighted control from
057's pre-relaxation coordinates at mu = 1e-3, 1e-4, 1e-5 (warm-started),
with independent GPU optimizers, and compare E_u, E_w, the unavoidable total,
and the directional-fabric overlaps with the committed 060 packing and the
060 report.
"""
from __future__ import annotations

import itertools as it

import numpy as np

import gpu_common as gc

MUS = (1e-3, 1e-4, 1e-5)
REPORT = {  # 060 report E2/E3 (angle energy only) and E5
    False: {1e-3: 976.7102, 1e-4: 976.7091, 1e-5: 976.7090},
    True: {1e-3: 948.5497, 1e-4: 948.5485, 1e-5: 948.5484},
    "unavoid": 441.1291,
    "aniso": {"angle, unweighted": 0.0248, "angle, weighted": 0.0275, "extra only, unweighted": 0.0269,
              "extra only, weighted": 0.0287, "spring (057)": 0.0322, "angle at start": 0.0202},
    "overlaps": {("angle, weighted", "spring (057)"): 0.906, ("angle, unweighted", "spring (057)"): 0.902,
                 ("angle, weighted", "angle, unweighted"): 0.990, ("angle, weighted", "angle at start"): 0.884,
                 ("spring (057)", "angle at start"): 0.916, ("extra only, weighted", "spring (057)"): 0.654},
}
CPU_SECONDS = "seconds per run (060 report); this machine's CPU rerun of the whole module: 30.6 s"


def fabrics(x_u, x_w, a57, hid, nH):
    L, T, O = float(a57["L"]), a57["T"], a57["O"]
    mu_, mw = gc.angle_measure(x_u, L, T, O, hid, nH), gc.angle_measure(x_w, L, T, O, hid, nH)
    xs = a57["x_weak"]
    b = xs[a57["J"]] + L * a57["OF"] - xs[a57["I"]]
    l = np.linalg.norm(b, axis=1)
    m0 = gc.angle_measure(a57["x_initial"], L, T, O, hid, nH)
    return {"angle, unweighted": mu_["fab_u"], "angle, weighted": mw["fab_w"],
            "extra only, unweighted": mu_["fab_extra_u"], "extra only, weighted": mw["fab_extra_w"],
            "spring (057)": gc.fabric((l - 1) ** 2, b / l[:, None]), "angle at start": m0["fab_u"]}


def main():
    print("GPU validation of 060:", gc.environment())
    chk = gc.Checks()
    a57, d57, ok57 = gc.load_packing("057_periodic_spring_control", "packing_057")
    a60, d60, ok60 = gc.load_packing("060_angle_energy_fixed_neighbors", "packing_060")
    chk("057 and 060 packing content hashes verified", ok57 and ok60, f"{d57[:16]}, {d60[:16]}")
    L, T, O = float(a57["L"]), a57["T"], a57["O"]
    hid, nH = gc.hinge_index(T, O)
    m_start = gc.angle_measure(a57["x_initial"], L, T, O, hid, nH)
    print(f"  start: E_u = {m_start['E_u']:.3f}, unavoidable = {m_start['unavoid']:.4f}, "
          f"extra = {m_start['extra']:.3f}, max closure defect {m_start['closure']:.1e}")
    chk("start: unavoidable total 441.129 and every hinge closed",
        abs(m_start["unavoid"] - REPORT["unavoid"]) < 1e-4 and m_start["closure"] < 1e-9)

    # implementation agreement at the committed minima
    for weighted, key in ((False, "x_unweighted"), (True, "x_weighted")):
        obj = gc.angle_objective(L, T, O, weighted, MUS[0])
        xt = gc.torch.as_tensor(a60[key], device=gc.DEV, dtype=gc.DT)
        _, g = obj.fg(xt)
        w = gc.torch.linalg.eigvalsh(obj.hessian(xt).to_dense()).cpu().numpy()
        print(f"  committed {key} (mu = 1e-3): autograd max|g| = {float(g.abs().max()):.1e}; "
              f"Hessian lowest {np.round(w[:4], 6).tolist()}")
        chk(f"committed {key} is stationary for the GPU energy (max|g| < 1e-9) and a local minimum "
            "(no eigenvalue below -1e-8 beyond translations)",
            float(g.abs().max()) < 1e-9 and w[3] > -1e-8)

    out_rows, xs_final, basin = {}, {}, {}
    for weighted in (False, True):
        tag = "weighted" if weighted else "unweighted"
        # (diag_060_basins.py: FIRE + TR from the same start reaches the same minima)
        x, rows = a57["x_initial"], []
        for mu in MUS:
            obj = gc.angle_objective(L, T, O, weighted, mu)
            finfo = {"steps": 0}
            with gc.Timer() as tm:
                x, info = gc.tr_newton(obj, x, gtol=1e-10, maxit=2000)
            m = gc.angle_measure(x, L, T, O, hid, nH)
            E = m["E_w"] if weighted else m["E_u"]
            r = {"mu": mu, "E": E, "unavoid": m["unavoid"], "extra": m["extra"], "minV": m["minV"],
                 "min_len": m["min_len"], "mean_len": m["mean_len"], "time_s": tm.dt,
                 "fire_steps": finfo["steps"], **{k: info[k] for k in ("iters", "cg", "status", "gmax",
                                                                          "roundoff_accepts")}}
            ref_key = f"x_{tag}" if mu == MUS[0] else (f"x_{tag}_weak" if mu == MUS[-1] else None)
            if ref_key:
                r["nonrigid_dx_vs_committed"] = gc.nonrigid_diff(x, a60[ref_key])
            print(f"  {tag} mu = {mu:g}: TR {info['iters']} ({info['status']}, "
                  f"max|g| {info['gmax']:.1e}) {tm.dt:.1f} s: E = {E:.4f} (report {REPORT[weighted][mu]}), "
                  f"unavoidable {m['unavoid']:.4f}, extra {m['extra']:.4f}, min V {m['minV']:.2e}"
                  + (f"; non-rigid |dx| vs committed {r['nonrigid_dx_vs_committed']:.1e}" if ref_key else ""))
            chk(f"{tag} mu = {mu:g}: converged and E matches report to 1e-4",
                info["status"] == "converged" and abs(E - REPORT[weighted][mu]) < 1.5e-4)
            chk(f"{tag} mu = {mu:g}: unavoidable total frozen at 441.129", abs(m["unavoid"] - REPORT["unavoid"]) < 1e-4)
            if ref_key:
                chk(f"{tag} mu = {mu:g}: same minimum as committed 060 (non-rigid |dx| < 1e-6)",
                    r["nonrigid_dx_vs_committed"] < 1e-6)
            rows.append(r)
        out_rows[tag], xs_final[tag] = rows, x

    F = fabrics(xs_final["unweighted"], xs_final["weighted"], a57, hid, nH)
    Fc = fabrics(a60["x_unweighted_weak"], a60["x_weighted_weak"], a57, hid, nH)
    fab_out = {}
    for k in F:
        fab_out[k] = {"aniso_gpu": F[k]["aniso"], "aniso_committed": Fc[k]["aniso"], "aniso_report": REPORT["aniso"][k]}
        print(f"  fabric {k:<24} aniso GPU {F[k]['aniso']:.5f}  committed {Fc[k]['aniso']:.5f}  report {REPORT['aniso'][k]}")
    ov_out = []
    for (a, b), rep in REPORT["overlaps"].items():
        og, oc = gc.overlap(F[a], F[b]), gc.overlap(Fc[a], Fc[b])
        ov_out.append({"pair": [a, b], "gpu": og, "committed": oc, "report": rep})
        print(f"  overlap {a} vs {b}: GPU {og:+.4f}  committed {oc:+.4f}  report {rep:+.3f}")
    chk("fabric overlaps match the report to ~1e-3", all(abs(o["gpu"] - o["report"]) < 1.5e-3 for o in ov_out))
    chk("fabric anisotropies match the report to printed precision",
        all(abs(v["aniso_gpu"] - v["aniso_report"]) < 6e-5 for v in fab_out.values()))
    out = {"module": "060", "environment": gc.environment(), "packing_sha256": {"057": d57, "060": d60},
           "cpu_reference_time": CPU_SECONDS, "rows": out_rows, "basin_note_tr_only": basin,
           "fabrics": fab_out, "overlaps": ov_out, "checks": chk.rows}
    print("  wrote", gc.save_result("gpu_060", out))
    print("VERDICT:", "PASS" if not chk.failures else f"FAIL ({len(chk.failures)})")


if __name__ == "__main__":
    main()
