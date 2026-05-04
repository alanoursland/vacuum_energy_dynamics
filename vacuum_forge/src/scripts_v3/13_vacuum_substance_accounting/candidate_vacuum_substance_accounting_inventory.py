# Candidate vacuum substance accounting inventory
#
# Purpose
# -------
# Group 13 begins here.
#
# Group 12 ended with:
#
#   E_vac_config should be treated as a local vacuum-substance / spacetime
#   configuration variable, not as a thermodynamic bucket.
#
# The corrected ontology is:
#
#   vacuum is spacetime.
#   creating vacuum creates spacetime.
#   changing local spacetime creates curvature.
#
# Therefore the accounting variables must be geometric or explicitly
# bookkeeping-constrained.
#
# This script inventories all variables needed to make:
#
#   E_vac_config,
#   q_v,
#   J_v,
#   scalar/trace conversion,
#   relaxation exchange,
#   ordinary closed-regime conservation,
#   and active-regime separation
#
# more than a repair reservoir.
#
# This is an inventory script, not a derivation.

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "CANDIDATE": "WARN",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DERIVED_REDUCED": "PASS",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class AccountingVariable:
    name: str
    kind: str
    candidate_meaning: str
    allowed_exchange: str
    forbidden_role: str
    status: str
    missing: str
    next_test: str


def build_inventory() -> List[AccountingVariable]:
    return [
        AccountingVariable(
            name="epsilon_vac_config",
            kind="geometric / spacetime-configuration candidate",
            candidate_meaning="local vacuum-spacetime configuration energy/density; likely tied to volume-form or trace geometry",
            allowed_exchange="exchanges with e_kappa during curvature excess/deficit restoration",
            forbidden_role="bottomless energy reservoir, coefficient tuning knob, or A-sector mass charge",
            status="CANDIDATE",
            missing="geometric definition, units, measure, relation to sqrt(gamma) or kappa",
            next_test="candidate_volume_form_configuration_variable.py",
        ),
        AccountingVariable(
            name="E_vac_config",
            kind="integrated configuration functional",
            candidate_meaning="spatial or support-integrated vacuum-spacetime configuration content",
            allowed_exchange="balances integral relaxation energy in ordinary closed regime",
            forbidden_role="global repair bucket invoked only after contradictions appear",
            status="CANDIDATE",
            missing="integration measure, support, boundary terms, locality/constraint status",
            next_test="candidate_vacuum_transport_current_constraints.py",
        ),
        AccountingVariable(
            name="q_v",
            kind="bookkeeping / ontology-native density proxy",
            candidate_meaning="vacuum-substance configuration density or charge proxy",
            allowed_exchange="may track configuration change if tied to geometry",
            forbidden_role="duplicate of matter density rho or exterior mass source",
            status="STRUCTURAL",
            missing="physical/geometric meaning and relation to volume form",
            next_test="candidate_volume_form_configuration_variable.py",
        ),
        AccountingVariable(
            name="J_v",
            kind="bookkeeping / transport or constraint current",
            candidate_meaning="vacuum-substance configuration flux or redistribution current",
            allowed_exchange="may represent local/constraint redistribution of vacuum configuration",
            forbidden_role="acausal repair current or hidden radiation channel",
            status="STRUCTURAL",
            missing="transport law, causal speed or constraint status, boundary behavior",
            next_test="candidate_vacuum_transport_current_constraints.py",
        ),
        AccountingVariable(
            name="sqrt_gamma",
            kind="geometric volume-form candidate",
            candidate_meaning="spatial volume element sqrt(det gamma_ij)",
            allowed_exchange="candidate geometric recipient of vacuum creation / volume reconfiguration",
            forbidden_role="unqualified observable before slicing/frame is specified",
            status="CANDIDATE",
            missing="choice of spatial metric/slicing and relation to kappa",
            next_test="candidate_volume_form_configuration_variable.py",
        ),
        AccountingVariable(
            name="ln_sqrt_gamma",
            kind="geometric trace/volume strain candidate",
            candidate_meaning="logarithmic local volume strain; delta ln sqrt(gamma)=1/2 gamma^ij delta gamma_ij",
            allowed_exchange="candidate scalar/trace conversion variable",
            forbidden_role="duplicating A-sector scalar mass response",
            status="CANDIDATE",
            missing="background/reference volume and recombination role",
            next_test="candidate_trace_vs_tt_geometric_split.py",
        ),
        AccountingVariable(
            name="kappa",
            kind="trace / volume mismatch variable",
            candidate_meaning="non-inertial trace/volume relaxation diagnostic; AB=e^(2 kappa)",
            allowed_exchange="relaxes toward kappa_min and exchanges imbalance with epsilon_vac_config",
            forbidden_role="ordinary scalar radiation, Box kappa, or rho-sourced exterior scalar charge",
            status="STRUCTURAL",
            missing="covariant origin, u^mu, source law, relation to volume form",
            next_test="candidate_scalar_conversion_not_damping.py",
        ),
        AccountingVariable(
            name="kappa_min",
            kind="local equilibrium / target configuration",
            candidate_meaning="local vacuum-spacetime equilibrium trace/volume configuration",
            allowed_exchange="shifted by trace/pressure or effective volume imbalance",
            forbidden_role="coordinate pressure knob or scalar wave source",
            status="STRUCTURAL",
            missing="S_trace_effective and chi_kappa",
            next_test="candidate_trace_vs_tt_geometric_split.py",
        ),
        AccountingVariable(
            name="e_kappa",
            kind="local free-energy candidate",
            candidate_meaning="1/2 K_kappa (kappa-kappa_min)^2",
            allowed_exchange="monotonically decreases while epsilon_vac_config compensates",
            forbidden_role="independent kinetic/momentum reservoir for scalar waves",
            status="CANDIDATE",
            missing="K_kappa derivation, volume measure, relation to geometry",
            next_test="candidate_scalar_conversion_not_damping.py",
        ),
        AccountingVariable(
            name="Gamma_relax",
            kind="exchange/restoration term",
            candidate_meaning="internal conversion between curvature/trace imbalance and vacuum-spacetime configuration",
            allowed_exchange="moves curvature excess into vacuum configuration or pulls from it for deficits",
            forbidden_role="energy destruction, Sigma_creation, or damping without destination",
            status="CONSTRAINED",
            missing="parent balance expression and sign convention",
            next_test="candidate_vacuum_accounting_parent_balance.py",
        ),
        AccountingVariable(
            name="Sigma_exchange",
            kind="matter/vacuum exchange source candidate",
            candidate_meaning="ordinary coupling between stress-energy and vacuum-spacetime configuration",
            allowed_exchange="may encode mass accelerating across gradient / vacuum creation-destruction coupling",
            forbidden_role="free source knob or duplicate of existing A/W/TT/kappa sources",
            status="UNRESOLVED",
            missing="covariant tensor expression for coupling",
            next_test="candidate_mass_acceleration_gradient_coupling.py",
        ),
        AccountingVariable(
            name="Sigma_creation",
            kind="active-regime source",
            candidate_meaning="nonordinary creation/destruction regime outside ordinary closed gravity",
            allowed_exchange="only active-regime physics when explicitly triggered",
            forbidden_role="ordinary closed-regime relaxation or hidden nonconservation",
            status="CONSTRAINED",
            missing="active-regime trigger/exclusion law",
            next_test="candidate_vacuum_accounting_parent_balance.py",
        ),
        AccountingVariable(
            name="M_ext",
            kind="A-sector exterior charge",
            candidate_meaning="exterior mass measured by A-sector flux / 1/r coefficient",
            allowed_exchange="fixed by A-sector mass flux, not by kappa or vacuum configuration exchange",
            forbidden_role="changed by kappa relaxation, boundary smoothing, or E_vac_config",
            status="DERIVED_REDUCED",
            missing="parent flux-charge theorem",
            next_test="candidate_boundary_volume_mode_no_exterior_charge.py",
        ),
        AccountingVariable(
            name="A_flux",
            kind="scalar constraint / exterior charge functional",
            candidate_meaning="surface flux or exterior coefficient defining A-sector mass response",
            allowed_exchange="responds to rho/mass source through scalar constraint",
            forbidden_role="adjusted by trace relaxation or vacuum accounting",
            status="DERIVED_REDUCED",
            missing="parent scalar constraint propagation for moving sources",
            next_test="candidate_boundary_volume_mode_no_exterior_charge.py",
        ),
        AccountingVariable(
            name="P_trace",
            kind="projector",
            candidate_meaning="routes trace/pressure/volume imbalance to kappa_min or volume configuration",
            allowed_exchange="trace/volume conversion channel",
            forbidden_role="source of h_TT, A_rad, Box kappa, or exterior kappa charge",
            status="STRUCTURAL",
            missing="parent projector definition",
            next_test="candidate_trace_vs_tt_geometric_split.py",
        ),
        AccountingVariable(
            name="P_TT",
            kind="projector",
            candidate_meaning="routes transverse-traceless shear to tensor radiation",
            allowed_exchange="volume-preserving shear propagation",
            forbidden_role="trace/volume creation channel",
            status="STRUCTURAL",
            missing="parent TT source identity and coefficient C_T",
            next_test="candidate_trace_vs_tt_geometric_split.py",
        ),
        AccountingVariable(
            name="P_boundary",
            kind="projector / interface condition",
            candidate_meaning="preserves exterior mass and suppresses exterior kappa charge at boundaries",
            allowed_exchange="local/interface volume reconfiguration with fixed M_ext",
            forbidden_role="boundary mass tuning or exterior scalar tail",
            status="CONSTRAINED",
            missing="boundary mass theorem",
            next_test="candidate_boundary_volume_mode_no_exterior_charge.py",
        ),
        AccountingVariable(
            name="P_recombination",
            kind="projector / assembly map",
            candidate_meaning="assembles A, W_i, h_TT, and kappa into geometry without double-counting",
            allowed_exchange="counts scalar/trace response once",
            forbidden_role="GR metric copy or A/kappa duplicate mass response",
            status="UNRESOLVED",
            missing="covariant or reduced recombination identity",
            next_test="candidate_vacuum_accounting_parent_balance.py",
        ),
    ]


def print_variable(v: AccountingVariable) -> None:
    print()
    print("-" * 120)
    print(v.name)
    print("-" * 120)
    print(f"Kind: {v.kind}")
    print(f"Candidate meaning: {v.candidate_meaning}")
    print(f"Allowed exchange: {v.allowed_exchange}")
    print(f"Forbidden role: {v.forbidden_role}")
    status_line(v.name, v.status)
    print(f"Missing: {v.missing}")
    print(f"Next test: {v.next_test}")


def case_0_problem_statement():
    header("Case 0: Vacuum substance accounting inventory problem")

    print("Question:")
    print()
    print("  What variables and balances are needed to make E_vac_config / q_v / J_v")
    print("  more than a repair reservoir?")
    print()
    print("Goal:")
    print()
    print("  inventory geometric variables, bookkeeping variables, allowed exchanges,")
    print("  forbidden roles, missing definitions, and next tests")
    print()
    print("Corrected ontology:")
    print()
    print("  vacuum is spacetime")
    print("  creating vacuum creates spacetime")
    print("  changing local spacetime creates curvature")
    print()
    print("Discipline:")
    print()
    print("  name the geometry")
    print("  no bottomless bucket")
    print("  no duplicate A-sector mass")
    print("  no hidden Sigma_creation")
    print("  no coefficient tuning reservoir")

    status_line("vacuum accounting inventory problem posed", "REQUIRED")


def case_1_inventory(entries: List[AccountingVariable]):
    header("Case 1: Accounting variable inventory")
    for entry in entries:
        print_variable(entry)


def case_2_compact_table(entries: List[AccountingVariable]):
    header("Case 2: Compact accounting ledger")

    print("| Variable | Kind | Status | Forbidden role | Missing | Next test |")
    print("|---|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.kind.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.forbidden_role.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " | "
            + e.next_test.replace("|", "/")
            + " |"
        )

    status_line("compact accounting ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[AccountingVariable]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The accounting inventory is mostly structural/candidate.")
    print("  The only reduced-derived pieces are the A-sector exterior mass/flux quantities.")
    print("  The central missing definition is the geometric meaning of epsilon_vac_config.")

    status_line("accounting status count produced", "STRUCTURAL")


def case_4_geometric_vs_bookkeeping():
    header("Case 4: Geometric versus bookkeeping variables")

    print("Geometric candidates:")
    print()
    print("  epsilon_vac_config")
    print("  sqrt_gamma")
    print("  ln_sqrt_gamma")
    print("  kappa")
    print("  kappa_min")
    print()
    print("Bookkeeping candidates:")
    print()
    print("  q_v")
    print("  J_v")
    print("  E_vac_config")
    print("  Gamma_relax")
    print("  Sigma_exchange")
    print()
    print("Protected / excluded from vacuum reservoir:")
    print()
    print("  M_ext")
    print("  A_flux")
    print("  Sigma_creation in ordinary regime")
    print()
    print("Interpretation:")
    print("  The next group should prefer geometric definitions first.")
    print("  Bookkeeping variables are allowed only if tied to geometry or explicitly constrained.")

    status_line("geometric/bookkeeping split stated", "CONSTRAINED")


def case_5_no_repair_reservoir_tests():
    header("Case 5: No-repair-reservoir tests")

    print("A vacuum-substance accounting variable fails if:")
    print()
    print("1. It absorbs arbitrary contradictions.")
    print("2. It changes M_ext.")
    print("3. It duplicates rho or A_flux.")
    print("4. It acts as Sigma_creation in ordinary gravity.")
    print("5. It hides acausal J_v transport.")
    print("6. It tunes alpha_W/K_c, beta_W, C_T, or K_T.")
    print("7. It converts scalar waves into far-zone scalar radiation.")
    print("8. It makes near-boundary predictions before observables are derived.")

    status_line("no-repair-reservoir tests stated", "RISK")


def case_6_conversion_picture():
    header("Case 6: Scalar/trace conversion picture")

    print("Working picture:")
    print()
    print("  scalar/trace disturbance is not an ordinary damped wave")
    print("  scalar/trace disturbance converts into vacuum-spacetime configuration")
    print("  curvature excess deposits into vacuum configuration")
    print("  curvature deficit pulls from vacuum configuration")
    print("  TT shear is volume-preserving and may propagate")
    print()
    print("Key mathematical target:")
    print()
    print("  identify the geometric variable whose change represents vacuum/spacetime creation")
    print()
    print("Likely first candidate:")
    print()
    print("  ln_sqrt_gamma = log spatial volume element")
    print()
    print("This is a target, not a derivation.")

    status_line("conversion picture stated", "CANDIDATE")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vacuum_substance_accounting_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_volume_form_configuration_variable.py")
    print("   Test whether vacuum configuration is represented by volume form / ln sqrt gamma.")
    print()
    print("3. candidate_trace_vs_tt_geometric_split.py")
    print("   Formalize why trace/volume modes convert while TT modes propagate.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_volume_form_configuration_variable.py")
    print()
    print("Reason:")
    print("  The inventory shows the central missing definition is geometric: what is epsilon_vac_config?")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The accounting inventory says:")
    print()
    print("  E_vac_config must be geometric or tightly constrained bookkeeping.")
    print("  The best immediate geometric targets are sqrt_gamma and ln_sqrt_gamma.")
    print("  q_v/J_v remain optional bookkeeping until tied to geometry.")
    print("  M_ext and A_flux are protected A-sector quantities.")
    print("  Sigma_creation is excluded from ordinary closed accounting.")
    print("  Gamma_relax is exchange/restoration, not destruction.")
    print()
    print("Possible next artifact:")
    print("  candidate_vacuum_substance_accounting_inventory.md")
    print()
    print("Possible next script:")
    print("  candidate_volume_form_configuration_variable.py")


def main():
    header("Candidate Vacuum Substance Accounting Inventory")
    case_0_problem_statement()
    entries = build_inventory()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_geometric_vs_bookkeeping()
    case_5_no_repair_reservoir_tests()
    case_6_conversion_picture()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
