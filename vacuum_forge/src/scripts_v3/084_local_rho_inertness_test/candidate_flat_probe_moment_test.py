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
    ("g84_probe_basis", "084_local_rho_inertness_test__candidate_payload_probe_basis", "g84_probe_basis"),
]
MARKER_ID = "g84_flat_moments"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, R, ell = sp.symbols("y R ell", nonzero=True)
    c = sp.Rational(3, 2) * ell / R
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    Xi = f * (1 + c*y)
    J = sp.simplify(w * sp.diff(Xi, y))
    rho = sp.factor(sp.diff(J, y))
    moments = [sp.factor(sp.integrate(sp.expand(y**n * rho), (y, -1, 1))) for n in range(3)]

    header("Candidate Flat Probe Moment Test")
    print(f"derived skew c = {c}")
    print(f"rho_skew = {rho}")
    for n, m in enumerate(moments):
        print(f"M{n} = integral(y^{n} rho dy) = {m}")

    with out.derived_results():
        out.line("M0 global source moment", StatusMark.PASS, str(moments[0]))
        out.line("M1 dipole moment", StatusMark.WARN, str(moments[1]))
        out.line("M2 quadratic moment", StatusMark.WARN, str(moments[2]))
    with out.governance_assessments():
        out.line("global neutrality", StatusMark.PASS, "M0 vanishes")
        out.line("dipole sensitivity", StatusMark.WARN, "M1 nonzero for ell/R != 0")
        out.line("quadratic sensitivity", StatusMark.WARN, "M2 nonzero")
    with out.counterexamples():
        out.line("global as local inertness", StatusMark.FAIL, "M0=0 does not imply M1=M2=0")
        out.line("payload inertness overclaim", StatusMark.FAIL, "low-order local payload probes detect rho")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, R, ell],
        output=sp.Matrix(moments),
        method="compute flat low-order moments of Group 83 skewed rho",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="flat_payload_moment_test",
        scope="reduced finite-mode inertness test",
    )
    record_claim(ns, MARKER_ID, "g84_flat_c1", GovernanceStatus.POLICY_RULE, "Group 83 skewed rho is globally neutral but not inert to low-order flat probes.")
    record_obligation(ns, "g84_flat_o1", "Compute weighted payload moments.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_weighted_probe_moment_test.py")

if __name__ == "__main__":
    main()
