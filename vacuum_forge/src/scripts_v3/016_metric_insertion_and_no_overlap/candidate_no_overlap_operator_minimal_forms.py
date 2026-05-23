# Candidate no-overlap operator minimal forms
#
# Group:
#   16_metric_insertion_and_no_overlap
#
# Script type:
#   SIEVE
#
# Purpose
# -------
# The residual non-metric bookkeeping audit found:
#
#   residual zeta/kappa may remain useful only as explicitly non-metric
#   diagnostic bookkeeping or first-order non-radiative relaxation.
#
# But it also found:
#
#   non-metric bookkeeping does not define O.
#
# This script tests whether a minimal no-overlap operator O can be more than a label.
#
# Target:
#
#   O[B_s, zeta_residual/kappa_residual, J_V] = 0
#
# Locked-door question:
#
#   Is there a minimal O that actually enforces count-once recombination,
#   rather than merely renaming residual-kill or bookkeeping?
#
# This is a sieve, not a derivation.

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
    ReasonCode,
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
class NoOverlapMinimalEntry:
    name: str
    form: str
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
        dependency_id="residual_nonmetric_bookkeeping_rule_marker",
        upstream_script_id="016_metric_insertion_and_no_overlap__candidate_residual_nonmetric_bookkeeping_rule",
        upstream_derivation_id="residual_nonmetric_bookkeeping_rule_marker",
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


def build_entries() -> List[NoOverlapMinimalEntry]:
    return [
        NoOverlapMinimalEntry(
            name="OM1: minimal O target",
            form="O[B_s, zeta_residual/kappa_residual, J_V] = 0",
            role="core count-once theorem target",
            allowed_if="O has explicit domain, pairing/projector/action, and blocks double-counting",
            forbidden_if="O is only a name for residual-kill or bookkeeping",
            status="THEOREM_TARGET",
            missing="definition of O",
            consequence="decides whether neutral residual metric trace can survive",
        ),
        NoOverlapMinimalEntry(
            name="OM2: orthogonality pairing",
            form="<Trace_B_s, Trace_residual>_O = 0",
            role="minimal mathematical no-overlap candidate",
            allowed_if="pairing is defined by metric/source/accounting structure, not chosen ad hoc",
            forbidden_if="inner product is arbitrary or coordinate/gauge artifact",
            status="CANDIDATE",
            missing="pairing definition and domain",
            consequence="could permit neutral residual if physically meaningful",
        ),
        NoOverlapMinimalEntry(
            name="OM3: projector split",
            form="P_B zeta enters B_s; P_R zeta is residual; P_B P_R = 0",
            role="operator split candidate",
            allowed_if="P_B and P_R are actual projectors with source/domain definitions",
            forbidden_if="projectors are labels for desired outcome",
            status="CANDIDATE",
            missing="projector definitions and composition theorem",
            consequence="natural route but risks bundle-renaming",
        ),
        NoOverlapMinimalEntry(
            name="OM4: metric insertion exclusivity",
            form="metric insertion map I_metric(zeta) = I_B_s(P_B zeta), I_metric(P_R zeta)=0",
            role="direct count-once insertion rule",
            allowed_if="insertion map is explicit and residual non-metric role is fenced",
            forbidden_if="residual later appears in metric source/accounting",
            status="SAFE_IF",
            missing="explicit insertion map and residual fence",
            consequence="equivalent to clean residual-kill convention if P_R is non-metric",
        ),
        NoOverlapMinimalEntry(
            name="OM5: residual-kill as O",
            form="O is implemented by zeta_residual_metric = 0 and kappa_residual_metric = 0/non-metric",
            role="safe convention, not derived operator",
            allowed_if="marked as provisional convention only",
            forbidden_if="called a derived no-overlap operator",
            status="SAFE_IF",
            missing="derivation from parent identity",
            consequence="safe but does not solve O theorem",
        ),
        NoOverlapMinimalEntry(
            name="OM6: energy/accounting exclusion O",
            form="epsilon_vac_config and e_kappa excluded from direct metric source after B_s insertion",
            role="accounting no-overlap guard",
            allowed_if="energy/accounting is diagnostic or recombined once",
            forbidden_if="exclusion is used to hide an actual source term",
            status="REQUIRED",
            missing="accounting recombination law",
            consequence="blocks energy-source backdoor but does not define full O",
        ),
        NoOverlapMinimalEntry(
            name="OM7: boundary-supported no-overlap",
            form="residual has compact/boundary-neutral support with zero exterior scalar charge",
            role="boundary safety candidate",
            allowed_if="boundary theorem plus no metric overlap are both explicit",
            forbidden_if="boundary neutrality is used as substitute for trace no-overlap",
            status="CANDIDATE",
            missing="boundary theorem and trace orthogonality",
            consequence="could protect exterior but does not alone prove count-once metric insertion",
        ),
        NoOverlapMinimalEntry(
            name="OM8: diagnostic elliptic overlap audit",
            form="solve diagnostic projection/elliptic problem to measure overlap",
            role="diagnostic tool",
            allowed_if="kept as audit only",
            forbidden_if="diagnostic result is promoted to physical O",
            status="SAFE_IF",
            missing="physical no-overlap mechanism",
            consequence="useful for testing branches but not ontology",
        ),
        NoOverlapMinimalEntry(
            name="OM9: neutral residual metric trace",
            form="Trace[g_ij^scalar] = Trace_B_s + Trace_residual_neutral with O=0",
            role="theorem-heavy alternative to residual-kill",
            allowed_if="O, boundary neutrality, no mass overlap, and no scalar charge are all derived",
            forbidden_if="used without explicit O",
            status="RISK",
            missing="full O and safety theorems",
            consequence="keeps neutral residual alive only at high proof burden",
        ),
        NoOverlapMinimalEntry(
            name="OM10: non-metric bookkeeping is not O",
            form="residual marked non-metric / bookkeeping",
            role="anti-hardening guard",
            allowed_if="used only as residual fence",
            forbidden_if="treated as proof of no-overlap",
            status="REQUIRED",
            missing="O still missing",
            consequence="prevents bookkeeping label from becoming fake theorem",
        ),
        NoOverlapMinimalEntry(
            name="OM11: fake orthogonality",
            form="<B_s,residual>=0 declared without pairing",
            role="rejected shortcut",
            allowed_if="never as theorem",
            forbidden_if="accepted as O",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents symbolic orthogonality from replacing mechanism",
        ),
        NoOverlapMinimalEntry(
            name="OM12: fake projector",
            form="P_B and P_R named without construction",
            role="rejected shortcut",
            allowed_if="never as theorem",
            forbidden_if="accepted as projectors",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents projector vocabulary from hiding missing operator",
        ),
        NoOverlapMinimalEntry(
            name="OM13: boundary-hidden overlap",
            form="overlap moved into boundary term or surface contribution",
            role="rejected/dangerous repair",
            allowed_if="only as diagnostic failure mode",
            forbidden_if="accepted as no-overlap",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents surface bookkeeping from hiding double-counting",
        ),
        NoOverlapMinimalEntry(
            name="OM14: recovery downstream",
            form="gamma_like and AB tested only after O or residual-kill convention is fixed",
            role="anti-smuggling guard",
            allowed_if="recovery remains check only",
            forbidden_if="recovery chooses pairing/projectors/O",
            status="RECOVERY_TARGET",
            missing="solutions after O",
            consequence="keeps GR-compatible recovery from defining no-overlap",
        ),
        NoOverlapMinimalEntry(
            name="OM15: parent identity route",
            form="parent trace/recombination identity derives O or residual-kill",
            role="future derivation route",
            allowed_if="identity is explicit and not GR rewrite",
            forbidden_if="decorative parent identity asserts O",
            status="THEOREM_TARGET",
            missing="parent no-overlap identity",
            consequence="strongest route for replacing convention with theorem",
        ),
        NoOverlapMinimalEntry(
            name="OM16: O failure",
            form="no explicit O, and residual-kill/non-metric convention is the only safe branch",
            role="status outcome / branch narrowing",
            allowed_if="used to keep O unresolved and residual-kill provisional",
            forbidden_if="treated as derivation of O",
            status="UNRESOLVED",
            missing="O",
            consequence="metric insertion remains convention-limited",
        ),
        NoOverlapMinimalEntry(
            name="OM17: recommended next move",
            form="if O remains unresolved, test boundary safety of B_s insertion under residual-kill convention",
            role="next local bottleneck",
            allowed_if="minimal O audit does not derive O",
            forbidden_if="jumping to parent equation before boundary safety",
            status="RECOMMENDED",
            missing="boundary safety audit",
            consequence="next script should be candidate_B_s_insertion_boundary_safety.py",
        ),
    ]


def print_entry(e: NoOverlapMinimalEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Form: {e.form}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"[INFO] {e.name}: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Minimal no-overlap operator problem")

    print("Question:")
    print()
    print("  Is there a minimal O that actually enforces count-once recombination,")
    print("  rather than merely renaming residual-kill or bookkeeping?")
    print()
    print("Target:")
    print()
    print("  O[B_s, zeta_residual/kappa_residual, J_V] = 0")
    print()
    print("Goal:")
    print()
    print("  test whether orthogonality, projectors, insertion exclusivity,")
    print("  residual-kill, energy exclusion, or boundary support can define a real O")
    print()
    print("Discipline:")
    print()
    print("  do not assert orthogonality without pairing")
    print("  do not name projectors without construction")
    print("  do not call residual-kill a derived O")
    print("  do not let bookkeeping label become O")
    print("  do not hide overlap in boundary terms")
    print("  keep recovery downstream")

    with out.governance_assessments():
        out.line(
            "minimal no-overlap operator problem posed",
            StatusMark.OBLIGATION,
            "required before neutral residual can be permitted",
        )


def case_1_inventory(entries: List[NoOverlapMinimalEntry]):
    header("Case 1: Minimal no-overlap operator inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[NoOverlapMinimalEntry], out: ScriptOutput):
    header("Case 2: Compact minimal O ledger")

    print("| Entry | Form | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact minimal O ledger produced", StatusMark.INFO, "candidate O forms enumerated")


def case_3_status_counts(entries: List[NoOverlapMinimalEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Minimal O forms can be named, but none is derived here.")
    print("  Orthogonality and projector routes are candidates only if their structure is real.")
    print("  Residual-kill and insertion exclusivity are safe conventions, not derived O.")
    print("  Non-metric bookkeeping is not O.")
    print("  If O remains unresolved, boundary safety should be tested under residual-kill convention.")

    with out.governance_assessments():
        out.line("minimal O status count produced", StatusMark.INFO, "O unresolved; candidate forms only")


def case_4_candidate_forms(out: ScriptOutput):
    header("Case 4: Candidate O forms")

    print("Candidate O forms:")
    print()
    print("1. orthogonality pairing")
    print("2. projector split")
    print("3. metric insertion exclusivity")
    print("4. residual-kill convention")
    print("5. energy/accounting exclusion")
    print("6. boundary-supported no-overlap")
    print("7. diagnostic elliptic overlap audit")
    print()
    print("Strict distinction:")
    print()
    print("  Candidate operator forms may become theorem targets.")
    print("  Safe conventions prevent damage.")
    print("  Diagnostic audits test overlap.")
    print("  None of these is automatically a derived O.")

    with out.governance_assessments():
        out.line("candidate O forms listed", StatusMark.INFO, "seven forms listed; none derived")


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: Minimal O decision tree")

    print("Decision tree:")
    print()
    print("1. Orthogonality pairing:")
    print("   candidate if pairing/domain is derived.")
    print()
    print("2. Projector split:")
    print("   candidate if projectors are real operators.")
    print()
    print("3. Metric insertion exclusivity:")
    print("   safe if residual is non-metric, but still convention unless derived.")
    print()
    print("4. Residual-kill:")
    print("   clean safe branch, not O theorem by itself.")
    print()
    print("5. Boundary-supported no-overlap:")
    print("   can protect exterior but does not alone prove trace no-overlap.")
    print()
    print("6. Fake O:")
    print("   rejected if it only renames desired outcome.")

    with out.governance_assessments():
        out.line("minimal O decision tree stated", StatusMark.INFO, "recommended next is boundary safety")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  No minimal O can be made real without undefined pairing, fake projectors,")
    print("  or residual relabeling.")
    print()
    print("Consequence:")
    print()
    print("  O remains unresolved.")
    print("  Continue only under residual-kill / non-metric convention.")
    print("  Test boundary safety next rather than claiming no-overlap theorem.")
    print()
    print("Bad failure:")
    print()
    print("  Call residual-kill, non-metric bookkeeping, or diagnostic projection a derived O.")

    with out.governance_assessments():
        out.line(
            "minimal O good failure stated",
            StatusMark.DEFER,
            "deferred; O unresolved, continue under residual-kill convention",
        )


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("Minimal O fails if:")
    print()
    print("1. orthogonality pairing is undefined")
    print("2. projectors are named but not constructed")
    print("3. residual-kill is treated as derived O")
    print("4. non-metric bookkeeping is treated as O")
    print("5. boundary terms hide overlap")
    print("6. diagnostic projection is promoted to ontology")
    print("7. recovery checks choose O")
    print("8. neutral residual is allowed without O")

    with out.governance_assessments():
        out.line("minimal O failure controls stated", StatusMark.WARN, "eight failure modes")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_no_overlap_operator_minimal_forms.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_B_s_insertion_boundary_safety.py")
    print("   Test boundary safety of B_s insertion under residual-kill / non-metric convention.")
    print()
    print("3. candidate_parent_identity_for_residual_kill.py")
    print("   Use only if a concrete parent identity candidate appears.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_B_s_insertion_boundary_safety.py")
    print()
    print("Reason:")
    print("  O remains unresolved, so the safe convention must now survive boundary safety:")
    print("  no exterior charge, no far-zone scalar flux, no M_ext shift, no shell source.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "candidate_B_s_insertion_boundary_safety.py")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("Minimal O remains unresolved.")
    print()
    print("Current best status:")
    print()
    print("  orthogonality: candidate only if pairing is real")
    print("  projector split: candidate only if projectors are real")
    print("  residual-kill / insertion exclusivity: safest convention, not derived O")
    print("  non-metric bookkeeping: useful fence, not O")
    print("  diagnostic overlap audit: useful diagnostic, not ontology")
    print()
    print("Best next script:")
    print()
    print("  candidate_B_s_insertion_boundary_safety.py")

    with out.governance_assessments():
        out.line(
            "minimal no-overlap operator audit complete",
            StatusMark.DEFER,
            "O unresolved; convention-limited",
        )


def main():
    header("Candidate No-Overlap Operator Minimal Forms")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_candidate_forms(out)
    case_5_decision_tree(out)
    case_6_good_failure(out)
    case_7_failure_controls(out)
    case_8_next_tests(out)
    final_interpretation(out)

    ns2 = ns
    if True:
        # Proof obligations for O theorem and derived forms
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_no_overlap_operator_O",
            script_id=SCRIPT_ID,
            title="Derive no-overlap operator O",
            status=ObligationStatus.OPEN,
            required_by=["neutral_residual_metric_trace_route"],
            description=(
                "Derive a concrete no-overlap operator O[B_s, zeta_residual/kappa_residual, J_V] = 0 "
                "with explicit domain, pairing or projector construction, and boundary safety. "
                "Residual-kill and non-metric bookkeeping are not sufficient."
            ),
        ))

        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_orthogonality_pairing_for_O",
            script_id=SCRIPT_ID,
            title="Derive orthogonality pairing for O",
            status=ObligationStatus.OPEN,
            required_by=["neutral_residual_metric_trace_route"],
            description=(
                "Define the pairing <Trace_B_s, Trace_residual>_O from metric/source/accounting structure, "
                "not chosen ad hoc."
            ),
        ))

        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_projector_split_for_O",
            script_id=SCRIPT_ID,
            title="Derive projector split P_B, P_R for O",
            status=ObligationStatus.OPEN,
            required_by=["neutral_residual_metric_trace_route"],
            description=(
                "Construct actual projectors P_B and P_R satisfying P_B * P_R = 0 "
                "with explicit source/domain definitions."
            ),
        ))

        # Route: residual-kill as safe convention (not derived O)
        ns2.record_route(RouteRecord(
            route_id="residual_kill_nonmetric_convention_route",
            script_id=SCRIPT_ID,
            name="Residual kill / non-metric residual convention",
            status=GovernanceStatus.PROVISIONAL_CONVENTION,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=["derive_no_overlap_operator_O"],
            activation_conditions=[
                "residual zeta/kappa metric trace is killed or non-metric",
                "no O derived yet",
                "energy/accounting is not a source reservoir",
                "boundary safety holds structurally",
            ],
        ))

        # Branch decision: O deferred
        ns2.record_branch_decision(BranchDecisionRecord(
            decision_id="defer_O_no_pairing_or_projector",
            script_id=SCRIPT_ID,
            branch_id="no_overlap_operator_O",
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            tier=ClaimTier.CONSTRAINED,
            reason_code=ReasonCode.MISSING_BOUNDARY_NEUTRALITY_THEOREM,
            obligation_ids=[
                "derive_no_overlap_operator_O",
                "derive_orthogonality_pairing_for_O",
                "derive_projector_split_for_O",
            ],
            description=(
                "O cannot be licensed because no pairing or projector construction exists. "
                "Residual-kill / non-metric convention is the only safe working branch. "
                "Boundary safety must now be tested under that convention."
            ),
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="no_overlap_operator_minimal_forms_marker",
            inputs=[],
            output=sp.Symbol("no_overlap_operator_minimal_forms_audited"),
            method="no_overlap_operator_minimal_forms_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
