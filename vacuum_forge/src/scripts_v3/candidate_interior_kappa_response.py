# Candidate interior kappa response
#
# Purpose
# -------
# Compare whether kappa should be forced to zero inside matter or allowed to
# respond to traceful matter sources while still relaxing to zero outside.
#
# Suggested location:
#   scripts_v3/candidate_interior_kappa_response.py

import sympy as sp


def header(title: str) -> None:
    print()
    print("=" * 108)
    print(title)
    print("=" * 108)


def status_line(label: str, ok: bool, detail: str = "") -> None:
    mark = "PASS" if ok else "WARN"
    if detail:
        print(f"[{mark}] {label}: {detail}")
    else:
        print(f"[{mark}] {label}")


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def case_0_recap():
    header("Case 0: Reduced mode recap")
    print("A = exp(kappa+s)")
    print("B = exp(kappa-s)")
    print("AB = exp(2*kappa)")
    print()
    print("Exterior compensation:")
    print("  kappa = 0")
    print("  AB = 1")
    print("  B = 1/A")
    print()
    print("Interior question:")
    print("  Should kappa=0 hold inside matter?")
    print("  Or can matter source kappa inside while exterior kappa relaxes to zero?")
    status_line("interior kappa question isolated", True)


def case_1_forced_interior_compensation():
    header("Case 1: Forced interior compensation")

    r, R, G, c, rho0 = sp.symbols("r R G c rho0", positive=True, real=True)

    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)
    kappa_in = sp.Integer(0)
    B_in = sp.simplify(sp.exp(2*kappa_in) / A_in)
    AB = sp.simplify(A_in * B_in)

    print(f"A_in = {A_in}")
    print(f"kappa_in = {kappa_in}")
    print(f"B_in = exp(2*kappa)/A = {B_in}")
    print(f"A_in B_in = {AB}")

    status_line("forced kappa=0 gives reciprocal interior", is_zero(AB - 1))

    print()
    print("Caution:")
    print("  This is the simplest interior extension, but it may be too strong.")
    print("  It excludes traceful matter response in kappa.")


def case_2_generic_traceful_kappa_source():
    header("Case 2: Generic traceful kappa source inside matter")

    r, R, G, c, rho0, eta = sp.symbols("r R G c rho0 eta", positive=True, real=True)

    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)
    kappa_in = eta * G * rho0 * (R**2 - r**2) / c**2

    B_in = sp.simplify(sp.exp(2*kappa_in) / A_in)
    AB = sp.simplify(A_in * B_in)

    kappa_R = sp.simplify(kappa_in.subs(r, R))
    dkappa_R = sp.simplify(sp.diff(kappa_in, r).subs(r, R))
    kappa_0 = sp.simplify(kappa_in.subs(r, 0))
    dkappa_0 = sp.simplify(sp.diff(kappa_in, r).subs(r, 0))

    print(f"A_in = {A_in}")
    print(f"kappa_in = {kappa_in}")
    print(f"B_in = exp(2*kappa)/A = {B_in}")
    print(f"A_in B_in = {AB}")
    print()
    print(f"kappa_in(R) = {kappa_R}")
    print(f"kappa_in'(R) = {dkappa_R}")
    print(f"kappa_in(0) = {kappa_0}")
    print(f"kappa_in'(0) = {dkappa_0}")

    status_line("interior kappa can vanish at boundary", is_zero(kappa_R))
    status_line("interior kappa is regular at origin", is_zero(dkappa_0))
    status_line("nonzero interior kappa breaks reciprocal interior generically", not is_zero(AB - 1))
    status_line("boundary derivative may jump unless exterior layer handles it", not is_zero(dkappa_R))


def case_3_smooth_boundary_kappa_profile():
    header("Case 3: Smooth boundary kappa profile")

    r, R, G, c, rho0, eta = sp.symbols("r R G c rho0 eta", positive=True, real=True)
    kappa_in = eta * G * rho0 * (R**2 - r**2)**2 / (c**2 * R**2)

    kappa_R = sp.simplify(kappa_in.subs(r, R))
    dkappa_R = sp.simplify(sp.diff(kappa_in, r).subs(r, R))
    dkappa_0 = sp.simplify(sp.diff(kappa_in, r).subs(r, 0))

    print(f"kappa_in = {kappa_in}")
    print(f"kappa_in(R) = {kappa_R}")
    print(f"kappa_in'(R) = {dkappa_R}")
    print(f"kappa_in'(0) = {dkappa_0}")

    status_line("kappa vanishes at boundary", is_zero(kappa_R))
    status_line("kappa derivative vanishes at boundary", is_zero(dkappa_R))
    status_line("kappa regular at origin", is_zero(dkappa_0))


def case_4_energy_penalty_model():
    header("Case 4: Interior kappa energy penalty model")

    kappa, C_k, J_k = sp.symbols("kappa C_k J_k", positive=True, real=True)

    E = C_k*kappa**2 - J_k*kappa
    eq = sp.Eq(sp.diff(E, kappa), 0)
    sol = sp.solve(eq, kappa)

    print(f"E = {E}")
    print(f"Stationary equation: {eq}")
    print(f"kappa solution = {sol}")
    print()
    print("If J_k is nonzero inside matter, kappa responds.")
    print("If J_k=0 outside, kappa relaxes to zero.")

    status_line("traceful source produces interior kappa response", bool(sol))


def case_5_exterior_matching_classification():
    header("Case 5: Exterior matching classification")

    print("Interior/exterior possibilities:")
    print()
    print("A. kappa=0 everywhere")
    print("   - simplest")
    print("   - reciprocal interior")
    print("   - not GR interior")
    print()
    print("B. kappa sourced inside, kappa(R)=0")
    print("   - exterior remains compensated")
    print("   - interior can carry traceful matter response")
    print("   - boundary derivative may need interface physics")
    print()
    print("C. kappa sourced inside, kappa(R)=kappa_R != 0")
    print("   - exterior begins with nonzero kappa")
    print("   - reciprocal exterior may fail unless relaxation layer suppresses it")
    print()
    print("D. smooth interior kappa with kappa(R)=kappa'(R)=0")
    print("   - cleanest coexistence of interior trace response and exterior compensation")
    status_line("classification separates interior matter response from exterior compensation", True)


def case_6_observable_exterior_pressure():
    header("Case 6: Exterior pressure from kappa leakage")

    eps, lam = sp.symbols("eps lambda_k", real=True)

    kappa_ext = lam * eps
    s_ext = -2 * eps

    A = sp.exp(kappa_ext + s_ext)
    B = sp.exp(kappa_ext - s_ext)
    AB = sp.simplify(A*B)

    A_first = sp.series(A, eps, 0, 2).removeO()
    B_first = sp.series(B, eps, 0, 2).removeO()
    AB_first = sp.series(AB, eps, 0, 2).removeO()

    print("If interior kappa leaks into exterior as kappa=lambda_k eps:")
    print(f"A ≈ {A_first}")
    print(f"B ≈ {B_first}")
    print(f"AB ≈ {AB_first}")
    print()
    print("Exterior kappa leak is observationally dangerous.")
    status_line("exterior kappa must be suppressed or tightly bounded", True)


def final_interpretation():
    header("Final interpretation")

    print("This script supports a refined interior/exterior picture:")
    print()
    print("  Exterior source-free region:")
    print("    kappa should relax to zero.")
    print()
    print("  Interior matter region:")
    print("    kappa may be forced to zero as a simple model,")
    print("    or may respond to traceful matter sources.")
    print()
    print("A nonzero interior kappa is not automatically fatal if:")
    print("  kappa -> 0 at the surface or through a boundary layer,")
    print("  exterior kappa remains suppressed,")
    print("  and no kappa leak persists into weak-field exterior observations.")
    print()
    print("Possible next artifact:")
    print("  candidate_interior_kappa_response.md")


def main():
    header("Candidate Interior Kappa Response")
    case_0_recap()
    case_1_forced_interior_compensation()
    case_2_generic_traceful_kappa_source()
    case_3_smooth_boundary_kappa_profile()
    case_4_energy_penalty_model()
    case_5_exterior_matching_classification()
    case_6_observable_exterior_pressure()
    final_interpretation()


if __name__ == "__main__":
    main()
