# Candidate Source Coupling Normalization

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or derivation from first principles. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_source_coupling_normalization.py
```

The guiding question was:

```text
Is the boundary/source charge normalization arbitrary, or is it fixed by
weak-field Newtonian and Schwarzschild matching?
```

The answer is:

```text
The normalization is fixed at the reduced matching level.
It is not yet derived from deeper physics.
```

The boundary action uses:

$$E_{\rm boundary}=-qA(R).$$

The boundary condition from variation is:

$$2K_AR^2A'(R)=q.$$

The areal flux is:

$$F_A=4\pi R^2A'(R).$$

Therefore:

$$F_A=\frac{2\pi q}{K_A}.$$

Newtonian and Schwarzschild matching require:

$$F_A=\frac{8\pi GM}{c^2}.$$

Therefore:

$$q_M=\frac{4K_AGM}{c^2}.$$

---

## Background

The boundary flux action study showed that the reduced radial bulk action:

$$L_{\rm bulk}=K_A r^2(A')^2$$

has boundary variation:

$$2K_Ar^2A'\delta A.$$

Thus:

$$r^2A'$$

is the boundary momentum conjugate to \(A\).

A source/interface coupling:

$$E_{\rm boundary}=-qA(R)$$

contributes:

$$-q\delta A(R).$$

Boundary stationarity gives:

$$2K_AR^2A'(R)-q=0.$$

Thus:

$$A'(R)=\frac{q}{2K_AR^2}.$$

Multiply by \(4\pi R^2\):

$$F_A=4\pi R^2A'(R)=\frac{2\pi q}{K_A}.$$

So the boundary charge \(q\) fixes the exterior \(A\)-flux.

---

## Newtonian Matching

For a conserved exterior flux:

$$F_A=F,$$

we have:

$$4\pi r^2A'=F.$$

Thus:

$$A'=\frac{F}{4\pi r^2}.$$

With asymptotic flatness:

$$A(\infty)=1,$$

integration gives:

$$A(r)=1-\frac{F}{4\pi r}.$$

The weak-field Newtonian metric requires:

$$A(r)=1+\frac{2\Phi}{c^2}.$$

For:

$$\Phi=-\frac{GM}{r},$$

this gives:

$$A(r)=1-\frac{2GM}{c^2r}.$$

Match:

$$1-\frac{F}{4\pi r}
=
1-\frac{2GM}{c^2r}.$$

Therefore:

$$F=\frac{8\pi GM}{c^2}.$$

So the exterior flux normalization is fixed by Newtonian matching.

---

## Boundary Charge from Flux

The boundary relation is:

$$F_A=\frac{2\pi q}{K_A}.$$

Using:

$$F_A=\frac{8\pi GM}{c^2},$$

we get:

$$\frac{2\pi q}{K_A}=\frac{8\pi GM}{c^2}.$$

Solve for \(q\):

$$q=\frac{4K_AGM}{c^2}.$$

Thus:

$$q_M=\frac{4K_AGM}{c^2}.$$

This is the required boundary/source charge normalization.

---

## Schwarzschild Radius Matching

The exterior Schwarzschild-form temporal factor is:

$$A=1-\frac{r_s}{r}.$$

Then:

$$A'=\frac{r_s}{r^2}.$$

The areal flux is:

$$F_A=4\pi r^2A'=4\pi r_s.$$

Set:

$$F_A=\frac{8\pi GM}{c^2}.$$

Then:

$$4\pi r_s=\frac{8\pi GM}{c^2}.$$

Therefore:

$$r_s=\frac{2GM}{c^2}.$$

So the same flux normalization fixes the Schwarzschild radius coefficient.

---

## Additivity in Mass

The boundary charge is:

$$q_M=\frac{4K_AGM}{c^2}.$$

For two masses \(M_1\) and \(M_2\):

$$q(M_1+M_2)=\frac{4K_AG(M_1+M_2)}{c^2}.$$

Also:

$$q(M_1)+q(M_2)=\frac{4K_AGM_1}{c^2}+\frac{4K_AGM_2}{c^2}.$$

Therefore:

$$q(M_1+M_2)=q(M_1)+q(M_2).$$

Similarly:

$$F(M_1+M_2)=F(M_1)+F(M_2).$$

Thus the boundary charge and areal flux are additive in mass.

This is necessary for a Gauss-law-like source interpretation.

---

## Energy Coupling Interpretation

The boundary coupling is:

$$E_{\rm boundary}=-q_M A(R).$$

Using:

$$q_M=\frac{4K_AGM}{c^2},$$

we get:

$$E_{\rm boundary}
=
-\frac{4K_AGM}{c^2}A(R).
$$

Interpretation:

```text
q_M has the length-like mass coupling GM/c^2 multiplied by the reduced
stiffness K_A.
```

The coefficient is fixed by Newtonian/Schwarzschild matching.

However, \(K_A\) remains a reduced stiffness or normalization parameter.

---

## What This Study Established

This study established:

1. The boundary relation is:
   $$2K_AR^2A'(R)=q.$$

2. The areal flux is:
   $$F_A=4\pi R^2A'(R).$$

3. Therefore:
   $$F_A=\frac{2\pi q}{K_A}.$$

4. Newtonian matching requires:
   $$F_A=\frac{8\pi GM}{c^2}.$$

5. Therefore:
   $$q_M=\frac{4K_AGM}{c^2}.$$

6. The same flux fixes:
   $$r_s=\frac{2GM}{c^2}.$$

7. The charge is additive in mass.

8. The normalization is not arbitrary once the weak-field limit is imposed.

---

## What This Study Did Not Establish

This study did not derive \(K_A\) from vacuum microphysics.

It did not prove why matter couples to \(A\).

It did not prove why the boundary action has exactly the form:

$$E_{\rm boundary}=-qA(R).$$

It did not include pressure/stress modifications.

It did not produce a full covariant source action.

It did not derive the coupling from P1-P3 or deeper ontology.

It only fixed the coefficient at the reduced matching level.

---

## Current Best Interpretation

The current best interpretation is:

```text
The boundary/source charge normalization is not free once Newtonian matching
is required.

But the coupling itself is not yet fundamental.

The reduced model explains which coefficient is needed; the future theory
must explain why the source action has that form.
```

The important distinction is:

```text
matched normalization: achieved
first-principles derivation: still open
```

---

## Relationship to the Boundary Flux Action

The boundary flux action found that a source/interface term can fix the areal flux.

This normalization study shows that the charge in that term must be:

$$q_M=\frac{4K_AGM}{c^2}.$$

Then:

$$F_A=\frac{8\pi GM}{c^2}.$$

And the exterior solution becomes:

$$A=1-\frac{2GM}{rc^2}.$$

With:

$$\kappa=0,$$

we get:

$$B=\frac1A.$$

Thus the source coupling normalization closes the reduced matching loop.

---

## Next Development Targets

### 1. Derive the Boundary Coupling

A possible note:

```text
candidate_boundary_source_coupling_origin.md
```

Purpose:

```text
Ask why matter should couple to A(R) through -qA(R).
```

### 2. Derive or Interpret K_A

A possible script:

```text
candidate_A_stiffness_normalization.py
```

Purpose:

```text
Explore whether K_A can be absorbed, normalized, or connected to a vacuum
stiffness parameter.
```

### 3. Pressure/Stress Modification

A possible script:

```text
candidate_pressure_boundary_charge_extension.py
```

Purpose:

```text
Ask whether pressure/stress modifies q, modifies kappa, or remains purely
interior.
```

---

## Summary

The source coupling normalization study shows that the boundary charge is fixed by weak-field matching.

The radial boundary condition is:

$$2K_AR^2A'(R)=q.$$

The areal flux is:

$$F_A=\frac{2\pi q}{K_A}.$$

Newtonian matching requires:

$$F_A=\frac{8\pi GM}{c^2}.$$

Therefore:

$$q_M=\frac{4K_AGM}{c^2}.$$

This normalization also gives:

$$r_s=\frac{2GM}{c^2}.$$

So the coefficient is not arbitrary at the reduced matching level.

The remaining open question is why the source/interface coupling has the form:

$$E_{\rm boundary}=-qA(R).$$
