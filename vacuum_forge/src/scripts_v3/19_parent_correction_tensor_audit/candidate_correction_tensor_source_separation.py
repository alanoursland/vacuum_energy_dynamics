# Candidate correction tensor source separation
#
# Group:
#   19_parent_correction_tensor_audit
#
# Script type:
#   AUDIT
#
# Purpose
# -------
# The correction tensor divergence-safety audit found:
#
#   Divergence-safe requires one of:
#
#     constructed identity,
#     independently defined source-balance partner,
#     defined projection / constraint propagation,
#     diagnostic-only status.
#
# Rejected:
#
#   Bianchi-like language,
#   decorative tensor closure,
#   recovery-chosen divergence,
#   leakage-canceling divergence,
#   source-by-divergence,
#   dark-patch divergence.
#
# H_curv and H_exch cannot yet pass divergence safety through their missing current/source objects.
#
# This script audits whether correction tensors avoid double-counting ordinary matter and vacuum sources.
#
# Locked-door question:
#
#   Can correction tensors avoid double-counting ordinary matter and vacuum sources?
#
# This is a source-separation audit, not a source law derivation.


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
class SourceSeparationEntry:
    name: str
    rule: str
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
        dependency_id="correction_tensor_divergence_safety_marker",
        upstream_script_id="19_parent_correction_tensor_audit__candidate_correction_tensor_divergence_safety",
        upstream_derivation_id="correction_tensor_divergence_safety_marker",
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


def build_entries() -> List[SourceSeparationEntry]:
    return [
        SourceSeparationEntry(
            name="SS1: source-separation target",
            rule="correction tensors must not double-count ordinary matter, curvature accounting, exchange sources, metric insertion, residual trace, dark sector, or boundary sources",
            role="core source-separation theorem target",
            allowed_if="each source sector is independently routed before correction tensor insertion",
            forbidden_if="H_curv/H_exch hide source overlap or repair missing source laws",
            status="THEOREM_TARGET",
            missing="source-separation theorem",
            consequence="decides whether correction tensors can enter parent equation without double-counting",
        ),
        SourceSeparationEntry(
            name="SS2: ordinary matter routing",
            rule="ordinary T_mu_nu / rho / scalar charge remains routed through established ordinary source side",
            role="ordinary matter guard",
            allowed_if="ordinary matter source does not appear again inside H_curv/H_exch",
            forbidden_if="ordinary matter is counted as both source and correction tensor content",
            status="REQUIRED",
            missing="ordinary matter source-separation theorem",
            consequence="protects ordinary matter coupling and A-sector mass result",
        ),
        SourceSeparationEntry(
            name="SS3: A-sector mass protection",
            rule="A-sector mass result is not modified by correction tensor source accounting",
            role="mass-source guard",
            allowed_if="any mass effect is derived through established A-sector law",
            forbidden_if="H_curv/H_exch shift M_ext or redefine source mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced reconstruction result",
        ),
        SourceSeparationEntry(
            name="SS4: e_curv not source reservoir",
            rule="e_curv remains diagnostic/accounting and is not placed inside H_curv as stress/source reservoir",
            role="curvature energy guard",
            allowed_if="e_curv is used only diagnostically",
            forbidden_if="e_curv supplies bounce money, regular-core tuning, pressure, or H_curv coefficients",
            status="REQUIRED",
            missing="source law if e_curv is promoted",
            consequence="preserves Group 17 closure",
        ),
        SourceSeparationEntry(
            name="SS5: A_curv diagnostic limit",
            rule="A_curv remains diagnostic/branch-filter unless dynamics are derived",
            role="curvature admissibility guard",
            allowed_if="H_curv does not promote A_curv into active source",
            forbidden_if="finite-admissibility failure becomes H_curv source by repair",
            status="REQUIRED",
            missing="A_curv dynamics/source theorem",
            consequence="prevents anti-singularity source smuggling",
        ),
        SourceSeparationEntry(
            name="SS6: J_curv absence",
            rule="J_curv is not defined and cannot be counted as source/current for H_curv",
            role="curvature current guard",
            allowed_if="H_curv remains independent of J_curv or deferred",
            forbidden_if="H_curv uses J_curv by name",
            status="REQUIRED",
            missing="J_curv definition",
            consequence="preserves curvature-current unresolved status",
        ),
        SourceSeparationEntry(
            name="SS7: Sigma/R not tuning knobs",
            rule="Sigma/R are not coefficients, cancellation knobs, or hidden tuning terms inside H_exch",
            role="exchange source guard",
            allowed_if="Sigma/R operators and strength laws are independent",
            forbidden_if="H_exch adjusts Sigma/R to close divergence or recovery",
            status="REQUIRED",
            missing="Sigma/R operators and distinction theorem",
            consequence="prevents exchange source double-counting",
        ),
        SourceSeparationEntry(
            name="SS8: J_V/J_exch unresolved guard",
            rule="J_V and J_exch are not defined enough to source H_exch",
            role="vacuum current guard",
            allowed_if="H_exch remains diagnostic/deferred until currents are real",
            forbidden_if="H_exch imports current content from role labels",
            status="REQUIRED",
            missing="J_V/J_exch definitions",
            consequence="preserves Group 18 role-level split",
        ),
        SourceSeparationEntry(
            name="SS9: J_sub/J_exch not ordinary matter channels",
            rule="J_sub and J_exch do not become ordinary matter coupling channels through correction tensors",
            role="ordinary-sector current guard",
            allowed_if="ordinary matter decoupling remains intact",
            forbidden_if="H_exch reroutes matter through J_sub/J_exch",
            status="REQUIRED",
            missing="ordinary matter decoupling theorem",
            consequence="prevents current split from becoming source overlap",
        ),
        SourceSeparationEntry(
            name="SS10: dark sector not ordinary relabel",
            rule="dark-sector source is absent/deferred and cannot relabel ordinary matter or ordinary exchange failure",
            role="dark source guard",
            allowed_if="dark branch remains optional and separated",
            forbidden_if="H_exch/H_curv uses dark sector to patch ordinary failure",
            status="REQUIRED",
            missing="dark source separation if reopened",
            consequence="preserves no-dark-patch rule",
        ),
        SourceSeparationEntry(
            name="SS11: zeta/B_s insertion not reopened",
            rule="correction tensors do not reopen B_s/F_zeta insertion or residual metric trace",
            role="metric insertion guard",
            allowed_if="B_s/F_zeta and O no-overlap are solved before tensor coupling",
            forbidden_if="H_metric_insert or H_exch restores scalar trace by correction",
            status="REQUIRED",
            missing="B_s/F_zeta insertion and O no-overlap theorem",
            consequence="preserves Group 16 guardrails",
        ),
        SourceSeparationEntry(
            name="SS12: residual killed/non-metric unless O derived",
            rule="residual zeta/kappa trace remains killed or non-metric unless no-overlap operator is derived",
            role="residual source guard",
            allowed_if="residual sector does not source correction tensor",
            forbidden_if="H_residual revives killed residual trace",
            status="REQUIRED",
            missing="O no-overlap or residual-kill derivation",
            consequence="prevents hidden scalar source restoration",
        ),
        SourceSeparationEntry(
            name="SS13: boundary source not counted as tensor correction",
            rule="boundary leakage, shell source, scalar tail, or mass shift cannot be reclassified as H source",
            role="boundary source guard",
            allowed_if="boundary source is structural and neutral before correction tensor",
            forbidden_if="boundary failure becomes H_curv/H_exch source",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="prevents boundary repair as source separation",
        ),
        SourceSeparationEntry(
            name="SS14: coefficient source separation",
            rule="correction tensor coefficients are not fitted from overlapping source sectors",
            role="coefficient origin guard",
            allowed_if="coefficients have single, derived origin",
            forbidden_if="coefficients absorb matter/exchange/curvature overlap or recovery mismatch",
            status="REQUIRED",
            missing="coefficient origin theorem",
            consequence="prevents coefficient-level double-counting",
        ),
        SourceSeparationEntry(
            name="SS15: projected source separation candidate",
            rule="defined projectors separate ordinary, curvature, exchange, residual, and dark sectors",
            role="future candidate route",
            allowed_if="projectors are real and do not hide overlap",
            forbidden_if="projector is invented after source collision appears",
            status="CANDIDATE",
            missing="projector / sector split theorem",
            consequence="possible future no-double-counting route",
        ),
        SourceSeparationEntry(
            name="SS16: diagnostic-only separation fallback",
            rule="H-like objects remain diagnostic-only and therefore do not source or double-count",
            role="safe fallback",
            allowed_if="not inserted into field equation",
            forbidden_if="diagnostic object becomes parent correction term",
            status="SAFE_IF",
            missing="none if kept diagnostic",
            consequence="allows source audits without source overlap",
        ),
        SourceSeparationEntry(
            name="SS17: ordinary T inside H_exch by fiat rejection",
            rule="ordinary T_mu_nu appears inside H_exch as exchange source by convenience",
            role="forbidden ordinary double-count",
            allowed_if="never without theorem",
            forbidden_if="accepted as H_exch source",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents ordinary matter double-counting",
        ),
        SourceSeparationEntry(
            name="SS18: e_curv inside H_curv source reservoir rejection",
            rule="e_curv is inserted into H_curv as source reservoir",
            role="forbidden curvature source overlap",
            allowed_if="never under current status",
            forbidden_if="accepted as H_curv source",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents curvature energy reservoir",
        ),
        SourceSeparationEntry(
            name="SS19: Sigma/R inside H_exch coefficient knobs rejection",
            rule="Sigma/R are hidden inside H_exch as adjustable coefficient knobs",
            role="forbidden exchange tuning",
            allowed_if="never as construction",
            forbidden_if="accepted as exchange correction",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents source/relaxation double-counting",
        ),
        SourceSeparationEntry(
            name="SS20: residual restored through tensor correction rejection",
            rule="B_s/F_zeta residual trace is restored through correction tensor after being killed/non-metric",
            role="forbidden residual source restoration",
            allowed_if="never without O/no-overlap theorem",
            forbidden_if="accepted as tensor correction",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents scalar trace resurrection",
        ),
        SourceSeparationEntry(
            name="SS21: dark sector relabels ordinary matter rejection",
            rule="dark-sector source is ordinary matter or ordinary exchange failure under a new name",
            role="forbidden dark relabel",
            allowed_if="never as mechanism",
            forbidden_if="accepted as dark correction",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents dark patch",
        ),
        SourceSeparationEntry(
            name="SS22: boundary source counted as tensor correction rejection",
            rule="boundary leakage/shell/scalar tail is counted as correction tensor source",
            role="forbidden boundary repair source",
            allowed_if="never as source separation",
            forbidden_if="accepted as H source",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents boundary repair tensor",
        ),
        SourceSeparationEntry(
            name="SS23: source-separation failure",
            rule="correction tensors cannot avoid ordinary/vacuum/source overlap",
            role="branch failure condition",
            allowed_if="used to keep correction tensors deferred or diagnostic-only",
            forbidden_if="patched with projectors, coefficients, or dark labels",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="correction tensors cannot be inserted",
        ),
        SourceSeparationEntry(
            name="SS24: recommended next move",
            rule="after source separation, audit boundary and mass neutrality",
            role="next local bottleneck",
            allowed_if="source separation remains theorem-targeted",
            forbidden_if="jumping to insertability before boundary/mass neutrality",
            status="RECOMMENDED",
            missing="boundary and mass neutrality audit",
            consequence="next script should be candidate_correction_tensor_boundary_and_mass_neutrality.py",
        ),
    ]


def print_entry(e: SourceSeparationEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Rule: {e.rule}")
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
    header("Case 0: Correction tensor source-separation problem")

    print("Question:")
    print()
    print("  Can correction tensors avoid double-counting ordinary matter and vacuum sources?")
    print()
    print("Goal:")
    print()
    print("  prevent H_curv/H_exch from hiding source overlap")
    print()
    print("Discipline:")
    print()
    print("  ordinary T_mu_nu remains in ordinary source side")
    print("  A-sector mass result protected")
    print("  e_curv not source reservoir")
    print("  Sigma/R not tuning knobs")
    print("  J_sub/J_exch not ordinary matter channels")
    print("  dark sector not ordinary matter relabel")
    print("  zeta/B_s insertion not reopened")
    print("  residual killed/non-metric unless O derived")
    print("  boundary source not counted as tensor correction")

    with out.unresolved_obligations():
        out.line("correction tensor source-separation problem posed", StatusMark.OBLIGATION, "source-separation audit required before any H insertion")


def case_1_inventory(entries: List[SourceSeparationEntry]):
    header("Case 1: Correction tensor source-separation inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[SourceSeparationEntry], out: ScriptOutput):
    header("Case 2: Compact source-separation ledger")

    print("| Entry | Rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact source-separation ledger produced", StatusMark.INFO, "STRUCTURAL")


def case_3_status_counts(entries: List[SourceSeparationEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Source separation is required but not derived.")
    print("  Ordinary matter must stay in ordinary source routing and A-sector mass accounting must remain protected.")
    print("  e_curv cannot become H_curv source reservoir.")
    print("  Sigma/R cannot become H_exch tuning knobs.")
    print("  J_sub/J_exch cannot become ordinary matter channels.")
    print("  Dark sector cannot relabel ordinary matter or ordinary exchange failure.")
    print("  zeta/B_s insertion and residual trace cannot be reopened by correction tensor.")
    print("  Boundary failure cannot be reclassified as correction tensor source.")
    print("  Projected source separation is a candidate only if projectors are real.")
    print("  Diagnostic-only remains the safest fallback.")
    print("  Next gate is boundary and mass neutrality.")

    with out.governance_assessments():
        out.line("source-separation status count produced", StatusMark.INFO, "STRUCTURAL")


def case_4_source_separation_classes(out: ScriptOutput):
    header("Case 4: Source-separation classes")

    print("Required separations:")
    print()
    print("1. ordinary matter vs correction tensors")
    print("2. A-sector mass source vs H sources")
    print("3. e_curv accounting vs H_curv source")
    print("4. A_curv diagnostic vs H_curv dynamics")
    print("5. J_curv absence vs H_curv current")
    print("6. Sigma/R role labels vs H_exch source/relaxation operators")
    print("7. J_V/J_exch role labels vs H_exch current")
    print("8. J_sub/J_exch vs ordinary matter channels")
    print("9. dark sector vs ordinary matter relabel")
    print("10. zeta/B_s insertion vs residual trace restoration")
    print("11. boundary source vs tensor correction")
    print()
    print("Candidate safe routes:")
    print()
    print("1. real projectors")
    print("2. diagnostic-only H-like objects")

    with out.governance_assessments():
        out.line("source-separation classes listed", StatusMark.PASS, "RECOMMENDED")


def case_4b_projector_sample(ns, out: ScriptOutput):
    header("Case 4b: Sample projector-based source separation")

    p_ordinary = sp.diag(1, 0, 0)
    p_correction = sp.diag(0, 1, 1)
    identity = sp.eye(3)
    overlap = sp.simplify(p_ordinary * p_correction)
    completeness = sp.simplify(p_ordinary + p_correction - identity)

    print("Sample projectors:")
    print(f"  P_ordinary = {p_ordinary}")
    print(f"  P_correction = {p_correction}")
    print()
    print(f"P_ordinary * P_correction = {overlap}")
    print(f"P_ordinary + P_correction - I = {completeness}")
    print()
    print("Interpretation:")
    print("  this is a compatibility example of exact sector separation by projectors.")
    print("  It does not prove the real sectors admit such projectors.")

    if overlap == sp.zeros(3) and completeness == sp.zeros(3):
        with out.sample_results():
            out.line(
                "sample projector separation witness",
                StatusMark.PASS,
                "projectors are orthogonal and complete in the toy source space",
            )
    else:
        with out.sample_results():
            out.line(
                "sample projector separation witness",
                StatusMark.FAIL,
                "toy projectors failed orthogonality/completeness",
            )

    ns.record_derivation(
        derivation_id="projector_source_separation_sample",
        inputs=[p_ordinary, p_correction],
        output=sp.Tuple(overlap, completeness),
        method="toy_projector_separation_compatibility",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
        scope="toy 3x3 diagonal projectors; not the real field-theory sector split",
    )


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: Source-separation decision tree")

    print("Decision tree:")
    print()
    print("1. Source sectors have real projectors / routing:")
    print("   projected source-separation candidate survives.")
    print()
    print("2. H-like object is diagnostic-only:")
    print("   safe if never inserted.")
    print()
    print("3. H_curv uses e_curv, A_curv, or J_curv as source without derivation:")
    print("   rejected or deferred.")
    print()
    print("4. H_exch uses Sigma/R or J_exch as source without derivation:")
    print("   rejected or deferred.")
    print()
    print("5. H reroutes ordinary matter, dark sector, residual trace, or boundary leakage:")
    print("   rejected.")
    print()
    print("6. Source separation cannot be proven:")
    print("   keep correction tensors deferred.")

    with out.governance_assessments():
        out.line("source-separation decision tree stated", StatusMark.PASS, "RECOMMENDED")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  correction tensors cannot avoid source overlap because source routing,")
    print("  projectors, current objects, or boundary neutrality are missing.")
    print()
    print("Consequence:")
    print()
    print("  keep H_curv/H_exch deferred or diagnostic-only.")
    print("  do not insert correction tensors into parent equation.")
    print()
    print("Bad failure:")
    print()
    print("  hide source overlap inside H_curv/H_exch coefficients or projector labels.")

    with out.governance_assessments():
        out.line("source-separation good failure stated", StatusMark.DEFER, "DEFERRED_PENDING_PREREQUISITES")


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("Source separation fails if:")
    print()
    print("1. ordinary matter appears inside H_curv/H_exch")
    print("2. A-sector mass accounting is changed")
    print("3. e_curv becomes source reservoir")
    print("4. A_curv diagnostic becomes dynamics")
    print("5. J_curv is used by name")
    print("6. Sigma/R become tuning knobs")
    print("7. J_V/J_exch role labels become source currents")
    print("8. J_sub/J_exch become matter channels")
    print("9. dark sector relabels ordinary matter")
    print("10. zeta/B_s insertion is reopened")
    print("11. residual trace is restored")
    print("12. boundary failure becomes source")
    print("13. projectors are invented after overlap")
    print("14. coefficients absorb overlap")

    with out.governance_assessments():
        out.line("source-separation failure controls stated", StatusMark.WARN, "RISK")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_correction_tensor_source_separation.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_correction_tensor_boundary_and_mass_neutrality.py")
    print("   Audit whether H_curv/H_exch avoid boundary repair and exterior mass shift.")
    print()
    print("3. candidate_source_separation_failure_summary.py")
    print("   Use if all source-separation routes collapse into overlap.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_correction_tensor_boundary_and_mass_neutrality.py")
    print()
    print("Reason:")
    print("  Source separation is not enough if the tensor repairs boundary behavior or shifts exterior mass.")
    print("  The next gate is boundary/mass neutrality.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "STRUCTURAL")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("Source separation is required but not derived.")
    print()
    print("Correction tensors cannot double-count:")
    print()
    print("  ordinary matter")
    print("  A-sector mass source")
    print("  e_curv accounting")
    print("  A_curv diagnostic status")
    print("  undefined J_curv")
    print("  Sigma/R role labels")
    print("  J_V/J_exch role labels")
    print("  J_sub/J_exch matter channels")
    print("  dark-sector labels")
    print("  zeta/B_s residual trace")
    print("  boundary failure")
    print()
    print("Candidate safe routes:")
    print()
    print("  real projectors")
    print("  diagnostic-only H-like objects")
    print()
    print("Best next script:")
    print()
    print("  candidate_correction_tensor_boundary_and_mass_neutrality.py")

    with out.governance_assessments():
        out.line("correction tensor source-separation audit complete", StatusMark.PASS, "CLOSED")

    out.print()


def record_governance(ns) -> None:
    required_obligations = [
        ("derive_ordinary_matter_source_separation_19",
         "Derive ordinary matter source separation theorem",
         "Ordinary T_mu_nu must stay in ordinary source routing (SS2)."),
        ("derive_A_sector_mass_protection_19",
         "Derive A-sector mass protection from correction tensor sources",
         "A-sector mass result must not be modified by correction tensor source accounting (SS3)."),
        ("guard_ecurv_not_source_reservoir_19",
         "Guard e_curv not-source-reservoir status",
         "e_curv must remain diagnostic/accounting only, not H_curv source (SS4)."),
        ("guard_A_curv_diagnostic_limit_19",
         "Guard A_curv diagnostic limit in source separation",
         "A_curv must remain diagnostic/branch-filter unless dynamics are derived (SS5)."),
        ("guard_J_curv_absence_source_19",
         "Guard J_curv absence as correction tensor source",
         "J_curv is not defined and cannot be counted as H_curv source/current (SS6)."),
        ("derive_Sigma_R_not_tuning_knobs_19",
         "Derive Sigma/R separation from H_exch tuning role",
         "Sigma/R must not be coefficients or cancellation knobs inside H_exch (SS7)."),
        ("guard_J_V_J_exch_unresolved_19",
         "Guard J_V/J_exch unresolved status in source separation",
         "J_V and J_exch are not defined enough to source H_exch (SS8)."),
        ("derive_J_sub_J_exch_not_matter_channels_19",
         "Derive J_sub/J_exch ordinary-matter-channel exclusion",
         "J_sub and J_exch must not become ordinary matter channels through correction tensors (SS9)."),
        ("guard_dark_sector_not_ordinary_relabel_19",
         "Guard dark sector not-ordinary-relabel status",
         "Dark-sector source cannot relabel ordinary matter or ordinary exchange failure (SS10)."),
        ("guard_zeta_Bs_insertion_not_reopened_19",
         "Guard zeta/B_s insertion not-reopened by correction tensors",
         "Correction tensors must not reopen B_s/F_zeta insertion or residual metric trace (SS11)."),
        ("guard_residual_killed_non_metric_19",
         "Guard residual killed/non-metric status",
         "Residual zeta/kappa trace must remain killed or non-metric unless O no-overlap is derived (SS12)."),
        ("derive_boundary_source_separation_19",
         "Derive boundary source separation from tensor correction",
         "Boundary leakage/shell/scalar tail cannot be reclassified as H source (SS13)."),
        ("derive_coefficient_source_separation_19",
         "Derive coefficient source separation",
         "Correction tensor coefficients must not be fitted from overlapping source sectors (SS14)."),
    ]

    for obligation_id, title, description in required_obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["correction_tensor_insertability_route"],
            description=description,
        ))

    all_obligation_ids = [o[0] for o in required_obligations]

    # Candidate routes
    ns.record_route(RouteRecord(
        route_id="projected_source_separation_candidate_route_19",
        script_id=SCRIPT_ID,
        name="Projected source separation candidate",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=all_obligation_ids,
        activation_conditions=[
            "real projectors separate ordinary, curvature, exchange, residual, and dark sectors",
            "projectors are not invented after source collision appears",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="diagnostic_only_source_separation_route_19",
        script_id=SCRIPT_ID,
        name="Diagnostic-only correction tensor (no source overlap)",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=["not inserted into field equation"],
    ))

    # SS23 BRANCH_KILLED -> DEFERRED_PENDING_PREREQUISITES per governance rule 5
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_source_separation_failure_branch_19",
        script_id=SCRIPT_ID,
        branch_id="correction_tensor_source_separation_failure",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=all_obligation_ids,
        description=(
            "SS23 failure condition: if correction tensors cannot avoid ordinary/vacuum/source overlap, "
            "they remain deferred or diagnostic-only. Mapped to DEFERRED_PENDING_PREREQUISITES because "
            "no contradiction has been demonstrated — source-separation prerequisites are simply absent."
        ),
    ))

    # Rejected routes
    for decision_id, branch_id, description in [
        ("reject_ordinary_T_inside_H_exch_19", "ordinary_T_inside_H_exch_fiat", "SS17: ordinary T inside H_exch by fiat rejected."),
        ("reject_ecurv_H_curv_reservoir_19", "ecurv_H_curv_source_reservoir", "SS18: e_curv inside H_curv as source reservoir rejected."),
        ("reject_sigma_r_H_exch_knobs_19", "sigma_r_H_exch_coefficient_knobs", "SS19: Sigma/R as H_exch coefficient knobs rejected."),
        ("reject_residual_restored_tensor_19", "residual_restored_through_tensor", "SS20: restoring residual trace through tensor correction rejected."),
        ("reject_dark_relabels_ordinary_19", "dark_sector_relabels_ordinary_matter", "SS21: dark sector relabeling ordinary matter rejected."),
        ("reject_boundary_source_tensor_19", "boundary_source_counted_as_tensor", "SS22: boundary source counted as tensor correction rejected."),
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
        claim_id="source_separation_not_derived_19",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.NOT_INSERTABLE_YET,
        statement=(
            "Source separation for correction tensors is required but not derived. "
            "All thirteen source-separation obligations remain open."
        ),
        obligation_ids=all_obligation_ids,
    ))


def main():
    header("Candidate Correction Tensor Source Separation")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_source_separation_classes(out)
    case_4b_projector_sample(ns, out)
    case_5_decision_tree(out)
    case_6_good_failure(out)
    case_7_failure_controls(out)
    case_8_next_tests(out)
    final_interpretation(out)

    with archive:
        record_governance(ns)
        ns.record_derivation(
            derivation_id="correction_tensor_source_separation_marker",
            inputs=[],
            output=sp.Symbol("correction_tensor_source_separation_complete"),
            method="correction_tensor_source_separation",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
