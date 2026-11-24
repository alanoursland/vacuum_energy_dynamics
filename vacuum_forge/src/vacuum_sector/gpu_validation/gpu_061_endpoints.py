"""GPU validation of forge 061 (neighbour changes), endpoint level.

For each saved endpoint (rule A Delaunay fixed point; rule B flip orders
1-3; packing_061.npz, hash-verified): exact mesh identities, E_w and the
coordination histogram from this folder's own code against the report;
stationarity of the GPU energy (mu = 1e-3) at the saved coordinates; an
independent GPU relaxation (trust-region Newton-CG) from the saved
coordinates perturbed by 1e-3 noise must return to the same minimum; and
for rule A, an independent periodic Delaunay triangulation of the saved
coordinates must reproduce the saved connectivity (the fixed point).

The full rule-A iteration and rule-B flip search are NOT rerun on the GPU:
the triangulation and flip bookkeeping are CPU work, and at N = 160 the
GPU relaxations are slower than the CPU module (59 s for all of 061).
"""
from __future__ import annotations

import numpy as np
import torch

import gpu_common as gc

MU = 1e-3
REPORT = {
    "delaunay": (368.818, {3: 40, 4: 274, 5: 439, 6: 280, 7: 96, 8: 21, 9: 3}, 993),
    "flips_1": (363.824, {4: 304, 5: 461, 6: 258, 7: 81, 8: 14}, 958),
    "flips_2": (359.023, {4: 318, 5: 433, 6: 263, 7: 89, 8: 10}, 953),
    "flips_3": (376.209, {4: 318, 5: 438, 6: 258, 7: 90, 8: 12}, 956),
}


def main():
    print("GPU validation of 061 endpoints:", gc.environment())
    chk = gc.Checks()
    a61, d61, ok61 = gc.load_packing("061_neighbour_changes", "packing_061")
    a57, d57, ok57 = gc.load_packing("057_periodic_spring_control", "packing_057")
    chk("061 and 057 packing hashes verified", ok61 and ok57, d61[:16])
    L = float(a57["L"])
    rows = {}
    for tag, (E_rep, hist_rep, nT_rep) in REPORT.items():
        x, T, O = a61[f"x_{tag}"], a61[f"T_{tag}"], a61[f"O_{tag}"]
        ident = gc.mesh_identities(x, L, T, O)
        hid, nH = gc.hinge_index(T, O)
        m = gc.angle_measure(x, L, T, O, hid, nH)
        obj = gc.angle_objective(L, T, O, True, MU)
        _, g = obj.fg(torch.as_tensor(x, device=gc.DEV, dtype=gc.DT))
        gmax = float(g.abs().max())
        xp = x + 1e-3 * np.random.default_rng(7).standard_normal(x.shape)
        with gc.Timer() as tm:
            xr, info = gc.tr_newton(obj, xp, gtol=1e-10, maxit=2000)
        dx = gc.nonrigid_diff(xr, x)
        mr = gc.angle_measure(xr, L, T, O, hid, nH)
        row = {"E_w": m["E_w"], "E_w_report": E_rep, "hist": m["hist"], "nT": m["nT"], "identities": ident,
               "closure": m["closure"], "minV": m["minV"], "gmax_saved": gmax, "relax_status": info["status"],
               "relax_iters": info["iters"], "relax_time_s": tm.dt, "nonrigid_dx_return": dx, "E_w_return": mr["E_w"]}
        print(f"  {tag}: T = {m['nT']}, E_w = {m['E_w']:.4f} (report {E_rep}), histogram {m['hist']}; "
              f"max|g| at saved x = {gmax:.1e}; perturbed -> TR {info['status']} in {info['iters']} it "
              f"({tm.dt:.1f} s), non-rigid |dx| = {dx:.1e}")
        chk(f"{tag}: exact mesh identities, positive volumes, every hinge closed",
            all(ident.values()) and m["closure"] < 1e-8)
        chk(f"{tag}: E_w, T and coordination histogram match the report",
            abs(m["E_w"] - E_rep) < 6e-4 and m["hist"] == hist_rep and m["nT"] == nT_rep)
        chk(f"{tag}: saved coordinates are stationary for the GPU energy (max|g| < 1e-9)", gmax < 1e-9)
        chk(f"{tag}: GPU relaxation from a 1e-3 perturbation returns to the same minimum (|dx| < 1e-7)",
            info["status"] == "converged" and dx < 1e-7)
        if tag == "delaunay":
            Td, Od = gc.periodic_delaunay(x, L)
            same = gc.tet_keyset(Td, Od) == gc.tet_keyset(T, O)
            row["delaunay_fixed_point"] = same
            chk("rule A endpoint is a Delaunay fixed point (independent periodic Delaunay of the saved "
                "coordinates reproduces the saved tetrahedra)", same)
        rows[tag] = row
    out = {"module": "061", "environment": gc.environment(), "packing_sha256": d61,
           "cpu_reference_time": "whole module 59.0 s on this machine's CPU", "endpoints": rows,
           "checks": chk.rows}
    print("  wrote", gc.save_result("gpu_061", out))
    print("VERDICT:", "PASS" if not chk.failures else f"FAIL ({len(chk.failures)})")


if __name__ == "__main__":
    main()
