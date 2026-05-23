# Candidate pairing incidence forms
#
# Group:
#   28_sector_pairing_no_overlap
#
# Script type:
#   PAIRING / INCIDENCE FORM INVENTORY
#
# Purpose
# -------
# Compare mathematical forms that could encode no-overlap:
# bilinear pairing, incidence matrix, projection algebra, quotient relation,
# routing graph, support separation, divergence-safe split, and coefficient-induced split.
#
# Locked-door question:
#
#   What mathematical form could encode no-overlap?
#
# This script does not derive a no-overlap theorem.
# It does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   A zero needs a measuring stick.

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


# =============================================================================
# Utilities
# =============================================================================


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "AUXILIARY_CANDIDATE": StatusMark.INFO,
        "CANDIDATE": StatusMark.DEFER,
        "CONDITIONALLY_USEFUL": StatusMark.INFO,
        "INSUFFICIENT": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARENT_EXCLUDED": StatusMark.FAIL,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g28_mem",
            "028_sector_pairing_no_overlap__candidate_sector_membership_rules",
            "g28_membership",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_inv",
            "028_sector_pairing_no_overlap__candidate_sector_inventory",
            "g28_sector_inventory",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_prob",
            "028_sector_pairing_no_overlap__candidate_sector_problem_ledger",
            "g28_sector_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_summary",
            "027_active_O_construction__candidate_group_27_status_summary",
            "g27_status_summary",
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


# =============================================================================
# Data models
# =============================================================================


@dataclass
class PairingFormSymbols:
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    A_eps: sp.Symbol
    A_kappa: sp.Symbol
    I_TR: sp.Symbol
    P_T: sp.Symbol
    P_R: sp.Symbol
    Q_rel: sp.Symbol
    G_route: sp.Symbol
    S_support: sp.Symbol
    D_div: sp.Symbol
    C_coeff: sp.Symbol
    pairing_gap: sp.Symbol
    incidence_gap: sp.Symbol
    projection_gap: sp.Symbol
    quotient_gap: sp.Symbol
    routing_gap: sp.Symbol
    support_gap: sp.Symbol
    divergence_gap: sp.Symbol
    coefficient_gap: sp.Symbol
    form_load: sp.Expr


@dataclass
class PairingFormCandidate:
    name: str
    form: str
    status: str
    works_if: str
    hazard: str


@dataclass
class FormTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class FormRequirement:
    name: str
    requirement: str
    status: str
    needed_for: str
    fails_if: str


@dataclass
class RejectedFormShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class FormConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> PairingFormSymbols:
    (
        T_zeta,
        R_zeta,
        R_kappa,
        A_eps,
        A_kappa,
        I_TR,
        P_T,
        P_R,
        Q_rel,
        G_route,
        S_support,
        D_div,
        C_coeff,
        pairing_gap,
        incidence_gap,
        projection_gap,
        quotient_gap,
        routing_gap,
        support_gap,
        divergence_gap,
        coefficient_gap,
    ) = sp.symbols(
        "T_zeta R_zeta R_kappa A_eps A_kappa I_TR P_T P_R Q_rel G_route S_support D_div C_coeff "
        "pairing_gap incidence_gap projection_gap quotient_gap routing_gap support_gap divergence_gap coefficient_gap",
        real=True,
    )

    form_load = sp.simplify(
        pairing_gap
        + incidence_gap
        + projection_gap
        + quotient_gap
        + routing_gap
        + support_gap
        + divergence_gap
        + coefficient_gap
    )

    return PairingFormSymbols(
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        A_eps=A_eps,
        A_kappa=A_kappa,
        I_TR=I_TR,
        P_T=P_T,
        P_R=P_R,
        Q_rel=Q_rel,
        G_route=G_route,
        S_support=S_support,
        D_div=D_div,
        C_coeff=C_coeff,
        pairing_gap=pairing_gap,
        incidence_gap=incidence_gap,
        projection_gap=projection_gap,
        quotient_gap=quotient_gap,
        routing_gap=routing_gap,
        support_gap=support_gap,
        divergence_gap=divergence_gap,
        coefficient_gap=coefficient_gap,
        form_load=form_load,
    )


def build_form_candidates() -> List[PairingFormCandidate]:
    return [
        PairingFormCandidate(
            name="P1: bilinear pairing",
            form="<X,Y> = 0",
            status="UNDERDETERMINED",
            works_if="the theory supplies a bilinear pairing on sector objects",
            hazard="ordinary inner-product orthogonality is assumed by habit",
        ),
        PairingFormCandidate(
            name="P2: incidence matrix",
            form="I(T_zeta, R_zeta)=0 and I(T_zeta, R_kappa)=0",
            status="CANDIDATE",
            works_if="incidence is defined by trace/source/role routing rather than naming",
            hazard="zero incidence is declared without rule",
        ),
        PairingFormCandidate(
            name="P3: projection algebra",
            form="P_T P_R = 0 with sector projectors",
            status="UNDERDETERMINED",
            works_if="sector projectors and composition law are derived",
            hazard="projection algebra smuggles active O",
        ),
        PairingFormCandidate(
            name="P4: quotient relation",
            form="X ~ Y modulo diagnostic/inert/accounting sector",
            status="UNDERDETERMINED",
            works_if="quotient sector has proven no metric/source/boundary/recovery/parent role",
            hazard="quotient hides residual geometry",
        ),
        PairingFormCandidate(
            name="P5: routing graph separation",
            form="no directed path from residual sector to safe trace/source role",
            status="CANDIDATE",
            works_if="edges are derived from construction roles, not recovery or repair",
            hazard="graph separation is asserted without edge rules",
        ),
        PairingFormCandidate(
            name="P6: support separation",
            form="support(T_zeta) cap support(R_zeta/R_kappa)=empty",
            status="INSUFFICIENT",
            works_if="support split also survives boundary/matching/divergence checks",
            hazard="transition layers or boundary terms reintroduce overlap",
        ),
        PairingFormCandidate(
            name="P7: divergence-safe split",
            form="sector split preserved by derivative/divergence",
            status="UNDERDETERMINED",
            works_if="commutation or explicit correction law is derived",
            hazard="divergence correction becomes hidden source",
        ),
        PairingFormCandidate(
            name="P8: coefficient-induced split",
            form="B_s/F_zeta coefficient origin identifies safe scalar channel",
            status="UNDERDETERMINED",
            works_if="coefficient origin is derived separately",
            hazard="insertion law is smuggled into no-overlap geometry",
        ),
        PairingFormCandidate(
            name="P9: recovery-defined split",
            form="sector split chosen because AB=1/Schwarzschild/gamma works",
            status="REJECTED",
            works_if="never allowed",
            hazard="recovery constructs no-overlap",
        ),
    ]


def build_tests() -> List[FormTest]:
    return [
        FormTest(
            name="T1: bilinear pairing availability",
            test="does current theory supply <X,Y>?",
            status="NOT_DERIVED",
            result="no explicit bilinear pairing is available",
            implication="orthogonality cannot yet be claimed",
        ),
        FormTest(
            name="T2: incidence matrix viability",
            test="can incidence be treated as a candidate form?",
            status="CANDIDATE",
            result="yes, if edge/incidence rules are derived next",
            implication="incidence is a strong candidate for the next detailed audit",
        ),
        FormTest(
            name="T3: projection algebra viability",
            test="can P_T P_R = 0 be asserted now?",
            status="NOT_DERIVED",
            result="no; projectors and composition law are not derived",
            implication="projection form risks smuggling active O",
        ),
        FormTest(
            name="T4: routing graph viability",
            test="can routing graph separation be treated as candidate?",
            status="CANDIDATE",
            result="yes, if edge rules are construction-derived and not recovery/repair-selected",
            implication="routing graph can complement incidence",
        ),
        FormTest(
            name="T5: support separation sufficiency",
            test="is support separation sufficient alone?",
            status="INSUFFICIENT",
            result="no; support does not control trace/source/divergence reentry alone",
            implication="support can only be auxiliary",
        ),
        FormTest(
            name="T6: coefficient-induced split viability",
            test="can coefficient origin define split now?",
            status="UNDERDETERMINED",
            result="not yet; coefficient origin remains open",
            implication="coefficient-origin handoff remains relevant",
        ),
        FormTest(
            name="T7: downstream closure test",
            test="does any form license O, residual control, insertion, or parent closure now?",
            status="REJECTED",
            result="no",
            implication="all downstream gates remain closed",
        ),
    ]


def build_requirements() -> List[FormRequirement]:
    return [
        FormRequirement(
            name="R1: define zero",
            requirement="state what zero pairing/incidence means",
            status="REQUIRED",
            needed_for="no-overlap theorem",
            fails_if="zero is only a notation",
        ),
        FormRequirement(
            name="R2: define objects paired",
            requirement="state which sector objects enter the form",
            status="REQUIRED",
            needed_for="membership/pairing consistency",
            fails_if="objects are selected by symbol name only",
        ),
        FormRequirement(
            name="R3: trace/residual separation",
            requirement="separate T_zeta from R_zeta/R_kappa without residual erasure",
            status="REQUIRED",
            needed_for="future kernel/image and count-once work",
            fails_if="residual sectors become inert by label",
        ),
        FormRequirement(
            name="R4: accounting no-reservoir",
            requirement="prevent A_eps/A_kappa from absorbing residual geometry",
            status="REQUIRED",
            needed_for="accounting discipline",
            fails_if="quotient/accounting form hides metric/source load",
        ),
        FormRequirement(
            name="R5: source/boundary/support auditability",
            requirement="preserve audit sectors without letting them select the form",
            status="REQUIRED",
            needed_for="guardrail independence",
            fails_if="repair need chooses incidence or routing edges",
        ),
        FormRequirement(
            name="R6: divergence safety",
            requirement="classify whether the form survives derivative/divergence",
            status="REQUIRED",
            needed_for="future field-equation use",
            fails_if="correction term becomes hidden source",
        ),
        FormRequirement(
            name="R7: recovery independence",
            requirement="reject recovery-selected form",
            status="REQUIRED",
            needed_for="anti-smuggling",
            fails_if="AB=1/Schwarzschild/gamma/weak-field selects the form",
        ),
        FormRequirement(
            name="R8: downstream separation",
            requirement="keep active O, residual control, insertion, and parent closure separate",
            status="REQUIRED",
            needed_for="not overclaiming",
            fails_if="form inventory is upgraded to theorem closure",
        ),
    ]


def build_shortcuts() -> List[RejectedFormShortcut]:
    return [
        RejectedFormShortcut(
            name="F1: inner product by habit",
            shortcut="use ordinary orthogonality without deriving pairing",
            status="REJECTED",
            reason="no bilinear pairing is supplied",
        ),
        RejectedFormShortcut(
            name="F2: zero incidence by naming",
            shortcut="write I(T,R)=0 without incidence rule",
            status="REJECTED",
            reason="zero must have content",
        ),
        RejectedFormShortcut(
            name="F3: projection algebra as O",
            shortcut="use P_T P_R=0 as active O construction",
            status="REJECTED",
            reason="projectors and active O are not derived",
        ),
        RejectedFormShortcut(
            name="F4: quotient hides residual",
            shortcut="mod out residual/accounting sector without no-reservoir theorem",
            status="REJECTED",
            reason="quotient can hide geometry",
        ),
        RejectedFormShortcut(
            name="F5: graph edge by desire",
            shortcut="delete residual-to-trace/source edge because closure needs it",
            status="REJECTED",
            reason="routing edges must be derived",
        ),
        RejectedFormShortcut(
            name="F6: support separation as full proof",
            shortcut="use disjoint support as full no-overlap",
            status="REJECTED",
            reason="support separation is insufficient alone",
        ),
        RejectedFormShortcut(
            name="F7: coefficient split as insertion",
            shortcut="use coefficient-induced split as B_s/F_zeta insertion theorem",
            status="REJECTED",
            reason="coefficient origin and insertion remain separate",
        ),
        RejectedFormShortcut(
            name="F8: recovery-defined form",
            shortcut="choose form from recovery success",
            status="REJECTED",
            reason="recovery may audit but not construct",
        ),
        RejectedFormShortcut(
            name="F9: form inventory opens parent",
            shortcut="treat form inventory as parent readiness",
            status="REJECTED",
            reason="parent equation remains closed",
        ),
    ]


def build_conclusions() -> List[FormConclusion]:
    return [
        FormConclusion(
            name="C1: bilinear pairing",
            conclusion="bilinear pairing is not derived",
            status="NOT_DERIVED",
            meaning="ordinary orthogonality cannot be claimed",
        ),
        FormConclusion(
            name="C2: incidence/routing",
            conclusion="incidence matrix and routing graph are the best candidate forms",
            status="CANDIDATE",
            meaning="they can express trace/residual separation without assuming projection algebra",
        ),
        FormConclusion(
            name="C3: projection/quotient",
            conclusion="projection and quotient forms remain underdetermined",
            status="UNDERDETERMINED",
            meaning="they risk smuggling active O or hiding residual geometry",
        ),
        FormConclusion(
            name="C4: support/divergence/coefficient",
            conclusion="support is insufficient alone; divergence and coefficient forms remain underdetermined",
            status="UNDERDETERMINED",
            meaning="these may become auxiliary or later routes",
        ),
        FormConclusion(
            name="C5: next route",
            conclusion="trace/residual incidence should be tested next",
            status="OPEN",
            meaning="incidence/routing candidates should be applied to T_zeta, R_zeta, and R_kappa",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Pairing/incidence form problem")
    print("Question:")
    print()
    print("  What mathematical form could encode no-overlap?")
    print()
    print("Reference discipline:")
    print()
    print("  A zero needs a measuring stick.")
    print("  Pairing, incidence, projection, routing, support, divergence, and coefficient forms are candidates only.")
    print("  No form may license active O, residual control, insertion, or parent closure.")

    with out.governance_assessments():
        out.line(
            "pairing/incidence form inventory opened",
            StatusMark.INFO,
            "comparing no-overlap form candidates without deriving no-overlap theorem",
        )


def case_1_symbol_ledger(symbols: PairingFormSymbols, out: ScriptOutput) -> None:
    header("Case 1: Pairing/incidence symbolic ledger")
    print("Candidate form symbols:")
    print()
    for name in [
        "I_TR",
        "P_T",
        "P_R",
        "Q_rel",
        "G_route",
        "S_support",
        "D_div",
        "C_coeff",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Form load:")
    print()
    print(f"  L_pairing_form = {sp.sstr(symbols.form_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Pairing/incidence/projection/routing form is not derived.")
    print("  Candidate forms must be tested without downstream closure.")

    with out.derived_results():
        out.line(
            "pairing/incidence form load stated",
            StatusMark.OBLIGATION,
            f"L_pairing_form = {sp.sstr(symbols.form_load)}",
        )


def case_2_form_candidates(items: List[PairingFormCandidate], out: ScriptOutput) -> None:
    header("Case 2: Candidate no-overlap forms")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Form: {item.form}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Works if: {item.works_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "candidate no-overlap forms classified",
            StatusMark.DEFER,
            f"{len(items)} no-overlap form candidates classified",
        )


def case_3_tests(items: List[FormTest], out: ScriptOutput) -> None:
    header("Case 3: Pairing/incidence form tests")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Test: {item.test}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Implication: {item.implication}")

    with out.governance_assessments():
        out.line(
            "pairing/incidence form tests completed",
            StatusMark.DEFER,
            "bilinear pairing not derived; incidence/routing are best candidate forms",
        )


def case_4_requirements(items: List[FormRequirement], out: ScriptOutput) -> None:
    header("Case 4: Requirements for any no-overlap form")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Requirement: {item.requirement}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Needed for: {item.needed_for}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "pairing/incidence form requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} requirements remain open for any no-overlap form",
        )


def case_5_shortcuts(items: List[RejectedFormShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected form shortcuts")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Shortcut: {item.shortcut}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "pairing/incidence form shortcuts rejected",
            StatusMark.FAIL,
            "inner product by habit, zero incidence by naming, projection as O, quotient hiding, graph edge by desire, support proof, coefficient insertion, recovery form, and parent readiness are rejected",
        )


def case_6_conclusions(items: List[FormConclusion], out: ScriptOutput) -> None:
    header("Case 6: Pairing/incidence form conclusions")
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
            "pairing/incidence form conclusion stated",
            StatusMark.DEFER,
            "incidence/routing are best candidate forms; trace/residual incidence should be tested next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Pairing/incidence form result:")
    print()
    print("  No bilinear pairing is derived.")
    print("  Ordinary orthogonality cannot be claimed.")
    print("  Incidence matrix and routing graph are the best current candidate forms.")
    print("  Projection algebra remains underdetermined and risks smuggling active O.")
    print("  Quotient form remains underdetermined and risks hiding residual geometry.")
    print("  Support separation is insufficient alone.")
    print("  Divergence-safe and coefficient-induced forms remain underdetermined.")
    print("  Recovery-defined forms are rejected.")
    print("  No form licenses active O, residual control, insertion, or parent closure.")
    print()
    print("Possible next script:")
    print("  candidate_trace_residual_incidence.py")
    print()
    print("Tiny goblin label:")
    print("  A zero needs a measuring stick.")

    with out.governance_assessments():
        out.line(
            "pairing/incidence form inventory complete",
            StatusMark.PASS,
            "incidence/routing candidates selected for trace/residual test",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: PairingFormSymbols) -> None:
    ns.record_derivation(
        derivation_id="g28_pair_forms",
        inputs=[
            symbols.pairing_gap,
            symbols.incidence_gap,
            symbols.projection_gap,
            symbols.quotient_gap,
            symbols.routing_gap,
            symbols.support_gap,
            symbols.divergence_gap,
            symbols.coefficient_gap,
        ],
        output=symbols.form_load,
        method="inventory candidate no-overlap mathematical forms and classify incidence/routing as best candidates",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="pairing_forms_marker",
        scope="Group 28 sector pairing/no-overlap geometry",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g28_forms_define_zero", "Define zero pairing/incidence content"),
        ("g28_forms_objects", "Define objects entering the form"),
        ("g28_forms_trace_res", "Test trace/residual incidence"),
        ("g28_forms_accounting", "Prevent accounting/quotient reservoir"),
        ("g28_forms_guardrail", "Preserve source/boundary/support auditability"),
        ("g28_forms_div", "Audit divergence-safe form behavior"),
        ("g28_forms_recovery", "Reject recovery-defined form"),
        ("g28_forms_downstream", "Keep O/residual/insertion/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g28_forms_route"],
            description=(
                "Pairing/incidence forms are inventoried here. Incidence/routing are best candidates, but no no-overlap theorem is derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g28_forms_define_zero",
        "g28_forms_objects",
        "g28_forms_trace_res",
        "g28_forms_accounting",
        "g28_forms_guardrail",
        "g28_forms_div",
        "g28_forms_recovery",
        "g28_forms_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g28_forms_route",
        script_id=SCRIPT_ID,
        name="Group 28 pairing/incidence forms route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "bilinear pairing is not assumed",
            "incidence/routing are candidate forms only",
            "projection/quotient forms are not treated as active O",
            "support separation is auxiliary only",
            "recovery does not define the form",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "inner_product_by_habit",
        "zero_incidence_by_naming",
        "projection_algebra_as_O",
        "quotient_hides_residual",
        "graph_edge_by_desire",
        "support_as_full_proof",
        "coefficient_split_as_insertion",
        "recovery_defined_form",
        "form_inventory_opens_parent",
        "form_inventory_as_residual_control",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; no-overlap form inventory is not theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g28_forms_not_theorem",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "No bilinear pairing is derived, so ordinary orthogonality cannot be claimed. Incidence matrix and routing graph are the best current candidate forms. "
            "Projection and quotient forms remain underdetermined and risk smuggling active O or hiding residual geometry. Support separation is insufficient alone. "
            "Divergence-safe and coefficient-induced forms remain underdetermined. No form licenses active O, residual control, insertion, or parent closure."
        ),
        derivation_ids=["g28_pair_forms"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Pairing Incidence Forms")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    forms = build_form_candidates()
    tests = build_tests()
    requirements = build_requirements()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_form_candidates(forms, out)
    case_3_tests(tests, out)
    case_4_requirements(requirements, out)
    case_5_shortcuts(shortcuts, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
