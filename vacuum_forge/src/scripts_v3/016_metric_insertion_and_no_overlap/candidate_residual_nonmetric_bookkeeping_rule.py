# Candidate residual non-metric bookkeeping rule
#
# Group:
#   16_metric_insertion_and_no_overlap
#
# Script type:
#   SIEVE
#
# Purpose
# -------
# The B_s-only insertion count-once audit found:
#
#   J_V-driven zeta may enter ordinary metric scalar trace only through B_s.
#   Residual zeta/kappa metric trace is killed or non-metric.
#
# But this does not mean residual variables must disappear.
#
# This script tests what residual zeta/kappa may still do safely if not metric trace.
#
# Locked-door question:
#
#   Can residual zeta/kappa remain useful as diagnostic bookkeeping or
#   first-order relaxation without becoming metric scalar trace,
#   shifting M_ext, or creating exterior scalar charge?
#
# This is a bookkeeping/relaxation fence, not a derivation.

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
class NonMetricResidualEntry:
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
        dependency_id="B_s_only_insertion_count_once_marker",
        upstream_script_id="016_metric_insertion_and_no_overlap__candidate_B_s_only_insertion_count_once",
        upstream_derivation_id="B_s_only_insertion_count_once_marker",
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


def build_entries() -> List[NonMetricResidualEntry]:
    return [
        NonMetricResidualEntry(
            name="NM1: non-metric residual target",
            rule="residual zeta/kappa may remain useful only as non-metric bookkeeping, diagnostic, or safe relaxation",
            role="core residual-after-kill target",
            allowed_if="residual cannot source metric trace, M_ext shift, or exterior scalar charge",
            forbidden_if="residual becomes hidden metric source or scalar gravity",
            status="THEOREM_TARGET",
            missing="non-metric residual rule",
            consequence="decides whether residual variables survive after B_s-only insertion",
        ),
        NonMetricResidualEntry(
            name="NM2: diagnostic residual",
            rule="residual zeta/kappa records mismatch, gauge/reduction status, or internal audit only",
            role="safe diagnostic branch",
            allowed_if="diagnostic has no source term in metric equations",
            forbidden_if="diagnostic is promoted to field source",
            status="SAFE_IF",
            missing="diagnostic scope statement",
            consequence="keeps residual useful without physics overclaim",
        ),
        NonMetricResidualEntry(
            name="NM3: configuration bookkeeping",
            rule="residual tracks vacuum-volume configuration history without direct metric insertion",
            role="non-metric bookkeeping branch",
            allowed_if="bookkeeping cannot shift M_ext or exterior charge",
            forbidden_if="bookkeeping becomes hidden source reservoir",
            status="CANDIDATE",
            missing="bookkeeping/accounting law",
            consequence="preserves ontology while blocking second trace",
        ),
        NonMetricResidualEntry(
            name="NM4: P_relax-only residual",
            rule="residual participates only in first-order non-radiative relaxation",
            role="possible safe dynamic branch",
            allowed_if="first-order, boundary-neutral, compact/support-safe, not metric trace",
            forbidden_if="P_relax becomes Box zeta, Box kappa, or ordinary scalar radiation",
            status="CANDIDATE",
            missing="P_relax operator and non-wave theorem",
            consequence="allows residual dynamics without far-zone scalar wave",
        ),
        NonMetricResidualEntry(
            name="NM5: energy/accounting diagnostic only",
            rule="epsilon_vac_config and e_kappa may audit configuration cost but not source extra metric trace",
            role="energy/accounting fence",
            allowed_if="energy terms are diagnostic or recombined once through B_s only",
            forbidden_if="energy terms become source reservoir or coefficient tuning knob",
            status="REQUIRED",
            missing="energy/accounting recombination rule",
            consequence="prevents killed residual from returning through energy",
        ),
        NonMetricResidualEntry(
            name="NM6: no M_ext shift",
            rule="non-metric residual cannot change exterior A-sector mass",
            role="mass-protection requirement",
            allowed_if="residual bookkeeping is mass-neutral",
            forbidden_if="residual alters measured exterior mass",
            status="REQUIRED",
            missing="mass-neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        NonMetricResidualEntry(
            name="NM7: no exterior scalar charge",
            rule="non-metric residual creates no exterior zeta/kappa charge and no far-zone scalar flux",
            role="ordinary exterior safety requirement",
            allowed_if="residual support/relaxation is boundary-neutral",
            forbidden_if="residual leaks scalar tail",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="prevents residual from becoming scalar gravity",
        ),
        NonMetricResidualEntry(
            name="NM8: kappa diagnostic fence",
            rule="kappa remains reduced diagnostic / non-metric residual / separately neutral unless derived",
            role="standing kappa safety rule",
            allowed_if="kappa does not enter metric scalar trace",
            forbidden_if="kappa restores killed zeta residual trace",
            status="REQUIRED",
            missing="kappa cleanup theorem",
            consequence="prevents kappa backdoor",
        ),
        NonMetricResidualEntry(
            name="NM9: non-metric residual cannot define O",
            rule="bookkeeping status does not itself prove no-overlap operator O",
            role="anti-hardening guard",
            allowed_if="O remains theorem target unless explicitly defined",
            forbidden_if="non-metric label is used as fake O",
            status="REQUIRED",
            missing="O operator",
            consequence="keeps no-overlap unresolved rather than renamed",
        ),
        NonMetricResidualEntry(
            name="NM10: forbidden hidden metric source",
            rule="non-metric residual later appears in metric equation source term",
            role="rejected regression",
            allowed_if="never unless recast through explicit B_s insertion and count-once",
            forbidden_if="accepted as hidden source",
            status="REJECTED",
            missing="not pursued",
            consequence="blocks source-reservoir behavior",
        ),
        NonMetricResidualEntry(
            name="NM11: forbidden Box residual",
            rule="residual evolves by Box zeta or Box kappa in ordinary sector",
            role="rejected scalar-radiation branch",
            allowed_if="never in ordinary branch",
            forbidden_if="accepted as relaxation",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents ordinary scalar radiation",
        ),
        NonMetricResidualEntry(
            name="NM12: forbidden coefficient reservoir",
            rule="residual bookkeeping adjusts coefficients to recover gamma_like or AB",
            role="rejected tuning branch",
            allowed_if="never as mechanism",
            forbidden_if="used to pass recovery",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents recovery smuggling through bookkeeping",
        ),
        NonMetricResidualEntry(
            name="NM13: neutral metric residual alternative",
            rule="residual metric trace survives only if O and boundary/mass neutrality are derived",
            role="theorem-heavy alternative",
            allowed_if="real O exists and residual is structurally neutral",
            forbidden_if="used because non-metric bookkeeping feels too restrictive",
            status="RISK",
            missing="O, boundary theorem, no mass overlap",
            consequence="keeps alternative alive but out of current convention",
        ),
        NonMetricResidualEntry(
            name="NM14: recovery downstream",
            rule="gamma_like and AB are tested only after residual role is fenced",
            role="anti-smuggling guard",
            allowed_if="recovery remains check only",
            forbidden_if="recovery chooses diagnostic/bookkeeping/relaxation role",
            status="RECOVERY_TARGET",
            missing="solutions after residual rule",
            consequence="keeps residual status from being selected by GR target",
        ),
        NonMetricResidualEntry(
            name="NM15: parent derivation route",
            rule="parent identity derives whether residual is killed, non-metric, or neutral",
            role="future derivation route",
            allowed_if="identity is explicit and not GR rewrite",
            forbidden_if="identity is decorative",
            status="THEOREM_TARGET",
            missing="parent residual identity",
            consequence="future route for replacing convention with theorem",
        ),
        NonMetricResidualEntry(
            name="NM16: residual bookkeeping failure",
            rule="residual cannot be kept non-metric and cannot be made neutral through O",
            role="branch failure condition",
            allowed_if="used to block residual variables from ordinary sector",
            forbidden_if="patched by relabeling residual as bookkeeping",
            status="BRANCH_KILLED",
            missing="applies if demonstrated",
            consequence="residual variables must remain outside ordinary metric/vacuum-current sector",
        ),
        NonMetricResidualEntry(
            name="NM17: recommended next move",
            rule="if non-metric roles survive, test minimal O forms or boundary safety next",
            role="next local bottleneck",
            allowed_if="residual bookkeeping is fenced but O remains unresolved",
            forbidden_if="jumping to parent equation before O/minimal forms are audited",
            status="RECOMMENDED",
            missing="minimal no-overlap operator audit",
            consequence="next script should be candidate_no_overlap_operator_minimal_forms.py",
        ),
    ]


def print_entry(e: NonMetricResidualEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Rule: {e.rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"[INFO] {e.name}: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Residual non-metric bookkeeping problem")

    print("Question:")
    print()
    print("  Can residual zeta/kappa remain useful as diagnostic bookkeeping or")
    print("  first-order relaxation without becoming metric scalar trace,")
    print("  shifting M_ext, or creating exterior scalar charge?")
    print()
    print("Goal:")
    print()
    print("  preserve useful residual variables while blocking second-spoon metric entry")
    print()
    print("Discipline:")
    print()
    print("  non-metric means no direct metric trace")
    print("  bookkeeping means no hidden source reservoir")
    print("  relaxation means not Box zeta/kappa")
    print("  diagnostic means not field source")
    print("  no M_ext shift")
    print("  no exterior scalar charge")
    print("  recovery downstream")

    with out.governance_assessments():
        out.line(
            "residual non-metric bookkeeping problem posed",
            StatusMark.OBLIGATION,
            "required before residual roles can be licensed",
        )


def case_1_inventory(entries: List[NonMetricResidualEntry]):
    header("Case 1: Residual non-metric bookkeeping inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[NonMetricResidualEntry], out: ScriptOutput):
    header("Case 2: Compact residual non-metric ledger")

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
        out.line("compact non-metric residual ledger produced", StatusMark.INFO, "residual roles enumerated")


def case_3_status_counts(entries: List[NonMetricResidualEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Residual variables can remain useful only if their non-metric role is explicit.")
    print("  Diagnostic and bookkeeping roles are safest.")
    print("  P_relax-only residual is possible but needs a non-wave theorem.")
    print("  Energy/accounting is dangerous unless diagnostic or recombined once.")
    print("  O remains unresolved; non-metric bookkeeping does not define it.")
    print("  Next gate is minimal no-overlap operator forms.")

    with out.governance_assessments():
        out.line("residual non-metric bookkeeping status count produced", StatusMark.INFO, "roles enumerated")


def case_4_allowed_roles(out: ScriptOutput):
    header("Case 4: Allowed residual roles")

    print("Allowed residual roles if fenced:")
    print()
    print("1. diagnostic mismatch / reduced-gauge audit")
    print("2. configuration bookkeeping")
    print("3. first-order non-radiative relaxation")
    print("4. energy/accounting diagnostic")
    print("5. parent-identity theorem target")
    print()
    print("Not allowed:")
    print()
    print("1. direct metric scalar trace")
    print("2. hidden metric source")
    print("3. exterior scalar charge")
    print("4. M_ext shift")
    print("5. Box zeta / Box kappa")
    print("6. coefficient reservoir")

    with out.governance_assessments():
        out.line("allowed residual roles listed", StatusMark.INFO, "five safe roles; six forbidden roles")


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: Non-metric residual decision tree")

    print("Decision tree:")
    print()
    print("1. Diagnostic-only residual:")
    print("   safest if never promoted to field source.")
    print()
    print("2. Configuration bookkeeping:")
    print("   allowed if no M_ext shift and no scalar charge.")
    print()
    print("3. P_relax-only residual:")
    print("   possible if first-order, non-radiative, boundary-neutral, non-metric.")
    print()
    print("4. Energy/accounting diagnostic:")
    print("   allowed only if not source reservoir.")
    print()
    print("5. Neutral metric residual:")
    print("   reserved for real O, not current convention.")
    print()
    print("6. Hidden metric source or scalar wave:")
    print("   rejected.")

    with out.governance_assessments():
        out.line("non-metric residual decision tree stated", StatusMark.INFO, "recommended next is minimal O audit")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  residual variables cannot be kept from becoming source reservoirs,")
    print("  metric trace, exterior charge, or scalar waves.")
    print()
    print("Consequence:")
    print()
    print("  residual variables must remain outside ordinary metric/vacuum-current sector,")
    print("  or the insertion branch is killed.")
    print()
    print("Bad failure:")
    print()
    print("  call residual non-metric, then let it source metric equations indirectly.")

    with out.governance_assessments():
        out.line(
            "residual non-metric bookkeeping good failure stated",
            StatusMark.DEFER,
            "deferred pending non-metric role theorems",
        )


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("Residual non-metric bookkeeping fails if:")
    print()
    print("1. diagnostic residual becomes field source")
    print("2. bookkeeping shifts M_ext")
    print("3. bookkeeping creates exterior scalar charge")
    print("4. energy/accounting becomes coefficient reservoir")
    print("5. P_relax becomes Box zeta / Box kappa")
    print("6. non-metric label is used as fake O")
    print("7. kappa restores killed trace")
    print("8. recovery checks choose residual role")

    with out.governance_assessments():
        out.line("residual non-metric bookkeeping failure controls stated", StatusMark.WARN, "eight failure modes")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_residual_nonmetric_bookkeeping_rule.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_no_overlap_operator_minimal_forms.py")
    print("   Test whether a minimal O is more than a label.")
    print()
    print("3. candidate_metric_insertion_early_failure_summary.py")
    print("   Use if residual roles cannot be fenced.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_no_overlap_operator_minimal_forms.py")
    print()
    print("Reason:")
    print("  Non-metric bookkeeping can fence residual roles provisionally,")
    print("  but O remains the missing theorem for any neutral residual alternative.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "candidate_no_overlap_operator_minimal_forms.py")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("Residual zeta/kappa may remain useful only if their role is explicitly non-metric.")
    print()
    print("Safest surviving roles:")
    print()
    print("  diagnostic")
    print("  configuration bookkeeping")
    print("  first-order non-radiative P_relax-only residual")
    print("  energy/accounting diagnostic only")
    print()
    print("Still not derived:")
    print()
    print("  O")
    print("  residual-kill theorem")
    print("  P_relax mechanism")
    print("  parent residual identity")
    print()
    print("Best next script:")
    print()
    print("  candidate_no_overlap_operator_minimal_forms.py")

    with out.governance_assessments():
        out.line(
            "residual non-metric bookkeeping audit complete",
            StatusMark.DEFER,
            "no residual-kill theorem derived; deferred",
        )


def main():
    header("Candidate Residual Non-Metric Bookkeeping Rule")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_allowed_roles(out)
    case_5_decision_tree(out)
    case_6_good_failure(out)
    case_7_failure_controls(out)
    case_8_next_tests(out)
    final_interpretation(out)

    ns2 = ns
    if True:
        # Proof obligations for residual non-metric theorems
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_nonmetric_residual_role_theorem",
            script_id=SCRIPT_ID,
            title="Derive non-metric residual role theorem",
            status=ObligationStatus.OPEN,
            required_by=["nonmetric_residual_bookkeeping_route"],
            description=(
                "Show that residual zeta/kappa may remain as diagnostic, "
                "configuration bookkeeping, or first-order non-radiative relaxation "
                "without becoming metric scalar trace, M_ext shift, or exterior scalar charge."
            ),
        ))

        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_P_relax_non_wave_theorem",
            script_id=SCRIPT_ID,
            title="Derive P_relax non-wave theorem",
            status=ObligationStatus.OPEN,
            required_by=["nonmetric_residual_bookkeeping_route"],
            description=(
                "Show that P_relax residual is first-order, non-radiative, "
                "boundary-neutral, and does not become Box zeta or Box kappa."
            ),
        ))

        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_kappa_cleanup_theorem",
            script_id=SCRIPT_ID,
            title="Derive kappa cleanup theorem",
            status=ObligationStatus.OPEN,
            required_by=["nonmetric_residual_bookkeeping_route"],
            description=(
                "Derive that kappa remains diagnostic/non-metric/separately neutral "
                "and cannot restore killed zeta residual metric trace."
            ),
        ))

        # Route: non-metric residual bookkeeping
        ns2.record_route(RouteRecord(
            route_id="nonmetric_residual_bookkeeping_provisional_route",
            script_id=SCRIPT_ID,
            name="Non-metric residual bookkeeping (diagnostic / configuration / P_relax)",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "derive_nonmetric_residual_role_theorem",
                "derive_P_relax_non_wave_theorem",
                "derive_kappa_cleanup_theorem",
            ],
            activation_conditions=[
                "residual is explicitly non-metric",
                "no M_ext shift from residual",
                "no exterior scalar charge from residual",
                "bookkeeping cannot source metric equations",
                "P_relax is non-radiative and first-order only",
            ],
        ))

        # Branch decision: deferred
        ns2.record_branch_decision(BranchDecisionRecord(
            decision_id="defer_nonmetric_residual_no_theorems",
            script_id=SCRIPT_ID,
            branch_id="nonmetric_residual_bookkeeping",
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            tier=ClaimTier.CONSTRAINED,
            reason_code=ReasonCode.MISSING_BOUNDARY_NEUTRALITY_THEOREM,
            obligation_ids=[
                "derive_nonmetric_residual_role_theorem",
                "derive_P_relax_non_wave_theorem",
                "derive_kappa_cleanup_theorem",
            ],
            description=(
                "Non-metric residual bookkeeping cannot be licensed because the "
                "non-metric role theorem, P_relax non-wave theorem, and kappa cleanup "
                "theorem are missing. Diagnostic/bookkeeping roles survive provisionally."
            ),
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="residual_nonmetric_bookkeeping_rule_marker",
            inputs=[],
            output=sp.Symbol("residual_nonmetric_bookkeeping_rule_audited"),
            method="residual_nonmetric_bookkeeping_rule_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
