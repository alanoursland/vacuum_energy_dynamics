# Development Plan

## What This Document Is

This document describes the current development state of the framework and lays out the next work targets.

It is not a theorem, postulate, consequence, or empirical consequence. It is a planning document. It belongs at the framework level or in a process/development area rather than inside the numbered theorem chain.

The framework currently has a coherent weak-field recovery spine. The next phase is to stabilize that spine, make the dependency structure clear, and then use it as a constraint on future field-equation design.

## Current State

The current version has three main layers.

First, the postulate layer defines the framework's ontology and local rules:

- P1: Vacuum-Energy Equivalence
- P2: Vacuum-Spacetime Identity
- P3: Vacuum Energy Density
- P3a: Spatial Differential is Curvature
- P4: Curvature Contains Energy
- P5: Vacuum Seeks Minimum Energy Configuration
- P6: Vacuum Exchange in Gradients
- P7: Static Exterior Vacuum Compensation
- P8: Static Exterior Temporal Self-Coupling
- SR Imports

Second, the foundation theorem layer derives the framework's first gravitational results and exterior recovery coefficients:

- T1: Gravitational Redshift
- T2: Gravitational Time Dilation
- T3: Reciprocal Exterior Scaling
- T4: Second-Order Temporal Self-Coupling

Third, the weak-field layer assembles those results into the static exterior weak-field metric and derives classical tests:

- T5: Static Exterior Weak-Field Metric
- T6: Newtonian Limit
- T7: Light Deflection
- T8: Shapiro Delay
- T9: Perihelion Precession
- Summary: Weak-Field GR Recovery

This is enough to say that the framework recovers the standard static exterior weak-field tests of general relativity through one-post-Newtonian order from the current postulate set.

P7 and P8 are part of the current theory. They are not external assumptions or provisional patches. They are also important design targets: a future field equation should explain why their exterior recovery behavior holds.

## Current Recovery Chain

The framework's weak-field recovery chain is:

P7 implies T3.

T3 gives

$$\gamma=1.$$

P8 implies T4.

T4 gives

$$\beta=1.$$

T3 and T4 feed into T5.

T5 gives the static exterior weak-field metric:

$$ds^2=-\left(1-\frac{2U}{c^2}+2\frac{U^2}{c^4}\right)c^2dt^2+\left(1+2\frac{U}{c^2}\right)d\vec{x}^{\,2}+O(c^{-6})_{tt}+O(c^{-4})_{ij}.$$

T5 feeds into T6 through T9.

T6 gives Newtonian acceleration:

$$\frac{d^2\mathbf{x}}{dt^2}=\nabla U.$$

For a point mass,

$$\frac{d^2\mathbf{x}}{dt^2}=-\frac{GM}{r^2}\hat{\mathbf r}.$$

T7 gives light deflection:

$$\Delta\theta=\frac{4GM}{bc^2}.$$

T8 gives Shapiro delay:

$$\Delta t_{\text{one-way}}\approx\frac{2GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).$$

T9 gives perihelion precession:

$$\Delta\varpi=\frac{6\pi GM}{a(1-e^2)c^2}.$$

This is the framework's current weak-field recovery result.

## Immediate Stabilization Tasks

### 1. Add a Root README

The project needs a root-level `README.md`.

Its job is to orient a reader before they enter the theorem chain.

It should explain:

- what the framework is trying to do,
- what the folder structure means,
- what the postulate/theorem taxonomy means,
- which results are currently recovered,
- which results depend on which postulates,
- and what work remains.

Suggested structure:

```text
# Vacuum Energy Dynamics Theory v3

## Project Aim
## Directory Structure
## File Taxonomy
## Current Postulates
## Current Theorem Chain
## Weak-Field Recovery Status
## Development Status
## Reading Order
```

The README should be short enough that a new reader can understand the whole package in one sitting.

### 2. Add an Overview Document

The project should also have an `overview.md`.

The README can be practical and navigational. The overview can be conceptual.

Suggested sections:

```text
# Overview

## Core Claim
## Vacuum as Energy
## Vacuum as Spacetime
## Curvature as Differential Vacuum Extent
## Configuration Energy
## Minimum-Energy Dynamics
## Vacuum Exchange in Gradients
## Static Exterior Recovery
## Weak-Field GR Recovery
## Remaining Development Targets
```

This document should describe the framework's conceptual architecture without reproducing every proof.

### 3. Add a Dependency Graph

The project should have a dependency document.

Suggested filename:

```text
dependency_graph.md
```

Its job is to make the epistemic structure visible.

Suggested content:

```text
P1, P2, P3, P3a, P4, P5, P6
  -> core ontology and dynamics

P7
  -> T3
  -> gamma = 1

P8
  -> T4
  -> beta = 1

T1, T2, T3, T4
  -> T5

T5
  -> T6, T7, T8, T9
```

It should also classify results by dependency:

```text
Core postulates:
  P1-P8

Derived directly from the foundational ontology and interaction rules:
  T1, T2

Derived using P7:
  T3, gamma = 1, light deflection, Shapiro delay

Derived using P8:
  T4, beta = 1

Derived using the assembled weak-field metric:
  T5, T6, T7, T8, T9, weak-field GR recovery
```

T6 should get a note: the leading Newtonian limit is more robust than the full assembled T5 dependency chain because it uses only the first-order temporal coefficient, but in the current file structure it is written downstream of T5 for cleanliness.

### 4. Formatting and Notation Audit

The current documents should be audited before the theory grows further.

Specific issues to check:

- Display equations should not begin with malformed Markdown like `# $$...`.
- Multi-line equations should use formatting that survives the editor being used.
- The potential convention should be consistent.
- Metric coefficient notation should be consistent.
- Imports sections should not make postulates depend on theorems.
- T3's areal-radius convention should not be confused with T5's PPN-compatible coordinates.
- P8/T4 should not be accidentally worded as a universal scalar metric ansatz.

Recommended equation style for maximum copy safety:

```markdown
$$-g_{tt}=1-\frac{2U}{c^2}+2\frac{U^2}{c^4}+O(c^{-6}).$$
```

Avoid display equations that become split across headings or lists in the editor. If multi-line equations are needed, put the opening and closing `$$` on their own lines and keep the equation body free of blank lines.

### 5. Write Field-Equation Design Constraints

Suggested filename:

```text
field_equation_design_constraints.md
```

This should be the next important development document after the README, overview, dependency, and formatting cleanup.

Its role is to say what any future field equation must reproduce.

Minimum constraints:

1. It must reproduce P7/T3 in the static source-free exterior limit: $$A(r)B(r)=1.$$
2. It must reproduce P8/T4 in the static source-free weak-field temporal sector: $$d\ln\alpha=-\frac{dU}{c^2}+O(c^{-6}).$$
3. It must reproduce the assembled T5 weak-field metric.
4. It must recover Newtonian acceleration.
5. It must recover light deflection, Shapiro delay, and perihelion precession.
6. It must avoid reducing the full framework to a universal scalar metric.
7. It must allow directional/tensor-like structure consistent with P3a and P4.

This document should explicitly frame P7 and P8 as design targets for the future field equation. The goal is not to keep P7 and P8 permanently primitive if a deeper derivation becomes available. The goal is to derive them from the future field equation or configuration-energy functional.

## Main Research Frontier

The next deep research target is:

**derive P7 and P8 from a deeper field equation or configuration-energy functional.**

The weak-field recovery suite is now built. The next question is why the recovery postulates hold.

There are three main routes.

### Route A: Configuration-Energy Functional

Develop a configuration-energy functional whose static source-free exterior minimum implies P7 and P8.

The target would be:

- static exterior compensation emerges from energy minimization,
- temporal-radial reciprocal scaling follows as a minimum-energy condition,
- temporal self-coupling follows from the way temporal configuration energy compounds,
- the weak-field exterior solution yields $\gamma=1$ and $\beta=1$.

This route is most native to P4 and P5.

The key question is:

What functional of vacuum configuration has P7 and P8 as its static exterior weak-field minimum conditions?

### Route B: Vacuum Mathematical Structure

Specify the mathematical structure of the vacuum deeply enough that P7 and P8 follow.

Possibilities include:

- tensor-like vacuum structure,
- constrained scalar-tensor structure,
- directional scale-factor structure,
- mode decomposition into trace, shear, and exchange channels,
- configuration variables whose static exterior trace-free and temporal self-coupling behavior produce the required weak-field coefficients.

This route connects to the earlier structure-search work. It should preserve directional/tensor-like content and avoid the scalar-metric failure mode.

The key question is:

What kind of vacuum object has static exterior perturbations whose weak-field limit gives $\gamma=1$ and $\beta=1$?

### Route C: Source Law and Mass Constraint

The framework still uses the weak-field exterior Newtonian potential profile

$$U=\frac{GM}{r}.$$

A future derivation should explain how mass-as-constraint produces this profile.

This requires a source law or constraint equation connecting localized mass-energy to the exterior vacuum configuration.

The key question is:

How does a localized mass constraint determine the exterior potential or curvature profile?

This may be separable from P7/P8, but ultimately the field equation must handle all of these at once.

## Medium-Term Physics Targets

After the stabilization and field-equation design documents, the next physics targets are:

### 1. Derive the Source Law

Current weak-field theorems use

$$U=\frac{GM}{r}.$$

This should eventually be derived from the framework's mass-as-constraint picture.

A future theorem or candidate document might be:

```text
t_or_h_source_law_for_static_mass.md
```

or

```text
candidate_mass_constraint_source_law.md
```

### 2. Strong-Field Exterior Structure

The current framework recovers the weak-field exterior metric but not the full Schwarzschild solution.

A future research document should ask whether the framework predicts exact Schwarzschild behavior or deviations in strong fields.

Possible filename:

```text
candidate_strong_field_exterior_structure.md
```

### 3. Rotating Sources and Frame Dragging

The current metric has no off-diagonal terms.

A future framework must address rotating sources and frame dragging.

Possible filename:

```text
candidate_rotating_exterior_frame_dragging.md
```

### 4. Gravitational Waves

P5 already suggests finite-speed relaxation and wave-like departures from minimum-energy configuration.

A future branch should derive gravitational-wave content:

- propagation speed,
- polarization modes,
- tensor/scalar content,
- energy carried by waves,
- relation to vacuum configuration energy.

Possible filename:

```text
candidate_gravitational_wave_modes.md
```

### 5. Cosmology

The framework distinguishes configuration-regime processes from substance-regime processes. Cosmic expansion is likely substance-regime vacuum creation, not P7-style exterior compensation.

Future cosmic work should address:

- expansion as vacuum creation,
- relation to energy accounting,
- dark energy / cosmological constant interpretation,
- whether expansion changes total vacuum amount,
- why local vacuum density remains constant under P3.

Possible files in `cosmic/`:

```text
e_or_c_cosmic_expansion_as_vacuum_creation.md
candidate_cosmological_dynamics.md
```

### 6. Quantum / Microscopic Model

The `quantum_model/` folder should eventually address what the vacuum is mathematically or microscopically.

Targets:

- why vacuum density is finite,
- whether configuration energy has a natural functional form,
- whether P7 and P8 can be derived from microscopic structure,
- whether vacuum exchange is quantized,
- how matter corresponds to vacuum constraints or excitations.

Possible files:

```text
candidate_vacuum_microstructure.md
candidate_configuration_energy_functional.md
candidate_exchange_quantization.md
```

## Near-Term File Plan

The recommended near-term file sequence is:

```text
README.md
overview.md
dependency_graph.md
development_plan.md
field_equation_design_constraints.md
```

Then, if continuing physics development:

```text
candidate_configuration_energy_functional.md
candidate_mass_constraint_source_law.md
candidate_strong_field_exterior_structure.md
candidate_gravitational_wave_modes.md
candidate_cosmological_dynamics.md
```

## Current Risks

### Risk 1: P7 and P8 Look Like Patches

P7 and P8 currently do important work. They close the weak-field exterior recovery.

Because they reproduce GR-relevant exterior coefficients, a reader may suspect they were chosen only to force agreement.

Mitigation: treat P7 and P8 explicitly as field-equation design targets and prioritize deriving them. Make clear that they are framework postulates now, but they should eventually become consequences of the deeper configuration-energy functional.

### Risk 2: Scalar-Metric Collapse

A scalar exponential metric can reproduce some desired weak-field coefficients, but it risks erasing the framework's directional/tensor-like structure.

Mitigation: keep P7 and P8 separate. Do not combine them into a universal scalar ansatz. Preserve P3a/P4 directional structure.

### Risk 3: Source Law Remains Imported

The current weak-field proofs use the Newtonian exterior potential profile.

Mitigation: develop the mass-constraint source law as a separate target.

### Risk 4: Coordinate Confusion

The framework now uses areal-radius language in T3, temporal scale-factor language in T4, and PPN-compatible coordinates in T5 through T9.

Mitigation: maintain convention notes and possibly add a notation glossary.

### Risk 5: Overclaiming GR Recovery

The framework recovers static exterior weak-field tests through one-post-Newtonian order. It does not yet recover full GR.

Mitigation: keep the recovery scope explicit in README, overview, summary, and theorem status sections.

## Success Criteria for the Next Phase

The next phase succeeds if the framework has:

1. A clean reader entry point.
2. A clear dependency graph.
3. Stable notation.
4. Correctly formatted equations.
5. A documented weak-field recovery chain.
6. A field-equation design constraints document.
7. A concrete research target for deriving P7 and P8.
8. No reliance on a universal scalar metric ansatz.
9. A clear statement of what has and has not been recovered.

## Development Priority Order

The recommended order is:

1. Clean formatting in T4 through T9.
2. Write README.
3. Write overview.
4. Write dependency graph.
5. Add this development plan.
6. Write field-equation design constraints.
7. Begin candidate configuration-energy functional work.
8. Begin source-law derivation work.
9. Only then branch into strong fields, waves, cosmology, and quantum model.

## Summary

The framework now has a coherent weak-field recovery spine.

The current theory can say:

Given the current postulate set, the framework recovers the standard static exterior weak-field tests of general relativity through one-post-Newtonian order.

The next job is not to keep adding weak-field tests. The next job is to explain why P7 and P8 hold.

That means the development focus should shift from weak-field recovery proofs to field-equation design, configuration-energy functionals, vacuum mathematical structure, and source-law derivation.
