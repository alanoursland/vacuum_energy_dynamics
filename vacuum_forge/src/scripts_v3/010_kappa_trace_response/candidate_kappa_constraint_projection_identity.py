# Group:
#   10_kappa_trace_response
#
# Script type:
#   DERIVATION
#
# Candidate kappa constraint projection identity
#
# Purpose
# -------
# The gauge-vs-physical trace study found the current best interpretation:
#
#   kappa = constrained non-propagating trace response
#
# This can reconcile:
#
#   interior trace response,
#   exterior kappa = 0,
#   compensated zero-charge source,
#   scalar-radiation safety.
#
# But the missing piece is:
#
#   a parent projection identity.
#
# This script tries to formalize a zero-charge projection for kappa:
#
#   S_kappa = P_0 S_trace
#
# where P_0 removes the monopole/support-average charge:
#
#   P_0 S = S - <S>_support
#
# so that:
#
#   integral_support S_kappa d^3x = 0.
#
# This is not yet a derivation from a covariant parent theory.
# It is a formal constraint identity candidate.

from pathlib import Path

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


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="kappa_gauge_vs_physical_trace_marker",
        upstream_script_id="010_kappa_trace_response__candidate_kappa_gauge_vs_physical_trace",
        upstream_derivation_id="kappa_gauge_vs_physical_trace_marker",
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


def case_0_problem_statement():
    header("Case 0: Kappa constraint projection identity problem")

    print("Question:")
    print()
    print("  Can the compensated kappa source be written as a projection identity")
    print("  rather than an arbitrary subtraction?")
    print()
    print("Candidate projection:")
    print()
    print("  P_0 S = S - <S>_support")
    print()
    print("Required identity:")
    print()
    print("  integral_support P_0 S d^3x = 0")


def case_1_define_projection_operator():
    header("Case 1: Define zero-charge projection operator")

    print("For a compact support region V:")
    print()
    print("  <S>_V = (1/V) integral_V S d^3x")
    print()
    print("Define:")
    print()
    print("  P_0 S = S - <S>_V")
    print()
    print("Then:")
    print()
    print("  integral_V P_0 S d^3x = 0")
    print()
    print("This removes monopole kappa charge over the support.")


def case_2_toy_profile_projection():
    header("Case 2: Toy pressure profile projection")

    r, R, p0 = sp.symbols("r R p0", positive=True, real=True)

    S = 3*p0*(1 - r**2/R**2)
    V = 4*sp.pi*R**3/3
    Q = sp.simplify(4*sp.pi*sp.integrate(r**2*S, (r, 0, R)))
    S_avg = sp.simplify(Q/V)
    P0S = sp.simplify(S - S_avg)
    Q_projected = sp.simplify(4*sp.pi*sp.integrate(r**2*P0S, (r, 0, R)))

    print("Raw source:")
    print()
    print(f"S = {S}")
    print()
    print("Average over support:")
    print()
    print(f"<S> = {S_avg}")
    print()
    print("Projected source:")
    print()
    print(f"P_0 S = {P0S}")
    print()
    print("Projected charge:")
    print()
    print(f"integral P_0 S d^3x = {Q_projected}")

    return r, R, S, S_avg, P0S, Q_projected


def case_3_projector_idempotence():
    header("Case 3: Projection idempotence")

    print("A true projection should satisfy:")
    print()
    print("  P_0(P_0 S) = P_0 S")
    print()
    print("Reason:")
    print("  once the support-average is removed, applying the same operation again")
    print("  changes nothing.")
    print()
    print("For compact support with fixed V:")
    print()
    print("  <P_0 S> = 0")
    print("  P_0(P_0 S) = P_0 S - <P_0 S> = P_0 S")
    print()
    print("Thus P_0 is idempotent if the support region is fixed.")


def case_4_exterior_tail_control():
    header("Case 4: Exterior tail control")

    alpha_k, K_k, Q_projected, r = sp.symbols("alpha_k K_k Q_projected r", positive=True, real=True)

    tail = alpha_k * Q_projected / (4*sp.pi*K_k*r)

    print("Massless exterior monopole tail:")
    print()
    print("  kappa_ext ~ alpha_k Q_projected/(4*pi K_k r)")
    print()
    print(f"kappa_ext = {tail}")
    print()
    print("If the projection identity enforces:")
    print()
    print("  Q_projected = 0")
    print()
    print("then the exterior monopole tail is removed.")


def case_5_constraint_not_local_law():
    header("Case 5: Constraint, not ordinary local law")

    print("The projection:")
    print()
    print("  P_0 S = S - <S>_V")
    print()
    print("is nonlocal over V.")
    print()
    print("Therefore it should be interpreted as:")
    print()
    print("  a constraint projection")
    print("  or a boundary/matching identity")
    print("  or a consequence of a parent conservation law")
    print()
    print("not as:")
    print()
    print("  an ordinary local scalar source")
    print()
    print("This supports kappa as constrained/non-propagating trace response.")


def case_6_possible_parent_forms():
    header("Case 6: Possible parent identity forms")

    print("Possible parent forms to investigate:")
    print()
    print("1. Zero exterior kappa charge:")
    print("   Q_kappa = integral_V S_kappa d^3x = 0")
    print()
    print("2. Trace balance constraint:")
    print("   accumulation of trace exchange is locally redistributed so net exterior")
    print("   scalar charge vanishes.")
    print()
    print("3. Boundary flux cancellation:")
    print("   F_kappa(R+) = 4*pi R^2 kappa'(R+) = 0")
    print()
    print("4. Projected source equation:")
    print("   L_kappa kappa = alpha_k P_0 S_trace")
    print()
    print("5. Gauge/constraint split:")
    print("   kappa = kappa_phys_constrained + kappa_gauge")
    print()
    print("None is derived yet.")


def case_7_schematic_projected_equation():
    header("Case 7: Schematic projected kappa equation")

    print("Candidate constrained equation:")
    print()
    print("  -K_k Delta kappa = alpha_k P_0 S_trace")
    print()
    print("with:")
    print()
    print("  integral P_0 S_trace d^3x = 0")
    print()
    print("Exterior condition:")
    print()
    print("  kappa_ext monopole = 0")
    print()
    print("If additionally boundary/higher multipoles vanish or are confined:")
    print()
    print("  kappa_ext = 0")
    print()
    print("Status:")
    print("  structural candidate only")


def case_8_failure_controls():
    header("Case 8: Failure controls")

    print("The projection identity fails if:")
    print()
    print("1. support V is arbitrary or observer-dependent.")
    print("2. subtraction is inserted only to kill an unwanted tail.")
    print("3. higher multipoles leak into exterior.")
    print("4. projection violates local energy/source accounting.")
    print("5. no parent identity enforces Q_kappa = 0.")
    print("6. kappa remains gauge-only but is treated as physical.")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_scalar_radiation_leak_check.py")
    print("   Check whether projected kappa remains non-radiative dynamically.")
    print()
    print("2. candidate_kappa_boundary_flux_cancellation.py")
    print("   Test exterior flux cancellation at the matter boundary.")
    print()
    print("3. candidate_kappa_projection_parent_balance.py")
    print("   Try to connect P_0 to vacuum-substance continuity balance.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_scalar_radiation_leak_check.py")
    print()
    print("Reason:")
    print("  Projection removes monopole leakage, but scalar radiation safety is still")
    print("  the next hard dynamical check.")


def final_interpretation():
    header("Final interpretation")

    print("The zero-charge projection:")
    print()
    print("  P_0 S = S - <S>")
    print()
    print("works algebraically:")
    print()
    print("  integral P_0 S d^3x = 0")
    print()
    print("and removes the massless exterior monopole tail.")
    print()
    print("But it is nonlocal over the support and must be interpreted as a")
    print("constraint/projection identity, not an ordinary local source law.")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_constraint_projection_identity.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_scalar_radiation_leak_check.py")


def main():
    header("Candidate Kappa Constraint Projection Identity")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    case_1_define_projection_operator()
    r, R, S, S_avg, P0S, Q_projected = case_2_toy_profile_projection()
    case_3_projector_idempotence()
    case_4_exterior_tail_control()
    case_5_constraint_not_local_law()
    case_6_possible_parent_forms()
    case_7_schematic_projected_equation()
    case_8_failure_controls()
    case_9_next_tests()
    final_interpretation()

    # Real algebraic computation: projection has zero charge
    ns.record_derivation(
        derivation_id="zero_charge_projection_identity_sample",
        inputs=[S, S_avg, P0S],
        output=Q_projected,
        method="integrate 4*pi*r^2*(S - <S>) over [0,R]; verify integral = 0",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="parabolic pressure profile; fixed compact support; parent identity not derived",
    )

    # Idempotence is a real identity (structural)
    ns.record_derivation(
        derivation_id="zero_charge_projector_idempotence",
        inputs=[],
        output=sp.Symbol("P0_idempotent_for_fixed_support"),
        method="algebraic: <P_0 S>=0 implies P_0(P_0 S)=P_0 S for fixed V",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
    )

    ns.record_derivation(
        derivation_id="kappa_constraint_projection_identity_marker",
        inputs=[],
        output=sp.Symbol("kappa_constraint_projection_identity_stated"),
        method="kappa_constraint_projection_identity_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_covariant_parent_identity_for_P0_in_10_kappa_trace",
        script_id=SCRIPT_ID,
        title="Derive a covariant parent identity from which the zero-charge projection P_0 follows",
        status=ObligationStatus.OPEN,
        description=(
            "The projection P_0 S = S - <S>_V removes monopole kappa charge algebraically "
            "and is idempotent for fixed support. But it is nonlocal over V and not "
            "derived from a covariant parent theory. A conservation law, matching identity, "
            "or constraint equation must be derived to license it as a physical source law."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="zero_charge_projection_is_constraint_not_local_law",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "The zero-charge projection P_0 is structurally idempotent for fixed compact "
            "support and removes monopole kappa leakage. It is best interpreted as a "
            "constraint projection rather than an ordinary local source law."
        ),
    ))

    with out.derived_results():
        out.line("zero-charge projection integral vanishes (toy profile)", StatusMark.PASS, "sample result")
        out.line("projector idempotence for fixed support", StatusMark.PASS, "algebraic identity")

    with out.governance_assessments():
        out.line("covariant parent identity for P_0", StatusMark.FAIL, "missing")
        out.line("projection as local source law", StatusMark.FAIL, "not licensed - nonlocal")

    with out.unresolved_obligations():
        out.line("derive covariant parent identity for P_0", StatusMark.OBLIGATION, "open")

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
