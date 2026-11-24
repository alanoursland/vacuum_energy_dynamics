"""GPU validation of forge 057 (periodic spring control).

From the saved 057 starting coordinates (x_initial; hash-verified), relax the
spring proxy + log-volume barrier at mu = 1e-2, 1e-3, 1e-4 (warm-started, as
057 does) with an independent GPU optimizer (gpu_common.tr_newton), then
compare energy per vertex, minimum volume, energy-fabric anisotropy and
principal axes with (a) the committed 057 coordinates, measured by this
script's own code, and (b) the numbers printed in the 057 report.
"""
from __future__ import annotations

import numpy as np

import gpu_common as gc

REPORT = {  # 057 report, E3/E4
    1e-2: {"E_per_N": 0.28886, "minV": 0.01487, "aniso": 0.0329},
    1e-3: {"E_per_N": 0.28697, "minV": 0.00164, "aniso": 0.0317},
    1e-4: {"E_per_N": 0.28677, "minV": 0.00017, "aniso": 0.0322},
}
CPU_SECONDS = "under 1 s per barrier strength (057 report; this machine's CPU rerun: 0.7 s at mu = 1e-2)"


def main():
    print("GPU validation of 057:", gc.environment())
    chk = gc.Checks()
    arr, digest, ok = gc.load_packing("057_periodic_spring_control", "packing_057")
    chk("057 packing content hash verified", ok, digest[:16])
    L, T, O, I, J, OF = float(arr["L"]), arr["T"], arr["O"], arr["I"], arr["J"], arr["OF"]
    committed = {1e-2: arr["x"], 1e-4: arr["x_weak"]}
    # implementation agreement: the committed minimum is a minimum of THIS code's energy
    obj = gc.spring_objective(L, T, O, I, J, OF, 1e-2)
    xt = gc.torch.as_tensor(arr["x"], device=gc.DEV, dtype=gc.DT)
    _, g = obj.fg(xt)
    w = gc.torch.linalg.eigvalsh(obj.hessian(xt).to_dense()).cpu().numpy()
    gmax_c = float(g.abs().max())
    print(f"  committed x (mu = 1e-2): autograd max|g| = {gmax_c:.2e} (report: 8.5e-12); "
          f"Hessian: 3 translation zeros {np.round(w[:3], 15).tolist()}, next {w[3]:.4f}")
    chk("committed 057 minimum is stationary for the independent GPU energy (max|g| < 1e-10)",
        gmax_c < 1e-10)
    chk("... and a strict local minimum (Hessian > 0 beyond the 3 translations)",
        abs(w[:3]).max() < 1e-10 and w[3] > 1e-3)

    # basin note: trust-region Newton-CG straight from x_initial
    with gc.Timer() as tm_tr:
        x_tr, info_tr = gc.tr_newton(obj, arr["x_initial"], gtol=1e-11)
    m_tr = gc.spring_measure(x_tr, L, T, O, I, J, OF)
    basin_note = {"E_per_N": m_tr["E_per_N"], "minV": m_tr["minV"], "aniso": m_tr["aniso"],
                  "nonrigid_dx_vs_committed": gc.nonrigid_diff(x_tr, arr["x"]),
                  "axis_angles_deg_vs_committed": gc.axis_angles(
                      m_tr["axes"], gc.spring_measure(arr["x"], L, T, O, I, J, OF)["axes"]),
                  "time_s": tm_tr.dt, "status": info_tr["status"]}
    print(f"  basin note -- TR Newton-CG directly from x_initial: {info_tr['status']}, E/N = "
          f"{m_tr['E_per_N']:.6f}, aniso = {m_tr['aniso']:.5f}, non-rigid |dx| vs committed = "
          f"{basin_note['nonrigid_dx_vs_committed']:.2f} (a different local minimum)")

    # primary independent optimizer: FIRE (descent path) then TR polish; warm-started in mu
    x = arr["x_initial"]
    rows = []
    for mu in (1e-2, 1e-3, 1e-4):
        obj = gc.spring_objective(L, T, O, I, J, OF, mu)
        with gc.Timer() as tm:
            xf, finfo = gc.fire(obj, x, ftol=1e-4)
            x, info = gc.tr_newton(obj, xf, gtol=1e-11)
        m = gc.spring_measure(x, L, T, O, I, J, OF)
        row = {"mu": mu, "time_s": tm.dt, "fire_steps": finfo["steps"],
               **{k: info[k] for k in ("iters", "cg", "status", "gmax", "roundoff_accepts", "rejects")},
               "E_per_N": m["E_per_N"], "minV": m["minV"], "aniso": m["aniso"],
               "axes": m["axes"], "dev_eigs": m["dev_eigs"]}
        print(f"  mu = {mu:g}: FIRE {finfo['steps']} steps, then TR {info['status']} in {info['iters']} iterations "
              f"({info['cg']} CG, {info['roundoff_accepts']} roundoff accepts), max|g| = {info['gmax']:.1e}, "
              f"{tm.dt:.2f} s; E/N = {m['E_per_N']:.6f}, min V = {m['minV']:.6f} V_ref, aniso = {m['aniso']:.5f}")
        chk(f"mu = {mu:g}: GPU optimizer converged (max|g| < 1e-11)", info["status"] == "converged")
        rep = REPORT[mu]
        chk(f"mu = {mu:g}: matches report E/N, min V, anisotropy to printed precision",
            abs(m["E_per_N"] - rep["E_per_N"]) < 6e-6 and abs(m["minV"] - rep["minV"]) < 6e-6
            and abs(m["aniso"] - rep["aniso"]) < 6e-5)
        if mu in committed:
            c = gc.spring_measure(committed[mu], L, T, O, I, J, OF)
            dx = gc.nonrigid_diff(x, committed[mu])
            ang = gc.axis_angles(m["axes"], c["axes"])
            row.update(committed={"E_per_N": c["E_per_N"], "minV": c["minV"], "aniso": c["aniso"]},
                       nonrigid_dx=dx, axis_angles_deg=ang,
                       dE_rel=abs(m["E_per_N"] / c["E_per_N"] - 1),
                       dminV_rel=abs(m["minV"] / c["minV"] - 1), daniso=abs(m["aniso"] - c["aniso"]))
            print(f"    vs committed: non-rigid max|dx| = {dx:.1e}; dE/E = {row['dE_rel']:.1e}; "
                  f"d minV/minV = {row['dminV_rel']:.1e}; d aniso = {row['daniso']:.1e}; "
                  f"axis angles = {', '.join(f'{a:.1e}' for a in ang)} deg")
            chk(f"mu = {mu:g}: same minimum as committed 057 (E/N, min V, anisotropy to 1e-6; "
                "axes to 1e-4 deg)",
                row["dE_rel"] < 1e-6 and row["dminV_rel"] < 1e-6 and row["daniso"] < 1e-6
                and max(ang) < 1e-4)
        rows.append(row)
    out = {"module": "057", "environment": gc.environment(), "packing_sha256": digest,
           "cpu_reference_time": CPU_SECONDS, "rows": rows, "basin_note_tr_only": basin_note,
           "checks": chk.rows}
    print("  wrote", gc.save_result("gpu_057", out))
    print("VERDICT:", "PASS" if not chk.failures else f"FAIL ({len(chk.failures)})")


if __name__ == "__main__":
    main()
