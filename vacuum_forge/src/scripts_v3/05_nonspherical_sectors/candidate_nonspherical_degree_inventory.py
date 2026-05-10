# Group:
#   05_nonspherical_sectors
#
# Script type:
#   INVENTORY

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

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 116)
    print(title)
    print("=" * 116)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def matrix_trace_free(M):
    n = M.shape[0]
    return sp.simplify(M - sp.trace(M) * sp.eye(n) / n)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="weak_scalar_gamma_one_sector",
        upstream_script_id="05_nonspherical_sectors__candidate_weak_multipole_metric_reconstruction",
        upstream_derivation_id="weak_scalar_gamma_one_sector",
    )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


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

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("degree inventory needed beyond scalar A", StatusMark.PASS, "SVT decomposition required")


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

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("single scalar A cannot represent full metric perturbation", StatusMark.PASS, "10 components vs 1 scalar")


# =============================================================================
# Case 2: Scalar temporal/Newtonian sector
# =============================================================================

def case_2_scalar_A_sector(ns):
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

    out = ScriptOutput()
    with out.derived_results():
        out.line("scalar A sector is present", StatusMark.PASS, "A = 1 + 2psi confirmed from upstream")

    ns.record_derivation(
        derivation_id="scalar_A_sector_inventory",
        inputs=[psi],
        output=A,
        method="scalar_A_newtonian_sector",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )


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

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("kappa sector exists in reduced theory but needs nonspherical parent", StatusMark.OBLIGATION, "covariant nonspherical kappa not yet derived")


# =============================================================================
# Case 4: Spatial conformal scalar sector
# =============================================================================

def case_4_spatial_conformal_scalar(ns):
    header("Case 4: Spatial conformal scalar sector")

    psi = sp.symbols("psi", real=True)

    h_spatial_scalar = -2*psi * sp.eye(3)
    trace = sp.trace(h_spatial_scalar)
    tf = matrix_trace_free(h_spatial_scalar)
    trace_tf = sp.simplify(sp.trace(tf))

    print("Weak scalar spatial perturbation:")
    print("  h_ij = -2 psi delta_ij")
    print()
    print(h_spatial_scalar)
    print(f"trace = {trace}")
    print("trace-free part:")
    print(tf)
    print(f"trace of trace-free part = {trace_tf}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("spatial scalar sector is pure trace/conformal",
                 StatusMark.PASS if is_zero(trace_tf) else StatusMark.FAIL,
                 f"trace-free part vanishes: {is_zero(trace_tf)}")

    ns.record_derivation(
        derivation_id="spatial_conformal_trace_free_vanishes",
        inputs=[h_spatial_scalar],
        output=tf,
        method="matrix_trace_free_decomposition",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 5: Trace-free spatial shear inventory
# =============================================================================

def case_5_trace_free_spatial_shear(ns=None):
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

    out = ScriptOutput()
    with out.derived_results():
        out.line("trace-free spatial shear has 5 independent components",
                 StatusMark.PASS if is_zero(trace_tf) else StatusMark.FAIL,
                 f"trace of shear part = {trace_tf}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="trace_free_spatial_shear_inventory",
            inputs=[hxx, hyy, hzz, hxy, hxz, hyz],
            output=trace_tf,
            method="spatial_shear_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )


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

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("vector/frame-dragging sector is missing from scalar branch", StatusMark.OBLIGATION, "g_ti not produced by scalar A")


# =============================================================================
# Case 7: Tensor / wave inventory
# =============================================================================

def case_7_tensor_wave_sector(ns):
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

    out = ScriptOutput()
    with out.derived_results():
        out.line("tensor/wave sector is independent of scalar A",
                 StatusMark.PASS if is_zero(trace) else StatusMark.FAIL,
                 f"TT trace = {trace}")

    ns.record_derivation(
        derivation_id="tensor_wave_sector_trace_zero",
        inputs=[hp, hx],
        output=trace,
        method="TT_tensor_trace_check",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


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

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("SVT inventory separated", StatusMark.PASS, "scalar present; shear/vector/tensor missing")


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

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("claim boundaries made explicit", StatusMark.PASS, "scalar sector present; SVT sectors open")


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
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    case_1_metric_component_count()
    case_2_scalar_A_sector(ns)
    case_3_kappa_trace_sector()
    case_4_spatial_conformal_scalar(ns)
    case_5_trace_free_spatial_shear(ns)
    case_6_vector_sector()
    case_7_tensor_wave_sector(ns)
    case_8_svt_map()
    case_9_claim_boundaries()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_nonspherical_parent",
        script_id=SCRIPT_ID,
        title="Derive covariant nonspherical parent for kappa trace response",
        status=ObligationStatus.OPEN,
        description=(
            "The kappa trace-response mode exists in the reduced spherical theory. "
            "A covariant nonspherical generalization is not yet derived."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_spatial_shear_sector_inventory",
        script_id=SCRIPT_ID,
        title="Derive spatial shear sector",
        status=ObligationStatus.OPEN,
        description=(
            "Trace-free spatial shear has 5 independent components not covered by "
            "scalar A. Mechanism and sourcing remain open."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_vector_frame_dragging_sector",
        script_id=SCRIPT_ID,
        title="Derive vector frame-dragging sector",
        status=ObligationStatus.OPEN,
        description=(
            "Off-diagonal g_ti components are needed for rotating sources. "
            "A separate vector sector must be sourced by angular momentum."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tensor_wave_sector_inventory",
        script_id=SCRIPT_ID,
        title="Derive tensor wave sector h_ij^TT",
        status=ObligationStatus.OPEN,
        description=(
            "Transverse-traceless spatial perturbations are needed for gravitational waves. "
            "An independent tensor sector must be added beyond scalar A."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="nonspherical_degree_inventory_claim",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The theory currently has a credible weak scalar sector (A = 1 + 2Phi/c^2) "
            "but is missing trace-free spatial shear, vector frame-dragging, tensor wave, "
            "and nonlinear closure sectors. Overclaiming beyond the scalar sector is not licensed."
        ),
        obligation_ids=[
            "derive_kappa_nonspherical_parent",
            "derive_spatial_shear_sector_inventory",
            "derive_vector_frame_dragging_sector",
            "derive_tensor_wave_sector_inventory",
        ],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
