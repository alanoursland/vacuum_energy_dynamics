# Candidate projection operator minimum structure
#
# Group:
#   20_no_overlap_and_projection_operators
#
# Script type:
#   REQUIREMENTS
#
# Purpose
# -------
# The first Group 20 script found that the no-overlap symbol O has too many
# jobs to be accepted as a universal operator. This script states the minimum
# mathematical structure any role-specific projector must have before it can be
# used in metric, source, current, curvature, boundary, or correction sectors.
#
# Locked-door question:
#
#   What minimum structure must O have to be a real projector?


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
class ProjectorRequirementEntry:
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
        dependency_id="no_overlap_operator_role_inventory_marker",
        upstream_script_id="20_no_overlap_and_projection_operators__candidate_no_overlap_operator_role_inventory",
        upstream_derivation_id="no_overlap_operator_role_inventory_marker",
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
        "DEFER": StatusMark.DEFER,
        "RECOMMENDED": StatusMark.PASS,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def build_entries() -> List[ProjectorRequirementEntry]:
    return [
        ProjectorRequirementEntry(
            name="P1: domain",
            requirement="state the mathematical space the projector acts on",
            role="well-posedness prerequisite",
            allowed_if="domain is specified before the projector is used",
            forbidden_if="O acts on whatever sector currently needs separation",
            status="REQUIRED",
            missing="domain for each role-specific projector",
            consequence="without domain, O is not an operator",
        ),
        ProjectorRequirementEntry(
            name="P2: codomain",
            requirement="state where the projected object lands",
            role="well-posedness prerequisite",
            allowed_if="codomain is distinct from or equal to the domain by explicit map",
            forbidden_if="projection output is inferred from desired no-overlap",
            status="REQUIRED",
            missing="codomain for each role-specific projector",
            consequence="without codomain, source and metric routing remain ambiguous",
        ),
        ProjectorRequirementEntry(
            name="P3: kernel",
            requirement="state what is removed or annihilated",
            role="no-overlap prerequisite",
            allowed_if="kernel is defined independently of recovery or failure patching",
            forbidden_if="kernel is whatever residual, source, or boundary term causes trouble",
            status="REQUIRED",
            missing="kernel definition",
            consequence="without kernel, residual-kill is only a convention",
        ),
        ProjectorRequirementEntry(
            name="P4: image",
            requirement="state what survives projection",
            role="sector routing prerequisite",
            allowed_if="image is a defined sector subspace or diagnostic label",
            forbidden_if="image is selected by GR recovery or insertability need",
            status="REQUIRED",
            missing="image definition",
            consequence="without image, projected sector identity is not meaningful",
        ),
        ProjectorRequirementEntry(
            name="P5: sector labels / basis",
            requirement="state the sector decomposition that domain, kernel, and image refer to",
            role="sector accounting prerequisite",
            allowed_if="basis or decomposition is stated before projection",
            forbidden_if="sector labels are invented after overlap is found",
            status="REQUIRED",
            missing="metric/source/current/curvature sector basis",
            consequence="without sector basis, no-overlap cannot be audited",
        ),
        ProjectorRequirementEntry(
            name="P6: composition / idempotence law",
            requirement="state P^2 = P or an equivalent projection rule",
            role="projector identity prerequisite",
            allowed_if="idempotence or a weaker named composition law is proved or declared as theorem target",
            forbidden_if="an arbitrary filter is called a projector",
            status="REQUIRED",
            missing="idempotence or equivalent law",
            consequence="without composition law, O is at most a diagnostic classifier",
        ),
        ProjectorRequirementEntry(
            name="P7: measure / pairing / inner product",
            requirement="state the measure or pairing used when orthogonality is claimed",
            role="orthogonality prerequisite",
            allowed_if="orthogonality is tied to a defined pairing and support",
            forbidden_if="orthogonal is used as a synonym for separate",
            status="REQUIRED",
            missing="measure or pairing",
            consequence="without measure, no orthogonality claim is licensed",
        ),
        ProjectorRequirementEntry(
            name="P8: locality / nonlocality status",
            requirement="state whether projection is algebraic, local differential, elliptic/nonlocal, support-based, or diagnostic-only",
            role="behavior prerequisite",
            allowed_if="nonlocality and support behavior are explicit",
            forbidden_if="nonlocal projection repairs boundary or scalar leakage by construction",
            status="REQUIRED",
            missing="locality class",
            consequence="nonlocal projectors are high-risk until boundary effects are known",
        ),
        ProjectorRequirementEntry(
            name="P9: covariance / gauge status",
            requirement="state whether the projector is covariant, gauge-fixed, gauge-invariant, or diagnostic in a chosen reduction",
            role="gauge discipline prerequisite",
            allowed_if="gauge status is explicit",
            forbidden_if="gauge-conditioned projection is promoted as covariant",
            status="REQUIRED",
            missing="covariance and gauge status",
            consequence="without gauge status, metric-sector O can overclaim",
        ),
        ProjectorRequirementEntry(
            name="P10: derivative / divergence behavior",
            requirement="state whether projection commutes with derivatives, divergence, constraints, or source identities",
            role="divergence safety prerequisite",
            allowed_if="commutation failure terms and boundary terms are accounted for",
            forbidden_if="Bianchi-like compatibility is asserted by name",
            status="THEOREM_TARGET",
            missing="projected divergence identity",
            consequence="no correction tensor becomes insertable from projection alone",
        ),
        ProjectorRequirementEntry(
            name="P11: boundary behavior",
            requirement="state exterior support, boundary flux, shell-source, far-zone, and M_ext behavior",
            role="boundary neutrality prerequisite",
            allowed_if="boundary behavior is structural and recovery-independent",
            forbidden_if="projection cancels boundary leakage or mass shift",
            status="THEOREM_TARGET",
            missing="boundary neutrality theorem",
            consequence="projection cannot protect exterior sector by declaration",
        ),
        ProjectorRequirementEntry(
            name="P12: source routing behavior",
            requirement="state how ordinary matter, A-sector mass, curvature accounting, exchange roles, and optional dark labels are routed",
            role="source separation prerequisite",
            allowed_if="ordinary matter and A-sector mass remain protected",
            forbidden_if="projection hides source double-counting or repair labels",
            status="THEOREM_TARGET",
            missing="source-sector projector",
            consequence="source separation remains a theorem target",
        ),
        ProjectorRequirementEntry(
            name="P13: metric insertion behavior",
            requirement="state how projection interacts with A, B_s, zeta, kappa, and residual metric trace",
            role="metric no-overlap prerequisite",
            allowed_if="scalar response is counted once and recovery remains downstream",
            forbidden_if="projection restores residual trace or chooses B_s by recovery",
            status="THEOREM_TARGET",
            missing="metric-sector projector",
            consequence="B_s/F_zeta insertion remains theorem target",
        ),
        ProjectorRequirementEntry(
            name="P14: diagnostic-only fallback",
            requirement="allow sector labels that classify records without active projection",
            role="safe fallback",
            allowed_if="labels are never used to erase sources or insert field-equation terms",
            forbidden_if="diagnostic labels become active operators",
            status="SAFE_IF",
            missing="none if kept diagnostic-only",
            consequence="audits can proceed while O remains undefined",
        ),
        ProjectorRequirementEntry(
            name="P15: O by declaration",
            requirement="define O as no-overlap by definition",
            role="forbidden shortcut",
            allowed_if="never as derivation",
            forbidden_if="accepted without domain/kernel/image/composition/boundary behavior",
            status="REJECTED",
            missing="not pursued",
            consequence="no-overlap language cannot replace projector structure",
        ),
        ProjectorRequirementEntry(
            name="P16: recovery projector",
            requirement="choose projection to recover gamma_like, AB, Schwarzschild, PPN, or expected exterior behavior",
            role="forbidden recovery-smuggling branch",
            allowed_if="recovery is a downstream test only",
            forbidden_if="recovery chooses kernel, image, support, coefficient, or residual status",
            status="REJECTED",
            missing="not pursued",
            consequence="recovery remains downstream",
        ),
        ProjectorRequirementEntry(
            name="P17: residual eraser",
            requirement="erase zeta/kappa residual trace after metric insertion",
            role="forbidden residual patch",
            allowed_if="residual-kill remains provisional or is derived by real kernel/image",
            forbidden_if="projection hides a still-active residual metric/source effect",
            status="REJECTED",
            missing="not pursued",
            consequence="residual-kill remains provisional",
        ),
        ProjectorRequirementEntry(
            name="P18: boundary patch",
            requirement="choose projection to cancel boundary leakage, scalar charge, far-zone flux, or M_ext shift",
            role="forbidden boundary repair branch",
            allowed_if="never as mechanism",
            forbidden_if="projection is selected after boundary failure appears",
            status="REJECTED",
            missing="not pursued",
            consequence="boundary neutrality must be structural",
        ),
        ProjectorRequirementEntry(
            name="P19: insertability patch",
            requirement="use projection to make H_curv/H_exch insertable",
            role="forbidden correction-tensor shortcut",
            allowed_if="never as mechanism",
            forbidden_if="projection substitutes for tensor definition, source origin, divergence, or boundary neutrality",
            status="REJECTED",
            missing="not pursued",
            consequence="H_curv/H_exch remain non-insertable",
        ),
        ProjectorRequirementEntry(
            name="P20: minimum projector burden",
            requirement="any future projector must satisfy the structural fields before being used",
            role="recommended next convention",
            allowed_if="future scripts treat missing fields as obligations, not optional detail",
            forbidden_if="later scripts invoke projector language before satisfying the burden",
            status="RECOMMENDED",
            missing="role-specific applications",
            consequence="next script should test the metric-sector no-overlap operator",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Projection operator minimum-structure problem")
    print("Question:")
    print()
    print("  What minimum structure must O have to be a real projector?")
    print()
    print("Goal:")
    print()
    print("  define the burden for any role-specific no-overlap projector")
    print()
    print("Discipline:")
    print()
    print("  no O by declaration")
    print("  no recovery projector")
    print("  no residual eraser")
    print("  no boundary patch")
    print("  no source separator by name")
    print("  no tensor insertability patch")
    print("  no orthogonality without measure or pairing")
    print("  no projector without domain/kernel/image/composition law")
    with out.unresolved_obligations():
        out.line("minimum projector burden posed", StatusMark.OBLIGATION, "role-specific applications still open")


def case_1_inventory(entries: List[ProjectorRequirementEntry]) -> None:
    header("Case 1: Minimum projector-structure inventory")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Requirement: {entry.requirement}")
        print(f"Role: {entry.role}")
        print(f"Allowed if: {entry.allowed_if}")
        print(f"Forbidden if: {entry.forbidden_if}")
        print(f"[{entry_status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Missing: {entry.missing}")
        print(f"Consequence: {entry.consequence}")


def case_2_compact_table(entries: List[ProjectorRequirementEntry], out: ScriptOutput) -> None:
    header("Case 2: Compact projector-structure ledger")
    print("| Entry | Requirement | Status | Consequence |")
    print("|---|---|---|---|")
    for entry in entries:
        print(f"| {entry.name} | {entry.requirement} | {entry.status} | {entry.consequence} |")
    with out.governance_assessments():
        out.line("compact projector-structure ledger produced", StatusMark.INFO, "minimum burden recorded")


def case_3_status_counts(entries: List[ProjectorRequirementEntry], out: ScriptOutput) -> None:
    header("Case 3: Status counts")
    counts = {}
    for entry in entries:
        counts[entry.status] = counts.get(entry.status, 0) + 1
    for status in sorted(counts):
        print(f"{status}: {counts[status]}")
    print()
    print("Interpretation:")
    print("  A real projector requires domain, codomain, kernel, image, sector basis,")
    print("  composition/idempotence, measure if orthogonality is claimed, locality status,")
    print("  gauge status, derivative/divergence behavior, and boundary behavior.")
    print("  O is not defined until those fields are supplied.")
    with out.governance_assessments():
        out.line("projector minimum-structure status count produced", StatusMark.INFO, str(counts))


def case_4_symbolic_idempotence_check(out: ScriptOutput) -> None:
    header("Case 4: Symbolic idempotence check")
    P = sp.MatrixSymbol("P", 3, 3)
    v = sp.MatrixSymbol("v", 3, 1)
    print("Formal projection law:")
    print()
    print("  P^2 = P")
    print()
    print("Applied twice:")
    print()
    print("  P(Pv) = P^2 v")
    print()
    print("If P^2 = P, then:")
    print()
    print("  P(Pv) = Pv")
    print()
    residual = sp.MatMul(P, P, v, evaluate=False)
    target = sp.MatMul(P, v, evaluate=False)
    print(f"Formal before imposing idempotence: {residual}")
    print(f"Formal target after idempotence:     {target}")
    print()
    print("Interpretation:")
    print("  Without a composition law such as P^2=P, a filter is not yet a projector.")
    with out.derived_results():
        out.line("projector idempotence burden stated", StatusMark.PASS, "P^2=P required or equivalent composition law needed")


def case_5_rejected_definitions(out: ScriptOutput) -> None:
    header("Case 5: Rejected definitions")
    print("Rejected:")
    print()
    print("1. O = no-overlap by definition.")
    print("2. O = residual eraser.")
    print("3. O = recovery projector.")
    print("4. O = boundary patch.")
    print("5. O = source separator by name.")
    print("6. O = correction tensor insertability patch.")
    print("7. orthogonality without measure or pairing.")
    print("8. projection without domain/kernel/image/composition law.")
    with out.counterexamples():
        out.line("O by declaration rejected", StatusMark.FAIL, "missing projector structure")
        out.line("recovery projector rejected", StatusMark.FAIL, "recovery remains downstream")
        out.line("insertability patch rejected", StatusMark.FAIL, "H_curv/H_exch remain non-insertable")


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("A real no-overlap projector must state at least:")
    print()
    print("  domain")
    print("  codomain")
    print("  kernel")
    print("  image")
    print("  sector basis")
    print("  composition / idempotence law")
    print("  measure or pairing if orthogonality is claimed")
    print("  locality / nonlocality status")
    print("  covariance / gauge status")
    print("  derivative / divergence behavior")
    print("  boundary behavior")
    print("  source and metric routing behavior")
    print()
    print("Therefore:")
    print()
    print("  O is still not defined.")
    print("  Projection language is allowed only as a theorem target or diagnostic label.")
    print("  Role-specific projector scripts must carry this minimum burden forward.")
    print()
    print("Possible next artifact:")
    print("  candidate_projection_operator_minimum_structure.md")
    print()
    print("Possible next script:")
    print("  candidate_metric_sector_no_overlap_operator.py")
    with out.governance_assessments():
        out.line("minimum projector structure complete", StatusMark.PASS, "projector burden defined; O still theorem target")


def record_governance(ns) -> None:
    ns.record_obligation(ProofObligationRecord(
        obligation_id="define_domain_codomain_kernel_image_20",
        script_id=SCRIPT_ID,
        title="Define domain, codomain, kernel, and image for projector candidates",
        status=ObligationStatus.OPEN,
        required_by=["minimum_projector_structure_route_20"],
        description=(
            "Any role-specific projector must define its domain, codomain, kernel, "
            "and image before it is used for no-overlap claims."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_projector_composition_law_20",
        script_id=SCRIPT_ID,
        title="Derive or state projector composition law",
        status=ObligationStatus.OPEN,
        required_by=["minimum_projector_structure_route_20"],
        description="Show P^2=P or an equivalent composition law for any true projector candidate.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="define_projector_measure_pairing_20",
        script_id=SCRIPT_ID,
        title="Define measure or pairing for orthogonality claims",
        status=ObligationStatus.OPEN,
        required_by=["minimum_projector_structure_route_20"],
        description="Any orthogonality or trace/traceless no-overlap claim must state its measure or pairing.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_projector_boundary_behavior_20",
        script_id=SCRIPT_ID,
        title="Derive boundary behavior for projector candidates",
        status=ObligationStatus.OPEN,
        required_by=["minimum_projector_structure_route_20"],
        description=(
            "Projection must not introduce boundary repair, exterior scalar charge, far-zone hidden flux, "
            "shell source, or M_ext shift."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_projected_divergence_behavior_20",
        script_id=SCRIPT_ID,
        title="Derive projected derivative and divergence behavior",
        status=ObligationStatus.OPEN,
        required_by=["minimum_projector_structure_route_20"],
        description="Show whether projectors commute with derivative/divergence operators or identify leakage terms.",
    ))

    ns.record_route(RouteRecord(
        route_id="minimum_projector_structure_route_20",
        script_id=SCRIPT_ID,
        name="Minimum projector structure route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "define_domain_codomain_kernel_image_20",
            "derive_projector_composition_law_20",
            "define_projector_measure_pairing_20",
            "derive_projector_boundary_behavior_20",
            "derive_projected_divergence_behavior_20",
        ],
        activation_conditions=[
            "domain/codomain/kernel/image are explicit",
            "composition law is available",
            "boundary behavior is known before recovery tests",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="diagnostic_projector_label_route_20",
        script_id=SCRIPT_ID,
        name="Diagnostic-only sector label route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "label is not treated as active operator",
            "label is not inserted into field equations",
            "label does not erase residual/source terms",
        ],
    ))

    for decision_id, branch_id, description in [
        (
            "reject_O_by_declaration_20",
            "O_by_declaration",
            "O by declaration is rejected because no-overlap language without domain/kernel/image/composition is not a projector.",
        ),
        (
            "reject_recovery_projector_20",
            "recovery_projector",
            "Recovery-defined projector is rejected: recovery may test only after projector structure exists.",
        ),
        (
            "reject_residual_eraser_projector_20",
            "residual_eraser_projector",
            "Residual eraser projector is rejected unless residual-kill is derived through a real kernel/image split.",
        ),
        (
            "reject_boundary_patch_projector_20",
            "boundary_patch_projector",
            "Boundary patch projector is rejected: boundary neutrality must be structural and not selected after leakage.",
        ),
        (
            "reject_insertability_patch_projector_20",
            "insertability_patch_projector",
            "Insertability patch projector is rejected: H_curv/H_exch still need tensor definitions, sources, divergence, and boundary behavior.",
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

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_active_projector_definition_20",
        script_id=SCRIPT_ID,
        branch_id="active_no_overlap_projector_definition",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "define_domain_codomain_kernel_image_20",
            "derive_projector_composition_law_20",
            "define_projector_measure_pairing_20",
            "derive_projector_boundary_behavior_20",
            "derive_projected_divergence_behavior_20",
        ],
        description="Active no-overlap projection remains deferred until the minimum projector burden is satisfied.",
    ))

    ns.record_claim(ClaimRecord(
        claim_id="projection_operator_minimum_structure_summary",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "A no-overlap projector requires domain, codomain, kernel, image, sector basis, "
            "composition/idempotence, measure or pairing for orthogonality, locality/gauge status, "
            "derivative/divergence behavior, and boundary behavior. O remains a theorem target until "
            "these are supplied."
        ),
        obligation_ids=[
            "define_domain_codomain_kernel_image_20",
            "derive_projector_composition_law_20",
            "define_projector_measure_pairing_20",
            "derive_projector_boundary_behavior_20",
            "derive_projected_divergence_behavior_20",
        ],
    ))


def main():
    header("Candidate Projection Operator Minimum Structure")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_symbolic_idempotence_check(out)
    case_5_rejected_definitions(out)
    final_interpretation(out)

    record_governance(ns)
    ns.record_derivation(
        derivation_id="projection_operator_minimum_structure_marker",
        inputs=[],
        output=sp.Symbol("projection_operator_minimum_structure_complete"),
        method="projection_operator_minimum_structure",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
