# KNOWLEDGE_FOREST — Entry Point

The Cosmos repository now has a machine-readable cross-repository research layer.

## Canonical files

- Architecture: [`docs/architecture/RELATIONAL_KNOWLEDGE_FOREST.md`](docs/architecture/RELATIONAL_KNOWLEDGE_FOREST.md)
- Relationship matrix: [`data/knowledge/relationship_matrix.json`](data/knowledge/relationship_matrix.json)
- Attention registry: [`data/knowledge/attention_registry.json`](data/knowledge/attention_registry.json)
- Deterministic builder: [`scripts/build_knowledge_forest.py`](scripts/build_knowledge_forest.py)

## Execute

```bash
python3 scripts/build_knowledge_forest.py --check
python3 scripts/build_knowledge_forest.py
```

Expected generated files:

```text
artifacts/knowledge_forest.md
artifacts/knowledge_forest.dot
```

## Connected nuclei

- Calendar forest: `rafaelmeloreisnovo/GEOMETRIA_SOLAR_Maia_Inca` — `CALENDARIOS.md`
- Cosmological validation: `instituto-Rafael/relativity-living-light`
- Celestial catalogue: `rafaelmeloreisnovo/Catalogo-cosmologico`
- Toroidal execution: `rafaelmeloreisnovo/ChipQuantum`

## Invariant

```text
source -> concept -> typed relation -> evidence state -> next experiment -> feedback
```

No similarity of symbols, numbers or shapes is promoted to physical causality without a derivation and a test.