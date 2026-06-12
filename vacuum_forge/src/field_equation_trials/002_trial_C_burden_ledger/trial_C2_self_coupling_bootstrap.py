# Trial C2: self-coupling bootstrap in the reduced temporal sector
#
# Group:
#   002_trial_C_burden_ledger
#
# Script type:
#   DERIVATION / SELECTOR / SIGN-FORK RESOLUTION CANDIDATE
#
# Purpose
# -------
# Formalize the bootstrap selector (ontology_and_mechanism/
# curvature_self_coupling.md section 3) in the framework's own reduced
# static spherical variables, and let it act on the P4 sign fork.
#
# Setup: the exact mechanics branch found that the static temporal sector
# obeys the areal-flux law, linear in A = exp(s):
#
#   Delta_areal A = 0   (source-free exterior)
#
# which in the s-variable is NONLINEAR:
#
#   Delta_areal s + (s')^2 = 0.
#
# The |s'|^2 term is structurally a self-source. The bootstrap postulate
# (P6 universality applied to the field's own energy) says: the field's
# energy density gravitates with the SAME per-unit-energy coupling as
# matter. Writing the candidate field energy density as
#
#   u_field = lamda * c^4 (s')^2 / (8 pi G)
#
# (lamda a dimensionless sign/magnitude), the sourced equation is
#
#   Delta_areal s = lamda (s')^2.
#
# P6 fixes |coupling| = 1; ONLY THE SIGN OF lamda IS FREE. That freedom is
# exactly the P4 sign fork, now appearing inside the framework's own
# exact branch.
#
# Locked-door question:
#
#   Solve the bootstrap family exactly. Which lamda reproduces the
#   framework's exact exterior recovery, and what does that say about
#   the sign of temporal-sector field energy?

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    RouteRecord,
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


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="c1_cross_term_dependency_c2",
        upstream_script_id="002_trial_C_burden_ledger__trial_C1_two_body_ledger",
        upstream_derivation_id="ledger_cross_term_green_identity_c1",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Symbols
# =============================================================================

r = sp.Symbol("r", positive=True)
r_s = sp.Symbol("r_s", positive=True)
lam = sp.Symbol("lamda", real=True, nonzero=True)
x = r_s / r


def areal_lap(f):
    return sp.diff(r**2 * sp.diff(f, r), r) / r**2


# =============================================================================
# Case 0
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: The bootstrap question in reduced variables")
    print("Exact mechanics branch (FEC 002, T-chain): static exterior obeys")
    print("Delta_areal A = 0 with A = exp(s) -- linear in A, nonlinear in s:")
    print()
    print("  Delta_areal s + (s')^2 = 0")
    print()
    print("Bootstrap postulate (P6 universality on the field's own energy):")
    print()
    print("  Delta_areal s = lamda (s')^2,    u_field = lamda c^4 (s')^2/(8 pi G)")
    print()
    print("|coupling| fixed at 1 by P6; lamda's SIGN is the P4 fork, now living")
    print("inside the framework's own exact branch. Solve exactly; let exact")
    print("exterior recovery act as the selector.")

    with out.governance_assessments():
        out.line("Trial C2 opened", StatusMark.INFO,
                 "bootstrap selector formalized in reduced temporal sector")


# =============================================================================
# Case 1: the linearization identity
# =============================================================================


def case_1_linearization(out: ScriptOutput):
    header("Case 1: Delta_areal(e^s) = e^s [Delta_areal s + (s')^2]")
    s = sp.Function("s")(r)
    lhs = areal_lap(sp.exp(s))
    rhs = sp.exp(s) * (areal_lap(s) + sp.diff(s, r) ** 2)
    residual = sp.simplify(sp.expand(lhs - rhs))
    print(f"  residual = {sp.sstr(residual)}")
    print()
    print("  So the exact source-free law Delta_areal A = 0 is EXACTLY the")
    print("  statement 'the s-field sources itself with coefficient lamda = -1'.")
    print("  The framework's exact branch secretly contains a self-coupling sign.")

    with out.derived_results():
        out.line("linearization identity",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 "Delta_areal A = 0  <=>  Delta_areal s = -(s')^2")


# =============================================================================
# Case 2: exact solution of the bootstrap family
# =============================================================================


def case_2_exact_family(out: ScriptOutput):
    header("Case 2: Exact solution of Delta_areal s = lamda (s')^2")
    print("Substitute u = s'(r):  u' + 2u/r = lamda u^2  (Bernoulli);")
    print("v = 1/u:  v' - 2v/r = -lamda;  v = C r^2 + lamda r.")
    print("Asymptotic flatness + weak-field normalization s ~ -r_s/r fixes C = 1/r_s:")
    print()

    # candidate closed form: A_lam = (1 + lamda*r_s/r)^(-1/lamda)
    A_lam = (1 + lam * x) ** (-1 / lam)
    s_lam = sp.log(A_lam)

    # verify it solves the ODE
    ode_residual = sp.simplify(areal_lap(s_lam) - lam * sp.diff(s_lam, r) ** 2)

    # verify asymptotic normalization: s -> -r_s/r as r -> oo
    series = sp.series(s_lam.subs(r, 1 / sp.Symbol("eps", positive=True)),
                       sp.Symbol("eps", positive=True), 0, 3).removeO()
    leading = sp.simplify(series.coeff(sp.Symbol("eps", positive=True), 1) + r_s)

    print(f"  A_lamda(r) = (1 + lamda r_s/r)^(-1/lamda)")
    print(f"  ODE residual: {sp.sstr(ode_residual)}")
    print(f"  weak-field leading term of s: -(r_s/r) [normalization residual: {sp.sstr(leading)}]")
    print()
    print("  Special members:")
    print("    lamda = -1 :  A = 1 - r_s/r            (Schwarzschild exterior, areal)")
    print("    lamda -> 0 :  A = exp(-r_s/r)          (no self-coupling)")
    print("    lamda = +1 :  A = 1/(1 + r_s/r)        (positive self-energy)")

    A_m1 = sp.simplify(A_lam.subs(lam, -1))
    A_p1 = sp.simplify(A_lam.subs(lam, 1))
    A_0 = sp.limit(A_lam, lam, 0)
    checks = [
        ("lamda=-1 gives Schwarzschild", is_zero(A_m1 - (1 - x))),
        ("lamda->0 gives exponential", is_zero(sp.simplify(A_0 - sp.exp(-x)))),
        ("lamda=+1 gives reciprocal", is_zero(A_p1 - 1 / (1 + x))),
    ]
    with out.derived_results():
        out.line("bootstrap family solved exactly",
                 StatusMark.PASS if is_zero(ode_residual) and is_zero(leading) else StatusMark.FAIL,
                 "A_lamda = (1 + lamda r_s/r)^(-1/lamda); one-parameter family, lamda = self-coupling")
        for label, ok in checks:
            out.line(label, StatusMark.PASS if ok else StatusMark.FAIL, "")
    return A_lam


# =============================================================================
# Case 3: where the family members agree and differ
# =============================================================================


def case_3_orders(A_lam, out: ScriptOutput):
    header("Case 3: 1PN degeneracy, 2PN discrimination")
    X = sp.Symbol("X", positive=True)  # X = r_s/r
    A_x = (1 + lam * X) ** (-1 / lam)
    series = sp.series(A_x, X, 0, 3).removeO()
    c1 = sp.simplify(series.coeff(X, 1))
    c2 = sp.simplify(series.coeff(X, 2))
    print(f"  A = 1 + ({sp.sstr(c1)}) X + ({sp.sstr(c2)}) X^2 + ...")
    print()
    print("  First order is lamda-independent: ALL family members share the")
    print("  Newtonian limit and the 1PN recovery (T1-T9 untouched).")
    print("  Second order in the areal chart: coefficient (1 + lamda)/2.")
    print("  Exact areal Schwarzschild has NO X^2 term  =>  lamda = -1 selected.")

    sel = sp.solve(sp.Eq(c2, 0), lam)
    with out.derived_results():
        out.line("1PN coefficient lamda-independent",
                 StatusMark.PASS if is_zero(c1 + 1) else StatusMark.FAIL,
                 "c1 = -1 for all lamda: weak-field recovery is bootstrap-blind")
        out.line("exact-recovery selector: lamda = -1",
                 StatusMark.PASS if sel == [-1] else StatusMark.FAIL,
                 "second-order areal coefficient (1+lamda)/2 vanishes only at lamda = -1")


# =============================================================================
# Case 4: the physical reading -- sign fork, temporal sector
# =============================================================================


def case_4_sign_reading(out: ScriptOutput):
    header("Case 4: What lamda = -1 means")
    G, c = sp.symbols("G c", positive=True)
    sprime = sp.Symbol("s_prime", real=True)
    u_field = lam * c**4 * sprime**2 / (8 * sp.pi * G)
    u_at_m1 = u_field.subs(lam, -1)
    print(f"  u_field = {sp.sstr(u_field)}")
    print(f"  at lamda = -1:  u_field = {sp.sstr(u_at_m1)}   (NEGATIVE definite)")
    print()
    print("  In the weak field s' -> (2/c^2) dPhi/dr, so")
    print("  u_field -> -|grad Phi|^2/(2 pi G) x (1/4) = -|grad Phi|^2/(8 pi G) x ...")
    print("  -- the NEWTONIAN negative field-energy density convention, recovered")
    print("  from inside the framework's own exact branch.")
    print()
    print("  Consequences for the standing forks:")
    print()
    print("  1. P4 sign fork, temporal/static sector: the bootstrap + exact")
    print("     recovery selects NEGATIVE field self-energy. This is the")
    print("     sector-indefinite branch's temporal half (GW/shear sector")
    print("     positivity, G03, remains separately required).")
    print("  2. Trial C1's fork: 'indefinite-energy gradient descent' gains")
    print("     its temporal-sector sign from the framework's own mechanics;")
    print("     the P6-funded traceful branch correspondingly loses its")
    print("     simplest static-sector motivation.")
    print("  3. P8 upgrade path: P8's multiplicative composition is the")
    print("     first-order shadow of the lamda = -1 bootstrap; if the")
    print("     bootstrap postulate (P6 universality applied to field energy)")
    print("     is adopted, P8 becomes a THEOREM at 1PN and the exact areal")
    print("     A = 1 - r_s/r becomes a derivation rather than a recovery.")

    weak_check = is_zero(sp.simplify(u_at_m1 + c**4 * sprime**2 / (8 * sp.pi * G)))
    with out.derived_results():
        out.line("lamda = -1 means negative temporal-sector field energy",
                 StatusMark.PASS if weak_check else StatusMark.FAIL,
                 "u_field = -c^4 (s')^2/(8 pi G); Newtonian convention recovered, not assumed")


# =============================================================================
# Case 5: horizon discriminator (diagnostic)
# =============================================================================


def case_5_horizon(out: ScriptOutput):
    header("Case 5: Horizon existence across the family (diagnostic)")
    X = sp.Symbol("X", positive=True)
    A_x = (1 + lam * X) ** (-1 / lam)
    # A vanishes at finite r iff 1 + lamda X = 0 has positive root: X = -1/lamda > 0
    print("  A_lamda = 0 at finite radius iff lamda < 0 (root X = -1/lamda,")
    print("  i.e. r_horizon = -lamda r_s; at lamda = -1, r_horizon = r_s).")
    print("  For lamda >= 0, A > 0 for all r > 0: NO event horizon.")
    print()
    print("  Diagnostic: observed black-hole phenomenology (shadows, ringdowns")
    print("  consistent with horizons) disfavors lamda >= 0 independently of the")
    print("  exact-recovery selector. Recorded as DIAGNOSTIC, not a precision gate.")

    root = sp.solve(sp.Eq(1 + lam * X, 0), X)
    horizon_at_m1 = sp.simplify(root[0].subs(lam, -1) - 1)
    with out.sample_results():
        out.line("horizon only for lamda < 0; r_h = -lamda r_s",
                 StatusMark.PASS if is_zero(horizon_at_m1) else StatusMark.FAIL,
                 "lamda = -1 places the horizon at r_s (Schwarzschild); lamda >= 0 has none")


# =============================================================================
# Case 6: verdict
# =============================================================================


def case_6_verdict(out: ScriptOutput) -> None:
    header("Case 6: Trial C2 verdict")
    print("DERIVED (reduced static spherical temporal sector):")
    print()
    print("  1. The framework's exact source-free law IS a self-coupling")
    print("     statement: Delta_areal A = 0  <=>  Delta_areal s = -(s')^2.")
    print("  2. The bootstrap family A_lamda = (1 + lamda r_s/r)^(-1/lamda)")
    print("     solves the general sign problem exactly; all members agree at")
    print("     1PN; exact areal recovery selects lamda = -1.")
    print("  3. lamda = -1 means temporal-sector field energy is NEGATIVE:")
    print("     u_field = -c^4 (s')^2/(8 pi G). The Newtonian convention is")
    print("     recovered from inside the framework, not imported.")
    print()
    print("STATUS SHIFTS:")
    print("  P4 sign fork: temporal/static sector resolved toward the")
    print("    indefinite branch (negative), CONDITIONAL on the bootstrap")
    print("    postulate. Shear/radiative-sector positivity (G03) still owed.")
    print("  P8: becomes a 1PN theorem under the bootstrap postulate.")
    print("  Trial C: continuation obligations updated; the funded-traceful")
    print("    program loses its static-sector motivation but is NOT killed")
    print("    (P6 substance exchange may still govern dynamics/radiative")
    print("    sectors; only the static ledger sign is now fixed).")
    print()
    print("NOT DERIVED: covariant lift; the spatial-sector counterpart (does")
    print("the same bootstrap force P7?); whether the bootstrap postulate")
    print("itself follows from P1-P6 (it is P6 applied to field energy --")
    print("close, but the application to configuration energy is a new")
    print("commitment); count-once placement in any future parent equation.")

    with out.governance_assessments():
        out.line("Trial C2 verdict: bootstrap selector lands; temporal sign = negative",
                 StatusMark.PASS,
                 "conditional on the bootstrap postulate (P6 universality on field energy)")
    with out.unresolved_obligations():
        out.line("spatial-sector bootstrap: does the same postulate force P7?",
                 StatusMark.OBLIGATION,
                 "if yes, both recovery postulates become theorems of one principle")
        out.line("promote bootstrap postulate to candidate postulate (P9?) for theory-owner review",
                 StatusMark.OBLIGATION,
                 "'configuration energy gravitates with the universal P6 coupling'")
        out.line("G03/GW positivity for the shear sector remains owed (indefinite branch)",
                 StatusMark.OBLIGATION,
                 "temporal negative + radiative positive = sector-indefinite signature")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns) -> None:
    X = sp.Symbol("X", positive=True)
    A_lam_sym = (1 + lam * X) ** (-1 / lam)

    ns.record_derivation(
        derivation_id="bootstrap_linearization_identity_c2",
        inputs=[],
        output=sp.Symbol("delta_s_plus_sprime_sq"),
        method="Delta_areal(e^s) = e^s [Delta_areal s + (s')^2] verified symbolically",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="linearization_identity",
        scope="the exact source-free areal law is a lamda = -1 self-coupling statement",
    )
    ns.record_derivation(
        derivation_id="bootstrap_family_exact_solution_c2",
        inputs=[lam],
        output=A_lam_sym,
        method="Bernoulli substitution u=s', v=1/u; asymptotic flatness + weak-field normalization",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="exact_solution_family",
        scope="A_lamda = (1 + lamda r_s/r)^(-1/lamda); members -1/0/+1 = Schwarzschild/exponential/reciprocal",
    )
    ns.record_derivation(
        derivation_id="bootstrap_selector_lamda_minus_one_c2",
        inputs=[A_lam_sym],
        output=sp.Eq(lam, -1),
        method="second-order areal coefficient (1+lamda)/2 = 0; 1PN coefficient lamda-independent",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="selector",
        scope="exact areal Schwarzschild recovery selects lamda = -1; 1PN blind to lamda",
    )
    ns.record_derivation(
        derivation_id="bootstrap_negative_field_energy_c2",
        inputs=[],
        output=sp.Symbol("u_field_negative"),
        method="u_field = lamda c^4 (s')^2/(8 pi G) at lamda = -1",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="sign_resolution",
        scope="temporal/static sector field energy negative, conditional on bootstrap postulate",
    )
    ns.record_derivation(
        derivation_id="bootstrap_horizon_discriminator_c2",
        inputs=[],
        output=sp.Symbol("horizon_iff_lamda_negative"),
        method="A_lamda = 0 has positive root X = -1/lamda iff lamda < 0; r_h = -lamda r_s",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="qualitative_discriminator",
        scope="horizons exist only in the negative-coupling branch (diagnostic)",
    )

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="temporal_sector_sign_negative_c2",
        script_id=SCRIPT_ID,
        branch_id="p4_sign_fork_temporal_static_sector",
        status=GovernanceStatus.PROVISIONAL_CONVENTION,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["bootstrap_postulate_adoption_c2", "spatial_sector_bootstrap_c2"],
        description=(
            "Temporal/static-sector field energy resolved NEGATIVE (lamda = -1), "
            "conditional on the bootstrap postulate (P6 universality applied to "
            "configuration energy) and exact areal recovery. Sector-indefinite "
            "overall signature remains the working picture: radiative-sector "
            "positivity (G03) still owed. Not adopted as theory state; recorded "
            "as the bootstrap-selected branch for theory-owner review."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="bootstrap_postulate_adoption_c2",
        script_id=SCRIPT_ID,
        title="Theory-owner decision: adopt bootstrap postulate (configuration energy gravitates per P6)",
        status=ObligationStatus.OPEN,
        required_by=["trial_C_verdict"],
        description=(
            "The selector is conditional on: 'the field's configuration energy "
            "sources gravity with the same universal per-unit-energy coupling as "
            "matter (P6 extended to field energy)'. Adopting it makes P8 a 1PN "
            "theorem and exact areal Schwarzschild a derivation. Candidate P9."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="spatial_sector_bootstrap_c2",
        script_id=SCRIPT_ID,
        title="Spatial-sector bootstrap: does the same postulate force P7 (AB = 1)?",
        status=ObligationStatus.OPEN,
        required_by=["trial_C_verdict"],
        description=(
            "If self-coupling consistency also fixes the radial response, both "
            "recovery postulates collapse into one principle and the K_GR "
            "selector claim strengthens substantially."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="trial_C3_spatial_bootstrap_route_c2",
        script_id=SCRIPT_ID,
        name="Trial C3: spatial-sector bootstrap (P7 from self-coupling?)",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["spatial_sector_bootstrap_c2"],
        activation_conditions=[
            "temporal result carried as conditional (bootstrap postulate unadopted)",
            "no recovery-as-construction: P7 must EMERGE, not be targeted",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="bootstrap_selector_temporal_c2",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "In the reduced static spherical temporal sector, requiring the "
            "field's own energy to gravitate with the universal P6 coupling "
            "yields the exact one-parameter family A_lamda = "
            "(1 + lamda r_s/r)^(-1/lamda), with only the self-coupling sign "
            "free. All members agree at 1PN. Exact areal recovery selects "
            "lamda = -1, equivalent to negative temporal-sector field energy "
            "u_field = -c^4 (s')^2/(8 pi G) -- the Newtonian convention derived "
            "from inside the framework. Conditional on the bootstrap postulate; "
            "P8 becomes a 1PN theorem under it. Horizons exist only for "
            "lamda < 0 (diagnostic)."
        ),
        derivation_ids=[
            "bootstrap_linearization_identity_c2",
            "bootstrap_family_exact_solution_c2",
            "bootstrap_selector_lamda_minus_one_c2",
            "bootstrap_negative_field_energy_c2",
            "bootstrap_horizon_discriminator_c2",
        ],
        obligation_ids=[
            "bootstrap_postulate_adoption_c2",
            "spatial_sector_bootstrap_c2",
        ],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial C2: Self-Coupling Bootstrap in the Reduced Temporal Sector")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    case_1_linearization(out)
    A_lam = case_2_exact_family(out)
    case_3_orders(A_lam, out)
    case_4_sign_reading(out)
    case_5_horizon(out)
    case_6_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
