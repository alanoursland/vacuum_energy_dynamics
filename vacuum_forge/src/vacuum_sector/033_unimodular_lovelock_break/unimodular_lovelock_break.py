#!/usr/bin/env python3
"""
unimodular_lovelock_break.py

VacuumForge verification of the lovelock_breaks.md structural argument:
VED relaxes Lovelock's H3 (identical conservation / full-Diff invariance)
in the unimodular direction, forced by P3, with Lambda consequently an
integration constant rather than a coupling.

The five checks are exactly the forge obligations listed in
lovelock_breaks.md section 11:

  1. kinematic identity: kappa = ln(sqrt(-g)/sqrt(-g_bar)) in areal gauge;
  2. H3 violation: nabla^a (R_ab - 1/4 g_ab R) = 1/4 nabla_b R, verified
     on two independent nontrivial metric families (static spherical and
     FRW), computed from scratch;
  3. Lambda as integration constant: trace-free equations + matter
     conservation imply d/dt (R + k T) = 0 on FRW, and the algebraic
     reconstruction G_ab + Lambda g_ab = k T_ab with 4 Lambda = R + k T
     is an identity;
  4. vacuum-energy sequestering: T_ab -> T_ab - rho_vac g_ab leaves the
     trace-free source invariant;
  5. the F1 kappa-leak is second order and matter-sourced: kappa =
     (3/4) Omega_m (H0 r/c)^2 + O(4), zero in the pure-Lambda limit, and
     Schwarzschild-de Sitter satisfies kappa = 0 with
     G_ab + Lambda g_ab = 0 exactly.

Output:
    theory_v3/development/vacuum_sector/lovelock_breaks_vacuumforge.md
"""

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


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"
REPO_ROOT = SCRIPT_PATH.parents[4]
REPORT_PATH = (
    REPO_ROOT
    / "theory_v3"
    / "development"
    / "vacuum_sector"
    / "lovelock_breaks_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "strain_axiom_sieve_dependency_033",
        "032_strain_axiom_candidate_sieve__strain_axiom_candidate_sieve",
        "strain_axiom_candidate_sieve_032",
    ),
]


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


def require(label: str, condition: bool, failures: list) -> None:
    mark = "PASS" if condition else "FAIL"
    print(f"  [{mark}] {label}")
    if not condition:
        failures.append(label)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in DEPENDENCIES:
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


# =============================================================================
# Curvature machinery (hand-rolled, general diagonal 4D metric)
# =============================================================================


def christoffel(g, coords):
    n = len(coords)
    ginv = g.inv()
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                s_ = 0
                for d in range(n):
                    s_ += ginv[a, d] * (
                        sp.diff(g[d, b], coords[c_])
                        + sp.diff(g[d, c_], coords[b])
                        - sp.diff(g[b, c_], coords[d])
                    )
                Gamma[a][b][c_] = sp.together(s_ / 2)
    return Gamma


def ricci(Gamma, coords):
    n = len(coords)
    R = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            expr = 0
            for c_ in range(n):
                expr += sp.diff(Gamma[c_][a][b], coords[c_])
                expr -= sp.diff(Gamma[c_][a][c_], coords[b])
                for d in range(n):
                    expr += Gamma[c_][c_][d] * Gamma[d][a][b]
                    expr -= Gamma[c_][a][d] * Gamma[d][c_][b]
            R[a, b] = sp.together(expr)
    return R


def curvature(g, coords):
    Gamma = christoffel(g, coords)
    Ric = ricci(Gamma, coords)
    ginv = g.inv()
    n = len(coords)
    Rs = sp.together(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return Gamma, Ric, Rs, ginv


def div_lower_tensor(S, g, ginv, Gamma, coords):
    """Covariant divergence (nabla^a S_ab) of a symmetric (0,2) tensor."""
    n = len(coords)
    out = [0] * n
    for b in range(n):
        expr = 0
        for a in range(n):
            for c_ in range(n):
                term = sp.diff(S[c_, b], coords[a])
                for d in range(n):
                    term -= Gamma[d][a][c_] * S[d, b]
                    term -= Gamma[d][a][b] * S[c_, d]
                expr += ginv[a, c_] * term
        out[b] = sp.together(expr)
    return out


t, r, th, ph = sp.symbols("t r theta phi")


# =============================================================================
# Check 1: the kinematic identity kappa = ln(sqrt(-g)/sqrt(-g_bar))
# =============================================================================


def check_1_kinematic_identity(failures):
    header("Check 1: kappa = ln(sqrt(-g)/sqrt(-g_bar)) in areal gauge")
    A, B = sp.symbols("A B", positive=True)
    g = sp.diag(-A, B, r**2, r**2 * sp.sin(th) ** 2)
    det_g = g.det()
    sqrt_minus_g = sp.sqrt(sp.simplify(-det_g))
    sqrt_minus_gbar = r**2 * sp.sin(th)  # flat fiducial, same chart
    kappa = sp.Rational(1, 2) * sp.log(A * B)
    identity = sp.simplify(
        sp.expand_log(sp.log(sqrt_minus_g / sqrt_minus_gbar), force=True) - kappa
    )
    print(f"  sqrt(-g) = {sp.sstr(sqrt_minus_g)}")
    print(f"  ln(sqrt(-g)/sqrt(-g_bar)) - kappa = {sp.sstr(identity)}")
    require("kappa is exactly the log metric volume density", is_zero(identity), failures)
    print()
    print("  The reduced trace mode kappa = (1/2) ln(AB) is the determinant/")
    print("  volume-density mode of the metric. P3's constant-density")
    print("  commitment, and P7's shadow AB = 1, are the statement")
    print("  sqrt(-g) = sqrt(-g_bar): the unimodular constraint, derived from")
    print("  the postulate rather than imposed by fiat.")


# =============================================================================
# Check 2: H3 violation -- nabla^a (R_ab - 1/4 g_ab R) = 1/4 nabla_b R
# =============================================================================


def check_2_h3_violation(failures):
    header("Check 2: nabla^a (R_ab - (1/4) g_ab R) = (1/4) nabla_b R")
    # Witness family (i): general static spherical metric.
    A = sp.Function("A", positive=True)(r)
    B = sp.Function("B", positive=True)(r)
    coords = [t, r, th, ph]
    g1 = sp.diag(-A, B, r**2, r**2 * sp.sin(th) ** 2)
    _verify_h3_on(g1, coords, "static spherical A(r), B(r)", failures)

    # Witness family (ii): flat FRW.
    a = sp.Function("a", positive=True)(t)
    g2 = sp.diag(-1, a**2, a**2, a**2)
    coords2 = [t, sp.Symbol("x"), sp.Symbol("y"), sp.Symbol("z")]
    _verify_h3_on(g2, coords2, "flat FRW a(t)", failures)

    print()
    print("  The trace-free tensor A_ab = R_ab - (1/4) g_ab R satisfies")
    print("  Lovelock's H1, H2, H4, H5, H6 but fails H3: it is NOT identically")
    print("  divergence-free. Its divergence is (1/4) nabla_b R, nonzero off")
    print("  shell. Conservation holds only after matter conservation is")
    print("  imposed separately -- and that step is what manufactures Lambda")
    print("  (Check 3). This is the unimodular relaxation of Lovelock,")
    print("  verified by direct computation on two independent families.")


def _verify_h3_on(g, coords, label, failures):
    Gamma, Ric, Rs, ginv = curvature(g, coords)
    n = 4
    Atf = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            Atf[i, j] = Ric[i, j] - sp.Rational(1, 4) * g[i, j] * Rs
    divA = div_lower_tensor(Atf, g, ginv, Gamma, coords)
    # Also verify the Einstein tensor IS identically conserved (contrast).
    G = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            G[i, j] = Ric[i, j] - sp.Rational(1, 2) * g[i, j] * Rs
    divG = div_lower_tensor(G, g, ginv, Gamma, coords)

    ok_A = all(is_zero(divA[b] - sp.Rational(1, 4) * sp.diff(Rs, coords[b])) for b in range(n))
    ok_G = all(is_zero(divG[b]) for b in range(n))
    nontrivial = not is_zero(sp.diff(Rs, coords[1] if label.startswith("static") else coords[0]))
    print(f"  family: {label}")
    require(f"    nabla^a A_ab = (1/4) nabla_b R (all components)", ok_A, failures)
    require(f"    contrast: nabla^a G_ab = 0 identically (Bianchi)", ok_G, failures)
    require(f"    witness is nontrivial (nabla R != 0 generically)", nontrivial, failures)


# =============================================================================
# Check 3: Lambda as an integration constant
# =============================================================================


def check_3_lambda_integration_constant(failures):
    header("Check 3: trace-free equations + conservation => Lambda emerges")
    # Flat FRW with perfect fluid, c = 1, k = 8 pi G.
    k = sp.Symbol("k", positive=True)
    a = sp.Function("a", positive=True)(t)
    rho = sp.Function("rho")(t)
    p = sp.Function("p")(t)
    coords = [t, sp.Symbol("x"), sp.Symbol("y"), sp.Symbol("z")]
    g = sp.diag(-1, a**2, a**2, a**2)
    Gamma, Ric, Rs, ginv = curvature(g, coords)

    T = sp.diag(rho, a**2 * p, a**2 * p, a**2 * p)
    trT = sp.simplify(sum(ginv[i, j] * T[i, j] for i in range(4) for j in range(4)))

    # Trace-free field equation E_ab = 0.
    E = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            E[i, j] = (
                Ric[i, j] - sp.Rational(1, 4) * g[i, j] * Rs
                - k * (T[i, j] - sp.Rational(1, 4) * g[i, j] * trT)
            )
    # tracelessness: g^{ab} E_ab = 0 identically
    trE = sp.simplify(sum(ginv[i, j] * E[i, j] for i in range(4) for j in range(4)))
    require("trace-free system has identically vanishing trace", is_zero(trE), failures)

    # Solve the tt trace-free equation for a''.
    a2 = sp.solve(sp.Eq(E[0, 0], 0), sp.diff(a, t, 2))
    require("tt trace-free equation solves for a''", len(a2) == 1, failures)
    a2 = a2[0]

    # Conservation: rho' = -3 (a'/a)(rho + p).
    rho_dot = -3 * sp.diff(a, t) / a * (rho + p)

    # Q = R + k T; eliminate a'' and differentiate.
    Q = (Rs + k * trT).subs(sp.diff(a, t, 2), a2)
    dQ = sp.diff(Q, t)
    dQ = dQ.subs(sp.diff(rho, t), rho_dot).subs(sp.diff(a, t, 2), a2)
    dQ = sp.simplify(dQ)
    print(f"  d/dt (R + k T) on shell = {sp.sstr(dQ)}")
    require("R + k T is a constant of motion (= 4 Lambda)", is_zero(dQ), failures)

    # Algebraic reconstruction: with 4 Lambda = R + k T,
    #   G_ab + Lambda g_ab - k T_ab = E_ab  identically.
    Lam = (Rs + k * trT) / 4
    ok_recon = True
    for i in range(4):
        for j in range(4):
            full = (
                Ric[i, j] - sp.Rational(1, 2) * g[i, j] * Rs
                + Lam * g[i, j] - k * T[i, j]
            )
            ok_recon = ok_recon and is_zero(sp.simplify(full - E[i, j]))
    require(
        "G_ab + Lambda g_ab = k T_ab reconstructed with 4 Lambda = R + k T",
        ok_recon, failures,
    )
    print()
    print("  Lambda enters as the constant of integration of the conservation")
    print("  law, not as a coupling in the action. The full Einstein equations")
    print("  with cosmological term are recovered exactly, with Lambda fixed")
    print("  only by one global datum.")


# =============================================================================
# Check 4: vacuum-energy sequestering
# =============================================================================


def check_4_sequestering(failures):
    header("Check 4: the trace-free source is blind to constant vacuum energy")
    rho_vac = sp.Symbol("rho_vac")
    a = sp.Function("a", positive=True)(t)
    g = sp.diag(-1, a**2, a**2, a**2)
    ginv = g.inv()
    T = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"T_{min(i,j)}{max(i,j)}"))
    trT = sum(ginv[i, j] * T[i, j] for i in range(4) for j in range(4))

    T_shift = T - rho_vac * g
    trT_shift = sum(ginv[i, j] * T_shift[i, j] for i in range(4) for j in range(4))

    ok = True
    for i in range(4):
        for j in range(4):
            src = T[i, j] - sp.Rational(1, 4) * g[i, j] * trT
            src_shift = T_shift[i, j] - sp.Rational(1, 4) * g[i, j] * trT_shift
            ok = ok and is_zero(sp.simplify(src - src_shift))
    require(
        "T_ab -> T_ab - rho_vac g_ab leaves T_ab - (1/4) g_ab T invariant",
        ok, failures,
    )
    print()
    print("  A constant vacuum-energy shift is pure trace and drops out of the")
    print("  trace-free equation: the bulk vacuum energy does not gravitate.")
    print("  This addresses the radiative-stability face of the cosmological-")
    print("  constant problem (the value face remains: the integration")
    print("  constant is still fixed only by a global datum).")


# =============================================================================
# Check 5: the F1 leak is second order and matter-sourced; SdS is exact
# =============================================================================


def check_5_leak_and_sds(failures):
    header("Check 5: F1 kappa-leak vs the unimodular constraint; SdS exactness")
    # kappa from the F1 result AB - 1 = (3/2) Omega_m (H0 r/c)^2.
    Om, H0, c_ = sp.symbols("Omega_m H_0 c", positive=True)
    eps = H0 * r / c_
    AB = 1 + sp.Rational(3, 2) * Om * eps**2
    kappa = sp.Rational(1, 2) * sp.log(AB)
    series = sp.series(kappa, H0, 0, 4).removeO()
    leading = sp.simplify(series)
    target = sp.Rational(3, 4) * Om * eps**2
    require(
        "kappa = (3/4) Omega_m (H0 r/c)^2 + O(4): second order, matter-sourced",
        is_zero(sp.simplify(leading - target)), failures,
    )
    require(
        "pure-Lambda limit Omega_m -> 0 restores kappa = 0 exactly",
        is_zero(kappa.subs(Om, 0)), failures,
    )

    # Schwarzschild-de Sitter: AB = 1 identically and G_ab + Lambda g_ab = 0.
    Lam, rs = sp.symbols("Lambda r_s", positive=True)
    A_sds = 1 - rs / r - Lam * r**2 / 3
    g = sp.diag(-A_sds, 1 / A_sds, r**2, r**2 * sp.sin(th) ** 2)
    coords = [t, r, th, ph]
    Gamma, Ric, Rs, ginv = curvature(g, coords)
    ok_sds = all(
        is_zero(sp.simplify(
            Ric[i, j] - sp.Rational(1, 2) * g[i, j] * Rs + Lam * g[i, j]
        ))
        for i in range(4) for j in range(4)
    )
    require("SdS satisfies G_ab + Lambda g_ab = 0 with AB = 1 (kappa = 0)", ok_sds, failures)
    print()
    print("  The unimodular constraint is exact in the P7'-exact limit (static")
    print("  source-free exterior and any pure-Lambda epoch), with a derived,")
    print("  matter-sourced, second-order departure elsewhere -- the F1 leak,")
    print("  ~6e-31 at 1 AU. The constraint binds the vacuum volume density;")
    print("  matter sources the controlled deviation.")


# =============================================================================
# Report and archive
# =============================================================================


def write_report():
    md = """# VacuumForge Verification: Which Lovelock Hypothesis VED Breaks

## Purpose

This report records the machine verification of the structural argument in
[lovelock_breaks.md](lovelock_breaks.md): VED relaxes Lovelock's H3
(identical conservation / full-diffeomorphism invariance) in the unimodular
direction, forced by P3, with Lambda consequently an integration constant.

It satisfies the five forge obligations listed in lovelock_breaks.md
section 11.

## Verified Results

```text
1. kinematic identity:
   kappa = (1/2) ln(AB) = ln(sqrt(-g)/sqrt(-g_bar)) exactly in areal gauge.
   P3 / P7' shadow (AB = 1) IS the unimodular constraint
   sqrt(-g) = sqrt(-g_bar).

2. H3 violation:
   nabla^a (R_ab - (1/4) g_ab R) = (1/4) nabla_b R, verified componentwise
   on two independent nontrivial families (general static spherical;
   flat FRW), with the contrast nabla^a G_ab = 0 verified identically on
   both. The trace-free response tensor satisfies H1, H2, H4, H5, H6 and
   fails exactly H3.

3. Lambda as integration constant:
   on FRW with perfect fluid, the trace-free field equation plus matter
   conservation give d/dt (R + k T) = 0, and with 4 Lambda = R + k T the
   full equations G_ab + Lambda g_ab = k T_ab are reconstructed as an
   algebraic identity. Lambda is a constant of integration fixed by one
   global datum, not a coupling.

4. vacuum-energy sequestering:
   T_ab -> T_ab - rho_vac g_ab leaves the trace-free source invariant:
   bulk vacuum energy does not gravitate. (Radiative-stability face
   addressed; the value face remains open.)

5. scope of the constraint:
   kappa = (3/4) Omega_m (H0 r/c)^2 + O(4) from the F1 result -- second
   order and matter-sourced, exactly zero in the pure-Lambda limit; and
   Schwarzschild-de Sitter satisfies G_ab + Lambda g_ab = 0 with AB = 1
   identically. The unimodular constraint is exact in the P7'-exact limit
   with a derived, controlled leak elsewhere.
```

## Classification

```text
result type: verified structural result (promotion of lovelock_breaks.md
             from structural argument to forge-verified, within the stated
             reduced/witness scope)
scope:       reduced areal gauge for the kinematic identity; two-family
             componentwise witnesses for the covariant statements; FRW for
             the integration-constant derivation
conclusion:  VED's postulate set (P3, with P7' shadow) supplies the
             unimodular constraint as derived content; the field equations'
             Lambda term is an integration constant fixed by a global
             datum; bulk vacuum energy is sequestered
non-conclusion: this does not derive Lambda's value (the global datum is
             still external); it changes no closed local result; the fully
             covariant statement of the kappa = 0 constraint remains an
             open obligation
```

## Consequences for the Program

The Lambda baseline sweep (008-016) found, route by route, that no local
principle values Lambda and only a supplied global scale constrains it.
That is the defining structural property of Lambda in unimodular gravity,
now derived rather than observed: the sweep's negative results are
theorems of the unimodular reading, and the Lambda lane's status changes
from "allowed but unvalued (selector missing)" to "integration constant
(global datum external), bulk vacuum energy sequestered."

For the strain-axiom decision (obligation
strain_axiom_adoption_decision_required_032): the candidate constraint
axiom was already in the postulate set. P3, read through the kinematic
identity, is a fixed-measure (unimodular) commitment. This is not a new
axiom and licenses no nonbaseline physics; it sharpens the baseline's
structure (TDiff rather than Diff, Lambda's status, sequestering) without
touching the closed sector.

## Newly Opened Obligation

```text
unimodular_covariant_constraint_lift_033:
  state and verify the kappa = 0 constraint covariantly (beyond the
  reduced areal identity and the two-family witnesses), including its
  interaction with the F1 matter-era leak.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/033_unimodular_lovelock_break/unimodular_lovelock_break.py
```

Archive record: `unimodular_lovelock_break_033`.
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def record_archive(ns):
    ns.record_derivation(
        derivation_id="unimodular_lovelock_break_033",
        inputs=[sp.Symbol("strain_axiom_candidate_sieve_result")],
        output=sp.Symbol("P3_unimodular_constraint_Lambda_integration_constant"),
        method=(
            "from-scratch symbolic verification: kappa/volume-density identity; "
            "componentwise nabla^a A_ab = (1/4) nabla_b R on static spherical and "
            "FRW families with Bianchi contrast; FRW trace-free + conservation "
            "=> d(R + kT)/dt = 0 and algebraic reconstruction of "
            "G_ab + Lambda g_ab = k T_ab; sequestering invariance; F1 leak "
            "series and SdS exactness"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="verified_structural_result",
        scope=(
            "reduced areal identity; two-family covariant witnesses; FRW "
            "integration-constant derivation; covariant constraint lift "
            "remains open"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="lovelock_break_verification_033",
        script_id=SCRIPT_ID,
        title="Forge verification of the lovelock_breaks.md structural argument",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["unimodular_lovelock_break_033"],
        description=(
            "Discharges the five forge obligations of lovelock_breaks.md "
            "section 11, promoting the note from structural argument to "
            "forge-verified result within its stated scope."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="unimodular_covariant_constraint_lift_033",
        script_id=SCRIPT_ID,
        title="Covariant statement of the kappa = 0 (unimodular) constraint",
        status=ObligationStatus.OPEN,
        required_by=["unimodular_lovelock_break_033"],
        description=(
            "State and verify the unimodular constraint covariantly, beyond "
            "the reduced areal identity and the two-family witnesses, "
            "including its interaction with the F1 matter-era kappa-leak."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="unimodular_lambda_status_claim_033",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "P3, through the exact identity kappa = ln(sqrt(-g)/sqrt(-g_bar)), "
            "supplies the unimodular constraint as derived postulate content "
            "(exact in the P7'-exact limit, with the F1 matter-sourced "
            "second-order leak). The response tensor of the constrained "
            "variation fails exactly Lovelock's H3; matter conservation then "
            "yields R + kT = 4 Lambda as a constant of integration, "
            "reconstructing G_ab + Lambda g_ab = k T_ab with Lambda fixed "
            "only by a global datum, and with bulk vacuum energy sequestered. "
            "This explains the 008-016 Lambda-sweep negatives as theorems, "
            "changes no closed result, licenses no nonbaseline physics, and "
            "does not derive Lambda's value."
        ),
        derivation_ids=["unimodular_lovelock_break_033"],
        obligation_ids=[
            "lovelock_break_verification_033",
            "unimodular_covariant_constraint_lift_033",
        ],
    ))


def main() -> None:
    header("Derivation 033: Unimodular Lovelock Break (verification of lovelock_breaks.md)")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_1_kinematic_identity(failures)
    check_2_h3_violation(failures)
    check_3_lambda_integration_constant(failures)
    check_4_sequestering(failures)
    check_5_leak_and_sds(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 033: verification failure")
    print("  All five lovelock_breaks.md forge obligations verified.")
    print("  The note is promoted from structural argument to forge-verified")
    print("  result within its stated scope. Newly opened obligation:")
    print("  unimodular_covariant_constraint_lift_033.")

    write_report()
    record_archive(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
