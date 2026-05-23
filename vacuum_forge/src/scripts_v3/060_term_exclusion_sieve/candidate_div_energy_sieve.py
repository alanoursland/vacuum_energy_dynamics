from __future__ import annotations

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
    ScriptOutput,
    StatusMark,
)

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"

SCRIPT_LABEL = 'Candidate Divergence/Energy Sieve'
MARKER_ID = 'g60_div'
DEPENDENCIES = [('g59_summary', '059_transition_term_audit__candidate_group_59_status_summary', 'g59_summary'), ('g60_problem', '060_term_exclusion_sieve__candidate_sieve_problem', 'g60_problem'), ('g60_src', '060_term_exclusion_sieve__candidate_source_trace_sieve', 'g60_src')]
QUESTION = 'Does the narrowed stress-only candidate survive divergence while preserving explicit energy burden?'
DISCIPLINE = 'This script rejects radial-only stress, retains closure-supported reduced D=0, and preserves nonfree energy/stress burden.'
OPENING_LINE = 'Divergence/energy sieve opened'
SCOPE = 'Group 60 divergence energy sieve'
NEXT_SCRIPT = 'candidate_sieve_classifier.py'

ENTRIES = [('V1: radial-only rejection', 'p_t=0 gives D != 0', 'DIVERGENCE_FAILING_TERM_REJECTED', 'radial-only stress remains dead', 'rejected'), ('V2: closure survivor', "p_t=p_r+r*p_r'/2 gives D=0", 'CLOSURE_SUPPORTED_TERM_SURVIVES', 'closure-supported stress survives reduced divergence', 'conditional'), ('V3: energy burden', 'layer stress/energy is nonfree', 'ENERGY_ACCOUNTING_REQUIRED', 'survivor must carry explicit energy/stress accounting', 'open')]
SHORTCUTS = [('X1: radial-only stress', 'accept eta^2 pressure without tangential closure', 'reduced divergence fails'), ('X2: D=0 as Bianchi', 'treat reduced closure as covariant identity', 'covariant lift required'), ('X3: free transition response', 'treat closure-supported term as costless', 'energy/stress accounting remains required')]
OBLIGATIONS = [('O1: covariant divergence identity', 'DIVERGENCE_IDENTITY_REQUIRED', 'lift closure route to covariant identity structure', 'avoid parent overclaim'), ('O2: energy/stress accounting', 'ENERGY_ACCOUNTING_REQUIRED', 'derive admissible energy/stress role for surviving closure response', 'avoid free response')]
LOCAL_CONCLUSIONS = [('divergence energy sieve applied', 'PASS', 'radial-only route rejected and closure route remains conditional'), ('energy burden retained', 'ENERGY_ACCOUNTING_REQUIRED', 'survivor is nonfree and needs accounting')]


@dataclass(frozen=True)
class Entry:
    name: str
    subject: str
    status: str
    detail: str
    boundary: str


@dataclass(frozen=True)
class Shortcut:
    name: str
    shortcut: str
    reason: str


@dataclass(frozen=True)
class ObligationEntry:
    name: str
    status: str
    obligation: str
    discipline: str


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


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
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


def mark(status: str) -> StatusMark:
    return {
        "PASS": StatusMark.PASS,
        "SIEVE_OPENED": StatusMark.INFO,
        "REPAIR_TERM_REJECTED": StatusMark.FAIL,
        "RESIDUE_CLUE_RETAINED": StatusMark.INFO,
        "DERIVATIVE_SIEVE_APPLIED": StatusMark.PASS,
        "DERIVATIVE_BURDEN_FOUND": StatusMark.OBLIGATION,
        "STRONG_LOCALITY_CONFIRMED": StatusMark.PASS,
        "WEIGHTED_NEUTRALITY_CONFIRMED": StatusMark.PASS,
        "SCALAR_CHARGE_TERM_REJECTED": StatusMark.FAIL,
        "STRESS_ONLY_INTERPRETATION_REQUIRED": StatusMark.OBLIGATION,
        "TUNING_ROUTE_REJECTED": StatusMark.FAIL,
        "SOURCE_CARRYING_TERM_REJECTED": StatusMark.FAIL,
        "TRACE_DOUBLE_COUNT_TERM_REJECTED": StatusMark.FAIL,
        "SOURCE_TRACE_SIEVE_APPLIED": StatusMark.PASS,
        "DIVERGENCE_FAILING_TERM_REJECTED": StatusMark.FAIL,
        "CLOSURE_SUPPORTED_TERM_SURVIVES": StatusMark.INFO,
        "ENERGY_ACCOUNTING_REQUIRED": StatusMark.OBLIGATION,
        "TERM_SURVIVES_NARROWLY": StatusMark.INFO,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "REPAIR_TERM_REJECTED",
        "SCALAR_CHARGE_TERM_REJECTED",
        "TUNING_ROUTE_REJECTED",
        "SOURCE_CARRYING_TERM_REJECTED",
        "TRACE_DOUBLE_COUNT_TERM_REJECTED",
        "DIVERGENCE_FAILING_TERM_REJECTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "DERIVATIVE_BURDEN_FOUND",
        "STRESS_ONLY_INTERPRETATION_REQUIRED",
        "ENERGY_ACCOUNTING_REQUIRED",
        "COVARIANT_LIFT_REQUIRED",
        "SOURCE_SAFETY_REQUIRED",
        "DIVERGENCE_IDENTITY_REQUIRED",
        "SAFETY_THEOREMS_REQUIRED",
        "POLICY_RULE",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "PHYSICAL_USE_BLOCKED",
        "NOT_INSERTABLE",
        "DEFERRED_WITH_TARGET",
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def record_marker(ns, marker_id: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(marker_id),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=scope,
    )


def record_claim(ns, claim_id: str, marker_id: str, status: str, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=governance_status(status),
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, title: str, statement: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


def record_governance(ns, marker_id: str, entries: List[Entry], obligations: List[ObligationEntry], scope: str) -> None:
    record_marker(ns, marker_id, scope)
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{marker_id}_c{idx}", marker_id, item.status, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(obligations, 1):
        record_obligation(ns, f"{marker_id}_o{idx}", item.name, f"{item.obligation}. Discipline: {item.discipline}.", item.status)


def print_entries(out: ScriptOutput, entries: List[Entry], title: str) -> None:
    header(title)
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}. Boundary: {item.boundary}")


def print_shortcuts(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    header("Rejected shortcuts and invalid upgrades")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def print_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Open obligations and deferred burdens")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def build_entries() -> List[Entry]:
    return [Entry(*item) for item in ENTRIES]


def build_shortcuts() -> List[Shortcut]:
    return [Shortcut(*item) for item in SHORTCUTS]


def build_obligations() -> List[ObligationEntry]:
    return [ObligationEntry(*item) for item in OBLIGATIONS]



def case_div_energy_sieve(out: ScriptOutput):
    header("Case 0: Divergence and energy-burden sieve")

    y, R, ell, p0 = sp.symbols("y R ell p0", positive=True)
    r = sp.simplify(R + ell*y)
    c = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    w = sp.simplify((1 - y**2)**2)
    eta = sp.simplify(w*(y - c))
    p_r = sp.simplify(p0*eta**2)

    dp_dr = sp.simplify(sp.diff(p_r, y)/ell)
    D_radial = sp.simplify(dp_dr + 2*p_r/r)
    p_t = sp.simplify(p_r + r*dp_dr/2)
    D_closure = sp.simplify(dp_dr + 2*(p_r-p_t)/r)

    energy_density = sp.simplify(p_r)
    E_layer = sp.simplify(sp.integrate(energy_density*ell, (y, -1, 1)))
    E_thin_coeff = sp.simplify(sp.limit(E_layer/ell, ell, 0, dir="+"))

    print(f"p_r = {p_r}")
    print(f"D radial-only = {D_radial}")
    print(f"p_t closure = {p_t}")
    print(f"D closure = {D_closure}")
    print(f"E_layer ~ integral p_r dr = {sp.factor(E_layer)}")
    print(f"thin coefficient E/ell -> {sp.factor(E_thin_coeff)}")

    with out.derived_results():
        out.line("radial-only D", StatusMark.FAIL if not is_zero(D_radial) else StatusMark.PASS, f"{D_radial}")
        out.line("closure p_t", StatusMark.PASS, f"{p_t}")
        out.line("closure D", StatusMark.PASS if is_zero(D_closure) else StatusMark.FAIL, f"{D_closure}")
        out.line("layer energy", StatusMark.OBLIGATION, f"E={sp.factor(E_layer)}")
        out.line("energy coefficient", StatusMark.OBLIGATION, f"E/ell -> {sp.factor(E_thin_coeff)}")

    return {"y": y, "R": R, "ell": ell, "p_r": p_r, "D_radial": D_radial, "D_closure": D_closure, "E_layer": E_layer}


def record_div_energy(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g60_divE",
        inputs=[data["y"], data["R"], data["ell"]],
        output=data["D_closure"],
        method="reject radial-only stress, retain closure-supported D=0, and state nonfree layer energy burden",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="divergence_energy_sieve",
        scope="reduced divergence/energy filter; not Bianchi or stress theorem",
    )



def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print(QUESTION)
    print("\nDiscipline:\n")
    print(DISCIPLINE)
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_LINE)

    data = case_div_energy_sieve(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_div_energy(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
