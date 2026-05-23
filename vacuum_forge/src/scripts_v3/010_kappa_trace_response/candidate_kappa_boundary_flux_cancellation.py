# Group:
#   10_kappa_trace_response
#
# Script type:
#   DERIVATION
#
# Candidate kappa boundary flux cancellation
#
# Purpose
# -------
# The kappa scalar-radiation leak check found:
#
#   static projection removes monopole leakage,
#   but scalar-radiation safety also requires dynamic/boundary control.
#
# It rejected:
#
#   ordinary massless hyperbolic kappa
#
# but allowed the possibility of:
#
#   elliptic/constrained kappa,
#   massive/restoring kappa,
#   relaxational/non-wave kappa,
#   short-lived or critically damped breathing response absorbed by vacuum.
#
# This script tests exterior boundary flux:
#
#   F_kappa(R,t) = 4*pi R^2 partial_r kappa(R,t)
#
# and classifies whether boundary behavior:
#
#   1. leaks exterior kappa,
#   2. cancels by projection,
#   3. is Yukawa-suppressed,
#   4. is damped/absorbed,
#   5. remains missing.
#
# This is not a final dynamic derivation.

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
        dependency_id="kappa_scalar_radiation_leak_check_marker",
        upstream_script_id="010_kappa_trace_response__candidate_kappa_scalar_radiation_leak_check",
        upstream_derivation_id="kappa_scalar_radiation_leak_check_marker",
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
    header("Case 0: Kappa boundary flux cancellation problem")

    print("Question:")
    print()
    print("  Does kappa leak through the matter/vacuum boundary?")
    print()
    print("Boundary diagnostic:")
    print()
    print("  F_kappa(R,t) = 4*pi R^2 partial_r kappa(R,t)")
    print()
    print("Required for exterior safety:")
    print()
    print("  no long-range undamped kappa flux to infinity")
    print()
    print("Allowed possibility:")
    print()
    print("  short-lived breathing response if damped/absorbed before becoming")
    print("  ordinary long-range scalar radiation")


def case_1_static_massless_tail_flux():
    header("Case 1: Static massless exterior tail flux")

    r, C1 = sp.symbols("r C1", positive=True, real=True)

    kappa = C1/r
    flux = sp.simplify(4*sp.pi*r**2*sp.diff(kappa, r))

    print("Massless exterior tail:")
    print()
    print(f"kappa = {kappa}")
    print()
    print("Boundary/exterior flux:")
    print()
    print(f"F_kappa = {flux}")
    print()
    print("If C1 != 0, exterior flux is nonzero.")
    print("Thus kappa_ext = C1/r is forbidden unless C1 = 0.")

    return r, kappa, flux


def case_2_projected_zero_charge_flux():
    header("Case 2: Projected zero-charge flux")

    alpha_k, K_k, Q_proj = sp.symbols("alpha_k K_k Q_proj", real=True)

    F = -alpha_k * Q_proj / K_k

    print("For schematic massless Poisson kappa:")
    print()
    print("  -K_k Delta kappa = alpha_k P_0 S_trace")
    print()
    print("Exterior flux is proportional to projected charge:")
    print()
    print(f"F_kappa ~ {F}")
    print()
    print("If:")
    print()
    print("  Q_proj = integral P_0 S_trace d^3x = 0")
    print()
    print("then:")
    print()
    print("  F_kappa = 0")

    return F


def case_3_boundary_matching_condition():
    header("Case 3: Boundary matching condition")

    print("Exterior-safe static matching requires:")
    print()
    print("  kappa(R+) = 0")
    print("  partial_r kappa(R+) = 0")
    print()
    print("or equivalently:")
    print()
    print("  F_kappa(R+) = 0")
    print()
    print("Interior kappa may be nonzero if it is confined, projected, or matched")
    print("through a boundary layer with no exterior flux.")
    print()
    print("This is analogous to permitting interior trace response without exterior")
    print("scalar charge.")


def case_4_yukawa_suppressed_flux():
    header("Case 4: Yukawa-suppressed exterior flux")

    r, C, m = sp.symbols("r C m", positive=True, real=True)

    kappa = C*sp.exp(-m*r)/r
    flux = sp.simplify(4*sp.pi*r**2*sp.diff(kappa, r))

    print("Yukawa exterior:")
    print()
    print(f"kappa = {kappa}")
    print()
    print("Flux:")
    print()
    print(f"F_kappa = {flux}")
    print()
    print("This does not make flux identically zero, but it suppresses it with distance.")
    print("Useful only if m is derived/constrained and the mode is not observable long-range.")

    return r, kappa, flux


def case_5_damped_breathing_boundary_response():
    header("Case 5: Damped breathing boundary response")

    t, omega0, Gamma, A0 = sp.symbols("t omega_0 Gamma A_0", positive=True, real=True)

    # Under-damped representative form. Critical/overdamped cases discussed textually.
    kappa_t = A0*sp.exp(-Gamma*t)*sp.cos(omega0*t)

    print("Representative damped trace/breathing response:")
    print()
    print("  kappa_boundary(t) = A0 exp(-Gamma t) cos(omega0 t)")
    print()
    print(f"kappa_boundary(t) = {kappa_t}")
    print()
    print("If Gamma is large enough, boundary trace perturbations are absorbed before")
    print("becoming long-range scalar radiation.")
    print()
    print("Critical damping condition for oscillator model:")
    print()
    print("  Gamma^2 = 4 omega0^2")
    print()
    print("Allowed only if damping/energy accounting is derived.")

    return kappa_t


def case_6_dynamic_boundary_warning():
    header("Case 6: Dynamic boundary warning")

    print("For moving or time-dependent support:")
    print()
    print("  R = R(t)")
    print("  S_trace = S_trace(r,t)")
    print("  <S_trace>_V = <S_trace>_V(t)")
    print()
    print("Projection can create boundary terms:")
    print()
    print("  d/dt integral_V(t) P_0 S d^3x")
    print()
    print("Even if the instantaneous charge is zero, boundary motion may create")
    print("effective flux terms unless the constraint propagates consistently.")
    print()
    print("This is currently unresolved.")


def case_7_classification():
    header("Case 7: Classification")

    print("| Boundary behavior | Status |")
    print("|---|---|")
    print("| massless 1/r tail | REJECTED / RISK |")
    print("| projected zero-charge static flux | CONSTRAINED_BY_IDENTITY |")
    print("| kappa(R+)=0 and kappa'(R+)=0 | CONSTRAINED_BY_IDENTITY |")
    print("| Yukawa suppressed exterior | PLAUSIBLE if m_k derived |")
    print("| damped/critically damped breathing | PLAUSIBLE if Gamma and energy accounting derived |")
    print("| moving support projection | RISK / unresolved |")


def case_8_failure_controls():
    header("Case 8: Failure controls")

    print("Boundary flux cancellation fails if:")
    print()
    print("1. F_kappa(R+) != 0 in a massless exterior.")
    print("2. kappa has a persistent 1/r tail.")
    print("3. damped breathing response carries energy to infinity before absorption.")
    print("4. Gamma is inserted by hand only to hide scalar radiation.")
    print("5. Yukawa scale m_k is inserted by hand only to hide scalar radiation.")
    print("6. moving support creates uncancelled flux terms.")
    print("7. suppression interferes with static A-sector gravity.")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_projection_parent_balance.py")
    print("   Connect P_0 and F_kappa=0 to vacuum-substance balance.")
    print()
    print("2. candidate_kappa_relaxation_energy_accounting.py")
    print("   Test whether damping/absorption can conserve or dissipate energy consistently.")
    print()
    print("3. candidate_kappa_boundary_layer_model.py")
    print("   Model confined interior kappa with boundary layer and zero exterior flux.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_relaxation_energy_accounting.py")
    print()
    print("Reason:")
    print("  User-raised possibility: breathing response may be absorbed by vacuum.")
    print("  That requires energy/damping accounting.")


def final_interpretation():
    header("Final interpretation")

    print("Static exterior safety requires:")
    print()
    print("  F_kappa(R+) = 0")
    print()
    print("Massless 1/r tails are rejected.")
    print()
    print("But a breathing response is not automatically fatal if:")
    print()
    print("  it is damped, absorbed, massive, constrained, or boundary-confined")
    print()
    print("and does not become ordinary long-range scalar radiation.")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_boundary_flux_cancellation.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_relaxation_energy_accounting.py")


def main():
    header("Candidate Kappa Boundary Flux Cancellation")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    r_tail, kappa_tail, flux_tail = case_1_static_massless_tail_flux()
    F_zero = case_2_projected_zero_charge_flux()
    case_3_boundary_matching_condition()
    r_yukawa, kappa_yukawa, flux_yukawa = case_4_yukawa_suppressed_flux()
    kappa_t = case_5_damped_breathing_boundary_response()
    case_6_dynamic_boundary_warning()
    case_7_classification()
    case_8_failure_controls()
    case_9_next_tests()
    final_interpretation()

    # Real algebraic computations
    ns.record_derivation(
        derivation_id="massless_1_over_r_kappa_flux_residual",
        inputs=[kappa_tail],
        output=flux_tail,
        method="compute 4*pi*r^2 * d/dr(C1/r)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
    )

    ns.record_derivation(
        derivation_id="yukawa_kappa_exterior_flux",
        inputs=[kappa_yukawa],
        output=flux_yukawa,
        method="compute 4*pi*r^2 * d/dr(C*exp(-m*r)/r)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
    )

    ns.record_derivation(
        derivation_id="kappa_boundary_flux_cancellation_marker",
        inputs=[],
        output=sp.Symbol("kappa_boundary_flux_cancellation_classified"),
        method="kappa_boundary_flux_cancellation_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_boundary_flux_zero_condition_in_10_kappa_trace",
        script_id=SCRIPT_ID,
        title="Derive the mechanism enforcing zero exterior boundary flux F_kappa(R+)=0",
        status=ObligationStatus.OPEN,
        description=(
            "Static exterior safety requires F_kappa(R+) = 0. The massless 1/r tail "
            "gives nonzero flux (C1 * (-4*pi)). Dynamic boundary motion adds further "
            "terms. A derivation of the mechanism ensuring zero exterior flux is required."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="massless_kappa_1_over_r_tail_flux_nonzero",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.OPEN_RISK,
        statement=(
            "The massless exterior tail kappa=C1/r has F_kappa = -4*pi*C1 (nonzero), "
            "confirming that a 1/r exterior kappa tail violates the required boundary "
            "flux cancellation condition F_kappa(R+)=0."
        ),
    ))

    with out.derived_results():
        out.line("massless 1/r tail exterior flux F_kappa = -4*pi*C1", StatusMark.PASS, "algebraic derivation")
        out.line("Yukawa exterior flux expression", StatusMark.PASS, "algebraic derivation")

    with out.governance_assessments():
        out.line("massless 1/r tail", StatusMark.FAIL, "exterior flux nonzero - forbidden")
        out.line("dynamic boundary projection", StatusMark.FAIL, "open risk - unresolved")
        out.line("boundary flux zero condition", StatusMark.OBLIGATION, "mechanism missing")

    with out.unresolved_obligations():
        out.line("derive F_kappa(R+)=0 mechanism", StatusMark.OBLIGATION, "open")

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
