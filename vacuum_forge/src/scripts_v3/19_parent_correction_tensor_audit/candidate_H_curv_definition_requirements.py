# Candidate H_curv definition requirements
#
# Group:
#   19_parent_correction_tensor_audit
#
# Script type:
#   REQUIREMENTS
#
# Purpose
# -------
# The parent correction tensor role inventory found:
#
#   H_curv and H_exch remain theorem targets only.
#   Correction tensor language is useful as requirements audit, not field equation.
#
# Candidate future tensor classes:
#
#   identically divergence-free,
#   source-balanced,
#   projected,
#   constraint-preserving,
#   diagnostic-only.
#
# Rejected:
#
#   repair tensor,
#   recovery tensor,
#   Bianchi-decorative tensor,
#   anti-singularity patch,
#   exchange-continuity patch,
#   premature parent insertion.
#
# This script fences H_curv before any curvature correction tensor is used.
#
# Locked-door question:
#
#   What must H_curv be to be more than an anti-singularity patch?
#
# This is a requirements audit, not a curvature correction tensor derivation.


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
class HCurvRequirementEntry:
    name: str
    requirement: str
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
        dependency_id="parent_correction_tensor_role_inventory_marker",
        upstream_script_id="19_parent_correction_tensor_audit__candidate_parent_correction_tensor_role_inventory",
        upstream_derivation_id="parent_correction_tensor_role_inventory_marker",
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


def build_entries() -> List[HCurvRequirementEntry]:
    return [
        HCurvRequirementEntry(
            name="HC1: H_curv definition target",
            requirement="H_curv has curvature admissibility object, domain, measure, source/current relation, projection class, tensor symmetry, divergence behavior, boundary behavior, matter separation, M_ext neutrality, scalar trace neutrality, and claim-level limit",
            role="core curvature correction theorem target",
            allowed_if="all requirements are explicit before H_curv is inserted",
            forbidden_if="H_curv is named as finite-curvature correction without structure",
            status="THEOREM_TARGET",
            missing="actual H_curv definition",
            consequence="decides whether curvature correction tensor language can become technical",
        ),
        HCurvRequirementEntry(
            name="HC2: curvature admissibility object requirement",
            requirement="A_curv or equivalent finite-admissibility object is formally defined",
            role="curvature source prerequisite",
            allowed_if="admissibility object is defined before H_curv",
            forbidden_if="H_curv defines A_curv by being useful",
            status="REQUIRED",
            missing="formal A_curv functional / invariant set",
            consequence="prevents H_curv from inventing curvature target",
        ),
        HCurvRequirementEntry(
            name="HC3: diagnostic status guard",
            requirement="A_curv remains diagnostic / branch-filter unless dynamics are derived",
            role="Group 17 preservation guard",
            allowed_if="H_curv does not promote diagnostic to dynamics",
            forbidden_if="H_curv turns branch filter into anti-singularity force",
            status="REQUIRED",
            missing="dynamics if stronger claim is wanted",
            consequence="preserves claim-level limits",
        ),
        HCurvRequirementEntry(
            name="HC4: domain requirement",
            requirement="domain D_curv/H_curv where correction acts is specified",
            role="definition prerequisite",
            allowed_if="domain is structural and not solution-tailored",
            forbidden_if="domain is chosen to exclude singular/leaky regions",
            status="REQUIRED",
            missing="D_curv / correction domain",
            consequence="prevents convenient-domain regularization",
        ),
        HCurvRequirementEntry(
            name="HC5: measure requirement",
            requirement="curvature/admissibility measure used by H_curv is specified",
            role="curvature accounting prerequisite",
            allowed_if="measure is defined independently of desired finite result",
            forbidden_if="measure hides divergence or boundary leakage",
            status="REQUIRED",
            missing="physical/geometry measure",
            consequence="prevents fake finite tensor accounting",
        ),
        HCurvRequirementEntry(
            name="HC6: source/current relation requirement",
            requirement="H_curv relation to A_curv, e_curv, or J_curv is explicit and non-circular",
            role="source-origin guard",
            allowed_if="source/current object exists before H_curv uses it",
            forbidden_if="H_curv defines its own source or uses undefined J_curv",
            status="REQUIRED",
            missing="source/current relation",
            consequence="prevents curvature correction from becoming source label",
        ),
        HCurvRequirementEntry(
            name="HC7: J_curv absence guard",
            requirement="J_curv is not defined and cannot be used as H_curv source/current",
            role="current absence guard",
            allowed_if="H_curv remains deferred or independent of J_curv",
            forbidden_if="H_curv imports J_curv by name",
            status="REQUIRED",
            missing="J_curv definition",
            consequence="preserves Group 17 current result",
        ),
        HCurvRequirementEntry(
            name="HC8: e_curv accounting guard",
            requirement="e_curv remains diagnostic/accounting only and not source reservoir",
            role="curvature energy guard",
            allowed_if="e_curv is not used to pay for H_curv",
            forbidden_if="e_curv supplies stress, pressure, bounce money, or tensor coefficient by fiat",
            status="REQUIRED",
            missing="source law if e_curv is promoted",
            consequence="prevents curvature energy reservoir",
        ),
        HCurvRequirementEntry(
            name="HC9: projection class requirement",
            requirement="H_curv projection class is specified: spacetime tensor, spatial tensor, projected sector tensor, or diagnostic-only object",
            role="covariance/projection guard",
            allowed_if="projection class is explicit and source-compatible",
            forbidden_if="projection hides overlap with metric/residual sectors",
            status="REQUIRED",
            missing="projection class and projector",
            consequence="prevents fake covariant-enough correction",
        ),
        HCurvRequirementEntry(
            name="HC10: tensor symmetry requirement",
            requirement="H_curv tensor rank, symmetry, trace behavior, and index placement are specified",
            role="tensor well-posedness guard",
            allowed_if="symmetry follows from insertion target",
            forbidden_if="symbol H_curv is used with no tensor type",
            status="REQUIRED",
            missing="tensor type / symmetry",
            consequence="prevents decorative tensor symbol",
        ),
        HCurvRequirementEntry(
            name="HC11: divergence behavior requirement",
            requirement="H_curv divergence behavior is specified without decorative Bianchi language",
            role="divergence-safety prerequisite",
            allowed_if="divergence identity or source-balanced partner is real",
            forbidden_if="divergence safety is asserted because H_curv is geometric",
            status="REQUIRED",
            missing="divergence identity or source partner",
            consequence="prevents fake parent compatibility",
        ),
        HCurvRequirementEntry(
            name="HC12: boundary behavior requirement",
            requirement="H_curv has no boundary repair flux, shell hiding, scalar tail cancellation, or M_ext shift",
            role="boundary neutrality guard",
            allowed_if="boundary behavior is structural and neutral",
            forbidden_if="H_curv repairs boundary leakage or finite-admissibility failure",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="protects exterior sector",
        ),
        HCurvRequirementEntry(
            name="HC13: ordinary matter separation requirement",
            requirement="H_curv does not reroute ordinary T_mu_nu or double-count matter",
            role="matter separation guard",
            allowed_if="ordinary matter remains in established source routing",
            forbidden_if="H_curv hides ordinary matter in curvature correction side",
            status="REQUIRED",
            missing="matter separation theorem",
            consequence="protects ordinary matter coupling",
        ),
        HCurvRequirementEntry(
            name="HC14: M_ext neutrality requirement",
            requirement="delta M_ext|H_curv = 0 unless derived through established A-sector source law",
            role="mass neutrality guard",
            allowed_if="H_curv is exterior-mass-neutral by theorem",
            forbidden_if="H_curv changes measured exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        HCurvRequirementEntry(
            name="HC15: scalar trace neutrality requirement",
            requirement="H_curv does not reopen B_s/F_zeta, residual trace, kappa, or exterior scalar charge",
            role="metric scalar guard",
            allowed_if="scalar/no-overlap guardrails remain closed",
            forbidden_if="H_curv restores killed residual metric trace",
            status="REQUIRED",
            missing="scalar trace neutrality / no-overlap theorem",
            consequence="preserves Group 16 guardrails",
        ),
        HCurvRequirementEntry(
            name="HC16: coefficient origin requirement",
            requirement="H_curv coefficients have ontology-native, action, stiffness, or admissibility origin",
            role="coefficient tuning guard",
            allowed_if="coefficients are derived before recovery and solution tests",
            forbidden_if="coefficients are chosen for finite core, exterior match, or recovery",
            status="REQUIRED",
            missing="coefficient origin",
            consequence="prevents regular-core / recovery tuning",
        ),
        HCurvRequirementEntry(
            name="HC17: claim-level limit requirement",
            requirement="H_curv does not license bounce, regular core, or dynamical avoidance without equations and solutions",
            role="anti-overclaim guard",
            allowed_if="claims remain diagnostic/theorem-target until dynamics exist",
            forbidden_if="H_curv is advertised as anti-singularity mechanism",
            status="REQUIRED",
            missing="dynamics, solutions, neutrality theorem",
            consequence="preserves Group 17 anti-singularity claim audit",
        ),
        HCurvRequirementEntry(
            name="HC18: diagnostic-only H_curv branch",
            requirement="H_curv-like object used only as diagnostic audit and never inserted into field equation",
            role="safe fallback branch",
            allowed_if="explicitly diagnostic-only",
            forbidden_if="diagnostic H_curv becomes correction tensor term",
            status="SAFE_IF",
            missing="none if kept diagnostic",
            consequence="allows curvature correction audits without parent insertion",
        ),
        HCurvRequirementEntry(
            name="HC19: identically divergence-free H_curv candidate",
            requirement="H_curv divergence vanishes by constructed identity",
            role="future tensor class candidate",
            allowed_if="identity is mathematically real and not repair",
            forbidden_if="identity is asserted by Bianchi-like language",
            status="CANDIDATE",
            missing="actual tensor identity",
            consequence="possible future divergence-safe route if constructed",
        ),
        HCurvRequirementEntry(
            name="HC20: source-balanced H_curv candidate",
            requirement="divergence of H_curv balances an independently defined curvature source side",
            role="future source-balance candidate",
            allowed_if="curvature source side exists before H_curv",
            forbidden_if="H_curv and source define each other",
            status="CANDIDATE",
            missing="curvature source side",
            consequence="possible future route if source partner is real",
        ),
        HCurvRequirementEntry(
            name="HC21: projected H_curv candidate",
            requirement="H_curv lives in defined curvature/admissibility projector subspace",
            role="future projection candidate",
            allowed_if="projector and sector split are defined",
            forbidden_if="projection hides overlap or residual scalar leakage",
            status="CANDIDATE",
            missing="projector / sector split",
            consequence="possible route to no-overlap if projector is real",
        ),
        HCurvRequirementEntry(
            name="HC22: arbitrary finite-curvature tensor rejection",
            requirement="H_curv is any tensor that makes curvature finite",
            role="forbidden anti-singularity shortcut",
            allowed_if="never as definition",
            forbidden_if="accepted as H_curv",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents finite-curvature by declaration",
        ),
        HCurvRequirementEntry(
            name="HC23: e_curv source reservoir rejection",
            requirement="H_curv sourced by e_curv as free reservoir / pressure / bounce money",
            role="forbidden curvature energy branch",
            allowed_if="never under current status",
            forbidden_if="accepted as H_curv source",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves e_curv diagnostic/accounting-only status",
        ),
        HCurvRequirementEntry(
            name="HC24: regular-core tuning rejection",
            requirement="H_curv coefficient/support chosen to make regular core",
            role="forbidden solution-tuning branch",
            allowed_if="never as construction",
            forbidden_if="accepted as curvature correction",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents solution-tailored correction tensor",
        ),
        HCurvRequirementEntry(
            name="HC25: boundary counterterm rejection",
            requirement="H_curv acts as boundary counterterm to cancel leakage, shell, scalar tail, or M_ext shift",
            role="forbidden boundary patch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as boundary behavior",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents boundary repair tensor",
        ),
        HCurvRequirementEntry(
            name="HC26: Bianchi decorative rejection",
            requirement="H_curv is divergence-safe because it is called geometric / Bianchi-compatible",
            role="forbidden divergence decoration",
            allowed_if="never as proof",
            forbidden_if="accepted as divergence safety",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents fake parent compatibility",
        ),
        HCurvRequirementEntry(
            name="HC27: recovery-fit correction rejection",
            requirement="H_curv chosen to recover gamma_like, AB, exterior matching, or PPN behavior",
            role="forbidden recovery construction",
            allowed_if="never as origin",
            forbidden_if="accepted as H_curv definition",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps recovery downstream",
        ),
        HCurvRequirementEntry(
            name="HC28: H_curv failure",
            requirement="H_curv cannot meet source, divergence, boundary, matter, mass, scalar, and claim-level requirements",
            role="branch failure condition",
            allowed_if="used to keep H_curv deferred or diagnostic-only",
            forbidden_if="patched with decorative tensor language",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="H_curv cannot be inserted into parent equation",
        ),
        HCurvRequirementEntry(
            name="HC29: recommended next move",
            requirement="after H_curv burden is stated, audit H_exch definition requirements",
            role="next local bottleneck",
            allowed_if="H_curv remains theorem target/deferred",
            forbidden_if="jumping to divergence-safety before H_exch burden is stated",
            status="RECOMMENDED",
            missing="H_exch requirements audit",
            consequence="next script should be candidate_H_exch_definition_requirements.py",
        ),
    ]


def print_entry(e: HCurvRequirementEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Requirement: {e.requirement}")
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
    header("Case 0: H_curv definition requirements problem")

    print("Question:")
    print()
    print("  What must H_curv be to be more than an anti-singularity patch?")
    print()
    print("Goal:")
    print()
    print("  state minimum curvature correction tensor burden before H_curv can be used")
    print()
    print("Discipline:")
    print()
    print("  no anti-singularity patch")
    print("  no e_curv source reservoir")
    print("  no undefined J_curv")
    print("  no regular-core tuning")
    print("  no boundary counterterm")
    print("  no Bianchi decoration")
    print("  no ordinary matter rerouting")
    print("  no M_ext shift")
    print("  no scalar trace leak")
    print("  no recovery-fit correction")

    with out.unresolved_obligations():
        out.line("H_curv definition requirements problem posed", StatusMark.OBLIGATION, "requirements audit required before H_curv can be used")


def case_1_inventory(entries: List[HCurvRequirementEntry]):
    header("Case 1: H_curv definition requirements inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[HCurvRequirementEntry], out: ScriptOutput):
    header("Case 2: Compact H_curv requirements ledger")

    print("| Entry | Requirement | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.requirement.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact H_curv requirements ledger produced", StatusMark.INFO, "STRUCTURAL")


def case_3_status_counts(entries: List[HCurvRequirementEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  H_curv is not defined yet.")
    print("  A real H_curv requires curvature admissibility object, domain, measure, source/current relation, projection class, tensor symmetry, divergence behavior, boundary behavior, matter separation, M_ext neutrality, scalar trace neutrality, coefficient origin, and claim-level limits.")
    print("  A_curv remains diagnostic/branch-filter unless dynamics are derived.")
    print("  e_curv remains diagnostic/accounting only.")
    print("  J_curv is not defined and cannot source H_curv.")
    print("  Diagnostic-only H_curv is the safest fallback.")
    print("  Anti-singularity patch, e_curv reservoir, regular-core tuning, boundary counterterm, Bianchi decoration, and recovery-fit correction are rejected.")
    print("  Next gate is H_exch definition requirements.")

    with out.governance_assessments():
        out.line("H_curv requirements status count produced", StatusMark.INFO, "STRUCTURAL")


def case_4_required_fields(out: ScriptOutput):
    header("Case 4: Required H_curv fields")

    print("Required H_curv fields:")
    print()
    print("1. curvature admissibility object")
    print("2. domain")
    print("3. measure")
    print("4. source/current relation")
    print("5. projection class")
    print("6. tensor symmetry / trace behavior")
    print("7. divergence behavior")
    print("8. boundary behavior")
    print("9. ordinary matter separation")
    print("10. M_ext neutrality")
    print("11. scalar trace neutrality")
    print("12. coefficient origin")
    print("13. claim-level limit")

    with out.governance_assessments():
        out.line("required H_curv fields listed", StatusMark.PASS, "RECOMMENDED")


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: H_curv definition decision tree")

    print("Decision tree:")
    print()
    print("1. H_curv has A_curv object, source/current relation, divergence behavior, and neutrality:")
    print("   curvature correction theorem target survives.")
    print()
    print("2. A_curv remains diagnostic only:")
    print("   H_curv remains diagnostic-only or deferred.")
    print()
    print("3. J_curv is required but undefined:")
    print("   H_curv cannot use J_curv.")
    print()
    print("4. e_curv is used as source reservoir:")
    print("   rejected.")
    print()
    print("5. H_curv enforces finite curvature / bounce / regular core:")
    print("   rejected.")
    print()
    print("6. H_curv is divergence-safe by name:")
    print("   rejected.")
    print()
    print("7. H_curv cannot meet requirements:")
    print("   keep deferred or diagnostic-only.")

    with out.governance_assessments():
        out.line("H_curv definition decision tree stated", StatusMark.PASS, "RECOMMENDED")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  H_curv cannot be defined without source/current origin, divergence behavior,")
    print("  boundary neutrality, matter separation, and claim-level control.")
    print()
    print("Consequence:")
    print()
    print("  keep H_curv deferred or diagnostic-only.")
    print("  do not insert it into a parent equation.")
    print()
    print("Bad failure:")
    print()
    print("  call H_curv a curvature correction because the theory wants finite curvature.")

    with out.governance_assessments():
        out.line("H_curv definition good failure stated", StatusMark.DEFER, "DEFERRED_PENDING_PREREQUISITES")


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("H_curv definition fails if:")
    print()
    print("1. A_curv is undefined")
    print("2. diagnostic A_curv is promoted to dynamics")
    print("3. J_curv is used before definition")
    print("4. e_curv becomes source reservoir")
    print("5. domain/measure hide divergence")
    print("6. projection hides overlap")
    print("7. tensor symmetry is unspecified")
    print("8. divergence safety is Bianchi decoration")
    print("9. boundary behavior repairs failure")
    print("10. ordinary matter is rerouted")
    print("11. M_ext shifts")
    print("12. scalar trace leaks")
    print("13. coefficients tune recovery or regular core")
    print("14. bounce/regular core is claimed")

    with out.governance_assessments():
        out.line("H_curv definition failure controls stated", StatusMark.WARN, "RISK")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_H_curv_definition_requirements.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_H_exch_definition_requirements.py")
    print("   Define what H_exch must be to be more than exchange-continuity paint.")
    print()
    print("3. candidate_H_curv_failure_summary.py")
    print("   Use if H_curv cannot meet curvature correction requirements.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_H_exch_definition_requirements.py")
    print()
    print("Reason:")
    print("  H_curv has now been fenced against anti-singularity and e_curv-reservoir overclaim.")
    print("  H_exch must next be fenced against exchange-continuity and Sigma/R paint.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "STRUCTURAL")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("H_curv is not defined yet.")
    print()
    print("It survives only as theorem target / diagnostic-only fallback requiring:")
    print()
    print("  curvature admissibility object")
    print("  domain")
    print("  measure")
    print("  source/current relation")
    print("  projection class")
    print("  tensor symmetry")
    print("  divergence behavior")
    print("  boundary behavior")
    print("  ordinary matter separation")
    print("  M_ext neutrality")
    print("  scalar trace neutrality")
    print("  coefficient origin")
    print("  claim-level limit")
    print()
    print("Rejected:")
    print()
    print("  anti-singularity patch")
    print("  e_curv source reservoir")
    print("  regular-core tuning")
    print("  boundary counterterm")
    print("  Bianchi decoration")
    print("  recovery-fit correction")
    print()
    print("Best next script:")
    print()
    print("  candidate_H_exch_definition_requirements.py")

    with out.governance_assessments():
        out.line("H_curv definition requirements audit complete", StatusMark.PASS, "CLOSED")

    out.print()


def record_governance(ns) -> None:
    # One ProofObligationRecord per REQUIRED entry
    required_obligations = [
        ("derive_A_curv_formal_definition_19", "Formally define A_curv curvature admissibility object",
         "A_curv or equivalent finite-admissibility object must be formally defined before H_curv can use it (HC2)."),
        ("derive_H_curv_domain_19", "Define H_curv domain D_curv",
         "Domain where H_curv acts must be specified, structural, not solution-tailored (HC4)."),
        ("derive_H_curv_measure_19", "Specify curvature/admissibility measure for H_curv",
         "Measure used by H_curv must be defined independently of desired finite result (HC5)."),
        ("derive_H_curv_source_current_relation_19", "Derive H_curv source/current relation",
         "H_curv relation to A_curv, e_curv, or J_curv must be explicit and non-circular (HC6)."),
        ("guard_J_curv_absence_19", "Guard J_curv absence in H_curv",
         "J_curv is not defined and cannot be used as H_curv source/current (HC7)."),
        ("derive_H_curv_projection_class_19", "Specify H_curv projection class",
         "Projection class must be explicit and source-compatible, not hiding overlap (HC9)."),
        ("derive_H_curv_tensor_symmetry_19", "Specify H_curv tensor symmetry and rank",
         "Tensor rank, symmetry, trace behavior, and index placement required (HC10)."),
        ("derive_H_curv_divergence_behavior_19", "Derive H_curv divergence behavior",
         "Divergence behavior must be specified without decorative Bianchi language (HC11)."),
        ("derive_H_curv_boundary_neutrality_19", "Derive H_curv boundary neutrality theorem",
         "H_curv must have no boundary repair flux, shell hiding, scalar tail cancellation, or M_ext shift (HC12)."),
        ("derive_H_curv_matter_separation_19", "Derive H_curv ordinary matter separation",
         "H_curv must not reroute ordinary T_mu_nu or double-count matter (HC13)."),
        ("derive_H_curv_mass_neutrality_19", "Derive H_curv M_ext neutrality theorem",
         "delta M_ext|H_curv = 0 unless derived through established A-sector source law (HC14)."),
        ("derive_H_curv_scalar_neutrality_19", "Derive H_curv scalar trace neutrality",
         "H_curv must not reopen B_s/F_zeta, residual trace, kappa, or exterior scalar charge (HC15)."),
        ("derive_H_curv_coefficient_origin_19", "Derive H_curv coefficient origin",
         "Coefficients must have ontology-native, action, stiffness, or admissibility origin (HC16)."),
    ]

    for obligation_id, title, description in required_obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["H_curv_insertion_route"],
            description=description,
        ))

    all_obligation_ids = [o[0] for o in required_obligations]

    # Candidate routes
    ns.record_route(RouteRecord(
        route_id="H_curv_diagnostic_only_route_19",
        script_id=SCRIPT_ID,
        name="Diagnostic-only H_curv audit object",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "explicitly diagnostic-only",
            "never inserted into field equation",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="H_curv_divergence_free_candidate_route_19",
        script_id=SCRIPT_ID,
        name="Identically divergence-free H_curv candidate",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=all_obligation_ids,
        activation_conditions=[
            "actual tensor identity constructed",
            "not asserted by Bianchi-like language",
        ],
    ))

    # Deferred branch for H_curv insertion
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_H_curv_definition_19",
        script_id=SCRIPT_ID,
        branch_id="H_curv_definition_and_insertion",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=all_obligation_ids,
        description=(
            "H_curv is not defined yet. All thirteen definition requirements are open obligations. "
            "Insertion is deferred until prerequisites are satisfied."
        ),
    ))

    # HC28 BRANCH_KILLED -> DEFERRED_PENDING_PREREQUISITES per governance rule 5
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_H_curv_failure_branch_19",
        script_id=SCRIPT_ID,
        branch_id="H_curv_definition_failure",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=all_obligation_ids,
        description=(
            "HC28 failure condition: if H_curv cannot meet requirements, it remains deferred or diagnostic-only. "
            "Mapped to DEFERRED_PENDING_PREREQUISITES because no contradiction has been demonstrated — "
            "the thirteen prerequisites are simply open."
        ),
    ))

    # Rejected routes
    for decision_id, branch_id, description in [
        ("reject_H_curv_finite_curvature_19", "H_curv_arbitrary_finite_curvature", "HC22: any tensor that makes curvature finite is rejected by policy."),
        ("reject_H_curv_ecurv_reservoir_19", "H_curv_ecurv_source_reservoir", "HC23: e_curv as source reservoir rejected by policy."),
        ("reject_H_curv_regular_core_tuning_19", "H_curv_regular_core_tuning", "HC24: regular-core tuning rejected by policy."),
        ("reject_H_curv_boundary_counterterm_19", "H_curv_boundary_counterterm", "HC25: boundary counterterm rejected by policy."),
        ("reject_H_curv_Bianchi_decorative_19", "H_curv_Bianchi_decorative", "HC26: Bianchi-like language is not proof."),
        ("reject_H_curv_recovery_fit_19", "H_curv_recovery_fit_correction", "HC27: recovery-fit correction rejected by policy."),
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=decision_id,
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            description=description,
        ))

    # Summary claim
    ns.record_claim(ClaimRecord(
        claim_id="H_curv_not_defined_yet_19",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.NOT_INSERTABLE_YET,
        statement=(
            "H_curv is not defined yet and is not insertable. "
            "It survives only as theorem target or diagnostic-only fallback."
        ),
        obligation_ids=all_obligation_ids,
    ))


def main():
    header("Candidate H_curv Definition Requirements")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_required_fields(out)
    case_5_decision_tree(out)
    case_6_good_failure(out)
    case_7_failure_controls(out)
    case_8_next_tests(out)
    final_interpretation(out)

    with archive:
        record_governance(ns)
        ns.record_derivation(
            derivation_id="H_curv_definition_requirements_marker",
            inputs=[],
            output=sp.Symbol("H_curv_definition_requirements_complete"),
            method="H_curv_definition_requirements",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
