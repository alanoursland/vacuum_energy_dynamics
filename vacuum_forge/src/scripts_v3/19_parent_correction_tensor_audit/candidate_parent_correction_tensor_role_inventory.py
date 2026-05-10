# Candidate parent correction tensor role inventory
#
# Group:
#   19_parent_correction_tensor_audit
#
# Script type:
#   INVENTORY
#
# Purpose
# -------
# Group 19 starts from the deferred parent-correction tensor bottleneck:
#
#   H_curv remains deferred.
#   H_exch remains deferred.
#
# Prior groups found:
#
#   A_curv is diagnostic / branch-filter theorem target, not dynamics.
#   e_curv is diagnostic/accounting only, not source.
#   J_curv is not defined.
#   Curvature balance is theorem target only, not law.
#
#   J_V is unresolved.
#   J_sub/J_exch split is role-level only.
#   J_sub is pure-wind theorem target only.
#   J_exch is active-exchange theorem target only.
#   Sigma/R are role-level only.
#   No active ordinary-sector source side for J_exch is derived.
#   No dark-sector coupling is required.
#
# This script inventories possible correction-tensor roles before any tensor
# form is proposed.
#
# Locked-door question:
#
#   What roles are being hidden inside H_curv and H_exch?
#
# This is a role inventory, not a parent field equation.


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


@dataclass
class CorrectionTensorRoleEntry:
    name: str
    role_candidate: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="vacuum_current_split_group_status_summary_marker",
        upstream_script_id="18_vacuum_current_split__candidate_vacuum_current_split_group_status_summary",
        upstream_derivation_id="vacuum_current_split_group_status_summary_marker",
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


def build_entries() -> List[CorrectionTensorRoleEntry]:
    return [
        CorrectionTensorRoleEntry(
            name="CT1: parent correction tensor audit target",
            role_candidate="H_curv and H_exch are possible correction tensors only if source, divergence, boundary, and bookkeeping are explicit",
            role="core Group 19 target",
            allowed_if="correction tensor language remains requirements-level until objects are defined",
            forbidden_if="H_curv/H_exch are inserted to make parent equation close",
            status="THEOREM_TARGET",
            missing="actual correction tensor definitions",
            consequence="decides whether correction-tensor language can become technical",
        ),
        CorrectionTensorRoleEntry(
            name="CT2: H_curv role",
            role_candidate="H_curv as curvature / finite-admissibility correction tensor candidate",
            role="curvature correction theorem target",
            allowed_if="A_curv/J_curv/source structure is real and ordinary-sector neutrality holds",
            forbidden_if="H_curv is anti-singularity patch, e_curv reservoir, or regular-core tuning",
            status="THEOREM_TARGET",
            missing="A_curv dynamics, J_curv, source side, divergence behavior",
            consequence="keeps curvature correction from hardening before curvature objects are real",
        ),
        CorrectionTensorRoleEntry(
            name="CT3: H_exch role",
            role_candidate="H_exch as vacuum exchange / current / source-relaxation correction tensor candidate",
            role="exchange correction theorem target",
            allowed_if="J_V/J_exch and Sigma/R operators are real and matter decoupling holds",
            forbidden_if="H_exch is exchange-continuity paint or Sigma/R tuning tensor",
            status="THEOREM_TARGET",
            missing="J_V/J_exch, Sigma/R, source side, divergence behavior",
            consequence="keeps exchange correction from patching missing current/source law",
        ),
        CorrectionTensorRoleEntry(
            name="CT4: H_metric_insert role",
            role_candidate="H_metric_insert as B_s/F_zeta insertion or no-overlap correction candidate",
            role="metric insertion correction candidate",
            allowed_if="B_s/F_zeta and O no-overlap are derived",
            forbidden_if="tensor restores residual scalar trace or copies GR spatial metric",
            status="RISK",
            missing="B_s/F_zeta insertion law and O no-overlap operator",
            consequence="dangerous because it may reopen Group 16 bottlenecks",
        ),
        CorrectionTensorRoleEntry(
            name="CT5: H_residual role",
            role_candidate="H_residual as residual-kill / non-metric residual correction candidate",
            role="residual bookkeeping candidate",
            allowed_if="residual role is non-metric or no-overlap operator is real",
            forbidden_if="H_residual restores killed zeta/kappa metric trace",
            status="RISK",
            missing="residual-kill derivation or O",
            consequence="dangerous because residual can become hidden scalar metric trace",
        ),
        CorrectionTensorRoleEntry(
            name="CT6: H_dark role",
            role_candidate="H_dark as dark-sector correction candidate",
            role="optional deferred branch",
            allowed_if="dark source separation is derived and ordinary sector remains neutral",
            forbidden_if="dark correction patches ordinary current/source failure",
            status="DEFER",
            missing="dark-sector source/coupling theorem",
            consequence="preserves no-dark-patch result from Group 18",
        ),
        CorrectionTensorRoleEntry(
            name="CT7: diagnostic tensor audit role",
            role_candidate="H-like object used only as diagnostic audit, not inserted into field equation",
            role="safe fallback",
            allowed_if="explicitly marked diagnostic-only",
            forbidden_if="diagnostic tensor becomes parent equation term",
            status="SAFE_IF",
            missing="none if kept diagnostic",
            consequence="allows audits without premature field-equation insertion",
        ),
        CorrectionTensorRoleEntry(
            name="CT8: identically divergence-free candidate",
            role_candidate="correction tensor whose divergence vanishes by mathematical identity",
            role="possible divergence-safe tensor class",
            allowed_if="identity is real and tensor source origin is not repair",
            forbidden_if="divergence-free is asserted by Bianchi-like language",
            status="CANDIDATE",
            missing="actual tensor identity",
            consequence="possible safe class if constructed, not named",
        ),
        CorrectionTensorRoleEntry(
            name="CT9: source-balanced divergence candidate",
            role_candidate="correction tensor divergence balances an independently defined source side",
            role="possible source-balance tensor class",
            allowed_if="source side exists before tensor is introduced",
            forbidden_if="source and tensor define each other decoratively",
            status="CANDIDATE",
            missing="source side and divergence relation",
            consequence="possible class if source partner is real",
        ),
        CorrectionTensorRoleEntry(
            name="CT10: projected correction candidate",
            role_candidate="correction tensor lives in a defined projector subspace",
            role="possible projection-safe tensor class",
            allowed_if="projector and target sector are independently defined",
            forbidden_if="projection is invented to hide overlap or leakage",
            status="CANDIDATE",
            missing="projector and sector split",
            consequence="possible route to no-double-counting if projectors are real",
        ),
        CorrectionTensorRoleEntry(
            name="CT11: constraint-preserving candidate",
            role_candidate="correction tensor preserves scalar/vector/tensor constraints",
            role="possible consistency tensor class",
            allowed_if="constraint propagation is derived and not recovery-tuned",
            forbidden_if="constraint preservation is asserted without propagation identity",
            status="CANDIDATE",
            missing="constraint propagation identity",
            consequence="possible route to parent compatibility if proven",
        ),
        CorrectionTensorRoleEntry(
            name="CT12: boundary-supported candidate",
            role_candidate="correction tensor supported near boundary/interface",
            role="high-risk boundary tensor class",
            allowed_if="support is structural and boundary-neutral",
            forbidden_if="tensor repairs boundary leakage, shell source, scalar tail, or M_ext shift",
            status="RISK",
            missing="support law and boundary neutrality theorem",
            consequence="dangerous because boundary repair is a recurring failure mode",
        ),
        CorrectionTensorRoleEntry(
            name="CT13: ordinary matter separation requirement",
            role_candidate="correction tensor does not reroute ordinary T_mu_nu or double-count matter",
            role="source separation guard",
            allowed_if="ordinary matter stays in established source routing",
            forbidden_if="H_curv/H_exch hides ordinary matter in correction side",
            status="REQUIRED",
            missing="source separation theorem",
            consequence="protects A-sector and ordinary matter coupling",
        ),
        CorrectionTensorRoleEntry(
            name="CT14: exterior mass neutrality requirement",
            role_candidate="correction tensor does not shift M_ext independently of A-sector",
            role="mass neutrality guard",
            allowed_if="mass effect is derived through established source law",
            forbidden_if="H_curv/H_exch changes measured exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        CorrectionTensorRoleEntry(
            name="CT15: scalar trace neutrality requirement",
            role_candidate="correction tensor does not leak B_s/zeta/kappa scalar charge",
            role="metric scalar guard",
            allowed_if="scalar trace routing and no-overlap remain closed",
            forbidden_if="H restores killed residual or creates far-zone scalar charge",
            status="REQUIRED",
            missing="scalar trace neutrality theorem",
            consequence="preserves metric insertion / no-overlap guardrails",
        ),
        CorrectionTensorRoleEntry(
            name="CT16: coefficient origin requirement",
            role_candidate="correction tensor coefficients have ontology-native or action/stiffness origin",
            role="coefficient tuning guard",
            allowed_if="coefficients are derived before recovery checks",
            forbidden_if="coefficients are chosen for gamma_like, AB, exterior matching, or regular core",
            status="REQUIRED",
            missing="coefficient origin",
            consequence="prevents recovery-tuned correction tensor",
        ),
        CorrectionTensorRoleEntry(
            name="CT17: H_repair rejection",
            role_candidate="correction tensor added to cancel singularity, boundary leakage, mass shift, or scalar charge",
            role="forbidden repair tensor",
            allowed_if="never as mechanism",
            forbidden_if="accepted as correction tensor",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents tensor patchwork",
        ),
        CorrectionTensorRoleEntry(
            name="CT18: H_recovery rejection",
            role_candidate="correction tensor chosen to pass gamma_like, AB, Schwarzschild exterior, or PPN behavior",
            role="forbidden recovery-smuggling tensor",
            allowed_if="never as construction mechanism",
            forbidden_if="accepted as tensor origin",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps recovery downstream",
        ),
        CorrectionTensorRoleEntry(
            name="CT19: H_Bianchi_decorative rejection",
            role_candidate="correction tensor declared divergence-safe by Bianchi-like language only",
            role="forbidden decorative tensor",
            allowed_if="never as result",
            forbidden_if="accepted as parent compatibility",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents fake divergence safety",
        ),
        CorrectionTensorRoleEntry(
            name="CT20: H_curv anti-singularity patch rejection",
            role_candidate="H_curv inserted to force bounce, regular core, or finite curvature",
            role="forbidden anti-singularity tensor",
            allowed_if="never without equations, solutions, and neutrality",
            forbidden_if="accepted as curvature correction",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves Group 17 claim limits",
        ),
        CorrectionTensorRoleEntry(
            name="CT21: H_exch exchange-continuity patch rejection",
            role_candidate="H_exch inserted to make exchange continuity true despite undefined J/Sigma/R",
            role="forbidden exchange paint tensor",
            allowed_if="never as mechanism",
            forbidden_if="accepted as exchange correction",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves Group 18 source/current limits",
        ),
        CorrectionTensorRoleEntry(
            name="CT22: parent equation insertion rejection",
            role_candidate="E_parent + H_curv + H_exch is written before correction tensors are defined",
            role="forbidden premature parent equation",
            allowed_if="deferred",
            forbidden_if="accepted as current field system",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents final parent equation overclaim",
        ),
        CorrectionTensorRoleEntry(
            name="CT23: correction tensor failure",
            role_candidate="H_curv/H_exch cannot be made source-separated, divergence-safe, and boundary-neutral",
            role="branch failure condition",
            allowed_if="used to keep correction tensors deferred or diagnostic-only",
            forbidden_if="patched with decorative identities",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="correction tensors cannot be inserted",
        ),
        CorrectionTensorRoleEntry(
            name="CT24: recommended next move",
            role_candidate="after role inventory, audit H_curv definition requirements",
            role="next local bottleneck",
            allowed_if="H_curv remains theorem target",
            forbidden_if="jumping to divergence-safety before H_curv burden is stated",
            status="RECOMMENDED",
            missing="H_curv requirements audit",
            consequence="next script should be candidate_H_curv_definition_requirements.py",
        ),
    ]


def print_entry(e: CorrectionTensorRoleEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Role candidate: {e.role_candidate}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    out = ScriptOutput()
    with out.governance_assessments():
        out.line(e.name, StatusMark.from_string(e.status), e.status)
    out.print()
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Parent correction tensor role inventory problem")

    print("Question:")
    print()
    print("  What roles are being hidden inside H_curv and H_exch?")
    print()
    print("Goal:")
    print()
    print("  inventory correction tensor roles without inserting them into a parent equation")
    print()
    print("Discipline:")
    print()
    print("  no final parent equation")
    print("  no H_curv anti-singularity patch")
    print("  no H_exch exchange-continuity patch")
    print("  no correction tensor from undefined current/source")
    print("  no ordinary matter rerouting")
    print("  no M_ext shift")
    print("  no scalar trace leakage")
    print("  no Bianchi-like decoration")
    print("  no recovery tuning")

    with out.unresolved_obligations():
        out.line("parent correction tensor role inventory problem posed", StatusMark.OBLIGATION, "role inventory required before any correction tensor is used")


def case_1_inventory(entries: List[CorrectionTensorRoleEntry]):
    header("Case 1: Parent correction tensor role inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[CorrectionTensorRoleEntry], out: ScriptOutput):
    header("Case 2: Compact correction tensor role ledger")

    print("| Entry | Role candidate | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.role_candidate.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact correction tensor role ledger produced", StatusMark.INFO, "STRUCTURAL")


def case_3_status_counts(entries: List[CorrectionTensorRoleEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  H_curv and H_exch remain theorem targets only.")
    print("  Correction tensor language is useful as requirements audit, not field equation.")
    print("  H_metric_insert and H_residual are risky because they can reopen B_s/F_zeta, O, or residual trace problems.")
    print("  H_dark remains deferred and optional.")
    print("  Diagnostic-only H-like audit objects are safest.")
    print("  Identically divergence-free, source-balanced, projected, and constraint-preserving classes are candidates only if constructed.")
    print("  Repair, recovery, Bianchi-decoration, anti-singularity patch, exchange-continuity patch, and premature parent insertion are rejected.")
    print("  Next gate is H_curv definition requirements.")

    with out.governance_assessments():
        out.line("correction tensor role status count produced", StatusMark.INFO, "STRUCTURAL")


def case_4_role_classes(out: ScriptOutput):
    header("Case 4: Correction tensor role classes")

    print("Candidate / theorem-target role classes:")
    print()
    print("1. H_curv curvature / finite-admissibility correction candidate")
    print("2. H_exch exchange / vacuum-current correction candidate")
    print("3. H_metric_insert B_s/F_zeta / no-overlap candidate")
    print("4. H_residual residual-kill / non-metric residual candidate")
    print("5. H_dark optional dark-sector candidate")
    print("6. diagnostic-only H-like audit object")
    print("7. identically divergence-free tensor class")
    print("8. source-balanced divergence tensor class")
    print("9. projected correction tensor class")
    print("10. constraint-preserving correction tensor class")
    print()
    print("Rejected role classes:")
    print()
    print("1. repair tensor")
    print("2. recovery tensor")
    print("3. Bianchi-decorative tensor")
    print("4. anti-singularity patch tensor")
    print("5. exchange-continuity patch tensor")
    print("6. premature parent-equation insertion")

    with out.governance_assessments():
        out.line("correction tensor role classes listed", StatusMark.PASS, "RECOMMENDED")


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: Correction tensor role decision tree")

    print("Decision tree:")
    print()
    print("1. H object has source origin, divergence behavior, boundary neutrality, and source separation:")
    print("   may proceed to definition requirements.")
    print()
    print("2. H object is diagnostic-only:")
    print("   safe if never inserted into field equation.")
    print()
    print("3. H_curv uses e_curv/A_curv/J_curv without dynamics/current:")
    print("   defer or reject.")
    print()
    print("4. H_exch uses J_V/J_exch/Sigma/R before definition:")
    print("   defer or reject.")
    print()
    print("5. H_metric_insert or H_residual reopens scalar trace:")
    print("   reject unless O/no-overlap is real.")
    print()
    print("6. H object is repair/recovery/Bianchi decoration:")
    print("   rejected.")
    print()
    print("7. Parent equation insertion appears:")
    print("   rejected as premature.")

    with out.governance_assessments():
        out.line("correction tensor role decision tree stated", StatusMark.PASS, "RECOMMENDED")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  H_curv/H_exch cannot be promoted beyond theorem targets")
    print("  because source/current/divergence/boundary structures are missing.")
    print()
    print("Consequence:")
    print()
    print("  keep correction tensors deferred or diagnostic-only.")
    print("  do not write parent equation.")
    print()
    print("Bad failure:")
    print()
    print("  insert H_curv/H_exch because parent closure needs them.")

    with out.governance_assessments():
        out.line("correction tensor role good failure stated", StatusMark.DEFER, "DEFERRED_PENDING_PREREQUISITES")


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("Correction tensor role inventory fails if:")
    print()
    print("1. H_curv is used as anti-singularity patch")
    print("2. H_exch is used as exchange-continuity patch")
    print("3. H is derived from undefined J_curv/J_V/J_exch")
    print("4. H uses e_curv as source reservoir")
    print("5. H uses Sigma/R as tuning knobs")
    print("6. H shifts M_ext")
    print("7. H reroutes ordinary matter")
    print("8. H leaks scalar trace")
    print("9. H restores killed residual metric trace")
    print("10. H is recovery-tuned")
    print("11. H is called divergence-safe by Bianchi-like language")
    print("12. parent equation is written prematurely")

    with out.governance_assessments():
        out.line("correction tensor role failure controls stated", StatusMark.WARN, "RISK")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_parent_correction_tensor_role_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_H_curv_definition_requirements.py")
    print("   Define what H_curv must be to be more than anti-singularity patch.")
    print()
    print("3. candidate_correction_tensor_role_failure_summary.py")
    print("   Use if all H roles collapse into decorative correction.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_H_curv_definition_requirements.py")
    print()
    print("Reason:")
    print("  H_curv is the first correction tensor to fence because curvature/admissibility language")
    print("  is especially prone to anti-singularity overclaim.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "STRUCTURAL")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("H_curv and H_exch remain theorem targets only.")
    print()
    print("Correction tensor language is useful as requirements audit, not field equation.")
    print()
    print("Candidate future tensor classes:")
    print()
    print("  identically divergence-free")
    print("  source-balanced")
    print("  projected")
    print("  constraint-preserving")
    print("  diagnostic-only")
    print()
    print("Rejected:")
    print()
    print("  repair tensor")
    print("  recovery tensor")
    print("  Bianchi-decorative tensor")
    print("  anti-singularity patch")
    print("  exchange-continuity patch")
    print("  premature parent insertion")
    print()
    print("Best next script:")
    print()
    print("  candidate_H_curv_definition_requirements.py")

    with out.governance_assessments():
        out.line("parent correction tensor role inventory complete", StatusMark.PASS, "CLOSED")

    out.print()


def record_governance(ns) -> None:
    # Obligations for each REQUIRED entry
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_source_separation_theorem_19_roles",
        script_id=SCRIPT_ID,
        title="Derive ordinary matter source separation theorem",
        status=ObligationStatus.OPEN,
        required_by=["parent_correction_tensor_insertion_route"],
        description=(
            "Show that H_curv and H_exch do not reroute ordinary T_mu_nu "
            "or double-count matter sources. CT13 requirement."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_mass_neutrality_theorem_19_roles",
        script_id=SCRIPT_ID,
        title="Derive exterior mass neutrality theorem for correction tensors",
        status=ObligationStatus.OPEN,
        required_by=["parent_correction_tensor_insertion_route"],
        description=(
            "Show that delta M_ext|H_curv/H_exch = 0 unless derived through "
            "established A-sector source law. CT14 requirement."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_scalar_trace_neutrality_theorem_19_roles",
        script_id=SCRIPT_ID,
        title="Derive scalar trace neutrality theorem for correction tensors",
        status=ObligationStatus.OPEN,
        required_by=["parent_correction_tensor_insertion_route"],
        description=(
            "Show that H_curv/H_exch does not leak B_s/zeta/kappa scalar charge. CT15 requirement."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_coefficient_origin_19_roles",
        script_id=SCRIPT_ID,
        title="Derive correction tensor coefficient origins",
        status=ObligationStatus.OPEN,
        required_by=["parent_correction_tensor_insertion_route"],
        description=(
            "Show that correction tensor coefficients have ontology-native or action/stiffness origin, "
            "not recovery-tuned values. CT16 requirement."
        ),
    ))

    # Route records for candidate tensor classes
    ns.record_route(RouteRecord(
        route_id="diagnostic_only_correction_tensor_route",
        script_id=SCRIPT_ID,
        name="Diagnostic-only H-like audit object",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "explicitly marked diagnostic-only",
            "never inserted into field equation",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="identically_divergence_free_correction_route",
        script_id=SCRIPT_ID,
        name="Identically divergence-free correction tensor class",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_source_separation_theorem_19_roles", "derive_mass_neutrality_theorem_19_roles"],
        activation_conditions=[
            "actual tensor identity is constructed",
            "source origin is not repair",
        ],
    ))

    # Branch decisions for deferred entries
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_H_curv_insertion_19",
        script_id=SCRIPT_ID,
        branch_id="H_curv_correction_tensor_insertion",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_source_separation_theorem_19_roles",
            "derive_mass_neutrality_theorem_19_roles",
            "derive_scalar_trace_neutrality_theorem_19_roles",
            "derive_coefficient_origin_19_roles",
        ],
        description=(
            "H_curv remains deferred: A_curv dynamics, J_curv, source side, "
            "and divergence behavior are missing. Prerequisites not satisfied."
        ),
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_H_exch_insertion_19",
        script_id=SCRIPT_ID,
        branch_id="H_exch_correction_tensor_insertion",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_source_separation_theorem_19_roles",
            "derive_mass_neutrality_theorem_19_roles",
            "derive_scalar_trace_neutrality_theorem_19_roles",
            "derive_coefficient_origin_19_roles",
        ],
        description=(
            "H_exch remains deferred: J_V/J_exch, Sigma/R, source side, "
            "and divergence behavior are missing. Prerequisites not satisfied."
        ),
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_H_dark_insertion_19",
        script_id=SCRIPT_ID,
        branch_id="H_dark_correction_tensor_insertion",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_source_separation_theorem_19_roles"],
        description="H_dark remains deferred: dark-sector source/coupling theorem missing.",
    ))

    # Rejected branch decisions (with policy reason, not contradiction)
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_H_repair_19",
        script_id=SCRIPT_ID,
        branch_id="H_repair_correction_tensor",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="Repair tensor (CT17) rejected by policy: no tensor that cancels singularity, boundary leakage, mass shift, or scalar charge may be accepted as a correction tensor.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_H_recovery_19",
        script_id=SCRIPT_ID,
        branch_id="H_recovery_correction_tensor",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="Recovery-smuggling tensor (CT18) rejected by policy: recovery must remain downstream.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_H_Bianchi_decorative_19",
        script_id=SCRIPT_ID,
        branch_id="H_Bianchi_decorative_tensor",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="Bianchi-decorative tensor (CT19) rejected by policy: naming is not proof.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_H_curv_antisingularity_patch_19",
        script_id=SCRIPT_ID,
        branch_id="H_curv_antisingularity_patch",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="H_curv anti-singularity patch (CT20) rejected by policy: preserves Group 17 claim limits.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_H_exch_exchange_continuity_patch_19",
        script_id=SCRIPT_ID,
        branch_id="H_exch_exchange_continuity_patch",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="H_exch exchange-continuity patch (CT21) rejected by policy: preserves Group 18 current/source limits.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_premature_parent_equation_19",
        script_id=SCRIPT_ID,
        branch_id="premature_parent_equation_insertion",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="Premature parent equation insertion (CT22) rejected by policy: no correction tensors defined.",
    ))

    # CT23 BRANCH_KILLED maps to DEFERRED_PENDING_PREREQUISITES per governance rule 5
    # (without evidence of demonstrated failure it is NOT KILLED_BY_CONTRADICTION)
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_correction_tensor_failure_branch_19",
        script_id=SCRIPT_ID,
        branch_id="correction_tensor_insertion_failure",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_source_separation_theorem_19_roles",
            "derive_mass_neutrality_theorem_19_roles",
            "derive_scalar_trace_neutrality_theorem_19_roles",
            "derive_coefficient_origin_19_roles",
        ],
        description=(
            "CT23 failure condition: if H_curv/H_exch cannot be made source-separated, "
            "divergence-safe, and boundary-neutral, correction tensors remain deferred. "
            "Branch is deferred, not killed, because no contradiction has been demonstrated — "
            "prerequisites are simply absent."
        ),
    ))

    # Summary claim for the role inventory
    ns.record_claim(ClaimRecord(
        claim_id="correction_tensor_role_inventory_informational",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.INFORMATIONAL,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "H_curv and H_exch are correction tensor theorem targets whose roles are inventoried "
            "but whose definitions, source/divergence/boundary structures, and insertability "
            "remain open obligations."
        ),
        obligation_ids=[
            "derive_source_separation_theorem_19_roles",
            "derive_mass_neutrality_theorem_19_roles",
            "derive_scalar_trace_neutrality_theorem_19_roles",
            "derive_coefficient_origin_19_roles",
        ],
    ))


def main():
    header("Candidate Parent Correction Tensor Role Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_role_classes(out)
    case_5_decision_tree(out)
    case_6_good_failure(out)
    case_7_failure_controls(out)
    case_8_next_tests(out)
    final_interpretation(out)

    record_governance(ns)
    ns.record_derivation(
        derivation_id="parent_correction_tensor_role_inventory_marker",
        inputs=[],
        output=sp.Symbol("parent_correction_tensor_role_inventory_complete"),
        method="parent_correction_tensor_role_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
