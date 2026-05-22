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
    ("g83_skew_derivation", "83_weighted_exactness_geometry_derivation__candidate_geometric_skew_derivation", "g83_skew_derivation"),
    ("g83_uniqueness_scaling", "83_weighted_exactness_geometry_derivation__candidate_uniqueness_and_scaling_test", "g83_uniqueness_scaling"),
]
MARKER_ID = "g83_repair_discriminator"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    decisions = [
        ("inside_reduced_model", "NOT_REPAIR", "c follows from measure-gradient orthogonality and moment ratio"),
        ("relative_to_Group82", "STRENGTHENED", "skew is no longer merely solved from charge after the fact"),
        ("relative_to_full_theory", "NOT_CLOSED", "f,w,mu and reduced layer are not covariantly derived"),
        ("local_rho_status", "OPEN", "local rho remains nonzero"),
        ("payload_status", "OPEN", "payload inertness remains unproven"),
        ("parent_status", "BLOCKED", "parent divergence and recombination remain blocked"),
    ]

    header("Candidate Repair Discriminator")
    for name, status, reason in decisions:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("reduced model repair status", StatusMark.PASS, "not repair inside accepted reduced weighted-exactness model")
        out.line("full theory status", StatusMark.WARN, "not full closure because reduced model assumptions remain")
        out.line("payload", StatusMark.OBLIGATION, "payload inertness remains open")
        out.line("parent", StatusMark.DEFER, "parent route remains blocked")
    with out.counterexamples():
        out.line("chosen skew", StatusMark.FAIL, "if c is inserted without measure-gradient derivation it is repair")
        out.line("model as full theory", StatusMark.FAIL, "reduced-class derivation cannot be promoted to full covariant theorem")
        out.line("weighted as local", StatusMark.FAIL, "weighted neutrality cannot be spent as local rho=0")
    with out.unresolved_obligations():
        out.line("covariant lift", StatusMark.OBLIGATION, "derive f,w,mu or lift reduced result covariantly")
        out.line("local inertness", StatusMark.OBLIGATION, "prove local rho inertness/no-payload if needed")

    record_marker(ns, MARKER_ID, "repair discriminator for derived weighted skew")
    record_claim(ns, MARKER_ID, "g83_repair_c1", GovernanceStatus.POLICY_RULE, "The skew is not repair inside the reduced weighted-exactness model, but full-theory closure remains open.")
    record_obligation(ns, "g83_repair_o1", "Lift reduced skew derivation covariantly or test local inertness.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_weighted_exactness_route_classifier.py")

if __name__ == "__main__":
    main()
