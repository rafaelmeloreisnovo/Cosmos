# Relational Knowledge Forest — Cosmos/RAFAELIA

<!-- markdownlint-disable MD013 MD060 -->

## 1. Purpose

This document defines an executable cross-repository architecture for research that cannot be reduced to one document, one discipline, or one isolated problem.

The forest connects:

- cosmology and observational models;
- solar, lunar, Venusian, agricultural and precessional calendars;
- celestial catalogues and provenance;
- toroidal geometry and graph topology;
- statistics, falsifiers and uncertainty;
- symbolic interpretation with explicit scientific boundaries;
- forgotten, underserved, ignored and latent research paths.

The invariant is not a preferred conclusion. The invariant is the traceable path:

```text
source -> concept -> relation -> claim state -> experiment -> result -> feedback
```

## 2. Repository roles

| Repository | Operational role |
|---|---|
| `rafaelmeloreisnovo/Cosmos` | Root index, cross-domain graph, research paths and semantic forest |
| `rafaelmeloreisnovo/GEOMETRIA_SOLAR_Maia_Inca` | Calendar, solar geometry and archaeoastronomical node |
| `instituto-Rafael/relativity-living-light` | Cosmological model, statistics, falsifiers and observational validation |
| `rafaelmeloreisnovo/Catalogo-cosmologico` | Celestial objects, observations, provenance and catalogue data |
| `rafaelmeloreisnovo/ChipQuantum` | T7 toroidal computation, geometry engine and low-level execution |
| `rafaelmeloreisnovo/TeoremasTesesTeorias` | Formal statements, definitions, theorem candidates and counterexamples |
| `rafaelmeloreisnovo/papers` | Publication layer, papers and reproducible research narratives |

A repository reference records a relationship; it does not by itself validate a scientific claim.

## 3. Node model

Every knowledge node MUST contain:

```text
id
label
repo
path
domain
evidence_state
attention_state
vector_state
source_refs
next_experiment
```

### 3.1 Evidence states

| State | Meaning |
|---|---|
| `VERIFIED` | Directly located in a repository file, dataset, result or executable artifact |
| `PARTIAL` | Some formal or empirical support exists, but the chain is incomplete |
| `DECLARED_BY_AUTHOR` | Authorship declaration exists without independent validation |
| `HYPOTHESIS` | Testable proposal with an identified falsifier |
| `TOKEN_VAZIO` | Required evidence, definition, dataset or derivation has not been located |
| `CONTRADICTION` | Located evidence conflicts with the claim |
| `PHILOSOPHICAL` | Interpretive layer that is not presented as an empirical physical claim |

### 3.2 Attention states

These states describe research treatment, not personal value:

| State | Operational meaning |
|---|---|
| `CORE` | Required by the current architecture |
| `ACTIVE` | Being calculated, documented or validated |
| `LATENT` | A relation is visible, but its mechanism has not been tested |
| `FORGOTTEN` | Previously present in the corpus but absent from the active research path |
| `UNDERSERVED` | Mentioned or partially treated, without sufficient depth or data |
| `IGNORED` | Deliberately excluded from current execution; exclusion reason must be recorded |
| `TOKEN_VAZIO` | Presence, relevance or evidence cannot yet be determined |

No node may be marked `FORGOTTEN`, `UNDERSERVED` or `IGNORED` without a `next_experiment` or an explicit exclusion reason.

## 4. Vector state

The cognitive-research vector is:

```math
v_n=(\psi,\chi,\rho,\Delta,\Sigma,\Omega)_n
```

where:

- `psi`: intention or research question;
- `chi`: observation, source or measured feature;
- `rho`: noise, ambiguity, bias or missing evidence;
- `Delta`: ethical and technical transformation;
- `Sigma`: coherent memory and provenance;
- `Omega`: bounded synthesis, never absolute truth by declaration.

A transition is valid only when it preserves provenance:

```math
v_{n+1}=T(v_n, e, s)
```

with `e` as evidence and `s` as the declared claim state.

## 5. Toroidal relationship layer

Toroidal language is represented as a topology and traversal model, not automatically as a physical equivalence.

For a torus parameterization:

```math
x=(R+r\cos\theta)\cos\phi
```

```math
y=(R+r\cos\theta)\sin\phi
```

```math
z=r\sin\theta
```

The two angular coordinates support two independent research cycles:

- `theta`: local cycle — document, observation, experiment, revision;
- `phi`: global cycle — calendar, orbit, cosmology, cross-repository synthesis.

The toroidal traversal invariant is:

```text
return to a node is allowed only with new evidence, a changed state, or a recorded contradiction
```

This prevents circular documentation that merely repeats the same assertion.

The Euler characteristic of an ideal torus is `chi = 0`. In this architecture it is used only as a topological reference for closed traversal. Any physical or computational claim involving `chi = 0`, T7 or 42 attractors remains governed by its own evidence and test artifacts in `ChipQuantum`.

## 6. Relationship types

Allowed edge types:

| Type | Meaning |
|---|---|
| `FORMALIZES` | Provides a mathematical or computational definition |
| `PROVIDES_DATA` | Supplies measurements or catalogue records |
| `TESTS` | Tests a claim or model against data |
| `FALSIFIES` | Defines or executes a rejection condition |
| `TEMPORALIZES` | Places a phenomenon in a calendar or cycle |
| `GEOMETRIZES` | Maps a concept to a geometric object or measurement |
| `TOPOLOGIZES` | Adds graph, manifold or toroidal structure |
| `IMPLEMENTS` | Provides executable code |
| `VISUALIZES` | Produces a diagram, chart or spatial representation |
| `CITES` | Records a source without implying validation |
| `CONTRASTS` | Preserves a disagreement, counterexample or alternative model |
| `EXTENDS` | Adds a bounded domain without replacing the source node |

## 7. Forest construction

The complete relationship network may contain cycles. To produce a readable forest:

1. build the full directed graph;
2. validate all nodes and edges;
3. reject orphan references and undeclared relation types;
4. calculate connected components;
5. choose roots by `CORE` status and repository role;
6. create a deterministic spanning forest for navigation;
7. preserve non-tree edges in a cross-link appendix;
8. emit an attention queue for latent and neglected nodes.

Thus the forest is a navigation projection of the graph, not a claim that knowledge itself is acyclic.

## 8. Multi-place calendar integration

The calendar branch must not assume that different cultures encode the same mechanism. It records comparable objects:

```text
place/culture
calendar type
observable
measurement method
period
uncertainty
source
alignment geometry
preservation state
claim state
```

Candidate coverage may include Mesoamerica, Andes, Amazonia, Egypt, Mesopotamia, Polynesia, northern Atlantic regions and other locations, but every location outside the current Maya/Inca corpus begins as `TOKEN_VAZIO` until a source and measurement are registered.

## 9. Latent and neglected paths

The initial registry includes:

- executable graph statistics for the current concept maps;
- Poincare sections and return maps for dynamic models;
- covariance and uncertainty for calendar alignments;
- erosion, restoration and chronological uncertainty in architectural measurements;
- cross-cultural comparison without forced equivalence;
- prime-number and modular relationships only where a formal rule exists;
- separation of geometric constants from cosmological parameters;
- semantic deduplication across repositories;
- negative results and contradictions as first-class nodes;
- provenance for images, tables and vectorized reconstructions.

## 10. Scientific boundary

The following implications are prohibited without an explicit derivation and evidence:

```text
symbolic similarity => physical causality
same number => same mechanism
calendar cycle => cosmological law
toroidal visualization => toroidal physical universe
repository presence => scientific validation
```

Permitted language:

```text
is represented by
is compared with
is tested against
shares a mathematical form with
is a candidate relation
is unsupported in the current corpus
```

## 11. Invariants

1. **Provenance invariant:** every scientific node has at least one source reference.
2. **Claim-boundary invariant:** evidence state travels with the node and edge.
3. **No-orphan invariant:** every edge endpoint exists.
4. **Attention invariant:** neglected nodes have a next action or exclusion reason.
5. **Cycle invariant:** a return requires new information or a changed state.
6. **Negative-result invariant:** contradiction is preserved, not deleted.
7. **Cross-repository invariant:** links do not duplicate entire documents.
8. **Execution invariant:** the matrix must be machine-validatable with standard-library tooling.
9. **Temporal invariant:** cycles are modeled by state transitions; wall-clock assumptions are optional metadata.
10. **TOKEN_VAZIO invariant:** absence is recorded rather than replaced by invented content.

## 12. Execution

From the `Cosmos` repository root:

```bash
python3 scripts/build_knowledge_forest.py
```

Expected deterministic outputs:

```text
artifacts/knowledge_forest.md
artifacts/knowledge_forest.dot
```

The script validates the matrix before generating the spanning forest and attention queue.

---

`Cosmos` remains the root map; specialized repositories remain authoritative for their own files, data and experiments.
