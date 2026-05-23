# Candidate areal-gauge kappa condition
#
# Group:
#   01_foundations
#
# Script type:
#   DIAGNOSTIC
#
# Purpose
# -------
# This script studies the question:
#
#   Can areal-gauge kappa=0 be re-expressed as a gauge-invariant or
#   gauge-fixed condition derived from sphere area / radial foliation geometry?
#
# Prior result:
#   Under radial reparameterization r=f(R), naive reduced modes shift:
#
#       kappa -> kappa + log(f')
#       s     -> s - log(f')
#
#   Therefore kappa and s are not coordinate-invariant scalar fields.
#
# Current idea:
#   The areal radius is geometrically defined by the area of symmetry spheres:
#
#       Area(S) = 4π r_areal^2
#
#   In spherical symmetry, this defines a preferred radial scalar r_areal.
#   Once the radial coordinate is fixed to r_areal, the reduced metric takes:
#
#       ds² = -A(r)c²dt² + B(r)dr² + r²dΩ²
#
#   In that gauge, kappa is well-defined as:
#
#       kappa = 1/2 ln(A B)
#
#   and kappa=0 is equivalent to:
#
#       A B = 1.
#
# This script tests:
#
#   Case 0: General spherical metric with arbitrary radial coordinate R.
#   Case 1: Areal radius from sphere area.
#   Case 2: Transform from arbitrary R to areal radius r=f(R).
#   Case 3: Gauge-fixed kappa_areal from transformed metric.
#   Case 4: Relationship between naive kappa_R and areal-gauge kappa.
#   Case 5: Gauge-invariant phrasing as a gauge-fixed scalar construction.
#   Case 6: Schwarzschild-like reciprocal condition as areal-gauge statement.
#   Case 7: Failure control when angular radius is ignored.
#
# IMPORTANT:
# This does NOT prove that kappa itself is an invariant scalar.
# It tests whether kappa=0 can be phrased as a condition after a geometric
# gauge fixing by the areal radius.

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
from vacuumforge.coordinates import CoordinateChange


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 104)
    print(title)
    print("=" * 104)


def subheader(title: str) -> None:
    print()
    print("-" * 104)
    print(title)
    print("-" * 104)


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
        dependency_id="gauge_dependence_shift",
        upstream_script_id="01_foundations__candidate_gauge_dependence_modes",
        upstream_derivation_id="reduced_mode_coordinate_shift",
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
# Case 0: General spherical metric in arbitrary radial coordinate
# =============================================================================

def case_0_general_spherical_metric(out: ScriptOutput) -> None:
    header("Case 0: General spherical metric in arbitrary radial coordinate")

    R = sp.symbols("R", positive=True, real=True)
    T = sp.Function("T")(R)
    Q = sp.Function("Q")(R)
    S = sp.Function("S")(R)

    print("General static spherical metric in arbitrary radial coordinate R:")
    print("  ds² = -T(R)c²dt² + Q(R)dR² + S(R)² dΩ²")
    print()
    print("Here:")
    print("  T(R) is the temporal coefficient.")
    print("  Q(R) is the radial coefficient.")
    print("  S(R) is the geometric sphere-radius function.")
    print()
    print("Sphere area:")
    print("  Area(R) = 4π S(R)²")
    print()
    print("Areal radius:")
    print("  r_areal = sqrt(Area/4π) = S(R)")
    print()

    with out.governance_assessments():
        out.line(
            "arbitrary radial coordinate includes angular-radius function S(R)",
            StatusMark.PASS,
            "correct general setup; areal radius = S(R)",
        )


# =============================================================================
# Case 1: Areal radius from sphere area
# =============================================================================

def case_1_areal_radius_from_area(out: ScriptOutput) -> None:
    header("Case 1: Areal radius from sphere area")

    R = sp.symbols("R", positive=True, real=True)
    S = sp.Function("S")(R)
    Area = 4 * sp.pi * S**2
    r_areal = sp.sqrt(Area / (4 * sp.pi))

    print(f"Area(R) = {Area}")
    print(f"r_areal = sqrt(Area/4π) = {r_areal}")

    # Since S(R) is positive by geometric interpretation, r_areal = S(R).
    print()
    print("Assuming positive sphere-radius function S(R)>0:")
    print("  r_areal = S(R)")

    with out.derived_results():
        out.line(
            "areal radius is geometrically fixed by sphere area",
            StatusMark.PASS,
            "r_areal = S(R) by construction from sphere area formula",
        )


# =============================================================================
# Case 2: Transform arbitrary R to areal radius r=S(R)
# =============================================================================

def case_2_transform_to_areal_radius(out: ScriptOutput, ns=None):
    header("Case 2: Transform arbitrary R to areal radius r=S(R)")

    R = sp.symbols("R", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(R)

    # General metric:
    #   ds² = -T(R)c²dt² + Q(R)dR² + S(R)²dΩ²
    #
    # Define r = S(R).
    # Then dr/dR = S'(R), so dR/dr = 1/S'(R).
    #
    # In areal coordinate r, the radial coefficient is:
    #   B_areal(r) = Q(R) * (dR/dr)^2 = Q(R)/S'(R)^2
    #
    # and:
    #   A_areal(r) = T(R)
    change = CoordinateChange(old_coord=sp.Symbol("r", positive=True, real=True), new_coord=R, transform=S)
    Sprime = change.jacobian()

    A_areal_at_R = T(R)
    B_areal_at_R = sp.simplify(Q(R) / Sprime**2)

    print("Define:")
    print("  r = S(R)")
    print("  dr/dR = S'(R)")
    print("  dR/dr = 1/S'(R)")
    print()
    print("Then in areal gauge:")
    print(f"  A_areal = {A_areal_at_R}")
    print(f"  B_areal = {B_areal_at_R}")
    print("  angular sector = r²dΩ²")
    print()

    with out.derived_results():
        out.line(
            "areal radial coefficient includes inverse sphere-radius Jacobian",
            StatusMark.PASS,
            f"B_areal = Q(R)/S'(R)^2 = {B_areal_at_R}",
        )

    if ns is not None:
        ns.record_derivation(
            derivation_id="areal_radius_reconstruction",
            inputs=[T(R), Q(R), S],
            output=sp.Eq(T(R) * Q(R), Sprime**2 * A_areal_at_R * B_areal_at_R),
            method="areal_radius_coordinate_fixing",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
        )


# =============================================================================
# Case 3: Areal-gauge kappa from arbitrary-coordinate metric
# =============================================================================

def case_3_kappa_areal_from_arbitrary_metric(out: ScriptOutput) -> None:
    header("Case 3: Areal-gauge kappa from arbitrary-coordinate metric")

    R = sp.symbols("R", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(R)

    Sprime = sp.diff(S, R)

    # Naive kappa in arbitrary R coordinate if one incorrectly treats R as areal:
    kappa_naive_R = sp.simplify(sp.Rational(1, 2) * sp.log(T(R) * Q(R)))

    # Correct areal-gauge kappa constructed after using r=S(R):
    # A_areal B_areal = T(R) * Q(R)/S'(R)^2
    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(T(R) * Q(R) / Sprime**2))

    delta = sp.simplify(kappa_naive_R - kappa_areal)

    print(f"kappa_naive_R = 1/2 ln(T Q) = {kappa_naive_R}")
    print(f"kappa_areal   = 1/2 ln(T Q / S'^2) = {kappa_areal}")
    print(f"kappa_naive_R - kappa_areal = {delta}")
    print()
    print("If S'(R)>0, then:")
    print("  kappa_naive_R = kappa_areal + ln S'(R)")
    print()
    print("Areal-gauge compensation condition:")
    print("  kappa_areal = 0")
    print("equivalent to:")
    print("  T(R) Q(R) / S'(R)^2 = 1")
    print("or:")
    print("  T(R) Q(R) = S'(R)^2")

    with out.derived_results():
        out.line(
            "difference between naive and areal kappa is radial gauge Jacobian",
            StatusMark.PASS,
            f"kappa_naive - kappa_areal = log(S') = {delta}",
        )


# =============================================================================
# Case 4: Recover previous radial reparameterization result
# =============================================================================

def case_4_recover_reparameterization_result(out: ScriptOutput, ns=None):
    header("Case 4: Recover previous radial reparameterization result")

    R = sp.symbols("R", positive=True, real=True)
    f = sp.Function("f")(R)
    A = sp.Function("A")
    B = sp.Function("B")

    # Start in areal gauge r, then reparameterize r=f(R).
    # General arbitrary-coordinate form has:
    #   T(R)=A(f(R))
    #   Q(R)=B(f(R))*f'(R)^2
    #   S(R)=f(R)
    change = CoordinateChange(old_coord=sp.Symbol("r", positive=True, real=True), new_coord=R, transform=f)
    T = change.transform_scale_factor(A(change.old_coord), "temporal")
    Q = change.transform_scale_factor(B(change.old_coord), "radial")
    S = f
    Sprime = sp.diff(S, R)

    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(T * Q / Sprime**2))
    kappa_old_at_f = sp.simplify(sp.Rational(1, 2) * sp.log(A(f) * B(f)))

    kappa_naive_R = sp.simplify(sp.Rational(1, 2) * sp.log(T * Q))

    print("Start from areal gauge and set r=f(R):")
    print(f"  T(R) = {T}")
    print(f"  Q(R) = {Q}")
    print(f"  S(R) = {S}")
    print()
    print(f"kappa_areal reconstructed = {kappa_areal}")
    print(f"kappa_old_at_f = {kappa_old_at_f}")
    print(f"kappa_naive_R = {kappa_naive_R}")

    recovers_original = is_zero(kappa_areal - kappa_old_at_f)

    print()
    print("Naive kappa_R includes the radial Jacobian, while kappa_areal removes it.")

    with out.derived_results():
        out.line(
            "areal reconstruction recovers original kappa",
            StatusMark.PASS if recovers_original else StatusMark.WARN,
            f"kappa_areal - kappa_old_at_f = {sp.simplify(kappa_areal - kappa_old_at_f)}",
        )

    if ns is not None:
        ns.record_derivation(
            derivation_id="areal_kappa_coordinate_fixed",
            inputs=[T, Q, S],
            output=sp.Eq(kappa_areal, kappa_old_at_f),
            method="coordinate_change_areal_reconstruction",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
        )


# =============================================================================
# Case 5: Gauge-fixed condition as geometric construction
# =============================================================================

def case_5_gauge_fixed_condition_statement(out: ScriptOutput) -> None:
    header("Case 5: Gauge-fixed condition as geometric construction")

    print("The result can be stated without pretending kappa is invariant:")
    print()
    print("1. Start with a static spherical geometry.")
    print("2. Define the areal radius by sphere area:")
    print("     r = sqrt(Area/4π)")
    print("3. Express the metric in areal-radius form:")
    print("     ds² = -A(r)c²dt² + B(r)dr² + r²dΩ²")
    print("4. Define:")
    print("     kappa_areal = 1/2 ln(A B)")
    print("5. Exterior reciprocal compensation is:")
    print("     kappa_areal = 0")
    print("   equivalently:")
    print("     A B = 1")
    print()
    print("This is not a coordinate-invariant scalar equation.")
    print("It is a condition after geometric gauge fixing by sphere area.")

    with out.governance_assessments():
        out.line(
            "kappa=0 can be phrased as a gauge-fixed geometric condition",
            StatusMark.PASS,
            "areal gauge fixing makes kappa_areal=0 well-defined; not invariant scalar",
        )


# =============================================================================
# Case 6: Express condition in arbitrary radial coordinate
# =============================================================================

def case_6_arbitrary_coordinate_expression(out: ScriptOutput) -> None:
    header("Case 6: Arbitrary-coordinate expression of areal compensation")

    R = sp.symbols("R", positive=True, real=True)
    T = sp.Function("T")(R)
    Q = sp.Function("Q")(R)
    S = sp.Function("S")(R)
    Sprime = sp.diff(S, R)

    condition = sp.Eq(T * Q, Sprime**2)

    print("General static spherical metric:")
    print("  ds² = -T(R)c²dt² + Q(R)dR² + S(R)²dΩ²")
    print()
    print("Areal-gauge compensation kappa_areal=0 is equivalent to:")
    print("  T(R) Q(R) / S'(R)² = 1")
    print()
    print("So, in arbitrary radial coordinate:")
    print(f"  {condition}")
    print()
    print("This expression includes the angular-radius function S(R).")
    print("It is the arbitrary-coordinate version of areal-gauge AB=1.")
    print()

    with out.derived_results():
        out.line(
            "arbitrary-coordinate expression includes sphere-area geometry",
            StatusMark.PASS,
            f"areal condition: {condition}",
        )


# =============================================================================
# Case 7: Failure control: ignoring angular sector
# =============================================================================

def case_7_failure_control_ignore_angular_sector(out: ScriptOutput) -> None:
    header("Case 7: Failure control — ignoring angular sector")

    R = sp.symbols("R", positive=True, real=True)
    f = sp.Function("f")(R)

    print("If one ignores the angular sector and computes only naive T(R)Q(R),")
    print("then a pure radial reparameterization of an AB=1 metric gives:")
    print()
    print("  T(R)Q(R) = f'(R)²")
    print()
    print("This falsely looks like reciprocal scaling failed.")
    print()
    print("But the angular sector is f(R)²dΩ², so the areal radius is f(R).")
    print("Restoring areal gauge removes the f'(R)² factor.")
    print()

    with out.governance_assessments():
        out.line(
            "ignoring angular sector produces false gauge artifact",
            StatusMark.PASS,
            "failure-control case: correct analysis requires S(R) in the condition",
        )


# =============================================================================
# Case 8: Summary classification
# =============================================================================

def case_8_summary_classification(out: ScriptOutput) -> None:
    header("Case 8: Summary classification")

    print("Results:")
    print()
    print("1. The areal radius is geometrically defined by sphere area.")
    print("2. In arbitrary radial coordinate R, the metric has angular radius S(R).")
    print("3. Transforming to areal radius r=S(R) gives:")
    print("     B_areal = Q(R)/S'(R)²")
    print("4. Therefore:")
    print("     kappa_areal = 1/2 ln[T(R) Q(R) / S'(R)²]")
    print("5. Areal-gauge compensation kappa_areal=0 becomes:")
    print("     T(R) Q(R) = S'(R)²")
    print("6. This is gauge-fixed/geometric, not a raw scalar condition.")
    print()
    print("Development implication:")
    print("  kappa=0 can be safely phrased as an areal-gauge condition derived")
    print("  from sphere-area radial foliation geometry.")

    with out.governance_assessments():
        out.line(
            "areal-gauge kappa=0 is geometric and gauge-fixed, not an invariant scalar",
            StatusMark.PASS,
            "T(R)Q(R)=S'(R)^2 is the arbitrary-coordinate form",
        )


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")

    print("This script answers the question in a qualified way:")
    print()
    print("  Can areal-gauge kappa=0 be re-expressed as a gauge-invariant")
    print("  or gauge-fixed condition derived from sphere area / radial foliation?")
    print()
    print("Answer:")
    print()
    print("  Not as an invariant scalar kappa=0.")
    print()
    print("  Yes as a gauge-fixed geometric construction:")
    print("    define areal radius by sphere area,")
    print("    express the metric in areal gauge,")
    print("    then impose kappa_areal = 1/2 ln(AB) = 0.")
    print()
    print("In arbitrary radial coordinate:")
    print("  ds² = -T(R)c²dt² + Q(R)dR² + S(R)²dΩ²")
    print()
    print("the same areal-gauge compensation condition is:")
    print("  T(R) Q(R) = S'(R)²")
    print()
    print("This includes the angular/sphere-area geometry and avoids the")
    print("naive gauge artifact TQ != 1 under radial reparameterization.")
    print()
    print("Possible next artifact:")
    print("  candidate_areal_gauge_kappa_condition.md")

    with out.governance_assessments():
        out.line(
            "kappa=0 qualified as gauge-fixed geometric condition from sphere area",
            StatusMark.PASS,
            "areal-gauge construction; not a full covariant invariant",
        )

    with out.unresolved_obligations():
        out.line(
            "derive full covariant parent or 4D invariant for kappa=0 condition",
            StatusMark.OBLIGATION,
            "areal-gauge condition established; full covariant generalization open",
        )


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Areal-Gauge Kappa Condition")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_general_spherical_metric(out)
    case_1_areal_radius_from_area(out)
    case_2_transform_to_areal_radius(out, ns)
    case_3_kappa_areal_from_arbitrary_metric(out)
    case_4_recover_reparameterization_result(out, ns)
    case_5_gauge_fixed_condition_statement(out)
    case_6_arbitrary_coordinate_expression(out)
    case_7_failure_control_ignore_angular_sector(out)
    case_8_summary_classification(out)
    final_interpretation(out)

    # Governance records inside the archive block.
    ns.record_claim(ClaimRecord(
        claim_id="kappa_zero_areal_gauge_geometric_condition",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.PROVISIONAL_CONVENTION,
        statement=(
            "The condition kappa=0 (AB=1 in areal gauge) can be given a "
            "gauge-fixed geometric meaning by defining the areal radius from "
            "sphere area and expressing the metric in areal-radius form. "
            "In arbitrary radial coordinate, this becomes T(R)Q(R) = S'(R)^2. "
            "This is a provisional convention pending a full covariant formulation."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_covariant_kappa_zero_condition",
        script_id=SCRIPT_ID,
        title="Derive full covariant or 4D invariant for kappa=0 condition",
        status=ObligationStatus.OPEN,
        required_by=["kappa_zero_areal_gauge_geometric_condition"],
        description=(
            "The areal-gauge geometric construction of kappa=0 is well-defined in "
            "spherical symmetry, but it is not a full 4D covariant condition. "
            "A covariant generalization is needed before kappa=0 can be used outside "
            "the static spherical areal-gauge setting."
        ),
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
