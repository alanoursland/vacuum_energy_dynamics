# Candidate curvature boundary and mass neutrality
#
# Group:
#   17_curvature_energy_and_finite_admissibility
#
# Purpose
# -------
# The curvature balance law audit found:
#
#   Curvature balance remains a theorem target, not a law.
#
# Strongest possible form:
#
#   nabla_mu J_curv^mu = Sigma_curv - R_curv
#
# But this is not usable until J_curv, Sigma_curv, R_curv, domain, and measure are defined.
#
# Safe fallback:
#
#   curvature admissibility remains diagnostic / branch-filter only.
#
# This script tests the next safety gate:
#
#   Does curvature admissibility or J_curv alter exterior mass,
#   create boundary repair behavior,
#   or leak an ordinary-sector scalar charge?
#
# This is a boundary/mass neutrality audit, not a current derivation.


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
        "DERIVED_REDUCED": "PASS",
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
class CurvatureNeutralityEntry:
    name: str
    neutrality_rule: str
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
        dependency_id="curvature_balance_law_marker",
        upstream_script_id="17_curvature_energy_and_finite_admissibility__candidate_curvature_balance_law",
        upstream_derivation_id="curvature_balance_law_marker",
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


def build_entries() -> List[CurvatureNeutralityEntry]:
    return [
        CurvatureNeutralityEntry(
            name="CN1: curvature boundary/mass neutrality target",
            neutrality_rule="curvature admissibility/J_curv creates no exterior mass shift, boundary repair, or ordinary scalar leakage",
            role="core ordinary-sector safety theorem target",
            allowed_if="neutrality follows structurally before anti-singularity claims",
            forbidden_if="neutrality is imposed after leakage appears",
            status="THEOREM_TARGET",
            missing="boundary and mass neutrality theorem",
            consequence="decides whether curvature admissibility can remain ordinary-sector safe",
        ),
        CurvatureNeutralityEntry(
            name="CN2: no M_ext shift",
            neutrality_rule="delta M_ext|curv = 0 unless derived through A-sector source law",
            role="mass protection requirement",
            allowed_if="curvature admissibility is diagnostic/interior or source-coupled only through derived A-sector law",
            forbidden_if="curvature energy/current changes measured exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        CurvatureNeutralityEntry(
            name="CN3: no boundary repair current",
            neutrality_rule="J_curv or boundary functional does not cancel blowup, leakage, or mass shift at boundary",
            role="boundary repair rejection",
            allowed_if="boundary behavior is diagnostic or structurally neutral",
            forbidden_if="boundary current is chosen to repair failure",
            status="REQUIRED",
            missing="boundary mechanism / neutrality proof",
            consequence="prevents singularity avoidance by boundary patch",
        ),
        CurvatureNeutralityEntry(
            name="CN4: no exterior scalar charge",
            neutrality_rule="curvature admissibility creates no exterior zeta/kappa/scalar charge",
            role="ordinary exterior scalar guard",
            allowed_if="curvature object is scalar-neutral or residual remains non-metric",
            forbidden_if="curvature admissibility leaks scalar charge outside source",
            status="REQUIRED",
            missing="exterior scalar neutrality theorem",
            consequence="prevents curvature admissibility from becoming scalar gravity",
        ),
        CurvatureNeutralityEntry(
            name="CN5: no far-zone curvature flux",
            neutrality_rule="no ordinary-sector far-zone curvature/admissibility flux unless a real radiative channel is derived",
            role="radiation/exterior guard",
            allowed_if="flux is diagnostic only or tied to derived tensor/current sector",
            forbidden_if="curvature flux becomes hidden scalar radiation",
            status="REQUIRED",
            missing="far-zone flux theorem",
            consequence="protects ordinary radiation constraints",
        ),
        CurvatureNeutralityEntry(
            name="CN6: no hidden matter coupling",
            neutrality_rule="curvature admissibility does not modify ordinary matter coupling or double-count T_mu_nu",
            role="matter separation guard",
            allowed_if="matter source remains routed independently",
            forbidden_if="curvature object fixes singular behavior by rerouting matter",
            status="REQUIRED",
            missing="matter separation theorem",
            consequence="prevents matter-sector repair behavior",
        ),
        CurvatureNeutralityEntry(
            name="CN7: no recovery-tuned smoothing",
            neutrality_rule="boundary smoothing/support is not chosen to pass gamma_like, AB, or exterior matching",
            role="anti-smuggling guard",
            allowed_if="support/smoothing follows admissibility object structurally",
            forbidden_if="smoothing is recovery fit",
            status="REQUIRED",
            missing="support/matching law",
            consequence="keeps recovery downstream",
        ),
        CurvatureNeutralityEntry(
            name="CN8: interior-only admissibility branch",
            neutrality_rule="finite admissibility acts only as interior branch filter / diagnostic",
            role="safe fallback branch",
            allowed_if="it has no exterior mass/charge/flux effect",
            forbidden_if="interior diagnostic secretly changes exterior fields",
            status="SAFE_IF",
            missing="interior/exterior separation theorem",
            consequence="keeps anti-singularity claim at diagnostic/branch-filter level",
        ),
        CurvatureNeutralityEntry(
            name="CN9: compact curvature support candidate",
            neutrality_rule="curvature admissibility support is compact or decays structurally with no exterior tail",
            role="candidate exterior-neutral route",
            allowed_if="support law is derived and not imposed as repair",
            forbidden_if="compact support is chosen after leakage is found",
            status="CANDIDATE",
            missing="support law and smooth matching",
            consequence="possible path to exterior neutrality if made real",
        ),
        CurvatureNeutralityEntry(
            name="CN10: boundary flux diagnostic only",
            neutrality_rule="boundary flux may diagnose admissibility leakage but cannot define physical repair flux",
            role="diagnostic boundary audit",
            allowed_if="kept explicitly diagnostic",
            forbidden_if="diagnostic flux becomes current mechanism",
            status="SAFE_IF",
            missing="physical boundary mechanism if promoted",
            consequence="useful for audits without hardening scaffold",
        ),
        CurvatureNeutralityEntry(
            name="CN11: smooth finite-admissible transition candidate",
            neutrality_rule="interior finite-admissible region transitions smoothly to exterior without shell source",
            role="candidate matching branch",
            allowed_if="transition follows from admissibility/support law",
            forbidden_if="transition function is tuned to recover exterior metric",
            status="CANDIDATE",
            missing="transition law and shell-avoidance theorem",
            consequence="possible if no recovery tuning or shell source",
        ),
        CurvatureNeutralityEntry(
            name="CN12: J_curv exterior-neutral candidate",
            neutrality_rule="J_curv is zero, tangent, diagnostic, or compact at ordinary exterior boundary",
            role="candidate current safety branch",
            allowed_if="J_curv has real direction/support law",
            forbidden_if="J_curv exterior behavior is chosen to cancel leakage",
            status="CANDIDATE",
            missing="J_curv support/orientation law",
            consequence="could keep current candidate alive if current is later defined",
        ),
        CurvatureNeutralityEntry(
            name="CN13: e_curv mass reservoir rejection",
            neutrality_rule="e_curv contributes to M_ext or boundary mass as free reservoir",
            role="forbidden mass repair branch",
            allowed_if="never under current status",
            forbidden_if="accepted as curvature energy role",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves curvature-energy fence",
        ),
        CurvatureNeutralityEntry(
            name="CN14: J_curv boundary repair rejection",
            neutrality_rule="J_curv chosen to cancel boundary leakage, singularity, or mass shift",
            role="forbidden repair-current branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as neutrality",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents painted current safety",
        ),
        CurvatureNeutralityEntry(
            name="CN15: singularity avoidance by boundary counterterm rejection",
            neutrality_rule="finite admissibility restored by boundary counterterm/cutoff",
            role="forbidden boundary patch",
            allowed_if="never as anti-singularity mechanism",
            forbidden_if="accepted as finite admissibility",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents boundary hiding",
        ),
        CurvatureNeutralityEntry(
            name="CN16: zeta/volume coupling guard",
            neutrality_rule="curvature-volume coupling cannot reopen B_s/F_zeta, residual trace, or O",
            role="Group 16 preservation guard",
            allowed_if="count-once and no-overlap issues remain closed",
            forbidden_if="zeta becomes hidden scalar charge or metric trace",
            status="RISK",
            missing="zeta coupling/no-overlap theorem",
            consequence="keeps curvature branch from undoing metric-insertion controls",
        ),
        CurvatureNeutralityEntry(
            name="CN17: H_curv deferred",
            neutrality_rule="H_curv is not introduced to enforce neutrality in Group 17",
            role="parent correction deferral",
            allowed_if="H_curv waits for divergence-safe audit",
            forbidden_if="H_curv is used as boundary/mass repair tensor",
            status="DEFER",
            missing="H_curv audit",
            consequence="prevents premature parent correction",
        ),
        CurvatureNeutralityEntry(
            name="CN18: anti-singularity claim guard",
            neutrality_rule="boundary/mass neutral admissibility does not by itself prove bounce or regular core",
            role="overclaim guard",
            allowed_if="claim remains diagnostic/branch-filter until dynamics/solutions exist",
            forbidden_if="neutrality is advertised as dynamical avoidance",
            status="REQUIRED",
            missing="claim audit",
            consequence="keeps anti-singularity claims honest",
        ),
        CurvatureNeutralityEntry(
            name="CN19: neutrality failure",
            neutrality_rule="curvature admissibility/J_curv shifts M_ext, repairs boundary, leaks scalar charge, or reroutes matter",
            role="branch failure condition",
            allowed_if="used to reject unsafe curvature object/current",
            forbidden_if="patched with boundary repair or hidden source",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="curvature admissibility must remain diagnostic-only or be rejected",
        ),
        CurvatureNeutralityEntry(
            name="CN20: recommended next move",
            neutrality_rule="after boundary/mass neutrality audit, test anti-singularity claim level",
            role="next local bottleneck",
            allowed_if="neutrality remains theorem target or candidate",
            forbidden_if="jumping to H_curv before claim audit",
            status="RECOMMENDED",
            missing="anti-singularity claim audit",
            consequence="next script should be candidate_curvature_anti_singularity_claim_audit.py",
        ),
    ]


def print_entry(e: CurvatureNeutralityEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Neutrality rule: {e.neutrality_rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Curvature boundary and mass neutrality problem")

    print("Question:")
    print()
    print("  Does curvature admissibility or J_curv alter exterior mass,")
    print("  create boundary repair behavior,")
    print("  or leak an ordinary-sector scalar charge?")
    print()
    print("Goal:")
    print()
    print("  protect ordinary exterior sector before anti-singularity claim audit")
    print()
    print("Discipline:")
    print()
    print("  no M_ext shift")
    print("  no boundary repair current")
    print("  no exterior scalar charge")
    print("  no far-zone hidden flux")
    print("  no hidden matter coupling")
    print("  no recovery-tuned smoothing")
    print("  no boundary counterterm singularity avoidance")
    print("  no H_curv yet")

    status_line("curvature boundary/mass neutrality problem posed", "REQUIRED")


def case_1_inventory(entries: List[CurvatureNeutralityEntry]):
    header("Case 1: Curvature boundary and mass neutrality inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[CurvatureNeutralityEntry]):
    header("Case 2: Compact curvature neutrality ledger")

    print("| Entry | Neutrality rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.neutrality_rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact curvature neutrality ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[CurvatureNeutralityEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Boundary/mass neutrality is required but not derived.")
    print("  Interior-only diagnostic admissibility is the safest fallback.")
    print("  Compact support, smooth transition, and exterior-neutral J_curv are candidates only if support/orientation laws become real.")
    print("  e_curv mass reservoir, J_curv boundary repair, and boundary counterterm avoidance are rejected.")
    print("  H_curv remains deferred.")
    print("  Next gate is anti-singularity claim level.")

    status_line("curvature boundary/mass neutrality status count produced", "STRUCTURAL")


def case_4_neutrality_routes():
    header("Case 4: Neutrality routes")

    print("Possible safe routes:")
    print()
    print("1. interior-only admissibility diagnostic")
    print("2. compact curvature support")
    print("3. boundary flux diagnostic only")
    print("4. smooth finite-admissible transition")
    print("5. J_curv exterior-neutral candidate")
    print()
    print("Rejected routes:")
    print()
    print("1. e_curv mass reservoir")
    print("2. J_curv boundary repair")
    print("3. boundary counterterm singularity avoidance")
    print("4. recovery-tuned smoothing")
    print("5. hidden ordinary matter rerouting")

    status_line("curvature neutrality routes listed", "RECOMMENDED")


def case_4b_sample_boundary_neutrality(ns):
    header("Case 4b: Sample compact-support neutrality profile")

    r, R, alpha = sp.symbols("r R alpha", positive=True)
    profile = alpha * (1 - (r / R) ** 2) ** 2
    boundary_value = sp.simplify(profile.subs(r, R))
    boundary_flux = sp.simplify(sp.diff(profile, r).subs(r, R))

    print(f"Sample interior curvature profile = {profile}")
    print(f"profile(R) = {boundary_value}")
    print(f"profile'(R) = {boundary_flux}")

    if boundary_value == 0 and boundary_flux == 0:
        status_line(
            "sample compact-support neutrality profile",
            "DERIVED_REDUCED",
            f"profile(R) = {boundary_value}, profile'(R) = {boundary_flux}",
        )
    else:
        status_line("sample compact-support neutrality profile", "RISK", "boundary sample leaves shell/leakage risk")

    ns.record_derivation(
        derivation_id="curvature_boundary_sample_compact_support",
        inputs=[profile],
        output=sp.Tuple(boundary_value, boundary_flux),
        method="symbolic compact-support neutrality sample",
        status=Status.DERIVED,
    )


def case_5_decision_tree():
    header("Case 5: Boundary/mass neutrality decision tree")

    print("Decision tree:")
    print()
    print("1. Interior diagnostic only:")
    print("   safest if no exterior mass/charge/flux effect.")
    print()
    print("2. Compact support:")
    print("   candidate only if support is derived.")
    print()
    print("3. Smooth transition:")
    print("   candidate only if not recovery-tuned and no shell source.")
    print()
    print("4. J_curv exterior-neutral:")
    print("   candidate only if J_curv has real direction/support law.")
    print()
    print("5. Boundary flux diagnostic:")
    print("   allowed only as diagnostic, not physical repair.")
    print()
    print("6. Any M_ext shift, scalar leakage, matter rerouting, or boundary repair:")
    print("   branch killed.")

    status_line("curvature boundary/mass neutrality decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  curvature admissibility/J_curv cannot be made exterior-neutral.")
    print()
    print("Consequence:")
    print()
    print("  keep curvature admissibility diagnostic-only or reject the unsafe current/object.")
    print("  do not patch with boundary counterterms, e_curv reservoirs, or H_curv.")
    print()
    print("Bad failure:")
    print()
    print("  call a boundary repair current 'neutrality' and proceed to anti-singularity claims.")

    status_line("curvature neutrality good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Curvature boundary/mass neutrality fails if:")
    print()
    print("1. M_ext shifts independently of A")
    print("2. boundary repair current appears")
    print("3. exterior scalar charge appears")
    print("4. hidden far-zone curvature/scalar flux appears")
    print("5. ordinary matter coupling is rerouted")
    print("6. recovery-tuned smoothing is used")
    print("7. singularity avoidance uses boundary counterterm")
    print("8. e_curv becomes mass reservoir")
    print("9. zeta/volume coupling reopens Group 16")
    print("10. H_curv is introduced as repair")
    print("11. neutrality is used to claim bounce/regular core")

    status_line("curvature boundary/mass neutrality failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_curvature_boundary_and_mass_neutrality.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_curvature_anti_singularity_claim_audit.py")
    print("   Audit what anti-singularity claim, if any, is currently licensed.")
    print()
    print("3. candidate_curvature_neutrality_failure_summary.py")
    print("   Use if boundary/mass neutrality fails.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_curvature_anti_singularity_claim_audit.py")
    print()
    print("Reason:")
    print("  After fencing object, condition, energy, current, balance, and neutrality,")
    print("  the next risk is overclaim: bounce, regular core, or dynamical avoidance.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Curvature boundary/mass neutrality is required but not derived.")
    print()
    print("Safest fallback:")
    print()
    print("  curvature admissibility remains interior diagnostic / branch-filter only.")
    print()
    print("Candidate safe routes:")
    print()
    print("  compact support")
    print("  smooth transition")
    print("  exterior-neutral J_curv")
    print("  boundary diagnostic only")
    print()
    print("Rejected:")
    print()
    print("  e_curv mass reservoir")
    print("  J_curv boundary repair")
    print("  boundary counterterm singularity avoidance")
    print("  recovery-tuned smoothing")
    print()
    print("Best next script:")
    print()
    print("  candidate_curvature_anti_singularity_claim_audit.py")

    status_line("curvature boundary/mass neutrality audit complete", "CLOSED")


def main():
    header("Candidate Curvature Boundary And Mass Neutrality")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_neutrality_routes()
    case_4b_sample_boundary_neutrality(ns)
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    ns.record_derivation(
        derivation_id="curvature_boundary_and_mass_neutrality_marker",
        inputs=[],
        output=sp.Symbol("curvature_boundary_and_mass_neutrality_complete"),
        method="curvature_boundary_and_mass_neutrality",
        status=Status.DERIVED,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
