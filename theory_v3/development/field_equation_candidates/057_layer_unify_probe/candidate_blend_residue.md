# candidate_blend_residue — Result Note

## Result

The script derives the symbolic derivative residues created by blending interior and exterior profiles:

```text
F = (1-s)*F_in + s*F_out
```

The first-derivative residue is:

```text
R1 = (F_out - F_in)*s'
```

The second-derivative residue is:

```text
R2 = (F_out - F_in)*s'' + 2*(F_out' - F_in')*s'
```

with the output form:

```text
-F_in*s'' + F_out*s'' - 2*F_in'*s' + 2*F_out'*s'
```

## Main Findings

This is the central unification-probe result of Group 57.

The finite layer exposes exactly the terms that a unified rule must explain:

```text
profile mismatch multiplied by s';
profile mismatch multiplied by s'';
derivative mismatch multiplied by s'.
```

These are not nuisance terms to hide. They are candidate clues for transition-layer response, curvature smoothing cost, or future geometric candidate terms.

The script also correctly rejects two bad moves:

```text
ignoring the residues;
inserting the residues as repair tensors.
```

## Boundary

The residues are diagnostics. They are not field-equation terms and not parent closure.

## Steering Consequence

The next check must account for the energy cost of these residues. Blending cannot be treated as a free interpolation.
