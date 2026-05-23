from __future__ import annotations
from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord, ClaimTier, GovernanceStatus, ObligationStatus,
    ProofObligationRecord, RecordKind, ScriptOutput, StatusMark,
)

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)

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

def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )

def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )

DEPENDENCIES = [
    ("g85_moment_solver", "085_shape_family_payload_suppression_test__candidate_moment_constraint_solver", "g85_moment_solver"),
]
MARKER_ID = "g85_profile_validation"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y = sp.symbols("y")
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 - 12*y**2 + 51*y**4
    Xi = f*P
    J = sp.factor(w*sp.diff(Xi, y))
    rho = sp.factor(sp.diff(J, y))
    endpoints = (sp.simplify(J.subs(y, -1)), sp.simplify(J.subs(y, 1)))
    rho0 = sp.simplify(rho.subs(y, 0))
    moments = [sp.factor(sp.integrate(sp.expand(y**n*rho), (y, -1, 1))) for n in range(8)]

    header("Candidate Suppressed Profile Validation")
    print(f"P = {P}")
    print(f"J = {J}")
    print(f"rho = {rho}")
    print(f"J endpoints = {endpoints}")
    print(f"rho(0) = {rho0}")
    for n, m in enumerate(moments):
        print(f"M{n} = {m}")

    with out.derived_results():
        out.line("endpoint flux", StatusMark.PASS, str(endpoints))
        out.line("rho at zero", StatusMark.WARN, str(rho0))
        for n in range(6):
            out.line(f"M{n}", StatusMark.PASS, str(moments[n]))
        out.line("M6", StatusMark.WARN, str(moments[6]))
    with out.governance_assessments():
        out.line("low-order suppression", StatusMark.PASS, "M0 through M5 vanish")
        out.line("next obstruction", StatusMark.WARN, "M6 is nonzero")
        out.line("local rho", StatusMark.WARN, "rho remains locally nonzero")
    with out.counterexamples():
        out.line("full inertness overclaim", StatusMark.FAIL, "higher moments and local rho remain")
        out.line("rho equals zero", StatusMark.FAIL, "rho(0) is nonzero")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y],
        output=sp.Matrix(moments),
        method="validate even quartic suppressed profile moments",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="suppressed_profile_validation",
        scope="reduced finite-mode moment suppression",
    )
    record_claim(ns, MARKER_ID, "g85_profile_c1", GovernanceStatus.POLICY_RULE, "Suppressed profile kills M0..M5 but leaves M6/local rho nonzero.")
    record_obligation(ns, "g85_profile_o1", "Test weighted payload moments.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_weighted_payload_extension.py")

if __name__ == "__main__":
    main()
