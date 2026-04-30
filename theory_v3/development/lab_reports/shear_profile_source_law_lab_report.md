# Lab Report: Candidate Shear Profile Source Law

## Experiment

**Script:** `candidate_shear_profile_source_law.py`  
**Experiment type:** Reduced-sector symbolic source-law test  
**Status:** Exploratory / pedagogical, not formal theory  
**Development unit:** Shear/source-law problem

## Purpose

The purpose of this experiment was to begin the next development unit after the log-scale and \(\kappa\)-suppression studies.

The previous unit established the reduced exterior compensation condition:

$$\kappa=0.$$

With the log-scale definitions:

$$a=\ln A,$$

$$b=\ln B,$$

$$\kappa=\frac{a+b}{2},$$

and:

$$s=\frac{a-b}{2},$$

we have:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Therefore:

$$AB=e^{2\kappa}.$$

So when:

$$\kappa=0,$$

we get:

$$A=e^s,$$

$$B=e^{-s},$$

and:

$$AB=1.$$

The \(\kappa\)-suppression studies showed how reciprocal scaling can be maintained while a compensated/shear mode remains active. This experiment asks the next question:

```text
Given kappa = 0 in the source-free exterior, what equation and source/interface condition give the correct exterior shear profile s(r)?
```

The target weak-field profile is:

$$s(r)=-\frac{2GM}{rc^2}.$$

This gives:

$$A=e^s\approx 1-\frac{2GM}{rc^2},$$

and:

$$B=e^{-s}\approx 1+\frac{2GM}{rc^2},$$

while preserving:

$$AB=1.$$

## Hypothesis

The toy source-law hypothesis tested here is:

```text
In the static source-free exterior, the shear mode s obeys a radial Laplace equation.
```

That is:

$$\nabla^2s=0$$

outside the source.

In spherical symmetry:

$$\nabla^2s=\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{ds}{dr}\right).$$

The expected general exterior solution is:

$$s(r)=C_1+\frac{C_2}{r}.$$

Asymptotic flatness should set:

$$C_1=0.$$

A mass/interface flux condition should then fix:

$$C_2=-\frac{2GM}{c^2}.$$

The chosen flux normalization was:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}.$$

This should produce:

$$s(r)=-\frac{2GM}{rc^2}.$$

## Results

### Case 0: Convention Check

The script verified the log-scale convention.

Starting from:

$$a=\kappa+s,$$

and:

$$b=\kappa-s,$$

the metric factors are:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

The product is:

$$AB=e^{2\kappa}.$$

Setting \(\kappa=0\) gives:

$$A=e^s,$$

$$B=e^{-s},$$

and:

$$AB=1.$$

All convention checks passed.

### Case 1: Source-Free Radial Laplace Equation

The source-free radial equation was:

$$\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{ds}{dr}\right)=0.$$

SymPy solved this as:

$$s(r)=C_1+\frac{C_2}{r}.$$

The script also directly checked that:

$$s(r)=C_1+\frac{C_2}{r}$$

satisfies:

$$\nabla^2s=0.$$

This passed.

### Case 2: Mass/Interface Flux Fixes the Coefficient

The script used:

$$s(r)=\frac{C}{r}.$$

Then:

$$s'(r)=-\frac{C}{r^2}.$$

So:

$$4\pi r^2s'(r)=-4\pi C.$$

The target mass/interface flux was:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}.$$

Solving:

$$-4\pi C=\frac{8\pi GM}{c^2}$$

gave:

$$C=-\frac{2GM}{c^2}.$$

Therefore:

$$s(r)=-\frac{2GM}{rc^2}.$$

The script confirmed that this fixed solution has the desired flux:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}.$$

This passed after correcting the symbolic assumption on \(C\), which must be allowed to take a negative value.

### Case 3: Weak-Field Metric Recovery from the Shear Profile

The script introduced the small parameter:

$$\epsilon=\frac{GM}{rc^2}.$$

With:

$$s=-2\epsilon,$$

the metric factors are:

$$A=e^s=e^{-2\epsilon},$$

and:

$$B=e^{-s}=e^{2\epsilon}.$$

The expansions were:

$$A=1-2\epsilon+2\epsilon^2+\cdots,$$

and:

$$B=1+2\epsilon+2\epsilon^2+\cdots.$$

The product remained:

$$AB=1$$

exactly.

Thus, to first order:

$$A\approx1-\frac{2GM}{rc^2},$$

and:

$$B\approx1+\frac{2GM}{rc^2}.$$

This matches the desired weak-field exterior behavior in the reduced compensated sector.

### Case 4: Poisson Source Form and Sign Check

The script checked the distributional sign convention.

Using:

$$\nabla^2\left(\frac{1}{r}\right)=-4\pi\delta^3(r),$$

and:

$$s=-\frac{2GM}{c^2r},$$

we get:

$$\nabla^2s=\frac{8\pi GM}{c^2}\delta^3(r).$$

For a mass density \(\rho\), the corresponding reduced Poisson form is:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

Outside the source:

$$\rho=0,$$

so:

$$\nabla^2s=0.$$

The script directly verified that:

$$s(r)=-\frac{2GM}{rc^2}$$

is harmonic for \(r>0\).

This passed.

### Case 5: Failure Controls

The script included two failure controls.

The first was the asymptotic constant. The general harmonic solution is:

$$s(r)=C_0+\frac{C_1}{r}.$$

If:

$$C_0\neq0,$$

then \(s(r)\) does not vanish at infinity, so asymptotic flatness fails.

Therefore:

$$C_0=0.$$

The second failure control tested the coefficient. If:

$$s=-\lambda\epsilon,$$

then:

$$A=e^{-\lambda\epsilon}\approx1-\lambda\epsilon.$$

The weak-field temporal target requires:

$$\lambda=2.$$

The script solved this and found:

$$\lambda=2.$$

Both failure controls passed.

## Main Result

The experiment established the following reduced exterior chain:

$$\kappa=0$$

implies:

$$A=e^s,$$

$$B=e^{-s},$$

and:

$$AB=1.$$

If the source-free exterior shear mode satisfies:

$$\nabla^2s=0,$$

then spherical symmetry gives:

$$s(r)=C_0+\frac{C_1}{r}.$$

Asymptotic flatness gives:

$$C_0=0.$$

The mass/interface flux condition:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}$$

fixes:

$$C_1=-\frac{2GM}{c^2}.$$

Therefore:

$$s(r)=-\frac{2GM}{rc^2}.$$

This recovers the weak-field exterior metric behavior:

$$A=e^s\approx1-\frac{2GM}{rc^2},$$

$$B=e^{-s}\approx1+\frac{2GM}{rc^2},$$

with:

$$AB=1$$

exactly.

## Interpretation

This experiment successfully begins the shear/source-law unit.

The previous unit answered:

```text
How can reciprocal scaling survive while exterior distortion remains active?
```

Answer:

```text
Suppress kappa, let s carry the compensated exterior distortion.
```

This experiment answers the next reduced question:

```text
If s obeys a Laplace/Poisson-type source law, does the correct weak-field exterior profile follow?
```

Answer:

```text
Yes.
```

The reduced equation:

$$\nabla^2s=0$$

outside the source gives the correct \(1/r\) shape.

The mass/interface flux normalization:

$$4\pi r^2s'(r)=\frac{8\pi GM}{c^2}$$

fixes the coefficient.

Together they produce:

$$s(r)=-\frac{2GM}{rc^2}.$$

This gives the expected weak-field metric coefficients while preserving reciprocal scaling.

## What Was Established

This study established:

1. The log-scale convention remains consistent: \(\kappa=0\) gives \(A=e^s\), \(B=e^{-s}\), and \(AB=1\).
2. A source-free radial Laplace equation gives \(s(r)=C_1+C_2/r\).
3. Asymptotic flatness removes the constant term.
4. A mass/interface flux condition fixes \(C_2=-2GM/c^2\).
5. The resulting shear profile is \(s(r)=-2GM/(rc^2)\).
6. This profile recovers the weak-field temporal and radial metric coefficients to first order.
7. \(AB=1\) remains exact in the reduced compensated sector.
8. The source sign convention is consistent with \(\nabla^2s=8\pi G\rho/c^2\).

## What Was Not Established

This study did not derive the shear equation from a deeper vacuum configuration-energy functional.

It did not derive the mass/interface flux condition from first principles.

It did not derive why the normalization is:

$$\frac{8\pi GM}{c^2}.$$

It did not derive a covariant field equation.

It did not identify the covariant parent of the reduced shear mode \(s\).

It did not address strong fields, rotating sources, time-dependent fields, gravitational waves, cosmology, or interior mass structure.

Therefore, this remains a reduced-sector source-law toy.

## Relationship to the Larger Framework

The result fits naturally after the log-scale and \(\kappa\)-suppression conclusions.

That prior unit established:

$$\kappa=0,\qquad s\neq0$$

as the reduced P7-style exterior structure.

This study then supplies a candidate reduced source law for \(s\):

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

Outside the source:

$$\nabla^2s=0.$$

For a localized mass \(M\), the exterior solution is:

$$s(r)=-\frac{2GM}{rc^2}.$$

This is the expected weak-field shear profile.

## Next Theoretical Target

The next theoretical target is to explain why the reduced shear equation and flux law should hold.

In compact form, the question is:

```text
What vacuum configuration-energy functional or source/interface rule produces
∇²s = 8πG rho / c²
while preserving kappa = 0 in the source-free exterior?
```

Equivalently:

```text
Why does mass impose the shear flux
4πr²s'(r)=8πGM/c²?
```

A future development note should explore whether this flux arises from mass-as-constraint, vacuum burden, interface smoothing, or a variational boundary condition.

## Conclusion

The candidate shear profile source-law toy passed.

It shows that once the source-free exterior is restricted to the compensated sector:

$$\kappa=0,$$

a simple Laplace/Poisson law for the shear mode \(s\) produces the desired weak-field profile:

$$s(r)=-\frac{2GM}{rc^2}.$$

This gives:

$$A=e^s\approx1-\frac{2GM}{rc^2},$$

and:

$$B=e^{-s}\approx1+\frac{2GM}{rc^2},$$

with:

$$AB=1.$$

The result is not yet a derivation of the full field equation. It is a successful reduced-sector source-law check.

The next step is to explain the origin of the shear equation and the mass/interface flux normalization from the deeper vacuum framework.
