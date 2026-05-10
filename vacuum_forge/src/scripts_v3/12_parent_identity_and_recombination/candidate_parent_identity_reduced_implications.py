# Candidate parent identity reduced implications
#
# Group:
#   12_parent_identity_and_recombination
#
# Script type:
#   INVENTORY

# Purpose
# -------
# The parent identity exclusion constraints ruled out false parent identities:
#
#   no decorative Bianchi restatement
#   no ordinary scalar A wave
#   no Box kappa
#   no rho double-sourced into kappa
#   no exterior kappa charge
#   no trace contamination of TT
#   no longitudinal current sourcing W_i
#   no boundary smoothing changing exterior mass
#   no Sigma_creation in ordinary closure
#   no GR coefficients inserted as derivation
#   no GR metric copied by form
#
# This script asks the positive companion question:
#
#   What must any surviving parent identity imply in each reduced sector?
#
# It does not derive the parent identity.
# It builds a reduced-sector test suite.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status, TheoryContext
from vacuumforge.metric.concrete_check import check_concrete_metric
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


@dataclass
class ReducedImplication:
    name: str
    sector: str
    parent_must_imply: str
    reduced_target: str
    why_required: str
    forbidden_alternative: str
    status: str
    missing_derivation: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="parent_identity_exclusion_constraints_marker",
        upstream_script_id="12_parent_identity_and_recombination__candidate_parent_identity_exclusion_constraints",
        upstream_derivation_id="parent_identity_exclusion_constraints_marker",
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


def build_implications() -> List[ReducedImplication]:
    return [
        ReducedImplication(
            name="R1: Static spherical A constraint",
            sector="A scalar / static spherical",
            parent_must_imply="A satisfies an areal scalar constraint sourced by rho.",
            reduced_target="Delta_areal A = 8*pi*G*rho/c^2",
            why_required="This is the strongest real reduced reconstruction and must survive parent closure.",
            forbidden_alternative="Box A ordinary scalar radiation or arbitrary Schwarzschild matching.",
            status="DERIVED_REDUCED_TARGET",
            missing_derivation="Parent projection yielding the areal operator and coefficient.",
        ),
        ReducedImplication(
            name="R2: Exterior Schwarzschild A",
            sector="A exterior",
            parent_must_imply="Exterior vacuum integration gives A_ext = 1 - 2GM/(c^2 r).",
            reduced_target="A_ext(r) = 1 - 2GM/(c^2*r)",
            why_required="This is the main real reconstruction event.",
            forbidden_alternative="Setting Schwarzschild A by metric ansatz.",
            status="DERIVED_REDUCED_TARGET",
            missing_derivation="Parent exterior vacuum reduction and mass-flux charge law.",
        ),
        ReducedImplication(
            name="R3: Exterior B reciprocal when kappa vanishes",
            sector="B / kappa exterior",
            parent_must_imply="Exterior kappa=0 gives AB=1 and therefore B=1/A.",
            reduced_target="AB = exp(2*kappa), kappa_ext=0 -> B=1/A",
            why_required="Reciprocal radial factor is necessary for Schwarzschild exterior and gamma=1 support.",
            forbidden_alternative="Independent B chosen by GR metric form.",
            status="DERIVED_REDUCED_TARGET",
            missing_derivation="Covariant/gauge interpretation of AB=e^(2 kappa).",
        ),
        ReducedImplication(
            name="R4: Weak scalar / Newtonian limit",
            sector="weak scalar",
            parent_must_imply="Weak field limit gives A ~= 1 + 2Phi/c^2 and nabla^2 Phi = 4*pi*G*rho.",
            reduced_target="A ~= 1 + 2Phi/c^2; nabla^2 Phi = 4*pi*G*rho",
            why_required="The parent must preserve the weak scalar and Newtonian limit.",
            forbidden_alternative="Scalar coefficient inserted only to match Newtonian gravity.",
            status="DERIVED_REDUCED_TARGET",
            missing_derivation="Weak-field parent expansion.",
        ),
        ReducedImplication(
            name="R5: Scalar constraint propagation",
            sector="scalar dynamics",
            parent_must_imply="Time evolution of the A constraint is compatible with continuity of rho and j_L.",
            reduced_target="partial_t C_A[A,rho] follows from continuity(rho,j_L)",
            why_required="A must remain a constraint without becoming scalar radiation.",
            forbidden_alternative="Box A scalar wave equation.",
            status="MISSING",
            missing_derivation="Continuity-compatible constraint propagation law.",
        ),
        ReducedImplication(
            name="R6: Transverse vector source",
            sector="W_i vector",
            parent_must_imply="W_i is sourced only by transverse current j_T.",
            reduced_target="curl curl W = -(alpha_W/(2*K_c))*j_T; div W=0",
            why_required="Frame-dragging shape depends on transverse current, not longitudinal continuity.",
            forbidden_alternative="P_L j sourcing W_i or free vector radiation imported by analogy.",
            status="STRUCTURAL_TARGET",
            missing_derivation="Parent current projection and normalization alpha_W/K_c.",
        ),
        ReducedImplication(
            name="R7: Angular momentum far-field shape",
            sector="W_i far field",
            parent_must_imply="Uniform rotating source reduces to angular momentum J and far-field vector dipole shape.",
            reduced_target="curl W far-field ~ J/r^3",
            why_required="This is the current vector-sector shape success.",
            forbidden_alternative="Claiming full Lense-Thirring recovery without coefficient derivation.",
            status="DERIVED_REDUCED_TARGET",
            missing_derivation="beta_W and absolute normalization from parent identity/action.",
        ),
        ReducedImplication(
            name="R8: TT tensor radiation only",
            sector="h_ij^TT",
            parent_must_imply="Ordinary long-range radiation propagates only in the TT tensor sector.",
            reduced_target="Box h_ij^TT = -C_T*S_ij^TT",
            why_required="GR-compatible radiation requires TT modes and excludes scalar breathing.",
            forbidden_alternative="A_rad, Box kappa, or free vector radiation as ordinary long-range modes.",
            status="STRUCTURAL_TARGET",
            missing_derivation="Tensor action stiffness, C_T, TT source identity.",
        ),
        ReducedImplication(
            name="R9: TT source trace exclusion",
            sector="h_ij^TT source",
            parent_must_imply="Trace and pressure do not directly source h_ij^TT.",
            reduced_target="source(h_TT) = P_TT S_ij; trace excluded",
            why_required="TT radiation must remain trace-free and not double-count kappa/trace response.",
            forbidden_alternative="Trace contamination of TT radiation.",
            status="CONSTRAINED_TARGET",
            missing_derivation="Parent projector identity for TT stress.",
        ),
        ReducedImplication(
            name="R10: Kappa trace-minimum relaxation",
            sector="kappa trace response",
            parent_must_imply="Trace/pressure shifts kappa_min and kappa relaxes first-order toward it.",
            reduced_target="dot(kappa) = -mu_kappa*K_kappa*(kappa-kappa_min)",
            why_required="Kappa must remain non-radiative trace/volume relaxation.",
            forbidden_alternative="Box kappa = alpha*trace_or_pressure.",
            status="STRUCTURAL_TARGET",
            missing_derivation="K_kappa, mu_kappa, chi_kappa, S_trace_effective from parent vacuum minimum.",
        ),
        ReducedImplication(
            name="R11: Exterior kappa neutrality",
            sector="kappa exterior",
            parent_must_imply="Ordinary closed matter has no exterior kappa charge.",
            reduced_target="Q_kappa=0; kappa->0; F_kappa(R+)=0",
            why_required="Prevents second scalar exterior field and scalar double-counting.",
            forbidden_alternative="kappa_ext ~ 1/r.",
            status="CONSTRAINED_TARGET",
            missing_derivation="Parent projection/boundary cancellation law.",
        ),
        ReducedImplication(
            name="R12: Boundary mass preservation",
            sector="boundary / interface",
            parent_must_imply="Kappa or boundary relaxation cannot change exterior A mass flux.",
            reduced_target="delta M_ext|kappa_relaxation = 0",
            why_required="Exterior mass is the A-sector charge and cannot be tuned by smoothing.",
            forbidden_alternative="Boundary smoothing changes measured gravitational mass.",
            status="CONSTRAINED_TARGET",
            missing_derivation="Boundary mass preservation theorem.",
        ),
        ReducedImplication(
            name="R13: Ordinary closed regime",
            sector="active regimes",
            parent_must_imply="Sigma_creation vanishes in ordinary closed gravity.",
            reduced_target="Sigma_creation = 0",
            why_required="Ordinary gravity must remain conservative/closed.",
            forbidden_alternative="Active-regime leakage into ordinary field equations.",
            status="CONSTRAINED_TARGET",
            missing_derivation="Active-regime trigger and exclusion law.",
        ),
        ReducedImplication(
            name="R14: Relaxation energy accounting",
            sector="vacuum relaxation",
            parent_must_imply="Gamma_relax transfers imbalance into vacuum configuration energy, not energy loss.",
            reduced_target="Gamma_relax -> vacuum configuration restoration/accounting",
            why_required="Kappa damping cannot destroy energy.",
            forbidden_alternative="Cosmetic relaxation as dissipation without destination variable.",
            status="STRUCTURAL_TARGET",
            missing_derivation="Vacuum configuration energy variable and balance law.",
        ),
        ReducedImplication(
            name="R15: Recombination without double-counting",
            sector="metric / geometry recombination",
            parent_must_imply="A, W_i, h_TT, and kappa combine without duplicating scalar response.",
            reduced_target="g_tt<-A, g_0i<-W_i, g_ij<-scalar response + constrained kappa + h_TT",
            why_required="Metric recombination is the main place silent GR import can occur.",
            forbidden_alternative="Copying GR metric form before deriving recombination.",
            status="UNRESOLVED",
            missing_derivation="Covariant or reduced parent recombination map.",
        ),
    ]


def print_implication(r: ReducedImplication) -> None:
    print()
    print("-" * 120)
    print(r.name)
    print("-" * 120)
    print(f"Sector: {r.sector}")
    print(f"Parent must imply: {r.parent_must_imply}")
    print(f"Reduced target: {r.reduced_target}")
    print(f"Why required: {r.why_required}")
    print(f"Forbidden alternative: {r.forbidden_alternative}")
    print(f"[INFO] {r.name}: {r.status}")
    print(f"Missing derivation: {r.missing_derivation}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Parent identity reduced implications problem")

    print("Question:")
    print()
    print("  What must any surviving parent identity imply in each reduced sector?")
    print()
    print("Goal:")
    print()
    print("  build a reduced-sector test suite for future parent identity candidates")
    print()
    print("Discipline:")
    print()
    print("  reduced targets are tests, not derivations")
    print("  a parent identity must force the sector ledger, not merely coexist with it")

    with out.unresolved_obligations():
        out.line("reduced implication problem posed", StatusMark.OBLIGATION, "15 reduced sector tests required")


def case_1_implication_inventory(entries: List[ReducedImplication]):
    header("Case 1: Reduced implication inventory")
    for entry in entries:
        print_implication(entry)


def case_2_compact_table(entries: List[ReducedImplication], out: ScriptOutput):
    header("Case 2: Compact reduced implication ledger")

    print("| Implication | Sector | Reduced target | Status | Missing derivation |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.sector.replace("|", "/")
            + " | "
            + e.reduced_target.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing_derivation.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact reduced implication ledger produced", StatusMark.INFO, "15 reduced sector tests recorded")


def case_3_status_counts(entries: List[ReducedImplication], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The parent identity has many clear reduced targets.")
    print("  Most are not derived from a parent identity yet.")
    print("  Scalar constraint propagation and recombination remain especially unresolved.")

    with out.governance_assessments():
        out.line("reduced implication count produced", StatusMark.INFO, str(counts))


def case_4_parent_identity_test_suite(out: ScriptOutput):
    header("Case 4: Parent identity test suite")

    print("A candidate parent identity passes only if it implies:")
    print()
    print("1. Static spherical A constraint.")
    print("2. Exterior Schwarzschild A.")
    print("3. Exterior B=1/A when kappa=0.")
    print("4. Weak scalar Newtonian limit.")
    print("5. Scalar constraint propagation from continuity.")
    print("6. Transverse W_i sourcing.")
    print("7. Angular momentum far-field vector shape.")
    print("8. TT-only ordinary radiation.")
    print("9. Trace exclusion from TT source.")
    print("10. Kappa first-order trace relaxation.")
    print("11. Exterior kappa neutrality.")
    print("12. Boundary mass preservation.")
    print("13. Sigma_creation=0 in ordinary closed gravity.")
    print("14. Relaxation energy accounting.")
    print("15. Recombination without scalar double-counting.")

    with out.unresolved_obligations():
        out.line("parent identity test suite stated", StatusMark.OBLIGATION, "15 tests required before parent identity is licensed")


def case_5_hardest_reduced_implications(out: ScriptOutput):
    header("Case 5: Hardest reduced implications")

    print("Hardest reduced implications:")
    print()
    print("1. Scalar constraint propagation.")
    print("   The parent must show A evolves consistently with continuity without Box A.")
    print()
    print("2. Kappa trace relaxation.")
    print("   The parent must show trace shifts kappa_min without Box kappa.")
    print()
    print("3. Boundary mass preservation.")
    print("   The parent must show kappa/boundary relaxation cannot tune M_ext.")
    print()
    print("4. Tensor/vector coefficient derivation.")
    print("   The parent must eventually fix C_T, K_T, alpha_W/K_c, beta_W.")
    print()
    print("5. Recombination.")
    print("   The parent must map sectors into geometry without copying GR by form.")

    with out.unresolved_obligations():
        out.line("hardest reduced implications identified", StatusMark.OBLIGATION, "5 hardest implications need derivation")


def case_5b_vf_reciprocal_implication_crosscheck(ns, out: ScriptOutput):
    header("Case 5b: VacuumForge reciprocal implication cross-check")

    ctx = TheoryContext("candidate_parent_identity_reduced_implications")
    ms = ctx.define_equal_response_algebraic_symbols()
    A_value = 1 - 2 * ms.G * ms.M / (ms.r * ms.c**2)
    B_value = 1 / A_value
    result = check_concrete_metric(ctx, A_value, B_value, ["reciprocal_scaling"])[0]
    product = sp.simplify(A_value * B_value)

    print(f"A_value = {A_value}")
    print(f"B_value = {B_value}")
    print(f"A_value * B_value = {product}")
    print(f"ConcreteMetricCheck status = {result.status}")

    ok = result.status == "satisfied_by_construction" and product == 1

    with out.derived_results():
        out.line(
            "reduced-implication ledger reproduces reciprocal exterior metric check",
            StatusMark.PASS if ok else StatusMark.FAIL,
            f"A*B = {product}",
        )

    ns.record_derivation(
        derivation_id="parent_identity_reciprocal_implication_crosscheck",
        inputs=[A_value, B_value],
        output=product,
        method="ConcreteMetricCheck reciprocal_scaling",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
    )


def case_6_next_tests(out: ScriptOutput):
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_parent_identity_reduced_implications.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_projector_structure_for_parent_identity.py")
    print("   Work out scalar/vector/TT/trace projectors.")
    print()
    print("3. candidate_scalar_constraint_not_radiation_identity.py")
    print("   Focus on why A constrains rather than radiates.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_projector_structure_for_parent_identity.py")
    print()
    print("Reason:")
    print("  The reduced implications require projectors. Projector structure is the next gate.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "projector structure script is the next gate")


def final_interpretation():
    header("Final interpretation")

    print("Any surviving parent identity must pass a reduced-sector test suite.")
    print()
    print("The clearest tests are:")
    print("  A constraint")
    print("  exterior Schwarzschild")
    print("  B=1/A when kappa=0")
    print("  transverse W_i")
    print("  TT-only radiation")
    print("  kappa relaxation, not Box kappa")
    print("  exterior kappa neutrality")
    print("  boundary mass preservation")
    print("  ordinary Sigma_creation=0")
    print("  recombination without double-counting")
    print()
    print("Possible next artifact:")
    print("  candidate_parent_identity_reduced_implications.md")
    print()
    print("Possible next script:")
    print("  candidate_projector_structure_for_parent_identity.py")


def main():
    header("Candidate Parent Identity Reduced Implications")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_implications()
    case_1_implication_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_parent_identity_test_suite(out)
    case_5_hardest_reduced_implications(out)
    case_5b_vf_reciprocal_implication_crosscheck(ns, out)
    case_6_next_tests(out)
    final_interpretation()

    # Proof obligations for each missing reduced implication
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_scalar_constraint_propagation_reduced",
        script_id=SCRIPT_ID,
        title="Derive continuity-compatible scalar constraint propagation (R5)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that partial_t C_A[A,rho] follows from partial_t rho + div j_L = 0. "
            "This is the most critical missing reduced implication for the parent identity."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_parent_vector_normalization_alpha_W",
        script_id=SCRIPT_ID,
        title="Derive parent current projection and normalization alpha_W/K_c (R6)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that the parent identity projects j onto j_T = P_T j feeding W_i, "
            "and derive the normalization alpha_W/K_c from parent action or stiffness."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tensor_action_stiffness_C_T",
        script_id=SCRIPT_ID,
        title="Derive tensor action stiffness C_T and TT source identity (R8)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that the parent identity gives Box h_ij^TT = -C_T*S_ij^TT "
            "with C_T derived from action/stiffness rather than matched."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_relaxation_parent_K_kappa",
        script_id=SCRIPT_ID,
        title="Derive K_kappa, mu_kappa, chi_kappa, S_trace_effective from parent vacuum minimum (R10)",
        status=ObligationStatus.OPEN,
        description=(
            "The parent identity must show that trace/pressure shifts kappa_min through "
            "S_trace_effective and chi_kappa, with K_kappa from the vacuum minimum structure."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_parent_recombination_map_R15",
        script_id=SCRIPT_ID,
        title="Derive covariant or reduced parent recombination map (R15)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that A, W_i, h_TT, kappa combine into a geometry-like object "
            "without duplicating scalar response. This is the hardest gate for R15."
        ),
    ))

    # Branch decision: parent identity test suite cannot be passed yet
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_parent_identity_test_suite_passage",
        script_id=SCRIPT_ID,
        branch_id="parent_identity_test_suite_passage",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_scalar_constraint_propagation_reduced",
            "derive_parent_vector_normalization_alpha_W",
            "derive_tensor_action_stiffness_C_T",
            "derive_kappa_relaxation_parent_K_kappa",
            "derive_parent_recombination_map_R15",
        ],
        description=(
            "No candidate parent identity can pass the full 15-test reduced-sector suite yet. "
            "The branch is deferred pending projector derivations and constraint propagation."
        ),
    ))

    ns.record_derivation(
        derivation_id="parent_identity_reduced_implications_marker",
        inputs=[],
        output=sp.Symbol("parent_identity_reduced_implications_built"),
        method="parent_identity_reduced_implications_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
