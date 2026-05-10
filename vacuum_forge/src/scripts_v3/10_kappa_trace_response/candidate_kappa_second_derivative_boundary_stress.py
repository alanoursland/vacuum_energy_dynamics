# Group:
#   10_kappa_trace_response
#
# Script type:
#   SAMPLE
#
# Candidate kappa second derivative boundary stress
#
# Purpose
# -------
# The kappa boundary-layer model found a compact profile:
#
#   kappa(r) = kappa_0 (1 - r^2/R^2)^2
#
# with:
#
#   kappa(R) = 0
#   kappa'(R) = 0
#   F_kappa(R) = 0
#
# so it can match to exterior kappa = 0 without exporting first-derivative flux.
#
# But the next trap is hidden interface stress:
#
#   Does kappa'' jump at R?
#   Does Delta kappa jump?
#   Does a shell source appear?
#
# This script checks second-derivative and effective-source behavior at the
# boundary, and compares the simple C1 profile to a smoother C2 compact profile.
#
# This is a boundary regularity test, not a final interface derivation.

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
    print("=" * 120)
    print(title)
    print("=" * 120)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="kappa_boundary_layer_model_marker",
        upstream_script_id="10_kappa_trace_response__candidate_kappa_boundary_layer_model",
        upstream_derivation_id="kappa_boundary_layer_model_marker",
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


def areal_laplacian(expr, r):
    return sp.simplify(sp.diff(expr, r, 2) + 2*sp.diff(expr, r)/r)


def case_0_problem_statement():
    header("Case 0: Kappa second-derivative boundary stress problem")

    print("Question:")
    print()
    print("  Does a compact interior kappa profile create hidden boundary stress")
    print("  through second-derivative or effective-source jumps?")
    print()
    print("Known from previous model:")
    print()
    print("  kappa(R)=0")
    print("  kappa'(R)=0")
    print("  exterior kappa=0")
    print()
    print("Need now:")
    print()
    print("  check kappa''(R)")
    print("  check Delta kappa(R)")
    print("  decide whether smoother compact profile is required")


def case_1_C1_profile_second_derivatives():
    header("Case 1: C1 compact profile second derivatives")

    r, R, k0 = sp.symbols("r R kappa_0", positive=True, real=True)

    x = r/R
    kappa = k0*(1 - x**2)**2
    dk = sp.simplify(sp.diff(kappa, r))
    d2k = sp.simplify(sp.diff(kappa, r, 2))
    lap = areal_laplacian(kappa, r)

    print("Profile:")
    print()
    print("  kappa = k0 (1 - r^2/R^2)^2")
    print()
    print(f"kappa = {kappa}")
    print()
    print("Boundary values:")
    print()
    print(f"kappa(R) = {sp.simplify(kappa.subs(r, R))}")
    print(f"kappa'(R) = {sp.simplify(dk.subs(r, R))}")
    print(f"kappa''(R-) = {sp.simplify(d2k.subs(r, R))}")
    print(f"Delta kappa(R-) = {sp.simplify(lap.subs(r, R))}")
    print()
    print("Exterior kappa=0 has:")
    print()
    print("  kappa''(R+) = 0")
    print("  Delta kappa(R+) = 0")
    print()
    print("Thus the second derivative/effective source jumps at R.")

    jump_d2 = sp.simplify(d2k.subs(r, R))
    jump_lap = sp.simplify(lap.subs(r, R))

    status = StatusMark.FAIL if (jump_d2 != 0 or jump_lap != 0) else StatusMark.PASS
    print(f"[{status}] C1 profile has second-derivative/effective-source jump")

    return r, R, k0, kappa, d2k, jump_d2, jump_lap


def case_2_C2_profile_candidate(r, R, k0):
    header("Case 2: C2 smoother compact profile candidate")

    x = r/R

    # Higher-power compact profile. This makes value, first derivative, and
    # second derivative vanish at R.
    kappa = k0*(1 - x**2)**3
    dk = sp.simplify(sp.diff(kappa, r))
    d2k = sp.simplify(sp.diff(kappa, r, 2))
    lap = areal_laplacian(kappa, r)

    print("Smoother profile:")
    print()
    print("  kappa = k0 (1 - r^2/R^2)^3")
    print()
    print(f"kappa = {kappa}")
    print()
    print("Boundary values:")
    print()
    print(f"kappa(R) = {sp.simplify(kappa.subs(r, R))}")
    print(f"kappa'(R) = {sp.simplify(dk.subs(r, R))}")
    print(f"kappa''(R-) = {sp.simplify(d2k.subs(r, R))}")
    print(f"Delta kappa(R-) = {sp.simplify(lap.subs(r, R))}")
    print()
    print("This profile matches exterior zero through second derivative/effective source.")

    ok = (
        sp.simplify(kappa.subs(r, R)) == 0
        and sp.simplify(dk.subs(r, R)) == 0
        and sp.simplify(d2k.subs(r, R)) == 0
        and sp.simplify(lap.subs(r, R)) == 0
    )

    status = StatusMark.PASS if ok else StatusMark.FAIL
    print(f"[{status}] C2 profile removes second-derivative/effective-source jump")

    return kappa, lap


def case_3_flux_and_charge_for_C2(r, R, kappa):
    header("Case 3: Flux and charge for C2 profile")

    dk = sp.simplify(sp.diff(kappa, r))
    flux = sp.simplify(4*sp.pi*r**2*dk)
    flux_R = sp.simplify(flux.subs(r, R))
    lap = areal_laplacian(kappa, r)
    source_integral = sp.simplify(4*sp.pi*sp.integrate(r**2*lap, (r, 0, R)))

    print("Flux:")
    print()
    print(f"F_kappa(r) = {flux}")
    print(f"F_kappa(R) = {flux_R}")
    print()
    print("Integrated effective source:")
    print()
    print(f"integral Delta kappa d^3x = {source_integral}")
    print()
    print("C2 profile keeps zero flux and zero net source.")

    ok = sp.simplify(flux_R) == 0 and sp.simplify(source_integral) == 0
    status = StatusMark.PASS if ok else StatusMark.FAIL
    print(f"[{status}] C2 profile has zero flux and zero net effective source")

    return flux_R, source_integral


def case_4_regular_center_check(r, R, k0, kappa):
    header("Case 4: Regular center check")

    dk = sp.simplify(sp.diff(kappa, r))
    d2k = sp.simplify(sp.diff(kappa, r, 2))
    lap = areal_laplacian(kappa, r)

    print("Center values for C2 profile:")
    print()
    print(f"kappa(0) = {sp.simplify(kappa.subs(r, 0))}")
    print(f"kappa'(0) = {sp.simplify(dk.subs(r, 0))}")
    print(f"kappa''(0) = {sp.simplify(d2k.subs(r, 0))}")
    print(f"Delta kappa(0) = {sp.simplify(lap.subs(r, 0))}")
    print()
    print("The profile is regular at the center.")


def case_5_effective_source_shape(r, R, kappa):
    header("Case 5: Effective source shape for C2 profile")

    lap = sp.factor(areal_laplacian(kappa, r))

    print("Effective source shape:")
    print()
    print("  S_eff ~ Delta kappa")
    print()
    print(f"S_eff = {lap}")
    print()
    print("This source shape has positive and negative regions so that net charge")
    print("vanishes.")
    print()
    print("It resembles a compensated trace source rather than raw positive pressure.")


def case_6_interface_interpretation():
    header("Case 6: Interface interpretation")

    print("The C1 profile:")
    print()
    print("  matches value and first derivative")
    print("  but jumps in second derivative/effective source")
    print()
    print("The C2 profile:")
    print()
    print("  matches value, first derivative, and second derivative")
    print("  has zero boundary flux")
    print("  has zero net effective source")
    print()
    print("Interpretation:")
    print("  if hidden shell stress is forbidden, use at least C2 compact profile")
    print("  or derive an allowed boundary layer/interface stress explicitly")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Boundary stress control fails if:")
    print()
    print("1. kappa'' jumps and no interface stress accounts for it.")
    print("2. Delta kappa jumps and implies an unmodeled shell source.")
    print("3. smoother profile cannot be sourced by matter trace/minimum shift.")
    print("4. compensated effective source is inserted by hand.")
    print("5. higher derivative terms in the true action require even higher smoothness.")
    print("6. boundary smoothness hides rather than explains scalar confinement.")


def case_8_classification():
    header("Case 8: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| C1 profile value/first derivative match | DERIVED_REDUCED |")
    print("| C1 profile second derivative jump | RISK |")
    print("| C2 profile value/first/second derivative match | DERIVED_REDUCED |")
    print("| C2 boundary flux zero | DERIVED_REDUCED |")
    print("| C2 net effective source zero | DERIVED_REDUCED |")
    print("| C2 source shape derived from matter trace | MISSING |")
    print("| physical interface law | MISSING |")
    print("| required smoothness from true action | MISSING |")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_boundary_layer_source_compatibility.py")
    print("   Check whether plausible pressure/trace/minimum shift can produce C2 source.")
    print()
    print("2. candidate_kappa_trace_response_status_summary.md")
    print("   Summarize group 10.")
    print()
    print("3. candidate_kappa_action_smoothness_requirement.py")
    print("   Determine smoothness required by candidate kappa action.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_boundary_layer_source_compatibility.py")
    print()
    print("Reason:")
    print("  C2 compactness works mathematically; now source compatibility is the issue.")


def final_interpretation():
    header("Final interpretation")

    print("The previous C1 compact profile avoids exterior flux but has a second")
    print("derivative/effective-source jump at the boundary.")
    print()
    print("A smoother C2 profile:")
    print()
    print("  kappa = k0 (1 - r^2/R^2)^3")
    print()
    print("matches exterior zero through second derivative, keeps boundary flux zero,")
    print("and has zero net effective source.")
    print()
    print("This removes the hidden shell-stress trap at toy level.")
    print()
    print("But source compatibility remains missing.")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_second_derivative_boundary_stress.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_boundary_layer_source_compatibility.py")


def main():
    header("Candidate Kappa Second Derivative Boundary Stress")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    r, R, k0, kappa_c1, d2k_c1, jump_d2, jump_lap = case_1_C1_profile_second_derivatives()
    kappa_c2, lap_c2 = case_2_C2_profile_candidate(r, R, k0)
    flux_R_c2, source_integral_c2 = case_3_flux_and_charge_for_C2(r, R, kappa_c2)
    case_4_regular_center_check(r, R, k0, kappa_c2)
    case_5_effective_source_shape(r, R, kappa_c2)
    case_6_interface_interpretation()
    case_7_failure_controls()
    case_8_classification()
    case_9_next_tests()
    final_interpretation()

    ns.record_derivation(
        derivation_id="C1_kappa_second_derivative_jump_sample",
        inputs=[kappa_c1],
        output=jump_d2,
        method="evaluate kappa''(R-) for kappa=k0*(1-r^2/R^2)^2",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="C1 toy profile only; value nonzero confirms jump risk",
    )

    ns.record_derivation(
        derivation_id="C2_kappa_profile_boundary_regularity_sample",
        inputs=[kappa_c2],
        output=flux_R_c2,
        method=(
            "verify kappa(R)=0, kappa'(R)=0, kappa''(R)=0, Delta_kappa(R)=0, "
            "F_kappa(R)=0 for kappa=k0*(1-r^2/R^2)^3"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="C2 toy profile; higher-order matching; source compatibility not proven",
    )

    ns.record_derivation(
        derivation_id="kappa_second_derivative_boundary_stress_marker",
        inputs=[],
        output=sp.Symbol("kappa_second_derivative_boundary_stress_classified"),
        method="kappa_second_derivative_boundary_stress_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_required_kappa_profile_smoothness_from_action_in_10_kappa_trace",
        script_id=SCRIPT_ID,
        title="Derive the minimum required smoothness of the kappa profile from the candidate action",
        status=ObligationStatus.OPEN,
        description=(
            "The C1 profile has a hidden kappa'' jump (shell stress). C2 resolves it. "
            "Whether C2 is sufficient or higher smoothness is required depends on "
            "derivative terms in the true kappa action. This derivation is missing."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="C2_kappa_profile_removes_hidden_shell_stress",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "The C2 compact profile kappa=k0*(1-r^2/R^2)^3 removes the hidden kappa'' "
            "jump present in the C1 profile, while preserving zero boundary flux and zero "
            "net effective source. This is the preferred toy boundary profile pending "
            "source compatibility and action smoothness derivation."
        ),
    ))

    with out.sample_results():
        out.line("C1 kappa''(R-) is nonzero - second derivative jump confirmed", StatusMark.FAIL, "C1 has hidden shell stress risk")
        out.line("C2 boundary conditions: kappa=0, kappa'=0, kappa''=0, F=0", StatusMark.PASS, "C2 preferred toy profile")

    with out.governance_assessments():
        out.line("C2 profile source compatibility", StatusMark.OBLIGATION, "missing")
        out.line("required smoothness from true action", StatusMark.OBLIGATION, "missing")

    with out.unresolved_obligations():
        out.line("derive required kappa smoothness from action", StatusMark.OBLIGATION, "open")

    out.print_all()

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
