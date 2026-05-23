# Candidate source-sector projection operator
#
# Group:
#   20_no_overlap_and_projection_operators
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Test whether projection language can separate ordinary matter, A-sector mass,
# curvature accounting, exchange roles, residual/source exclusions, and optional
# dark labels without source double-counting or repair behavior.
#
# Locked-door question:
#
#   Can O separate ordinary matter, curvature accounting, and exchange sources?


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
class SourceProjectionEntry:
    name: str
    candidate: str
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
        dependency_id="metric_sector_no_overlap_operator_marker",
        upstream_script_id="020_no_overlap_and_projection_operators__candidate_metric_sector_no_overlap_operator",
        upstream_derivation_id="metric_sector_no_overlap_operator_marker",
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


def entry_status_mark(status: str) -> StatusMark:
    return {
        "CANDIDATE": StatusMark.INFO,
        "CONSTRAINED": StatusMark.INFO,
        "DEFER": StatusMark.DEFER,
        "RECOMMENDED": StatusMark.PASS,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "SAFE_IF": StatusMark.INFO,
        "STRUCTURAL": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def build_entries() -> List[SourceProjectionEntry]:
    return [
        SourceProjectionEntry(
            name="S1: source-sector projection target",
            candidate="O_source separates ordinary matter, A-sector mass, curvature accounting, exchange roles, residual labels, and optional dark labels",
            role="core Group 20 source target",
            allowed_if="source domain/kernel/image and routing rules are specified before correction or exchange use",
            forbidden_if="O_source is named to avoid source double-counting without a real split",
            status="THEOREM_TARGET",
            missing="explicit source-sector projector",
            consequence="source-sector projection remains theorem target",
        ),
        SourceProjectionEntry(
            name="S2: ordinary matter source projector",
            candidate="ordinary T_mu_nu / rho remains routed through established matter source channels",
            role="ordinary matter protection rule",
            allowed_if="ordinary matter is not rerouted into curvature, exchange, residual, or dark labels by convenience",
            forbidden_if="projection hides ordinary matter inside H_curv, H_exch, J_exch, e_curv, or dark source",
            status="REQUIRED",
            missing="ordinary matter separation theorem",
            consequence="ordinary matter source routing remains protected but not derived by O_source",
        ),
        SourceProjectionEntry(
            name="S3: A-sector mass projector",
            candidate="rho and M_ext remain A-sector mass / scalar constraint sources",
            role="A-sector mass protection rule",
            allowed_if="A carries the long-range mass response and other sectors do not duplicate it",
            forbidden_if="curvature, exchange, zeta, kappa, or correction tensors become independent mass-source channels",
            status="REQUIRED",
            missing="A-sector source separation theorem",
            consequence="strongest reduced A-sector result remains protected",
        ),
        SourceProjectionEntry(
            name="S4: curvature diagnostic projector",
            candidate="A_curv/e_curv classify curvature admissibility without becoming dynamics or source reservoir",
            role="curvature source-separation candidate",
            allowed_if="curvature variables remain diagnostic/branch-filter unless independent dynamics are derived",
            forbidden_if="projection promotes A_curv or e_curv into a source that repairs singularities or boundaries",
            status="SAFE_IF",
            missing="curvature diagnostic/source split",
            consequence="curvature accounting remains diagnostic only",
        ),
        SourceProjectionEntry(
            name="S5: exchange role projector",
            candidate="Sigma/R/J_exch roles remain separate from ordinary matter and repair terms",
            role="exchange source-separation theorem target",
            allowed_if="Sigma and R have independent operators, strengths, signs, and domains",
            forbidden_if="Sigma/R are adjusted as tuning knobs or cancellation labels",
            status="THEOREM_TARGET",
            missing="Sigma/R operators and source-strength law",
            consequence="exchange source side remains unresolved",
        ),
        SourceProjectionEntry(
            name="S6: residual/source exclusion projector",
            candidate="residual zeta/kappa bookkeeping is excluded from ordinary source roles",
            role="residual source safety rule",
            allowed_if="residual variables are non-metric, diagnostic, or projected with real kernel/image",
            forbidden_if="residual bookkeeping becomes hidden scalar source or coefficient reservoir",
            status="SAFE_IF",
            missing="residual source-exclusion theorem",
            consequence="residual variables may survive only with no source effect",
        ),
        SourceProjectionEntry(
            name="S7: correction tensor source projector",
            candidate="H_curv/H_exch source sides are separated from ordinary matter, curvature diagnostics, and exchange labels",
            role="correction tensor insertability prerequisite",
            allowed_if="source origin exists before correction tensor and divergence relation are introduced",
            forbidden_if="correction tensor defines its own source or absorbs unresolved sectors",
            status="THEOREM_TARGET",
            missing="H source origin and source-sector projector",
            consequence="H_curv/H_exch remain non-insertable",
        ),
        SourceProjectionEntry(
            name="S8: dark-sector optional projector",
            candidate="dark source labels remain optional and downstream",
            role="optional branch guard",
            allowed_if="dark coupling is derived and ordinary sector remains neutral",
            forbidden_if="dark sector patches ordinary source, boundary, or recovery failure",
            status="DEFER",
            missing="dark-sector source/coupling theorem",
            consequence="dark labels do not participate in ordinary source projection",
        ),
        SourceProjectionEntry(
            name="S9: boundary source exclusion projector",
            candidate="boundary mismatch, shell terms, far-zone leakage, and M_ext shifts are not promoted to source channels",
            role="boundary source guard",
            allowed_if="boundary behavior is structural and neutral",
            forbidden_if="projection turns boundary failure into source term",
            status="THEOREM_TARGET",
            missing="boundary source exclusion theorem",
            consequence="boundary repair remains rejected",
        ),
        SourceProjectionEntry(
            name="S10: diagnostic-only source labels",
            candidate="sector source labels classify evidence without active source routing",
            role="safe fallback",
            allowed_if="labels do not write field equations, erase sources, or insert correction tensors",
            forbidden_if="diagnostic label becomes active projector",
            status="SAFE_IF",
            missing="none if kept diagnostic",
            consequence="source audits can continue without O_source",
        ),
        SourceProjectionEntry(
            name="S11: source separator by name",
            candidate="O_source separates ordinary, curvature, exchange, residual, and dark sources by declaration",
            role="forbidden shortcut",
            allowed_if="never as derivation",
            forbidden_if="accepted without domain/kernel/image/source laws",
            status="REJECTED",
            missing="not pursued",
            consequence="source separation cannot be obtained by naming O_source",
        ),
        SourceProjectionEntry(
            name="S12: repair-source projector",
            candidate="projection turns singularity, boundary leakage, scalar charge, or recovery mismatch into a source side",
            role="forbidden repair branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as curvature or exchange source route",
            status="REJECTED",
            missing="not pursued",
            consequence="projection cannot create repair sources",
        ),
        SourceProjectionEntry(
            name="S13: source-sector current decision",
            candidate="O_source cannot yet be defined; diagnostic labels and protected source routing remain safest",
            role="current branch decision",
            allowed_if="future source scripts carry domain/kernel/image and source-law burden",
            forbidden_if="later scripts treat source projection as solved",
            status="RECOMMENDED",
            missing="role-specific source projector derivation",
            consequence="next script should test current split projection",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Source-sector projection problem")
    print("Question:")
    print()
    print("  Can O separate ordinary matter, curvature accounting, and exchange sources?")
    print()
    print("Goal:")
    print()
    print("  address the Group 19 source-separation bottleneck directly")
    print()
    print("Discipline:")
    print()
    print("  ordinary T_mu_nu not double-counted")
    print("  rho/scalar charge remains A-sector")
    print("  e_curv is not reservoir")
    print("  A_curv is not dynamics by projection")
    print("  Sigma/R are not tuning knobs")
    print("  J_sub/J_exch are not matter channels")
    print("  dark sector is not relabel")
    print("  boundary failure is not source")
    with out.unresolved_obligations():
        out.line("source-sector projection problem posed", StatusMark.OBLIGATION, "O_source not yet defined")


def case_1_inventory(entries: List[SourceProjectionEntry]) -> None:
    header("Case 1: Source-sector projection inventory")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Candidate: {entry.candidate}")
        print(f"Role: {entry.role}")
        print(f"Allowed if: {entry.allowed_if}")
        print(f"Forbidden if: {entry.forbidden_if}")
        print(f"[{entry_status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Missing: {entry.missing}")
        print(f"Consequence: {entry.consequence}")


def case_2_compact_table(entries: List[SourceProjectionEntry], out: ScriptOutput) -> None:
    header("Case 2: Compact source-sector ledger")
    print("| Entry | Candidate | Status | Consequence |")
    print("|---|---|---|---|")
    for entry in entries:
        print(f"| {entry.name} | {entry.candidate} | {entry.status} | {entry.consequence} |")
    with out.governance_assessments():
        out.line("compact source-sector projection ledger produced", StatusMark.INFO, "source O remains theorem target")


def case_3_status_counts(entries: List[SourceProjectionEntry], out: ScriptOutput) -> None:
    header("Case 3: Status counts")
    counts = {}
    for entry in entries:
        counts[entry.status] = counts.get(entry.status, 0) + 1
    for status in sorted(counts):
        print(f"{status}: {counts[status]}")
    print()
    print("Interpretation:")
    print("  Source-sector projection remains theorem-targeted.")
    print("  Ordinary matter and A-sector mass routing are required guardrails.")
    print("  Diagnostic-only labels are safer than active source projectors for now.")
    with out.governance_assessments():
        out.line("source-sector status count produced", StatusMark.INFO, str(counts))


def case_4_source_vector_check(out: ScriptOutput) -> None:
    header("Case 4: Source-routing vector check")
    rho, e_curv, sigma_exch, dark = sp.symbols("rho e_curv Sigma_exch dark")
    source_vec = sp.Matrix([rho, e_curv, sigma_exch, dark])
    P_A = sp.diag(1, 0, 0, 0)
    P_non_A = sp.eye(4) - P_A
    a_source = P_A * source_vec
    non_a_source = P_non_A * source_vec
    overlap = sp.simplify((P_A * P_non_A * source_vec)[0])
    print("Toy source vector:")
    print()
    print("  S = [rho, e_curv, Sigma_exch, dark]^T")
    print()
    print("A-sector projector candidate:")
    print(P_A)
    print()
    print(f"P_A S = {a_source}")
    print(f"(I - P_A) S = {non_a_source}")
    print(f"P_A(I-P_A)S first component = {overlap}")
    print()
    print("Interpretation:")
    print("  A block-diagonal source label can separate bookkeeping components in a toy vector.")
    print("  This does not derive physical source projectors, source strengths, covariance, or boundary behavior.")
    with out.sample_results():
        out.line("toy A-sector source label separates rho component", StatusMark.PASS, "diagnostic vector split only")
    with out.governance_assessments():
        out.line("toy source split insufficient for O_source", StatusMark.DEFER, "physical source laws and boundary behavior missing")


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("Source-sector projection fails if:")
    print()
    print("1. ordinary matter is counted in multiple source channels.")
    print("2. rho stops being protected as A-sector mass source.")
    print("3. e_curv becomes a source reservoir.")
    print("4. A_curv becomes dynamics by projection.")
    print("5. Sigma/R become tuning knobs.")
    print("6. J_sub/J_exch become ordinary matter channels.")
    print("7. dark sector patches ordinary failure.")
    print("8. boundary leakage becomes source.")
    print("9. correction tensor source is defined by the tensor it is meant to support.")
    with out.counterexamples():
        out.line("source separator by name rejected", StatusMark.FAIL, "domain/kernel/image/source laws missing")
        out.line("repair-source projector rejected", StatusMark.FAIL, "projection cannot create repair source")
        out.line("dark patch source rejected", StatusMark.FAIL, "dark sector remains optional/downstream")


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Source-sector projection is not solved.")
    print()
    print("Current protected routing:")
    print()
    print("  rho / M_ext -> A-sector mass source")
    print("  A_curv / e_curv -> diagnostic / accounting only")
    print("  Sigma/R -> exchange roles only, operators missing")
    print("  J_sub/J_exch -> not ordinary matter channels")
    print("  dark labels -> optional downstream only")
    print("  boundary failure -> not source")
    print()
    print("Useful safe fallback:")
    print()
    print("  diagnostic source labels, not active source projectors")
    print()
    print("Missing before O_source can be real:")
    print()
    print("  source-domain projector")
    print("  ordinary matter separation theorem")
    print("  A-sector mass protection theorem")
    print("  Sigma/R source-strength law")
    print("  correction tensor source origin")
    print("  boundary source exclusion theorem")
    print()
    print("Possible next artifact:")
    print("  candidate_source_sector_projection_operator.md")
    print()
    print("Possible next script:")
    print("  candidate_current_split_projection_operator.py")
    with out.governance_assessments():
        out.line("source-sector O remains theorem target", StatusMark.DEFER, "diagnostic labels remain safest current route")


def record_governance(ns) -> None:
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_O_source_20",
        script_id=SCRIPT_ID,
        title="Derive source-sector projection operator",
        status=ObligationStatus.OPEN,
        required_by=["source_sector_projection_route_20"],
        description="Define O_source with domain, codomain, kernel, image, source routing, and boundary behavior.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_ordinary_matter_separation_20",
        script_id=SCRIPT_ID,
        title="Derive ordinary matter source separation",
        status=ObligationStatus.OPEN,
        required_by=["source_sector_projection_route_20"],
        description="Show ordinary T_mu_nu/rho is not rerouted or double-counted in curvature, exchange, residual, dark, or correction sectors.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_A_sector_mass_source_protection_20",
        script_id=SCRIPT_ID,
        title="Derive A-sector mass source protection",
        status=ObligationStatus.OPEN,
        required_by=["source_sector_projection_route_20"],
        description="Show rho and M_ext remain A-sector source/charge unless a parent theorem derives otherwise.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_exchange_source_strength_law_20",
        script_id=SCRIPT_ID,
        title="Derive exchange source and relaxation operators",
        status=ObligationStatus.OPEN,
        required_by=["source_sector_projection_route_20"],
        description="Define Sigma/R operators, strengths, signs, and domains before using exchange source projection.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_boundary_source_exclusion_20",
        script_id=SCRIPT_ID,
        title="Derive boundary source exclusion",
        status=ObligationStatus.OPEN,
        required_by=["source_sector_projection_route_20"],
        description="Show boundary leakage, shell terms, scalar charge, and M_ext shifts are not promoted to source channels.",
    ))

    ns.record_route(RouteRecord(
        route_id="source_sector_projection_route_20",
        script_id=SCRIPT_ID,
        name="Source-sector projection theorem route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_O_source_20",
            "derive_ordinary_matter_separation_20",
            "derive_A_sector_mass_source_protection_20",
            "derive_exchange_source_strength_law_20",
            "derive_boundary_source_exclusion_20",
        ],
        activation_conditions=[
            "source projector has domain/kernel/image",
            "ordinary matter routing is protected",
            "exchange operators are defined",
            "boundary failure is not a source",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="diagnostic_source_label_route_20",
        script_id=SCRIPT_ID,
        name="Diagnostic source labels",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "labels classify evidence only",
            "labels are not active source projectors",
            "labels do not insert correction tensors or exchange sources",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_O_source_20",
        script_id=SCRIPT_ID,
        branch_id="source_sector_projection_operator",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_O_source_20",
            "derive_ordinary_matter_separation_20",
            "derive_A_sector_mass_source_protection_20",
            "derive_exchange_source_strength_law_20",
            "derive_boundary_source_exclusion_20",
        ],
        description="O_source remains deferred: source routing can be labeled diagnostically but no physical source projector is derived.",
    ))
    for decision_id, branch_id, description in [
        (
            "reject_source_separator_by_name_20",
            "source_separator_by_name",
            "Reject O_source by declaration without domain/kernel/image/source laws.",
        ),
        (
            "reject_repair_source_projector_20",
            "repair_source_projector",
            "Reject projection that turns singularity, boundary leakage, scalar charge, or recovery mismatch into a source side.",
        ),
        (
            "reject_dark_patch_source_20",
            "dark_sector_patch_source",
            "Reject dark-sector labels as patches for ordinary source failures.",
        ),
        (
            "reject_correction_tensor_source_by_tensor_20",
            "correction_tensor_source_by_tensor",
            "Reject correction tensor source defined by the tensor it is meant to support.",
        ),
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=decision_id,
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            description=description,
        ))

    ns.record_claim(ClaimRecord(
        claim_id="source_sector_projection_summary",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "Source-sector projection remains theorem-targeted. Ordinary matter and A-sector mass routing "
            "must remain protected; curvature and residual variables remain diagnostic unless independently "
            "derived; Sigma/R and correction tensor source sides remain unresolved."
        ),
        obligation_ids=[
            "derive_O_source_20",
            "derive_ordinary_matter_separation_20",
            "derive_A_sector_mass_source_protection_20",
            "derive_exchange_source_strength_law_20",
            "derive_boundary_source_exclusion_20",
        ],
    ))


def main():
    header("Candidate Source-Sector Projection Operator")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_source_vector_check(out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_governance(ns)
    ns.record_derivation(
        derivation_id="source_sector_projection_operator_marker",
        inputs=[],
        output=sp.Symbol("source_sector_projection_operator_complete"),
        method="source_sector_projection_operator",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
