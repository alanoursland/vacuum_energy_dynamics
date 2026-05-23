# Candidate Boundary Flux Action

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full covariant action. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_boundary_flux_action.py
```

The guiding question was:

```text
Can the areal-flux law arise as a boundary/interface condition from variation
of a reduced radial action?
```

The answer is yes, in a reduced static spherical sense.

The key result is:

```text
The radial A-action exposes r²A' as the boundary momentum conjugate to A.
A source/interface coupling can fix that boundary momentum.
With the right mass normalization, this gives the areal-flux condition.
```

The areal-flux condition is:

$$4\pi R^2A'(R)=\frac{8\pi GM}{c^2}.$$

The exterior bulk equation then gives:

$$A(r)=1-\frac{2GM}{rc^2}.$$

With exterior compensation:

$$\kappa=0,$$

we get:

$$B=\frac1A.$$

Thus the exact Schwarzschild exterior metric factors are recovered in the reduced static spherical sector.

---

## Background

The exact exterior mechanics branch uses:

$$A=e^s,$$

and treats \(A\) as the exact static spherical source variable.

The exterior source-free equation is:

$$\Delta_{\rm areal}A=0,$$

where:

$$\Delta_{\rm areal}A
=
\frac1{r^2}\frac{d}{dr}(r^2A').$$

Equivalently:

$$\frac{d}{dr}(r^2A')=0.$$

Thus:

$$r^2A'=\text{constant}.$$

The areal flux is:

$$F_A=4\pi r^2A'.$$

Earlier work showed that if:

$$F_A=\frac{8\pi GM}{c^2},$$

then:

$$A=1-\frac{2GM}{rc^2}.$$

The boundary-flux action study asks whether this flux can be generated as a boundary condition from an action principle.

---

## Radial Bulk Action

Consider the reduced radial bulk action density:

$$L_{\rm bulk}=K_A r^2(A')^2.$$

The Euler-Lagrange equation is:

$$-2K_A\frac{d}{dr}(r^2A')=0.$$

Therefore:

$$\frac{d}{dr}(r^2A')=0.$$

This is the source-free areal-flux equation.

Thus the reduced bulk action already has the correct source-free exterior equation.

---

## Boundary Variation

Variation of the bulk action gives a boundary term:

$$[2K_A r^2A'\delta A]_{\partial}.$$

So the boundary momentum conjugate to \(A\) is proportional to:

$$r^2A'.$$

This is the key observation.

The areal flux is:

$$F_A=4\pi r^2A'.$$

So the same quantity that appears as the boundary momentum is the flux-carrying object.

This supports the interpretation that the source may act by setting boundary/interface flux.

---

## Source Boundary Coupling

Introduce a boundary/source coupling at \(r=R\):

$$E_{\rm boundary}=-qA(R).$$

Its variation contributes:

$$-q\delta A(R).$$

The total boundary stationarity condition is:

$$2K_AR^2A'(R)-q=0.$$

Thus:

$$A'(R)=\frac{q}{2K_AR^2}.$$

Multiply by \(4\pi R^2\):

$$F_A(R)=4\pi R^2A'(R)=\frac{2\pi q}{K_A}.$$

Therefore a boundary source fixes the areal flux.

---

## Mass Normalization

Choose the source/interface charge:

$$q_M=\frac{4K_AGM}{c^2}.$$

Then:

$$A'(R)=\frac{2GM}{R^2c^2}.$$

The areal flux becomes:

$$F_A(R)=4\pi R^2A'(R).$$

Substitute:

$$F_A(R)=4\pi R^2\frac{2GM}{R^2c^2}.$$

Thus:

$$F_A(R)=\frac{8\pi GM}{c^2}.$$

This is exactly the flux normalization needed to recover the Schwarzschild exterior coefficient.

---

## Exterior Solution from Boundary Flux

The source-free exterior bulk equation is:

$$\frac{d}{dr}(r^2A')=0.$$

The general solution is:

$$A(r)=C_0+\frac{C_1}{r}.$$

The areal flux is:

$$F_A=4\pi r^2A'=-4\pi C_1.$$

Set:

$$F_A=\frac{8\pi GM}{c^2}.$$

Then:

$$-4\pi C_1=\frac{8\pi GM}{c^2}.$$

So:

$$C_1=-\frac{2GM}{c^2}.$$

Asymptotic flatness requires:

$$C_0=1.$$

Therefore:

$$A(r)=1-\frac{2GM}{rc^2}.$$

This is the exact Schwarzschild exterior temporal factor.

---

## Coupling to Kappa Compensation

The log-scale relation is:

$$AB=e^{2\kappa}.$$

In the source-free exterior, compensation gives:

$$\kappa=0.$$

Thus:

$$AB=1.$$

Therefore:

$$B=\frac1A.$$

Using:

$$A=1-\frac{2GM}{rc^2},$$

we get:

$$B=\frac1{1-2GM/(rc^2)}.$$

So the boundary flux action plus exterior compensation recovers the exact Schwarzschild exterior metric factors.

---

## Bulk Source Versus Boundary Source

There are two equivalent reduced descriptions.

The bulk-density form is:

$$\frac{d}{dr}(4\pi r^2A')
=
4\pi r^2\frac{8\pi G}{c^2}\rho.$$

The boundary/interface form is:

$$4\pi R^2A'(R)
=
\frac{8\pi GM}{c^2}.$$

For the exterior region \(r>R\), both descriptions give the same result:

$$A=1-\frac{2GM}{rc^2}.$$

This suggests that matter can be viewed as determining the boundary flux seen by the exterior.

That is a better fit to the current mechanics than treating \(A\) as a standard curved-space harmonic scalar.

---

## What This Study Established

This study established:

1. The reduced radial bulk action:
   $$L_{\rm bulk}=K_A r^2(A')^2$$
   gives:
   $$\frac{d}{dr}(r^2A')=0.$$

2. Variation of the bulk action produces the boundary term:
   $$2K_A r^2A'\delta A.$$

3. Thus \(r^2A'\) is the boundary momentum conjugate to \(A\).

4. A boundary coupling:
   $$E_{\rm boundary}=-qA(R)$$
   fixes:
   $$2K_AR^2A'(R)=q.$$

5. With:
   $$q_M=4K_AGM/c^2,$$
   the flux is:
   $$4\pi R^2A'(R)=8\pi GM/c^2.$$

6. The exterior solution is:
   $$A=1-2GM/(rc^2).$$

7. With \(\kappa=0\):
   $$B=1/A.$$

8. The exact Schwarzschild exterior metric factors are recovered.

---

## What This Study Did Not Establish

This study did not derive a full covariant boundary action.

It did not derive the mass coupling \(q_M=4K_AGM/c^2\) from deeper principles.

It did not explain why the source couples specifically to \(A\).

It did not include pressure or stress.

It did not treat nonspherical boundaries.

It did not handle time dependence.

It did not derive Einstein's equations.

It only shows that the areal-flux law can be interpreted as a reduced boundary/interface condition.

---

## Current Best Interpretation

The current best interpretation is:

```text
The exterior A field obeys a source-free radial bulk equation.
Matter fixes the boundary momentum r²A' through a source/interface coupling.
This boundary momentum is the areal flux of A.
Mass normalization of the boundary charge gives the Schwarzschild coefficient.
```

This is a meaningful step toward a parent principle for the areal-flux law.

The central open question becomes:

```text
Why does matter couple to the boundary value of A in exactly this way?
```

---

## Next Development Targets

### 1. Boundary Flux Parent Principle

A possible next note:

```text
candidate_areal_flux_parent_principle.md
```

Purpose:

```text
Explore whether the boundary flux law can be elevated to a source/interface
principle for vacuum response.
```

### 2. Source Coupling Normalization

A possible script:

```text
candidate_source_coupling_normalization.py
```

Purpose:

```text
Ask whether q_M=4K_AGM/c² can be derived from weak-field normalization or
from matching to Newtonian mass-energy.
```

### 3. Boundary Layer Kappa Response

A possible script:

```text
candidate_boundary_kappa_relaxation_layer.py
```

Purpose:

```text
Test whether interior kappa response can relax to exterior kappa=0 through
a boundary/interface layer.
```

---

## Summary

The boundary flux action study provides a reduced variational route to the areal-flux law.

The radial bulk action gives source-free flux conservation:

$$\frac{d}{dr}(r^2A')=0.$$

The boundary variation exposes:

$$r^2A'$$

as the momentum conjugate to \(A\).

A source boundary coupling:

$$E_{\rm boundary}=-qA(R)$$

fixes that momentum.

With:

$$q_M=\frac{4K_AGM}{c^2},$$

the boundary condition becomes:

$$4\pi R^2A'(R)=\frac{8\pi GM}{c^2}.$$

The exterior solution is:

$$A=1-\frac{2GM}{rc^2}.$$

With \(\kappa=0\):

$$B=\frac1A.$$

Thus the exact Schwarzschild exterior metric factors are recovered in the reduced static spherical sector.

The open problem is to derive the boundary coupling and its normalization from a deeper physical principle.
