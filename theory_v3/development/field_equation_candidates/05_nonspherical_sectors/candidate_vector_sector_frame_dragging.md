# Candidate Vector Sector Frame Dragging

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or derived frame-dragging theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_sector_frame_dragging.py
```

The guiding question was:

```text
Can the scalar A branch reproduce frame dragging, or does the theory require
a separate vector sector?
```

The answer is:

```text
The scalar A branch cannot reproduce frame dragging.
A separate weak vector sector is required.
```

The source-channel split is now:

```text
mass / density -> scalar A-flux
trace / pressure -> kappa interior response
angular momentum / mass current -> vector W_i
```

This is a useful result because it keeps the scalar branch from being overclaimed.

---

## Background

The current scalar sector has:

$$A=1+\frac{2\Phi}{c^2},$$

and first-order reciprocal spatial compensation:

$$B=\frac1A\approx1-\frac{2\Phi}{c^2}.$$

This reproduces the weak scalar metric sector and a \(\gamma=1\) proxy.

However, rotating sources require off-diagonal metric components:

$$g_{ti}\neq0.$$

These are frame-dragging or gravitomagnetic components.

Scalar \(A\) and reduced \(\kappa\) do not generate such components.

The vector-sector study asked what kind of additional mode is required.

---

## Scalar Metric Has No Vector Components

The weak scalar metric branch has:

$$h_{ti}=0.$$

The script represented this as:

$$h_{ti}=(0,0,0).$$

Therefore scalar \(A\) cannot represent frame dragging.

This was the first key result:

```text
scalar sector has zero vector components.
```

So frame dragging cannot be hidden inside \(A\), \(s\), or exterior reciprocal compensation.

It needs its own sector.

---

## Introducing a Vector Potential

The script introduced a candidate vector sector:

$$W_i=(W_x,W_y,W_z).$$

This vector would appear in the off-diagonal metric components:

$$g_{ti}.$$

The interpretation is:

```text
W_i is independent of scalar A.
It should be sourced by mass current or angular momentum.
```

This is analogous to the way electromagnetic magnetism requires a vector potential, while electrostatics can be represented by a scalar potential.

The theory is not yet deriving \(W_i\); it is identifying that such a sector is necessary.

---

## Angular Momentum Source

A rotating source is characterized by angular momentum:

$$\vec J=(J_x,J_y,J_z).$$

The source-channel split becomes:

```text
density / mass -> scalar A
mass current / spin -> vector W_i
```

This is important because the scalar \(A\)-flux is controlled by mass:

$$F_A=\frac{8\pi GM}{c^2}.$$

But frame dragging should be controlled by angular momentum, not by scalar mass alone.

Thus \(M\) and \(\vec J\) must source different sectors.

---

## Dipole-Like Exterior Vector Potential

For angular momentum along the \(z\)-axis:

$$\vec J=J\hat z.$$

The cross product is:

$$\vec J\times\vec r=(-Jy,Jx,0).$$

The script tested a dipole-like exterior vector potential:

$$
\vec W
=
\frac{\vec J\times\vec r}{r^3}.
$$

In Cartesian components:

$$
\vec W
=
\left(
-\frac{Jy}{(x^2+y^2+z^2)^{3/2}},
\frac{Jx}{(x^2+y^2+z^2)^{3/2}},
0
\right).
$$

The curl is nonzero:

$$
\nabla\times\vec W
=
\left(
\frac{3Jxz}{r^5},
\frac{3Jyz}{r^5},
\frac{J(-x^2-y^2+2z^2)}{r^5}
\right).
$$

This confirms that a dipole-like vector potential can carry a frame-dragging-like field.

The script did not set the physical normalization. It only confirmed the correct structural kind of object.

---

## Vector Sector Does Not Alter Scalar A-Flux Directly

The script emphasized that the vector sector should not be confused with scalar \(A\)-flux.

Scalar \(A\)-flux is:

$$F_A=\int \nabla A\cdot d\vec S.$$

This is sourced by mass.

The vector sector is encoded in \(g_{ti}\)-like components and should be sourced by mass current or angular momentum.

Thus:

$$M\rightarrow A\text{-flux},$$

and:

$$\vec J\rightarrow W_i.$$

This separation prevents rotating-source physics from contaminating the scalar mass-flux law.

---

## Candidate Weak Vector Equation

A minimal weak vector-sector placeholder is:

$$\nabla^2 W_i=\text{source}_i.$$

The source should be related to mass current density.

In a source-free exterior:

$$\nabla^2W_i=0.$$

A rotating compact source would produce dipole-like \(W_i\) terms.

This is only a placeholder. The following remain open:

```text
normalization,
gauge structure,
source definition,
covariant parent,
relationship to standard gravitomagnetism.
```

---

## Vector-Sector Targets

A viable vector sector should eventually reproduce:

1. weak gravitomagnetic effects,
2. frame dragging by rotating bodies,
3. correct angular-momentum falloff,
4. no contamination of scalar mass flux,
5. gauge-aware treatment of vector potentials,
6. coupling to moving matter or mass current.

This gives the next benchmark list for the vector branch.

---

## What This Study Established

This study established:

1. Scalar \(A\) has no \(g_{ti}\) components.
2. Frame dragging requires an independent vector sector.
3. Mass \(M\) should source scalar \(A\)-flux.
4. Angular momentum or mass current should source vector \(W_i\).
5. A dipole-like exterior vector potential has nonzero curl.
6. A weak vector Poisson/Laplace class is a plausible first placeholder.
7. Normalization, gauge structure, and covariant parent remain open.

---

## What This Study Did Not Establish

This study did not derive the frame-dragging field equation.

It did not reproduce the Lense-Thirring metric.

It did not fix numerical normalization.

It did not derive a vector source from stress-energy.

It did not define vector gauge freedom.

It did not produce a covariant parent.

It only established that the scalar branch cannot do the vector job and that a separate vector sector is structurally necessary.

---

## Current Best Interpretation

The current best interpretation is:

```text
The scalar A branch carries mass-density/Newtonian potential physics.

The kappa branch may carry traceful interior matter response.

The vector branch must carry mass-current/angular-momentum physics.
```

This gives a cleaner sector map:

$$\rho \rightarrow A,$$

$$p,T^\mu{}_\mu\rightarrow \kappa,$$

$$T^{0i},\vec J\rightarrow W_i.$$

The exact source mappings are still future work.

---

## Next Development Targets

### 1. Vector Normalization Test

A possible script:

```text
candidate_vector_sector_normalization.py
```

Purpose:

```text
Match the weak vector potential to the known frame-dragging/Lense-Thirring
scaling and identify the required normalization.
```

### 2. Vector Gauge Structure

A possible script:

```text
candidate_vector_gauge_structure.py
```

Purpose:

```text
Identify gauge freedoms in W_i and separate physical curl-like content from
pure-gradient modes.
```

### 3. Wave Sector

A direct next script:

```text
candidate_wave_sector_linearized_modes.py
```

Purpose:

```text
Ask whether the theory has, lacks, or must add transverse-traceless tensor
wave modes.
```

---

## Summary

The vector-sector frame-dragging study establishes a necessary missing sector.

Scalar \(A\) cannot produce:

$$g_{ti}\neq0.$$

Frame dragging requires a new vector mode:

$$W_i.$$

Mass sources scalar \(A\)-flux, while angular momentum or mass current should source \(W_i\).

A dipole-like exterior vector potential:

$$\vec W\sim\frac{\vec J\times\vec r}{r^3}$$

has nonzero curl and is structurally appropriate for frame-dragging-like behavior.

But normalization, gauge structure, and the covariant parent remain open.
