# Candidate O boundary source mass
#
# Group:
#   27_active_O_construction
#
# Script type:
#   BOUNDARY / SOURCE / MASS COMPATIBILITY AUDIT
#
# Purpose
# -------
# Audit whether candidate active O can preserve boundary neutrality, source
# no-double-counting, mass behavior, scalar-tail/current-flux neutrality, and
# support/matching guardrails.
#
# Locked-door question:
#
#   Does O preserve boundary neutrality, source no-double-counting, and A-sector mass?
#
# This script does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   No hiding leaks under the operator rug.

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
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE": StatusMark.DEFER,
        "CONDITIONALLY_SAFE": StatusMark.INFO,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PRESERVED_IF": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        ("g27_O_problem", "027_active_O_construction__candidate_O_problem_ledger", "g27_O_problem", RecordKind.INVENTORY_MARKER),
        ("g27_dc", "027_active_O_construction__candidate_O_domain_codomain", "g27_O_domain_codomain", RecordKind.INVENTORY_MARKER),
        ("g27_ki", "027_active_O_construction__candidate_O_kernel_image", "g27_O_kernel_image", RecordKind.INVENTORY_MARKER),
        ("g27_pair", "027_active_O_construction__candidate_O_no_overlap_pairing", "g27_O_pairing", RecordKind.INVENTORY_MARKER),
        ("g27_alg", "027_active_O_construction__candidate_O_projection_law", "g27_O_alg_law", RecordKind.INVENTORY_MARKER),
        ("g27_div", "027_active_O_construction__candidate_O_divergence_commutation", "g27_O_divergence", RecordKind.INVENTORY_MARKER),
        ("g26_summary", "026_residual_control_theorem_attempt__candidate_group_26_status_summary", "g26_status_summary", RecordKind.INVENTORY_MARKER),
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
    for attr in ("routes_path", "branch_decisions_path", "claims_path", "obligations_path", "derivations_path", "governance_path"):
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
class BoundarySourceMassSymbols:
    O: sp.Symbol
    M_A: sp.Symbol
    tail_scalar: sp.Symbol
    flux_current: sp.Symbol
    shell_load: sp.Symbol
    source_load: sp.Symbol
    support_load: sp.Symbol
    mass_gap: sp.Symbol
    scalar_gap: sp.Symbol
    current_gap: sp.Symbol
    boundary_gap: sp.Symbol
    source_gap: sp.Symbol
    shell_gap: sp.Symbol
    support_gap: sp.Symbol
    bsm_gap: sp.Expr


@dataclass
class BSMCandidate:
    name: str
    candidate: str
    status: str
    works_if: str
    hazard: str


@dataclass
class BSMTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class BSMRequirement:
    name: str
    requirement: str
    status: str
    required_for: str
    fails_if: str


@dataclass
class RejectedBSMShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class BSMConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> BoundarySourceMassSymbols:
    (
        O,
        M_A,
        tail_scalar,
        flux_current,
        shell_load,
        source_load,
        support_load,
        mass_gap,
        scalar_gap,
        current_gap,
        boundary_gap,
        source_gap,
        shell_gap,
        support_gap,
    ) = sp.symbols(
        "O M_A tail_scalar flux_current shell_load source_load support_load "
        "mass_gap scalar_gap current_gap boundary_gap source_gap shell_gap support_gap",
        real=True,
    )

    bsm_gap = sp.simplify(
        mass_gap + scalar_gap + current_gap + boundary_gap + source_gap + shell_gap + support_gap
    )

    return BoundarySourceMassSymbols(
        O=O,
        M_A=M_A,
        tail_scalar=tail_scalar,
        flux_current=flux_current,
        shell_load=shell_load,
        source_load=source_load,
        support_load=support_load,
        mass_gap=mass_gap,
        scalar_gap=scalar_gap,
        current_gap=current_gap,
        boundary_gap=boundary_gap,
        source_gap=source_gap,
        shell_gap=shell_gap,
        support_gap=support_gap,
        bsm_gap=bsm_gap,
    )


def build_candidates() -> List[BSMCandidate]:
    return [
        BSMCandidate(
            name="B1: mass-neutral O",
            candidate="O does not shift A-sector mass M_A",
            status="UNDERDETERMINED",
            works_if="O action is proven not to move residuals into A-sector mass",
            hazard="mass shift hidden as residual cleanup",
        ),
        BSMCandidate(
            name="B2: scalar-tail-neutral O",
            candidate="O creates no scalar tail at boundary",
            status="UNDERDETERMINED",
            works_if="boundary scalar-tail behavior is explicitly derived",
            hazard="tail is hidden by projection/replacement language",
        ),
        BSMCandidate(
            name="B3: current-flux-neutral O",
            candidate="O creates no non-A current flux channel",
            status="UNDERDETERMINED",
            works_if="current behavior is explicitly derived",
            hazard="current leakage becomes invisible residual route",
        ),
        BSMCandidate(
            name="B4: source-neutral O",
            candidate="O creates no ordinary source duplication or source reservoir",
            status="UNDERDETERMINED",
            works_if="source routing remains auditable and unchanged",
            hazard="O correction/residual image becomes hidden source",
        ),
        BSMCandidate(
            name="B5: shell/support-neutral O",
            candidate="O creates no shell, seam, smoothing, transition, or support load",
            status="UNDERDETERMINED",
            works_if="support/matching behavior is explicitly derived",
            hazard="support layer hides residual cleanup",
        ),
        BSMCandidate(
            name="B6: repair-selected O",
            candidate="choose O because it fixes boundary/source/mass failure",
            status="REJECTED",
            works_if="never allowed",
            hazard="repair need constructs O",
        ),
    ]


def build_tests() -> List[BSMTest]:
    return [
        BSMTest(
            name="T1: A-sector mass test",
            test="can O be asserted mass-neutral now?",
            status="NOT_DERIVED",
            result="no; mass behavior is not derived",
            implication="mass neutrality remains open",
        ),
        BSMTest(
            name="T2: scalar-tail test",
            test="can O be asserted scalar-tail-neutral now?",
            status="NOT_DERIVED",
            result="no; boundary scalar-tail behavior is not derived",
            implication="boundary neutrality remains open",
        ),
        BSMTest(
            name="T3: current-flux test",
            test="can O be asserted current-flux-neutral now?",
            status="NOT_DERIVED",
            result="no; current behavior is not derived",
            implication="current neutrality remains open",
        ),
        BSMTest(
            name="T4: source no-double-counting test",
            test="can O be asserted source-neutral now?",
            status="NOT_DERIVED",
            result="no; source behavior is not derived",
            implication="source no-double-counting remains open",
        ),
        BSMTest(
            name="T5: support/matching test",
            test="can O be asserted support-neutral now?",
            status="NOT_DERIVED",
            result="no; support/matching behavior is not derived",
            implication="support neutrality remains open",
        ),
        BSMTest(
            name="T6: repair-selection test",
            test="can boundary/source/mass failure select O?",
            status="REJECTED",
            result="no; repair need may reject a candidate O but cannot define it",
            implication="O must be recovery/repair independent",
        ),
    ]


def build_requirements() -> List[BSMRequirement]:
    return [
        BSMRequirement(
            name="R1: no A-mass shift",
            requirement="O must not move residual cleanup into A-sector mass",
            status="REQUIRED",
            required_for="mass neutrality",
            fails_if="O changes M_A or hides mass correction",
        ),
        BSMRequirement(
            name="R2: no scalar tail",
            requirement="O must not create boundary scalar-tail leakage",
            status="REQUIRED",
            required_for="boundary neutrality",
            fails_if="O creates or hides scalar tail",
        ),
        BSMRequirement(
            name="R3: no current flux",
            requirement="O must not create non-A current-flux leakage",
            status="REQUIRED",
            required_for="current neutrality",
            fails_if="O creates current channel",
        ),
        BSMRequirement(
            name="R4: no ordinary source duplication",
            requirement="O must not create or hide ordinary source load",
            status="REQUIRED",
            required_for="source no-double-counting",
            fails_if="O residual image or correction carries ordinary source role",
        ),
        BSMRequirement(
            name="R5: no shell/support load",
            requirement="O must not create shell, seam, smoothing, transition, or support load",
            status="REQUIRED",
            required_for="support/matching neutrality",
            fails_if="O support layer carries cleanup",
        ),
        BSMRequirement(
            name="R6: no downstream gate",
            requirement="boundary/source/mass compatibility does not license insertion or parent closure",
            status="REQUIRED",
            required_for="downstream gate protection",
            fails_if="compatibility audit opens B_s/F_zeta insertion or parent equation",
        ),
    ]


def build_shortcuts() -> List[RejectedBSMShortcut]:
    return [
        RejectedBSMShortcut(
            name="S1: mass neutrality by label",
            shortcut="declare O mass-neutral by naming it no-overlap",
            status="REJECTED",
            reason="mass behavior must be derived",
        ),
        RejectedBSMShortcut(
            name="S2: boundary repair as O",
            shortcut="choose O to cancel boundary scalar-tail or shell failure",
            status="REJECTED",
            reason="boundary failure cannot construct O",
        ),
        RejectedBSMShortcut(
            name="S3: source repair as O",
            shortcut="choose O to cancel ordinary source duplication",
            status="REJECTED",
            reason="source failure cannot construct O",
        ),
        RejectedBSMShortcut(
            name="S4: support hiding",
            shortcut="hide residual cleanup in smoothing/support/matching data",
            status="REJECTED",
            reason="support data cannot be cleanup reservoir",
        ),
        RejectedBSMShortcut(
            name="S5: current neutrality by label",
            shortcut="declare O current-neutral without current behavior",
            status="REJECTED",
            reason="current flux behavior must be derived",
        ),
        RejectedBSMShortcut(
            name="S6: compatibility licenses insertion",
            shortcut="use boundary/source/mass compatibility as B_s/F_zeta insertion law",
            status="REJECTED",
            reason="insertion law remains separate",
        ),
        RejectedBSMShortcut(
            name="S7: compatibility opens parent",
            shortcut="use boundary/source/mass compatibility as parent readiness",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_conclusions() -> List[BSMConclusion]:
    return [
        BSMConclusion(
            name="C1: mass behavior",
            conclusion="A-sector mass neutrality is not derived",
            status="NOT_DERIVED",
            meaning="O mass behavior remains open",
        ),
        BSMConclusion(
            name="C2: boundary/current behavior",
            conclusion="scalar-tail and current-flux neutrality are not derived",
            status="NOT_DERIVED",
            meaning="boundary/current behavior remains open",
        ),
        BSMConclusion(
            name="C3: source behavior",
            conclusion="source no-double-counting is not derived for O",
            status="NOT_DERIVED",
            meaning="O source behavior remains open",
        ),
        BSMConclusion(
            name="C4: support behavior",
            conclusion="support/matching neutrality is not derived",
            status="NOT_DERIVED",
            meaning="O support behavior remains open",
        ),
        BSMConclusion(
            name="C5: next route",
            conclusion="recovery independence must be audited next",
            status="OPEN",
            meaning="O must not be selected from recovery after guardrail risks are exposed",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: O boundary/source/mass problem")
    print("Question:")
    print()
    print("  Does O preserve boundary neutrality, source no-double-counting, and A-sector mass?")
    print()
    print("Reference discipline:")
    print()
    print("  O cannot be selected from repair needs.")
    print("  O cannot hide leakage in mass, scalar tail, current flux, shell, source, or support data.")
    print("  Compatibility is not insertion or parent closure.")

    with out.governance_assessments():
        out.line(
            "O boundary/source/mass audit opened",
            StatusMark.INFO,
            "testing O compatibility with mass, boundary, current, source, shell, and support guardrails",
        )


def case_1_symbol_ledger(symbols: BoundarySourceMassSymbols, out: ScriptOutput) -> None:
    header("Case 1: Boundary/source/mass symbolic ledger")
    print("Guardrail symbols:")
    print()
    print(f"  M_A          = {sp.sstr(symbols.M_A)}")
    print(f"  tail_scalar  = {sp.sstr(symbols.tail_scalar)}")
    print(f"  flux_current = {sp.sstr(symbols.flux_current)}")
    print(f"  shell_load   = {sp.sstr(symbols.shell_load)}")
    print(f"  source_load  = {sp.sstr(symbols.source_load)}")
    print(f"  support_load = {sp.sstr(symbols.support_load)}")
    print()
    print("Boundary/source/mass gap:")
    print()
    print(f"  L_O_bsm_gap = {sp.sstr(symbols.bsm_gap)}")

    with out.derived_results():
        out.line(
            "O boundary/source/mass gap stated",
            StatusMark.OBLIGATION,
            f"L_O_bsm_gap = {sp.sstr(symbols.bsm_gap)}",
        )


def case_2_candidates(items: List[BSMCandidate], out: ScriptOutput) -> None:
    header("Case 2: Candidate boundary/source/mass behaviors")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Works if: {item.works_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "O boundary/source/mass candidates classified",
            StatusMark.PASS,
            f"{len(items)} candidates classified",
        )


def case_3_tests(items: List[BSMTest], out: ScriptOutput) -> None:
    header("Case 3: Boundary/source/mass tests")
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
            "O boundary/source/mass tests completed",
            StatusMark.DEFER,
            "mass, boundary, current, source, and support neutrality are not derived",
        )


def case_4_requirements(items: List[BSMRequirement], out: ScriptOutput) -> None:
    header("Case 4: Boundary/source/mass requirements")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Requirement: {item.requirement}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Required for: {item.required_for}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "O boundary/source/mass requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} requirements remain open",
        )


def case_5_shortcuts(items: List[RejectedBSMShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected boundary/source/mass shortcuts")
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
            "O boundary/source/mass shortcuts rejected",
            StatusMark.FAIL,
            "mass neutrality by label, boundary/source repair, support hiding, current neutrality by label, insertion, and parent shortcuts are rejected",
        )


def case_6_conclusions(items: List[BSMConclusion], out: ScriptOutput) -> None:
    header("Case 6: Boundary/source/mass conclusions")
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
            "O boundary/source/mass conclusion stated",
            StatusMark.DEFER,
            "O guardrail behavior not derived; recovery independence is next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("O boundary/source/mass result:")
    print()
    print("  A-sector mass neutrality is not derived.")
    print("  scalar-tail neutrality is not derived.")
    print("  current-flux neutrality is not derived.")
    print("  source no-double-counting is not derived for O.")
    print("  support/matching neutrality is not derived.")
    print("  boundary/source/mass failure may reject O but cannot select O.")
    print("  compatibility does not license insertion or parent closure.")
    print("  recovery independence must be audited next.")
    print("  O is not derived by this script.")
    print()
    print("Possible next script:")
    print("  candidate_O_recovery_independence.py")
    print()
    print("Tiny goblin label:")
    print("  No hiding leaks under the operator rug.")

    with out.governance_assessments():
        out.line(
            "O boundary/source/mass audit complete",
            StatusMark.PASS,
            "guardrail behavior not derived; recovery independence remains next",
        )


def record_derivations(ns, symbols: BoundarySourceMassSymbols) -> None:
    ns.record_derivation(
        derivation_id="g27_O_bsm",
        inputs=[
            symbols.mass_gap,
            symbols.scalar_gap,
            symbols.current_gap,
            symbols.boundary_gap,
            symbols.source_gap,
            symbols.shell_gap,
            symbols.support_gap,
        ],
        output=symbols.bsm_gap,
        method="state active-O boundary/source/mass guardrail gaps",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="O_bsm_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_bsm_mass", "Derive O A-sector mass neutrality"),
        ("g27_bsm_scalar", "Derive O scalar-tail neutrality"),
        ("g27_bsm_current", "Derive O current-flux neutrality"),
        ("g27_bsm_source", "Derive O source no-double-counting"),
        ("g27_bsm_support", "Derive O support/matching neutrality"),
        ("g27_bsm_no_repair", "Prevent repair-selected O"),
        ("g27_bsm_no_downstream", "Keep insertion and parent gates closed"),
        ("g27_bsm_next_recovery", "Audit recovery independence next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_bsm_route"],
            description=(
                "O boundary/source/mass behavior is not derived here. Guardrail failure may reject O but cannot construct it."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_bsm_mass",
        "g27_bsm_scalar",
        "g27_bsm_current",
        "g27_bsm_source",
        "g27_bsm_support",
        "g27_bsm_no_repair",
        "g27_bsm_no_downstream",
        "g27_bsm_next_recovery",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_bsm_route",
        script_id=SCRIPT_ID,
        name="Group 27 O boundary/source/mass route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "mass neutrality is not assumed",
            "boundary/source/current/support neutrality is not assumed",
            "guardrail failure may reject O but not select O",
            "insertion and parent gates remain closed",
            "recovery independence remains next",
        ],
    ))

    for branch_id in [
        "mass_neutral_by_label",
        "boundary_repair_as_O",
        "source_repair_as_O",
        "support_hiding",
        "current_neutral_by_label",
        "bsm_licenses_insertion",
        "bsm_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; O boundary/source/mass behavior must be derived and cannot open downstream gates.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_bsm_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "O boundary/source/mass behavior is not derived. A-sector mass neutrality, scalar-tail neutrality, current-flux neutrality, "
            "source no-double-counting, and support/matching neutrality remain open. Guardrail failure may reject O but cannot select O. "
            "Compatibility does not license insertion or parent closure; recovery independence must be audited next."
        ),
        derivation_ids=["g27_O_bsm"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate O Boundary Source Mass")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    candidates = build_candidates()
    tests = build_tests()
    requirements = build_requirements()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_candidates(candidates, out)
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
