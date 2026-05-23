# Candidate postulate candidate ledger
#
# Group:
#   32_explicit_minimal_postulate_selection
#
# Human title:
#   Explicit Minimal Postulate Selection
#
# Script type:
#   CANDIDATE LEDGER / EXPLICIT-CHOICE AUDIT
#
# Purpose
# -------
# Inventory all candidate postulates opened by the explicit-selection problem.
# Classify them as admissible candidates, inherited disciplines, high-risk strong
# postulates, theorem/construction targets, forbidden immediate routes, or not-ready
# downstream gates.
#
# Locked-door question:
#
#   Which candidate postulates are actually available for explicit choice,
#   which are only inherited disciplines, and which remain too strong or not ready?
#
# This script does not adopt a postulate.
# It does not derive trace normalization.
# It does not derive safe trace membership.
# It does not derive trace/residual incidence.
# It does not derive the complete coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not derive active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Label the teeth before choosing which bite is real.

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


def status_mark(status: str) -> StatusMark:
    return {
        "ADMISSIBLE_CANDIDATE": StatusMark.INFO,
        "ADOPTABLE_ONLY_BY_EXPLICIT_DECISION": StatusMark.OBLIGATION,
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE_REMAINS": StatusMark.DEFER,
        "DEFERRED_STRONG_POSTULATE_OR_THEOREM_TARGET": StatusMark.DEFER,
        "FORBIDDEN_IMMEDIATE_ROUTE": StatusMark.FAIL,
        "GOVERNANCE_DISCIPLINE": StatusMark.INFO,
        "HIGH_RISK": StatusMark.DEFER,
        "INHERITED_PARTIAL_CONSTRAINT": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g32_problem",
            "32_explicit_minimal_postulate_selection__candidate_explicit_postulate_selection_problem",
            "g32_explicit_selection_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_summary",
            "31_source_divergence_coefficient_law__candidate_group_31_status_summary",
            "g31_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_obligations",
            "31_source_divergence_coefficient_law__candidate_source_divergence_obligations",
            "g31_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_trace_norm",
            "31_source_divergence_coefficient_law__candidate_trace_normalization_from_source_divergence",
            "g31_trace_normalization_fork",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
            "g30_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, expected_record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
        )

    return archive, ns, invalidated


def ensure_archive_write_dirs(ns) -> None:
    for attr in (
        "routes_path",
        "branch_decisions_path",
        "claims_path",
        "obligations_path",
        "derivations_path",
        "governance_path",
    ):
        path_obj = getattr(ns, attr, None)
        if path_obj is not None:
            path_obj.mkdir(parents=True, exist_ok=True)


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


@dataclass
class LedgerSymbols:
    P_trace_norm: sp.Symbol
    P_safe_membership: sp.Symbol
    P_guardrail_visibility: sp.Symbol
    P_div_explicitness: sp.Symbol
    P_source_no_hidden: sp.Symbol
    P_incidence_zero: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_insertion: sp.Symbol
    P_parent: sp.Symbol
    L_admissible_candidates: sp.Expr
    L_inherited_discipline: sp.Expr
    L_deferred_or_not_ready: sp.Expr
    L_downstream_gate: sp.Expr


@dataclass
class CandidatePostulateEntry:
    name: str
    symbol: str
    ledger_class: str
    status: str
    source_status: str
    role: str
    adoptable_if: str
    forbidden_if: str
    not_equivalent_to: str
    next_obligation: str


@dataclass
class InheritedDisciplineEntry:
    name: str
    symbol: str
    status: str
    inherited_from: str
    discipline: str
    theorem_gap: str
    adoption_boundary: str


@dataclass
class DeferredStrongEntry:
    name: str
    symbol: str
    status: str
    reason: str
    allowed_future_form: str
    forbidden_use_now: str


@dataclass
class LedgerRule:
    name: str
    rule: str
    status: str
    reason: str


@dataclass
class LedgerObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class LedgerConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> LedgerSymbols:
    (
        P_trace_norm,
        P_safe_membership,
        P_guardrail_visibility,
        P_div_explicitness,
        P_source_no_hidden,
        P_incidence_zero,
        P_active_O,
        P_residual_kill,
        P_insertion,
        P_parent,
    ) = sp.symbols(
        "P_trace_norm P_safe_membership P_guardrail_visibility P_div_explicitness "
        "P_source_no_hidden P_incidence_zero P_active_O P_residual_kill P_insertion P_parent",
        real=True,
    )

    L_admissible_candidates = sp.simplify(
        P_trace_norm + P_safe_membership + P_guardrail_visibility + P_div_explicitness
    )
    L_inherited_discipline = sp.simplify(P_source_no_hidden)
    L_deferred_or_not_ready = sp.simplify(
        P_incidence_zero + P_active_O + P_residual_kill + P_insertion + P_parent
    )
    L_downstream_gate = sp.simplify(P_active_O + P_residual_kill + P_insertion + P_parent)

    return LedgerSymbols(
        P_trace_norm=P_trace_norm,
        P_safe_membership=P_safe_membership,
        P_guardrail_visibility=P_guardrail_visibility,
        P_div_explicitness=P_div_explicitness,
        P_source_no_hidden=P_source_no_hidden,
        P_incidence_zero=P_incidence_zero,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_insertion=P_insertion,
        P_parent=P_parent,
        L_admissible_candidates=L_admissible_candidates,
        L_inherited_discipline=L_inherited_discipline,
        L_deferred_or_not_ready=L_deferred_or_not_ready,
        L_downstream_gate=L_downstream_gate,
    )


def build_admissible_candidates() -> List[CandidatePostulateEntry]:
    return [
        CandidatePostulateEntry(
            name="A1: trace normalization",
            symbol="P_trace_norm",
            ledger_class="candidate postulate",
            status="ADMISSIBLE_CANDIDATE",
            source_status="not derived by Group 31; candidate remains",
            role="choose how B_s reads the volume-trace scalar zeta through a fixed normalization rule",
            adoptable_if="only by explicit user/theory decision, not by theorem-route partiality",
            forbidden_if="normalization is selected from recovery, repair, source neutrality, divergence explicitness, insertion, or parent fit",
            not_equivalent_to="safe membership, trace/residual incidence, insertion, complete coefficient law, or parent closure",
            next_obligation="define normalization candidate without choosing the value from recovery or repair",
        ),
        CandidatePostulateEntry(
            name="A2: safe trace membership",
            symbol="P_safe_membership",
            ledger_class="candidate postulate",
            status="ADMISSIBLE_CANDIDATE",
            source_status="not derived by Group 31; open separate gap",
            role="assign zeta_Bs to T_zeta as safe trace membership",
            adoptable_if="only by explicit decision and with fences against incidence/no-overlap smuggling",
            forbidden_if="membership is used to assert zero trace/residual incidence, residual kill, active O, or insertion",
            not_equivalent_to="trace normalization, no-overlap geometry, residual control, or B_s/F_zeta insertion",
            next_obligation="state membership domain and non-incidence fence before package tests",
        ),
        CandidatePostulateEntry(
            name="A3: guardrail visibility",
            symbol="P_guardrail_visibility",
            ledger_class="candidate governance/postulate discipline",
            status="ADMISSIBLE_CANDIDATE",
            source_status="compatible with Group 31 anti-hidden-pocket discipline",
            role="require boundary, source, current, mass, support, and related guardrail loads to remain visible and auditable",
            adoptable_if="only as visibility discipline, not as neutrality theorem",
            forbidden_if="visibility is treated as boundary neutrality, scalar silence, mass neutrality, or divergence safety",
            not_equivalent_to="neutrality theorem, source no-double-counting theorem, or parent compatibility",
            next_obligation="map guardrail loads and distinguish visibility from neutrality",
        ),
        CandidatePostulateEntry(
            name="A4: divergence explicitness",
            symbol="P_div_explicitness",
            ledger_class="candidate governance/postulate discipline",
            status="ADMISSIBLE_CANDIDATE",
            source_status="Group 31 found non-reservoir explicitness admissible as discipline, not adopted",
            role="require correction/divergence terms to be explicit, auditable, and non-reservoir",
            adoptable_if="only as explicitness discipline weaker than full divergence-safe coefficient law",
            forbidden_if="explicitness is treated as divergence safety, residual cleanup, insertion, or parent readiness",
            not_equivalent_to="divergence-safe coefficient law or source no-double-counting theorem",
            next_obligation="carry non-reservoir and no-hidden-correction burden into dependency graph",
        ),
    ]


def build_inherited_disciplines() -> List[InheritedDisciplineEntry]:
    return [
        InheritedDisciplineEntry(
            name="I1: source hidden-pocket exclusion",
            symbol="P_source_no_hidden",
            status="INHERITED_PARTIAL_CONSTRAINT",
            inherited_from="Group 31 partial-constraint closure",
            discipline=(
                "ordinary source load may not be hidden in coefficient, residual, boundary, support, "
                "correction, exchange, curvature, or parent-placeholder channels"
            ),
            theorem_gap="full source no-double-counting theorem remains not derived",
            adoption_boundary="may be narrowed into an explicit postulate only by a later explicit decision",
        ),
    ]


def build_deferred_or_not_ready() -> List[DeferredStrongEntry]:
    return [
        DeferredStrongEntry(
            name="D1: trace/residual zero incidence",
            symbol="P_incidence_zero",
            status="DEFERRED_STRONG_POSTULATE_OR_THEOREM_TARGET",
            reason="would assert I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0; too close to residual-control/no-overlap smuggling",
            allowed_future_form="separate theorem target or explicitly labeled strong postulate after warnings",
            forbidden_use_now="cannot be folded into safe membership or Package B by implication",
        ),
        DeferredStrongEntry(
            name="D2: active O",
            symbol="P_active_O",
            status="NOT_READY",
            reason="active no-overlap operator is not constructed",
            allowed_future_form="construction target with domain, codomain, kernel, image, pairing, and boundary behavior",
            forbidden_use_now="cannot be adopted by name and cannot be licensed by package selection",
        ),
        DeferredStrongEntry(
            name="D3: residual kill",
            symbol="P_residual_kill",
            status="NOT_READY",
            reason="residual-control theorem is not derived",
            allowed_future_form="residual-control theorem or explicit high-risk postulate in a separate decision",
            forbidden_use_now="cannot be declared as consequence of safe membership, explicitness, or Package B",
        ),
        DeferredStrongEntry(
            name="D4: B_s/F_zeta insertion",
            symbol="P_insertion",
            status="NOT_READY",
            reason="normalization, membership, incidence, coefficient-law, and no-overlap gates remain open",
            allowed_future_form="theorem target after prerequisites or insertion-precondition inventory",
            forbidden_use_now="cannot be adopted as a minimal postulate and cannot follow from candidate package survival",
        ),
        DeferredStrongEntry(
            name="D5: parent closure",
            symbol="P_parent",
            status="FORBIDDEN_IMMEDIATE_ROUTE",
            reason="parent field equation is not ready and upstream scalar recombination gates are open",
            allowed_future_form="future parent route only after insertion, divergence safety, residual control, and source routing are resolved",
            forbidden_use_now="cannot be opened by explicit package selection",
        ),
    ]


def build_ledger_rules() -> List[LedgerRule]:
    return [
        LedgerRule(
            name="R1: candidate survival is not adoption",
            rule="an admissible candidate remains unadopted until an explicit user/theory decision records adoption",
            status="POLICY_RULE",
            reason="Group 31 partiality and Group 32 ledger classification do not select postulates",
        ),
        LedgerRule(
            name="R2: candidate postulate is not theorem",
            rule="an adopted postulate, if later chosen, must not be reported as derived",
            status="POLICY_RULE",
            reason="explicit choice is not proof",
        ),
        LedgerRule(
            name="R3: trace normalization is not membership",
            rule="P_trace_norm and P_safe_membership remain separate candidates",
            status="REQUIRED",
            reason="normalization selects how B_s reads zeta; membership assigns zeta_Bs to T_zeta",
        ),
        LedgerRule(
            name="R4: membership is not incidence",
            rule="safe membership must not imply I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0",
            status="REQUIRED",
            reason="zero incidence is high-risk and separate from membership",
        ),
        LedgerRule(
            name="R5: visibility is not neutrality",
            rule="guardrail visibility may require loads to remain auditable but does not make them neutral",
            status="REQUIRED",
            reason="neutrality remains theorem-level burden",
        ),
        LedgerRule(
            name="R6: explicitness is not divergence safety",
            rule="divergence explicitness is weaker than a divergence-safe coefficient law",
            status="REQUIRED",
            reason="Group 31 classified explicitness as partial discipline only",
        ),
        LedgerRule(
            name="R7: inherited source exclusion is not full theorem",
            rule="P_source_no_hidden preserves hidden-pocket exclusions but does not complete source no-double-counting",
            status="REQUIRED",
            reason="Group 31 ruled out shortcuts but did not derive the full sector theorem",
        ),
        LedgerRule(
            name="R8: package is not insertion",
            rule="no candidate package may license B_s/F_zeta insertion in this ledger",
            status="POLICY_RULE",
            reason="package selection can at most prepare later precondition audits",
        ),
        LedgerRule(
            name="R9: package is not parent closure",
            rule="no candidate package may open the parent field equation",
            status="POLICY_RULE",
            reason="parent gate remains closed",
        ),
    ]


def build_obligations() -> List[LedgerObligation]:
    return [
        LedgerObligation(
            name="O1: trace normalization definition",
            obligation="define the candidate normalization role without selecting a value from recovery or repair",
            status="OPEN",
            blocks="package sufficiency and trace-anchor audit",
            discipline="normalization candidate is real choice, not derived theorem",
        ),
        LedgerObligation(
            name="O2: safe membership fence",
            obligation="state zeta_Bs -> T_zeta membership while explicitly excluding incidence, residual kill, active O, and insertion",
            status="OPEN",
            blocks="dependency graph and package tests",
            discipline="membership is not no-overlap geometry",
        ),
        LedgerObligation(
            name="O3: visibility versus neutrality split",
            obligation="separate guardrail visibility from boundary/source/current/mass/support neutrality theorems",
            status="OPEN",
            blocks="package sufficiency classification",
            discipline="visible load is not neutral load",
        ),
        LedgerObligation(
            name="O4: explicitness versus divergence safety split",
            obligation="separate non-reservoir divergence explicitness from divergence-safe coefficient law",
            status="OPEN",
            blocks="dependency graph and package tests",
            discipline="explicit correction is not full divergence theorem",
        ),
        LedgerObligation(
            name="O5: inherited source exclusion status",
            obligation="carry P_source_no_hidden as inherited partial constraint unless explicitly narrowed into a postulate",
            status="OPEN",
            blocks="package minimality accounting",
            discipline="hidden-pocket exclusion is not full source no-double-counting theorem",
        ),
        LedgerObligation(
            name="O6: deferred strong candidates",
            obligation="keep incidence, residual kill, active O, insertion, and parent closure outside the minimal candidate ledger",
            status="NOT_READY",
            blocks="overreach and downstream gates",
            discipline="do not use candidate package to open downstream gates",
        ),
    ]


def build_conclusions() -> List[LedgerConclusion]:
    return [
        LedgerConclusion(
            name="C1: candidate ledger complete",
            conclusion="candidate postulates are inventoried and classified",
            status="REQUIRED",
            meaning="trace normalization, safe membership, guardrail visibility, and divergence explicitness remain admissible candidates",
        ),
        LedgerConclusion(
            name="C2: inherited discipline separated",
            conclusion="source hidden-pocket exclusion is classified separately as inherited partial constraint",
            status="INHERITED_PARTIAL_CONSTRAINT",
            meaning="it may participate in packages but is not the full source no-double-counting theorem",
        ),
        LedgerConclusion(
            name="C3: strong/not-ready items separated",
            conclusion="incidence, active O, residual kill, insertion, and parent closure are not available as minimal postulates now",
            status="NOT_READY",
            meaning="they remain high-risk, theorem targets, construction targets, or forbidden immediate routes",
        ),
        LedgerConclusion(
            name="C4: no adoption",
            conclusion="this ledger adopts no postulate",
            status="NOT_ADOPTED",
            meaning="candidate classification is not explicit theory choice",
        ),
        LedgerConclusion(
            name="C5: next",
            conclusion="postulate dependency graph should run next",
            status="OPEN",
            meaning="dependency and no-smuggling edges are needed before package minimality tests",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Candidate postulate ledger problem")
    print("Question:")
    print()
    print("  Which candidate postulates are actually available for explicit choice,")
    print("  which are only inherited disciplines, and which remain too strong or not ready?")
    print()
    print("Discipline:")
    print()
    print("  This script inventories candidates.")
    print("  It adopts no postulate.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Label the teeth before choosing which bite is real.")

    with out.governance_assessments():
        out.line(
            "candidate postulate ledger opened",
            StatusMark.INFO,
            "first concrete audit after explicit-selection opener",
        )


def case_1_symbolic_ledger(symbols: LedgerSymbols, out: ScriptOutput) -> None:
    header("Case 1: Candidate ledger symbolic loads")
    print("Candidate symbols:")
    print()
    for name in [
        "P_trace_norm",
        "P_safe_membership",
        "P_guardrail_visibility",
        "P_div_explicitness",
        "P_source_no_hidden",
        "P_incidence_zero",
        "P_active_O",
        "P_residual_kill",
        "P_insertion",
        "P_parent",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")

    print()
    print("Admissible candidate-choice load:")
    print(f"  L_admissible_candidates = {sp.sstr(symbols.L_admissible_candidates)}")
    print()
    print("Inherited discipline load:")
    print(f"  L_inherited_discipline = {sp.sstr(symbols.L_inherited_discipline)}")
    print()
    print("Deferred / not-ready load:")
    print(f"  L_deferred_or_not_ready = {sp.sstr(symbols.L_deferred_or_not_ready)}")
    print()
    print("Downstream gate load:")
    print(f"  L_downstream_gate = {sp.sstr(symbols.L_downstream_gate)}")

    with out.derived_results():
        out.line(
            "candidate ledger symbolic loads stated",
            StatusMark.OBLIGATION,
            (
                f"L_admissible_candidates = {sp.sstr(symbols.L_admissible_candidates)}; "
                f"L_inherited_discipline = {sp.sstr(symbols.L_inherited_discipline)}; "
                f"L_deferred_or_not_ready = {sp.sstr(symbols.L_deferred_or_not_ready)}"
            ),
        )


def case_2_admissible_candidates(items: List[CandidatePostulateEntry], out: ScriptOutput) -> None:
    header("Case 2: Admissible candidate-postulate ledger")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Symbol: {item.symbol}")
        print(f"Ledger class: {item.ledger_class}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Source status: {item.source_status}")
        print(f"Role: {item.role}")
        print(f"Adoptable if: {item.adoptable_if}")
        print(f"Forbidden if: {item.forbidden_if}")
        print(f"Not equivalent to: {item.not_equivalent_to}")
        print(f"Next obligation: {item.next_obligation}")

    with out.governance_assessments():
        out.line(
            "admissible candidate-postulate ledger stated",
            StatusMark.DEFER,
            f"{len(items)} admissible candidates inventoried; none adopted",
        )


def case_3_inherited_disciplines(items: List[InheritedDisciplineEntry], out: ScriptOutput) -> None:
    header("Case 3: Inherited discipline / partial-constraint ledger")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Symbol: {item.symbol}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Inherited from: {item.inherited_from}")
        print(f"Discipline: {item.discipline}")
        print(f"Theorem gap: {item.theorem_gap}")
        print(f"Adoption boundary: {item.adoption_boundary}")

    with out.governance_assessments():
        out.line(
            "inherited source-hidden discipline separated",
            StatusMark.INFO,
            "P_source_no_hidden is inherited partial constraint unless explicitly narrowed into a postulate",
        )


def case_4_deferred_or_not_ready(items: List[DeferredStrongEntry], out: ScriptOutput) -> None:
    header("Case 4: Deferred strong / not-ready candidate ledger")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Symbol: {item.symbol}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Allowed future form: {item.allowed_future_form}")
        print(f"Forbidden use now: {item.forbidden_use_now}")

    with out.governance_assessments():
        out.line(
            "strong and not-ready candidates separated",
            StatusMark.DEFER,
            "incidence, active O, residual kill, insertion, and parent closure excluded from minimal candidate ledger",
        )


def case_5_ledger_rules(items: List[LedgerRule], out: ScriptOutput) -> None:
    header("Case 5: Ledger no-smuggling rules")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Rule: {item.rule}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.governance_assessments():
        out.line(
            "candidate-ledger no-smuggling rules stated",
            StatusMark.OBLIGATION,
            f"{len(items)} rules stated before dependency graph and package tests",
        )


def case_6_obligations(items: List[LedgerObligation], out: ScriptOutput) -> None:
    header("Case 6: Candidate-ledger obligations")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "candidate-ledger obligations opened",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations stated",
        )


def case_7_conclusions(items: List[LedgerConclusion], out: ScriptOutput) -> None:
    header("Case 7: Candidate-ledger conclusions")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "candidate postulate ledger conclusion stated",
            StatusMark.PASS,
            "candidate ledger complete; no postulate adopted; dependency graph should run next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Candidate postulate ledger result:")
    print()
    print("  Trace normalization remains an admissible candidate postulate, not derived and not adopted.")
    print("  Safe trace membership remains an admissible candidate postulate, not derived and not adopted.")
    print("  Guardrail visibility remains admissible discipline, but visibility is not neutrality.")
    print("  Divergence explicitness remains admissible discipline, but explicitness is not divergence-safe coefficient law.")
    print("  Source hidden-pocket exclusion is inherited partial constraint, not full source no-double-counting theorem.")
    print("  Trace/residual zero incidence remains high-risk and separate from safe membership.")
    print("  Active O, residual kill, B_s/F_zeta insertion, and parent closure remain not ready.")
    print("  No postulate is adopted by this ledger.")
    print()
    print("Possible next script:")
    print("  candidate_postulate_dependency_graph.py")
    print()
    print("Tiny goblin label:")
    print("  Label the teeth before choosing which bite is real.")

    with out.governance_assessments():
        out.line(
            "candidate postulate ledger complete",
            StatusMark.PASS,
            "dependency graph should run next; package tests remain premature until no-smuggling edges are mapped",
        )


def record_inventory_marker(ns, symbols: LedgerSymbols) -> None:
    ns.record_derivation(
        derivation_id="g32_candidate_postulate_ledger",
        inputs=[
            symbols.P_trace_norm,
            symbols.P_safe_membership,
            symbols.P_guardrail_visibility,
            symbols.P_div_explicitness,
            symbols.P_source_no_hidden,
            symbols.P_incidence_zero,
            symbols.P_active_O,
            symbols.P_residual_kill,
            symbols.P_insertion,
            symbols.P_parent,
        ],
        output=(
            symbols.L_admissible_candidates
            + symbols.L_inherited_discipline
            + symbols.L_deferred_or_not_ready
        ),
        method="inventory and classify candidate postulates without adopting them",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="candidate_postulate_ledger_marker",
        scope="Group 32 explicit minimal postulate selection",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[LedgerObligation]) -> None:
    obligation_id_map = {
        "O1: trace normalization definition": "g32_define_trace_normalization_candidate",
        "O2: safe membership fence": "g32_safe_membership_non_incidence_fence",
        "O3: visibility versus neutrality split": "g32_visibility_not_neutrality",
        "O4: explicitness versus divergence safety split": "g32_explicitness_not_divergence_safety",
        "O5: inherited source exclusion status": "g32_source_no_hidden_inherited_status",
        "O6: deferred strong candidates": "g32_keep_strong_candidates_deferred",
    }

    for item in obligations:
        obligation_id = obligation_id_map[item.name]
        status = ObligationStatus.OPEN
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=item.obligation,
            status=status,
            required_by=["g32_candidate_postulate_ledger"],
            description=f"{item.discipline} Blocks: {item.blocks}.",
        ))


def record_governance(
    ns,
    candidates: List[CandidatePostulateEntry],
    inherited: List[InheritedDisciplineEntry],
    deferred: List[DeferredStrongEntry],
    rules: List[LedgerRule],
) -> None:
    obligation_ids = [
        "g32_define_trace_normalization_candidate",
        "g32_safe_membership_non_incidence_fence",
        "g32_visibility_not_neutrality",
        "g32_explicitness_not_divergence_safety",
        "g32_source_no_hidden_inherited_status",
        "g32_keep_strong_candidates_deferred",
    ]

    ns.record_route(RouteRecord(
        route_id="g32_candidate_postulate_ledger_route",
        script_id=SCRIPT_ID,
        name="Group 32 candidate postulate ledger route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "Group 32 explicit selection route opened",
            "candidate ledger required before dependency graph and package tests",
            "no postulate adoption is performed by ledger classification",
            "downstream gates remain closed",
        ],
    ))

    for item in candidates:
        ns.record_claim(ClaimRecord(
            claim_id=f"g32_candidate_{item.symbol}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=(
                f"{item.symbol} is classified as {item.status}: {item.role}. "
                f"It is adoptable only under: {item.adoptable_if}. It is forbidden if: {item.forbidden_if}."
            ),
            derivation_ids=["g32_candidate_postulate_ledger"],
            obligation_ids=obligation_ids,
        ))

    for item in inherited:
        ns.record_claim(ClaimRecord(
            claim_id=f"g32_inherited_{item.symbol}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                f"{item.symbol} is inherited as partial-constraint discipline from {item.inherited_from}: "
                f"{item.discipline}. It is not the full theorem because: {item.theorem_gap}."
            ),
            derivation_ids=["g32_candidate_postulate_ledger"],
            obligation_ids=obligation_ids,
        ))

    for item in deferred:
        status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        if item.status == "FORBIDDEN_IMMEDIATE_ROUTE":
            status = GovernanceStatus.POLICY_RULE
        ns.record_claim(ClaimRecord(
            claim_id=f"g32_deferred_{item.symbol}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=(
                f"{item.symbol} is classified as {item.status}: {item.reason}. "
                f"Allowed future form: {item.allowed_future_form}. Forbidden now: {item.forbidden_use_now}."
            ),
            derivation_ids=["g32_candidate_postulate_ledger"],
            obligation_ids=obligation_ids,
        ))

    for item in rules:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"g32_rule_{item.name.split(':')[0].lower().replace(' ', '_')}",
            script_id=SCRIPT_ID,
            branch_id=item.name,
            status=GovernanceStatus.POLICY_RULE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"{item.rule} Reason: {item.reason}",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g32_candidate_postulate_ledger_complete",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 32 candidate postulate ledger is complete. Trace normalization, safe membership, guardrail visibility, "
            "and divergence explicitness remain admissible candidates. Source hidden-pocket exclusion is inherited partial constraint. "
            "Trace/residual incidence is high-risk/deferred. Active O, residual kill, insertion, and parent closure remain not ready. "
            "No postulate is adopted by this ledger. Dependency graph should run next."
        ),
        derivation_ids=["g32_candidate_postulate_ledger"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Postulate Candidate Ledger")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    candidates = build_admissible_candidates()
    inherited = build_inherited_disciplines()
    deferred = build_deferred_or_not_ready()
    rules = build_ledger_rules()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_admissible_candidates(candidates, out)
    case_3_inherited_disciplines(inherited, out)
    case_4_deferred_or_not_ready(deferred, out)
    case_5_ledger_rules(rules, out)
    case_6_obligations(obligations, out)
    case_7_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, candidates, inherited, deferred, rules)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
