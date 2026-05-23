# Group:
#   13_vacuum_substance_accounting
#
# Script type:
#   AUDIT

# Candidate epsilon-kappa double-counting check
#
# Purpose
# -------
# The epsilon_vac_config functional audit proposed:
#
#   epsilon_vac_config =
#     1/2 K_zeta (zeta-zeta_min)^2
#     + 1/2 L_zeta |grad zeta|^2
#     + 1/2 K_lock (kappa-(zeta-zeta_min))^2
#
# Existing kappa relaxation accounting also uses:
#
#   e_kappa = 1/2 K_kappa (kappa-kappa_min)^2
#
# Potential problem:
#
#   If epsilon_vac_config contains kappa mismatch energy,
#   and e_kappa is also counted separately,
#   the same trace/volume imbalance may be counted twice.
#
# This script audits whether e_kappa should be inside or outside
# epsilon_vac_config.
#
# It is not a derivation.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    EvidenceRecord,
    EvidenceType,
    GovernanceStatus,
    HandoffImportRecord,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
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
class DoubleCountingEntry:
    name: str
    option: str
    accounting_rule: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str


def build_entries() -> List[DoubleCountingEntry]:
    return [
        DoubleCountingEntry(
            name="D1: e_kappa outside epsilon_vac_config",
            option="epsilon_vac_config contains zeta geometry; e_kappa is separate sector relaxation energy",
            accounting_rule="E_total includes epsilon_vac_config + e_kappa once each",
            allowed_if="kappa is an independent relaxation diagnostic not already included in epsilon",
            forbidden_if="epsilon includes K_lock or kappa mismatch representing same energy",
            status="SAFE_IF",
            missing="whether kappa is independent or just zeta mismatch",
        ),
        DoubleCountingEntry(
            name="D2: e_kappa inside epsilon_vac_config",
            option="epsilon_vac_config includes kappa mismatch energy",
            accounting_rule="E_total includes epsilon_vac_config only; do not add e_kappa separately",
            allowed_if="kappa mismatch is part of vacuum configuration energy",
            forbidden_if="e_kappa is also counted as separate energy",
            status="SAFE_IF",
            missing="how Gamma_relax is written when e_kappa is internal",
        ),
        DoubleCountingEntry(
            name="D3: kappa-zeta locking as constraint, not energy",
            option="K_lock -> constraint enforcing kappa = zeta-zeta_min",
            accounting_rule="locking term not counted as physical energy if it is a Lagrange constraint",
            allowed_if="parent/projector defines kappa as diagnostic projection of zeta",
            forbidden_if="finite K_lock counted while also enforcing equality exactly",
            status="CANDIDATE",
            missing="constraint versus penalty interpretation",
        ),
        DoubleCountingEntry(
            name="D4: kappa-zeta locking as penalty energy",
            option="finite K_lock penalty energy included in epsilon_vac_config",
            accounting_rule="locking energy counted inside epsilon; no duplicate e_kappa for same mismatch",
            allowed_if="kappa and zeta can differ physically",
            forbidden_if="creates extra scalar degree of freedom",
            status="RISK",
            missing="degree-of-freedom count and projector identity",
        ),
        DoubleCountingEntry(
            name="D5: Gamma_relax with external e_kappa",
            option="Gamma_relax transfers from e_kappa to epsilon_vac_config",
            accounting_rule="d e_kappa/dtau + d epsilon_vac_config/dtau = 0",
            allowed_if="e_kappa is outside epsilon_vac_config",
            forbidden_if="epsilon already contains e_kappa",
            status="CANDIDATE",
            missing="sign convention and source of relaxation rate",
        ),
        DoubleCountingEntry(
            name="D6: Gamma_relax with internal e_kappa",
            option="Gamma_relax is internal redistribution within epsilon_vac_config",
            accounting_rule="d epsilon_vac_config/dtau accounts for kappa relaxation internally",
            allowed_if="e_kappa included in epsilon_vac_config",
            forbidden_if="additional transfer equation adds same change again",
            status="CANDIDATE",
            missing="internal bookkeeping decomposition",
        ),
        DoubleCountingEntry(
            name="D7: forbidden duplicate total energy",
            option="E_total = epsilon_vac_config + e_kappa when epsilon already includes kappa mismatch",
            accounting_rule="do not do this",
            allowed_if="never",
            forbidden_if="same trace/volume mismatch counted twice",
            status="FORBIDDEN",
            missing="not pursued",
        ),
        DoubleCountingEntry(
            name="D8: forbidden duplicate source response",
            option="rho or trace response creates A mass, zeta charge, and kappa charge independently",
            accounting_rule="source response must be routed once by projectors",
            allowed_if="never unless parent identity forces distinct channels",
            forbidden_if="scalar mass/volume response double-counted",
            status="FORBIDDEN",
            missing="P_recombination and source projector identity",
        ),
        DoubleCountingEntry(
            name="D9: recommended provisional convention",
            option="treat e_kappa outside epsilon_vac_config for now; keep epsilon purely zeta-volume until kappa-zeta map is derived",
            accounting_rule="epsilon_vac_config = zeta displacement + gradient/interface terms; e_kappa separate; no K_lock energy counted yet",
            allowed_if="we label K_lock as diagnostic/constraint target, not physical energy",
            forbidden_if="we need kappa-zeta locking energy to enforce consistency",
            status="RECOMMENDED",
            missing="later revisit after kappa-zeta map",
        ),
        DoubleCountingEntry(
            name="D10: later unified convention",
            option="after kappa-zeta map, absorb e_kappa into epsilon_vac_config or eliminate kappa as independent energy",
            accounting_rule="single trace/volume energy functional",
            allowed_if="parent projector shows kappa is not independent",
            forbidden_if="done before derivation",
            status="STRUCTURAL",
            missing="parent projector / recombination derivation",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="epsilon_vac_config_functional_marker",
        upstream_script_id="13_vacuum_substance_accounting__candidate_epsilon_vac_config_functional",
        upstream_derivation_id="epsilon_vac_config_functional_marker",
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


def print_entry(e: DoubleCountingEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Option: {e.option}")
    print(f"Accounting rule: {e.accounting_rule}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: epsilon-kappa double-counting problem")

    print("Question:")
    print()
    print("  Should e_kappa be inside or outside epsilon_vac_config?")
    print()
    print("Goal:")
    print()
    print("  prevent the same trace/volume mismatch from being counted twice")
    print()
    print("Discipline:")
    print()
    print("  count scalar/trace energy once")
    print("  do not count K_lock twice")
    print("  do not duplicate source response")
    print("  do not treat constraint penalties as physical energy unless derived")
    print("  keep provisional conventions explicit")

    with out.unresolved_obligations():
        out.line("epsilon-kappa double-counting problem posed", StatusMark.OBLIGATION, "open: kappa-zeta map required before final convention")


def case_1_inventory(entries: List[DoubleCountingEntry]):
    header("Case 1: Double-counting inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[DoubleCountingEntry], out: ScriptOutput):
    header("Case 2: Compact double-counting ledger")

    print("| Entry | Option | Status | Accounting rule | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.option.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.accounting_rule.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact double-counting ledger produced", StatusMark.PASS, "ledger complete")


def case_3_status_counts(entries: List[DoubleCountingEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Both inside and outside conventions are possible.")
    print("  The safest provisional convention is to keep e_kappa outside epsilon_vac_config.")
    print("  K_lock should remain diagnostic/constraint-like until the kappa-zeta map is derived.")

    with out.governance_assessments():
        out.line("double-counting status count produced", StatusMark.PASS, "counts complete")


def case_4_recommended_convention(out: ScriptOutput):
    header("Case 4: Recommended provisional convention")

    print("Recommended for now:")
    print()
    print("  epsilon_vac_config contains:")
    print("    1/2 K_zeta (zeta-zeta_min)^2")
    print("    1/2 L_zeta |grad zeta|^2")
    print()
    print("  e_kappa remains separate:")
    print("    e_kappa = 1/2 K_kappa (kappa-kappa_min)^2")
    print()
    print("  K_lock is not counted as physical energy yet.")
    print("  Treat K_lock as a diagnostic/constraint target.")
    print()
    print("Reason:")
    print("  the kappa-zeta map is not derived, so combining them risks double-counting.")

    with out.governance_assessments():
        out.line("recommended provisional convention stated", StatusMark.PASS, "provisional convention explicit: e_kappa outside epsilon")


def case_5_forbidden_patterns(out: ScriptOutput):
    header("Case 5: Forbidden patterns")

    print("Forbidden:")
    print()
    print("1. epsilon includes kappa mismatch and E_total also adds e_kappa.")
    print("2. K_lock enforces equality exactly and is also counted as finite energy.")
    print("3. rho contributes to A mass, zeta exterior charge, and kappa exterior charge.")
    print("4. Gamma_relax transfers energy between two terms that are already the same term.")
    print("5. Recombination counts zeta and kappa as independent scalar gravity sectors.")

    with out.governance_assessments():
        out.line("forbidden double-counting patterns stated", StatusMark.PASS, "five forbidden patterns identified")


def case_6_updated_functional(out: ScriptOutput):
    header("Case 6: Updated provisional functional")

    print("Provisional epsilon_vac_config:")
    print()
    print("  epsilon_vac_config =")
    print("    1/2 K_zeta (zeta-zeta_min)^2")
    print("    + 1/2 L_zeta |grad zeta|^2")
    print()
    print("Separate kappa relaxation energy:")
    print()
    print("  e_kappa = 1/2 K_kappa (kappa-kappa_min)^2")
    print()
    print("Provisional exchange accounting:")
    print()
    print("  d e_kappa/dtau + d epsilon_vac_config/dtau = 0")
    print()
    print("Constraint target:")
    print()
    print("  kappa ~ zeta - zeta_min")
    print()
    print("but no K_lock energy counted until derived.")

    with out.governance_assessments():
        out.line("updated provisional functional stated", StatusMark.DEFER, "candidate route: provisional convention")


def case_6b_symbolic_accounting_split(ns, out: ScriptOutput) -> None:
    header("Case 6b: Symbolic provisional accounting split")

    K_zeta, L_zeta, K_kappa = sp.symbols("K_zeta L_zeta K_kappa")
    zeta, zeta_min, kappa, kappa_min, grad_zeta_sq = sp.symbols(
        "zeta zeta_min kappa kappa_min grad_zeta_sq"
    )
    epsilon = sp.simplify(
        sp.Rational(1, 2) * K_zeta * (zeta - zeta_min) ** 2
        + sp.Rational(1, 2) * L_zeta * grad_zeta_sq
    )
    e_kappa = sp.simplify(sp.Rational(1, 2) * K_kappa * (kappa - kappa_min) ** 2)
    total = sp.simplify(epsilon + e_kappa)

    print("Provisional symbolic split:")
    print()
    print(f"  epsilon_vac_config = {epsilon}")
    print(f"  e_kappa = {e_kappa}")
    print(f"  E_total = {total}")
    print()
    print("Interpretation:")
    print("  the provisional convention counts zeta-geometry and kappa-relaxation once each, separately.")

    with out.sample_results():
        out.line("symbolic provisional energy split", StatusMark.PASS, "epsilon and e_kappa kept separate")

    ns.record_derivation(
        derivation_id="epsilon_kappa_provisional_split",
        inputs=[zeta, zeta_min, kappa, kappa_min, grad_zeta_sq],
        output=sp.Tuple(epsilon, e_kappa, total),
        method="symbolic provisional epsilon/e_kappa split",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="provisional accounting convention; not derived from parent identity",
    )


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_epsilon_kappa_double_counting_check.md")
    print("   Artifact for this script.")
    print()
    print("2. vacuum_substance_accounting_summary.md")
    print("   Summarize group 13 after resolving provisional accounting.")
    print()
    print("3. candidate_kappa_zeta_map.py")
    print("   Directly test whether kappa equals/proxies zeta-zeta_min.")
    print()
    print("Recommended next:")
    print()
    print("  vacuum_substance_accounting_summary.md")
    print()
    print("Reason:")
    print("  Group 13 has reached a natural summary point with a provisional accounting convention.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.PASS, "vacuum_substance_accounting_summary.md")


def final_interpretation():
    header("Final interpretation")

    print("To avoid double-counting:")
    print()
    print("  keep e_kappa outside epsilon_vac_config for now")
    print("  keep epsilon_vac_config as zeta displacement plus gradient/interface terms")
    print("  treat K_lock as diagnostic/constraint target, not physical energy")
    print("  revisit after the kappa-zeta map is derived")
    print()
    print("Possible next artifact:")
    print("  candidate_epsilon_kappa_double_counting_check.md")
    print()
    print("Recommended next:")
    print("  vacuum_substance_accounting_summary.md")


def main():
    header("Candidate Epsilon Kappa Double Counting Check")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()

    case_0_problem_statement(out)
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_recommended_convention(out)
    case_5_forbidden_patterns(out)
    case_6_updated_functional(out)
    case_6b_symbolic_accounting_split(ns, out)
    case_7_next_tests(out)
    final_interpretation()

    ns.record_claim(ClaimRecord(
        claim_id="e_kappa_outside_epsilon_vac_config_provisional",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "Provisional convention: e_kappa is kept outside epsilon_vac_config until the kappa-zeta map is derived. "
            "epsilon_vac_config = 1/2 K_zeta (zeta-zeta_min)^2 + 1/2 L_zeta |grad zeta|^2. "
            "K_lock is treated as a diagnostic/constraint target, not physical energy. "
            "This convention must be revisited after the kappa-zeta map is derived."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="epsilon_kappa_double_counting_forbidden",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "E_total = epsilon_vac_config + e_kappa is forbidden when epsilon_vac_config already contains "
            "the kappa mismatch energy (D7). The same trace/volume imbalance must not be counted twice. "
            "Source response must be routed once by projectors (D8)."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_zeta_map_for_unified_convention",
        script_id=SCRIPT_ID,
        title="Derive kappa-zeta map to unify e_kappa and epsilon_vac_config",
        status=ObligationStatus.OPEN,
        description=(
            "After the kappa-zeta map is derived, determine whether e_kappa should be absorbed into "
            "epsilon_vac_config or remain separate. Until then, maintain provisional convention D9."
        ),
    ))
    # D7 is the concrete double-counting witness: counting epsilon (which includes kappa mismatch)
    # and e_kappa separately when they represent the same energy is the exact OVERLAP_WITNESS.
    ns.record_evidence(EvidenceRecord(
        evidence_id="epsilon_kappa_double_counting_overlap_witness",
        script_id=SCRIPT_ID,
        evidence_type=EvidenceType.OVERLAP_WITNESS,
        challenges=["epsilon_kappa_double_counting_forbidden"],
        description=(
            "Entry D7 identifies the concrete double-counting witness: "
            "E_total = epsilon_vac_config + e_kappa when epsilon already contains the K_lock kappa-mismatch "
            "term counts the same trace/volume imbalance twice. "
            "This is a real overlap witness that the governance rule epsilon_kappa_double_counting_forbidden "
            "is designed to prevent. The provisional convention D9 is adopted to avoid this overlap."
        ),
    ))
    # HandoffImportRecord: as the last script in group 13, declare the group 13 outputs
    # available for downstream groups.
    ns.record_handoff_import(HandoffImportRecord(
        handoff_id="group_13_vacuum_substance_accounting_handoff",
        script_id=SCRIPT_ID,
        imported_as=RecordKind.SUMMARY_CLAIM,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        imported_record_refs=[
            "claim:epsilon_kappa_double_counting_forbidden",
            "claim:epsilon_kappa_hybrid_provisional_convention",
            "evidence:epsilon_kappa_double_counting_overlap_witness",
            "obligation:derive_kappa_zeta_map_for_unified_convention",
            "derivation:epsilon_kappa_double_counting_check_marker",
        ],
        description=(
            "Group 13 outputs: "
            "(1) zeta=ln sqrt(gamma) as leading geometric vacuum-configuration candidate; "
            "(2) trace/TT geometric split with delta zeta|TT=0 at linear order; "
            "(3) scalar conversion-not-damping policy; "
            "(4) binary-radiation safety filter (TT-only, no Box zeta/kappa); "
            "(5) boundary no-exterior-charge theorem target (Q_volume=0, F_zeta(R+)=0); "
            "(6) J_v class constraints (absent, compact, constrained, or causal); "
            "(7) parent balance skeleton u^mu nabla_mu epsilon + nabla_mu J_v = Sigma_exchange - Gamma_relax; "
            "(8) minimal epsilon_vac_config scaffold (zeta displacement + gradient terms); "
            "(9) provisional double-counting convention: e_kappa outside epsilon_vac_config."
        ),
    ))
    ns.record_derivation(
        derivation_id="epsilon_kappa_double_counting_check_marker",
        inputs=[],
        output=sp.Symbol("epsilon_kappa_double_counting_check_audited"),
        method="epsilon_kappa_double_counting_check_audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
