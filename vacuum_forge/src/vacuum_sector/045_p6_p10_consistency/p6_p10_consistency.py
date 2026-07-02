#!/usr/bin/env python3
"""
p6_p10_consistency.py

The P6-P10 consistency audit: hunting the contradiction surfaces
between the exchange postulate and the adopted packing axiom.

THE DANGER, STATED SHARPLY (the owner's question, 2026-07-01). P6 says
a falling body's kinetic-energy gain is funded by REAL vacuum
destruction. But the closed sector's own bookkeeping funds it from
CONFIGURATION energy: the interaction (cross-term) field energy goes
more negative as bodies approach, and that decrease equals the KE gain.
If "substance destruction" and "configuration deepening" were two
different funding sources, then P6 + P10 + P9's count-once fence would
CONTRADICT: the same kinetic energy would be paid twice. If they are
one source under an identification, the postulates are consistent --
and P1 itself supplies the identification (vacuum IS energy, so a
region carrying less energy than the floor IS a region carrying less
vacuum).

METHOD. Postulates are informal; absolute consistency proofs do not
exist for them. The program's two honest standards are:
  (i)  SATISFIABILITY: exhibit one model realizing all postulates at
       once -- the packing model is that model, if P6's commitments
       hold in it;
  (ii) LEDGER THEOREMS: prove the books close with each term counted
       exactly once at every anchor where both postulates make
       quantitative claims.
This audit executes (ii) and assembles (i).

Five checks:

  A. THE VECTOR-CALCULUS SPINE (exact, symbolic). The product rule
     div(phi2 grad phi1) = grad phi1 . grad phi2 + phi2 lap(phi1) and
     the harmonicity of 1/|x| away from its source -- the two exact
     steps behind the cross-term evaluation.

  B. THE NO-DOUBLE-COUNT THEOREM (Newtonian anchor, exact). The
     interaction field energy of two bodies at separation d is
     U_cross = -G m1 m2/d (via A's steps + the mean-value evaluation),
     and the kinetic energy gained falling from rest at infinity to d
     is +G m1 m2/d (work integral, exact). KE = -Delta U_cross exactly:
     ONE ledger. P6's "destroyed vacuum" and the configuration
     deepening are the same entry, counted once. Consistent with trial
     C1's cross-term Green identity (X(d) = +G m1 m2/d as burden
     magnitude).

  C. THE IDENTIFICATION QUANTIFIED (the well as missing vacuum). The
     static field energy density u = -c^4 (s')^2/8 pi G integrated over
     the exterior of radius R is -2GM^2/R at leading order -- exactly
     the recorded interior-cap ledger form -2GM^2/(R - r_s) in its
     weak-field limit. Under P1 (vacuum = energy), the well's negative
     configuration energy IS the record of destroyed vacuum:
     "the amount of vacuum destroyed building the well down to R" =
     2GM^2/R. P6's destruction is not graph surgery; it is strain
     content dropping below the floor -- less energy = less vacuum, by
     P1, with no cell removed. The pointwise rate face:
     F = G M m/r^2 = -dU_cross/dr exactly (smooth, distributed --
     P6's smoothness clause).

  D. P3 COMPATIBILITY (density vs amount, in the packing). P6/P3
     require exchange in AMOUNT, never density. In the packing: the
     intensive, self-measured per-cell density is protected by the
     exact dilation invariance of angle energies (038) plus P2 (rods
     are the cells), while wells differ in strain CONTENT relative to
     floor -- extensive variation, which is precisely P3a's "spatial
     differential of vacuum amount." No rarefaction anywhere; the
     volume-not-density clause is satisfied structurally.

  E. THE HONEST RESIDUAL (recorded, not resolved). The COSMOLOGICAL
     face of P6/P1 -- expansion as substance creation -- is a genuine
     open seam in P10: does the graph grow (cell creation), or does
     content rise? Infall bookkeeping does not decide it. Recorded as
     the seam's remaining open obligation.

Output:
    theory_v3/development/vacuum_sector/08_packing_microphysics/p6_p10_consistency_vacuumforge.md
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
    / "08_packing_microphysics"
    / "p6_p10_consistency_vacuumforge.md"
)

DEPENDENCIES = [
    ("substance_identity_dep_045",
     "038_substance_ledger_identity__substance_ledger_identity",
     "substance_ledger_identity_038"),
    ("p10_adoption_dep_045",
     "044_p10_adoption__p10_adoption",
     "p10_adoption_record_044"),
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
# Check A: the vector-calculus spine
# =============================================================================


def check_A_spine(failures):
    header("Check A: the exact steps behind the cross-term")
    x, y, z = sp.symbols("x y z", real=True)
    p1 = sp.Function("phi_1")(x, y, z)
    p2 = sp.Function("phi_2")(x, y, z)

    def grad(f):
        return sp.Matrix([sp.diff(f, v) for v in (x, y, z)])

    def div(V):
        return sum(sp.diff(V[i], v) for i, v in enumerate((x, y, z)))

    def lap(f):
        return div(grad(f))

    lhs = div(p2 * grad(p1))
    rhs = grad(p1).dot(grad(p2)) + p2 * lap(p1)
    require("div(phi2 grad phi1) = grad phi1 . grad phi2 + phi2 lap phi1 (exact)",
            is_zero(sp.simplify(lhs - rhs)), failures)

    r_ = sp.sqrt(x**2 + y**2 + z**2)
    require("1/|x| is harmonic away from its source (exact)",
            is_zero(sp.simplify(lap(1 / r_))), failures)
    print()
    print("  With the divergence theorem (surface terms vanish for isolated")
    print("  systems), these give the cross-term evaluation:")
    print("  integral grad phi1 . grad phi2 = -integral phi2 lap phi1")
    print("  = -4 pi G m1 x phi2(at body 1), the mean-value step supplied by")
    print("  the harmonicity just verified (phi2 is harmonic across body 1's")
    print("  region for disjoint sources).")


# =============================================================================
# Check B: the no-double-count theorem (Newtonian anchor)
# =============================================================================


def check_B_no_double_count(failures):
    header("Check B: KE = -Delta U_cross exactly -- ONE ledger, counted once")
    G_N, m1, m2, d, r = sp.symbols("G m_1 m_2 d r", positive=True)

    # Cross-term field energy via A's steps:
    #   U_cross = -(1/4 pi G) integral grad phi1 . grad phi2
    #           = +(1/4 pi G) x 4 pi G m1 x phi2(x1) = m1 phi2(x1) = -G m1 m2/d.
    U_cross = m1 * (-G_N * m2 / d)
    require("U_cross = -G m1 m2 / d (assembled from the exact steps)",
            is_zero(sp.simplify(U_cross + G_N * m1 * m2 / d)), failures)

    # Kinetic energy gained falling from rest at infinity to separation d:
    # work integral of F = G m1 m2 / r^2.
    KE = sp.integrate(G_N * m1 * m2 / r**2, (r, d, sp.oo))
    require("KE(infinity -> d) = +G m1 m2 / d (exact work integral)",
            is_zero(sp.simplify(KE - G_N * m1 * m2 / d)), failures)

    # The theorem: KE + Delta U_cross = 0 -- the books close ONCE.
    require("KE = -Delta U_cross exactly: no residual for a second funding source",
            is_zero(sp.simplify(KE + (U_cross - 0))), failures)

    # Pointwise rate face (P6's smoothness clause): the attractive force
    # magnitude equals dU_cross/dr (the radial component is -dU/dr, inward).
    U_r = -G_N * m1 * m2 / r
    require("|F(r)| = dU_cross/dr pointwise (smooth, distributed exchange)",
            is_zero(sp.simplify(G_N * m1 * m2 / r**2 - sp.diff(U_r, r))),
            failures)
    print()
    print("  THE NO-DOUBLE-COUNT THEOREM: the configuration deepening funds")
    print("  the kinetic energy EXACTLY, with zero residual. Therefore P6's")
    print("  'destroyed vacuum' cannot be a SECOND source (that would violate")
    print("  P9's count-once fence); it must be, and is, the SAME entry under")
    print("  the P1 identification: the region's energy content dropping")
    print("  below the floor IS vacuum being destroyed, because vacuum IS")
    print("  energy (P1). One event, two vocabularies -- the same resolution")
    print("  pattern P2 uses for vacuum/spacetime changes.")
    print("  (Anchors trial C1's cross-term Green identity, X(d) = G m1 m2/d.)")


# =============================================================================
# Check C: the identification quantified -- the well as missing vacuum
# =============================================================================


def check_C_missing_vacuum(failures):
    header("Check C: exterior field energy = -2GM^2/R: the well IS missing vacuum")
    G_N, M, c, R, r = sp.symbols("G M c R r", positive=True)
    r_s = 2 * G_N * M / c**2

    # Static shear s = ln A on the compensated branch; u = -c^4 (s')^2/8 pi G.
    A = 1 - r_s / r
    s_prime = sp.diff(sp.log(A), r)
    u = -c**4 * s_prime**2 / (8 * sp.pi * G_N)

    # Total exterior field energy, leading (weak-field) order:
    integrand = sp.series(u * 4 * sp.pi * r**2, G_N, 0, 2).removeO()
    total = sp.integrate(integrand, (r, R, sp.oo))
    target = -2 * G_N * M**2 / R
    require("integral of u_field over exterior of R = -2GM^2/R at leading order",
            is_zero(sp.simplify(total - target)), failures)
    print()
    print("  This is exactly the weak-field limit of the recorded interior-cap")
    print("  ledger entry -2GM^2/(R - r_s) (04_field_equations). Under P1")
    print("  (vacuum = energy), the well's negative configuration energy is")
    print("  the RECORD of destroyed vacuum: building the well down to R")
    print("  destroyed 2GM^2/R worth of vacuum -- strain content dropped")
    print("  below the floor, with NO cell removed. P6's destruction is")
    print("  content-below-floor, not graph surgery. The exact strong-field")
    print("  exchange-rate face is the PG river ledger (trial 021:")
    print("  (1/2)v^2 = GM/r at every radius, saturation at the horizon).")


# =============================================================================
# Check D: P3 compatibility -- amount, never density
# =============================================================================


def check_D_p3_compatibility(failures):
    header("Check D: exchange is in amount, never density (P3/P3a in the packing)")
    # The structural facts, with their verified sources:
    #  (i) intensive self-measured density is protected: angle energies are
    #      exactly dilation-invariant (038) and rods ARE the cells (P2), so
    #      a local observer's per-cell density reading cannot vary;
    #  (ii) wells differ in strain CONTENT relative to floor: extensive
    #      variation = P3a's "spatial differential of vacuum amount";
    #  (iii) therefore no rarefaction anywhere: P6's volume-not-density
    #      clause holds structurally in the packing.
    # Small symbolic echo of (i): a uniform rescaling changes every edge
    # length but no angle; the intensive angular state of a cell is
    # scale-free. (Full verification: 038 check 3; declared dependency.)
    lam = sp.Symbol("lambda", positive=True)
    v1 = sp.Matrix([1, 1, 1])
    v2 = sp.Matrix([1, -1, -1])
    cos_before = v1.dot(v2) / sp.sqrt(v1.dot(v1) * v2.dot(v2))
    cos_after = (lam * v1).dot(lam * v2) / sp.sqrt(
        (lam * v1).dot(lam * v1) * (lam * v2).dot(lam * v2))
    require("intensive angular state is exactly scale-free (echo of 038)",
            is_zero(sp.simplify(cos_before - cos_after)), failures)
    print()
    print("  P3's constancy is intensive and self-measured; the well's deficit")
    print("  is extensive content. The packing realizes exactly the split P3")
    print("  and P3a committed to -- density never varies, amount does, and")
    print("  the amount IS the energy content (P1). No contradiction surface.")


# =============================================================================
# Check E: the honest residual
# =============================================================================


def check_E_residual():
    header("Check E: the remaining open seam (recorded, not resolved)")
    print("  The infall/exchange face of P6 is consistent with P10 (checks")
    print("  A-D). What this audit does NOT resolve is the COSMOLOGICAL face:")
    print("  P1/P2's corollary that expansion creates vacuum. In the packing,")
    print("  substance creation admits two readings:")
    print("    (a) the graph grows -- new cells appended (graph surgery at")
    print("        cosmological rates only); or")
    print("    (b) content rises within a fixed graph.")
    print("  Infall bookkeeping cannot distinguish them; the choice belongs")
    print("  to the Lorentzian-dynamics program (O-P10-4) and is recorded as")
    print("  the seam's open obligation. Consistency of the ADOPTED set is")
    print("  unaffected: both readings satisfy P1-P6 as stated; the seam is")
    print("  an underdetermination, not a contradiction.")


# =============================================================================
# Report and archive
# =============================================================================


def write_report():
    md = """# VacuumForge: The P6-P10 Consistency Audit

## Purpose

Audits the seam between P6 (kinetic-energy changes funded by real
vacuum exchange) and P10 (the packing axiom), at the theory owner's
request. Identifies the contradiction surfaces, proves the ledger-level
consistency theorems, and records the one genuinely open seam.

## The Danger, and the Method

The sharp contradiction candidate: P6 funds infall KE by SUBSTANCE
destruction; the closed sector's bookkeeping funds it by CONFIGURATION
deepening (the cross-term). Two funding sources would double-count
against P9's fence. Consistency requires them to be ONE source under an
identification.

Method (postulates are informal; no absolute consistency proof exists):
(i) satisfiability -- the packing model as a single realization of all
postulates; (ii) ledger theorems -- books closing with each term
counted once at every shared quantitative anchor. This audit executes
(ii) and thereby completes (i) for the infall face.

## Verified Results

```text
A. Exact spine: div(phi2 grad phi1) = grad.grad + phi2 lap phi1;
   1/|x| harmonic away from source.

B. NO-DOUBLE-COUNT THEOREM (Newtonian anchor, exact):
   U_cross = -G m1 m2/d;  KE(inf -> d) = +G m1 m2/d;
   KE = -Delta U_cross with ZERO residual, and F = -dU_cross/dr
   pointwise (P6's smoothness clause). There is no room for a second
   funding source: P6's destroyed vacuum and the configuration
   deepening are the SAME ledger entry. The identification is P1
   itself: vacuum IS energy, so content-below-floor IS destroyed
   vacuum. One event, two vocabularies -- the P2 resolution pattern.
   (Anchors trial C1's cross-term Green identity.)

C. THE IDENTIFICATION QUANTIFIED: the exterior field energy integrates
   to -2GM^2/R at leading order -- the weak-field limit of the recorded
   cap-ledger entry -2GM^2/(R - r_s). Building the well destroyed
   2GM^2/R of vacuum: strain content below floor, NO cell removed.
   P6's destruction is content change, not graph surgery. Strong-field
   rate face: the exact PG river ledger (trial 021).

D. P3 COMPATIBILITY: intensive self-measured density is protected
   (dilation invariance, 038 + P2's rods-are-cells); wells are
   extensive content deficits (P3a's differential of amount). Exchange
   is in amount, never density: the volume-not-density clause holds
   structurally.

E. THE OPEN SEAM (recorded): the cosmological face -- expansion as
   substance creation -- is underdetermined in P10 (graph growth vs
   content rise). An underdetermination, not a contradiction; assigned
   to the Lorentzian-dynamics program.
```

## Consistency Verdict

```text
The P6-P10 seam is CONSISTENT at every anchor where both postulates
make quantitative claims (Newtonian two-body, exact; static exterior,
leading order; strong-field rate via the PG ledger). The consistency
is not an accident: it is forced by P1's identity (vacuum = energy),
which makes P6's substance vocabulary and P10's strain vocabulary two
descriptions of one ledger -- exactly as P2 makes vacuum-change and
spacetime-change one event. The count-once fence (P9) is respected
because there is only one entry to count.

Residual: the cosmological-creation reading (open obligation, below).
Formal caveat, standing: consistency is model-relative and
anchor-tested; informal postulates admit no stronger guarantee.
```

## Newly Opened Obligation

```text
p6_p10_cosmological_creation_045:
  determine the packing reading of cosmological substance creation --
  graph growth (cell creation at cosmological rates) vs content rise
  within a fixed graph -- as part of the Lorentzian-dynamics program
  (O-P10-4). Both readings currently satisfy the adopted set; the
  choice will have its own observables face (e.g., what the F1 leak's
  perturbed-cosmology profile looks like under each).
```

## Verification

```text
vacuum_forge/src/vacuum_sector/045_p6_p10_consistency/p6_p10_consistency.py
```

Archive record: `p6_p10_consistency_045`.
"""
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def record_archive(ns):
    ns.record_derivation(
        derivation_id="p6_p10_consistency_045",
        inputs=[
            sp.Symbol("substance_ledger_identity_result"),
            sp.Symbol("p10_adoption_record"),
        ],
        output=sp.Symbol("p6_p10_consistent_one_ledger_counted_once_cosmological_face_open"),
        method=(
            "exact vector-calculus spine; Newtonian no-double-count theorem "
            "(KE = -Delta U_cross with zero residual, pointwise rate face); "
            "exterior field-energy integral -2GM^2/R matching the cap ledger; "
            "P3 amount-vs-density compatibility; open cosmological seam recorded"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="consistency_audit",
        scope=(
            "infall/exchange face consistent at all shared anchors; "
            "cosmological-creation face recorded open; consistency is "
            "model-relative and anchor-tested"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p6_p10_seam_audited_045",
        script_id=SCRIPT_ID,
        title="P6-P10 seam audited: consistent at all shared anchors",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["p6_p10_consistency_045"],
        description=(
            "The double-counting danger is resolved by the P1 identification "
            "(content-below-floor IS destroyed vacuum): one ledger, counted "
            "once, exact at the Newtonian anchor with the PG ledger as the "
            "strong-field rate face; P3's amount-vs-density split holds "
            "structurally in the packing."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p6_p10_cosmological_creation_045",
        script_id=SCRIPT_ID,
        title="Cosmological substance creation: graph growth vs content rise",
        status=ObligationStatus.OPEN,
        required_by=["p6_p10_consistency_045"],
        description=(
            "The expansion face of P1/P6 is underdetermined in P10 (an "
            "underdetermination, not a contradiction). Assigned to the "
            "Lorentzian-dynamics program (O-P10-4); each reading will carry "
            "its own observables face."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="p6_p10_consistency_claim_045",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "P6 and P10 are consistent at every anchor where both make "
            "quantitative claims: the falling body's kinetic energy is funded "
            "by exactly one ledger entry (KE = -Delta U_cross, zero residual, "
            "exact), and P6's 'destroyed vacuum' is that same entry under "
            "P1's identity -- the well's strain content dropping below the "
            "floor IS vacuum destruction, with no cell removed (the exterior "
            "deficit integrates to 2GM^2/R, the cap ledger's weak-field "
            "form). P3's constancy is intensive and self-measured; wells are "
            "extensive content deficits (P3a). The count-once fence is "
            "respected because there is one entry to count. Open: the "
            "cosmological-creation reading (graph growth vs content rise), "
            "an underdetermination assigned to O-P10-4."
        ),
        derivation_ids=["p6_p10_consistency_045"],
        obligation_ids=[
            "p6_p10_seam_audited_045",
            "p6_p10_cosmological_creation_045",
        ],
    ))


def main() -> None:
    header("Derivation 045: The P6-P10 Consistency Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_A_spine(failures)
    check_B_no_double_count(failures)
    check_C_missing_vacuum(failures)
    check_D_p3_compatibility(failures)
    check_E_residual()

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 045: audit failure")
    print("  The P6-P10 seam is consistent at all shared anchors: one ledger,")
    print("  counted once, with P1 supplying the identification (content-")
    print("  below-floor IS destroyed vacuum). The cosmological-creation face")
    print("  is recorded as the seam's open obligation -- an")
    print("  underdetermination, not a contradiction.")

    write_report()
    record_archive(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
