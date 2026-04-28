# SR Imports

## What This Document Is

This document lists the content the framework imports from special relativity. These are not postulates of the framework; they are commitments inherited from special relativity that the framework adopts wholesale. Derivations within the framework invoke them by their labels (SR1, SR2, etc.).

Each import is stated, briefly characterized, and noted for its role in the framework. The labels are stable references so that downstream derivations can cite specific imports without ambiguity.

The framework adopts special relativity as a starting point and does not attempt to rederive it. Where the framework's content extends or reinterprets SR-level content, the extension is made through framework postulates in the framework's own postulate documents. The imports in this document are SR's content as such, not framework reinterpretations of it.

---

## SR1: Lorentz Invariance

The laws of physics take the same form in all inertial reference frames. There is no preferred inertial frame; physical phenomena are invariant under Lorentz transformations between inertial observers.

This is the foundational symmetry of special relativity. Every other SR import is consistent with it and most can be derived from it together with a few additional commitments.

The framework inherits Lorentz invariance as a constraint on its postulates and consequences. Framework content that violates Lorentz invariance would be inconsistent with this import and is not allowed.

---

## SR2: Invariance of the Speed of Light

The speed of light in vacuum, $c$, is the same in all inertial reference frames, independent of the motion of the source or the observer.

This is the empirical content that distinguishes special relativity from Galilean relativity. Combined with SR1, it forces the Lorentz transformation as the relationship between inertial frames.

The framework treats $c$ as a fundamental constant of the vacuum substrate, not just as the speed of a particular type of wave. The framework's commitment that information propagates through the vacuum at finite speed inherits its specific value from this import.

---

## SR3: Spacetime Interval and Minkowski Structure

The spacetime interval $ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$ is invariant under Lorentz transformations. This invariant structure on spacetime is the Minkowski metric, and it is the geometric structure of spacetime in the absence of gravity.

The framework's commitment is that this is the local structure of vacuum at every point, in the absence of curvature. Framework postulates introduce additional structure (constant density, configuration energy, dynamics) that is layered on top of this Minkowski local structure. Where the framework discusses curved spacetime, the curvature is a deviation from this local Minkowski structure that obtains in the absence of mass.

---

## SR4: Mass-Energy Equivalence

A body's total energy and its inertial mass are related by $E = mc^2$. Mass and energy are different expressions of the same quantity. All forms of energy contribute to inertia, and all inertial mass corresponds to energy.

This is the most heavily used import in the framework's derivations. Several specific content commitments follow from it that the framework invokes:

A photon of energy $E$ has inertial mass $E/c^2$ for purposes of momentum and force calculations, even though its rest mass is zero.

Kinetic energy contributes to a body's inertial mass; a moving body has slightly more inertial mass than the same body at rest, with the difference being the kinetic energy divided by $c^2$.

All forms of energy participate equivalently in the framework's vacuum exchange and configuration interactions. The framework does not need to specify a separate "mass" coupling to gravity beyond the energy coupling, because mass is a form of energy.

The framework's force-on-energy structure (Postulate 3) is licensed by this import: forces in curvature gradients act on every quantum of energy with strength proportional to that quantum, regardless of whether the energy is in the form of rest mass, kinetic energy, photon energy, or any other form.

---

## SR5: Energy-Momentum Relation

For a body of rest mass $m$ and momentum $p$, the total energy is given by $E^2 = (pc)^2 + (mc^2)^2$. For massive bodies at rest, this reduces to $E = mc^2$. For massless particles like photons, this reduces to $E = pc$.

The framework uses this import wherever energy and momentum need to be related, particularly in the redshift derivation (where the photon's energy-momentum relation $p = E/c$ is invoked) and in the equations of motion derivations (where the relativistic energy-momentum relation supersedes the Newtonian $E = p^2/2m$ at high velocities).

---

## SR6: Time Dilation in Inertial Frames

Clocks moving relative to an inertial observer run slow as measured by that observer, by the Lorentz factor $\gamma = 1/\sqrt{1 - v^2/c^2}$. Two clocks that are synchronized in one inertial frame are not synchronized in another.

This is the kinematic time dilation of special relativity. The framework distinguishes this from gravitational time dilation, which is a separate effect derived within the framework from the curvature-induced variation in vacuum-per-coordinate-span. The framework's gravitational time dilation reduces to SR6 in the absence of curvature; both effects can be present simultaneously, with SR6 governing the kinematic part.

---

## SR7: Length Contraction in Inertial Frames

A body moving relative to an inertial observer is contracted along the direction of motion as measured by that observer, by the Lorentz factor $\gamma = 1/\sqrt{1 - v^2/c^2}$.

The framework uses this for completeness in the kinematic structure but invokes it less frequently than the time dilation companion.

---

## SR8: Relativistic Doppler Effect

A source emitting electromagnetic radiation at frequency $\nu_0$ in its rest frame is observed at a different frequency by an observer in relative motion. For motion along the line of sight at velocity $v$, the observed frequency is $\nu = \nu_0 \sqrt{(1-\beta)/(1+\beta)}$ where $\beta = v/c$. To first order in $v/c$, this gives $\nu \approx \nu_0(1 - v/c)$ for a receding source.

The framework's redshift derivation invokes this in its first-order form when relating the gravitational redshift to the equivalent-elevator argument. The exact form is invoked when extending derivations beyond first order.

---

## SR9: Local Validity of SR in Inertial Frames

In any inertial frame, special relativity holds exactly. The framework adopts this as the local content of physics in the absence of gravity, and its commitments about curved spacetime extend SR locally rather than replacing it.

Specifically: at any point in the framework's curved vacuum, there is a local inertial frame in which the vacuum's local geometry is approximately Minkowski (SR3) and in which all SR content holds to leading order. Framework physics is the smooth extension of SR's local content to situations where the global geometry is curved.

This import is structurally important: it commits the framework to recovering SR exactly in the limit of no curvature, and to recovering SR locally even in the presence of curvature. Framework content that would violate this limit is inconsistent with this import.

---

## How These Imports Are Used

Framework derivations cite imports by label. A derivation that uses mass-energy equivalence and the photon energy-momentum relation cites SR4 and SR5. A derivation that uses local Minkowski structure plus the invariance of $c$ cites SR2, SR3, and SR9.

When a framework postulate or consequence depends on SR content, the dependency is explicit. The framework's claim is that the postulate plus the cited SR imports together produce the derived result.

When a framework derivation appears to use SR content that is not in this list, the derivation is incomplete: either the missing content should be added to this list as an additional import, or the derivation should be revised to depend only on what is here.

This document is the canonical list of what the framework takes from SR. Updates to this list should be deliberate and noted; the imports are stable commitments that downstream derivations rely on.

---

## What This Document Does Not Include

This document includes SR content that the framework adopts wholesale. It does not include:

Framework postulates. Those are stated separately in their own documents and are framework commitments rather than imports.

Content from general relativity. The framework does not import GR; it attempts to give a substantivalist reformulation that recovers GR's content in appropriate limits. GR results are reference points for comparison, not commitments the framework adopts.

Quantum mechanical content. The framework is currently classical and does not invoke quantum mechanical commitments. Quantum extensions are open work, and any quantum imports would be added in a separate document if the framework develops a quantum formulation.

Mathematical machinery (linear algebra, calculus, differential geometry). These are tools the framework uses freely without listing as imports.

---

## Notes on Specific Imports

A few of the imports listed above deserve additional commentary on their role in the framework.

SR4 (mass-energy equivalence) is the most heavily invoked import. The framework's force-on-energy structure, its treatment of photons as participating in vacuum interactions, its commitment that all forms of energy contribute equivalently to gravitational phenomena — all of these depend on SR4. If SR4 turned out to be wrong or to require modification, the framework would need substantial revision.

SR9 (local validity of SR) is the structural import that ensures the framework recovers SR in the appropriate limit. Without it, the framework's commitment to extending SR rather than replacing it would not be enforceable. Framework consistency checks should verify that derivations preserve SR in the no-curvature limit.

SR2 (invariance of $c$) plays a role in fixing the value of various framework constants. The framework's gravitational wave speed, its information propagation speed, and the constant relating energy and mass are all specifically $c$, with this value being inherited from SR rather than being a free parameter the framework chooses.

The kinematic effects (SR6, SR7, SR8) are listed for completeness but are used less heavily than the structural and energetic content. The framework's derivations rarely depend on the specific kinematic forms in detail; they more often depend on the underlying Lorentz structure (SR1) and the energy-momentum relation (SR5).

---

This list may be expanded as the framework's derivations require additional SR content. Any expansion should be noted and the new import labeled with the next available SRn.
