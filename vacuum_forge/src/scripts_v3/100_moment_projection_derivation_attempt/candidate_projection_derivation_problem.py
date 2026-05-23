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

def beta_moment(s):
    s = sp.sympify(s)
    return sp.factor(sp.Rational(768, 1) / sp.prod(2*s + 2*m + 1 for m in range(5)))

def row_ratio(k):
    k = sp.sympify(k)
    return sp.factor((2*k - 1) / (2*k + 3))

def hierarchy_entry(k, j):
    return sp.factor(beta_moment(k+j) - row_ratio(k) * beta_moment(k+j-1))

def weight(x):
    return (1 - x**2)**4

def trial_phi(j, x):
    return x**(2*j)

def test_psi(k, x):
    return x**(2*k) - row_ratio(k) * x**(2*k-2)

DEPENDENCIES = [
    ("g099_summary", "099_hierarchy_source_origin_audit__candidate_group_099_status_summary", "g099_summary"),
]
MARKER_ID = "g100_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    header("Candidate Projection Derivation Problem")
    print("Open Group 100: derive A_N as a formal weighted test/trial projection matrix.")
    print("Target: A[k,j] = 2 ∫ psi_k phi_j (1-x^2)^4 dx.")
    print("phi_j=x^(2j)")
    print("psi_k=x^(2k)-((2k-1)/(2k+3))x^(2k-2)")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "formal projection derivation attempt opened")
        out.line("real target", StatusMark.PASS, "derive weight/test/trial representation for A_N")
        out.line("scope", StatusMark.INFO, "formal projection origin, not physical residual/source derivation")
    with out.counterexamples():
        out.line("projection as field equation", StatusMark.FAIL, "residual/source/boundary not derived")
        out.line("projection as burden ledger", StatusMark.FAIL, "physical ledger assignment remains deferred")
    with out.unresolved_obligations():
        out.line("moment identity", StatusMark.OBLIGATION, "verify weighted moment identity")
        out.line("projection equality", StatusMark.OBLIGATION, "derive A[k,j] from test/trial functions")

    record_marker(ns, MARKER_ID, "Group 100 opening; moment projection derivation attempt")
    record_claim(ns, MARKER_ID, "g100_problem_c1", GovernanceStatus.POLICY_RULE, "Group 100 attempts to derive A_N as a formal weighted projection matrix.")
    record_obligation(ns, "g100_problem_o1", "Verify weighted moment identity.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_weighted_moment_identity.py")

if __name__ == "__main__":
    main()
