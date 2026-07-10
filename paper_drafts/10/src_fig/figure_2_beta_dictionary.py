"""Figure 2: the dictionary beta = lambda + 2, family members, and the
experimental fences.

Main panel: the line beta(lambda), the named members, the complete
static-accounting interval, and the classical-era Mercury band (drawn
to scale). Inset: zoom by four orders
of magnitude around the Schwarzschild point, where the modern
LLR + Cassini band |beta - 1| <= 1e-4 becomes visible.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[1] / "md" / "figure_2_beta_dictionary.png"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 8,
    "axes.linewidth": 0.6,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,
})

fig, ax = plt.subplots(figsize=(3.4, 2.8), dpi=300)

# the dictionary
lam_lo, lam_hi = -1.6, 1.5
ax.plot([lam_lo, lam_hi], [lam_lo + 2, lam_hi + 2], "k-", lw=1.2)

# full interval admitted by the static-accounting theorem
ax.axvspan(-0.25, 0.25, color="0.94", zorder=0)

# classical-era Mercury band, |beta - 1| <~ 0.03, to scale
ax.axhspan(1 - 0.03, 1 + 0.03, color="0.85", zorder=0)
ax.text(1.43, 1.06, "Mercury (classical era)", fontsize=6.5,
        ha="right", va="bottom", color="0.25")

# members: (lambda, label, marker, filled)
members = [
    (-1.0, "Schwarzschild", "o", True),
    (-0.5, "Shuler ($n=-1$)", "x", False),
    (-0.25, "ledger (rest)", "s", False),
    (0.0, "exponential", "^", False),
    (0.25, "ledger (redshift)", "D", False),
    (0.5, "Shuler ($n=+1$)", "x", False),
    (1.0, "reciprocal", "o", False),
]
for lam, name, mk, filled in members:
    ax.plot(lam, lam + 2, mk, ms=5,
            mfc=("k" if filled else "white"), mec="k", mew=0.9, zorder=5)

# direct labels, placed to avoid the line (above-left of each point)
ax.annotate("Schwarzschild", xy=(-1.0, 1.0), xytext=(-1.52, 1.28),
            fontsize=7, arrowprops=dict(arrowstyle="-", lw=0.6, color="0.2"))
ax.annotate(r"Shuler ($n=-1$)", xy=(-0.5, 1.5), xytext=(-1.37, 1.58),
            fontsize=6.5, arrowprops=dict(arrowstyle="-", lw=0.6, color="0.2"))
ax.annotate("ledger (rest)", xy=(-0.25, 1.75), xytext=(-1.05, 1.95),
            fontsize=7, arrowprops=dict(arrowstyle="-", lw=0.6, color="0.2"))
ax.annotate("exponential", xy=(0.0, 2.0), xytext=(-0.62, 2.42),
            fontsize=7, arrowprops=dict(arrowstyle="-", lw=0.6, color="0.2"))
ax.annotate("ledger (redshift)", xy=(0.25, 2.25), xytext=(-0.30, 2.85),
            fontsize=7, arrowprops=dict(arrowstyle="-", lw=0.6, color="0.2"))
ax.annotate(r"Shuler ($n=+1$)", xy=(0.5, 2.5), xytext=(0.50, 2.68),
            fontsize=6.5, arrowprops=dict(arrowstyle="-", lw=0.6, color="0.2"))
ax.annotate("reciprocal", xy=(1.0, 3.0), xytext=(0.55, 3.28),
            fontsize=7, arrowprops=dict(arrowstyle="-", lw=0.6, color="0.2"))

ax.set_xlim(lam_lo, lam_hi)
ax.set_ylim(0.3, 3.6)
ax.set_xlabel(r"self-energy counting weight $\lambda$")
ax.set_ylabel(r"PPN $\beta$")

# inset: the modern fence, four orders of magnitude down; placed clear
# of the Mercury band and of the main line
axins = ax.inset_axes([0.64, 0.30, 0.33, 0.26])
half = 6e-4
axins.plot([-1 - half, -1 + half], [1 - half, 1 + half], "k-", lw=1.0)
axins.axhspan(1 - 1e-4, 1 + 1e-4, color="0.85", zorder=0)
axins.plot(-1.0, 1.0, "ko", ms=3)
axins.set_xlim(-1 - half, -1 + half)
axins.set_ylim(1 - half, 1 + half)
axins.set_xticks([])
axins.set_yticks([])
axins.set_title("LLR + Cassini", fontsize=6, pad=2)
axins.text(-1 - 0.88 * half, 1 + 0.78 * half,
           r"$|\beta-1|\lesssim 10^{-4}$", fontsize=5.5, ha="left",
           va="top")
axins.text(-1 - 0.88 * half, 1 - 0.82 * half,
           r"zoom at $(-1,\,1)$", fontsize=5.5, ha="left", va="bottom",
           color="0.35")
for spine in axins.spines.values():
    spine.set_linewidth(0.5)

fig.tight_layout(pad=0.3)
fig.savefig(OUT)
print(f"wrote {OUT}")
