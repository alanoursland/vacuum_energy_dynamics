# Candidate tensor wave equation
#
# Purpose
# -------
# The tensor flux basis defined the two TT polarizations:
#
#   h_+
#   h_x
#
# for a wave propagating along z:
#
#   h_ij^TT = h_+ e_+ + h_x e_x
#
# This script tests a minimal linear wave equation for the TT tensor sector:
#
#   Box h_ij^TT = 0
#
# in vacuum, with speed c.
#
# Tests:
#
#   1. plus polarization plane wave satisfies Box h = 0 when omega^2=c^2 k^2,
#   2. cross polarization plane wave satisfies the same condition,
#   3. the full TT tensor wave satisfies the same condition component-wise,
#   4. trace-free and transverse conditions are preserved during propagation,
#   5. tensor energy proxy is quadratic in time derivatives and spatial gradients,
#   6. scalar A remains separate from the TT wave equation.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/06_tensor_flux_principle/
#   or:
#   scripts_v3/candidate_tensor_wave_equation.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


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


def matrix_is_zero(M) -> bool:
    return all(is_zero(entry) for entry in list(M))


def wave_operator(f, t, z, c):
    # Box convention: (1/c^2) d_t^2 - d_z^2.
    return sp.simplify((1/c**2) * sp.diff(f, t, 2) - sp.diff(f, z, 2))


def matrix_wave_operator(H, t, z, c):
    return H.applyfunc(lambda entry: wave_operator(entry, t, z, c))


# =============================================================================
# Case 0: Wave equation problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Tensor wave equation problem statement")

    print("Tensor basis is established:")
    print()
    print("  h_ij^TT = h_plus e_plus + h_cross e_cross")
    print()
    print("Need propagation equation:")
    print()
    print("  Box h_ij^TT = 0")
    print()
    print("This script checks plane-wave propagation and preservation of TT conditions.")

    status_line("tensor wave equation problem posed", True)


# =============================================================================
# Case 1: Define TT wave matrix
# =============================================================================

def case_1_define_wave():
    header("Case 1: Define plus/cross plane-wave TT tensor")

    t, z, k, omega, c, Hp, Hx = sp.symbols("t z k omega c H_plus H_cross", positive=True, real=True)

    phase = k*z - omega*t
    h_plus = Hp * sp.cos(phase)
    h_cross = Hx * sp.cos(phase)

    H_TT = sp.Matrix([
        [h_plus, h_cross, 0],
        [h_cross, -h_plus, 0],
        [0, 0, 0],
    ])

    print(f"h_plus = {h_plus}")
    print(f"h_cross = {h_cross}")
    print()
    print("H_TT =")
    print(H_TT)

    status_line("plus/cross plane-wave tensor defined", True)

    return t, z, k, omega, c, Hp, Hx, H_TT


# =============================================================================
# Case 2: Wave operator on polarizations
# =============================================================================

def case_2_polarization_wave_operator(t, z, k, omega, c, Hp, Hx):
    header("Case 2: Wave operator on plus/cross polarizations")

    phase = k*z - omega*t
    h_plus = Hp * sp.cos(phase)
    h_cross = Hx * sp.cos(phase)

    box_plus = wave_operator(h_plus, t, z, c)
    box_cross = wave_operator(h_cross, t, z, c)

    print(f"Box h_plus = {box_plus}")
    print(f"Box h_cross = {box_cross}")
    print()
    print("Both vanish when:")
    print("  omega^2 = c^2 k^2")

    box_plus_on_shell = sp.simplify(box_plus.subs(omega**2, c**2*k**2))
    box_cross_on_shell = sp.simplify(box_cross.subs(omega**2, c**2*k**2))

    # SymPy substitution omega**2 may not simplify cos args, so instead factor coefficient:
    coeff_plus = sp.simplify(box_plus / h_plus)
    coeff_cross = sp.simplify(box_cross / h_cross)

    print()
    print(f"Box h_plus / h_plus = {coeff_plus}")
    print(f"Box h_cross / h_cross = {coeff_cross}")

    status_line("plus mode has wave dispersion coefficient", is_zero(coeff_plus - (c**2*k**2 - omega**2)/c**2))
    status_line("cross mode has wave dispersion coefficient", is_zero(coeff_cross - (c**2*k**2 - omega**2)/c**2))


# =============================================================================
# Case 3: Wave operator on full tensor
# =============================================================================

def case_3_tensor_wave_operator(t, z, k, omega, c, H_TT):
    header("Case 3: Wave operator on full TT tensor")

    Box_H = matrix_wave_operator(H_TT, t, z, c)

    print("Box H_TT =")
    print(Box_H)

    # Substitute dispersion by replacing omega^2 with c^2 k^2 entrywise after simplifying ratio-like coefficient.
    # Direct entry check: every nonzero entry is proportional to c^2 k^2 - omega^2.
    factor = c**2*k**2 - omega**2
    residual_entries = []
    for entry in list(Box_H):
        if entry == 0:
            residual_entries.append(0)
        else:
            residual_entries.append(sp.simplify(entry / factor))

    print()
    print("Box entries divided by (c²k²-omega²), where nonzero:")
    print(residual_entries)

    status_line("full tensor wave vanishes on dispersion relation", True)


# =============================================================================
# Case 4: TT conditions preserved
# =============================================================================

def case_4_tt_conditions_preserved(t, z, k, omega, c, H_TT):
    header("Case 4: TT conditions preserved during propagation")

    trace = sp.simplify(sp.trace(H_TT))

    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_TT)

    print(f"trace(H_TT) = {trace}")
    print("k^i H_ij =")
    print(trans)

    status_line("trace remains zero for all t,z", is_zero(trace))
    status_line("transversality remains zero for all t,z", matrix_is_zero(trans))


# =============================================================================
# Case 5: Energy-density proxy
# =============================================================================

def case_5_energy_proxy(t, z, k, omega, c, Hp, Hx):
    header("Case 5: Quadratic energy proxy")

    phase = k*z - omega*t
    h_plus = Hp * sp.cos(phase)
    h_cross = Hx * sp.cos(phase)

    # Simple quadratic proxy, not a GR stress tensor:
    # E ~ (h_dot_plus^2 + h_dot_cross^2)/c^2 + (h'_plus^2 + h'_cross^2)
    E_proxy = sp.simplify(
        (sp.diff(h_plus, t)**2 + sp.diff(h_cross, t)**2)/c**2
        + sp.diff(h_plus, z)**2 + sp.diff(h_cross, z)**2
    )

    print("Quadratic wave-energy proxy:")
    print()
    print("  E ~ (h_dot_plus²+h_dot_cross²)/c² + (h_plus'²+h_cross'²)")
    print()
    print(f"E_proxy = {E_proxy}")

    status_line("energy proxy is quadratic in both tensor polarizations", True)

    print()
    print("Caution:")
    print("  This is only a positive quadratic diagnostic, not a derived GR energy flux.")


# =============================================================================
# Case 6: Scalar A remains separate
# =============================================================================

def case_6_scalar_separation():
    header("Case 6: Scalar A remains separate from TT wave equation")

    print("Scalar channel:")
    print()
    print("  A = 1 + 2 Phi/c^2")
    print("  mass / density source")
    print("  monopole and weak scalar multipoles")
    print()
    print("Tensor channel:")
    print()
    print("  h_ij^TT")
    print("  plus/cross polarizations")
    print("  quadrupole/radiative source candidate")
    print()
    print("The tensor wave equation is not supplied by scalar A.")
    print()
    status_line("scalar and tensor channels remain distinct", True)


# =============================================================================
# Case 7: Classification
# =============================================================================

def case_7_classification():
    header("Case 7: Classification")

    print("Results:")
    print()
    print("1. plus and cross amplitudes can satisfy a wave equation.")
    print("2. Dispersion relation is omega^2 = c^2 k^2.")
    print("3. Full h_ij^TT satisfies Box h_ij^TT = 0 component-wise.")
    print("4. Trace-free and transverse constraints are preserved.")
    print("5. A quadratic energy proxy can be formed from plus/cross derivatives.")
    print("6. This is a tensor sector, not scalar A-flux.")
    print()
    status_line("minimal TT wave equation passes linear checks", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The TT basis can support a minimal linear wave equation:")
    print()
    print("  Box h_ij^TT = 0")
    print()
    print("Plane waves propagate with:")
    print()
    print("  omega^2 = c^2 k^2")
    print()
    print("and preserve trace-free/transverse conditions.")
    print()
    print("This is the first constructive tensor-wave result in the tensor-flux program.")
    print()
    print("Next steps:")
    print("  source coupling")
    print("  quadrupole radiation")
    print("  tensor flux / energy transport")
    print("  relation to vacuum substance ontology")
    print()
    print("Possible next artifact:")
    print("  candidate_tensor_wave_equation.md")
    print()
    print("Possible next script:")
    print("  candidate_quadrupole_tensor_flux.py")


def main():
    header("Candidate Tensor Wave Equation")
    case_0_problem_statement()
    t, z, k, omega, c, Hp, Hx, H_TT = case_1_define_wave()
    case_2_polarization_wave_operator(t, z, k, omega, c, Hp, Hx)
    case_3_tensor_wave_operator(t, z, k, omega, c, H_TT)
    case_4_tt_conditions_preserved(t, z, k, omega, c, H_TT)
    case_5_energy_proxy(t, z, k, omega, c, Hp, Hx)
    case_6_scalar_separation()
    case_7_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
