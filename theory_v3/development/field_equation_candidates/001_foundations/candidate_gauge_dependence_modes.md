# Candidate Gauge-Dependence Modes

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or full covariant field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_gauge_dependence_modes.py
```

The guiding question was:

```text
How do the reduced log-scale modes kappa and s behave under radial
coordinate changes?  Are they coordinate-invariant scalar fields?
```

The answer is no.

Under a radial reparameterization \(r = f(R)\), the naive reduced modes shift:

$$\kappa \rightarrow \kappa + \ln f'(R),$$

and:

$$s \rightarrow s - \ln f'(R).$$

Therefore \(\kappa\) and \(s\) are not coordinate-invariant scalar fields. They are reduced variables that depend on the radial gauge choice.

---

## Background

The reduced exterior program uses the static spherical areal-gauge metric:

$$ds^2 = -A(r)c^2dt^2 + B(r)dr^2 + r^2 d\Omega^2.$$

The log-scale variables are:

$$a = \ln A,$$

and:

$$b = \ln B.$$

Then:

$$\kappa = \frac{a+b}{2},$$

and:

$$s = \frac{a-b}{2}.$$

The exterior compensation condition is:

$$\kappa = 0 \quad \Longleftrightarrow \quad AB = 1.$$

The question addressed here is whether this compensation condition, and the modes themselves, survive under radial coordinate changes.

---

## General Radial Reparameterization

Consider a general radial reparameterization:

$$r = f(R).$$

The transformed metric coefficients are:

$$A_{\rm new}(R) = A(f(R)),$$

and:

$$B_{\rm new}(R) = B(f(R))[f'(R)]^2.$$

The angular sector becomes:

$$f(R)^2 d\Omega^2.$$

In log-scale variables:

$$a_{\rm new} = a(f(R)),$$

and:

$$b_{\rm new} = b(f(R)) + 2\ln f'(R).$$

The naive reduced modes become:

$$\kappa_{\rm new} = \kappa(f(R)) + \ln f'(R),$$

and:

$$s_{\rm new} = s(f(R)) - \ln f'(R).$$

The shifts are:

$$\delta\kappa = +\ln f'(R),$$

and:

$$\delta s = -\ln f'(R).$$

These are equal and opposite. The sum \(\kappa + s = a\) is invariant (temporal coefficient does not change), but the individual modes shift.

---

## Scaling Reparameterization

For the special case of a constant scaling:

$$r = \lambda R,$$

the shifts become:

$$\delta\kappa = \ln\lambda,$$

and:

$$\delta s = -\ln\lambda.$$

This confirms that even a simple rescaling of the radial coordinate shifts the naive reduced modes.

---

## Infinitesimal Radial Shift

For an infinitesimal radial perturbation:

$$r = R + \epsilon\,\xi(R),$$

the Jacobian is:

$$f'(R) = 1 + \epsilon\,\xi'(R).$$

To first order:

$$\delta\kappa = \epsilon\,\xi'(R),$$

and:

$$\delta s = -\epsilon\,\xi'(R).$$

Even an infinitesimal coordinate change shifts the naive reduced modes.

---

## Reciprocal Scaling Gauge Warning

Start with an areal-gauge compensated sector:

$$A(r) = e^{s(r)}, \quad B(r) = e^{-s(r)}, \quad AB = 1.$$

After the reparameterization \(r = f(R)\):

$$A_{\rm new} = e^{s(f(R))},$$

$$B_{\rm new} = e^{-s(f(R))}[f'(R)]^2.$$

The naive product is:

$$A_{\rm new} B_{\rm new} = [f'(R)]^2.$$

This falsely appears as though reciprocal compensation has failed. The geometry has not changed; only the gauge representation has changed.

---

## Full Determinant Behavior

The full four-dimensional volume element transforms correctly under coordinate change. The apparent shift in \(\kappa\) is a reduced temporal-radial-sector effect caused by leaving areal gauge, not a physical change in the metric.

The full determinant magnitude is:

$$\sqrt{|g_{\rm new}|} = f(R)^2 \sin\theta \cdot f'(R),$$

which includes the correct radial Jacobian factor.

---

## Restoring Areal Gauge

The areal radius is defined geometrically by the area of symmetry spheres:

$$\text{Area} = 4\pi r_{\rm areal}^2.$$

After a radial reparameterization \(r = f(R)\), the angular sector is \(f(R)^2 d\Omega^2\), so the areal radius is \(r_{\rm areal} = f(R)\).

If we restore areal gauge by using \(r_{\rm areal}\) as the radial coordinate, the metric returns to its original areal-gauge form, and the original reduced \(\kappa\) and \(s\) are recovered.

This shows that \(\kappa\) and \(s\) are meaningful only after the reduced gauge has been specified.

---

## What This Study Established

This study established:

1. Under \(r = f(R)\), naive reduced modes shift:
   $$\kappa_{\rm new} = \kappa_{\rm old} + \ln f',$$
   $$s_{\rm new} = s_{\rm old} - \ln f'.$$
2. Therefore \(\kappa\) and \(s\) are not coordinate-invariant scalars.
3. \(AB = 1\) is a reduced areal-gauge condition. After radial reparameterization, naive \(A_{\rm new} B_{\rm new} = [f']^2\).
4. The full determinant and volume element transform correctly. The apparent \(\kappa\) shift is a gauge representation effect.
5. Restoring areal gauge recovers the original reduced modes.
6. To use \(\kappa\) and \(s\) physically, the theory must either:
   - fix a gauge, such as areal-radius gauge, or
   - identify covariant or gauge-aware parent quantities.

---

## What This Study Did Not Establish

This study did not produce a gauge-invariant definition of \(\kappa\) or \(s\).

It did not identify a covariant parent structure.

It did not handle non-radial coordinate changes.

It did not address time-dependent or non-spherical geometries.

It only characterized the gauge sensitivity of the reduced modes under radial reparameterization.

---

## Relationship to the Log-Scale Modes Study

The log-scale modes study introduced \(\kappa\) and \(s\) as reduced variables in areal gauge. This gauge-dependence study shows that those variables are tied to that gauge choice. Without fixing the areal gauge, the modes shift by the radial Jacobian.

---

## Relationship to the Covariant Parent Modes Study

The covariant parent modes study interprets \(\kappa\) as a trace-like mode and \(s\) as a shear-like mode. This gauge-dependence study provides the motivation for that interpretation: since the naive modes are gauge-dependent, a more geometric or covariant parent structure is needed.

---

## Relationship to the Areal-Gauge Kappa Condition Study

The areal-gauge kappa condition study builds directly on this result. It shows that the gauge artifact can be absorbed by including the angular-radius function \(S(R)\) when expressing the compensation condition in arbitrary coordinates:

$$T(R)Q(R) = [S'(R)]^2.$$

This removes the false Jacobian artifact identified here.

---

## Development Implication

The key implication is:

```text
Do not treat kappa or s as invariant fields yet.
Treat them as reduced variables extracted after symmetry and gauge choice.
```

The next theoretical task is to find a gauge-aware or covariant parent structure whose static spherical areal-gauge reduction gives \(\kappa\) and \(s\).

---

## Summary

The gauge-dependence mode study confirms the main danger:

$$\kappa \text{ and } s \text{ are clean reduced variables, but they are gauge-sensitive.}$$

A radial coordinate change \(r = f(R)\) shifts the naive temporal-radial log modes by \(\ln f'\):

$$\kappa \rightarrow \kappa + \ln f',$$

and:

$$s \rightarrow s - \ln f'.$$

Therefore:

$$\kappa = 0 \text{ and } AB = 1$$

should be understood as areal-gauge reduced exterior statements, not coordinate-invariant scalar equations by themselves.

The full geometry is unchanged. Only the reduced representation shifts.

This motivates the search for gauge-aware or covariant parent structures in subsequent studies.
