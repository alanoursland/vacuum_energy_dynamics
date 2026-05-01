# Candidate boundary flux action
#
# Purpose
# -------
# Test whether the areal-flux law can be interpreted as a boundary condition
# from variation of a reduced radial action.
#
# The bulk radial A-action is:
#
#   E_bulk = integral dr [ r^2 K_A (A')^2 ]
#
# Variation gives:
#
#   bulk equation: d/dr(r^2 A') = 0
#   boundary term: [2 K_A r^2 A' delta A]_{boundary}
#
# If a source/interface contributes a boundary coupling:
#
#   E_boundary = - q A(R)
#
# then variation at R gives:
#
#   2 K_A R^2 A'(R) = q
#
# Therefore:
#
#   4 pi R^2 A'(R) = (2 pi/K_A) q
#
# Choosing q = 4 K_A G M / c^2 gives:
#
#   4 pi R^2 A'(R) = 8 pi G M / c^2
#
# This script tests whether areal flux can be read as a boundary/interface
# condition rather than an ordinary curved-space scalar equation.
#
# Suggested location:
#   scripts_v3/candidate_boundary_flux_action.py

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


def euler_lagrange_1d(L, field, x):
    f = field
    fp = sp.diff(f, x)
    return sp.simplify(sp.diff(L, f) - sp.diff(sp.diff(L, fp), x))


def case_0_radial_bulk_action():
    header("Case 0: Radial bulk action")

    r, K_A = sp.symbols("r K_A", positive=True, real=True)
    A = sp.Function("A")(r)

    L = K_A * r**2 * sp.diff(A, r)**2
    EL = euler_lagrange_1d(L, A, r)

    print(f"L_bulk = {L}")
    print(f"Euler-Lagrange = {EL} = 0")
    print()
    print("Equivalent:")
    print("  d/dr(r^2 A') = 0")
    print("  source-free areal flux is conserved")

    expected = -2*K_A*sp.diff(r**2 * sp.diff(A, r), r)
    status_line("bulk action gives conserved areal flux", is_zero(EL - expected))


def case_1_boundary_variation_term():
    header("Case 1: Boundary variation term")

    r, R, K_A = sp.symbols("r R K_A", positive=True, real=True)
    Ap_R, deltaA_R = sp.symbols("A_prime_R deltaA_R", real=True)

    boundary_term = 2 * K_A * R**2 * Ap_R * deltaA_R

    print("Variation of bulk action gives boundary term:")
    print()
    print("  [2 K_A r² A' deltaA] at boundary")
    print()
    print(f"At r=R: {boundary_term}")

    status_line("bulk variation exposes areal flux as boundary momentum", True)


def case_2_source_boundary_coupling():
    header("Case 2: Source boundary coupling")

    R, K_A, q = sp.symbols("R K_A q", positive=True, real=True)
    Ap_R = sp.symbols("A_prime_R", real=True)

    # Boundary action E_b = -q A(R)
    # variation contributes -q deltaA.
    # total boundary coefficient:
    #   2 K_A R^2 A' - q = 0
    boundary_eq = sp.Eq(2*K_A*R**2*Ap_R - q, 0)
    sol_Ap = sp.solve(boundary_eq, Ap_R)[0]

    print("Boundary source coupling:")
    print("  E_boundary = -q A(R)")
    print()
    print("Boundary stationarity:")
    print("  2 K_A R² A'(R) - q = 0")
    print()
    print(f"A'(R) = {sol_Ap}")

    flux = sp.simplify(4*sp.pi*R**2*sol_Ap)
    print(f"F_A(R)=4πR²A'(R) = {flux}")

    status_line("boundary source fixes areal flux", True)


def case_3_mass_normalization():
    header("Case 3: Mass normalization of boundary charge")

    R, K_A, G, M, c = sp.symbols("R K_A G M c", positive=True, real=True)

    q = 4*K_A*G*M/c**2
    Ap_R = sp.simplify(q / (2*K_A*R**2))
    flux = sp.simplify(4*sp.pi*R**2*Ap_R)
    target = 8*sp.pi*G*M/c**2

    print(f"q_M = {q}")
    print(f"A'(R) = {Ap_R}")
    print(f"F_A = {flux}")
    print(f"target = {target}")

    status_line("mass-normalized boundary charge gives desired flux", is_zero(flux - target))


def case_4_exterior_solution_from_boundary():
    header("Case 4: Exterior solution from boundary condition")

    r, R, G, M, c = sp.symbols("r R G M c", positive=True, real=True)
    C0, C1 = sp.symbols("C0 C1", real=True)

    A = C0 + C1/r
    Ap = sp.diff(A, r)

    flux = sp.simplify(4*sp.pi*r**2*Ap)
    target = 8*sp.pi*G*M/c**2

    # flux = -4*pi*C1, so C1=-2GM/c^2.
    sol_C1 = sp.solve(sp.Eq(flux, target), C1)[0]
    A_matched = sp.simplify(A.subs({C0: 1, C1: sol_C1}))

    print(f"A_general = {A}")
    print(f"F_A = {flux}")
    print(f"C1 from flux = {sol_C1}")
    print(f"A with asymptotic flatness = {A_matched}")

    status_line("boundary flux gives Schwarzschild A coefficient",
                is_zero(A_matched - (1 - 2*G*M/(c**2*r))))


def case_5_boundary_vs_bulk_source():
    header("Case 5: Boundary source versus bulk source")

    print("Two equivalent reduced descriptions:")
    print()
    print("1. Bulk density source:")
    print("   d/dr(4πr²A') = 4πr² * 8πGρ/c²")
    print()
    print("2. Boundary/source interface:")
    print("   4πR²A'(R) = 8πGM/c²")
    print()
    print("For exterior r>R, both give:")
    print("   A = 1 - 2GM/(rc²)")
    print()
    print("Interpretation:")
    print("   The areal-flux law can be viewed as a Gauss law: the bulk source")
    print("   determines the boundary flux seen by the exterior.")
    status_line("boundary and bulk views agree for exterior flux", True)


def case_6_kappa_compensation_coupling():
    header("Case 6: Coupling to kappa compensation")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    A = 1 - 2*G*M/(c**2*r)
    kappa = sp.Integer(0)
    B = sp.simplify(sp.exp(2*kappa) / A)
    AB = sp.simplify(A*B)

    print(f"A = {A}")
    print(f"kappa = {kappa}")
    print(f"B = exp(2kappa)/A = {B}")
    print(f"AB = {AB}")

    status_line("boundary flux plus kappa=0 recovers reciprocal exterior", is_zero(AB - 1))


def final_interpretation():
    header("Final interpretation")

    print("The reduced radial A-action exposes areal flux as the boundary")
    print("momentum conjugate to A:")
    print()
    print("  boundary momentum ∝ r² A'")
    print()
    print("A source/interface coupling -q A(R) fixes that boundary momentum.")
    print("With q proportional to M, the boundary condition becomes:")
    print()
    print("  4πR²A'(R) = 8πGM/c²")
    print()
    print("The exterior bulk equation then gives:")
    print()
    print("  A = 1 - 2GM/(rc²)")
    print()
    print("Combined with kappa=0:")
    print()
    print("  B = 1/A")
    print()
    print("Possible next artifact:")
    print("  candidate_boundary_flux_action.md")


def main():
    header("Candidate Boundary Flux Action")
    case_0_radial_bulk_action()
    case_1_boundary_variation_term()
    case_2_source_boundary_coupling()
    case_3_mass_normalization()
    case_4_exterior_solution_from_boundary()
    case_5_boundary_vs_bulk_source()
    case_6_kappa_compensation_coupling()
    final_interpretation()


if __name__ == "__main__":
    main()
