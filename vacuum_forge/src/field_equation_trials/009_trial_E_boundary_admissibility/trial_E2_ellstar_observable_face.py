# Trial E2: the observable face of ell* -- which data actually constrains beta?
#
# Group:
#   009_trial_E_boundary_admissibility
#
# Script type:
#   DERIVATION / DATA CONFRONTATION (LAYER 3, verified anchors) / CHANNEL KILL
#
# Claim under test (theory owner, after external-AI discussion):
#   "ell* is plausibly the most testable number, more so than the kappa-leak,
#    because its observable face sits in existing data -- the neutron-star
#    phase-transition edge perturbs tidal deformability measured in GW
#    inspirals."
#
# Honest findings (verified below):
#
#   T1  THE STATIC FACE. The same beta(s'')^2 term that smooths boundaries
#       (E1-c3) necessarily modifies the static two-body potential: the
#       Green function of (-Lap + beta Lap^2) is exactly
#         Newton MINUS a Yukawa of range ell* = sqrt(beta), |alpha| = 1
#       (naive scalar reduction; the f(R)-class degenerate realization
#       gives alpha = 1/3 -- the exact alpha is owed by the covariant
#       parent). Boundary smoothing and a short-range fifth-force
#       deviation are THE SAME PARAMETER. You cannot have one without
#       the other.
#
#   T2  THE EXISTING BOUND. Short-range gravity data already in the data
#       gate pipeline (Lee 2020, VERIFIED_FROM_ABSTRACT: |alpha| = 1
#       excluded for lambda >= 38.6 um) therefore bounds
#         ell* < 38.6 um  (at |alpha| = 1),   beta < 1.5e-9 m^2.
#       For alpha = 1/3 the bound weakens to that curve's 1/3-crossing --
#       which requires the already-registered alpha(lambda) digitization.
#
#   T3  THE HIERARCHY KILL. With ell* capped at tens of microns, the
#       neutron-star edge-smoothing perturbation to tidal deformability
#       scales as (ell*/R_NS) ~ 3e-9, against GW measurement precision
#       no better than ~1e-1. Shortfall >= 3e7 at maximum generosity:
#       the GW channel for ell* is KILLED by the bench-top bound.
#
#   T4  THE CONVERGENCE. The testable face of ell* is the SAME micron
#       window as the UFFT squeeze (29.9 um < a_disc < 38.6 um). Two
#       independent program parameters now point at one experimental
#       window; the alpha(lambda) digitization obligation is doubly
#       load-bearing.
#
# So the claim's core insight survives (ell* IS data-active today, unlike
# the kappa-leak) but its dataset inverts: the data that constrains beta
# is Eot-Wash/Casimir-class bench-top data, not gravitational waves.

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
        dependency_id="e1_beta_mechanism_dependency_e2",
        upstream_script_id="009_trial_E_boundary_admissibility__trial_E1_sharp_source_gate",
        upstream_derivation_id="beta_smoothing_mechanism_e1",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Symbols and verified anchors
# =============================================================================

r, k = sp.symbols("r k", positive=True)
beta = sp.Symbol("beta", positive=True)
ellstar = sp.sqrt(beta)

# Layer-1 verified anchors (data gate protocol; provenance in
# src_exp/dataexp/datasets/short_range_gravity.py):
#   Lee 2020 (PRL 124, 101101; VERIFIED_FROM_ABSTRACT):
#     |alpha| = 1 Yukawa excluded for lambda >= 38.6 um.
LEE2020_ALPHA1_CROSSING_M = 38.6e-6

# Astrophysical scales for the hierarchy estimate (order-of-magnitude;
# the kill margin dwarfs any refinement):
R_NS_M = 1.2e4                 # neutron star radius ~ 12 km
GW_TIDAL_PRECISION = 1e-1      # optimistic future fractional precision on
                               # tidal deformability (GW170817-era was ~5e-1);
                               # order-of-magnitude, FROM_MEMORY -- the kill
                               # below survives any precision better than 1e0.


# =============================================================================
# Case 0: the claim under test
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Which data actually constrains beta?")
    print("Claim (theory owner / external AI): ell* is most testable via the")
    print("neutron-star phase-transition edge in GW tidal-deformability data,")
    print("because that data already exists.")
    print()
    print("Counter-hypothesis to check first: the SAME beta produces a static")
    print("two-body deviation at range ell*, so bench-top short-range gravity")
    print("data may already bound ell* -- and if the bound is microns, the")
    print("neutron-star lever arm (ell*/R_NS) is ~1e-9 and the GW channel is")
    print("dead by hierarchy. Order of operations matters: derive the static")
    print("face BEFORE trusting the astrophysical channel.")

    with out.governance_assessments():
        out.line("Trial E2 opened", StatusMark.INFO,
                 "observable face of ell*; claim tested, not adopted")


# =============================================================================
# Case 1 (T1): the static face -- boundary smoothing IS a short-range Yukawa
# =============================================================================


def case_1_static_face(out: ScriptOutput) -> None:
    header("Case 1 (T1): The static face of beta -- Newton minus Yukawa at range ell*")
    print("The E1-c3 operator acting on the static potential: (-Lap + beta Lap^2).")
    print()

    # momentum space: exact partial fraction
    propagator = 1 / (k**2 + beta * k**4)
    partial = 1 / k**2 - 1 / (k**2 + 1 / beta)
    pf_res = sp.simplify(propagator - partial)
    print(f"  momentum space:  1/(k^2 + beta k^4) - [1/k^2 - 1/(k^2 + 1/beta)] = {sp.sstr(pf_res)}")
    print("  i.e. Coulomb/Newton MINUS massive (Yukawa) propagator, mass^2 = 1/beta.")

    # position space: G(r) ~ (1/r)(1 - e^{-r/ell*}) annihilated away from origin
    Gfun = (1 - sp.exp(-r / ellstar)) / r

    def lap_radial(f):
        return sp.diff(r**2 * sp.diff(f, r), r) / r**2

    op_res = sp.simplify(-lap_radial(Gfun) + beta * lap_radial(lap_radial(Gfun)))
    print(f"  position space:  (-Lap + beta Lap^2)[(1 - e^(-r/ell*))/r] = {sp.sstr(op_res)}   (away from origin)")
    print()
    print("  THEOREM T1: the boundary-smoothing coefficient and a short-range")
    print("  Yukawa deviation are ONE parameter:")
    print("    V(r) = -(Gm/r) [1 - e^(-r/ell*)]   (naive scalar reduction: alpha = -1)")
    print("  The deviation has |alpha| = 1 at range ell* = sqrt(beta). In the")
    print("  degenerate (ghost-safe, f(R)-class) realization the tensor")
    print("  structure gives alpha = +1/3; the exact alpha is owed by the")
    print("  covariant parent. Either way |alpha| = O(1): the bench-top")
    print("  Yukawa searches apply directly.")

    ok = is_zero(pf_res) and is_zero(op_res)
    with out.derived_results():
        out.line("boundary smoothing <=> short-range Yukawa, same parameter",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 "1/(k^2+beta k^4) = 1/k^2 - 1/(k^2+1/beta); position-space Green identity verified")


# =============================================================================
# Case 2 (T2): the existing bound from the data gate pipeline
# =============================================================================


def case_2_existing_bound(out: ScriptOutput) -> None:
    header("Case 2 (T2): ell* is ALREADY bounded by the short-range anchors")
    ell_bound = LEE2020_ALPHA1_CROSSING_M
    beta_bound = ell_bound**2
    print(f"  Lee 2020 anchor (VERIFIED_FROM_ABSTRACT): |alpha| = 1 excluded for lambda >= {ell_bound*1e6:.1f} um")
    print(f"  =>  at |alpha| = 1:   ell* < {ell_bound*1e6:.1f} um")
    print(f"  =>  beta = ell*^2 < {beta_bound:.2e} m^2")
    print()
    print("  Caveats, recorded: (i) if the parent's realization gives")
    print("  alpha = 1/3 (f(R)-class), the bound weakens to that curve's")
    print("  1/3-crossing -- reading it requires the alpha(lambda) curve")
    print("  digitization already registered as a manual artifact in")
    print("  src_exp/dataexp (this makes that obligation doubly load-bearing).")
    print("  (ii) The bound assumes the deviation couples to ordinary matter")
    print("  at gravitational strength, which T1's derivation gives it.")
    print()
    print("  CONSEQUENCE: ell* is a micron-class length TODAY, before any")
    print("  parent functional is written. Boundary smoothing, if present at")
    print("  all, is capped at the width of a human hair.")

    with out.sample_results():
        out.line(f"ell* < {ell_bound*1e6:.1f} um at |alpha| = 1 (Lee 2020 anchor)",
                 StatusMark.PASS,
                 f"beta < {beta_bound:.2e} m^2; alpha = 1/3 reading blocked on alpha(lambda) digitization")


# =============================================================================
# Case 3 (T3): the GW tidal channel dies by hierarchy
# =============================================================================


def case_3_gw_hierarchy(out: ScriptOutput) -> None:
    header("Case 3 (T3): Neutron-star tidal channel -- hierarchy kill")
    ell_bound = LEE2020_ALPHA1_CROSSING_M
    lever = ell_bound / R_NS_M
    shortfall = GW_TIDAL_PRECISION / lever
    print("  Smoothing an internal density discontinuity over width ell*")
    print("  perturbs the density profile in a shell of fractional volume")
    print("  ~ ell*/R_NS; the Love number / tidal deformability response is a")
    print("  smooth O(1) functional of the profile, so")
    print()
    print(f"    delta(Lambda)/Lambda  ~  (ell*/R_NS) x O(1)  <=  {lever:.1e}")
    print()
    print(f"  GW tidal precision (optimistic, order-of-magnitude): ~{GW_TIDAL_PRECISION:.0e}")
    print(f"  SHORTFALL >= {shortfall:.1e}  at maximum generosity.")
    print()
    print("  The bench-top bound makes the GW face invisible: for NS tidal")
    print("  data to see ell*, it would need ell* ~ meters-to-kilometers,")
    print("  excluded by bench-top gravity by >= 8 orders of magnitude.")
    print("  The claim's dataset inverts: ell* IS data-active (the insight")
    print("  survives), but the active data is Eot-Wash/Casimir-class, not GW.")
    print()
    print("  Threats to validity: the O(1) response factor and the precision")
    print("  figure are order-of-magnitude (precision FROM_MEMORY); the kill")
    print("  margin (>= 7 orders) dwarfs both. A rescue would need a NS")
    print("  observable with ell*-sensitivity amplified by >= 1e7, which no")
    print("  tidal-deformability mechanism provides.")

    killed = shortfall > 1e6
    with out.counterexamples():
        out.line("GW tidal deformability as the discovery channel for ell*",
                 StatusMark.FAIL if killed else StatusMark.PASS,
                 f"hierarchy kill: lever arm {lever:.0e} vs precision {GW_TIDAL_PRECISION:.0e}; shortfall >= {shortfall:.0e}")


# =============================================================================
# Case 4: verdict and the convergence
# =============================================================================


def case_4_verdict(out: ScriptOutput) -> None:
    header("Case 4: Trial E2 verdict")
    print("VERDICT on the claim: half right, dataset inverted.")
    print()
    print("  RIGHT: ell* is data-active today, unlike the kappa-leak -- it is")
    print("         the program's most immediately testable parameter.")
    print("  WRONG: the active data is bench-top short-range gravity, which")
    print("         already caps ell* < ~38.6 um (|alpha| = 1). The NS/GW")
    print("         channel is killed by >= 7 orders of hierarchy.")
    print()
    print("CONVERGENCE RECORDED: the testable face of ell* lands in the same")
    print("micron window as the UFFT squeeze (29.9 um < a_disc < 38.6 um).")
    print("Two independent program parameters now funnel into one experimental")
    print("window; the alpha(lambda) digitization is doubly load-bearing and")
    print("is promoted to the data program's top priority.")
    print()
    print("Standing E1 conclusion sharpened: IF K_strain has beta != 0, the")
    print("prediction is a micron-or-smaller smoothing scale plus a bench-top")
    print("Yukawa deviation at the SAME range -- a doubly-faced, falsifiable")
    print("signature. IF future bench-top data pushes the |alpha| ~ O(1)")
    print("exclusion far below the parent's natural ell*, beta = 0 is forced")
    print("and the smooth-boundary intuition dies by data.")

    with out.governance_assessments():
        out.line("Trial E2 verdict: ell* bench-top-bounded; GW channel killed",
                 StatusMark.PASS,
                 "claim's insight retained, dataset corrected; convergence with UFFT window recorded")
    with out.unresolved_obligations():
        out.line("alpha(lambda) digitization (Lee 2020 / Tan 2020 curves)",
                 StatusMark.OBLIGATION,
                 "now constrains BOTH a_disc and ell* (alpha = 1/3 reading); top data priority")
        out.line("exact alpha of the beta-term in the covariant parent (1 vs 1/3 vs other)",
                 StatusMark.OBLIGATION,
                 "needed to read the bound precisely; naive scalar gives -1, f(R)-class gives +1/3")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="yukawa_face_of_beta_e2",
        inputs=[],
        output=sp.Symbol("boundary_smoothing_equals_yukawa_range_ellstar"),
        method="exact partial fraction of 1/(k^2 + beta k^4) and position-space "
               "Green identity for (1 - e^(-r/ell*))/r",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="equivalence_theorem",
        scope="the E1 smoothing coefficient and a |alpha| = O(1) short-range Yukawa are one parameter",
    )
    ns.record_derivation(
        derivation_id="ellstar_benchtop_bound_e2",
        inputs=[],
        output=sp.Symbol("ellstar_below_38p6_um_at_alpha_1"),
        method="Layer-3 confrontation with the Lee 2020 VERIFIED_FROM_ABSTRACT anchor "
               "(|alpha| = 1 excluded for lambda >= 38.6 um)",
        status=Status.OBSERVATIONAL_CONSTRAINT,
        record_kind=RecordKind.DERIVATION,
        result_type="data_bound",
        scope="beta < 1.5e-9 m^2 at |alpha| = 1; alpha = 1/3 reading blocked on curve digitization",
    )
    ns.record_derivation(
        derivation_id="ns_tidal_hierarchy_kill_e2",
        inputs=[],
        output=sp.Symbol("gw_tidal_channel_shortfall_3e7"),
        method="lever arm ell*/R_NS ~ 3e-9 vs tidal precision ~1e-1 (order-of-magnitude)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="channel_exclusion",
        scope="NS tidal deformability cannot see a bench-top-capped ell*; margin >= 7 orders",
    )

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="kill_gw_tidal_channel_for_ellstar_e2",
        script_id=SCRIPT_ID,
        branch_id="ellstar_discovery_via_ns_tidal_deformability",
        status=GovernanceStatus.FAILED_BY_WITNESS,
        tier=ClaimTier.EXCLUSION,
        obligation_ids=[],
        description=(
            "The proposal to treat NS tidal deformability in GW data as the discovery "
            "channel for ell* is killed by hierarchy: the same beta produces a "
            "bench-top Yukawa already capped at ell* < ~38.6 um (|alpha| = 1, Lee 2020), "
            "making the NS lever arm ell*/R_NS ~ 3e-9 against ~1e-1 measurement "
            "precision. Shortfall >= 3e7 at maximum generosity."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="alpha_curve_digitization_priority_e2",
        script_id=SCRIPT_ID,
        title="alpha(lambda) curve digitization: now constrains BOTH a_disc and ell*",
        status=ObligationStatus.OPEN,
        required_by=["data_program"],
        description="Manual artifacts with instructions already registered in src_exp/dataexp; "
                    "promoted to top data priority by the E2/UFFT window convergence.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="parent_alpha_value_e2",
        script_id=SCRIPT_ID,
        title="Exact Yukawa amplitude alpha of the beta-term in the covariant parent",
        status=ObligationStatus.OPEN,
        required_by=["k_strain_program"],
        description="Naive scalar reduction gives alpha = -1; degenerate f(R)-class gives +1/3; "
                    "the parent must say which (sign is itself a discriminator).",
    ))

    ns.record_route(RouteRecord(
        route_id="ellstar_benchtop_route_e2",
        script_id=SCRIPT_ID,
        name="ell* discovery/exclusion route: bench-top short-range gravity (micron window)",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["alpha_curve_digitization_priority_e2", "parent_alpha_value_e2"],
        activation_conditions=[
            "same experimental window as the UFFT squeeze (29.9-38.6 um): shared apparatus",
            "future |alpha| ~ O(1) exclusions below the parent's natural ell* force beta = 0",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="ellstar_observable_face_e2",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The boundary-smoothing scale ell* = sqrt(beta) and a gravitational-strength "
            "short-range Yukawa deviation are the same parameter (exact propagator "
            "identity). Existing bench-top data therefore caps ell* < ~38.6 um at "
            "|alpha| = 1 (Lee 2020 anchor), making ell* the program's most immediately "
            "data-active parameter -- through bench-top gravity, NOT gravitational "
            "waves: the NS tidal channel is killed by >= 7 orders of hierarchy. "
            "Convergence: ell*'s window coincides with the UFFT squeeze window; the "
            "alpha(lambda) digitization is doubly load-bearing."
        ),
        derivation_ids=[
            "yukawa_face_of_beta_e2",
            "ellstar_benchtop_bound_e2",
            "ns_tidal_hierarchy_kill_e2",
        ],
        obligation_ids=["alpha_curve_digitization_priority_e2", "parent_alpha_value_e2"],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial E2: The Observable Face of ell*")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    case_1_static_face(out)
    case_2_existing_bound(out)
    case_3_gw_hierarchy(out)
    case_4_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
