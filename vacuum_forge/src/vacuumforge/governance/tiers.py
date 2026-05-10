"""Claim-strength tiers."""

from enum import Enum


class ClaimTier(str, Enum):
    INFORMATIONAL = "informational"
    CONSTRAINED = "constrained"
    EXCLUSION = "exclusion"
    LICENSING = "licensing"
