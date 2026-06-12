# Trial E1: sharp-source gate -- must curvature be smooth at mass boundaries?
#
# Group:
#   009_trial_E_boundary_admissibility
#
# Script type:
#   GATE DERIVATION / DICHOTOMY THEOREM / CONSTRAINT EXPORT
#
# Purpose
# -------
# Theory-owner intuition under test: "curvature at mass boundaries must be
# smooth in VED because of curvature energy; GR allows non-smooth curvature
# but does not require it."
#
# Honest findings (each verified below):
#
#   E1-a  The derived reduced static law ADMITS sharp sources. A step
#         density gives A, A' continuous and A'' jumping by exactly the
#         source jump; the derived field energy -(c^4/8piG)(s')^2 is
#         finite and continuous across the jump. The intuition is NOT yet
#         in the theory.
#
#   E1-b  GR control: the uniform-density star (interior Schwarzschild)
#         satisfies the junction conditions with A, A', B continuous, B'
#         and Ricci jumping, surface pressure zero. GR handles the sharp
#         boundary with no layer.
#
#   E1-c  Dichotomy theorems:
#         (c1) TRANSCRIPTION: any second-order response that is pointwise
#              algebraic in the source (GR-form AND the derived VED form)
#              REQUIRES a curvature jump given a sharp source, and yields
#              smooth curvature given a smooth source. At this level GR
#              and reduced VED are IDENTICAL: curvature smoothness equals
#              source smoothness, both ways.
#         (c2) NO ENERGY BARRIER: the derived (s')^2 energy assigns cost
#              difference O(ell) to smoothing a curvature kink -- it
#              cannot dynamically prefer smooth boundaries.
#         (c3) THE MECHANISM: adding a curvature-energy term beta (s'')^2
#              raises the field equation to fourth order, and fourth-order
#              matching FORCES curvature continuity: the jump migrates to
#              the fourth derivative and the boundary smooths over a
#              DERIVED width ell* = sqrt(beta). The intuition is exactly
#              the statement beta != 0 in K_strain -- gated by
#              Ostrogradsky/G20 (healthy only for degenerate structures,
#              f(R)-like loophole noted).
#
# Verdict: UNDERDETERMINED at reduced level, as forecast -- a
# constraint-recording trial. The smooth-boundary intuition is neither
# earned nor killed; it is now EQUIVALENT to a sharp question about
# K_strain's higher-curvature content, with a derived prediction shape
# (minimum smoothing scale ell* = sqrt(beta)) and a named gate (G20).
#
# Record correction: the old transition-layer program (groups 052-065)
# was quarantined diagnostic-only and never derived a forced layer; the
# boundary-lift route (066-081) adopted no axiom. Claims that "the old
# program showed conservation forces a layer" overstate the corpus.

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
        dependency_id="c2_selector_dependency_009",
        upstream_script_id="002_trial_C_burden_ledger__trial_C2_self_coupling_bootstrap",
        upstream_derivation_id="bootstrap_selector_lamda_minus_one_c2",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="g02_uniqueness_dependency_009",
        upstream_script_id="006_gate_G03_radiative_positivity__gate_G03_radiative_positivity",
        upstream_derivation_id="flat_vacuum_uniqueness_g02",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Curvature machinery (C3 pattern, static spherical)
# =============================================================================

t, r, th, ph = sp.symbols("t r theta phi")
COORDS = [t, r, th, ph]


def metric(Afun, Bfun):
    return sp.diag(-Afun, Bfun, r**2, r**2 * sp.sin(th) ** 2)


def christoffel(g):
    ginv = g.inv()
    n = 4
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                s_ = 0
                for d in range(n):
                    s_ += ginv[a, d] * (sp.diff(g[d, b], COORDS[c_])
                                        + sp.diff(g[d, c_], COORDS[b])
                                        - sp.diff(g[b, c_], COORDS[d]))
                Gamma[a][b][c_] = sp.simplify(s_ / 2)
    return Gamma


def ricci(Gamma):
    n = 4
    R_ = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            expr = 0
            for c_ in range(n):
                expr += sp.diff(Gamma[c_][a][b], COORDS[c_])
                expr -= sp.diff(Gamma[c_][a][c_], COORDS[b])
                for d in range(n):
                    expr += Gamma[c_][c_][d] * Gamma[d][a][b]
                    expr -= Gamma[c_][a][d] * Gamma[d][c_][b]
            R_[a, b] = sp.simplify(expr)
    return R_


def einstein_mixed(g):
    Gamma = christoffel(g)
    Ric = ricci(Gamma)
    ginv = g.inv()
    Rs = sp.simplify(sum(ginv[i, j] * Ric[i, j] for i in range(4) for j in range(4)))
    G_mixed = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            G_mixed[a, b] = sp.simplify(sum(
                ginv[a, c_] * (Ric[c_, b] - sp.Rational(1, 2) * g[c_, b] * Rs)
                for c_ in range(4)))
    return G_mixed


# =============================================================================
# Common symbols
# =============================================================================

c = sp.Symbol("c", positive=True)
G_N = sp.Symbol("G", positive=True)
rho0 = sp.Symbol("rho_0", positive=True)
Rb = sp.Symbol("R", positive=True)          # boundary radius
kappa = 8 * sp.pi * G_N / c**2              # derived areal-flux coupling


# =============================================================================
# Case 0: problem statement
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Trial E1 -- must curvature be smooth at mass boundaries?")
    print("Intuition under test (theory owner): curvature energy forces smooth")
    print("curvature at mass boundaries in VED; GR allows but does not require")
    print("non-smooth curvature.")
    print()
    print("Discipline notes, stated up front:")
    print("  - The old transition-layer program (groups 052-065) is QUARANTINED")
    print("    diagnostic-only; it never derived a forced layer. No support is")
    print("    drawn from it here.")
    print("  - The projection ladder's proved selection (m = 2) sits at R = 0:")
    print("    BOUNDEDNESS, the weakest rung -- not smoothness.")
    print("  - Forecast verdict class: UNDERDETERMINED (constraint-recording).")

    with out.governance_assessments():
        out.line("Trial E1 opened", StatusMark.INFO,
                 "gates E-G1/E-G2/E-G3; intuition registered as candidate, not theorem")


# =============================================================================
# Case 1 (E1-a): the derived static law admits sharp sources
# =============================================================================


def case_1_sharp_source_reduced(out: ScriptOutput) -> None:
    header("Case 1 (E1-a): Step source in the derived areal-flux law")
    print("Delta_areal A = (8 pi G/c^2) rho with rho = rho_0 theta(R - r).")
    print()

    # piecewise solution: (r^2 A')' = kappa rho r^2
    M_tot = sp.Rational(4, 3) * sp.pi * Rb**3 * rho0
    A_ext = 1 - 2 * G_N * M_tot / (c**2 * r)
    # interior: A' = kappa rho0 r / 3; integrate, match A at R
    A_in_prime = kappa * rho0 * r / 3
    A_in = sp.integrate(A_in_prime, r) + sp.Symbol("C_A")
    C_A_val = sp.solve(sp.Eq(A_in.subs(r, Rb), A_ext.subs(r, Rb)), sp.Symbol("C_A"))[0]
    A_in = A_in.subs(sp.Symbol("C_A"), C_A_val)

    # verify the law on both branches
    def areal(Af):
        return sp.simplify(sp.diff(r**2 * sp.diff(Af, r), r) / r**2)

    law_in = sp.simplify(areal(A_in) - kappa * rho0)
    law_ext = sp.simplify(areal(A_ext))
    # continuity and jump structure at R
    jump_A = sp.simplify(A_ext.subs(r, Rb) - A_in.subs(r, Rb))
    jump_A1 = sp.simplify(sp.diff(A_ext, r).subs(r, Rb) - sp.diff(A_in, r).subs(r, Rb))
    jump_A2 = sp.simplify(sp.diff(A_ext, r, 2).subs(r, Rb) - sp.diff(A_in, r, 2).subs(r, Rb))
    print(f"  law residual (interior, exterior) = ({sp.sstr(law_in)}, {sp.sstr(law_ext)})")
    print(f"  [A]  at R = {sp.sstr(jump_A)}")
    print(f"  [A'] at R = {sp.sstr(jump_A1)}")
    print(f"  [A''] at R = {sp.sstr(jump_A2)}   (target: -kappa rho_0 = {sp.sstr(-kappa * rho0)})")

    # derived field energy across the boundary: s = ln A, u ~ (s'/..)^2
    s_in_prime = sp.simplify(sp.diff(A_in, r) / A_in)
    s_ext_prime = sp.simplify(sp.diff(A_ext, r) / A_ext)
    jump_sprime = sp.simplify(s_ext_prime.subs(r, Rb) - s_in_prime.subs(r, Rb))
    # exterior energy integral converges: integrand (s')^2 r^2 = a^2/(r-a)^2
    a_ = 2 * G_N * M_tot / c**2
    E_ext_integrand = sp.simplify((s_ext_prime**2) * r**2)
    E_ext = sp.integrate(a_**2 / (r - a_) ** 2, (r, Rb, sp.oo))
    print()
    print(f"  [s'] at R = {sp.sstr(jump_sprime)}   (gradient continuous: energy density continuous)")
    print(f"  exterior energy integral  Int (s')^2 r^2 dr = {sp.sstr(sp.simplify(E_ext))}   (finite for R > r_s)")
    print()
    print("  GATE E-G1: PASS -- the derived static law ADMITS the sharp source.")
    print("  A and A' continuous, A'' jumps by exactly the source jump, the")
    print("  derived (s')^2 energy is continuous and finite. Nothing in the")
    print("  adopted reduced theory smooths, forbids, or even notices the edge.")
    print("  The smooth-boundary intuition is NOT yet in the theory.")

    ok = (is_zero(law_in) and is_zero(law_ext) and is_zero(jump_A)
          and is_zero(jump_A1) and is_zero(jump_A2 + kappa * rho0)
          and is_zero(jump_sprime))
    # finiteness: closed form contains no infinities, and a numerical witness
    # in the physical regime R > r_s is positive and finite
    E_num = E_ext.subs({G_N: 1, c: 1, rho0: sp.Rational(1, 1000), Rb: 1})
    e_ok = (not E_ext.has(sp.oo, sp.zoo, sp.nan)) and E_num.is_positive and E_num.is_finite
    with out.derived_results():
        out.line("sharp source admitted by the derived static law",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 "[A] = [A'] = 0; [A''] = -kappa rho_0; jump transcribed, not forbidden")
        out.line("derived field energy finite and continuous across the jump",
                 StatusMark.PASS if (ok and bool(e_ok)) else StatusMark.FAIL,
                 "(s')^2 penalizes gradients, not curvature jumps")


# =============================================================================
# Case 2 (E1-b): GR control -- the uniform-density star
# =============================================================================


def case_2_gr_control(out: ScriptOutput) -> None:
    header("Case 2 (E1-b): GR control -- interior Schwarzschild junction")
    r_s = sp.Symbol("r_s", positive=True)

    A_in = (sp.Rational(3, 2) * sp.sqrt(1 - r_s / Rb)
            - sp.Rational(1, 2) * sp.sqrt(1 - r_s * r**2 / Rb**3)) ** 2
    B_in = 1 / (1 - r_s * r**2 / Rb**3)
    A_ext = 1 - r_s / r
    B_ext = 1 / A_ext

    # junction data at r = R
    jA = sp.simplify(A_in.subs(r, Rb) - A_ext.subs(r, Rb))
    jA1 = sp.simplify(sp.diff(A_in, r).subs(r, Rb) - sp.diff(A_ext, r).subs(r, Rb))
    jB = sp.simplify(B_in.subs(r, Rb) - B_ext.subs(r, Rb))
    jB1 = sp.simplify(sp.diff(B_in, r).subs(r, Rb) - sp.diff(B_ext, r).subs(r, Rb))
    print(f"  [A]  = {sp.sstr(jA)}")
    print(f"  [A'] = {sp.sstr(jA1)}")
    print(f"  [B]  = {sp.sstr(jB)}")
    print(f"  [B'] = {sp.sstr(jB1)}   (nonzero: the density jump, transcribed)")

    # interior Einstein tensor: surface pressure and the curvature jump
    G_in = einstein_mixed(metric(A_in, B_in))
    Grr_surface = sp.simplify(G_in[1, 1].subs(r, Rb))
    Gtt_in_surface = sp.simplify(G_in[0, 0].subs(r, Rb))
    print(f"  G^r_r(R-) = {sp.sstr(Grr_surface)}   (zero: surface pressure vanishes -- junction condition)")
    print(f"  G^t_t(R-) = {sp.sstr(Gtt_in_surface)}   vs  G^t_t(R+) = 0   (Ricci REQUIRED to jump)")
    print()
    print("  GATE E-G2: PASS (control). GR handles the sharp boundary with")
    print("  metric A, A', B continuous, B' and Ricci jumping, no layer and no")
    print("  surface shell. Given sharp matter GR REQUIRES the curvature jump;")
    print("  given smooth matter it requires smooth curvature. GR itself")
    print("  imposes NOTHING on the edge profile.")

    ok = (is_zero(jA) and is_zero(jA1) and is_zero(jB)
          and (not is_zero(jB1)) and is_zero(Grr_surface)
          and (not is_zero(Gtt_in_surface)))
    with out.derived_results():
        out.line("uniform-density star junction verified from scratch",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 "[A]=[A']=[B]=0, [B'] != 0, G^r_r(R)=0, G^t_t jumps: sharp boundary fine in GR")


# =============================================================================
# Case 3 (E1-c): dichotomy -- what would force smoothing, and at what cost
# =============================================================================


def case_3_dichotomy(out: ScriptOutput) -> None:
    header("Case 3 (E1-c): Dichotomy -- transcription, no barrier, and the beta mechanism")

    # ---- (c1) transcription is generic for second-order algebraic responses
    # For F(A, A', A'') = kappa rho with A, A' continuous across the boundary,
    # the jump is carried entirely by A'': [F] = (dF/dA'') [A''] = kappa [rho].
    # Witness it on the VED self-coupling form: Delta_areal s = kappa rho e^-s - (s')^2.
    A_f = sp.Function("A")(r)
    s_f = sp.log(A_f)
    lhs = sp.simplify(sp.diff(r**2 * sp.diff(s_f, r), r) / r**2 + sp.diff(s_f, r) ** 2
                      - (sp.diff(r**2 * sp.diff(A_f, r), r) / r**2) / A_f)
    print("  (c1) Transcription. The C2 form Delta_areal s + (s')^2 = kappa rho/A is")
    print(f"       identical to the areal law: residual = {sp.sstr(lhs)}")
    print("       With A, A' continuous, [s''] = [A'']/A(R) = -kappa rho_0/A(R) != 0:")
    print("       the VED reduced form REQUIRES the curvature jump exactly as GR")
    print("       does. Both directions: smooth source <=> smooth curvature.")
    c1_ok = is_zero(lhs)

    # ---- (c2) no energy barrier in the derived (s')^2 functional
    # Kink model: s'(x) = |x| (curvature s'' jumps -1 -> +1 at 0). Smoothing
    # family over width ell: s'_ell = (x^2 + ell^2)/(2 ell) on |x| < ell (C^1).
    x, ell = sp.symbols("x ell", positive=True)
    E_sharp = sp.integrate(x**2, (x, -1, 1))
    inner = sp.integrate(((x**2 + ell**2) / (2 * ell)) ** 2, (x, -ell, ell))
    outer = 2 * sp.integrate(x**2, (x, ell, 1))
    dE = sp.simplify(inner + outer - E_sharp)
    dE_limit = sp.limit(dE, ell, 0)
    print()
    print("  (c2) No energy barrier. Smoothing a curvature kink over width ell:")
    print(f"       Delta E(ell) = {sp.sstr(sp.expand(dE))},  lim(ell->0) = {sp.sstr(dE_limit)}")
    print("       The derived (s')^2 energy cannot prefer smooth boundaries: the")
    print("       sharp configuration costs the same in the limit. P5 has no")
    print("       lever here, and the static sector is source-slaved anyway (G02).")
    c2_ok = is_zero(dE_limit)

    # ---- (c3) the mechanism: curvature energy => fourth order => smoothness
    # Toy: energy ~ Int [(u')^2 + beta (u'')^2]; EL: beta u'''' - u'' = kappa rho.
    # For the curvature v = u'': beta v'' - v = kappa rho. Step source, bounded
    # solution: v is CONTINUOUS with transition width sqrt(beta).
    beta = sp.Symbol("beta", positive=True)
    kap, r0 = sp.symbols("kappa_s rho_b", positive=True)
    ellstar = sp.sqrt(beta)
    v_left = -kap * r0 + (kap * r0 / 2) * sp.exp(x / ellstar)    # x < 0 (matter side)
    v_right = -(kap * r0 / 2) * sp.exp(-x / ellstar)             # x > 0 (vacuum side)
    ode_left = sp.simplify(beta * sp.diff(v_left, x, 2) - v_left - kap * r0)
    ode_right = sp.simplify(beta * sp.diff(v_right, x, 2) - v_right)
    jv = sp.simplify(v_right.subs(x, 0) - v_left.subs(x, 0))
    jv1 = sp.simplify(sp.diff(v_right, x).subs(x, 0) - sp.diff(v_left, x).subs(x, 0))
    print()
    print("  (c3) The mechanism. Add curvature energy beta (s'')^2: the response")
    print("       becomes FOURTH order; for the curvature v = s'' the equation is")
    print("       beta v'' - v = kappa rho. Bounded solution across a step source:")
    print(f"         ODE residuals (matter, vacuum) = ({sp.sstr(ode_left)}, {sp.sstr(ode_right)})")
    print(f"         [v] at boundary  = {sp.sstr(jv)}    [v'] at boundary = {sp.sstr(jv1)}")
    print("       CURVATURE IS CONTINUOUS, transitioning over the DERIVED width")
    print("         ell* = sqrt(beta).")
    print("       The smooth-boundary intuition is EXACTLY the statement that")
    print("       K_strain contains a nonzero curvature-energy coefficient beta.")
    print("       Cost: fourth-order dynamics faces the Ostrogradsky/G20 ghost")
    print("       gate -- healthy only for degenerate structures (the f(R)-class")
    print("       loophole). The gate travels with the route.")
    c3_ok = (is_zero(ode_left) and is_zero(ode_right)
             and is_zero(jv) and is_zero(jv1))

    with out.derived_results():
        out.line("transcription theorem: reduced VED = GR at sharp boundaries",
                 StatusMark.PASS if c1_ok else StatusMark.FAIL,
                 "second-order algebraic responses REQUIRE the curvature jump given sharp sources, both theories")
        out.line("no energy barrier in the derived (s')^2 functional",
                 StatusMark.PASS if c2_ok else StatusMark.FAIL,
                 "Delta E -> 0 as ell -> 0; curvature jumps cost nothing at this order")
        out.line("beta-mechanism: curvature energy forces curvature continuity with ell* = sqrt(beta)",
                 StatusMark.PASS if c3_ok else StatusMark.FAIL,
                 "fourth-order matching; the intuition becomes a sharp question about K_strain; G20 gate attached")


# =============================================================================
# Case 4: verdict
# =============================================================================


def case_4_verdict(out: ScriptOutput) -> None:
    header("Case 4: Trial E1 verdict")
    print("VERDICT: UNDERDETERMINED at reduced level (constraint-recording), as")
    print("forecast. The intuition is neither earned nor killed:")
    print()
    print("  E-G1  sharp sources ADMITTED by the derived reduced theory")
    print("  E-G2  GR control verified: identical boundary behavior at this level")
    print("  E-G3  mechanism classified: smooth boundaries <=> beta != 0 in")
    print("        K_strain (curvature-energy term), with derived smoothing scale")
    print("        ell* = sqrt(beta) and the G20 ghost gate attached")
    print()
    print("EXPORTED CONSTRAINT (the trial's product): the smooth-boundary")
    print("question is now a single sharp question about the parent --")
    print("does K_strain contain higher-curvature energy? If yes: VED predicts a")
    print("minimum smoothing scale at matter boundaries where GR transcribes the")
    print("profile exactly (a kappa-leak-family deviation), and must pass G20.")
    print("If no: the intuition dies honestly, and VED matches GR at boundaries.")
    print()
    print("RECORD CORRECTION: the old transition-layer program never derived a")
    print("forced layer (quarantined diagnostic-only at group 065; no axiom")
    print("adopted at 078-080). The intuition's support is the c3 mechanism,")
    print("not the old program.")

    with out.governance_assessments():
        out.line("Trial E1 verdict: UNDERDETERMINED, constraint exported",
                 StatusMark.PASS,
                 "smooth boundaries <=> nonzero curvature-energy in K_strain; ell* = sqrt(beta); G20 gate")
    with out.unresolved_obligations():
        out.line("decide beta in K_strain (higher-curvature content of the parent)",
                 StatusMark.OBLIGATION,
                 "the single question this trial reduces the intuition to")
        out.line("if beta != 0: G20/Ostrogradsky health (degenerate structure required)",
                 StatusMark.OBLIGATION,
                 "ghost gate travels with the smooth-boundary route")
        out.line("matter-side smoothing route (P6 back-reaction on the edge profile)",
                 StatusMark.OBLIGATION,
                 "unexplored alternative: smoothing in rho rather than in the response")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="sharp_source_admitted_e1",
        inputs=[],
        output=sp.Symbol("step_source_solution_A_C1_curvature_jump_transcribed"),
        method="piecewise solution of the derived areal-flux law with step density; "
               "junction data and energy integral computed exactly",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="gate_result",
        scope="E-G1 PASS: reduced VED admits sharp sources; smooth-boundary intuition not yet in the theory",
    )
    ns.record_derivation(
        derivation_id="gr_control_junction_e1",
        inputs=[],
        output=sp.Symbol("interior_schwarzschild_junction_verified"),
        method="full Einstein tensor of the interior Schwarzschild solution; junction "
               "data at the stellar surface computed from scratch",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="control",
        scope="E-G2 PASS: GR transcribes the source jump (Ricci jump required given sharp matter, "
              "nothing imposed on the edge profile)",
    )
    ns.record_derivation(
        derivation_id="transcription_no_barrier_e1",
        inputs=[],
        output=sp.Symbol("second_order_responses_transcribe_jumps_no_energy_barrier"),
        method="C2-form/areal-law identity; explicit smoothing family with Delta E -> 0",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="dichotomy_theorem",
        scope="reduced VED and GR identical at boundaries: curvature smoothness = source smoothness, both ways",
    )
    ns.record_derivation(
        derivation_id="beta_smoothing_mechanism_e1",
        inputs=[],
        output=sp.Symbol("curvature_energy_forces_continuity_with_ellstar_sqrt_beta"),
        method="fourth-order toy beta v'' - v = kappa rho solved across step source; "
               "continuity of curvature and transition width verified",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="mechanism_theorem",
        scope="smooth boundaries <=> beta != 0 in K_strain; derived smoothing scale ell* = sqrt(beta); "
              "Ostrogradsky/G20 gate attached",
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="k_strain_beta_decision_e1",
        script_id=SCRIPT_ID,
        title="Decide K_strain's higher-curvature content (beta): the smooth-boundary question",
        status=ObligationStatus.OPEN,
        required_by=["k_strain_program"],
        description="Trial E1 reduced the theory-owner's smooth-boundary intuition to this single "
                    "question. beta != 0 yields a minimum smoothing scale ell* = sqrt(beta) "
                    "(new prediction vs GR) and must pass G20; beta = 0 kills the intuition.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="matter_side_smoothing_route_e1",
        script_id=SCRIPT_ID,
        title="Matter-side smoothing: P6 back-reaction on the edge profile (unexplored)",
        status=ObligationStatus.OPEN,
        required_by=[],
        description="Alternative to the beta mechanism: smoothing could live in rho's dynamics "
                    "rather than the geometric response. Outside the static source-slaved sector.",
    ))

    ns.record_route(RouteRecord(
        route_id="smooth_boundary_beta_route_e1",
        script_id=SCRIPT_ID,
        name="Smooth-boundary route: nonzero curvature-energy beta in K_strain",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["k_strain_beta_decision_e1"],
        activation_conditions=[
            "G20/Ostrogradsky health (degenerate higher-order structure required)",
            "prediction shape registered: minimum smoothing scale ell* = sqrt(beta) at matter boundaries",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="boundary_dichotomy_e1",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Reduced level: the derived VED static law and GR are IDENTICAL at mass "
            "boundaries -- both transcribe source smoothness into curvature smoothness "
            "exactly (jump required given sharp matter, smooth given smooth matter, "
            "nothing imposed on the edge profile), and the derived (s')^2 energy "
            "carries no barrier against curvature jumps. The theory-owner's "
            "smooth-boundary intuition is therefore equivalent to a nonzero "
            "curvature-energy coefficient beta in the covariant parent, which would "
            "force curvature continuity with derived smoothing scale ell* = sqrt(beta) "
            "(a testable deviation from GR) at the price of the Ostrogradsky/G20 gate. "
            "Verdict: UNDERDETERMINED at reduced level; constraint exported to the "
            "K_strain program. The old transition-layer program provides NO support "
            "(quarantined diagnostic-only, group 065)."
        ),
        derivation_ids=[
            "sharp_source_admitted_e1",
            "gr_control_junction_e1",
            "transcription_no_barrier_e1",
            "beta_smoothing_mechanism_e1",
        ],
        obligation_ids=["k_strain_beta_decision_e1", "matter_side_smoothing_route_e1"],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial E1: Sharp-Source Gate -- Boundary Admissibility")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    case_1_sharp_source_reduced(out)
    case_2_gr_control(out)
    case_3_dichotomy(out)
    case_4_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
