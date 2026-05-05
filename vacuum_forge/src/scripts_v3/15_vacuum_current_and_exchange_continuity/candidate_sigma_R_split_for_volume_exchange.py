# Candidate Sigma/R split for volume exchange
#
# Purpose
# -------
# The exchange-continuity opening script found:
#
#   nabla_mu J_V^mu = Sigma_V - R_V
#
# is the right locked door, but not yet a law.
#
# The next bottleneck is to split:
#
#   Sigma_V = source / creation / destruction term
#   R_V     = relaxation / reconfiguration / return term
#
# before claiming exchange continuity defines J_V.
#
# This script inventories possible Sigma_V and R_V roles.
#
# It is not a derivation of either term.

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
        "CLOSED": "PASS",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class SigmaRSplitEntry:
    name: str
    term: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[SigmaRSplitEntry]:
    return [
        SigmaRSplitEntry(
            name="SR1: Sigma/R split target",
            term="nabla_mu J_V^mu = Sigma_V - R_V with source and relaxation independently meaningful",
            role="core requirement for exchange continuity to become a law",
            allowed_if="Sigma_V and R_V have distinct mechanisms and compatible signs",
            forbidden_if="Sigma_V and R_V are named only to balance the equation",
            status="THEOREM_TARGET",
            missing="mechanism split, sign convention, operator definitions",
            consequence="decides whether continuity has a source side worth using",
        ),
        SigmaRSplitEntry(
            name="SR2: Sigma_V as source-driven creation/destruction",
            term="Sigma_V[A,T] creates or destroys vacuum-volume configuration",
            role="source side of volume continuity",
            allowed_if="source law is explicit and not chosen from recovery",
            forbidden_if="Sigma_V becomes gamma_like / AB repair term",
            status="CANDIDATE",
            missing="complete Sigma_V law and coefficient origin",
            consequence="can feed volume exchange only if independently defined",
        ),
        SigmaRSplitEntry(
            name="SR3: acceleration-gradient Sigma_V",
            term="Sigma_V ~ chi rho a^mu nabla_mu A",
            role="best inherited source-driven candidate from Group 14",
            allowed_if="frame/projection, chi-origin, and static safety are defined",
            forbidden_if="coordinate velocity or recovery-fitted chi is used",
            status="CANDIDATE",
            missing="frame/projection, chi-origin, static-source safety",
            consequence="remains theorem target until frame and chi are real",
        ),
        SigmaRSplitEntry(
            name="SR4: trace/volume conversion Sigma_V",
            term="Sigma_V from trace/pressure/volume conversion into zeta",
            role="possible conversion source",
            allowed_if="projected, compact/boundary-neutral, and non-radiative",
            forbidden_if="raw pressure/trace scalar source creates exterior charge",
            status="RISK",
            missing="P_trace/P_boundary mechanism and no scalar charge theorem",
            consequence="dangerous because it can revive rejected trace scalar gravity",
        ),
        SigmaRSplitEntry(
            name="SR5: active creation Sigma_V",
            term="Sigma_creation != 0 active/non-ordinary regime",
            role="nonconservative or active-regime source",
            allowed_if="explicitly outside ordinary closed gravity",
            forbidden_if="leaks into ordinary-sector recovery",
            status="CONSTRAINED",
            missing="active-regime ontology and boundary conditions",
            consequence="not available for ordinary static/weak recovery branch",
        ),
        SigmaRSplitEntry(
            name="SR6: R_V as local equilibrium restoration",
            term="R_V restores zeta or volume configuration toward local equilibrium",
            role="relaxation / reconfiguration side of continuity",
            allowed_if="local equilibrium target is defined before use",
            forbidden_if="R_V is damping pasted onto scalar waves",
            status="CANDIDATE",
            missing="equilibrium target and operator",
            consequence="can balance Sigma_V only if not energy destruction",
        ),
        SigmaRSplitEntry(
            name="SR7: R_V as zeta_min relaxation",
            term="R_V ~ lambda_z (zeta - zeta_min)",
            role="minimal local relaxation candidate",
            allowed_if="zeta_min and lambda_z have ontology/source origin",
            forbidden_if="lambda_z is tuned to kill scalar exterior charge",
            status="RISK",
            missing="zeta_min, lambda_z, sign convention",
            consequence="may become another coefficient patch if not derived",
        ),
        SigmaRSplitEntry(
            name="SR8: R_V as kappa-linked relaxation",
            term="R_V linked to kappa residual / e_kappa exchange",
            role="connects Group 14 residual accounting to volume continuity",
            allowed_if="kappa remains diagnostic/non-metric or separately neutral",
            forbidden_if="kappa reintroduces duplicate scalar trace",
            status="RISK",
            missing="post-Group-14 kappa status and no-overlap theorem",
            consequence="high double-counting risk unless kappa cleanup is explicit",
        ),
        SigmaRSplitEntry(
            name="SR9: R_V as boundary-neutral reconfiguration",
            term="R_V redistributes local volume with zero exterior flux / zero charge",
            role="ordinary-sector safety mechanism candidate",
            allowed_if="compact support or boundary theorem is explicit",
            forbidden_if="R_V cancels exterior scalar charge by tuning",
            status="CANDIDATE",
            missing="boundary/no-flux theorem and flux direction",
            consequence="could protect exterior neutrality but cannot replace source law",
        ),
        SigmaRSplitEntry(
            name="SR10: Sigma/R double-counting guard",
            term="Sigma_V and R_V must not be two names for the same volume change",
            role="prevents fake continuity balance",
            allowed_if="creation and relaxation mechanisms are distinct but coupled",
            forbidden_if="same effect appears with opposite signs to force closure",
            status="REQUIRED",
            missing="source/relaxation accounting rule",
            consequence="without this, continuity is algebraic bookkeeping only",
        ),
        SigmaRSplitEntry(
            name="SR11: sign/orientation convention",
            term="positive Sigma_V and positive R_V must have fixed creation/restoration meaning",
            role="required for physical interpretation",
            allowed_if="sign follows from exchange ontology before recovery",
            forbidden_if="signs chosen from desired recovery",
            status="UNRESOLVED",
            missing="orientation convention",
            consequence="needed before flux direction, simulation, or recovery claims",
        ),
        SigmaRSplitEntry(
            name="SR12: ordinary closed-regime constraint",
            term="ordinary gravity has no net volume charge, no far-zone scalar flux, no M_ext shift",
            role="safety guard for Sigma/R split",
            allowed_if="Sigma/R balance is compact, neutral, and recombination-safe",
            forbidden_if="ordinary static source creates exterior zeta/kappa charge",
            status="REQUIRED",
            missing="static neutrality and boundary theorem",
            consequence="kills Sigma/R split if it produces scalar gravity",
        ),
        SigmaRSplitEntry(
            name="SR13: decorative Sigma/R rejection",
            term="Sigma_V and R_V named without mechanisms or operators",
            role="rejected shortcut",
            allowed_if="never as derivation",
            forbidden_if="used to promote J_V",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents continuity from becoming painted conservation language",
        ),
        SigmaRSplitEntry(
            name="SR14: recovery downstream",
            term="after Sigma/R/J_V structure fixed, test gamma_like and AB",
            role="ordinary-regime recovery target",
            allowed_if="checked only after split and flux law exist",
            forbidden_if="used to choose Sigma/R signs or coefficients",
            status="RECOVERY_TARGET",
            missing="solutions after exchange law",
            consequence="keeps recovery from becoming construction",
        ),
        SigmaRSplitEntry(
            name="SR15: recommended next move",
            term="after Sigma/R split, test J_V flux direction law",
            role="best next bottleneck if split survives",
            allowed_if="Sigma/R are sufficiently separated as source and relaxation targets",
            forbidden_if="jumping to flux direction while Sigma/R are still decorative",
            status="RECOMMENDED",
            missing="volume flux direction law",
            consequence="next script should test what determines J_V direction",
        ),
    ]


def print_entry(e: SigmaRSplitEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Term: {e.term}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Sigma/R split problem")

    print("Question:")
    print()
    print("  What is source/creation, and what is relaxation/reconfiguration?")
    print()
    print("Goal:")
    print()
    print("  split Sigma_V and R_V before using exchange continuity to define J_V")
    print()
    print("Discipline:")
    print()
    print("  do not use Sigma_V as recovery repair spell")
    print("  do not use R_V as scalar-charge cancellation patch")
    print("  do not let Sigma/R double-count the same volume change")
    print("  preserve ordinary closed-regime neutrality")
    print("  keep sign/orientation explicit")
    print("  keep gamma/AB recovery downstream")

    status_line("Sigma/R split problem posed", "REQUIRED")


def case_1_inventory(entries: List[SigmaRSplitEntry]):
    header("Case 1: Sigma/R split inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[SigmaRSplitEntry]):
    header("Case 2: Compact Sigma/R split ledger")

    print("| Entry | Term | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.term.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact Sigma/R ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[SigmaRSplitEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Sigma_V and R_V can be separated as roles, but neither is yet derived.")
    print("  Acceleration-gradient Sigma_V remains the strongest source candidate.")
    print("  R_V as local equilibrium restoration is the cleanest relaxation candidate.")
    print("  Trace-source and kappa-linked branches are risky because they can revive double-counting.")
    print("  Flux direction is still missing and should be tested next if this split survives.")

    status_line("Sigma/R status count produced", "STRUCTURAL")


def case_4_split_decision_tree():
    header("Case 4: Split decision tree")

    print("Decision tree:")
    print()
    print("1. Sigma_V as source-driven creation/destruction:")
    print("   viable only if source law and coefficient origin are independent.")
    print()
    print("2. Sigma_V as trace/volume conversion:")
    print("   dangerous unless projected, compact, and non-radiative.")
    print()
    print("3. R_V as local equilibrium restoration:")
    print("   cleanest relaxation role if equilibrium target exists.")
    print()
    print("4. R_V as zeta_min or kappa-linked relaxation:")
    print("   possible but high coefficient/double-counting risk.")
    print()
    print("5. R_V as boundary-neutral reconfiguration:")
    print("   useful safety mechanism, not a substitute for flux law.")
    print()
    print("6. If Sigma/R remain decorative:")
    print("   exchange continuity branch fails or defers.")

    status_line("Sigma/R split decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  Sigma_V and R_V cannot be separated without using R_V as a patch,")
    print("  or Sigma_V as a recovery-tuned source.")
    print()
    print("Consequence:")
    print()
    print("  exchange continuity remains a theorem target.")
    print("  Do not proceed to J_V flux direction until the source side is meaningful.")
    print()
    print("Bad failure:")
    print("  define Sigma_V and R_V as whatever makes nabla_mu J_V^mu balance.")

    status_line("Sigma/R split good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Sigma/R split fails if:")
    print()
    print("1. Sigma_V is chosen from gamma_like or AB")
    print("2. R_V is used to cancel scalar charge by hand")
    print("3. Sigma_V and R_V double-count the same volume change")
    print("4. trace/pressure source revives scalar gravity")
    print("5. kappa-linked R_V restores duplicate residual trace")
    print("6. signs are chosen from desired recovery")
    print("7. ordinary closed regime gets net volume charge")
    print("8. J_V is promoted before flux direction exists")

    status_line("Sigma/R split failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_sigma_R_split_for_volume_exchange.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_volume_flux_direction_law.py")
    print("   Test what determines J_V direction.")
    print()
    print("3. candidate_sigma_R_early_failure_summary.py")
    print("   Use if Sigma/R cannot be split without decoration.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_volume_flux_direction_law.py")
    print()
    print("Reason:")
    print("  If Sigma/R are separated as source and relaxation roles, the next missing object is the flux direction of J_V.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Sigma_V and R_V can be separated as roles, but not yet derived.")
    print()
    print("Best current interpretation:")
    print()
    print("  Sigma_V = source / creation / destruction side")
    print("  R_V     = relaxation / reconfiguration / return side")
    print()
    print("The next missing object is still:")
    print()
    print("  J_V flux direction")
    print()
    print("Best next test:")
    print("  candidate_volume_flux_direction_law.py")


def main():
    header("Candidate Sigma/R Split For Volume Exchange")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_split_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
