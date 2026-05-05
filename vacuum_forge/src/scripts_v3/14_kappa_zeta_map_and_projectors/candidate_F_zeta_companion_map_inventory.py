# Candidate F_zeta companion map inventory
#
# Purpose
# -------
# The zeta companion branch test found:
#
#   Zeta companion branch is the only live branch that might solve q-origin.
#
# It survives only if:
#
#   F_zeta is derived,
#   residual zeta trace is killed/non-metric,
#   boundary neutrality and no-overlap hold.
#
# This script inventories possible F_zeta[A,zeta] maps and coefficient-origin
# constraints, while keeping residual-kill requirements attached.
#
# It is not a derivation.

from dataclasses import dataclass
from typing import List


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
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class FZetaMapEntry:
    name: str
    map_form: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[FZetaMapEntry]:
    return [
        FZetaMapEntry(
            name="FZ1: F_zeta theorem target",
            map_form="B_s = F_zeta[A,zeta] fixes q before recovery checks",
            role="core map target for zeta companion branch",
            allowed_if="F_zeta follows from volume-exchange law",
            forbidden_if="map coefficient chosen from gamma_like or AB",
            status="THEOREM_TARGET",
            missing="volume-exchange derivation of F_zeta",
            consequence="decides whether zeta companion branch solves A_spatial",
        ),
        FZetaMapEntry(
            name="FZ2: pure algebraic zeta map",
            map_form="B_s = lambda_z zeta",
            role="minimal companion map",
            allowed_if="lambda_z is fixed by ontology before recovery checks",
            forbidden_if="lambda_z is tuned to gamma_like",
            status="RISK",
            missing="lambda_z origin and gauge/slicing status",
            consequence="too easy to become coefficient patch unless derived",
        ),
        FZetaMapEntry(
            name="FZ3: algebraic A-plus-zeta map",
            map_form="B_s = G[A] + lambda_z zeta",
            role="lets A-sector and zeta-volume both contribute to B_s",
            allowed_if="G and lambda_z have separate non-overlapping origins",
            forbidden_if="G[A] duplicates A_spatial while zeta remains residual",
            status="RISK",
            missing="count-once split and lambda_z origin",
            consequence="danger of duplicating A-sector spatial trace",
        ),
        FZetaMapEntry(
            name="FZ4: differential zeta map",
            map_form="Delta B_s = r_z Delta zeta + H[A,S_A]",
            role="derivative companion candidate",
            allowed_if="r_z and H follow from exchange operator",
            forbidden_if="r_z is chosen to match q",
            status="CANDIDATE",
            missing="operator deriving r_z and H",
            consequence="may avoid direct algebraic identification but still needs coefficient origin",
        ),
        FZetaMapEntry(
            name="FZ5: source-driven map",
            map_form="Sigma_V[A,T] -> zeta -> B_s",
            role="postulate-facing map using source-driven volume creation",
            allowed_if="Sigma_V is expressed before recovery checks",
            forbidden_if="source term is invented to repair A_spatial",
            status="CANDIDATE",
            missing="source-driven volume creation law",
            consequence="connects to mass/source coupling but remains central missing mechanism",
        ),
        FZetaMapEntry(
            name="FZ6: non-metric bookkeeping map",
            map_form="zeta tracks vacuum configuration; metric trace insertion only through B_s",
            role="safe ontology-preserving map",
            allowed_if="bookkeeping-to-metric map is explicit",
            forbidden_if="zeta appears separately as metric trace",
            status="CANDIDATE",
            missing="bookkeeping-to-metric rule",
            consequence="could preserve vacuum ontology while avoiding exterior scalar charge",
        ),
        FZetaMapEntry(
            name="FZ7: residual-kill theorem",
            map_form="zeta_residual_metric = 0 or non-metric after F_zeta map",
            role="mandatory companion-branch broom",
            allowed_if="proved or made definitional by map",
            forbidden_if="residual zeta remains metric-active",
            status="REQUIRED",
            missing="residual-kill / non-metric theorem",
            consequence="prevents zeta from being both companion and residual",
        ),
        FZetaMapEntry(
            name="FZ8: no-overlap operator",
            map_form="O[B_s,zeta_residual/kappa_residual] = 0",
            role="count-once recombination guardrail",
            allowed_if="operator is explicit or residual killed",
            forbidden_if="overlap is asserted without consequence",
            status="REQUIRED",
            missing="overlap operator or residual-kill theorem",
            consequence="map fails if B_s and residual trace overlap",
        ),
        FZetaMapEntry(
            name="FZ9: boundary neutrality",
            map_form="Q_ext[zeta independent] = 0; companion contribution absorbed into B_s",
            role="protects no exterior scalar charge",
            allowed_if="zeta has no independent exterior charge",
            forbidden_if="F_zeta creates scalar exterior charge",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="prevents companion branch from becoming scalar gravity",
        ),
        FZetaMapEntry(
            name="FZ10: kappa cleanup consequence",
            map_form="kappa remains diagnostic/non-metric or separately neutral after zeta map",
            role="prevents kappa from resurrecting killed residual trace",
            allowed_if="kappa does not become overlapping metric scalar",
            forbidden_if="kappa replaces residual zeta trace",
            status="CONSTRAINED",
            missing="post-F_zeta kappa status script",
            consequence="requires later kappa cleanup after F_zeta branch decision",
        ),
        FZetaMapEntry(
            name="FZ11: recovery checks downstream",
            map_form="after F_zeta fixed, test gamma_like=1 and AB->1",
            role="ordinary-regime recovery tests",
            allowed_if="checked after map and coefficients are derived",
            forbidden_if="used to choose F_zeta",
            status="RECOVERY_TARGET",
            missing="solutions after F_zeta",
            consequence="tests but does not define map",
        ),
        FZetaMapEntry(
            name="FZ12: recommended next move",
            map_form="test differential/source-driven maps before accepting algebraic lambda_z",
            role="best current concrete path",
            allowed_if="residual-kill theorem stays attached",
            forbidden_if="testing map coefficients without residual kill",
            status="RECOMMENDED",
            missing="source-driven volume creation law or differential map test",
            consequence="next script should test source-driven volume creation law, not tune algebraic map",
        ),
    ]


def print_entry(e: FZetaMapEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Map form: {e.map_form}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: F_zeta companion map inventory problem")

    print("Question:")
    print()
    print("  Which F_zeta[A,zeta] maps can be tested without turning zeta into a recovery patch?")
    print()
    print("Goal:")
    print()
    print("  inventory companion map forms and keep residual-kill requirements attached")
    print()
    print("Discipline:")
    print()
    print("  do not tune map coefficients from gamma_like or AB")
    print("  do not let zeta remain metric residual")
    print("  preserve boundary neutrality")
    print("  preserve no-overlap")
    print("  expose kappa cleanup consequence")
    print("  prefer source-driven/differential maps over algebraic fitting")

    status_line("F_zeta companion map problem posed", "REQUIRED")


def case_1_inventory(entries: List[FZetaMapEntry]):
    header("Case 1: F_zeta companion map inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[FZetaMapEntry]):
    header("Case 2: Compact F_zeta map ledger")

    print("| Entry | Map form | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.map_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact F_zeta map ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[FZetaMapEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Algebraic F_zeta maps are high-risk coefficient patches.")
    print("  Differential and source-driven maps are better candidates but need exchange/source laws.")
    print("  Residual-kill, no-overlap, and boundary neutrality are mandatory.")
    print("  Kappa cleanup is downstream, not optional.")

    status_line("F_zeta map status count produced", "STRUCTURAL")


def case_4_map_decision_tree():
    header("Case 4: F_zeta map decision tree")

    print("Decision tree:")
    print()
    print("1. Pure algebraic map B_s = lambda_z zeta?")
    print("   Only acceptable if lambda_z is derived before recovery.")
    print()
    print("2. A-plus-zeta algebraic map?")
    print("   Requires count-once split: G[A] and zeta must not duplicate spatial trace.")
    print()
    print("3. Differential zeta map?")
    print("   Better candidate if r_z follows from exchange operator.")
    print()
    print("4. Source-driven map?")
    print("   Best postulate-facing route if Sigma_V can be expressed.")
    print()
    print("5. Non-metric bookkeeping?")
    print("   Safe only if metric insertion occurs solely through B_s.")

    status_line("F_zeta map decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  no F_zeta map has coefficient origin without residual zeta trace staying active.")
    print()
    print("Consequence:")
    print()
    print("  zeta companion branch fails.")
    print("  A_spatial returns to recovery theorem target status.")
    print("  zeta may remain residual only under P_relax if neutral and non-radiative.")
    print()
    print("Bad failure:")
    print("  choose lambda_z from gamma_like and declare zeta the companion.")

    status_line("F_zeta map good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("F_zeta map inventory fails if:")
    print()
    print("1. lambda_z is chosen from gamma_like")
    print("2. AB diagnostic chooses map coefficient")
    print("3. G[A] duplicates A_spatial mass trace")
    print("4. zeta residual metric trace remains active")
    print("5. boundary neutrality is absent")
    print("6. no-overlap operator/theorem is absent")
    print("7. kappa restores killed residual trace")
    print("8. source-driven volume creation remains unnamed")

    status_line("F_zeta map failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_F_zeta_companion_map_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_source_driven_volume_creation_law.py")
    print("   Express Sigma_V[A,T] before using it in F_zeta.")
    print()
    print("3. candidate_kappa_diagnostic_or_residual_after_zeta.py")
    print("   Clean up kappa after zeta residual trace is killed/non-metric.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_source_driven_volume_creation_law.py")
    print()
    print("Reason:")
    print("  The best non-fitting F_zeta route is source-driven volume creation. Express Sigma_V before adding more map structure.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("F_zeta map inventory narrows the companion branch:")
    print()
    print("  algebraic maps are risky patches,")
    print("  differential maps need an exchange operator,")
    print("  source-driven maps need Sigma_V[A,T].")
    print()
    print("Best next test:")
    print("  candidate_source_driven_volume_creation_law.py")


def main():
    header("Candidate F_zeta Companion Map Inventory")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_map_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
