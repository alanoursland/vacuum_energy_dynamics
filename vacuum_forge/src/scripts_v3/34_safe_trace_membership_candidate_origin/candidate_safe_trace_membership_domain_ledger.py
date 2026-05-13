# Candidate safe trace membership domain ledger
#
# Group:
#   34_safe_trace_membership_candidate_origin
#
# Human title:
#   Safe Trace Membership Candidate Origin
#
# Script type:
#   INVENTORY / DOMAIN LEDGER
#
# Purpose
# -------
# Inventory the objects needed before the candidate safe trace membership
# statement can be meaningful:
#
#   zeta_Bs -> T_zeta
#
# The origin opener established that safe membership must be tested as typed
# trace-sector membership, not selected from recovery, repair, incidence,
# residual kill, active O, insertion, or parent fit.
#
# Locked-door question:
#
#   What are zeta_Bs, T_zeta, the membership domain/codomain, and the exclusion
#   zones that must be declared before safe membership can be claimed?
#
# This script does not adopt a safe-membership postulate.
# It does not derive a safe-membership theorem.
# It does not derive trace/residual zero incidence.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not open active O or parent closure.
#
# Tiny goblin rule:
#
#   Count the shelves before declaring the cup belongs.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
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


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def subheader(title: str) -> None:
    print()
    print("-" * 120)
    print(title)
    print("-" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "ADMISSIBLE_DOMAIN_OBJECT": StatusMark.INFO,
        "CANDIDATE_MEMBERSHIP_CRITERION": StatusMark.INFO,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "EXCLUSION_ZONE": StatusMark.DEFER,
        "FILTER_FAIL": StatusMark.FAIL,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "ROLE_SEPARATION": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g34_origin_problem",
            "34_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_origin_problem",
            "g34_safe_membership_origin_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_summary",
            "33_trace_normalization_candidate_origin__candidate_group_33_status_summary",
            "g33_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_summary",
            "32_explicit_minimal_postulate_selection__candidate_group_32_status_summary",
            "g32_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=record_kind,
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


@dataclass
class DomainSymbols:
    zeta_Bs: sp.Symbol
    T_zeta: sp.Symbol
    D_Bs: sp.Symbol
    C_Tzeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    S_ord: sp.Symbol
    C_div: sp.Symbol
    N_trace: sp.Symbol
    M_safe: sp.Symbol
    P_incidence_zero: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_insertion: sp.Symbol
    P_parent: sp.Symbol
    L_domain_objects: sp.Basic
    L_exclusion_zones: sp.Basic
    L_downstream_gates: sp.Basic
    L_domain_gap: sp.Basic


@dataclass
class DomainObjectEntry:
    name: str
    object_name: str
    status: str
    role: str
    required_declaration: str
    forbidden_upgrade: str


@dataclass
class CriterionEntry:
    name: str
    criterion: str
    status: str
    allowed_use: str
    forbidden_use: str
    consequence: str


@dataclass
class FenceEntry:
    name: str
    fence: str
    status: str
    reason: str
    failure_mode: str


@dataclass
class ObligationEntry:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class ConclusionEntry:
    name: str
    conclusion: str
    status: str
    meaning: str


def case_0_problem(out: ScriptOutput) -> None:
    header("Candidate Safe Trace Membership Domain Ledger")
    header("Case 0: Safe-membership domain ledger problem")
    print("Question:")
    print()
    print("  What are zeta_Bs, T_zeta, the membership domain/codomain, and the exclusion")
    print("  zones that must be declared before safe membership can be claimed?")
    print()
    print("Discipline:")
    print()
    print("  This script inventories membership objects and fences.")
    print("  It adopts no safe-membership postulate.")
    print("  It derives no safe-membership theorem.")
    print("  It derives no trace/residual zero incidence.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Count the shelves before declaring the cup belongs.")

    with out.governance_assessments():
        out.line(
            "safe-membership domain ledger opened",
            StatusMark.INFO,
            "membership objects and exclusion zones are inventoried before membership forms",
        )


def case_1_symbolic_ledger(out: ScriptOutput) -> DomainSymbols:
    header("Case 1: Safe-membership domain symbolic ledger")

    zeta_Bs, T_zeta, D_Bs, C_Tzeta = sp.symbols("zeta_Bs T_zeta D_Bs C_Tzeta")
    R_zeta, R_kappa, S_ord, C_div = sp.symbols("R_zeta R_kappa S_ord C_div")
    N_trace, M_safe = sp.symbols("N_trace M_safe")
    P_incidence_zero, P_active_O, P_residual_kill, P_insertion, P_parent = sp.symbols(
        "P_incidence_zero P_active_O P_residual_kill P_insertion P_parent"
    )

    L_domain_objects = sp.simplify(zeta_Bs + T_zeta + D_Bs + C_Tzeta + M_safe)
    L_exclusion_zones = sp.simplify(R_zeta + R_kappa + S_ord + C_div)
    L_downstream_gates = sp.simplify(P_incidence_zero + P_active_O + P_residual_kill + P_insertion + P_parent)
    L_domain_gap = sp.simplify(L_domain_objects + L_exclusion_zones + L_downstream_gates + N_trace)

    print("Membership/domain symbols:")
    for sym in [
        zeta_Bs,
        T_zeta,
        D_Bs,
        C_Tzeta,
        R_zeta,
        R_kappa,
        S_ord,
        C_div,
        N_trace,
        M_safe,
        P_incidence_zero,
        P_active_O,
        P_residual_kill,
        P_insertion,
        P_parent,
    ]:
        print(f"  {sym} = {sym}")

    print()
    print(f"Domain object load:\n  L_domain_objects = {L_domain_objects}")
    print()
    print(f"Exclusion-zone load:\n  L_exclusion_zones = {L_exclusion_zones}")
    print()
    print(f"Downstream gate load:\n  L_downstream_gates = {L_downstream_gates}")
    print()
    print(f"Domain-ledger gap:\n  L_domain_gap = {L_domain_gap}")

    with out.derived_results():
        out.line(
            "safe-membership domain loads stated",
            StatusMark.OBLIGATION,
            f"L_domain_objects = {L_domain_objects}; L_exclusion_zones = {L_exclusion_zones}",
        )

    return DomainSymbols(
        zeta_Bs=zeta_Bs,
        T_zeta=T_zeta,
        D_Bs=D_Bs,
        C_Tzeta=C_Tzeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        S_ord=S_ord,
        C_div=C_div,
        N_trace=N_trace,
        M_safe=M_safe,
        P_incidence_zero=P_incidence_zero,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_insertion=P_insertion,
        P_parent=P_parent,
        L_domain_objects=L_domain_objects,
        L_exclusion_zones=L_exclusion_zones,
        L_downstream_gates=L_downstream_gates,
        L_domain_gap=L_domain_gap,
    )


def build_domain_objects() -> List[DomainObjectEntry]:
    return [
        DomainObjectEntry(
            name="D1: zeta_Bs object",
            object_name="zeta_Bs",
            status="ADMISSIBLE_DOMAIN_OBJECT",
            role="candidate trace object induced by the B_s spatial-response side",
            required_declaration="state whether this is metric trace contribution, bookkeeping trace variable, or normalized trace payload",
            forbidden_upgrade="must not be treated as residual kill, insertion, or source carrier",
        ),
        DomainObjectEntry(
            name="D2: T_zeta trace sector",
            object_name="T_zeta",
            status="ADMISSIBLE_DOMAIN_OBJECT",
            role="typed target sector for zeta trace membership",
            required_declaration="state domain/codomain, sector basis, and what counts as trace-sector content",
            forbidden_upgrade="must not be an undefined sector label used as proof of membership",
        ),
        DomainObjectEntry(
            name="D3: D_Bs membership domain",
            object_name="D_Bs",
            status="ADMISSIBLE_DOMAIN_OBJECT",
            role="domain containing objects that may be tested for membership",
            required_declaration="state what objects can be tested for membership before claiming zeta_Bs belongs",
            forbidden_upgrade="must not include residual/source/correction zones by convenience",
        ),
        DomainObjectEntry(
            name="D4: C_Tzeta membership codomain",
            object_name="C_Tzeta",
            status="ADMISSIBLE_DOMAIN_OBJECT",
            role="codomain or target class for accepted trace-sector assignments",
            required_declaration="state what the membership statement lands in and how it is typed",
            forbidden_upgrade="must not imply no-overlap operator or incidence theorem",
        ),
        DomainObjectEntry(
            name="D5: N_trace compatibility node",
            object_name="N_trace",
            status="COMPATIBILITY_ONLY",
            role="trace-normalization candidate from Group 33 compatible-if-declared forms",
            required_declaration="carry as separate node from safe membership",
            forbidden_upgrade="normalization must not choose membership and membership must not choose normalization",
        ),
    ]


def case_2_domain_objects(out: ScriptOutput) -> List[DomainObjectEntry]:
    header("Case 2: Membership domain objects")
    entries = build_domain_objects()
    for item in entries:
        subheader(item.name)
        print(f"Object: {item.object_name}")
        print(f"Role: {item.role}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Required declaration: {item.required_declaration}")
        print(f"Forbidden upgrade: {item.forbidden_upgrade}")

    with out.governance_assessments():
        out.line(
            "membership domain objects stated",
            StatusMark.INFO,
            f"{len(entries)} membership/domain objects inventoried",
        )
    return entries


def build_criteria() -> List[CriterionEntry]:
    return [
        CriterionEntry(
            name="M1: typed membership criterion",
            criterion="zeta_Bs belongs to T_zeta only if both object and sector type are declared before use",
            status="CANDIDATE_MEMBERSHIP_CRITERION",
            allowed_use="candidate criterion for later membership-form testing",
            forbidden_use="must not be treated as derived theorem now",
            consequence="membership remains candidate until criterion is derived or adopted",
        ),
        CriterionEntry(
            name="M2: role-purity criterion",
            criterion="zeta_Bs is accepted only as trace-sector payload, not residual/source/correction payload",
            status="CANDIDATE_MEMBERSHIP_CRITERION",
            allowed_use="anti-smuggling criterion for membership forms",
            forbidden_use="must not become residual kill or full source no-double-counting theorem",
            consequence="forms that hide residual/source/correction load fail later sieve",
        ),
        CriterionEntry(
            name="M3: normalization compatibility criterion",
            criterion="membership form must be compatible with separately declared N_trace convention",
            status="COMPATIBILITY_ONLY",
            allowed_use="compatibility check with Group 33 forms",
            forbidden_use="must not collapse membership and normalization into one postulate",
            consequence="normalization and membership remain separate Package B nodes",
        ),
        CriterionEntry(
            name="M4: visibility criterion",
            criterion="membership cannot hide ordinary source load or correction/divergence reservoir load",
            status="CANDIDATE_MEMBERSHIP_CRITERION",
            allowed_use="negative filter against hidden load membership forms",
            forbidden_use="must not select membership merely because a candidate avoids one failure",
            consequence="visibility filters may reject but not choose membership",
        ),
    ]


def case_3_membership_criteria(out: ScriptOutput) -> List[CriterionEntry]:
    header("Case 3: Candidate membership criteria")
    entries = build_criteria()
    for item in entries:
        subheader(item.name)
        print(f"Criterion: {item.criterion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Allowed use: {item.allowed_use}")
        print(f"Forbidden use: {item.forbidden_use}")
        print(f"Consequence: {item.consequence}")

    with out.governance_assessments():
        out.line(
            "candidate membership criteria stated",
            StatusMark.DEFER,
            f"{len(entries)} criteria stated; none derived or adopted",
        )
    return entries


def build_fences() -> List[FenceEntry]:
    return [
        FenceEntry(
            name="F1: residual-zeta fence",
            fence="T_zeta membership does not include R_zeta or erase residual zeta",
            status="EXCLUSION_ZONE",
            reason="membership is not residual control",
            failure_mode="safe membership silently becomes residual kill",
        ),
        FenceEntry(
            name="F2: residual-kappa fence",
            fence="T_zeta membership does not include R_kappa or erase residual kappa",
            status="EXCLUSION_ZONE",
            reason="kappa residual control is separate theorem target",
            failure_mode="membership smuggles kappa residual non-entry",
        ),
        FenceEntry(
            name="F3: ordinary-source fence",
            fence="T_zeta membership does not carry ordinary source load S_ord",
            status="EXCLUSION_ZONE",
            reason="ordinary source load remains visible and protected",
            failure_mode="membership becomes source pocket",
        ),
        FenceEntry(
            name="F4: correction-divergence fence",
            fence="T_zeta membership does not carry hidden correction or divergence reservoir C_div",
            status="EXCLUSION_ZONE",
            reason="divergence explicitness remains non-reservoir discipline",
            failure_mode="membership becomes correction reservoir",
        ),
        FenceEntry(
            name="F5: incidence fence",
            fence="zeta_Bs -> T_zeta does not imply I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0",
            status="REQUIRED",
            reason="incidence remains high-risk and separate",
            failure_mode="membership becomes zero-incidence theorem by implication",
        ),
        FenceEntry(
            name="F6: downstream fence",
            fence="membership does not imply active O, residual kill, insertion, or parent closure",
            status="NOT_READY",
            reason="downstream gates remain closed",
            failure_mode="membership opens field-equation gates prematurely",
        ),
    ]


def case_4_exclusion_fences(out: ScriptOutput) -> List[FenceEntry]:
    header("Case 4: Membership exclusion fences")
    entries = build_fences()
    for item in entries:
        subheader(item.name)
        print(f"Fence: {item.fence}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Failure mode: {item.failure_mode}")

    with out.governance_assessments():
        out.line(
            "membership exclusion fences stated",
            StatusMark.OBLIGATION,
            f"{len(entries)} fences stated against residual/source/correction/downstream smuggling",
        )
    return entries


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry(
            name="O1: define zeta_Bs object",
            obligation="declare what zeta_Bs is before testing membership",
            status="OPEN",
            blocks="membership-form testing",
            discipline="object must be visible before membership is claimed",
        ),
        ObligationEntry(
            name="O2: define T_zeta sector",
            obligation="declare T_zeta domain/codomain and sector basis",
            status="OPEN",
            blocks="typed trace-sector membership",
            discipline="sector label is not proof",
        ),
        ObligationEntry(
            name="O3: preserve normalization separation",
            obligation="keep P_trace_norm and P_safe_membership as separate nodes",
            status="OPEN",
            blocks="Package B collapse",
            discipline="membership is not normalization",
        ),
        ObligationEntry(
            name="O4: preserve exclusion zones",
            obligation="keep residual/source/correction zones outside membership unless separately derived",
            status="OPEN",
            blocks="smuggling and hidden load",
            discipline="membership is not residual/source/correction cleanup",
        ),
        ObligationEntry(
            name="O5: adoption boundary",
            obligation="keep P_safe_membership unadopted unless a separate explicit decision is requested",
            status="OPEN",
            blocks="accidental adoption",
            discipline="domain ledger is not postulate selection",
        ),
        ObligationEntry(
            name="O6: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="domain ledger is not insertion or parent closure",
        ),
    ]


def case_5_obligations(out: ScriptOutput) -> List[ObligationEntry]:
    header("Case 5: Safe-membership domain obligations")
    entries = build_obligations()
    for item in entries:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "safe-membership domain obligations opened",
            StatusMark.OBLIGATION,
            f"{len(entries)} obligations stated",
        )
    return entries


def build_conclusions() -> List[ConclusionEntry]:
    return [
        ConclusionEntry(
            name="C1: domain objects visible",
            conclusion="zeta_Bs, T_zeta, membership domain, and membership codomain are visible as required objects",
            status="REQUIRED",
            meaning="membership can now be tested without hiding objects in prose",
        ),
        ConclusionEntry(
            name="C2: membership remains candidate",
            conclusion="safe membership remains a candidate typed-sector assignment, not a theorem",
            status="NOT_DERIVED",
            meaning="domain ledger does not prove zeta_Bs belongs to T_zeta",
        ),
        ConclusionEntry(
            name="C3: exclusion zones fenced",
            conclusion="residual, source, correction, incidence, and downstream zones are fenced from membership",
            status="REQUIRED",
            meaning="membership cannot smuggle residual control or hidden load",
        ),
        ConclusionEntry(
            name="C4: no adoption",
            conclusion="this domain ledger adopts no safe-membership postulate",
            status="NOT_ADOPTED",
            meaning="explicit decision remains separate",
        ),
        ConclusionEntry(
            name="C5: downstream gates",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="domain ledger does not open downstream gates",
        ),
        ConclusionEntry(
            name="C6: next",
            conclusion="safe-membership selector rejection should run next",
            status="OPEN",
            meaning="selector firewall should be made explicit before membership-form comparison",
        ),
    ]


def case_6_conclusions(out: ScriptOutput) -> List[ConclusionEntry]:
    header("Case 6: Safe-membership domain conclusions")
    entries = build_conclusions()
    for item in entries:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "safe-membership domain ledger conclusion stated",
            StatusMark.PASS,
            "domain objects visible; no membership derived or adopted; selector rejection should run next",
        )
    return entries


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Safe-membership domain ledger result:")
    print()
    print("  zeta_Bs, T_zeta, membership domain, and membership codomain are now visible objects.")
    print("  A candidate membership criterion can be typed, but it is not derived by this ledger.")
    print("  Safe membership remains separate from trace normalization.")
    print("  Safe membership remains separate from trace/residual zero incidence.")
    print("  Residual, ordinary-source, and correction/divergence zones are fenced from membership.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print("  No safe-membership postulate is adopted by this ledger.")
    print()
    print("Possible next script:")
    print("  candidate_safe_trace_membership_selector_rejection.py")
    print()
    print("Tiny goblin label:")
    print("  Count the shelves before declaring the cup belongs.")

    with out.governance_assessments():
        out.line(
            "safe-membership domain ledger complete",
            StatusMark.PASS,
            "selector rejection should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: DomainSymbols) -> None:
    ns.record_derivation(
        derivation_id="g34_safe_membership_domain_ledger",
        inputs=[symbols.zeta_Bs, symbols.T_zeta, symbols.D_Bs, symbols.C_Tzeta],
        output=symbols.L_domain_gap,
        method="safe trace membership domain ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="domain_ledger_marker",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[ObligationEntry]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g34_domain_obligation_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation} Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(
    ns,
    objects: List[DomainObjectEntry],
    criteria: List[CriterionEntry],
    fences: List[FenceEntry],
    conclusions: List[ConclusionEntry],
) -> None:
    obligation_ids = [
        "g34_domain_obligation_o1",
        "g34_domain_obligation_o2",
        "g34_domain_obligation_o3",
        "g34_domain_obligation_o4",
        "g34_domain_obligation_o5",
        "g34_domain_obligation_o6",
    ]

    ns.record_route(
        RouteRecord(
            route_id="g34_safe_membership_domain_route",
            script_id=SCRIPT_ID,
            name="Safe trace membership domain/codomain ledger route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=obligation_ids,
            activation_conditions=[
                "safe membership is tested as typed trace-sector assignment",
                "zeta_Bs, T_zeta, domain, and codomain must be visible before membership forms",
                "membership must not imply normalization, incidence, residual kill, active O, insertion, or parent closure",
            ],
        )
    )

    for item in objects:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_domain_object_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                statement=(
                    f"{item.object_name}: {item.role}. Required declaration: {item.required_declaration}. "
                    f"Forbidden upgrade: {item.forbidden_upgrade}."
                ),
                derivation_ids=["g34_safe_membership_domain_ledger"],
                obligation_ids=obligation_ids,
            )
        )

    for item in criteria:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_route(
            RouteRecord(
                route_id=f"g34_membership_criterion_{ident}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=obligation_ids,
                activation_conditions=[
                    item.criterion,
                    f"Allowed use: {item.allowed_use}",
                    f"Forbidden use: {item.forbidden_use}",
                    f"Consequence: {item.consequence}",
                ],
            )
        )

    for item in fences:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_membership_fence_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=(
                    GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
                    if item.status in {"EXCLUSION_ZONE", "NOT_READY"}
                    else GovernanceStatus.POLICY_RULE
                ),
                statement=f"{item.fence}. Reason: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g34_safe_membership_domain_ledger"],
                obligation_ids=obligation_ids,
            )
        )

    for item in conclusions:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_domain_conclusion_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=(
                    GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
                    if item.status in {"NOT_READY", "NOT_DERIVED", "NOT_ADOPTED", "OPEN"}
                    else GovernanceStatus.CANDIDATE_ROUTE
                ),
                statement=f"{item.conclusion}. Meaning: {item.meaning}.",
                derivation_ids=["g34_safe_membership_domain_ledger"],
                obligation_ids=obligation_ids,
            )
        )


def main() -> None:
    out = ScriptOutput()
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    case_0_problem(out)
    symbols = case_1_symbolic_ledger(out)
    objects = case_2_domain_objects(out)
    criteria = case_3_membership_criteria(out)
    fences = case_4_exclusion_fences(out)
    obligations = case_5_obligations(out)
    conclusions = case_6_conclusions(out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, objects, criteria, fences, conclusions)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
