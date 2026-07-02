# Why does the vacuum's fixed density freeze the metric's volume mode?

Textbook unimodular gravity posits √(−g) = const by hand; this theory derives it from the vacuum's substance ontology.

## The idea

Unimodular gravity is a well-known variant of GR: instead of letting the full
metric vary, you fix the spacetime volume form, √(−g), to a non-dynamical
background value and only let the *shape* of the metric vary. It reproduces
GR's field equations with one twist — Λ shows up as an integration constant
of the conservation law, not a coupling in the action. The literature always
introduces this constraint as a postulate. VED's claim is that the constraint
isn't postulated here — it falls out of P3 (constant vacuum energy density),
already on the books for other reasons.

The bridge is a kinematic identity, not an analogy. In the static spherical
areal gauge used throughout the reduced program,

```text
kappa = ln( sqrt(-g) / sqrt(-g_bar) )
```

where κ = ½ln(AB) is the reduced trace/conformal mode and √(−ḡ) is the flat
fiducial volume density. This is an exact algebraic identity (direct
computation from the metric determinant −g = AB·r⁴sin²θ) — κ *is*, literally,
the log of the metric volume density relative to the fiducial one. It's not
"trace-like," it's the volume mode by definition.

So whatever fixes κ = 0 fixes √(−g) = √(−ḡ), i.e. imposes the unimodular
constraint. Three independent threads in the framework converge on κ = 0:

- **P3 itself.** "The substance's density does not vary — only its
  configuration does" is a statement about amount-per-volume. Fixing the
  vacuum's volume density *is* fixing √(−g) for the vacuum sector — that's
  what "constant density" means once P1–P2 have already identified vacuum,
  energy, and spacetime as the same substance.
- **P7′ (static frame indifference).** Its metric shadow in the static
  exterior is AB = 1, which by the identity above is exactly
  √(−g) = √(−ḡ) there.
- **The sign architecture (G02/G03).** The trace/scalar sector is
  independently forced to be non-propagating — the determinant mode carries
  no dynamics. Same content, different derivation route.

Under this restriction the metric variation is trace-free (δ√(−g) = 0), so
extremizing the Einstein–Hilbert action yields only the *trace-free* Einstein
equation, R_ab − ¼g_ab R = (8πG/c⁴)(T_ab − ¼g_ab T). That tensor satisfies
five of Lovelock's six hypotheses but fails H3 (identical divergence-freedom):
∇ᵃ(R_ab − ¼g_ab R) = ¼∇_b R ≠ 0 off shell. Conservation is restored only
on-shell, by feeding in ∇ᵃT_ab = 0 as separate input — and that on-shell step
is exactly what manufactures Λ as an integration constant downstream.

Why is this the *acceptable* symmetry break, out of Lovelock's six
hypotheses? Because it's the only one that adds no propagating degree of
freedom and no ghost — it removes a mode (the volume mode) rather than adding
one. Relaxing H1 or H2 instead (Palatini/scalar-tensor, f(R)) buys fifth
forces or Ostrogradsky ghosts; relaxing H3 in the unimodular direction buys
none of that. Local classical dynamics stays identical to GR — only Λ's
status and vacuum-energy's coupling to gravity change (see
[idea_sequestering.md](idea_sequestering.md)).

One honesty clause: the constraint is exact only in the P7′-exact limit
(static source-free exterior, pure-Λ/SdS). In a matter cosmology there's a
calculable leak, κ = O((H₀r/c)²) from the F1 result — unobservable
(~6×10⁻³¹ at 1 AU) but real, and it's the reason this is stated as a limiting
identification rather than an unconditional one.

**Proof:** forge 033 (`vacuum_forge/src/vacuum_sector/033_unimodular_lovelock_break/`) →
[../theory_v3/development/vacuum_sector/lovelock_breaks.md](../theory_v3/development/vacuum_sector/lovelock_breaks.md).

**Where next:**
- [Sequestering →](idea_sequestering.md) — the direct payoff: why the constant floor density then cancels out of the field equations exactly.
- [The substance ontology →](idea_vacuum_substance.md) — what "constant density" even means once vacuum, energy, and spacetime are the same thing.
- [Frame indifference (P7′) →](idea_frame_indifference.md) — the static-metric shadow AB = 1 that supplies half of this derivation.
- [The cosmological constant trail →](hub_lambda.md) — where this feeds into Λ becoming an integration constant, not a coupling.
