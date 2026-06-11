# Trial C1: two-body burden ledger
#
# Group:
#   002_trial_C_burden_ledger
#
# Script type:
#   DERIVATION / LEDGER / BRANCH DISCRIMINATOR
#
# Purpose
# -------
# Settle the structure of the two-body burden ledger by calculation:
#
#   E_burden = J_curv + E_interface + E_substance/exchange + ...
#
# Questions (gate G01 attack; feeds G24, G21 and Trials A and B):
#
#   1. Which burden component carries the separation dependence?
#   2. What force law does burden-gradient descent produce, per sign branch?
#   3. Can interface subadditivity supply the long-range force?
#   4. Is the cross-term magnitude consistent with the merger-energy gate?
#
# Sources:
#   ontology_and_mechanism/positive_curvature_energy_J_curv.md
#   ontology_and_mechanism/radius_scaling_positive_curvature_energy_j_curv.md
#   ontology_and_mechanism/gravity_as_vacuum_burden_reduction.md
#   ontology_and_mechanism/p4_sign_fork_infall_ledger.md
#
# Discipline: the goal is to demote or promote MECHANISMS, not to fit
# parameters. The Green-identity step that evaluates the interaction
# integral uses the distributional identity Lap(Phi_2) = 4*pi*G*rho_2 with
# a point source; that step is recorded explicitly as an imported standard
# identity, not hidden.

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
        dependency_id="charter_jcurv_cross_term_dependency_c1",
        upstream_script_id="000_trial_charter__trial_gate_inventory",
        upstream_derivation_id="trial_jcurv_cross_term_t000",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="charter_infall_budget_dependency_c1",
        upstream_script_id="000_trial_charter__trial_gate_inventory",
        upstream_derivation_id="trial_traceful_infall_budget_t000",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Symbols
# =============================================================================

G, c = sp.symbols("G c", positive=True)
m1, m2, m, M = sp.symbols("m1 m2 m M", positive=True)
d, r, R = sp.symbols("d r R", positive=True)
rho0 = sp.Symbol("rho0", positive=True)


# =============================================================================
# Case 0
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: The two-body burden question")
    print("The burden picture proposes attraction = motion toward lower total")
    print("vacuum burden (gravity_as_vacuum_burden_reduction.md):")
    print()
    print("  F = -dE_burden/dd,   E_burden = J_curv + E_interface + E_substance + ...")
    print()
    print("This script computes, per component:")
    print()
    print("  the separation dependence, the implied gradient-descent force law,")
    print("  the sign branch structure, and the merger-energy magnitude.")

    with out.governance_assessments():
        out.line("Trial C1 opened",
                 StatusMark.INFO,
                 "mechanism discrimination by ledger; no parameter fitting")


# =============================================================================
# Case 1: the cross-term by Green identity
# =============================================================================


def case_1_cross_term(out: ScriptOutput):
    header("Case 1: Interaction term of quadratic field energy (Green identity)")
    print("Positive-magnitude convention (P4 as written):")
    print()
    print("  J_curv = (1/8 pi G) int |grad Phi|^2 d^3x,   Phi = Phi_1 + Phi_2")
    print()
    print("Cross-term:")
    print()
    print("  X(d) = (1/4 pi G) int grad Phi_1 . grad Phi_2 d^3x")
    print("       = -(1/4 pi G) int Phi_1 Lap(Phi_2) d^3x        [by parts; decay at infinity]")
    print("       = -(1/4 pi G) * Phi_1(x_2) * 4 pi G m2          [Lap Phi_2 = 4 pi G m2 delta^3]")
    print("       = -Phi_1(x_2) m2 = +G m1 m2 / d                 [Phi_1(x_2) = -G m1/d]")
    print()

    Phi1_at_2 = -G * m1 / d
    X = sp.simplify(-(Phi1_at_2) * m2)
    X_expected = G * m1 * m2 / d

    # consistency with the charter's fixed-radius merger identity:
    def J(mm):
        return G * mm**2 / (2 * R)
    merger_cross = sp.simplify(J(m1 + m2) - J(m1) - J(m2))  # = +G m1 m2 / R
    merger_match = sp.simplify(merger_cross - X.subs(d, R))

    print(f"  X(d) = {sp.sstr(X)}")
    print(f"  charter merger identity: J(m1+m2) - J(m1) - J(m2) = {sp.sstr(merger_cross)}")

    with out.derived_results():
        out.line("cross-term X(d) = +G m1 m2 / d",
                 StatusMark.PASS if is_zero(X - X_expected) else StatusMark.FAIL,
                 "positive: approaching wells RAISES stored quadratic curvature energy")
        out.line("consistent with fixed-R merger identity",
                 StatusMark.PASS if is_zero(merger_match) else StatusMark.FAIL,
                 "the two routes to the cross-term agree (superadditivity confirmed)")
    return X


# =============================================================================
# Case 2: gradient-descent force law per sign branch
# =============================================================================


def case_2_force_per_branch(X, out: ScriptOutput):
    header("Case 2: Burden-gradient descent force law, per sign branch")
    print("Force on the separation coordinate under energy-gradient descent:")
    print()
    print("  F(d) = -dE/dd")
    print()

    E_pos = X                       # positive-definite branch: E(d) = const + G m1 m2/d
    E_neg = -X                      # negative interaction branch (standard Newtonian field energy)

    F_pos = sp.simplify(-sp.diff(E_pos, d))
    F_neg = sp.simplify(-sp.diff(E_neg, d))
    newton = -G * m1 * m2 / d**2    # attractive = force decreasing d (negative sign on d-axis)

    print(f"  positive branch:  E = +G m1 m2/d  =>  F = {sp.sstr(F_pos)}   (> 0: REPULSIVE)")
    print(f"  negative branch:  E = -G m1 m2/d  =>  F = {sp.sstr(F_neg)}   (< 0: attractive, Newton)")
    print()
    print("THE SHARP RESULT: under the positive-definite reading of P4 with")
    print("quadratic gradient energy, gradient descent on configuration energy")
    print("alone predicts REPULSION. Attraction in the positive branch cannot be")
    print("configuration-energy minimization; it must be FUNDED dynamics:")
    print("P6 substance exchange pays both the kinetic energy and the rising")
    print("well energy (charter budget: substance destroyed = 2*dKE).")
    print()
    print("Equivalently: 'gravity = burden reduction' with J_curv as the burden")
    print("is self-contradictory; 'gravity = funded exchange against rising")
    print("burden' is the consistent positive-branch statement.")

    pos_repulsive = sp.simplify(F_pos * d**2 / (G * m1 * m2)) == 1
    neg_newton = is_zero(F_neg - newton)

    with out.derived_results():
        out.line("positive branch: F = +G m1 m2/d^2 (repulsive)",
                 StatusMark.PASS if pos_repulsive else StatusMark.FAIL,
                 "burden-gradient descent on positive J_curv pushes masses APART")
        out.line("negative branch: F = -G m1 m2/d^2 (Newton)",
                 StatusMark.PASS if neg_newton else StatusMark.FAIL,
                 "energy-gradient attraction requires the negative/indefinite interaction branch")

    with out.counterexamples():
        out.line("'gravity = J_curv burden reduction' as long-range mechanism",
                 StatusMark.FAIL,
                 "killed by sign: the d-dependent burden component RISES on approach in the positive branch")
    return F_pos, F_neg


# =============================================================================
# Case 3: interface term -- step, not gradient
# =============================================================================


def case_3_interface_term(out: ScriptOutput):
    header("Case 3: Interface/surface-gravity term: subadditive but separation-blind")
    print("The burden-reduction note's subadditivity toy: J_sg = G M / R^2 with")
    print("R = (3M/(4 pi rho0))^(1/3) at fixed density:")
    print()

    R_of_M = (3 * M / (4 * sp.pi * rho0)) ** sp.Rational(1, 3)
    J_sg = sp.simplify(G * M / R_of_M**2)
    ratio = sp.simplify(J_sg.subs(M, 2 * M) / (2 * J_sg))
    ratio_expected = 2 ** sp.Rational(1, 3) / 2

    print(f"  J_sg(M) = {sp.sstr(J_sg)}   ~  M^(1/3)")
    print(f"  J_sg(2M) / (2 J_sg(M)) = {sp.sstr(ratio)} = 2^(-2/3) < 1   (subadditive)")
    print()
    print("BUT: for two separated bodies, each interface is a property of its own")
    print("boundary. Before contact, the interface burden of the pair is")
    print()
    print("  E_int(d) = J_sg(m1) + J_sg(m2)   for all d > R1 + R2")
    print()
    print("which is separation-INDEPENDENT:")

    E_int = J_sg.subs(M, m1) + J_sg.subs(M, m2)
    dE_int = sp.simplify(sp.diff(E_int, d))
    print(f"  dE_int/dd = {sp.sstr(dE_int)}")
    print()
    print("So interface subadditivity contributes a STEP at merger, not a")
    print("gradient during approach. It cannot supply the inverse-square law.")
    print("The only d-dependent burden component at long range is the cross-term.")

    subadd_ok = is_zero(ratio - ratio_expected)
    step_ok = is_zero(dE_int)

    with out.derived_results():
        out.line("interface toy is subadditive: 2^(-2/3) < 1",
                 StatusMark.PASS if subadd_ok else StatusMark.FAIL,
                 "merging is cheaper in interface burden -- but only AT merger")
        out.line("interface burden is separation-blind before contact",
                 StatusMark.PASS if step_ok else StatusMark.FAIL,
                 "dE_int/dd = 0 for d > R1 + R2: a step at merger, not a force")

    with out.counterexamples():
        out.line("interface subadditivity as origin of the 1/d^2 force",
                 StatusMark.FAIL,
                 "no separation dependence at long range; cannot drive approach")
    return E_int


# =============================================================================
# Case 4: merger-energy magnitude (gate G24, order-of-magnitude only)
# =============================================================================


def case_4_merger_magnitude(out: ScriptOutput):
    header("Case 4: Cross-term magnitude vs the merger-energy gate (diagnostic)")
    print("Equal masses m, merger-scale separation d = N * r_s, r_s = 2 G m / c^2:")
    print()

    N = sp.Symbol("N", positive=True)
    r_s = 2 * G * m / c**2
    X_at_merger = sp.simplify(G * m**2 / (N * r_s))
    fraction = sp.simplify(X_at_merger / (2 * m * c**2))

    print(f"  |X| at d = N r_s:  {sp.sstr(X_at_merger)} = m c^2 / (2N)")
    print(f"  fraction of total mass-energy 2 m c^2:  {sp.sstr(fraction)} = 1/(4N)")
    print()
    print("  Observed BBH radiated fraction ~ 5%  =>  1/(4N) ~ 0.05  =>  N ~ 5.")
    print("  Few-Schwarzschild-radius separations: order-of-magnitude CONSISTENT.")
    print()
    print("  Mass scaling: |X| = G m1 m2 / d. At fixed compactness d ~ G(m1+m2)/c^2:")

    X_general = G * m1 * m2 / (sp.Symbol("N", positive=True) * 2 * G * (m1 + m2) / c**2)
    X_general = sp.simplify(X_general)
    reduced_mass_form = sp.simplify(X_general - c**2 * (m1 * m2 / (m1 + m2)) / (2 * sp.Symbol("N", positive=True)))

    print(f"  |X| = c^2/(2N) * m1 m2/(m1+m2)   (reduced-mass scaling)")
    print()
    print("  GR's radiated energy also scales with the symmetric mass ratio")
    print("  nu = m1 m2/(m1+m2)^2; the cross-term carries the same m1 m2/(m1+m2)")
    print("  structure. Recorded as DIAGNOSTIC consistency, not precision (G24")
    print("  precision verdict requires the actual functional and waveforms).")

    frac_ok = is_zero(fraction - 1 / (4 * N))
    scaling_ok = is_zero(reduced_mass_form)

    with out.sample_results():
        out.line("merger fraction = 1/(4N); ~5% at N ~ 5",
                 StatusMark.PASS if frac_ok else StatusMark.FAIL,
                 "cross-term magnitude is the right size at merger separations (diagnostic)")
        out.line("reduced-mass scaling m1 m2/(m1+m2) at fixed compactness",
                 StatusMark.PASS if scaling_ok else StatusMark.FAIL,
                 "same mass-ratio structure as GR's radiated energy (diagnostic, not precision)")


# =============================================================================
# Case 5: branch table and verdict
# =============================================================================


def case_5_verdict(out: ScriptOutput) -> None:
    header("Case 5: Sharpened fork and Trial C1 verdict")
    print("The two-body ledger by component:")
    print()
    print("  component        d-dependence       sign        role")
    print("  -------------    ---------------    --------    ----------------------------")
    print("  J_curv cross     +G m1 m2/d         positive    rises on approach (funded)")
    print("  interface        none (d > R1+R2)   n/a         merger step only")
    print("  substance (P6)   via dynamics       payer       funds KE + rising well = 2*dKE")
    print()
    print("Branch consequences:")
    print()
    print("  POSITIVE branch (P4 as written):")
    print("    - attraction is NOT energy-gradient descent; it is P6-funded exchange")
    print("    - burden-reduction survives only as merger/interface accounting")
    print("    - anti-singularity lever (J -> inf as R -> 0) AVAILABLE")
    print("    - open burden: derive F = -G M m/r^2 from P6 exchange dynamics;")
    print("      traceful budget must hide under the Cassini gate (G21)")
    print()
    print("  NEGATIVE/INDEFINITE branch:")
    print("    - attraction = energy-gradient descent with correct Newton law")
    print("    - must survive G02 (flat-vacuum stability) and G03 (GW energy sign)")
    print("    - anti-singularity lever LOST unless rebuilt from interface terms")
    print()
    print("Trial C1 verdict: MECHANISM DEMOTION (a kill within the trial).")
    print("  'Gravity as vacuum burden reduction' is DEMOTED as the long-range")
    print("  force mechanism: its d-dependent component has the wrong sign in the")
    print("  positive branch and its subadditive component has no d-dependence.")
    print("  It survives as merger accounting. The live fork is now exactly two")
    print("  named programs: funded-exchange (positive, P6, traceful budget) vs")
    print("  indefinite-energy gradient descent (the K_strain signature question).")

    with out.governance_assessments():
        out.line("Trial C1 verdict: burden-reduction demoted as long-range mechanism",
                 StatusMark.PASS,
                 "killed by sign + separation-blindness; survives as merger/interface accounting")
    with out.unresolved_obligations():
        out.line("positive branch: derive inverse-square law from P6 exchange dynamics",
                 StatusMark.OBLIGATION,
                 "without it the positive branch has no force mechanism at all")
        out.line("positive branch: traceful budget vs Cassini (G21 kappa-leak bound)",
                 StatusMark.OBLIGATION,
                 "2*dKE substance budget must not disturb gamma at parts in 10^5")
        out.line("negative/indefinite branch: G02 flat stability + G03 GW energy sign",
                 StatusMark.OBLIGATION,
                 "sector-indefinite signature is the surviving form (K_strain question)")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns, X) -> None:
    ns.record_derivation(
        derivation_id="ledger_cross_term_green_identity_c1",
        inputs=[],
        output=X,
        method=(
            "X = (1/4piG) int grad Phi1 . grad Phi2 = -(1/4piG) int Phi1 Lap Phi2 "
            "= -Phi1(x2) m2 = +G m1 m2/d; imported standard identity: "
            "Lap Phi2 = 4 pi G m2 delta^3(x - x2)"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="interaction_energy",
        scope="quadratic gradient energy, positive-magnitude convention, point sources",
    )
    ns.record_derivation(
        derivation_id="ledger_positive_branch_repulsion_c1",
        inputs=[X],
        output=sp.Symbol("F_pos_repulsive"),
        method="F = -d/dd (+G m1 m2/d) = +G m1 m2/d^2 > 0",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="force_law_branch",
        scope=(
            "burden-gradient descent on positive-definite quadratic curvature energy "
            "is REPULSIVE; positive-branch attraction must be P6-funded dynamics"
        ),
    )
    ns.record_derivation(
        derivation_id="ledger_interface_separation_blind_c1",
        inputs=[],
        output=sp.Integer(0),
        method="d/dd [J_sg(m1) + J_sg(m2)] = 0 for d > R1 + R2; subadditivity 2^(-2/3) verified",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="separation_independence",
        scope="interface burden is a merger step, not a long-range force source",
    )
    ns.record_derivation(
        derivation_id="ledger_merger_magnitude_diagnostic_c1",
        inputs=[],
        output=sp.Symbol("one_over_4N"),
        method="|X|/(2mc^2) = 1/(4N) at d = N r_s; reduced-mass scaling at fixed compactness",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="merger_energy_scale",
        scope="order-of-magnitude consistency with G24; not a precision verdict",
    )

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="demote_burden_reduction_long_range_c1",
        script_id=SCRIPT_ID,
        branch_id="gravity_as_burden_reduction_long_range",
        status=GovernanceStatus.FAILED_BY_WITNESS,
        tier=ClaimTier.EXCLUSION,
        evidence_ids=[],
        obligation_ids=[],
        description=(
            "Burden-gradient descent cannot be the long-range attraction mechanism: "
            "the d-dependent component (J_curv cross-term) is POSITIVE (+G m1 m2/d, "
            "repulsive under descent) and the subadditive component (interface) is "
            "separation-blind before contact. Burden reduction survives only as "
            "merger/interface accounting. Witnesses: ledger_positive_branch_repulsion_c1, "
            "ledger_interface_separation_blind_c1."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_inverse_square_from_p6_exchange_c1",
        script_id=SCRIPT_ID,
        title="Positive branch: derive F = -G M m / r^2 from P6 exchange dynamics",
        status=ObligationStatus.OPEN,
        required_by=["trial_C_verdict"],
        description=(
            "With burden descent demoted, the positive branch's force mechanism must "
            "come from funded substance exchange (budget 2*dKE). Until derived, the "
            "positive branch has bookkeeping but no force law."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="traceful_budget_vs_cassini_c1",
        script_id=SCRIPT_ID,
        title="Positive branch: 2*dKE traceful budget vs Cassini gamma bound (G21)",
        status=ObligationStatus.OPEN,
        required_by=["trial_C_verdict"],
        description=(
            "The substance destruction funding infall must not source kappa beyond "
            "|gamma - 1| < 2.3e-5 in static exteriors."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="indefinite_branch_g02_g03_c1",
        script_id=SCRIPT_ID,
        title="Negative/indefinite branch: pass G02 (flat stability) and G03 (GW energy sign)",
        status=ObligationStatus.OPEN,
        required_by=["trial_C_verdict"],
        description=(
            "Energy-gradient attraction requires negative interaction energy; a globally "
            "negative configuration energy breaks the P5 ground state and the observed "
            "positive GW energy. The surviving form is sector-indefinite signature -- "
            "the K_strain signature question."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="trial_C_continuation_c1",
        script_id=SCRIPT_ID,
        name="Trial C continuation: branch-resolution (C2)",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_inverse_square_from_p6_exchange_c1",
            "traceful_budget_vs_cassini_c1",
            "indefinite_branch_g02_g03_c1",
        ],
        activation_conditions=[
            "burden-reduction is no longer available as the long-range mechanism",
            "exactly two programs remain: P6-funded exchange vs indefinite-signature descent",
            "any candidate functional fed to Trial A or B must declare which program it uses",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="two_body_ledger_structure_c1",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Two-body burden ledger: the only separation-dependent burden component at "
            "long range is the field-energy cross-term, equal to +G m1 m2/d in the "
            "positive-magnitude convention (Green identity; consistent with the fixed-R "
            "merger identity). Interface subadditivity (2^(-2/3)) is separation-blind "
            "before contact. Therefore burden-gradient descent yields repulsion in the "
            "positive branch and Newtonian attraction only in the negative/indefinite "
            "branch. Cross-term magnitude at merger separations is 1/(4N) of total "
            "mass-energy with reduced-mass scaling (diagnostic consistency with G24)."
        ),
        derivation_ids=[
            "ledger_cross_term_green_identity_c1",
            "ledger_positive_branch_repulsion_c1",
            "ledger_interface_separation_blind_c1",
            "ledger_merger_magnitude_diagnostic_c1",
        ],
        obligation_ids=[
            "derive_inverse_square_from_p6_exchange_c1",
            "traceful_budget_vs_cassini_c1",
            "indefinite_branch_g02_g03_c1",
        ],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial C1: Two-Body Burden Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    X = case_1_cross_term(out)
    case_2_force_per_branch(X, out)
    case_3_interface_term(out)
    case_4_merger_magnitude(out)
    case_5_verdict(out)

    record_results(ns, X)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
