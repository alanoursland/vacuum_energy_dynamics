# 6. Quadratic Metric Gate Status

## Claim

Exact metric reconstruction requires exact quadratic/parallelogram response.
A Hessian approximation alone is not the same as a globally exact metric
branch.

## SymPy check

For `Q(z)=az^2`, the parallelogram defect vanishes. For `Q(z)=az^2+bz^4`, the
parallelogram defect is nonzero.

## Ledger status

Conditional gate. Metric geometry is closed downstream of exact quadratic
response; exact quadratic response itself remains a load-bearing selector.
