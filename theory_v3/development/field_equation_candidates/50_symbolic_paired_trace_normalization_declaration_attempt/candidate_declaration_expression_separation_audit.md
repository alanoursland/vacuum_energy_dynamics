# candidate_declaration_expression_separation_audit — Result Note

## Result

The expression-separation audit confirms that the attempted declaration preserves the metric and scale expressions as distinct branch-indexed candidates.

## Main Findings

The metric expression remains `log(B_s_metric)=2*zeta/d`, and the scale expression remains `log(b_s_scale)=zeta/d`. The factor-of-two burden is therefore still visible inside the declaration attempt.

The audit explicitly rejects unqualified `B_s`, neutral `F_zeta` with an expression, compromise expressions, and convenience-based activation of either branch. This prevents the declaration attempt from quietly becoming a single neutral law.

## Boundary

Expression separation does not select either branch. It also does not make either expression insertable or parent-facing.

## Steering Consequence

This keeps the paired declaration attempt honest. The declaration attempt survives only because it refuses to solve the branch problem by hiding it. Any later summary or declaration-adjacent work must continue carrying both expressions explicitly.
