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
    ("g84_flat_moments", "084_local_rho_inertness_test__candidate_flat_probe_moment_test", "g84_flat_moments"),
]
MARKER_ID = "g84_weighted_moments"

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
    mu = R**2 + 2*R*ell*y + ell**2*y**2
    weighted = [sp.factor(sp.integrate(sp.expand(mu * y**n * rho), (y, -1, 1))) for n in range(3)]

    header("Candidate Weighted Probe Moment Test")
    print(f"mu = {mu}")
    for n, m in enumerate(weighted):
        print(f"W{n} = integral(mu*y^{n}*rho dy) = {m}")

    with out.derived_results():
        out.line("W0 weighted total moment", StatusMark.PASS, str(weighted[0]))
        out.line("W1 weighted dipole moment", StatusMark.WARN, str(weighted[1]))
        out.line("W2 weighted quadratic moment", StatusMark.WARN, str(weighted[2]))
    with out.governance_assessments():
        out.line("weighted total neutrality", StatusMark.PASS, "W0 vanishes by Group 83 skew")
        out.line("weighted local probes", StatusMark.WARN, "W1/W2 remain nonzero in general")
    with out.counterexamples():
        out.line("weighted total as local inertness", StatusMark.FAIL, "W0=0 does not imply W1=W2=0")
        out.line("weighted payload ignored", StatusMark.FAIL, "weighted low-order probes detect rho")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, R, ell],
        output=sp.Matrix(weighted),
        method="compute weighted low-order moments of Group 83 skewed rho",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_payload_moment_test",
        scope="reduced finite-mode inertness test",
    )
    record_claim(ns, MARKER_ID, "g84_weight_c1", GovernanceStatus.POLICY_RULE, "Weighted total neutrality does not imply weighted low-order inertness.")
    record_obligation(ns, "g84_weight_o1", "Test skew tradeoff between weighted neutrality and dipole inertness.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_skew_inertness_tradeoff_test.py")

if __name__ == "__main__":
    main()
