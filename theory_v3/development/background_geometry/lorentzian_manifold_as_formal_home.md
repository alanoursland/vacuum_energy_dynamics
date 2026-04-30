# Smooth Lorentzian Manifold as the Formal Home

## What This Document Is

This document argues for using a smooth Lorentzian manifold with metric as the preferred mathematical setting for future development of the framework.

It is a development note, not a postulate. It does not add a new commitment to the theory. No theorem depends on this document.

Its purpose is to explain why the smooth Lorentzian manifold is the natural formal language for the framework, how that language works, and how it connects to the framework's ontology: vacuum as spacetime, metric as vacuum configuration, and curvature as variation in vacuum extent.

Suggested file location:

```text
04_development/background_geometry/lorentzian_manifold_as_formal_home.md
```

The core recommendation is:

```text
Use a smooth Lorentzian manifold as the formal representation of vacuum/spacetime, with the metric interpreted as the vacuum's local geometric configuration.
```

Riemannian geometry remains useful for spatial slices, static toy models, and informal graph intuition. But the full theory needs Lorentzian geometry because it includes time, light cones, null propagation, local special relativity, redshift, and time dilation.

This is the same geometric setting used by standard GR, but it is not the same theoretical commitment. The manifold-and-metric language supplies the relativistic geometry. The framework's distinct content lies in interpreting the metric as vacuum configuration and in developing a field equation from vacuum substance and configuration-energy principles rather than assuming Einstein's equation as primitive.

## The Thesis

The framework should be developed on a smooth manifold equipped with a Lorentzian metric:

$$(M,g).$$

Here:

- $M$ is the manifold: the collection of spacetime events or locations.
- $g$ is the metric: the mathematical object that tells us proper time, proper length, causal structure, volume, and curvature.
- The metric $g$ is interpreted physically as the vacuum's local geometric configuration.

The manifold is not a container that the vacuum sits inside.

The manifold-with-metric is the mathematical representation of the vacuum/spacetime structure itself.

This matches the framework's core ontology:

- P2 says vacuum is spacetime.
- The manifold represents spacetime.
- Therefore the manifold-with-metric represents the vacuum in its configured state.

The metric should not be treated as a free-floating mathematical field placed on top of a separate background space. In this framework, the metric is the vacuum's intrinsic structure.

## Same Geometric Arena as GR, Different Theory

The recommended formal setting is the same geometric category used by standard general relativity: a smooth four-dimensional Lorentzian manifold with metric.

Standard GR represents spacetime as

$$(M,g),$$

where $M$ is a smooth four-dimensional manifold and $g$ is a Lorentzian metric. The metric determines proper time, proper distance, light cones, null paths, curvature, and volume.

This framework should use the same kind of geometric arena because it needs the same relativistic structures: local special relativity, causal order, gravitational time dilation, redshift, null propagation, and curvature.

But sharing the same geometric arena does not mean sharing the same theory.

In standard GR, the metric is determined by Einstein's field equation:

$$G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}.$$

In this framework, the metric is interpreted as vacuum configuration: the directional arrangement and extent of vacuum. The future field equation is not yet fixed. It should eventually be derived from the framework's ontology: vacuum substance, configuration energy, minimum-energy behavior, and exchange dynamics.

So the distinction is:

```text
Standard GR:
  smooth Lorentzian manifold + Einstein field equation
  metric = spacetime geometry

This framework:
  smooth Lorentzian manifold as formal language
  metric = vacuum configuration
  field equation = future configuration/substance dynamics to be derived
```

What is shared is the geometric language, the relativistic structure, and the mathematical toolkit: covariant derivatives, curvature tensors, geodesics, variational principles, and null conditions.

What differs is the interpretation of the metric, the source of the field equation, and the ontological commitment: this framework treats the metric as encoding vacuum substance and configuration, not merely as abstract spacetime geometry.

The weak-field theorem chain already demonstrates this relationship. It uses the same metric language and the same null-condition machinery as standard GR, but arrives at the exterior metric through the framework's own postulates rather than through the Einstein field equation.

The framework does not reject Lorentzian geometry. It reinterprets what the metric is and seeks a different foundational route to the equation that determines it.

## Why This Is a Development Note Rather Than a Postulate

This document should not be put in the postulate folder yet.

The current postulates already carry the theory's formal commitments. This document only identifies the best mathematical language for future development.

The framework can use smooth Lorentzian geometry as its working language without making a new postulate that says "spacetime is a Lorentzian manifold." That distinction matters because the future field equation is still under development. The geometry language should guide that development without prematurely constraining it.

A future version of the framework may decide to make this formal setting explicit in a postulate or foundation document. For now, it is safer to keep it as background geometry.

The document's role is:

- to orient readers who have not worked with differential geometry,
- to explain why Lorentzian rather than purely Riemannian geometry is needed,
- to connect the graph intuition back to smooth geometry,
- and to prevent confusion between intrinsic geometry and embedding-space pictures.

## What Is a Manifold?

A manifold is a space that may be globally complicated but looks locally like ordinary coordinate space.

A two-dimensional sphere is the standard example. Globally, a sphere is curved and closed. But if you zoom in on a small patch of the Earth's surface, that patch looks approximately like a flat plane. You can draw local coordinates on it, such as latitude and longitude, or local east/north coordinates.

A four-dimensional spacetime manifold works similarly. Locally, it can be described by coordinates such as

$$(t,x,y,z).$$

But the coordinates are labels. They are not the physical content.

The physical content is in coordinate-independent structures defined on the manifold. The most important of these is the metric.

## Coordinates Are Labels, Not Physics

A coordinate system assigns numbers to points on the manifold.

For example, one observer might label an event by

$$(t,x,y,z),$$

while another observer uses different labels

$$(t',x',y',z').$$

The event itself is not changed by relabeling. Only the description changes.

This distinction matters for the framework because the informal graph model can make it look like there are two coordinate systems:

1. an internal graph coordinate system, defined by adjacency and paths;
2. an external embedding coordinate system, used to draw or construct the graph.

The formal manifold picture resolves this.

Only intrinsic geometry is physical. Coordinate labels are descriptive tools. Embedding coordinates are visualization scaffolding, not part of the physics.

The framework should therefore avoid treating the graph's embedding space as real. The physical content is the intrinsic metric structure.

## What Is a Metric?

A metric is the object that tells us how to compute physical intervals.

In ordinary Euclidean space, the distance between nearby points is

$$ds^2=dx^2+dy^2+dz^2.$$

This is a Riemannian metric: all directions contribute positively to distance.

In spacetime, the interval is different. In flat special-relativistic spacetime, the interval can be written as

$$ds^2=-c^2dt^2+dx^2+dy^2+dz^2.$$

This is the Minkowski metric. The minus sign on the time part is essential. It means time is not just another spatial direction.

In a curved spacetime, the metric becomes position-dependent:

$$ds^2=g_{\mu
u}(x)dx^\mu dx^
u.$$

The symbols $g_{\mu
u}$ are the metric components. They encode how the vacuum/spacetime structure converts coordinate differences into physical intervals.

In the framework's language, the metric tells us how much vacuum extent corresponds to coordinate displacement in each direction.

## Riemannian Versus Lorentzian Geometry

A Riemannian metric has all positive signs. It measures spatial distances.

A Lorentzian metric has one time direction and three space directions. Its signature is usually written as

$$(-,+,+,+).$$

A Lorentzian metric is a special case of a pseudo-Riemannian metric.

The full framework needs Lorentzian geometry because it includes:

- time,
- causal order,
- light cones,
- null paths,
- clocks,
- redshift,
- time dilation,
- local special relativity,
- and the invariant speed of light.

A purely Riemannian manifold cannot represent these features directly because it has no null directions and no causal structure.

However, Riemannian geometry is still useful in limited contexts.

A spatial slice of spacetime can be Riemannian. If a spacetime is static and we look only at its spatial geometry at a fixed time, that spatial geometry is usually positive-definite. This is the setting where many graph and point-cloud intuitions are easiest to picture.

So the clean rule is:

```text
Use Lorentzian geometry for full spacetime. Use Riemannian geometry for spatial slices and static intuition.
```

## Proper Time, Proper Length, and Null Paths

The Lorentzian metric classifies intervals into three types.

A timelike interval is one that a massive object or clock can follow. With the signature used here, timelike intervals have

$$ds^2<0.$$

The proper time along a timelike path is

$$d	au=rac{\sqrt{-ds^2}}{c}.$$

A spacelike interval is a spatial separation. It has

$$ds^2>0.$$

A null interval is the path of light. It has

$$ds^2=0.$$

The null condition is central to weak-field light propagation. T7 and T8 use

$$ds^2=0$$

to derive light deflection and Shapiro delay.

This is one of the main reasons the full framework needs Lorentzian geometry. A Riemannian manifold has no null paths.

## Local Special Relativity

The framework imports local special relativity.

In geometric terms, this means that at every sufficiently small region of spacetime, the metric can be approximated by the flat Minkowski metric:

$$ds^2pprox -c^2dt^2+dx^2+dy^2+dz^2.$$

This does not mean spacetime is globally flat. It means every observer in a local inertial frame measures local physics according to special relativity.

Curvature appears when these local inertial frames cannot be patched together globally without mismatch.

This is exactly the right structure for the framework. Local observers measure ordinary local clocks, rulers, and light speed. Gravitational effects appear in how different local frames relate across a curved vacuum configuration.

## The Metric as Vacuum Configuration

In standard mathematical language, the metric is a geometric object on the manifold.

In this framework, the metric is interpreted physically as the vacuum's local configuration.

This interpretation is important.

The metric is not merely a coordinate convention. It is not just bookkeeping. It encodes the physical structure of the vacuum/spacetime itself.

When the metric changes, the vacuum configuration changes.

When the metric is flat, the vacuum is in its unconstrained minimum-energy configuration.

When the metric is curved, the vacuum is in a constrained configuration. That configuration carries energy by P4.

This is how the smooth manifold language connects to the framework's ontology.

## Density Versus Amount in Manifold Language

The graph model distinguishes density from amount.

The smooth manifold version does the same.

Vacuum density is energy per unit proper vacuum volume. P3 says this is finite and locally constant.

Proper volume is computed from the metric. On a spatial slice with spatial metric $h_{ij}$, the proper volume element is

$$dV_{	ext{proper}}=\sqrt{\det h}\,d^3x.$$

Here $d^3x$ is coordinate volume, while $dV_{	ext{proper}}$ is physical volume.

The ratio between them,

$$\sqrt{\det h},$$

depends on the metric.

So even if vacuum energy density per proper volume is constant, the amount of vacuum associated with a coordinate region can vary because the metric varies.

This is the continuum version of the graph-model distinction:

- per-node energy is constant;
- number or arrangement of nodes per coordinate region can vary.

In smooth language:

- intrinsic density is constant;
- proper volume per coordinate volume is metric-dependent.

This is why the framework can have constant local density and still have curvature.

Curvature is not a varying scalar density. Curvature is variation in the metric structure of vacuum extent.

## Vacuum Amount, Metric Change, and Substance Change

A smooth Lorentzian manifold can represent changes in proper length, proper volume, curvature, and causal structure through the metric. That is the configuration side. But when the framework says vacuum is created or destroyed, that is a substance-side statement. The metric can describe the smooth configuration response to such an event, but the full substance bookkeeping may require additional structure in the future field equation.

Three kinds of change should be distinguished.

**Coordinate relabeling.** Nothing physical changes. The same manifold point is described with different coordinate labels. No vacuum is created, destroyed, or rearranged. This is pure gauge.

**Configuration change on a fixed manifold.** The topology stays the same, but the metric changes. Proper volume per coordinate volume changes:

$$dV_{\text{proper}}=\sqrt{\det h}\,d^3x.$$

This is the clean manifold-language version of "less or more vacuum amount per coordinate region" at the configuration level. The metric deforms smoothly, and all configuration-energy bookkeeping proceeds through metric derivatives.

**Substance-regime change.** Vacuum amount is actually created or destroyed. This is not merely a coordinate change and not merely a passive metric deformation. It is a change in the ontological content of the vacuum. But it still cannot appear as a discontinuity. The future theory must specify how substance change couples to smooth configuration change.

The current smooth-manifold language captures the configuration response: the metric changes smoothly, and that change determines proper volume, curvature, and causal structure. The framework's deeper substance-regime claim is stronger: in some processes, vacuum amount itself may be created or destroyed. The present document does not formalize that process. It only states the geometric requirement that any such process must have a smooth finite-energy metric representation in the surrounding vacuum.

In a smooth-manifold formulation, adding or removing vacuum should not be modeled first as a discontinuous topological deletion. A sharp deletion, boundary collapse, or point-joining operation would generally create singular or discontinuous geometric structure. Since the framework forbids infinite configuration energy, that is not the default mathematical representation. The right formal move is: substance changes are accompanied by smooth metric responses, and the metric remains the language for describing the resulting configuration.

This is the formal-geometry version of the lesson from the informal graph model's "Removing a Node" section. In the graph picture, node removal must be accompanied by smooth reorganization of neighboring relations. In the manifold picture, any substance-regime event must be accompanied by a smooth finite-energy metric response.

## Caution: Do Not Overstate the Mass Interior

The framework should not currently say that there is no vacuum at mass. It is not yet committed to an interior model of mass. The safe statement is that mass may consume, constrain, displace, or reorganize vacuum, and whatever happens must produce a smooth finite-energy exterior configuration.

The present theory specifies the exterior geometric structure that results from mass. It does not specify the interior structure of mass, whether vacuum is absent, reduced, transformed, or dynamically exchanged in that region. What is currently required is weaker and safer: whatever mass does to vacuum, the surrounding vacuum configuration must remain smooth and finite-energy.

## Directional Extent and Tensor Structure

A scalar field assigns one number to each point.

A metric assigns a rule for measuring displacement in every direction at each point.

That is a much richer object.

For a displacement vector $v^\mu$, the metric assigns the squared interval

$$g_{\mu
u}v^\mu v^
u.$$

This means the vacuum's local extent is directional. A coordinate displacement in one direction may correspond to a different proper interval than the same coordinate displacement in another direction.

This is the smooth-manifold version of the graph's directional adjacency structure.

The framework should therefore avoid reducing the vacuum to a scalar field. Scalar quantities may appear in special symmetric cases, such as the Newtonian potential $U$ in a static spherical weak field. But the general vacuum configuration is metric/tensorial, not scalar.

This supports the current separation between P7 and P8. They should not be collapsed into one universal scalar metric ansatz.

## Curvature

Curvature measures how the metric changes from place to place in a way that cannot be removed by coordinate relabeling.

In flat spacetime, one can choose coordinates where the metric is globally Minkowski:

$$ds^2=-c^2dt^2+dx^2+dy^2+dz^2.$$

In curved spacetime, one can always make the metric look Minkowskian at a single point, but not globally. The mismatch between nearby local inertial frames is curvature.

Mathematically, curvature is encoded in objects built from the metric and its derivatives, especially the Riemann curvature tensor.

The details can be technical, but the concept is straightforward:

```text
The metric tells us local interval structure.
Curvature tells us how that local interval structure changes across the manifold.
```

In the framework's language:

```text
The metric is local vacuum extent.
Curvature is variation in vacuum extent.
```

This is the smooth-manifold expression of P3a.

## Configuration Energy

P4 says curvature contains energy.

In smooth geometry, this suggests that configuration energy should be a functional of the metric and its derivatives.

A generic expression would look like

$$E_{	ext{config}}[g].$$

This notation means: the configuration energy depends on the whole metric configuration, not just on a value at one point.

In standard GR, the action is built from curvature. A familiar piece is the Einstein-Hilbert term, which involves the Ricci scalar $R$:

$$S_{	ext{EH}}\propto \int R\sqrt{-g}\,d^4x.$$

The framework does not need to adopt the Einstein-Hilbert action as a postulate here. But the smooth Lorentzian setting makes clear what kind of object the future field equation probably needs: a variational principle or field equation built from the metric and its derivatives.

The graph model's "spring energy" becomes, in continuum form, a configuration-energy functional of the metric.

## Minimum-Energy Configuration

P5 says the vacuum seeks a minimum-energy configuration.

In smooth geometric language, this suggests a variational principle.

A variational principle asks which metric configuration makes an action or energy functional stationary or minimal, subject to constraints.

Schematically:

$$\delta E_{	ext{config}}[g]=0.$$

This is not yet the framework's field equation. It is the shape a future field equation may take.

P7 and P8 are part of the current postulate set. They are not external assumptions. They supply the exterior recovery structure that lets the framework derive $\gamma=1$ and $\beta=1$.

At the same time, they are also design targets for the future field equation. A more complete version of the framework should derive the behavior expressed by P7 and P8 from the deeper configuration-energy and substance-dynamics law.

This is analogous to how an effective principle can later become a theorem once a deeper theory is found.

The weak-field recovery follows from the current postulate set, with P7 and P8 doing specific exterior-recovery work.

A successful field equation should reproduce:

$$A(r)B(r)=1$$

in the static source-free exterior setting, and

$$d\lnlpha=-rac{dU}{c^2}+O(c^{-6})$$

in the static exterior weak-field temporal sector.

## Intrinsic Geometry Versus Embedding Space

The graph model began with a point cloud imagined inside a background space. That picture is useful, but it creates a question: what is the background space physically?

The smooth manifold answer is: there is no physical embedding space.

A manifold does not need to live inside a higher-dimensional container. It has intrinsic geometry.

This is the same point often made in GR. When people draw a curved sheet embedded in three-dimensional space, the surrounding space is only a visualization. The actual geometry of the sheet is intrinsic and can be measured by beings living on the sheet without reference to the embedding.

The framework should treat the graph picture the same way.

The embedding space is pedagogical scaffolding. The physical content is the intrinsic geometry: metric, proper time, proper length, proper volume, curvature, and causal structure.

This avoids the false idea that the vacuum exists inside some prior space.

The vacuum/spacetime structure is what makes physical location meaningful in the first place.

## How the Graph Model Translates

The informal graph model can be translated into smooth geometry as follows:

```text
Graph node -> local quantum or patch of vacuum extent
Graph edge -> local adjacency relation
Edge length -> metric information
Edge strain -> configuration energy
Graph path length -> proper distance approximation
Graph relaxation -> minimum-energy metric configuration
Graph curvature/defect -> curvature of the metric
Node count per coordinate region -> proper vacuum amount per coordinate region
Per-node energy -> constant intrinsic vacuum density
```

None of these translations are formal commitments. They are development aids.

The important point is that the graph model helps identify the right continuum distinctions.

It teaches that density and amount are different. It teaches that geometry should be intrinsic. It teaches that configuration energy should be local and metric-dependent. It teaches that directional structure is essential.

Once those lessons are extracted, the graph itself can be set aside.

## Why Not Stay With the Graph?

The graph model is useful, but it introduces unnecessary commitments if made formal too early.

A literal graph theory of spacetime would have to answer many hard questions:

- Are nodes physically real?
- What sets the node spacing?
- Are edges fixed or dynamic?
- What determines connectivity?
- Is the graph Lorentz invariant?
- How does a continuum limit emerge?
- How are quantum fields represented?
- How is causal structure encoded?

Those questions may eventually matter. But they are not needed for the current development stage.

The current framework already has a strong continuum postulate/theorem chain. The immediate goal is field-equation design, not quantized spacetime.

So the graph should remain informal, while the formal theory is developed on a smooth Lorentzian manifold.

## Why Not Use a Purely Riemannian Manifold?

A purely Riemannian manifold is useful for spatial geometry, but not for the full theory.

The full theory needs:

- proper time,
- time dilation,
- light cones,
- null propagation,
- local SR,
- causal ordering,
- and relativistic dynamics.

These require Lorentzian signature.

A Riemannian spatial slice can still be used when the theory restricts attention to space at a fixed time. The graph model often lives at that level. But the full vacuum/spacetime configuration must be Lorentzian.

The distinction can be summarized:

```text
Spatial geometry: Riemannian.
Spacetime geometry: Lorentzian.
```

## Mathematical Setting Versus Dynamics

It is important to separate the mathematical setting from the dynamical law.

The mathematical setting says what kind of object represents spacetime/vacuum. The recommended setting is a smooth Lorentzian manifold with metric:

$$(M,g).$$

The dynamical law says what determines the metric $g$.

Standard GR answers this with the Einstein field equation. This framework has not yet fixed the full field equation. Its current postulates and theorems constrain what that future equation must reproduce, especially in the static exterior weak-field regime.

The weak-field theorem chain shows that the current postulate set recovers the standard exterior weak-field metric through one-post-Newtonian order. That is a recovery result, not an adoption of Einstein's equation as primitive.

The field-equation development problem is therefore:

```text
Find the vacuum configuration-energy and substance-exchange dynamics that determine g and reproduce the recovered weak-field behavior.
```

Using a Lorentzian manifold answers the question "what kind of geometric object is the vacuum/spacetime configuration?" It does not answer the question "what equation determines that configuration?"

## Why This Does Not Force General Relativity

Using a smooth Lorentzian manifold does not mean the framework has simply assumed general relativity.

General relativity uses a Lorentzian manifold and a specific dynamical law: the Einstein field equation.

This framework can use the same geometric language while giving the metric a different physical interpretation and while seeking a different derivational foundation for the field equation.

The mathematical setting is:

$$(M,g).$$

The open dynamical question is:

```text
What determines g?
```

GR answers this by postulating the Einstein field equation.

This framework aims to answer it through vacuum configuration energy, minimum-energy structure, vacuum substance, and exchange dynamics. The current weak-field theorems already impose design constraints on that future equation: it must reproduce the static exterior results associated with $\gamma=1$ and $\beta=1$.

So the framework is GR-compatible in its geometric language, but not identical to GR in ontology or field-equation development.

## Relation to P1 Through P8

P1 says vacuum is energy. The manifold picture does not directly supply this; it gives the geometric arena whose configuration can carry energy.

P2 says vacuum is spacetime. This is the strongest reason to use a manifold-with-metric. Spacetime is represented by $(M,g)$, so vacuum is represented by $(M,g)$.

P3 says vacuum energy density is finite and locally constant. In manifold language, this should mean constant density per unit proper vacuum volume.

P3a says spatial differential of vacuum amount is curvature. In manifold language, vacuum amount is encoded by proper lengths, areas, and volumes determined by the metric, and curvature is built from derivatives of the metric.

P4 says curvature contains energy. In manifold language, configuration energy should be a functional of $g$ and its derivatives.

P5 says vacuum seeks minimum-energy configuration. In manifold language, this points toward a variational principle for $g$.

P6 says energy in gradients exchanges with vacuum. In manifold language, this concerns how matter, radiation, and metric configuration exchange energy in curved geometry.

P7 says static source-free exterior curvature is compensated temporal-radial redistribution. In manifold language, this constrains the static exterior metric.

P8 says static source-free exterior temporal distortion self-couples. In manifold language, this constrains the second-order temporal behavior of the weak-field metric.

The manifold metric is primarily the language of configuration. It tells us how vacuum extent is arranged. It does not, by itself, complete the bookkeeping for vacuum substance creation or destruction. P1–P3 refer most directly to vacuum substance: vacuum is energy, vacuum is spacetime, and vacuum energy density is constant. P3a–P5 refer strongly to vacuum configuration: curvature is variation in vacuum extent, curvature carries energy, and vacuum seeks a minimum-energy configuration. P6 is a bridge: energy in gradients exchanges with vacuum, and that exchange can involve substance-regime bookkeeping. P7 and P8 are exterior configuration constraints. Future substance-regime work must specify how changes in vacuum substance produce or respond to smooth metric changes.

## Relation to the Weak-Field Theorem Chain

The current weak-field theorem chain already uses Lorentzian metric language.

T1 and T2 deal with redshift and time dilation, which require temporal metric structure.

T3 uses a static spherical metric form and derives reciprocal exterior scaling.

T4 uses the temporal scale factor

$$lpha=\sqrt{-g_{tt}}.$$

T5 assembles a weak-field spacetime metric.

T6 derives the Newtonian limit from the metric connection.

T7 and T8 use the null condition

$$ds^2=0.$$

T9 uses the one-post-Newtonian orbital equation.

All of this is Lorentzian geometry in practice. This document simply makes the background language explicit.

## How to State This in Future Work

A future field-equation design document can safely use language like this:

```text
We represent the vacuum/spacetime configuration by a smooth Lorentzian manifold $(M,g)$. The metric $g$ encodes local causal structure, proper time, proper distance, proper volume, and directional vacuum extent. The field-equation problem is to determine how $g$ is fixed by vacuum configuration energy, matter constraints, and exchange dynamics.
```

It should avoid saying:

```text
The manifold is a container in which vacuum lives.
```

It should also avoid saying:

```text
The graph model is the true microscopic structure.
```

The correct framing is:

```text
The smooth Lorentzian manifold is the current formal language. The graph model is an informal scaffold for understanding what the metric means physically.
```

## Technical Glossary

**Manifold:** A space that locally looks like ordinary coordinate space, even if its global structure is curved or complicated.

**Coordinate chart:** A way of assigning numbers to points in a local region of the manifold.

**Metric:** The object that converts coordinate displacements into proper intervals. It determines proper time, proper length, proper volume, causal structure, and curvature.

**Riemannian metric:** A positive-definite metric appropriate for spatial geometry.

**Lorentzian metric:** A metric with one time direction and three space directions, appropriate for spacetime.

**Pseudo-Riemannian metric:** A metric that is not positive-definite. Lorentzian metrics are the physically relevant pseudo-Riemannian metrics for relativity.

**Proper time:** Time measured by a clock along its own path.

**Proper length:** Physical length measured by local rulers.

**Null path:** A path with $ds^2=0$, followed by light in spacetime.

**Curvature:** Coordinate-independent variation in the metric, describing how local inertial frames fail to fit together globally.

**Intrinsic geometry:** Geometry defined within the manifold itself, without reference to an embedding space.

**Embedding:** A way of representing a manifold inside a higher-dimensional space. Useful for visualization, but not necessarily physical.

**Configuration energy:** In this framework, energy associated with the metric/vacuum configuration and its curvature.

**General relativity:** A theory that uses a smooth Lorentzian manifold with metric and determines that metric using the Einstein field equation. The present framework uses the same type of geometric setting but interprets the metric as vacuum configuration and seeks a field equation grounded in vacuum ontology.

## Summary

A smooth Lorentzian manifold with metric is the appropriate formal home for the framework's vacuum configuration.

The manifold provides the differentiable structure. The Lorentzian metric provides proper time, proper distance, null paths, causal structure, volume, and curvature. In the framework's interpretation, that metric is the vacuum's local geometric configuration.

The scope of this recommendation should be understood precisely. The smooth Lorentzian manifold is the right formal language for vacuum/spacetime configuration. Substance-regime processes — vacuum creation and destruction — are deeper ontology that the future field equation must address. Any substance change must appear geometrically as a smooth finite-energy configuration response. Topological excision or boundary collapse is a useful thought experiment, not the default formal move.

Riemannian geometry remains useful for spatial slices and graph-model intuition, but the full spacetime theory must be Lorentzian.

The graph model helps motivate the interpretation, but it should remain informal. The formal theory should be smooth-manifold-first.

This document does not add a postulate. It records the current best mathematical direction for development:

```text
Represent vacuum/spacetime as a smooth Lorentzian manifold $(M,g)$, interpret $g$ as vacuum configuration, and seek a field equation or configuration-energy principle that determines $g$. Recognize that substance-regime bookkeeping may require additional formal structure beyond the metric alone.
```

The framework should use the same smooth Lorentzian geometric arena as standard GR, but it should not treat that arena as the whole theory. The distinctive theory begins when the metric is interpreted as vacuum configuration and the field equation is sought from vacuum substance, configuration energy, and exchange dynamics.
