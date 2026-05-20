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
    print(); print("=" * 120); print(title); print("=" * 120)


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT); ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(dependency_id=dep_id, upstream_script_id=upstream_script_id, upstream_derivation_id=upstream_derivation_id)
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated: print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared."); return
    print("[INFO] Archive dependency check:")
    for check in checks: print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(ClaimRecord(claim_id=claim_id, script_id=SCRIPT_ID, claim_kind=RecordKind.GOVERNANCE_CLAIM, tier=ClaimTier.CONSTRAINED, status=status, statement=statement, derivation_ids=[marker_id], obligation_ids=[]))


def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(ProofObligationRecord(obligation_id=obligation_id, script_id=SCRIPT_ID, title=obligation_id, status=status, required_by=[SCRIPT_ID], description=statement))


DEPENDENCIES = [
    ("g73_requirements", "73_layer_generator_construction__candidate_geometric_layer_generator_requirements", "g73_requirements"),
]
MARKER_ID = "g73_signed_distance"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, ell, A = sp.symbols("y ell A", nonzero=True)
    window = sp.expand((1 - y**2)**2)
    endpoint_data = {
        "value_minus": sp.simplify(window.subs(y, -1)),
        "value_plus": sp.simplify(window.subs(y, 1)),
        "slope_minus": sp.simplify(sp.diff(window, y).subs(y, -1)),
        "slope_plus": sp.simplify(sp.diff(window, y).subs(y, 1)),
    }
    layer_flux = A * window
    layer_divergence_scaffold = sp.simplify(sp.diff(layer_flux, y) / ell)
    integral_flux_derivative = sp.simplify(sp.integrate(sp.diff(layer_flux, y), (y, -1, 1)))

    header("Candidate Signed-Distance Layer Scaffold")
    print("signed layer coordinate: y = n/ell")
    print(f"window = {window}")
    print(f"endpoint data = {endpoint_data}")
    print(f"layer flux scaffold J_layer = {layer_flux}")
    print(f"D_layer scaffold = dJ_layer/dn = {layer_divergence_scaffold}")
    print(f"integral of dJ/dy across layer = {integral_flux_derivative}")
    print("Interpretation:")
    print("  signed-distance support can localize a layer-flux scaffold")
    print("  but support/local divergence scaffold is not physical D_layer legitimacy")

    with out.derived_results():
        out.line("window endpoints", StatusMark.PASS, str(endpoint_data))
        out.line("layer divergence scaffold", StatusMark.PASS, str(layer_divergence_scaffold))
        out.line("integrated derivative", StatusMark.PASS, str(integral_flux_derivative))
    with out.governance_assessments():
        out.line("scaffold", StatusMark.INFO, "signed-distance layer scaffold retained only as theorem target input")
        out.line("legitimacy", StatusMark.OBLIGATION, "scaffold does not derive physical/covariant D_layer")
    with out.counterexamples():
        out.line("support as theorem", StatusMark.FAIL, "endpoint locality is not D_layer legitimacy")
        out.line("old diagnostic promotion", StatusMark.FAIL, "window-like diagnostics cannot be promoted to physical D_layer")
    with out.unresolved_obligations():
        out.line("geometric flux origin", StatusMark.OBLIGATION, "derive layer flux and amplitude from boundary geometry")
        out.line("covariant lift", StatusMark.OBLIGATION, "replace signed-distance toy coordinate with covariant boundary/layer object")

    ns.record_derivation(derivation_id=MARKER_ID, inputs=[], output=layer_divergence_scaffold, method="construct signed-distance layer flux scaffold and derivative", status=Status.DERIVED, record_kind=RecordKind.COMPATIBILITY_EXAMPLE, result_type="signed_distance_layer_scaffold", scope="scaffold only; not D_layer theorem")
    record_claim(ns, MARKER_ID, "g73_signed_c1", GovernanceStatus.POLICY_RULE, "Signed-distance layer scaffold is not physical D_layer legitimacy by itself.")
    record_claim(ns, MARKER_ID, "g73_signed_c2", GovernanceStatus.REJECTED_ROUTE, "Endpoint locality and diagnostic window shapes cannot be promoted to physical D_layer.")
    record_obligation(ns, "g73_signed_o1", "Derive layer flux/amplitude from covariant boundary geometry.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_boundary_measure_origin_test.py")


if __name__ == "__main__": main()
