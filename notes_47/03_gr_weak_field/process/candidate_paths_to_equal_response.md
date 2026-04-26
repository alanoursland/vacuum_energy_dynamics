# Candidate: Paths to Equal-Response

---

## What This Document Is

This is a candidate document of a slightly different kind than the framework's other candidates. It does not adopt a provisional commitment; it analyzes what would be required to derive an existing one. The commitment in question is the Equal-Response component of the unity assumption from `candidate_vacuum_variation_unity.md` — the claim that the vacuum's spatial-mapping response and time-mapping response share the same coupling coefficient, giving $\gamma_v = 1$ in the weak-field metric.

The Single-Function component of unity is more approachable than Equal-Response, though spherical symmetry alone is not sufficient to derive it. The Equal-Response component is the stronger claim, and it is what actually pins $\gamma_v$ to the value 1. Until Equal-Response is derived, every framework result that depends on the closed weak-field metric — light deflection, Shapiro delay, perihelion precession — inherits provisional status.

Closing Equal-Response is the highest-leverage foundational work in the weak-field program. This document classifies the candidate derivation paths the framework might pursue, identifies what each path would need to become rigorous, and concludes that Equal-Response is most likely not derivable from spherical symmetry alone — it requires additional structural commitments, most plausibly about the vacuum's mathematical structure.

The document's contribution is the classification and the identification of concrete next targets. It does not derive Equal-Response.

---

## Why This Matters

The unity candidate adopts $\gamma_v = 1$ as a provisional commitment that closes the weak-field metric. Without this closure, the weak-field metric remains parameterized; light deflection gives $\Delta\theta = (1+\gamma_v)(2GM/bc^2)$ rather than $4GM/bc^2$; Shapiro delay similarly inherits the $(1+\gamma_v)$ factor; perihelion precession depends on both $\gamma_v$ and $\beta$ through the PPN expression. With unity, all of these reduce to standard GR predictions matching observation.

The unity candidate has two components: Static Single-Function (the static spherically-symmetric response is one radial function) and Equal-Response (time-mapping and spatial-mapping share one coupling coefficient). The Single-Function component is more approachable than Equal-Response, but spherical symmetry alone only reduces independent structures to radial functions; it does not by itself guarantee there is only one such function. GR's static spherical metric, for instance, generically has two radial functions before the field equations relate them. The Single-Function commitment therefore requires more than symmetry — it requires the framework's structure (whatever it is) to give one function rather than two or more. The harder claim is Equal-Response. Even granting that there is a single radial function describing the response, why does that function couple equally to time and space?

If Equal-Response is derived rather than adopted, the framework's weak-field metric becomes fully foundational. The light deflection, Shapiro delay, and perihelion precession proofs lose their provisional status (perihelion still inherits the $\beta = 1$ candidate's status, which is independent). The framework's reproduction of weak-field GR becomes a derivation rather than a closure-by-adoption.

This is the most consequential foundational step the framework could take in its current state. It would convert several "consistent with GR given unity" results into "derived to match GR" results. The work is worth doing carefully and worth analyzing thoroughly before attempting.

---

## What Equal-Response Claims, Precisely

The framework's weak-field metric for a static spherically symmetric mass takes the form:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right), \quad g_{ij} \approx \left(1 - 2\gamma_v \frac{\Phi}{c^2}\right)\delta_{ij}$$

where $\gamma_v$ is the framework's spatial-mapping coupling coefficient and $\Phi$ is the gravitational potential.

The time component's coefficient is $2$ (the factor of $2$ in front of $\Phi/c^2$). This was derived by the redshift and time dilation proofs from Postulates 2, 3, and mass-energy equivalence — energy bookkeeping in a gradient. The spatial component's coefficient is $2\gamma_v$ where $\gamma_v$ is currently undetermined.

Equal-Response is the claim that $\gamma_v = 1$, making the spatial coefficient also equal to $2$.

This is not the claim that the spatial metric is isotropic (that follows from spherical symmetry). It is not the claim that there is only one independent function in the spatial response (that's the Single-Function component). It is specifically the claim that whatever single function describes the response, it produces the *same* magnitude in the spatial channel as it does in the temporal channel.

A framework with $\gamma_v \neq 1$ would still be internally coherent — it would just predict $\gamma \neq 1$ in PPN terms, conflicting with observation. The question is what the framework's structure forces $\gamma_v$ to be, before observation enters.

---

## Path 1: Local Lorentz Invariance

The framework adopts special relativity (per `overview.md`), which means every local inertial frame must recover Minkowski geometry. A free-falling observer in a gravity well, sampling their local environment, must measure light at $c$, must observe Lorentz-invariant interval structure, and must find no preferred local direction.

This is the equivalence principle in the framework's terms — already implicit in Postulate 3's universality clause and explicit in the framework's adoption of SR.

The question for Equal-Response: does demanding local Lorentz invariance in a gravity well force $\gamma_v = 1$?

The argument runs: in the local frame, the proper time interval and proper spatial intervals are determined by $g_{00}$ and $g_{ij}$ respectively. For light to propagate locally at $c$ in all directions, the metric must produce a light cone with the right shape. For the local frame to have no preferred direction, the spatial metric must be isotropic. For boosts to behave Lorentz-invariantly, the time and space components must combine into a Minkowski signature with the right relative scaling.

What this argument actually forces: the time and space coefficients must produce locally-Minkowski structure. Local-Minkowski structure is preserved by any positive ratio of coefficients — a metric with $\gamma_v = 0.5$ can still produce locally-Minkowski geometry if you rescale coordinates appropriately. The local observer would measure $c$ for light, would observe Lorentz-invariant intervals, and would find no preferred direction. They would just be using coordinates that map differently to the underlying vacuum than an observer in flat space would.

So Path 1 alone does not force $\gamma_v = 1$. It forces a relation between $g_{00}$ and $g_{ij}$ such that local Minkowski structure is recoverable, but a range of $\gamma_v$ values satisfies this constraint.

A stronger version of Path 1: demand not just locally-Minkowski structure at each point but consistent Lorentz transformation behavior across nearby points. If two local observers at slightly different gravitational potentials must compare measurements through Lorentz transformations (since SR is the framework's underlying invariance group), and if the transformations must close consistently, the coefficient ratio between $g_{00}$ and $g_{ij}$ might be more tightly constrained.

This stronger version is closer to what's needed but still probably doesn't pin $\gamma_v$ to exactly 1. It might force $\gamma_v$ to satisfy some specific algebraic relation, but the relation might admit multiple solutions. Working out what the strongest local-Lorentz-invariance argument actually forces is open work.

---

## Path 2: Null Propagation Consistency

Light propagates along null geodesics: $ds^2 = 0$. Locally, light moves at $c$. Globally, light moving through a region with varying vacuum extent traces curved paths in coordinate terms.

The framework's commitment is that local-$c$ propagation is preserved everywhere (per Postulate 1's information-propagation reading and per the gravitational waves consequence's discussion). The question is whether demanding that light's null geodesics behave consistently — without anomalous refraction, dispersion, or direction-dependence — forces $\gamma_v = 1$.

Path 2 has been used implicitly in the light deflection and Shapiro delay proofs. Both proofs derived their results assuming the framework's metric structure with $\gamma_v$ as a free parameter, and both gave results parameterized by $(1 + \gamma_v)$. The factor of two between $\gamma_v = 0$ and $\gamma_v = 1$ is the difference between Einstein's 1911 and 1915 light-deflection predictions. Observation distinguishes between them; theory needs to do so as well.

The question for Equal-Response: does the structure of light's null propagation in the framework's vacuum force $\gamma_v$ to a specific value?

The framework's null condition for light gives, to first order:
$$\frac{dl}{dt} = c\left(1 + (1 + \gamma_v)\frac{\Phi}{c^2}\right)$$

This is the coordinate speed of light in the weak-field limit. For light to propagate without anomalous direction-dependence, the coefficient $(1 + \gamma_v)$ must be the same for radial and tangential propagation. This is automatically true under spherical symmetry (the spatial metric is isotropic, so the coefficient is the same in all directions).

For light to propagate at the right *speed* — for observers everywhere to measure $c$ locally — any positive value of $\gamma_v$ works. The constraint is not on $\gamma_v$ but on the relation between coordinate and proper distances, which is what $\gamma_v$ parameterizes.

So Path 2 alone does not force $\gamma_v = 1$ either. It forces null propagation to be isotropic and locally-$c$, but these constraints are satisfied by any $\gamma_v$ that respects spherical symmetry.

A stronger version of Path 2: demand that light's null geodesics minimize travel time in some specific sense — a Fermat-like principle for the framework's vacuum. The spatial-curvature-as-vacuum-extent commitment from `consequence_curvature_as_spatial_differential.md` suggests that null paths should somehow "minimize vacuum traversed" or follow analogous principles. Whether this gives a tighter constraint on $\gamma_v$ depends on how the principle is formalized.

This connects to the framework's open question about what null geodesics actually correspond to physically — the active-exchange picture from the redshift proof versus the metric-geodesic picture from the GR-style derivations. If the two pictures must agree quantitatively, that agreement might constrain $\gamma_v$.

---

## Path 3: Vacuum as One Substance

This is the framework-native path. Postulate 1 commits to vacuum being one substance — spacetime itself, not a field on spacetime and not a coupled time-and-space pair. The unity candidate's Equal-Response component is essentially the claim that this one-substance ontology forces equal coefficients.

The argument runs: if vacuum is one substance, and a perturbation of this substance produces both temporal and spatial mapping changes, then the response of the substance to the perturbation should be uniform across the components produced. A perturbation that produced different temporal and spatial responses would be acting on the substance differently in different components — but the substance has no internal partition into "temporal aspect" and "spatial aspect" that would justify differential response.

Stated this way, Equal-Response is a structural consequence of vacuum-monism. Different coefficients for time and space would mean treating them as separate aspects of vacuum that respond independently, contradicting the one-substance commitment.

This is the most natural framework argument. It is also the most hand-wavy. The "one substance, uniform response" intuition doesn't have rigorous content until you specify what "uniform response" means mathematically. Without a formal definition of the vacuum's mathematical structure, the argument is closer to a slogan than to a derivation.

What would make Path 3 rigorous: pinning down the vacuum's mathematical structure such that the one-substance commitment has formal content. If the vacuum is a tensor field of some kind, "uniform response" means the perturbation acts on all tensor components equally. If the vacuum has scalar-plus-other structure, "uniform response" might mean something different. If the vacuum has scalar structure only, "uniform response" might not have meaningful content distinct from spherical symmetry.

The mathematical structure of the vacuum is on the framework's open work list. Path 3 is the path most directly tied to that question. Resolving the vacuum's mathematical structure would likely close Equal-Response simultaneously, since the structural argument for one-substance-uniform-response would become rigorous once the structure is specified.

This is also the path that connects most directly to the framework's identity postulate. Postulate 1 says vacuum is spacetime, not vacuum-living-on-spacetime. The Equal-Response claim is a quantitative version of this same identity at the metric level: time-mapping and spatial-mapping aren't separate metric components that happen to be coupled, they're two readings of the same vacuum perturbation.

---

## Path 4: PPN Reverse-Engineering as Constraint

This path is not a derivation of Equal-Response from the framework's commitments. It is the inverse: treat $\gamma_v = 1$ as fixed by observation (PPN $\gamma$ is constrained to $1 + (2.1 \pm 2.3) \times 10^{-5}$ by Cassini), and ask what this implies about the framework's vacuum structure.

Observation requires $\gamma = 1$. Different vacuum structures predict different generic $\gamma$ values, though the specific predictions depend on theory class:

Tensor-like coupling (the framework's response transforms as a rank-2 tensor under the underlying symmetry) generically predicts $\gamma = 1$. This matches GR.

Scalar-tensor theories produce $\gamma$ values that depend on coupling parameters. In Brans-Dicke gravity, $\gamma = (1+\omega)/(2+\omega)$, approaching 1 only as $\omega \to \infty$. Solar-system constraints on $\gamma = 1$ therefore force $\omega$ to be very large — equivalent to saying the scalar contribution must be strongly suppressed. Other scalar-tensor theories give other relations, but the general pattern is that $\gamma = 1$ requires the scalar component to be suppressed.

Many pure scalar or scalar-dominated theories produce $\gamma \neq 1$. The classic scalar-style "half-deflection" result corresponds, in the framework's PPN convention $\Delta\theta = (1+\gamma_v)(2GM/bc^2)$, to $\gamma_v = 0$ rather than $\gamma_v = 1/2$ — Einstein's 1911 prediction was half the GR value because it included only the time-mapping contribution, with no spatial-mapping contribution at all. Pure scalar theories are ruled out by observation regardless of how the scalar limit is parameterized.

Higher-tensor or richer structures might predict still other values.

The constraint from $\gamma = 1$ therefore selects the framework's vacuum structure as either pure-tensor or scalar-tensor with suppressed scalar component. It rules out pure-scalar. This is consistent with what the unity candidate already noted (observational constraints rule out pure scalar gravitational waves but permit scalar-tensor structures with suppressed scalar components).

Path 4 is not a derivation but a constraint. It says: whatever the framework's vacuum structure ends up being, it must be one of the structures consistent with $\gamma = 1$. This rules out some possibilities and points toward others. It does not by itself derive $\gamma_v = 1$ from the framework's commitments — observation is doing the work of pinning $\gamma$ to 1, and the framework is being constrained to be consistent with that.

But Path 4 connects directly to Path 3. If the vacuum's mathematical structure must be tensor-like (or scalar-tensor with suppressed scalar) to match observation, then Path 3's structural argument can be made rigorous. The vacuum is a tensor object; perturbations act on it tensorially; tensorial response gives equal coefficients; Equal-Response follows.

So Path 4's role is constraint identification rather than derivation. It tells the framework what kind of vacuum structure it must have, which feeds into Path 3 to give the structural argument concrete content.

---

## Path 5: Variational Principle / Energy Minimization

This path takes Postulate 5 seriously as the source of Equal-Response. Postulate 5 commits the framework to vacuum configurations being minimum-energy given constraints. A static spherically symmetric mass-pinned configuration is the answer to a minimization problem — among all configurations satisfying the constraint, the actual vacuum takes the one that minimizes total configuration energy.

The question for Equal-Response: among all configurations parameterized by $\gamma_v$, does the energy minimum occur specifically at $\gamma_v = 1$?

The argument runs: $\gamma_v$ is a parameter describing how the vacuum's perturbation distributes between time-mapping and spatial-mapping responses. Different values of $\gamma_v$ correspond to different ways of allocating the perturbation amplitude across the two channels. If the configuration energy depends on this allocation, there is a specific $\gamma_v$ that minimizes the energy.

Why might $\gamma_v = 1$ be the minimum? Several possibilities:

A configuration with $\gamma_v \neq 1$ has a mismatch between time-mapping and spatial-mapping responses to the same underlying perturbation. Mismatched response might fail to satisfy a balance condition the framework's structure requires — for instance, the vacuum exchange dynamics might not close properly when temporal and spatial responses are imbalanced.

Configuration energy in the framework should be a function of perturbation amplitude. If $\gamma_v$ parameterizes channel imbalance and the energy is a function of imbalance with minimum at the balanced point, then $\gamma_v = 1$ would be the variational minimum. The functional form of the energy versus $\gamma_v$ would need to be derivable from the framework's commitments, which currently don't specify it.

The framework's energy-conservation reading might force this. If perturbing the vacuum costs energy and the cost is determined by the perturbation amplitude as a single quantity, then the energy decomposed into time-component and space-component contributions would naturally split equally for symmetric reasons — any unequal split would correspond to extracting more energy from one channel than from the other, which is what an asymmetric response would mean.

This is the most distinctively framework-native potential derivation. Unlike Path 3 (which appeals to the structural one-substance commitment) or Path 4 (which constrains via observation), Path 5 grounds Equal-Response in the framework's dynamical principle: configurations minimize energy. If the minimization gives $\gamma_v = 1$, Equal-Response becomes a consequence of Postulate 5 rather than a structural claim about the vacuum's mathematical type.

What would make Path 5 rigorous: a specific expression for configuration energy as a function of $\gamma_v$ in static spherically symmetric perturbations. The energy should be derivable from Postulate 4 (configurations carry energy) plus the framework's commitment that vacuum exchange is the energy mechanism. With such an expression, minimization is a calculus problem: find the $\gamma_v$ that minimizes the energy.

Path 5 also has appealing connections to other framework themes. It would tie Equal-Response to the framework's distinctive ontological move (energy ledger closed when vacuum is included) rather than to auxiliary structure imported from GR or PPN considerations. It would make the unity of the framework's metric a consequence of dynamics rather than a separate commitment. And it would suggest that other underdetermined parameters in the framework (the second-order $\beta$ identification, possibly aspects of wave mode structure) might also be determined by similar variational arguments.

The path is genuinely speculative — the framework hasn't worked out what configuration energy as a function of perturbation amplitude actually looks like, and without that, the minimization can't be performed. But it points at a derivation route that would be more distinctive than Path 3 + Path 4 if it works. If energy minimization forces $\gamma_v = 1$, Equal-Response becomes a thermodynamic necessity rather than a structural claim about vacuum tensorial nature.

This path may eventually deserve its own candidate document. For now, it's named here as one of the active derivation routes worth developing.

---

## What This Analysis Concludes

Equal-Response is not derivable from spherical symmetry alone. Spherical symmetry forces isotropy of the spatial response, but isotropy is consistent with any $\gamma_v$ that maintains spherical structure. Something more is needed.

Path 1 (local Lorentz invariance) and Path 2 (null propagation consistency) constrain the relation between $g_{00}$ and $g_{ij}$ but neither alone forces $\gamma_v = 1$. Stronger versions of either path — using global Lorentz consistency or Fermat-like null principles — might give tighter constraints, but whether they pin $\gamma_v$ to exactly 1 is open.

Path 3 (vacuum as one substance) is the framework-native structural argument and the most directly tied to the identity postulate. It is currently a slogan rather than a derivation. Making it rigorous requires pinning down the vacuum's mathematical structure.

Path 4 (PPN reverse-engineering) constrains the vacuum structure to be tensor-like or scalar-tensor with suppressed scalar component. Combined with Path 3, this gives one plausible derivation route: tensor-like vacuum structure produces equal coefficients automatically.

Path 5 (variational principle / energy minimization) is the framework-native dynamical argument. It would derive Equal-Response from Postulate 5's minimum-energy commitment if configuration energy as a function of $\gamma_v$ has its minimum at $\gamma_v = 1$. This is potentially the most distinctive route — it would ground Equal-Response in the framework's own dynamics rather than in tensor structure.

Two candidate routes therefore stand out: the structural route (Path 3 + Path 4) through the vacuum's mathematical structure, and the dynamical route (Path 5) through energy minimization. Both are speculative; both are distinct enough that pursuing them in parallel would be useful.

The most likely route to deriving Equal-Response runs through one of these or some combination. This is Tier 3 work on the framework's research priority list, but Equal-Response gives it a concrete entry point. The question "what is the vacuum mathematically?" can be partially answered by "whatever it is, it must produce $\gamma_v = 1$ under static spherically symmetric perturbation, and it must do so as a minimum of configuration energy."

Stated as a research target: define a vacuum perturbation object whose static spherical solution produces $\gamma_v = 1$. The simplest candidate is a tensor-like vacuum perturbation whose static spherical weak-field solution gives the PPN relation $\gamma_v = 1$ in the framework's metric coordinates. Whether this is unique or whether other structures work is open.

---

## Concrete Next Targets

Several pieces of work would advance Equal-Response derivation:

**Formalize the strongest version of Path 1.** Work out what local Lorentz invariance combined with consistent transformation behavior across nearby points actually forces. Determine whether this argument alone constrains $\gamma_v$ or only the relation between $g_{00}$ and $g_{ij}$.

**Formalize a Fermat-like principle for null propagation in the framework's vacuum.** The framework treats null paths as paths along which photons exchange energy with vacuum. Whether this exchange picture gives a variational principle that constrains $\gamma_v$ is open work that connects Path 2 to Path 3.

**Define the simplest vacuum structure that produces $\gamma_v = 1$.** Probably tensor-like. Specify its perturbation equation under static spherical symmetry and verify that the static solution gives the PPN $\gamma_v = 1$ relation in the framework's metric coordinates.

**Connect to scalar-tensor literature.** If the framework is scalar-tensor with suppressed scalar component, the suppression mechanism should be derivable from the framework's commitments. Brans-Dicke gravity has a free parameter $\omega$ that tunes scalar contribution; the framework would need either to derive its analogue or to argue the scalar contribution vanishes structurally.

**Develop Path 5 into its own candidate document.** Specify configuration energy as a function of $\gamma_v$ for static spherically symmetric perturbations, derive the value of $\gamma_v$ that minimizes the energy, and check whether minimization gives $\gamma_v = 1$. If it does, Equal-Response becomes a consequence of Postulate 5. This is potentially the most distinctive derivation route because it grounds Equal-Response in the framework's own dynamics.

---

## Open Questions

**Is Equal-Response equivalent to vacuum being a tensor field?** Path 3 plus Path 4 suggest yes, but a rigorous equivalence proof would be substantial. If equivalent, deriving Equal-Response and pinning down the vacuum's mathematical structure are the same work.

**Are there non-tensor structures that produce $\gamma_v = 1$?** Path 4 rules out pure-scalar but doesn't establish that tensor is the unique answer. Some richer structures might satisfy the constraint.

**Does Equal-Response hold beyond static spherical symmetry?** The unity candidate is explicit about its static spherically symmetric scope. Whether the same coupling holds for time-varying or non-spherical configurations (waves, asymmetric mass distributions) is open. This connects to the wave-mode-structure question.

**What about the second-order $g_{00}$?** The candidate `candidate_second_order_time_metric_from_redshift.md` adopts $\beta = 1$ via a separate informal extension. Equal-Response specifically addresses the first-order spatial coefficient. Whether deriving Equal-Response also constrains second-order behavior, or whether $\beta = 1$ requires separate derivation, is open.

**Do the structural and dynamical routes converge?** Path 3 + Path 4 derive Equal-Response from vacuum being a tensor field. Path 5 derives it from energy minimization. If both routes work, they should give the same answer. Whether they're independently true, or whether one implies the other, or whether they're equivalent statements of the same underlying fact, is open. The convergence (or lack thereof) might itself be informative about the framework's structure.

---

## Status

Equal-Response remains adopted rather than derived. The unity candidate's provisional status is unchanged.

What this document contributes: a classification of derivation paths, identification of which paths constrain $\gamma_v$ and which only constrain relations, identification of two plausible derivation routes (the structural route through vacuum mathematical structure, and the dynamical route through energy minimization), and concrete next targets.

The framework's weak-field metric remains closed by the unity candidate's adoption rather than by a derivation. The light deflection, Shapiro delay, and perihelion precession proofs remain provisional. Closing this provisional status requires actually performing one of the derivation paths analyzed here, which remains future work.

If the framework eventually derives Equal-Response — most likely through resolving the vacuum's mathematical structure (Path 3 + Path 4) or through working out energy minimization (Path 5) — this document's role becomes historical. It records what the framework knew and considered before the derivation existed. Until then, it serves as a roadmap.

---

## References

Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Reviews in Relativity*, 17(1), 4.

Brans, C., & Dicke, R. H. (1961). Mach's Principle and a Relativistic Theory of Gravitation. *Physical Review*, 124(3), 925–935.