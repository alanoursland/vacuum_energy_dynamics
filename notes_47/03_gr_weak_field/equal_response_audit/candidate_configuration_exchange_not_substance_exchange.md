# Candidate: Configuration Exchange, Not Substance Exchange

## What This Document Is

This is a candidate document. It refines the framework's interpretation of vacuum exchange in gravitational processes by distinguishing two physically distinct mechanisms: configuration exchange and substance exchange.

The refinement is motivated by the structure-search investigations (`structure_search_baseline_results.md`, `structure_search_higher_dimensional_results.md`) which established that the Equal-Response problem reduces to a single conservation law: local gravitational exchange preserves the trace $a + b$ of the metric scale variables. This conservation law has two compatible physical readings — configuration exchange and substance exchange — and the framework cannot adopt both without internal tension.

This document proposes the configuration-exchange reading explicitly, derives its consequences conditional on adopting trace conservation, and identifies which existing framework content is affected by the choice.

The document is conditional throughout. Trace conservation has not been derived from the original five postulates. Whether the framework adopts trace conservation as a postulate, derives it from richer structure, or rejects it in favor of another route to Equal-Response, is an open decision the framework has not made.

## The Distinction

The framework distinguishes three quantities that have been conflated in earlier language:

**Vacuum density** ($\rho_v$). Postulate 2 commits to this as a finite, locally constant intensive property. It is not a degree of freedom that varies across space or time. Local gravitational phenomena cannot be explained by spatial variation in $\rho_v$.

**Vacuum substance content** (or trace content). Under Postulate 1, vacuum is spacetime, so the amount of vacuum in a region equals the amount of space in that region. Substance change means change in the conformal/trace mode of the local metric — change in the size of the causal cell. Cosmic expansion creates substance: more space exists, so more vacuum exists, so more vacuum-energy exists. This is the framework's clearest case of substance change.

**Vacuum configuration energy** ($E_{\text{config}}$). Postulate 4 commits to non-flat vacuum configurations carrying positive energy relative to flat vacuum. This energy is independent of the substance content — a region can have the same amount of vacuum but different configuration energy depending on its curvature or deformation state.

The total vacuum energy of a region admits the conceptual decomposition

$$E_{\text{vac}} = E_{\text{substance}} + E_{\text{config}}.$$

The substance term scales with the amount of vacuum present (related to but not identical to $\rho_v V$, which presumes a specific functional form). The configuration term scales with the deformation state. The framework has not yet derived precise functional forms for either term, but the distinction itself is structural and follows from Postulates 1, 2, and 4 taken together.

## Core Claim

**Candidate Principle: Configuration Exchange, Not Substance Exchange.**

If the framework adopts trace conservation for local gravitational exchange, then local exchange operates on configuration energy alone. It does not change the local substance content of the vacuum. Cosmic expansion is reserved as the framework's mechanism for substance creation; ordinary gravity is reserved as the framework's mechanism for configuration redistribution.

Equivalently:

- Local gravitational exchange may change curvature, shape, strain, or configuration energy.
- Local gravitational exchange does not create or destroy net conformal vacuum content.
- Substance creation and destruction are reserved for traceful processes such as cosmic expansion.

In mode language, with $\kappa = (a+b)/2$ the conformal/trace mode and $\sigma = (a-b)/2$ the shear mode, the trace-conservation condition is

$$J_\kappa = 0$$

for local gravitational exchange, while

$$J_\kappa \neq 0$$

for genuine substance creation.

The reciprocal-scale condition $AB = 1$ is equivalent to $\kappa = 0$, so trace conservation provides the route to Equal-Response: $J_\kappa = 0$ at the energy minimum gives $\kappa = 0$, which gives $AB = 1$, which gives $\gamma_v = 1$.

## Why Trace Conservation Forces the Choice

The structure-search investigations established that trace-free exchange is a codimension-1 constraint regardless of dimension — it is preservation of the single quantity $a + b$. Once the framework's mode decomposition exists, "vacuum exchange" must be one of two physical processes:

**Reading A (Configuration Exchange):** Exchange preserves $a + b$. The vacuum's substance content is unchanged; only its configuration energy is redistributed.

**Reading B (Substance Exchange):** Exchange does not preserve $a + b$. Vacuum substance is locally created or destroyed during ordinary gravitational interaction.

The two readings are logically exhaustive given the mode decomposition. They are also mutually exclusive: trace conservation either holds or it doesn't.

The framework's earlier "vacuum consumption / regeneration" language was compatible with both readings. The mode decomposition makes the readings distinguishable. The choice between them is now a structural commitment the framework must make.

## Conditional Argument for Reading A

This argument shows: if trace conservation holds, then ordinary gravitational exchange must be configuration exchange, not substance exchange.

**Premise 1.** Vacuum energy decomposes into substance and configuration contributions:

$$E_{\text{vac}} = E_{\text{substance}} + E_{\text{config}}.$$

This follows from Postulates 1, 2, and 4 as discussed above. The decomposition is conceptual; the precise functional forms are not yet derived.

**Premise 2.** Substance change is conformal/trace mode change. By construction, $\kappa$ tracks the conformal/trace content of the local metric. A change in net vacuum substance content is a change in $\kappa$, hence

$$\Delta E_{\text{substance}} \neq 0 \implies J_\kappa \neq 0.$$

**Premise 3.** Trace conservation. If the framework adopts trace conservation for local exchange:

$$J_\kappa = 0$$

for ordinary gravitational interaction.

**Conclusion.** From Premises 2 and 3 (taking the contrapositive of Premise 2):

$$J_\kappa = 0 \implies \Delta E_{\text{substance}} = 0$$

for local exchange. From Premise 1, the energy exchanged in local gravity must come from $E_{\text{config}}$:

$$\Delta E_{\text{matter}} + \Delta E_{\text{config}} = 0$$

up to any radiated configuration energy.

Therefore, under trace conservation, ordinary gravitational exchange is configuration exchange, not substance exchange.

## Status of the Argument

The argument is *conditional* on adopting trace conservation (Premise 3). Trace conservation is not a theorem of the original five postulates as currently written.

What the original postulates establish:

- The substance / configuration distinction itself (from Postulates 1, 2, 4).
- That configuration energy exists and is positive for non-flat vacuum (Postulate 4).
- That gradient-driven exchange occurs (Postulate 3).

What the original postulates do not establish:

- That local exchange must preserve the trace.
- That substance change is forbidden in local interactions.

So this document does not prove Configuration Exchange from the five postulates. It proves the conditional:

> If the framework adopts trace conservation for local exchange (whether as a new postulate, a derived consequence of richer vacuum structure, or an emergent constraint), then ordinary gravitational exchange must be interpreted as configuration exchange.

## Impact on the Existing Framework

The remainder of this document identifies which framework content is affected by adopting Configuration Exchange under the conditional above. Each item identifies (a) what changes, (b) what stays the same, and (c) under what conditions the change applies.

### Postulate 3

**What changes.** Postulate 3's "consumption" and "regeneration" language must be read as configuration-level exchange, not as literal local creation or destruction of vacuum substance. The postulate's content — that energy moves along curvature gradients with corresponding vacuum exchange — remains intact, but the *kind* of exchange is constrained to be trace-preserving.

**What stays the same.** The postulate's role in the framework. It still mediates the energy ledger between matter and vacuum during gravitational interaction. The redshift, time dilation, and free-fall derivations that depend on Postulate 3's exchange content still go through, because they depend on energy being exchanged, not on whether the exchange is substance or configuration.

**Conditions.** This change applies if the framework adopts trace conservation. If trace conservation is rejected, Postulate 3 retains its ambiguity and the framework would need to specify the substance-exchange reading and address the cosmological-accumulation tension separately.

A cleaner Postulate 3 formulation under Configuration Exchange:

> When energy moves along a curvature gradient, it exchanges energy with the vacuum configuration. This exchange is trace-preserving: it changes the reciprocal relation between temporal and spatial scale modes without altering the net conformal vacuum content of the region. Descent draws energy from the local configuration; ascent returns energy to it.

### Postulate 4

**What changes.** Postulate 4 becomes load-bearing in a more specific way. Under Configuration Exchange, the configuration energy reservoir is the *only* source for ordinary gravitational phenomena. A gravity well has gravitational potential energy because the vacuum configuration is non-flat; a falling body gains kinetic energy because the configuration releases configuration energy; a gravitational wave carries energy because it is a propagating configuration disturbance.

**What stays the same.** The postulate's content as written — that non-flat configurations carry positive energy — is unchanged. What changes is its interpretive role: configuration energy is now identified as the gravitational reservoir.

**Conditions.** Same as for Postulate 3. If trace conservation is adopted, configuration energy carries the framework's gravitational phenomena. If trace conservation is rejected, configuration energy is one reservoir among potentially others (with substance energy contributing as well).

### The Static-Gravity Proofs

**What changes.** The proofs (Newtonian limit, redshift, time dilation, light deflection, Shapiro delay, perihelion precession) do not directly depend on whether exchange is substance or configuration. They depend on the energy ledger balancing, the metric components taking specific forms, and the equations of motion following from the metric. None of these are affected by the substance / configuration distinction.

**What stays the same.** All of the static-gravity content remains intact under Configuration Exchange. The provisional commitments (unity, second-order time-metric) are independent of this choice.

**Conditions.** No conditional dependence. The proofs work under either reading; the difference is interpretive.

### The Cosmic Expansion Consequence

**What changes.** The contrast between local gravity and cosmic expansion becomes sharper. Under Configuration Exchange, the two are *qualitatively different mechanisms*: local gravity is trace-preserving configuration exchange, cosmic expansion is traceful substance creation. They are not the same process at different scales; they operate by different rules.

**What stays the same.** The cosmic expansion consequence document's content is preserved. Expansion creates space, space is vacuum, vacuum is energy, so expansion creates energy. This is exactly substance creation, which is what cosmic expansion is allowed to be.

**Conditions.** Under Configuration Exchange, the cosmological tension named in the cosmic expansion document is resolved structurally: local gravity does not accumulate cosmologically because it does not create substance at all. Under substance exchange, the tension would remain — local creation would in principle accumulate, and the framework would need additional structure to explain why it doesn't.

### The Eternal Renewal Candidate

**What changes.** Less than I initially thought. The eternal renewal candidate operates in a regime (very late, very dilute void; very high-amplitude fluctuation) where the framework's local-vs-cosmological distinction may break down anyway. The runaway-compression mechanism that drives bubble ignition is currently underspecified, and whether it operates by configuration exchange, substance creation, or both at different stages is open.

**What stays the same.** The candidate's overall picture (no absolute beginning, no heat death, bubble universes) is independent of the configuration / substance choice for *local* gravity. The cosmological-scale processes the candidate posits are traceful by construction.

**Conditions.** The eternal renewal candidate's load-bearing assumptions (runaway threshold, localization, entropy reset) are open regardless of which reading the framework adopts for local exchange. Configuration Exchange clarifies what local gravity does and doesn't do; it doesn't directly constrain what high-amplitude vacuum fluctuations do at the threshold of bubble ignition.

### The Equal-Response Problem

**What changes.** The conditional chain to Equal-Response goes through trace conservation:

```
trace conservation (single conservation law)
-> J_kappa = 0
-> kappa = 0 at energy minimum
-> AB = 1
-> gamma_v = 1
```

Under Configuration Exchange, this chain is interpretively grounded: trace conservation is the mathematical expression of the physical claim that local exchange operates on configuration alone. The structure-search results show this conservation law is codimension-1 (a single constraint, not a directional fine-tuning).

**What stays the same.** The wall is still at the first step. Adopting Configuration Exchange does not derive trace conservation; it makes trace conservation interpretable as a physical principle (preservation of the local conformal cell content during exchange) that the framework might be able to derive from richer structure.

**Conditions.** The Equal-Response chain closes if trace conservation is added. Configuration Exchange is the physical content of that addition; it is not a separate route to Equal-Response. Adopting one means adopting the other.

### The Wave-Modes Branch

**What changes.** Possibly significant, possibly nothing — this is the area I want to flag as least clear. The wave-modes branch wants to explain why gravitational waves are tensor (transverse-traceless) rather than scalar. Under Configuration Exchange, propagating disturbances of the vacuum carry configuration energy, and the trace-preservation constraint on local exchange might extend to a constraint on which propagation modes are physically realized — specifically, that scalar (trace) modes are suppressed or absent because they would correspond to substance creation/destruction at every point along the wave.

This is suggestive but not derived. The relationship between the local-exchange constraint and the propagation-mode constraint requires additional argument. It is the natural place to look, but the connection should be developed before relying on it.

**What stays the same.** The wave-modes branch's open-question status. Configuration Exchange potentially provides a framework-internal reason for tensor-only waves, but does not by itself derive this.

**Conditions.** Conditional on (a) trace conservation holding for local exchange, (b) trace conservation extending to wave propagation in a derivable way. The second condition is open work.

## What This Does Not Do

Configuration Exchange does not derive trace conservation. It derives the *physical interpretation* of trace conservation under the assumption that trace conservation holds.

Configuration Exchange does not unify gravity and cosmology. It distinguishes them as different mechanisms operating in different regimes, with cosmic expansion as the framework's substance-creation mechanism and local gravity as its configuration-exchange mechanism.

Configuration Exchange does not solve the cosmological constant problem. It clarifies that $\rho_\Lambda$'s constancy during expansion is consistent with substance being created at constant density, but does not derive the value of the constant.

Configuration Exchange does not address strong-field gravity. The substance / configuration distinction holds at all field strengths in principle, but the framework's strong-field behavior depends on the vacuum's mathematical structure, which is open work.

## Proposed Terminology

The following terms should be used consistently if Configuration Exchange is adopted:

- **Configuration exchange** for ordinary local gravitational energy exchange (trace-preserving).
- **Substance creation** or **substance destruction** for traceful changes in net vacuum content (cosmological-scale processes).
- **Trace conservation** for the constraint $J_\kappa = 0$ on local exchange.
- **Configuration energy** for the energy stored in non-flat vacuum configurations (the reservoir for local gravity).
- **Substance content** for the net amount of vacuum in a region (changeable only by traceful processes).

The following terms should be deprecated or qualified:

- **"Vacuum is consumed"** — use only with explicit clarification that configuration exchange is meant.
- **"Vacuum is regenerated"** — same caveat.
- **"Local vacuum creation"** — should be reserved for traceful processes; not used for ordinary gravity.

## Summary

Configuration Exchange is the physical interpretation of trace conservation. If the framework adopts trace conservation for local exchange (whether as a postulate, a derived consequence, or an emergent constraint), then ordinary gravitational interaction operates on configuration energy alone, while cosmic expansion remains the framework's mechanism for genuine substance creation.

The candidate document remains conditional. Trace conservation has not been derived from the original five postulates. The structure-search results show that trace conservation is a single conservation law (codimension-1), making it a tractable target for derivation from a physical principle — most plausibly, conservation of the local conformal cell content during exchange.

If the framework eventually derives trace conservation, Configuration Exchange becomes a consequence. If trace conservation is added as a structural postulate, Configuration Exchange is its physical interpretation. If trace conservation is rejected, the framework retains the substance-exchange reading and must develop one of the alternative routes to Equal-Response, while addressing the cosmological-accumulation tension that substance exchange creates.

The choice is currently held open. The methodology supports holding both readings provisionally and re-deriving downstream content under each setting as the framework develops further.