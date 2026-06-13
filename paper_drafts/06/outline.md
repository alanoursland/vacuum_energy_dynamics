# Paper 6 Outline: Static Frame Indifference Excludes Scalaron Hair

## Working Title

**`g_tt g_rr = -1` as a Selection Principle: Frame Indifference Forces
`f(R) = R`**

Shorter title option:

**Static Frame Indifference Excludes Scalaron Hair**

## Target Venues

Primary:

- arXiv gr-qc short note.

Journal possibilities:

- Physical Review D Brief Report.
- Classical and Quantum Gravity Letter.

Decision gate:

This should become a standalone paper only if the novelty check passes.
Otherwise it should be a theorem section inside Paper 1.

## Central Claim

In `R + a R^2` gravity, any nonzero `a` produces mandatory static scalaron
hair outside a sourced body. That hair carries intrinsic temporal-radial
anisotropy and therefore violates static frame indifference, whose metric
shadow is `g_tt g_rr = -1` in areal gauge. Therefore static frame
indifference forces `a = 0`, selecting `f(R) = R` plus Lambda from the
healthy local `f(R)` family.

## Intended Reader

Modified-gravity and f(R) researchers.

This paper should be written almost entirely in standard f(R) language.
VED should appear only as motivation for the principle of static frame
indifference, not as a prerequisite.

## Abstract Skeleton

We show that a static frame-indifference condition selects the
Einstein-Hilbert action from the healthy `R + a R^2` extension. In
areal-radius gauge, static frame indifference is represented by
`g_tt g_rr = -1`, or equivalently the absence of a preferred temporal-
radial frame in static vacuum. The higher-derivative scalar response of
`R + a R^2` carries an intrinsic anisotropy,
`D^t_t - D^r_r = -R''`, whenever the scalar curvature profile is
nontrivial. We then show that for a sourced static body, fourth-order
matching conditions force nontrivial exterior scalaron hair for every
`a != 0`; the would-be hairless condition reduces to
`x cosh x = sinh x`, which has no positive solution. Thus every nonzero
`a` violates static frame indifference around ordinary sources. The only
allowed value is `a = 0`, leaving Einstein gravity with a cosmological
term. If the principle is dropped, existing short-range Yukawa tests bound
the scalaron range; if the principle is kept, the prediction is a null
Yukawa channel at gravitational strength.

## Section Plan

### 1. Introduction

Purpose:

- State the problem: f(R) gravity introduces scalar degrees of freedom.
- Observational constraints usually bound the scalaron; this note gives a
  principle that eliminates it.
- Define static frame indifference in physical terms.

Need:

- careful novelty positioning after literature pass.

### 2. Static Frame Indifference

Goal:

State the selection principle independently of VED.

Definition:

A strictly static vacuum exterior should carry no energy current and no
preferred frame in the temporal-radial plane.

Metric shadow in static spherical areal gauge:

```text
g_tt g_rr = -1
```

or, with metric functions,

```text
A(r) B(r) = 1.
```

Clarify:

- This is not a coordinate gauge condition once areal radius is fixed.
- It is a physical restriction on static vacuum response.
- Schwarzschild and Schwarzschild-de Sitter satisfy it.

### 3. `R + a R^2` Field Equations and Scalaron Mode

Content:

- Write action:

```text
S = c^4/(16 pi G) int sqrt(-g) (R + a R^2 - 2 Lambda) + S_matter.
```

- State scalaron mass/range:

```text
m^2 = 1/(6a),    ell = sqrt(6a)
```

for `a > 0`.

- Note `a < 0` is tachyonic/unstable and not the target.

### 4. Anisotropy Lemma

Goal:

Show any nontrivial scalaron profile violates static frame indifference.

Core result:

```text
D^t_t - D^r_r = -R''
```

up to the paper's exact conventions.

Interpretation:

- nonzero static scalar curvature profile creates temporal-radial stress
  anisotropy;
- anisotropy identifies a preferred t-r frame;
- in areal gauge, this appears as `AB != 1` wherever hair contributes.

Assumed by writing time:

- final convention-correct expression for the anisotropy equation.

### 5. Exterior Scalaron Solution

Goal:

Write the exterior hair profile and connect it to Yukawa form.

Content:

- source-free scalaron equation outside matter;
- regular asymptotically flat/de Sitter-compatible solution;
- Yukawa tail:

```text
R_ext ~ C exp(-r/ell) / r
```

or equivalent.

Clarify:

- the coefficient `C` is determined by interior matching;
- hairless exterior means `C = 0`.

### 6. Mandatory-Hair Lemma

Goal:

Prove `C = 0` is impossible for a nontrivial sourced body when `a != 0`.

Core matching:

- fourth-order equations require continuity of `R` and `R'` at the
  surface;
- imposing hairless exterior forces a condition equivalent to:

```text
x cosh x = sinh x
```

for `x > 0`.

Proof:

```text
h(x) = x cosh x - sinh x
h(0) = 0
h'(x) = x sinh x > 0 for x > 0
```

Therefore no positive root exists. Hair is mandatory.

Assumed by writing time:

- final statement of source model and matching assumptions;
- extension or caveat for realistic smooth density profiles.

### 7. Selection Theorem

Combine:

1. Any `a != 0` sourced star has exterior scalaron hair.
2. Any exterior scalaron hair violates static frame indifference.
3. Static frame indifference is the selection principle.

Therefore:

```text
a = 0.
```

Conclusion:

Within the healthy local `R + aR^2` family, static frame indifference
selects Einstein-Hilbert plus Lambda.

### 8. Relation to Existing f(R) No-Hair and Screening Literature

Goal:

Position carefully.

Topics:

- known f(R) star exteriors;
- known `g_tt g_rr != -1` behavior;
- chameleon/thin-shell suppression;
- scalar-tensor equivalence;
- no-hair theorems and their assumptions.

Novelty to claim only if literature supports it:

- mandatory-hair lemma in this sharp root-condition form;
- frame indifference as an exact selection principle;
- `a = 0` selected before experimental bound fitting.

### 9. Phenomenological Corollary: Yukawa Null Test

Content:

- If `a` is allowed, scalaron gives a gravitational-strength Yukawa
  correction with fixed coupling convention, e.g. alpha = 1/3.
- Existing short-range tests bound range.
- Lee 2020 vector-extracted alpha = 1/3 crossing: 54.05 micrometers.
- Static frame indifference predicts no such gravitational-strength
  Yukawa at any range.

Careful phrasing:

- experimental data are not used to select `a = 0`;
- data show where the principle is already being tested.

### 10. Discussion

Questions:

- Is static frame indifference too strong?
- What kinds of theories evade the theorem?
- What about nonlocal gravity, screening environments, nonstatic sources,
  rotation, cosmology?
- What would count as an appeal or carve-out?

### 11. Conclusion

Close:

The scalaron is not merely constrained by experiment. Under static frame
indifference, it is forbidden: any nonzero `R^2` coefficient produces
mandatory static hair, and mandatory hair violates the principle.

## Figures and Tables

- Figure 1: logic flow from `a != 0` to hair to anisotropy to violation.
- Figure 2: schematic scalaron exterior profile and `AB != 1` region.
- Table 1: assumptions and theorem roles.
- Table 2: literature positioning / known vs claimed-new statements.
- Table 3: Yukawa bounds and alpha = 1/3 crossing.

## Appendices

- Appendix A: derivation of anisotropy lemma.
- Appendix B: scalaron matching calculation.
- Appendix C: proof that `x cosh x = sinh x` has no positive root.
- Appendix D: Yukawa parameter translation.
- Appendix E: verification script index.

## Claims To Avoid

- Do not claim all modified gravity is ruled out.
- Do not claim f(R) hair is unknown in general.
- Do not imply experiments are the reason for `a = 0`.
- Do not make VED ontology necessary for the theorem once the principle is
  stated.

## Claims To Emphasize

- The selection is principle-based, not fit-based.
- Mandatory hair plus frame indifference is the core contradiction.
- Schwarzschild/SdS satisfy the principle exactly.
- A gravitational-strength Yukawa detection would falsify the principle.

## Assumed Missing Pieces By Writing Time

1. Literature novelty check.
2. Convention-clean anisotropy derivation.
3. Matching theorem stated for an acceptable source class.
4. Yukawa parameter translation checked.
5. Citation-ready Lee 2020 extraction provenance.
6. Decision: standalone note or absorbed into Paper 1.
