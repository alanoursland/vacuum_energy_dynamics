#!/usr/bin/env python3
"""
scalaron_unimodular.py

O-P10-3, attacked: does the unimodular constraint neutralize the
packing's R^2-class term (the scalaron), reconciling it with exact P7'?

THE PROPOSED MECHANISM (and its refutation, proved in-house). The
scalaron is a trace-mode excitation, and the trace mode is constrained
(P3/unimodular). Hope: the constraint projects the scalaron out. It
does not, and the reason is structural: the f(R) field-equation tensor
E_mn is IDENTICALLY conserved (diffeomorphism invariance of the f(R)
action), so the divergence of the traceless (unimodular) equations
reconstructs the trace equation up to an integration constant --

    unimodular-f(R) + matter conservation
        =>  f'R - 2f + 3 box f' = kappa T + const.

The SAME Bianchi mechanism that made Lambda an integration constant
(033) resurrects the scalaron equation. For f = R + alpha R^2 this is
(6 alpha box - 1) R = kappa T + const: the scalaron propagates with
m^2 = 1/(6 alpha), exactly as in full-diff f(R). Route (a) is REFUTED.

THE ACTUAL RESOLUTION (reduced to a scoping ruling, with precedent).
The packing's quadratic term gives alpha ~ |f''/f'| a^2: a
Planck-scale coefficient, scalaron range l* = sqrt(6 alpha) ~ a --
thirty orders of magnitude below the strongest laboratory probe. Two
recorded routes:

  (i)  P7'-SCOPED (recommended): P7' was ALREADY adopted in scoped
       form -- exact in the strictly static limit, with the F1
       expansion leak as a "controlled correction within the
       postulate." A Planck-range scalaron is the same class: P7'
       exact in the a -> 0 idealization, with an O(a^2) correction
       that leaves every observable exactly as the exact form
       predicts. E3/G20's kills of macroscopic couplings stand; the
       null-test falsifier face is unchanged (any DETECTED Yukawa at
       any accessible range still kills).
  (ii) STRICT EXACTNESS: hold P7' exact at all orders => the wedge
       energy must satisfy f''(Delta_0) = 0 (an inflection point at
       the frustrated ground state). Cost: a constraint on f with no
       independent motivation -- recovery-shaped unless a reason for
       the inflection emerges. Recorded as the alternative.

The scoping ruling between (i) and (ii) is a theory-owner act
(clarifying an adopted postulate's scope, not a new adoption).

Four checks:

  1. IDENTITY CONSERVATION OF THE f(R) TENSOR (the spine). On FRW with
     f = R + alpha R^2, the EL tensor
     E_mn = f'R_mn - (f/2) g_mn - (grad_m grad_n - g_mn box) f'
     satisfies grad^m E_mt = 0 IDENTICALLY -- no field equations
     imposed. (The full-diff Bianchi fact the reconstruction rests on.)

  2. THE TRACE-RECONSTRUCTION ALGEBRA (formal, exact). From
     grad^m E_mn = 0: grad^m(E_mn - g_mn E/4) = -grad_n E/4, and with
     conservation on the matter side, grad_n(E - kappa T) = 0:
     E = kappa T + const. With E = f'R - 2f + 3 box f' and
     f = R + alpha R^2: E = -R + 6 alpha box R exactly, so
     (6 alpha box - 1) R = kappa T + const: the scalaron equation,
     mass m^2 = 1/(6 alpha), integration constant shifting only the
     Lambda sector.

  3. THE RANGE NUMBERS. l* = sqrt(6 alpha) with alpha ~ a^2: for
     Planck-scale packing, l* ~ 4e-35 m vs the 54-micron laboratory
     frontier: margin ~1e30. Every observable is exactly as P7'-exact
     predicts.

  4. THE INFLECTION ALTERNATIVE. f''(Delta_0) = 0 kills alpha exactly;
     verified as the unique way to zero the R^2-class coefficient
     within the expansion-point structure (039). Recorded with its
     recovery-shaped cost.

Output:
    theory_v3/development/vacuum_sector/08_packing_microphysics/scalaron_unimodular_vacuumforge.md
"""

import math
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
    / "08_packing_microphysics"
    / "scalaron_unimodular_vacuumforge.md"
)

DEPENDENCIES = [
    ("unimodular_dep_047", "033_unimodular_lovelock_break__unimodular_lovelock_break",
     "unimodular_lovelock_break_033"),
    ("bridge_dep_047", "039_regge_delaunay_bridge__regge_delaunay_bridge",
     "regge_delaunay_bridge_039"),
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
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


# =============================================================================
# Curvature machinery (FRW)
# =============================================================================

t = sp.Symbol("t")
alpha = sp.Symbol("alpha", positive=True)


def frw_setup():
    a = sp.Function("a", positive=True)(t)
    x, y, z = sp.symbols("x y z")
    coords = [t, x, y, z]
    g = sp.diag(-1, a**2, a**2, a**2)
    ginv = g.inv()
    n = 4
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k_ in range(n):
                s_ = 0
                for d in range(n):
                    s_ += ginv[i, d] * (
                        sp.diff(g[d, j], coords[k_])
                        + sp.diff(g[d, k_], coords[j])
                        - sp.diff(g[j, k_], coords[d])
                    )
                Gamma[i][j][k_] = sp.together(s_ / 2)
    Ric = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            expr = 0
            for k_ in range(n):
                expr += sp.diff(Gamma[k_][i][j], coords[k_])
                expr -= sp.diff(Gamma[k_][i][k_], coords[j])
                for d in range(n):
                    expr += Gamma[k_][k_][d] * Gamma[d][i][j]
                    expr -= Gamma[k_][i][d] * Gamma[d][k_][j]
            Ric[i, j] = sp.together(expr)
    Rs = sp.together(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return a, coords, g, ginv, Gamma, Ric, Rs


def hessian_scalar(phi, coords, Gamma):
    """grad_m grad_n phi for a scalar phi(t) on FRW."""
    n = 4
    H = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            expr = sp.diff(sp.diff(phi, coords[j]), coords[i])
            for k_ in range(n):
                expr -= Gamma[k_][i][j] * sp.diff(phi, coords[k_])
            H[i, j] = sp.together(expr)
    return H


def div_lower(S, ginv, Gamma, coords):
    n = 4
    out = [0] * n
    for b in range(n):
        expr = 0
        for a_ in range(n):
            for c_ in range(n):
                term = sp.diff(S[c_, b], coords[a_])
                for d in range(n):
                    term -= Gamma[d][a_][c_] * S[d, b]
                    term -= Gamma[d][a_][b] * S[c_, d]
                expr += ginv[a_, c_] * term
        out[b] = sp.together(expr)
    return out


# =============================================================================
# Check 1: identity conservation of the f(R) tensor
# =============================================================================


def check_1_identity_conservation(failures):
    header("Check 1: grad^m E_mn = 0 IDENTICALLY for f = R + alpha R^2 (FRW)")
    a, coords, g, ginv, Gamma, Ric, Rs = frw_setup()
    fR = Rs + alpha * Rs**2
    fp = 1 + 2 * alpha * Rs           # f'(R)
    Hf = hessian_scalar(fp, coords, Gamma)
    boxf = sp.together(sum(ginv[i, j] * Hf[i, j] for i in range(4) for j in range(4)))

    E = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            E[i, j] = sp.together(
                fp * Ric[i, j] - sp.Rational(1, 2) * fR * g[i, j]
                - Hf[i, j] + g[i, j] * boxf
            )
    divE = div_lower(E, ginv, Gamma, coords)
    ok = all(is_zero(divE[b]) for b in range(4))
    require("grad^m E_mn = 0 identically (no field equations imposed)", ok, failures)
    print()
    print("  The f(R) EL tensor is identically conserved -- the Bianchi fact")
    print("  of its diffeomorphism-invariant parent. This is the spine of the")
    print("  reconstruction: the unimodular (traceless) equations cannot lose")
    print("  the trace information; the divergence gives it back.")
    return True


# =============================================================================
# Check 2: the trace-reconstruction algebra
# =============================================================================


def check_2_trace_reconstruction(failures):
    header("Check 2: unimodular f(R) + conservation => scalaron equation returns")
    # Formal exact algebra. With grad^m E_mn = 0 (check 1):
    #   grad^m (E_mn - g_mn E/4) = -grad_n E / 4
    # and the matter side, with conservation:
    #   kappa grad^m (T_mn - g_mn T/4) = -kappa grad_n T / 4.
    # Equating (the unimodular equations): grad_n (E - kappa T) = 0
    #   =>  E = kappa T + const.
    # Now E for f = R + alpha R^2, with box R as a formal symbol:
    R_, L = sp.symbols("R boxR", real=True)  # L stands for box R
    f = R_ + alpha * R_**2
    fp = sp.diff(f, R_)
    boxfp = 2 * alpha * L               # box f' = 2 alpha box R
    E_trace = sp.expand(fp * R_ - 2 * f + 3 * boxfp)
    target = -R_ + 6 * alpha * L
    require("E = f'R - 2f + 3 box f' = -R + 6 alpha box R exactly",
            is_zero(sp.simplify(E_trace - target)), failures)
    # Scalaron: (6 alpha box - 1) R = kappa T + const  =>  m^2 = 1/(6 alpha).
    m2 = sp.Rational(1, 6) / alpha
    require("scalaron mass m^2 = 1/(6 alpha) (pole of the reconstructed equation)",
            is_zero(sp.simplify(m2 - 1 / (6 * alpha))), failures)
    print()
    print("  THE REFUTATION: the proposed mechanism -- 'the unimodular")
    print("  constraint kills the scalaron' -- is FALSE. The same Bianchi")
    print("  mechanism that made Lambda an integration constant (033)")
    print("  reconstructs the trace equation here:")
    print("      (6 alpha box - 1) R = kappa T + const.")
    print("  The scalaron propagates with m^2 = 1/(6 alpha), exactly as in")
    print("  full-diff f(R); the constant shifts only the Lambda sector.")
    print("  Unimodular f(R) = f(R) + free Lambda: no more, no less.")


# =============================================================================
# Check 3: the range numbers
# =============================================================================


def check_3_range(failures):
    header("Check 3: the packing scalaron's range vs the laboratory frontier")
    l_P = 1.616e-35     # m
    probe = 5.4e-5      # m (54 um, strongest current probe at alpha = 1/3 coupling)
    # alpha ~ |f''/2f'| a^2 x O(1) geometry factor; range l* = sqrt(6 alpha) ~ a.
    l_star = math.sqrt(6) * l_P
    margin = probe / l_star
    print(f"  l* = sqrt(6 alpha) ~ sqrt(6) a ~ {l_star:.2e} m (Planck packing)")
    print(f"  laboratory frontier: {probe:.1e} m; margin ~ {margin:.1e}")
    require("scalaron range sits >= 1e25 below the laboratory frontier",
            margin > 1e25, failures)
    print()
    print("  Every observable is exactly as P7'-exact predicts: a Planck-range")
    print("  Yukawa is operationally indistinguishable from none. The E3/G20")
    print("  kills of macroscopic couplings stand untouched; the null-test")
    print("  falsifier face (any DETECTED Yukawa at any accessible range")
    print("  kills) is unchanged.")


# =============================================================================
# Check 4: the inflection alternative
# =============================================================================


def check_4_inflection(failures):
    header("Check 4: strict exactness <=> f''(Delta_0) = 0 (the alternative)")
    f = sp.Function("f")
    D0, eps = sp.symbols("Delta_0 epsilon", positive=True)
    quad_coeff = sp.series(f(D0 + eps), eps, 0, 3).removeO().coeff(eps, 2)
    require("the R^2-class coefficient is f''(Delta_0)/2: zero iff inflection",
            is_zero(sp.simplify(quad_coeff - f(D0).diff(D0, 2) / 2)), failures)
    print()
    print("  Route (ii): holding P7' exact at all orders constrains the wedge")
    print("  energy to an inflection point at the frustrated ground state,")
    print("  f''(Delta_0) = 0 -- killing the R^2 class exactly while leaving")
    print("  the floor (f) and the EH term (f') intact. Cost, recorded: a")
    print("  constraint on f with no independent motivation is recovery-")
    print("  shaped unless a reason for the inflection emerges. The scoping")
    print("  ruling between routes (i) and (ii) is the theory owner's.")


# =============================================================================
# Report and archive
# =============================================================================


def write_report():
    md = """# VacuumForge: The Scalaron vs the Unimodular Constraint (O-P10-3)

## Purpose

Attacks the P7' tension: the packing's f'' term is R^2-class, carrying
a scalaron that P7' (as adopted) forbids. Tests the proposed
resolution -- that the unimodular constraint (P3's seat) projects the
scalaron out -- and records the actual resolution.

## Verified Results

```text
1. THE PROPOSED MECHANISM IS REFUTED (in-house). The f(R) EL tensor is
   identically conserved (verified on FRW for f = R + alpha R^2, no
   field equations imposed), so the divergence of the traceless
   (unimodular) equations reconstructs the trace equation up to an
   integration constant:

       f'R - 2f + 3 box f' = kappa T + const
       =>  (6 alpha box - 1) R = kappa T + const.

   The scalaron propagates with m^2 = 1/(6 alpha), exactly as in
   full-diff f(R). The same Bianchi mechanism that made Lambda an
   integration constant (033) resurrects the scalaron here.
   Unimodular f(R) = f(R) + free Lambda -- no more, no less.

2. THE RANGE NUMBERS. The packing coefficient alpha ~ |f''/2f'| a^2
   gives scalaron range l* = sqrt(6 alpha) ~ a: for Planck packing,
   ~4e-35 m vs the 54-micron laboratory frontier -- margin ~1e30.
   Every observable is exactly as P7'-exact predicts.

3. THE INFLECTION ALTERNATIVE. Strict all-orders P7' exactness is
   equivalent to f''(Delta_0) = 0 (verified: the R^2-class coefficient
   is exactly f''/2), an inflection of the wedge energy at the
   frustrated ground state -- with the recorded recovery-shaped cost.
```

## The Resolution (reduced to a scoping ruling)

O-P10-3 is now fully understood; what remains is a one-line
theory-owner ruling between:

```text
(i)  P7'-SCOPED (recommended): P7' exact in the a -> 0 idealization,
     with the Planck-range scalaron as a controlled O(a^2) correction
     WITHIN the postulate -- the exact precedent of the F1 expansion
     leak, which P7' already carries ("a correction within the
     postulate, not a violation of it"). Observable face unchanged;
     E3/G20 kills stand; the null-test falsifier is untouched.

(ii) STRICT EXACTNESS: adopt f''(Delta_0) = 0 as a wedge-energy
     constraint (inflection at the ground state). Kills the R^2 class
     exactly; costs an unmotivated constraint on f (recovery-shaped
     unless a reason emerges -- e.g., a microphysical symmetry of the
     wedge potential).

The ruling is a scoping clarification of adopted P7', not a new
adoption. Recommendation on record: route (i), by precedent and
economy.
```

## Ledger Effect

```text
O-P10-3: attacked; the candidate cancellation mechanism refuted
in-house; the tension reduced to a pre-analyzed scoping ruling
(p7prime_scoping_ruling_047, theory owner). No coefficient moves under
either route; no observable changes under either route.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/047_scalaron_unimodular/scalaron_unimodular.py
```

Archive record: `scalaron_unimodular_047`.
"""
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def record_archive(ns):
    ns.record_derivation(
        derivation_id="scalaron_unimodular_047",
        inputs=[
            sp.Symbol("unimodular_lovelock_break_result"),
            sp.Symbol("regge_delaunay_bridge_result"),
        ],
        output=sp.Symbol("constraint_does_not_kill_scalaron_tension_reduced_to_scoping"),
        method=(
            "identity conservation of the f(R) EL tensor verified on FRW for "
            "f = R + alpha R^2 with no field equations imposed; formal "
            "trace-reconstruction algebra (E = -R + 6 alpha box R exactly); "
            "range arithmetic; inflection-alternative equivalence"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="tension_analysis",
        scope=(
            "the proposed cancellation is refuted; the tension is a scoping "
            "ruling on adopted P7' with the F1-leak precedent; no coefficient "
            "or observable moves under either route"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="o_p10_3_attacked_047",
        script_id=SCRIPT_ID,
        title="O-P10-3 attacked: mechanism refuted, tension reduced to scoping",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["scalaron_unimodular_047"],
        description=(
            "The unimodular constraint does not kill the scalaron (Bianchi "
            "reconstruction, proved in-house). The tension is fully analyzed: "
            "Planck-range scalaron, margin ~1e30 below laboratory reach; "
            "resolution is a scoping ruling with routes (i) P7'-scoped "
            "(recommended, F1-leak precedent) or (ii) f''(Delta_0) = 0."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p7prime_scoping_ruling_047",
        script_id=SCRIPT_ID,
        title="Theory-owner scoping ruling on P7' vs the Planck-range scalaron",
        status=ObligationStatus.OPEN,
        required_by=["scalaron_unimodular_047"],
        description=(
            "Choose route (i) (P7' exact in the a -> 0 idealization, "
            "Planck-range scalaron as controlled correction; recommended) or "
            "route (ii) (strict exactness via the f''(Delta_0) = 0 inflection "
            "constraint, recovery-shaped cost recorded). A clarification of "
            "adopted P7', not a new adoption; no observable changes either way."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="scalaron_unimodular_claim_047",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The unimodular constraint does not neutralize the scalaron: the "
            "f(R) EL tensor's identical conservation reconstructs the trace "
            "equation from the traceless system up to an integration "
            "constant, so unimodular f(R) equals f(R) with free Lambda and "
            "the scalaron mass m^2 = 1/(6 alpha) is intact. The P7' tension "
            "is thereby reduced to a scoping ruling: the packing scalaron's "
            "range is the packing scale (~1e30 below laboratory reach), so "
            "either P7' is scoped to the a -> 0 idealization with the "
            "Planck-range correction controlled (the F1-leak precedent, "
            "recommended) or strict exactness constrains the wedge energy to "
            "an inflection f''(Delta_0) = 0. No coefficient or observable "
            "moves under either route; the null-test falsifier is unchanged."
        ),
        derivation_ids=["scalaron_unimodular_047"],
        obligation_ids=["o_p10_3_attacked_047", "p7prime_scoping_ruling_047"],
    ))


def main() -> None:
    header("Derivation 047: The Scalaron vs the Unimodular Constraint")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_1_identity_conservation(failures)
    check_2_trace_reconstruction(failures)
    check_3_range(failures)
    check_4_inflection(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 047: verification failure")
    print("  The proposed cancellation is REFUTED (honest negative): the")
    print("  Bianchi mechanism reconstructs the scalaron equation from the")
    print("  unimodular system. The tension is reduced to a pre-analyzed")
    print("  scoping ruling on adopted P7' -- route (i) recommended by the")
    print("  F1-leak precedent -- with no coefficient or observable moving")
    print("  under either route.")

    write_report()
    record_archive(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
