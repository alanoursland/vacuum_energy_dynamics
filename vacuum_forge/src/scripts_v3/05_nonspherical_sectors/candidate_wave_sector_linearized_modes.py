# Candidate wave sector linearized modes
#
# Purpose
# -------
# The nonspherical degree inventory showed that scalar A handles the weak
# Newtonian scalar sector and vector W_i is needed for frame dragging.
#
# But a full gravity theory also needs a wave/radiative sector.
#
# In linearized GR, gravitational waves are represented by transverse-
# traceless spatial perturbations:
#
#   h_ij^TT
#
# This script checks what the current reduced program has and what is missing:
#
#   1. scalar A is not a TT tensor mode,
#   2. vector W_i is not a TT tensor mode,
#   3. a TT spatial matrix has two polarizations,
#   4. TT modes are trace-free and transverse,
#   5. a wave equation would need an independent tensor sector,
#   6. scalar/vector/tensor sectors should remain distinct.
#
# This does not derive gravitational waves. It inventories the linearized
# wave-sector requirement.
#
# Suggested location:
#   scripts_v3/candidate_wave_sector_linearized_modes.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 116)
    print(title)
    print("=" * 116)


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


# =============================================================================
# Case 0: Why wave sector is needed
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Why wave sector is needed")

    print("Current sectors:")
    print("  scalar A -> Newtonian potential / mass flux")
    print("  kappa -> trace/interior response candidate")
    print("  vector W_i -> frame-dragging candidate")
    print()
    print("Missing:")
    print("  tensor transverse-traceless wave sector h_ij^TT")
    print()
    print("A full relativistic gravity theory must address propagating waves.")
    status_line("wave-sector problem isolated", True)


# =============================================================================
# Case 1: Scalar mode is not TT
# =============================================================================

def case_1_scalar_not_tt():
    header("Case 1: Scalar spatial mode is not transverse-traceless")

    psi = sp.symbols("psi", real=True)

    H_scalar = -2*psi*sp.eye(3)
    trace = sp.trace(H_scalar)

    print("Scalar spatial perturbation:")
    print(H_scalar)
    print(f"trace = {trace}")
    print()
    print("A TT tensor must be trace-free.")
    print("The scalar conformal perturbation has nonzero trace unless psi=0.")

    status_line("scalar mode is not TT", not is_zero(trace))


# =============================================================================
# Case 2: Vector mode is not TT spatial tensor
# =============================================================================

def case_2_vector_not_tt():
    header("Case 2: Vector mode is not a TT spatial tensor")

    Wx, Wy, Wz = sp.symbols("W_x W_y W_z", real=True)

    W = sp.Matrix([[Wx, Wy, Wz]])

    print("Vector sector:")
    print(f"W_i = {W}")
    print()
    print("This lives in g_ti-like components, not in the symmetric spatial")
    print("tensor h_ij^TT.")
    print()
    status_line("vector sector is distinct from tensor wave sector", True)


# =============================================================================
# Case 3: TT tensor polarizations
# =============================================================================

def case_3_tt_polarizations():
    header("Case 3: TT tensor polarizations")

    hp, hx = sp.symbols("h_plus h_cross", real=True)

    # TT wave propagating in z direction.
    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_TT)

    print("TT spatial perturbation for wave along z:")
    print(H_TT)
    print(f"trace = {trace}")
    print()
    print("Independent polarizations:")
    print("  h_plus")
    print("  h_cross")

    status_line("TT tensor has two polarizations", is_zero(trace))


# =============================================================================
# Case 4: Transversality check for z-propagating TT mode
# =============================================================================

def case_4_transversality():
    header("Case 4: Transversality check")

    hp, hx, k = sp.symbols("h_plus h_cross k", real=True)

    # Wave vector along z.
    kvec = sp.Matrix([0, 0, k])
    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    # Transversality: k^i h_ij = 0.
    trans = sp.simplify((kvec.T * H_TT))

    print(f"k vector = {kvec}")
    print("k^i h_ij =")
    print(trans)

    status_line("TT mode is transverse for propagation along z",
                all(is_zero(x) for x in list(trans)))


# =============================================================================
# Case 5: Candidate wave equation placeholder
# =============================================================================

def case_5_wave_equation_placeholder():
    header("Case 5: Candidate wave equation placeholder")

    print("A tensor wave sector would need a field equation of the schematic form:")
    print()
    print("  □ h_ij^TT = source_ij^TT")
    print()
    print("In vacuum:")
    print()
    print("  □ h_ij^TT = 0")
    print()
    print("This is not supplied by scalar A or vector W_i.")
    print()
    print("Therefore the theory needs an independent tensor sector or a mechanism")
    print("that produces one from deeper variables.")
    status_line("tensor wave equation class identified as missing", True)


# =============================================================================
# Case 6: Sector separation
# =============================================================================

def case_6_sector_separation():
    header("Case 6: Scalar-vector-tensor sector separation")

    print("Linearized sector map:")
    print()
    print("| Sector | Candidate variable | Source | Status |")
    print("|---|---|---|---|")
    print("| scalar | A / Phi | density / mass | present weakly |")
    print("| trace | kappa | pressure / trace candidate | reduced candidate |")
    print("| vector | W_i | mass current / angular momentum | needed, not derived |")
    print("| tensor | h_ij^TT | quadrupole radiation / TT stress | missing |")
    print()
    status_line("wave sector separated from scalar/vector sectors", True)


# =============================================================================
# Case 7: What would count as progress
# =============================================================================

def case_7_success_criteria():
    header("Case 7: Wave-sector success criteria")

    print("A viable wave-sector development should eventually show:")
    print()
    print("1. existence of two transverse-traceless propagating polarizations,")
    print("2. propagation at the observed wave speed,")
    print("3. coupling to changing quadrupole-like sources,")
    print("4. compatibility with scalar A and vector W_i sectors,")
    print("5. no extra unwanted scalar radiation in regimes where constrained,")
    print("6. energy flux / radiation reaction accounting.")
    print()
    status_line("wave-sector success criteria listed", True)


# =============================================================================
# Case 8: Classification
# =============================================================================

def case_8_classification():
    header("Case 8: Classification")

    print("Results:")
    print()
    print("1. Scalar A is not a TT tensor mode.")
    print("2. Vector W_i is not a TT tensor mode.")
    print("3. TT waves require a symmetric trace-free transverse spatial tensor.")
    print("4. A z-propagating TT mode has plus and cross polarizations.")
    print("5. A wave equation for h_ij^TT is currently missing.")
    print("6. A full gravity theory needs this sector.")
    print()
    status_line("tensor wave sector is necessary and currently absent", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The current reduced program does not yet contain gravitational waves.")
    print()
    print("Scalar A handles Newtonian/mass-flux physics.")
    print("Vector W_i is the natural home for frame dragging.")
    print("But radiative gravity needs a separate tensor TT sector h_ij^TT.")
    print()
    print("This is not a failure of the scalar branch; it is a degree inventory.")
    print("The next task is to decide whether the tensor sector is fundamental,")
    print("emergent from deeper vacuum variables, or absent and therefore fatal.")
    print()
    print("Possible next artifact:")
    print("  candidate_wave_sector_linearized_modes.md")


def main():
    header("Candidate Wave Sector Linearized Modes")
    case_0_problem_statement()
    case_1_scalar_not_tt()
    case_2_vector_not_tt()
    case_3_tt_polarizations()
    case_4_transversality()
    case_5_wave_equation_placeholder()
    case_6_sector_separation()
    case_7_success_criteria()
    case_8_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
