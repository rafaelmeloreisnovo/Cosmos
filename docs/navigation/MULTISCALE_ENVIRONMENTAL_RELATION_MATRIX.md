# Multiscale Environmental Relation Matrix

**Date:** 2026-07-19  
**Role:** transdisciplinary contextualization  
**Evidence state:** `claim_allowed=false` for new physical bridges

## 1. Context invariant

Cosmos may connect domains, but it cannot convert semantic proximity into
physical identity. The canonical contextual invariant is:

```math
\boxed{
\mathcal C
=
(\text{entity},\text{state},\text{scale},\text{relation},
\text{evidence},\text{boundary},\text{next test})
}
```

A contextual edge is meaningful only when all seven fields are present.

The physical possibility gate is:

```math
\text{possibility}
\rightarrow
\{\text{carrier, medium, scale, units, conservation, rate,
observable, baseline, falsifier}\}
\rightarrow
\text{testable relation}.
```

## 2. Multiscale ladder

```text
MICRO
  atoms, ions, electrons, photons, isotopes, bonds, spin, charge

MESO
  minerals, grains, crystals, fluids, plasma cells, reaction fronts

PLANETARY
  crust, ocean, atmosphere, ionosphere, magnetosphere, rotation

STELLAR
  stellar wind, radiation, corona, magnetic topology, particle flux

ASTROPHYSICAL
  disks, jets, shocks, compact objects, interstellar/intergalactic plasma

COSMOLOGICAL
  expansion, distances, structure growth, background and perturbations
```

A relation may cross adjacent or distant levels only as one of:

- `CONTEXTUALIZES`;
- `MODULATES`;
- `COUPLES`;
- `CORRELATES_WITH`;
- `SCALE_BRIDGE_HYPOTHESIS`;
- `ANALOGY_ONLY`.

## 3. Relation semantics

| Type | Meaning | What it does not mean |
|---|---|---|
| `STANDARD_MECHANISM` | accepted baseline mechanism | final explanation of every observation |
| `MODULATES` | changes amplitude, phase, rate or boundary | creates the phenomenon from nothing |
| `COUPLES` | explicit interaction term with units | verbal similarity |
| `CORRELATES_WITH` | measurable association | causality |
| `CONTEXTUALIZES` | supplies domain meaning | mathematical equivalence |
| `SCALE_BRIDGE_HYPOTHESIS` | proposed bridge awaiting tests | confirmed cross-scale law |
| `ANALOGY_ONLY` | didactic or geometric similarity | shared physical mechanism |
| `CONTRADICTS` | statements cannot coexist as written | one side is automatically false without review |
| `FALSIFIES` | test can reject a proposition | test necessarily confirms the alternative |

## 4. Environmental state space

```math
X_p=
(M,R,\Omega_{\rm rot},a_\star,F_\star,
\mathbf B,\mathbf E,\mathbf g,T,P,\rho,
\mathbf x_{\rm chem},x_e,\sigma,
\mathcal A,\mathcal O,\mathcal C,t).
```

This state vector supports expandable contextualization without pretending that
all combinations are physically realizable.

### Expansion dimensions

- object class: planet, moon, star, disk, cloud, laboratory system;
- composition: elements, isotopes, molecules, dust and plasma species;
- phase: solid, liquid, gas, supercritical fluid, partially ionized plasma,
  relativistic plasma;
- forcing: stellar wind, radiation, tides, rotation, shocks and fields;
- geometry: spherical, layered, toroidal, filamentary, turbulent or fractured;
- time: rotation, season, magnetic cycle, eruption, orbital and evolutionary time;
- observation: spectra, timing, polarization, fields, currents, temperature,
  pressure, density and reaction products.

## 5. Significant correlation matrix

| Context A | Context B | Allowed relation | Required discriminator |
|---|---|---|---|
| stellar wind | magnetosphere | `COUPLES / STANDARD_MECHANISM` | field orientation, particle flux, time lag |
| magnetosphere | ionosphere | `COUPLES / MODULATES` | conductance, precipitation, current systems |
| ionosphere | Earth-ionosphere cavity | `MODULATES` | frequency, amplitude, phase, Q and lightning baseline |
| local mineralogy | local magnetic anomaly | `MODULATES / STANDARD_MECHANISM` | mineral phase, remanence and survey geometry |
| local mineralogy | global cavity mode | `SCALE_BRIDGE_HYPOTHESIS` | transfer function and global effect size |
| ocean/atmosphere motion | electric field/current | `COUPLES / STANDARD_MECHANISM` | velocity, conductivity and magnetic field |
| plasma state | photon propagation | `COUPLES / STANDARD_MECHANISM` | DM, RM, polarization and frequency law |
| plasma residual | RLL propagation term | `SCALE_BRIDGE_HYPOTHESIS` | preregistered residual after null models |
| composition + P + T | phase | `COUPLES / STANDARD_MECHANISM` | equation of state and phase boundary |
| reaction network | energy/radiation | `COUPLES / STANDARD_MECHANISM` | rates, products, spectra and conservation |
| similar frequency values | shared physical cause | `ANALOGY_ONLY` | carrier and coupling equation required |
| toroidal geometry across domains | same mechanism | `ANALOGY_ONLY` | forces and governing equations required |

## 6. Observation composition

```math
O_{\rm obs}
=
\mathcal T_{\rm instrument}
\circ
\mathcal T_{\rm environment}
\circ
\mathcal T_{\rm source/cosmology}
(O_0)+N.
```

The order matters. An environmental transfer effect can mimic, hide or distort a
source effect. It cannot be assigned to cosmology before the environmental and
instrumental operators are modeled.

## 7. Chemistry as a constrained graph

```math
G_{\rm reaction}=(V_{\rm species},E_{\rm reactions}).
```

Every edge must preserve declared conserved quantities and include a rate or
threshold. Context exploration is therefore not unrestricted permutation of the
periodic table.

```math
\sum Z_{\rm in}=\sum Z_{\rm out},
\quad
\sum A_{\rm in}=\sum A_{\rm out},
\quad
\sum q_{\rm in}=\sum q_{\rm out}.
```

The same elements may produce different phases and products when pressure,
temperature, density, radiation, field and cooling history change.

## 8. Repository projection map

| Repository | Contextual role |
|---|---|
| `rafaelmeloreisnovo/Mapa` | federation, authority and typed relations |
| `instituto-Rafael/relativity-living-light` | claims, observables, null models and falsifiers |
| `instituto-Rafael/PlamaticGravity-` | plasma/MHD/gravity mechanisms and boundaries |
| `rafaelmeloreisnovo/Cosmos` | ontology, scale separation and reading paths |
| `rafaelmeloreisnovo/papers` | editorial synthesis, provenance and manuscript route |

Potential future consumers remain `TOKEN_VAZIO` until they accept a typed
contract: `Fisica`, `Particula-Omega-`, `Catalogo-cosmologico`,
`GEOMETRIA_SOLAR_Maia_Inca` and `RafPolimata`.

## 9. Expansion rule

A new context may be added without rewriting the invariant. It must provide:

```yaml
entity: TOKEN_VAZIO
state_vector: TOKEN_VAZIO
scale: TOKEN_VAZIO
relation_type: TOKEN_VAZIO
evidence_state: TOKEN_VAZIO
boundary: TOKEN_VAZIO
next_test: TOKEN_VAZIO
```

No empty field is inferred. `TOKEN_VAZIO` is preserved until evidence or a
formal definition closes it.

## 10. Boundary

Cosmos can show that two domains are related, comparable or potentially
integrable. It cannot establish that the relation is causal, universal or a new
law of nature.

```text
semantic connection != physical equivalence
correlation != causation
same geometry != same force
same frequency != same carrier
expandable context != unlimited claim
```
