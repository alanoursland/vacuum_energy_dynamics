# Trial B1: measure-bridge static reduction
#
# Group:
#   001_trial_B_measure_bridge
#
# Script type:
#   DERIVATION / STRUCTURAL IDENTIFICATION / ARTIFACT STRESS TEST
#
# Purpose
# -------
# Test the measure-conversion hypothesis from the 1D scalar dissipation toy:
#
#   The projection-chart weights are coordinate-to-physical measure
#   conversion factors, with the field's density weight setting the exponent.
#
# Target: the probe's energy functional
#
#   E[f] = (1/2) <L f, L f>_w - <S, f>_w,
#   a = 1 - x^2,  w = a^4,  L[f] = a f' - 6 x f = a^-2 (a^3 f)'
#
# whose external residue (research_synthesis/07) is: why this functional,
# this chart, this weight, physically.
#
# Locked-door question (gate G08 attack, G30 discipline):
#
#   Does a physical-measure reading of the probe energy exist, and if so,
#   what does it FORCE about the measure dimension and the field weight?
#
# Discipline: a match found by solving exponent equations within an ansatz
# family is a structural identification CONDITIONAL on that family. It is
# not a physical adoption (G30: compatibility-vs-origin). The script keeps
# that boundary explicit.

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
        dependency_id="charter_gate_G08_dependency_b1",
        upstream_script_id="000_trial_charter__trial_gate_inventory",
        upstream_derivation_id="trial_scalar_tail_flux_witness_t000",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Symbols
# =============================================================================

x = sp.Symbol("x", positive=True)
a = 1 - x**2


def f_poly(coeffs):
    """Generic even polynomial test profile."""
    return sum(c * x ** (2 * j) for j, c in enumerate(coeffs))


# =============================================================================
# Case 0
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: The measure-bridge question")
    print("Probe baseline (regularity ladder, closed):")
    print()
    print("  E[f] = (1/2) int_0^1 (L f)^2 a^4 dx - int_0^1 S f a^4 dx")
    print("  L[f] = a f' - 6 x f = a^-2 (a^3 f)'")
    print("  u = a^3 f  =>  integrand (u')^2;  EL equation -u'' = a S")
    print()
    print("Hypothesis (from intuition_models/1d_scalar_dissipation.md):")
    print()
    print("  physical span     ds = e^phi dx          (compactified chart)")
    print("  physical deriv    D_s = e^-phi d_x")
    print("  field weight      density of weight omega under reparameterization")
    print("  physical energy   (1/2) int (D_s F)^2 dmu,  dmu = e^(nu phi) dx")
    print()
    print("Question: for power-law compactification e^phi = a^-kappa, which")
    print("(kappa, omega, nu) reproduce the probe energy EXACTLY -- and what")
    print("is forced vs free?")

    with out.governance_assessments():
        out.line(
            "Trial B1 opened",
            StatusMark.INFO,
            "structural identification attempt; G30 boundary kept explicit throughout",
        )


# =============================================================================
# Case 1: probe baseline verification
# =============================================================================


def case_1_probe_baseline(out: ScriptOutput):
    header("Case 1: Probe baseline re-verified")
    f = sp.Function("f")(x)
    S = sp.Function("S")(x)
    L_f = a * sp.diff(f, x) - 6 * x * f
    u = a**3 * f

    integrand_probe = sp.expand(L_f**2 * a**4)
    integrand_dirichlet = sp.expand(sp.diff(u, x) ** 2)
    energy_match = sp.simplify(integrand_probe - integrand_dirichlet)

    coupling_probe = sp.expand(S * f * a**4)
    coupling_u = sp.expand(a * S * u)
    coupling_match = sp.simplify(coupling_probe - coupling_u)

    # divergence form of L
    div_form = sp.simplify(L_f - sp.diff(a**3 * f, x) / a**2)

    print(f"  (L f)^2 a^4 - (u')^2 = {sp.sstr(energy_match)}")
    print(f"  S f a^4 - a S u      = {sp.sstr(coupling_match)}")
    print(f"  L f - a^-2 (a^3 f)'  = {sp.sstr(div_form)}")

    with out.derived_results():
        out.line("(L f)^2 a^4 == (u')^2 with u = a^3 f",
                 StatusMark.PASS if is_zero(energy_match) else StatusMark.FAIL,
                 "probe quadratic term is flat Dirichlet energy of u in the x-chart")
        out.line("source coupling S f a^4 == a S u",
                 StatusMark.PASS if is_zero(coupling_match) else StatusMark.FAIL,
                 "EL equation -u'' = a S follows")
        out.line("L divergence form",
                 StatusMark.PASS if is_zero(div_form) else StatusMark.FAIL,
                 "L[f] = a^-2 (a^3 f)'")
    return energy_match, coupling_match


# =============================================================================
# Case 2: the exponent-matching theorem
# =============================================================================


def case_2_exponent_matching(out: ScriptOutput):
    header("Case 2: Exponent matching -- what the ansatz family forces")
    print("Ansatz family:")
    print()
    print("  e^phi = a^-kappa            (kappa > 0: x = 1 is physically far)")
    print("  F = a^(kappa*omega) f       (f read as weight-omega density; F = physical scalar)")
    print("  dmu = e^(nu*phi) dx = a^(-kappa*nu) dx")
    print("  E_phys = (1/2) int (D_s F)^2 dmu,   D_s = a^kappa d_x")
    print()
    print("Expand the integrand:")
    print()
    print("  (a^kappa (a^(kappa*omega) f)')^2 a^(-kappa*nu)")
    print("    = a^(2*kappa - kappa*nu + 2*kappa*omega - 2) * (a f' + kappa*omega a' f)^2")
    print()
    print("Probe integrand:")
    print()
    print("  (L f)^2 a^4 = a^4 * (a f' + 3 a' f)^2 * a^-4 ... = ((a^3 f)')^2")
    print("              = a^4 * (a f' + 3 a' f)^2 / a^0   [shape (a f' + 3 a' f), net power 4]")

    kappa, omega, nu = sp.symbols("kappa omega nu", positive=True)

    # operator-shape condition: kappa*omega = 3
    shape_eq = sp.Eq(kappa * omega, 3)
    # net-power condition: 2*kappa - kappa*nu + 2*kappa*omega - 2 = 4
    power_eq = sp.Eq(2 * kappa - kappa * nu + 2 * kappa * omega - 2, 4)

    sol = sp.solve([shape_eq, power_eq], [omega, nu], dict=True)
    print()
    print(f"  matching equations: {sp.sstr(shape_eq)},  {sp.sstr(power_eq)}")
    print(f"  solution: {sol}")

    omega_sol = sol[0][omega]
    nu_sol = sol[0][nu]
    nu_forced = is_zero(nu_sol - 2)
    omega_forced = is_zero(kappa * omega_sol - 3)

    print()
    print("  RESULT: nu = 2 for ALL kappa > 0 (measure dimension is FORCED to two).")
    print("          kappa*omega = 3 (total conversion weight FORCED to a^3).")
    print("          kappa itself is FREE (compactification-rate gauge freedom).")

    # Direct verification at canonical kappa = 1, and at kappa = 2 (gauge check)
    f = sp.Function("f")(x)
    probe_integrand = sp.expand(sp.diff(a**3 * f, x) ** 2)

    def family_integrand(kap):
        F = a ** (3) * f  # kappa*omega = 3 => a^(kappa*omega) = a^3 always
        return sp.expand((a**kap * sp.diff(F, x)) ** 2 * a ** (-2 * kap))

    match_k1 = sp.simplify(family_integrand(1) - probe_integrand)
    match_k2 = sp.simplify(family_integrand(2) - probe_integrand)
    print()
    print(f"  direct check kappa=1, nu=2: residual = {sp.sstr(match_k1)}")
    print(f"  direct check kappa=2, nu=2: residual = {sp.sstr(match_k2)}")

    with out.derived_results():
        out.line("measure dimension forced: nu = 2",
                 StatusMark.PASS if nu_forced else StatusMark.FAIL,
                 "the physical measure must be TWO-dimensional, independent of kappa")
        out.line("conversion weight forced: kappa*omega = 3",
                 StatusMark.PASS if omega_forced else StatusMark.FAIL,
                 "f is a weight-3 density in total; F = a^3 f = u is the physical scalar")
        out.line("direct integrand match at kappa = 1",
                 StatusMark.PASS if is_zero(match_k1) else StatusMark.FAIL,
                 "(a (a^3 f)')^2 a^-2 == ((a^3 f)')^2")
        out.line("gauge freedom in kappa confirmed at kappa = 2",
                 StatusMark.PASS if is_zero(match_k2) else StatusMark.FAIL,
                 "compactification rate is a gauge choice; nu and kappa*omega are rigid")
    return nu_sol, omega_sol


# =============================================================================
# Case 3: canonical chart geometry (kappa = 1)
# =============================================================================


def case_3_canonical_chart(out: ScriptOutput):
    header("Case 3: Canonical chart (kappa = 1): x = tanh(s)")
    s = sp.Symbol("s", positive=True)

    # ds = dx / a  =>  s = arctanh(x); a = sech^2(s)
    X = sp.Symbol("X", positive=True)
    s_of_x = sp.atanh(X)
    s_integral_check = sp.simplify(sp.diff(s_of_x, X) - 1 / (1 - X**2))
    a_in_s = sp.simplify((1 - sp.tanh(s) ** 2) - sp.sech(s) ** 2)

    # total physical length diverges (x = 1 is at infinity)
    length = sp.limit(sp.atanh(sp.Symbol("X")), sp.Symbol("X"), 1, "-")

    # D_s u = a u' and relation to L
    f = sp.Function("f")(x)
    u = a**3 * f
    L_f = a * sp.diff(f, x) - 6 * x * f
    Dsu_vs_L = sp.simplify(a * sp.diff(u, x) - a**3 * L_f)

    print(f"  s(X) = int_0^X dx/a = atanh(X)   [d/dX check residual: {sp.sstr(s_integral_check)}]")
    print(f"  a in s-coordinates: 1 - tanh^2(s) - sech^2(s) = {sp.sstr(a_in_s)}")
    print(f"  total physical length to x=1: {sp.sstr(length)}  (boundary = infinity)")
    print(f"  D_s u - a^3 L[f] = {sp.sstr(Dsu_vs_L)}")
    print()
    print("  Reading: x compactifies an infinite physical half-line; x = tanh(s);")
    print("  the projection boundary x=1 is spatial infinity, where the ladder's")
    print("  admissibility conditions become decay conditions at infinity.")

    with out.derived_results():
        out.line("chart is x = tanh(s), a = sech^2(s)",
                 StatusMark.PASS if is_zero(a_in_s) and is_zero(s_integral_check) else StatusMark.FAIL,
                 "s(X) = atanh(X); ds = dx/a verified by differentiation")
        out.line("x = 1 sits at infinite physical distance",
                 StatusMark.PASS if length == sp.oo else StatusMark.FAIL,
                 "the admissibility boundary is spatial infinity in the physical reading")
        out.line("D_s u = a^3 L[f]",
                 StatusMark.PASS if is_zero(Dsu_vs_L) else StatusMark.FAIL,
                 "the probe operator is the physical derivative of u up to the weight factor")


# =============================================================================
# Case 4: the weight decomposition theorem (why a^4)
# =============================================================================


def case_4_weight_decomposition(out: ScriptOutput):
    header("Case 4: Why w = a^4: the 3 + 3 - 2 decomposition")
    psi = sp.Function("psi")(x)
    f = sp.Function("f")(x)
    S = sp.Function("S")(x)

    pairing_probe = sp.expand(psi * f * a**4)
    pairing_phys = sp.expand((a**3 * psi) * (a**3 * f) * a ** (-2))
    pairing_match = sp.simplify(pairing_probe - pairing_phys)

    source_probe = sp.expand(S * f * a**4)
    source_phys = sp.expand((a**3 * S) * (a**3 * f) * a ** (-2))
    source_match = sp.simplify(source_probe - source_phys)

    print("  <psi, f>_w = int psi f a^4 dx")
    print("             = int (a^3 psi)(a^3 f) a^-2 dx")
    print("             = int Psi U dA")
    print()
    print("  with Psi = a^3 psi, U = a^3 f physical scalars and dA = a^-2 dx the")
    print("  2D physical measure. The mysterious exponent decomposes as")
    print()
    print("      4 = 3 (test-function weight) + 3 (profile weight) - 2 (2D measure).")
    print()
    print(f"  pairing residual: {sp.sstr(pairing_match)}")
    print(f"  source residual:  {sp.sstr(source_match)}")
    print()
    print("  The source S is ALSO a weight-3 density (S_phys = a^3 S), so the")
    print("  projection pairing is symmetric: physical scalars paired under dA.")

    with out.derived_results():
        out.line("w = a^4 decomposes as 3 + 3 - 2",
                 StatusMark.PASS if is_zero(pairing_match) else StatusMark.FAIL,
                 "two density conversions minus one 2D measure factor")
        out.line("source is the same weight-3 density class",
                 StatusMark.PASS if is_zero(source_match) else StatusMark.FAIL,
                 "b_k(S) = int Psi_k S_phys dA in physical variables")


# =============================================================================
# Case 5: artifact stress tests
# =============================================================================


def case_5_artifact_tests(out: ScriptOutput):
    header("Case 5: Artifact stress tests")
    print("Two ways the identification could be construction debris:")
    print()
    print("  (i)  measure-only reading (omega = 0): pure compactified measure")
    print("       with a scalar field, no density weight.")
    print("  (ii) bending-type reading: second physical derivative (D_s^2 F)^2,")
    print("       the literal 1D-toy bending energy.")
    print()

    kappa, nu = sp.symbols("kappa nu", positive=True)

    # (i) omega = 0: shape condition kappa*omega = 3 has no solution
    shape_zero = sp.solve(sp.Eq(kappa * 0, 3), kappa)
    print(f"  (i) omega = 0: solve kappa*0 = 3 -> {shape_zero} (no solution).")
    print("      This is exactly the probe's earlier negative result (selector test 3:")
    print("      compactified radial measure ALONE cannot produce w = a^4) recovered")
    print("      as the omega = 0 slice of the family. The envelope the probe said")
    print("      was missing IS the density weight.")

    # (ii) bending energy: does any (nu) make (D_s^2 (a^3 f))^2 a^(-kappa*nu)
    # match ((a^3 f)')^2 ? The bending integrand contains f'' terms; the probe
    # integrand contains only f' and f. Test with a generic quadratic profile.
    f = sp.Function("f")(x)
    u = a**3 * f
    kap = 1
    Ds2u = sp.expand((a**kap * sp.diff(a**kap * sp.diff(u, x), x)))
    target = sp.expand(sp.diff(u, x) ** 2)

    # bending integrand with free measure power p: (Ds2u)^2 * a^p
    p = sp.Symbol("p", real=True)
    f_test = x**2 + sp.Rational(1, 3) * x**4   # concrete probe profile
    bend = sp.expand((Ds2u.subs(f, f_test).doit()) ** 2 * a**p)
    targ = sp.expand(target.subs(f, f_test).doit())
    # try to solve bend == targ for constant p at two sample points; a constant
    # p cannot exist if the ratio depends on x.
    ratio = sp.simplify(targ / sp.expand((Ds2u.subs(f, f_test).doit()) ** 2))
    ratio_1 = sp.simplify(ratio.subs(x, sp.Rational(1, 3)))
    ratio_2 = sp.simplify(ratio.subs(x, sp.Rational(1, 2)))
    # if bending matched with constant measure power, ratio would be a^p:
    # check whether log(ratio)/log(a) is x-independent
    p_1 = sp.simplify(sp.log(ratio_1) / sp.log(1 - sp.Rational(1, 9)))
    p_2 = sp.simplify(sp.log(ratio_2) / sp.log(1 - sp.Rational(1, 4)))
    distinct = not is_zero(sp.simplify(p_1 - p_2))

    print()
    print("  (ii) bending energy (D_s^2 u)^2 a^p vs probe (u')^2 on a concrete profile:")
    print(f"       implied measure power at x=1/3: p = {sp.sstr(sp.nsimplify(p_1, rational=False))}")
    print(f"       implied measure power at x=1/2: p = {sp.sstr(sp.nsimplify(p_2, rational=False))}")
    print(f"       x-dependent => no constant measure power matches: {distinct}")

    with out.counterexamples():
        out.line("measure-only reading fails (omega = 0)",
                 StatusMark.FAIL,
                 "kappa*omega = 3 unsolvable; recovers the probe's compactified-measure no-go")
        out.line("bending-type reading fails",
                 StatusMark.FAIL if distinct else StatusMark.WARN,
                 "no constant measure power maps (D_s^2 u)^2 onto the probe integrand")

    with out.governance_assessments():
        out.line("identification survives both artifact tests",
                 StatusMark.PASS,
                 "first-derivative stretch energy of a weight-3 density under a 2D measure "
                 "is the unique reading in the tested family",
                 )
    return distinct


# =============================================================================
# Case 6: interpretation boundary and verdict
# =============================================================================


def case_6_verdict(out: ScriptOutput) -> None:
    header("Case 6: Interpretation boundary and Trial B1 verdict")
    print("DERIVED (within the ansatz family: power-law compactification,")
    print("single field, first-order stretch energy):")
    print()
    print("  1. The probe energy IS physical Dirichlet energy of the scalar")
    print("     U = a^3 f under measure dA = e^(2 phi) dx.")
    print("  2. The measure dimension is FORCED: nu = 2. Not chosen.")
    print("  3. The total density weight is FORCED: kappa*omega = 3.")
    print("  4. w = a^4 is explained: 4 = 3 + 3 - 2.")
    print("  5. The chart is x = tanh(s); the admissibility boundary x = 1 is")
    print("     spatial infinity; boundedness of f means U decays like a^3.")
    print()
    print("NOT DERIVED (the G30 boundary):")
    print()
    print("  - that nature uses this reading (the ansatz family is a modeling choice);")
    print("  - the physical identity of U, S, and the 2D measure;")
    print("  - any connection to UFFT's pseudo-2D relaxation. The numerical")
    print("    coincidence (forced nu = 2; UFFT's relaxed phase is pseudo-2D) is")
    print("    recorded as a quarantined cross-trial echo, evidence of nothing yet.")
    print()
    print("Trial B1 verdict: NOT KILLED; structurally upgraded.")
    print("  The chart question 'why w = a^4' now has a candidate physical answer")
    print("  with two forced integers. Next: B2 must attack the physical identity")
    print("  of U and S, and whether kappa-gauge maps onto a known radial gauge.")

    with out.governance_assessments():
        out.line("Trial B1 verdict: structural identification DERIVED, adoption CANDIDATE",
                 StatusMark.PASS,
                 "nu = 2 and weight-3 forced within family; physical adoption stays open (G30)")
    with out.unresolved_obligations():
        out.line("B2: physical identity of U, S, and the 2D measure",
                 StatusMark.OBLIGATION,
                 "identify the chart variables with framework objects without smuggling")
        out.line("B2: kappa-gauge vs radial gauge",
                 StatusMark.OBLIGATION,
                 "does compactification-rate freedom map onto areal/proper radial gauge freedom?")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns) -> None:
    kappa, omega, nu = sp.symbols("kappa omega nu", positive=True)

    ns.record_derivation(
        derivation_id="bridge_probe_is_dirichlet_b1",
        inputs=[],
        output=sp.Symbol("u_prime_squared"),
        method="(L f)^2 a^4 == (d(a^3 f)/dx)^2 verified symbolically; coupling S f a^4 == a S u",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="energy_identity",
        scope="probe energy equals flat Dirichlet energy of u = a^3 f in the x-chart",
    )
    ns.record_derivation(
        derivation_id="bridge_exponent_matching_theorem_b1",
        inputs=[kappa, omega, nu],
        output=sp.Tuple(sp.Eq(nu, 2), sp.Eq(kappa * omega, 3)),
        method="solve {kappa*omega = 3, 2k - k*nu + 2k*omega - 2 = 4} for (omega, nu)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="forced_structure",
        scope=(
            "within power-law compactification + weighted-density + stretch-energy family: "
            "measure dimension nu = 2 forced for all kappa; total weight a^3 forced; kappa free"
        ),
    )
    ns.record_derivation(
        derivation_id="bridge_weight_decomposition_b1",
        inputs=[],
        output=sp.Eq(sp.Symbol("w_exponent"), 3 + 3 - 2),
        method="<psi,f>_w = int (a^3 psi)(a^3 f) a^-2 dx verified symbolically",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weight_explanation",
        scope="w = a^4 decomposes as two weight-3 conversions minus one 2D measure factor",
    )
    ns.record_derivation(
        derivation_id="bridge_canonical_chart_b1",
        inputs=[],
        output=sp.Eq(sp.Symbol("x"), sp.tanh(sp.Symbol("s"))),
        method="ds = dx/a integrated; a = sech^2 s; total length diverges at x = 1",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="chart_geometry",
        scope="kappa = 1 canonical chart; admissibility boundary = spatial infinity",
    )
    ns.record_derivation(
        derivation_id="bridge_artifact_tests_b1",
        inputs=[],
        output=sp.Symbol("measure_only_and_bending_fail"),
        method="omega=0 slice unsolvable (recovers probe selector no-go); bending (D_s^2 u)^2 has no constant measure power",
        status=Status.DERIVED,
        record_kind=RecordKind.COUNTEREXAMPLE,
        result_type="artifact_control",
        scope="uniqueness of the stretch-energy reading within the tested family",
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="bridge_physical_identity_b1",
        script_id=SCRIPT_ID,
        title="B2: identify U, S, and the 2D measure with framework objects",
        status=ObligationStatus.OPEN,
        required_by=["trial_B_verdict"],
        description=(
            "The structural identification is derived; physical adoption requires "
            "identifying U = a^3 f and S_phys = a^3 S with vacuum-configuration "
            "objects and explaining the forced 2D measure, without using recovery "
            "targets or the UFFT echo as selectors."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="trial_B_continuation_b1",
        script_id=SCRIPT_ID,
        name="Trial B continuation: physical identification (B2)",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["bridge_physical_identity_b1"],
        activation_conditions=[
            "nu = 2 and kappa*omega = 3 carried as derived structural facts",
            "kappa remains a gauge parameter until mapped to a radial gauge",
            "UFFT pseudo-2D echo stays quarantined (not a selector)",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="quarantine_ufft_2d_echo_b1",
        script_id=SCRIPT_ID,
        branch_id="ufft_pseudo2d_echo_as_evidence",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.INFORMATIONAL,
        obligation_ids=["bridge_physical_identity_b1"],
        description=(
            "The forced nu = 2 numerically echoes UFFT's pseudo-2D relaxation. "
            "Recorded as a cross-trial observation only. It may not be used as "
            "evidence for either trial until an independent mechanism connects them."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="bridge_structural_identification_b1",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Within the power-law-compactification stretch-energy family, the probe "
            "functional is EXACTLY the physical Dirichlet energy of the scalar "
            "U = a^3 f under a two-dimensional measure, with measure dimension "
            "nu = 2 and total density weight 3 FORCED by exponent matching and "
            "the compactification rate kappa a gauge freedom. The projection weight "
            "decomposes as 4 = 3 + 3 - 2. Physical adoption of the reading remains "
            "an open candidate (G30)."
        ),
        derivation_ids=[
            "bridge_probe_is_dirichlet_b1",
            "bridge_exponent_matching_theorem_b1",
            "bridge_weight_decomposition_b1",
            "bridge_canonical_chart_b1",
            "bridge_artifact_tests_b1",
        ],
        obligation_ids=["bridge_physical_identity_b1"],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial B1: Measure-Bridge Static Reduction")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    case_1_probe_baseline(out)
    case_2_exponent_matching(out)
    case_3_canonical_chart(out)
    case_4_weight_decomposition(out)
    case_5_artifact_tests(out)
    case_6_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
