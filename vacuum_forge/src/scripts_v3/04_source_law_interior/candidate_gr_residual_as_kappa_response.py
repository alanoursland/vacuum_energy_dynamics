# Group:
#   04_source_law_interior
#
# Script type:
#   DIAGNOSTIC
#
# Candidate GR residual as kappa response
#
# Purpose
# -------
# The reduced constant-density interior A model matches GR interior
# Schwarzschild at the boundary and through first weak-field order, but
# differs at second order inside matter.
#
# The GR interior Schwarzschild solution also generally has:
#
#   A_GR B_GR != 1
#
# inside matter, while:
#
#   A_GR B_GR = 1
#
# at the exterior boundary.
#
# This script asks whether the missing interior structure can be represented
# as an effective interior kappa profile:
#
#   kappa_GR(r) = 1/2 ln(A_GR B_GR)
#
# using dimensionless variables:
#
#   x = r/R
#   u = r_s/R = 2GM/(c^2 R)
#
# Main tests:
#
#   1. kappa_GR is generally nonzero inside.
#   2. kappa_GR(1)=0 at the boundary.
#   3. leading weak-field kappa_GR shape.
#   4. kappa_GR derivative at boundary.
#   5. whether the residual A_GR - A_red has the same boundary behavior.
#
# IMPORTANT:
# This is a diagnostic comparison to GR interior Schwarzschild, not a
# derivation of GR and not a commitment that the model must match GR exactly.

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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    return archive, ns, invalidated


def series_u(expr, u, order):
    return sp.simplify(sp.series(expr, u, 0, order).removeO())


def case_0_define_gr_kappa(out: ScriptOutput, ns=None):
    header("Case 0: Define GR interior kappa diagnostic")

    x, u = sp.symbols("x u", real=True)

    A_gr = sp.Rational(1, 4) * (3*sp.sqrt(1-u) - sp.sqrt(1-u*x**2))**2
    B_gr = 1 / (1 - u*x**2)
    AB_gr = sp.simplify(A_gr * B_gr)
    kappa_gr = sp.simplify(sp.Rational(1, 2) * sp.log(AB_gr))

    print("Dimensionless variables:")
    print("  x = r/R")
    print("  u = r_s/R = 2GM/(c^2 R)")
    print()
    print(f"A_GR = {A_gr}")
    print(f"B_GR = {B_gr}")
    print(f"A_GR B_GR = {AB_gr}")
    print(f"kappa_GR = 1/2 ln(A_GR B_GR) = {kappa_gr}")

    nontrivial_AB = not is_zero(AB_gr - 1)

    with out.derived_results():
        out.line("GR interior has nontrivial AB diagnostic",
                 StatusMark.PASS if nontrivial_AB else StatusMark.FAIL,
                 "A_GR * B_GR != 1 inside matter")

    if ns is not None:
        ns.record_derivation(
            derivation_id="gr_interior_AB_diagnostic",
            inputs=[A_gr, B_gr, x, u],
            output=AB_gr,
            method="A_GR * B_GR",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="GR constant-density interior, dimensionless variables",
        )

    return x, u, A_gr, B_gr, AB_gr, kappa_gr


def case_1_boundary_behavior(out: ScriptOutput, x, u, AB_gr, kappa_gr, ns=None):
    header("Case 1: Boundary behavior")

    AB_boundary = sp.simplify(AB_gr.subs(x, 1))
    kappa_boundary = sp.simplify(kappa_gr.subs(x, 1))

    dAB_boundary = sp.simplify(sp.diff(AB_gr, x).subs(x, 1))
    dkappa_boundary = sp.simplify(sp.diff(kappa_gr, x).subs(x, 1))

    print(f"A_GR B_GR at x=1 = {AB_boundary}")
    print(f"kappa_GR(1) = {kappa_boundary}")
    print(f"d/dx(A_GR B_GR)|1 = {dAB_boundary}")
    print(f"kappa_GR'(1) = {dkappa_boundary}")

    ab_at_boundary = is_zero(AB_boundary - 1)
    kappa_at_boundary = is_zero(kappa_boundary)
    dkappa_nonzero = not is_zero(dkappa_boundary)

    with out.derived_results():
        out.line("AB returns to 1 at boundary",
                 StatusMark.PASS if ab_at_boundary else StatusMark.FAIL,
                 f"A_GR B_GR(x=1) = {AB_boundary}")
        out.line("kappa returns to zero at boundary",
                 StatusMark.PASS if kappa_at_boundary else StatusMark.FAIL,
                 f"kappa_GR(1) = {kappa_boundary}")
        out.line("kappa derivative generally nonzero at boundary",
                 StatusMark.PASS if dkappa_nonzero else StatusMark.FAIL,
                 f"kappa_GR'(1) = {dkappa_boundary}")

    print()
    print("Interpretation:")
    print("  GR interior restores exterior compensation at the boundary,")
    print("  but the derivative can carry boundary/interface information.")

    if ns is not None:
        ns.record_derivation(
            derivation_id="gr_interior_kappa_boundary_residual",
            inputs=[kappa_gr, x, u],
            output=kappa_boundary,
            method="kappa_GR.subs(x, 1)",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="GR interior kappa at exterior boundary",
        )


def case_2_weak_field_kappa_shape(out: ScriptOutput, x, u, AB_gr, kappa_gr, ns=None):
    header("Case 2: Weak-field kappa shape")

    AB_series = series_u(AB_gr, u, 3)
    kappa_series = series_u(kappa_gr, u, 3)

    print(f"A_GR B_GR series through u^2 = {AB_series}")
    print(f"kappa_GR series through u^2 = {kappa_series}")

    leading_kappa = sp.simplify(series_u(kappa_gr, u, 2))
    second_order_kappa = sp.simplify(series_u(kappa_gr, u, 3))

    print()
    print(f"leading kappa = {leading_kappa}")
    print(f"through second order = {second_order_kappa}")

    first_order_nonzero = not is_zero(leading_kappa)
    boundary_vanishes = is_zero(sp.simplify(second_order_kappa.subs(x, 1)))

    with out.derived_results():
        out.line("kappa has first-order interior contribution",
                 StatusMark.PASS if first_order_nonzero else StatusMark.FAIL,
                 f"leading kappa = {leading_kappa}")
        out.line("kappa vanishes at boundary to this order",
                 StatusMark.PASS if boundary_vanishes else StatusMark.FAIL)

    if ns is not None:
        ns.record_derivation(
            derivation_id="gr_interior_kappa_weak_field_shape",
            inputs=[kappa_gr, x, u],
            output=leading_kappa,
            method="series_u(kappa_GR, u, 2)",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="weak-field series through first order in compactness",
        )


def case_3_center_behavior(out: ScriptOutput, x, u, kappa_gr):
    header("Case 3: Center behavior")

    kappa_center = sp.simplify(kappa_gr.subs(x, 0))
    dkappa_center = sp.simplify(sp.diff(kappa_gr, x).subs(x, 0))

    print(f"kappa_GR(0) = {kappa_center}")
    print(f"kappa_GR'(0) = {dkappa_center}")
    print(f"kappa_GR(0) series = {series_u(kappa_center, u, 4)}")

    with out.derived_results():
        out.line("kappa is regular at center",
                 StatusMark.PASS if is_zero(dkappa_center) else StatusMark.FAIL,
                 f"kappa_GR'(0) = {dkappa_center}")
        out.line("center kappa is generally nonzero",
                 StatusMark.PASS if not is_zero(kappa_center) else StatusMark.FAIL,
                 f"kappa_GR(0) = {kappa_center}")


def case_4_compare_A_residual(out: ScriptOutput, x, u, A_gr, ns=None):
    header("Case 4: Compare A residual")

    A_red = 1 - sp.Rational(3, 2)*u + sp.Rational(1, 2)*u*x**2
    residual_A = sp.simplify(A_gr - A_red)

    residual_series = series_u(residual_A, u, 4)
    residual_boundary = sp.simplify(residual_A.subs(x, 1))
    dresidual_boundary = sp.simplify(sp.diff(residual_A, x).subs(x, 1))

    print(f"A_red = {A_red}")
    print(f"A_GR - A_red = {residual_A}")
    print(f"residual series through u^3 = {residual_series}")
    print()
    print(f"residual at x=1 = {residual_boundary}")
    print(f"residual derivative at x=1 = {dresidual_boundary}")

    boundary_zero = is_zero(residual_boundary)
    deriv_zero = is_zero(dresidual_boundary)

    with out.derived_results():
        out.line("A residual vanishes at boundary",
                 StatusMark.PASS if boundary_zero else StatusMark.FAIL,
                 f"residual(x=1) = {residual_boundary}")
        out.line("A residual derivative vanishes at boundary",
                 StatusMark.PASS if deriv_zero else StatusMark.FAIL,
                 f"d/dx residual(x=1) = {dresidual_boundary}")

    print()
    print("Interpretation:")
    print("  The A-lapse residual is interior-supported and boundary-smooth.")
    print("  This makes it a plausible pressure/stress/interior-response correction.")

    if ns is not None:
        ns.record_derivation(
            derivation_id="gr_vs_reduced_A_residual_boundary_check",
            inputs=[A_gr, A_red, x, u],
            output=sp.Matrix([residual_boundary, dresidual_boundary]),
            method="A_GR - A_red boundary and derivative check",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="GR vs reduced A residual at x=1",
        )


def case_5_effective_kappa_profile_fit(out: ScriptOutput, x, u, kappa_gr, ns=None):
    header("Case 5: Toy effective kappa profile fit")

    eta = sp.symbols("eta", real=True)

    # Fit leading GR kappa to a simple shape eta*u*(1-x^2)
    kappa_leading = series_u(kappa_gr, u, 2)
    toy = eta * u * (1 - x**2)

    # Fit at center x=0.
    eta_solution = sp.solve(sp.Eq(toy.subs(x, 0), kappa_leading.subs(x, 0)), eta)
    toy_fit = sp.simplify(toy.subs(eta, eta_solution[0])) if eta_solution else toy

    print(f"kappa_GR leading = {kappa_leading}")
    print(f"toy profile = eta*u*(1-x^2)")
    print(f"eta from center fit = {eta_solution}")
    print(f"toy fit = {toy_fit}")
    print(f"difference = {sp.simplify(kappa_leading - toy_fit)}")

    with out.sample_results():
        out.line("simple (1-x^2) shape can capture leading kappa if fit succeeds",
                 StatusMark.PASS if bool(eta_solution) else StatusMark.FAIL,
                 f"eta = {eta_solution}")

    if ns is not None and eta_solution:
        ns.record_derivation(
            derivation_id="gr_interior_kappa_profile_toy_fit",
            inputs=[kappa_leading, x, u],
            output=toy_fit,
            method="center-fit eta*u*(1-x^2) to leading kappa_GR",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="toy profile fit, constant-density GR interior, first order in u",
        )


def case_6_interpretation_summary(out: ScriptOutput):
    header("Case 6: Interpretation summary")

    print("Results:")
    print()
    print("1. GR interior has A_GR B_GR != 1 inside matter.")
    print("2. Therefore kappa_GR = 1/2 ln(A_GR B_GR) is nonzero inside.")
    print("3. At the boundary x=1, A_GR B_GR = 1 and kappa_GR=0.")
    print("4. The derivative of kappa at the boundary can be nonzero.")
    print("5. The A residual relative to the reduced flux model is boundary-smooth.")
    print()
    print("Interpretation:")
    print("  This supports treating kappa=0 as an exterior/source-free condition,")
    print("  while matter interiors may carry traceful kappa response.")
    print()
    print("Possible next artifact:")
    print("  candidate_gr_residual_as_kappa_response.md")

    with out.governance_assessments():
        out.line("GR interior kappa diagnostic supports exterior-only kappa=0 hypothesis",
                 StatusMark.PASS,
                 "kappa_GR vanishes at boundary; GR interior has nontrivial kappa")

    with out.unresolved_obligations():
        out.line("derive interior kappa source from matter coupling (not just GR comparison)",
                 StatusMark.OBLIGATION,
                 "GR comparison is diagnostic only; mechanism remains underived")


def main():
    header("Candidate GR Residual as Kappa Response")
    archive, ns, invalidated = prepare_archive()
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")

    out = ScriptOutput()

    x, u, A_gr, B_gr, AB_gr, kappa_gr = case_0_define_gr_kappa(out, ns)
    case_1_boundary_behavior(out, x, u, AB_gr, kappa_gr, ns)
    case_2_weak_field_kappa_shape(out, x, u, AB_gr, kappa_gr, ns)
    case_3_center_behavior(out, x, u, kappa_gr)
    case_4_compare_A_residual(out, x, u, A_gr, ns)
    case_5_effective_kappa_profile_fit(out, x, u, kappa_gr, ns)
    case_6_interpretation_summary(out)

    out.print_summary()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_gr_interior_kappa_from_matter_coupling",
        script_id=SCRIPT_ID,
        title="Derive interior kappa source from matter coupling, not GR comparison",
        status=ObligationStatus.OPEN,
        description=(
            "The GR interior kappa diagnostic shows kappa is nonzero inside matter "
            "and vanishes at the boundary. This supports the exterior-only kappa=0 "
            "hypothesis but does not derive the mechanism. The source law for "
            "interior kappa from matter coupling remains open."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="gr_interior_kappa_boundary_smooth",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "The GR interior kappa diagnostic (kappa_GR = 1/2 ln(A_GR B_GR)) is "
            "nonzero inside matter, vanishes at the exterior boundary, and is regular "
            "at the center. The A residual A_GR - A_red is boundary-smooth. This is "
            "a diagnostic result, not a derivation of the mechanism."
        ),
        obligation_ids=["derive_gr_interior_kappa_from_matter_coupling"],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
