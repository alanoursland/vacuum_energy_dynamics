# Development Hints for the Reduced A-Sector and Scalar-Recombination Program

## Purpose

This note collects development hints for the current field-equation program using only the language of the reduced static spherical model, its scalar-response audit, and its unresolved recombination problem.

The central idea is to treat the reduced \(A\)-sector success as a hard constraint on any future parent construction. The current branch already recovers the ordinary exterior mass response, but the full theory is not licensed until scalar spatial response, trace membership, compensation, residual control, source neutrality, boundary neutrality, and parent divergence safety are closed without undefined repair objects.

External motivation: possible vacuum manipulation / Casimir relevance.
Archive status: not evidence, not derivation, not a source of field-equation licenses.
Allowed use: generate audit questions about boundary behavior, vacuum accounting, source neutrality, and exterior loads.
Forbidden use: justify coefficients, currents, correction tensors, parent closure, or insertion.

## 1. Preserve the reduced \(A\)-sector as the strongest licensed anchor

The most stable result remains

\[
\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho,
\]

with

\[
\Delta_{\rm areal}A
=
\frac1{r^2}\frac{d}{dr}\left(r^2A'\right),
\]

\[
F_A=4\pi r^2A'(r),
\]

and

\[
M_A=\frac{c^2F_A}{8\pi G}.
\]

Any parent construction should preserve the exterior audit success

\[
A_{\rm ext}(r)=1-\frac{2GM}{c^2r},
\]

\[
M_A=M.
\]

This should be treated as a non-negotiable reduced-branch constraint. New scalar, residual, exchange, or vacuum-accounting terms should not disturb this result unless their non-entry into the reduced \(A\)-sector has been explicitly proved.

## 2. Treat \(B=1/A\) as recovered compensation, not as a primitive rule

The compensated reduced static spherical exterior branch gives

\[
\kappa_{\rm areal}
=
\frac12\ln(AB),
\]

and the compensated condition

\[
\kappa_{\rm areal}=0
\]

implies

\[
AB=1,
\]

so

\[
B=\frac1A.
\]

This is a recovered exterior result, not yet a licensed parent construction rule.

A future parent derivation should explain why the compensated branch produces \(AB=1\) in the reduced exterior case, while also showing which variables are prevented from re-entering the metric as independent contributions.

## 3. Make \(B_s/F_\zeta\) a licensed recombination law, not a patch

The central missing object remains

\[
B_s/F_\zeta.
\]

This should not be introduced as a repair factor. It needs a domain, codomain, normalization convention, source behavior, boundary behavior, and metric-entry rule.

A useful target is:

\[
B_s/F_\zeta
\quad
\text{must determine the allowed scalar spatial response without producing an additional exterior mass contribution.}
\]

That means \(B_s/F_\zeta\) should be active in the scalar-response accounting but neutral with respect to already-counted \(A\)-sector mass response.

The recombination law should answer:

1. What is the source of \(B_s\)?
2. What is the source of \(F_\zeta\)?
3. What trace convention fixes \(F_\zeta\)?
4. Which part, if any, enters the metric?
5. Which part is internal bookkeeping only?
6. Which part is projected out by the no-overlap structure?
7. What happens at the matter boundary?
8. What happens in the exterior vacuum branch?

Until these are answered, \(B_s/F_\zeta\) remains a candidate object, not a licensed equation.

## 4. Use the exterior \(1/r\) branch as an audit signature

The reduced \(A\)-sector produces the exterior areal mass response

\[
A_{\rm ext}(r)=1-\frac{2GM}{c^2r}.
\]

Any scalar-response or recombination rule that produces an additional independent \(1/r\) metric contribution risks double-counting the same exterior mass response.

Therefore, a future rule should distinguish between:

\[
\text{already-counted exterior mass response}
\]

and

\[
\text{permitted scalar spatial-response bookkeeping}.
\]

A scalar or residual term may be allowed to shape an internal response operator, but it should not automatically become an additional exterior metric source.

This gives a practical audit question:

\[
\text{Does this term create a second exterior }1/r\text{ metric contribution?}
\]

If yes, the term is suspect unless a no-overlap theorem removes the duplication.

## 5. Define the no-overlap operator before using correction objects

The candidate no-overlap operator \(O\) is required but absent.

It should be constructed before introducing objects such as

\[
J_V,\quad J_{\rm sub},\quad J_{\rm exch},\quad \Sigma_V,\quad R_V,\quad H_{\rm curv},\quad H_{\rm exch}.
\]

The operator \(O\) should specify:

\[
\mathrm{dom}(O),
\qquad
\mathrm{codom}(O),
\qquad
\ker(O),
\qquad
\mathrm{im}(O),
\]

and should prove whether

\[
O^2=O.
\]

It should also state its behavior under divergence:

\[
\nabla\cdot O(\cdot)
\]

or the appropriate covariant parent analogue.

A useful design constraint is that \(O\) should separate at least four roles:

\[
\text{ordinary exterior mass response},
\]

\[
\text{scalar spatial-response accounting},
\]

\[
\text{compensation / residual accounting},
\]

\[
\text{ordinary tensor radiation sector}.
\]

If a contribution is assigned to one role, the operator should prevent it from entering another role unless a theorem explicitly licenses the transfer.

## 6. Make residual non-reentry a theorem

The total metric double-count load is

\[
L_{\rm double}
=
e_{\kappa,{\rm metric}}
+
\epsilon_{{\rm vac},{\rm metric}}
+
\kappa_{\rm metric}
+
\zeta_{{\rm residual},{\rm metric}}.
\]

The theory needs one of two outcomes:

\[
L_{\rm double}\to0,
\]

or

\[
L_{\rm double}
\quad
\text{is inert / non-metric}.
\]

This should not be assumed. It should be proved.

A useful development path is to require each contribution to pass a metric-entry test:

\[
e_{\kappa,{\rm metric}}\stackrel{?}{=}0,
\]

\[
\epsilon_{{\rm vac},{\rm metric}}\stackrel{?}{=}0,
\]

\[
\kappa_{\rm metric}\stackrel{?}{=}0,
\]

\[
\zeta_{{\rm residual},{\rm metric}}\stackrel{?}{=}0.
\]

If any term is nonzero, it must have a licensed source, boundary behavior, and divergence behavior. Otherwise it should be projected into the inert sector or removed.

## 7. Keep \(\zeta\) and \(\kappa\) from becoming unlicensed long-range scalar radiation

The long-range scalar breathing route is rejected:

\[
A_{\rm rad},\zeta,\kappa
\quad
\text{as ordinary scalar breathing radiation}.
\]

Therefore, \(\zeta\) and \(\kappa\) should not be allowed to become free exterior radiative fields by accident.

A safer role is:

\[
\zeta,\kappa
\quad
\text{as constrained scalar-response / compensation variables},
\]

not independent radiative channels.

The allowed long-range radiation candidate remains

\[
h^{TT}_{ij}.
\]

Thus a future parent theory should show that scalar residual variables either:

1. vanish in the exterior radiative channel,
2. are gauge / compensation diagnostics,
3. are projected out by \(O\), or
4. remain internal to the scalar-response bookkeeping and do not propagate as ordinary long-range scalar radiation.

## 8. Separate angular geometry from scalar recombination

The angular sector should be explained by ordinary spherical geometry on the reduced static branch. Scalar recombination should not be asked to explain angular labels or angular multiplicity.

The angular part is already structurally tied to the sphere through the usual angular operator:

\[
\hat L^2Y=\ell(\ell+1)Y.
\]

The scalar recombination problem should instead focus on radial response, trace membership, compensation, and metric-entry control.

This separation prevents \(B_s\), \(F_\zeta\), \(\zeta\), or \(\kappa\) from being assigned unnecessary angular duties.

## 9. Demand a reduced scalar-response theorem before the full parent equation

The schematic parent equation

\[
E_{\rm parent}+H_{\rm curv}+H_{\rm exch}
=
\text{source side}
\]

is not yet licensed.

Before attempting the full parent equation, it may be better to prove a narrower reduced theorem:

On the compensated static spherical exterior branch,

\[
AB=1,
\]

the licensed scalar-response variables produce a well-defined reduced radial operator whose source behavior, boundary behavior, and exterior behavior are all neutral with respect to the already-counted \(A\)-sector mass.

This theorem should prove:

1. the reduced \(A\)-sector still gives \(M_A=M\),
2. \(B=1/A\) is recovered only through compensation,
3. \(B_s/F_\zeta\) has a declared trace convention,
4. residual variables do not re-enter the metric,
5. no extra exterior scalar radiation is introduced,
6. the divergence behavior is safe.

Only after this reduced theorem is closed should \(H_{\rm curv}\), \(H_{\rm exch}\), \(J_V\), \(\Sigma_V\), or \(R_V\) be inserted into a parent equation.

## 10. Use source neutrality and boundary neutrality as hard gates

Any candidate scalar or residual construction should pass two neutrality tests.

### Source neutrality

The candidate must not alter the ordinary mass audit:

\[
M_A=M.
\]

If a candidate changes \(F_A\), \(M_A\), or \(A_{\rm ext}\), it must explain why this is not double-counting ordinary exterior mass.

### Boundary neutrality

The candidate must behave safely across the matter/exterior boundary.

It should not introduce a discontinuity, shell term, hidden surface source, or compensating repair object unless that object is independently derived.

A useful boundary question is:

\[
\text{Does the candidate create an unlicensed jump in }A,\ B,\ \zeta,\ \kappa,\ B_s,\text{ or }F_\zeta?
\]

If yes, the candidate is not yet licensed.

## 11. Treat trace normalization as a convention that must be declared before use

The map

\[
P_{\rm trace\_norm}
\]

and the target

\[
T_\zeta
\]

must be fixed before using

\[
\zeta_{B_s}\to T_\zeta.
\]

The trace-sector rule should specify:

1. what object is being traced,
2. what metric or reduced geometry performs the trace,
3. what normalization is used,
4. whether the trace object is metric-entering or internal,
5. how the trace rule behaves in the exterior branch,
6. how it behaves under compensation.

Without this, \(\zeta_{B_s}\to T_\zeta\) is only compatible-if-declared, not a derivation.

## 12. Do not use undefined repair objects to close the theory

Objects such as

\[
H_{\rm curv},
\quad
H_{\rm exch},
\quad
J_V,
\quad
J_{\rm sub},
\quad
J_{\rm exch},
\quad
\Sigma_V,
\quad
R_V
\]

should not be used to cancel residual errors until their own source, divergence, boundary, and metric-entry rules are known.

A correction tensor is not licensed merely because it cancels a defect.

A current is not licensed merely because it improves bookkeeping.

A residual operator is not licensed merely because it prevents double-counting.

Each object must have an independent construction and must preserve the reduced \(A\)-sector audit.

## 13. Proposed minimal closure theorem

A useful near-term target is the following theorem.

### Reduced scalar-recombination closure theorem

Assume:

\[
\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho,
\]

\[
A_{\rm ext}(r)=1-\frac{2GM}{c^2r},
\]

\[
M_A=M,
\]

and

\[
AB=1
\]

on the compensated reduced exterior branch.

Then construct \(B_s/F_\zeta\), \(P_{\rm trace\_norm}\), and \(O\) such that:

\[
L_{\rm double}=0
\]

or

\[
L_{\rm double}
\quad
\text{is inert / non-metric},
\]

while preserving:

\[
M_A=M,
\]

\[
B=\frac1A,
\]

and

\[
h^{TT}_{ij}
\]

as the only ordinary long-range radiation candidate.

The theorem should also prove source neutrality, boundary neutrality, trace consistency, and divergence safety.

## 14. Development order

A safe development order is:

1. Freeze the reduced \(A\)-sector audit.
2. Declare the trace normalization convention.
3. Define \(B_s/F_\zeta\) with source and boundary behavior.
4. Define \(O\) with domain, codomain, kernel, image, idempotence, and divergence behavior.
5. Prove residual non-reentry.
6. Prove source neutrality.
7. Prove boundary neutrality.
8. Prove that scalar variables do not become ordinary long-range scalar radiation.
9. Only then introduce exchange, vacuum-current, or curvature-correction objects.
10. Only after that attempt the parent field equation.

## 15. Guiding principle

The reduced branch already carries the ordinary exterior mass response.

The remaining scalar and residual machinery should therefore be judged by whether it explains compensation, trace accounting, and spatial response without re-counting the same mass response.

In compact form:

\[
\text{new scalar structure}
\neq
\text{second exterior mass source}.
\]

The intended outcome is not more metric load. The intended outcome is licensed recombination with no residual re-entry.
