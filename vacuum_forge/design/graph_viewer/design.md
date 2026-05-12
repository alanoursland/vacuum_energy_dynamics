# Graph Viewer Design

## Purpose

The graph viewer is a diagnostic tool that renders the vacuum forge archive as an
interactive visual graph. Its goal is to make the theory's epistemic shape legible
at a glance: what is derived, what is merely constrained, what is explicitly forbidden,
and what blocks the finish line.

The output is a single self-contained `.html` file. Opening it in a browser requires
no server, no credentials, and no installed packages beyond the Python build step.

---

## Conceptual model

The archive records knowledge at four nested levels:

```
project
  └── group (01_foundations … 27_active_O_construction)
        └── script (one .py file = one script namespace)
              └── record (claim, obligation, route, handoff, derivation, branch)
                    └── burden item (structured field within a record)
```

The graph viewer exposes all four levels interactively, controlled by the user
clicking into nodes to descend.

---

## Architecture

```
vacuum_forge/tools/graph_viewer/
    __init__.py
    loader.py        # reads .vacuumforge_archive → GraphData
    mapper.py        # (RecordKind, status) → Cytoscape CSS class + color
    aggregator.py    # synthesizes group-level and parent-gate nodes
    template.html    # Cytoscape.js app; contains %%GRAPH_DATA%% slot
    build.py         # entry: reads archive, fills template, writes graph.html
```

Invocation:

```bash
python -m tools.graph_viewer \
    --archive src/scripts_v3/.vacuumforge_archive \
    --output  graph.html
```

Or as a vacuumforge CLI subcommand alongside `vf_lint`:

```bash
python -m vacuumforge graph --output graph.html
```

---

## Packages

### Recommended stack

| Package | Role | Install |
|---|---|---|
| `dash-cytoscape` | Interactive graph in a local Dash server | `pip install dash-cytoscape` |
| `dash` | Web server + Python callbacks (already installed) | — |
| `networkx` | Layout pre-computation if needed (already installed) | — |

`dash-cytoscape` is a thin wrapper around Cytoscape.js. It weighs ~50 KB, has no
complex build step, and exposes Python callbacks for click events. This is the
recommended path for the interactive expand-on-click behaviour, because the
level-switching logic stays in Python rather than being split across Python and JS.

### Zero-new-package fallback

If no new packages are acceptable at build time:

- Python builds a static `.html` file with `%%GRAPH_DATA%%` filled by `str.replace`.
- Cytoscape.js is loaded from CDN inside the template (three `<script>` tags).
- All level-switching and click interaction is implemented in JavaScript inside
  the template.

This fallback produces a fully functional viewer. Its only limitation is that the
expand-on-click and burden-panel logic must be written in JS rather than Python.

### CDN libraries (used by both paths)

```html
<script src="https://unpkg.com/cytoscape@3.29.2/dist/cytoscape.min.js"></script>
<script src="https://unpkg.com/dagre@0.8.5/dist/dagre.min.js"></script>
<script src="https://unpkg.com/cytoscape-dagre@2.5.0/cytoscape-dagre.js"></script>
```

dagre provides the hierarchical directed-acyclic-graph layout algorithm, which is
the right choice for a proof-dependency graph: groups flow left-to-right in order,
the parent equation gate sits at the far right as a sink.

---

## Graph levels

### Level 0 — Group overview (27 nodes + 1 gate)

One node per group folder. One synthetic node for the parent equation gate.
Edges are group-to-group handoff arrows derived from `HandoffImportRecord` and
cross-group `DependencyDeclaration` records.

This is the primary view: the one that shows the macro epistemic shape.
Group 26 appears as an amber obstruction knot. Group 27 appears as a green
construction target with open borders. The parent equation gate sits at the far
right, dashed and locked.

### Level 1 — Script detail (expand a group)

Click a group node. The group expands in place to show its constituent script
namespaces as smaller nodes, with intra-group dependency edges (from
`dependencies.json`) as arrows between them.

Each script node is colored by its dominant record type and bordered by its
aggregate status.

### Level 2 — Record burst (expand a script)

Click a script node. The script expands to show all its individual records as
nodes: claims, obligations, routes, handoffs, branches.

Rejected routes appear as red nodes orbiting the main claim ring. Open obligations
appear as amber dashed nodes with arrows inward to the routes that require them.
Handoff records appear as green nodes with double borders.

### Level 3 — Burden panel (click a record)

Click any record node. A side panel opens showing the record's structured content:

- For an obligation: `title`, `status`, `description`, `required_by`, `satisfied_by`,
  `failed_by`, `superseded_by`.
- For a claim: `statement`, `tier`, `status`, `obligation_ids`, `source_claim_ids`,
  `evidence_ids`.
- For a route: `name`, `status`, `activation_conditions`, `required_obligations`.
- For a handoff: `imported_as`, `status`, `source_record_ref`.

If the record has a structured burden list in its metadata, each burden item is
rendered as a colored chip: green (satisfied), amber (open), red (failed),
gray (not yet attempted).

This is the "burden blossom" view. Clicking the `active O` obligation node opens
the panel. Right now almost every chip would be open amber. As construction
succeeds, chips turn green.

---

## Visual encoding

### Node fill color (record type)

| Visual category | Actual types | Color |
|---|---|---|
| Group / script container | group folders, `SCRIPT_METADATA` | dark slate `#3a4a5c` |
| Derivation / marker | `DERIVATION`, `INVENTORY_MARKER`, `DIAGNOSTIC_EXAMPLE`, `SAMPLE_DERIVATION` | steel blue `#4a7fa5` |
| Claim | `GOVERNANCE_CLAIM`, `SUMMARY_CLAIM`, `MEMO_RECORD`, `MEMO_STATEMENT` | violet `#7c5cbf` |
| Obligation | `PROOF_OBLIGATION` | amber `#c8860a` |
| Rejected route | `ROUTE_RECORD` with `REJECTED_ROUTE` status | red `#b83232` |
| Candidate route | `ROUTE_RECORD` with any other status | muted rose `#8a4040` |
| Closure gate | synthetic parent equation node | deep gray `#222` |
| Handoff | `HANDOFF_IMPORT` | green `#3a7a4a` |
| Branch decision | `BRANCH_DECISION` | teal `#3a7a7a` |

### Node border style (status)

| Status condition | Border |
|---|---|
| `GovernanceStatus.LICENSED_CLAIM`, `ObligationStatus.SATISFIED`, `Status.PROVEN` | solid 2px |
| `ObligationStatus.OPEN`, `GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION`, `DEFERRED_PENDING_PREREQUISITES`, `NOT_INSERTABLE_YET` | dashed 2px |
| Record is a `HANDOFF_IMPORT` (any status) | double 3px |
| `GovernanceStatus.REJECTED_ROUTE`, `KILLED_BY_CONTRADICTION`, `FAILED_BY_WITNESS`, `ObligationStatus.FAILED` | solid red 2px |
| `GovernanceStatus.HEURISTIC`, partial-reduction metadata present | thick amber 3px |

### Edge types

| Edge meaning | Style |
|---|---|
| Script dependency (`dependencies.json`) | thin gray, directed |
| Claim → obligation it carries | amber dashed, directed |
| Obligation → route that requires it | amber solid, directed |
| Cross-group handoff | green, thick, directed |
| Claim → source claim it depends on | blue, thin, directed |
| Route → claim it activates | violet, thin, directed |

---

## Loader design (`loader.py`)

The loader does not use the `ProjectArchive` Python API, which is per-script. It
walks the archive filesystem directly and reads JSON files, because it needs
cross-script and cross-group aggregation.

### Archive layout

```
.vacuumforge_archive/
    {group}__{script}/
        claims/         *.json   → ClaimRecord shape
        obligations/    *.json   → ProofObligationRecord shape
        routes/         *.json   → RouteRecord shape
        handoffs/       *.json   → HandoffImportRecord shape
        branches/       *.json   → BranchDecisionRecord shape
        derivations/    *.json   → DerivationRecord shape
        evidence/       *.json   → EvidenceRecord shape
        dependencies.json        → list[DependencyDeclaration shape]
        last_run_metadata.json
```

Namespace name format: `{group_prefix}__{script_stem}`.
Group prefix is everything before the double underscore.

### GraphData structure

```python
@dataclass
class GraphNode:
    node_id: str           # unique, e.g. "claim::g26_summary_not_theorem"
    level: int             # 0=group, 1=script, 2=record
    label: str             # short display label
    full_label: str        # full ID or statement
    kind: str              # RecordKind value, or "group", or "gate"
    status: str            # GovernanceStatus / ObligationStatus value
    group: str             # group prefix
    script_id: str | None  # None for group and gate nodes
    css_classes: list[str] # assigned by mapper.py
    detail: dict           # full record content for the side panel

@dataclass
class GraphEdge:
    edge_id: str
    source: str            # node_id
    target: str            # node_id
    edge_kind: str         # "dependency", "obligation", "handoff", "source_claim", …
    levels: list[int]      # which view levels show this edge
    css_classes: list[str]

@dataclass
class GraphData:
    nodes: list[GraphNode]
    edges: list[GraphEdge]
```

### Intra-script edges

Within a script namespace, edges are extracted from record fields:

| Field | Edge produced |
|---|---|
| `claim.obligation_ids` | claim → obligation (for each referenced obligation) |
| `claim.source_claim_ids` | source claim → this claim |
| `obligation.required_by` | obligation → route |
| `obligation.satisfied_by` | obligation → satisfying record |
| `route.required_obligations` | route → obligation (cross-check; redundant with above) |
| `handoff.source_record_ref` | source record → handoff node |

### Cross-script and cross-group edges

- `dependencies.json` in each namespace provides `upstream_script_id` references.
  These produce level-1 (script → script) edges. At level 0 they are aggregated
  into group → group edges when the upstream is in a different group.
- A `HandoffImportRecord` whose `source_record_ref` points to a record in a different
  group produces a green cross-group handoff edge at level 0.

---

## Aggregator design (`aggregator.py`)

### Group-level status

A group node's visual status is synthesized from its constituent script records:

| Rule | Visual result |
|---|---|
| Any `HandoffImportRecord` exists in the group | double border (handoff-ready) |
| Any obligation has `status = "open"` | dashed border |
| Any route has `GovernanceStatus.REJECTED_ROUTE` | red badge count on the group node |
| Any claim has `GovernanceStatus.HEURISTIC` or partial-reduction metadata | thick amber border |
| All obligations are `satisfied` and all claims are `licensed_claim` | solid border (closed) |

Group node fill: amber if the dominant open status is a controlled obstruction or
theorem attempt; green if the group's primary output is a handoff record; dark slate
otherwise.

The "dominant open status" rule uses the group's summary script as the authority.
Each group has a `candidate_group_NN_status_summary.py` script; the status of that
script's primary claim determines the group-level color.

### Parent equation gate

The parent equation is a synthetic `level=0` node with `kind="gate"` and
`status="open"` (dashed, deep gray). It is created by the aggregator, not read
from the archive.

Its incoming edges are collected by scanning all claims across all groups for
statements that contain `"parent equation"` and whose `obligation_ids` reference
parent closure. Any such claim contributes a group → gate edge at level 0.

The gate's burden panel (level 3) shows a static prerequisite list hardcoded in
the aggregator, each wired to its corresponding obligation record by ID so that
its status chip is live:

```
residual control       → open
B_s/F_zeta insertion   → open
source routing         → open
boundary neutrality    → open
support matching       → open
divergence safety      → open
parent identity        → open
```

The gate border flips from dashed to solid when all feeding obligations have
`status = "satisfied"`. Until then: locked.

---

## Mapper design (`mapper.py`)

`mapper.py` is a pure translation layer. It takes a `(kind, status)` pair and
returns a list of Cytoscape CSS class names. The CSS classes are defined in the
HTML template.

```python
FILL_MAP = {
    "group":                "fill-slate",
    "gate":                 "fill-gate",
    "derivation":           "fill-blue",
    "inventory_marker":     "fill-blue",
    "diagnostic_example":   "fill-blue",
    "sample_derivation":    "fill-blue",
    "governance_claim":     "fill-violet",
    "summary_claim":        "fill-violet",
    "memo_record":          "fill-violet",
    "memo_statement":       "fill-violet",
    "proof_obligation":     "fill-amber",
    "route_record":         "fill-red",       # overridden below for non-rejected
    "handoff_import":       "fill-green",
    "branch_decision":      "fill-teal",
}

BORDER_MAP = {
    "licensed_claim":              "border-solid",
    "satisfied":                   "border-solid",
    "proven":                      "border-solid",
    "open":                        "border-dashed",
    "unresolved_proof_obligation": "border-dashed",
    "deferred_pending_prerequisites": "border-dashed",
    "not_insertable_yet":          "border-dashed",
    "rejected_route":              "border-red",
    "killed_by_contradiction":     "border-red",
    "failed_by_witness":           "border-red",
    "failed":                      "border-red",
    "heuristic":                   "border-amber-thick",
}

def map_node_classes(kind: str, status: str, is_handoff: bool = False) -> list[str]:
    classes = ["node", FILL_MAP.get(kind, "fill-slate")]
    if is_handoff:
        classes.append("border-double")
    elif kind == "route_record" and status != "rejected_route":
        classes.append("fill-red-muted")
        classes.append(BORDER_MAP.get(status, "border-dashed"))
    else:
        classes.append(BORDER_MAP.get(status, "border-dashed"))
    return classes
```

---

## Template design (`template.html`)

The template is a self-contained HTML file. The Python build step replaces the
single token `%%GRAPH_DATA%%` with the JSON-serialised `GraphData`.

### Structure

```html
<!DOCTYPE html>
<html>
<head>
  <!-- CDN: Cytoscape.js, dagre, cytoscape-dagre -->
  <style>/* Cytoscape CSS stylesheet + panel/nav styles */</style>
</head>
<body>
  <div id="nav">   <!-- breadcrumb: Project > Group 26 > script > ... -->
  <div id="toolbar"> <!-- filter checkboxes: types, statuses -->
  <div id="cy">    <!-- Cytoscape canvas -->
  <div id="panel"> <!-- burden detail panel (hidden until click) -->
  <script>
    const GRAPH_DATA = %%GRAPH_DATA%%;
    /* level navigation, click handlers, filter logic */
  </script>
</body>
</html>
```

### Level switching (JS)

All three levels of data are embedded at build time. Level switching re-initialises
the Cytoscape instance with a filtered subset:

```js
function showLevel(level, groupFilter, scriptFilter) {
  const nodes = GRAPH_DATA.nodes.filter(n =>
    n.level === level &&
    (groupFilter  === null || n.group     === groupFilter) &&
    (scriptFilter === null || n.script_id === scriptFilter)
  );
  const nodeIds = new Set(nodes.map(n => n.node_id));
  const edges = GRAPH_DATA.edges.filter(e =>
    e.levels.includes(level) &&
    nodeIds.has(e.source) &&
    nodeIds.has(e.target)
  );
  cy.elements().remove();
  cy.add([...nodes.map(toElem), ...edges.map(toElem)]);
  cy.layout({ name: level < 2 ? 'dagre' : 'cose', rankDir: 'LR' }).run();
}
```

Layout: dagre (hierarchical, left-to-right) at levels 0 and 1; cose
(force-directed) at level 2 (record burst), since records within a script have
no strict temporal ordering.

### Click handlers

```js
cy.on('tap', 'node', function(evt) {
  const node = evt.target;
  const level = node.data('level');
  if (level === 0) showLevel(1, node.data('group'), null);
  else if (level === 1) showLevel(2, null, node.data('script_id'));
  else openPanel(node.data('detail'));
});
```

### Burden panel

The panel reads the `detail` field from the node's data object. For records with
a `burden_items` key in their metadata, each item is rendered as a coloured chip:

```js
function openPanel(detail) {
  const panel = document.getElementById('panel');
  panel.innerHTML = renderDetail(detail);
  panel.classList.remove('hidden');
}
```

---

## Build output

The build step writes one file: `graph.html`. The file is self-contained after
the CDN scripts are fetched on first load. It can be committed as a snapshot.

Recommended: commit a snapshot after each group closes, named by group number:

```
theory_v3/development/snapshots/
    graph_after_group_26.html
    graph_after_group_27.html
    ...
```

---

## Open design questions

**1. Group color rule for amber vs. slate**

The current rule uses the group's summary script as the authority for the
dominant open status. A refinement question: should a group be amber if *any*
claim is HEURISTIC, or only if the summary script's primary claim is? The summary
script is the natural authority and avoids false positives from diagnostic
sub-scripts. Recommended: use the summary script.

**2. Rejected-route runes at level 0**

At level 0, rejected routes are too fine-grained to show as individual nodes.
Options:
- A count badge on the group node ("7 rejected routes").
- Suppressed entirely at level 0 (they appear at level 2).
- A small red dot cluster orbiting the group node (cosmetic, no click).

The count badge is the most informative without cluttering the macro view.

**3. Cross-group dependency edge density**

The archive currently has mostly intra-group dependencies. If cross-group
dependencies grow, level-0 edge routing may become dense. A toolbar toggle to
hide dependency edges (showing only handoff edges) at level 0 is advisable from
the start.

**4. Structured burden item metadata**

The burden list for active O (domain, codomain, kernel, image, pairing, …) does
not yet exist as structured metadata in the archive. The panel can render the
record's `description` field as free text, or from a `burden_items: list[{name,
status}]` key added to `metadata`. The structured format is preferable for live
status chip rendering.

Decision required: add `burden_items` to claim/obligation `metadata` in the
scripts that have structured burdens.

**5. Parent gate edge collection**

Parent gate incoming edges are currently collected by keyword-scanning
`claim.statement` for `"parent equation"`. This is fragile. A cleaner approach:
add a `contributes_to_parent_gate: true` boolean to claim `metadata`, set
explicitly in the summary scripts, and use that flag for edge collection.

**6. Offline vs. CDN**

The CDN approach requires a network connection on first load. For a fully offline
viewer, the three Cytoscape libraries can be bundled inline into the template as
base64-encoded strings or inlined minified JS. Total size is ~300 KB. This is a
build option (`--offline` flag), not the default.
