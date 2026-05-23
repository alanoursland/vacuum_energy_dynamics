# Candidate O domain codomain
#
# Group:
#   27_active_O_construction
#
# Script type:
#   OPERATOR STRUCTURE INVENTORY
#
# Purpose
# -------
# Test the admissible domain and codomain candidates for active O.
#
# Locked-door question:
#
#   What are the admissible domain and codomain of O?
#
# This script does not derive active O.
# It does not define kernel or image.
# It does not define the no-overlap criterion.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# Tiny goblin rule:
#
#   No door without a room on both sides.

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
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# =============================================================================
# Utilities
# =============================================================================


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "ADMISSIBLE_CANDIDATE": StatusMark.INFO,
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE": StatusMark.DEFER,
        "FORBIDDEN": StatusMark.FAIL,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PRESERVE": StatusMark.OBLIGATION,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "TARGET": StatusMark.DEFER,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g27_O_problem",
            "027_active_O_construction__candidate_O_problem_ledger",
            "g27_O_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g26_summary",
            "026_residual_control_theorem_attempt__candidate_group_26_status_summary",
            "g26_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g26_oblig",
            "026_residual_control_theorem_attempt__candidate_residual_control_theorem_attempt_obligations",
            "g26_obligation_status",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g26_consistency",
            "026_residual_control_theorem_attempt__candidate_residual_control_boundary_source_recovery_consistency",
            "g26_rc_consistency_marker",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, expected_record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
        )

    return archive, ns, invalidated


def ensure_archive_write_dirs(ns) -> None:
    for attr in (
        "routes_path",
        "branch_decisions_path",
        "claims_path",
        "obligations_path",
        "derivations_path",
        "governance_path",
    ):
        path_obj = getattr(ns, attr, None)
        if path_obj is not None:
            path_obj.mkdir(parents=True, exist_ok=True)


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


# =============================================================================
# Data models
# =============================================================================


@dataclass
class DomainCodomainSymbols:
    zeta_Bs: sp.Symbol
    zeta_res: sp.Symbol
    kappa_res: sp.Symbol
    eps_acc: sp.Symbol
    ekappa_acc: sp.Symbol
    boundary_data: sp.Symbol
    source_data: sp.Symbol
    support_data: sp.Symbol
    safe_trace_sector: sp.Symbol
    inert_sector: sp.Symbol
    diagnostic_sector: sp.Symbol
    projected_sector: sp.Symbol
    domain_candidate: sp.Expr
    codomain_candidate: sp.Expr
    domain_gap: sp.Symbol
    codomain_gap: sp.Symbol
    dc_gap: sp.Expr


@dataclass
class DomainCandidate:
    name: str
    sector: str
    status: str
    include_if: str
    hazard: str


@dataclass
class CodomainCandidate:
    name: str
    sector: str
    status: str
    include_if: str
    hazard: str


@dataclass
class DomainCodomainPair:
    name: str
    mapping: str
    status: str
    works_if: str
    fails_if: str


@dataclass
class RejectedDomainCodomainShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class DomainCodomainConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> DomainCodomainSymbols:
    (
        zeta_Bs,
        zeta_res,
        kappa_res,
        eps_acc,
        ekappa_acc,
        boundary_data,
        source_data,
        support_data,
        safe_trace_sector,
        inert_sector,
        diagnostic_sector,
        projected_sector,
        domain_gap,
        codomain_gap,
    ) = sp.symbols(
        "zeta_Bs zeta_res kappa_res eps_acc ekappa_acc boundary_data source_data support_data "
        "safe_trace_sector inert_sector diagnostic_sector projected_sector domain_gap codomain_gap",
        real=True,
    )

    domain_candidate = sp.Tuple(
        zeta_Bs,
        zeta_res,
        kappa_res,
        eps_acc,
        ekappa_acc,
        boundary_data,
        source_data,
        support_data,
    )

    codomain_candidate = sp.Tuple(
        safe_trace_sector,
        inert_sector,
        diagnostic_sector,
        projected_sector,
    )

    dc_gap = sp.simplify(domain_gap + codomain_gap)

    return DomainCodomainSymbols(
        zeta_Bs=zeta_Bs,
        zeta_res=zeta_res,
        kappa_res=kappa_res,
        eps_acc=eps_acc,
        ekappa_acc=ekappa_acc,
        boundary_data=boundary_data,
        source_data=source_data,
        support_data=support_data,
        safe_trace_sector=safe_trace_sector,
        inert_sector=inert_sector,
        diagnostic_sector=diagnostic_sector,
        projected_sector=projected_sector,
        domain_candidate=domain_candidate,
        codomain_candidate=codomain_candidate,
        domain_gap=domain_gap,
        codomain_gap=codomain_gap,
        dc_gap=dc_gap,
    )


def build_domain_candidates() -> List[DomainCandidate]:
    return [
        DomainCandidate(
            name="D1: safe trace input",
            sector="zeta_to_Bs / zeta_Bs",
            status="ADMISSIBLE_CANDIDATE",
            include_if="O must preserve the safe scalar trace channel",
            hazard="O changes zeta_to_Bs or duplicates it",
        ),
        DomainCandidate(
            name="D2: zeta residual input",
            sector="zeta_residual_metric",
            status="ADMISSIBLE_CANDIDATE",
            include_if="O is meant to separate dangerous zeta residual reentry",
            hazard="zeta residual erased by name rather than mapped by law",
        ),
        DomainCandidate(
            name="D3: kappa residual input",
            sector="kappa_metric",
            status="ADMISSIBLE_CANDIDATE",
            include_if="O is meant to prevent kappa from restoring residual trace/source role",
            hazard="kappa erased by diagnostic vocabulary",
        ),
        DomainCandidate(
            name="D4: epsilon/e_kappa accounting input",
            sector="epsilon_vac_metric and e_kappa_metric",
            status="CANDIDATE",
            include_if="O needs to distinguish accounting targets from geometric residuals",
            hazard="accounting variables become hidden metric/source reservoirs",
        ),
        DomainCandidate(
            name="D5: boundary/current data input",
            sector="boundary scalar-tail and current-flux data",
            status="CANDIDATE",
            include_if="O boundary/current behavior is audited",
            hazard="boundary/current failure selects O",
        ),
        DomainCandidate(
            name="D6: source-routing data input",
            sector="ordinary source / routing data",
            status="CANDIDATE",
            include_if="O must preserve source no-double-counting",
            hazard="O duplicates or repairs ordinary source load",
        ),
        DomainCandidate(
            name="D7: support/matching data input",
            sector="support radius, smoothing, transition, seam/matching data",
            status="CANDIDATE",
            include_if="O must preserve support/matching neutrality",
            hazard="support/matching data selects O or hides residuals",
        ),
    ]


def build_codomain_candidates() -> List[CodomainCandidate]:
    return [
        CodomainCandidate(
            name="C1: safe metric trace sector",
            sector="safe_trace_sector",
            status="ADMISSIBLE_CANDIDATE",
            include_if="O preserves zeta_to_Bs as ordinary scalar trace",
            hazard="residuals enter safe trace sector too",
        ),
        CodomainCandidate(
            name="C2: inert residual sector",
            sector="inert_sector",
            status="CANDIDATE",
            include_if="residuals are mapped to a derived non-reentering sector",
            hazard="inert sector exists by label only",
        ),
        CodomainCandidate(
            name="C3: diagnostic-only sector",
            sector="diagnostic_sector",
            status="CANDIDATE",
            include_if="kappa/accounting variables remain diagnostic without construction role",
            hazard="diagnostic data later becomes metric/source/boundary data",
        ),
        CodomainCandidate(
            name="C4: projected-out sector",
            sector="projected_sector / kernel-like remainder",
            status="CANDIDATE",
            include_if="O is eventually a projection or replacement map with removed components",
            hazard="projected-out means erased by name",
        ),
        CodomainCandidate(
            name="C5: parent-equation sector",
            sector="parent source/field-equation sector",
            status="REJECTED",
            include_if="never at this stage",
            hazard="O opens parent equation before residual/insertion/divergence closure",
        ),
    ]


def build_pairs() -> List[DomainCodomainPair]:
    return [
        DomainCodomainPair(
            name="P1: preserve safe trace",
            mapping="O(zeta_Bs) -> safe_trace_sector",
            status="CANDIDATE",
            works_if="O preserves zeta_to_Bs without adding residual trace",
            fails_if="O modifies zeta_to_Bs or creates a second zeta path",
        ),
        DomainCodomainPair(
            name="P2: separate zeta residual",
            mapping="O(zeta_residual_metric) -> inert/projected/diagnostic sector",
            status="UNDERDETERMINED",
            works_if="inert/projected/diagnostic codomain is structurally defined",
            fails_if="zeta residual is erased by name",
        ),
        DomainCodomainPair(
            name="P3: separate kappa residual",
            mapping="O(kappa_metric) -> inert/projected/diagnostic sector",
            status="UNDERDETERMINED",
            works_if="kappa no-reentry or diagnostic codomain is structurally defined",
            fails_if="kappa is killed by diagnostic vocabulary",
        ),
        DomainCodomainPair(
            name="P4: isolate accounting pair",
            mapping="O(epsilon_vac_metric, e_kappa_metric) -> accounting/diagnostic sector",
            status="UNDERDETERMINED",
            works_if="accounting sector has no metric/source/boundary/recovery/parent role",
            fails_if="accounting sector hides geometric residuals",
        ),
        DomainCodomainPair(
            name="P5: protect boundary/source/support data",
            mapping="O(boundary/source/support data) -> unchanged guardrail data or audited compatibility sector",
            status="UNDERDETERMINED",
            works_if="O does not select itself from guardrail failure",
            fails_if="boundary/source/support failure chooses O",
        ),
        DomainCodomainPair(
            name="P6: parent sector exclusion",
            mapping="O(anything) -> parent field-equation readiness",
            status="REJECTED",
            works_if="not allowed in this group",
            fails_if="O domain/codomain classification opens parent equation",
        ),
    ]


def build_shortcuts() -> List[RejectedDomainCodomainShortcut]:
    return [
        RejectedDomainCodomainShortcut(
            name="S1: universal domain by default",
            shortcut="O acts on every object because it is an operator",
            status="REJECTED",
            reason="domain must be defined, not assumed universal",
        ),
        RejectedDomainCodomainShortcut(
            name="S2: safe codomain by label",
            shortcut="O output is safe because it is called projected",
            status="REJECTED",
            reason="codomain must be proved non-reentering or safe",
        ),
        RejectedDomainCodomainShortcut(
            name="S3: residuals sent to inert by naming",
            shortcut="zeta/kappa residuals are mapped to inert sector by label",
            status="REJECTED",
            reason="inert sector requires no-reentry theorem",
        ),
        RejectedDomainCodomainShortcut(
            name="S4: accounting codomain as reservoir",
            shortcut="epsilon/e_kappa codomain carries hidden metric/source role",
            status="REJECTED",
            reason="accounting pair cannot repair geometry",
        ),
        RejectedDomainCodomainShortcut(
            name="S5: recovery-selected domain",
            shortcut="domain/codomain chosen because weak-field or Schwarzschild recovery works",
            status="REJECTED",
            reason="recovery may audit but not construct O",
        ),
        RejectedDomainCodomainShortcut(
            name="S6: parent codomain",
            shortcut="O codomain includes parent equation readiness",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_conclusions() -> List[DomainCodomainConclusion]:
    return [
        DomainCodomainConclusion(
            name="K1: domain candidate",
            conclusion="candidate domain ledger is available",
            status="CANDIDATE",
            meaning="zeta_Bs, zeta/kappa residuals, accounting pair, and guardrail data are possible domain sectors",
        ),
        DomainCodomainConclusion(
            name="K2: codomain candidate",
            conclusion="candidate codomain ledger is available",
            status="CANDIDATE",
            meaning="safe trace, inert, diagnostic, and projected sectors are possible codomain targets",
        ),
        DomainCodomainConclusion(
            name="K3: safe trace preservation",
            conclusion="O(zeta_Bs) -> safe trace sector is the cleanest candidate mapping",
            status="CANDIDATE",
            meaning="this protects zeta_to_Bs but does not yet define full O",
        ),
        DomainCodomainConclusion(
            name="K4: residual codomain",
            conclusion="zeta/kappa residual codomain is underdetermined",
            status="UNDERDETERMINED",
            meaning="kernel/image and no-overlap criterion are needed next",
        ),
        DomainCodomainConclusion(
            name="K5: parent codomain",
            conclusion="parent equation codomain is rejected",
            status="REJECTED",
            meaning="domain/codomain classification cannot open parent closure",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: O domain/codomain problem")
    print("Question:")
    print()
    print("  What are the admissible domain and codomain of O?")
    print()
    print("Reference discipline:")
    print()
    print("  O cannot act on undefined input sectors.")
    print("  O cannot output into undefined safe sectors.")
    print("  Domain/codomain classification is not yet kernel, image, no-overlap, insertion, or parent closure.")

    with out.governance_assessments():
        out.line(
            "O domain/codomain inventory opened",
            StatusMark.INFO,
            "testing admissible O input and output sectors",
        )


def case_1_symbol_ledger(symbols: DomainCodomainSymbols, out: ScriptOutput) -> None:
    header("Case 1: Candidate domain/codomain symbolic ledger")
    print("Candidate domain:")
    print()
    print(f"  D_O_candidate = {sp.sstr(symbols.domain_candidate)}")
    print()
    print("Candidate codomain:")
    print()
    print(f"  C_O_candidate = {sp.sstr(symbols.codomain_candidate)}")
    print()
    print("Domain/codomain gap:")
    print()
    print(f"  L_domain_codomain_gap = {sp.sstr(symbols.dc_gap)}")
    print()
    print("Interpretation:")
    print()
    print("  This is a candidate inventory, not a finished operator.")
    print("  Domain and codomain must be narrowed before kernel/image can be claimed.")

    with out.derived_results():
        out.line(
            "O domain/codomain candidate ledger stated",
            StatusMark.OBLIGATION,
            f"D_O = {sp.sstr(symbols.domain_candidate)} ; C_O = {sp.sstr(symbols.codomain_candidate)}",
        )


def case_2_domains(domains: List[DomainCandidate], out: ScriptOutput) -> None:
    header("Case 2: Candidate O domain sectors")
    for item in domains:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Sector: {item.sector}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Include if: {item.include_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "O domain candidates classified",
            StatusMark.PASS,
            f"{len(domains)} domain candidates classified",
        )


def case_3_codomain(codomains: List[CodomainCandidate], out: ScriptOutput) -> None:
    header("Case 3: Candidate O codomain sectors")
    for item in codomains:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Sector: {item.sector}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Include if: {item.include_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "O codomain candidates classified",
            StatusMark.PASS,
            f"{len(codomains)} codomain candidates classified",
        )


def case_4_pairs(pairs: List[DomainCodomainPair], out: ScriptOutput) -> None:
    header("Case 4: Candidate domain/codomain mappings")
    for item in pairs:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Mapping: {item.mapping}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Works if: {item.works_if}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "O domain/codomain mappings classified",
            StatusMark.OBLIGATION,
            "safe trace mapping candidate exists; residual mappings remain underdetermined",
        )


def case_5_shortcuts(shortcuts: List[RejectedDomainCodomainShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected domain/codomain shortcuts")
    for item in shortcuts:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Shortcut: {item.shortcut}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "O domain/codomain shortcuts rejected",
            StatusMark.FAIL,
            "universal domain, safe codomain by label, inert sector by naming, accounting reservoir, recovery-selected domain, and parent codomain are rejected",
        )


def case_6_conclusions(conclusions: List[DomainCodomainConclusion], out: ScriptOutput) -> None:
    header("Case 6: Domain/codomain conclusions")
    for item in conclusions:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "O domain/codomain conclusion stated",
            StatusMark.DEFER,
            "candidate domain/codomain available; residual codomain remains underdetermined pending kernel/image and no-overlap criterion",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("O domain/codomain result:")
    print()
    print("  Candidate domain sectors are available.")
    print("  Candidate codomain sectors are available.")
    print("  O(zeta_Bs) -> safe trace sector is the cleanest candidate preservation mapping.")
    print("  zeta/kappa residual codomain remains underdetermined.")
    print("  accounting codomain cannot become a hidden reservoir.")
    print("  parent field-equation codomain is rejected.")
    print("  Kernel/image and no-overlap criterion remain next.")
    print("  O is not derived by this script.")
    print()
    print("Possible next script:")
    print("  candidate_O_kernel_image.py")
    print()
    print("Tiny goblin label:")
    print("  No door without a room on both sides.")

    with out.governance_assessments():
        out.line(
            "O domain/codomain inventory complete",
            StatusMark.PASS,
            "domain/codomain candidates classified; O remains not derived",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: DomainCodomainSymbols) -> None:
    ns.record_derivation(
        derivation_id="g27_O_domain_codomain",
        inputs=[
            symbols.zeta_Bs,
            symbols.zeta_res,
            symbols.kappa_res,
            symbols.eps_acc,
            symbols.ekappa_acc,
            symbols.boundary_data,
            symbols.source_data,
            symbols.support_data,
        ],
        output=sp.Tuple(symbols.domain_candidate, symbols.codomain_candidate),
        method="state candidate active-O domain and codomain inventories",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="O_domain_codomain_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_dc_narrow_domain", "Narrow O domain"),
        ("g27_dc_narrow_codomain", "Narrow O codomain"),
        ("g27_dc_safe_trace", "Preserve zeta_to_Bs safe trace sector"),
        ("g27_dc_res_sector", "Define residual codomain sector"),
        ("g27_dc_accounting", "Keep accounting codomain non-reservoir"),
        ("g27_dc_no_parent", "Exclude parent codomain"),
        ("g27_dc_next_kernel", "Derive kernel/image next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_dc_route"],
            description=(
                "O domain/codomain candidates are inventoried here, but O is not yet derived. Kernel/image and no-overlap criterion remain open."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_dc_narrow_domain",
        "g27_dc_narrow_codomain",
        "g27_dc_safe_trace",
        "g27_dc_res_sector",
        "g27_dc_accounting",
        "g27_dc_no_parent",
        "g27_dc_next_kernel",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_dc_route",
        script_id=SCRIPT_ID,
        name="Group 27 O domain/codomain route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "O domain and codomain remain candidates, not full operator structure",
            "safe trace sector is preserved",
            "zeta/kappa residual codomain is not resolved by naming",
            "accounting codomain is not hidden reservoir",
            "parent codomain is rejected",
        ],
    ))

    for branch_id in [
        "O_universal_domain",
        "O_safe_codomain_by_label",
        "O_inert_by_naming",
        "O_accounting_reservoir",
        "O_recovery_domain",
        "O_parent_codomain",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; O domain/codomain must be constructed, not assumed.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_dc_not_operator",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Candidate active-O domain and codomain sectors are inventoried. O(zeta_Bs) -> safe trace sector is the cleanest candidate preservation mapping; "
            "zeta/kappa residual codomain remains underdetermined; accounting codomain cannot be a hidden reservoir; parent codomain is rejected. "
            "This does not derive O."
        ),
        derivation_ids=["g27_O_domain_codomain"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate O Domain Codomain")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    domains = build_domain_candidates()
    codomains = build_codomain_candidates()
    pairs = build_pairs()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_domains(domains, out)
    case_3_codomain(codomains, out)
    case_4_pairs(pairs, out)
    case_5_shortcuts(shortcuts, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
