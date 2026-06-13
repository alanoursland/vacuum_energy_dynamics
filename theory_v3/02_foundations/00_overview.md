# 02 — Foundations: Overview

**What this folder is:** the framework's first theorem chain (T1–T4),
built directly on the postulates before any field equations existed.
Each file is a self-contained derivation with its dependencies stated.

**What the proofs are:**

| theorem | establishes | depends on |
|---|---|---|
| T1 (gravitational redshift) | first-order temporal mapping from energy bookkeeping | P1–P6 |
| T2 (time dilation) | observer-level consequence of T1 | T1 |
| T3 (reciprocal exterior scaling) | AB = 1 in static source-free exteriors | **P7′** (via its shadow; see banner in the file) |
| T4 (second-order temporal self-coupling) | $d\ln\alpha = -dU/c^2$, no independent $U^2/c^4$ term | **P9 + the C2 bootstrap** (P8 demoted to theorem; see banner) |

**What the proofs are not:**

- They are **not field equations** and never claimed to be: each is a
  restricted structural result in the static, source-free exterior
  regime.
- They are **not superseded**: the admitted field equations
  (`04_field_equations/`) *subsume* them — every T-result is now also a
  corollary of the full equations — but the chains here remain the
  postulate-level derivations and show which commitment carries which
  result.
- They are **no longer conditional on standalone P7/P8**: those two
  postulates changed status during the trials program (P7 → shadow of
  adopted P7′; P8 → theorem under P9). The proof texts retain their
  original conditional framing for fidelity; the banners at the top of
  T3 and T4 give the correct modern reading. The dependency-bearing
  files are `01_postulates/shadow_p7_static_exterior_vacuum_compensation.md`
  and `01_postulates/demoted_p8_static_exterior_temporal_self_coupling.md`.

**Where the story continues:** the direct, self-contained derivation of
the full field equations (with these foundations folded in as §2's
bookkeeping sector) is `04_field_equations/proof.md`; the chain map is
`04_field_equations/02_derivation_chain.md`; the trials notebook that
built it is `development/field_equation_trials/`.
