# Candidate timelike domain for volume current
#
# Purpose
# -------
# The volume flux-direction law inventory found:
#
#   Sigma_V - R_V gives divergence, not direction.
#   J_V needs an independent flux / transport law.
#
# If any direction candidate survives, the next gate is:
#
#   J_V^2 < 0
#   J_V != 0
#
# where u_vac = J_V / sqrt(-J_V^2) is used.
#
# This script inventories timelike/nonzero domain requirements for surviving
# J_V candidates.
#
# It is not a derivation of J_V.

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
class TimelikeDomainEntry:
    name: str
    domain_test: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[TimelikeDomainEntry]:
    return [
        TimelikeDomainEntry(
            name="TD1: timelike-domain target",
            domain_test="J_V^2 < 0 and J_V != 0 where u_vac = J_V / sqrt(-J_V^2) is used",
            role="core viability condition for defining vacuum rest frame from current",
            allowed_if="domain is proved or explicitly restricted before u_vac is used",
            forbidden_if="J_V is normalized where it is spacelike, null, or zero",
            status="THEOREM_TARGET",
            missing="domain theorem for candidate J_V",
            consequence="decides whether J_V can define u_vac anywhere useful",
        ),
        TimelikeDomainEntry(
            name="TD2: zeta-gradient current domain",
            domain_test="J_V^mu ~ -D_z nabla^mu zeta requires (nabla zeta)^2 < 0 and nabla zeta != 0",
            role="domain test for minimal zeta-gradient flux",
            allowed_if="zeta gradient is timelike/nonzero in active exchange regions only",
            forbidden_if="used in static, spacelike, null, or zero-gradient regimes",
            status="RISK",
            missing="zeta-gradient causal character theorem",
            consequence="likely domain-limited, not a general vacuum clock",
        ),
        TimelikeDomainEntry(
            name="TD3: exchange-potential current domain",
            domain_test="J_V^mu ~ -D_V nabla^mu Phi_V requires (nabla Phi_V)^2 < 0 and Phi_V defined",
            role="domain test for exchange-potential flux",
            allowed_if="Phi_V exists and has timelike gradient where u_vac is needed",
            forbidden_if="Phi_V is invented or has spacelike/null gradient in target regimes",
            status="CANDIDATE",
            missing="Phi_V definition and causal-character theorem",
            consequence="could define u_vac only if exchange potential has clock-like gradient",
        ),
        TimelikeDomainEntry(
            name="TD4: causal transport current domain",
            domain_test="transport J_V has causal/timelike current with finite characteristic speed",
            role="domain test for dynamic current candidate",
            allowed_if="transport law preserves timelike/nonzero J_V without Box zeta",
            forbidden_if="transport becomes scalar radiation or spacelike signal",
            status="CANDIDATE",
            missing="transport equation and hyperbolic/first-order domain theorem",
            consequence="strong candidate if it avoids scalar wave behavior",
        ),
        TimelikeDomainEntry(
            name="TD5: compact-support redistribution domain",
            domain_test="J_V timelike/nonzero only inside compact active region; zero boundary flux",
            role="domain-limited ordinary-sector safety branch",
            allowed_if="u_vac is used only in active region and no exterior scalar charge is created",
            forbidden_if="normalization is demanded outside support where J_V=0",
            status="SAFE_IF",
            missing="support theorem and interior causal character",
            consequence="may define local u_vac but not a global vacuum clock",
        ),
        TimelikeDomainEntry(
            name="TD6: zero-flux local equilibrium",
            domain_test="J_V = 0 in static/local equilibrium while Sigma_V = R_V pointwise",
            role="equilibrium branch with no current-defined clock",
            allowed_if="u_vac not required from J_V in zero-current equilibrium",
            forbidden_if="u_vac is normalized from J_V=0",
            status="SAFE_IF",
            missing="separate equilibrium-frame rule if frame is still needed",
            consequence="protects neutrality but forces u_vac fallback outside current definition",
        ),
        TimelikeDomainEntry(
            name="TD7: spacelike redistribution current",
            domain_test="J_V^2 > 0 in spatial redistribution regimes",
            role="failure / non-clock branch",
            allowed_if="treated as spatial flux that does not define u_vac",
            forbidden_if="used to normalize vacuum rest frame",
            status="CONSTRAINED",
            missing="separate treatment of spatial flux versus frame current",
            consequence="J_V may exist as redistribution current without defining u_vac",
        ),
        TimelikeDomainEntry(
            name="TD8: null transition current",
            domain_test="J_V^2 = 0 at transition or boundary surfaces",
            role="domain boundary / failure surface",
            allowed_if="normalization excluded or patched by separate limit rule",
            forbidden_if="u_vac used at null current points",
            status="RISK",
            missing="transition-domain rule",
            consequence="creates boundaries where vacuum clock is undefined",
        ),
        TimelikeDomainEntry(
            name="TD9: vanishing-current nodes",
            domain_test="J_V = 0 at equilibrium nodes, centers, or exterior",
            role="normalization failure zone",
            allowed_if="domain of u_vac excludes zero-current regions",
            forbidden_if="global u_vac is claimed from J_V",
            status="REQUIRED",
            missing="domain restriction / fallback frame",
            consequence="prevents false global vacuum rest frame",
        ),
        TimelikeDomainEntry(
            name="TD10: domain-limited u_vac",
            domain_test="u_vac exists only on D_V = {J_V^2 < 0, J_V != 0}",
            role="honest partial-definition branch",
            allowed_if="field equations do not require u_vac outside D_V",
            forbidden_if="u_vac is silently extended beyond its domain",
            status="CANDIDATE",
            missing="domain-dependent equation rules",
            consequence="may save J_V definition by limiting where clock is used",
        ),
        TimelikeDomainEntry(
            name="TD11: equilibrium-frame fallback",
            domain_test="where J_V = 0, define vacuum frame by equilibrium/minimization rather than current",
            role="possible fallback if current vanishes in static equilibrium",
            allowed_if="equilibrium frame is independently defined",
            forbidden_if="arbitrary preferred frame is introduced",
            status="DEFER",
            missing="equilibrium-frame definition",
            consequence="may be needed if static regions require u_vac but have J_V=0",
        ),
        TimelikeDomainEntry(
            name="TD12: boundary neutrality requirement",
            domain_test="candidate domain must not create exterior scalar charge or forbidden far-zone flux",
            role="ordinary-sector safety guard",
            allowed_if="boundary theorem holds on and outside current domain",
            forbidden_if="timelike current leaks scalar flux or changes M_ext",
            status="REQUIRED",
            missing="boundary theorem tied to domain",
            consequence="kills timelike domains that become scalar gravity",
        ),
        TimelikeDomainEntry(
            name="TD13: no-overlap requirement",
            domain_test="J_V-driven zeta enters metric only through B_s, or residual killed/non-metric",
            role="count-once recombination guard",
            allowed_if="no-overlap theorem holds on current domain",
            forbidden_if="domain creates independent residual trace",
            status="REQUIRED",
            missing="domain-sensitive no-overlap theorem",
            consequence="prevents current-defined frame from reviving scalar duplicate",
        ),
        TimelikeDomainEntry(
            name="TD14: recovery downstream",
            domain_test="gamma_like and AB checked only after direction and domain are fixed",
            role="ordinary-regime recovery target",
            allowed_if="checked after J_V domain is defined",
            forbidden_if="used to select where J_V is timelike",
            status="RECOVERY_TARGET",
            missing="solutions after domain law",
            consequence="keeps recovery from choosing the current domain",
        ),
        TimelikeDomainEntry(
            name="TD15: recommended next move",
            domain_test="if domain survives, test static-source neutrality for J_V/Sigma/R",
            role="best next bottleneck",
            allowed_if="at least one candidate current has a viable timelike/nonzero domain",
            forbidden_if="jumping to static neutrality without a domain",
            status="RECOMMENDED",
            missing="static-source neutrality test",
            consequence="next script should test whether the candidate current produces exterior scalar charge around static sources",
        ),
    ]


def print_entry(e: TimelikeDomainEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Domain test: {e.domain_test}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Timelike domain problem")

    print("Question:")
    print()
    print("  Is J_V timelike and nonzero where u_vac is needed?")
    print()
    print("Goal:")
    print()
    print("  test whether surviving current candidates can define u_vac")
    print()
    print("Discipline:")
    print()
    print("  do not normalize spacelike/null/zero J_V")
    print("  do not claim global u_vac from domain-limited current")
    print("  separate active current regions from equilibrium regions")
    print("  preserve boundary neutrality")
    print("  preserve no-overlap / residual-kill")
    print("  keep recovery checks downstream")

    status_line("timelike domain problem posed", "REQUIRED")


def case_1_inventory(entries: List[TimelikeDomainEntry]):
    header("Case 1: Timelike domain inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[TimelikeDomainEntry]):
    header("Case 2: Compact timelike-domain ledger")

    print("| Entry | Domain test | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.domain_test.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact timelike-domain ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[TimelikeDomainEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  J_V can define u_vac only where J_V is timelike and nonzero.")
    print("  Zeta-gradient and null/transition domains are risky.")
    print("  Compact-support domains may be safe but only define local u_vac.")
    print("  Zero-flux equilibrium protects neutrality but cannot define u_vac from J_V.")
    print("  If a domain survives, static-source neutrality is the next bottleneck.")

    status_line("timelike-domain status count produced", "STRUCTURAL")


def case_4_domain_decision_tree():
    header("Case 4: Domain decision tree")

    print("Decision tree:")
    print()
    print("1. Timelike/nonzero current:")
    print("   u_vac can be defined on that active domain.")
    print()
    print("2. Spacelike current:")
    print("   may be a spatial redistribution flux, not a vacuum clock.")
    print()
    print("3. Null current:")
    print("   transition / boundary zone; u_vac undefined unless separate limit rule exists.")
    print()
    print("4. Zero current:")
    print("   equilibrium/no-flux zone; u_vac cannot be normalized from J_V.")
    print()
    print("5. Domain-limited u_vac:")
    print("   acceptable only if equations do not need u_vac outside domain.")
    print()
    print("6. Equilibrium-frame fallback:")
    print("   deferred unless static regions require a frame.")

    status_line("timelike-domain decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  surviving J_V candidates are spacelike, null, or zero in the regimes")
    print("  where u_vac is needed.")
    print()
    print("Consequence:")
    print()
    print("  J_V cannot define u_vac there.")
    print("  Exchange continuity remains a theorem target or requires equilibrium-frame fallback.")
    print()
    print("Bad failure:")
    print("  normalize J_V anyway and pretend the vacuum clock exists globally.")

    status_line("timelike-domain good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Timelike-domain test fails if:")
    print()
    print("1. J_V is normalized where J_V^2 >= 0")
    print("2. J_V is normalized where J_V = 0")
    print("3. zeta-gradient current is used outside timelike/nonzero domain")
    print("4. global u_vac is claimed from compact/local current")
    print("5. equilibrium regions require u_vac but have no fallback")
    print("6. boundary neutrality is absent")
    print("7. no-overlap is absent")
    print("8. recovery checks choose the current domain")

    status_line("timelike-domain failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_timelike_domain_for_volume_current.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_static_source_neutrality_for_J_V.py")
    print("   Test whether candidate J_V/Sigma/R structure creates exterior scalar charge around static sources.")
    print()
    print("3. candidate_equilibrium_frame_without_JV.py")
    print("   Use only if J_V vanishes where a frame is still required.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_static_source_neutrality_for_J_V.py")
    print()
    print("Reason:")
    print("  If a timelike/nonzero domain can be stated, the next ordinary-sector gate is static-source neutrality.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("J_V defines u_vac only on a timelike/nonzero domain.")
    print()
    print("Best current interpretation:")
    print()
    print("  u_vac is domain-limited unless a separate equilibrium-frame rule is derived.")
    print()
    print("Best next test:")
    print("  candidate_static_source_neutrality_for_J_V.py")


def main():
    header("Candidate Timelike Domain For Volume Current")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_domain_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
