# Group:
#   04_source_law_interior
#
# Script type:
#   DIAGNOSTIC
#
# Candidate compare GR interior Schwarzschild
#
# Purpose
# -------
# Compare the reduced constant-density interior A model to the exact GR
# interior Schwarzschild solution for a uniform-density sphere.
#
# This is a diagnostic comparison, not an attempt to derive GR.
#
# Reduced areal-flux interior:
#
#   A_red(r) = 1 - 4*pi*G*rho0*R^2/c^2 + 4*pi*G*rho0*r^2/(3*c^2)
#
# GR interior Schwarzschild lapse factor:
#
#   A_GR(r) = [1/4] [3 sqrt(1-r_s/R) - sqrt(1-r_s*r^2/R^3)]^2
#
# with:
#
#   r_s = 2GM/c^2
#   M = (4*pi/3) rho0 R^3
#
# Exterior boundary:
#   A_GR(R) = A_red(R) = 1-r_s/R
#
# Weak-field:
#   A_GR and A_red agree at first order in compactness.

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


def header(title: str) -> None:
    print()
    print("=" * 108)
    print(title)
    print("=" * 108)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def series(expr, var, order=3):
    return sp.series(expr, var, 0, order).removeO()


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="interior_A_boundary_matching",
        upstream_script_id="04_source_law_interior__candidate_interior_A_source_model",
        upstream_derivation_id="interior_A_boundary_matching",
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


def case_0_define_models(out: ScriptOutput):
    header("Case 0: Define reduced and GR interior models")

    x, u = sp.symbols("x u", real=True)

    # Dimensionless radius x=r/R.
    # Compactness u = r_s/R = 2GM/(c^2 R).
    A_red = 1 - sp.Rational(3, 2)*u + sp.Rational(1, 2)*u*x**2
    A_gr = sp.Rational(1, 4) * (3*sp.sqrt(1-u) - sp.sqrt(1-u*x**2))**2
    A_ext_boundary = 1 - u

    print("Dimensionless variables:")
    print("  x = r/R")
    print("  u = r_s/R = 2GM/(c^2 R)")
    print()
    print(f"A_red(x) = {A_red}")
    print(f"A_GR(x)  = {A_gr}")
    print(f"A_boundary = {A_ext_boundary}")

    red_at_1 = is_zero(A_red.subs(x, 1) - A_ext_boundary)
    gr_at_1 = is_zero(A_gr.subs(x, 1) - A_ext_boundary)

    with out.derived_results():
        out.line("both models match exterior A at x=1",
                 StatusMark.PASS if (red_at_1 and gr_at_1) else StatusMark.FAIL,
                 f"A_red(1)-A_ext={sp.simplify(A_red.subs(x,1)-A_ext_boundary)}; "
                 f"A_GR(1)-A_ext={sp.simplify(A_gr.subs(x,1)-A_ext_boundary)}")

    return x, u, A_red, A_gr


def case_1_boundary_derivatives(out: ScriptOutput, x, u, A_red, A_gr):
    header("Case 1: Boundary derivative comparison")

    d_red = sp.diff(A_red, x)
    d_gr = sp.simplify(sp.diff(A_gr, x))

    d_red_1 = sp.simplify(d_red.subs(x, 1))
    d_gr_1 = sp.simplify(d_gr.subs(x, 1))

    print(f"dA_red/dx = {d_red}")
    print(f"dA_GR/dx  = {d_gr}")
    print()
    print(f"dA_red/dx at x=1 = {d_red_1}")
    print(f"dA_GR/dx at x=1  = {d_gr_1}")

    residual = sp.simplify(d_red_1 - d_gr_1)
    ok = is_zero(residual)

    with out.derived_results():
        out.line("boundary derivatives match",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 f"dA_red/dx(1) - dA_GR/dx(1) = {residual}")


def case_2_weak_field_series(out: ScriptOutput, x, u, A_red, A_gr, ns=None):
    header("Case 2: Weak-field compactness series")

    A_gr_series = sp.simplify(series(A_gr, u, 3))
    A_red_series = sp.simplify(series(A_red, u, 3))
    diff_series = sp.simplify(series(A_gr - A_red, u, 3))

    print(f"A_red series = {A_red_series}")
    print(f"A_GR series  = {A_gr_series}")
    print(f"A_GR - A_red through u^2 = {diff_series}")

    first_order_diff = sp.simplify(series(A_gr - A_red, u, 2))
    second_order_diff = sp.simplify(series(A_gr - A_red, u, 3))

    first_order_ok = is_zero(first_order_diff)
    second_order_differs = not is_zero(second_order_diff)

    with out.derived_results():
        out.line("models agree through first order in compactness",
                 StatusMark.PASS if first_order_ok else StatusMark.FAIL,
                 f"first order diff = {first_order_diff}")
        out.line("models differ at second order",
                 StatusMark.PASS if second_order_differs else StatusMark.FAIL,
                 f"second order diff = {second_order_diff}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="gr_interior_first_order_match",
            inputs=[x, u],
            output=first_order_diff,
            method="gr_vs_reduced_interior_series",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="weak-field series through first order in compactness u",
            metadata={"second_order_difference": str(second_order_diff)},
        )


def case_3_residual_shape(out: ScriptOutput, x, u, A_red, A_gr):
    header("Case 3: Residual shape")

    residual = sp.simplify(A_gr - A_red)
    residual_series = sp.simplify(series(residual, u, 4))

    print(f"Residual exact = {residual}")
    print(f"Residual series through u^3 = {residual_series}")

    center_residual = sp.simplify(residual.subs(x, 0))
    boundary_residual = sp.simplify(residual.subs(x, 1))

    print()
    print(f"Residual at center x=0 = {center_residual}")
    print(f"Residual at boundary x=1 = {boundary_residual}")

    with out.derived_results():
        out.line("residual vanishes at boundary",
                 StatusMark.PASS if is_zero(boundary_residual) else StatusMark.FAIL,
                 f"residual(x=1) = {boundary_residual}")
        out.line("residual is generally nonzero inside",
                 StatusMark.PASS if not is_zero(center_residual) else StatusMark.FAIL,
                 f"residual(x=0) = {center_residual}")


def case_4_center_values(out: ScriptOutput, x, u, A_red, A_gr):
    header("Case 4: Center lapse comparison")

    A_red_0 = sp.simplify(A_red.subs(x, 0))
    A_gr_0 = sp.simplify(A_gr.subs(x, 0))

    print(f"A_red(0) = {A_red_0}")
    print(f"A_GR(0)  = {A_gr_0}")
    print()
    print(f"A_red(0) series = {series(A_red_0, u, 4)}")
    print(f"A_GR(0) series  = {series(A_gr_0, u, 4)}")
    print(f"center difference series = {series(A_gr_0 - A_red_0, u, 4)}")

    first_ok = is_zero(series(A_gr_0 - A_red_0, u, 2))
    higher_differs = not is_zero(series(A_gr_0 - A_red_0, u, 4))

    with out.derived_results():
        out.line("center values agree at first order",
                 StatusMark.PASS if first_ok else StatusMark.FAIL)
        out.line("center values differ beyond first order",
                 StatusMark.PASS if higher_differs else StatusMark.FAIL)


def case_5_B_comparison(out: ScriptOutput):
    header("Case 5: Radial metric comparison")

    x, u = sp.symbols("x u", real=True)

    A_red = 1 - sp.Rational(3, 2)*u + sp.Rational(1, 2)*u*x**2
    B_red = sp.simplify(1/A_red)

    # GR constant-density interior radial metric:
    B_gr = sp.simplify(1 / (1 - u*x**2))

    print(f"B_red = 1/A_red = {B_red}")
    print(f"B_GR  = {B_gr}")

    diff_series = sp.simplify(series(B_gr - B_red, u, 3))
    print(f"B_GR - B_red through u^2 = {diff_series}")

    differs_first = not is_zero(series(B_gr - B_red, u, 2))

    with out.derived_results():
        out.line("B differs already at first order generically",
                 StatusMark.PASS if differs_first else StatusMark.FAIL,
                 f"first order B diff = {series(B_gr - B_red, u, 2)}")

    print()
    print("Interpretation:")
    print("  Forcing kappa=0 inside gives B_red=1/A_red.")
    print("  GR interior does not generally have AB=1 inside matter.")


def case_6_kappa_gr_inside(out: ScriptOutput, ns=None):
    header("Case 6: GR interior kappa diagnostic")

    x, u = sp.symbols("x u", real=True)

    A_gr = sp.Rational(1, 4) * (3*sp.sqrt(1-u) - sp.sqrt(1-u*x**2))**2
    B_gr = 1 / (1 - u*x**2)

    AB_gr = sp.simplify(A_gr * B_gr)
    kappa_gr = sp.simplify(sp.Rational(1, 2) * sp.log(AB_gr))

    print(f"A_GR * B_GR = {AB_gr}")
    print(f"kappa_GR = 1/2 ln(A_GR B_GR) = {kappa_gr}")

    AB_boundary = sp.simplify(AB_gr.subs(x, 1))
    AB_series = sp.simplify(series(AB_gr, u, 3))

    print()
    print(f"A_GR B_GR at x=1 = {AB_boundary}")
    print(f"A_GR B_GR series = {AB_series}")

    ab_boundary_ok = is_zero(AB_boundary - 1)
    ab_not_unity_inside = not is_zero(AB_gr - 1)

    with out.derived_results():
        out.line("GR interior has AB=1 at boundary",
                 StatusMark.PASS if ab_boundary_ok else StatusMark.FAIL,
                 f"A_GR B_GR at x=1 = {AB_boundary}")
        out.line("GR interior does not generally have AB=1 inside",
                 StatusMark.PASS if ab_not_unity_inside else StatusMark.FAIL)

    if ns is not None:
        ns.record_derivation(
            derivation_id="gr_interior_kappa_diagnostic",
            inputs=[A_gr, B_gr, x, u],
            output=sp.simplify(AB_boundary - 1),
            method="kappa_GR = 1/2 ln(A_GR * B_GR)",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="GR constant-density interior, dimensionless",
        )

    with out.unresolved_obligations():
        out.line("derive interior kappa source from matter coupling",
                 StatusMark.OBLIGATION,
                 "GR interior has kappa!=0 inside matter; reduced model enforces kappa=0 by hand")


def final_interpretation():
    header("Final interpretation")

    print("The reduced interior A model and GR interior Schwarzschild agree")
    print("at the exterior boundary and at first weak-field order for A.")
    print()
    print("They differ at higher order inside the source.")
    print()
    print("The largest structural difference is that the reduced model, when")
    print("forced to kappa=0 inside, has B=1/A everywhere.")
    print()
    print("The GR interior Schwarzschild solution does not generally have AB=1")
    print("inside matter, although AB=1 is recovered at the exterior boundary.")
    print()
    print("Interpretation:")
    print("  kappa=0 may be an exterior/source-free condition, not an interior")
    print("  matter condition.")
    print()
    print("Possible next artifact:")
    print("  candidate_compare_gr_interior_schwarzschild.md")


def main():
    header("Candidate Compare GR Interior Schwarzschild")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    x, u, A_red, A_gr = case_0_define_models(out)
    case_1_boundary_derivatives(out, x, u, A_red, A_gr)
    case_2_weak_field_series(out, x, u, A_red, A_gr, ns)
    case_3_residual_shape(out, x, u, A_red, A_gr)
    case_4_center_values(out, x, u, A_red, A_gr)
    case_5_B_comparison(out)
    case_6_kappa_gr_inside(out, ns)
    final_interpretation()

    out.print_summary()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_interior_kappa_from_matter_coupling",
        script_id=SCRIPT_ID,
        title="Derive interior kappa source from matter coupling",
        status=ObligationStatus.OPEN,
        description=(
            "GR interior Schwarzschild has AB != 1 inside matter, implying "
            "kappa != 0. The reduced model enforces kappa=0 inside by hand. "
            "A mechanism or source law that produces interior kappa from "
            "matter coupling remains underived."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="reduced_interior_differs_from_gr_second_order",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "The reduced constant-density interior A model agrees with the GR "
            "interior Schwarzschild solution at the boundary and at first weak-field "
            "order, but differs at second order inside matter. The discrepancy is "
            "interior-supported and boundary-smooth."
        ),
        obligation_ids=["derive_interior_kappa_from_matter_coupling"],
    ))

    ns.write_run_metadata()

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
