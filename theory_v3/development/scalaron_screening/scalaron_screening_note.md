# Scalaron Screening Does Not Rescue the Scalaron Under P7'

## Status

This note discharges the scalaron screening objection to the E3 kill.
It does not reopen the admitted equations.

The admitted chain remains:

```text
G20:
  ghost safety leaves only a R^2 + Gauss-Bonnet at <= 4 derivatives

E3:
  a != 0 -> mandatory scalaron hair around static sources
  scalaron hair -> AB != 1 / preferred static t-r frame
  P7' forbids that static vacuum structure
  therefore a = 0
```

The question addressed here is whether screening can rescue \(a \neq 0\)
without appealing P7'.

It cannot.

## Screening Versus P7'

Screening can change observational visibility. It can make a scalar
profile short-ranged, small, environment-dependent, or hard to detect.

P7' is not a detectability bound. It is an exact static-frame-
indifference condition: a strictly static vacuum configuration carries
no preferred frame in the \(t-r\) plane. In the static spherical shadow,
that means

$$AB=1.$$

Therefore the relevant question is not whether scalaron hair can be made
small. The relevant question is whether the scalaron contribution can be
made exactly compatible with \(AB=1\) in every static source-free
exterior.

## General Screened Profile

Write the scalaron contribution to the weak-field exterior as \(q(r)\):

$$\phi=\phi_{\rm GR}-q(r), \qquad \psi=\phi_{\rm GR}+q(r).$$

E3's areal-gauge shadow gives, at linear order,

$$AB-1=\frac{2}{c^2}\left(\phi+r\psi'\right).$$

The GR part cancels:

$$\phi_{\rm GR}+r\phi_{\rm GR}'=0.$$

Thus any scalaron contribution gives

$$\phi+r\psi'=r q'(r)-q(r).$$

Exact P7' requires

$$r q'(r)-q(r)=0.$$

The solution is

$$q(r)=C r.$$

Asymptotic flatness forces \(C=0\). Hence the only P7'-compatible
screened scalar profile is

$$q(r)\equiv0.$$

Any nonzero screened profile violates P7' somewhere. Screening changes
the magnitude or support of the violation; it does not turn the
violation into an allowed static vacuum configuration.

## G20 Yukawa Witness

For the G20 scalaron exterior,

$$q(r)=\frac{GM}{3r}e^{-r/\ell_*}.$$

The P7' shadow is

$$r q'(r)-q(r)=-\left(\frac{r}{\ell_*}+2\right)q(r),$$

which is nonzero wherever the hair is nonzero. The profile is screened
outside \(\ell_*\), but it is not P7'-compatible.

## Consequence

Combining this note with E3:

```text
a != 0 -> mandatory q != 0 somewhere
q != 0 somewhere -> P7' violation
therefore P7' -> a = 0
```

So scalaron screening does not rescue \(a \neq 0\) inside the admitted
theory.

The only escape is the already recorded theory-owner appeal: re-scope
P7' so that it does not forbid the scalaron layer, or so that it applies
only beyond some range or only in the two-derivative sector. That is a
postulate revision, not a screened solution under the current postulate
set. It needs independent grounding; otherwise it is recovery-shaped.

## Forge Validation

Machine-checked support:

```text
vacuum_forge/src/field_equation_trials/013_scalaron_screening/
  scalaron_screening_p7prime_obstruction.py
```

The script verifies:

- \(\phi+r\psi'=r q'-q\) for a general screened scalar profile;
- exact P7' plus asymptotic flatness forces \(q=0\);
- the G20 Yukawa scalaron profile has a nonzero P7' shadow;
- the screening-rescue route is killed unless P7' is appealed.

Run:

```text
cd vacuum_forge/src
PYTHONPATH=. python field_equation_trials/013_scalaron_screening/scalaron_screening_p7prime_obstruction.py
```

In the current workspace, use the Anaconda interpreter:

```text
cd vacuum_forge/src
$env:PYTHONPATH='.'
& 'C:\Users\alano\anaconda3\python.exe' field_equation_trials\013_scalaron_screening\scalaron_screening_p7prime_obstruction.py
```
