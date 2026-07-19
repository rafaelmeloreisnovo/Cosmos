# Time–Observer–Wave–Radiation Multiscale Matrix

**Date:** 2026-07-19  
**State:** `ONTOLOGY_ACTIVE / PHYSICAL_CLAIMS_BOUNDED`  
**Claim allowed:** `false`

## 1. Central invariant

The session can be compressed into one relational structure:

```math
\boxed{
\text{gradient}
\rightarrow
\text{relative motion}
\rightarrow
\text{transduction}
\rightarrow
\text{wave/reaction}
\rightarrow
\text{damping}
\rightarrow
\text{signal}
\rightarrow
\text{observation}
}
```

The geometry of this path may recur across scales, but the carrier, constitutive law and energy source must be redeclared at every scale.

## 2. Six-scale ladder

| Scale | State variables | Dominant relations | Typical signal |
|---|---|---|---|
| Crystal/micro | lattice strain, polarization, defects | piezoelectricity, phonons, fracture | voltage, light, heat |
| Rock/meso | stress field, pores, fluids, faults | elasticity, electrokinetics, fracture, chemistry | seismic and EM transients |
| Planetary | gravity, atmosphere, ionosphere, oceans, crust | waves, induction, global electric circuit, magnetosphere | magnetic, atmospheric and spectral variability |
| Stellar | pressure, temperature, reactions, radiation | hydrostatic balance, fusion, transport | photons, particles, neutrinos, winds |
| Astrophysical plasma | density, current, magnetic topology, rotation | MHD/kinetic waves, shocks, reconnection | radio through gamma, polarization, jets |
| Cosmological | expansion, stress-energy, distribution functions | geometry, perturbations, propagation | distances, growth, CMB, lensing, dispersion |

## 3. Relation types

```text
CAUSES
COUPLES_TO
TRANSDUCES_TO
MODULATES
DAMPENS
AMPLIFIES
PROPAGATES_THROUGH
IS_MEASURED_BY
IS_INFERRED_BY
CORRELATES_WITH
HAS_ANALOGOUS_FORM
CONTRADICTS
FALSIFIES
TOKEN_VAZIO
```

### Prohibited collapse

```text
HAS_ANALOGOUS_FORM != CAUSES
CORRELATES_WITH != TRANSDUCES_TO
IS_MEASURED_BY != CREATES
same frequency != same carrier
same spectrum label != same origin
```

## 4. Time as a physical and epistemic coordinate

For a physical state:

```math
X(t+\Delta t)=\mathcal F[X(t),B(t),S(t)]
```

where `B` represents boundary conditions and `S` external sources.

For a recorded state:

```math
Y_k=\mathcal H_k[X(t)]+N_k
```

Time must declare:

- physical timescale;
- relaxation and damping time;
- reaction and cooling time;
- propagation delay;
- detector exposure and cadence;
- clock reference and drift;
- analysis window and latency.

The same process can appear different when sampled above, near or below its characteristic timescale.

## 5. Observer decomposition

```math
O=(position,orientation,clock,bandwidth,resolution,
calibration,selection,model,uncertainty)
```

The observed datum is:

```math
D_{obs}=\mathcal T_O\circ\mathcal T_I\circ\mathcal T_M(D_{source})+N
```

where:

- `T_O`: observer and inference conventions;
- `T_I`: instrument response;
- `T_M`: medium and propagation;
- `N`: noise and unmodelled residual.

This does not make physical reality subjective. It distinguishes event from record and record from interpretation.

## 6. Damping matrix

The word `amortization` is represented as dissipation or relaxation:

```math
\mathbf M\ddot{\mathbf q}
+\mathbf C\dot{\mathbf q}
+\mathbf K\mathbf q
=\mathbf F(t)
```

| Coordinate | Restoring term | Loss term |
|---|---|---|
| elastic displacement | stiffness | internal friction/fracture |
| pressure wave | compressibility | viscosity/shock heating |
| electric charge | capacitance/field | leakage/resistance |
| magnetic perturbation | field tension | diffusion/reconnection |
| temperature | heat capacity | conduction/radiation |
| chemical abundance | free-energy landscape | reverse reaction/diffusion |
| plasma mode | pressure and magnetic tension | collisions/kinetic damping |
| observed signal | source coherence | bandwidth/noise/filtering |

The matrix form is an invariant of description, not proof that all systems share the same physics.

## 7. Quartz, seismic motion and gold

A meaningful relation chain is:

```text
fault loading
CAUSES stress/strain
COUPLES_TO quartz orientation and fabric
TRANSDUCES_TO piezoelectric potential
COUPLES_TO hydrothermal chemistry
MAY_MODULATE gold deposition and nanoparticle accumulation
```

A 2024 experiment supports the specific deposition pathway under controlled conditions. It does not prove that all gold-quartz associations have one origin, nor that quartz alone predicts seismic events.

## 8. Fracture, tape and X-rays

```text
stick-slip peeling
TRANSDUCES_TO charge separation/discharge
EMITS radio/visible/X-ray under moderate vacuum
IS_MEASURED_BY synchronized force and radiation detectors
```

The result is a strong example of mechanical-to-electromagnetic concentration. Its boundary conditions remain part of the claim.

## 9. Radiation ontology

### Massive particle radiation

```text
alpha -> helium nuclei
beta- -> electrons
beta+ -> positrons
neutron -> neutral massive particle
```

### Photon radiation

```text
radio -> microwave -> infrared -> visible -> ultraviolet/UVC
-> X-ray -> gamma
```

The photon ladder is ordered broadly by frequency/energy, but band boundaries are conventional and may overlap. Alpha and beta do not belong on that frequency ladder.

## 10. Reaction-path ontology

```text
mechanical deformation
  -> defect activation and surface chemistry
  -> thermal excitation
  -> molecular reaction/dissociation
  -> atomic excitation/ionization
  -> plasma kinetics
  -> pair/nuclear channels
```

Each transition requires a threshold, rate and competing pathway. More energy does not guarantee one predetermined product.

## 11. Solar wind and seismic relation boundary

Solar-wind forcing may modify magnetosphere and ionosphere. Seismic processes act primarily through lithosphere, crustal fluids and mechanical stress. Both may influence electromagnetic measurements, but:

```text
shared detector band
!= shared source
```

A correlation study must control at least:

- geomagnetic activity;
- lightning and weather;
- power infrastructure;
- station motion and orientation;
- local mineralogy and conductivity;
- instrument drift;
- multiple-comparison bias;
- time-lag preregistration.

## 12. Collective scaling

The statement that a subparticle becomes gigantic in cosmology is replaced by:

```math
\text{microscopic ensemble}
\rightarrow
\text{distribution function}
\rightarrow
\text{collective fields}
\rightarrow
\text{macroscopic observable}
```

Cosmological magnitude may arise from number, coherence, integrated path length, optical depth, stress-energy and causal volume. It does not require an elementary particle to enlarge its intrinsic size.

## 13. Cross-repository projection

| Repository | Authority |
|---|---|
| `Fisica` | solid mechanics, piezoelectricity, radiation taxonomy |
| `PlamaticGravity-` | plasma/MHD translation and phase boundary |
| `relativity-living-light` | B10 observation operator, baselines and falsifiers |
| `Cosmos` | multiscale ontology and relation typing |
| `papers` | full editorial packet and bibliography |
| `Mapa` | authority graph, pointers and drift control |

## 14. Expansion protocol

A new node is admissible when it declares:

```yaml
entity: ...
scale: ...
phase: ...
carrier: ...
source_of_energy: ...
coupling: ...
timescale: ...
damping: ...
observable: ...
instrument: ...
relation_type: ...
evidence_state: ...
falsifier: ...
```

Missing mandatory fields remain `TOKEN_VAZIO`; they are not inferred from semantic similarity.

## 15. Boundary

This matrix permits expansive contextualization while preserving domain identity. It is not a proof that geophysical, atmospheric, plasma and cosmological phenomena are one mechanism.
