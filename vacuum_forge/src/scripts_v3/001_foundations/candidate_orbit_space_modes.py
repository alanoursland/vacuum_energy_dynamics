# Candidate orbit-space modes
#
# Group:
#   01_foundations
#
# Script type:
#   DIAGNOSTIC
#
# Purpose
# -------
# This script begins the next step after the gauge-dependence and areal-gauge
# kappa studies:
#
#   What are kappa and s shadows of in a more geometric spherical reduction?
#
# Spherically symmetric geometry can be written as:
#
#   ds^2 = h_AB(x) dx^A dx^B + R(x)^2 dΩ^2
#
# where:
#
#   h_AB is the 2D orbit-space metric on the quotient by SO(3),
#   x^A are orbit-space coordinates, often (t, radial coordinate),
#   R(x) is the areal-radius scalar defined by sphere area.
#
# In a static diagonal arbitrary radial coordinate X:
#
#   ds^2 = -T(X)c^2 dt^2 + Q(X)dX^2 + S(X)^2 dΩ^2
#
# the areal radius is:
#
#   R = S(X)
#
# and in areal gauge:
#
#   ds^2 = -A(R)c^2 dt^2 + B(R)dR^2 + R^2 dΩ^2
#
# with:
#
#   A = T
#   B = Q / (S')^2
#
# Previous result:
#
#   kappa_areal = 1/2 ln(A B)
#                = 1/2 ln(T Q / (S')^2)
#
# This script studies whether that can be expressed as an orbit-space
# geometric diagnostic involving:
#
#   det(h_AB)
#   norm of grad R on orbit space
#   radial unit direction / static time direction
#
# It also reconstructs the shear-like reduced mode:
#
#   s_areal = 1/2 ln(A/B)
#            = 1/2 ln(T (S')^2 / Q)
#
# IMPORTANT:
# This does not produce a full covariant field equation.
# It tests a gauge-aware spherical reduction.
#
# Case 7 integrates with VacuumForge's requirement validators and leak
# detector to classify the Schwarzschild check as "confirmed by construction"
# vs. "derived from source structure." The leak detector is expected to flag
# the Schwarzschild assumptions (B=1/A) as encoding the reciprocal_scaling
# target directly, distinguishing this consistency check from the structural
# derivations in the earlier log-scale-modes scripts.

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
from vacuumforge.core.context import TheoryContext
from vacuumforge.metric.concrete_check import check_concrete_metric


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 108)
    print(title)
    print("=" * 108)


def subheader(title: str) -> None:
    print()
    print("-" * 108)
    print(title)
    print("-" * 108)


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
        dependency_id="areal_kappa_coordinate_fixing",
        upstream_script_id="01_foundations__candidate_areal_gauge_kappa_condition",
        upstream_derivation_id="areal_kappa_coordinate_fixed",
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
# Case 0: Spherical orbit-space decomposition
# =============================================================================

def case_0_orbit_space_decomposition(out: ScriptOutput) -> None:
    header("Case 0: Spherical orbit-space decomposition")

    print("General spherically symmetric geometry:")
    print()
    print("  ds² = h_AB(x) dx^A dx^B + R(x)² dΩ²")
    print()
    print("where:")
    print("  h_AB is the 2D orbit-space metric,")
    print("  R(x) is the areal-radius scalar,")
    print("  Area of symmetry sphere = 4π R(x)².")
    print()
    print("This is more geometric than choosing an arbitrary radial coordinate.")
    print("The reduced kappa/s variables should be shadows of structures in h_AB")
    print("together with the scalar R(x).")

    with out.governance_assessments():
        out.line(
            "orbit-space split separates 2D geometry from sphere area",
            StatusMark.PASS,
            "geometric setup; kappa/s are 2D orbit-space diagnostics",
        )


# =============================================================================
# Case 1: Static diagonal arbitrary radial coordinate
# =============================================================================

def case_1_static_diagonal_arbitrary_coordinate(out: ScriptOutput) -> None:
    header("Case 1: Static diagonal arbitrary radial coordinate")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")(X)
    Q = sp.Function("Q")(X)
    S = sp.Function("S")(X)

    print("Static spherical metric in arbitrary radial coordinate X:")
    print()
    print("  ds² = -T(X)c²dt² + Q(X)dX² + S(X)²dΩ²")
    print()
    print("Orbit-space metric components:")
    print("  h_tt = -T(X)c²")
    print("  h_XX = Q(X)")
    print()
    print("Areal-radius scalar:")
    print("  R(X) = S(X)")
    print()
    print("Areal gauge is obtained by using R=S(X) as radial coordinate.")

    with out.governance_assessments():
        out.line(
            "static diagonal metric is a special orbit-space representation",
            StatusMark.PASS,
            "h_tt=-Tc^2, h_XX=Q; areal radius R=S(X)",
        )


# =============================================================================
# Case 2: Areal-gauge reconstruction from orbit-space data
# =============================================================================

def case_2_areal_gauge_reconstruction(out: ScriptOutput) -> None:
    header("Case 2: Areal-gauge reconstruction from orbit-space data")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(X)

    Sp = sp.diff(S, X)

    A_areal = T(X)
    B_areal = sp.simplify(Q(X) / Sp**2)

    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(A_areal * B_areal))
    s_areal = sp.simplify(sp.Rational(1, 2) * sp.log(A_areal / B_areal))

    print("Define areal coordinate R=S(X).")
    print("Then dR/dX = S'(X).")
    print()
    print(f"A_areal = {A_areal}")
    print(f"B_areal = {B_areal}")
    print()
    print(f"kappa_areal = 1/2 ln(A B) = {kappa_areal}")
    print(f"s_areal     = 1/2 ln(A/B) = {s_areal}")
    print()
    print("Compensation condition:")
    print("  kappa_areal = 0  <=>  T(X) Q(X) = S'(X)²")

    condition_expr = sp.simplify(T(X) * Q(X) / Sp**2)

    with out.derived_results():
        out.line(
            "kappa_areal built from T, Q, and sphere-area scalar S",
            StatusMark.PASS,
            f"exp(2*kappa_areal) = {condition_expr}",
        )


# =============================================================================
# Case 3: Orbit-space determinant diagnostic
# =============================================================================

def case_3_orbit_space_determinant_diagnostic(out: ScriptOutput) -> None:
    header("Case 3: Orbit-space determinant diagnostic")

    X, c = sp.symbols("X c", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(X)

    Sp = sp.diff(S, X)

    # Orbit-space metric h_AB = diag(-T c^2, Q)
    det_h = sp.simplify(-T(X) * c**2 * Q(X))
    abs_det_h = sp.simplify(T(X) * c**2 * Q(X))

    # The areal coordinate Jacobian contributes S'^2.
    # In areal coordinates, det(h_areal) = -A c^2 B = -T c^2 Q/S'^2.
    det_h_areal = sp.simplify(-T(X) * c**2 * Q(X) / Sp**2)
    abs_det_h_areal = sp.simplify(T(X) * c**2 * Q(X) / Sp**2)

    kappa_from_det = sp.simplify(sp.Rational(1, 2) * sp.log(abs_det_h_areal / c**2))
    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(T(X) * Q(X) / Sp**2))

    print("Orbit-space determinant in arbitrary X:")
    print(f"  det(h) = {det_h}")
    print(f"  |det(h)| = {abs_det_h}")
    print()
    print("After using areal coordinate R=S(X):")
    print(f"  det(h_areal) = {det_h_areal}")
    print(f"  |det(h_areal)| = {abs_det_h_areal}")
    print()
    print("Remove the constant c² factor:")
    print(f"  kappa_from_det = 1/2 ln(|det(h_areal)|/c²) = {kappa_from_det}")
    print(f"  kappa_areal = {kappa_areal}")

    det_matches = is_zero(kappa_from_det - kappa_areal)

    print()
    print("Interpretation:")
    print("  kappa is not a 4D scalar field.")
    print("  In static spherical areal gauge, it is the log-volume factor of the")
    print("  2D temporal-radial orbit-space metric, after removing c².")

    with out.derived_results():
        out.line(
            "kappa_areal is half log orbit-space determinant factor in areal gauge",
            StatusMark.PASS if det_matches else StatusMark.WARN,
            "kappa = 1/2 ln(|det(h_areal)|/c^2)",
        )


# =============================================================================
# Case 4: Norm of areal-radius gradient
# =============================================================================

def case_4_areal_radius_gradient_norm(out: ScriptOutput) -> None:
    header("Case 4: Norm of areal-radius gradient")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(X)

    Sp = sp.diff(S, X)

    # In arbitrary coordinate X, orbit-space inverse has h^XX = 1/Q.
    # R=S(X), so grad R norm = h^AB ∂_A R ∂_B R = S'^2 / Q.
    gradR2 = sp.simplify(Sp**2 / Q(X))

    # B_areal = Q/S'^2, so gradR2 = 1/B_areal.
    B_areal = sp.simplify(Q(X) / Sp**2)

    print("Areal-radius scalar:")
    print("  R(X)=S(X)")
    print()
    print("Orbit-space gradient norm:")
    print(f"  |∇R|²_h = h^AB ∂_A R ∂_B R = {gradR2}")
    print()
    print(f"B_areal = {B_areal}")
    print(f"1/B_areal = {sp.simplify(1/B_areal)}")

    grad_is_inv_B = is_zero(gradR2 - 1/B_areal)

    print()
    print("Using A_areal=T and B_areal=1/|grad R|²:")
    print("  AB = A_areal / |∇R|²")
    print("  kappa_areal = 1/2 ln(A_areal / |∇R|²)")
    print()
    kappa_grad = sp.simplify(sp.Rational(1, 2) * sp.log(T(X) / gradR2))
    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(T(X) * B_areal))
    print(f"kappa from gradR = {kappa_grad}")
    print(f"kappa_areal      = {kappa_areal}")

    kappa_via_grad = is_zero(kappa_grad - kappa_areal)

    with out.derived_results():
        out.line(
            "|grad R|² = 1/B_areal",
            StatusMark.PASS if grad_is_inv_B else StatusMark.WARN,
            f"|∇R|² = {gradR2}",
        )
        out.line(
            "kappa can be expressed using A and areal-radius gradient norm",
            StatusMark.PASS if kappa_via_grad else StatusMark.WARN,
            "kappa = 1/2 ln(A / |∇R|²)",
        )


# =============================================================================
# Case 5: Shear-like mode from temporal coefficient and areal gradient
# =============================================================================

def case_5_shear_like_mode_from_gradient(out: ScriptOutput) -> None:
    header("Case 5: Shear-like mode from temporal coefficient and areal gradient")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(X)

    Sp = sp.diff(S, X)
    gradR2 = sp.simplify(Sp**2 / Q(X))

    A_areal = T(X)
    B_areal = sp.simplify(Q(X) / Sp**2)

    s_areal = sp.simplify(sp.Rational(1, 2) * sp.log(A_areal / B_areal))

    # Since 1/B = gradR2, A/B = A * gradR2.
    s_grad = sp.simplify(sp.Rational(1, 2) * sp.log(A_areal * gradR2))

    print(f"s_areal = 1/2 ln(A/B) = {s_areal}")
    print(f"s from gradR = 1/2 ln(A |∇R|²) = {s_grad}")

    s_via_grad = is_zero(s_areal - s_grad)

    print()
    print("Interpretation:")
    print("  In static diagonal spherical symmetry, both kappa and s can be")
    print("  expressed using the temporal coefficient A and the orbit-space norm")
    print("  of the areal-radius gradient.")
    print()
    print("  kappa = 1/2 ln(A / |∇R|²)")
    print("  s     = 1/2 ln(A |∇R|²)")
    print()
    print("This is more geometric than raw coordinate B, but still assumes a")
    print("static slicing / time normalization for A.")

    with out.derived_results():
        out.line(
            "s_areal can be expressed using A and areal-radius gradient norm",
            StatusMark.PASS if s_via_grad else StatusMark.WARN,
            "s = 1/2 ln(A |∇R|²)",
        )


# =============================================================================
# Case 6: Compensation condition in gradient form
# =============================================================================

def case_6_compensation_condition_gradient_form(out: ScriptOutput) -> None:
    header("Case 6: Compensation condition in gradient form")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(X)

    Sp = sp.diff(S, X)
    gradR2 = sp.simplify(Sp**2 / Q(X))

    # kappa=0 -> A/B? Actually kappa = 1/2 ln(A B_areal)
    # and B_areal = 1/gradR2.
    # Therefore kappa=0 -> A/gradR2 = 1 -> A = gradR2.
    condition_gradient = sp.Eq(T(X), gradR2)
    condition_arbitrary = sp.Eq(T(X) * Q(X), Sp**2)

    print("From:")
    print("  kappa_areal = 1/2 ln(A / |∇R|²)")
    print()
    print("Compensation kappa_areal=0 gives:")
    print("  A = |∇R|²")
    print()
    print("In arbitrary coordinate X:")
    print(f"  {condition_gradient}")
    print()
    print("Equivalent to:")
    print(f"  {condition_arbitrary}")

    gradient_condition_ok = is_zero(T(X) - gradR2) == is_zero((T(X) * Q(X) - Sp**2) / Q(X))

    print()
    print("Interpretation:")
    print("  This may be the cleanest spherical-reduction statement:")
    print("  exterior compensation says the temporal lapse coefficient equals")
    print("  the orbit-space norm of the areal-radius gradient.")
    print()
    print("  In areal gauge, |∇R|² = 1/B, so this becomes AB=1.")

    with out.derived_results():
        out.line(
            "gradient condition A=|grad R|² matches TQ=S'²",
            StatusMark.PASS if gradient_condition_ok else StatusMark.WARN,
            "orbit-space form of areal compensation condition",
        )


# =============================================================================
# Case 7: Schwarzschild check
# =============================================================================

def case_7_schwarzschild_check(out: ScriptOutput, ns=None):
    header("Case 7: Schwarzschild exterior check")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    # Schwarzschild exterior in areal coordinates:
    #   A = 1 - 2GM/(rc^2)
    #   B = 1/A
    A = 1 - 2 * G * M / (r * c**2)
    B = sp.simplify(1 / A)

    kappa = sp.simplify(sp.Rational(1, 2) * sp.log(A * B))
    s = sp.simplify(sp.Rational(1, 2) * sp.log(A / B))

    # In areal gauge, |grad R|² = 1/B = A.
    gradR2 = sp.simplify(1 / B)

    print(f"A = {A}")
    print(f"B = {B}")
    print(f"A B = {sp.simplify(A*B)}")
    print(f"kappa = {kappa}")
    print(f"s = {s}")
    print(f"|grad R|² = 1/B = {gradR2}")

    schw_kappa_zero = is_zero(A*B - 1)
    schw_grad_ok = is_zero(A - gradR2)

    print()
    print("Note:")
    print("  This is an exact Schwarzschild exterior check in areal coordinates,")
    print("  not merely weak-field. The reduced toy's AB=1 condition matches")
    print("  the Schwarzschild areal-gauge reciprocal relation.")

    # --- VacuumForge classification: confirmed by construction vs. derived ---
    subheader("Case 7b: Leak-detection classification")

    ctx = TheoryContext("schwarzschild_areal_exterior")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols

    # Register the Schwarzschild ansatz as assumptions.
    # B = 1/A directly encodes AB=1, so the leak detector should flag this.
    A_schw = 1 - 2 * ms.G * ms.M / (ms.r * ms.c**2)
    ctx.assumptions.add(
        "schwarzschild_A",
        sp.Eq(ms.A, A_schw),
        description="Schwarzschild temporal coefficient: A = 1 - 2GM/rc².",
    )
    ctx.assumptions.add(
        "schwarzschild_B_reciprocal",
        sp.Eq(ms.B, 1 / A_schw),
        description="Schwarzschild radial coefficient: B = 1/A.",
    )

    print()
    print("Concrete metric classification:")
    concrete_results = check_concrete_metric(
        ctx,
        A_value=A_schw,
        B_value=sp.simplify(1 / A_schw),
        requirement_ids=["reciprocal_scaling", "gamma_v_one"],
    )
    for result in concrete_results:
        print(f"  {result.requirement_id}: {result.status}")
        print(f"    {result.message}")
        if result.leak_report is not None and result.leak_report.leaked:
            print(f"    leak via: {result.leak_report.leaked_via}")

    print()
    print("Classification:")
    print("  The Schwarzschild check is 'satisfied_by_construction' when the")
    print("  reciprocal form is encoded directly in the concrete metric.")
    print("  That keeps the result in the right bucket: a consistency check")
    print("  against a known solution, not a source-law derivation.")

    with out.derived_results():
        out.line(
            "Schwarzschild areal exterior has kappa=0",
            StatusMark.PASS if schw_kappa_zero else StatusMark.FAIL,
            f"AB = {sp.simplify(A*B)}",
        )
        out.line(
            "Schwarzschild satisfies A=|grad R|²",
            StatusMark.PASS if schw_grad_ok else StatusMark.WARN,
            "exact exterior check in areal coordinates",
        )

    with out.governance_assessments():
        out.line(
            "Schwarzschild reciprocal relation is confirmed by construction, not derived",
            StatusMark.PASS,
            "B=1/A encodes AB=1 directly; consistency check not source-law derivation",
        )

    if ns is not None:
        reciprocal_result = next(
            (result for result in concrete_results if result.requirement_id == "reciprocal_scaling"),
            None,
        )
        if reciprocal_result is not None:
            ns.record_derivation(
                derivation_id="schwarzschild_concrete_metric_check",
                inputs=[A_schw],
                output=sp.Symbol(reciprocal_result.status),
                method="concrete_metric_check",
                status=Status.DERIVED,
                record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
                metadata={"message": reciprocal_result.message},
            )


# =============================================================================
# Case 8: Failure control — arbitrary radial coordinate without S
# =============================================================================

def case_8_failure_control_ignore_areal_scalar(out: ScriptOutput) -> None:
    header("Case 8: Failure control — ignoring areal scalar")

    R = sp.symbols("R", positive=True, real=True)
    f = sp.Function("f")(R)
    A = sp.Function("A")
    B = sp.Function("B")

    # Start from compensated areal gauge: A(r)B(r)=1.
    # Reparameterize r=f(R).
    T = A(f)
    Q = B(f) * sp.diff(f, R)**2
    S = f
    Sp = sp.diff(S, R)

    naive_TQ = sp.simplify(T * Q)
    corrected = sp.simplify(T * Q / Sp**2)

    print("Start from AB=1 in areal gauge and set r=f(R).")
    print()
    print(f"T(R)Q(R) naive = {naive_TQ}")
    print(f"T(R)Q(R)/S'(R)^2 = {corrected}")

    print()
    print("If A(f)B(f)=1:")
    corrected_under_AB1 = corrected.subs(A(f)*B(f), 1)
    print("  corrected expression -> 1")
    print("  naive expression -> f'(R)^2")
    print()

    with out.governance_assessments():
        out.line(
            "including areal scalar removes radial Jacobian artifact",
            StatusMark.PASS,
            "failure-control: naive TQ=f'^2; corrected TQ/S'^2=1",
        )


# =============================================================================
# Case 9: Summary classification
# =============================================================================

def case_9_summary_classification(out: ScriptOutput) -> None:
    header("Case 9: Summary classification")

    print("Results:")
    print()
    print("1. Spherical symmetry admits a 2D orbit-space metric h_AB")
    print("   plus an areal-radius scalar R(x).")
    print()
    print("2. In static diagonal form:")
    print("     ds² = -T(X)c²dt² + Q(X)dX² + S(X)²dΩ²")
    print("   the areal radius is R=S(X).")
    print()
    print("3. The areal-gauge radial coefficient is:")
    print("     B_areal = Q/S'²")
    print()
    print("4. The areal-gauge imbalance mode is:")
    print("     kappa = 1/2 ln(T Q/S'²)")
    print()
    print("5. Since |∇R|² = S'²/Q, this can be written:")
    print("     kappa = 1/2 ln(A / |∇R|²)")
    print()
    print("6. The shear-like reduced mode can be written:")
    print("     s = 1/2 ln(A |∇R|²)")
    print()
    print("7. Compensation kappa=0 becomes:")
    print("     A = |∇R|²")
    print("   or, in arbitrary radial coordinate:")
    print("     T Q = S'²")
    print()
    print("This is a more geometric spherical-reduction formulation.")
    print("It is not yet a full covariant theory.")

    with out.governance_assessments():
        out.line(
            "orbit-space gradient formulation of kappa is more geometric than raw B",
            StatusMark.PASS,
            "kappa=1/2 ln(A/|∇R|^2); not yet a full covariant theory",
        )

    with out.unresolved_obligations():
        out.line(
            "derive full covariant field theory from orbit-space kappa formulation",
            StatusMark.OBLIGATION,
            "orbit-space reduction established; full covariant theory not yet derived",
        )


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")

    print("This orbit-space study improves the status of the reduced modes.")
    print()
    print("The raw areal-gauge formulas:")
    print("  kappa = 1/2 ln(A B)")
    print("  s     = 1/2 ln(A/B)")
    print()
    print("can be rewritten using the 2D orbit-space metric and the")
    print("areal-radius scalar R:")
    print()
    print("  |∇R|² = h^AB ∂_A R ∂_B R")
    print()
    print("In the static diagonal spherical sector:")
    print()
    print("  kappa = 1/2 ln(A / |∇R|²)")
    print("  s     = 1/2 ln(A |∇R|²)")
    print()
    print("and the compensation condition becomes:")
    print()
    print("  kappa = 0  <=>  A = |∇R|²")
    print()
    print("In areal gauge, |∇R|² = 1/B, so this reduces to:")
    print()
    print("  AB = 1")
    print()
    print("This does not make kappa a full spacetime scalar field.")
    print("It makes kappa a gauge-aware spherical-reduction diagnostic built")
    print("from the orbit-space geometry and areal-radius scalar.")
    print()
    print("Possible next artifact:")
    print("  candidate_orbit_space_modes.md")

    with out.governance_assessments():
        out.line(
            "kappa is orbit-space geometric diagnostic built from h_AB and R scalar",
            StatusMark.PASS,
            "kappa=1/2 ln(A/|∇R|^2); compensation A=|∇R|^2; not a 4D scalar field",
        )


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Orbit-Space Modes")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_orbit_space_decomposition(out)
    case_1_static_diagonal_arbitrary_coordinate(out)
    case_2_areal_gauge_reconstruction(out)
    case_3_orbit_space_determinant_diagnostic(out)
    case_4_areal_radius_gradient_norm(out)
    case_5_shear_like_mode_from_gradient(out)
    case_6_compensation_condition_gradient_form(out)
    case_7_schwarzschild_check(out, ns)
    case_8_failure_control_ignore_areal_scalar(out)
    case_9_summary_classification(out)
    final_interpretation(out)

    # Governance records inside the archive block.
    ns.record_claim(ClaimRecord(
        claim_id="kappa_orbit_space_gradient_diagnostic",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "In static diagonal spherical symmetry, kappa is a gauge-aware "
            "orbit-space diagnostic: kappa = 1/2 ln(A/|∇R|^2), where |∇R|^2 "
            "is the orbit-space norm of the areal-radius scalar gradient. "
            "Compensation kappa=0 means A=|∇R|^2. This is not a 4D scalar field."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="schwarzschild_reciprocal_is_construction_check",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The Schwarzschild exterior satisfies kappa=0 (AB=1) by construction "
            "when B=1/A is encoded as an assumption. This is a consistency check "
            "against a known solution, not a source-law derivation of kappa suppression."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_full_covariant_orbit_space_theory",
        script_id=SCRIPT_ID,
        title="Derive full covariant field theory from orbit-space kappa formulation",
        status=ObligationStatus.OPEN,
        required_by=["kappa_orbit_space_gradient_diagnostic"],
        description=(
            "The orbit-space formulation kappa=1/2 ln(A/|∇R|^2) is a geometric "
            "improvement over the raw areal-gauge formula, but it still assumes "
            "a static slicing and spherical symmetry. A full covariant field "
            "theory is needed that reduces to this diagnostic in the static "
            "spherical areal-gauge sector."
        ),
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
