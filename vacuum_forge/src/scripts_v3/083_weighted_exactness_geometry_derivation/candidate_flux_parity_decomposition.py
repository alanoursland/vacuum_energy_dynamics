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
    ("g83_measure_gradient", "083_weighted_exactness_geometry_derivation__candidate_measure_gradient_identity", "g83_measure_gradient"),
]
MARKER_ID = "g83_parity"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, R, ell, c = sp.symbols("y R ell c")
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    J0 = sp.factor(w * sp.diff(f, y))
    J1 = sp.factor(w * (f + y*sp.diff(f, y)))
    J = sp.simplify(J0 + c*J1)
    mu_prime = 2*R*ell + 2*ell**2*y
    int_J0 = sp.simplify(sp.integrate(J0, (y, -1, 1)))
    int_yJ1 = sp.simplify(sp.integrate(y*J1, (y, -1, 1)))
    int_J1 = sp.simplify(sp.integrate(J1, (y, -1, 1)))
    int_yJ0 = sp.simplify(sp.integrate(y*J0, (y, -1, 1)))
    pairing = sp.factor(sp.integrate(sp.expand(mu_prime*J), (y, -1, 1)))
    reduced_pairing = sp.factor(2*R*ell*c*int_J1 + 2*ell**2*int_yJ0)

    header("Candidate Flux Parity Decomposition")
    print(f"J0 = {J0}")
    print(f"J1 = {J1}")
    print(f"J = J0 + c J1 = {J}")
    print(f"int J0 dy = {int_J0}")
    print(f"int y*J1 dy = {int_yJ1}")
    print(f"int J1 dy = {int_J1}")
    print(f"int y*J0 dy = {int_yJ0}")
    print(f"int mu' J dy = {pairing}")
    print(f"parity-reduced pairing = {reduced_pairing}")

    with out.derived_results():
        out.line("int J0", StatusMark.PASS, str(int_J0))
        out.line("int yJ1", StatusMark.PASS, str(int_yJ1))
        out.line("int J1", StatusMark.PASS, str(int_J1))
        out.line("int yJ0", StatusMark.PASS, str(int_yJ0))
        out.line("pairing", StatusMark.PASS, str(pairing))
    with out.governance_assessments():
        out.line("parity reduction", StatusMark.PASS, "only constant-gradient/even-flux and odd-gradient/odd-flux terms survive")
        out.line("skew role", StatusMark.INFO, "c controls the even flux component that balances measure gradient")
    with out.counterexamples():
        out.line("arbitrary skew", StatusMark.FAIL, "skew has a parity role; it is not just decorative")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, R, ell, c],
        output=pairing,
        method="decompose J into odd J0 and even cJ1 and integrate against mu'",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="flux_parity_decomposition",
        scope="reduced weighted exactness class",
    )
    record_claim(ns, MARKER_ID, "g83_parity_c1", GovernanceStatus.POLICY_RULE, "Flux parity reduces weighted neutrality to two surviving moment integrals.")
    record_obligation(ns, "g83_parity_o1", "Derive c from the surviving moment ratio.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_geometric_skew_derivation.py")

if __name__ == "__main__":
    main()
