# Radiative TT Averaging Lift

## Statement

In a local inertial patch, let the radiative perturbation be transverse
and traceless:

$$
h^{TT}_{ij}=A_{ij}(U,\mathbf x)\,p(\theta),
$$

where \(\theta\) is the fast phase and \(U\) denotes slow variables.
Let the wavelength be \(\lambda\), the background/envelope scale be
\(L\), and choose an averaging cell \(\ell_{\rm avg}\) such that

$$
\lambda \ll \ell_{\rm avg} \ll L.
$$

Then, to leading short-wave order,

$$
\boxed{
<t_{ab}> =
{c^4\over 32\pi G}
<\partial_a h^{TT}_{ij}\partial_b h^{TT}_{ij}>
}
$$

with corrections suppressed by powers of \(\lambda/L\). For a retarded
wave this averaged stress is positive and null-transported.

## Averaging Rules

The cell average over the fast phase is

$$
<F>={1\over 2\pi}\int_0^{2\pi}F(\theta)\,d\theta .
$$

For periodic carriers,

$$
<\sin\theta>=<\cos\theta>=<\sin\theta\cos\theta>=0,
$$

and

$$
<\sin^2\theta>=<\cos^2\theta>={1\over2}.
$$

Any fast total derivative averages to zero:

$$
<\partial_\theta P(\theta)> = 0
$$

for periodic \(P\). This is the local version of discarding fast
boundary terms inside an averaging cell.

## Scale-Separated Derivative Product

Write

$$
h=A(U)\cos\theta.
$$

For any derivative direction \(a\),

$$
\partial_a h = k_a\partial_\theta h + e_a\partial_U h
= -k_a A\sin\theta + e_a A_U\cos\theta .
$$

Therefore

$$
<\partial_a h\,\partial_b h>
= {1\over2}k_a k_b A^2
+ {1\over2}e_a e_b A_U^2 .
$$

The mixed term is proportional to \(<\sin\theta\cos\theta>\) and
vanishes exactly. Since \(k\sim1/\lambda\) and \(e A_U/A\sim1/L\), the
slow-envelope term is smaller than the fast term by \(O((\lambda/L)^2)\)
when the envelope is nonzero. Thus the leading averaged stress is the
fast derivative product used by the radiative bootstrap.

## Retarded TT Wave Check

For

$$
h_+ = A\cos\omega(t-z/c),\qquad
h_\times = B\sin\omega(t-z/c),
$$

the averaged derivative contractions are

$$
<\dot h_{ij}\dot h_{ij}>
= \omega^2(A^2+B^2),
$$

up to the conventional polarization counting already fixed in 008. The
mixed \(t,z\) and \(z,z\) products obey

$$
c<\partial_t h_{ij}\partial_z h_{ij}>
=-<\partial_t h_{ij}\partial_t h_{ij}>,
$$

and

$$
c^2<\partial_z h_{ij}\partial_z h_{ij}>
=<\partial_t h_{ij}\partial_t h_{ij}>.
$$

So the averaged stress is transported on the null direction of the wave.

## What This Retires

This retires the Isaacson averaging portion of the covariant-lift debt:
secular/oscillatory terms, total fast derivatives, and envelope
suppression are now stated and forge-checked.

It does not retire the separate gauge-invariance obligation for
averaged \(<t_{ab}>\). That should be handled as the next targeted
radiative lift.

