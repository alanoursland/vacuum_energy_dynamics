# Trial A2: Weyl-screening gate (G26) for UFFT's tidal nucleation sector
#
# Group:
#   003_trial_A_ufft_gates
#
# Script type:
#   DERIVATION / GATE CONFRONTATION / KILL TEST
#
# Purpose
# -------
# Run gate G26 against UFFT's Tidal Vacuum Nucleation (TVN) sector in its
# minimal form:
#
#   alpha_eff = alpha_0 - kappa_W * I,    I = tidal invariant (E_ij E^ij
#   Newtonian; C^2 Weyl covariantly),
#   nucleation when alpha_eff < alpha_c, i.e. when I > I_c.
#
# Locked-door question:
#
#   Can the minimal Weyl/tidal threshold nucleate dark-matter-like vacuum
#   relaxation at galactic scales WITHOUT nucleating throughout the solar
#   system and around every star?
#
# Method: pure computation. (1) derive the point-mass tidal invariant,
# (2) reuse the charter's midpoint invariant for a mass pair, (3) compute
# the curvature hierarchy between solar-system and galactic-bridge
# environments, (4) state the monotone-threshold (up-set) theorem,
# (5) confront UFFT's bounded relaxation variable with the required
# dark-matter spatial profile.
#
# No parameter is fitted. No data file is consumed; the inputs are
# astronomical scales (G, M_sun, AU, kpc) used as order-of-magnitude
# stage props, not precision data.

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
        dependency_id="charter_midpoint_invariant_dependency_a2",
        upstream_script_id="000_trial_charter__trial_gate_inventory",
        upstream_derivation_id="trial_midpoint_tidal_invariant_t000",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Case 0
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Gate G26 against minimal TVN")
    print("UFFT's tidal sector (memo sections 15-17):")
    print()
    print("  alpha_eff(x) = alpha_0 - kappa E_ij E^ij      (Newtonian)")
    print("  alpha_eff(g) = alpha_0 - kappa_W C^2           (covariant)")
    print("  nucleation when alpha_eff < alpha_c  <=>  invariant > I_c")
    print()
    print("Intended phenomenology: relaxed-vacuum bridges between galaxy pairs")
    print("acting as dark-matter-like positive sources (Delta(rho+3P) = -2*Delta_rho).")
    print()
    print("Gate G26: this must not trigger in the solar system without a")
    print("derived screening mechanism. This script tests whether the minimal")
    print("threshold form can have it both ways.")

    with out.governance_assessments():
        out.line("Trial A2 opened", StatusMark.INFO,
                 "G26 confrontation of the minimal Weyl/tidal threshold; kill test")


# =============================================================================
# Case 1: point-mass tidal invariant
# =============================================================================


def case_1_point_mass_invariant(out: ScriptOutput):
    header("Case 1: Point-mass tidal invariant (Newtonian proxy and Weyl)")
    x, y, z = sp.symbols("x y z", real=True)
    G, M = sp.symbols("G M", positive=True)
    r = sp.sqrt(x**2 + y**2 + z**2)
    Phi = -G * M / r
    coords = (x, y, z)
    E = sp.Matrix(3, 3, lambda i, j: sp.diff(Phi, coords[i], coords[j]))
    # evaluate on the x-axis at distance R0 (rotational symmetry)
    R0 = sp.Symbol("R0", positive=True)
    E0 = sp.simplify(E.subs({x: R0, y: 0, z: 0}))
    invariant = sp.simplify(sum(E0[i, j] ** 2 for i in range(3) for j in range(3)))
    expected = 6 * G**2 * M**2 / R0**6
    trace0 = sp.simplify(E0.trace())

    print(f"  E_ij = diag({sp.sstr(E0[0,0])}, {sp.sstr(E0[1,1])}, {sp.sstr(E0[2,2])})")
    print(f"  E_ij E^ij = {sp.sstr(invariant)}   (expected 6 G^2 M^2 / R0^6)")
    print(f"  trace E = {sp.sstr(trace0)}  (vacuum check)")
    print()
    print("  Covariant counterpart: Schwarzschild exterior has C^2 = K =")
    print("  48 G^2 M^2/(c^4 r^6) -- the same r^-6 profile times 8/c^4. The")
    print("  Newtonian invariant is the correct scaling proxy for this gate.")

    with out.derived_results():
        out.line("point-mass invariant = 6 G^2 M^2 / r^6",
                 StatusMark.PASS if is_zero(invariant - expected) else StatusMark.FAIL,
                 "eigenvalues (-2, 1, 1) GM/r^3; trace-free")
        out.line("vacuum trace check",
                 StatusMark.PASS if is_zero(trace0) else StatusMark.FAIL,
                 f"trace E = {sp.sstr(trace0)}")
    return invariant, expected


# =============================================================================
# Case 2: the curvature hierarchy
# =============================================================================


def case_2_hierarchy(out: ScriptOutput):
    header("Case 2: Solar-system vs galactic-bridge tidal hierarchy")
    # order-of-magnitude stage props (not precision data)
    G_si = 6.674e-11
    M_sun = 1.989e30
    AU = 1.496e11
    kpc = 3.086e19
    M_gal = 1.0e12 * M_sun         # large spiral including halo
    d_gal = 50 * kpc               # interacting-pair separation scale

    def I_point(M, r):
        return 6 * (G_si * M / r**3) ** 2

    def I_midpoint(M, d):
        return 1536 * (G_si * M) ** 2 / d**6   # charter witness

    I_1AU = I_point(M_sun, AU)
    I_saturn = I_point(M_sun, 9.6 * AU)
    I_bridge = I_midpoint(M_gal, d_gal)
    ratio = I_1AU / I_bridge

    # radius around the Sun where the solar invariant falls to the bridge value
    r_eq = (6 ** 0.5 * G_si * M_sun / (I_bridge ** 0.5)) ** (1.0 / 3.0)

    print(f"  I(Sun, 1 AU)        = {I_1AU:.3e}  s^-4")
    print(f"  I(Sun, Saturn)      = {I_saturn:.3e}  s^-4")
    print(f"  I(bridge midpoint)  = {I_bridge:.3e}  s^-4   (2 x 1e12 M_sun at 50 kpc)")
    print(f"  hierarchy ratio I_1AU / I_bridge = {ratio:.3e}")
    print(f"  equal-invariant radius around the Sun: r_eq = {r_eq:.3e} m"
          f" = {r_eq/AU:.3e} AU = {r_eq/(3.086e16):.2f} pc")
    print()
    print("  Every point within ~2 pc of the Sun -- the ENTIRE planetary system,")
    print("  Kuiper belt, and Oort cloud -- has tidal invariant ABOVE the")
    print("  galactic-bridge midpoint value, by up to ~34 orders of magnitude")
    print("  at 1 AU. Every star in the galaxy carries a comparable")
    print("  super-threshold bubble.")

    hierarchy_ok = ratio > 1e30
    r_eq_pc = r_eq / 3.086e16
    bubble_ok = 0.5 < r_eq_pc < 10

    with out.derived_results():
        out.line("solar invariant exceeds bridge invariant by > 30 orders",
                 StatusMark.PASS if hierarchy_ok else StatusMark.FAIL,
                 f"I_1AU / I_bridge = {ratio:.2e}")
        out.line("super-threshold bubble around each star ~ parsec scale",
                 StatusMark.PASS if bubble_ok else StatusMark.FAIL,
                 f"r_eq = {r_eq_pc:.2f} pc around the Sun")
    return ratio, r_eq


# =============================================================================
# Case 3: the up-set theorem
# =============================================================================


def case_3_upset_theorem(out: ScriptOutput):
    header("Case 3: Monotone threshold => nucleation set is an up-set")
    alpha0, kappaW, I1, I2, alphac = sp.symbols(
        "alpha0 kappa_W I1 I2 alpha_c", positive=True)
    alpha_eff = lambda I: alpha0 - kappaW * I

    # monotonicity: I2 > I1  =>  alpha_eff(I2) < alpha_eff(I1)
    diff = sp.simplify(alpha_eff(I2) - alpha_eff(I1))   # = -kappa_W (I2 - I1)
    mono_ok = is_zero(diff + kappaW * (I2 - I1))

    print("  alpha_eff(I) = alpha_0 - kappa_W I is strictly decreasing in I.")
    print(f"  alpha_eff(I2) - alpha_eff(I1) = {sp.sstr(diff)}  < 0 for I2 > I1")
    print()
    print("  THEOREM (trivial but decisive): the nucleation region")
    print("  {alpha_eff < alpha_c} = {I > I_c} is an UP-SET in the tidal")
    print("  invariant. If any galactic-bridge midpoint nucleates, then every")
    print("  region of HIGHER invariant nucleates -- which by Case 2 includes")
    print("  the entire solar system and a ~pc bubble around every star.")
    print()
    print("  The threshold has the WRONG SIGN of spatial dependence for dark")
    print("  matter: relaxation triggers most where curvature is strongest")
    print("  (near stars), least in the low-curvature outskirts where the")
    print("  dark-matter phenomenology lives.")

    with out.derived_results():
        out.line("nucleation set is an up-set in the invariant",
                 StatusMark.PASS if mono_ok else StatusMark.FAIL,
                 "bridge nucleation => solar-system nucleation (no escape within minimal form)")
    return mono_ok


# =============================================================================
# Case 4: profile mismatch for the dark-matter role
# =============================================================================


def case_4_profile_mismatch(out: ScriptOutput):
    header("Case 4: Saturation profile vs required dark-matter profile")
    chi, alpha, beta, lam = sp.symbols("chi alpha beta lamda", positive=True)
    chi_star = (beta + sp.sqrt(beta**2 + 4 * lam * alpha)) / (2 * lam)
    # deep above threshold alpha_eff = -alpha (alpha > 0): chi_* grows like
    # sqrt(alpha/lam) -- verify the asymptotic
    asym = sp.limit(chi_star / sp.sqrt(alpha / lam), alpha, sp.oo)

    print("  Above threshold (alpha_eff < 0, write alpha_eff = -alpha):")
    print()
    print(f"  chi_* = [beta + sqrt(beta^2 + 4*lamda*alpha)]/(2*lamda)")
    print(f"  chi_* / sqrt(alpha/lamda) -> {sp.sstr(asym)} as alpha -> oo")
    print()
    print("  So in the minimal quartic, the relaxation amplitude GROWS with the")
    print("  invariant (the memo's chi in [0,1] is an unenforced intent --")
    print("  danger zone 2). Either way -- growing chi_* or clamped chi = 1 --")
    print("  the induced source Delta(rho+3P) = -2*Delta_rho(chi) is LARGEST")
    print("  (or saturated) in high-curvature regions:")
    print()
    print("    predicted extra source:  max near stars, min at halo outskirts")
    print("    required (rotation curves): min near stars, dominant at outskirts")
    print()
    print("  The spatial profile is inverted relative to the dark-matter role,")
    print("  independent of all coupling values. No choice of kappa_W rescues")
    print("  the minimal form: the up-set structure fixes the gradient's sign.")

    with out.derived_results():
        out.line("relaxation amplitude is monotone in the invariant",
                 StatusMark.PASS if asym == 1 else StatusMark.FAIL,
                 "chi_* ~ sqrt(alpha_excess/lamda); no decrease toward strong curvature")

    with out.counterexamples():
        out.line("minimal TVN as dark-matter mechanism",
                 StatusMark.FAIL,
                 "profile inverted: nucleation strongest near stars, weakest where halos are needed")


# =============================================================================
# Case 5: verdict
# =============================================================================


def case_5_verdict(out: ScriptOutput) -> None:
    header("Case 5: Trial A2 verdict")
    print("Gate G26 verdict on UFFT's minimal tidal-nucleation sector:")
    print()
    print("  KILLED (FAILED_BY_WITNESS), with the kill carried by structure,")
    print("  not by parameter values:")
    print()
    print("  1. Up-set theorem: bridge nucleation implies solar-system")
    print("     nucleation (hierarchy witness: ~34 orders of magnitude,")
    print("     ~2 pc super-threshold bubble around the Sun).")
    print("  2. Profile inversion: the induced source is largest exactly where")
    print("     dark matter must be smallest. Wrong sign of spatial gradient")
    print("     for halo phenomenology, for every kappa_W.")
    print()
    print("Survival routes (burden on UFFT, recorded as obligations):")
    print()
    print("  S1. Trigger inversion: relaxation favored by LOW curvature")
    print("      (alpha_eff increasing in the invariant) -- changes the memo's")
    print("      mechanism but matches the dark-matter spatial profile;")
    print("      must then explain why laboratory confinement (high constraint)")
    print("      triggers relaxation while stellar tides do not.")
    print("  S2. Derived screening: a mechanism making nucleation depend on")
    print("      something other than a local curvature threshold (e.g.")
    print("      environment-dependent alpha_0, gradient/nonlocal terms).")
    print("  S3. Retreat: drop the dark-sector claim; keep the boundary/Casimir")
    print("      sector (independent coupling gamma/a^2, NOT killed here).")
    print()
    print("Scope note: this verdict does NOT touch UFFT's Casimir/boundary")
    print("sector or the bulk-frustration -> Lambda sector. Trial A continues")
    print("with those sectors; the tidal sector is closed pending S1-S3.")

    with out.governance_assessments():
        out.line("Trial A2 verdict: minimal TVN sector KILLED at gate G26",
                 StatusMark.PASS,
                 "structural kill (up-set + profile inversion); Casimir and Lambda sectors unaffected")
    with out.unresolved_obligations():
        out.line("S1/S2: derive trigger inversion or screening for any revived tidal sector",
                 StatusMark.OBLIGATION,
                 "low-curvature-triggered relaxation or non-threshold mechanism required")
        out.line("re-run G26 against any revived tidal sector before other gates",
                 StatusMark.OBLIGATION,
                 "the hierarchy witness stands regardless of parameter choices")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns, ratio: float, r_eq: float) -> None:
    ns.record_derivation(
        derivation_id="point_mass_tidal_invariant_a2",
        inputs=[],
        output=sp.Symbol("six_G2M2_over_r6"),
        method="Hessian of -GM/r on axis; eigenvalues (-2,1,1)GM/r^3; sum of squares",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="tidal_invariant",
        scope="E_ij E^ij = 6 G^2 M^2 / r^6 for a point mass (trace-free verified); "
              "Schwarzschild C^2 = 48 G^2 M^2/(c^4 r^6) is the covariant counterpart",
    )
    ns.record_derivation(
        derivation_id="tidal_hierarchy_witness_a2",
        inputs=[],
        output=sp.Float(ratio),
        method="I(Sun,1AU)/I(midpoint of 1e12 Msun pair at 50 kpc); equal-invariant radius",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="hierarchy_witness",
        scope=f"ratio ~ {ratio:.1e}; super-threshold bubble around Sun r_eq ~ {r_eq:.2e} m (~2 pc); "
              "astronomical inputs are order-of-magnitude stage props",
    )
    ns.record_derivation(
        derivation_id="nucleation_upset_theorem_a2",
        inputs=[],
        output=sp.Symbol("upset_in_invariant"),
        method="alpha_eff = alpha_0 - kappa_W*I strictly decreasing => {I > I_c} is an up-set",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="structural_theorem",
        scope="bridge nucleation implies nucleation everywhere the invariant is larger",
    )
    ns.record_derivation(
        derivation_id="relaxation_profile_monotone_a2",
        inputs=[],
        output=sp.Symbol("chi_star_monotone"),
        method="chi_*/sqrt(alpha/lamda) -> 1 as alpha_excess -> oo (sympy limit)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="profile_theorem",
        scope="relaxation amplitude grows (or clamps) with the invariant; induced source "
              "profile inverted relative to dark-matter requirements",
    )

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="kill_minimal_tvn_dark_sector_a2",
        script_id=SCRIPT_ID,
        branch_id="ufft_minimal_weyl_threshold_dark_matter",
        status=GovernanceStatus.FAILED_BY_WITNESS,
        tier=ClaimTier.EXCLUSION,
        obligation_ids=["derive_trigger_inversion_or_screening_a2"],
        description=(
            "Minimal TVN (alpha_eff = alpha_0 - kappa_W * invariant, threshold "
            "nucleation) cannot serve the dark-sector role: the nucleation set is "
            "an up-set in the tidal invariant, the solar-system invariant exceeds "
            "galactic-bridge values by ~34 orders of magnitude (witness: "
            "tidal_hierarchy_witness_a2), and the induced-source profile is "
            "inverted relative to halo phenomenology for every coupling value. "
            "The kill is structural, parameter-free. UFFT's Casimir/boundary and "
            "bulk-Lambda sectors are unaffected."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_trigger_inversion_or_screening_a2",
        script_id=SCRIPT_ID,
        title="Derive trigger inversion or screening before reviving any tidal sector",
        status=ObligationStatus.OPEN,
        required_by=["trial_A_verdict"],
        description=(
            "Survival routes: (S1) relaxation favored by LOW curvature, with an "
            "explanation of why laboratory confinement still triggers it; (S2) a "
            "derived screening mechanism replacing the local curvature threshold; "
            "(S3) retreat to boundary/Casimir + Lambda sectors only."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="trial_A_post_g26_route_a2",
        script_id=SCRIPT_ID,
        name="Trial A continuation after G26: Casimir + Lambda sectors only",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_trigger_inversion_or_screening_a2"],
        activation_conditions=[
            "tidal/dark-sector claims suspended pending S1/S2",
            "remaining live gates for the surviving sectors: G25 (quantitative), "
            "G04 (chi scalar safety), G02 (flat stability), G20 (Weyl^2 ghost check "
            "now applies only if the covariant coupling is retained), G23/G24",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_structural_kill_a2",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.EXCLUSION,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Gate G26 kills the minimal Weyl/tidal-threshold nucleation sector of "
            "UFFT for the dark-sector role, by the up-set theorem plus the "
            "solar/galactic hierarchy witness plus profile inversion. The kill is "
            "independent of all coupling values. Casimir/boundary and "
            "bulk-frustration sectors survive and continue through Trial A."
        ),
        derivation_ids=[
            "point_mass_tidal_invariant_a2",
            "tidal_hierarchy_witness_a2",
            "nucleation_upset_theorem_a2",
            "relaxation_profile_monotone_a2",
        ],
        obligation_ids=["derive_trigger_inversion_or_screening_a2"],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial A2: Weyl-Screening Gate (G26) vs Minimal Tidal Vacuum Nucleation")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    case_1_point_mass_invariant(out)
    ratio, r_eq = case_2_hierarchy(out)
    case_3_upset_theorem(out)
    case_4_profile_mismatch(out)
    case_5_verdict(out)

    record_results(ns, ratio, r_eq)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
