# Group:
#   10_kappa_trace_response
#
# Script type:
#   SAMPLE
#
# Candidate kappa boundary layer model
#
# Purpose
# -------
# The non-inertial kappa relaxation model found:
#
#   kappa is not a wave,
#   kappa is a non-inertial trace/volume relaxation coordinate,
#   matter trace shifts the local vacuum-curvature minimum,
#   kappa relaxes monotonically toward that minimum,
#   there is no independent kappa momentum channel.
#
# This fits the earlier rule:
#
#   propagating breathing waves are not allowed.
#
# The next concrete issue is the boundary:
#
#   interior kappa may exist,
#   exterior kappa must vanish,
#   exterior flux must vanish.
#
# This script builds toy boundary-layer profiles that satisfy:
#
#   kappa(R+) = 0
#   partial_r kappa(R+) = 0
#
# while allowing interior trace response.
#
# This is not a derived matter/vacuum interface theory.
# It is a boundary-control model.

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
        dependency_id="kappa_noninertial_vacuum_curvature_relaxation_marker",
        upstream_script_id="10_kappa_trace_response__candidate_kappa_noninertial_vacuum_curvature_relaxation",
        upstream_derivation_id="kappa_noninertial_vacuum_curvature_relaxation_marker",
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


def case_0_problem_statement():
    header("Case 0: Kappa boundary-layer problem")

    print("Question:")
    print()
    print("  Can interior kappa exist while exterior kappa and exterior flux vanish?")
    print()
    print("Boundary requirements:")
    print()
    print("  kappa(R+) = 0")
    print("  partial_r kappa(R+) = 0")
    print()
    print("Goal:")
    print()
    print("  allow interior trace/volume response")
    print("  forbid exterior kappa tail")
    print("  forbid propagating breathing leakage")


def case_1_simple_profile():
    header("Case 1: Smooth compact interior profile")

    r, R, k0 = sp.symbols("r R kappa_0", positive=True, real=True)

    # Smooth profile with kappa(R)=0 and kappa'(R)=0.
    x = r/R
    kappa = k0 * (1 - x**2)**2
    dk = sp.simplify(sp.diff(kappa, r))

    kappa_R = sp.simplify(kappa.subs(r, R))
    dk_R = sp.simplify(dk.subs(r, R))
    kappa_0_val = sp.simplify(kappa.subs(r, 0))
    dk_0 = sp.simplify(dk.subs(r, 0))

    print("Toy compact interior profile:")
    print()
    print("  kappa(r) = kappa_0 (1 - r^2/R^2)^2")
    print()
    print(f"kappa(r) = {kappa}")
    print()
    print("Boundary values:")
    print()
    print(f"kappa(R) = {kappa_R}")
    print(f"kappa'(R) = {dk_R}")
    print()
    print("Center values:")
    print()
    print(f"kappa(0) = {kappa_0_val}")
    print(f"kappa'(0) = {dk_0}")

    ok = sp.simplify(kappa_R) == 0 and sp.simplify(dk_R) == 0

    StatusMark_val = StatusMark.PASS if ok else StatusMark.FAIL
    print(f"[{StatusMark_val}] smooth compact profile has zero value and flux at boundary")

    return r, R, k0, kappa, dk


def case_2_boundary_flux(r, R, kappa, dk):
    header("Case 2: Boundary flux diagnostic")

    flux = sp.simplify(4*sp.pi*r**2*dk)
    flux_R = sp.simplify(flux.subs(r, R))

    print("Flux diagnostic:")
    print()
    print("  F_kappa(r) = 4*pi r^2 kappa'(r)")
    print()
    print(f"F_kappa(r) = {flux}")
    print()
    print("At boundary:")
    print()
    print(f"F_kappa(R) = {flux_R}")

    ok = sp.simplify(flux_R) == 0
    StatusMark_val = StatusMark.PASS if ok else StatusMark.FAIL
    print(f"[{StatusMark_val}] boundary flux vanishes")

    return flux, flux_R


def case_3_no_exterior_tail():
    header("Case 3: Exterior extension")

    print("Define exterior:")
    print()
    print("  kappa_ext(r>R) = 0")
    print()
    print("Since the interior profile satisfies:")
    print()
    print("  kappa(R-) = 0")
    print("  kappa'(R-) = 0")
    print()
    print("and exterior satisfies:")
    print()
    print("  kappa(R+) = 0")
    print("  kappa'(R+) = 0")
    print()
    print("there is no jump in value or first derivative.")
    print()
    print("Thus no exterior 1/r tail is required by matching.")


def case_4_effective_source_from_profile(r, R, k0, kappa):
    header("Case 4: Effective source implied by profile")

    lap = sp.simplify(sp.diff(kappa, r, 2) + 2*sp.diff(kappa, r)/r)

    print("If a schematic elliptic operator is used:")
    print()
    print("  Delta_areal kappa = kappa'' + 2 kappa'/r")
    print()
    print("then the toy profile implies:")
    print()
    print(f"Delta kappa = {lap}")
    print()
    print("This is the effective source shape needed to support the boundary-confined profile.")
    print()
    print("It is not derived from matter trace yet.")

    return lap


def case_5_source_integral_check(r, R, kappa):
    header("Case 5: Effective source integral check")

    lap = sp.simplify(sp.diff(kappa, r, 2) + 2*sp.diff(kappa, r)/r)
    integral = sp.simplify(4*sp.pi*sp.integrate(r**2*lap, (r, 0, R)))

    print("Integrated Laplacian source:")
    print()
    print("  integral Delta kappa d^3x")
    print()
    print(f"= {integral}")
    print()
    print("By divergence theorem this equals boundary flux.")
    print("Since boundary flux is zero, the integrated source is zero.")
    print()
    print("This matches the zero-charge projection idea.")

    ok = sp.simplify(integral) == 0
    StatusMark_val = StatusMark.PASS if ok else StatusMark.FAIL
    print(f"[{StatusMark_val}] effective source has zero net charge")

    return integral


def case_6_boundary_layer_interpretation():
    header("Case 6: Boundary-layer interpretation")

    print("The toy profile shows a possible pattern:")
    print()
    print("  kappa can be nonzero inside matter")
    print("  kappa can relax to zero at the boundary")
    print("  kappa' can also vanish at the boundary")
    print("  exterior kappa can be identically zero")
    print()
    print("Interpretation:")
    print("  trace/volume response is interior-confined")
    print("  no scalar charge is exported")
    print("  no exterior breathing field is launched")
    print()
    print("But:")
    print("  the profile is chosen, not derived.")


def case_7_noninertial_compatibility():
    header("Case 7: Compatibility with non-inertial relaxation")

    print("The profile is compatible with non-inertial relaxation if:")
    print()
    print("  kappa_min(r) is nonzero inside matter")
    print("  kappa_min(R) = 0")
    print("  kappa_min'(R) = 0")
    print("  exterior kappa_min = 0")
    print()
    print("Then kappa can relax locally toward kappa_min without carrying")
    print("momentum through the boundary.")
    print()
    print("This realizes:")
    print()
    print("  local trace relaxation")
    print("  no propagating breathing wave")


def case_8_failure_controls():
    header("Case 8: Failure controls")

    print("The boundary-layer model fails if:")
    print()
    print("1. kappa'(R+) is nonzero and exports flux.")
    print("2. profile requires an unphysical shell source at R.")
    print("3. second derivative jump creates hidden boundary stress.")
    print("4. chosen profile cannot be produced by trace/pressure source.")
    print("5. boundary confinement is inserted only to hide scalar radiation.")
    print("6. non-inertial relaxation secretly includes a second-order wave channel.")


def case_9_classification():
    header("Case 9: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| compact profile kappa = k0(1-r^2/R^2)^2 | PLAUSIBLE toy model |")
    print("| kappa(R)=0 | DERIVED_REDUCED |")
    print("| kappa'(R)=0 | DERIVED_REDUCED |")
    print("| boundary flux F_kappa(R)=0 | DERIVED_REDUCED |")
    print("| exterior kappa=0 extension | CONSTRAINED_BY_IDENTITY |")
    print("| effective source integral zero | DERIVED_REDUCED |")
    print("| source/interface derivation | MISSING |")
    print("| hidden boundary stress check | MISSING |")


def case_10_next_tests():
    header("Case 10: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_boundary_layer_source_compatibility.py")
    print("   Check whether plausible pressure/trace source can produce the compact profile.")
    print()
    print("2. candidate_kappa_trace_response_status_summary.md")
    print("   Summarize group 10 current status.")
    print()
    print("3. candidate_kappa_second_derivative_boundary_stress.py")
    print("   Check hidden shell/boundary stress from derivative jumps.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_second_derivative_boundary_stress.py")
    print()
    print("Reason:")
    print("  Value and flux match, but second derivative/interface stress is the next trap.")


def final_interpretation():
    header("Final interpretation")

    print("A toy compact kappa profile can allow:")
    print()
    print("  interior kappa response")
    print("  kappa(R)=0")
    print("  kappa'(R)=0")
    print("  F_kappa(R)=0")
    print("  exterior kappa=0")
    print()
    print("This supports the idea that kappa can be an interior, non-propagating")
    print("trace relaxation variable rather than a breathing wave.")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_boundary_layer_model.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_second_derivative_boundary_stress.py")


def main():
    header("Candidate Kappa Boundary Layer Model")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    r, R, k0, kappa, dk = case_1_simple_profile()
    flux, flux_R = case_2_boundary_flux(r, R, kappa, dk)
    case_3_no_exterior_tail()
    lap = case_4_effective_source_from_profile(r, R, k0, kappa)
    integral = case_5_source_integral_check(r, R, kappa)
    case_6_boundary_layer_interpretation()
    case_7_noninertial_compatibility()
    case_8_failure_controls()
    case_9_classification()
    case_10_next_tests()
    final_interpretation()

    with archive:
        ns.record_derivation(
            derivation_id="compact_kappa_profile_boundary_conditions_sample",
            inputs=[kappa],
            output=flux_R,
            method="compute kappa(R), kappa'(R), F_kappa(R) for kappa=kappa_0*(1-r^2/R^2)^2",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="toy parabolic-square profile; not derived from trace or relaxation law",
        )

        ns.record_derivation(
            derivation_id="compact_kappa_profile_zero_net_source_sample",
            inputs=[kappa, lap],
            output=integral,
            method="integrate 4*pi*r^2*Delta_kappa from 0 to R; verify = 0",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="toy profile; divergence theorem argument",
        )

        ns.record_derivation(
            derivation_id="kappa_boundary_layer_model_marker",
            inputs=[],
            output=sp.Symbol("kappa_boundary_layer_model_classified"),
            method="kappa_boundary_layer_model_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_kappa_boundary_interface_source_in_10_kappa_trace",
            script_id=SCRIPT_ID,
            title="Derive the boundary interface source law that produces the compact kappa profile",
            status=ObligationStatus.OPEN,
            description=(
                "The toy compact profile kappa=kappa_0*(1-r^2/R^2)^2 satisfies boundary "
                "conditions by construction. A physical derivation of the interface source "
                "or kappa_min(r) that produces this profile from matter trace is required."
            ),
        ))

        ns.record_claim(ClaimRecord(
            claim_id="compact_kappa_profile_is_boundary_safe_toy",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=(
                "The compact profile kappa=kappa_0*(1-r^2/R^2)^2 satisfies kappa(R)=0, "
                "kappa'(R)=0, F_kappa(R)=0, and zero net effective source charge. "
                "This is a toy demonstration that interior-confined kappa is structurally "
                "possible. Source/interface derivation remains missing."
            ),
        ))

        with out.sample_results():
            out.line("kappa(R)=0, kappa'(R)=0, F_kappa(R)=0 for compact profile", StatusMark.PASS, "sample - toy profile")
            out.line("integrated effective source = 0", StatusMark.PASS, "sample - divergence theorem")

        with out.governance_assessments():
            out.line("boundary-confined kappa structurally possible", StatusMark.PASS, "toy model confirmed")
            out.line("interface source derivation", StatusMark.OBLIGATION, "missing")
            out.line("hidden boundary stress check", StatusMark.OBLIGATION, "not yet done")

        with out.unresolved_obligations():
            out.line("derive boundary interface source law", StatusMark.OBLIGATION, "open")

        out.print_all()

        ns.write_run_metadata()


if __name__ == "__main__":
    main()
