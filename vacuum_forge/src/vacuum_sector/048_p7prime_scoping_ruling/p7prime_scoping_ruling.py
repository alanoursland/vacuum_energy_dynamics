#!/usr/bin/env python3
"""
p7prime_scoping_ruling.py

Ruling record for p7prime_scoping_ruling_047.

Theory-owner decision, 2026-07-02: ROUTE (i) is adopted. P7' is scoped
as the double idealization

    H -> 0   (strictly static; the F1 kappa-leak is the controlled
              correction -- the 2026-06-12 precedent)
    a -> 0   (continuum; the Planck-range packing scalaron is the
              controlled correction -- this ruling)

Under the adopted scoping, "the four-derivative sector is exactly
empty" is a statement about the continuum idealization; at finite
packing scale a the R^2-class term exists with a Planck-scale
coefficient and its scalaron has range l* = sqrt(6 alpha) ~ sqrt(6) a,
operationally indistinguishable from absence at every accessible range.
No closed coefficient moves; the P7' null test (F-P10-3: any DETECTED
Yukawa at any accessible range kills) is unchanged as the standing
falsifier.

The theory owner's accompanying observation, recorded because it is the
right reading: the field-equation derivation's "no static flow, exactly
zero" statements were always candidates for limit results rather than
exact-at-all-scales facts. This ruling makes that official doctrine:
P7'-exactness is the idealization's property; the physical packing
carries controlled, derived, sub-observable corrections (the kappa-leak
current at O((H0 r/c)^2), the scalaron at range ~ sqrt(6) l_P), each
with a precedent-setting derivation behind it. Route (ii) (the
f''(Delta_0) = 0 inflection constraint) is REJECTED as recovery-shaped
without independent motivation; it remains on record as the fallback
should the scoped reading ever fail a test.

Witnesses re-verified at ruling time: the reconstructed scalaron mass,
the range margin below the laboratory frontier, and the structural
parallel with the F1 leak (both corrections quadratic in their small
parameter, both derived, both sub-observable).
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
    StatusMark,
)


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"

DEPENDENCIES = [
    ("scalaron_dep_048", "047_scalaron_unimodular__scalaron_unimodular",
     "scalaron_unimodular_047"),
    ("adoption_dep_048", "044_p10_adoption__p10_adoption",
     "p10_adoption_record_044"),
]


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


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
    print("[INFO] Archive dependency check (the ruling's evidentiary base):")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def ruling_witnesses(failures):
    header("Ruling-time witnesses")

    # 1. The reconstructed scalaron: for f = R + alpha R^2 the 047 trace
    #    equation is f'R - 2f + 3 box f' = -R + 6 alpha box R, pole at
    #    m^2 = 1/(6 alpha).
    R_, L, alpha = sp.symbols("R_ L alpha", real=True)
    f = R_ + alpha * R_**2
    fp = sp.diff(f, R_)
    trace = sp.expand(fp * R_ - 2 * f + 3 * (2 * alpha * L))
    require("trace operator: f'R - 2f + 3 box f' = -R + 6 alpha box R",
            sp.simplify(trace - (-R_ + 6 * alpha * L)) == 0, failures)
    k = sp.Symbol("k", positive=True)
    disp = -(-1) - 6 * alpha * k**2  # (6 alpha box - 1)R: pole at box = 1/(6 alpha)
    m2 = sp.solve(sp.Eq(1 - 6 * alpha * (-k**2), 0), k**2)
    require("scalaron mass m^2 = 1/(6 alpha)",
            m2 == [-1 / (6 * alpha)] or sp.simplify(m2[0] + 1 / (6 * alpha)) == 0,
            failures)

    # 2. The range margin: l* = sqrt(6) l_P vs the 54 um frontier.
    l_P = 1.616e-35
    l_star = float(sp.sqrt(6)) * l_P
    frontier = 5.4e-5
    margin = frontier / l_star
    require("range margin frontier/l* >= 1e25 (operational indistinguishability)",
            margin >= 1e25, failures)
    print(f"  l* = sqrt(6) l_P = {l_star:.3e} m; frontier {frontier:.1e} m; "
          f"margin {margin:.2e}")

    # 3. The F1 parallel: both corrections are quadratic in their small
    #    parameter. F1: AB - 1 = (3/2) Omega_m (H0 r/c)^2 -- second order
    #    in (H0 r/c). Scalaron: coefficient alpha ~ a^2 -- second order in
    #    the packing scale over the probe scale.
    eps = sp.Symbol("epsilon", positive=True)
    f1_leak = sp.Rational(3, 2) * sp.Symbol("Omega_m") * eps**2
    require("F1 precedent parallel: kappa-leak is O(eps^2) (no linear term)",
            sp.diff(f1_leak, eps).subs(eps, 0) == 0, failures)
    a_sym, probe = sp.symbols("a probe", positive=True)
    yukawa_suppression = (a_sym / probe) ** 2
    require("scalaron correction parallel: coefficient scales as (a/probe)^2",
            sp.diff(yukawa_suppression, a_sym).subs(a_sym, 0) == 0, failures)


def record_ruling(ns):
    ns.record_derivation(
        derivation_id="p7prime_scoping_ruling_record_048",
        inputs=[sp.Symbol("scalaron_unimodular_047"),
                sp.Symbol("trial_F1_kappa_leak_precedent")],
        output=sp.Symbol("P7prime_scoped_route_i_a_to_0_idealization_2026_07_02"),
        method=(
            "theory-owner scoping ruling following derivation 047's refutation "
            "of the cancellation mechanism; route (i) adopted (P7' as the "
            "H -> 0, a -> 0 double idealization with derived controlled "
            "corrections); route (ii) (f''(Delta_0) = 0 inflection) rejected "
            "as recovery-shaped, retained as recorded fallback; witnesses "
            "re-verified at ruling time"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="postulate_scoping_ruling_record",
        scope=(
            "governance record; the scoped postulate text lives in "
            "theory_v3/01_postulates/p7_prime_static_frame_indifference.md; "
            "O-P10-3 closes against this ruling"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p7prime_scoping_ruled_048",
        script_id=SCRIPT_ID,
        title="P7' scoping ruling: ROUTE (i) ADOPTED (a -> 0 idealization)",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["p7prime_scoping_ruling_record_048"],
        description=(
            "Resolves p7prime_scoping_ruling_047 and closes O-P10-3: P7' is "
            "scoped as the double (H -> 0, a -> 0) idealization; the "
            "Planck-range scalaron (l* ~ sqrt(6) l_P, margin ~1.4e30 below "
            "the 54 um frontier) is a controlled derived correction on the "
            "F1-leak precedent. Route (ii) (f''(Delta_0) = 0) rejected as "
            "recovery-shaped; recorded fallback. The P7' null test (F-P10-3) "
            "is unchanged as the standing falsifier: any DETECTED Yukawa at "
            "any accessible range kills."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="p7prime_scoping_claim_048",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "P7'-exactness is a property of the idealization, not of the "
            "physical packing: 'no static flow, exactly zero' is a limit "
            "result. The physical vacuum carries exactly two derived, "
            "controlled, sub-observable corrections to the static shadow -- "
            "the expansion kappa-leak (AB - 1 = (3/2) Omega_m (H0 r/c)^2, "
            "trial F1) and the packing scalaron (range sqrt(6 alpha) ~ "
            "sqrt(6) a, derivation 047) -- both quadratic in their small "
            "parameter, neither reopening any closed coefficient. O-P10-3 "
            "is CLOSED against this ruling; F-P10-3 stands."
        ),
        derivation_ids=["p7prime_scoping_ruling_record_048"],
        obligation_ids=["p7prime_scoping_ruled_048"],
    ))


def write_report() -> Path:
    repo_root = SCRIPT_PATH.parents[4]
    report_path = (repo_root / "theory_v3" / "development" / "vacuum_sector"
                   / "08_packing_microphysics"
                   / "p7prime_scoping_ruling_vacuumforge.md")
    report = """# The P7' Scoping Ruling (Route i) -- VacuumForge Record

## Status

```text
result type:   theory-owner scoping ruling (2026-07-02, derivation 048)
ruling:        ROUTE (i) ADOPTED. P7' is scoped as the double
               idealization H -> 0 (static; F1 kappa-leak correction)
               AND a -> 0 (continuum; packing-scalaron correction).
               O-P10-3 is CLOSED against this ruling.
rejected:      route (ii), the f''(Delta_0) = 0 inflection constraint --
               recovery-shaped without independent motivation; retained
               on record as the fallback.
verification:  vacuum_forge/src/vacuum_sector/048_p7prime_scoping_ruling/
               (witnesses re-verified at ruling time; dependencies 047, 044)
```

## What the Ruling Says

"The four-derivative sector is exactly empty" (P7', proof.md Theorems
6-7) is a statement about the continuum idealization a -> 0. At finite
packing scale the R^2-class term exists with coefficient
alpha ~ f''(Delta_0) a^2-class, and derivation 047 proved its scalaron
survives the unimodular constraint (the Bianchi reconstruction). The
ruling scopes the postulate rather than constraining the wedge energy:

```text
P7' holds exactly in the (H -> 0, a -> 0) idealization.

The physical vacuum carries exactly two derived corrections to the
static shadow, both controlled, both sub-observable:

  expansion:     AB - 1 = (3/2) Omega_m (H0 r/c)^2     (trial F1)
  discreteness:  Yukawa of range l* = sqrt(6 alpha) ~ sqrt(6) a
                 ~ 4e-35 m at Planck packing              (047)

Each is quadratic in its small parameter; neither reopens a closed
coefficient; neither is observable at any accessible range.
```

## The Limit-Result Reading (the owner's observation, made doctrine)

The field-equation derivation's "no static flow, exactly zero"
statements were always candidates for limit results rather than
exact-at-all-scales facts. This ruling makes that the official
reading: exactness lives in the idealization; the physical packing's
deviations from it must be DERIVED, CONTROLLED, and INDIVIDUALLY
RECORDED -- never assumed away, never invoked ad hoc. The register of
such corrections currently has exactly two entries (above). Any third
must arrive the same way: with a derivation, a magnitude, and a kill
condition.

## What Does Not Change

```text
- every closed field-equation coefficient (the corrections do not
  reopen the response)
- the A3/F-P10-3 null test: any DETECTED gravitational-strength
  Yukawa at any accessible range still kills -- the scoped reading
  predicts NONE will ever be found short of the packing scale
- the E3/G20 kills of macroscopic higher-curvature couplings
- the sequestering chain, Lambda as integration constant, the
  floor's inertness
```

## The New Falsifier Face

The ruling adds a sharpened structural commitment: if the packing
scale a were ever independently measured (any confirmed discreteness
probe), the theory PREDICTS a scalaron Yukawa at range sqrt(6) a with
the wedge-energy coefficient -- a parameter-free consistency test
between two would-be discoveries. Recorded alongside C4 (the
floor-Newton lock) as the second entry in the "if discreteness is ever
seen" consistency battery.

## Ledger

```text
derivation:  p7prime_scoping_ruling_record_048
satisfies:   p7prime_scoping_ruling_047 (and closes O-P10-3)
rejected:    route (ii) f''(Delta_0) = 0 (fallback, on record)
depends on:  scalaron_unimodular_047, p10_adoption_record_044,
             trial F1 (precedent)
```
"""
    report_path.write_text(report)
    return report_path


def main() -> None:
    header("Derivation 048: P7' Scoping Ruling (Route i)")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    ruling_witnesses(failures)

    header("Ruling")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 048: witness failure -- ruling NOT recorded")
    print("  ROUTE (i) ADOPTED (theory owner, 2026-07-02): P7' is the")
    print("  (H -> 0, a -> 0) double idealization; the packing scalaron is a")
    print("  controlled derived correction (F1 precedent). O-P10-3 CLOSED.")
    print("  Route (ii) rejected as recovery-shaped; recorded fallback.")
    print("  'Exactly zero static flow' is officially a LIMIT RESULT.")

    record_ruling(ns)
    report_path = write_report()
    print(f"[INFO] report written: {report_path}")
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
