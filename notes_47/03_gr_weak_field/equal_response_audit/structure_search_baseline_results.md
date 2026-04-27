# Structure Search Baseline Results

## What This Document Is

This document reports the first structure-search investigation conducted with VacuumForge. It uses the M40 release-candidate tooling to test whether trace-free exchange — the property the candidate Exchange-Creation Separation postulate asserts — can be derived from a candidate vacuum configuration structure rather than imposed by hand.

The investigation runs five candidate vacuum-structure families through the structure analyzer, plus a sign-pattern enumeration over 2D direction space, plus a constructed example showing the kernel structure explicitly. The aim is to characterize *which* structures produce trace-free exchange and which don't, and to identify what structural property the exchange operator must satisfy.

The result advances the Equal-Response derivation problem in a specific way: the wall has not been crossed, but it has been relocated to a sharper question. What was previously "why is local exchange trace-free?" is now "why must the local exchange operator act in the trace-kernel direction of the vacuum configuration space?"

This document records the result, explains why the relocation matters, and identifies the next theoretical target.

## Background

The framework's Equal-Response problem (per `process/candidate_paths_to_equal_response.md`, `process/candidate_reciprocal_scale_equal_response.md`, `process/candidate_mismatch_energy_for_equal_response.md`, `process/candidate_exchange_creation_separation.md`, and `process/attempt_deriving_exchange_creation_separation_from_existing_postulates.md`) reached the following state through verbal analysis:

Reciprocal scaling $AB = 1$ — equivalently $\kappa = (\ln A + \ln B)/2 = 0$ — gives $\gamma_v = 1$ and closes the unity assumption. The conditional chain is derived: $J_\kappa = 0$ implies $\kappa = 0$ at the energy minimum, which implies $AB = 1$.

The wall is at $J_\kappa = 0$ itself. The candidate Exchange-Creation Separation principle asserts that local vacuum exchange is trace-free ($J_\kappa = 0$) while vacuum creation is traceful ($J_\kappa \neq 0$). This principle, if true, closes the chain.

The verbal analysis in `attempt_deriving_exchange_creation_separation_from_existing_postulates.md` concluded that neither Postulate 2 (constant local density) nor Postulate 3 (vacuum exchange in gradients) plainly entail trace-free exchange. The principle either needs to be a postulate or needs to be derived from deeper structural commitments the framework hasn't yet articulated.

The structure search asks: do *any* natural candidate structures produce trace-free exchange? If yes, the Exchange-Creation Separation postulate may not be the cleanest framing of the missing principle — there may be a deeper structural commitment that produces it as a consequence.

## Methodology

VacuumForge's structure search represents candidate vacuum configurations through three components:

A *projection map* that translates configuration variables to the metric scale variables $a$ and $b$.

*Source operators* that describe how matter perturbations push the configuration in different directions.

*Classification* of operators as exchange (matter ↔ vacuum redistribution) or creation (vacuum content change).

The analyzer computes $J_a$, $J_b$, $J_\kappa$, and $J_\sigma$ for each operator and classifies the result as trace-free, pure-trace, mixed, or conditional. Crucially, it also detects "leak" cases where trace-free behavior was assumed via the operator definition rather than derived from structural constraints.

Three scripts were run:

- `e1.py` analyzes five candidate families: direct mode basis, two-channel exchange, general linear projection, conserved volume, and mixed exchange.
- `e2.py` enumerates eight sign patterns for 2D exchange operators.
- `e3.py` constructs an explicit trace-kernel example to verify the analyzer's behavior.

## Results

### Family Analysis

**Direct mode basis** (operator chosen as $J_a = S$, $J_b = -S$, in coordinates that are already $\kappa$ and $\sigma$): Status `tautological`. The analyzer correctly flags a leak warning: "Exchange operator explicitly zeroes all trace-contributing variables. Trace-free exchange is assumed via the operator definition, not derived from deeper structure." This result is the discriminator working — when the exchange direction is built into coordinates that are already mode coordinates, $J_\kappa = 0$ is trivial and unrevealing.

**Two-channel exchange** (antisymmetric exchange $J_a = S$, $J_b = -S$ with non-trivial projection): Status `derived`. The analyzer registers a downstream derived source with $J_\kappa = 0$. This is the case where structural commitment to antisymmetric exchange direction produces trace-free behavior as a consequence rather than as a definition.

**General linear projection** (parameterized 2D linear projection with arbitrary coefficients): Status `conditional`. The trace-free condition becomes an algebraic constraint:
$$\alpha_1 e_1 + \alpha_2 e_2 + \beta_1 e_1 + \beta_2 e_2 = 0$$
Generic linear projections do not produce trace-free exchange. The trace-free condition holds only on a measure-zero subset of parameter space — the kernel of the trace map. This tells us trace-free exchange is *not generic*; it is a special structural property.

**Conserved volume family** (exchange that preserves a volume-form invariant): Status `derived`. Volume-conserving operators automatically lie in the trace kernel. Creation in this family is mixed (changes both volume and shape) rather than pure trace.

**Mixed exchange family** (one-sided exchange $J_a = S$, $J_b = 0$): Status `failed`. The classifier correctly identifies that an operator pushing only the time channel produces $J_\kappa = S \neq 0$. One-sided exchange is not trace-free. This is the tool serving its diagnostic purpose: it refuses to call this structure trace-free even though it's a sensible-looking exchange operation.

### Sign Pattern Enumeration

Of eight sign patterns enumerated for 2D exchange directions, only two produce trace-free exchange:

```
(+1, -1)  trace-free derived
(-1, +1)  trace-free derived
(+1, +1)  failed
(-1, -1)  failed
(+1,  0)  failed
(-1,  0)  failed
( 0, +1)  failed
( 0, -1)  failed
```

The two trace-free patterns are precisely the antisymmetric exchange directions. All other directions either source the trace mode or vanish.

### Trace Kernel Construction

The constructed example (`e3.py`) explicitly verifies the kernel structure: an exchange operator in the direction $[S, -S]$ lies in the kernel of the trace projection $[1, 1]$ (the dot product is zero), while a creation operator in the direction $[C, C]$ lies in the trace direction. The analyzer reports the expected results, confirming the underlying mathematics.

## Interpretation

The structure search produces a sharper characterization of trace-free exchange than the verbal analysis reached.

**Trace-free exchange is not generic.** Generic linear projections do not produce $J_\kappa = 0$. The condition is satisfied only by exchange operators lying in the trace kernel of the projection map. In 2D this is a one-dimensional subspace of a two-dimensional direction space — measure zero.

**The missing principle is more specific than "exchange is trace-free."** The structural fact the framework needs is:

> Local vacuum exchange acts in the trace-kernel direction of the vacuum configuration space.

Or equivalently:

> Local exchange is antisymmetric between the pre-mode channels; creation acts in the symmetric (trace) direction.

This is sharper than "exchange is trace-free" because it identifies *what makes exchange trace-free* — the operator's direction in configuration space relative to the trace projection — rather than merely asserting trace-freeness as a property.

**The wall has moved, not been crossed.** The structure search does not derive trace-free exchange from existing framework postulates. It demonstrates that trace-free exchange is a special structural property and characterizes what makes a candidate structure produce it. The remaining theoretical question is *why* physical local vacuum exchange must take the trace-kernel direction.

This is real progress. "Why is exchange trace-free?" is a vague question. "Why must the local exchange operator lie in the trace kernel of the configuration space's trace projection?" is a specific question about the geometry of vacuum response, which can be attacked directly.

## Connection to Existing Process Documents

The structure search confirms the verbal analysis in `attempt_deriving_exchange_creation_separation_from_existing_postulates.md` computationally. Trace-free exchange does not fall out of generic structures; it requires specific commitment to antisymmetric exchange direction. The candidate postulate Exchange-Creation Separation is consistent with this finding but may be reformulated more sharply.

The `direct_mode_basis` family's leak warning illustrates exactly the case-3 failure mode (assumption inserted in disguise) that motivated VacuumForge's design. When the exchange operator is defined in mode coordinates, $J_\kappa = 0$ is trivially true but meaningless. The tool catches this distinction. Verbal analysis can miss it because the equations look the same as a derived case.

The `general_linear_projection` family's conditional output gives the framework a concrete object to study: the algebraic constraint that distinguishes trace-free from generic linear exchange. Whether this constraint can be motivated from deeper physical principles is the next research question.

## Candidate Principle (Reformulated)

The Exchange-Creation Separation principle, sharpened by the structure search, becomes:

> Local vacuum exchange operates in the trace-kernel direction of the configuration space's projection to metric mode coordinates. Vacuum creation operates in the trace direction.
>
> In mode terms: $J_\kappa = 0$ for exchange because the exchange operator is structurally constrained to the kernel of the trace map; $J_\kappa \neq 0$ for creation because the creation operator carries trace content.

This is more specific than the original Exchange-Creation Separation candidate. It names the structural feature (trace-kernel constraint) rather than the resulting property (trace-freeness). If the trace-kernel constraint can be derived from existing postulates or from a richer vacuum mathematical structure, the framework gains a derivation. If not, the framework would adopt the constraint as the missing structural commitment.

## What the Structure Search Does Not Show

The structure search demonstrates that trace-free exchange requires the operator to lie in the trace kernel. It does *not* demonstrate that physical vacuum exchange must take this direction. The "why" remains open.

Possible directions for the remaining question:

The trace-kernel direction may correspond to *conformally invariant exchange* — exchange that preserves the proper time-space ratio of the causal cell while redistributing between time and space. This connects to the framework's identity postulate: vacuum is one substance, and its conformal content (the "size" of the causal cell) might be invariant under matter-vacuum exchange.

The trace-kernel direction may correspond to *energy-bookkept exchange* in a specific sense — not just total energy conservation, which the verbal analysis showed is too weak, but conservation of conformal content per causal cell. This would strengthen the channel-conservation reading of Postulate 3 that the verbal analysis tentatively examined.

The trace-kernel direction may emerge from a richer vacuum mathematical structure (tensor field, scalar-tensor with constraint, etc.) where the trace projection has a natural physical meaning rather than being a coordinate artifact.

Each of these is a candidate route. None has been pursued in this baseline run.

## Status

The structure search advances the Equal-Response derivation problem by isolating the specific structural fact the framework needs to motivate. The conditional chain is now:

```
trace-kernel exchange direction
  → trace-free exchange (J_kappa = 0)
    → kappa = 0 at energy minimum
      → AB = 1
        → gamma_v = 1
```

The first step — "exchange operates in the trace-kernel direction" — remains the wall. But it is a sharper wall than "exchange is trace-free," because it identifies what about the exchange operation produces trace-freeness.

The candidate Exchange-Creation Separation postulate, if eventually adopted, should be stated in terms of the trace-kernel direction rather than in terms of trace-freeness directly. This is a more structurally meaningful commitment.

The framework's options remain (A) derive the trace-kernel direction from existing postulates or richer vacuum structure, (B) adopt the trace-kernel direction as a structural postulate, or (C) accept Equal-Response as observation-fixed. The choice among these is unchanged by this investigation, but Option (A) now has a concrete target: derive why physical exchange must lie in the trace kernel.

## Reproduction

In `vacuum_energy_dynamics/vacuum_forge/src`:

```
python scripts/e1.py    # Five-family analysis
python scripts/e2.py    # 2D sign-pattern enumeration
python scripts/e3.py    # Trace-kernel construction
```

Each script prints structured output showing the structure analyzer's classifications, including leak warnings where trace-free behavior is detected as assumed rather than derived.

## Next Investigation

Two natural next runs:

**Constraint exploration on the general linear projection.** The conditional family produces an explicit algebraic constraint on parameters for trace-free exchange. Examine whether this constraint can be motivated from a physical principle — conformal invariance, channel conservation, identity-postulate symmetry, or some other commitment — rather than being imposed by hand.

**Higher-dimensional structure search.** The 2D analysis may overstate the genericness of failure (failures dominate sign-pattern enumeration partly because 2D space is small). A 3+1 generalization (M34 capability) could reveal whether the trace-kernel direction is more or less constrained in higher dimensions, which bears on the candidate postulate's risks identified in `candidate_exchange_creation_separation.md`.

Both investigations stay within VacuumForge's release-candidate capabilities and do not require new framework commitments.