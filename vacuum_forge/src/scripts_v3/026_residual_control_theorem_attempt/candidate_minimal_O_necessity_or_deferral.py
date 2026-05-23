# Candidate minimal O necessity or deferral
#
# Group:
#   26_residual_control_theorem_attempt
#
# Script type:
#   CLASSIFICATION / CONTROLLED OBSTRUCTION FOLLOW-UP
#
# Purpose
# -------
# Classify active O after the non-O residual-control obstruction test.
#
# Locked-door question:
#
#   Is active O necessary, optional, deferred, or only a rejected shortcut?
#
# This script does not derive active no-overlap O.
# It does not derive residual kill.
# It does not derive strict non-metric inertness.
# It does not derive zeta/kappa non-reentry.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# It classifies O status under the current licensed ledger:
#
#   non-O residual control has not closed,
#   zeta/kappa geometric residuals are the sharp obstruction,
#   accounting residuals are only partially reduced,
#   insertion law and coefficient origin remain missing.
#
# Tiny goblin rule:
#
#   Need a key? Maybe. Still no fake key.

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
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE": StatusMark.DEFER,
        "CONDITIONALLY_REQUIRED": StatusMark.DEFER,
        "DEFERRED": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPTIONAL_OPEN": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "problem_ledger_dep_26",
            "26_residual_control_theorem_attempt__candidate_residual_control_theorem_problem_ledger",
            "residual_control_theorem_problem_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "zeta_kappa_dep_26",
            "26_residual_control_theorem_attempt__candidate_zeta_kappa_nonreentry_theorem_attempt",
            "zeta_kappa_nonreentry_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "epsilon_ekappa_dep_26",
            "26_residual_control_theorem_attempt__candidate_epsilon_ekappa_inertness_theorem_attempt",
            "epsilon_ekappa_inertness_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "nonO_obstruction_dep_26",
            "26_residual_control_theorem_attempt__candidate_residual_control_without_active_O_obstruction",
            "residual_control_without_active_O_obstruction_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_O_burden_dep_26",
            "25_residual_kill_or_no_overlap_theorem__candidate_no_overlap_operator_minimum_burden",
            "no_overlap_operator_minimum_burden_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_reentry_dep_26",
            "25_residual_kill_or_no_overlap_theorem__candidate_residual_reentry_exclusion_audit",
            "residual_reentry_exclusion_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_summary_dep_26",
            "25_residual_kill_or_no_overlap_theorem__candidate_group_25_residual_kill_status_summary",
            "group25_residual_kill_status_summary_marker_25",
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
class OClassificationLedger:
    nonO_closure_gap: sp.Symbol
    geometric_reentry_gap: sp.Symbol
    accounting_partial_gap: sp.Symbol
    insertion_law_gap: sp.Symbol
    coefficient_origin_gap: sp.Symbol
    O_structure_gap: sp.Symbol
    O_recovery_independence_gap: sp.Symbol
    O_classification_load: sp.Expr


@dataclass
class OStatusOption:
    name: str
    option: str
    status: str
    condition: str
    current_classification: str


@dataclass
class ODependencyTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class RejectedOClassifierShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


@dataclass
class OClassificationConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_ledger() -> OClassificationLedger:
    (
        nonO_closure_gap,
        geometric_reentry_gap,
        accounting_partial_gap,
        insertion_law_gap,
        coefficient_origin_gap,
        O_structure_gap,
        O_recovery_independence_gap,
    ) = sp.symbols(
        "nonO_closure_gap geometric_reentry_gap accounting_partial_gap insertion_law_gap coefficient_origin_gap O_structure_gap O_recovery_independence_gap",
        real=True,
    )

    O_classification_load = sp.simplify(
        nonO_closure_gap
        + geometric_reentry_gap
        + accounting_partial_gap
        + insertion_law_gap
        + coefficient_origin_gap
        + O_structure_gap
        + O_recovery_independence_gap
    )

    return OClassificationLedger(
        nonO_closure_gap=nonO_closure_gap,
        geometric_reentry_gap=geometric_reentry_gap,
        accounting_partial_gap=accounting_partial_gap,
        insertion_law_gap=insertion_law_gap,
        coefficient_origin_gap=coefficient_origin_gap,
        O_structure_gap=O_structure_gap,
        O_recovery_independence_gap=O_recovery_independence_gap,
        O_classification_load=O_classification_load,
    )


def build_status_options() -> List[OStatusOption]:
    return [
        OStatusOption(
            name="O1: O_REQUIRED",
            option="active O is required for residual control",
            status="NOT_DERIVED",
            condition="all non-O routes are formally blocked and residual control still requires a separator/projection theorem",
            current_classification="not proven; current obstruction is controlled but not an impossibility theorem",
        ),
        OStatusOption(
            name="O2: O_OPTIONAL_OPEN",
            option="active O remains one open route among others",
            status="OPTIONAL_OPEN",
            condition="non-O routes are not closed but also not formally impossible; insertion law or coefficient origin may still change the residual-control picture",
            current_classification="best current classification",
        ),
        OStatusOption(
            name="O3: O_DEFERRED_TO_INSERTION",
            option="active O classification depends on B_s/F_zeta insertion law or coefficient origin",
            status="DEFERRED",
            condition="zeta residual split cannot be evaluated until insertion law/coefficient origin is specified",
            current_classification="also live; insertion-law dependency remains open",
        ),
        OStatusOption(
            name="O4: O_REJECTED_AS_SHORTCUT",
            option="active O is being used only as eraser by name",
            status="REJECTED",
            condition="O has no domain/codomain/kernel/image/composition/pairing/divergence/boundary/source/mass/support/recovery-independence structure",
            current_classification="rejected whenever O is invoked without full burden",
        ),
        OStatusOption(
            name="O5: O_DERIVED",
            option="active O exists as a real no-overlap operator",
            status="NOT_DERIVED",
            condition="full O operator structure and compatibility behavior are derived",
            current_classification="not derived",
        ),
    ]


def build_dependency_tests() -> List[ODependencyTest]:
    return [
        ODependencyTest(
            name="T1: non-O closure test",
            test="have non-O routes closed residual control?",
            status="BLOCKED",
            result="no; direct kill, full inertness, zeta/kappa non-reentry, and full accounting inertness are not derived",
            implication="active O remains live but not proven necessary",
        ),
        ODependencyTest(
            name="T2: geometric residual separator test",
            test="is an O-like separator needed to separate zeta/kappa residual geometry?",
            status="NOT_DERIVED",
            result="not derived; zeta/kappa remain blocked by insertion law, coefficient origin, non-reentry, or active O",
            implication="O may be useful, but necessity is not proven",
        ),
        ODependencyTest(
            name="T3: insertion-law dependency test",
            test="could B_s/F_zeta insertion law change the O classification?",
            status="DEFERRED",
            result="yes; zeta residual non-reentry may depend on insertion law and coefficient origin",
            implication="O necessity should not be declared before insertion/coefficient dependency is resolved",
        ),
        ODependencyTest(
            name="T4: O burden test",
            test="is active O currently derivable from existing structure?",
            status="NOT_DERIVED",
            result="no; domain, codomain, kernel, image, composition, pairing, divergence, boundary, source, mass, scalar/current/support behavior, and recovery independence remain open",
            implication="active O cannot be used yet",
        ),
        ODependencyTest(
            name="T5: shortcut rejection test",
            test="can O be used as a placeholder eraser while structure is missing?",
            status="REJECTED",
            result="no; O by name is rejected",
            implication="O may be target, not tool",
        ),
        ODependencyTest(
            name="T6: parent/insertion gate test",
            test="does O classification open B_s/F_zeta insertion or parent equation?",
            status="NOT_READY",
            result="no; classification does not derive O, insertion, or parent closure",
            implication="downstream gates stay closed",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedOClassifierShortcut]:
    return [
        RejectedOClassifierShortcut(
            name="S1: O declared required by frustration",
            shortcut="declare O required because non-O routes have not closed yet",
            forbidden_use="lack of current proof upgraded to necessity theorem",
            status="REJECTED",
            consequence="controlled obstruction becomes overclaim",
        ),
        RejectedOClassifierShortcut(
            name="S2: O optional means O usable",
            shortcut="treat optional-open O as available operator",
            forbidden_use="classification status used as construction",
            status="REJECTED",
            consequence="active O burden is bypassed",
        ),
        RejectedOClassifierShortcut(
            name="S3: O deferred means insertion solved",
            shortcut="treat O deferral to insertion law as B_s/F_zeta insertion theorem",
            forbidden_use="dependency classification replaces insertion law",
            status="REJECTED",
            consequence="metric recombination is smuggled",
        ),
        RejectedOClassifierShortcut(
            name="S4: O by placeholder",
            shortcut="use O as eraser because it is named no-overlap",
            forbidden_use="operator name replaces domain/kernel/image/pairing/divergence/boundary/source structure",
            status="REJECTED",
            consequence="fake O eraser returns",
        ),
        RejectedOClassifierShortcut(
            name="S5: O selected by recovery",
            shortcut="choose O because Schwarzschild/gamma/AB/B=1/A/PPN recovery needs it",
            forbidden_use="recovery target selects operator",
            status="REJECTED",
            consequence="recovery constructs residual control",
        ),
        RejectedOClassifierShortcut(
            name="S6: O selected by boundary/source failure",
            shortcut="choose O to repair tail, flux, shell, support, or source duplication",
            forbidden_use="repair need selects operator",
            status="REJECTED",
            consequence="boundary/source repair is smuggled",
        ),
        RejectedOClassifierShortcut(
            name="S7: O classification licenses insertion",
            shortcut="O status classification licenses B_s/F_zeta insertion",
            forbidden_use="classification replaces insertion theorem",
            status="REJECTED",
            consequence="metric insertion gate opens falsely",
        ),
        RejectedOClassifierShortcut(
            name="S8: O classification opens parent",
            shortcut="O status classification opens parent equation",
            forbidden_use="classification replaces parent identity and divergence closure",
            status="REJECTED",
            consequence="parent gate opens falsely",
        ),
    ]


def build_conclusions() -> List[OClassificationConclusion]:
    return [
        OClassificationConclusion(
            name="C1: O necessity",
            conclusion="not proven",
            status="NOT_DERIVED",
            meaning="current non-O obstruction is not enough to prove active O mathematically necessary",
        ),
        OClassificationConclusion(
            name="C2: O optional-open",
            conclusion="best current classification",
            status="OPTIONAL_OPEN",
            meaning="active O remains a live theorem route, but non-O routes and insertion/coefficient dependency are not formally exhausted",
        ),
        OClassificationConclusion(
            name="C3: O deferred-to-insertion",
            conclusion="also live",
            status="DEFERRED",
            meaning="B_s/F_zeta insertion law and coefficient origin may decide whether O is required",
        ),
        OClassificationConclusion(
            name="C4: O as shortcut",
            conclusion="rejected",
            status="REJECTED",
            meaning="O cannot be used without full operator structure and compatibility behavior",
        ),
        OClassificationConclusion(
            name="C5: next route",
            conclusion="audit surviving residual-control route against boundary/source/recovery consistency",
            status="SAFE_IF",
            meaning="since O is optional-open/deferred and not usable, the next step should test consistency of the current obstruction/handoff state",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Minimal O necessity or deferral problem")
    print("Question:")
    print()
    print("  Is active O necessary, optional, deferred, or only a rejected shortcut?")
    print()
    print("Reference discipline:")
    print()
    print("  Non-O residual control has not closed, but that is not yet a mathematical no-go theorem.")
    print("  O cannot be used unless full operator structure is derived.")
    print("  O necessity may be blocked by missing insertion law and coefficient origin.")

    with out.governance_assessments():
        out.line(
            "minimal O necessity/deferral classifier opened",
            StatusMark.INFO,
            "classifying active O after controlled non-O obstruction without deriving O",
        )


def case_1_classification_ledger(ledger: OClassificationLedger, out: ScriptOutput) -> None:
    header("Case 1: O classification gap ledger")
    print("Classification gaps:")
    print()
    for name in [
        "nonO_closure_gap",
        "geometric_reentry_gap",
        "accounting_partial_gap",
        "insertion_law_gap",
        "coefficient_origin_gap",
        "O_structure_gap",
        "O_recovery_independence_gap",
    ]:
        print(f"  {name} = {sp.sstr(getattr(ledger, name))}")
    print()
    print("O classification load:")
    print()
    print(f"  L_O_classification = {sp.sstr(ledger.O_classification_load)}")
    print()
    print("Interpretation:")
    print()
    print("  O necessity cannot be asserted while insertion/coefficient and O-structure gaps remain open.")
    print("  O usability cannot be asserted while O_structure_gap remains open.")

    with out.derived_results():
        out.line(
            "O classification gap load stated",
            StatusMark.OBLIGATION,
            f"L_O_classification = {sp.sstr(ledger.O_classification_load)}",
        )


def case_2_status_options(options: List[OStatusOption], out: ScriptOutput) -> None:
    header("Case 2: O status options")
    for option in options:
        print()
        print("-" * 120)
        print(option.name)
        print("-" * 120)
        print(f"Option: {option.option}")
        print(f"[{status_mark(option.status).value}] {option.name}: {option.status}")
        print(f"Condition: {option.condition}")
        print(f"Current classification: {option.current_classification}")

    with out.governance_assessments():
        out.line(
            "active O status options classified",
            StatusMark.PASS,
            f"{len(options)} O status options classified",
        )


def case_3_dependency_tests(tests: List[ODependencyTest], out: ScriptOutput) -> None:
    header("Case 3: O dependency tests")
    for test in tests:
        print()
        print("-" * 120)
        print(test.name)
        print("-" * 120)
        print(f"Test: {test.test}")
        print(f"[{status_mark(test.status).value}] {test.name}: {test.status}")
        print(f"Result: {test.result}")
        print(f"Implication: {test.implication}")

    with out.governance_assessments():
        out.line(
            "active O dependency tests completed",
            StatusMark.PASS,
            f"{len(tests)} dependency tests evaluated; O remains optional-open/deferred and not derived",
        )


def case_4_rejected_shortcuts(shortcuts: List[RejectedOClassifierShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected O-classification shortcuts")
    for shortcut in shortcuts:
        print()
        print("-" * 120)
        print(shortcut.name)
        print("-" * 120)
        print(f"Shortcut: {shortcut.shortcut}")
        print(f"Forbidden use: {shortcut.forbidden_use}")
        print(f"[{status_mark(shortcut.status).value}] {shortcut.name}: {shortcut.status}")
        print(f"Consequence: {shortcut.consequence}")

    with out.counterexamples():
        out.line(
            "O-classification shortcuts rejected",
            StatusMark.FAIL,
            "necessity-by-frustration, optional-as-usable, deferral-as-insertion, placeholder O, recovery/repair-selected O, insertion, and parent shortcuts are rejected",
        )


def case_5_conclusions(conclusions: List[OClassificationConclusion], out: ScriptOutput) -> None:
    header("Case 5: O classification conclusions")
    for conclusion in conclusions:
        print()
        print("-" * 120)
        print(conclusion.name)
        print("-" * 120)
        print(f"Conclusion: {conclusion.conclusion}")
        print(f"[{status_mark(conclusion.status).value}] {conclusion.name}: {conclusion.status}")
        print(f"Meaning: {conclusion.meaning}")

    with out.governance_assessments():
        out.line(
            "minimal O necessity/deferral classification stated",
            StatusMark.DEFER,
            "active O is optional-open/deferred, not required by theorem and not available as operator",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The minimal O necessity/deferral classifier fails if a later script allows:")
    print()
    print("1. O declared necessary from frustration alone")
    print("2. optional-open O treated as usable operator")
    print("3. deferred O treated as insertion theorem")
    print("4. O used without domain/codomain/kernel/image")
    print("5. O used without composition/pairing/no-overlap criterion")
    print("6. O used without derivative/divergence behavior")
    print("7. O used without boundary/source/mass/scalar/current/support behavior")
    print("8. O selected from recovery or boundary/source failure")
    print("9. O classification licenses B_s/F_zeta insertion")
    print("10. O classification opens parent equation")

    with out.governance_assessments():
        out.line(
            "O classification failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not convert O classification into active O theorem, insertion, or parent closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Minimal O necessity/deferral result:")
    print()
    print("  Active O is not proven mathematically necessary.")
    print("  Active O is not derived.")
    print("  Active O remains optional-open and deferred to missing insertion/coefficient and operator-structure theorems.")
    print("  Active O is rejected as a shortcut whenever invoked without full structure.")
    print("  Under current licensed objects, non-O residual control has not closed, but this is not enough to use O.")
    print("  B_s/F_zeta insertion and parent closure remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_residual_control_boundary_source_recovery_consistency.py")
    print()
    print("Tiny goblin label:")
    print("  Need a key? Maybe. Still no fake key.")

    with out.governance_assessments():
        out.line(
            "minimal O necessity/deferral classifier complete",
            StatusMark.PASS,
            "O optional-open/deferred; O not derived and not usable as shortcut",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: OClassificationLedger) -> None:
    ns.record_derivation(
        derivation_id="minimal_O_classification_load_26",
        inputs=[
            ledger.nonO_closure_gap,
            ledger.geometric_reentry_gap,
            ledger.accounting_partial_gap,
            ledger.insertion_law_gap,
            ledger.coefficient_origin_gap,
            ledger.O_structure_gap,
            ledger.O_recovery_independence_gap,
        ],
        output=ledger.O_classification_load,
        method="sum active-O classification gaps after non-O obstruction",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="minimal_O_classification_ledger",
        scope="Group 26 residual control theorem attempt",
    )

    ns.record_derivation(
        derivation_id="minimal_O_necessity_or_deferral_marker_26",
        inputs=[
            sp.Symbol("nonO_obstruction"),
            sp.Symbol("geometric_reentry_open"),
            sp.Symbol("insertion_law_open"),
            sp.Symbol("coefficient_origin_open"),
            sp.Symbol("O_structure_open"),
        ],
        output=sp.Symbol("O_optional_open_deferred_not_derived"),
        method="Group 26 minimal active-O necessity or deferral classification",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="classification_marker",
        scope="Group 26 residual control theorem attempt",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g26_do_not_claim_O_required_without_no_go", "Do not claim O required without formal no-go theorem"),
        ("g26_keep_O_optional_open", "Keep active O optional-open unless necessity is derived"),
        ("g26_track_O_deferral_to_insertion", "Track O deferral to insertion law and coefficient origin"),
        ("g26_derive_O_structure_before_use", "Derive active O structure before use"),
        ("g26_derive_O_recovery_independence_before_use", "Derive O recovery independence before use"),
        ("g26_reject_O_as_shortcut", "Reject active O as shortcut"),
        ("g26_keep_insertion_parent_closed_after_O_classification", "Keep insertion and parent gates closed after O classification"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g26_minimal_O_necessity_or_deferral_route"],
            description=(
                "Active O remains optional-open/deferred and not derived. It may not be used without full operator structure and recovery independence."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g26_do_not_claim_O_required_without_no_go",
        "g26_keep_O_optional_open",
        "g26_track_O_deferral_to_insertion",
        "g26_derive_O_structure_before_use",
        "g26_derive_O_recovery_independence_before_use",
        "g26_reject_O_as_shortcut",
        "g26_keep_insertion_parent_closed_after_O_classification",
    ]

    ns.record_route(RouteRecord(
        route_id="g26_minimal_O_necessity_or_deferral_route",
        script_id=SCRIPT_ID,
        name="Group 26 minimal active-O necessity or deferral classifier",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "O necessity is not claimed without formal no-go theorem",
            "O remains optional-open/deferred while insertion law and coefficient origin remain open",
            "O is not used without full operator structure",
            "O is not selected from recovery or repair needs",
            "insertion and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "O_required_by_frustration",
        "optional_O_used_as_operator",
        "deferred_O_treated_as_insertion",
        "O_without_domain_kernel_image",
        "O_without_composition_pairing",
        "O_without_divergence_boundary_source_behavior",
        "O_selected_from_recovery",
        "O_selected_from_boundary_source_failure",
        "O_classification_licenses_insertion",
        "O_classification_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_26",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; O classification cannot replace active-O theorem, insertion, or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_O_optional_open_deferred_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Active O is not proven mathematically necessary, is not derived, and is not usable as a shortcut. "
            "It remains optional-open and deferred to missing insertion/coefficient and operator-structure theorems. "
            "O classification does not license B_s/F_zeta insertion or parent closure."
        ),
        derivation_ids=[
            "minimal_O_classification_load_26",
            "minimal_O_necessity_or_deferral_marker_26",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Minimal O Necessity Or Deferral")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    options = build_status_options()
    tests = build_dependency_tests()
    shortcuts = build_rejected_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_classification_ledger(ledger, out)
    case_2_status_options(options, out)
    case_3_dependency_tests(tests, out)
    case_4_rejected_shortcuts(shortcuts, out)
    case_5_conclusions(conclusions, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
