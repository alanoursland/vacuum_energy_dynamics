# Group:
#   04_source_law_interior
#
# Script type:
#   DIAGNOSTIC
#
# Candidate boundary kappa relaxation layer
#
# Purpose
# -------
# Interior studies suggest kappa may be nonzero inside matter, while exact
# Schwarzschild exterior recovery requires:
#
#   kappa_ext = 0
#
# This script tests simple boundary/interface relaxation profiles that carry
# interior kappa to exterior kappa=0.
#
# It does not solve a full field equation. It checks profile classes and
# matching conditions:
#
#   1. sharp boundary cutoff,
#   2. smooth polynomial boundary layer,
#   3. exponential exterior relaxation,
#   4. energy penalty toy,
#   5. exterior leak suppression.

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


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Problem statement")

    print("Interior matter may source kappa.")
    print("Exterior source-free region should suppress kappa.")
    print()
    print("Need:")
    print("  kappa_inside may be nonzero")
    print("  kappa_exterior -> 0")
    print("  weak-field exterior kappa leak must be tiny or absent")
    print()
    print("This script tests boundary relaxation profile classes.")

    with out.governance_assessments():
        out.line("boundary kappa relaxation problem isolated",
                 StatusMark.PASS,
                 "interior kappa nonzero; exterior suppression required")

    with out.unresolved_obligations():
        out.line("derive boundary kappa relaxation mechanism from field equation",
                 StatusMark.OBLIGATION,
                 "profiles tested here are toy/diagnostic; no full field equation derived")


def case_1_sharp_cutoff(out: ScriptOutput):
    header("Case 1: Sharp cutoff profile")

    r, R, k0 = sp.symbols("r R k0", positive=True, real=True)

    print("Toy profile:")
    print("  kappa = k0 inside")
    print("  kappa = 0 outside")
    print()
    print("This enforces exterior compensation but creates a derivative/jump")
    print("localized at the boundary.")
    print()

    with out.governance_assessments():
        out.line("sharp cutoff needs interface stress or boundary condition",
                 StatusMark.PASS,
                 "kappa jump requires boundary physics; exterior compensation enforced by hand")


def case_2_smooth_polynomial_inside(out: ScriptOutput, ns=None):
    header("Case 2: Smooth polynomial interior profile")

    r, R, k0 = sp.symbols("r R k0", positive=True, real=True)

    # Smooth inside profile with kappa(R)=0 and kappa'(R)=0:
    kappa = k0 * (1 - (r/R)**2)**2

    k_R = sp.simplify(kappa.subs(r, R))
    dk_R = sp.simplify(sp.diff(kappa, r).subs(r, R))
    dk_0 = sp.simplify(sp.diff(kappa, r).subs(r, 0))

    print(f"kappa_in(r) = {kappa}")
    print(f"kappa(R) = {k_R}")
    print(f"kappa'(R) = {dk_R}")
    print(f"kappa'(0) = {dk_0}")

    with out.sample_results():
        out.line("profile vanishes at boundary",
                 StatusMark.PASS if is_zero(k_R) else StatusMark.FAIL,
                 f"kappa(R) = {k_R}")
        out.line("profile derivative vanishes at boundary",
                 StatusMark.PASS if is_zero(dk_R) else StatusMark.FAIL,
                 f"kappa'(R) = {dk_R}")
        out.line("profile regular at center",
                 StatusMark.PASS if is_zero(dk_0) else StatusMark.FAIL,
                 f"kappa'(0) = {dk_0}")

    print()
    print("Interpretation:")
    print("  Smooth interior kappa can die at the surface without exterior leak.")

    if ns is not None:
        ns.record_derivation(
            derivation_id="smooth_polynomial_kappa_profile_check",
            inputs=[kappa, r, R],
            output=sp.Matrix([k_R, dk_R, dk_0]),
            method="kappa = k0*(1-(r/R)^2)^2 boundary and regularity check",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="quartic polynomial interior kappa profile",
        )


def case_3_exponential_exterior_relaxation(out: ScriptOutput, ns=None):
    header("Case 3: Exponential exterior relaxation")

    r, R, kR, L = sp.symbols("r R kR L", positive=True, real=True)

    kappa_ext = kR * sp.exp(-(r - R)/L)
    k_at_R = sp.simplify(kappa_ext.subs(r, R))
    asymptotic = sp.limit(kappa_ext, r, sp.oo)
    derivative_R = sp.simplify(sp.diff(kappa_ext, r).subs(r, R))

    print(f"kappa_ext(r) = {kappa_ext}")
    print(f"kappa_ext(R) = {k_at_R}")
    print(f"lim r->inf kappa_ext = {asymptotic}")
    print(f"kappa_ext'(R) = {derivative_R}")

    with out.sample_results():
        out.line("exterior relaxation decays asymptotically",
                 StatusMark.PASS if is_zero(asymptotic) else StatusMark.FAIL,
                 f"lim = {asymptotic}")

    print()
    print("Caution:")
    print("  Any nonzero exterior tail is an observational kappa-leak channel.")
    print("  For ordinary exterior Schwarzschild recovery, prefer kR=0 or very")
    print("  short relaxation length.")

    with out.governance_assessments():
        out.line("exponential exterior tail is a kappa-leak risk",
                 StatusMark.PASS,
                 "kR must be very small or relaxation scale L very short to avoid deviation")

    if ns is not None:
        ns.record_derivation(
            derivation_id="exponential_exterior_kappa_decay_check",
            inputs=[kappa_ext, r, R, L],
            output=asymptotic,
            method="limit r->inf of kR*exp(-(r-R)/L)",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="exponential exterior kappa relaxation profile",
        )


def case_4_massive_kappa_relaxation_equation(out: ScriptOutput):
    header("Case 4: Massive kappa relaxation equation outside")

    r, m = sp.symbols("r m", positive=True, real=True)
    kappa = sp.Function("kappa")(r)

    print("Candidate exterior relaxation equation:")
    print()
    print("  kappa'' + 2 kappa'/r - m^2 kappa = 0")
    print()
    print("The decaying spherical solution has form:")
    print()
    print("  kappa_ext ~ C exp(-m r)/r")
    print()
    print("This supports rapid exterior suppression if m is large.")

    with out.governance_assessments():
        out.line("massive exterior kappa mode can suppress leaks",
                 StatusMark.PASS,
                 "decaying mode exp(-mr)/r gives rapid exterior suppression")

    with out.unresolved_obligations():
        out.line("derive exterior kappa mass parameter m from vacuum physics",
                 StatusMark.OBLIGATION,
                 "massive relaxation is candidate; mass m not derived from first principles")


def case_5_energy_penalty_boundary_layer(out: ScriptOutput, ns=None):
    header("Case 5: Energy penalty picture")

    kappa, C_k, J_inside = sp.symbols("kappa C_k J_inside", positive=True, real=True)

    E_inside = C_k*kappa**2 - J_inside*kappa
    sol_inside = sp.solve(sp.Eq(sp.diff(E_inside, kappa), 0), kappa)

    E_outside = C_k*kappa**2
    sol_outside = sp.solve(sp.Eq(sp.diff(E_outside, kappa), 0), kappa)

    print(f"E_inside = {E_inside}")
    print(f"kappa_inside_eq = {sol_inside}")
    print()
    print(f"E_outside = {E_outside}")
    print(f"kappa_outside_eq = {sol_outside}")

    with out.sample_results():
        out.line("sourceful interior can prefer nonzero kappa",
                 StatusMark.PASS if bool(sol_inside) else StatusMark.FAIL,
                 f"kappa_eq = {sol_inside}")
        out.line("source-free exterior prefers kappa=0",
                 StatusMark.PASS if (sol_outside == [0]) else StatusMark.FAIL,
                 f"kappa_eq = {sol_outside}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="energy_penalty_interior_exterior_kappa",
            inputs=[E_inside, E_outside],
            output=sp.Matrix([sol_inside[0] if sol_inside else sp.nan,
                              sol_outside[0] if sol_outside else sp.nan]),
            method="stationary equation of quadratic kappa energy with/without source",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="toy energy penalty model",
        )


def case_6_exterior_observable_constraint(out: ScriptOutput, ns=None):
    header("Case 6: Exterior observable constraint")

    eps, lam = sp.symbols("eps lambda_k", real=True)

    kappa = lam * eps
    s = -2*eps
    A = sp.exp(kappa+s)
    B = sp.exp(kappa-s)
    AB = sp.simplify(A*B)

    A1 = sp.series(A, eps, 0, 2).removeO()
    B1 = sp.series(B, eps, 0, 2).removeO()
    AB1 = sp.series(AB, eps, 0, 2).removeO()

    print(f"A approx {A1}")
    print(f"B approx {B1}")
    print(f"AB approx {AB1}")
    print()
    print("Any persistent exterior lambda_k shifts weak-field coefficients.")
    print("Thus exterior kappa relaxation must be efficient.")

    with out.governance_assessments():
        out.line("exterior kappa leak remains deviation channel",
                 StatusMark.PASS,
                 "nonzero lambda_k shifts A, B, AB at first order in eps")

    if ns is not None:
        ns.record_derivation(
            derivation_id="exterior_kappa_leak_weak_field_constraint",
            inputs=[kappa, s, eps],
            output=AB1,
            method="series A*B to first order in eps with kappa=lambda_k*eps",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="weak-field exterior kappa leak constraint",
        )


def final_interpretation():
    header("Final interpretation")

    print("Boundary kappa relaxation is plausible in reduced toy profiles.")
    print()
    print("Cleanest profile class:")
    print("  nonzero kappa inside")
    print("  kappa(R)=0")
    print("  kappa'(R)=0")
    print("  kappa=0 outside")
    print()
    print("Alternative:")
    print("  exterior massive relaxation tail, but this creates a kappa-leak")
    print("  deviation channel unless strongly suppressed.")
    print()
    print("Possible next artifact:")
    print("  candidate_boundary_kappa_relaxation_layer.md")


def main():
    header("Candidate Boundary Kappa Relaxation Layer")
    archive, ns, invalidated = prepare_archive()
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")

    out = ScriptOutput()

    case_0_problem_statement(out)
    case_1_sharp_cutoff(out)
    case_2_smooth_polynomial_inside(out, ns)
    case_3_exponential_exterior_relaxation(out, ns)
    case_4_massive_kappa_relaxation_equation(out)
    case_5_energy_penalty_boundary_layer(out, ns)
    case_6_exterior_observable_constraint(out, ns)
    final_interpretation()

    out.print_summary()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_relaxation_mechanism",
        script_id=SCRIPT_ID,
        title="Derive boundary kappa relaxation mechanism from field equation",
        status=ObligationStatus.OPEN,
        description=(
            "The profiles tested here (sharp cutoff, smooth polynomial, exponential "
            "tail, energy penalty) are toy/diagnostic. No full field equation for "
            "the kappa relaxation layer has been derived. The mechanism that carries "
            "interior kappa to exterior kappa=0 remains an open obligation."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_exterior_kappa_mass",
        script_id=SCRIPT_ID,
        title="Derive exterior kappa mass parameter from vacuum physics",
        status=ObligationStatus.OPEN,
        description=(
            "A massive exterior kappa mode (kappa ~ C exp(-mr)/r) can suppress "
            "exterior kappa leaks if m is large. The mass parameter m is not derived "
            "from first principles and remains open."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="smooth_interior_kappa_profile_viable",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "A smooth interior kappa profile with kappa(R)=0 and kappa'(R)=0 is "
            "the cleanest class for reconciling interior kappa response with exterior "
            "kappa=0. This is a diagnostic assessment; mechanism derivation is open."
        ),
        obligation_ids=["derive_kappa_relaxation_mechanism"],
    ))

    ns.record_route(RouteRecord(
        route_id="smooth_interior_kappa_compact_support_route",
        script_id=SCRIPT_ID,
        name="Smooth interior kappa with compact support vanishing at boundary",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_kappa_relaxation_mechanism"],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
