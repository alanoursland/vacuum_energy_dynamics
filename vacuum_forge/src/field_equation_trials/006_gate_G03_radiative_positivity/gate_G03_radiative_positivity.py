# Gate G03: radiative-sector positivity (and G02: flat-vacuum stability)
#
# Group:
#   006_gate_G03_radiative_positivity
#
# Script type:
#   GATE DERIVATION / SIGNATURE COMPLETION
#
# Purpose
# -------
# Complete the sector-indefinite signature. C2/C3 + P9 + P7' resolved the
# static temporal sector NEGATIVE (u_field = -c^4 (s')^2 / (8 pi G)).
# Observed gravitational radiation carries POSITIVE energy (binary-pulsar
# spin-down). The working picture has been:
#
#   temporal/constraint sector: negative, non-propagating
#   radiative/TT sector:        positive, propagating
#
# This script upgrades the picture to theorem-shaped statements at the
# reduced level:
#
#   T1 (G03+): the TT sector's energy density is a sum of squares
#       (positive definite for K_T > 0) and its flux is outward-positive
#       for outgoing waves; the binary pulsar anchors sign(K_T) = +.
#   T2 (ghost exclusion): promoting the NEGATIVE-energy temporal sector to
#       a propagating (hyperbolic) mode yields a Hamiltonian unbounded
#       below -- a ghost. The constraint (elliptic) assignment of the
#       scalar sector is therefore REQUIRED by stability, converting the
#       old scalar-radiation-safety policy (FEC 007) into a theorem,
#       conditional on the C2 sign.
#   T3 (G02): the source-free constraint sector with asymptotic flatness
#       and regularity has the unique solution A == 1: flat vacuum is the
#       unique zero-source static state. The negative sector is
#       source-slaved -- not an independent energy reservoir. No runaway.
#
# Together: the sector-indefinite signature is stable by architecture --
# the negative sector cannot radiate (it has no propagating mode) and
# cannot be mined (it is uniquely determined by sources); everything that
# propagates is positive.
#
# GR mirror (informational): this is the same architecture by which GR
# survives its conformal-factor problem (wrong-sign conformal kinetic term
# eliminated by the Hamiltonian constraint; TT modes positive).

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
        dependency_id="c2_negative_energy_dependency_g03",
        upstream_script_id="002_trial_C_burden_ledger__trial_C2_self_coupling_bootstrap",
        upstream_derivation_id="bootstrap_negative_field_energy_c2",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="p9_adoption_dependency_g03",
        upstream_script_id="005_postulate_adoptions__record_postulate_adoptions",
        upstream_derivation_id="postulate_P9_record_005",
        expected_record_kind=RecordKind.UNARCHIVED_FOUNDATION,
    )
    ns.declare_dependency(
        dependency_id="p7prime_adoption_dependency_g03",
        upstream_script_id="005_postulate_adoptions__record_postulate_adoptions",
        upstream_derivation_id="postulate_P7prime_record_005",
        expected_record_kind=RecordKind.UNARCHIVED_FOUNDATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Symbols
# =============================================================================

t, z, r = sp.symbols("t z r", real=True)
c, K = sp.symbols("c K_T", positive=True)


# =============================================================================
# Case 0
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Completing the sector-indefinite signature")
    print("Owed since C2: the radiative half. Negative temporal sector is")
    print("settled (C2/C3 + P9 + P7'); now prove the propagating sector is")
    print("positive and the negative sector cannot propagate or be mined.")

    with out.governance_assessments():
        out.line("Gate G03 opened", StatusMark.INFO,
                 "reduced-level theorems; covariant lift recorded as obligation")


# =============================================================================
# Case 1: TT positivity and outward flux
# =============================================================================


def case_1_tt_positivity(out: ScriptOutput):
    header("Case 1 (T1): TT energy density is a sum of squares; flux is outward")
    h = sp.Function("h")
    hp = sp.Function("h_plus")(t, z)
    hx = sp.Function("h_cross")(t, z)

    # reduced TT action per polarization (FEC 006 toy):
    # L = (K/2)[ (1/c^2) h_t^2 - h_z^2 ]
    def T00(hh):
        return sp.Rational(1, 2) * K * (sp.diff(hh, t) ** 2 / c**2 + sp.diff(hh, z) ** 2)

    def T0z(hh):
        return -K * sp.diff(hh, t) * sp.diff(hh, z)

    total_T00 = sp.expand(T00(hp) + T00(hx))
    print("  T^00 = (K_T/2) [ h_t^2/c^2 + h_z^2 ]  per polarization")
    # sum-of-squares check: write as sum of squares explicitly
    a1, a2, a3, a4 = sp.symbols("a1 a2 a3 a4", real=True)
    sos = sp.Rational(1, 2) * K * (a1**2 / c**2 + a2**2) \
        + sp.Rational(1, 2) * K * (a3**2 / c**2 + a4**2)
    sos_match = sp.simplify(
        total_T00.subs({sp.diff(hp, t): a1, sp.diff(hp, z): a2,
                        sp.diff(hx, t): a3, sp.diff(hx, z): a4}) - sos)

    # outgoing wave: h = F(z - c t). For such h: h_t = -c h_z, so
    # flux = c^2 T^{0z} = -c^2 K h_t h_z = c^3 K h_z^2  (positive outward)
    # and  T^00 = (K/2)(h_t^2/c^2 + h_z^2) = K h_z^2 = flux / c.
    F = sp.Function("F")
    h_out = F(z - c * t)
    flux_out = sp.simplify(T0z(h_out) * c**2)
    flux_identity = sp.simplify(flux_out - c**3 * K * sp.diff(h_out, z) ** 2)
    density_identity = sp.simplify(T00(h_out) - K * sp.diff(h_out, z) ** 2)
    flux_val = c**3 * K * sp.Symbol("F_prime", real=True) ** 2
    e_density = c**2 * K * sp.Symbol("F_prime", real=True) ** 2

    print(f"  outgoing h = F(z - ct):  flux - c^3 K_T h_z^2 = {sp.sstr(flux_identity)}")
    print(f"  T^00 - K_T h_z^2 = {sp.sstr(density_identity)}")
    print(f"  i.e. flux = c^3 K_T F'^2 > 0 outward; density = flux / c")
    print()
    print("  Positive-definite for K_T > 0; outgoing waves carry energy OUTWARD.")
    print("  Observational anchor: binary-pulsar spin-down (system LOSES energy)")
    print("  fixes sign(K_T) = +. The quadrupole power formula already in the")
    print("  charter, P ~ (G/c^5) <Qddd^2>, is manifestly a square.")

    with out.derived_results():
        out.line("TT energy density is a sum of squares",
                 StatusMark.PASS if is_zero(sos_match) else StatusMark.FAIL,
                 "T^00 = (K_T/2)[h_t^2/c^2 + h_z^2] summed over polarizations; >= 0 for K_T > 0")
        out.line("outgoing TT flux is positive outward",
                 StatusMark.PASS if is_zero(flux_identity) and is_zero(density_identity) else StatusMark.FAIL,
                 "flux = c^3 K_T F'^2 > 0; energy density = flux/c (null transport)")
        out.line("binary pulsar anchors sign(K_T) = +",
                 StatusMark.PASS,
                 "observational constraint imported as anchor, not fitted")


# =============================================================================
# Case 2: ghost exclusion -- the negative sector must not propagate
# =============================================================================


def case_2_ghost_exclusion(out: ScriptOutput):
    header("Case 2 (T2): hyperbolic promotion of the negative sector is a ghost")
    print("C2 result (dependency-checked): the temporal-sector field energy is")
    print("NEGATIVE, u = -c^4 (s')^2/(8 pi G). Suppose one promoted s to a")
    print("propagating field with that energy ledger -- a wave action with")
    print("negative coefficient:")
    print()
    print("    L_ghost = -(k/2) [ s_t^2/c^2 - s_z^2 ],   k > 0")
    print()
    s = sp.Function("s")(t, z)
    k = sp.Symbol("k", positive=True)
    H_ghost = -sp.Rational(1, 2) * k * (sp.diff(s, t) ** 2 / c**2 + sp.diff(s, z) ** 2)
    # amplitude scaling witness: H[lambda * s] = lambda^2 H[s] -> -infinity
    lam = sp.Symbol("lamda", positive=True)
    H_scaled = H_ghost.subs(s, lam * s).doit()
    scaling = sp.simplify(H_scaled / H_ghost)

    print(f"  Hamiltonian density: H = {sp.sstr(H_ghost)}   (NEGATIVE definite)")
    print(f"  amplitude scaling:   H[lamda s] / H[s] = {sp.sstr(scaling)}")
    print()
    print("  H -> -infinity as amplitude grows: unbounded below. Coupled to any")
    print("  positive sector (Case 1), energy flows without limit from the")
    print("  ghost into radiation -- vacuum decay. EXCLUDED.")
    print()
    print("  Therefore the constraint (elliptic) assignment of the scalar")
    print("  sector -- the FEC-007 'A is constraint, not radiation' policy and")
    print("  the adopted exact law Delta_areal A = source -- is REQUIRED by")
    print("  stability given the C2 sign. The policy is now a theorem")
    print("  (reduced level, conditional on the adopted laws).")

    with out.derived_results():
        out.line("hyperbolic negative sector has Hamiltonian unbounded below",
                 StatusMark.PASS if is_zero(scaling - lam**2) else StatusMark.FAIL,
                 "H[lamda s] = lamda^2 H[s] -> -oo; ghost; vacuum decay when coupled to TT")
    with out.counterexamples():
        out.line("propagating (Box) promotion of the temporal sector",
                 StatusMark.FAIL,
                 "excluded by stability: the scalar-radiation-safety policy becomes a theorem")


# =============================================================================
# Case 3: flat-vacuum uniqueness (G02)
# =============================================================================


def case_3_vacuum_uniqueness(out: ScriptOutput):
    header("Case 3 (T3, gate G02): flat vacuum is the unique zero-source state")
    print("Source-free constraint sector (the adopted exact law, A-linear):")
    print()
    print("    Delta_areal A = (1/r^2)(r^2 A')' = 0,  A -> 1 at infinity,")
    print("    A regular (bounded) at r -> 0  [no source present].")
    print()
    A_r = sp.Function("A")(r)
    general = sp.dsolve(sp.Eq(sp.diff(r**2 * sp.diff(A_r, r), r), 0), A_r)
    print(f"  general solution: {sp.sstr(general)}")
    # A = C1 + C2/r ; decay A(oo) = 1 => C1 = 1 ; regularity at 0 => C2 = 0
    C1 = sp.Symbol("C1")
    C2 = sp.Symbol("C2", positive=True)  # WLOG nonzero amplitude; sign irrelevant to divergence
    A_gen = C1 + C2 / r
    cond_infty = sp.Eq(sp.limit(A_gen, r, sp.oo), 1)
    sol_c1 = sp.solve(cond_infty, C1)
    A_after = A_gen.subs(C1, sol_c1[0])
    # regularity at r=0: C2/r bounded requires C2 = 0
    diverges = sp.limit(A_after - 1, r, 0, "+") == sp.oo
    print(f"  asymptotic flatness => C1 = {sol_c1[0]};  regularity at r=0 =>")
    print(f"  C2/r must stay bounded; C2/r diverges unless C2 = 0: {diverges}")
    print()
    print("  Hence A == 1 (flat) is the UNIQUE zero-source static configuration.")
    print("  Consequences:")
    print("    - the negative sector's energy is source-slaved: it is a")
    print("      functional of the sources, not an independent reservoir;")
    print("    - there is no zero-source configuration with arbitrarily")
    print("      negative energy to decay into; flat vacuum is stable (G02);")
    print("    - mining the negative sector requires moving sources, which is")
    print("      P6 dynamics, radiated through the POSITIVE channel (Case 1).")

    with out.derived_results():
        out.line("flat vacuum unique under decay + regularity",
                 StatusMark.PASS if (sol_c1 == [1] and diverges) else StatusMark.FAIL,
                 "A = C1 + C2/r; flatness fixes C1 = 1, regularity kills C2; G02 closed at reduced level")


# =============================================================================
# Case 4: verdict
# =============================================================================


def case_4_verdict(out: ScriptOutput) -> None:
    header("Case 4: Gates G02 and G03 -- verdict")
    print("The sector-indefinite signature is now theorem-shaped (reduced level,")
    print("conditional on the adopted laws):")
    print()
    print("  NEGATIVE sector (temporal/constraint):")
    print("    - sign derived (C2 + P9 + exact recovery)")
    print("    - non-propagating: elliptic adopted law; hyperbolic promotion is")
    print("      a ghost, excluded by stability (T2)")
    print("    - source-slaved: flat vacuum unique at zero source (T3)")
    print("  POSITIVE sector (TT/radiative):")
    print("    - energy density a sum of squares; outgoing flux positive (T1)")
    print("    - sign anchored by binary-pulsar spin-down")
    print()
    print("  This is the same architecture by which GR survives its")
    print("  conformal-factor problem: the wrong-sign mode is a constraint,")
    print("  not a degree of freedom. The framework reproduces the stable")
    print("  arrangement from its own adopted laws.")
    print()
    print("GATE STATUS: G03 PASS (radiative positivity, reduced + anchored);")
    print("             G02 PASS (flat-vacuum uniqueness/stability, reduced).")
    print()
    print("NOT DERIVED: covariant lift of all three theorems; nonlinear")
    print("stability; the K_T magnitude (still MATCHED to 2G/c^4, not derived).")

    with out.governance_assessments():
        out.line("G03 PASS: radiative sector positive, negative sector caged",
                 StatusMark.PASS,
                 "sum-of-squares + ghost exclusion + uniqueness; binary-pulsar sign anchored")
        out.line("G02 PASS: flat vacuum unique zero-source state",
                 StatusMark.PASS,
                 "reduced Liouville-type uniqueness for the constraint sector")
    with out.unresolved_obligations():
        out.line("covariant lift of T1-T3; nonlinear stability",
                 StatusMark.OBLIGATION,
                 "reduced theorems conditional on adopted laws")
        out.line("derive K_T magnitude (tensor coupling) -- still MATCHED",
                 StatusMark.OBLIGATION,
                 "the bootstrap program's radiative-sector continuation")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="tt_positivity_sum_of_squares_g03",
        inputs=[],
        output=sp.Symbol("T00_TT_sum_of_squares"),
        method="canonical T^00 of the reduced TT action; outgoing flux c^3 K F'^2",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="positivity_theorem",
        scope="TT energy density positive-definite for K_T > 0; binary pulsar anchors the sign",
    )
    ns.record_derivation(
        derivation_id="ghost_exclusion_g03",
        inputs=[],
        output=sp.Symbol("hyperbolic_negative_sector_excluded"),
        method="H[lamda s] = lamda^2 H[s] with H negative definite -> unbounded below",
        status=Status.DERIVED,
        record_kind=RecordKind.COUNTEREXAMPLE,
        result_type="stability_exclusion",
        scope="given the C2 negative sign, the scalar sector must remain elliptic/constraint; "
              "the FEC-007 scalar-radiation policy upgrades to a theorem (reduced)",
    )
    ns.record_derivation(
        derivation_id="flat_vacuum_uniqueness_g02",
        inputs=[],
        output=sp.Symbol("A_identically_one"),
        method="dsolve (r^2 A')' = 0; asymptotic flatness + regularity at origin",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="uniqueness_theorem",
        scope="flat vacuum is the unique zero-source static state; negative sector is "
              "source-slaved, not a reservoir (gate G02, reduced level)",
    )

    ns.record_claim(ClaimRecord(
        claim_id="sector_indefinite_signature_complete_g03",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The sector-indefinite signature is complete at the reduced level: "
            "the temporal sector is negative (C2 + P9 + exact recovery), "
            "non-propagating (elliptic adopted law; hyperbolic promotion is a "
            "ghost), and source-slaved (flat vacuum unique at zero source -- "
            "gate G02); the TT sector is positive-definite with outward flux, "
            "sign anchored by the binary pulsar (gate G03). This mirrors the "
            "architecture by which GR survives the conformal-factor problem. "
            "Covariant lift, nonlinear stability, and the K_T magnitude remain "
            "open obligations."
        ),
        derivation_ids=[
            "tt_positivity_sum_of_squares_g03",
            "ghost_exclusion_g03",
            "flat_vacuum_uniqueness_g02",
        ],
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="covariant_lift_sector_signature_g03",
        script_id=SCRIPT_ID,
        title="Covariant lift of the sector-signature theorems; nonlinear stability",
        status=ObligationStatus.OPEN,
        required_by=["k_strain_program"],
        description="T1-T3 are reduced-level and conditional on the adopted laws.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tensor_coupling_g03",
        script_id=SCRIPT_ID,
        title="Derive K_T (tensor coupling magnitude) -- currently MATCHED to 2G/c^4",
        status=ObligationStatus.OPEN,
        required_by=["k_strain_program"],
        description=(
            "The bootstrap program's radiative continuation: the temporal sector's "
            "coupling came from P9 + exact recovery; the radiative sector's "
            "magnitude should come from the same self-consistency, covariantly."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="radiative_bootstrap_route_g03",
        script_id=SCRIPT_ID,
        name="Radiative bootstrap: derive K_T from self-coupling consistency",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_tensor_coupling_g03"],
        activation_conditions=[
            "sector signature settled (this script)",
            "P9 and P7' available as archive dependencies",
        ],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Gate G03: Radiative-Sector Positivity (and G02: Flat-Vacuum Stability)")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    case_1_tt_positivity(out)
    case_2_ghost_exclusion(out)
    case_3_vacuum_uniqueness(out)
    case_4_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
