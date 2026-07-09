# Contributing to Cosmos — RAFAELIA

## Scope

Contributions should relate to one of the 17 knowledge domains documented in `docs/areas/`,
or extend the RAFAELIA cosmological framework.

## Branch Naming

| Type | Pattern |
|---|---|
| Research | `research/<domain>-<topic>` |
| Documentation | `docs/<topic>` |
| Script | `feat/script-<name>` |
| Fix | `fix/<issue>` |

## Commit Convention

```
research: add Fibonacci-galaxy pattern analysis for NGC 628
docs: expand areas/06-fractal-geometry.md with IFS examples
feat: add galaxy-spiral-comparator.py to scripts/technologies/
fix: correct spiral arm count in cosmos-espiral-M81.md
```

## Adding a Knowledge Domain Document

1. Place in `docs/areas/` with the format `NN-domain-name.md`
2. Include YAML front matter:

```yaml
---
title: "Domain Title"
domain: "cosmology | mathematics | ..."
date: YYYY-MM-DD
status: "draft | review | stable"
---
```

3. Cross-reference in `docs/navigation/NAVIGATION.md`
4. Update `README.md` knowledge domains table

## Adding a Script

1. Place in the appropriate `scripts/<category>/` directory
2. Include a README.md in that subdirectory if starting a new category
3. Scripts must include a header docstring / comment explaining purpose, usage, dependencies

## Pull Request Checklist

- [ ] Content placed in correct `docs/` or `scripts/` location
- [ ] YAML front matter added to new docs
- [ ] Navigation updated if adding new domain
- [ ] README updated if adding new domain or major document
- [ ] CHANGELOG.md updated under `[Unreleased]`
- [ ] Code of Conduct observed; all cited sources properly attributed
