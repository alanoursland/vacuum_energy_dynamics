"""Diagnostic for gpu_060: TR alone and FIRE + TR from 057 x_initial both reach
the committed 060 minima (weighted and unweighted, mu = 1e-3)."""
import sys, time
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import numpy as np
import gpu_common as gc
a57, _, _ = gc.load_packing("057_periodic_spring_control", "packing_057")
a60, _, _ = gc.load_packing("060_angle_energy_fixed_neighbors", "packing_060")
L, T, O = float(a57["L"]), a57["T"], a57["O"]
hid, nH = gc.hinge_index(T, O)
for weighted in (True, False):
    tag = "weighted" if weighted else "unweighted"
    obj = gc.angle_objective(L, T, O, weighted, 1e-3)
    t = time.time()
    x, i = gc.tr_newton(obj, a57["x_initial"], gtol=1e-10, maxit=2000)
    m = gc.angle_measure(x, L, T, O, hid, nH)
    print(tag, "TR only:", i["status"], i["iters"], "E_w %.4f E_u %.4f dx %.1e  %.1fs" % (m["E_w"], m["E_u"], gc.nonrigid_diff(x, a60["x_" + tag]), time.time() - t), flush=True)
    for ftol in (1e-1, 1e-2):
        t = time.time()
        xf, fi = gc.fire(obj, a57["x_initial"], ftol=ftol, max_steps=100000)
        x, i = gc.tr_newton(obj, xf, gtol=1e-10, maxit=2000)
        m = gc.angle_measure(x, L, T, O, hid, nH)
        print(tag, f"FIRE({ftol}) {fi['steps']} + TR:", i["status"], i["iters"], "E_w %.4f E_u %.4f dx %.1e  %.1fs" % (m["E_w"], m["E_u"], gc.nonrigid_diff(x, a60["x_" + tag]), time.time() - t), flush=True)
