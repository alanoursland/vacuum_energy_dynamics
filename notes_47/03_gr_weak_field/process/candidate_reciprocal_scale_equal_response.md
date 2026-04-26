# Candidate: Reciprocal Scaling and the Equal-Response Target

---

## What This Document Is

This is a process document, like `candidate_paths_to_equal_response.md`, sitting in the `process/` subfolder. It does not adopt a provisional commitment or perform a derivation; it sharpens the formulation of an existing problem.

The problem in question is the Equal-Response component of the unity assumption from `candidate_vacuum_variation_unity.md`: the claim that $\gamma_v = 1$, equating the spatial-mapping coupling to the time-mapping coupling at first order in the weak-field metric.

`candidate_paths_to_equal_response.md` classified five derivation paths and identified Path 5 (variational principle / energy minimization) as the most distinctive framework-native route, alongside the structural Path 3 (vacuum as one substance). What that document did not do was specify what *exactly* the candidate energy functional would minimize. The "mismatch" variable was named but not pinned down.

This document pins it down. The Equal-Response claim, in its correct form, is a **reciprocal-scale condition** between temporal and spatial scale factors — not a parallel-scale condition. Identifying this distinction sharpens both the target and what Path 5 would have to derive. It also reveals an unexpected unification: the same ansatz that closes Equal-Response at first order naturally closes the second-order time-metric candidate as well.

The document does not derive the reciprocal condition. It identifies it as the right target, names the candidate justification (Path 5 with a specific mismatch variable), and is honest about what remains to be derived.

---

## The Naive Reading and Why It Fails

A natural first reading of the framework's identity postulate, applied to the metric, runs roughly as follows. Vacuum is one substance; a perturbation of vacuum at radius $r$ is one object; that one object has projections into the time component and the spatial components of the metric; therefore the perturbations of $g_{00}$ and $g_{ij}$ should both reflect "the same vacuum reduction" applied uniformly.

In equation form: if $\delta(r)$ is the local vacuum reduction at radius $r$, the naive reading proposes

$$\frac{d\tau}{dt} \approx 1 - \delta, \qquad \frac{dL}{dx} \approx 1 - \delta$$

so that proper time per coordinate time and proper length per coordinate length are reduced by the same factor.

This reading fails as a viable weak-field metric. The failure is structural: the metric it produces cannot reproduce the framework's own light-deflection or Shapiro-delay targets, much less match observation.

To see the failure, compute the coordinate speed of light in this metric. Locally, light propagates at $c$: $dL/d\tau = c$. Translating to coordinate quantities through the scale factors $A = d\tau/dt$ and $B = dL/dx$:

$$\frac{dx}{dt} = \frac{d\tau/dt}{dL/dx} \cdot \frac{dL}{d\tau} = c \cdot \frac{A}{B}$$

Under the naive reading, $A = B = 1 - \delta$, so $A/B = 1$ and the coordinate speed of light is $c$ uniformly — independent of position relative to the mass.

But Shapiro delay and the spatial contribution to light deflection both depend on the coordinate speed of light differing from $c$ in the asymptotic-observer's coordinates. If $A/B = 1$ everywhere, both effects vanish. The naive reading is therefore ruled out as a viable weak-field metric — by the framework's own observational targets, regardless of how we want to interpret "same vacuum perturbation projecting equally."

A clarification on framing. The "coordinate speed of light is less than $c$" language can be misleading. Light is locally $c$ in every frame; this is preserved by any of the metrics under discussion. What "Shapiro delay" actually describes is a frame-translation effect: the asymptotic observer, comparing their coordinate system to local proper measurements along the photon's path, computes a longer coordinate-time round-trip than they would for the same coordinate distance in flat space. The light isn't slowing down in any absolute sense; the asymptotic observer's clock runs at a different rate than the local clocks the photon traverses, and the integration along the path produces extra coordinate-time.

So the failure of the naive reading is not "light moves slower than it should in this metric." It's "the asymptotic observer's frame relates to local frames in a way that produces no frame-translation effect on photon round-trips, contradicting the observed Shapiro delay." The frame-translation is what's wrong.

---

## The Reciprocal Reading

The corrected formulation uses scale factors $A(r)$ and $B(r)$ defined as

$$A(r) = \sqrt{-g_{00}}, \qquad B(r) = \sqrt{g_{ii}}$$

in the framework's PPN-compatible weak-field coordinates. Physically, $A$ is the rate at which proper time elapses per coordinate time at radius $r$ (relative to infinity), and $B$ is the proper length per coordinate length.

The redshift and time-dilation chain pins down $A$ at first order:

$$A(r) \approx 1 + \frac{\Phi(r)}{c^2}$$

with $\Phi < 0$ in a well, so $A < 1$: clocks at the bottom of a well run slower than clocks at infinity, as observed.

The spatial scale factor $B$ remains parameterized:

$$B(r) \approx 1 - \gamma_v \frac{\Phi(r)}{c^2}$$

with $\gamma_v$ undetermined. The Equal-Response claim is $\gamma_v = 1$, giving $B \approx 1 - \Phi/c^2$, so $B > 1$ in a well: spatial proper length per coordinate length is larger near a mass.

The crucial observation: $A$ and $B$ move in *opposite directions* under vacuum perturbation. $A$ decreases below 1 in a well; $B$ increases above 1. The Equal-Response claim, restated, is that the magnitudes of these opposite-direction changes are equal.

In compact form, Equal-Response with $\gamma_v = 1$ corresponds to

$$A(r) \cdot B(r) \approx 1$$

at first order, or equivalently

$$\ln A(r) + \ln B(r) \approx 0.$$

This is the **reciprocal-scale condition**. The temporal scale factor and spatial scale factor are reciprocals of each other.

The reciprocal condition recovers the full standard PPN weak-field form:

$$g_{00} = -A^2 \approx -\left(1 + \frac{2\Phi}{c^2}\right), \qquad g_{ij} = B^2 \delta_{ij} \approx \left(1 - \frac{2\Phi}{c^2}\right) \delta_{ij}$$

which gives $\gamma_v = 1$ and matches GR's weak-field metric in isotropic coordinates.

The coordinate speed of light under reciprocal scaling: $A/B \approx 1 + 2\Phi/c^2$, which is less than 1 in a well. This produces the observed Shapiro delay and spatial contribution to light deflection.

---

## Why Reciprocal Rather Than Parallel?

The reciprocal-scale form matches observation; the parallel-scale form does not. But matching observation is not the same as deriving the form from the framework's commitments. The framework's identity postulate, the curvature consequence, and Postulate 2 do not uniquely select the reciprocal form over the parallel form — both are configurations the framework's vocabulary can describe.

What's needed: an argument internal to the framework that *forces* reciprocal rather than parallel. This is the actual content of the Equal-Response derivation problem.

Some heuristic motivation for reciprocal scaling exists. One reading: vacuum perturbation does not deplete proper extent uniformly; rather, it acts in a balanced way between time-mapping and any single direction of space-mapping. The temporal scale factor $A$ is compensated by each spatial scale factor $B$ at the level of a time-space pair: $AB = 1$ pairs one time scale with one spatial scale, leaving the time-space ratio $A/B$ free to take whatever value the perturbation produces.

This is *not* the same as saying total proper-spacetime-volume is conserved. The four-volume element is $\sqrt{-g} = A B^3$ in three spatial dimensions, which under $AB = 1$ becomes $B^2$, not unity. The reciprocal condition pairs $A$ with $B$ component-by-component, not $A$ with $B^3$ globally. The picture is balanced time-space coupling, not volume conservation.

This balanced-pairing picture is consistent with the framework's vacuum-substance ontology and gives the right metric. It is not, however, a formal consequence of Postulate 2 (which says density is locally constant) or of any other current postulate. The picture is plausible but not derived.

The frame-translation framing illuminates the same point. The metric describes how the asymptotic observer's frame relates to local frames along the perturbation. Two questions are involved: (1) how do clocks compare across frames? (2) how do rulers compare across frames? The redshift derivation answers question 1: clocks compare via $A(r)$. Equal-Response is the claim that the answer to question 2 is $B(r) = 1/A(r)$.

There's no logical necessity in this. Frames could relate such that clocks and rulers disagree by the same factor in the same direction (parallel), or by the same factor in opposite directions (reciprocal), or by different factors. The framework's commitments need to select one, and the empirical correctness of the reciprocal form tells us this is the answer the framework should produce — but doesn't tell us *why* it should produce that answer.

---

## Connection to the Second-Order Time Metric

Reframing Equal-Response as a reciprocal-scale condition produces an unexpected connection to a separate provisional candidate: `candidate_second_order_time_metric_from_redshift.md`, which closes $g_{00}$ at second order with $\beta = 1$ via the redshift exponential $g_{00} = -\exp(2\Phi/c^2)$.

If the reciprocal condition holds *exactly* (not just at first order), then with $A(r) = \exp(\Phi/c^2)$:

$$B(r) = \frac{1}{A(r)} = \exp(-\Phi/c^2)$$

The full metric becomes

$$g_{00} = -A^2 = -\exp(2\Phi/c^2), \qquad g_{ij} = B^2 \delta_{ij} = \exp(-2\Phi/c^2) \delta_{ij}$$

This is a single ansatz — exact reciprocal exponential scaling — that would simultaneously match both provisional candidates if it could be derived. The time component gives $\beta = 1$ (matching the second-order candidate). The spatial component gives $\gamma_v = 1$ (matching unity).

The two provisional commitments the framework currently holds are, on this reading, two faces of one underlying ansatz: a vacuum perturbation produces reciprocal exponential scale factors. If this ansatz can be derived, both candidates would unify under it, and the framework's static weak-field metric would be determined to all orders within this exponential ansatz, once the potential profile $\Phi(r)$ is supplied by an independent source equation.

This is a substantial structural insight. It does not, by itself, derive the ansatz. But it tells us that the two open foundational gaps in the weak-field program might not be independent — closing one might close both, if the right unifying principle can be found.

---

## Path 5 Made Concrete

The previous paths-to-equal-response document identified Path 5 (variational principle / energy minimization) as the most distinctive framework-native derivation route, and named "mismatch" as the variable that should carry positive configuration energy. With the reciprocal-scale formulation in hand, the mismatch variable has a concrete form.

Define:

$$\mu(r) = \ln A(r) + \ln B(r)$$

The reciprocal condition $AB = 1$ corresponds to $\mu = 0$ everywhere. Departures from reciprocal scaling correspond to nonzero $\mu(r)$.

A configuration energy functional that derives reciprocal scaling would assign positive energy to configurations with $\mu \neq 0$. The simplest plausible form:

$$E_{\text{mismatch}} = \int C(r) \, \mu(r)^2 \, d^3x$$

with $C(r) > 0$. Postulate 5's minimum-energy commitment then forces $\mu = 0$ at minimum, deriving the reciprocal condition.

This is a candidate form, not a derivation. The work that remains is to show that the framework's actual configuration energy (whatever its full form turns out to be) contains a term of this kind with positive coefficient. That requires either deriving configuration energy from existing commitments (which loops back to the question of the vacuum's mathematical structure) or postulating a specific energy form (which would be adopting another commitment rather than deriving Equal-Response from existing ones).

What's been gained by introducing $\mu$: the derivation problem now has a specific target. Instead of "show Equal-Response follows from Path 5," the target is "show that configuration energy contains a positive-coefficient term in $(\ln A + \ln B)^2$." That's a much sharper question.

---

## The Path 3 / Path 5 Combination

The previous paths document treated Path 3 (vacuum as one substance) and Path 5 (energy minimization) as separate routes. The reciprocal-scale formulation suggests they may combine productively.

Path 3 supplies the mismatch variable. The "one substance" intuition motivates the claim that $A$ and $B$ are not independent — they're projections of one perturbation. The variable $\mu = \ln A + \ln B$ is the natural measure of how far a configuration deviates from "one substance projecting consistently into both components." When $\mu = 0$, the projections are reciprocal and the substance projects coherently. When $\mu \neq 0$, the projections are inconsistent — the substance is being treated as two separable aspects.

Path 5 supplies the dynamical mechanism. Postulate 5 says configurations relax to minimum energy. If $\mu \neq 0$ corresponds to internal mismatch and internal mismatch carries positive energy, then $\mu = 0$ is the minimum and reciprocal scaling is the relaxed configuration.

The combination is more compelling than either path alone. Path 3 alone is verbal — "one substance, equal projections" — and doesn't pin down the specific form of the relationship. Path 5 alone needs a specific mismatch variable to operate on. The reciprocal-scale formulation provides exactly what each path lacks: a concrete variable (Path 3's contribution) that has clear physical meaning as mismatch (Path 5's contribution).

The combined argument:

1. By Postulate 1, vacuum is one substance.
2. A perturbation of vacuum has projections into $g_{00}$ and $g_{ij}$.
3. The natural measure of mismatch between these projections is $\mu = \ln A + \ln B$.
4. By Postulate 4, configurations carry energy; by Postulate 5, configurations relax to minimum energy.
5. If the configuration energy has a positive-coefficient term in $\mu^2$, the relaxed configuration has $\mu = 0$.
6. Therefore $AB = 1$ (the reciprocal condition), and $\gamma_v = 1$ at first order.

Step 5 is the gap. It remains a hypothesis about the form of configuration energy, not a derivation. But identifying this gap precisely — *positive-coefficient mismatch term in configuration energy* — is more useful than the previous abstract characterization.

---

## What This Document Establishes and What It Doesn't

**Establishes:** The Equal-Response claim, correctly formulated, is the reciprocal-scale condition $AB = 1$, not a parallel-scale condition. The naive reading "vacuum depletion reduces both time and space proper extents" is inconsistent with observation. The corrected reading is that vacuum perturbation produces opposite-direction changes of equal magnitude in temporal and spatial scale factors.

**Establishes:** The reciprocal form, taken to all orders as $A = \exp(\Phi/c^2)$, $B = \exp(-\Phi/c^2)$, would unify both the unity candidate ($\gamma_v = 1$) and the second-order time-metric candidate ($\beta = 1$) under one ansatz. The two provisional commitments may be two faces of one underlying reciprocal-scale principle, if that principle can be derived.

**Establishes:** Path 5's mismatch variable has a concrete form: $\mu = \ln A + \ln B$. The Path 3 / Path 5 combination becomes more compelling when stated in terms of this variable: vacuum monism provides the variable, energy minimization provides the dynamics, and reciprocal scaling falls out of the combination.

**Does not establish:** Why the framework's configuration energy should contain a positive-coefficient term in $\mu^2$. This is the gap that, when filled, would convert the reciprocal-scale formulation from a target to a derivation. Filling it requires either (a) deriving configuration energy from the framework's existing commitments, which loops back to specifying the vacuum's mathematical structure, or (b) postulating a specific energy form, which would be adopting an additional commitment rather than deriving Equal-Response from existing ones.

**Does not establish:** That the exact reciprocal exponential ansatz is forced beyond first order. Showing $AB = 1$ at first order is consistent with many higher-order completions; the exponential is the simplest. Strong-field deviations from Schwarzschild might appear at higher orders even if first-order $\gamma_v = 1$ and second-order $\beta = 1$ both hold.

---

## Status

The reciprocal-scale formulation is the correct target for the Equal-Response derivation. The naive parallel-scale reading is ruled out as a viable weak-field metric by the framework's observational targets, and the corrected target connects naturally to the second-order time-metric candidate.

Equal-Response remains adopted rather than derived. The unity candidate's provisional status is unchanged. What has changed is the precision with which the open derivation problem is stated.

The work that would close Equal-Response: produce a configuration energy functional that contains a positive-coefficient term in $(\ln A + \ln B)^2$, derived from or consistent with the framework's existing postulates. Whether such a functional exists naturally within the framework's commitments, or requires additional structure, is the foundational question.

If this work succeeds, three things happen simultaneously: $\gamma_v = 1$ becomes derived rather than adopted; $\beta = 1$ becomes derived through the same exponential ansatz; and the framework's static weak-field metric becomes determined within the reciprocal exponential ansatz, once the potential profile $\Phi(r)$ is supplied by an independent source equation. The downstream proofs (light deflection, Shapiro delay, perihelion precession) all lose their provisional status simultaneously.

This is the highest-leverage foundational target the framework currently has. The reciprocal-scale formulation makes it concrete; the energy functional remains to be specified.