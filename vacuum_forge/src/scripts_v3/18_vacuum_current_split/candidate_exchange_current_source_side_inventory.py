# Candidate exchange current source-side inventory
#
# Group:
#   18_vacuum_current_split
#
# Purpose
# -------
# The ordinary matter decoupling audit found:
#
#   Ordinary matter decoupling is required but not derived.
#   rho/scalar charge must remain routed to A-sector.
#   J_sub cannot push matter; J_exch cannot reroute matter.
#   No fifth force, hidden scalar charge, M_ext shift, boundary matter repair,
#   or recovery-tuned coupling is allowed.
#   Zero-net and zero-creation ordinary-sector branches remain the safest
#   current-compatible branches.
#
# This script inventories possible source sides for J_exch.
#
# Locked-door question:
#
#   If J_exch exists, what source side could make it real?
#
# This is a source-side inventory, not an exchange-current derivation.


from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "SAFE_IF": "WARN",
        "CANDIDATE": "WARN",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "RECOMMENDED": "PASS",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DANGER": "FAIL",
        "THEOREM_TARGET": "WARN",
        "RECOVERY_TARGET": "WARN",
        "BRANCH_KILLED": "FAIL",
        "DEFER": "WARN",
        "CLOSED": "PASS",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class ExchangeSourceEntry:
    name: str
    source_candidate: str
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
        dependency_id="ordinary_matter_decoupling_for_vacuum_currents_marker",
        upstream_script_id="18_vacuum_current_split__candidate_ordinary_matter_decoupling_for_vacuum_currents",
        upstream_derivation_id="ordinary_matter_decoupling_for_vacuum_currents_marker",
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


def build_entries() -> List[ExchangeSourceEntry]:
    return [
        ExchangeSourceEntry(
            name="ES1: exchange source-side target",
            source_candidate="J_exch requires a source side that is not ordinary-sector repair",
            role="core source-side theorem target",
            allowed_if="source is explicit, non-decorative, and decoupled from ordinary matter repair",
            forbidden_if="source side is named to keep J_exch alive",
            status="THEOREM_TARGET",
            missing="actual exchange source operator",
            consequence="decides whether active exchange can become technical",
        ),
        ExchangeSourceEntry(
            name="ES2: Sigma_V / R_V role-level split",
            source_candidate="Sigma_V and R_V as role-level source/relaxation placeholders",
            role="current known accounting branch",
            allowed_if="explicitly marked role-level only",
            forbidden_if="treated as derived operators or tuned against each other",
            status="SAFE_IF",
            missing="Sigma_V and R_V operators",
            consequence="preserves source/relaxation vocabulary without fake law",
        ),
        ExchangeSourceEntry(
            name="ES3: Sigma/R double-counting guard",
            source_candidate="Sigma_exch and R_exch must be distinct, not one hidden tuning knob",
            role="source accounting guard",
            allowed_if="source and relaxation have independent definitions",
            forbidden_if="Sigma/R are adjusted to pass recovery, boundary, or neutrality checks",
            status="REQUIRED",
            missing="Sigma/R separation theorem",
            consequence="prevents exchange balance from becoming tuning mechanism",
        ),
        ExchangeSourceEntry(
            name="ES4: curvature admissibility failure",
            source_candidate="finite-admissibility failure triggers or labels exchange",
            role="diagnostic/theorem-target candidate",
            allowed_if="A_curv remains diagnostic/branch-filter unless dynamics are derived",
            forbidden_if="curvature admissibility becomes active repair source",
            status="RISK",
            missing="A_curv dynamics and J_curv absent",
            consequence="dangerous until Group 17 theorem targets are solved",
        ),
        ExchangeSourceEntry(
            name="ES5: finite volume response",
            source_candidate="zeta / volume response sources or gates exchange",
            role="curvature-volume bridge candidate",
            allowed_if="B_s/F_zeta insertion, residual-kill, and no-overlap are solved",
            forbidden_if="zeta becomes hidden scalar source or residual trace",
            status="RISK",
            missing="B_s/F_zeta insertion and no-overlap theorem",
            consequence="promising but unsafe until Group 16 bottlenecks are solved",
        ),
        ExchangeSourceEntry(
            name="ES6: matter-induced exchange",
            source_candidate="ordinary matter directly sources J_exch",
            role="high-risk ordinary-sector branch",
            allowed_if="explicit theorem derives coupling without double-counting or matter repair",
            forbidden_if="ordinary T or rho is used as Sigma_exch by convenience",
            status="RISK",
            missing="matter-to-exchange source theorem",
            consequence="unsafe under current decoupling status",
        ),
        ExchangeSourceEntry(
            name="ES7: boundary exchange",
            source_candidate="exchange sourced at boundary, endpoint, shell, or admissibility edge",
            role="high-risk boundary branch",
            allowed_if="boundary support is structural and not repair",
            forbidden_if="boundary exchange cancels leakage, scalar tail, or singularity",
            status="RISK",
            missing="boundary support theorem",
            consequence="dangerous because boundary repair is forbidden",
        ),
        ExchangeSourceEntry(
            name="ES8: dark-sector exchange",
            source_candidate="dark-sector source couples to J_exch",
            role="optional deferred branch",
            allowed_if="ordinary matter decoupling and exterior neutrality are preserved",
            forbidden_if="dark sector patches ordinary-sector failure",
            status="DEFER",
            missing="dark-sector coupling rule",
            consequence="keeps speculative coupling downstream",
        ),
        ExchangeSourceEntry(
            name="ES9: zero-net exchange",
            source_candidate="Sigma_exch - R_exch = 0 in ordinary sector",
            role="ordinary-sector neutral branch",
            allowed_if="ordinary curvature arises from warping/constraint or balanced exchange",
            forbidden_if="zero-net branch still claims active net source",
            status="CANDIDATE",
            missing="ordinary-sector zero-net theorem",
            consequence="safest branch if exchange vocabulary is kept",
        ),
        ExchangeSourceEntry(
            name="ES10: zero-creation branch",
            source_candidate="Sigma_exch = R_exch = 0 in ordinary sector",
            role="strong ordinary-sector neutral branch",
            allowed_if="J_exch inactive for ordinary matter and ordinary curvature arises otherwise",
            forbidden_if="creation/destruction is still invoked as active ordinary source",
            status="CANDIDATE",
            missing="ordinary-sector zero-creation theorem",
            consequence="cleanest ordinary-sector no-exchange branch",
        ),
        ExchangeSourceEntry(
            name="ES11: curvature-from-warping branch",
            source_candidate="curvature changes arise from constrained time/space warping, not net vacuum creation/destruction",
            role="non-exchange curvature branch",
            allowed_if="warping relation is derived without GR rewrite or recovery tuning",
            forbidden_if="used to avoid defining exchange while still claiming exchange dynamics",
            status="CANDIDATE",
            missing="warping constraint / parent relation",
            consequence="important alternative to active source-side exchange",
        ),
        ExchangeSourceEntry(
            name="ES12: latent-exchange branch",
            source_candidate="Sigma/R exist as ontology/accounting but vanish or balance in ordinary sector",
            role="ontology/accounting candidate",
            allowed_if="latent exchange has no ordinary metric/matter source role",
            forbidden_if="latent exchange becomes hidden source reservoir",
            status="CANDIDATE",
            missing="regime condition for latent vs active exchange",
            consequence="preserves substance language without forcing ordinary creation/destruction",
        ),
        ExchangeSourceEntry(
            name="ES13: source support law",
            source_candidate="J_exch active only where explicit exchange source is nonzero",
            role="candidate active-domain rule",
            allowed_if="source support is derived independently",
            forbidden_if="support chosen to hide boundary/exterior effects",
            status="CANDIDATE",
            missing="source support theorem",
            consequence="possible route to separating J_exch from J_sub",
        ),
        ExchangeSourceEntry(
            name="ES14: relaxation mechanism",
            source_candidate="R_exch as real relaxation/return/sink mechanism",
            role="required if balance is used",
            allowed_if="relaxation is distinct from source and cannot be tuned",
            forbidden_if="R_exch cancels Sigma_exch by construction",
            status="REQUIRED",
            missing="R_exch mechanism",
            consequence="prevents cancellation knob",
        ),
        ExchangeSourceEntry(
            name="ES15: source sign/strength law",
            source_candidate="Sigma_exch has sign, magnitude, and domain rule",
            role="required source specificity",
            allowed_if="source strength follows from ontology-native operator",
            forbidden_if="source strength is chosen to pass recovery/boundary constraints",
            status="REQUIRED",
            missing="source strength law",
            consequence="prevents source coefficient tuning",
        ),
        ExchangeSourceEntry(
            name="ES16: ordinary T as source by fiat rejection",
            source_candidate="Sigma_exch = function(T_mu_nu) by convenience",
            role="forbidden matter double-count branch",
            allowed_if="never without source theorem",
            forbidden_if="accepted as exchange source",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves ordinary matter decoupling",
        ),
        ExchangeSourceEntry(
            name="ES17: boundary repair source rejection",
            source_candidate="boundary leakage / shell / scalar tail defines Sigma_exch",
            role="forbidden boundary repair branch",
            allowed_if="never as source definition",
            forbidden_if="accepted as exchange source",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents boundary patch current",
        ),
        ExchangeSourceEntry(
            name="ES18: curvature repair source rejection",
            source_candidate="curvature blowup or finite-admissibility failure directly defines Sigma_exch as repair",
            role="forbidden anti-singularity shortcut",
            allowed_if="never without dynamics",
            forbidden_if="accepted as exchange source",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents curvature-admissibility overclaim",
        ),
        ExchangeSourceEntry(
            name="ES19: e_curv reservoir rejection",
            source_candidate="e_curv supplies source strength for J_exch",
            role="forbidden source reservoir branch",
            allowed_if="never under Group 17 closure",
            forbidden_if="accepted as exchange source",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves e_curv diagnostic/accounting-only status",
        ),
        ExchangeSourceEntry(
            name="ES20: recovery source rejection",
            source_candidate="Sigma_exch/R_exch chosen to pass gamma_like, AB, or exterior matching",
            role="forbidden recovery-smuggling branch",
            allowed_if="never as source definition",
            forbidden_if="accepted as exchange source",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps recovery downstream",
        ),
        ExchangeSourceEntry(
            name="ES21: H_exch source shortcut rejection",
            source_candidate="exchange source is defined only to justify future H_exch",
            role="forbidden parent-correction shortcut",
            allowed_if="deferred to Group 19",
            forbidden_if="accepted as source-side origin",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents decorative correction tensor",
        ),
        ExchangeSourceEntry(
            name="ES22: source-side failure",
            source_candidate="no source side can be defined without repair, matter double-count, or boundary patch",
            role="branch failure condition",
            allowed_if="used to keep J_exch role-level or inactive in ordinary sector",
            forbidden_if="patched by source labels",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="J_exch cannot be active ordinary-sector current",
        ),
        ExchangeSourceEntry(
            name="ES23: recommended next move",
            source_candidate="after source-side inventory, audit optional dark-sector coupling",
            role="next local bottleneck",
            allowed_if="ordinary source sides remain unsafe or theorem-targeted",
            forbidden_if="dark sector used to patch ordinary source failure",
            status="RECOMMENDED",
            missing="dark-sector optional branch audit",
            consequence="next script should be candidate_dark_sector_coupling_optional_branch.py",
        ),
    ]


def print_entry(e: ExchangeSourceEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Source candidate: {e.source_candidate}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Exchange current source-side problem")

    print("Question:")
    print()
    print("  If J_exch exists, what source side could make it real?")
    print()
    print("Goal:")
    print()
    print("  inventory possible source sides without ordinary-sector repair")
    print()
    print("Discipline:")
    print()
    print("  no ordinary T as Sigma_exch by fiat")
    print("  no boundary repair source")
    print("  no curvature repair source")
    print("  no e_curv source reservoir")
    print("  no recovery-shaped source")
    print("  no H_exch shortcut")
    print("  preserve zero-net / zero-creation ordinary branches")
    print("  keep dark-sector branch optional")

    status_line("exchange current source-side problem posed", "REQUIRED")


def case_1_inventory(entries: List[ExchangeSourceEntry]):
    header("Case 1: Exchange current source-side inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ExchangeSourceEntry]):
    header("Case 2: Compact exchange source-side ledger")

    print("| Entry | Source candidate | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.source_candidate.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact exchange source-side ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ExchangeSourceEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  No active ordinary-sector source side for J_exch is derived.")
    print("  Sigma/R remain role-level unless distinct operators and strength laws are found.")
    print("  Curvature admissibility, volume response, matter-induced exchange, and boundary exchange are high risk.")
    print("  Zero-net exchange, zero creation, curvature-from-warping, and latent exchange remain the safest ordinary-sector branches.")
    print("  Dark-sector exchange remains deferred and optional.")
    print("  Next gate is dark-sector coupling optionality.")

    status_line("exchange source-side status count produced", "STRUCTURAL")


def case_4_source_classes():
    header("Case 4: Source-side classes")

    print("Source-side classes:")
    print()
    print("1. role-level Sigma_V / R_V")
    print("2. curvature admissibility failure")
    print("3. finite volume response")
    print("4. matter-induced exchange")
    print("5. boundary exchange")
    print("6. dark-sector exchange")
    print("7. zero-net exchange")
    print("8. zero-creation branch")
    print("9. curvature-from-warping")
    print("10. latent-exchange accounting")
    print()
    print("Safest ordinary-sector branches:")
    print()
    print("  zero-net exchange")
    print("  zero creation")
    print("  curvature-from-warping")
    print("  latent exchange as accounting only")

    status_line("exchange source-side classes listed", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: Exchange source-side decision tree")

    print("Decision tree:")
    print()
    print("1. Source/relaxation operators exist:")
    print("   J_exch source-side theorem target survives.")
    print()
    print("2. Sigma/R are role-level only:")
    print("   J_exch remains role-level.")
    print()
    print("3. Source is ordinary matter by convenience:")
    print("   rejected.")
    print()
    print("4. Source is boundary/curvature repair:")
    print("   rejected.")
    print()
    print("5. Source is e_curv reservoir:")
    print("   rejected.")
    print()
    print("6. Ordinary sector has zero-net or zero creation:")
    print("   safest branch.")
    print()
    print("7. Dark sector appears:")
    print("   defer to optional branch audit.")

    status_line("exchange source-side decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  no source side can make J_exch active in the ordinary sector")
    print("  without repair, matter double-count, boundary patch, or source reservoir.")
    print()
    print("Consequence:")
    print()
    print("  keep J_exch role-level or inactive in ordinary sector.")
    print("  preserve zero-net/zero-creation and curvature-from-warping branches.")
    print()
    print("Bad failure:")
    print()
    print("  define Sigma_exch as the thing that makes the exchange current work.")

    status_line("exchange source-side good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Exchange source-side fails if:")
    print()
    print("1. Sigma/R are undefined but used as operators")
    print("2. Sigma/R are tuning knobs")
    print("3. ordinary T defines Sigma_exch by convenience")
    print("4. boundary leakage defines source")
    print("5. curvature failure defines repair source")
    print("6. e_curv becomes reservoir")
    print("7. recovery chooses source strength")
    print("8. H_exch is smuggled in")
    print("9. dark sector patches ordinary failure")
    print("10. zero-net branch still claims net exchange")

    status_line("exchange source-side failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_exchange_current_source_side_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_dark_sector_coupling_optional_branch.py")
    print("   Audit whether dark-sector coupling can remain optional and separated.")
    print()
    print("3. candidate_exchange_source_side_failure_summary.py")
    print("   Use if all source-side candidates collapse into repair.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_dark_sector_coupling_optional_branch.py")
    print()
    print("Reason:")
    print("  Ordinary source sides are not derived and are high risk.")
    print("  The remaining optional branch is dark-sector coupling, but it must not patch ordinary failure.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("No active ordinary-sector source side for J_exch is derived.")
    print()
    print("High-risk source candidates:")
    print()
    print("  curvature admissibility failure")
    print("  finite volume response")
    print("  matter-induced exchange")
    print("  boundary exchange")
    print()
    print("Safest ordinary-sector branches:")
    print()
    print("  zero-net exchange")
    print("  zero creation")
    print("  curvature-from-warping")
    print("  latent exchange as accounting")
    print()
    print("Best next script:")
    print()
    print("  candidate_dark_sector_coupling_optional_branch.py")

    status_line("exchange current source-side inventory complete", "CLOSED")


def main():
    header("Candidate Exchange Current Source-Side Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_source_classes()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    ns.record_derivation(
        derivation_id="exchange_current_source_side_inventory_marker",
        inputs=[],
        output=sp.Symbol("exchange_current_source_side_inventory_complete"),
        method="exchange_current_source_side_inventory",
        status=Status.DERIVED,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
