# Boundary Flux Field Bridge 74: Far-Field Correction Power Filter

## Purpose

This report classifies which far-field powers are produced by polynomial
nonlinear scalar strain densities:

```text
Phi_p(z)=1/2 z + alpha/(2p)z^p.
```

## Validated Checks

- potential and field correction powers verified for p=2..8: passed
- power filter solution: passed
- low-power filter table generated: passed

## Correction Powers

From proof `51`, the first nonlinear potential correction has power:

```text
r^(-(4p-3)).
```

The field correction has power:

```text
r^(-(4p-2)).
```

Checked cases:

```text
p=2: potential correction r^-5, field correction r^-6
p=3: potential correction r^-9, field correction r^-10
p=4: potential correction r^-13, field correction r^-14
p=5: potential correction r^-17, field correction r^-18
p=6: potential correction r^-21, field correction r^-22
p=7: potential correction r^-25, field correction r^-26
p=8: potential correction r^-29, field correction r^-30
```

## Power Filter

To obtain a potential correction `r^-m`, one needs:

```text
m = 4p - 3
p = (m+3)/4.
```

Low-power table:

```text
m=2: p=(m+3)/4=5/4, produced=False
m=3: p=(m+3)/4=3/2, produced=False
m=4: p=(m+3)/4=7/4, produced=False
m=5: p=(m+3)/4=2, produced=True
m=6: p=(m+3)/4=9/4, produced=False
m=7: p=(m+3)/4=5/2, produced=False
m=8: p=(m+3)/4=11/4, produced=False
```

## Interpretation

Polynomial scalar strain nonlinearities of this form do not produce arbitrary
far-field correction powers. They produce the sequence:

```text
r^-5, r^-9, r^-13, ...
```

for potential corrections.

If a target theory requires a different weak-field correction hierarchy, this
family is too narrow or the correction must enter through a different part of
the model.
