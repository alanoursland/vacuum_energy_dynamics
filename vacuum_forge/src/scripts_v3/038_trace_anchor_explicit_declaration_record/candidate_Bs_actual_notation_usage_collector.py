from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    ScriptOutput,
    StatusMark,
)

# Group:
#   38_trace_anchor_explicit_declaration_record
# Script type:
#   AUDIT / EVIDENCE-COLLECTOR

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
SCRIPT_LABEL = "Candidate B_s Actual Notation Usage Collector"
MARKER_ID = "g38_bs_usage"

DEPENDENCIES = [
    (
        "g38_bs_evsrc",
        "038_trace_anchor_explicit_declaration_record__candidate_Bs_notation_evidence_source_inventory",
        "g38_bs_evsrc",
    ),
    (
        "g38_bs_fork",
        "038_trace_anchor_explicit_declaration_record__candidate_Bs_convention_declaration_fork",
        "g38_bs_fork",
    ),
    (
        "g38_recon",
        "038_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_batch_reconciliation",
        "g38_recon",
    ),
]

# Search configuration.
# The default search root is the full scripts_v3 directory.
# Add narrower relative paths here if the search is too broad in a local run.
SEARCH_ROOT_HINTS: List[str] = []
MAX_FILES_TO_SCAN = 800
MAX_SNIPPETS_TOTAL = 80
MAX_SNIPPETS_PER_CLASS = 16
CONTEXT_CHARS = 160

TEXT_SUFFIXES = {".py", ".md", ".txt", ".rst"}
SEARCH_TERMS = ["B_s", "B\\_s", "F_zeta", "F_\\zeta", "zeta/d", "2*zeta/d", "2 zeta / d", "trace normalization"]

METRIC_HINTS = [
    "metric coefficient",
    "metric component",
    "radial metric",
    "spatial metric",
    "line element",
    "ds^2",
    "dr^2",
    "differential square",
    "B(r)",
    "B =",
    "g_rr",
]

SCALE_HINTS = [
    "scale factor",
    "scale-factor",
    "scale response",
    "per-direction scale",
    "square-root",
    "sqrt",
    "exponential scale",
    "log(B_s)=zeta/d",
    "zeta/d",
]

DETERMINANT_HINTS = [
    "determinant",
    "volume root",
    "volume-root",
    "volume element",
    "per-dimension",
    "per dimension",
    "det(",
]

FUNCTIONAL_HINTS = ["F_zeta", "F_\\zeta", "functional", "response functional", "response-function"]
RECOVERY_HINTS = ["Schwarzschild", "gamma", "AB=1", "B=1/A", "recovery", "parent fit", "insertion convenience"]


@dataclass
class UsageHit:
    file: str
    term: str
    line_no: int
    snippet: str
    classification: str
    rationale: str


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def subheader(title: str) -> None:
    print()
    print("-" * 120)
    print(title)
    print("-" * 120)


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=RecordKind.INVENTORY_MARKER,
        )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def mark(status: str) -> StatusMark:
    return {
        "FOUND": StatusMark.PASS,
        "NOT_FOUND": StatusMark.DEFER,
        "METRIC_LIKE": StatusMark.INFO,
        "SCALE_LIKE": StatusMark.INFO,
        "DETERMINANT_ROOT_LIKE": StatusMark.INFO,
        "FUNCTIONAL_NEUTRAL": StatusMark.DEFER,
        "RECOVERY_SELECTOR": StatusMark.FAIL,
        "AMBIGUOUS": StatusMark.DEFER,
        "CONFLICT": StatusMark.FAIL,
        "NOT_READY": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def scripts_root() -> Path:
    return Path(__file__).resolve().parents[1]


def iter_search_roots() -> List[Path]:
    root = scripts_root()
    if not SEARCH_ROOT_HINTS:
        return [root]
    roots = []
    for item in SEARCH_ROOT_HINTS:
        p = Path(item)
        if not p.is_absolute():
            p = root / p
        if p.exists():
            roots.append(p)
    return roots or [root]


def iter_text_files(roots: Sequence[Path]) -> Iterable[Path]:
    seen = set()
    count = 0
    for root in roots:
        if root.is_file():
            candidates = [root]
        else:
            candidates = root.rglob("*")
        for path in candidates:
            if count >= MAX_FILES_TO_SCAN:
                return
            if not path.is_file():
                continue
            if ".vacuumforge_archive" in path.parts:
                continue
            if "__pycache__" in path.parts:
                continue
            if path.suffix not in TEXT_SUFFIXES:
                continue
            key = str(path.resolve())
            if key in seen:
                continue
            seen.add(key)
            count += 1
            yield path


def safe_read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="latin-1")
        except Exception:
            return ""
    except Exception:
        return ""


def line_number_for(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def make_snippet(text: str, index: int, term: str) -> str:
    start = max(0, index - CONTEXT_CHARS)
    end = min(len(text), index + len(term) + CONTEXT_CHARS)
    snippet = text[start:end].replace("\n", " ")
    return " ".join(snippet.split())


def contains_any(text_lower: str, hints: Sequence[str]) -> bool:
    return any(h.lower() in text_lower for h in hints)


def classify_snippet(snippet: str) -> Tuple[str, str]:
    s = snippet.lower()
    metric = contains_any(s, METRIC_HINTS)
    scale = contains_any(s, SCALE_HINTS)
    determinant = contains_any(s, DETERMINANT_HINTS)
    functional = contains_any(s, FUNCTIONAL_HINTS)
    recovery = contains_any(s, RECOVERY_HINTS)

    if recovery and not (metric or scale or determinant):
        return "RECOVERY_SELECTOR", "recovery/fit language appears without independent notation-origin evidence"
    if metric and not scale:
        return "METRIC_LIKE", "line-element, metric-component, radial/spatial metric, or B notation hint found"
    if scale and not metric:
        return "SCALE_LIKE", "scale-factor, per-direction scale, square-root, or zeta/d hint found"
    if determinant and not metric:
        return "DETERMINANT_ROOT_LIKE", "determinant/volume-root hint found; root convention still required"
    if functional and not (metric or scale or determinant):
        return "FUNCTIONAL_NEUTRAL", "F_zeta/functional response language found without scale-vs-metric convention"
    if metric and scale:
        return "AMBIGUOUS", "metric-like and scale-like hints both appear in local context"
    if recovery:
        return "RECOVERY_SELECTOR", "recovery/fit language appears; not admissible as selector"
    return "AMBIGUOUS", "term found but local context does not decide scale-vs-metric convention"


def collect_usage_hits() -> List[UsageHit]:
    hits: List[UsageHit] = []
    class_counts: Dict[str, int] = {}
    for path in iter_text_files(iter_search_roots()):
        if len(hits) >= MAX_SNIPPETS_TOTAL:
            break
        text = safe_read_text(path)
        if not text:
            continue
        for term in SEARCH_TERMS:
            start = 0
            while len(hits) < MAX_SNIPPETS_TOTAL:
                idx = text.find(term, start)
                if idx < 0:
                    break
                snippet = make_snippet(text, idx, term)
                classification, rationale = classify_snippet(snippet)
                if class_counts.get(classification, 0) < MAX_SNIPPETS_PER_CLASS:
                    try:
                        rel = str(path.relative_to(scripts_root()))
                    except ValueError:
                        rel = str(path)
                    hits.append(
                        UsageHit(
                            file=rel,
                            term=term,
                            line_no=line_number_for(text, idx),
                            snippet=snippet,
                            classification=classification,
                            rationale=rationale,
                        )
                    )
                    class_counts[classification] = class_counts.get(classification, 0) + 1
                start = idx + len(term)
                if class_counts.get(classification, 0) >= MAX_SNIPPETS_PER_CLASS and len(hits) >= MAX_SNIPPETS_TOTAL:
                    break
    return hits


def summarize_hits(hits: Sequence[UsageHit]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for hit in hits:
        counts[hit.classification] = counts.get(hit.classification, 0) + 1
    return counts


def classify_overall(counts: Dict[str, int]) -> Tuple[str, str]:
    metric = counts.get("METRIC_LIKE", 0)
    scale = counts.get("SCALE_LIKE", 0)
    det = counts.get("DETERMINANT_ROOT_LIKE", 0)
    functional = counts.get("FUNCTIONAL_NEUTRAL", 0)
    ambiguous = counts.get("AMBIGUOUS", 0)

    if metric == scale == det == functional == ambiguous == 0:
        return "NOT_FOUND", "no B_s/B/F_zeta notation snippets were found under the configured search roots"
    if metric > 0 and scale == 0 and det == 0:
        return "METRIC_LIKE", "only metric-like admissible usage was found; still requires explicit declaration before use"
    if scale > 0 and metric == 0:
        return "SCALE_LIKE", "scale-like usage was found without metric-like conflict; still requires explicit declaration before use"
    if metric > 0 and scale > 0:
        return "CONFLICT", "both metric-like and scale-like usage were found; a repair or notation split may be needed"
    if det > 0 and metric == 0 and scale == 0:
        return "DETERMINANT_ROOT_LIKE", "only determinant/volume-root-like usage was found; root convention remains needed"
    return "AMBIGUOUS", "usage was found but does not decide the convention"


def case_0(out: ScriptOutput):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What actual project-file usage of B_s, inherited B, or F_zeta can be")
    print("  collected before choosing scale-factor versus metric-coefficient convention?")
    print("\nDiscipline:\n")
    print("  This script collects notation snippets only.")
    print("  It does not choose a B_s convention.")
    print("  It does not fill declarations, adopt Package B, prove components, or open insertion.")
    print("\nTiny goblin rule:\n  Read the labels already on the jars. Do not write new labels.")
    with out.governance_assessments():
        out.line("B_s actual notation usage collector opened", StatusMark.PASS, "file-scan evidence collector only; no convention installed")


def case_1(out: ScriptOutput):
    header("Case 1: Symbolic actual-usage ledger")
    line_metric, scale_lang, det_root, F_neutral, recovery_bad, ambiguous, missing = sp.symbols(
        "line_metric scale_lang det_root F_neutral recovery_bad ambiguous missing"
    )
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )
    L_usage = sp.simplify(line_metric + scale_lang + det_root + F_neutral + recovery_bad + ambiguous + missing)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    print(f"Actual-usage evidence load: L_usage = {L_usage}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream}")
    with out.derived_results():
        out.line("B_s actual-usage symbolic ledger stated", StatusMark.PASS, f"L_usage={L_usage}; L_downstream_closed={L_downstream}")


def case_2(out: ScriptOutput, hits: Sequence[UsageHit]):
    header("Case 2: Collected notation snippets")
    if not hits:
        print("No snippets found under configured search roots.")
        with out.governance_assessments():
            out.line("no actual notation snippets found", StatusMark.DEFER, "B_s convention remains deferred")
        return

    for idx, hit in enumerate(hits, 1):
        subheader(f"H{idx}: {hit.classification} in {hit.file}:{hit.line_no}")
        print(f"Term: {hit.term}")
        print(f"Rationale: {hit.rationale}")
        print(f"Snippet: {hit.snippet}")
        with out.governance_assessments():
            out.line(
                f"H{idx}: {hit.file}:{hit.line_no}",
                mark(hit.classification),
                f"{hit.classification}: {hit.rationale}",
            )


def case_3(out: ScriptOutput, counts: Dict[str, int], overall: Tuple[str, str]):
    header("Case 3: Usage classification summary")
    if counts:
        for cls in sorted(counts):
            print(f"{cls}: {counts[cls]}")
    else:
        print("No classified hits.")
    status, detail = overall
    print(f"overall_classification = {status}")
    print(f"detail = {detail}")
    with out.governance_assessments():
        out.line("actual B_s notation usage classified", mark(status), f"{status}: {detail}")
        out.line("no convention installed", StatusMark.DEFER, "usage evidence must feed a later explicit convention declaration or repair script")


def case_4(out: ScriptOutput):
    header("Case 4: Invalid actual-usage upgrades")
    shortcuts = [
        ("X1: snippet as declaration", "treat a found snippet as installed B_s convention", "found usage is evidence, not declaration record"),
        ("X2: conflicting snippets hidden", "ignore scale/metric conflict and choose silently", "conflict must be repaired or explicitly split"),
        ("X3: recovery snippet as selector", "use recovery-context hit as convention evidence", "recovery remains audit only"),
        ("X4: usage evidence as adoption", "treat notation evidence as Package B adoption", "adoption requires separate explicit decision"),
        ("X5: usage evidence as insertion", "treat notation evidence as B_s/F_zeta insertion", "downstream gates remain closed"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_5(out: ScriptOutput, overall: Tuple[str, str]):
    header("Case 5: Local conclusions")
    status, detail = overall
    with out.governance_assessments():
        out.line("B_s actual notation usage collection complete", mark(status), f"{status}: {detail}")
        if status == "CONFLICT":
            out.line("repair needed", StatusMark.FAIL, "write notation-conflict repair or notation-splitting script before declaration")
        elif status in {"METRIC_LIKE", "SCALE_LIKE", "DETERMINANT_ROOT_LIKE"}:
            out.line("evidence can support later declaration", StatusMark.DEFER, "later script may prepare explicit convention record; this script does not install it")
        else:
            out.line("convention remains deferred", StatusMark.DEFER, "more evidence or explicit theory choice needed")
        out.line("downstream gates remain closed", StatusMark.DEFER, "actual-usage collection is not declaration, adoption, theorem proof, insertion, active O, residual control, or parent readiness")


def record_marker(ns, marker_id: str, symbol_name: str):
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="actual notation usage collector marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 38 B_s actual notation usage collector",
    )


def record_claim(ns, claim_id: str, marker_id: str, status, statement: str):
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, marker_id: str, statement: str, status=ObligationStatus.OPEN):
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


def record_governance(ns, hits: Sequence[UsageHit], counts: Dict[str, int], overall: Tuple[str, str]):
    record_marker(ns, MARKER_ID, "g38_Bs_actual_notation_usage_collected")
    status, detail = overall
    record_claim(
        ns,
        "g38_bs_usage_overall",
        MARKER_ID,
        GovernanceStatus.CANDIDATE_ROUTE if status not in {"CONFLICT", "RECOVERY_SELECTOR"} else GovernanceStatus.POLICY_RULE,
        f"Actual B_s notation usage classification: {status}. {detail}. Counts: {counts}.",
    )
    for idx, hit in enumerate(hits[:20], 1):
        record_claim(
            ns,
            f"g38_bs_usage_h{idx}",
            MARKER_ID,
            GovernanceStatus.CANDIDATE_ROUTE if hit.classification not in {"RECOVERY_SELECTOR", "CONFLICT"} else GovernanceStatus.POLICY_RULE,
            f"{hit.classification} hit in {hit.file}:{hit.line_no} for term {hit.term}. Rationale: {hit.rationale}. Snippet: {hit.snippet}",
        )
    record_obligation(
        ns,
        "g38_bs_usage_no_auto_declaration",
        MARKER_ID,
        "Do not treat collected notation snippets as an installed B_s convention; a separate declaration or repair record is still required.",
    )
    if status == "CONFLICT":
        record_obligation(
            ns,
            "g38_bs_usage_repair_conflict",
            MARKER_ID,
            "Resolve metric-like versus scale-like notation conflict before completing Group 38 declaration.",
        )
    elif status not in {"METRIC_LIKE", "SCALE_LIKE"}:
        record_obligation(
            ns,
            "g38_bs_usage_more_evidence_or_choice",
            MARKER_ID,
            "Find stronger notation evidence or make explicit theory choice before completing Group 38 declaration.",
        )


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0(out)
    case_1(out)
    hits = collect_usage_hits()
    counts = summarize_hits(hits)
    overall = classify_overall(counts)
    case_2(out, hits)
    case_3(out, counts, overall)
    case_4(out)
    case_5(out, overall)
    record_governance(ns, hits, counts, overall)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
