# Proof: The Field Equations of Vacuum Energy Dynamics

**Purpose.** A direct, linear derivation of the field equations from the
postulates, written for a practitioner who wants to verify two things:
(1) each step is sound, and (2) **general relativity is not imported to
derive general relativity.** The path was found by exploration
(`development/field_equation_trials/`); this document is the direct
route. Every nontrivial step carries a verification pointer to a
machine-checked derivation (sympy, re-run from scratch on every
execution).

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
- **One external mathematical theorem plus one in-house closure theorem**,
  stated and discharged in §4: linear uniqueness of the massless spin-2
  operator (Fierz–Pauli 1939) and the 018 uniqueness proof of its
  self-coupled closure. Both are theorems of *special-relativistic field theory on Minkowski
  space*: their statements and proofs nowhere assume that Einstein's
  equations hold in nature. Using them is using mathematics, not
  importing GR's physical content.

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

This is postulate content doing work, stated as such — P7′ is one of
the nine commitments, adopted with its fence and its own observable
face (§7). It is *not* extracted from the Schwarzschild solution; the
adoption record and the equivalence theorem ("$AB=1$ ⟺ no preferred
t–r frame," proved as differential geometry in trial C3) predate every
use below.

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
re-deriving it as a positive bolt-on source. (Independently: trial C3
proves the explicit positive-source placement breaks Lemma 2 —
a scalar-gradient stress has $T^t{}_t \neq T^r{}_r$ — so the
geometry-side negative counting is the *only* P7′-compatible option.)

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

---

## 3. Stability and the sector signature

Three theorems establish that the negative energy of §2.3 cannot
destabilize anything — *before* the dynamics is even fixed, these are
constraints any dynamics must satisfy; after §4 they hold in it.

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

**Theorem 4 (radiative positivity).** The propagating (transverse-
traceless) sector's energy density is a sum of squares — positive
definite — with outward null flux for outgoing waves. (Coefficient
derived in §4.3.)

> Verification: `006_gate_G03_radiative_positivity/`.

---

## 4. The dynamical closure: from linear kinematics to the full equations

The static sector (§2) constrains but does not constitute dynamics.
This section derives the full response law. **This is where the two
external theorems are used; both are SR field theory.**

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
stress, repeat — has a unique consistent completion by the in-house
closure-uniqueness program in 018: the geometric response

$$N\,\mathcal G_{ab}[g] = T_{ab},$$

where $\mathcal G_{ab}$ is the (now *derived*) Einstein combination and
a cosmological term $\Lambda g_{ab}$ remains permitted. *Status of the
former import:* the Deser-style uniqueness theorem has been reproduced
in-house under the stated local, two-derivative, no-extra-field scope;
it is coefficient-free and no number depends on the historical citation.

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

> Verification: `009_trial_E_boundary_admissibility/trial_E3_p7prime_vs_scalaron.py`.

---

## 6. The result

Collecting §§2–5:

$$\boxed{\;G_{ab} + \Lambda g_{ab} = \frac{8\pi G}{c^4}\,T_{ab}\;}
\qquad\Longleftrightarrow\qquad
S = \frac{c^4}{16\pi G}\!\int\!\sqrt{-g}\,(R - 2\Lambda)
\;+\; S_{\text{matter}}\;(+\,\text{GB}).$$

Einstein's field equations, with: the response form from the
self-coupled closure of substance kinematics (§4); the normalization
from the bookkeeping-derived static law (§2, Newton-anchored once); the
sector architecture (negative–constraint / positive–radiative) as
stability theorems (§3); the higher-derivative sector exactly empty
(§5); and $\Lambda$ permitted but not valued (its origin belongs to the
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
| "The Einstein tensor was assumed." | It is first *used as a response law* in §4.3, where it is *derived* (closure of K1–K3 under P9). §§1–3 use no tensor response. Its appearance in trial scripts predating the closure was always as a conditional object under stated gates; the proof's ordering removes even that. |
| "Fierz–Pauli/Deser smuggle in GR." | Fierz–Pauli and the in-house Deser-style closure are uniqueness theorems of field theory on Minkowski space, proved with no input from gravitational phenomenology. They constrain *any* theory with this kinematics; the kinematics came from P2. The former Deser citation is now historical context rather than active rigor debt, and no number moves with it. |
| "Schwarzschild was the target." | It is derived twice, independently (§2 bookkeeping; §4 closure), and the routes' agreement is a falsifiable internal check that happened to pass. The §2 route uses no field equations at all. |
| "The postulates were reverse-engineered." | The adoption records are timestamped and fenced (P9, P7′: 2026-06-11), and both postulates were adopted *before* their decisive consequences were known — P7′'s elimination of the four-derivative sector (§5.2) and its exactness under Λ (SdS) were discovered afterward. Six of the theory owner's own candidate mechanisms were killed by these same postulates' gates. |
| "GR data calibrated the constants." | One constant ($G$) enters, from Newton. Everything else is derived. Pulsar, GPB, LAGEOS, Eöt-Wash enter only afterward, as kill conditions — each could have falsified a derived coefficient; none did. |
| "AB = 1 is Schwarzschild knowledge." | $AB=1$ is the metric shadow of adopted P7′ (substance statement: no preferred static t–r frame), with the shadow equivalence proved as differential geometry. It is also *independently checkable*: P7′ predicts **no gravitational-strength Yukawa deviation at any range** (since it forbids the only ghost-safe mechanism, §5.2) — a standing null test, currently probed to 54 μm at the scalaron coupling $\alpha = 1/3$. A bench-top detection would falsify P7′ and reopen §5. |

## 8. Scope, rigor closures, and remaining debts

Completed proof-hardening closures are indexed in
`06_rigor_closures.md`: P8/T4 formal rewrite, scalaron screening,
tensor-virial identity in generality, Isaacson-style TT averaging,
radiative gauge invariance, the general time-dependent vector-sector
lift, and the in-house closure-uniqueness proof replacing the active
Deser citation. These closures support this proof without changing the field
equations or moving any coefficient.

The sector derivations are theorem-grade at reduced level (static
spherical; linearized TT; vector sector through general linear time
dependence; quasi-static cosmological patch) with exact solutions where
stated. Current live debts after the closures above are: covariant lift
of the C2/C3 static bookkeeping sector; nonlinear stability; and the
metric-branch input audit recorded in `05_open_obligations.md`. The
earlier tensor-virial, Isaacson averaging, radiative gauge, vector
time-dependence, and closure-uniqueness debts are retired in
`06_rigor_closures.md`.

## 9. Verification index

| step | script (under `vacuum_forge/src/field_equation_trials/`) | report |
|---|---|---|
| Lemma 1 / Theorem 1 | `002_.../trial_C2_self_coupling_bootstrap.py` | trials archive |
| Lemma 2 / placement | `002_.../trial_C3_spatial_bootstrap.py` | trials archive |
| Theorems 2–4 | `006_gate_G03_radiative_positivity/...` | `gate_G03_..._lab_report.md` |
| Lemma 4 / Theorem 5 | `008_radiative_bootstrap/radiative_bootstrap_KT.py` | `radiative_bootstrap_KT_lab_report.md` |
| Theorem 6 | `010_gate_G20_beta_health/gate_G20_beta_health.py` | `gate_G20_beta_health_lab_report.md` |
| Theorem 7 | `009_.../trial_E3_p7prime_vs_scalaron.py` | `trial_E3_..._lab_report.md` |
| boundary corollary | `009_.../trial_E1_sharp_source_gate.py` | `trial_E1_..._lab_report.md` |
| cosmological corollary | `011_trial_F_cosmology/trial_F1_kappa_leak_coefficient.py` | `trial_F1_kappa_leak_lab_report.md` |
| vector corollary | `012_vector_sector/vector_sector_closure.py` | `vector_sector_closure_lab_report.md` |
| scalaron screening closure | `013_scalaron_screening/scalaron_screening_p7prime_obstruction.py` | `06_rigor_closures.md` |
| tensor-virial closure | `014_tensor_virial_identity/tensor_virial_identity_general.py` | `06_rigor_closures.md` |
| TT averaging closure | `015_isaacson_averaging/isaacson_tt_averaging.py` | `06_rigor_closures.md` |
| radiative gauge closure | `016_radiative_gauge_invariance/radiative_gauge_invariance.py` | `06_rigor_closures.md` |
| time-dependent vector lift | `017_vector_time_dependent/vector_time_dependent.py` | `06_rigor_closures.md` |

Run any of them: `cd vacuum_forge/src && PYTHONPATH=. python <script>` —
each re-derives its theorems from scratch and verifies its declared
dependencies against the archive.
