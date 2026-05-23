# Candidate projection commutation and divergence
#
# Group:
#   20_no_overlap_and_projection_operators
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Test whether no-overlap projectors can commute with derivatives/divergence
# without producing source leakage, boundary terms, scalar trace leakage, or
# hidden repair behavior.
#
# Locked-door question:
#
#   Does O commute with derivatives/divergence in a way that preserves constraints?


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
class CommutationEntry:
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
        dependency_id="current_split_projection_operator_marker",
        upstream_script_id="020_no_overlap_and_projection_operators__candidate_current_split_projection_operator",
        upstream_derivation_id="current_split_projection_operator_marker",
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


def build_entries() -> List[CommutationEntry]:
    return [
        CommutationEntry(
            name="D1: divergence-compatible projection target",
            candidate="O commutes with derivative/divergence strongly enough to preserve constraints",
            role="core Group 20 divergence target",
            allowed_if="commutator, boundary terms, and source routing are derived",
            forbidden_if="Bianchi or conservation compatibility is asserted by name",
            status="THEOREM_TARGET",
            missing="projected divergence identity and boundary law",
            consequence="divergence-compatible projection remains theorem target",
        ),
        CommutationEntry(
            name="D2: algebraic constant projector",
            candidate="constant matrix projector with D(O)=0",
            role="safe local toy class",
            allowed_if="sector basis is fixed and covariantly meaningful",
            forbidden_if="constant basis is coordinate artifact",
            status="SAFE_IF",
            missing="covariant sector basis and measure",
            consequence="can commute algebraically in toy basis only",
        ),
        CommutationEntry(
            name="D3: variable local projector",
            candidate="position-dependent O(x)",
            role="generic local projection risk",
            allowed_if="commutator term (nabla O) field is part of the theory",
            forbidden_if="(nabla O) field is ignored or hidden as source",
            status="RISK",
            missing="commutator source accounting",
            consequence="derivative leakage appears as (nabla O) field",
        ),
        CommutationEntry(
            name="D4: covariantly constant projector",
            candidate="nabla_mu O = 0 on the relevant domain",
            role="strong compatibility route",
            allowed_if="connection-compatible sector bundle is derived",
            forbidden_if="covariant constancy is assumed to avoid leakage",
            status="THEOREM_TARGET",
            missing="connection-compatible sector decomposition",
            consequence="promising but not currently derived",
        ),
        CommutationEntry(
            name="D5: constraint projector",
            candidate="O projects onto constraint-satisfying sector",
            role="possible structural route",
            allowed_if="constraint propagation and source compatibility are proved",
            forbidden_if="projection repairs constraint violation after evolution",
            status="CANDIDATE",
            missing="constraint propagation theorem",
            consequence="candidate route only",
        ),
        CommutationEntry(
            name="D6: Hodge-like projector",
            candidate="longitudinal/transverse or exact/coexact/harmonic split",
            role="possible divergence-aware class",
            allowed_if="metric, measure, boundary conditions, and domain are fixed",
            forbidden_if="boundary terms and harmonic modes are ignored",
            status="CANDIDATE",
            missing="Hodge data and boundary conditions",
            consequence="useful analogy, not a derived O",
        ),
        CommutationEntry(
            name="D7: nonlocal elliptic projector",
            candidate="solve auxiliary elliptic equation to project divergence-free part",
            role="possible but dangerous route",
            allowed_if="causality, boundary data, and source neutrality are controlled",
            forbidden_if="nonlocal solve becomes repair operator",
            status="RISK",
            missing="causal/domain/boundary law",
            consequence="cannot be inserted without stronger structure",
        ),
        CommutationEntry(
            name="D8: boundary-sensitive projector",
            candidate="O carries boundary terms explicitly",
            role="boundary leakage audit route",
            allowed_if="surface flux is derived and neutral",
            forbidden_if="surface term is suppressed to save recovery",
            status="THEOREM_TARGET",
            missing="boundary flux neutrality theorem",
            consequence="handoff to boundary/exterior neutrality script",
        ),
        CommutationEntry(
            name="D9: diagnostic-only projector",
            candidate="O labels sectors after a derivation but does not alter equations",
            role="safe fallback",
            allowed_if="labels do not change sources or divergence identities",
            forbidden_if="diagnostic label becomes active correction",
            status="SAFE_IF",
            missing="none for diagnostic use",
            consequence="safe bookkeeping while active O remains deferred",
        ),
        CommutationEntry(
            name="D10: commutes by declaration",
            candidate="declare [nabla, O] = 0 without deriving it",
            role="forbidden shortcut",
            allowed_if="never",
            forbidden_if="used to claim Bianchi/conservation compatibility",
            status="REJECTED",
            missing="not pursued",
            consequence="projected divergence cannot be asserted",
        ),
        CommutationEntry(
            name="D11: Bianchi compatibility by name",
            candidate="O is compatible with Bianchi identity because it is called a projection",
            role="forbidden parent-equation shortcut",
            allowed_if="never",
            forbidden_if="used to insert H_curv/H_exch or parent correction tensors",
            status="REJECTED",
            missing="not pursued",
            consequence="no correction tensor becomes insertable from O alone",
        ),
        CommutationEntry(
            name="D12: divergence decision",
            candidate="divergence-compatible O remains deferred until commutator and boundary terms are derived",
            role="current branch decision",
            allowed_if="future scripts keep divergence compatibility as obligation",
            forbidden_if="O is used as Bianchi repair",
            status="RECOMMENDED",
            missing="commutator law and boundary neutrality",
            consequence="next script should test boundary and exterior neutrality",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Projection commutation problem")
    print("Question:")
    print()
    print("  Does O commute with derivatives/divergence in a way that preserves constraints?")
    print()
    print("Goal:")
    print()
    print("  prevent projection language from becoming a divergence or Bianchi repair")
    print()
    print("Discipline:")
    print()
    print("  [nabla, O] must be derived, not declared")
    print("  boundary terms must be explicit")
    print("  source leakage must not be relabeled as exchange or curvature")
    print("  mass and scalar trace neutrality remain required")
    print("  recovery cannot choose the projector")
    with out.unresolved_obligations():
        out.line("projection commutation problem posed", StatusMark.OBLIGATION, "projected divergence identity not yet derived")


def case_1_inventory(entries: List[CommutationEntry]) -> None:
    header("Case 1: Commutation and divergence inventory")
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


def case_2_compact_table(entries: List[CommutationEntry], out: ScriptOutput) -> None:
    header("Case 2: Compact commutation ledger")
    print("| Entry | Candidate | Status | Consequence |")
    print("|---|---|---|---|")
    for entry in entries:
        print(f"| {entry.name} | {entry.candidate} | {entry.status} | {entry.consequence} |")
    with out.governance_assessments():
        out.line("compact projection commutation ledger produced", StatusMark.INFO, "divergence-compatible O remains theorem target")


def case_3_status_counts(entries: List[CommutationEntry], out: ScriptOutput) -> None:
    header("Case 3: Status counts")
    counts = {}
    for entry in entries:
        counts[entry.status] = counts.get(entry.status, 0) + 1
    for status in sorted(counts):
        print(f"{status}: {counts[status]}")
    print()
    print("Interpretation:")
    print("  Constant toy projectors may commute only in a fixed algebraic basis.")
    print("  Variable or boundary-sensitive projectors create commutator and surface terms.")
    print("  Divergence-compatible projection remains a theorem target.")
    with out.governance_assessments():
        out.line("projection commutation status count produced", StatusMark.INFO, str(counts))


def case_4_local_commutator_check(out: ScriptOutput) -> None:
    header("Case 4: Local commutator check")
    x = sp.symbols("x")
    p = sp.Function("p")(x)
    q = sp.Function("q")(x)
    a = sp.Function("a")(x)
    b = sp.Function("b")(x)
    O = sp.diag(p, q)
    v = sp.Matrix([a, b])
    commutator = sp.diff(O * v, x) - O * sp.diff(v, x)
    expected = sp.diff(O, x) * v
    constant_check = commutator.subs({sp.diff(p, x): 0, sp.diff(q, x): 0})

    print("Let:")
    print()
    print("  O(x) = diag(p(x), q(x))")
    print("  v(x) = [a(x), b(x)]^T")
    print()
    print("Commutator:")
    print()
    print("  d(Ov)/dx - O dv/dx =")
    print(f"  {commutator}")
    print()
    print("Expected leakage:")
    print()
    print("  (dO/dx)v =")
    print(f"  {expected}")
    print()
    print("If dO/dx = 0:")
    print()
    print(f"  commutator -> {constant_check}")
    print()
    print("Interpretation:")
    print("  A variable projector does not commute with derivatives.")
    print("  The leakage term is not optional; it must be assigned, canceled by theorem, or rejected.")
    with out.sample_results():
        out.line("variable projector produces commutator leakage", StatusMark.PASS, "d(Ov)-O(dv)=(dO)v")
    with out.governance_assessments():
        out.line("constant projector commutation is only toy-safe", StatusMark.INFO, "requires fixed covariant sector basis")


def case_5_projected_divergence_identity(out: ScriptOutput) -> None:
    header("Case 5: Projected divergence identity")
    print("Formal requirement:")
    print()
    print("  nabla_mu(O X)^mu = O nabla_mu X^mu + (nabla_mu O) X^mu")
    print()
    print("Therefore projected conservation requires one of:")
    print()
    print("1. nabla_mu O = 0 on the relevant sector.")
    print("2. (nabla_mu O) X^mu is a derived neutral term.")
    print("3. boundary/source terms cancel by an explicit theorem.")
    print("4. O is diagnostic-only and does not alter the field equation.")
    print()
    print("It is not enough to say:")
    print()
    print("  O preserves Bianchi identity")
    print("  O preserves conservation")
    print("  O prevents overlap")
    print()
    print("without the commutator and boundary accounting.")
    with out.unresolved_obligations():
        out.line("derive projected divergence identity", StatusMark.OBLIGATION, "commutator and boundary terms required")


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("Projection commutation fails if:")
    print()
    print("1. [nabla, O] is set to zero by declaration.")
    print("2. Bianchi compatibility is claimed by name.")
    print("3. boundary terms are dropped.")
    print("4. nonlocal projection repairs divergence failure.")
    print("5. source leakage is relabeled as Sigma/R.")
    print("6. scalar trace leakage is hidden by projection.")
    print("7. M_ext shifts through the projected sector.")
    print("8. recovery chooses O after the fact.")
    with out.counterexamples():
        out.line("commutes by declaration rejected", StatusMark.FAIL, "no projected divergence theorem")
        out.line("Bianchi compatibility by name rejected", StatusMark.FAIL, "no correction tensor insertability follows")
        out.line("nonlocal repair projection rejected", StatusMark.FAIL, "projection cannot repair divergence failure after the fact")


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Divergence-compatible projection is not solved.")
    print()
    print("Allowed status:")
    print()
    print("  constant algebraic projectors are toy-safe only")
    print("  diagnostic-only sector labels remain safe")
    print("  constraint/Hodge-like projectors remain candidate classes")
    print("  covariantly constant and boundary-neutral projectors remain theorem targets")
    print()
    print("Rejected:")
    print()
    print("  commutation by declaration")
    print("  Bianchi compatibility by name")
    print("  nonlocal repair projection")
    print("  recovery-chosen divergence projector")
    print()
    print("Missing before divergence-compatible O can be real:")
    print()
    print("  commutator identity")
    print("  connection-compatible sector basis")
    print("  projected divergence law")
    print("  boundary flux neutrality")
    print("  source, mass, and scalar trace leakage controls")
    print()
    print("Possible next artifact:")
    print("  candidate_projection_commutation_and_divergence.md")
    print()
    print("Possible next script:")
    print("  candidate_projection_boundary_and_exterior_neutrality.py")
    with out.governance_assessments():
        out.line("divergence-compatible O remains theorem target", StatusMark.DEFER, "commutator and boundary laws missing")


def record_governance(ns) -> None:
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_projected_divergence_identity_20",
        script_id=SCRIPT_ID,
        title="Derive projected divergence identity",
        status=ObligationStatus.OPEN,
        required_by=["projection_commutation_route_20"],
        description="Derive nabla_mu(OX)^mu and account for all commutator, source, and boundary terms.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_commutator_law_20",
        script_id=SCRIPT_ID,
        title="Derive commutator law for O",
        status=ObligationStatus.OPEN,
        required_by=["projection_commutation_route_20"],
        description="Show when [nabla, O] vanishes or where its leakage term is routed.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_connection_compatible_sector_basis_20",
        script_id=SCRIPT_ID,
        title="Derive connection-compatible sector basis",
        status=ObligationStatus.OPEN,
        required_by=["projection_commutation_route_20"],
        description="Define the sector basis and connection conditions needed for covariant projection.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_projection_boundary_terms_20",
        script_id=SCRIPT_ID,
        title="Derive projection boundary terms",
        status=ObligationStatus.OPEN,
        required_by=["projection_commutation_route_20"],
        description="Show the boundary flux induced by O and prove neutrality or controlled routing.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_projection_leakage_controls_20",
        script_id=SCRIPT_ID,
        title="Derive source, mass, and scalar leakage controls",
        status=ObligationStatus.OPEN,
        required_by=["projection_commutation_route_20"],
        description="Prevent projected divergence terms from shifting sources, M_ext, or scalar trace charge.",
    ))

    ns.record_route(RouteRecord(
        route_id="projection_commutation_route_20",
        script_id=SCRIPT_ID,
        name="Projection commutation theorem route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_projected_divergence_identity_20",
            "derive_commutator_law_20",
            "derive_connection_compatible_sector_basis_20",
            "derive_projection_boundary_terms_20",
            "derive_projection_leakage_controls_20",
        ],
        activation_conditions=[
            "commutator identity is derived",
            "boundary terms are explicit",
            "source/mass/scalar leakage is controlled",
            "projection is not chosen by recovery",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="diagnostic_projection_label_route_20",
        script_id=SCRIPT_ID,
        name="Diagnostic-only projection label fallback",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "projection labels do not alter field equations",
            "labels are not used to claim divergence compatibility",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_divergence_compatible_O_20",
        script_id=SCRIPT_ID,
        branch_id="divergence_compatible_projection",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_projected_divergence_identity_20",
            "derive_commutator_law_20",
            "derive_connection_compatible_sector_basis_20",
            "derive_projection_boundary_terms_20",
            "derive_projection_leakage_controls_20",
        ],
        description="Divergence-compatible O remains deferred until commutator, boundary, and leakage controls are derived.",
    ))
    for decision_id, branch_id, description in [
        (
            "reject_commutes_by_declaration_20",
            "commutes_by_declaration",
            "Reject declaring [nabla, O] = 0 without a sector-basis and connection theorem.",
        ),
        (
            "reject_bianchi_compatibility_by_name_20",
            "bianchi_compatibility_by_name",
            "Reject using projection language alone to claim Bianchi or conservation compatibility.",
        ),
        (
            "reject_nonlocal_repair_projection_20",
            "nonlocal_repair_projection",
            "Reject nonlocal projection chosen to repair divergence, boundary, scalar, or recovery failure.",
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
        claim_id="projection_commutation_summary",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "A no-overlap projector does not automatically commute with derivatives or divergence. "
            "Variable, boundary-sensitive, or nonlocal projectors carry commutator and surface terms; "
            "divergence-compatible projection remains a theorem target."
        ),
        obligation_ids=[
            "derive_projected_divergence_identity_20",
            "derive_commutator_law_20",
            "derive_connection_compatible_sector_basis_20",
            "derive_projection_boundary_terms_20",
            "derive_projection_leakage_controls_20",
        ],
    ))


def main():
    header("Candidate Projection Commutation And Divergence")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_local_commutator_check(out)
    case_5_projected_divergence_identity(out)
    case_6_failure_controls(out)
    final_interpretation(out)

    record_governance(ns)
    ns.record_derivation(
        derivation_id="projection_commutation_and_divergence_marker",
        inputs=[],
        output=sp.Symbol("projection_commutation_and_divergence_complete"),
        method="projection_commutation_and_divergence",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
