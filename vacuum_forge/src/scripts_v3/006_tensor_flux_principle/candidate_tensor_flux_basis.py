# Group:
#   06_tensor_flux_principle
#
# Script type:
#   DERIVATION

# Candidate tensor flux basis
#
# Purpose
# -------
# The scalar-flux no-wave failure control showed that scalar A-flux cannot
# produce gravitational waves. Tensor radiation requires an independent
# transverse-traceless spatial tensor:
#
#   h_ij^TT
#
# This script defines the minimal tensor basis for the next tensor-flux
# development stage.
#
# Tests:
#
#   1. plus and cross basis tensors are trace-free,
#   2. plus and cross basis tensors are transverse for propagation along z,
#   3. plus and cross are linearly independent,
#   4. a general TT wave has two polarizations,
#   5. scalar breathing mode is orthogonal/distinct from TT basis,
#   6. TT projection removes trace/longitudinal content for z-propagating waves.

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
    RouteRecord,
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
    print("=" * 120)
    print(title)
    print("=" * 120)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="scalar_flux_not_tt_guardrail",
        upstream_script_id="06_tensor_flux_principle__candidate_scalar_flux_no_wave_failure_control",
        upstream_derivation_id="scalar_flux_not_tt_guardrail",
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


def matrix_is_zero(M) -> bool:
    return all(is_zero(entry) for entry in list(M))


def inner(A, B):
    # Frobenius inner product for spatial tensors.
    return sp.simplify(sum(A[i, j] * B[i, j] for i in range(3) for j in range(3)))


# =============================================================================
# Case 0: Tensor basis problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Tensor basis problem statement")

    print("Scalar A-flux cannot be the wave sector.")
    print()
    print("Need a tensor channel:")
    print()
    print("  h_ij^TT")
    print("  trace-free")
    print("  transverse")
    print("  two polarizations")
    print()
    print("This script defines the plus/cross TT basis for propagation along z.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("tensor flux basis problem posed", StatusMark.PASS, "TT basis construction starting")


# =============================================================================
# Case 1: Define plus and cross basis
# =============================================================================

def case_1_define_basis():
    header("Case 1: Define plus and cross basis tensors")

    e_plus = sp.Matrix([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 0],
    ])

    e_cross = sp.Matrix([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ])

    print("e_plus =")
    print(e_plus)
    print()
    print("e_cross =")
    print(e_cross)

    out = ScriptOutput()
    with out.derived_results():
        out.line("plus and cross basis tensors defined", StatusMark.PASS, "e_plus = diag(1,-1,0); e_cross = sym off-diag xy")

    return e_plus, e_cross


# =============================================================================
# Case 2: Trace-free checks
# =============================================================================

def case_2_trace_free(e_plus, e_cross, ns):
    header("Case 2: Trace-free checks")

    tr_plus = sp.trace(e_plus)
    tr_cross = sp.trace(e_cross)

    print(f"Tr(e_plus) = {tr_plus}")
    print(f"Tr(e_cross) = {tr_cross}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("plus basis is trace-free",
                 StatusMark.PASS if is_zero(tr_plus) else StatusMark.FAIL,
                 f"Tr(e_plus) = {tr_plus}")
        out.line("cross basis is trace-free",
                 StatusMark.PASS if is_zero(tr_cross) else StatusMark.FAIL,
                 f"Tr(e_cross) = {tr_cross}")

    ns.record_derivation(
        derivation_id="tt_basis_trace_free_plus",
        inputs=[e_plus],
        output=tr_plus,
        method="trace_of_e_plus",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )
    ns.record_derivation(
        derivation_id="tt_basis_trace_free_cross",
        inputs=[e_cross],
        output=tr_cross,
        method="trace_of_e_cross",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 3: Transversality checks
# =============================================================================

def case_3_transverse(e_plus, e_cross, ns):
    header("Case 3: Transversality checks for propagation along z")

    k = sp.symbols("k", real=True)
    kvec = sp.Matrix([0, 0, k])

    trans_plus = sp.simplify(kvec.T * e_plus)
    trans_cross = sp.simplify(kvec.T * e_cross)

    print(f"k vector = {kvec}")
    print()
    print("k^i e_plus_ij =")
    print(trans_plus)
    print()
    print("k^i e_cross_ij =")
    print(trans_cross)

    out = ScriptOutput()
    with out.derived_results():
        out.line("plus basis is transverse",
                 StatusMark.PASS if matrix_is_zero(trans_plus) else StatusMark.FAIL,
                 f"k^i e_plus = {trans_plus}")
        out.line("cross basis is transverse",
                 StatusMark.PASS if matrix_is_zero(trans_cross) else StatusMark.FAIL,
                 f"k^i e_cross = {trans_cross}")

    ns.record_derivation(
        derivation_id="tt_basis_transversality_plus",
        inputs=[kvec, e_plus],
        output=trans_plus,
        method="transversality_check_e_plus",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )
    ns.record_derivation(
        derivation_id="tt_basis_transversality_cross",
        inputs=[kvec, e_cross],
        output=trans_cross,
        method="transversality_check_e_cross",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 4: Basis inner products
# =============================================================================

def case_4_inner_products(e_plus, e_cross, ns):
    header("Case 4: Basis inner products")

    pp = inner(e_plus, e_plus)
    cc = inner(e_cross, e_cross)
    pc = inner(e_plus, e_cross)

    print(f"<plus, plus> = {pp}")
    print(f"<cross, cross> = {cc}")
    print(f"<plus, cross> = {pc}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("plus and cross are nonzero",
                 StatusMark.PASS if not is_zero(pp) and not is_zero(cc) else StatusMark.FAIL,
                 f"<+,+>={pp}, <x,x>={cc}")
        out.line("plus and cross are orthogonal",
                 StatusMark.PASS if is_zero(pc) else StatusMark.FAIL,
                 f"<+,x>={pc}")

    ns.record_derivation(
        derivation_id="tt_basis_orthogonality_residual",
        inputs=[e_plus, e_cross],
        output=pc,
        method="frobenius_inner_product_plus_cross",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 5: General TT wave from basis
# =============================================================================

def case_5_general_tt_wave(e_plus, e_cross, ns):
    header("Case 5: General TT wave from plus/cross basis")

    hp, hx = sp.symbols("h_plus h_cross", real=True)

    H_TT = sp.simplify(hp * e_plus + hx * e_cross)
    trace_tt = sp.trace(H_TT)

    print("H_TT = h_plus e_plus + h_cross e_cross =")
    print(H_TT)
    print()
    print(f"trace = {trace_tt}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("general basis combination is trace-free",
                 StatusMark.PASS if is_zero(trace_tt) else StatusMark.FAIL,
                 f"trace = {trace_tt}")
        out.line("general basis combination has two amplitudes", StatusMark.PASS, "h_plus and h_cross are free parameters")

    ns.record_derivation(
        derivation_id="general_tt_wave_trace_zero",
        inputs=[hp, hx, e_plus, e_cross],
        output=trace_tt,
        method="linear_combination_tt_basis_trace",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 6: Scalar breathing mode is distinct
# =============================================================================

def case_6_breathing_distinct(e_plus, e_cross, ns):
    header("Case 6: Scalar breathing mode is distinct from TT basis")

    b = sp.symbols("b", real=True)

    H_breathing = sp.Matrix([
        [b, 0, 0],
        [0, b, 0],
        [0, 0, 0],
    ])

    tr_b = sp.trace(H_breathing)
    ip_plus = inner(H_breathing, e_plus)
    ip_cross = inner(H_breathing, e_cross)

    print("Breathing mode =")
    print(H_breathing)
    print()
    print(f"trace = {tr_b}")
    print(f"<breathing, plus> = {ip_plus}")
    print(f"<breathing, cross> = {ip_cross}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("breathing mode is not traceless unless trivial",
                 StatusMark.PASS if not is_zero(tr_b) else StatusMark.FAIL,
                 f"trace = {tr_b}")
        out.line("breathing mode is distinct from TT basis",
                 StatusMark.PASS if is_zero(ip_plus) and is_zero(ip_cross) else StatusMark.FAIL,
                 f"<b,+>={ip_plus}, <b,x>={ip_cross}")

    ns.record_derivation(
        derivation_id="breathing_orthogonal_to_tt_basis",
        inputs=[H_breathing, e_plus, e_cross],
        output=sp.Matrix([ip_plus, ip_cross]),
        method="frobenius_inner_product_breathing_vs_tt",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 7: TT projection for z propagation
# =============================================================================

def case_7_tt_projection_z(ns):
    header("Case 7: TT projection for z-propagating spatial tensor")

    hxx, hyy, hzz, hxy, hxz, hyz = sp.symbols("h_xx h_yy h_zz h_xy h_xz h_yz", real=True)

    H = sp.Matrix([
        [hxx, hxy, hxz],
        [hxy, hyy, hyz],
        [hxz, hyz, hzz],
    ])

    # For propagation along z, transverse projection keeps x/y block and removes z components.
    H_transverse = sp.Matrix([
        [hxx, hxy, 0],
        [hxy, hyy, 0],
        [0, 0, 0],
    ])

    # Remove trace in transverse 2-plane.
    trace_2 = hxx + hyy
    H_TT_z = sp.Matrix([
        [hxx - trace_2 / 2, hxy, 0],
        [hxy, hyy - trace_2 / 2, 0],
        [0, 0, 0],
    ])

    trace_tt_z = sp.simplify(sp.trace(H_TT_z))

    print("General symmetric spatial tensor:")
    print(H)
    print()
    print("Transverse x/y block:")
    print(H_transverse)
    print()
    print("TT projection for z propagation:")
    print(H_TT_z)
    print()
    print(f"trace = {trace_tt_z}")

    k = sp.symbols("k", real=True)
    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_TT_z)

    print("k^i H_TT_ij =")
    print(trans)

    out = ScriptOutput()
    with out.derived_results():
        out.line("z-TT projection is trace-free",
                 StatusMark.PASS if is_zero(trace_tt_z) else StatusMark.FAIL,
                 f"trace = {trace_tt_z}")
        out.line("z-TT projection is transverse",
                 StatusMark.PASS if matrix_is_zero(trans) else StatusMark.FAIL,
                 f"k^i H_TT = {trans}")

    ns.record_derivation(
        derivation_id="tt_projection_z_trace_free_transverse",
        inputs=[H],
        output=sp.Matrix([trace_tt_z, trans[0], trans[1], trans[2]]),
        method="TT_projection_z_propagation",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 8: Tensor flux channel interpretation
# =============================================================================

def case_8_tensor_flux_interpretation():
    header("Case 8: Tensor flux channel interpretation")

    print("Interpretation:")
    print()
    print("  A-flux is scalar / monopole flow.")
    print("  h_ij^TT is tensor / quadrupole radiative flow.")
    print()
    print("The TT basis supplies the two polarizations needed for the tensor channel.")
    print()
    print("Next steps:")
    print("  add a wave equation")
    print("  add propagation speed")
    print("  add quadrupole source coupling")
    print("  define tensor-flux conservation/radiation law")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("tensor flux channel basis established", StatusMark.PASS, "TT basis: trace-free, transverse, two polarizations")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The plus/cross TT basis gives the minimal tensor object needed for")
    print("a gravitational-wave sector.")
    print()
    print("For propagation along z:")
    print()
    print("  e_plus  = diag(1,-1,0)")
    print("  e_cross = off-diagonal xy symmetric mode")
    print()
    print("Both are trace-free and transverse.")
    print("Their linear combination gives h_ij^TT with two polarizations.")
    print()
    print("This begins the tensor-flux program:")
    print()
    print("  scalar A-flux -> monopole channel")
    print("  tensor TT flux -> quadrupole radiative channel")
    print()
    print("Possible next artifact:")
    print("  candidate_tensor_flux_basis.md")
    print()
    print("Possible next script:")
    print("  candidate_tensor_wave_equation.py")


def main():
    header("Candidate Tensor Flux Basis")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    e_plus, e_cross = case_1_define_basis()
    case_2_trace_free(e_plus, e_cross, ns)
    case_3_transverse(e_plus, e_cross, ns)
    case_4_inner_products(e_plus, e_cross, ns)
    case_5_general_tt_wave(e_plus, e_cross, ns)
    case_6_breathing_distinct(e_plus, e_cross, ns)
    case_7_tt_projection_z(ns)
    case_8_tensor_flux_interpretation()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tensor_wave_equation_from_basis",
        script_id=SCRIPT_ID,
        title="Derive tensor wave equation from TT basis",
        status=ObligationStatus.OPEN,
        description=(
            "The TT basis is established. A field equation Box h_ij^TT = source must "
            "be added to give the basis physical propagation."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="tt_basis_established_claim",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "The plus/cross TT basis is trace-free, transverse, and orthogonal for "
            "propagation along z. It supplies the two polarizations needed for a "
            "tensor-flux gravitational-wave channel."
        ),
        obligation_ids=["derive_tensor_wave_equation_from_basis"],
    ))

    ns.record_route(RouteRecord(
        route_id="tensor_tt_flux_basis_route",
        script_id=SCRIPT_ID,
        name="Tensor TT flux channel via plus/cross basis",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_tensor_wave_equation_from_basis"],
        activation_conditions=[
            "e_plus and e_cross are trace-free and transverse",
            "basis is orthogonal",
            "wave equation is added",
        ],
    ))

    ns.record_derivation(
        derivation_id="tensor_tt_basis_marker",
        inputs=[],
        output=sp.Symbol("tt_basis_established"),
        method="tensor_tt_basis_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
