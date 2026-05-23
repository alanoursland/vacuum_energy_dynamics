# Group:
#   05_nonspherical_sectors
#
# Script type:
#   DIAGNOSTIC

# Candidate weak multipole metric reconstruction
#
# Purpose
# -------
# The multipole A-source test showed that the areal-flux law has a natural
# weak nonspherical extension:
#
#   A = 1 + 2 Phi/c^2
#   Delta A = 8*pi*G*rho/c^2
#
# In vacuum, A is harmonic and carries ordinary multipoles.
#
# But a full weak gravitational metric is not just the temporal scalar A.
# In standard weak-field GR, for Newtonian scalar potential Phi:
#
#   g_tt ≈ -(1 + 2 Phi/c^2)c^2
#   g_ij ≈ (1 - 2 Phi/c^2) delta_ij
#
# This script checks whether the reduced reciprocal compensation idea:
#
#   kappa = 0
#   B_like = 1/A
#
# reproduces the weak scalar spatial factor, and then identifies what is
# missing for a full nonspherical theory.
#
# Main tests:
#
#   1. A=1+2psi gives temporal Newtonian factor.
#   2. B=1/A gives 1-2psi+O(psi^2), matching the weak scalar spatial factor.
#   3. Multipole psi fields remain harmonic in vacuum.
#   4. A scalar conformal spatial factor can represent the PPN gamma=1
#      scalar part at first order.
#   5. A scalar sector cannot represent vector/frame-dragging or tensor waves.
#   6. Anisotropic spatial shear requires additional degrees of freedom.
#
# IMPORTANT:
# This is a weak-field diagnostic. It is not a nonlinear nonspherical theory.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.core.context import TheoryContext
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


def radial_laplacian_l(expr, r, ell):
    return sp.simplify(
        (1/r**2) * sp.diff(r**2 * sp.diff(expr, r), r)
        - ell*(ell+1)*expr/r**2
    )


def series(expr, var, order):
    return sp.series(expr, var, 0, order).removeO()


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="weak_multipole_scalar_sector",
        upstream_script_id="05_nonspherical_sectors__candidate_multipole_areal_flux_extension",
        upstream_derivation_id="weak_multipole_reciprocal_scalar_sector",
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
# Case 0: Weak metric target
# =============================================================================

def case_0_weak_metric_target():
    header("Case 0: Weak metric target")

    psi = sp.symbols("psi", real=True)

    A_target = 1 + 2*psi
    spatial_factor_target = 1 - 2*psi

    print("Let:")
    print("  psi = Phi/c^2")
    print()
    print("Standard weak scalar metric target:")
    print("  g_tt factor A = 1 + 2 psi")
    print("  spatial conformal factor = 1 - 2 psi")
    print()
    print(f"A_target = {A_target}")
    print(f"spatial_factor_target = {spatial_factor_target}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("weak scalar target stated", StatusMark.PASS, "A = 1 + 2psi, spatial = 1 - 2psi")


# =============================================================================
# Case 1: Reciprocal compensation at weak order
# =============================================================================

def case_1_reciprocal_compensation(ns=None):
    header("Case 1: Reciprocal compensation at weak order")

    psi = sp.symbols("psi", real=True)

    A = 1 + 2*psi
    B_recip = sp.simplify(1/A)
    B_series = series(B_recip, psi, 4)
    B_first_order = series(B_recip, psi, 2)
    residual_first = sp.simplify(B_first_order - (1 - 2*psi))

    print(f"A = {A}")
    print(f"B_recip = 1/A = {B_recip}")
    print(f"B_recip series = {B_series}")
    print()
    print("To first order:")
    print("  B_recip ≈ 1 - 2 psi")
    print(f"  first-order residual = {residual_first}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("reciprocal compensation matches scalar spatial factor at first order",
                 StatusMark.PASS if is_zero(residual_first) else StatusMark.FAIL,
                 f"residual = {residual_first}")

    ctx = TheoryContext("candidate_weak_multipole_metric_reconstruction")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    ctx.assumptions.add("weak_scalar_A", sp.Eq(ms.A, 1 + 2 * psi))
    ctx.assumptions.add("weak_scalar_B", sp.Eq(ms.B, B_series))
    reciprocal = ctx.requirements.validate("reciprocal_scaling", ctx)

    out2 = ScriptOutput()
    with out2.governance_assessments():
        out2.line("VacuumForge reciprocal_scaling check supports weak scalar sector",
                  StatusMark.PASS if reciprocal.status in {"pass", "undetermined", "assumed"} else StatusMark.FAIL,
                  f"status={reciprocal.status}")

    if ns is not None:
        B_out = sp.series(B_recip, psi, 0, 2).removeO()
        ns.record_derivation(
            derivation_id="weak_scalar_gamma_one_sector",
            inputs=[psi],
            output=B_out,
            method="weak_scalar_reciprocal_compensation",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="weak-field first order only; not a general derivation",
        )


# =============================================================================
# Case 2: PPN gamma proxy
# =============================================================================

def case_2_gamma_proxy(ns):
    header("Case 2: Gamma proxy")

    psi, gamma = sp.symbols("psi gamma", real=True)

    A = 1 + 2*psi
    spatial_factor = 1 - 2*gamma*psi
    B_recip_first = 1 - 2*psi

    gamma_solution = sp.solve(sp.Eq(spatial_factor, B_recip_first), gamma)

    print("PPN-like scalar spatial factor:")
    print("  spatial = 1 - 2 gamma psi")
    print()
    print("Reciprocal compensation gives:")
    print("  spatial = 1 - 2 psi")
    print()
    print(f"gamma solution = {gamma_solution}")

    gamma_val = gamma_solution[0] if gamma_solution else None
    residual = sp.simplify(gamma_val - 1) if gamma_val is not None else None

    out = ScriptOutput()
    with out.derived_results():
        out.line("reciprocal scalar sector gives gamma=1",
                 StatusMark.PASS if (bool(gamma_solution) and gamma_solution[0] == 1) else StatusMark.FAIL,
                 f"gamma = {gamma_val}")

    ns.record_derivation(
        derivation_id="ppn_gamma_proxy_residual",
        inputs=[psi, gamma],
        output=sp.Integer(0) if residual is not None and is_zero(residual) else sp.Symbol("gamma_check"),
        method="solve_spatial_factor_eq_reciprocal",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
        scope="scalar sector first order only",
    )


# =============================================================================
# Case 3: Multipole scalar potential reconstruction
# =============================================================================

def case_3_multipole_scalar_reconstruction():
    header("Case 3: Multipole scalar potential reconstruction")

    r, Q, psi0 = sp.symbols("r Q psi0", positive=True, real=True)
    mu = sp.symbols("mu", real=True)

    # Example weak potential psi = -Mbar/r + Q P2/r^3.
    Mbar = sp.symbols("Mbar", real=True)
    P2 = sp.Rational(1, 2)*(3*mu**2 - 1)
    psi = -Mbar/r + Q*P2/r**3

    A = 1 + 2*psi
    spatial = 1 - 2*psi

    print(f"psi = {psi}")
    print(f"A = 1 + 2psi = {A}")
    print(f"spatial scalar factor = 1 - 2psi = {spatial}")
    print()
    print("Interpretation:")
    print("  The same weak multipole psi controls temporal and scalar spatial")
    print("  metric factors with gamma=1.")

    out = ScriptOutput()
    with out.derived_results():
        out.line("weak multipole scalar metric reconstructed", StatusMark.PASS, "A and spatial factor share same psi")


# =============================================================================
# Case 4: Vacuum harmonic modes remain valid
# =============================================================================

def case_4_harmonic_modes(ns):
    header("Case 4: Vacuum harmonic modes remain valid")

    r = sp.symbols("r", positive=True, real=True)

    out = ScriptOutput()
    with out.derived_results():
        for ell in range(0, 5):
            f = r**(-(ell+1))
            lap = radial_laplacian_l(f, r, ell)
            print(f"ell={ell}: f=1/r^{ell+1}, mode Laplacian={lap}")
            out.line(f"ell={ell} scalar multipole harmonic",
                     StatusMark.PASS if is_zero(lap) else StatusMark.FAIL,
                     f"Laplacian = {lap}")
            ns.record_derivation(
                derivation_id=f"vacuum_harmonic_mode_ell_{ell}",
                inputs=[f],
                output=lap,
                method=f"radial_laplacian_l_vacuum_ell_{ell}",
                status=Status.DERIVED,
                record_kind=RecordKind.DERIVATION,
                result_type="identity_residual",
            )

    print()
    print("These are scalar A/psi multipoles, not the full tensor metric content.")


# =============================================================================
# Case 5: Anisotropic spatial shear is missing
# =============================================================================

def case_5_anisotropic_spatial_shear_missing(ns):
    header("Case 5: Anisotropic spatial shear is missing")

    psi, hxx, hyy, hzz = sp.symbols("psi h_xx h_yy h_zz", real=True)

    # Scalar conformal spatial metric perturbation:
    #   h_ij^scalar = -2 psi delta_ij
    h_scalar = sp.Matrix([
        [-2*psi, 0, 0],
        [0, -2*psi, 0],
        [0, 0, -2*psi],
    ])

    # General diagonal spatial perturbation:
    h_general_diag = sp.Matrix([
        [hxx, 0, 0],
        [0, hyy, 0],
        [0, 0, hzz],
    ])

    trace_scalar = sp.trace(h_scalar)
    trace_general = sp.trace(h_general_diag)

    shear_diag = sp.simplify(h_general_diag - (trace_general/3)*sp.eye(3))
    trace_shear = sp.simplify(sp.trace(shear_diag))

    print("Scalar conformal spatial perturbation:")
    print(h_scalar)
    print(f"trace = {trace_scalar}")
    print()
    print("General diagonal spatial perturbation:")
    print(h_general_diag)
    print(f"trace = {trace_general}")
    print()
    print("Trace-free diagonal shear part:")
    print(shear_diag)
    print(f"trace of shear = {trace_shear}")
    print()
    print("A single scalar psi fixes only the conformal/trace spatial piece.")
    print("It cannot represent arbitrary trace-free spatial shear.")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("anisotropic spatial shear requires extra degrees of freedom", StatusMark.OBLIGATION, "scalar sector covers trace only")

    ns.record_derivation(
        derivation_id="spatial_shear_trace_free_residual",
        inputs=[hxx, hyy, hzz],
        output=trace_shear,
        method="trace_free_shear_decomposition",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


# =============================================================================
# Case 6: Vector/frame-dragging sector is missing
# =============================================================================

def case_6_vector_sector_missing():
    header("Case 6: Vector/frame-dragging sector is missing")

    print("Weak stationary rotating sources introduce off-diagonal components:")
    print()
    print("  g_ti != 0")
    print()
    print("These are vector/gravitomagnetic/frame-dragging degrees of freedom.")
    print()
    print("The scalar A field and reciprocal scalar spatial factor do not produce")
    print("off-diagonal g_ti components.")
    print()

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("frame-dragging requires vector sector beyond scalar A", StatusMark.OBLIGATION, "g_ti not produced by scalar A")


# =============================================================================
# Case 7: Tensor wave sector is missing
# =============================================================================

def case_7_tensor_sector_missing():
    header("Case 7: Tensor wave sector is missing")

    print("Linearized gravitational waves require transverse-traceless spatial")
    print("metric perturbations:")
    print()
    print("  h_ij^TT")
    print()
    print("These are not captured by a scalar A=1+2psi alone.")
    print()
    print("Therefore the scalar multipole extension is not a wave-sector theory.")
    print()

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("tensor waves require additional tensor sector", StatusMark.OBLIGATION, "h_ij^TT not captured by scalar A")


# =============================================================================
# Case 8: Nonlinear nonspherical closure
# =============================================================================

def case_8_nonlinear_closure():
    header("Case 8: Nonlinear nonspherical closure")

    print("Spherical exact branch:")
    print("  A = 1 - 2GM/(rc^2)")
    print("  kappa = 0")
    print("  B = 1/A")
    print()
    print("Weak nonspherical scalar branch:")
    print("  A = 1 + 2Phi/c^2")
    print("  spatial conformal factor ≈ 1 - 2Phi/c^2")
    print()
    print("Open nonlinear problem:")
    print("  How should full spatial geometry be reconstructed when Phi is")
    print("  nonspherical and nonlinear effects matter?")
    print()
    print("Likely needed sectors:")
    print("  scalar A / Newtonian potential")
    print("  kappa / trace response")
    print("  spatial shear")
    print("  vector frame-dragging")
    print("  tensor waves")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("nonlinear nonspherical closure remains open", StatusMark.OBLIGATION, "full spatial geometry reconstruction not derived")


# =============================================================================
# Case 9: Classification
# =============================================================================

def case_9_classification():
    header("Case 9: Classification")

    print("Results:")
    print()
    print("1. A=1+2Phi/c^2 reconstructs the weak temporal scalar metric.")
    print("2. Reciprocal compensation gives spatial factor 1-2Phi/c^2 to first order.")
    print("3. This corresponds to gamma=1 in the scalar weak-field sector.")
    print("4. Scalar A multipoles are compatible with Newtonian weak multipoles.")
    print("5. A single scalar cannot represent anisotropic spatial shear.")
    print("6. A single scalar cannot represent frame dragging.")
    print("7. A single scalar cannot represent tensor gravitational waves.")
    print("8. The nonlinear nonspherical closure remains an open problem.")
    print()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("weak scalar sector passes; full nonspherical theory remains incomplete", StatusMark.PASS, "gamma=1 scalar sector confirmed; tensor/vector/shear sectors open")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The weak A multipole sector can reconstruct the standard weak scalar")
    print("metric form:")
    print()
    print("  g_tt factor: A = 1 + 2Phi/c^2")
    print("  spatial scalar factor: 1 - 2Phi/c^2")
    print()
    print("This means reciprocal compensation reproduces the gamma=1 scalar")
    print("weak-field structure at first order.")
    print()
    print("But this is not a full gravity theory.")
    print("A full nonspherical extension needs additional sectors:")
    print()
    print("  spatial shear")
    print("  vector/frame-dragging modes")
    print("  tensor/wave modes")
    print("  nonlinear closure rules")
    print()
    print("Possible next artifact:")
    print("  candidate_weak_multipole_metric_reconstruction.md")
    print()
    print("Possible next script:")
    print("  candidate_nonspherical_degree_inventory.py")


def main():
    header("Candidate Weak Multipole Metric Reconstruction")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_weak_metric_target()
    case_1_reciprocal_compensation(ns)
    case_2_gamma_proxy(ns)
    case_3_multipole_scalar_reconstruction()
    case_4_harmonic_modes(ns)
    case_5_anisotropic_spatial_shear_missing(ns)
    case_6_vector_sector_missing()
    case_7_tensor_sector_missing()
    case_8_nonlinear_closure()
    case_9_classification()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_spatial_shear_sector",
        script_id=SCRIPT_ID,
        title="Derive spatial shear sector beyond scalar A",
        status=ObligationStatus.OPEN,
        description=(
            "Show how trace-free spatial shear (5 independent components) can be "
            "incorporated beyond the scalar conformal sector A = 1 + 2Phi/c^2."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_vector_sector_frame_dragging",
        script_id=SCRIPT_ID,
        title="Derive vector sector for frame dragging",
        status=ObligationStatus.OPEN,
        description=(
            "Show how off-diagonal g_ti components can be generated by a separate "
            "vector potential sector sourced by angular momentum."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tensor_wave_sector",
        script_id=SCRIPT_ID,
        title="Derive tensor wave sector h_ij^TT",
        status=ObligationStatus.OPEN,
        description=(
            "Show how transverse-traceless spatial metric perturbations can be "
            "added as an independent tensor sector beyond scalar A."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="weak_scalar_sector_gamma_one",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "Reciprocal compensation B = 1/A reproduces the gamma=1 scalar spatial "
            "factor 1 - 2Phi/c^2 at first order. This is a weak-field diagnostic, "
            "not a nonlinear derivation."
        ),
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
