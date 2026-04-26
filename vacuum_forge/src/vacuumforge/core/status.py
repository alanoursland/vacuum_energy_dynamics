"""Status vocabulary for theory statements and results."""

from enum import Enum


class Status(str, Enum):
    DEFINITION = "definition"
    POSTULATE = "postulate"
    CANDIDATE_POSTULATE = "candidate_postulate"
    ASSUMPTION = "assumption"
    DERIVED = "derived"
    PROVISIONAL = "provisional"
    OBSERVATIONAL_CONSTRAINT = "observational_constraint"
    FAILED_DERIVATION = "failed_derivation"
    OPEN_QUESTION = "open_question"
    TARGET = "target"


class Exactness(str, Enum):
    EXACT = "exact"
    FIRST_ORDER = "first_order"
    SECOND_ORDER = "second_order"
    ORDER_N = "order_n"
    UNDETERMINED = "undetermined"


class SourceClass(str, Enum):
    TRACE_FREE = "trace_free"
    PURE_TRACE = "pure_trace"
    MIXED = "mixed"
    ZERO = "zero"
    UNDETERMINED = "undetermined"
