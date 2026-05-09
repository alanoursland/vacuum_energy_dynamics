# Candidate dark-sector coupling optional branch
#
# Group:
#   18_vacuum_current_split
#
# Purpose
# -------
# The exchange current source-side inventory found:
#
#   No active ordinary-sector source side for J_exch is derived.
#   Sigma/R remain role-level unless distinct operators and strength laws are found.
#   Curvature admissibility, volume response, matter-induced exchange, and boundary exchange are high risk.
#   Zero-net exchange, zero creation, curvature-from-warping, and latent exchange remain the safest ordinary-sector branches.
#   Dark-sector exchange remains deferred and optional.
#
# This script audits whether dark-sector coupling can remain optional and separated.
#
# Locked-door question:
#
#   Can a dark-sector coupling be attached to vacuum exchange
#   without contaminating ordinary matter?
#
# This is an optional-branch audit, not a dark-sector derivation.


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
class DarkSectorEntry:
    name: str
    branch: str
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
        dependency_id="exchange_current_source_side_inventory_marker",
        upstream_script_id="18_vacuum_current_split__candidate_exchange_current_source_side_inventory",
        upstream_derivation_id="exchange_current_source_side_inventory_marker",
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


def build_entries() -> List[DarkSectorEntry]:
    return [
        DarkSectorEntry(
            name="DS1: dark-sector optionality target",
            branch="dark-sector coupling remains optional and separated from ordinary matter",
            role="core optional-branch guard",
            allowed_if="ordinary-sector failures are not patched by dark coupling",
            forbidden_if="dark sector is introduced to rescue J_sub/J_exch ordinary behavior",
            status="THEOREM_TARGET",
            missing="dark-sector coupling rule",
            consequence="decides whether dark coupling can remain a future branch",
        ),
        DarkSectorEntry(
            name="DS2: no dark-sector coupling",
            branch="no dark-sector coupling is introduced in Group 18",
            role="safest default",
            allowed_if="ordinary-sector current split remains unresolved/theorem-targeted",
            forbidden_if="dark coupling is treated as necessary without derivation",
            status="SAFE_IF",
            missing="none",
            consequence="keeps Group 18 ordinary-sector clean",
        ),
        DarkSectorEntry(
            name="DS3: dark coupling to J_exch only",
            branch="dark sector couples to active exchange branch, not pure substrate wind",
            role="candidate future branch",
            allowed_if="ordinary matter decoupling, mass neutrality, and source-side separation hold",
            forbidden_if="used to patch ordinary J_exch source failure",
            status="CANDIDATE",
            missing="dark source operator and decoupling theorem",
            consequence="most plausible dark branch if kept separated",
        ),
        DarkSectorEntry(
            name="DS4: dark coupling to J_sub",
            branch="dark sector couples to pure substrate flow",
            role="high-risk branch",
            allowed_if="pure wind neutrality survives and dark coupling does not make wind gravitate ordinarily",
            forbidden_if="dark coupling makes J_sub preferred-frame force or mass source",
            status="RISK",
            missing="J_sub definition and dark substrate coupling theorem",
            consequence="dangerous because it threatens pure wind neutrality",
        ),
        DarkSectorEntry(
            name="DS5: dark coupling to curvature admissibility",
            branch="dark sector couples through A_curv / curvature-admissibility channel",
            role="deferred curvature branch",
            allowed_if="A_curv dynamics or J_curv is later defined",
            forbidden_if="curvature admissibility is promoted from diagnostic to dynamics",
            status="DEFER",
            missing="A_curv dynamics / J_curv definition",
            consequence="preserves Group 17 closure",
        ),
        DarkSectorEntry(
            name="DS6: dark coupling to finite volume response",
            branch="dark sector couples through zeta / volume response",
            role="high-risk volume branch",
            allowed_if="B_s/F_zeta insertion, no-overlap, and scalar neutrality are solved",
            forbidden_if="dark coupling reopens residual trace or hidden scalar charge",
            status="RISK",
            missing="Group 16 insertion/no-overlap theorem",
            consequence="deferred until metric insertion is safe",
        ),
        DarkSectorEntry(
            name="DS7: ordinary matter separation requirement",
            branch="dark coupling does not alter ordinary matter routing",
            role="ordinary-sector guard",
            allowed_if="ordinary rho/T_mu_nu remain routed through established sectors",
            forbidden_if="dark coupling explains ordinary matter leak",
            status="REQUIRED",
            missing="ordinary/dark separation theorem",
            consequence="prevents dark sector from patching matter decoupling failure",
        ),
        DarkSectorEntry(
            name="DS8: ordinary exterior mass neutrality requirement",
            branch="dark coupling does not shift M_ext for ordinary exterior",
            role="mass neutrality guard",
            allowed_if="dark branch is invisible/neutral in ordinary exterior unless theorem derives otherwise",
            forbidden_if="dark coupling changes measured ordinary exterior mass",
            status="REQUIRED",
            missing="ordinary exterior neutrality theorem",
            consequence="protects A-sector exterior mass result",
        ),
        DarkSectorEntry(
            name="DS9: no hidden scalar charge requirement",
            branch="dark coupling does not leak through B_s/zeta/kappa as ordinary scalar charge",
            role="scalar-sector guard",
            allowed_if="dark coupling is scalar-neutral in ordinary sector",
            forbidden_if="dark branch creates ordinary scalar fifth force",
            status="REQUIRED",
            missing="scalar neutrality theorem",
            consequence="preserves Group 16 and ordinary-sector safety",
        ),
        DarkSectorEntry(
            name="DS10: source-side separation requirement",
            branch="dark Sigma_exch is distinct from ordinary Sigma_exch and ordinary T_mu_nu",
            role="source accounting guard",
            allowed_if="dark source is explicitly separated",
            forbidden_if="dark source relabels ordinary matter or boundary failure",
            status="REQUIRED",
            missing="dark source separation theorem",
            consequence="prevents double-counting and repair relabeling",
        ),
        DarkSectorEntry(
            name="DS11: dark coupling used to patch ordinary sector",
            branch="dark coupling is introduced because ordinary J_sub/J_exch failed",
            role="forbidden repair branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as dark-sector motivation",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents speculative patching",
        ),
        DarkSectorEntry(
            name="DS12: dark coupling shifts M_ext ordinary exterior",
            branch="dark coupling changes ordinary exterior mass without derived law",
            role="forbidden mass branch",
            allowed_if="never without theorem",
            forbidden_if="accepted as ordinary-sector effect",
            status="REJECTED",
            missing="not pursued",
            consequence="protects ordinary exterior mass",
        ),
        DarkSectorEntry(
            name="DS13: dark coupling as boundary repair",
            branch="dark sector cancels boundary leakage, shell source, scalar tail, or singularity behavior",
            role="forbidden boundary repair branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as dark source",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents boundary patch by dark label",
        ),
        DarkSectorEntry(
            name="DS14: dark coupling as recovery repair",
            branch="dark coupling chosen to pass gamma_like, AB, or exterior matching",
            role="forbidden recovery branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as dark coupling",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps recovery downstream",
        ),
        DarkSectorEntry(
            name="DS15: dark coupling as H_exch shortcut",
            branch="dark coupling introduced to justify H_exch/H_curv parent correction",
            role="forbidden parent-correction shortcut",
            allowed_if="deferred to Group 19",
            forbidden_if="accepted as correction-tensor source",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents decorative parent tensor",
        ),
        DarkSectorEntry(
            name="DS16: optional branch failure",
            branch="dark coupling cannot be separated from ordinary repair behavior",
            role="branch failure condition",
            allowed_if="used to keep dark sector deferred/absent",
            forbidden_if="patched with dark labels",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="dark-sector branch should remain absent",
        ),
        DarkSectorEntry(
            name="DS17: recommended next move",
            branch="close Group 18 with vacuum-current split status summary",
            role="next local bottleneck",
            allowed_if="dark coupling remains optional/deferred",
            forbidden_if="opening Group 19 before summary ledger",
            status="RECOMMENDED",
            missing="Group 18 status summary",
            consequence="next script should be candidate_vacuum_current_split_group_status_summary.py",
        ),
    ]


def print_entry(e: DarkSectorEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Branch: {e.branch}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Dark-sector optional coupling problem")

    print("Question:")
    print()
    print("  Can a dark-sector coupling be attached to vacuum exchange")
    print("  without contaminating ordinary matter?")
    print()
    print("Goal:")
    print()
    print("  keep dark-sector speculation optional and separated")
    print()
    print("Discipline:")
    print()
    print("  no dark patch for ordinary failure")
    print("  no ordinary matter rerouting")
    print("  no M_ext shift")
    print("  no hidden scalar charge")
    print("  no boundary repair")
    print("  no recovery repair")
    print("  no H_exch shortcut")
    print("  preserve no-dark-coupling default")

    status_line("dark-sector optional coupling problem posed", "REQUIRED")


def case_1_inventory(entries: List[DarkSectorEntry]):
    header("Case 1: Dark-sector optional coupling inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[DarkSectorEntry]):
    header("Case 2: Compact dark-sector optionality ledger")

    print("| Entry | Branch | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.branch.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact dark-sector optionality ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[DarkSectorEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  No dark-sector coupling is required.")
    print("  The safest default is no dark-sector coupling in Group 18.")
    print("  Dark coupling to J_exch is the least bad future candidate, if ordinary separation holds.")
    print("  Dark coupling to J_sub or zeta/volume is risky.")
    print("  Curvature-admissibility coupling is deferred.")
    print("  Dark sector must not patch ordinary failure, shift M_ext, create scalar charge, repair boundary, tune recovery, or justify H_exch.")
    print("  Next gate is Group 18 status summary.")

    status_line("dark-sector optionality status count produced", "STRUCTURAL")


def case_4_branch_classes():
    header("Case 4: Dark-sector branch classes")

    print("Dark-sector branch classes:")
    print()
    print("1. no dark-sector coupling")
    print("2. dark coupling to J_exch only")
    print("3. dark coupling to J_sub")
    print("4. dark coupling to curvature admissibility")
    print("5. dark coupling to zeta / finite volume response")
    print()
    print("Forbidden:")
    print()
    print("1. dark patch for ordinary sector")
    print("2. dark ordinary M_ext shift")
    print("3. dark boundary repair")
    print("4. dark recovery repair")
    print("5. dark H_exch shortcut")

    status_line("dark-sector branch classes listed", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: Dark-sector optionality decision tree")

    print("Decision tree:")
    print()
    print("1. No dark coupling:")
    print("   safest default.")
    print()
    print("2. Dark coupling to J_exch only:")
    print("   candidate if ordinary separation and source law exist.")
    print()
    print("3. Dark coupling to J_sub:")
    print("   high risk; threatens pure wind neutrality.")
    print()
    print("4. Dark coupling to curvature admissibility or volume:")
    print("   deferred until A_curv/J_curv or B_s/F_zeta issues are solved.")
    print()
    print("5. Dark coupling fixes ordinary failure:")
    print("   rejected.")
    print()
    print("6. Dark coupling justifies H_exch:")
    print("   rejected/deferred to Group 19.")

    status_line("dark-sector optionality decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  dark coupling cannot be separated from ordinary repair behavior.")
    print()
    print("Consequence:")
    print()
    print("  keep dark sector absent or deferred.")
    print("  close Group 18 without dark coupling.")
    print()
    print("Bad failure:")
    print()
    print("  introduce dark-sector coupling because ordinary J_exch source side failed.")

    status_line("dark-sector optionality good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Dark-sector optionality fails if:")
    print()
    print("1. dark coupling patches ordinary current failure")
    print("2. ordinary matter routing changes")
    print("3. M_ext shifts")
    print("4. hidden scalar charge appears")
    print("5. boundary repair appears")
    print("6. recovery selects dark coupling")
    print("7. H_exch/H_curv is justified by dark label")
    print("8. dark source relabels ordinary matter")
    print("9. dark coupling makes pure wind gravitate")
    print("10. no-dark default is abandoned without theorem")

    status_line("dark-sector optionality failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_dark_sector_coupling_optional_branch.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_vacuum_current_split_group_status_summary.py")
    print("   Close Group 18 with status summary and handoff.")
    print()
    print("3. candidate_dark_sector_optional_failure_summary.py")
    print("   Use if dark branch collapses into ordinary repair.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vacuum_current_split_group_status_summary.py")
    print()
    print("Reason:")
    print("  Group 18 has audited split, pure wind, J_sub, J_exch, ordinary matter decoupling, source sides, and dark optionality.")
    print("  It should close with a summary ledger before Group 19.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("No dark-sector coupling is required.")
    print()
    print("Safest default:")
    print()
    print("  no dark-sector coupling in Group 18")
    print()
    print("Least bad future candidate:")
    print()
    print("  dark coupling to J_exch only, if ordinary separation and source law exist")
    print()
    print("Rejected:")
    print()
    print("  dark patch for ordinary failure")
    print("  dark M_ext shift")
    print("  dark scalar charge leak")
    print("  dark boundary repair")
    print("  dark recovery repair")
    print("  dark H_exch shortcut")
    print()
    print("Best next script:")
    print()
    print("  candidate_vacuum_current_split_group_status_summary.py")

    status_line("dark-sector optional coupling audit complete", "CLOSED")


def main():
    header("Candidate Dark-Sector Coupling Optional Branch")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_branch_classes()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    ns.record_derivation(
        derivation_id="dark_sector_coupling_optional_branch_marker",
        inputs=[],
        output=sp.Symbol("dark_sector_coupling_optional_branch_complete"),
        method="dark_sector_coupling_optional_branch",
        status=Status.DERIVED,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
