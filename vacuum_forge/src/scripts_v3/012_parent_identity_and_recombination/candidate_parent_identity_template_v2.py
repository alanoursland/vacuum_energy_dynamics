# Candidate parent identity template v2
#
# Group:
#   12_parent_identity_and_recombination
#
# Script type:
#   REQUIREMENTS

# Purpose
# -------
# Group 12 has now built several constraints around the parent identity:
#
#   false parent identities excluded,
#   reduced implications listed,
#   projectors required,
#   scalar radiation excluded,
#   kappa relaxation frame/covariance audited,
#   boundary mass preservation required,
#   recombination constrained,
#   relaxation energy accounting tied to vacuum-substance exchange.
#
# This script attempts a tighter parent identity scaffold.
#
# It is still not a derivation.
#
# It is a second scaffold that must include:
#
#   sector projectors,
#   ordinary closed-regime accounting,
#   first-order kappa relaxation,
#   relaxation exchange with vacuum substance,
#   exterior mass preservation,
#   recombination no-double-counting.
#
# Canonical next artifact:
#   candidate_parent_identity_template_v2.md

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
class ParentClause:
    name: str
    clause: str
    required_reduction: str
    forbidden_failure: str
    status: str
    missing: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="relaxation_energy_accounting_identity_marker",
        upstream_script_id="12_parent_identity_and_recombination__candidate_relaxation_energy_accounting_identity",
        upstream_derivation_id="relaxation_energy_accounting_identity_marker",
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


def build_clauses() -> List[ParentClause]:
    return [
        ParentClause(
            name="P2.1: parent balance object",
            clause="Div E_parent[A,W,h_TT,kappa; projectors] = B_closed[T] + B_relax[Gamma_relax]",
            required_reduction="A single balance scaffold that routes sources through projectors.",
            forbidden_failure="Decorative Bianchi restatement with no sector reductions.",
            status="CANDIDATE",
            missing="Definition of E_parent, Div, B_closed, B_relax.",
        ),
        ParentClause(
            name="P2.2: ordinary closed regime",
            clause="Sigma_creation = 0 and B_active = 0 in ordinary gravity",
            required_reduction="No active creation term enters ordinary field equations.",
            forbidden_failure="Gamma_relax or Sigma_creation acts as net creation/destruction.",
            status="CONSTRAINED",
            missing="Active-regime trigger/exclusion law.",
        ),
        ParentClause(
            name="P2.3: scalar projector",
            clause="P_scalar B_closed[T] -> rho_eff -> C_A[A,rho]=0",
            required_reduction="Delta_areal A = 8*pi*G*rho/c^2 and weak Newtonian limit.",
            forbidden_failure="Box A or A_rad ordinary scalar radiation.",
            status="STRUCTURAL",
            missing="Parent definition of P_scalar and C_A.",
        ),
        ParentClause(
            name="P2.4: scalar constraint propagation",
            clause="partial_tau C_A[A,rho] follows from continuity(rho,j_L)",
            required_reduction="Moving sources update A without scalar radiation.",
            forbidden_failure="Adding Box A by hand for dynamics.",
            status="MISSING",
            missing="Continuity-compatible scalar constraint propagation identity.",
        ),
        ParentClause(
            name="P2.5: vector projector",
            clause="P_T B_closed[T] -> j_T -> curl curl W = -(alpha_W/(2K_c))*j_T",
            required_reduction="W_i sourced only by transverse current.",
            forbidden_failure="P_L j or scalar continuity sources W_i.",
            status="STRUCTURAL",
            missing="Parent projection and alpha_W/K_c normalization.",
        ),
        ParentClause(
            name="P2.6: TT projector",
            clause="P_TT B_closed[T] -> S_ij^TT -> Box h_ij^TT = -C_T S_ij^TT",
            required_reduction="Ordinary long-range radiation is TT-only.",
            forbidden_failure="Trace stress, A_rad, Box kappa, or free W_i radiation.",
            status="STRUCTURAL",
            missing="C_T, tensor action stiffness, TT source identity.",
        ),
        ParentClause(
            name="P2.7: trace / kappa minimum projector",
            clause="P_trace B_closed[T] -> S_trace_effective -> kappa_min",
            required_reduction="Trace/pressure shifts kappa_min, not scalar radiation.",
            forbidden_failure="Box kappa = alpha trace.",
            status="STRUCTURAL",
            missing="S_trace_effective and chi_kappa.",
        ),
        ParentClause(
            name="P2.8: first-order kappa relaxation",
            clause="u^mu nabla_mu kappa = -lambda_kappa (kappa-kappa_min)",
            required_reduction="Kappa relaxes without momentum channel or breathing wave.",
            forbidden_failure="Second-order kappa oscillator/sloshing.",
            status="CANDIDATE",
            missing="Definition of u^mu and lambda_kappa.",
        ),
        ParentClause(
            name="P2.9: relaxation/vacuum-substance exchange",
            clause="dE_kappa/dtau + dE_vac_config/dtau = 0 for internal relaxation",
            required_reduction="Curvature excess/deficit exchanges with vacuum substance instead of disappearing.",
            forbidden_failure="Gamma_relax destroys energy or acts like Sigma_creation.",
            status="CANDIDATE",
            missing="Definition of E_vac_config or q_v/J_v balance.",
        ),
        ParentClause(
            name="P2.10: exterior kappa neutrality",
            clause="Q_kappa = 0, F_kappa(R+) = 0, kappa_ext -> 0",
            required_reduction="No exterior kappa 1/r tail.",
            forbidden_failure="Second exterior scalar charge.",
            status="CONSTRAINED",
            missing="Projection/boundary cancellation identity.",
        ),
        ParentClause(
            name="P2.11: boundary mass preservation",
            clause="delta M_ext|kappa_relaxation = 0 and delta M_ext|Gamma_relax = 0",
            required_reduction="Kappa/boundary relaxation cannot change A-sector exterior mass.",
            forbidden_failure="Boundary smoothing tunes measured mass.",
            status="REQUIRED",
            missing="Boundary mass preservation theorem.",
        ),
        ParentClause(
            name="P2.12: recombination without double-counting",
            clause="R[A,W,h_TT,kappa] counts scalar response once",
            required_reduction="g_tt<-A, g_0i<-W_i, g_ij<-scalar(A)+kappa_trace+h_TT",
            forbidden_failure="Metric copied from GR or A/kappa duplicate rho response.",
            status="CANDIDATE",
            missing="P_recombination identity.",
        ),
        ParentClause(
            name="P2.13: coefficient derivation gate",
            clause="P_coeff(action/stiffness) -> alpha_W/K_c, beta_W, C_T, K_T",
            required_reduction="Coefficients remain labeled until parent action/stiffness derives them.",
            forbidden_failure="GR coefficients inserted as derivation.",
            status="MISSING",
            missing="Parent action/stiffness principle.",
        ),
    ]


def print_clause(c: ParentClause) -> None:
    print()
    print("-" * 120)
    print(c.name)
    print("-" * 120)
    print(f"Clause: {c.clause}")
    print(f"Required reduction: {c.required_reduction}")
    print(f"Forbidden failure: {c.forbidden_failure}")
    print(f"[INFO] {c.name}: {c.status}")
    print(f"Missing: {c.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Parent identity template v2 problem")

    print("Question:")
    print()
    print("  Can group-12 constraints tighten the parent identity scaffold?")
    print()
    print("Goal:")
    print()
    print("  write a second parent scaffold that includes exclusions, projectors, recombination,")
    print("  and relaxation energy exchange with vacuum substance")
    print()
    print("Discipline:")
    print()
    print("  still not a derivation")
    print("  no decorative Bianchi restatement")
    print("  no scalar radiation")
    print("  no energy destruction")
    print("  no metric copying as derivation")

    with out.governance_assessments():
        out.line("parent template v2 problem posed", StatusMark.DEFER, "scaffold only; not a derivation")


def case_1_clause_inventory(entries: List[ParentClause]):
    header("Case 1: Parent v2 clause inventory")
    for entry in entries:
        print_clause(entry)


def case_2_compact_table(entries: List[ParentClause], out: ScriptOutput):
    header("Case 2: Compact parent v2 ledger")

    print("| Clause | Required reduction | Status | Missing |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.required_reduction.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact parent v2 ledger produced", StatusMark.INFO, "13 parent v2 clauses recorded")


def case_3_status_counts(entries: List[ParentClause], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Template v2 is tighter than the first parent scaffold.")
    print("  It includes projectors, kappa relaxation, boundary mass preservation,")
    print("  recombination, and relaxation energy exchange.")
    print("  It is still not closure.")

    with out.governance_assessments():
        out.line("parent v2 status count produced", StatusMark.INFO, str(counts))


def case_4_candidate_symbolic_parent(out: ScriptOutput):
    header("Case 4: Candidate symbolic parent v2")

    print("Candidate scaffold:")
    print()
    print("  Div E_parent[A,W,h_TT,kappa; P_scalar,P_T,P_TT,P_trace,P_boundary]")
    print("    = B_closed[T]")
    print("    + B_relax[Gamma_relax, E_vac_config]")
    print()
    print("Ordinary closed regime:")
    print()
    print("  Sigma_creation = 0")
    print()
    print("Projector reductions:")
    print()
    print("  P_scalar -> A constraint")
    print("  P_T -> W_i")
    print("  P_TT -> h_TT")
    print("  P_trace -> kappa_min")
    print("  P_boundary -> delta M_ext = 0")
    print("  P_recombination -> scalar counted once")
    print()
    print("Relaxation exchange:")
    print()
    print("  dE_kappa/dtau + dE_vac_config/dtau = 0")
    print()
    print("This is still a scaffold.")

    with out.governance_assessments():
        out.line("candidate symbolic parent v2 stated", StatusMark.DEFER, "scaffold only; E_parent undefined")


def case_5_pass_fail_tests(out: ScriptOutput):
    header("Case 5: Parent v2 pass/fail tests")

    print("Template v2 fails if:")
    print()
    print("1. E_parent is not defined.")
    print("2. P_scalar does not derive A constraint.")
    print("3. Scalar constraint propagation remains impossible.")
    print("4. Box A, A_rad, or Box kappa appears.")
    print("5. rho sources long-range kappa.")
    print("6. trace contaminates h_TT.")
    print("7. P_L j sources W_i.")
    print("8. Gamma_relax has no energy destination.")
    print("9. boundary relaxation changes M_ext.")
    print("10. recombination counts scalar response twice.")
    print("11. coefficients are copied from GR.")

    with out.unresolved_obligations():
        out.line("parent v2 pass/fail tests stated", StatusMark.OBLIGATION, "11 tests required before v2 scaffold is licensed")


def case_6_next_tests(out: ScriptOutput):
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_parent_identity_template_v2.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_vacuum_configuration_energy_variable.py")
    print("   Try to define E_vac_config or q_v/J_v accounting.")
    print()
    print("3. parent_identity_and_recombination_summary.md")
    print("   Summarize group 12 so far.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vacuum_configuration_energy_variable.py")
    print()
    print("Reason:")
    print("  Template v2 now depends explicitly on E_vac_config; the vacuum-substance variable must be examined.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "vacuum configuration energy variable script is the next gate")


def final_interpretation():
    header("Final interpretation")

    print("Parent identity template v2 is more constrained than v1.")
    print()
    print("It now requires:")
    print("  sector projectors")
    print("  scalar constraint propagation")
    print("  TT-only radiation")
    print("  first-order kappa relaxation")
    print("  vacuum-substance exchange")
    print("  boundary mass preservation")
    print("  recombination without double-counting")
    print("  coefficient derivation gate")
    print()
    print("It is still not closure.")
    print()
    print("Possible next artifact:")
    print("  candidate_parent_identity_template_v2.md")
    print()
    print("Possible next script:")
    print("  candidate_vacuum_configuration_energy_variable.py")


def main():
    header("Candidate Parent Identity Template V2")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_clauses()
    case_1_clause_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_candidate_symbolic_parent(out)
    case_5_pass_fail_tests(out)
    case_6_next_tests(out)
    final_interpretation()

    # Proof obligations: each missing clause becomes a proof obligation
    # Template v2 requirements as obligations
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_E_parent_definition_and_sector_projections_P2_1",
        script_id=SCRIPT_ID,
        title="Define E_parent and derive its sector projector reductions (P2.1)",
        status=ObligationStatus.OPEN,
        description=(
            "Div E_parent must be defined and its reduced projections must force the known sectors: "
            "A constraint (P_scalar), W_i (P_T), h_TT (P_TT), kappa_min (P_trace). "
            "A decorative Bianchi restatement is forbidden."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_scalar_constraint_propagation_P2_4",
        script_id=SCRIPT_ID,
        title="Derive continuity-compatible scalar constraint propagation (P2.4)",
        status=ObligationStatus.OPEN,
        description=(
            "partial_tau C_A[A,rho] must follow from continuity(rho,j_L) without Box A. "
            "This is the hardest and most critical missing clause in template v2."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_alpha_W_K_c_parent_normalization_P2_5",
        script_id=SCRIPT_ID,
        title="Derive parent projection and alpha_W/K_c normalization (P2.5)",
        status=ObligationStatus.OPEN,
        description=(
            "The vector projector P_T must feed curl curl W = -(alpha_W/(2K_c))*j_T. "
            "alpha_W/K_c must be derived from parent action/stiffness, not matched."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tensor_stiffness_C_T_TT_source_P2_6",
        script_id=SCRIPT_ID,
        title="Derive tensor action stiffness C_T and TT source identity (P2.6)",
        status=ObligationStatus.OPEN,
        description=(
            "P_TT must project to S_ij^TT feeding Box h_ij^TT = -C_T*S_ij^TT. "
            "C_T must be derived from action/stiffness."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_u_mu_lambda_kappa_frame_P2_8",
        script_id=SCRIPT_ID,
        title="Define u^mu and derive lambda_kappa for kappa relaxation (P2.8)",
        status=ObligationStatus.OPEN,
        description=(
            "The frame field u^mu and lambda_kappa = mu_kappa*K_kappa must be defined "
            "to license the first-order kappa relaxation u^mu nabla_mu kappa = -lambda_kappa*(kappa-kappa_min)."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_E_vac_config_relaxation_exchange_P2_9",
        script_id=SCRIPT_ID,
        title="Define E_vac_config and derive relaxation/vacuum-substance exchange (P2.9)",
        status=ObligationStatus.OPEN,
        description=(
            "dE_kappa/dtau + dE_vac_config/dtau = 0 for internal relaxation must be derived. "
            "E_vac_config or q_v/J_v balance must be defined."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_recombination_scalar_once_P2_12",
        script_id=SCRIPT_ID,
        title="Derive P_recombination counting scalar response once (P2.12)",
        status=ObligationStatus.OPEN,
        description=(
            "R[A,W,h_TT,kappa] must count scalar response once. "
            "P_recombination identity must be derived, not copied from GR."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_coeff_action_stiffness_principle_P2_13",
        script_id=SCRIPT_ID,
        title="Derive P_coeff / action stiffness principle for observable coefficients (P2.13)",
        status=ObligationStatus.OPEN,
        description=(
            "alpha_W/K_c, beta_W, C_T, K_T must be derived from a parent action or "
            "stiffness principle. GR coefficient insertion is forbidden."
        ),
    ))

    # Policy claim: template v2 is a scaffold, not closure
    ns.record_claim(ClaimRecord(
        claim_id="parent_identity_template_v2_is_scaffold_not_closure",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Parent identity template v2 is a requirements scaffold, not a closure theorem. "
            "It defines the structure and gates that a positive parent identity must satisfy, "
            "but it does not constitute a derived parent identity. "
            "No reduced-sector implication can be claimed as derived from template v2 alone."
        ),
    ))

    # Branch decision: positive parent identity v2 derivation deferred
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_parent_identity_v2_positive_derivation",
        script_id=SCRIPT_ID,
        branch_id="parent_identity_v2_positive_derivation",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_E_parent_definition_and_sector_projections_P2_1",
            "derive_scalar_constraint_propagation_P2_4",
            "derive_alpha_W_K_c_parent_normalization_P2_5",
            "derive_tensor_stiffness_C_T_TT_source_P2_6",
            "derive_u_mu_lambda_kappa_frame_P2_8",
            "derive_E_vac_config_relaxation_exchange_P2_9",
            "derive_P_recombination_scalar_once_P2_12",
            "derive_P_coeff_action_stiffness_principle_P2_13",
        ],
        description=(
            "No positive parent identity v2 can be derived until all 8 core obligations are satisfied. "
            "Template v2 is a scaffold; the branch to a positive parent identity is deferred pending "
            "projector derivations, scalar constraint propagation, and E_vac_config definition."
        ),
    ))

    ns.record_derivation(
        derivation_id="parent_identity_template_v2_marker",
        inputs=[],
        output=sp.Symbol("parent_identity_template_v2_built"),
        method="parent_identity_template_v2_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
