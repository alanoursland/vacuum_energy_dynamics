# Candidate H_exch definition requirements
#
# Group:
#   19_parent_correction_tensor_audit
#
# Script type:
#   REQUIREMENTS
#
# Purpose
# -------
# The H_curv definition requirements audit found:
#
#   H_curv is not defined yet.
#
# It survives only as theorem target / diagnostic-only fallback requiring:
#
#   curvature admissibility object,
#   domain,
#   measure,
#   source/current relation,
#   projection class,
#   tensor symmetry,
#   divergence behavior,
#   boundary behavior,
#   ordinary matter separation,
#   M_ext neutrality,
#   scalar trace neutrality,
#   coefficient origin,
#   claim-level limit.
#
# Rejected:
#
#   anti-singularity patch,
#   e_curv source reservoir,
#   regular-core tuning,
#   boundary counterterm,
#   Bianchi decoration,
#   recovery-fit correction.
#
# This script fences H_exch before any exchange correction tensor is used.
#
# Locked-door question:
#
#   What must H_exch be to be more than exchange-continuity paint?
#
# This is a requirements audit, not an exchange correction tensor derivation.


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
class HExchRequirementEntry:
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
        dependency_id="H_curv_definition_requirements_marker",
        upstream_script_id="019_parent_correction_tensor_audit__candidate_H_curv_definition_requirements",
        upstream_derivation_id="H_curv_definition_requirements_marker",
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


def build_entries() -> List[HExchRequirementEntry]:
    return [
        HExchRequirementEntry(
            name="HE1: H_exch definition target",
            requirement="H_exch has J_V/J_exch definition, Sigma/R operators, source/relaxation distinction, domain, orientation, projection class, tensor symmetry, divergence behavior, boundary behavior, ordinary matter decoupling, M_ext neutrality, and scalar trace neutrality",
            role="core exchange correction theorem target",
            allowed_if="all requirements are explicit before H_exch is inserted",
            forbidden_if="H_exch is named as exchange correction without current/source structure",
            status="THEOREM_TARGET",
            missing="actual H_exch definition",
            consequence="decides whether exchange correction tensor language can become technical",
        ),
        HExchRequirementEntry(
            name="HE2: J_V absence guard",
            requirement="J_V remains unresolved and cannot be used as H_exch source/current",
            role="vacuum current absence guard",
            allowed_if="H_exch remains deferred or independent of J_V",
            forbidden_if="H_exch imports J_V by name",
            status="REQUIRED",
            missing="J_V definition",
            consequence="preserves Group 18 vacuum-current result",
        ),
        HExchRequirementEntry(
            name="HE3: J_exch theorem-target guard",
            requirement="J_exch remains active-exchange theorem target only",
            role="exchange-current guard",
            allowed_if="H_exch does not promote role-level J_exch to operator",
            forbidden_if="H_exch treats J_exch as physical current before definition",
            status="REQUIRED",
            missing="J_exch definition",
            consequence="prevents exchange-current hardening by tensor name",
        ),
        HExchRequirementEntry(
            name="HE4: Sigma/R operator requirement",
            requirement="Sigma_exch and R_exch are defined as operators before H_exch uses them",
            role="source/relaxation prerequisite",
            allowed_if="source and relaxation are independently defined",
            forbidden_if="H_exch defines Sigma/R by making balance work",
            status="REQUIRED",
            missing="Sigma_exch / R_exch operators",
            consequence="prevents exchange-continuity paint",
        ),
        HExchRequirementEntry(
            name="HE5: source/relaxation distinction requirement",
            requirement="Sigma_exch and R_exch are not two names for one hidden tuning mechanism",
            role="double-counting guard",
            allowed_if="source and relaxation have distinct origins and strength laws",
            forbidden_if="Sigma/R are adjusted to cancel divergence, boundary leakage, or recovery mismatch",
            status="REQUIRED",
            missing="Sigma/R separation and strength laws",
            consequence="prevents exchange tuning tensor",
        ),
        HExchRequirementEntry(
            name="HE6: ordinary-sector source-side absence guard",
            requirement="no active ordinary-sector source side for J_exch is derived",
            role="ordinary-sector safety guard",
            allowed_if="H_exch remains inactive/role-level in ordinary sector",
            forbidden_if="H_exch invents ordinary exchange source",
            status="REQUIRED",
            missing="ordinary-sector exchange source theorem",
            consequence="preserves zero-net / zero-creation ordinary branches",
        ),
        HExchRequirementEntry(
            name="HE7: domain requirement",
            requirement="domain D_exch/H_exch where correction acts is specified",
            role="definition prerequisite",
            allowed_if="domain follows from source/current structure",
            forbidden_if="domain is chosen to hide leakage, mass shift, or scalar charge",
            status="REQUIRED",
            missing="exchange correction domain",
            consequence="prevents convenient exchange-support tensor",
        ),
        HExchRequirementEntry(
            name="HE8: orientation / flux behavior requirement",
            requirement="H_exch relation to exchange flux direction or transport behavior is specified",
            role="orientation prerequisite",
            allowed_if="orientation follows from defined current/source law",
            forbidden_if="orientation is chosen to cancel boundary or recovery failure",
            status="REQUIRED",
            missing="exchange orientation / flux law",
            consequence="prevents repair-current tensor",
        ),
        HExchRequirementEntry(
            name="HE9: projection class requirement",
            requirement="H_exch projection class is specified: spacetime tensor, spatial tensor, projected exchange-sector tensor, or diagnostic-only object",
            role="covariance/projection guard",
            allowed_if="projection class is explicit and source-compatible",
            forbidden_if="projection hides overlap with matter, metric, or residual sectors",
            status="REQUIRED",
            missing="projection class / projector",
            consequence="prevents fake covariant-enough exchange tensor",
        ),
        HExchRequirementEntry(
            name="HE10: tensor symmetry requirement",
            requirement="H_exch tensor rank, symmetry, trace behavior, and index placement are specified",
            role="tensor well-posedness guard",
            allowed_if="symmetry follows from insertion target",
            forbidden_if="symbol H_exch is used with no tensor type",
            status="REQUIRED",
            missing="tensor type / symmetry",
            consequence="prevents decorative tensor symbol",
        ),
        HExchRequirementEntry(
            name="HE11: divergence behavior requirement",
            requirement="H_exch divergence behavior is specified without decorative continuity or Bianchi language",
            role="divergence-safety prerequisite",
            allowed_if="divergence identity or source-balanced partner is real",
            forbidden_if="divergence safety is asserted because H_exch closes exchange",
            status="REQUIRED",
            missing="divergence identity or source partner",
            consequence="prevents fake parent compatibility",
        ),
        HExchRequirementEntry(
            name="HE12: boundary behavior requirement",
            requirement="H_exch has no boundary repair flux, shell hiding, scalar tail cancellation, or M_ext shift",
            role="boundary neutrality guard",
            allowed_if="boundary behavior is structural and neutral",
            forbidden_if="H_exch repairs boundary leakage or exchange failure",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="protects exterior sector",
        ),
        HExchRequirementEntry(
            name="HE13: ordinary matter decoupling requirement",
            requirement="H_exch does not reroute ordinary T_mu_nu, ordinary rho, or scalar charge",
            role="matter separation guard",
            allowed_if="ordinary matter remains routed to A-sector unless theorem derives otherwise",
            forbidden_if="H_exch hides ordinary matter in exchange correction side",
            status="REQUIRED",
            missing="ordinary matter decoupling theorem",
            consequence="protects ordinary matter coupling",
        ),
        HExchRequirementEntry(
            name="HE14: M_ext neutrality requirement",
            requirement="delta M_ext|H_exch = 0 unless derived through established A-sector source law",
            role="mass neutrality guard",
            allowed_if="H_exch is exterior-mass-neutral by theorem",
            forbidden_if="H_exch changes measured exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        HExchRequirementEntry(
            name="HE15: scalar trace neutrality requirement",
            requirement="H_exch does not reopen B_s/F_zeta, residual trace, kappa, or exterior scalar charge",
            role="metric scalar guard",
            allowed_if="scalar/no-overlap guardrails remain closed",
            forbidden_if="H_exch becomes hidden scalar channel",
            status="REQUIRED",
            missing="scalar trace neutrality / no-overlap theorem",
            consequence="preserves Group 16 guardrails",
        ),
        HExchRequirementEntry(
            name="HE16: coefficient origin requirement",
            requirement="H_exch coefficients have ontology-native, action, stiffness, or exchange-source origin",
            role="coefficient tuning guard",
            allowed_if="coefficients are derived before recovery and boundary tests",
            forbidden_if="coefficients are chosen for exchange closure, exterior match, or recovery",
            status="REQUIRED",
            missing="coefficient origin",
            consequence="prevents exchange-continuity tuning",
        ),
        HExchRequirementEntry(
            name="HE17: zero-net / zero-creation preservation requirement",
            requirement="H_exch preserves ordinary-sector zero-net exchange and zero-creation branches unless source theorem derives otherwise",
            role="ordinary-sector neutral branch guard",
            allowed_if="ordinary sector remains inactive, balanced, or latent",
            forbidden_if="H_exch reintroduces net ordinary exchange by tensor insertion",
            status="REQUIRED",
            missing="ordinary-sector exchange neutrality theorem",
            consequence="preserves Group 18 safest branches",
        ),
        HExchRequirementEntry(
            name="HE18: dark-sector no-patch guard",
            requirement="H_exch does not use dark-sector coupling as ordinary-sector patch",
            role="dark-sector guard",
            allowed_if="dark branch remains absent/deferred or separately sourced",
            forbidden_if="H_exch invokes dark coupling to repair ordinary source failure",
            status="REQUIRED",
            missing="dark source separation if reopened",
            consequence="preserves no-dark-patch result",
        ),
        HExchRequirementEntry(
            name="HE19: diagnostic-only H_exch branch",
            requirement="H_exch-like object used only as diagnostic audit and never inserted into field equation",
            role="safe fallback branch",
            allowed_if="explicitly diagnostic-only",
            forbidden_if="diagnostic H_exch becomes correction tensor term",
            status="SAFE_IF",
            missing="none if kept diagnostic",
            consequence="allows exchange correction audits without parent insertion",
        ),
        HExchRequirementEntry(
            name="HE20: identically divergence-free H_exch candidate",
            requirement="H_exch divergence vanishes by constructed identity",
            role="future tensor class candidate",
            allowed_if="identity is mathematically real and not repair",
            forbidden_if="identity is asserted by Bianchi-like language",
            status="CANDIDATE",
            missing="actual tensor identity",
            consequence="possible future divergence-safe route if constructed",
        ),
        HExchRequirementEntry(
            name="HE21: source-balanced H_exch candidate",
            requirement="divergence of H_exch balances independently defined exchange source/relaxation side",
            role="future source-balance candidate",
            allowed_if="exchange source and relaxation sides exist before H_exch",
            forbidden_if="H_exch and Sigma/R define each other",
            status="CANDIDATE",
            missing="exchange source/relaxation side",
            consequence="possible future route if source partner is real",
        ),
        HExchRequirementEntry(
            name="HE22: projected H_exch candidate",
            requirement="H_exch lives in defined exchange/current projector subspace",
            role="future projection candidate",
            allowed_if="projector and sector split are defined",
            forbidden_if="projection hides matter, metric, or residual overlap",
            status="CANDIDATE",
            missing="projector / sector split",
            consequence="possible route to no-overlap if projector is real",
        ),
        HExchRequirementEntry(
            name="HE23: exchange-continuity paint rejection",
            requirement="H_exch is whatever makes nabla_mu J_exch^mu = Sigma_exch - R_exch work",
            role="forbidden exchange paint",
            allowed_if="never as definition",
            forbidden_if="accepted as H_exch",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents decorative exchange closure",
        ),
        HExchRequirementEntry(
            name="HE24: Sigma/R tuning tensor rejection",
            requirement="H_exch uses Sigma/R as coefficient knobs or cancellation terms",
            role="forbidden source tuning branch",
            allowed_if="never as construction",
            forbidden_if="accepted as exchange correction",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents hidden tuning mechanism",
        ),
        HExchRequirementEntry(
            name="HE25: boundary repair tensor rejection",
            requirement="H_exch cancels boundary leakage, shell source, scalar tail, or M_ext shift",
            role="forbidden boundary patch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as boundary behavior",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents boundary repair tensor",
        ),
        HExchRequirementEntry(
            name="HE26: ordinary matter rerouting rejection",
            requirement="H_exch reroutes ordinary matter to fix exchange, curvature, or boundary behavior",
            role="forbidden matter repair branch",
            allowed_if="never without source theorem",
            forbidden_if="accepted as exchange correction",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves ordinary matter decoupling",
        ),
        HExchRequirementEntry(
            name="HE27: dark-sector patch rejection",
            requirement="H_exch invokes dark sector to patch ordinary exchange-source failure",
            role="forbidden dark patch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as exchange correction source",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves optional/deferred dark-sector status",
        ),
        HExchRequirementEntry(
            name="HE28: recovery-fit correction rejection",
            requirement="H_exch chosen to recover gamma_like, AB, exterior matching, or PPN behavior",
            role="forbidden recovery construction",
            allowed_if="never as origin",
            forbidden_if="accepted as H_exch definition",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps recovery downstream",
        ),
        HExchRequirementEntry(
            name="HE29: H_exch failure",
            requirement="H_exch cannot meet current, source, divergence, boundary, matter, mass, scalar, and zero-net requirements",
            role="branch failure condition",
            allowed_if="used to keep H_exch deferred or diagnostic-only",
            forbidden_if="patched with decorative tensor language",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="H_exch cannot be inserted into parent equation",
        ),
        HExchRequirementEntry(
            name="HE30: recommended next move",
            requirement="after H_curv and H_exch burdens are stated, audit correction tensor divergence safety",
            role="next local bottleneck",
            allowed_if="H_exch remains theorem target/deferred",
            forbidden_if="jumping to insertability before divergence meaning is audited",
            status="RECOMMENDED",
            missing="divergence-safety audit",
            consequence="next script should be candidate_correction_tensor_divergence_safety.py",
        ),
    ]


def print_entry(e: HExchRequirementEntry) -> None:
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
        out.line(e.name, StatusMark(e.status) if e.status in StatusMark._value2member_map_ else StatusMark.INFO, e.status)

    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: H_exch definition requirements problem")

    print("Question:")
    print()
    print("  What must H_exch be to be more than exchange-continuity paint?")
    print()
    print("Goal:")
    print()
    print("  state minimum exchange correction tensor burden before H_exch can be used")
    print()
    print("Discipline:")
    print()
    print("  no exchange-continuity paint")
    print("  no undefined J_V/J_exch")
    print("  no undefined Sigma/R")
    print("  no Sigma/R tuning")
    print("  no boundary repair")
    print("  no ordinary matter rerouting")
    print("  no M_ext shift")
    print("  no scalar trace leak")
    print("  no dark-sector patch")
    print("  no recovery-fit correction")

    with out.unresolved_obligations():
        out.line("H_exch definition requirements problem posed", StatusMark.OBLIGATION, "requirements audit required before H_exch can be used")


def case_1_inventory(entries: List[HExchRequirementEntry]):
    header("Case 1: H_exch definition requirements inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[HExchRequirementEntry], out: ScriptOutput):
    header("Case 2: Compact H_exch requirements ledger")

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
        out.line("compact H_exch requirements ledger produced", StatusMark.INFO, "STRUCTURAL")


def case_3_status_counts(entries: List[HExchRequirementEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  H_exch is not defined yet.")
    print("  A real H_exch requires real current/source structure: J_V or J_exch, Sigma/R operators, source/relaxation distinction, domain, orientation, projection class, tensor symmetry, divergence behavior, boundary behavior, ordinary matter decoupling, M_ext neutrality, scalar trace neutrality, and coefficient origin.")
    print("  J_V remains unresolved.")
    print("  J_exch remains theorem target only.")
    print("  Sigma/R remain role-level only.")
    print("  No active ordinary-sector source side for J_exch is derived.")
    print("  Diagnostic-only H_exch is the safest fallback.")
    print("  Exchange-continuity paint, Sigma/R tuning, boundary repair, matter rerouting, dark patch, and recovery-fit correction are rejected.")
    print("  Next gate is correction tensor divergence safety.")

    with out.governance_assessments():
        out.line("H_exch requirements status count produced", StatusMark.INFO, "STRUCTURAL")


def case_4_required_fields(out: ScriptOutput):
    header("Case 4: Required H_exch fields")

    print("Required H_exch fields:")
    print()
    print("1. J_V or J_exch definition")
    print("2. Sigma/R operators")
    print("3. source/relaxation distinction")
    print("4. ordinary-sector source-side status")
    print("5. domain")
    print("6. orientation / flux behavior")
    print("7. projection class")
    print("8. tensor symmetry / trace behavior")
    print("9. divergence behavior")
    print("10. boundary behavior")
    print("11. ordinary matter decoupling")
    print("12. M_ext neutrality")
    print("13. scalar trace neutrality")
    print("14. coefficient origin")
    print("15. zero-net / zero-creation preservation")
    print("16. dark-sector no-patch guard")

    with out.governance_assessments():
        out.line("required H_exch fields listed", StatusMark.PASS, "RECOMMENDED")


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: H_exch definition decision tree")

    print("Decision tree:")
    print()
    print("1. H_exch has J/source/relaxation, divergence behavior, and neutrality:")
    print("   exchange correction theorem target survives.")
    print()
    print("2. J_V remains unresolved:")
    print("   H_exch cannot use J_V.")
    print()
    print("3. J_exch remains theorem target only:")
    print("   H_exch cannot use J_exch as operator.")
    print()
    print("4. Sigma/R remain role-level:")
    print("   H_exch remains diagnostic-only or deferred.")
    print()
    print("5. H_exch makes exchange continuity work:")
    print("   rejected as paint.")
    print()
    print("6. H_exch reroutes matter, shifts mass, leaks scalar, or patches dark:")
    print("   rejected.")
    print()
    print("7. H_exch cannot meet requirements:")
    print("   keep deferred or diagnostic-only.")

    with out.governance_assessments():
        out.line("H_exch definition decision tree stated", StatusMark.PASS, "RECOMMENDED")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  H_exch cannot be defined without current/source origin, divergence behavior,")
    print("  boundary neutrality, matter decoupling, and zero-net ordinary-sector control.")
    print()
    print("Consequence:")
    print()
    print("  keep H_exch deferred or diagnostic-only.")
    print("  do not insert it into a parent equation.")
    print()
    print("Bad failure:")
    print()
    print("  call H_exch an exchange correction because exchange continuity needs a tensor.")

    with out.governance_assessments():
        out.line("H_exch definition good failure stated", StatusMark.DEFER, "DEFERRED_PENDING_PREREQUISITES")


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("H_exch definition fails if:")
    print()
    print("1. J_V is used before definition")
    print("2. J_exch is promoted from theorem target to operator")
    print("3. Sigma/R are undefined")
    print("4. Sigma/R become tuning knobs")
    print("5. ordinary-sector source side is invented")
    print("6. domain/orientation hide leakage")
    print("7. projection hides overlap")
    print("8. tensor symmetry is unspecified")
    print("9. divergence safety is exchange-continuity paint")
    print("10. boundary behavior repairs failure")
    print("11. ordinary matter is rerouted")
    print("12. M_ext shifts")
    print("13. scalar trace leaks")
    print("14. dark sector patches ordinary failure")
    print("15. coefficients tune recovery or exchange closure")

    with out.governance_assessments():
        out.line("H_exch definition failure controls stated", StatusMark.WARN, "RISK")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_H_exch_definition_requirements.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_correction_tensor_divergence_safety.py")
    print("   Audit what divergence-safe means without being decorative.")
    print()
    print("3. candidate_H_exch_failure_summary.py")
    print("   Use if H_exch cannot meet exchange correction requirements.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_correction_tensor_divergence_safety.py")
    print()
    print("Reason:")
    print("  H_curv and H_exch have now both been burdened.")
    print("  The next shared bottleneck is what divergence-safe actually means without decoration.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "STRUCTURAL")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("H_exch is not defined yet.")
    print()
    print("It survives only as theorem target / diagnostic-only fallback requiring:")
    print()
    print("  J_V or J_exch definition")
    print("  Sigma/R operators")
    print("  source/relaxation distinction")
    print("  domain")
    print("  orientation / flux behavior")
    print("  projection class")
    print("  tensor symmetry")
    print("  divergence behavior")
    print("  boundary behavior")
    print("  ordinary matter decoupling")
    print("  M_ext neutrality")
    print("  scalar trace neutrality")
    print("  coefficient origin")
    print("  zero-net / zero-creation preservation")
    print()
    print("Rejected:")
    print()
    print("  exchange-continuity paint")
    print("  Sigma/R tuning tensor")
    print("  boundary repair tensor")
    print("  ordinary matter rerouting")
    print("  dark-sector patch")
    print("  recovery-fit correction")
    print()
    print("Best next script:")
    print()
    print("  candidate_correction_tensor_divergence_safety.py")

    with out.governance_assessments():
        out.line("H_exch definition requirements audit complete", StatusMark.PASS, "CLOSED")



def record_governance(ns) -> None:
    required_obligations = [
        ("guard_J_V_absence_H_exch_19", "Guard J_V absence in H_exch",
         "J_V remains unresolved and cannot be used as H_exch source/current (HE2)."),
        ("guard_J_exch_theorem_target_H_exch_19", "Guard J_exch theorem-target status in H_exch",
         "J_exch remains active-exchange theorem target only; H_exch must not promote it (HE3)."),
        ("derive_Sigma_R_operators_H_exch_19", "Derive Sigma_exch and R_exch operators",
         "Sigma_exch and R_exch must be defined as operators before H_exch uses them (HE4)."),
        ("derive_Sigma_R_distinction_H_exch_19", "Derive Sigma/R source/relaxation distinction",
         "Sigma_exch and R_exch must have distinct origins and strength laws, not be tuning knobs (HE5)."),
        ("guard_ordinary_sector_source_side_H_exch_19", "Guard ordinary-sector source-side absence",
         "No active ordinary-sector source side for J_exch is derived; H_exch must not invent one (HE6)."),
        ("derive_H_exch_domain_19", "Define H_exch domain D_exch",
         "Domain where H_exch acts must be specified and follow from source/current structure (HE7)."),
        ("derive_H_exch_orientation_19", "Specify H_exch orientation/flux behavior",
         "H_exch relation to exchange flux direction must be specified (HE8)."),
        ("derive_H_exch_projection_class_19", "Specify H_exch projection class",
         "Projection class must be explicit and source-compatible (HE9)."),
        ("derive_H_exch_tensor_symmetry_19", "Specify H_exch tensor symmetry and rank",
         "Tensor rank, symmetry, trace behavior, and index placement required (HE10)."),
        ("derive_H_exch_divergence_behavior_19", "Derive H_exch divergence behavior",
         "Divergence behavior must be specified without decorative continuity or Bianchi language (HE11)."),
        ("derive_H_exch_boundary_neutrality_19", "Derive H_exch boundary neutrality theorem",
         "H_exch must have no boundary repair flux, shell hiding, scalar tail cancellation, or M_ext shift (HE12)."),
        ("derive_H_exch_matter_decoupling_19", "Derive H_exch ordinary matter decoupling",
         "H_exch must not reroute ordinary T_mu_nu, ordinary rho, or scalar charge (HE13)."),
        ("derive_H_exch_mass_neutrality_19", "Derive H_exch M_ext neutrality theorem",
         "delta M_ext|H_exch = 0 unless derived through established A-sector source law (HE14)."),
        ("derive_H_exch_scalar_neutrality_19", "Derive H_exch scalar trace neutrality",
         "H_exch must not reopen B_s/F_zeta, residual trace, kappa, or exterior scalar charge (HE15)."),
        ("derive_H_exch_coefficient_origin_19", "Derive H_exch coefficient origin",
         "Coefficients must have ontology-native, action, stiffness, or exchange-source origin (HE16)."),
        ("derive_H_exch_zero_net_preservation_19", "Derive H_exch zero-net/zero-creation preservation",
         "H_exch must preserve ordinary-sector zero-net exchange and zero-creation branches (HE17)."),
        ("guard_H_exch_no_dark_patch_19", "Guard H_exch dark-sector no-patch rule",
         "H_exch must not use dark-sector coupling as ordinary-sector patch (HE18)."),
    ]

    for obligation_id, title, description in required_obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["H_exch_insertion_route"],
            description=description,
        ))

    all_obligation_ids = [o[0] for o in required_obligations]

    # Candidate routes
    ns.record_route(RouteRecord(
        route_id="H_exch_diagnostic_only_route_19",
        script_id=SCRIPT_ID,
        name="Diagnostic-only H_exch audit object",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "explicitly diagnostic-only",
            "never inserted into field equation",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="H_exch_source_balanced_candidate_route_19",
        script_id=SCRIPT_ID,
        name="Source-balanced H_exch candidate",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=all_obligation_ids,
        activation_conditions=[
            "exchange source and relaxation sides exist before H_exch",
            "Sigma/R are not defined by H_exch",
        ],
    ))

    # Deferred branch for H_exch
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_H_exch_definition_19",
        script_id=SCRIPT_ID,
        branch_id="H_exch_definition_and_insertion",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=all_obligation_ids,
        description=(
            "H_exch is not defined yet. All seventeen definition requirements are open obligations. "
            "Insertion is deferred until prerequisites are satisfied."
        ),
    ))

    # HE29 BRANCH_KILLED -> DEFERRED_PENDING_PREREQUISITES per governance rule 5
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_H_exch_failure_branch_19",
        script_id=SCRIPT_ID,
        branch_id="H_exch_definition_failure",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=all_obligation_ids,
        description=(
            "HE29 failure condition: if H_exch cannot meet requirements, it remains deferred or diagnostic-only. "
            "Mapped to DEFERRED_PENDING_PREREQUISITES because no contradiction has been demonstrated — "
            "the seventeen prerequisites are simply open."
        ),
    ))

    # Rejected routes
    for decision_id, branch_id, description in [
        ("reject_H_exch_exchange_continuity_paint_19", "H_exch_exchange_continuity_paint", "HE23: exchange-continuity paint rejected by policy."),
        ("reject_H_exch_sigma_r_tuning_19", "H_exch_sigma_r_tuning_tensor", "HE24: Sigma/R tuning tensor rejected by policy."),
        ("reject_H_exch_boundary_repair_19", "H_exch_boundary_repair_tensor", "HE25: boundary repair tensor rejected by policy."),
        ("reject_H_exch_ordinary_matter_rerouting_19", "H_exch_ordinary_matter_rerouting", "HE26: ordinary matter rerouting rejected by policy."),
        ("reject_H_exch_dark_patch_19", "H_exch_dark_sector_patch", "HE27: dark-sector patch rejected by policy."),
        ("reject_H_exch_recovery_fit_19", "H_exch_recovery_fit_correction", "HE28: recovery-fit correction rejected by policy."),
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
        claim_id="H_exch_not_defined_yet_19",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.NOT_INSERTABLE_YET,
        statement=(
            "H_exch is not defined yet and is not insertable. "
            "It survives only as theorem target or diagnostic-only fallback."
        ),
        obligation_ids=all_obligation_ids,
    ))


def main():
    header("Candidate H_exch Definition Requirements")
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

    record_governance(ns)
    ns.record_derivation(
        derivation_id="H_exch_definition_requirements_marker",
        inputs=[],
        output=sp.Symbol("H_exch_definition_requirements_complete"),
        method="H_exch_definition_requirements",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
