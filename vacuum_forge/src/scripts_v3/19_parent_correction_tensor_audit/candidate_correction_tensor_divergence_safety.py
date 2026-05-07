# Candidate correction tensor divergence safety
#
# Group:
#   19_parent_correction_tensor_audit
#
# Purpose
# -------
# The H_curv and H_exch definition requirements audits found:
#
#   H_curv is not defined yet.
#   H_exch is not defined yet.
#
# H_curv survives only as theorem target / diagnostic-only fallback.
# H_exch survives only as theorem target / diagnostic-only fallback.
#
# Both require divergence behavior before they can be inserted into a parent equation.
#
# This script audits what "divergence-safe" means without becoming decorative.
#
# Locked-door question:
#
#   What does divergence-safe mean without being decorative?
#
# This is a divergence-safety audit, not a divergence proof.


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
class DivergenceSafetyEntry:
    name: str
    criterion: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[DivergenceSafetyEntry]:
    return [
        DivergenceSafetyEntry(
            name="DSF1: divergence-safety target",
            criterion="a correction tensor is divergence-safe only through real identity, real source-balance partner, defined projection, or diagnostic-only status",
            role="core divergence-safety theorem target",
            allowed_if="divergence behavior is specified before field-equation insertion",
            forbidden_if="divergence safety is declared to make parent equation close",
            status="THEOREM_TARGET",
            missing="actual divergence identity / source partner / projection theorem",
            consequence="decides whether correction tensors can become parent-equation terms",
        ),
        DivergenceSafetyEntry(
            name="DSF2: identically divergence-free tensor",
            criterion="nabla_mu H^{mu nu} = 0 by constructed mathematical identity",
            role="strong candidate tensor class",
            allowed_if="identity is real, local/covariant enough, and not repair",
            forbidden_if="identity is asserted by analogy or Bianchi-like language",
            status="CANDIDATE",
            missing="actual identity and tensor definition",
            consequence="cleanest insertable class if source separation and boundary neutrality also hold",
        ),
        DivergenceSafetyEntry(
            name="DSF3: constraint-compatible tensor",
            criterion="divergence behavior preserves independently defined constraint propagation",
            role="candidate consistency tensor class",
            allowed_if="constraint propagation equation is real and not recovery-tuned",
            forbidden_if="constraint preservation is asserted without propagation identity",
            status="CANDIDATE",
            missing="constraint propagation theorem",
            consequence="possible route to parent compatibility if constraints are explicit",
        ),
        DivergenceSafetyEntry(
            name="DSF4: source-balanced divergence tensor",
            criterion="nabla_mu H^{mu nu} balances an independently defined source/exchange term",
            role="candidate source-balance class",
            allowed_if="source side is defined before H and not by H",
            forbidden_if="H and source define each other decoratively",
            status="CANDIDATE",
            missing="independent source partner",
            consequence="possible route if source-side accounting is already real",
        ),
        DivergenceSafetyEntry(
            name="DSF5: projected tensor",
            criterion="divergence safety holds within a defined projector subspace",
            role="candidate projected class",
            allowed_if="projector, target sector, and projected divergence are defined",
            forbidden_if="projection is invented to hide overlap or leakage",
            status="CANDIDATE",
            missing="projector and projected-divergence theorem",
            consequence="possible route to no-overlap if projector is real",
        ),
        DivergenceSafetyEntry(
            name="DSF6: diagnostic tensor",
            criterion="H-like object is diagnostic-only and not inserted into field equation",
            role="safe fallback",
            allowed_if="explicitly never contributes to parent equation",
            forbidden_if="diagnostic object later becomes correction tensor term",
            status="SAFE_IF",
            missing="none if kept diagnostic",
            consequence="allows auditing without divergence-safety burden",
        ),
        DivergenceSafetyEntry(
            name="DSF7: boundary-supported tensor",
            criterion="H has boundary/interface support with controlled divergence",
            role="high-risk boundary class",
            allowed_if="support is structural, boundary-neutral, and does not shift M_ext or scalar charge",
            forbidden_if="boundary support repairs leakage, shell source, or scalar tail",
            status="RISK",
            missing="boundary support and neutrality theorem",
            consequence="dangerous because boundary repair is recurring failure mode",
        ),
        DivergenceSafetyEntry(
            name="DSF8: compact-support zero-flux tensor",
            criterion="H has compact support with structural zero exterior flux",
            role="candidate boundary-safe subcase",
            allowed_if="compact support and zero-flux follow from tensor/source law",
            forbidden_if="support is chosen to hide exterior effects",
            status="CANDIDATE",
            missing="support law and exterior flux theorem",
            consequence="possible route if not solution-tailored",
        ),
        DivergenceSafetyEntry(
            name="DSF9: H_curv divergence guard",
            criterion="H_curv cannot be divergence-safe through undefined A_curv dynamics, J_curv, or e_curv reservoir",
            role="curvature divergence guard",
            allowed_if="H_curv remains diagnostic/deferred until source/divergence structure exists",
            forbidden_if="curvature correction is made safe by naming curvature balance",
            status="REQUIRED",
            missing="A_curv dynamics / J_curv / curvature source side",
            consequence="preserves H_curv requirements audit",
        ),
        DivergenceSafetyEntry(
            name="DSF10: H_exch divergence guard",
            criterion="H_exch cannot be divergence-safe through undefined J_V, J_exch, Sigma/R, or exchange continuity",
            role="exchange divergence guard",
            allowed_if="H_exch remains diagnostic/deferred until current/source/divergence structure exists",
            forbidden_if="exchange correction is made safe by writing continuity",
            status="REQUIRED",
            missing="J_V/J_exch/Sigma/R definitions",
            consequence="preserves H_exch requirements audit",
        ),
        DivergenceSafetyEntry(
            name="DSF11: ordinary matter separation",
            criterion="divergence safety does not reroute ordinary T_mu_nu or double-count matter",
            role="source separation guard",
            allowed_if="ordinary matter remains in established source routing",
            forbidden_if="divergence balance hides ordinary matter in correction side",
            status="REQUIRED",
            missing="ordinary matter separation theorem",
            consequence="protects ordinary matter coupling",
        ),
        DivergenceSafetyEntry(
            name="DSF12: M_ext neutrality",
            criterion="divergence-safe tensor does not shift M_ext independently of A-sector",
            role="mass neutrality guard",
            allowed_if="mass neutrality is structural or derived through A-sector",
            forbidden_if="divergence-safe tensor changes exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        DivergenceSafetyEntry(
            name="DSF13: scalar trace neutrality",
            criterion="divergence-safe tensor does not leak B_s/zeta/kappa scalar charge",
            role="metric scalar guard",
            allowed_if="scalar/no-overlap guardrails remain closed",
            forbidden_if="divergence safety creates hidden scalar channel",
            status="REQUIRED",
            missing="scalar trace neutrality theorem",
            consequence="preserves Group 16 guardrails",
        ),
        DivergenceSafetyEntry(
            name="DSF14: coefficient origin requirement",
            criterion="divergence-safe construction does not rely on recovery-fit coefficients",
            role="coefficient tuning guard",
            allowed_if="coefficients follow from tensor/source identity",
            forbidden_if="coefficients are tuned to make divergence vanish",
            status="REQUIRED",
            missing="coefficient origin",
            consequence="prevents tuned divergence safety",
        ),
        DivergenceSafetyEntry(
            name="DSF15: Bianchi-like language rejection",
            criterion="H is divergence-safe because it is geometric / Bianchi-compatible by phrase",
            role="forbidden divergence decoration",
            allowed_if="never as proof",
            forbidden_if="accepted as divergence safety",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents fake parent compatibility",
        ),
        DivergenceSafetyEntry(
            name="DSF16: decorative tensor rejection",
            criterion="H, source, and divergence relation are introduced together and define each other",
            role="forbidden circular closure",
            allowed_if="never as derivation",
            forbidden_if="accepted as parent correction",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents decorative correction tensor",
        ),
        DivergenceSafetyEntry(
            name="DSF17: recovery-chosen divergence rejection",
            criterion="divergence behavior chosen to pass gamma_like, AB, exterior matching, or PPN behavior",
            role="forbidden recovery construction",
            allowed_if="never as origin",
            forbidden_if="accepted as divergence condition",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps recovery downstream",
        ),
        DivergenceSafetyEntry(
            name="DSF18: leakage-canceling divergence rejection",
            criterion="divergence chosen to cancel boundary leakage, scalar tail, shell source, mass shift, or singularity",
            role="forbidden repair divergence",
            allowed_if="never as mechanism",
            forbidden_if="accepted as divergence safety",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents repair tensor",
        ),
        DivergenceSafetyEntry(
            name="DSF19: source-by-divergence rejection",
            criterion="source side is defined as whatever equals nabla_mu H^{mu nu}",
            role="forbidden source relabeling",
            allowed_if="never without independent source meaning",
            forbidden_if="accepted as source-balanced divergence",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents fake source balance",
        ),
        DivergenceSafetyEntry(
            name="DSF20: dark-patch divergence rejection",
            criterion="dark sector is invoked to absorb correction tensor divergence",
            role="forbidden dark patch",
            allowed_if="never as ordinary-sector repair",
            forbidden_if="accepted as divergence partner",
            status="REJECTED",
            missing="not pursued",
            consequence="preserves no-dark-patch rule",
        ),
        DivergenceSafetyEntry(
            name="DSF21: divergence-safety failure",
            criterion="no real identity, source partner, projection theorem, or diagnostic-only status exists",
            role="branch failure condition",
            allowed_if="used to keep correction tensors deferred",
            forbidden_if="patched by Bianchi smoke or source relabeling",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="correction tensors cannot be inserted",
        ),
        DivergenceSafetyEntry(
            name="DSF22: recommended next move",
            criterion="after divergence-safety audit, audit source separation",
            role="next local bottleneck",
            allowed_if="divergence safety remains theorem-targeted",
            forbidden_if="jumping to insertability before source separation",
            status="RECOMMENDED",
            missing="source-separation audit",
            consequence="next script should be candidate_correction_tensor_source_separation.py",
        ),
    ]


def print_entry(e: DivergenceSafetyEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Criterion: {e.criterion}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Correction tensor divergence-safety problem")

    print("Question:")
    print()
    print("  What does divergence-safe mean without being decorative?")
    print()
    print("Goal:")
    print()
    print("  distinguish real divergence safety from Bianchi smoke, repair, and source relabeling")
    print()
    print("Discipline:")
    print()
    print("  no Bianchi-like language as proof")
    print("  no source and tensor defining each other")
    print("  no recovery-chosen divergence")
    print("  no leakage-canceling divergence")
    print("  no ordinary matter rerouting")
    print("  no M_ext shift")
    print("  no scalar trace leak")
    print("  no dark-sector patch")
    print("  diagnostic-only remains allowed if not inserted")

    status_line("correction tensor divergence-safety problem posed", "REQUIRED")


def case_1_inventory(entries: List[DivergenceSafetyEntry]):
    header("Case 1: Correction tensor divergence-safety inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[DivergenceSafetyEntry]):
    header("Case 2: Compact divergence-safety ledger")

    print("| Entry | Criterion | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.criterion.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact divergence-safety ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[DivergenceSafetyEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Divergence-safe does not mean named geometric or Bianchi-flavored.")
    print("  The safest routes are: diagnostic-only, constructed identity, independently defined source-balance partner, or defined projection/constraint propagation.")
    print("  Boundary-supported tensors remain risky.")
    print("  H_curv and H_exch cannot be divergence-safe through their currently undefined source/current objects.")
    print("  Ordinary matter separation, M_ext neutrality, scalar trace neutrality, and coefficient origin remain required.")
    print("  Bianchi-like language, decorative tensor closure, recovery-chosen divergence, leakage-canceling divergence, source relabeling, and dark-patch divergence are rejected.")
    print("  Next gate is source separation.")

    status_line("correction tensor divergence-safety status count produced", "STRUCTURAL")


def case_4_divergence_classes():
    header("Case 4: Divergence-safety classes")

    print("Candidate divergence-safety classes:")
    print()
    print("1. identically divergence-free tensor")
    print("2. constraint-compatible tensor")
    print("3. source-balanced divergence tensor")
    print("4. projected tensor")
    print("5. diagnostic-only tensor")
    print("6. compact-support zero-flux tensor")
    print()
    print("High risk:")
    print()
    print("1. boundary-supported tensor")
    print()
    print("Rejected:")
    print()
    print("1. Bianchi-like language")
    print("2. decorative tensor closure")
    print("3. recovery-chosen divergence")
    print("4. leakage-canceling divergence")
    print("5. source-by-divergence")
    print("6. dark-patch divergence")

    status_line("divergence-safety classes listed", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: Divergence-safety decision tree")

    print("Decision tree:")
    print()
    print("1. H has constructed divergence-free identity:")
    print("   candidate survives if source separation and boundary neutrality also hold.")
    print()
    print("2. H has independently defined source partner:")
    print("   source-balanced candidate survives if source is not defined by H.")
    print()
    print("3. H has defined projection/constraint propagation:")
    print("   candidate survives if projection does not hide overlap.")
    print()
    print("4. H is diagnostic-only:")
    print("   safe if never inserted into field equation.")
    print()
    print("5. H uses Bianchi-like phrase, recovery target, leakage cancellation, or source relabeling:")
    print("   rejected.")
    print()
    print("6. No route exists:")
    print("   keep correction tensors deferred.")

    status_line("divergence-safety decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  correction tensor divergence safety cannot be established")
    print("  because no identity, source partner, projection theorem, or diagnostic-only status is available.")
    print()
    print("Consequence:")
    print()
    print("  keep H_curv/H_exch deferred.")
    print("  do not insert correction tensors into parent equation.")
    print()
    print("Bad failure:")
    print()
    print("  call a tensor divergence-safe because the parent equation needs it to be.")

    status_line("divergence-safety good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Divergence safety fails if:")
    print()
    print("1. Bianchi-like language is used as proof")
    print("2. H and source define each other")
    print("3. divergence is chosen by recovery behavior")
    print("4. divergence cancels leakage/singularity/boundary/mass failure")
    print("5. source is defined as divergence of H")
    print("6. dark sector absorbs ordinary divergence failure")
    print("7. ordinary matter is rerouted")
    print("8. M_ext shifts")
    print("9. scalar trace leaks")
    print("10. coefficients are tuned to make divergence vanish")
    print("11. boundary-supported tensor repairs boundary")
    print("12. diagnostic-only tensor is inserted into field equation")

    status_line("divergence-safety failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_correction_tensor_divergence_safety.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_correction_tensor_source_separation.py")
    print("   Audit whether correction tensors avoid double-counting ordinary matter and vacuum sources.")
    print()
    print("3. candidate_divergence_safety_failure_summary.py")
    print("   Use if all divergence-safety routes collapse into decoration.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_correction_tensor_source_separation.py")
    print()
    print("Reason:")
    print("  Divergence safety requires more than an identity or balance form.")
    print("  The next shared bottleneck is whether the correction tensor double-counts source sectors.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Divergence-safe requires one of:")
    print()
    print("  constructed identity")
    print("  independently defined source-balance partner")
    print("  defined projection / constraint propagation")
    print("  diagnostic-only status")
    print()
    print("Rejected:")
    print()
    print("  Bianchi-like language")
    print("  decorative tensor closure")
    print("  recovery-chosen divergence")
    print("  leakage-canceling divergence")
    print("  source-by-divergence")
    print("  dark-patch divergence")
    print()
    print("H_curv and H_exch cannot yet pass divergence safety through their missing current/source objects.")
    print()
    print("Best next script:")
    print()
    print("  candidate_correction_tensor_source_separation.py")

    status_line("correction tensor divergence-safety audit complete", "CLOSED")


def main():
    header("Candidate Correction Tensor Divergence Safety")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_divergence_classes()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
