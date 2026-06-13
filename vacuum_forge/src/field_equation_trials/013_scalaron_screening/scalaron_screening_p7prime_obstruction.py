# Trial 013: Scalaron screening vs P7'
#
# Script type:
#   APPEAL-FILE LEMMA / OBJECTION CLOSURE / SYMBOLIC CHECK
#
# Purpose
# -------
# G20 left one ghost-safe four-derivative channel: a R^2, with a healthy
# scalaron. E3 then killed that channel under adopted P7': scalaron hair
# is mandatory for a != 0 and gives AB != 1 / a preferred static t-r
# frame in vacuum.
#
# This script closes the predictable screening objection:
#
#   "What if the scalaron is screened?"
#
# Screening can make the scalar profile short-ranged, small,
# environment-dependent, or difficult to detect. P7' is stricter: it is
# an exact static-frame-indifference condition. In the scalaron weak-field
# form, any nonzero scalar profile q(r) produces
#
#   phi + r psi' = r q' - q.
#
# Exact P7' requires r q' - q = 0. The only solution is q = C r, and
# asymptotic flatness forces C = 0. Therefore screening cannot rescue
# a != 0 unless P7' is re-scoped by theory-owner appeal.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
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


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="e3_shadow_violation_dependency_013",
        upstream_script_id="009_trial_E_boundary_admissibility__trial_E3_p7prime_vs_scalaron",
        upstream_derivation_id="shadow_violation_e3",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="e3_mandatory_hair_dependency_013",
        upstream_script_id="009_trial_E_boundary_admissibility__trial_E3_p7prime_vs_scalaron",
        upstream_derivation_id="mandatory_hair_e3",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="e3_p7prime_closure_dependency_013",
        upstream_script_id="009_trial_E_boundary_admissibility__trial_E3_p7prime_vs_scalaron",
        upstream_derivation_id="p7prime_forces_a_zero_e3",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="g20_scalaron_health_dependency_013",
        upstream_script_id="010_gate_G20_beta_health__gate_G20_beta_health",
        upstream_derivation_id="scalaron_health_g20",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="g20_alpha_dependency_013",
        upstream_script_id="010_gate_G20_beta_health__gate_G20_beta_health",
        upstream_derivation_id="alpha_one_third_g20",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


r = sp.Symbol("r", positive=True)
G_N = sp.Symbol("G", positive=True)
M_m = sp.Symbol("M", positive=True)
ell = sp.Symbol("ell_star", positive=True)
C = sp.Symbol("C")
q = sp.Function("q")


def case_1_general_shadow(out: ScriptOutput):
    header("Case 1: General screened scalar profile and the P7' shadow")

    phi_gr = -G_N * M_m / r
    q_r = q(r)
    phi = phi_gr - q_r
    psi = phi_gr + q_r

    gr_shadow = sp.simplify(phi_gr + r * sp.diff(phi_gr, r))
    scalar_shadow = sp.simplify(phi + r * sp.diff(psi, r))
    expected = sp.simplify(r * sp.diff(q_r, r) - q_r)
    residual = sp.simplify(scalar_shadow - expected)

    print(f"  GR cancellation: phi_GR + r phi_GR' = {sp.sstr(gr_shadow)}")
    print(f"  scalaron form:   phi + r psi' = {sp.sstr(scalar_shadow)}")
    print(f"  expected:        r q' - q = {sp.sstr(expected)}")
    print(f"  residual:        {sp.sstr(residual)}")
    print()
    print("  P7' demands AB = 1 in static vacuum. In E3's areal-gauge shadow,")
    print("  AB - 1 = 2(phi + r psi')/c^2. Therefore the scalar contribution")
    print("  must satisfy r q' - q = 0 exactly, not merely approximately.")

    ok = is_zero(gr_shadow) and is_zero(residual)
    with out.derived_results():
        out.line(
            "general screened scalar shadow derived",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "for phi = phi_GR - q and psi = phi_GR + q, the P7' shadow is r q' - q",
        )
    return ok, expected


def case_2_exact_p7prime_solution(out: ScriptOutput):
    header("Case 2: Exact P7' compatibility forces q = 0 under asymptotic flatness")

    q_candidate = C * r
    ode_residual = sp.simplify(r * sp.diff(q_candidate, r) - q_candidate)
    asymptotic_limit = sp.limit(q_candidate, r, sp.oo)
    nonzero_C_diverges = asymptotic_limit.has(sp.oo)

    print("  Exact P7' condition for the scalar profile:")
    print("    r q'(r) - q(r) = 0")
    print("  General solution:")
    print("    q(r) = C r")
    print(f"  solution residual: {sp.sstr(ode_residual)}")
    print(f"  limit q(r) as r -> infinity for C r: {sp.sstr(asymptotic_limit)}")
    print()
    print("  Asymptotic flatness requires the scalar contribution to vanish at")
    print("  infinity. The only P7'-compatible scalar profile satisfying that")
    print("  boundary condition is q(r) = 0.")

    ok = is_zero(ode_residual) and nonzero_C_diverges
    with out.derived_results():
        out.line(
            "P7'-compatible asymptotically flat scalar profile is identically zero",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "r q' - q = 0 -> q = C r; asymptotic flatness forces C = 0",
        )
    return ok


def case_3_g20_yukawa_witness(out: ScriptOutput):
    header("Case 3: G20 Yukawa scalaron profile is not P7'-compatible")

    q_yukawa = G_N * M_m * sp.exp(-r / ell) / (3 * r)
    shadow = sp.simplify(r * sp.diff(q_yukawa, r) - q_yukawa)
    normalized = sp.simplify(shadow / q_yukawa)

    print("  G20 scalar contribution:")
    print(f"    q(r) = {sp.sstr(q_yukawa)}")
    print("  P7' shadow:")
    print(f"    r q' - q = {sp.sstr(shadow)}")
    print(f"    (r q' - q)/q = {sp.sstr(normalized)}")
    print()
    print("  The screened Yukawa profile becomes small outside ell*, but it is")
    print("  not identically zero. It therefore violates exact P7' wherever the")
    print("  hair is present.")

    ok = not is_zero(shadow) and sp.simplify(normalized + r / ell + 2) == 0
    with out.derived_results():
        out.line(
            "G20 Yukawa scalaron hair has nonzero P7' shadow",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "q = GM e^(-r/ell*)/(3r) gives r q' - q = -(r/ell* + 2) q, not zero",
        )
    return ok


def case_4_governance(out: ScriptOutput):
    header("Case 4: Governance result")
    print("  Screening changes detectability, range, or amplitude. P7' is an")
    print("  exact structural gate. Under the admitted postulate set:")
    print()
    print("    a != 0  -> mandatory scalaron hair (E3)")
    print("    hair != 0 -> nonzero P7' shadow (this script)")
    print("    P7' exact -> hair must be zero")
    print()
    print("  Therefore screening does not rescue a != 0. The only route is the")
    print("  existing theory-owner appeal: re-scope P7'. That is a postulate")
    print("  revision, not a screened solution inside the admitted theory.")

    with out.governance_assessments():
        out.line(
            "screening does not rescue the scalaron under exact P7'",
            StatusMark.PASS,
            "small/short-range/environmental hair still violates AB = 1 unless it is identically zero",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="general_screened_scalar_shadow_013",
        inputs=[],
        output=sp.Symbol("phi_plus_r_psi_prime_eq_rqprime_minus_q"),
        method="symbolic substitution phi = -GM/r - q(r), psi = -GM/r + q(r) into E3's areal-gauge shadow",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="screening_obstruction_lemma",
        scope="any static screened scalar profile in the scalaron weak-field form",
    )
    ns.record_derivation(
        derivation_id="p7prime_screened_scalar_zero_013",
        inputs=[],
        output=sp.Symbol("exact_P7prime_plus_asymptotic_flatness_forces_q_zero"),
        method="solve r q' - q = 0 -> q = C r; asymptotic flatness forces C = 0",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="no_go_lemma",
        scope="screening cannot make a nonzero static scalar profile compatible with exact P7'",
    )
    ns.record_derivation(
        derivation_id="g20_yukawa_violates_p7prime_013",
        inputs=[],
        output=sp.Symbol("g20_yukawa_has_nonzero_p7prime_shadow"),
        method="substitute q = GM exp(-r/ell*)/(3r); derive r q' - q = -(r/ell* + 2) q",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="witness",
        scope="the G20 screened Yukawa profile violates exact P7' wherever hair is present",
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="scalaron_screening_g20_discharge_013",
        script_id=SCRIPT_ID,
        title="Scalaron screening note: screening cannot rescue a != 0 under exact P7'",
        status=ObligationStatus.SATISFIED,
        satisfied_by=[
            "general_screened_scalar_shadow_013",
            "p7prime_screened_scalar_zero_013",
            "g20_yukawa_violates_p7prime_013",
        ],
        description=(
            "G20's screening language concerns detectability and bound reading. "
            "Exact P7' requires the scalar contribution to have zero t-r shadow. "
            "For any static scalaron profile q, that condition is r q' - q = 0, "
            "whose asymptotically flat solution is q = 0. Therefore screening does "
            "not rescue a != 0; only a theory-owner re-scope of P7' can reopen it."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_screening_rescue_013",
        script_id=SCRIPT_ID,
        branch_id="screening_rescues_a_nonzero_without_p7prime_appeal",
        status=GovernanceStatus.KILLED_BY_CONTRADICTION,
        tier=ClaimTier.EXCLUSION,
        obligation_ids=["scalaron_screening_g20_discharge_013"],
        description=(
            "Screening cannot rescue a != 0 under the admitted postulate set. "
            "A nonzero screened scalar profile still has AB != 1 / preferred static "
            "t-r frame somewhere. E3 makes such hair mandatory for a != 0, so P7' "
            "still forces a = 0. The only escape is the existing P7' appeal."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="scalaron_screening_objection_closed_013",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The scalaron screening objection is closed under the admitted theory. "
            "Screening may suppress the G20 scalaron's observable range or amplitude, "
            "but exact P7' is a structural condition: any nonzero static scalaron "
            "profile q gives phi + r psi' = r q' - q. Exact P7' plus asymptotic "
            "flatness forces q = 0. Since E3 proves scalaron hair is mandatory for "
            "a != 0, screening does not rescue a != 0 unless P7' is re-scoped by "
            "the theory owner."
        ),
        derivation_ids=[
            "general_screened_scalar_shadow_013",
            "p7prime_screened_scalar_zero_013",
            "g20_yukawa_violates_p7prime_013",
        ],
        obligation_ids=["scalaron_screening_g20_discharge_013"],
    ))


def main() -> None:
    header("Trial 013: Scalaron Screening vs P7'")
    _, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ok1, _ = case_1_general_shadow(out)
    ok2 = case_2_exact_p7prime_solution(out)
    ok3 = case_3_g20_yukawa_witness(out)
    case_4_governance(out)

    if not (ok1 and ok2 and ok3):
        raise SystemExit("Scalaron screening obstruction checks failed.")

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
