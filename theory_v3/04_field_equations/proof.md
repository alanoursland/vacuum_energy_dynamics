# Proof: The Field Equations of Vacuum Energy Dynamics

**Purpose.** A direct, linear derivation of the field equations from the
postulates, written for a practitioner who wants to verify two things:
(1) each step is sound, and (2) **general relativity is not imported to
derive general relativity.** The path was found by exploration
(`development/field_equation_trials/`); this document is the direct
route. Every nontrivial step carries a verification pointer to a
machine-checked derivation (sympy, re-run from scratch on every
execution).

**Self-containment.** This document states and proves, in place, every
result the derivation depends on — including the closure-uniqueness
theorem (§4.4), the radiative-sector rigor closures (§4.5), the
covariant lift of the static sector (§2.4), and the nonlinear stability
theorems (§3). The verification pointers reference machine checks of
what is written here, not content that lives elsewhere. The two
declared external *mathematical* imports (§0.1) are stated with their
import class and proofs cited; everything else is on this page.

---

## 0. Inputs, conventions, and the anti-circularity ledger

### 0.1 Inputs

The derivation uses, and only uses:

- **Special relativity.** Minkowski space as the zero-source vacuum
  state; local Lorentz invariance; SR energy bookkeeping
  ($E=mc^2$, four-momentum). (`01_postulates/sr_imports.md`)
- **One empirical constant.** Newton's $G$, entering exactly once, as
  the normalization of the weak-field source law (§2.1). No other
  measurement is used as input. (Observations appear again only in §7,
  *after* the equations are fixed, as falsification tests.)
- **The postulates.** P1–P6 (vacuum = energy = spacetime; constant
  density; curvature = spatial differential of vacuum amount; curvature
  configurations carry energy; minimum-energy; exchange in gradients),
  P7′ (static frame indifference), P9 (configuration energy gravitates
  at the universal coupling, counted exactly once). Full statements in
  `01_postulates/`.
- **Two external mathematical theorems**, each a theorem of
  *special-relativistic field theory or PDE analysis on Minkowski
  space*, whose statements and proofs nowhere assume that Einstein's
  equations hold in nature:
  1. **Fierz–Pauli (1939):** linear uniqueness of the massless spin-2
     operator (used in §4.1).
  2. **Christodoulou–Klainerman (1993) / Lindblad–Rodnianski (2010):**
     global small-data nonlinear stability of the flat state for the
     equations derived below (used only in §3's global anchor; no
     coefficient depends on it).

  Using them is using mathematics, not importing GR's physical content.
  The self-coupled closure theorem formerly cited from Deser (1970) is
  **proved in-house in §4.4** and is no longer an import.

### 0.2 What is **not** an input

- The Einstein field equations, the Einstein–Hilbert action, and the
  Einstein tensor *as a physical response law*. (The Einstein tensor as
  a *differential-geometric object* — a particular combination of
  second derivatives of a metric — is used in §5 as pure geometry,
  after the response law has been derived in §4. No step before §4
  uses it.)
- Any GR phenomenology: no solar-system tests, no binary pulsar, no
  gravitational-wave data enter the derivation. They appear in §7 as
  *post-derivation kill conditions*: observations that could have
  falsified the derived equations and did not.
- The Schwarzschild solution. It is *derived twice*, by independent
  routes (§2 bookkeeping; §4 closure), and the agreement is an internal
  consistency check, not an input.

### 0.3 Conventions

Coordinates $(t,r,\theta,\phi)$ or $(t,x,y,z)$; metric signature
$(-,+,+,+)$ with $g_{tt} \to -c^2$ at infinity. Static spherical
configurations are written

$$ds^2 = -c^2 A(r)\,dt^2 + B(r)\,dr^2 + r^2 d\Omega^2 .$$

Reduced variables: $s \equiv \tfrac12\ln(A/B)$ (shear),
$\kappa \equiv \tfrac12\ln(AB)$ (trace). The areal Laplacian is
$\Delta_{\text{areal}} f \equiv (r^2 f')'/r^2$.

---

## 1. The kinematic layer: why there is a metric and why coupling is universal

**P2 (vacuum–spacetime identity)** states that the vacuum substance's
configuration *is* spacetime: the temporal and spatial mappings of the
vacuum are what clocks and rods read. Three consequences, used
throughout:

**(K1) The configuration is restricted to the metric branch.** A local
configuration of the substance assigns rates and lengths to all
directions at a point. By itself, that statement would allow a general
direction-dependent norm (a Finsler-type structure), not necessarily a
symmetric bilinear metric. The proof therefore uses the SR import in
§0.1 in its algebraic form: the zero-source tangent structure has a
quadratic Lorentz interval, and admissible weak configurations are
perturbations of that quadratic interval. By the polarization identity,
the local interval is represented by a symmetric, nondegenerate rank-2
tensor $g_{ab}$, and perturbations are symmetric tensor fields $h_{ab}$
on Minkowski space.

This is a branch restriction, not a derivation from P2 alone. P2 says
the vacuum configuration is what clocks and rods read; SR supplies the
quadratic local line-element structure used by the Fierz-Pauli
classification below. Finsler-like generalizations are not killed here;
they are outside this proof's metric/SR branch.

**(K2) Coupling is universal with no free constant.** Matter does not
couple *to* the vacuum configuration through an adjustable charge;
matter's clocks and rods *are* the vacuum's mappings (P2). All matter
therefore responds to $g_{ab}$ identically — the equivalence-principle
content arrives as ontology, not as an assumed principle — and the
matter-side coupling of $h_{ab}$ is fixed kinematically. (Operationally:
$h$ is metric strain; geodesic response and the interaction term
$\tfrac12 h_{ab}T^{ab}$ follow from expanding matter's SR action in the
mappings. No constant is introduced.)

**(K3) Gauge freedom is relabeling.** Identifying which vacuum element
is "where" is a labeling choice; physics cannot depend on it.
Infinitesimally, relabelings act as
$h_{ab} \to h_{ab} + \partial_a\xi_b + \partial_b\xi_a$. Any dynamical
law for $h_{ab}$ must be invariant under this — this is
diffeomorphism gauge symmetry derived from the substance picture, not
assumed from GR.

---

## 2. The static bookkeeping sector (no field equations needed)

This section derives the exact static spherical exterior using only
substance bookkeeping. Nothing here uses a tensor response law.
Section 2.4 then lifts the sector covariantly: the reduced statements
proved in gauge-fixed variables are shown to be chart-free geometric
statements, with staticity itself derived rather than assumed.

### 2.1 Lemma 1 (the areal-flux source law)

*Statement.* In the static weak-field regime, the temporal mapping
satisfies a flux law: for some monotonic distortion variable
$\mathcal A$ built from $A$ (fixed in §2.3),

$$F(r) \equiv 4\pi r^2\,\mathcal A'(r) = \frac{8\pi G}{c^2}\,
M_{\text{enc}}(r), \qquad\text{equivalently}\qquad
\Delta_{\text{areal}}\,\mathcal A = \frac{8\pi G}{c^2}\rho .$$

*Derivation.* **P3a** makes the spatial differential of the vacuum
amount the carrier of curvature: a localized source does not act at a
distance; it conditions the vacuum configuration in its neighborhood,
and the conditioning propagates outward as a *gradient*. **P6** supplies
the accounting: the energy exchanged with matter moving in the gradient
is drawn from the vacuum, so the gradient's strength must track the
enclosed energy content — additively in the source (two sources
condition twice the vacuum), isotropically (P1–P3 give the substance no
preferred direction), and locally (the differential at radius $r$ can
depend only on what is enclosed). Additivity + isotropy + locality for
a radial differential is precisely a Gauss-type flux law: the surface
integral of the differential counts the enclosed source. The constant
is then **fixed by the Newton anchor**: matching the first-order
temporal mapping to Newtonian dynamics ($A \approx 1 + 2\Phi/c^2$,
$\Delta\Phi = 4\pi G\rho$; T1/T2/T6 chain) gives $8\pi G/c^2$. This is
the derivation's *only* empirical normalization.

*What is and is not claimed.* The flux law's **form** is postulate
bookkeeping; its **constant** is the Newton anchor; the **choice of
distortion variable** $\mathcal A$ (i.e., which function of $A$ obeys
the linear law — $A$ itself? $\ln A$? something else?) is *not* yet
fixed. First order cannot distinguish the candidates; §2.3 fixes the
variable exactly, from P9.

> Verification: `02_foundations/` T1–T2;
> `vacuum_forge/.../002_trial_C_burden_ledger/trial_C2_self_coupling_bootstrap.py`.

### 2.2 Lemma 2 (the P7′ shadow: $AB = 1$)

*Statement.* In a static, source-free exterior, $A(r)B(r) = 1$.

*Derivation.* **P7′** (adopted postulate): a strictly static vacuum
configuration carries no energy current and no preferred frame in the
t–r plane. **P3** (constant density) gives its metric shadow: in the
configuration regime (no exchange, P6 quiescent), curvature is
*redistribution* of vacuum extent, not creation — temporal stretching
and radial compression must compensate, $A B = \text{const}$, and
asymptotic flatness sets the constant to 1.

The shadow equivalence is differential geometry, proved from scratch:
for the general static spherical metric of §0.3, the mixed Einstein
combination satisfies the **t–r block identity**

$$G^t{}_t - G^r{}_r = -\frac{(\ln AB)'}{rB},$$

so (conditional on a second-order divergence-free response, the gates
G15/G16/G20; unconditionally after §4 closes the response) the three
statements are equivalent: $AB=\text{const}$ ⟺ $T^t{}_t=T^r{}_r$
(radial-boost invariance of the effective stress: no energy current,
no preferred t–r frame) ⟺ configuration energy is counted inside the
nonlinear response rather than as an explicit scalar-type source. The
explicit-source placement is *excluded*: a static radial scalar-type
stress has $T^t{}_t - T^r{}_r = -(\phi')^2/B \neq 0$ wherever the
field has a gradient, which by the identity breaks $AB=1$. P9's
count-once placement question is thereby resolved geometry-side.

This is postulate content doing work, stated as such — P7′ is one of
the nine commitments, adopted with its fence and its own observable
face (§7). It is *not* extracted from the Schwarzschild solution; the
adoption record and the equivalence theorem predate every use below.

> Verification: `01_postulates/p7_prime_static_frame_indifference.md`;
> `vacuum_forge/.../trial_C3_spatial_bootstrap.py` (the t–r block
> identity is pure geometry: it holds for *any* static spherical
> metric, independent of any field equation).

### 2.3 Theorem 1 (the exact exterior, and the sign of field energy)

*Statement.* The static spherical exterior is exactly

$$A = 1 - \frac{2GM}{c^2 r}, \qquad B = A^{-1},$$

and the static configuration carries the **negative** energy density

$$u_{\text{field}} = -\frac{c^4\,(s')^2}{8\pi G}.$$

*Derivation.* Two requirements meet:

(i) **P9** (configuration energy gravitates at the universal coupling,
counted exactly once — and, by its fence, counted *inside the adopted
law*, not as a bolt-on source). The static gradient carries
configuration energy (P4); a candidate law that ignores it violates P9.

(ii) **The exponential identity.** For any $s$,

$$\Delta_{\text{areal}}\big(e^{s}\big) =
e^{s}\Big[\Delta_{\text{areal}} s + (s')^2\Big].$$

Consequence: the flux law is linear in the variable $\mathcal A = e^s
= A$ *if and only if* the shear obeys
$\Delta_{\text{areal}} s = -(s')^2$ in vacuum — i.e., if and only if
the field self-sources with energy density exactly
$u = -c^4 (s')^2/8\pi G$ at the universal coupling $8\pi G/c^4$,
counted once, geometry-side. Among the one-parameter family of
candidate distortion variables ($A_\lambda = (1+\lambda r_s/r)^{-1/\lambda}$,
parametrizing which function of $A$ obeys the linear law), **P9 selects
$\lambda = -1$**: it is the unique member whose nonlinear content
equals its own bookkeeping energy at the universal coupling. The
alternatives fail P9 in one of two ways: $\lambda = 0$ (law linear in
$\ln A$) counts no self-energy at all; $\lambda = +1$ and others count
it with the wrong weight. Solving the now-fixed law in vacuum:
$\Delta_{\text{areal}}A = 0 \Rightarrow A = 1 - 2GM/c^2r$ with the
constant fixed by the Newton anchor; Lemma 2 supplies $B = 1/A$.

The **sign** of $u_{\text{field}}$ is forced, not chosen: the identity
produces $-(s')^2$, and P9's count-once placement (the fence) forbids
re-deriving it as a positive bolt-on source. (Independently: the
placement exclusion in §2.2 proves the explicit positive-source
placement breaks Lemma 2, so the geometry-side negative counting is
the *only* P7′-compatible option.)

*Two remarks for the practitioner.*
1. The multiplicative-composition statement formerly carried as
   postulate P8 ("each shell acts on the already-distorted rate") is
   the exponential structure $A = e^s$ — here it is a *consequence*,
   which is why P8 is demoted
   (`01_postulates/demoted_p8_static_exterior_temporal_self_coupling.md`).
2. Nothing in this section used a tensor response law. The exterior is
   pure bookkeeping: flux law (P3a/P6/Newton) + variable selection (P9)
   + compensation (P7′/P3).

> Verification: `trial_C2_self_coupling_bootstrap.py` (identity, family,
> selector, exact solution); `trial_C3_spatial_bootstrap.py`
> (placement exclusion).

### 2.4 Theorem 1c (covariant lift of the static sector)

The reduced statements of §§2.1–2.3 were proved in areal gauge with
staticity assumed. Four theorems remove both restrictions. (These use
the Einstein tensor as pure geometry, in the same conditional role as
§2.2's identity; after §4 they are unconditional statements about the
closed parent.)

**(a) The flux law is the covariant tt-equation.** For *any* static
spherical metric,

$$G^t{}_t = -\frac{1}{r^2}\frac{d}{dr}\Big[r\Big(1-\tfrac1B\Big)\Big]
\qquad\text{identically}.$$

Define the **Misner–Sharp mass** — a quasilocal geometric invariant,
since $r$ is fixed by the orbit area $4\pi r^2$ and
$(\nabla r)^2 = g^{rr}$ is a scalar:

$$m(r) \equiv \frac{c^2 r}{2G}\Big(1-(\nabla r)^2\Big).$$

Then $m'(r) = -(c^2 r^2/2G)\,G^t{}_t$ identically, and the response law
$N G^t{}_t = T^t{}_t = -\rho c^2$ with $N = c^4/8\pi G$ reads

$$m'(r) = \frac{4\pi r^2}{c^2}\,\rho :$$

Lemma 1's areal flux law, with $M_{\text{enc}}$ now a chart-free
invariant rather than a gauge artifact.

**(b) The P7′ shadow is chart-invariant.** In an arbitrary radial chart
$ds^2 = -c^2 a(\rho)dt^2 + b(\rho)d\rho^2 + R(\rho)^2 d\Omega^2$,

$$G^t{}_t - G^\rho{}_\rho
= -\frac{R'}{R\,b}\,\frac{d}{d\rho}\ln\frac{a\,b}{R'^2},$$

so the shadow variable is the invariant combination $ab/R'^2$ — the
areal-gauge product $AB$ after the relabeling $r = R(\rho)$. Since
$(\nabla r)^2 = R'^2/b$ and the static Killing norm is
$-\xi^2/c^2 = a$, the shadow $AB=1$ is the chart-free statement

$$(\nabla r)^2 = -\xi^2/c^2 .$$

P7′ constrains geometry, not coordinates.

**(c) The bootstrap equation is the covariant vacuum tt-equation.** On
the compensated branch $B = 1/A$,

$$G^t{}_t = \frac{rA' + A - 1}{r^2},
\qquad
\frac{d}{dr}\big[r^2 G^t{}_t\big] = r\,\Delta_{\text{areal}}A ,$$

and the solution families coincide under asymptotic flatness:
$\{\Delta_{\text{areal}}A = 0,\ A\to1\}$ and
$\{G^t{}_t=0,\ B=1/A\}$ are both exactly $\{A = 1 + C/r\}$. The
angular equation is then implied (Bianchi): all $G^a{}_b$ vanish on
the selected solution. The bookkeeping route and the covariant route
are one route in two variable sets.

**(d) Staticity is derived (Birkhoff-type).** For time-dependent
spherical $A(t,r)$, $B(t,r)$ in the areal chart,

$$G_{tr} = \frac{\dot B}{rB},$$

so vacuum forces $B = B(r)$. $G^t{}_t$ then depends only on $B$ and
gives $B = (1+C_1/r)^{-1}$; the t–r identity forces $A = h(t)/B$; and
$h(t)$ is pure relabeling — the Kretschmann invariant equals
$12\,r_s^2/r^6$ for arbitrary $h(t)>0$, so $d\tau = \sqrt h\,dt$ (a K3
gauge move) lands on the static solution. The staticity assumption of
§§2.1–2.3 is a theorem of the spherical vacuum sector.

> Verification:
> `vacuum_forge/.../019_static_covariant_lift/static_covariant_lift.py`
> (all four statements, from scratch, including the distorted-chart
> Schwarzschild witness $r = \rho + r_s e^{-\rho/r_s}$).

---

## 3. Stability and the sector signature

Three theorems establish that the negative energy of §2.3 cannot
destabilize anything — *before* the dynamics is even fixed, these are
constraints any dynamics must satisfy; after §4 they hold in it. Two
further theorems then extend the protection to full nonlinearity in
the spherical sector, and the global small-data statement is anchored.

**Theorem 2 (ghost exclusion).** Promoting the static shear $s$ to a
propagating (hyperbolic) degree of freedom yields a Hamiltonian density
that is negative definite and unbounded below
($H[\lambda s] = \lambda^2 H[s] \to -\infty$). Stability (P5's
minimum-energy commitment) therefore forces the $s$-sector to be
**elliptic/constraint-type**: the negative-energy mode does not
propagate. This is *why* the scalar sector must be a constraint —
derived, not imposed.

**Theorem 3 (source binding).** The source-free constraint sector
$(r^2 A')' = 0$ with asymptotic flatness and regularity has the unique
solution $A \equiv 1$: flat vacuum is the unique zero-source static
state. The negative reservoir is a *functional of its sources* — it
cannot decay, and it cannot be mined except by moving sources, whose
energy accounting runs through the positive channel.

**Theorem 3n (nonlinear source binding).** Theorem 3 holds at full
nonlinearity. By §2.4(d) the *complete* spherical vacuum sector is the
one-parameter family $B = r/(C_1+r)$, $A = 1/B$, whose Kretschmann
scalar is

$$K = \frac{12\,C_1^2}{r^6},$$

divergent at the center for every $C_1 \neq 0$. A regular center
therefore forces $C_1 = 0$: **flat is the unique source-free regular
spherical state at arbitrary field strength.** The negative reservoir
supports no free-standing configuration to decay into.

**Theorem 3m (no mining — Misner–Sharp positivity).** For any
spherical configuration with $B = (1 - 2Gm(r)/c^2 r)^{-1}$ and
arbitrary $A(r)$, the identity of §2.4(a) gives, with the closed
parent,

$$m'(r) = \frac{4\pi r^2}{c^2}\,\rho
\qquad\text{exactly — no weak-field expansion}.$$

For $\rho \ge 0$ and a regular center ($m(0)=0$),
$m(r) = (4\pi/c^2)\int_0^r \rho\,r'^2 dr' \ge 0$ for all $r$. The
negative configuration energy $u_{\text{field}}$ is already bookkept
inside $m$ (the exterior mass is the matter integral minus binding);
no arrangement of sources, however strong, drives a quasilocal mass
negative. **There is no nonlinear channel that extracts unbounded
energy from the static sector.**

**Theorem 4 (radiative positivity).** The propagating (transverse-
traceless) sector's energy density is a sum of squares — positive
definite — with outward null flux for outgoing waves. (Coefficient
derived in §4.3.)

**Global anchor (external mathematical import, recorded as such).**
What Theorems 2–4, 3n, 3m do not cover is the global, nonspherical,
small-data statement: Minkowski-asymptotic data close to flat evolve
globally and disperse. For the equations derived below this is the
Christodoulou–Klainerman theorem (1993; harmonic-gauge proof by
Lindblad–Rodnianski 2010) — PDE analysis about a specific hyperbolic
system, taking no gravitational phenomenology as input: the §0.1
import class, identical in kind to Fierz–Pauli. No coefficient,
equation, or falsifier of the framework depends on it; it upgrades
confidence in the flat state's global basin, nothing else. An in-house
re-derivation at that scale is declared out of scope by decision,
visibly, not carried as a hidden debt.

> Verification: `006_gate_G03_radiative_positivity/` (Theorems 2–4);
> `020_nonlinear_stability/nonlinear_stability_scoped.py`
> (Theorems 3n, 3m; TT positivity re-check; import record).

---

## 4. The dynamical closure: from linear kinematics to the full equations

The static sector (§2) constrains but does not constitute dynamics.
This section derives the full response law. The linear step uses the
Fierz–Pauli import (§0.1); the nonlinear closure theorem is proved
in-house in §4.4.

### 4.1 Lemma 3 (linear uniqueness — Fierz–Pauli)

By K1–K3, perturbations are symmetric tensors $h_{ab}$ on Minkowski
space with relabeling gauge symmetry, coupled universally to matter.
The unique local, second-order, gauge-invariant linear field operator
for such a field is the linearized "Einstein" operator (massless
spin-2; Fierz–Pauli 1939). *Status:* classical uniqueness theorem of SR
field theory. Nothing about gravity's actual dynamics is assumed; gauge
invariance came from K3, not from GR.

### 4.2 Lemma 4 (the linear theory cannot fix its own normalization)

In the linear theory with kinematically fixed matter coupling (K2),
every radiated observable scales as $1/K_T$ (the kinetic normalization)
and the work–flux balance holds identically *for every* $K_T$: the
linear sector's only physical combination is
$(\text{coupling})^2/K_T$. The normalization is physical but
*undeterminable at linear order*. Something beyond the linear theory
must fix it — exactly P9's territory.

> Verification: `008_radiative_bootstrap/radiative_bootstrap_KT.py` (T1).

### 4.3 Theorem 5 (the self-coupled closure and its normalizations)

**P9** requires the field's own energy-momentum to source it, at the
universal coupling, counted once. Iterating this requirement on the
Fierz–Pauli theory — couple $h$ to its own stress tensor, recompute the
stress, repeat — has a unique consistent completion (Theorem 5u,
proved in §4.4): the geometric response

$$N\,\mathcal G_{ab}[g] = T_{ab},$$

where $\mathcal G_{ab}$ is the (now *derived*) Einstein combination and
a cosmological term $\Lambda g_{ab}$ remains permitted.

The normalizations then follow with no further freedom:

- **$N = c^4/8\pi G$:** the closure's static weak field must reproduce
  Lemma 1's derived law ($G_{tt}^{(1)} = 2\Delta\Phi$, computed from
  scratch, against $\Delta\Phi = 4\pi G\rho$).
- **$K_T = c^4/16\pi G$ (per polarization):** expanding the *same*
  response to second order in a TT wave, the wave's own energy sources
  the background at coupling $N$ (P9 realized in the radiative sector);
  reading the energy density off the second-order piece fixes $K_T$ —
  the quantity Lemma 4 proved the linear theory could not fix.
  Corollaries with no free constants: wave amplitude $2G/c^4$, angular
  projector average $2/5$, quadrupole power
  $P = (G/5c^5)\langle\dddot Q_{ij}\dddot Q_{ij}\rangle$.

**The consistency loop (the proof's central cross-check).** The
closure's exact static spherical vacuum solution is Schwarzschild with
$B = 1/A$ — *the same exterior* derived in §2.3 from pure bookkeeping,
with the same constant. Two independent routes — substance accounting
(P3a/P6/P7′/P9 + Newton) and field-theoretic closure (K1–K3 + P9 +
Newton) — meet at one metric. A failure of this match would have
falsified the framework internally; the match is exact.

> Verification: `008_radiative_bootstrap/` (T2: $N$; T3: $K_T$, both
> polarizations, null transport; T4: Green identity, virial witness,
> projector $2/5$, assembly); `trial_C3` case 3 (closure's vacuum
> equations re-select $\lambda=-1$ independently).

### 4.4 Theorem 5u (closure uniqueness — the in-house proof)

*Statement.* Given a local, two-derivative, massless spin-2 field on
Minkowski space with relabeling gauge symmetry, universal coupling to
stress, no extra propagating fields, and self-energy sourcing at the
same universal coupling, the unique consistent nonlinear closure is
the Einstein–Hilbert (equivalently torsion-free Palatini) response, up
to boundary terms, field redefinitions, normalization (fixed in §4.3),
a cosmological term, and inert four-dimensional Gauss–Bonnet.

This is structural and coefficient-free: the coefficients were already
fixed by the static bookkeeping anchor and P9. The proof runs in seven
steps, each machine-verified.

**Step 1 (conservation forces self-coupling).** The linear operator of
§4.1 is identically conserved, $\partial^\mu G^{(1)}_{\mu\nu} = 0$, so
its source must be conserved. The gauge variation of the matter
coupling $\tfrac12\int h_{\mu\nu}T^{\mu\nu}$ reduces, after
integration by parts, to a term proportional to
$\partial_\mu T^{\mu\nu}$. Once matter exchanges energy-momentum with
the field, $\partial_\mu T_{\text{matter}}^{\mu\nu} \neq 0$: a
compensating field stress with the opposite divergence is *forced*.
The self-coupling chain is not optional.

**Step 2 (the finite first-order closure).** In densitized
inverse-metric variables $\mathfrak g^{\mu\nu} = \eta^{\mu\nu} +
H^{\mu\nu}$, split the first-order Ricci object into a
derivative-linear part $R^{\text{lin}}_{\mu\nu}$ and a
connection-quadratic part $Q_{\mu\nu}$. Then

$$(\eta + H)\!\cdot\!(R^{\text{lin}} + Q)
= \underbrace{\eta\!\cdot\!R^{\text{lin}}}_{\text{boundary}}
+ \underbrace{H\!\cdot\!R^{\text{lin}} + \eta\!\cdot\!Q}_{\text{free core}}
+ \underbrace{H\!\cdot\!Q}_{\text{self-coupling}},$$

and $H\!\cdot\!Q$ is *generated* by the universal replacement
$\eta \to \eta + \epsilon H$ in the connection-quadratic term:
$\tfrac{d}{d\epsilon}[(\eta+\epsilon H)\!\cdot\!Q]_{\epsilon=0}
= H\!\cdot\!Q$. The iteration terminates at first order in this
variable set — the bootstrap is finite, not an infinite tower.

**Step 3 (monomial exhaustiveness).** Under the theorem's assumptions
(locality, two derivatives, no extra fields, torsion-free first-order
form), the available building blocks are $\eta^{\mu\nu}$, $H^{\mu\nu}$,
the connection, and at most two derivatives. Up to integration by
parts, the only derivative-bearing contractions are the Ricci-type
$R^{\text{lin}}_{\mu\nu}$ (one differentiated connection) and
$Q_{\mu\nu}$ (connection-quadratic); no extra tensor, scalar,
preferred vector, torsion, or nonmetricity field exists to build an
independent contraction. Expanding the density coefficient in powers
of $H$, the complete basis is

$$\eta\!\cdot\!R^{\text{lin}},\quad H\!\cdot\!R^{\text{lin}},\quad
\eta\!\cdot\!Q,\quad H\!\cdot\!Q,\quad
H^p\!\cdot\!R^{\text{lin}},\ H^p\!\cdot\!Q\ (p\ge2),$$

plus zero-derivative density terms ($\Lambda$). This is an
exhaustiveness lemma, not an ansatz convenience: the later steps only
have to decide the fate of the listed higher-$H$ entries.

**Step 4 (connection elimination).** The torsion-free Palatini
connection equation, written with
$P_a{}^{\mu\nu} = \nabla_a\mathfrak g^{\mu\nu}$, is
$P_a{}^{\mu\nu} - \delta_a^{(\mu}P_b{}^{\nu)b} = 0$; its trace gives
$\tfrac{1-D}{2}P_b{}^{\mu b} = 0$, so in $D=4$ dimensions
$P_b{}^{\mu b}=0$ and hence $P_a{}^{\mu\nu}=0$: the connection is the
metric-density-compatible one, uniquely (a local component solve
confirms the homogeneous difference of two such connections vanishes).
No independent connection sector survives.

**Step 5 (mismatch exclusion, all orders).** In a split density
$A\!\cdot\!R^{\text{lin}} + B\!\cdot\!Q$, the derivative part of the
connection equation is controlled by $A$ and the algebraic
connection-transport part by $B$; a *single* compatible metric-density
connection (Step 4) requires $A = B$ at every order in $H$. Since the
$H$-degree grading separates each $H^p$ class, coefficient matching
$c_R^{(p)} D[H^p] + c_Q^{(p)} C[H^p] = \lambda_p(D[H^p]+C[H^p])$
forces $c_R^{(p)} = c_Q^{(p)}$, and a pure mismatch direction
$H^p\!\cdot\!R^{\text{lin}} - H^p\!\cdot\!Q$ has coefficient zero for
every $p \ge 2$. Mismatches cannot hide by mixing degrees (a
finite-tower witness verifies the independence).

**Step 6 (field-redefinition reduction, all orders).** The surviving
equal-coefficient directions are absorbed: the nonlinear metric-density
variable choice $K = H + \sum_p a_p H^p$ inserted into the Palatini
replacement generates exactly
$\sum_p a_p\,H^p\!\cdot\!(R^{\text{lin}}+Q)$, so every
equal-coefficient higher-$H$ term is variable-choice freedom, not
physics.

**Step 7 (accounting).** Every basis element of Step 3 is now
classified: boundary ($\eta\!\cdot\!R^{\text{lin}}$), free core
(normalization, fixed in §4.3), generated self-coupling
($H\!\cdot\!Q$), connection-inconsistent (mismatch directions), or
field-redefinition freedom (equal-coefficient tower). The residuals
are the admitted cosmological term and out-of-scope alternatives
(higher derivatives — handled by §5; extra fields, torsion,
nonuniversal coupling — outside the kinematics K1–K3 established).
The closure is Einstein–Hilbert/Palatini, uniquely. $\blacksquare$

*Import status.* The historical Deser (1970) citation is context, not
dependency: no number moves with it, and the theorem above is proved
within the stated scope by the eleven machine-checked rungs.

> Verification: `018_closure_uniqueness/closure_step_1.py` …
> `closure_step_11_final_accounting.py` (one rung per step above;
> steps 3 and 5–6 span several rungs).

### 4.5 Radiative-sector rigor (the closure's corollaries, hardened)

Four supporting theorems make §4.3's radiative corollaries exact
statements rather than leading-order readings. Each is proved from
scratch; none moves a coefficient.

**(a) Tensor-virial identity.** For an isolated symmetric stress
tensor on flat background with $x^0 = ct$, flat conservation, vanishing
surface terms, and enough regularity to commute derivatives,

$$\int T^{ij}\,d^3x
= \frac{1}{2c^2}\frac{d^2}{dt^2}\int T^{00}x^i x^j\,d^3x .$$

This is the identity that converts source integrals into quadrupole
moments in the power formula — proved in generality, not by compact
witness.

**(b) Isaacson-style TT averaging.** With averaging window
$\lambda \ll \ell_{\text{avg}} \ll L$, fast periodic total derivatives
and cross terms average away, slow envelope corrections are suppressed
by powers of $\lambda/L$, and the retarded TT stress remains positive
and null-transported. The second-order energy reading of §4.3 is
therefore well-defined at local inertial short-wave level.

**(c) Radiative gauge invariance.** The averaged radiative stress
built from TT-projected data is invariant under admissible
high-frequency relabeling gauge transformations at leading short-wave
order: the leading fast pure-gauge piece is longitudinal,
$n_i v_j + n_j v_i$, and the TT projector annihilates it for unit
propagation direction ($n_i n_i = 1$). Slow gauge-envelope terms fall
in the $\lambda/L$-suppressed class of (b). The radiated energy is a
gauge statement about physics, not about coordinates.

**(d) The vector sector through general linear time dependence.** In
transverse gauge ($g_{ti} = w_i$, $\partial_i w_i = 0$),

$$G_{ti}^{(1)} = -\tfrac12\Delta w_i,
\qquad
G_{ij}^{(1)} = -\frac{1}{2c^2}\big(\partial_i\dot w_j
+ \partial_j\dot w_i\big).$$

The first is an elliptic constraint; with the §4.3 normalization and
slow matter momentum $T_{ti} = -\rho c^2 v_i$ it gives
$\Delta w_i = (16\pi G/c^2)\rho v_i^T$ — the Lense–Thirring equation as
the stationary limit, not a separate assumption. For a source-free
transverse Fourier mode $w_i = W_i e^{i(kz-\Omega t)}$ the constraint
gives $\tfrac12 k^2 W_i = 0$, so $W_i = 0$ for $k \neq 0$: there is no
vector dispersion relation and no independent vector radiation. Only
TT modes propagate — the massless spin-2 architecture, verified rather
than assumed.

> Verification: `014_tensor_virial_identity/…`, `015_isaacson_averaging/…`,
> `016_radiative_gauge_invariance/…`, `017_vector_time_dependent/…`.

---

## 5. Eliminating the residual freedom

Theorem 5 fixes the two-derivative response but permits
higher-curvature terms. Two theorems close that door. (From here on
the Einstein tensor and curvature scalars are used freely — they were
derived in §4; this is the point of the proof's ordering.)

### 5.1 Theorem 6 (ghost gate: only $aR^2$ + Gauss–Bonnet survive)

Any quadratic-curvature term that modifies the TT propagator yields
$1/(k^2 + b\,k^4) = 1/k^2 - 1/(k^2 + 1/b)$: a massive spin-2 pole with
residue $-1$ in a sector that is dynamical (Theorem 4) — a ghost,
excluded by the same stability that caged the scalar sector (Theorem
2). Gauss–Bonnet is topological in 4D (inert). The $R^2$ term puts its
extra pole in the *constraint* sector as a healthy massive scalar
(the scalaron, $m^2 = 1/6a$, $a>0$; $a<0$ is a tachyon, excluded by
Theorem 3's flat-vacuum stability). Hence the residual freedom is a
single coefficient: $a \ge 0$ on $R^2$.

> Verification: `010_gate_G20_beta_health/` (linearized identities from
> scratch; $\alpha=+1/3$ exterior solved exactly with delta
> bookkeeping; TT untouched by $R^2$; partial-fraction residues).

### 5.2 Theorem 7 (P7′ forces $a = 0$)

Two lemmas, then the contradiction:

- **Anisotropy:** any static scalaron profile carries
  $D^t{}_t - D^r{}_r = -R'' \neq 0$ — a preferred t–r frame; in areal
  gauge, $AB - 1 = 2(\phi + r\psi')/c^2 \neq 0$ within
  $\ell^* = \sqrt{6a}$ of any source (exactly zero on the §2 exterior).
- **Mandatory hair:** fourth-order matching ($R$, $R'$ continuous)
  admits no hairless exterior: the condition would require
  $x\cosh x = \sinh x$ for $x>0$, impossible since
  $h(x)=x\cosh x-\sinh x$ has $h(0)=0$, $h'=x\sinh x>0$. Every static
  star leaks hair for any $a\neq 0$.

**P7′** forbids static vacuum configurations with a preferred t–r
frame. Therefore $a = 0$: the postulate that fixed the spatial sector
in §2.2 *also* closes the four-derivative sector. (This kill is
postulate-content with teeth: it converts the bench-top short-range
window into a null test — §7.)

**Corollary (screening cannot rescue $a \neq 0$).** Screening
mechanisms change a scalaron's detectability, range, or amplitude;
they do not change its P7′ status. For a general screened contribution
$\phi = \phi_{\text{GR}} - q(r)$, $\psi = \phi_{\text{GR}} + q(r)$,
the P7′ shadow is

$$r\,q'(r) - q(r),$$

and exact P7′ plus asymptotic flatness force $q \equiv 0$: the only
"screened" profile satisfying the postulate is no profile at all. A
detection in the short-range window therefore cannot be absorbed by
screening; it falsifies P7′ (the appeal door recorded in
`05_open_obligations.md`, default closed).

> Verification: `009_trial_E_boundary_admissibility/trial_E3_p7prime_vs_scalaron.py`;
> `013_scalaron_screening/scalaron_screening_p7prime_obstruction.py`.

---

## 6. The result

Collecting §§2–5:

$$\boxed{\;G_{ab} + \Lambda g_{ab} = \frac{8\pi G}{c^4}\,T_{ab}\;}
\qquad\Longleftrightarrow\qquad
S = \frac{c^4}{16\pi G}\!\int\!\sqrt{-g}\,(R - 2\Lambda)
\;+\; S_{\text{matter}}\;(+\,\text{GB}).$$

Einstein's field equations, with: the response form from the
self-coupled closure of substance kinematics (§4, uniqueness proved
in-house in §4.4); the normalization from the bookkeeping-derived
static law (§2, Newton-anchored once, lifted covariantly in §2.4); the
sector architecture (negative–constraint / positive–radiative) as
stability theorems, now nonlinear in the spherical sector (§3); the
higher-derivative sector exactly empty, screening included (§5); and
$\Lambda$ permitted but not valued (its origin belongs to the
vacuum-sector program, not to this proof).

Corollaries, each verified against the observation that could kill it:
the weak-field tests (T5–T9), quadrupole radiation
(binary-pulsar-class), Lense–Thirring frame dragging $w =
-(2G/c^2)(\mathbf S\times\mathbf r)/r^3$ (GPB/LAGEOS-class),
Schwarzschild–de Sitter exactness ($AB=1$ for any $\Lambda$), and the
matter-era trace correction
$AB-1 = \tfrac32\Omega_m(H_0 r/c)^2$.

---

## 7. Why this is not circular — the ledger, discharged

| suspicion | discharge |
|---|---|
| "The Einstein tensor was assumed." | It is first *used as a response law* in §4.3, where it is *derived* (closure of K1–K3 under P9, uniqueness proved in §4.4). §§1–3 use no tensor response (§2.2/§2.4 use the Einstein tensor as differential geometry only, in identities that hold for any metric). |
| "Fierz–Pauli/Deser smuggle in GR." | Fierz–Pauli is a uniqueness theorem of field theory on Minkowski space, proved with no input from gravitational phenomenology; it constrains *any* theory with this kinematics, and the kinematics came from P2. The Deser-style closure is no longer an import at all: §4.4 proves it in-house under the stated scope, and no number moves with the historical citation. |
| "Schwarzschild was the target." | It is derived twice, independently (§2 bookkeeping; §4 closure), and the routes' agreement is a falsifiable internal check that happened to pass. The §2 route uses no field equations at all. |
| "The postulates were reverse-engineered." | The adoption records are timestamped and fenced (P9, P7′: 2026-06-11), and both postulates were adopted *before* their decisive consequences were known — P7′'s elimination of the four-derivative sector (§5.2) and its exactness under Λ (SdS) were discovered afterward. Six of the theory owner's own candidate mechanisms were killed by these same postulates' gates. |
| "GR data calibrated the constants." | One constant ($G$) enters, from Newton. Everything else is derived. Pulsar, GPB, LAGEOS, Eöt-Wash enter only afterward, as kill conditions — each could have falsified a derived coefficient; none did. |
| "AB = 1 is Schwarzschild knowledge." | $AB=1$ is the metric shadow of adopted P7′ (substance statement: no preferred static t–r frame), with the shadow equivalence proved as differential geometry (§2.2) and shown chart-invariant (§2.4b). It is also *independently checkable*: P7′ predicts **no gravitational-strength Yukawa deviation at any range** (since it forbids the only ghost-safe mechanism, §5.2, screening included) — a standing null test, currently probed to 54 μm at the scalaron coupling $\alpha = 1/3$. A bench-top detection would falsify P7′ and reopen §5. |
| "Nonlinear stability is asserted." | It is proved in-house where the framework claims theorem grade (Theorems 3n, 3m; quadratic signature Theorems 2/4 with the §4.5d vector sector), and the global small-data statement is carried as a *declared* external mathematical import (§0.1, §3) on which no coefficient depends. |

## 8. Scope and remaining limitation

This document is self-contained: every load-bearing theorem is stated
and proved above, with machine-check pointers per step. The former
rigor-debt ledger is clear — the P8/T4 rewrite, scalaron screening
(§5.2 corollary), tensor-virial identity (§4.5a), TT averaging
(§4.5b), radiative gauge invariance (§4.5c), the time-dependent vector
sector (§4.5d), closure uniqueness (§4.4), the covariant statics lift
(§2.4), and the scoped nonlinear-stability closure (§3) are all in
place. The historical closure index is preserved in
`06_rigor_closures.md`; nothing there is needed to read this proof.

The sector derivations are theorem-grade at reduced level (static
spherical, with its covariant lift and derived staticity; linearized
TT with averaging and gauge invariance; vector sector through general
linear time dependence; quasi-static cosmological patch) with exact
solutions where stated, and the static spherical sector is
theorem-grade at full nonlinearity (Theorems 3n, 3m). The two declared
external mathematical imports are Fierz–Pauli 1939 (§4.1) and
CK93/LR10 (§3's global anchor); neither carries a coefficient.

The one remaining recorded limitation is the **metric-branch input
audit** (`05_open_obligations.md`): §1's K1 step is scoped to the
SR-compatible quadratic branch. P2 by itself gives "clock/rod readings
from vacuum configuration"; deriving that the local interval is a
symmetric bilinear metric rather than Finslerian needs a
quadratic-response selector that does not yet exist. This bounds the
*novelty claim* (what is derived from P2 alone), not the derivation's
validity within the declared SR branch.

## 9. Verification index

| step | script (under `vacuum_forge/src/field_equation_trials/`) | report |
|---|---|---|
| Lemma 1 / Theorem 1 | `002_.../trial_C2_self_coupling_bootstrap.py` | trials archive |
| Lemma 2 / placement | `002_.../trial_C3_spatial_bootstrap.py` | trials archive |
| Theorem 1c (§2.4) | `019_static_covariant_lift/static_covariant_lift.py` | `06_rigor_closures.md` |
| Theorems 2–4 | `006_gate_G03_radiative_positivity/...` | `gate_G03_..._lab_report.md` |
| Theorems 3n, 3m (§3) | `020_nonlinear_stability/nonlinear_stability_scoped.py` | `06_rigor_closures.md` |
| Lemma 4 / Theorem 5 | `008_radiative_bootstrap/radiative_bootstrap_KT.py` | `radiative_bootstrap_KT_lab_report.md` |
| Theorem 5u (§4.4) | `018_closure_uniqueness/closure_step_1.py` … `closure_step_11_final_accounting.py` | `development/closure_uniqueness/` |
| §4.5a tensor-virial | `014_tensor_virial_identity/tensor_virial_identity_general.py` | `06_rigor_closures.md` |
| §4.5b TT averaging | `015_isaacson_averaging/isaacson_tt_averaging.py` | `06_rigor_closures.md` |
| §4.5c radiative gauge | `016_radiative_gauge_invariance/radiative_gauge_invariance.py` | `06_rigor_closures.md` |
| §4.5d vector sector | `012_vector_sector/vector_sector_closure.py`, `017_vector_time_dependent/vector_time_dependent.py` | `06_rigor_closures.md` |
| Theorem 6 | `010_gate_G20_beta_health/gate_G20_beta_health.py` | `gate_G20_beta_health_lab_report.md` |
| Theorem 7 | `009_.../trial_E3_p7prime_vs_scalaron.py` | `trial_E3_..._lab_report.md` |
| §5.2 screening corollary | `013_scalaron_screening/scalaron_screening_p7prime_obstruction.py` | `06_rigor_closures.md` |
| boundary corollary | `009_.../trial_E1_sharp_source_gate.py` | `trial_E1_..._lab_report.md` |
| cosmological corollary | `011_trial_F_cosmology/trial_F1_kappa_leak_coefficient.py` | `trial_F1_kappa_leak_lab_report.md` |

Run any of them: `cd vacuum_forge/src && PYTHONPATH=. python <script>` —
each re-derives its theorems from scratch and verifies its declared
dependencies against the archive.

## References (external mathematical imports)

Fierz, M., & Pauli, W. (1939). On relativistic wave equations for
particles of arbitrary spin in an electromagnetic field. *Proceedings
of the Royal Society A*, 173(953), 211–232.

Christodoulou, D., & Klainerman, S. (1993). *The Global Nonlinear
Stability of the Minkowski Space*. Princeton University Press.

Lindblad, H., & Rodnianski, I. (2010). The global stability of
Minkowski space-time in harmonic gauge. *Annals of Mathematics*,
171(3), 1401–1477.

Deser, S. (1970). Self-interaction and gauge invariance. *General
Relativity and Gravitation*, 1, 9–18. (Historical context only; the
closure theorem is proved in-house in §4.4.)
