# Trial E3: P7' vs the scalaron -- the candidate parent's four-derivative sector closes
#
# Group:
#   009_trial_E_boundary_admissibility
#
# Script type:
#   CANDIDATE WRITE-DOWN / CONTRADICTION THEOREM / SECTOR CLOSURE
#
# Purpose
# -------
# First candidate parent at <= 4-derivative order, assembled from the
# constraint ledger (008: EH normalization forced; G20: only aR^2 + GB
# survive the ghost gate):
#
#   K1:  S = (c^4/16 pi G) Int sqrt(-g) (R - 2 Lambda)  +  a Int sqrt(-g) R^2
#        (+ Gauss-Bonnet, inert)
#
# Testing K1 against the ADOPTED POSTULATES uncovers a collision the
# E1/E2/G20 chain did not see:
#
#   T1  P7''s metric shadow AB = 1 is RESPONSE-INDEPENDENT geometry
#       (C3: G^t_t - G^r_r = -(ln AB)'/(rB) for any static spherical
#       metric). The G20 scalaron exterior has, in areal gauge,
#         AB - 1 = 2(phi + r psi')/c^2 != 0   within ell* of the surface
#       (vanishes identically for the GR solution phi = psi = -GM/r).
#       Equivalently: the R^2 response term itself carries a t-r
#       anisotropy D^t_t - D^r_r = -R'' != 0 wherever hair exists --
#       precisely the preferred-frame stress P7' forbids.
#
#   T2  THE HAIR IS MANDATORY for a != 0: fourth-order matching (E1-c3:
#       R and R' continuous) admits NO hairless exterior. The interior
#       solution R = kappa rho c^2 + A sinh(mr)/r cannot satisfy
#       R(R_b) = R'(R_b) = 0 (requires x cosh x = sinh x, impossible for
#       x > 0); a sourced star ALWAYS leaks scalaron hair.
#
#   T3  CONTRADICTION: P7' (adopted 2026-06-11, exact at H -> 0) forbids
#       static exterior configurations with a preferred t-r frame; any
#       a != 0 mandates them. Therefore
#
#         P7'  ==>  a = 0.
#
#       The smooth-boundary route is KILLED_BY_CONTRADICTION with the
#       adopted postulate set -- not by data, not by ghosts: by P7'.
#       Appeal path (theory-owner decision, documented, NOT taken here):
#       re-scope P7' to the two-derivative sector or to r >> ell*.
#
#   T4  SECTOR CLOSURE: with a = 0, candidate K1 collapses to
#         K_strain (<= 4 derivatives) = (c^4/16 pi G)(R - 2 Lambda) + GB
#       EXACTLY. All local gravitational physics of VED = GR. Boundary
#       behavior = GR (curvature jumps transcribed; E1's verdict
#       upgrades from UNDERDETERMINED to RESOLVED under the adopted
#       set). VED's novelty is quarantined to: the kappa-leak channel
#       (H != 0), the B2 measure/matter sector, the interior cap, and
#       Lambda's origin. P7' acquires a SECOND observable face: the
#       micron-window becomes a NULL TEST (any |alpha| ~ O(1) Yukawa
#       detection at micron range would force P7' revision).

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
    RouteRecord,
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
        dependency_id="c3_tr_identity_dependency_e3",
        upstream_script_id="002_trial_C_burden_ledger__trial_C3_spatial_bootstrap",
        upstream_derivation_id="tr_block_identity_c3",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="p7prime_dependency_e3",
        upstream_script_id="005_postulate_adoptions__record_postulate_adoptions",
        upstream_derivation_id="postulate_P7prime_record_005",
        expected_record_kind=RecordKind.UNARCHIVED_FOUNDATION,
    )
    ns.declare_dependency(
        dependency_id="g20_alpha_dependency_e3",
        upstream_script_id="010_gate_G20_beta_health__gate_G20_beta_health",
        upstream_derivation_id="alpha_one_third_g20",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="e1_matching_dependency_e3",
        upstream_script_id="009_trial_E_boundary_admissibility__trial_E1_sharp_source_gate",
        upstream_derivation_id="beta_smoothing_mechanism_e1",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Symbols
# =============================================================================

r, x_ = sp.symbols("r x", positive=True)
c = sp.Symbol("c", positive=True)
G_N = sp.Symbol("G", positive=True)
M_m = sp.Symbol("M", positive=True)
a_c = sp.Symbol("a", positive=True)
eps = sp.Symbol("epsilon", positive=True)
m_s = 1 / sp.sqrt(6 * a_c)


# =============================================================================
# Case 0: the candidate
# =============================================================================


def case_0_candidate(out: ScriptOutput) -> None:
    header("Case 0: Candidate K1 -- the ledger-assembled parent at <= 4 derivatives")
    print("Constraint ledger entering this script:")
    print("  008: two-derivative sector = EH with N = c^4/(8 pi G), K_T = c^4/(16 pi G)")
    print("  G20: four-derivative sector = a R^2 (a > 0) + Gauss-Bonnet, nothing else")
    print("  probe gates: + Lambda allowed")
    print()
    print("  K1:  S = (c^4/16 pi G) Int sqrt(-g) (R - 2 Lambda) + a Int sqrt(-g) R^2  (+ GB)")
    print()
    print("One coefficient left: a. This script tests K1 against the ADOPTED")
    print("POSTULATES -- and finds that P7' decides a.")

    with out.governance_assessments():
        out.line("candidate K1 written down from the ledger", StatusMark.INFO,
                 "single undetermined coefficient: a (the smooth-boundary coefficient)")


# =============================================================================
# Case 1 (T1): the hair violates P7''s metric shadow
# =============================================================================


def case_1_shadow_violation(out: ScriptOutput) -> None:
    header("Case 1 (T1): Scalaron hair breaks AB = 1 (P7''s response-independent shadow)")

    # areal-gauge transform at linear order, from the G20 isotropic-like gauge:
    # spatial metric (1 - 2 eps psi/c^2)(dr^2 + r^2 dOmega^2); set
    # rbar = r (1 - eps psi/c^2). Verify g_rbar_rbar = 1 + 2 eps r psi'/c^2.
    psi_f = sp.Function("psi")(r)
    rbar = r * (1 - eps * psi_f / c**2)
    drbar_dr = sp.diff(rbar, r)
    g_rbar = sp.series((1 - 2 * eps * psi_f / c**2) / drbar_dr**2, eps, 0, 2).removeO()
    g_rbar_lin = sp.expand(g_rbar).coeff(eps, 1)
    transform_res = sp.simplify(g_rbar_lin - 2 * r * sp.diff(psi_f, r) / c**2)
    print(f"  areal transform check: g_rbar_rbar^(1) - 2 r psi'/c^2 = {sp.sstr(transform_res)}")
    print("  =>  AB - 1 = 2 eps (phi + r psi')/c^2  at linear order.")
    print()

    # evaluate the shadow on GR and on the G20 hair
    e_ = sp.exp(-m_s * r)
    phi_gr = -G_N * M_m / r
    psi_gr = -G_N * M_m / r
    phi_hair = -(G_N * M_m / r) * (1 + sp.Rational(1, 3) * e_)
    psi_hair = -(G_N * M_m / r) * (1 - sp.Rational(1, 3) * e_)

    shadow_gr = sp.simplify(phi_gr + r * sp.diff(psi_gr, r))
    shadow_hair = sp.simplify(phi_hair + r * sp.diff(psi_hair, r))
    print(f"  GR exterior:    phi + r psi' = {sp.sstr(shadow_gr)}   (AB = 1 holds)")
    print(f"  hair exterior:  phi + r psi' = {sp.sstr(shadow_hair)}")
    print()

    # the response-side face: the R^2 operator's own t-r anisotropy on flat
    # background for static R(r): D^t_t - D^r_r = -R''.
    R_f = sp.Function("Rs")(r)
    lapR = sp.diff(r**2 * sp.diff(R_f, r), r) / r**2
    D_t_t = -lapR                                # g^tt(grad_t grad_t R) - box R, flat static
    D_r_r = sp.diff(R_f, r, 2) - lapR
    anisotropy = sp.simplify((D_t_t - D_r_r) + sp.diff(R_f, r, 2))
    print(f"  response anisotropy check: (D^t_t - D^r_r) + R'' = {sp.sstr(anisotropy)}")
    print()
    print("  THEOREM T1: by C3's response-independent identity")
    print("  G^t_t - G^r_r = -(ln AB)'/(rB), the hair region has AB != 1 and a")
    print("  preferred t-r frame in STATIC VACUUM -- exactly the configuration")
    print("  P7' forbids. The violator is the R^2 response term itself")
    print("  (D^t_t - D^r_r = -R''), the same scalar-gradient anisotropy that")
    print("  C3-2 used to kill explicit-source placement.")

    ok = (is_zero(transform_res) and is_zero(shadow_gr)
          and not is_zero(shadow_hair) and is_zero(anisotropy))
    with out.derived_results():
        out.line("scalaron hair violates AB = 1 in static vacuum; GR exterior does not",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 "AB - 1 = 2(phi + r psi')/c^2: zero for GR, nonzero within ell* for the hair")
        out.line("the R^2 response term carries the forbidden t-r anisotropy",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 "D^t_t - D^r_r = -R'' != 0 wherever hair exists (the C3-2 stress pattern)")


# =============================================================================
# Case 2 (T2): the hair is mandatory for a != 0
# =============================================================================


def case_2_mandatory_hair(out: ScriptOutput) -> None:
    header("Case 2 (T2): No hairless matching exists -- a sourced star must leak hair")
    print("Interior of a uniform ball (trace equation, regular at origin):")
    print("  R_in = kappa rho c^2 + A sinh(mr)/r ;   exterior: R_ext = C e^(-mr)/r.")
    print("Fourth-order matching (E1-c3): R and R' continuous at the surface.")
    print("Hairless means C = 0, i.e. R_in(R_b) = 0 AND R_in'(R_b) = 0.")
    print()

    # homogeneous solutions check
    lap = lambda f: sp.diff(r**2 * sp.diff(f, r), r) / r**2
    hom_in = sp.simplify(sp.sinh(m_s * r) / r - 6 * a_c * lap(sp.sinh(m_s * r) / r))
    hom_ext = sp.simplify(sp.exp(-m_s * r) / r - 6 * a_c * lap(sp.exp(-m_s * r) / r))
    print(f"  homogeneous checks: (1 - 6a Lap)[sinh(mr)/r] = {sp.sstr(hom_in)}, "
          f"(1 - 6a Lap)[e^(-mr)/r] = {sp.sstr(hom_ext)}")

    # the obstruction: eliminating A from the two hairless conditions requires
    # x cosh x - sinh x = 0 at x = m R_b > 0. Show h(x) = x cosh x - sinh x > 0:
    h = x_ * sp.cosh(x_) - sp.sinh(x_)
    h_at_0 = h.subs(x_, 0)
    h_prime = sp.simplify(sp.diff(h, x_) - x_ * sp.sinh(x_))
    print(f"  h(x) = x cosh x - sinh x:  h(0) = {h_at_0},  h'(x) - x sinh x = {sp.sstr(h_prime)}")
    print("  h' = x sinh x > 0 for x > 0  =>  h > 0 for all x > 0:")
    print("  the second condition forces A = 0, and then the first reads")
    print("  kappa rho c^2 = 0 -- contradiction. NO hairless solution exists.")
    print()
    print("  THEOREM T2: for ANY a != 0, every static star leaks scalaron hair")
    print("  into its exterior. T1's P7' violation is not a choice; it is")
    print("  mandatory.")

    ok = is_zero(hom_in) and is_zero(hom_ext) and h_at_0 == 0 and is_zero(h_prime)
    with out.derived_results():
        out.line("hairless exterior impossible for a != 0",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 "x cosh x = sinh x has no positive root (h' = x sinh x > 0); sourced stars always leak hair")


# =============================================================================
# Case 3 (T3): the contradiction theorem
# =============================================================================


def case_3_contradiction(out: ScriptOutput) -> None:
    header("Case 3 (T3): P7' ==> a = 0 (the route dies by postulate)")
    print("  P7' (ADOPTED, exact at H -> 0): strictly static vacuum carries no")
    print("       energy current and no preferred frame in the t-r plane.")
    print("  T1:  any scalaron hair is a static vacuum configuration WITH a")
    print("       preferred t-r frame (AB != 1, D^t_t - D^r_r = -R'').")
    print("  T2:  a != 0 makes such hair MANDATORY around every star.")
    print("  ==>  under the adopted postulate set, a = 0. QED.")
    print()
    print("  VERDICT: the smooth-boundary route -- E1's beta mechanism, E2's")
    print("  bench-top face, G20's surviving scalaron class -- is KILLED BY")
    print("  CONTRADICTION with P7'. Not by data, not by ghosts: the theory's")
    print("  own adopted frame-indifference postulate forbids the hair that")
    print("  smoothing requires. The E1 verdict upgrades from UNDERDETERMINED")
    print("  to RESOLVED: VED boundary behavior is IDENTICAL to GR; curvature")
    print("  jumps at sharp matter edges are transcribed, not smoothed.")
    print()
    print("  APPEAL PATH (theory-owner decision, documented, NOT taken here):")
    print("  re-scope P7' to the two-derivative sector or to r >> ell*. Note")
    print("  the cost: P7' was adopted as an ontology statement about the")
    print("  static vacuum, and the hair is static vacuum; a scope carve-out")
    print("  would be recovery-shaped unless given independent grounding.")

    with out.governance_assessments():
        out.line("smooth-boundary route KILLED_BY_CONTRADICTION (P7')", StatusMark.PASS,
                 "P7' + mandatory hair => a = 0; appeal path documented as theory-owner decision")
    with out.unresolved_obligations():
        out.line("theory-owner review: P7' scope vs the smooth-boundary intuition",
                 StatusMark.OBLIGATION,
                 "default = kill stands (a = 0); appeal = re-scope P7' with independent grounding")


# =============================================================================
# Case 4 (T4): sector closure and what remains of VED's novelty
# =============================================================================


def case_4_closure(out: ScriptOutput) -> None:
    header("Case 4 (T4): K_strain at <= 4 derivatives is CLOSED")
    print("  With a = 0:")
    print()
    print("    K_strain (<= 4 derivatives) = (c^4/16 pi G)(R - 2 Lambda) + Gauss-Bonnet")
    print()
    print("  EXACTLY -- every coefficient derived, matched-coefficient count")
    print("  zero, four-derivative freedom eliminated by P7' + the ghost gate.")
    print("  All local gravitational physics of VED = GR: statics (C2/C3),")
    print("  radiation (008/G03), boundaries (E1-E3), stability (G02).")
    print()
    print("  VED's remaining novelty budget, quarantined and live:")
    print("    1. the kappa-leak channel: AB - 1 = O(H_0 r/c) (P7' at the limit)")
    print("    2. Lambda's origin (the frustration floor, Trial D's w = -1 sector)")
    print("    3. the B2 measure/matter sector (the bridge's physical identity)")
    print("    4. the interior cap (finite admissibility; engineering seam)")
    print("    5. the dark sector as excess EoS (Trial D2)")
    print()
    print("  P7' gains a SECOND observable face: the micron window becomes a")
    print("  NULL TEST. VED-with-P7' predicts NO |alpha| ~ O(1) Yukawa at any")
    print("  range; a detection in the bench-top window would force the P7'")
    print("  appeal. (The UFFT squeeze stands apart: a_disc is a Casimir-")
    print("  sector parameter, not a gravitational Yukawa.)")

    with out.governance_assessments():
        out.line("K_strain <= 4-derivative sector closed", StatusMark.PASS,
                 "= EH + Lambda + GB exactly; novelty quarantined to kappa-leak, Lambda, B2, interior, dark EoS")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="shadow_violation_e3",
        inputs=[],
        output=sp.Symbol("hair_has_AB_neq_1_in_static_vacuum"),
        method="linear areal-gauge transform AB - 1 = 2(phi + r psi')/c^2; zero on GR, "
               "nonzero on the G20 hair; response anisotropy D^t_t - D^r_r = -R''",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="contradiction_witness",
        scope="scalaron hair is a static vacuum configuration with a preferred t-r frame",
    )
    ns.record_derivation(
        derivation_id="mandatory_hair_e3",
        inputs=[],
        output=sp.Symbol("no_hairless_matching_for_a_nonzero"),
        method="interior/exterior matching of the trace equation; x cosh x = sinh x has "
               "no positive root (h' = x sinh x > 0)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="no_go_theorem",
        scope="every static star leaks scalaron hair for any a != 0",
    )
    ns.record_derivation(
        derivation_id="p7prime_forces_a_zero_e3",
        inputs=[],
        output=sp.Eq(sp.Symbol("a"), 0),
        method="T1 + T2 + adopted P7' (postulate_P7prime_record_005)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="sector_closure",
        scope="under the adopted postulate set the four-derivative coefficient vanishes; "
              "VED boundary behavior = GR exactly",
    )
    ns.record_derivation(
        derivation_id="k_strain_4deriv_closure_e3",
        inputs=[],
        output=sp.Symbol("K_strain_leq4_eq_EH_plus_Lambda_plus_GB"),
        method="ledger assembly (008 normalizations, G20 classification) + a = 0 (this script)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="candidate_closure",
        scope="candidate K1 collapses to EH + Lambda + GB; zero free coefficients at <= 4 derivatives",
    )

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="kill_smooth_boundary_route_e3",
        script_id=SCRIPT_ID,
        branch_id="smooth_boundary_beta_route_e1",
        status=GovernanceStatus.KILLED_BY_CONTRADICTION,
        tier=ClaimTier.EXCLUSION,
        obligation_ids=["p7prime_scope_review_e3"],
        description=(
            "The smooth-boundary route (E1 beta mechanism, E2 bench-top face, G20 "
            "scalaron class) contradicts adopted P7': scalaron hair is a static vacuum "
            "configuration with a preferred t-r frame (AB != 1), and the hair is "
            "mandatory for any a != 0. Under the adopted postulate set a = 0; VED "
            "boundary behavior is identical to GR. Appeal path: theory-owner re-scope "
            "of P7' (default: kill stands)."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="p7prime_scope_review_e3",
        script_id=SCRIPT_ID,
        title="Theory-owner review: P7' scope vs the smooth-boundary intuition",
        status=ObligationStatus.OPEN,
        required_by=[],
        description="Default: kill stands, a = 0. Appeal: re-scope P7' (two-derivative sector "
                    "or r >> ell*) -- requires independent grounding to avoid being "
                    "recovery-shaped. The micron-window null test rides on this decision.",
    ))

    ns.record_route(RouteRecord(
        route_id="p7prime_null_test_route_e3",
        script_id=SCRIPT_ID,
        name="P7' null test: no gravitational-strength Yukawa at any range",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "a bench-top |alpha| ~ O(1) detection at micron range would force the P7' appeal",
            "distinct from the UFFT squeeze (a_disc is Casimir-sector, not gravitational)",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="candidate_K1_closure_e3",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Candidate K1 (ledger-assembled parent at <= 4 derivatives) tested against "
            "the adopted postulates: P7' forces its single free coefficient to zero "
            "(scalaron hair has AB != 1 in static vacuum and is mandatory for a != 0). "
            "K_strain at <= 4 derivatives = (c^4/16 pi G)(R - 2 Lambda) + Gauss-Bonnet "
            "exactly; VED's local gravitational physics = GR, including boundary "
            "behavior (Trial E resolved: curvature jumps transcribed). The smooth-"
            "boundary route is KILLED_BY_CONTRADICTION with appeal documented. P7' "
            "acquires a second observable face: a null test in the micron window."
        ),
        derivation_ids=[
            "shadow_violation_e3",
            "mandatory_hair_e3",
            "p7prime_forces_a_zero_e3",
            "k_strain_4deriv_closure_e3",
        ],
        obligation_ids=["p7prime_scope_review_e3"],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial E3: P7' vs the Scalaron -- Closing the Four-Derivative Sector")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_candidate(out)
    case_1_shadow_violation(out)
    case_2_mandatory_hair(out)
    case_3_contradiction(out)
    case_4_closure(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
