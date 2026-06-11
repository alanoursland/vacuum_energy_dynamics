# Trial gate inventory and starting-state witnesses
#
# Group:
#   000_trial_charter
#
# Script type:
#   CHARTER / GATE INVENTORY / BASELINE DERIVATIONS
#
# Purpose
# -------
# Open the field-equation trials program. This script does three jobs:
#
#   1. Record the gate inventory (G1-G31) as standing proof obligations that
#      every trial candidate must face, cheapest kill first.
#   2. Pin the candidate-roster baseline equations into the trial archive as
#      validated symbolic derivations (UFFT phase structure, tidal nucleation
#      invariant, crossover scale, dark-bridge sign, scalar-tail flux witness,
#      boundary-contact selector, J_curv cross-term/infall ledger).
#   3. Register the three opening trials (A: UFFT, B: measure bridge,
#      C: burden decomposition) as candidate routes with their gate burdens.
#
# Locked-door question:
#
#   What must any candidate strain functional survive, and what symbolic
#   baseline does each opening trial start from?
#
# This script does not run any gate. It does not adopt UFFT. It does not
# derive a field equation, select a parameter, or open parent closure.
#
# Companion document:
#   theory_v3/development/field_equation_trials/00_introduction.md

from dataclasses import dataclass
from pathlib import Path
from typing import List

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


# =============================================================================
# Utilities
# =============================================================================


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
        print("[INFO] Archive dependencies: none declared (charter opener).")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    # Charter opener: no upstream dependencies. The trial archive is separate
    # from the scripts_v3 archive by construction (ARCHIVE_ROOT lives under
    # field_equation_trials/, and .vacuumforge_archive is gitignored).
    return archive, ns, invalidated


# =============================================================================
# Data models
# =============================================================================


@dataclass
class GateEntry:
    gate_id: str
    tier: str
    title: str
    kill_criterion: str
    obligation_id: str


@dataclass
class TrialEntry:
    trial_id: str
    name: str
    source_note: str
    classification: str
    first_gates: List[str]


# =============================================================================
# Gate inventory
# =============================================================================


def build_gates() -> List[GateEntry]:
    def g(gid, tier, title, kill):
        return GateEntry(gid, tier, title, kill, f"gate_{gid}_t000")

    return [
        # Tier 1: cheap discriminators
        g("G01", "discriminator", "two-body cross-term sign X(r)",
          "candidate config energy gives X(r) sign incompatible with its own infall ledger"),
        g("G02", "discriminator", "flat-vacuum stability",
          "flat vacuum is not the unconstrained minimum (spontaneous curdling)"),
        g("G03", "discriminator", "gravitational-wave energy sign",
          "radiative sector carries negative energy (binary pulsar spin-down is positive)"),
        g("G04", "discriminator", "scalar-radiation safety",
          "unsuppressed long-range scalar breathing mode (quadrupole channel unprotected)"),
        # Tier 2: recovery gates
        g("G05", "recovery", "derive P7: AB = 1 in static source-free exterior",
          "candidate cannot derive reciprocal scaling; assuming it demotes to MATCHED"),
        g("G06", "recovery", "derive P8: d ln alpha = -dU/c^2 through O(c^-4)",
          "wrong second-order temporal coefficient (beta != 1)"),
        g("G07", "recovery", "Newtonian limit with areal-flux normalization",
          "F_A != 8*pi*G*M/c^2 or wrong 1/r exterior"),
        g("G08", "recovery", "scalar-sector admissibility reduction",
          "static scalar reduction fails to produce -u'' = aS bounded-response problem"),
        # Tier 3: fortress gates
        g("G09", "fortress", "mass coin: delta M_A = 0 for non-A sectors",
          "any non-A sector shifts exterior mass (q/r A-tail => delta M_A = -c^2 q/(2G))"),
        g("G10", "fortress", "scalar-tail silence sector-by-sector",
          "any sector leaves C/r exterior tail with C != 0 (flux -4*pi*C)"),
        g("G11", "fortress", "count-once trace: L_double = 0",
          "scalar spatial trace enters the metric through more than one channel"),
        g("G12", "fortress", "source no-double-counting",
          "rho routed to any sector besides A without a derived parent identity"),
        g("G13", "fortress", "boundary no-shell: value AND slope matching",
          "C1 value-match left with boundary flux -4*pi*R*phi0; smoothness claimed as neutrality"),
        g("G14", "fortress", "no-repair rule",
          "counterterm, repair current, O-by-name, dark patch, or recovery-tuned parameter"),
        # Tier 4: probe gates
        g("G15", "probe", "quadratic/parallelogram response -> metric",
          "nonquadratic residual hidden inside the metric branch instead of routed as epsilon"),
        g("G16", "probe", "calibration-coherent transport -> Levi-Civita",
          "torsion/nonmetricity introduced without explicit defect ledger"),
        g("G17", "probe", "shared-metric matter coupling -> stress tensor",
          "matter coupled through anything other than the shared interval/volume structure"),
        g("G18", "probe", "no un-routed extra fields",
          "extra field enters dynamics without explicit routing (routed fields legal)"),
        g("G19", "probe", "Weyl/TT sector integrity",
          "scalar data used to fake traceless/tensor content (rank-deficiency violation)"),
        g("G20", "probe", "action bookkeeping: D=4 Lovelock/locality/boundary + ghost check",
          "higher-curvature coupling introduces ghosts, instabilities, or ill-posed boundary variation"),
        # Tier 5: observational gates
        g("G21", "observational", "Cassini: |gamma - 1| < 2.3e-5",
          "kappa-leak or scalar response exceeding the PPN gamma budget"),
        g("G22", "observational", "perihelion/LLR: beta = 1",
          "second-order temporal self-coupling off the PPN beta budget"),
        g("G23", "observational", "binary-pulsar orbital decay",
          "chi-sector drag, bridge hysteresis, or extra radiation off the GR quadrupole rate"),
        g("G24", "observational", "LIGO merger energy and chirp-mass scaling",
          "burden difference off the few-percent release or wrong mass scaling"),
        g("G25", "observational", "short-range gravity at 10-100 microns",
          "boundary-relaxation force excluded by torsion-balance/microcantilever data"),
        g("G26", "observational", "solar-system Weyl screening",
          "kappa_W C^2 nucleation triggered by Sun/planets without a derived screen"),
        g("G27", "observational", "equivalence principle",
          "composition-dependent coupling (violates P6 per-unit-energy universality)"),
        g("G28", "observational", "cosmology consistency (deferred until statics pass)",
          "expansion history, structure growth, or CMB violated; early-universe transition catastrophe"),
        # Tier 6: discipline gates
        g("G29", "discipline", "status vocabulary enforced",
          "candidate advertised above DERIVED/CONDITIONAL/MATCHED/DIAGNOSTIC/THEOREM_TARGET/KILLED status"),
        g("G30", "discipline", "compatibility-vs-origin",
          "a value solved-for presented as derived (the c = 3*ell/(2R) standard)"),
        g("G31", "discipline", "verdict document required",
          "trial ends without an explicit epsilon=0 / epsilon!=0 / underdetermined / KILLED verdict"),
    ]


def build_trials() -> List[TrialEntry]:
    return [
        TrialEntry(
            trial_id="trial_A_ufft",
            name="Trial A: UFFT (Unified Frustration Field Theory)",
            source_note="ontology_and_mechanism/unified_frustration_field_theory_memo.md",
            classification="elastic-medium + relaxation K_strain branch with explicitly routed chi field",
            first_gates=["G25", "G04", "G26", "G02", "G20", "G23", "G24", "G05", "G06", "G07"],
        ),
        TrialEntry(
            trial_id="trial_B_measure_bridge",
            name="Trial B: measure-conversion bridge (1D toy -> projection chart)",
            source_note="intuition_models/1d_scalar_dissipation.md",
            classification="chart-origin attack: weights as coordinate-to-physical measure conversion",
            first_gates=["G08", "G30"],
        ),
        TrialEntry(
            trial_id="trial_C_burden_ledger",
            name="Trial C: burden decomposition (sign fork by calculation)",
            source_note="ontology_and_mechanism/{positive_curvature_energy,radius_scaling,burden_reduction,p4_sign_fork}",
            classification="energy-bookkeeping discriminator feeding Trials A and B",
            first_gates=["G01", "G24", "G21"],
        ),
    ]


# =============================================================================
# Case 0: charter
# =============================================================================


def case_0_charter(out: ScriptOutput) -> None:
    header("Case 0: Trial charter")
    print("The trials program inverts the archived search's polarity:")
    print()
    print("  field_equation_candidates:  built the filter, found no candidates.")
    print("  projection_origin_probe:    closed the formal mysteries, localized the gap.")
    print("  field_equation_trials:      feeds candidates to the filter.")
    print()
    print("Working unit: one named candidate functional per trial, stated boldly")
    print("enough to be killable, run through the gates cheapest-kill-first.")
    print()
    print("Verdicts per trial: epsilon = 0 / epsilon != 0 / underdetermined / KILLED.")
    print("All four are deliverables.")

    with out.governance_assessments():
        out.line(
            "field_equation_trials opened",
            StatusMark.INFO,
            "gate inventory + baseline witnesses + trial routes; no gate is run here",
        )


# =============================================================================
# Case 1: gate inventory
# =============================================================================


def case_1_gate_inventory(gates: List[GateEntry], out: ScriptOutput) -> None:
    header("Case 1: Gate inventory (G1-G31)")
    current_tier = None
    for gate in gates:
        if gate.tier != current_tier:
            current_tier = gate.tier
            print()
            print(f"--- tier: {current_tier} ---")
        print(f"  [{gate.gate_id}] {gate.title}")
        print(f"         kill: {gate.kill_criterion}")

    with out.governance_assessments():
        out.line(
            "gate inventory recorded",
            StatusMark.PASS,
            f"{len(gates)} standing gates across 6 tiers; each is an OPEN obligation per trial",
        )


# =============================================================================
# Case 2: baseline symbolic witnesses
# =============================================================================


def case_2a_scalar_tail_witness(out: ScriptOutput):
    header("Case 2a: Scalar-tail flux witness (G10 instrument)")
    r = sp.Symbol("r", positive=True)
    C = sp.Symbol("C", real=True)
    phi_tail = C / r
    F_phi = sp.simplify(4 * sp.pi * r**2 * sp.diff(phi_tail, r))
    residual = sp.simplify(F_phi + 4 * sp.pi * C)
    print(f"  phi_tail = {sp.sstr(phi_tail)}")
    print(f"  F_phi = 4*pi*r^2*phi_tail' = {sp.sstr(F_phi)}")

    with out.derived_results():
        out.line(
            "1/r tail flux witness",
            StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
            f"F_phi = {sp.sstr(F_phi)}; silence requires C = 0",
        )
    return F_phi, phi_tail, r, C


def case_2b_boundary_contact_selector(out: ScriptOutput):
    header("Case 2b: Boundary-contact selector (G13 instrument; closed m=2 result)")
    x, m = sp.Symbol("x", positive=True), sp.Symbol("m", positive=True, integer=True)
    profile = (1 - x) ** m
    slope_m1 = sp.diff(profile.subs(m, 1), x).subs(x, 1)
    slope_m2 = sp.diff(profile.subs(m, 2), x).subs(x, 1)
    print(f"  profile ~ (1-x)^m;  slope at x=1:  m=1 -> {slope_m1},  m=2 -> {slope_m2}")
    print("  m=1 fails derivative silence; m=2 passes (probe gates 17/11 and 18/10).")

    with out.derived_results():
        out.line(
            "m=1 fails slope silence",
            StatusMark.PASS if slope_m1 != 0 else StatusMark.FAIL,
            f"slope(m=1) = {slope_m1}",
        )
        out.line(
            "m=2 passes slope silence",
            StatusMark.PASS if slope_m2 == 0 else StatusMark.FAIL,
            f"slope(m=2) = {slope_m2}",
        )
    return profile


def case_2c_ufft_phase_structure(out: ScriptOutput):
    header("Case 2c: UFFT chi-potential phase structure (Trial A baseline)")
    chi = sp.Symbol("chi", real=True)
    alpha, beta, lam = sp.symbols("alpha beta lamda", positive=True)
    V = sp.Rational(1, 2) * alpha * chi**2 - sp.Rational(1, 3) * beta * chi**3 \
        + sp.Rational(1, 4) * lam * chi**4
    dV = sp.diff(V, chi)

    stationary = sp.solve(sp.Eq(dV, 0), chi)
    print(f"  V(chi) = {sp.sstr(V)}")
    print(f"  stationary points: {[sp.sstr(s) for s in stationary]}")

    # Nonzero branch and discriminant threshold
    nonzero = [s for s in stationary if s != 0]
    disc = beta**2 - 4 * lam * alpha
    chi_plus = (beta + sp.sqrt(disc)) / (2 * lam)
    branch_ok = any(is_zero(sp.simplify(s - chi_plus)) for s in nonzero)

    # Coexistence: V = 0 and V' = 0 at nonzero chi
    coexist = sp.solve([sp.Eq(V, 0), sp.Eq(dV, 0)], [alpha, chi], dict=True)
    co_pairs = [(sol[alpha], sol[chi]) for sol in coexist if sol.get(chi, 0) != 0]
    alpha_co_expected = 2 * beta**2 / (9 * lam)
    chi_co_expected = 2 * beta / (3 * lam)
    co_ok = any(
        is_zero(sp.simplify(a - alpha_co_expected)) and is_zero(sp.simplify(c - chi_co_expected))
        for (a, c) in co_pairs
    )
    print(f"  discriminant threshold: alpha_disc = beta^2/(4*lamda)")
    print(f"  coexistence: alpha_co = {sp.sstr(alpha_co_expected)}, chi_co = {sp.sstr(chi_co_expected)}")
    print(f"  spinodal: alpha_sp = 0  (chi=0 loses local stability)")

    # Threshold ordering through a(alpha) = sqrt(gamma/(alpha0 - alpha)),
    # numeric sanity sample with positive denominators.
    a0, g0, b0, l0 = 1.0, 1.0, 1.0, 1.0
    import math
    a_disc = math.sqrt(g0 / (a0 - b0**2 / (4 * l0)))
    a_co = math.sqrt(g0 / (a0 - 2 * b0**2 / (9 * l0)))
    a_sp = math.sqrt(g0 / a0)
    ordering_ok = a_disc > a_co > a_sp
    print(f"  sample ordering (alpha0=beta=lamda=gamma=1): "
          f"a_disc={a_disc:.4f} > a_co={a_co:.4f} > a_sp={a_sp:.4f} : {ordering_ok}")

    with out.derived_results():
        out.line("chi_plus branch from stationarity", StatusMark.PASS if branch_ok else StatusMark.FAIL,
                 "chi_+ = [beta + sqrt(beta^2 - 4*lamda*alpha)]/(2*lamda)")
        out.line("coexistence point derived", StatusMark.PASS if co_ok else StatusMark.FAIL,
                 "alpha_co = 2*beta^2/(9*lamda), chi_co = 2*beta/(3*lamda) from V = V' = 0")
        out.line("first-order threshold ordering a_disc > a_co > a_sp",
                 StatusMark.PASS if ordering_ok else StatusMark.FAIL,
                 "hysteresis window between coexistence and spinodal confirmed in sample")
    return V, chi_plus, alpha_co_expected, chi_co_expected


def case_2d_tidal_invariant(out: ScriptOutput):
    header("Case 2d: Midpoint tidal invariant and nucleation separation (Trial A baseline)")
    x, y, z = sp.symbols("x y z", real=True)
    G, M, d = sp.symbols("G M d", positive=True)
    Phi = -G * M / sp.sqrt((x - d / 2)**2 + y**2 + z**2) \
          - G * M / sp.sqrt((x + d / 2)**2 + y**2 + z**2)
    coords = (x, y, z)
    E = sp.Matrix(3, 3, lambda i, j: sp.diff(Phi, coords[i], coords[j]))
    E0 = sp.simplify(E.subs({x: 0, y: 0, z: 0}))
    invariant = sp.simplify(sum(E0[i, j]**2 for i in range(3) for j in range(3)))
    expected = 1536 * G**2 * M**2 / d**6
    trace0 = sp.simplify(E0.trace())
    print(f"  E_ij at midpoint = diag({sp.sstr(E0[0,0])}, {sp.sstr(E0[1,1])}, {sp.sstr(E0[2,2])})")
    print(f"  E_ij E^ij = {sp.sstr(invariant)}  (expected {sp.sstr(expected)})")
    print(f"  trace E = {sp.sstr(trace0)}  (vacuum Laplace check)")

    kappa, alpha0, alphac = sp.symbols("kappa alpha0 alpha_c", positive=True)
    d_c = sp.solve(sp.Eq(kappa * expected, alpha0 - alphac), d)
    d_c_pos = [s for s in d_c if s.is_positive is not False]
    scaling_ok = any(is_zero(sp.simplify(s - (1536 * kappa * G**2 * M**2 / (alpha0 - alphac)) ** sp.Rational(1, 6)))
                     for s in d_c_pos)
    print(f"  d_c = (1536*kappa*G^2*M^2/(alpha0-alpha_c))^(1/6)  ~  M^(1/3)")

    with out.derived_results():
        out.line("midpoint tidal invariant = 1536 G^2 M^2 / d^6",
                 StatusMark.PASS if is_zero(invariant - expected) else StatusMark.FAIL,
                 "Hessian of two-point-mass potential at the midpoint")
        out.line("vacuum Laplace check at midpoint",
                 StatusMark.PASS if is_zero(trace0) else StatusMark.FAIL,
                 f"trace E = {sp.sstr(trace0)}")
        out.line("nucleation separation d_c ~ M^(1/3)",
                 StatusMark.PASS if scaling_ok else StatusMark.FAIL,
                 "kappa*E^2 = alpha0 - alpha_c solved for d")
    return invariant, expected


def case_2e_crossover_scale(out: ScriptOutput):
    header("Case 2e: Casimir/dark-energy crossover scale (G25 anchor)")
    hbar = 1.054571817e-34
    c = 2.99792458e8
    rho_lambda = 5.4e-10
    import math
    a_lambda = (math.pi**2 * hbar * c / (720 * rho_lambda)) ** 0.25
    in_window = 2.0e-5 < a_lambda < 4.0e-5
    print(f"  a_Lambda = (pi^2 hbar c / (720 rho_Lambda))^(1/4) = {a_lambda:.3e} m")
    print("  UFFT's crossover sits inside torsion-balance territory: G25 is the cheapest Trial A gate.")

    with out.derived_results():
        out.line("crossover scale ~ 30 microns",
                 StatusMark.PASS if in_window else StatusMark.FAIL,
                 f"a_Lambda = {a_lambda:.3e} m for rho_Lambda = 5.4e-10 J/m^3")
    return a_lambda


def case_2f_dark_bridge_sign(out: ScriptOutput):
    header("Case 2f: Dark-bridge sign result (Trial A baseline)")
    drho = sp.Symbol("Delta_rho", real=True)
    active = sp.simplify((drho) + 3 * (-drho))  # rho + 3P with P = -rho
    print(f"  Delta(rho + 3P) with vacuum equation of state P = -rho:  {sp.sstr(active)}")
    print("  Delta_rho < 0 (relaxed region) => active source -2*Delta_rho > 0:")
    print("  a vacuum-energy deficit gravitates as a positive effective source.")

    with out.derived_results():
        out.line("Delta(rho+3P) = -2*Delta_rho",
                 StatusMark.PASS if is_zero(active + 2 * drho) else StatusMark.FAIL,
                 "vacuum-energy deficit acts as positive gravitational source")
    return active


def case_2g_jcurv_ledger(out: ScriptOutput):
    header("Case 2g: J_curv cross-term and infall ledger (Trial C baseline, G01 instrument)")
    G, R = sp.symbols("G R", positive=True)
    m1, m2, lam = sp.symbols("m1 m2 lamda", positive=True)

    def J(m):
        return G * m**2 / (2 * R)

    cross = sp.simplify(J(m1) + J(m2) - J(m1 + m2))
    cross_expected = -G * m1 * m2 / R
    scaling = sp.simplify(J(m1).subs(R, lam * R) - J(m1) / lam)

    # Infall ledger under positive-J accounting: approach from infinity to
    # separation R gains KE = G m1 m2 / R while the stored cross-term rises
    # by the same amount; both must be funded.
    dKE = G * m1 * m2 / R
    dJ = -cross  # stored curvature energy increase = +G m1 m2 / R
    budget = sp.simplify(dKE + dJ)
    budget_expected = 2 * dKE

    print(f"  J(m) = G m^2/(2R);  J(m1)+J(m2)-J(m1+m2) = {sp.sstr(cross)}")
    print(f"  radius scaling: J(m, lamda*R) = J(m,R)/lamda")
    print(f"  infall budget (positive-J accounting): dKE + dJ = {sp.sstr(budget)} = 2*dKE")

    with out.derived_results():
        out.line("cross-term = -G m1 m2 / R (= U_grav)",
                 StatusMark.PASS if is_zero(cross - cross_expected) else StatusMark.FAIL,
                 "combined well stores MORE curvature energy: J_curv is superadditive at fixed R")
        out.line("1/R radius scaling",
                 StatusMark.PASS if is_zero(scaling) else StatusMark.FAIL,
                 "compression doubles burden; R -> 0 diverges (anti-singularity lever)")
        out.line("traceful infall budget = 2*dKE",
                 StatusMark.PASS if is_zero(budget - budget_expected) else StatusMark.FAIL,
                 "under positive-J accounting, substance (P6) funds KE and the well increase",
        )
    return cross, budget


# =============================================================================
# Case 3: trial routes
# =============================================================================


def case_3_trial_routes(trials: List[TrialEntry], gates: List[GateEntry], out: ScriptOutput) -> None:
    header("Case 3: Opening trial roster")
    by_id = {g.gate_id: g for g in gates}
    for trial in trials:
        print()
        print("-" * 120)
        print(trial.name)
        print("-" * 120)
        print(f"Source: {trial.source_note}")
        print(f"Classification: {trial.classification}")
        print("First gates (cheapest kill first):")
        for gid in trial.first_gates:
            print(f"  [{gid}] {by_id[gid].title}")

    with out.governance_assessments():
        out.line("three opening trials registered",
                 StatusMark.PASS,
                 "A (UFFT), B (measure bridge), C (burden ledger); A and B independent, C feeds both")


# =============================================================================
# Case 4: failure controls
# =============================================================================


def case_4_failure_controls(out: ScriptOutput) -> None:
    header("Case 4: Failure controls (charter discipline)")
    print("The trials program fails as a process if any later script:")
    print()
    print("1. selects a parameter to pass a gate and calls the result derived (G30)")
    print("2. uses recovery targets (Schwarzschild, AB=1, gamma, beta) as construction tools")
    print("3. keeps a candidate alive with no live theorem target and no unrun gate")
    print("4. ends a trial without a verdict document (G31)")
    print("5. lets the trial archive depend on or write into the scripts_v3 archive")
    print("6. records archive markers instead of actual symbolic content")
    print("7. introduces an un-routed field to absorb a gate failure (G18/G14)")

    with out.unresolved_obligations():
        out.line("every trial must end in an explicit verdict",
                 StatusMark.OBLIGATION,
                 "epsilon = 0 / epsilon != 0 / underdetermined / KILLED")


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The trial program is open. Standing state:")
    print()
    print("  31 gates recorded as standing obligations across 6 tiers.")
    print("  Baseline equations validated and archived:")
    print("    scalar-tail flux witness, m=2 contact selector, UFFT phase structure")
    print("    (chi_+, alpha_co = 2*beta^2/(9*lamda), chi_co = 2*beta/(3*lamda),")
    print("    threshold ordering), midpoint tidal invariant 1536 G^2 M^2/d^6 with")
    print("    d_c ~ M^(1/3), crossover a_Lambda ~ 30 microns, dark-bridge sign")
    print("    -2*Delta_rho, J_curv cross-term and the 2*dKE traceful budget.")
    print("  Trials A/B/C registered as candidate routes with first-gate schedules.")
    print()
    print("No gate has been run. No candidate has been adopted or killed.")
    print()
    print("Next scripts:")
    print("  trial_A1_short_range_gravity_bounds.py   (G25 vs UFFT pressure spectrum)")
    print("  trial_B1_measure_bridge_static_reduction.py  (toy energy -> w = a^4?)")
    print("  trial_C1_two_body_burden_ledger.py       (per-term dominance vs separation)")

    with out.governance_assessments():
        out.line("charter complete; the gates eat first",
                 StatusMark.PASS,
                 "baseline witnesses archived; trial routes registered; verdict discipline armed")


# =============================================================================
# Archive recording
# =============================================================================


def record_baseline_derivations(ns, F_phi, V, chi_plus, alpha_co, chi_co,
                                invariant, expected_invariant, cross, budget) -> None:
    r = sp.Symbol("r", positive=True)
    C = sp.Symbol("C", real=True)

    ns.record_derivation(
        derivation_id="trial_scalar_tail_flux_witness_t000",
        inputs=[C / r],
        output=F_phi,
        method="F = simplify(4*pi*r**2*diff(C/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="surface_flux_witness",
        scope="reusable G10 instrument for all trials",
    )
    ns.record_derivation(
        derivation_id="trial_ufft_chi_plus_branch_t000",
        inputs=[V],
        output=chi_plus,
        method="solve dV/dchi = 0; nonzero branch",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="phase_branch",
        scope="UFFT relaxation sector stationary structure",
    )
    ns.record_derivation(
        derivation_id="trial_ufft_coexistence_point_t000",
        inputs=[V],
        output=sp.Tuple(alpha_co, chi_co),
        method="solve {V = 0, dV/dchi = 0} at nonzero chi",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="first_order_transition_threshold",
        scope="UFFT coexistence alpha_co = 2*beta^2/(9*lamda), chi_co = 2*beta/(3*lamda)",
    )
    ns.record_derivation(
        derivation_id="trial_midpoint_tidal_invariant_t000",
        inputs=[expected_invariant],
        output=invariant,
        method="Hessian of two-point-mass Newtonian potential at midpoint; sum of squares",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="tidal_invariant",
        scope="UFFT tidal nucleation source E_ij E^ij = 1536 G^2 M^2 / d^6 (trace-free verified)",
    )
    ns.record_derivation(
        derivation_id="trial_jcurv_cross_term_t000",
        inputs=[],
        output=cross,
        method="J(m)=G m^2/(2R); J(m1)+J(m2)-J(m1+m2)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="superadditivity_witness",
        scope="J_curv cross-term = -G m1 m2 / R; combined well stores more",
    )
    ns.record_derivation(
        derivation_id="trial_traceful_infall_budget_t000",
        inputs=[cross],
        output=budget,
        method="dKE + dJ under positive-J accounting",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="energy_ledger",
        scope="positive-J infall requires substance funding = 2*dKE (G01 instrument)",
    )


def record_gate_obligations(ns, gates: List[GateEntry]) -> None:
    for gate in gates:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=gate.obligation_id,
            script_id=SCRIPT_ID,
            title=f"[{gate.gate_id}/{gate.tier}] {gate.title}",
            status=ObligationStatus.OPEN,
            required_by=["trial_verdict_discipline_t000"],
            description=f"Standing gate for all trials. Kill criterion: {gate.kill_criterion}",
        ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="trial_verdict_discipline_t000",
        script_id=SCRIPT_ID,
        title="Every trial ends in an explicit verdict",
        status=ObligationStatus.OPEN,
        required_by=[],
        description="epsilon = 0 / epsilon != 0 / underdetermined / KILLED; kills are deliverables.",
    ))


def record_trial_routes(ns, trials: List[TrialEntry], gates: List[GateEntry]) -> None:
    gate_obligation = {g.gate_id: g.obligation_id for g in gates}
    for trial in trials:
        ns.record_route(RouteRecord(
            route_id=f"{trial.trial_id}_route_t000",
            script_id=SCRIPT_ID,
            name=trial.name,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[gate_obligation[g] for g in trial.first_gates],
            activation_conditions=[
                f"source: {trial.source_note}",
                f"classification: {trial.classification}",
                "gates run cheapest-kill-first; a kill stops the trial and produces the verdict",
                "parameters may be bounded by gates, never selected by them",
            ],
            description=trial.classification,
        ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_recovery_as_construction_t000",
        script_id=SCRIPT_ID,
        branch_id="recovery_selected_trial_parameters",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["gate_G30_t000"],
        description=(
            "Reject any trial step that selects parameters, branches, or residual "
            "status from recovery targets (Schwarzschild, AB=1, gamma, beta, PPN). "
            "Recovery audits; it does not construct."
        ),
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_candidate_hoarding_t000",
        script_id=SCRIPT_ID,
        branch_id="candidate_alive_without_target_or_gate",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["trial_verdict_discipline_t000"],
        description=(
            "Reject keeping a candidate alive with no live theorem target and no "
            "unrun gate (the FEC postmortem's candidate-hoarding failure mode)."
        ),
    ))


def record_charter_claims(ns) -> None:
    ns.record_claim(ClaimRecord(
        claim_id="trial_charter_rule_t000",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.LICENSING,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Field-equation trials run named candidate functionals through the "
            "standing gates G1-G31 cheapest-kill-first. Every trial ends in an "
            "explicit verdict: epsilon = 0, epsilon != 0, underdetermined, or "
            "KILLED. Parameters may be bounded by gates, never selected by them. "
            "Kills are deliverables."
        ),
        derivation_ids=[],
        obligation_ids=["trial_verdict_discipline_t000"],
    ))
    ns.record_claim(ClaimRecord(
        claim_id="trial_baseline_witnesses_t000",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Baseline symbolic witnesses validated and archived: scalar-tail flux "
            "F = -4*pi*C; boundary-contact selector (m=1 fails, m=2 passes slope "
            "silence); UFFT chi_+ branch, coexistence (2*beta^2/(9*lamda), "
            "2*beta/(3*lamda)) and threshold ordering a_disc > a_co > a_sp; "
            "midpoint tidal invariant 1536 G^2 M^2/d^6 (trace-free) with "
            "d_c ~ M^(1/3); crossover a_Lambda ~ 30 microns; dark-bridge sign "
            "Delta(rho+3P) = -2*Delta_rho; J_curv cross-term -G m1 m2/R with "
            "traceful infall budget 2*dKE."
        ),
        derivation_ids=[
            "trial_scalar_tail_flux_witness_t000",
            "trial_ufft_chi_plus_branch_t000",
            "trial_ufft_coexistence_point_t000",
            "trial_midpoint_tidal_invariant_t000",
            "trial_jcurv_cross_term_t000",
            "trial_traceful_infall_budget_t000",
        ],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Field Equation Trials: Gate Inventory and Starting-State Witnesses")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    gates = build_gates()
    trials = build_trials()

    case_0_charter(out)
    case_1_gate_inventory(gates, out)
    F_phi, _, _, _ = case_2a_scalar_tail_witness(out)
    case_2b_boundary_contact_selector(out)
    V, chi_plus, alpha_co, chi_co = case_2c_ufft_phase_structure(out)
    invariant, expected_invariant = case_2d_tidal_invariant(out)
    case_2e_crossover_scale(out)
    case_2f_dark_bridge_sign(out)
    cross, budget = case_2g_jcurv_ledger(out)
    case_3_trial_routes(trials, gates, out)
    case_4_failure_controls(out)
    final_interpretation(out)

    record_baseline_derivations(ns, F_phi, V, chi_plus, alpha_co, chi_co,
                                invariant, expected_invariant, cross, budget)
    record_gate_obligations(ns, gates)
    record_trial_routes(ns, trials, gates)
    record_charter_claims(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
