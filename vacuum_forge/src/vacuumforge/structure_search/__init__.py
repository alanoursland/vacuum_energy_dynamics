"""StructureSearch: upstream module for searching candidate vacuum structures.

Searches for mathematical structures that make local vacuum exchange
inherently trace-free, sitting upstream of the existing source,
energy, metric, PPN, and requirement-validation systems.
"""

from vacuumforge.structure_search.variables import PreModeVariable
from vacuumforge.structure_search.projection import ProjectionMap
from vacuumforge.structure_search.operators import SourceOperator
from vacuumforge.structure_search.structure import VacuumStructure
from vacuumforge.structure_search.results import (
    InducedModeSource,
    StructureAnalysisResult,
    StructureStatus,
)
from vacuumforge.structure_search.analyzer import StructureAnalyzer
from vacuumforge.structure_search.search import StructureSearchEngine
from vacuumforge.structure_search.families import (
    direct_mode_basis,
    symmetric_antisymmetric_pair,
    two_channel_exchange,
    general_linear_projection,
    conserved_volume_family,
)

__all__ = [
    "PreModeVariable",
    "ProjectionMap",
    "SourceOperator",
    "VacuumStructure",
    "InducedModeSource",
    "StructureAnalysisResult",
    "StructureStatus",
    "StructureAnalyzer",
    "StructureSearchEngine",
    "direct_mode_basis",
    "symmetric_antisymmetric_pair",
    "two_channel_exchange",
    "general_linear_projection",
    "conserved_volume_family",
]
