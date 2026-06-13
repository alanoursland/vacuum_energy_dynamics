# Paper 2 Outline: Gravity's Sector-Indefinite Signature

## Working Title

**Gravity's Sector-Indefinite Signature from a Self-Consistency
Bootstrap: Why the Negative Mode Cannot Propagate and Cannot Be Mined**

Shorter title option:

**Why Gravity's Negative Mode Is a Constraint**

## Target Venues

Primary target: American Journal of Physics or European Journal of
Physics, if framed as a pedagogical structural note.

Fallback / parallel target: arXiv gr-qc as a standalone technical note.

The paper should not require acceptance of the full Vacuum Energy
Dynamics ontology. It should present a minimal bootstrap argument whose
output matches the familiar GR architecture: a negative static/conformal
sector, a positive radiative sector, and a constraint that prevents the
negative sector from becoming a propagating ghost.

## Central Claim

A gravitational theory that contains all three ingredients:

1. a second-order static response with self-sourced field energy,
2. universal gravitation of configuration/field energy counted once,
3. stability of the vacuum,

is forced into a sector-indefinite architecture:

- the static scalar/temporal sector carries negative field energy,
- that negative sector cannot be promoted to a propagating mode,
- the source-free static sector is source-bound and cannot be mined,
- the propagating transverse-traceless sector is positive,
- the radiative normalization is fixed only after self-coupling is
  included.

This gives a clean answer to the conformal-factor puzzle: the wrong-sign
sector is not a physical radiative degree of freedom. It is a constraint.

## Intended Reader

The primary reader is a GR instructor, advanced undergraduate, beginning
graduate student, or theorist who knows the conformal-factor problem but
has mostly seen it handled as a formal feature of the ADM/Hamiltonian
constraint structure.

The paper should make the result feel calculationally elementary:
one static spherical bootstrap, one Hamiltonian sign argument, one
source-free uniqueness argument, and one radiative positivity argument.

## Framing Constraint

Do not lead with the full VED ontology. Lead with the general problem:

> Gravity appears to contain a negative-energy scalar/static sector.
> Why does that not make the theory catastrophically unstable?

Then show that the answer follows from self-consistency. VED appears as
the derivation source and provenance archive, not as a prerequisite for
the reader.

## Abstract Skeleton

General relativity contains an indefinite gravitational energy
architecture: the static/conformal sector has the wrong sign, while
radiative transverse-traceless modes carry positive energy. This note
gives a compact derivation of why such an architecture is stable. Starting
from a static self-coupling bootstrap, the gravitational field energy in
the scalar/static sector is forced to be negative,
`u = -c^4(s')^2/(8 pi G)`. If this sector is promoted to a hyperbolic
degree of freedom, its Hamiltonian is unbounded below; stability therefore
forces it to be elliptic/constraint-type. The source-free constraint
equation has flat space as its unique regular asymptotically flat
solution, so the negative reservoir is source-bound and cannot be mined.
The transverse-traceless sector is then the only propagating sector and
has positive definite energy. A final normalization argument shows why
linear radiation theory alone cannot fix the gravitational-wave kinetic
coefficient, while the second-order self-coupled bootstrap can. The result
is a short, verifiable derivation of the sector assignment that makes
gravity stable despite an indefinite energy signature.

## Section Plan

### 1. Introduction: the puzzle

Goal: state the conformal/static-sector problem without relying on VED
jargon.

Content:

- In field theories, a negative-energy propagating mode is normally fatal.
- Gravity appears to contain a wrong-sign scalar/static sector.
- GR survives because the dangerous sector is constrained rather than
  radiative.
- The paper asks: can this assignment be derived from a simple
  self-consistency argument?

Deliverable:

- A one-paragraph preview of the answer:
  negative static energy is forced; propagation is forbidden by stability;
  source-free flatness prevents mining; TT waves carry the positive
  radiative energy.

Avoid:

- claims that the paper derives all of GR;
- detailed ontology of vacuum substance;
- strong philosophical claims.

### 2. Minimal assumptions and notation

Goal: give the reader the smallest setup needed for the proof.

Assumptions:

1. Static spherical exterior response can be described by metric factors
   `A(r)` and `B(r)`, with shear variable
   `s = (1/2) ln(A/B)`.
2. The source-free static exterior obeys a second-order areal-flux law in
   the self-coupled variable.
3. Field/configuration energy gravitates universally and is counted once.
4. Stable vacuum means no propagating Hamiltonian sector may be unbounded
   below.
5. Propagating radiation is the transverse-traceless sector of a massless
   spin-2 perturbation.

Definitions:

- `Delta_areal f = (r^2 f')'/r^2`.
- `A = e^s` in the static compensated exterior.
- `u_field` is the local static field-energy density inferred by the
  self-coupling identity.

Assumed by writing time:

- crisp derivation of `AB = 1` from static frame indifference, or a
  paper-local statement that the static compensated sector is the setting
  under analysis;
- clean notation bridge between areal coordinates and weak-field
  perturbation notation.

### 3. Static bootstrap: why the scalar/static energy is negative

Goal: derive the sign, not merely state it.

Core calculation:

For the self-coupled static variable,

```text
Delta_areal(e^s) = e^s [Delta_areal s + (s')^2].
```

If the areal-flux law is linear in `A = e^s`, then the vacuum shear
equation contains

```text
Delta_areal s = -(s')^2.
```

Reading the nonlinear term as universal self-sourcing gives

```text
u_field = -c^4 (s')^2 / (8 pi G).
```

Points to make:

- The negative sign is not a convention; it is selected by the
  self-coupling identity.
- A positive explicit scalar source would break static frame indifference
  / compensated exterior structure.
- This is the static analogue of the conformal-factor wrong sign.

Expected equation block:

1. areal flux law,
2. exponential identity,
3. shear equation,
4. field-energy density,
5. exact exterior as optional corollary.

Verification/provenance:

- Trial C2 self-coupling bootstrap.
- Trial C3 placement exclusion.

### 4. Ghost exclusion: why the negative sector cannot propagate

Goal: turn the sign result into the constraint assignment.

Argument:

Assume, for contradiction, that `s` is a propagating hyperbolic field with
energy density proportional to `-(dot s^2 + |grad s|^2)` or equivalent
wrong-sign Hamiltonian structure. Then scaling a compact field
configuration by `lambda` gives

```text
H[lambda s] = lambda^2 H[s] -> -infinity
```

for any negative-energy witness. Coupled to positive radiative modes, this
would allow unbounded decay. Stability therefore forbids hyperbolic
propagation for the negative sector.

Conclusion:

The negative static/conformal sector must be elliptic: it is solved from
sources as a constraint, not evolved as an independent wave.

Important phrasing:

- This is not "negative energy is harmless."
- It is "negative energy is harmless only because it is non-propagating
  and source-bound."

Verification/provenance:

- G03/T2 ghost exclusion.

### 5. Source-bound constraint: why the negative reservoir cannot be mined

Goal: answer the obvious objection that a static negative-energy field
could still be exploited.

Core theorem:

The source-free static equation

```text
(r^2 A')' = 0
```

with regularity and asymptotic flatness has the unique solution

```text
A = 1.
```

Therefore the negative static sector has no independent source-free
configuration to extract from. It exists only as a functional of sources.
To change it, one must move or change sources; the energy bookkeeping then
runs through the positive radiative/dynamical channel.

Points to make:

- No source, no well.
- No independent well, no mineable reservoir.
- The "negative field energy" is real in the static ledger but not a free
  thermodynamic fuel.

Verification/provenance:

- G02 flat-vacuum uniqueness / source-binding result.

### 6. Radiative positivity: what is allowed to propagate

Goal: show that the propagating sector is safe and has the expected sign.

Setup:

- Decompose perturbations into constrained scalar/static content and
  transverse-traceless radiative content.
- The TT sector carries the physical waves.

Core result:

```text
<u_TT> = c^2/(32 pi G) <dot h_ij dot h_ij>
```

up to convention and polarization normalization, with outward null flux.

Points to make:

- The energy density is a sum of squares.
- Flux equals `c` times energy density for outgoing radiation.
- This is exactly the sector that may propagate without instability.

Verification/provenance:

- G03 radiative positivity.
- 008 radiative bootstrap.

### 7. The normalization gap: why linear theory cannot fix `K_T`

Goal: include the "pedagogical nugget" that makes the paper more than a
sign argument.

Claim:

At linear order, the radiative kinetic normalization `K_T` is physically
present but underdetermined. Amplitude and flux scale so that work-flux
balance holds for every `K_T`; the linear theory cannot select the
coefficient.

Suggested derivation:

- Write a schematic wave equation:

```text
K_T Box h = source.
```

- Then `h ~ source / K_T`.
- Radiative flux is `K_T dot h^2`, hence scales as `source^2 / K_T`.
- Work done on sources scales the same way.
- Therefore linear balance checks cannot determine `K_T`.

Then:

- P9/self-coupling at second order fixes the normalization.
- The derived value is

```text
K_T = c^4/(16 pi G)
```

per the paper's convention, yielding the standard quadrupole coefficient.

Verification/provenance:

- 008 T1-T4 radiative bootstrap.

### 8. The complete sector architecture

Goal: assemble the result in a compact table.

Table columns:

- sector,
- sign,
- dynamical character,
- why it has that character,
- observational/physical role.

Rows:

- static scalar/shear: negative, elliptic constraint, source-bound;
- TT radiation: positive, hyperbolic propagating, carries waves;
- vector/momentum sector: constraint-sourced, bounded/magnetic-type;
- trace/kappa sector: suppressed in static vacuum by frame indifference.

Main text:

- The architecture is sector-indefinite, not positive definite.
- Stability comes from assigning the indefinite sectors correctly.
- This mirrors GR's Hamiltonian-constraint resolution of the conformal
  factor problem, but the paper derives it from the bootstrap logic.

### 9. Relation to standard GR treatments

Goal: position the paper honestly.

Points:

- Standard GR already has the relevant architecture.
- ADM/Hamiltonian formulations show that the conformal mode is
  constrained.
- This paper's contribution is a compact derivation path from
  self-coupling, sign, and stability, with machine-checkable elementary
  components.

Related work to cite:

- ADM/Hamiltonian GR and the Hamiltonian constraint.
- Fierz-Pauli massless spin-2 field.
- Deser self-coupling/bootstrap route.
- Standard gravitational-wave energy derivations.
- Pedagogical discussions of the conformal-factor problem.

Assumed by writing time:

- a short literature note identifying where standard texts assert or
  derive the non-propagating conformal assignment;
- references chosen to match the target venue's style.

### 10. Verification and reproducibility

Goal: make the paper credible and reproducible without overloading the
main text.

Content:

- State that all algebraic claims have companion scripts.
- Give a table:
  - static sign/bootstrap: C2,
  - placement exclusion: C3,
  - ghost exclusion/source-binding/radiative positivity: G02/G03,
  - radiative normalization/quadrupole: 008.
- Explain that scripts re-derive from scratch and check declared
  dependencies.

For AJP/EJP:

- Put script details in an appendix or supplement.
- Keep the main text readable without requiring code execution.

For arXiv:

- Include a compact verification table in the main paper.

### 11. Conclusion

Goal: leave the reader with a simple theorem-level takeaway.

Possible closing claim:

Gravity's indefinite energy signature is not an accident and not a
pathology. The static self-coupling that gives attraction forces a
negative sector; stability then forbids that sector from propagating;
regular source-free flatness prevents it from being mined; the remaining
propagating sector is positive. This is the minimal architecture a stable
self-coupled gravitational field can have.

End with:

- connection to the larger VED derivation of Einstein's equations,
  carefully phrased as context;
- note that the present paper stands on the sector architecture alone.

## Figures

### Figure 1: Sector Architecture Diagram

Flow:

```text
self-coupling -> negative static energy
negative static energy + stability -> constraint, not radiation
constraint + source-free uniqueness -> not mineable
TT sector -> positive radiation
```

Purpose: visual map of the paper.

### Figure 2: Energy Sign and Dynamical Character

Two-by-two chart:

- negative + propagating: forbidden ghost,
- negative + constraint: allowed static gravity,
- positive + propagating: gravitational waves,
- positive + constraint: nondangerous but not central.

Purpose: make clear that the issue is not sign alone, but sign plus
dynamical character.

### Figure 3: Bootstrap Loop for `K_T`

Loop:

```text
linear wave equation -> work/flux balance underdetermined
self-coupling of wave energy -> second-order source
universal coupling -> fixes K_T
quadrupole coefficient -> observational kill condition
```

Purpose: explain why radiative normalization is not available at linear
order.

## Appendices

### Appendix A: Static Bootstrap Algebra

Include:

- areal Laplacian identity,
- one-parameter family if useful,
- sign extraction for `u_field`.

### Appendix B: Ghost Exclusion Witness

Include:

- explicit wrong-sign Hamiltonian witness,
- scaling argument,
- stability contradiction.

### Appendix C: Source-Free Uniqueness

Include:

- solution of `(r^2 A')' = 0`,
- regularity/asymptotic-flatness conditions,
- conclusion `A = 1`.

### Appendix D: Linear Underdetermination of `K_T`

Include:

- scaling of amplitude and flux with `K_T`,
- why linear work-flux balance cannot determine normalization,
- second-order bootstrap summary.

### Appendix E: Verification Scripts

Include:

- script names,
- theorem labels,
- what each script checks,
- how to run them.

## Theorem Dependency Map

```text
Static self-coupling bootstrap
  -> negative static energy
  -> ghost exclusion if promoted
  -> constraint assignment

Source-free static equation + regularity + flatness
  -> flat vacuum unique
  -> negative sector source-bound

TT decomposition + radiative energy calculation
  -> positive propagating sector

Linear underdetermination lemma + P9/self-coupling
  -> K_T fixed
  -> quadrupole coefficient fixed
```

## Claims To Avoid

- Do not claim this paper derives the full Einstein equations.
- Do not claim positivity of total gravitational energy.
- Do not claim the negative static energy is directly extractable.
- Do not claim novelty for the existence of the conformal constraint
  itself.
- Do not rely on VED-specific ontology where a standard field-theory
  statement is enough.

## Claims To Emphasize

- The sign of the static sector is derived from self-coupling.
- Stability forces the negative sector to be non-propagating.
- Source-free uniqueness prevents mining.
- TT radiation is positive.
- Linear radiation theory cannot fix its own normalization.
- The full architecture is simple enough to verify with elementary
  symbolic scripts.

## Assumed Missing Pieces By Writing Time

These are allowed assumptions for planning. If later work disproves any
one of them, the paper plan should be adjusted rather than defended.

1. A clean, paper-local derivation or statement of the static
   self-coupling bootstrap.
2. A finalized notation convention for `s`, `A`, `B`, `K_T`, and TT
   normalization.
3. A polished proof of ghost exclusion with no hidden sign convention.
4. A polished proof of source-free uniqueness / source binding.
5. A concise derivation of radiative positivity and null flux.
6. A concise derivation of the `K_T` underdetermination lemma.
7. A second-order bootstrap derivation fixing `K_T`.
8. A related-work pass on conformal-factor discussions in GR pedagogy and
   Hamiltonian GR.
9. Cleaned verification scripts and a public archive path or DOI.

## Drafting Order

1. Write Sections 3-7 first, because they are the proof core.
2. Write Appendix A-D from the verification scripts.
3. Build Figures 1-3.
4. Write Introduction and Section 9 after the proof core is stable.
5. Write the abstract last.

## One-Sentence Version

The paper shows that gravity's wrong-sign static/conformal sector is not
a pathology because self-coupling makes it negative, stability makes it a
constraint, source-free uniqueness makes it unmineable, and the only
propagating gravitational sector is positive.
