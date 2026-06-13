# 5. Workflow Component 2: Machine-Verified Derivation Chains

The workflow treats executable scripts as the minimum reproducibility floor for
algebraic claims. A theorem claim should have a script that rederives its key
identity or calculation from scratch whenever it is run.

In the case study, scripts are organized into numbered trial groups. Each
group has an intended role: chartering, bootstrap calculation, postulate
adoption record, radiative positivity, higher-curvature health, boundary
admissibility, cosmology, or vector closure.

The scripts serve several functions:

- they make algebraic manipulations reproducible;
- they provide concrete witnesses for abstract claims;
- they expose sign errors and coefficient drift;
- they declare dependencies on upstream results;
- they prevent silent mutation of earlier conclusions.

This is weaker than formal proof. A script can verify a symbolic identity or
test a family of ansatzes, but it may not prove a theorem in full analytic
generality. A compact witness is not the same as a general proof. A dependency
check can enforce archive consistency but cannot guarantee that the physical
interpretation is correct.

The proper claim is therefore limited: executable derivation scripts raise the
cost of rationalization. They make it harder for a model or human to quietly
change signs, move coefficients, or reuse assumptions without leaving a trace.
