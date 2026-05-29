# 3. Trace/traceless decomposition identity

For a symmetric matrix `H`, the split

```text
H = (tr H / n) I + H_TF
H_TF = H - (tr H / n) I
```

has `tr(H_TF)=0`, and the script verifies exact reconstruction.

Interpretation:

```text
scalar trace channel -> isotropic part;
directional tensor channel -> traceless shear part.
```
