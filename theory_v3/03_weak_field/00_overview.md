# 03 — Weak Field: Overview

**What this folder is:** the classical-test recovery chain (T5–T9),
showing that the framework's static exterior reproduces the weak-field
phenomenology of GR — written when this recovery was the open question,
before the field equations existed.

**What the proofs are:**

| theorem | recovers | classical anchor |
|---|---|---|
| T5 (static exterior weak-field metric) | the 1PN exterior metric | — |
| T6 (Newtonian limit) | Newtonian gravity | everything |
| T7 (light deflection) | 1.75″ at the solar limb | Eddington-class |
| T8 (Shapiro delay) | radar echo delay | Cassini-class |
| T9 (perihelion precession) | 43″/century for Mercury | classical |

**What the proofs are not:**

- They are **not independent evidence anymore**: the full field
  equations (`04_field_equations/`) are now derived, and every recovery
  here is a corollary of them. The folder's value is historical and
  pedagogical — it shows the *minimal* commitments (P7′'s shadow + the
  P8-content) that already pin the weak field, well before the full
  equations were available.
- They are **not conditional on standalone P7/P8** in the current
  theory: P7 is the metric shadow of adopted P7′ (Trial C3), and P8 is
  a theorem under P9 + the C2 bootstrap. The original conditional
  language is retained in the proof texts; read it with the
  substitutions "P7 → P7′ (via C3)" and "P8 → P9 + C2". See the banner
  on `summary_weak_field_gr_recovery.md` and the renamed postulate
  files in `01_postulates/`.
- They do **not** exhaust the tests: frame dragging (GPB/LAGEOS-class),
  gravitational-wave energy loss (binary-pulsar-class), and strong-field
  statics are covered by the full equations — see
  `04_field_equations/01_the_field_equations.md` (coefficient table with
  kill-condition anchors).

**Where the story continues:** `04_field_equations/proof.md` for the
direct derivation these recoveries are corollaries of (the weak-field
tests appear there as §6 kill-condition corollaries);
`04_field_equations/01_the_field_equations.md` for the equations and
coefficient table; `02_derivation_chain.md` there for the full
postulates-to-equations chain.
