# Which Lovelock Hypothesis VED Breaks

## Status

```text
result type:    structural argument / candidate result, not yet forge-verified
scope:          which hypothesis of Lovelock's theorem VED relaxes, and how
conclusion:     VED relaxes divergence-free / full-diffeomorphism invariance in
                the unimodular direction, forced by P3; Lambda is consequently an
                integration constant, not a coupling
non-conclusion: this does not derive Lambda's value and does not change the
                closed local response
```

This note answers a specific question raised by the candidate-response-shapes
exploration: *given that the closed sector reproduces the Einstein field
equations, and Lovelock's theorem says that result is forced, which of
Lovelock's hypotheses is VED actually free in?* The answer is sharp and, the
note argues, provable rather than analogical. It is written to be checkable by
a reader who knows the unimodular-gravity literature.

The forge obligations that would promote this from "structural argument" to
"verified result" are listed at the end; they are the only thing that would
motivate opening a subfolder for this line.

## 1. Lovelock's theorem, stated precisely

**Theorem (Lovelock 1971, 1972).** Let $A^{ab}$ be a tensor satisfying

1. **(H1, single field)** $A^{ab}$ is a concomitant of the metric alone:
   $A^{ab}=A^{ab}\!\left(g_{cd},\,\partial_e g_{cd},\,\partial_e\partial_f g_{cd}\right)$
   — no other fields, no independent connection;
2. **(H2, second order)** it depends on at most second derivatives of $g_{ab}$;
3. **(H3, conservation)** it is identically divergence-free,
   $\nabla_a A^{ab}=0$ for *every* metric (off shell);
4. **(H4, symmetric rank-2)** $A^{ab}=A^{ba}$;
5. **(H5, locality)** it is a local concomitant (finite derivative order);
6. **(H6, dimension)** $\dim M = 4$.

Then $A^{ab}=\alpha\,G^{ab}+\beta\,g^{ab}$ for constants $\alpha,\beta$.

In the Lagrangian form, H3 is the statement that the action is invariant under
the **full** diffeomorphism group $\mathrm{Diff}(M)$; the Euler–Lagrange tensor
of a $\mathrm{Diff}$-invariant local metric action is automatically
divergence-free by Noether's second theorem. $\beta g^{ab}$ is the
cosmological term: Lovelock *permits* it but fixes neither its value nor its
status. (Gauss–Bonnet appears as well but is a topological total derivative in
4D and drops out of the field equations.)

The program's "the closed sector is forced to be GR" is exactly this theorem.
The remaining freedom of VED therefore lives entirely in whichever hypothesis
VED does not actually obey.

## 2. A kinematic identity: kappa *is* the metric volume-density mode

Work in the static spherical areal gauge used throughout the reduced program,

$$ds^2=-A(r)\,c^2dt^2+B(r)\,dr^2+r^2\,d\Omega^2 .$$

The metric determinant is

$$-g=A\,B\,r^4\sin^2\theta
\qquad\Longrightarrow\qquad
\sqrt{-g}=\sqrt{AB}\;r^2\sin\theta .$$

With the flat fiducial determinant $\sqrt{-\bar g}=r^2\sin\theta$, the reduced
trace mode $\kappa=\tfrac12\ln(AB)$ obeys the **exact identity**

$$\boxed{\;\kappa=\ln\frac{\sqrt{-g}}{\sqrt{-\bar g}}\;}$$

so $\kappa$ is not "trace-like" by analogy: it is, exactly, the logarithm of
the metric volume density relative to the fiducial volume density. Equivalently
$\kappa$ is the conformal/determinant mode of the metric in this sector. This is
the kinematic fact the rest of the argument rests on, and it is checkable by
direct computation.

## 3. P3 (and its shadow P7′) impose the unimodular constraint

The condition the reduced program imposes on this mode is

$$\kappa=0\quad\Longleftrightarrow\quad AB=1\quad\Longleftrightarrow\quad
\sqrt{-g}=\sqrt{-\bar g}.$$

By the identity of §2 this is precisely the **unimodular constraint**: the
metric volume form is fixed to a non-dynamical fiducial volume form, and the
determinant mode is removed from the dynamics.

This is not an extra assumption bolted on; it is the geometric content the
postulates already carry:

- **P3 (constant vacuum energy density).** With P1–P2 identifying vacuum,
  energy, and spacetime, "the substance's density does not vary — only its
  configuration does" is a constraint on the amount-per-volume, i.e. on the
  volume measure carried by the configuration. Fixing the vacuum volume density
  is fixing $\sqrt{-g}$ for the vacuum sector.
- **P7′ (static frame indifference).** Its metric shadow is $AB=1$ in the
  static exterior (the demoted-P7 content), which by §2 is exactly
  $\sqrt{-g}=\sqrt{-\bar g}$ there.
- **The sign architecture (G02/G03).** The scalar/trace sector is forced to be
  non-propagating and constraint-like. In unimodular language this is the
  statement that the determinant/conformal mode is not a dynamical degree of
  freedom. Same content.

So the framework's most robust structural commitments are, jointly, the
unimodular restriction applied to the vacuum sector.

## 4. The hypothesis that breaks: H3 (with an H1 dual)

Under the unimodular restriction the metric variation is constrained to be
trace-free ($g_{ab}\delta g^{ab}=0$, since $\delta\sqrt{-g}=0$), so the
stationarity of the Einstein–Hilbert action yields only the **trace-free**
Einstein equation

$$R_{ab}-\tfrac14 g_{ab}R=\frac{8\pi G}{c^4}\Big(T_{ab}-\tfrac14 g_{ab}T\Big).$$

The left-hand tensor $A_{ab}\equiv R_{ab}-\tfrac14 g_{ab}R$ satisfies H1, H2,
H4, H5, H6 — it is a local, second-order, symmetric, metric-built tensor in 4D.
But it **fails H3**. Using the contracted Bianchi identity
$\nabla^a R_{ab}=\tfrac12\nabla_b R$,

$$\nabla^a A_{ab}=\nabla^aR_{ab}-\tfrac14\nabla_bR
=\tfrac12\nabla_bR-\tfrac14\nabla_bR=\tfrac14\nabla_bR\;\neq\;0
\quad\text{(identically).}$$

This is the crisp statement of what VED is free in: **its response tensor is
not identically divergence-free.** It is conserved only *on shell*, after the
separate input of matter conservation — and that on-shell step is exactly what
manufactures $\Lambda$ (§6). VED therefore sits at the one relaxation of
Lovelock's hypotheses that the theorem's conclusion is sensitive to here, and
it is the well-studied **unimodular** relaxation: $\mathrm{Diff}(M)$ reduced to
the **transverse (volume-preserving) diffeomorphisms** $\mathrm{TDiff}(M)$
generated by divergence-free $\xi^a$ ($\nabla_a\xi^a=0$), which preserve
$\sqrt{-g}$.

**Formulation duality (H3 vs H1).** Which hypothesis one calls "broken" is a
formulation choice, and a careful reader should see both:

```text
fixed-volume-form formulation:
  add a non-dynamical background volume form; symmetry is TDiff, not Diff.
  -> H3 (full-diffeo / identical conservation) is the relaxed hypothesis.

Henneaux-Teitelboim parametrized formulation:
  restore full Diff by introducing a Lagrange-multiplier vector density whose
  equation of motion forces d(Lambda) = 0.
  -> full Diff and H3 are kept, but H1 (metric-only) is relaxed by the extra
     field.
```

The two are physically equivalent. The honest one-line statement is: **VED
relaxes the joint (H1, H3) content of Lovelock at the unimodular point** — it
either drops full-diffeomorphism conservation (fixed volume form) or adds the
non-dynamical structure that carries the same information. It does **not** touch
H2, H5, or H6 — which is why the ghost-gated higher-derivative routes and any
$D\neq4$ moves remain correctly closed.

## 5. Impact of relaxing each Lovelock hypothesis, and why this one is acceptable

The wider impact of declining a Lovelock hypothesis depends entirely on *which*
one. They are not interchangeable: each opens a different sector of theory space
with a different stability cost and a different observational signature. The
point of this section is that VED's relaxation (H3, unimodular) is the **mildest
one available** — the only one whose wider impact leaves all local physics
identical to GR.

```text
relaxed       opens                         stability / theoretical cost        observational channel
hypothesis
-----------   ---------------------------   ---------------------------------   --------------------------
H2 2nd-order  higher-curvature, f(R),       CATASTROPHIC: Ostrogradsky ghost,   massive ghost / extra
              R^2, Weyl^2                   loss of unitarity and vacuum         scalar; gated off in VED
                                            stability
H1 metric-    scalar-tensor, Palatini,      new propagating modes; fifth        extra GW polarizations,
   only       torsion, nonmetricity         forces; equivalence-principle and   Yukawa, EP tests
                                            screening burdens
H5 locality   nonlocal gravity             causality / initial-value control;   IR / cosmological
                                            ghost-free nonlocality is delicate   leakage
H6 D = 4      Lovelock / Gauss-Bonnet      requires committing to extra         KK modes, GB couplings
              become dynamical              dimensions and their stabilization
H3 full-      unimodular gravity:          MILD: no new degrees of freedom,     Lambda status; vacuum-
   diffeo     Lambda as integration        no ghost; only a non-dynamical       energy gravitation;
              constant                      background volume form is added      nearly untestable locally
```

### Why H2, H1, H5, H6 are the costly breaks

- **H2 (second order).** Relaxing it is the higher-derivative route. By
  Ostrogradsky's theorem a non-degenerate higher-derivative Lagrangian has an
  unbounded-below Hamiltonian — a ghost — so the vacuum is unstable. This is the
  exact failure mode the program's residual-gate stack keeps detecting
  (spin-2/Weyl ghost; scalaron blocked by P7′). Its wider impact is that you
  threaten the stability of the theory itself. Highest cost, and already closed.
- **H1 (metric only).** Adding an independent connection or extra field
  generically adds **propagating degrees of freedom**: a scalar (Brans–Dicke /
  $f(R)$ scalaron), torsion modes, or nonmetricity. These show up as extra
  gravitational-wave polarizations, fifth forces, and equivalence-principle
  violations, all tightly constrained, and each needs its own screening story to
  survive. Moderate-to-high cost; this is roadmap route 1B's burden.
- **H5 (locality).** Nonlocal gravity can be confined to the IR, but generic
  nonlocality endangers causality and the initial-value formulation, and
  ghost-free nonlocal constructions are delicate. Principled cost.
- **H6 ($D=4$).** Making Gauss–Bonnet (or higher Lovelock terms) dynamical
  requires actually committing to extra dimensions and a stabilization mechanism
  — a large ontological price not on the table for a 4D substance theory.

The common feature: every one of these adds structure that **propagates** — a
ghost, a scalar, a polarization, a tower of modes — and therefore changes local
physics and faces immediate experimental exposure.

### Why H3 (unimodular) has an acceptable impact

Relaxing H3 in the unimodular direction is qualitatively different because it
**removes** a mode rather than adding one:

```text
no new propagating degrees of freedom   (UG has the same two graviton
                                         polarizations as GR)
no ghost                                 (nothing higher-derivative; the trace
                                         mode is constrained, not dynamical)
local dynamics identical to GR           (classical UG and GR+Lambda share a
                                         solution space)
```

Everything that changes is **global or structural**, not local:

1. **Lambda's status** shifts from a coupling in the action to a constant of
   integration fixed by one global datum (§6).
2. **Vacuum energy is sequestered** — a constant shift of the matter Lagrangian
   is pure trace and drops out of the trace-free equation, so the bulk vacuum
   energy does not gravitate (§6, point 1). This is a *benefit*, not a cost: it
   defuses the radiative-stability face of the cosmological-constant problem.
3. **The path-integral measure / quantum-cosmology bookkeeping** differ
   ($\Lambda$ becomes conjugate to the spacetime four-volume), which is where
   any genuine quantum distinction from GR would live.

The honest costs, stated so they cannot ambush the claim:

- **Absolute structure.** The fixed background volume form is a non-dynamical
  field. Eliminating absolute structure was one of GR's signature achievements,
  and unimodular gravity reintroduces a mild form of it. This is the standard
  foundational objection and should be conceded openly.
- **Recoverability.** The Henneaux–Teitelboim formulation restores full
  diffeomorphism invariance by adding a multiplier field, at the cost of H1
  instead. That this is possible shows the "violation" is partly a matter of
  presentation — which both weakens any "we broke a sacred symmetry" rhetoric
  and reassures that the relaxation is benign and well understood.

Net assessment: among the six hypotheses, H3-unimodular is the unique relaxation
that (i) introduces no instability, (ii) introduces no new local degree of
freedom, (iii) leaves every tested prediction of GR intact, and (iv) changes
exactly the one quantity — the status and gravitation of $\Lambda$ — that the
vacuum-sector program is trying to explain. That is why it is the acceptable
break, and the others are not.

## 6. Consequence: Lambda is an integration constant, and vacuum energy decouples

Take the divergence of the full Einstein tensor built from the trace-free
equation. The Bianchi identity gives $\nabla^aG_{ab}=0$ geometrically; writing
$G_{ab}=A_{ab}-\tfrac14 g_{ab}R$ and using the trace-free equation,

$$0=\nabla^aG_{ab}
=\frac{8\pi G}{c^4}\Big(\nabla^aT_{ab}-\tfrac14\nabla_bT\Big)-\tfrac14\nabla_bR .$$

Imposing matter conservation $\nabla^aT_{ab}=0$ as an independent input leaves

$$\nabla_b\!\left(R+\frac{8\pi G}{c^4}T\right)=0
\quad\Longrightarrow\quad
R+\frac{8\pi G}{c^4}T=\text{const}\equiv 4\Lambda .$$

Substituting back reconstructs the *full* equations with a cosmological term,

$$G_{ab}+\Lambda\,g_{ab}=\frac{8\pi G}{c^4}\,T_{ab},$$

but $\Lambda$ has entered as a **constant of integration of the conservation
law**, not as a coupling in the action. Two consequences a professional reader
will want stated explicitly:

1. **Vacuum-energy sequestering.** A constant shift $T_{ab}\to T_{ab}-\rho_{\rm
   vac}\,g_{ab}$ is pure trace, so $T_{ab}-\tfrac14 g_{ab}T$ is unchanged: the
   trace-free equation is *blind* to $\rho_{\rm vac}$. The bulk vacuum energy
   does not gravitate. This addresses the radiative-stability ("why doesn't the
   enormous vacuum energy gravitate") face of the cosmological-constant problem
   — but not the value face (the residual integration constant is still free).
2. **$\Lambda$ is fixed only by a global datum** (a single boundary/initial
   condition; in the Henneaux–Teitelboim canonical form it is conjugate to the
   total four-volume / "cosmic time").

## 7. Why this *explains* the program's own results

The unimodular reading is not merely consistent with the vacuum-sector program;
it reproduces three of its empirical findings as theorems rather than
observations:

```text
program finding                                  unimodular explanation
-----------------------------------------------  ----------------------------------
trace mode kappa is frozen / constraint-like     determinant mode is non-dynamical
(G02/G03, P7')                                    by construction

closed local sector = GR exactly                  classical UG and GR+Lambda share
                                                  the same solution space

Lambda allowed but UNVALUED by the local          Lambda is an integration
equation; every local selector (variational,      constant; only a single global
boundary, topology, measure, relaxation) leaves   datum can fix it -- exactly what
it free, and only a global datum constrains it     the 008-016 sweep discovered
(the entire Lambda baseline sweep)                 empirically
```

The last row is the strong one. The Lambda sweep spent derivations 008–016
discovering, route by route, that no *local* principle values $\Lambda$ and that
it is fixable only by a supplied global/boundary scale. That is the defining
structural property of $\Lambda$ in unimodular gravity. The sweep was, in
effect, an empirical rediscovery of the unimodular status of $\Lambda$.

## 8. Refinement: VED is unimodular in the P7′-exact limit, with a calculable leak

VED is **not** exactly unimodular once matter is present. The F1 result gives

$$AB-1=\tfrac32\,\Omega_m\Big(\frac{H_0 r}{c}\Big)^2,
\qquad AB-1\equiv 0\ \text{in any pure-}\Lambda\ \text{epoch (SdS)} .$$

By §2 this is $\kappa=\tfrac12\ln(AB)\neq0$ at $O\big((H_0r/c)^2\big)$ in a
matter cosmology, i.e. a controlled departure from the unimodular constraint.
The honest statement is therefore:

```text
VED imposes the unimodular constraint EXACTLY in the sector where P7' is exact
(static source-free exterior, and pure-Lambda / SdS, where AB = 1 identically),
and exhibits a calculable matter-sourced departure kappa = O((H0 r/c)^2)
elsewhere (F1).
```

This is a refinement of textbook unimodular gravity, not a contradiction of it:
the constraint binds the *vacuum* volume density (P3 is about the vacuum), and
matter is the source of the small $\kappa$-leak. The leak is $\sim6\times
10^{-31}$ at 1 AU — unobservable, an honesty entry, not a prediction. It does,
however, mean the unimodular identification should be stated as holding in the
P7′-exact limit, with F1 as the controlled correction.

## 9. Honest limits

- **No new local predictions follow from this alone.** Classical UG and GR+
  $\Lambda$ share a solution space, so this argument does not, by itself,
  produce an observable deviation. That is consistent with the program's
  standing result that the closed sector predicts no accessible departure from
  GR. The novelty is structural: the *status* of $\Lambda$, the symmetry group
  ($\mathrm{TDiff}$ vs $\mathrm{Diff}$), vacuum-energy sequestering, and the
  path-integral measure.
- **This does not solve the $\Lambda$-smallness problem.** It converts $\Lambda$
  from a coupling into a boundary-fixed integration constant and removes the
  bulk vacuum energy from gravitating; the value of the residual constant is
  still external. A *derivation* of that value is a separate obligation (the
  frustration/packing route in the response-shapes note, whose own decisive
  gate is the curvature-scale smallness problem).
- **The identity of §2 is sector-scoped.** It is exact in static spherical
  areal gauge. The general claim "$\kappa$ is the conformal/volume mode" is
  true mode-theoretically, but a covariant statement (and the covariant form of
  the $\kappa=0$ constraint) is the same covariant-parent obligation the program
  already carries.

## 10. What is genuinely new here

The genuinely new content, relative to both standard UG and the current VED
documents, is the **derivation of the unimodular constraint from a physical
postulate** rather than its imposition by fiat. Textbook UG *posits*
$\sqrt{-g}=\text{const}$. VED would *derive* it from P3 (constant vacuum energy
density) via the identity $\kappa=\ln(\sqrt{-g}/\sqrt{-\bar g})$ and the
constraint $\kappa=0$. If that derivation holds, the chain

```text
P3 (constant vacuum density)
  -> sqrt(-g) fixed (unimodular constraint), exact in the P7'-exact limit
  -> trace-free Einstein equations
  -> Lambda as integration constant, vacuum energy sequestered
```

is a structural result that closes, in one stroke, the question the Lambda
baseline sweep left open ("why is Lambda unvalued by every local route?").

## 11. Forge obligations (what would make this a verified result)

The following are concrete, scriptable checks. They are the only thing that
would justify a dedicated subfolder for this line.

```text
1. Verify the kinematic identity kappa = ln(sqrt(-g)/sqrt(-g_bar)) in the
   reduced areal gauge symbolically (sympy: det of diag(-A,B,r^2,r^2 sin^2)).
2. Verify nabla^a (R_ab - 1/4 g_ab R) = 1/4 nabla_b R via the contracted
   Bianchi identity (the H3-violation computation).
3. Verify that the trace-free Einstein equation plus nabla^a T_ab = 0 yields
   R + (8 pi G/c^4) T = const, i.e. Lambda as an integration constant, and
   reconstruct G_ab + Lambda g_ab = (8 pi G/c^4) T_ab.
4. Verify trace-free blindness: substitute T_ab -> T_ab - rho_vac g_ab and show
   the trace-free equation is invariant (sequestering).
5. Cross-check the F1 leak kappa = (1/2) ln(AB) = O((H0 r/c)^2) against the
   unimodular constraint to confirm the departure is matter-sourced and
   second-order.
```

Items 1–4 are short and decisive; item 5 connects to existing F1 output.

## References

```text
D. Lovelock, J. Math. Phys. 12, 498 (1971).
D. Lovelock, J. Math. Phys. 13, 874 (1972).
S. Weinberg, Rev. Mod. Phys. 61, 1 (1989).        [cosmological constant review]
J.J. van der Bij, H. van Dam, Y.J. Ng, Physica A 116, 307 (1982).
M. Henneaux, C. Teitelboim, Phys. Lett. B 222, 195 (1989).
W.G. Unruh, Phys. Rev. D 40, 1048 (1989).
Y.J. Ng, H. van Dam, J. Math. Phys. 32, 1337 (1991).
G.F.R. Ellis, H. van Elst, J. Murugan, J.-P. Uzan,
  Class. Quantum Grav. 28, 225007 (2011).         [trace-free Einstein eqs]
```
