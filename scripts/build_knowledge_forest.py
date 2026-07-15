#!/usr/bin/env python3
"""Validate the Cosmos relationship matrix and emit a deterministic knowledge forest.

Standard-library only. Designed for local execution, Termux and CI.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Set, Tuple

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MATRIX = ROOT / "data" / "knowledge" / "relationship_matrix.json"
DEFAULT_ATTENTION = ROOT / "data" / "knowledge" / "attention_registry.json"
DEFAULT_MARKDOWN = ROOT / "artifacts" / "knowledge_forest.md"
DEFAULT_DOT = ROOT / "artifacts" / "knowledge_forest.dot"

NODE_REQUIRED = {
    "id",
    "label",
    "repo",
    "path",
    "domain",
    "evidence_state",
    "attention_state",
    "vector_state",
    "source_refs",
    "next_experiment",
}
EDGE_REQUIRED = {"source", "relation", "target", "evidence_state", "rationale"}
ATTENTION_REQUIRED = {
    "id",
    "node_id",
    "attention_state",
    "reason",
    "risk_if_ignored",
    "next_action",
    "exit_condition",
}
VECTOR_KEYS = {"psi", "chi", "rho", "Delta", "Sigma", "Omega"}
ATTENTION_PRIORITY = {
    "CORE": 0,
    "ACTIVE": 1,
    "UNDERSERVED": 2,
    "LATENT": 3,
    "FORGOTTEN": 4,
    "TOKEN_VAZIO": 5,
    "IGNORED": 6,
}


class ValidationError(RuntimeError):
    """Raised when the machine-readable research contract is invalid."""


def load_json(path: Path) -> Dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise ValidationError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(
            f"invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    if not isinstance(value, dict):
        raise ValidationError(f"top-level JSON value must be an object: {path}")
    return value


def require_keys(item: Mapping[str, Any], required: Set[str], context: str) -> List[str]:
    missing = sorted(required.difference(item))
    return [f"{context}: missing field {field!r}" for field in missing]


def validate_contract(
    matrix: Mapping[str, Any], attention: Mapping[str, Any]
) -> Tuple[Dict[str, Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    errors: List[str] = []

    nodes_raw = matrix.get("nodes")
    edges_raw = matrix.get("edges")
    records_raw = attention.get("records")

    if not isinstance(nodes_raw, list):
        errors.append("matrix.nodes must be a list")
        nodes_raw = []
    if not isinstance(edges_raw, list):
        errors.append("matrix.edges must be a list")
        edges_raw = []
    if not isinstance(records_raw, list):
        errors.append("attention.records must be a list")
        records_raw = []

    evidence_states = set(matrix.get("evidence_states", []))
    attention_states = set(matrix.get("attention_states", []))
    relation_types = set(matrix.get("relation_types", []))
    if not evidence_states:
        errors.append("matrix.evidence_states must not be empty")
    if not attention_states:
        errors.append("matrix.attention_states must not be empty")
    if not relation_types:
        errors.append("matrix.relation_types must not be empty")

    nodes: Dict[str, Dict[str, Any]] = {}
    for index, raw in enumerate(nodes_raw):
        context = f"nodes[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(require_keys(raw, NODE_REQUIRED, context))
        node_id = raw.get("id")
        if not isinstance(node_id, str) or not node_id.strip():
            errors.append(f"{context}: id must be a non-empty string")
            continue
        if node_id in nodes:
            errors.append(f"{context}: duplicate node id {node_id!r}")
            continue
        nodes[node_id] = dict(raw)

        if raw.get("evidence_state") not in evidence_states:
            errors.append(
                f"{context}: invalid evidence_state {raw.get('evidence_state')!r}"
            )
        if raw.get("attention_state") not in attention_states:
            errors.append(
                f"{context}: invalid attention_state {raw.get('attention_state')!r}"
            )
        if not isinstance(raw.get("domain"), list) or not raw.get("domain"):
            errors.append(f"{context}: domain must be a non-empty list")
        if not isinstance(raw.get("source_refs"), list) or not raw.get("source_refs"):
            errors.append(f"{context}: source_refs must be a non-empty list")
        vector = raw.get("vector_state")
        if not isinstance(vector, dict):
            errors.append(f"{context}: vector_state must be an object")
        else:
            missing_vector = sorted(VECTOR_KEYS.difference(vector))
            for field in missing_vector:
                errors.append(f"{context}: vector_state missing {field!r}")
        if raw.get("attention_state") in {
            "LATENT",
            "FORGOTTEN",
            "UNDERSERVED",
            "IGNORED",
            "TOKEN_VAZIO",
        } and not str(raw.get("next_experiment", "")).strip():
            errors.append(f"{context}: neglected/latent node requires next_experiment")

    root_id = matrix.get("root_id")
    if root_id not in nodes:
        errors.append(f"matrix.root_id {root_id!r} does not reference an existing node")

    edges: List[Dict[str, Any]] = []
    seen_edges: Set[Tuple[str, str, str]] = set()
    for index, raw in enumerate(edges_raw):
        context = f"edges[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(require_keys(raw, EDGE_REQUIRED, context))
        source = raw.get("source")
        target = raw.get("target")
        relation = raw.get("relation")
        if source not in nodes:
            errors.append(f"{context}: orphan source {source!r}")
        if target not in nodes:
            errors.append(f"{context}: orphan target {target!r}")
        if relation not in relation_types:
            errors.append(f"{context}: invalid relation {relation!r}")
        if raw.get("evidence_state") not in evidence_states:
            errors.append(
                f"{context}: invalid evidence_state {raw.get('evidence_state')!r}"
            )
        key = (str(source), str(relation), str(target))
        if key in seen_edges:
            errors.append(f"{context}: duplicate edge {key}")
        seen_edges.add(key)
        edges.append(dict(raw))

    attention_records: List[Dict[str, Any]] = []
    seen_attention_ids: Set[str] = set()
    seen_attention_nodes: Set[str] = set()
    for index, raw in enumerate(records_raw):
        context = f"attention.records[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(require_keys(raw, ATTENTION_REQUIRED, context))
        record_id = raw.get("id")
        node_id = raw.get("node_id")
        state = raw.get("attention_state")
        if not isinstance(record_id, str) or not record_id:
            errors.append(f"{context}: id must be a non-empty string")
        elif record_id in seen_attention_ids:
            errors.append(f"{context}: duplicate id {record_id!r}")
        else:
            seen_attention_ids.add(record_id)
        if node_id not in nodes:
            errors.append(f"{context}: unknown node_id {node_id!r}")
        else:
            if node_id in seen_attention_nodes:
                errors.append(f"{context}: duplicate attention record for {node_id!r}")
            seen_attention_nodes.add(str(node_id))
            if state != nodes[str(node_id)].get("attention_state"):
                errors.append(
                    f"{context}: state {state!r} differs from node state "
                    f"{nodes[str(node_id)].get('attention_state')!r}"
                )
        if state not in attention_states:
            errors.append(f"{context}: invalid attention_state {state!r}")
        attention_records.append(dict(raw))

    if errors:
        rendered = "\n".join(f"- {message}" for message in errors)
        raise ValidationError(f"knowledge contract failed:\n{rendered}")

    return nodes, edges, attention_records


def build_undirected_adjacency(
    nodes: Mapping[str, Mapping[str, Any]], edges: Sequence[Mapping[str, Any]]
) -> Dict[str, Set[str]]:
    adjacency: Dict[str, Set[str]] = {node_id: set() for node_id in nodes}
    for edge in edges:
        source = str(edge["source"])
        target = str(edge["target"])
        adjacency[source].add(target)
        adjacency[target].add(source)
    return adjacency


def connected_components(adjacency: Mapping[str, Set[str]]) -> List[List[str]]:
    unseen = set(adjacency)
    components: List[List[str]] = []
    while unseen:
        start = min(unseen)
        queue = deque([start])
        unseen.remove(start)
        component: List[str] = []
        while queue:
            current = queue.popleft()
            component.append(current)
            for neighbor in sorted(adjacency[current]):
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
        components.append(sorted(component))
    return components


def node_sort_key(node_id: str, nodes: Mapping[str, Mapping[str, Any]]) -> Tuple[int, str]:
    state = str(nodes[node_id].get("attention_state", "TOKEN_VAZIO"))
    return (ATTENTION_PRIORITY.get(state, 99), node_id)


def choose_component_root(
    component: Sequence[str], root_id: str, nodes: Mapping[str, Mapping[str, Any]]
) -> str:
    if root_id in component:
        return root_id
    return min(component, key=lambda node_id: node_sort_key(node_id, nodes))


def spanning_forest(
    nodes: Mapping[str, Mapping[str, Any]],
    adjacency: Mapping[str, Set[str]],
    root_id: str,
) -> Tuple[List[str], Dict[str, str], Dict[str, List[str]], Set[frozenset[str]]]:
    roots: List[str] = []
    parent: Dict[str, str] = {}
    children: Dict[str, List[str]] = defaultdict(list)
    tree_pairs: Set[frozenset[str]] = set()

    for component in connected_components(adjacency):
        root = choose_component_root(component, root_id, nodes)
        roots.append(root)
        visited = {root}
        queue = deque([root])
        while queue:
            current = queue.popleft()
            neighbors = sorted(
                adjacency[current], key=lambda node_id: node_sort_key(node_id, nodes)
            )
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                parent[neighbor] = current
                children[current].append(neighbor)
                tree_pairs.add(frozenset((current, neighbor)))
                queue.append(neighbor)

    for node_id in children:
        children[node_id].sort(key=lambda value: node_sort_key(value, nodes))
    roots.sort(key=lambda value: (value != root_id, node_sort_key(value, nodes)))
    return roots, parent, children, tree_pairs


def render_tree_lines(
    root: str,
    nodes: Mapping[str, Mapping[str, Any]],
    children: Mapping[str, Sequence[str]],
) -> List[str]:
    lines: List[str] = []
    stack: List[Tuple[str, int]] = [(root, 0)]
    while stack:
        node_id, depth = stack.pop()
        node = nodes[node_id]
        indent = "  " * depth
        lines.append(
            f"{indent}- `{node_id}` — {node['label']} "
            f"[{node['attention_state']} | {node['evidence_state']}]"
        )
        for child in reversed(children.get(node_id, [])):
            stack.append((child, depth + 1))
    return lines


def markdown_report(
    matrix: Mapping[str, Any],
    nodes: Mapping[str, Mapping[str, Any]],
    edges: Sequence[Mapping[str, Any]],
    attention_records: Sequence[Mapping[str, Any]],
) -> str:
    adjacency = build_undirected_adjacency(nodes, edges)
    components = connected_components(adjacency)
    roots, _parent, children, tree_pairs = spanning_forest(
        nodes, adjacency, str(matrix["root_id"])
    )

    evidence_counts = Counter(str(node["evidence_state"]) for node in nodes.values())
    attention_counts = Counter(str(node["attention_state"]) for node in nodes.values())
    orphan_count = sum(1 for neighbors in adjacency.values() if not neighbors)

    lines: List[str] = [
        "# Generated Knowledge Forest",
        "",
        "> Deterministic navigation projection generated from `data/knowledge/relationship_matrix.json`.",
        "> The full graph may contain cycles; non-tree relations are preserved below.",
        "",
        "## Contract summary",
        "",
        f"- Schema version: `{matrix.get('schema_version', 'TOKEN_VAZIO')}`",
        f"- Matrix date: `{matrix.get('generated_on', 'TOKEN_VAZIO')}`",
        f"- Nodes: **{len(nodes)}**",
        f"- Directed edges: **{len(edges)}**",
        f"- Connected components: **{len(components)}**",
        f"- Orphan nodes: **{orphan_count}**",
        f"- Attention records: **{len(attention_records)}**",
        "",
        "## Evidence-state distribution",
        "",
        "| State | Nodes |",
        "|---|---:|",
    ]
    for state in matrix.get("evidence_states", []):
        lines.append(f"| `{state}` | {evidence_counts.get(str(state), 0)} |")

    lines.extend(
        [
            "",
            "## Attention-state distribution",
            "",
            "| State | Nodes |",
            "|---|---:|",
        ]
    )
    for state in matrix.get("attention_states", []):
        lines.append(f"| `{state}` | {attention_counts.get(str(state), 0)} |")

    lines.extend(["", "## Spanning forest", ""])
    for index, root in enumerate(roots, start=1):
        lines.append(f"### Tree {index}: `{root}`")
        lines.append("")
        lines.extend(render_tree_lines(root, nodes, children))
        lines.append("")

    lines.extend(["## Cross-links outside the spanning forest", ""])
    cross_links = []
    for edge in edges:
        pair = frozenset((str(edge["source"]), str(edge["target"])))
        if pair not in tree_pairs:
            cross_links.append(edge)
    if cross_links:
        lines.extend(
            [
                "| Source | Relation | Target | Evidence | Rationale |",
                "|---|---|---|---|---|",
            ]
        )
        for edge in sorted(
            cross_links,
            key=lambda value: (
                str(value["source"]),
                str(value["relation"]),
                str(value["target"]),
            ),
        ):
            rationale = str(edge["rationale"]).replace("|", "\\|")
            lines.append(
                f"| `{edge['source']}` | `{edge['relation']}` | `{edge['target']}` | "
                f"`{edge['evidence_state']}` | {rationale} |"
            )
    else:
        lines.append("No cross-links outside the spanning forest.")

    lines.extend(["", "## Attention queue", ""])
    if attention_records:
        lines.extend(
            [
                "| ID | Node | State | Next action | Exit condition |",
                "|---|---|---|---|---|",
            ]
        )
        for record in sorted(attention_records, key=lambda value: str(value["id"])):
            next_action = str(record["next_action"]).replace("|", "\\|")
            exit_condition = str(record["exit_condition"]).replace("|", "\\|")
            lines.append(
                f"| `{record['id']}` | `{record['node_id']}` | "
                f"`{record['attention_state']}` | {next_action} | {exit_condition} |"
            )
    else:
        lines.append("No attention records.")

    lines.extend(
        [
            "",
            "## Research invariants",
            "",
            "- Repository presence is not scientific validation.",
            "- Symbolic similarity is not physical causality.",
            "- `TOKEN_VAZIO` is retained instead of fabricated evidence.",
            "- Contradictions and null results remain first-class records.",
            "- A cycle may return only with new evidence or a changed state.",
            "",
        ]
    )
    return "\n".join(lines)


def dot_escape(value: Any) -> str:
    return str(value).replace("\\", "\\\\").replace('"', '\\"')


def dot_report(
    nodes: Mapping[str, Mapping[str, Any]], edges: Sequence[Mapping[str, Any]]
) -> str:
    lines = [
        "digraph knowledge_forest {",
        "  rankdir=LR;",
        '  graph [label="Cosmos/RAFAELIA Relationship Matrix", labelloc=t];',
        '  node [shape=box, fontname="monospace"];',
        '  edge [fontname="monospace"];',
    ]
    for node_id in sorted(nodes):
        node = nodes[node_id]
        label = (
            f"{node_id}\\n{node['label']}\\n"
            f"{node['attention_state']} | {node['evidence_state']}"
        )
        lines.append(f'  "{dot_escape(node_id)}" [label="{dot_escape(label)}"];')
    for edge in sorted(
        edges,
        key=lambda value: (
            str(value["source"]), str(value["relation"]), str(value["target"])
        ),
    ):
        label = f"{edge['relation']} | {edge['evidence_state']}"
        lines.append(
            f'  "{dot_escape(edge["source"])}" -> "{dot_escape(edge["target"])}" '
            f'[label="{dot_escape(label)}"];'
        )
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    parser.add_argument("--attention", type=Path, default=DEFAULT_ATTENTION)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    parser.add_argument("--dot", type=Path, default=DEFAULT_DOT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate only; do not write generated artifacts",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    try:
        matrix = load_json(args.matrix)
        attention = load_json(args.attention)
        nodes, edges, attention_records = validate_contract(matrix, attention)
    except ValidationError as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 2

    print(
        f"[OK] contract valid: nodes={len(nodes)} edges={len(edges)} "
        f"attention={len(attention_records)}"
    )
    if args.check:
        return 0

    atomic_write(args.markdown, markdown_report(matrix, nodes, edges, attention_records))
    atomic_write(args.dot, dot_report(nodes, edges))
    print(f"[OK] wrote {args.markdown}")
    print(f"[OK] wrote {args.dot}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
