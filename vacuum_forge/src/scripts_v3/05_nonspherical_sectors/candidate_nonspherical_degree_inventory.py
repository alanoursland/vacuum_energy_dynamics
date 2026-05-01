# Candidate nonspherical degree inventory
#
# Purpose
# -------
# The weak multipole metric reconstruction showed:
#
#   A = 1 + 2 Phi/c^2
#
# reconstructs the weak temporal scalar metric, and reciprocal compensation
# gives the scalar spatial factor:
#
#   spatial ≈ 1 - 2 Phi/c^2
#
# at first order.
#
# But that scalar sector is not a full nonspherical gravity theory.
#
# This script inventories the degrees of freedom needed beyond scalar A:
#
#   1. scalar A / Newtonian potential,
#   2. kappa / trace-response mode,
#   3. scalar spatial conformal mode,
#   4. trace-free spatial shear,
#   5. vector / frame-dragging sector,
#   6. tensor / wave sector,
#   7. nonlinear closure rules.
#
# Goal:
#   Prevent overclaiming. Identify what has been covered and what remains open.
#
# Suggested location:
#   scripts_v3/candidate_nonspherical_degree_inventory.py

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


def matrix_trace_free(M):
    n = M.shape[0]
    return sp.simplify(M - sp.trace(M) * sp.eye(n) / n)


# =============================================================================
# Case 0: Inventory problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Inventory problem statement")

    print("Known weak scalar success:")
    print()
    print("  A = 1 + 2 Phi/c^2")
    print("  spatial scalar factor ≈ 1 - 2 Phi/c^2")
    print()
    print("This captures the Newtonian scalar / PPN gamma=1 sector.")
    print()
    print("But nonspherical gravity also needs:")
    print("  trace response")
    print("  trace-free spatial shear")
    print("  vector/frame-dragging modes")
    print("  tensor/wave modes")
    print("  nonlinear closure")
    print()
    status_line("degree inventory needed beyond scalar A", True)


# =============================================================================
# Case 1: Symmetric metric perturbation count
# =============================================================================

def case_1_metric_component_count():
    header("Case 1: Metric component count")

    print("A symmetric 4D metric has 10 components:")
    print()
    print("  g_tt: 1")
    print("  g_ti: 3")
    print("  g_ij symmetric spatial: 6")
    print()
    print("Coordinate/gauge freedom removes 4 functions in a covariant theory,")
    print("but reduced sector variables must still account for the physical")
    print("scalar/vector/tensor structures.")
    print()
    print("Scalar A covers only one temporal scalar component.")
    print()
    status_line("single scalar A cannot represent full metric perturbation", True)


# =============================================================================
# Case 2: Scalar temporal/Newtonian sector
# =============================================================================

def case_2_scalar_A_sector():
    header("Case 2: Scalar A / Newtonian sector")

    psi = sp.symbols("psi", real=True)

    A = 1 + 2*psi

    print("Let psi = Phi/c^2.")
    print()
    print(f"A = {A}")
    print()
    print("This controls:")
    print("  g_tt weak scalar/Newtonian potential")
    print("  ordinary weak multipoles through Phi")
    print()
    status_line("scalar A sector is present", True)


# =============================================================================
# Case 3: Kappa trace response sector
# =============================================================================

def case_3_kappa_trace_sector():
    header("Case 3: Kappa / trace-response sector")

    a, b, kappa, s = sp.symbols("a b kappa s", real=True)

    kappa_expr = (a + b) / 2
    s_expr = (a - b) / 2

    print("Reduced spherical log variables:")
    print()
    print("  a = ln A")
    print("  b = ln B")
    print("  kappa = (a+b)/2")
    print("  s = (a-b)/2")
    print()
    print(f"kappa = {kappa_expr}")
    print(f"s = {s_expr}")
    print()
    print("Known status:")
    print("  exterior source-free branch suppresses kappa")
    print("  matter interiors may source kappa")
    print("  kappa is not yet generalized covariantly for nonspherical fields")
    print()
    status_line("kappa sector exists in reduced theory but needs nonspherical parent", True)


# =============================================================================
# Case 4: Spatial conformal scalar sector
# =============================================================================

def case_4_spatial_conformal_scalar():
    header("Case 4: Spatial conformal scalar sector")

    psi = sp.symbols("psi", real=True)

    h_spatial_scalar = -2*psi * sp.eye(3)
    trace = sp.trace(h_spatial_scalar)
    tf = matrix_trace_free(h_spatial_scalar)

    print("Weak scalar spatial perturbation:")
    print("  h_ij = -2 psi delta_ij")
    print()
    print(h_spatial_scalar)
    print(f"trace = {trace}")
    print("trace-free part:")
    print(tf)

    status_line("spatial scalar sector is pure trace/conformal", is_zero(tf))


# =============================================================================
# Case 5: Trace-free spatial shear inventory
# =============================================================================

def case_5_trace_free_spatial_shear():
    header("Case 5: Trace-free spatial shear sector")

    hxx, hyy, hzz, hxy, hxz, hyz = sp.symbols("h_xx h_yy h_zz h_xy h_xz h_yz", real=True)

    H = sp.Matrix([
        [hxx, hxy, hxz],
        [hxy, hyy, hyz],
        [hxz, hyz, hzz],
    ])

    H_tf = matrix_trace_free(H)
    trace_tf = sp.simplify(sp.trace(H_tf))

    print("General symmetric spatial perturbation h_ij:")
    print(H)
    print()
    print("Trace-free spatial shear part:")
    print(H_tf)
    print(f"trace of shear part = {trace_tf}")
    print()
    print("A scalar conformal factor cannot represent these 5 trace-free")
    print("spatial degrees of freedom.")
    print()
    status_line("trace-free spatial shear has 5 independent components", is_zero(trace_tf))


# =============================================================================
# Case 6: Vector / frame-dragging inventory
# =============================================================================

def case_6_vector_sector():
    header("Case 6: Vector / frame-dragging sector")

    Vx, Vy, Vz = sp.symbols("V_x V_y V_z", real=True)

    g_ti = sp.Matrix([[Vx, Vy, Vz]])

    print("Weak vector sector appears in off-diagonal components:")
    print()
    print("  g_ti")
    print()
    print(g_ti)
    print()
    print("This sector is needed for:")
    print("  rotating sources")
    print("  gravitomagnetic effects")
    print("  frame dragging")
    print()
    print("Scalar A and scalar reciprocal compensation do not produce g_ti.")
    print()
    status_line("vector/frame-dragging sector is missing from scalar branch", True)


# =============================================================================
# Case 7: Tensor / wave inventory
# =============================================================================

def case_7_tensor_wave_sector():
    header("Case 7: Tensor / wave sector")

    hp, hx = sp.symbols("h_plus h_cross", real=True)

    # Example TT wave propagating in z direction.
    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_TT)

    print("Example transverse-traceless tensor perturbation:")
    print()
    print(H_TT)
    print(f"trace = {trace}")
    print()
    print("This sector is needed for:")
    print("  gravitational waves")
    print("  radiative tensor degrees of freedom")
    print()
    print("It is not represented by scalar A.")
    print()
    status_line("tensor/wave sector is independent of scalar A", is_zero(trace))


# =============================================================================
# Case 8: Scalar-vector-tensor decomposition map
# =============================================================================

def case_8_svt_map():
    header("Case 8: Scalar-vector-tensor map")

    print("Weak-field sector inventory:")
    print()
    print("| Sector | Current status | Needed for |")
    print("|---|---|---|")
    print("| scalar A / Phi | present | Newtonian potential, weak multipoles |")
    print("| scalar spatial conformal | present at first order via reciprocal compensation | gamma=1 scalar spatial metric |")
    print("| kappa trace response | reduced/interior candidate | matter trace/interior deviation |")
    print("| spatial shear | missing | anisotropic spatial geometry |")
    print("| vector g_ti | missing | frame dragging / rotation |")
    print("| tensor TT | missing | gravitational waves |")
    print("| nonlinear closure | missing | strong nonspherical gravity |")
    print()
    status_line("SVT inventory separated", True)


# =============================================================================
# Case 9: What current program can and cannot claim
# =============================================================================

def case_9_claim_boundaries():
    header("Case 9: Claim boundaries")

    print("Currently supported claims:")
    print()
    print("1. Static spherical exterior recovery works in the reduced sector.")
    print("2. Weak scalar multipoles are compatible with A=1+2Phi/c^2.")
    print("3. Reciprocal compensation gives gamma=1 scalar spatial factor at first order.")
    print("4. Interior kappa response is plausible and boundary-contained.")
    print()
    print("Not yet supported:")
    print()
    print("1. Full nonlinear nonspherical metric reconstruction.")
    print("2. Frame-dragging.")
    print("3. Gravitational waves.")
    print("4. Complete covariant field equations.")
    print("5. Full matter stress-energy coupling.")
    print()
    status_line("claim boundaries made explicit", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The nonspherical degree inventory shows that the theory currently has")
    print("a credible weak scalar sector, but not a full nonspherical gravity sector.")
    print()
    print("Present:")
    print("  scalar A / Newtonian potential")
    print("  first-order scalar spatial compensation")
    print("  reduced kappa trace-response candidate")
    print()
    print("Missing:")
    print("  trace-free spatial shear")
    print("  vector/frame-dragging modes")
    print("  tensor/wave modes")
    print("  nonlinear nonspherical closure")
    print()
    print("Possible next artifact:")
    print("  candidate_nonspherical_degree_inventory.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_sector_frame_dragging.py")


def main():
    header("Candidate Nonspherical Degree Inventory")
    case_0_problem_statement()
    case_1_metric_component_count()
    case_2_scalar_A_sector()
    case_3_kappa_trace_sector()
    case_4_spatial_conformal_scalar()
    case_5_trace_free_spatial_shear()
    case_6_vector_sector()
    case_7_tensor_wave_sector()
    case_8_svt_map()
    case_9_claim_boundaries()
    final_interpretation()


if __name__ == "__main__":
    main()
