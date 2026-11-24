"""Diagnostic for gpu_057: is the committed 057 point a minimum of the GPU
energy, and which minimum does the GPU optimizer reach under different
globalizations? Prints gradient at the committed points, the lowest
non-translation Hessian eigenvalues, and endpoints of several runs."""
import numpy as np
import torch

import gpu_common as gc


def hess_dense(obj, x):
    return obj.hessian(torch.as_tensor(x, device=gc.DEV, dtype=gc.DT)).to_dense()


def low_eigs(obj, x, k=6):
    w = torch.linalg.eigvalsh(hess_dense(obj, x)).cpu().numpy()
    return w[:k]


def main():
    arr, digest, ok = gc.load_packing("057_periodic_spring_control", "packing_057")
    L, T, O, I, J, OF = float(arr["L"]), arr["T"], arr["O"], arr["I"], arr["J"], arr["OF"]
    obj = gc.spring_objective(L, T, O, I, J, OF, 1e-2)
    xc = arr["x"]
    f, g = obj.fg(torch.as_tensor(xc, device=gc.DEV, dtype=gc.DT))
    print(f"committed x (mu=1e-2): GPU energy {f:.12f}; max|grad| (autograd) {float(g.abs().max()):.2e}")
    print("  lowest Hessian eigenvalues at committed x:", np.array2string(low_eigs(obj, xc), precision=3))
    x0 = arr["x_initial"]
    runs = {}
    for label, start, d0 in (("TR delta0=0.5 from x_initial", x0, 0.5),
                             ("TR delta0=1e3 from x_initial", x0, 1e3),
                             ("TR delta0=0.05 from x_initial", x0, 0.05),
                             ("TR from committed + 1e-3 noise", xc + 1e-3 * np.random.default_rng(1).standard_normal(xc.shape), 0.5)):
        x, info = gc.tr_newton(obj, start, gtol=1e-11, delta0=d0)
        m = gc.spring_measure(x, L, T, O, I, J, OF)
        runs[label] = x
        print(f"{label}: {info['status']} ({info['iters']} it) E/N {m['E_per_N']:.8f} minV {m['minV']:.6f} "
              f"aniso {m['aniso']:.5f}; non-rigid |x - committed| {gc.nonrigid_diff(x, xc):.1e}; "
              f"low eigs {np.array2string(low_eigs(obj, x, 5), precision=3)}")


if __name__ == "__main__":
    main()
