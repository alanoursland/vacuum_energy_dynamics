# Candidate projector structure for parent identity
#
# Group:
#   12_parent_identity_and_recombination
#
# Script type:
#   INVENTORY

# Purpose
# -------
# The reduced-implication test suite showed that any parent identity must imply:
#
#   A scalar constraint,
#   transverse W_i sourcing,
#   TT-only radiation,
#   kappa trace relaxation,
#   exterior kappa neutrality,
#   boundary mass preservation,
#   recombination without scalar double-counting.
#
# These implications require projectors.
#
# This script audits the projector structure needed for a parent identity:
#
#   P_scalar
#   P_L
#   P_T
#   P_TT
#   P_trace
#   P_relax
#   P_boundary
#   P_recombination
#
# It does not derive the projectors covariantly.
# It builds a projector requirement ledger.
# P_L and P_T are verified symbolically in the flat background.

from dataclasses import dataclass
from pathlib import Path
from typing import List

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


@dataclass
class ProjectorEntry:
    name: str
    acts_on: str
    feeds: str
    excludes: str
    schematic_form: str
    status: str
    risk: str
    missing: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="parent_identity_reduced_implications_marker",
        upstream_script_id="12_parent_identity_and_recombination__candidate_parent_identity_reduced_implications",
        upstream_derivation_id="parent_identity_reduced_implications_marker",
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


def build_projectors() -> List[ProjectorEntry]:
    return [
        ProjectorEntry(
            name="P_scalar",
            acts_on="density / scalar source content",
            feeds="A-sector scalar constraint",
            excludes="ordinary scalar radiation A_rad and independent kappa charge",
            schematic_form="P_scalar[T] -> rho_eff -> C_A[A,rho]",
            status="STRUCTURAL",
            risk="Scalar source leaks into A_rad or kappa.",
            missing="Parent definition of scalar charge and areal operator.",
        ),
        ProjectorEntry(
            name="P_L",
            acts_on="matter current j",
            feeds="scalar continuity / density redistribution",
            excludes="transverse W_i source",
            schematic_form="P_L j = grad Delta^{-1} div j",
            status="DERIVED_REDUCED",
            risk="Longitudinal current contaminates frame dragging.",
            missing="Covariant or curved-background generalization.",
        ),
        ProjectorEntry(
            name="P_T",
            acts_on="matter current j",
            feeds="W_i transverse vector response",
            excludes="scalar continuity source",
            schematic_form="P_T = I - k k^T/k^2 in Fourier space",
            status="DERIVED_REDUCED",
            risk="Vector sector receives gauge/longitudinal current.",
            missing="Parent current projection and normalization.",
        ),
        ProjectorEntry(
            name="P_TT",
            acts_on="spatial stress / quadrupole source S_ij",
            feeds="h_ij^TT tensor radiation",
            excludes="trace stress, pressure, scalar/kappa response",
            schematic_form="P_TT S_ij = transverse trace-free projection",
            status="STRUCTURAL",
            risk="Trace contamination of TT radiation.",
            missing="Parent TT source identity and tensor coupling C_T.",
        ),
        ProjectorEntry(
            name="P_trace",
            acts_on="stress trace / pressure / volume imbalance",
            feeds="kappa_min shift",
            excludes="A-sector rho source, h_TT, Box kappa radiation",
            schematic_form="P_trace[T] -> S_trace_effective -> kappa_min",
            status="STRUCTURAL",
            risk="Trace becomes a scalar wave or repair knob.",
            missing="S_trace_effective and chi_kappa.",
        ),
        ProjectorEntry(
            name="P_relax",
            acts_on="kappa - kappa_min imbalance",
            feeds="first-order kappa relaxation / vacuum restoration",
            excludes="second-order kappa momentum channel",
            schematic_form="P_relax: kappa-kappa_min -> dot kappa = -mu K (kappa-kappa_min)",
            status="CONSTRAINED",
            risk="Hidden breathing wave or energy loss.",
            missing="Vacuum configuration energy accounting.",
        ),
        ProjectorEntry(
            name="P_boundary",
            acts_on="boundary / interface relaxation data",
            feeds="local smoothing or kappa boundary condition",
            excludes="change in exterior A mass flux",
            schematic_form="P_boundary enforces delta M_ext = 0 and F_kappa(R+) = 0",
            status="CONSTRAINED",
            risk="Boundary smoothing tunes measured mass.",
            missing="Boundary mass preservation theorem.",
        ),
        ProjectorEntry(
            name="P_closed",
            acts_on="active-regime source balance",
            feeds="ordinary closed gravity sector",
            excludes="Sigma_creation",
            schematic_form="P_closed: Sigma_creation -> 0 in ordinary regime",
            status="CONSTRAINED",
            risk="Active-regime leakage into ordinary gravity.",
            missing="Active-regime trigger/exclusion law.",
        ),
        ProjectorEntry(
            name="P_recombination",
            acts_on="sector fields A, W_i, h_TT, kappa",
            feeds="metric / geometry-like recombination map",
            excludes="scalar double-counting and GR form-copying",
            schematic_form="R[A,W,h_TT,kappa] -> g-like object",
            status="UNRESOLVED",
            risk="Silent GR metric import.",
            missing="Covariant or reduced parent recombination identity.",
        ),
        ProjectorEntry(
            name="P_coeff",
            acts_on="parent action / stiffness constants",
            feeds="alpha_W/K_c, beta_W, C_T, K_T",
            excludes="coefficient matching by hand",
            schematic_form="parent stiffness/coupling projection -> observable coefficients",
            status="MISSING",
            risk="GR coefficients inserted as derivation.",
            missing="Action/stiffness derivation.",
        ),
    ]


def compute_projector_identities(ns, out: ScriptOutput):
    """Verify P_T and P_L idempotence and complementarity in flat Fourier space."""
    header("Symbolic projector verification: P_T and P_L")

    # 3D flat Fourier space projectors
    # P_T_ij = delta_ij - k_i k_j / k^2
    # P_L_ij = k_i k_j / k^2
    # Verify: P_T^2 = P_T, P_L^2 = P_L, P_T + P_L = I (trace: 3, 1, 3 for 3D space ... wait, trace)
    # Work in 2D symbolic block for conciseness: use k = (k1, k2) in 2D

    k1, k2 = sp.symbols("k1 k2", real=True)
    k_sq = k1**2 + k2**2

    # Build 2D projectors
    I2 = sp.eye(2)
    k_vec = sp.Matrix([k1, k2])
    P_L_mat = k_vec * k_vec.T / k_sq
    P_T_mat = I2 - P_L_mat

    # Verify idempotence
    P_T_sq_residual = sp.simplify(P_T_mat * P_T_mat - P_T_mat)
    P_L_sq_residual = sp.simplify(P_L_mat * P_L_mat - P_L_mat)
    # Verify complementarity
    complement_residual = sp.simplify(P_T_mat + P_L_mat - I2)
    # Verify orthogonality
    cross_residual = sp.simplify(P_T_mat * P_L_mat)

    print(f"P_T^2 - P_T residual: {P_T_sq_residual}")
    print(f"P_L^2 - P_L residual: {P_L_sq_residual}")
    print(f"P_T + P_L - I residual: {complement_residual}")
    print(f"P_T * P_L residual: {cross_residual}")

    all_zero = (
        P_T_sq_residual == sp.zeros(2, 2)
        and P_L_sq_residual == sp.zeros(2, 2)
        and complement_residual == sp.zeros(2, 2)
        and cross_residual == sp.zeros(2, 2)
    )

    with out.derived_results():
        out.line("P_T idempotence residual", StatusMark.PASS if P_T_sq_residual == sp.zeros(2, 2) else StatusMark.FAIL,
                 f"{P_T_sq_residual}")
        out.line("P_L idempotence residual", StatusMark.PASS if P_L_sq_residual == sp.zeros(2, 2) else StatusMark.FAIL,
                 f"{P_L_sq_residual}")
        out.line("P_T + P_L = I residual", StatusMark.PASS if complement_residual == sp.zeros(2, 2) else StatusMark.FAIL,
                 f"{complement_residual}")
        out.line("P_T * P_L orthogonality residual", StatusMark.PASS if cross_residual == sp.zeros(2, 2) else StatusMark.FAIL,
                 f"{cross_residual}")

    ns.record_derivation(
        derivation_id="transverse_projector_P_T_idempotence_residual",
        inputs=[P_T_mat],
        output=P_T_sq_residual,
        method="simplify(P_T*P_T - P_T) in flat 2D Fourier space",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )
    ns.record_derivation(
        derivation_id="longitudinal_projector_P_L_idempotence_residual",
        inputs=[P_L_mat],
        output=P_L_sq_residual,
        method="simplify(P_L*P_L - P_L) in flat 2D Fourier space",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )
    ns.record_derivation(
        derivation_id="projector_complementarity_residual",
        inputs=[P_T_mat, P_L_mat],
        output=complement_residual,
        method="simplify(P_T + P_L - I) in flat 2D Fourier space",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )
    ns.record_derivation(
        derivation_id="projector_orthogonality_residual",
        inputs=[P_T_mat, P_L_mat],
        output=cross_residual,
        method="simplify(P_T * P_L) in flat 2D Fourier space",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )

    return all_zero


def print_projector(p: ProjectorEntry) -> None:
    print()
    print("-" * 120)
    print(p.name)
    print("-" * 120)
    print(f"Acts on: {p.acts_on}")
    print(f"Feeds: {p.feeds}")
    print(f"Excludes: {p.excludes}")
    print(f"Schematic form: {p.schematic_form}")
    print(f"[INFO] {p.name}: {p.status}")
    print(f"Risk: {p.risk}")
    print(f"Missing: {p.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Projector structure problem")

    print("Question:")
    print()
    print("  What projector structure is required for a parent identity?")
    print()
    print("Goal:")
    print()
    print("  make source/sector routing explicit before trying a parent identity")
    print()
    print("Discipline:")
    print()
    print("  projectors are not derivations")
    print("  projectors must prevent forbidden overlaps")
    print("  recombination must come after source splitting")

    with out.governance_assessments():
        out.line("projector structure problem posed", StatusMark.DEFER, "projector inventory in progress")


def case_1_projector_inventory(entries: List[ProjectorEntry]):
    header("Case 1: Projector inventory")
    for entry in entries:
        print_projector(entry)


def case_2_compact_table(entries: List[ProjectorEntry], out: ScriptOutput):
    header("Case 2: Compact projector ledger")

    print("| Projector | Feeds | Excludes | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.feeds.replace("|", "/")
            + " | "
            + e.excludes.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact projector ledger produced", StatusMark.INFO, "10 projectors audited")


def case_3_status_counts(entries: List[ProjectorEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Reduced current projectors P_L and P_T are the clearest.")
    print("  Scalar, TT, trace, and relaxation projectors are structural.")
    print("  Recombination and coefficient projectors remain unresolved/missing.")

    with out.governance_assessments():
        out.line("projector status count produced", StatusMark.INFO, str(counts))


def case_4_required_decomposition(out: ScriptOutput):
    header("Case 4: Required source decomposition")

    print("Parent source decomposition must route:")
    print()
    print("  rho / scalar charge -> P_scalar -> A")
    print("  longitudinal current -> P_L -> scalar continuity")
    print("  transverse current -> P_T -> W_i")
    print("  TT stress -> P_TT -> h_ij^TT")
    print("  trace / pressure -> P_trace -> kappa_min")
    print("  kappa imbalance -> P_relax -> first-order relaxation")
    print("  boundary data -> P_boundary -> M_ext preservation and kappa exterior safety")
    print("  active-regime terms -> P_closed -> Sigma_creation=0 in ordinary regime")
    print("  sector fields -> P_recombination -> geometry without double-counting")

    with out.governance_assessments():
        out.line("required source decomposition stated", StatusMark.DEFER, "decomposition is a requirement, not yet derived")


def case_5_projector_consistency_tests(out: ScriptOutput):
    header("Case 5: Projector consistency tests")

    print("Projector tests:")
    print()
    print("1. P_scalar rho must not feed A_rad.")
    print("2. P_scalar rho must not feed long-range kappa.")
    print("3. P_T j must be divergence-free/transverse.")
    print("4. P_L j must not feed curl W.")
    print("5. P_TT S must be trace-free.")
    print("6. P_trace T must not feed h_TT.")
    print("7. P_trace T must not create Box kappa.")
    print("8. P_boundary must preserve M_ext.")
    print("9. P_closed must set Sigma_creation=0 in ordinary gravity.")
    print("10. P_recombination must count scalar response exactly once.")

    with out.unresolved_obligations():
        out.line("projector consistency tests stated", StatusMark.OBLIGATION, "10 consistency tests required")


def case_6_hardest_projectors(out: ScriptOutput):
    header("Case 6: Hardest projectors")

    print("Hardest projectors:")
    print()
    print("1. P_scalar:")
    print("   must explain A as constraint rather than scalar radiation.")
    print()
    print("2. P_trace / P_relax:")
    print("   must explain kappa relaxation rather than Box kappa.")
    print()
    print("3. P_boundary:")
    print("   must preserve exterior mass under boundary smoothing.")
    print()
    print("4. P_recombination:")
    print("   must produce geometry without silent GR import.")
    print()
    print("5. P_coeff:")
    print("   must derive vector/tensor coefficients rather than matching them.")

    with out.unresolved_obligations():
        out.line("hardest projectors identified", StatusMark.OBLIGATION, "5 hardest projectors need derivation")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_projector_structure_for_parent_identity.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_scalar_constraint_not_radiation_identity.py")
    print("   Focus on why A constrains rather than radiates.")
    print()
    print("3. candidate_kappa_covariant_relaxation_requirement.py")
    print("   Focus on kappa's first-order relaxation and frame/covariance issue.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_scalar_constraint_not_radiation_identity.py")
    print()
    print("Reason:")
    print("  P_scalar is the hardest immediate gate: the parent must explain scalar constraint, not scalar radiation.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "scalar constraint script is the next gate")


def final_interpretation():
    header("Final interpretation")

    print("The parent identity needs projectors before it can be meaningful.")
    print()
    print("Current clearest projectors:")
    print("  P_L")
    print("  P_T")
    print()
    print("Current structural projectors:")
    print("  P_scalar")
    print("  P_TT")
    print("  P_trace")
    print("  P_relax")
    print("  P_boundary")
    print()
    print("Current unresolved/missing projectors:")
    print("  P_recombination")
    print("  P_coeff")
    print()
    print("Possible next artifact:")
    print("  candidate_projector_structure_for_parent_identity.md")
    print()
    print("Possible next script:")
    print("  candidate_scalar_constraint_not_radiation_identity.py")


def main():
    header("Candidate Projector Structure for Parent Identity")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_projectors()
    case_1_projector_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)

    all_projector_identities_pass = compute_projector_identities(ns, out)

    case_4_required_decomposition(out)
    case_5_projector_consistency_tests(out)
    case_6_hardest_projectors(out)
    case_7_next_tests(out)
    final_interpretation()

    # Proof obligations for unresolved/missing projectors
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_scalar_parent_definition",
        script_id=SCRIPT_ID,
        title="Define P_scalar from parent identity to route rho to A",
        status=ObligationStatus.OPEN,
        description=(
            "Show that the parent identity contains a scalar projector P_scalar "
            "routing rho_eff to the A-sector constraint C_A[A,rho]=0, "
            "excluding A_rad and long-range kappa."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_TT_parent_source_identity",
        script_id=SCRIPT_ID,
        title="Derive parent TT source identity and tensor coupling C_T",
        status=ObligationStatus.OPEN,
        description=(
            "Show that the parent identity contains P_TT projecting S_ij to S_ij^TT "
            "feeding h_ij^TT, and derive tensor coupling C_T from action/stiffness."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_recombination_parent_identity",
        script_id=SCRIPT_ID,
        title="Derive P_recombination: covariant or reduced parent recombination identity",
        status=ObligationStatus.OPEN,
        description=(
            "Show that sector fields A, W_i, h_TT, kappa recombine into a geometry-like object "
            "without scalar double-counting or silent GR import."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_coeff_action_stiffness",
        script_id=SCRIPT_ID,
        title="Derive P_coeff from parent action/stiffness principle",
        status=ObligationStatus.OPEN,
        description=(
            "Show that alpha_W/K_c, beta_W, C_T, K_T follow from a parent action or "
            "stiffness principle rather than being matched to GR."
        ),
    ))

    # Policy claim: P_L and P_T are structurally sound in flat Fourier space
    ns.record_claim(ClaimRecord(
        claim_id="P_L_P_T_flat_projector_identities_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "P_L = k k^T / k^2 and P_T = I - k k^T / k^2 satisfy idempotence, "
            "complementarity, and orthogonality in flat 2D Fourier space. "
            "Curved-background generalization remains an open obligation."
        ),
        derivation_ids=[
            "transverse_projector_P_T_idempotence_residual",
            "longitudinal_projector_P_L_idempotence_residual",
            "projector_complementarity_residual",
            "projector_orthogonality_residual",
        ],
    ))

    # Branch decision: full parent identity projector structure deferred
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_parent_projector_structure_derivation",
        script_id=SCRIPT_ID,
        branch_id="parent_projector_structure_derivation",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_P_scalar_parent_definition",
            "derive_P_TT_parent_source_identity",
            "derive_P_recombination_parent_identity",
            "derive_P_coeff_action_stiffness",
        ],
        description=(
            "The full projector structure for the parent identity cannot be derived until "
            "scalar projector, TT projector, recombination projector, and coefficient projector "
            "derivations are available."
        ),
    ))

    ns.record_derivation(
        derivation_id="projector_structure_for_parent_identity_marker",
        inputs=[],
        output=sp.Symbol("projector_structure_for_parent_identity_built"),
        method="projector_structure_for_parent_identity_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
