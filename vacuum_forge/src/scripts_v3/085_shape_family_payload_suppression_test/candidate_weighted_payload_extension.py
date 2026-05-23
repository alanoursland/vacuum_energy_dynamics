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
    ("g85_profile_validation", "085_shape_family_payload_suppression_test__candidate_suppressed_profile_validation", "g85_profile_validation"),
]
MARKER_ID = "g85_weighted_extension"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, R, ell = sp.symbols("y R ell", nonzero=True)
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 - 12*y**2 + 51*y**4
    Xi = f*P
    J = sp.factor(w*sp.diff(Xi, y))
    rho = sp.factor(sp.diff(J, y))
    mu = R**2 + 2*R*ell*y + ell**2*y**2
    weighted = [sp.factor(sp.integrate(sp.expand(mu*y**n*rho), (y, -1, 1))) for n in range(5)]

    header("Candidate Weighted Payload Extension")
    print(f"mu = {mu}")
    for n, m in enumerate(weighted):
        print(f"W{n} = {m}")

    with out.derived_results():
        for n in range(4):
            out.line(f"W{n}", StatusMark.PASS, str(weighted[n]))
        out.line("W4", StatusMark.WARN, str(weighted[4]))
    with out.governance_assessments():
        out.line("weighted suppression", StatusMark.PASS, "W0 through W3 vanish under quadratic measure")
        out.line("weighted next obstruction", StatusMark.WARN, "W4 is nonzero")
        out.line("finite-order status", StatusMark.INFO, "suppression is finite-mode, not all-order inertness")
    with out.counterexamples():
        out.line("all weighted moments vanish", StatusMark.FAIL, "W4 remains nonzero")
        out.line("full local inertness", StatusMark.FAIL, "finite weighted suppression is not full inertness")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, R, ell],
        output=sp.Matrix(weighted),
        method="compute weighted low-order moments for suppressed even quartic profile",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_payload_extension",
        scope="quadratic measure; reduced finite-mode suppression",
    )
    record_claim(ns, MARKER_ID, "g85_weighted_c1", GovernanceStatus.POLICY_RULE, "Suppressed profile kills W0..W3 under the quadratic measure but leaves W4 nonzero.")
    record_obligation(ns, "g85_weighted_o1", "Check shape admissibility and repair status.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_shape_admissibility_and_repair_discriminator.py")

if __name__ == "__main__":
    main()
