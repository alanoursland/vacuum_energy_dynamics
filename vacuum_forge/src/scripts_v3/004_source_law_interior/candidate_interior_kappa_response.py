# Group:
#   04_source_law_interior
#
# Script type:
#   DIAGNOSTIC
#
# Candidate interior kappa response
#
# Purpose
# -------
# Compare whether kappa should be forced to zero inside matter or allowed to
# respond to traceful matter sources while still relaxing to zero outside.

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
    RouteRecord,
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
    ns.declare_dependency(
        dependency_id="gr_interior_first_order_match",
        upstream_script_id="04_source_law_interior__candidate_compare_gr_interior_schwarzschild",
        upstream_derivation_id="gr_interior_first_order_match",
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


def case_0_recap(out: ScriptOutput):
    header("Case 0: Reduced mode recap")
    print("A = exp(kappa+s)")
    print("B = exp(kappa-s)")
    print("AB = exp(2*kappa)")
    print()
    print("Exterior compensation:")
    print("  kappa = 0")
    print("  AB = 1")
    print("  B = 1/A")
    print()
    print("Interior question:")
    print("  Should kappa=0 hold inside matter?")
    print("  Or can matter source kappa inside while exterior kappa relaxes to zero?")

    with out.governance_assessments():
        out.line("interior kappa question isolated",
                 StatusMark.PASS,
                 "kappa=0 is established exterior/source-free condition; interior remains open")

    with out.unresolved_obligations():
        out.line("derive interior kappa condition from matter coupling",
                 StatusMark.OBLIGATION,
                 "no first-principles derivation of whether kappa=0 holds inside matter")


def case_1_forced_interior_compensation(out: ScriptOutput):
    header("Case 1: Forced interior compensation")

    r, R, G, c, rho0 = sp.symbols("r R G c rho0", positive=True, real=True)

    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)
    kappa_in = sp.Integer(0)
    B_in = sp.simplify(sp.exp(2*kappa_in) / A_in)
    AB = sp.simplify(A_in * B_in)

    print(f"A_in = {A_in}")
    print(f"kappa_in = {kappa_in}")
    print(f"B_in = exp(2*kappa)/A = {B_in}")
    print(f"A_in B_in = {AB}")

    with out.sample_results():
        out.line("forced kappa=0 gives reciprocal interior",
                 StatusMark.PASS if is_zero(AB - 1) else StatusMark.FAIL,
                 "by-construction when kappa=0 is imposed")

    print()
    print("Caution:")
    print("  This is the simplest interior extension, but it may be too strong.")
    print("  It excludes traceful matter response in kappa.")


def case_2_generic_traceful_kappa_source(out: ScriptOutput, ns=None):
    header("Case 2: Generic traceful kappa source inside matter")

    r, R, G, c, rho0, eta = sp.symbols("r R G c rho0 eta", positive=True, real=True)

    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)
    kappa_in = eta * G * rho0 * (R**2 - r**2) / c**2

    B_in = sp.simplify(sp.exp(2*kappa_in) / A_in)
    AB = sp.simplify(A_in * B_in)

    kappa_R = sp.simplify(kappa_in.subs(r, R))
    dkappa_R = sp.simplify(sp.diff(kappa_in, r).subs(r, R))
    kappa_0 = sp.simplify(kappa_in.subs(r, 0))
    dkappa_0 = sp.simplify(sp.diff(kappa_in, r).subs(r, 0))

    print(f"A_in = {A_in}")
    print(f"kappa_in = {kappa_in}")
    print(f"B_in = exp(2*kappa)/A = {B_in}")
    print(f"A_in B_in = {AB}")
    print()
    print(f"kappa_in(R) = {kappa_R}")
    print(f"kappa_in'(R) = {dkappa_R}")
    print(f"kappa_in(0) = {kappa_0}")
    print(f"kappa_in'(0) = {dkappa_0}")

    with out.sample_results():
        out.line("interior kappa can vanish at boundary",
                 StatusMark.PASS if is_zero(kappa_R) else StatusMark.FAIL,
                 f"kappa_in(R) = {kappa_R}")
        out.line("interior kappa is regular at origin",
                 StatusMark.PASS if is_zero(dkappa_0) else StatusMark.FAIL,
                 f"kappa_in'(0) = {dkappa_0}")
        out.line("nonzero interior kappa breaks reciprocal interior generically",
                 StatusMark.PASS if not is_zero(AB - 1) else StatusMark.FAIL)
        out.line("boundary derivative may jump unless exterior layer handles it",
                 StatusMark.PASS if not is_zero(dkappa_R) else StatusMark.FAIL,
                 f"kappa_in'(R) = {dkappa_R}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="generic_traceful_kappa_boundary_check",
            inputs=[kappa_in, r, R],
            output=kappa_R,
            method="kappa_in(R) = eta*G*rho0*(R^2-R^2)/c^2",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="toy traceful kappa profile, constant density, linear ansatz",
        )


def case_3_smooth_boundary_kappa_profile(out: ScriptOutput, ns=None):
    header("Case 3: Smooth boundary kappa profile")

    r, R, G, c, rho0, eta = sp.symbols("r R G c rho0 eta", positive=True, real=True)
    kappa_in = eta * G * rho0 * (R**2 - r**2)**2 / (c**2 * R**2)

    kappa_R = sp.simplify(kappa_in.subs(r, R))
    dkappa_R = sp.simplify(sp.diff(kappa_in, r).subs(r, R))
    dkappa_0 = sp.simplify(sp.diff(kappa_in, r).subs(r, 0))

    print(f"kappa_in = {kappa_in}")
    print(f"kappa_in(R) = {kappa_R}")
    print(f"kappa_in'(R) = {dkappa_R}")
    print(f"kappa_in'(0) = {dkappa_0}")

    with out.sample_results():
        out.line("kappa vanishes at boundary",
                 StatusMark.PASS if is_zero(kappa_R) else StatusMark.FAIL,
                 f"kappa(R) = {kappa_R}")
        out.line("kappa derivative vanishes at boundary",
                 StatusMark.PASS if is_zero(dkappa_R) else StatusMark.FAIL,
                 f"kappa'(R) = {dkappa_R}")
        out.line("kappa regular at origin",
                 StatusMark.PASS if is_zero(dkappa_0) else StatusMark.FAIL,
                 f"kappa'(0) = {dkappa_0}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="smooth_boundary_kappa_profile_check",
            inputs=[kappa_in, r, R],
            output=sp.Matrix([kappa_R, dkappa_R, dkappa_0]),
            method="kappa = eta*G*rho0*(R^2-r^2)^2/(c^2*R^2) profile check",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="quartic smooth kappa profile",
        )


def case_4_energy_penalty_model(out: ScriptOutput, ns=None):
    header("Case 4: Interior kappa energy penalty model")

    kappa, C_k, J_k = sp.symbols("kappa C_k J_k", positive=True, real=True)

    E = C_k*kappa**2 - J_k*kappa
    eq = sp.Eq(sp.diff(E, kappa), 0)
    sol = sp.solve(eq, kappa)

    print(f"E = {E}")
    print(f"Stationary equation: {eq}")
    print(f"kappa solution = {sol}")
    print()
    print("If J_k is nonzero inside matter, kappa responds.")
    print("If J_k=0 outside, kappa relaxes to zero.")

    with out.derived_results():
        out.line("traceful source produces interior kappa response",
                 StatusMark.PASS if bool(sol) else StatusMark.FAIL,
                 f"kappa_eq = {sol}")

    ctx = TheoryContext("candidate_interior_kappa_response")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    ctx.energy.source_coupled(
        C_kappa=ms.C_kappa,
        C_sigma=ms.C_sigma,
        J_kappa=J_k,
        J_sigma=sp.Integer(0),
        kappa=ms.kappa,
        sigma=ms.sigma,
    )
    vf_sol = ctx.energy.solve_stationary("source_coupled_energy")
    if vf_sol.solutions:
        k_eq = sp.simplify(vf_sol.solutions[0][ms.kappa])
        expected = J_k / (2 * ms.C_kappa)
        vf_ok = is_zero(k_eq - expected)

        with out.derived_results():
            out.line("VacuumForge reproduces interior kappa response",
                     StatusMark.PASS if vf_ok else StatusMark.FAIL,
                     f"kappa_eq = {k_eq}")

        if ns is not None:
            ns.record_derivation(
                derivation_id="interior_kappa_energy_response",
                inputs=[J_k],
                output=sp.Eq(ms.kappa, J_k / (2 * ms.C_kappa)),
                method="vacuumforge_source_coupled_energy",
                status=Status.DERIVED,
                record_kind=RecordKind.SAMPLE_DERIVATION,
                scope="quadratic kappa energy with traceful source J_k",
            )


def case_5_exterior_matching_classification(out: ScriptOutput):
    header("Case 5: Exterior matching classification")

    print("Interior/exterior possibilities:")
    print()
    print("A. kappa=0 everywhere")
    print("   - simplest")
    print("   - reciprocal interior")
    print("   - not GR interior")
    print()
    print("B. kappa sourced inside, kappa(R)=0")
    print("   - exterior remains compensated")
    print("   - interior can carry traceful matter response")
    print("   - boundary derivative may need interface physics")
    print()
    print("C. kappa sourced inside, kappa(R)=kappa_R != 0")
    print("   - exterior begins with nonzero kappa")
    print("   - reciprocal exterior may fail unless relaxation layer suppresses it")
    print()
    print("D. smooth interior kappa with kappa(R)=kappa'(R)=0")
    print("   - cleanest coexistence of interior trace response and exterior compensation")

    with out.governance_assessments():
        out.line("classification separates interior matter response from exterior compensation",
                 StatusMark.PASS,
                 "options A-D represent distinct physical routes")

    with out.unresolved_obligations():
        out.line("derive which interior/exterior kappa option applies",
                 StatusMark.OBLIGATION,
                 "no first-principles derivation selects option A, B, C, or D")


def case_6_observable_exterior_pressure(out: ScriptOutput, ns=None):
    header("Case 6: Exterior pressure from kappa leakage")

    eps, lam = sp.symbols("eps lambda_k", real=True)

    kappa_ext = lam * eps
    s_ext = -2 * eps

    A = sp.exp(kappa_ext + s_ext)
    B = sp.exp(kappa_ext - s_ext)
    AB = sp.simplify(A*B)

    A_first = sp.series(A, eps, 0, 2).removeO()
    B_first = sp.series(B, eps, 0, 2).removeO()
    AB_first = sp.series(AB, eps, 0, 2).removeO()

    print("If interior kappa leaks into exterior as kappa=lambda_k eps:")
    print(f"A approx {A_first}")
    print(f"B approx {B_first}")
    print(f"AB approx {AB_first}")
    print()
    print("Exterior kappa leak is observationally dangerous.")

    with out.governance_assessments():
        out.line("exterior kappa must be suppressed or tightly bounded",
                 StatusMark.PASS,
                 "nonzero exterior kappa shifts weak-field coefficients")

    if ns is not None:
        ns.record_derivation(
            derivation_id="exterior_kappa_leak_weak_field_shift",
            inputs=[kappa_ext, s_ext, eps],
            output=AB_first,
            method="series expansion of A*B to first order in eps",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="first-order weak-field kappa leak diagnostic",
        )


def final_interpretation():
    header("Final interpretation")

    print("This script supports a refined interior/exterior picture:")
    print()
    print("  Exterior source-free region:")
    print("    kappa should relax to zero.")
    print()
    print("  Interior matter region:")
    print("    kappa may be forced to zero as a simple model,")
    print("    or may respond to traceful matter sources.")
    print()
    print("A nonzero interior kappa is not automatically fatal if:")
    print("  kappa -> 0 at the surface or through a boundary layer,")
    print("  exterior kappa remains suppressed,")
    print("  and no kappa leak persists into weak-field exterior observations.")
    print()
    print("Possible next artifact:")
    print("  candidate_interior_kappa_response.md")


def main():
    header("Candidate Interior Kappa Response")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_recap(out)
    case_1_forced_interior_compensation(out)
    case_2_generic_traceful_kappa_source(out, ns)
    case_3_smooth_boundary_kappa_profile(out, ns)
    case_4_energy_penalty_model(out, ns)
    case_5_exterior_matching_classification(out)
    case_6_observable_exterior_pressure(out, ns)
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_interior_exterior_kappa_option",
        script_id=SCRIPT_ID,
        title="Derive which interior/exterior kappa option applies from first principles",
        status=ObligationStatus.OPEN,
        description=(
            "Four options are identified: kappa=0 everywhere, interior kappa with "
            "kappa(R)=0, interior kappa with kappa(R)!=0, or smooth interior kappa "
            "with kappa(R)=kappa'(R)=0. No first-principles derivation has selected "
            "among these options."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_interior_kappa_source_law",
        script_id=SCRIPT_ID,
        title="Derive interior kappa source law from matter coupling",
        status=ObligationStatus.OPEN,
        description=(
            "If kappa is sourced inside matter, the source law J_k must be derived "
            "from a matter coupling. The toy energy model only establishes the "
            "response structure; the source origin is missing."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="exterior_kappa_must_be_suppressed",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Any persistent exterior kappa shifts weak-field coefficients and creates "
            "an observational deviation channel. The exterior kappa must be suppressed "
            "or tightly bounded regardless of the interior kappa option."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="smooth_interior_kappa_vanishing_at_surface_route",
        script_id=SCRIPT_ID,
        name="Smooth interior kappa vanishing at surface (option D)",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_interior_exterior_kappa_option",
                              "derive_interior_kappa_source_law"],
    ))

    ns.write_run_metadata()

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
