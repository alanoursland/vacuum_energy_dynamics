# Candidate parent equation insertability audit
#
# Group:
#   19_parent_correction_tensor_audit
#
# Script type:
#   AUDIT
#
# Purpose
# -------
# The correction tensor boundary/mass neutrality audit found:
#
#   Boundary/mass neutrality is required but not derived.
#
# Required:
#
#   no M_ext shift independent of A,
#   no boundary counterterm,
#   no exterior scalar charge,
#   no far-zone hidden flux,
#   no shell source by support,
#   no recovery-tuned boundary smoothing,
#   no dark boundary patch,
#   no anti-singularity by boundary tensor.
#
# Candidate routes:
#
#   diagnostic-only,
#   interior-only branch filter,
#   compact support with structural zero-flux,
#   divergence-free interior tensor with neutral boundary,
#   source-balanced tensor with neutral boundary.
#
# This script decides whether any correction tensor can be inserted into a parent equation yet.
#
# Locked-door question:
#
#   Can any correction tensor be inserted into a parent equation yet?
#
# This is an insertability audit, not a parent field equation.


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
    HandoffImportRecord,
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
class InsertabilityEntry:
    name: str
    criterion: str
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
        dependency_id="correction_tensor_boundary_and_mass_neutrality_marker",
        upstream_script_id="19_parent_correction_tensor_audit__candidate_correction_tensor_boundary_and_mass_neutrality",
        upstream_derivation_id="correction_tensor_boundary_and_mass_neutrality_marker",
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


def build_entries() -> List[InsertabilityEntry]:
    return [
        InsertabilityEntry(
            name="PI1: parent equation insertability target",
            criterion="a correction tensor is insertable only if tensor definition, source origin, projection class, divergence relation, boundary neutrality, source separation, mass neutrality, scalar neutrality, coefficient origin, and recovery-independent construction are all available",
            role="core insertability theorem target",
            allowed_if="all prerequisites are defined before field-equation insertion",
            forbidden_if="parent equation is written because correction tensors are wanted",
            status="THEOREM_TARGET",
            missing="complete insertability theorem",
            consequence="decides whether H_curv/H_exch can enter parent equation",
        ),
        InsertabilityEntry(
            name="PI2: tensor definition requirement",
            criterion="H_curv/H_exch tensor rank, symmetry, trace behavior, index placement, and domain are defined",
            role="tensor well-posedness prerequisite",
            allowed_if="tensor type is explicit before insertion",
            forbidden_if="H symbol is inserted without tensor definition",
            status="REQUIRED",
            missing="tensor definition",
            consequence="prevents decorative parent term",
        ),
        InsertabilityEntry(
            name="PI3: source origin requirement",
            criterion="correction tensor source origin is independently defined",
            role="source prerequisite",
            allowed_if="source exists before correction tensor uses it",
            forbidden_if="source is defined by the tensor divergence or usefulness",
            status="REQUIRED",
            missing="source origin theorem",
            consequence="prevents source-by-tensor closure",
        ),
        InsertabilityEntry(
            name="PI4: projection class requirement",
            criterion="projection class / sector placement is defined",
            role="no-overlap prerequisite",
            allowed_if="projector and target sector are real",
            forbidden_if="projection hides metric/matter/residual overlap",
            status="REQUIRED",
            missing="projection / sector theorem",
            consequence="prevents source and metric overlap",
        ),
        InsertabilityEntry(
            name="PI5: divergence relation requirement",
            criterion="divergence relation is a constructed identity, independent source balance, defined projection/constraint theorem, or diagnostic-only non-insertion",
            role="divergence prerequisite",
            allowed_if="divergence safety is real before insertion",
            forbidden_if="Bianchi-like language or decorative continuity is used",
            status="REQUIRED",
            missing="divergence-safety theorem",
            consequence="prevents fake parent compatibility",
        ),
        InsertabilityEntry(
            name="PI6: boundary neutrality requirement",
            criterion="correction tensor has no boundary repair, hidden shell source, scalar tail, far-zone flux, or boundary counterterm",
            role="boundary prerequisite",
            allowed_if="boundary behavior is structural and neutral",
            forbidden_if="boundary mismatch motivates insertion",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="protects exterior sector",
        ),
        InsertabilityEntry(
            name="PI7: ordinary matter separation requirement",
            criterion="ordinary T_mu_nu / rho / scalar charge remains in ordinary source routing",
            role="ordinary matter prerequisite",
            allowed_if="ordinary matter is not double-counted or rerouted",
            forbidden_if="correction tensor carries ordinary matter by convenience",
            status="REQUIRED",
            missing="ordinary matter separation theorem",
            consequence="protects ordinary matter coupling",
        ),
        InsertabilityEntry(
            name="PI8: M_ext neutrality requirement",
            criterion="delta M_ext|H = 0 unless derived through established A-sector source law",
            role="mass prerequisite",
            allowed_if="exterior mass neutrality is structural",
            forbidden_if="H shifts measured exterior mass",
            status="REQUIRED",
            missing="M_ext neutrality theorem",
            consequence="protects strongest A-sector result",
        ),
        InsertabilityEntry(
            name="PI9: scalar trace neutrality requirement",
            criterion="H does not reopen B_s/F_zeta, residual trace, kappa, or exterior scalar charge",
            role="scalar prerequisite",
            allowed_if="scalar trace/no-overlap guardrails remain closed",
            forbidden_if="H becomes hidden scalar metric/source channel",
            status="REQUIRED",
            missing="scalar trace neutrality / O no-overlap theorem",
            consequence="preserves Group 16 guardrails",
        ),
        InsertabilityEntry(
            name="PI10: coefficient origin requirement",
            criterion="coefficients have ontology-native, action, stiffness, source, or identity origin",
            role="coefficient prerequisite",
            allowed_if="coefficients are derived before recovery/boundary tests",
            forbidden_if="coefficients tune finite core, exchange closure, boundary, or recovery",
            status="REQUIRED",
            missing="coefficient origin theorem",
            consequence="prevents tuning by constants",
        ),
        InsertabilityEntry(
            name="PI11: recovery-independent construction requirement",
            criterion="correction tensor is not chosen to pass gamma_like, AB, exterior matching, or PPN behavior",
            role="recovery-smuggling guard",
            allowed_if="recovery remains downstream test",
            forbidden_if="recovery behavior selects tensor form",
            status="REQUIRED",
            missing="not a mechanism",
            consequence="keeps recovery downstream",
        ),
        InsertabilityEntry(
            name="PI12: H_curv insertability status",
            criterion="H_curv is not insertable because A_curv dynamics/J_curv/source/divergence/boundary/mass/scalar structures are missing",
            role="curvature correction status",
            allowed_if="H_curv remains theorem target or diagnostic-only",
            forbidden_if="H_curv is inserted to get finite curvature",
            status="DEFER",
            missing="H_curv prerequisites",
            consequence="prevents anti-singularity correction insertion",
        ),
        InsertabilityEntry(
            name="PI13: H_exch insertability status",
            criterion="H_exch is not insertable because J_V/J_exch/Sigma/R/source/divergence/boundary/mass/scalar structures are missing",
            role="exchange correction status",
            allowed_if="H_exch remains theorem target or diagnostic-only",
            forbidden_if="H_exch is inserted to close exchange continuity",
            status="DEFER",
            missing="H_exch prerequisites",
            consequence="prevents exchange correction insertion",
        ),
        InsertabilityEntry(
            name="PI14: diagnostic-only route",
            criterion="H-like object remains diagnostic-only and is not a parent equation term",
            role="safe fallback",
            allowed_if="explicitly not inserted",
            forbidden_if="diagnostic object becomes parent correction",
            status="SAFE_IF",
            missing="none if kept diagnostic",
            consequence="only currently safe route",
        ),
        InsertabilityEntry(
            name="PI15: theorem-target parent form",
            criterion="E_parent + H_curv + H_exch = source side is allowed only as theorem target",
            role="non-law parent form",
            allowed_if="explicitly marked not current field equation",
            forbidden_if="presented as current minimal field system",
            status="THEOREM_TARGET",
            missing="all H/source/divergence prerequisites",
            consequence="preserves future syntax without overclaim",
        ),
        InsertabilityEntry(
            name="PI16: divergence theorem target parent form",
            criterion="Div(E_parent + H_curv + H_exch) = B_closed[T] + B_relax is allowed only as theorem target",
            role="non-law divergence form",
            allowed_if="explicitly marked not law",
            forbidden_if="used as closure before B_closed/B_relax/H are defined",
            status="THEOREM_TARGET",
            missing="parent divergence identity and source terms",
            consequence="prevents decorative parent divergence closure",
        ),
        InsertabilityEntry(
            name="PI17: H_curv finite-curvature insertion rejection",
            criterion="H_curv inserted to get finite curvature, regular core, bounce, or anti-singularity behavior",
            role="forbidden curvature insertion",
            allowed_if="never as mechanism",
            forbidden_if="accepted as parent correction",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves Group 17 claim limits",
        ),
        InsertabilityEntry(
            name="PI18: H_exch exchange-continuity insertion rejection",
            criterion="H_exch inserted to close nabla_mu J_exch^mu = Sigma_exch - R_exch",
            role="forbidden exchange insertion",
            allowed_if="never while J/Sigma/R are undefined",
            forbidden_if="accepted as exchange correction",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves Group 18 current/source limits",
        ),
        InsertabilityEntry(
            name="PI19: Bianchi-like insertion rejection",
            criterion="H inserted because geometric terms can be made Bianchi-compatible by name",
            role="forbidden divergence insertion",
            allowed_if="never as proof",
            forbidden_if="accepted as parent compatibility",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents Bianchi smoke",
        ),
        InsertabilityEntry(
            name="PI20: recovery insertion rejection",
            criterion="H inserted to recover GR-like gamma, AB, exterior matching, or PPN behavior",
            role="forbidden recovery insertion",
            allowed_if="never as construction",
            forbidden_if="accepted as parent correction",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps recovery downstream",
        ),
        InsertabilityEntry(
            name="PI21: boundary leakage insertion rejection",
            criterion="H inserted to cancel boundary leakage, shell source, scalar tail, or exterior mass mismatch",
            role="forbidden boundary insertion",
            allowed_if="never as mechanism",
            forbidden_if="accepted as correction tensor",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents boundary repair",
        ),
        InsertabilityEntry(
            name="PI22: undefined-current insertion rejection",
            criterion="H inserted using undefined J_curv, J_V, J_sub, J_exch, Sigma/R, or dark source",
            role="forbidden source/current insertion",
            allowed_if="never before definitions",
            forbidden_if="accepted as parent correction source",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents undefined-source parent equation",
        ),
        InsertabilityEntry(
            name="PI23: parent insertion failure",
            criterion="no correction tensor satisfies all insertability requirements",
            role="closure failure condition",
            allowed_if="used to keep H_curv/H_exch deferred or diagnostic-only",
            forbidden_if="patched with theorem-target parent equation as law",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="no parent correction tensor is insertable yet",
        ),
        InsertabilityEntry(
            name="PI24: recommended next move",
            criterion="after insertability audit, close Group 19 with status summary",
            role="next local bottleneck",
            allowed_if="no tensor is insertable yet",
            forbidden_if="opening a new parent equation group without closure summary",
            status="RECOMMENDED",
            missing="Group 19 status summary",
            consequence="next script should be candidate_parent_correction_tensor_group_status_summary.py",
        ),
    ]


def print_entry(e: InsertabilityEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Criterion: {e.criterion}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    out = ScriptOutput()
    with out.governance_assessments():
        out.line(e.name, StatusMark.from_string(e.status), e.status)

    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Parent equation insertability problem")

    print("Question:")
    print()
    print("  Can any correction tensor be inserted into a parent equation yet?")
    print()
    print("Goal:")
    print()
    print("  decide whether H_curv/H_exch can appear in a parent equation or must remain deferred")
    print()
    print("Discipline:")
    print()
    print("  no final parent equation")
    print("  no correction tensor without definition")
    print("  no source-by-tensor")
    print("  no Bianchi smoke")
    print("  no boundary repair")
    print("  no ordinary matter double-count")
    print("  no M_ext shift")
    print("  no scalar trace leak")
    print("  no recovery insertion")
    print("  no undefined current/source insertion")

    with out.unresolved_obligations():
        out.line("parent equation insertability problem posed", StatusMark.OBLIGATION, "insertability audit required before any parent equation is written")


def case_1_inventory(entries: List[InsertabilityEntry]):
    header("Case 1: Parent equation insertability inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[InsertabilityEntry], out: ScriptOutput):
    header("Case 2: Compact parent insertability ledger")

    print("| Entry | Criterion | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.criterion.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact parent insertability ledger produced", StatusMark.INFO, "STRUCTURAL")


def case_3_status_counts(entries: List[InsertabilityEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  No correction tensor is insertable into a parent equation yet.")
    print("  H_curv and H_exch remain deferred or diagnostic-only.")
    print("  The only safe current route is diagnostic-only H-like audit objects.")
    print("  Parent equation forms may be retained only as theorem targets, not laws.")
    print("  Insertability requires tensor definition, source origin, projection class, divergence relation, boundary neutrality, ordinary matter separation, M_ext neutrality, scalar trace neutrality, coefficient origin, and recovery-independent construction.")
    print("  H_curv finite-curvature insertion, H_exch exchange-continuity insertion, Bianchi-like insertion, recovery insertion, boundary leakage insertion, and undefined-current insertion are rejected.")
    print("  Next gate is Group 19 status summary.")

    with out.governance_assessments():
        out.line("parent equation insertability status count produced", StatusMark.INFO, "STRUCTURAL")


def case_4_insertability_requirements(out: ScriptOutput):
    header("Case 4: Insertability requirements")

    print("Insertability requirements:")
    print()
    print("1. tensor definition")
    print("2. source origin")
    print("3. projection class")
    print("4. divergence relation")
    print("5. boundary neutrality")
    print("6. ordinary matter separation")
    print("7. M_ext neutrality")
    print("8. scalar trace neutrality")
    print("9. coefficient origin")
    print("10. recovery-independent construction")
    print()
    print("Current result:")
    print()
    print("  no correction tensor satisfies all requirements")

    with out.governance_assessments():
        out.line("parent insertability requirements listed", StatusMark.PASS, "RECOMMENDED")


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: Parent insertability decision tree")

    print("Decision tree:")
    print()
    print("1. H satisfies all insertability requirements:")
    print("   may become future parent-equation candidate.")
    print()
    print("2. H is diagnostic-only:")
    print("   safe, but not inserted.")
    print()
    print("3. H_curv is used for finite curvature:")
    print("   rejected.")
    print()
    print("4. H_exch is used for exchange continuity:")
    print("   rejected.")
    print()
    print("5. H is inserted through Bianchi, recovery, boundary, or undefined-current language:")
    print("   rejected.")
    print()
    print("6. No H satisfies requirements:")
    print("   parent correction tensors remain deferred.")

    with out.governance_assessments():
        out.line("parent insertability decision tree stated", StatusMark.PASS, "RECOMMENDED")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  no correction tensor is insertable yet.")
    print()
    print("Consequence:")
    print()
    print("  keep H_curv/H_exch deferred or diagnostic-only.")
    print("  do not write the parent field equation.")
    print()
    print("Bad failure:")
    print()
    print("  write a theorem-target parent equation as if it were the current field system.")

    with out.governance_assessments():
        out.line("parent insertability good failure stated", StatusMark.DEFER, "DEFERRED_PENDING_PREREQUISITES")


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("Parent insertability fails if:")
    print()
    print("1. tensor definition is missing")
    print("2. source origin is undefined")
    print("3. projection class is undefined")
    print("4. divergence relation is decorative")
    print("5. boundary neutrality is missing")
    print("6. ordinary matter is double-counted")
    print("7. M_ext shifts")
    print("8. scalar trace leaks")
    print("9. coefficient origin is recovery-tuned")
    print("10. H_curv is finite-curvature patch")
    print("11. H_exch is exchange-continuity patch")
    print("12. Bianchi language is used as proof")
    print("13. boundary leakage motivates insertion")
    print("14. undefined current/source is used")
    print("15. diagnostic-only H is inserted")

    with out.governance_assessments():
        out.line("parent insertability failure controls stated", StatusMark.WARN, "RISK")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_parent_equation_insertability_audit.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_parent_correction_tensor_group_status_summary.py")
    print("   Close Group 19 with status summary and handoff.")
    print()
    print("3. candidate_parent_insertability_failure_summary.py")
    print("   Use if insertability failure needs standalone emphasis.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_parent_correction_tensor_group_status_summary.py")
    print()
    print("Reason:")
    print("  Group 19 has audited correction tensors for roles, definition requirements, divergence safety, source separation, boundary/mass neutrality, and insertability.")
    print("  It should close with a summary ledger.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "STRUCTURAL")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("No correction tensor is insertable into a parent equation yet.")
    print()
    print("H_curv:")
    print("  deferred or diagnostic-only")
    print()
    print("H_exch:")
    print("  deferred or diagnostic-only")
    print()
    print("Only safe current route:")
    print()
    print("  diagnostic-only H-like audit objects")
    print()
    print("Parent equation forms:")
    print()
    print("  theorem targets only")
    print("  not current field equations")
    print()
    print("Best next script:")
    print()
    print("  candidate_parent_correction_tensor_group_status_summary.py")

    with out.governance_assessments():
        out.line("parent equation insertability audit complete", StatusMark.PASS, "CLOSED")



def record_governance(ns) -> None:
    # One obligation per REQUIRED entry
    required_obligations = [
        ("derive_tensor_definition_for_insertability_19",
         "Derive correction tensor definition for insertability",
         "H_curv/H_exch tensor rank, symmetry, trace behavior, index placement, and domain must be defined (PI2)."),
        ("derive_source_origin_for_insertability_19",
         "Derive correction tensor source origin",
         "Source origin must be independently defined before insertion (PI3)."),
        ("derive_projection_class_for_insertability_19",
         "Derive correction tensor projection class",
         "Projection class/sector placement must be defined, not hiding overlap (PI4)."),
        ("derive_divergence_relation_for_insertability_19",
         "Derive correction tensor divergence relation",
         "Divergence relation must be a constructed identity, source balance, or projection theorem — not Bianchi (PI5)."),
        ("derive_boundary_neutrality_for_insertability_19",
         "Derive correction tensor boundary neutrality",
         "No boundary repair, hidden shell source, scalar tail, far-zone flux, or counterterm (PI6)."),
        ("derive_ordinary_matter_separation_for_insertability_19",
         "Derive ordinary matter separation for insertability",
         "Ordinary T_mu_nu must stay in ordinary source routing (PI7)."),
        ("derive_M_ext_neutrality_for_insertability_19",
         "Derive M_ext neutrality for insertability",
         "delta M_ext|H = 0 unless derived through A-sector source law (PI8)."),
        ("derive_scalar_trace_neutrality_for_insertability_19",
         "Derive scalar trace neutrality for insertability",
         "H must not reopen B_s/F_zeta, residual trace, kappa, or exterior scalar charge (PI9)."),
        ("derive_coefficient_origin_for_insertability_19",
         "Derive coefficient origin for insertability",
         "Coefficients must have ontology-native, action, stiffness, source, or identity origin (PI10)."),
    ]

    for obligation_id, title, description in required_obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["parent_correction_tensor_insertion"],
            description=description,
        ))

    all_obligation_ids = [o[0] for o in required_obligations]

    # Deferred branches for H_curv and H_exch
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_H_curv_parent_insertion_19",
        script_id=SCRIPT_ID,
        branch_id="H_curv_parent_equation_insertion",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=all_obligation_ids,
        description=(
            "H_curv is not insertable into a parent equation because A_curv dynamics, J_curv, source, "
            "divergence, boundary, mass, and scalar structures are missing. Deferred pending prerequisites."
        ),
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_H_exch_parent_insertion_19",
        script_id=SCRIPT_ID,
        branch_id="H_exch_parent_equation_insertion",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=all_obligation_ids,
        description=(
            "H_exch is not insertable into a parent equation because J_V, J_exch, Sigma/R, source, "
            "divergence, boundary, mass, and scalar structures are missing. Deferred pending prerequisites."
        ),
    ))

    # PI23 BRANCH_KILLED -> DEFERRED_PENDING_PREREQUISITES per governance rule 5
    # "not insertable yet" != "branch killed" — this is the key governance item 14 point
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_parent_insertion_failure_branch_19",
        script_id=SCRIPT_ID,
        branch_id="parent_correction_tensor_insertion_failure",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=all_obligation_ids,
        description=(
            "PI23 failure condition: no correction tensor satisfies all insertability requirements. "
            "The branch is DEFERRED_PENDING_PREREQUISITES — not killed by contradiction. "
            "Governance item 14: 'not insertable yet' does not equal 'branch killed.' "
            "Prerequisites are simply absent; no formal contradiction has been proved."
        ),
    ))

    # Rejected insertion routes
    for decision_id, branch_id, description in [
        ("reject_H_curv_finite_curvature_insertion_19", "H_curv_finite_curvature_parent_insertion",
         "PI17: H_curv inserted to get finite curvature/regular core/bounce rejected by policy."),
        ("reject_H_exch_exchange_continuity_insertion_19", "H_exch_exchange_continuity_parent_insertion",
         "PI18: H_exch inserted to close exchange continuity while J/Sigma/R undefined, rejected by policy."),
        ("reject_Bianchi_parent_insertion_19", "Bianchi_like_parent_insertion",
         "PI19: Bianchi-like insertion rejected by policy."),
        ("reject_recovery_parent_insertion_19", "recovery_motivated_parent_insertion",
         "PI20: recovery insertion rejected by policy."),
        ("reject_boundary_leakage_parent_insertion_19", "boundary_leakage_motivated_parent_insertion",
         "PI21: boundary-leakage-motivated insertion rejected by policy."),
        ("reject_undefined_current_parent_insertion_19", "undefined_current_source_parent_insertion",
         "PI22: insertion using undefined J_curv/J_V/J_sub/J_exch/Sigma/R/dark rejected by policy."),
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=decision_id,
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            description=description,
        ))

    # No parent equation yet claim
    ns.record_claim(ClaimRecord(
        claim_id="no_parent_equation_yet_19",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.NOT_INSERTABLE_YET,
        statement=(
            "No parent correction tensor satisfies all insertability requirements. "
            "H_curv and H_exch remain deferred or diagnostic-only. "
            "No parent field equation is ready."
        ),
        obligation_ids=all_obligation_ids,
    ))

    # Handoff import from this audit to the group summary
    ns.record_handoff_import(HandoffImportRecord(
        handoff_id="insertability_audit_to_group_summary_19",
        script_id=SCRIPT_ID,
        imported_as=RecordKind.SUMMARY_CLAIM,
        status=GovernanceStatus.NOT_INSERTABLE_YET,
        imported_record_refs=[
            "claim:no_parent_equation_yet_19",
            "obligation:derive_tensor_definition_for_insertability_19",
            "obligation:derive_source_origin_for_insertability_19",
            "obligation:derive_projection_class_for_insertability_19",
            "obligation:derive_divergence_relation_for_insertability_19",
            "obligation:derive_boundary_neutrality_for_insertability_19",
            "obligation:derive_ordinary_matter_separation_for_insertability_19",
            "obligation:derive_M_ext_neutrality_for_insertability_19",
            "obligation:derive_scalar_trace_neutrality_for_insertability_19",
            "obligation:derive_coefficient_origin_for_insertability_19",
            "branch:defer_H_curv_parent_insertion_19",
            "branch:defer_H_exch_parent_insertion_19",
        ],
        description=(
            "Insertability audit handoff: no correction tensor is insertable yet. "
            "All ten prerequisites remain open. Both H_curv and H_exch are deferred. "
            "Group 19 group status summary should import this conclusion."
        ),
    ))


def main():
    header("Candidate Parent Equation Insertability Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_insertability_requirements(out)
    case_5_decision_tree(out)
    case_6_good_failure(out)
    case_7_failure_controls(out)
    case_8_next_tests(out)
    final_interpretation(out)

    record_governance(ns)
    ns.record_derivation(
        derivation_id="parent_equation_insertability_audit_marker",
        inputs=[],
        output=sp.Symbol("parent_equation_insertability_audit_complete"),
        method="parent_equation_insertability_audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
