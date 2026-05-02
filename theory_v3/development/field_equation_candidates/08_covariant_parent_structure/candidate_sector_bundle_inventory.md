# Candidate Sector Bundle Inventory

## What This Document Is

This document is a development note for the `08_covariant_parent_structure/` group.

It is not a covariant derivation, not a final field-equation proposal, and not a proof that the reduced sectors are physically complete. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_sector_bundle_inventory.py
```

The guiding question was:

```text
Can the reduced sector program be organized as a coherent bundle that might be
the shadow of one deeper geometric/covariant parent structure?
```

The answer is yes at the reduced architecture level.

The current sector bundle is:

```text
A_constraint -> scalar/static mass response
A_rad        -> controlled/absent scalar radiative component
kappa        -> trace/interior response
W_i          -> vector/current/frame-dragging response
h_ij^TT      -> tensor/quadrupole/radiative response
```

This does not yet prove the existence of a covariant parent.

It states what the parent must explain.

---

## Important Method Note

The script mostly passes because it is an inventory and consistency-classification script.

It is checking whether each sector can be stated coherently, whether the known algebraic identities hold, and whether the open requirements are correctly listed.

It is not trying to falsify the whole theory.

A stronger future script should include explicit failure conditions such as:

```text
missing source coupling,
incorrect gauge behavior,
uncontrolled extra polarization,
conflicting equation type,
failure to map into metric variables,
failure to preserve known static exterior behavior.
```

So the pass result should be read as:

```text
The reduced sector bundle is internally organized.
```

not as:

```text
The covariant theory has been proven.
```

---

## Sector Bundle Problem

The group-08 question is:

```text
Can the reduced sectors be organized as the shadow of one deeper
geometric/covariant parent structure?
```

The current sectors are:

```text
A_constraint -> scalar/static mass response
A_rad        -> controlled/absent scalar radiative component
kappa        -> trace/interior response
W_i          -> vector/current response
h_ij^TT      -> tensor/radiative response
```

The script inventories the bundle and records open requirements.

It confirmed:

```text
sector bundle inventory problem posed.
```

---

## Current Sector Table

The script produced this sector table:

| Sector | Variable | Source | Equation type | Metric location | Radiation status |
|---|---|---|---|---|---|
| scalar constraint | \(A_{\rm constraint}\) | mass density \(\rho/M\) | elliptic Poisson | \(g_{tt}\) / scalar potential | nonradiative/static |
| scalar radiative hazard | \(A_{\rm rad}\) | scalar breathing source? | controlled or absent | scalar spatial trace | dangerous unless suppressed |
| trace/interior | \(\kappa\) | pressure/stress/trace candidate | response/relaxation | volume/trace imbalance | suppressed exterior |
| vector current | \(W_i\) | mass current / angular momentum | vector constraint/evolution TBD | \(g_{ti}\) / shift | frame dragging, not ordinary wave yet |
| tensor radiation | \(h_{ij}^{TT}\) | trace-free quadrupole derivatives | hyperbolic wave | spatial TT metric | active radiation |

This is the clearest current map of the reduced theory.

---

## A_constraint Static Scalar Sector

The scalar constraint exterior is:

$$
A=1-\frac{2GM}{c^2r}.
$$

For \(r>0\), it satisfies:

$$
\nabla^2A=0.
$$

The script confirmed:

```text
A_constraint supports static exterior gravity.
```

Role:

```text
static scalar mass response,
Newtonian potential channel,
monopole A-flux.
```

Parent requirement:

```text
explain why A_constraint is elliptic/constraint-like, not an unsuppressed
long-range scalar radiation mode.
```

This is one of the most important requirements.

The scalar branch must preserve static gravity without becoming free scalar radiation.

---

## A_rad Controlled Scalar Radiative Hazard

If \(A_{\rm rad}\) is an unsuppressed scalar plane wave:

$$
A_{\rm rad}=H\cos(kx-\omega t),
$$

then:

$$
\frac{\Box A_{\rm rad}}{A_{\rm rad}}
=
k^2-\frac{\omega^2}{c^2}.
$$

This propagates when:

$$
\omega^2=c^2k^2.
$$

The script confirmed:

```text
A_rad is dangerous if unsuppressed.
```

Safety requirement:

```text
A_rad must be absent, projected out, damped/absorbed, massive,
relaxed to minimum, weakly coupled, or observationally constrained.
```

Thus \(A_{\rm rad}\) is not part of the ordinary safe radiation claim.

---

## Moving Gravity Well Versus Scalar Gravity Wave

The script recorded an important distinction.

A moving mass can carry a moving scalar gravity well.

For example:

$$
A_{\rm well}(x,t)=f(x-X(t)).
$$

With \(X(t)=vt\), this is a translated scalar configuration:

$$
A_{\rm well}(x,t)=f(x-vt).
$$

That is different from an independent scalar wave:

$$
A_{\rm wave}=H\cos(kx-\omega t).
$$

The scalar wave has a dispersion relation and can carry a breathing polarization.

The moving well can instead be interpreted as a moving or retarded scalar constraint configuration tied to the source.

The script confirmed:

```text
moving well distinguished from free scalar wave.
```

This distinction is useful.

It allows the theory to say:

```text
gravity wells can move with matter
```

without saying:

```text
the scalar channel contains independent long-range scalar gravity waves.
```

In other words:

```text
a moving scalar well is not automatically scalar radiation.
```

---

## Kappa Trace / Interior Response Sector

The \(\kappa\) sector is currently interpreted as:

```text
trace/interior matter response,
volume/metric determinant imbalance,
suppressed in ordinary exterior.
```

A toy energy is:

$$
E_\kappa=\frac12m_\kappa^2\kappa^2.
$$

Then:

$$
\frac{dE_\kappa}{d\kappa}=m_\kappa^2\kappa.
$$

This supports exterior suppression or relaxation toward:

$$
\kappa=0.
$$

The script confirmed:

```text
kappa sector classified as trace/interior response.
```

Parent requirement:

```text
explain source of kappa inside matter and suppression/relaxation outside.
```

---

## W_i Vector / Current Sector

The vector sector is:

$$
W_i=(V_x,V_y,V_z).
$$

Source candidates:

```text
mass current,
angular momentum.
```

Metric location:

```text
g_ti / shift-like sector.
```

Role:

```text
frame dragging,
rotational/current response.
```

The script confirmed:

```text
vector sector classified as current/frame-dragging response.
```

Parent requirement:

```text
derive frame dragging and decide whether vector radiation exists or is constrained.
```

This sector is necessary because scalar \(A\) cannot produce frame dragging.

---

## h_ij^TT Tensor / Radiation Sector

The tensor radiation sector is:

$$
h_{ij}^{TT}
=
\begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

Its trace is:

$$
0.
$$

For propagation along \(z\):

$$
k^ih_{ij}=0.
$$

The script confirmed:

```text
tensor sector remains TT radiation channel.
```

Role:

```text
ordinary long-range gravitational radiation,
plus/cross polarizations,
quadrupole tensor flux.
```

Parent requirement:

```text
derive TT wave equation, coupling, flux, and gauge constraints from parent
structure.
```

---

## Constraint / Evolution Split

The script stated the current preferred equation character:

| Variable | Preferred equation character | Reason |
|---|---|---|
| \(A_{\rm constraint}\) | constraint / elliptic | static scalar gravity, no scalar waves |
| \(A_{\rm rad}\) | absent or controlled | avoid scalar breathing radiation |
| \(\kappa\) | response / relaxation / sourced interior | exterior suppression |
| \(W_i\) | constraint or slow vector response TBD | frame dragging |
| \(h_{ij}^{TT}\) | evolution / hyperbolic | gravitational waves |

This split is central to the covariant-parent problem.

A parent theory must allow some sectors to behave as constraints and others as dynamical degrees of freedom.

---

## Covariant / Geometric Parent Requirements

A successful parent structure must explain:

1. Why \(A_{\rm constraint}\) is long-ranged and Poisson-like.
2. Why \(A_{\rm rad}\) is absent, suppressed, absorbed, or controlled.
3. Why \(\kappa\) is suppressed in exterior but may respond inside matter.
4. How \(W_i\) arises from mass current and angular momentum.
5. How \(h_{ij}^{TT}\) propagates with plus/cross modes.
6. How sources couple to each sector.
7. What the gauge freedoms are.
8. Which variables are physical and which are coordinate shadows.
9. How the reduced sectors recombine into metric/geometric structure.

The script confirmed:

```text
parent requirements enumerated.
```

This is the real output of group 08’s first study.

---

## What This Study Established

This study established:

1. The current reduced sector bundle is coherent as an architecture.
2. \(A_{\rm constraint}\) handles static scalar mass response.
3. \(A_{\rm rad}\) is a controlled scalar-radiation hazard.
4. \(\kappa\) is a trace/interior response candidate.
5. \(W_i\) is a vector/current/frame-dragging candidate.
6. \(h_{ij}^{TT}\) is the tensor radiation channel.
7. Moving scalar wells and free scalar waves are distinct.
8. The parent theory must supply constraint/evolution split, gauge structure, source coupling, and recombination into geometry.

---

## What This Study Did Not Establish

This study did not derive a covariant parent.

It did not prove the sectors are complete.

It did not prove that the sector split is unique.

It did not derive gauge transformations.

It did not derive source couplings.

It did not derive \(W_i\) dynamics.

It did not derive \(\kappa\) matter response.

It only organized the current reduced sector bundle and identified parent requirements.

---

## Current Best Interpretation

The sector bundle is coherent as a reduced architecture:

```text
A_constraint -> static scalar mass response
A_rad        -> controlled scalar radiation hazard
kappa        -> trace/interior response
W_i          -> vector/current response
h_ij^TT      -> tensor radiation
```

Important distinction:

```text
A moving gravity well is not automatically a scalar gravity wave.
It can be a moving/retarded scalar constraint configuration tied to the source.

A free scalar breathing wave would be a separate A_rad mode and remains
controlled/unsafe unless suppressed.
```

---

## Next Development Target

The next script should be:

```text
candidate_covariant_parent_requirements.py
```

Purpose:

```text
Turn the parent requirements into explicit pass/fail criteria for any future
covariant or geometric parent theory.
```

Unlike this inventory script, the next script should be more adversarial.

It should mark requirements as:

```text
satisfied by current reduced program,
partially satisfied,
missing,
or contradiction risk.
```

This will help avoid the illusion that every passing consistency check is a proof.

---

## Summary

The sector bundle inventory begins group 08 by mapping the current reduced theory:

$$
A_{\rm constraint},\quad A_{\rm rad},\quad \kappa,\quad W_i,\quad h_{ij}^{TT}.
$$

It distinguishes a moving scalar gravity well from a scalar radiation wave.

It states the current constraint/evolution split.

It identifies what a covariant parent must explain.

The result is not a proof.

It is a map of the dragon skeleton we are trying to assemble.
