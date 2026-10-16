# Oblivion Forge
## A Machine-Independent, Multi-Scale, Multi-Process Fabrication Research Program

**Version:** 0.1 — Public concept release  
**Date:** 16 October 2026  
**Status:** Open research thought experiment; not peer reviewed; not experimentally validated as an integrated system  
**Publication:** Public research proposal — community feedback welcome  
**Relationship:** Proposed research expansion of the existing Oblivion AOS / Oblivion Forge project
**Origin:** A late-night, approximately 3 a.m. thought experiment about turning recycled soda cans into aluminum prints, which grew into a much broader idea for an open fabrication system.
**Acknowledgment:** Conceived by GitHub user [Oblivion1276](https://github.com/Oblivion1276); research draft developed with AI assistance and references to the cited prior art.

> **Central thesis.** A general-purpose fabrication platform should encode *what a designed object is*, *what material and interface behaviors it requires*, and *which manufacturing operations can realize it*, while delegating deterministic execution to diverse, independently safeguarded tools and facilities. It should be able to coordinate polymers, metals, textiles, composites, electronics, optics, microfabrication, assembly, inspection, and recycling without presuming one universal printhead or chamber.

## Abstract

Additive manufacturing, CNC machining, electronics assembly, lithography, fiber placement, chemical processing, and robotics have largely developed specialized software representations and machine control stacks. This separation makes it difficult to manufacture artifacts combining rigid and flexible structures, conductive networks, continuous fibers, embedded or printed electronics, optical elements, and multiple length scales. Oblivion Forge is proposed as an open-source research program for an agent-assisted, machine-independent fabrication representation and orchestration system. It separates an **intelligent planning layer**, responsible for reasoning about material interactions and candidate processes, from a **typed manufacturing compiler**, responsible for validating process dependencies and compiling instructions, and from **deterministic local machine controllers**, responsible for execution under independent safety protections.

The proposal encompasses independently moving toolheads; additive, subtractive, solid-state, assembly and textile operations; five-axis and robotic motion; thermal and optical processing; optical wavelength-selective and nonlinear conversion layers; vacuum or controlled-atmosphere processes; silicon and non-silicon electronics; organic, inorganic, recycled, and graded materials; and structures with intentionally bonded, sliding, woven, or unconstrained interfaces. A representative research question asks whether one intermediate representation (Forge IR) can preserve material, interface, process, geometric, temporal, safety, and provenance requirements across heterogeneous manufacturing backends. The document reviews relevant open-source systems and established physical research, identifies limitations and falsifiable hypotheses, proposes benchmark families, and maps the research to Oblivion Forge's existing job/session and authorization architecture. It does **not** claim that a universal fabricator has been built, that every combination of materials is physically compatible, or that computational material models replace real-world validation.

**Keywords:** hybrid manufacturing; multi-material fabrication; multi-axis robotics; computer-aided manufacturing; programmable textiles; additive manufacturing; lithography; nonlinear optics; foundation models for materials; manufacturing intermediate representation; open-source science; digital twins.

---

## 1. Problem statement and motivation

The envisioned system is not merely a metal 3D printer or a printer with many nozzles. It is a *fabrication suite*: a coherent description of heterogeneous physical artifacts and the manufacturing operations needed to produce them. It may employ one workstation, a house-sized arrangement of work cells, or a distributed set of specialized machines. Its physical scale can vary independently of its logical architecture.

Today's tools are competent within narrower domains. Slicers turn printable geometry into extrusion paths; CNC systems perform high-rigidity material removal; pick-and-place machines position prefabricated electronic parts; lithography tools pattern light-sensitive coatings; and knitting languages express textile actions. A mixed object may require all these operations plus bonding, metrology, atmosphere control, thermal conditioning, and handling. Crossing these boundaries often loses the relationships between materials and interfaces.

**Primary research problem:** Can a validated, extensible, machine-independent *representation of fabrication intent and operations* support heterogeneous, multi-scale, multi-material manufacturing while preserving the constraints required for safe, repeatable execution?

The proposal explicitly distinguishes:

1. **Intent:** the function an object or system should perform, described by a person or agent.
2. **Design:** geometry, materials, interfaces, behavior, tolerances, and topology.
3. **Manufacturing plan:** ordered or concurrent process operations, prerequisites, fixtures, consumables, metrology, and approvals.
4. **Machine execution:** deterministic, locally enforced procedures translated into hardware-specific commands.
5. **Evidence:** what was actually produced and measured, including unresolved differences from predictions.

An agent can understand *why* carbon-fiber strands should follow a load path; a machine need only know *where and how* to position them under an authorized procedure. Intelligent interpretation must not be delegated to a real-time control loop as a substitute for motion safety, electrical interlocks, or material-specific operating procedures.

## 2. Scope and explicit non-goals

**In scope:** material deposition and removal; wire-fed and solid-state metal operations; polymer extrusion; mold/casting workflows; simultaneous or cooperative toolheads; CNC machining; controlled thermal processing; robotic insertion; fiber winding, weaving and placement; selective bonding; origami/4D structures; wood- and cellulose-based materials; bone-derived and other biological-origin feedstocks where lawful and appropriately handled; optical printing; photolithography; printed conductors and electronic patterns; semiconductor design integration; inspection; physics-based simulation; material discovery; recycling; and software interoperability.

**Not assumed:** one apparatus can safely combine every process; all material pairs bond; a vacuum alone cold-welds arbitrary objects; lasers can cool ordinary metals; a deposited transparent layer can arbitrarily change any light wavelength; a modest lithography system can manufacture a modern CPU; machine-learning models faithfully predict all manufacturing phenomena; or raw elements can be converted directly into arbitrary objects. The word *universal* here refers to extensible **orchestration and representation**, not unlimited physical capability.

**Research stance:** broad ambition is acceptable, but every proposed physical effect must be tagged as (i) established, (ii) demonstrated in a narrower context, (iii) plausible and untested in this integration, or (iv) speculative/unsupported.

## 3. Relevant prior art and research landscape

### 3.1 Hybrid and multi-axis manufacturing

Oak Ridge National Laboratory (ORNL) has demonstrated a workflow combining additive friction stir deposition (AFSD), structured-light scanning, and CNC machining of aluminum components [1, 2]. AFSD forms deposits through frictional heating and plastic flow rather than melting the deposited metal. This is important for the earlier idea of making aluminum workable without fully liquefying it: hot metal can be plastically formed, and some aluminum alloys can also be processed in a semi-solid solid-plus-liquid range. Neither behaves like ordinary thermoplastic filament; material-specific force, microstructure, oxidation, and flow constraints apply.

Multi-axis tool orientation is established. LinuxCNC documents five-axis forward/inverse kinematics, including rotary/tilting tables and tool orientation [3]. Multiple independently controlled heads offer further possibilities—parallel work on separate regions, sequential tool handoffs, or synchronized cooperative operations—but make collision avoidance, thermal interference, alignment, and shared-workpiece state critical.

### 3.2 Fibers, flexible materials and 4D structures

Carbon fiber consists of extremely fine continuous filaments grouped into tows, which can be woven, braided, stitched, wound, placed along load paths, and consolidated with a matrix material. Toray documents continuous carbon-fiber tow, weaving, braiding and multiaxial textiles [4]. **Uncured fiber cloth is flexible; conventional cured fiber-reinforced resin composites are generally much stiffer.** Selectively bonded textiles, compliant matrices, tailored fiber paths, fold hinges, and shape-memory composites can enable programmed mobility rather than requiring full layer-to-layer fusion.

Electrothermally activated origami using continuous carbon-fiber-reinforced composites has been demonstrated [5]. Harvard's Wyss Institute describes 4D printed hydrogel composites whose wood-derived cellulose fibril orientation programs direction-dependent swelling [6]. These examples support treating fiber orientation, weave, local stiffness, swelling, strain, and temporal transformations as first-class design fields rather than afterthoughts.

### 3.3 Electronics and microfabrication

Printed conductive traces and component insertion are distinct from fabrication of active semiconductor transistors. OpenPnP provides open-source component placement [7]. OpenROAD, LibreLane and OpenRAM provide parts of semiconductor design and SRAM generation workflows, but producing physical chips also requires process-design kits, deposition, masks or direct-write lithography, etching, doping where relevant, clean processing, and extensive verification [8–10]. For low-density electronics, coarser feature sizes may be useful—yet making even simple reliable transistors remains significantly harder than printing copper traces.

The openMLA initiative researches open-hardware maskless lithography and describes a low-cost design goal around five-micrometer patterning for one early project, with active development moved to Codeberg [11]. That is a plausible specialized **work cell**, not something that belongs in the dusty chamber of a machining or welding station.

### 3.4 Optical conversion and volumetric processing

The proposed idea of fabricating an optical layer so incoming light can reach and selectively activate material beneath it deserves serious investigation. Nonlinear optical metasurfaces have demonstrated frequency conversion, including near-infrared-to-ultraviolet conversion [12]. Triplet-fusion upconversion nanocapsules have been used for volumetric 3D printing [13]; another study reports upconversion-assisted multi-material stereolithography capable of writing through previously printed regions [14]. These are research precedents, **not** demonstrations that arbitrary solid printed objects can convert arbitrary incident wavelengths at will.

This distinction motivates a dedicated research program in optical process planning, energy transmission, wavelength conversion, and spatially selective internal activation.

## 4. Proposed system architecture

Forge should be **facility-agnostic**: it can orchestrate one printer or multiple specialist rooms without knowing in advance how many actuators or workstations exist. A machine/cell advertises capabilities; an operation declares required capabilities. Planning, compilation, and execution remain distinct.

```text
Human / Agent Intent
        |
        v
Design and Requirements Model
  - geometry / kinematics / tolerances
  - materials / fiber orientation / electronics / optics
  - interface relationships / desired time response
        |
        v
FORGE IR  <-->  Knowledge, Evidence and Model Registry
        |
        v
Typed Manufacturing Planner + Compiler
  - process selection, sequencing and parallelism
  - compatibility and hazard checks
  - uncertainty / verification / approvals
        |
        v
Job / Resource Orchestrator (DRAGON, AETHER, Forge session)
        |
        +----------------------+-----------------------+
        v                      v                       v
Polymer/CNC cell       Optics/microfab cell     Metal/textile/assembly cells
local controller       local controller         local controller
local safety            local safety             local safety
        \______________________|_______________________/
                               |
                               v
                    Measurements + Evidence
                               |
                               v
                      Model refinement / DOOM
```

### 4.1 Multiple heads and facilities

A *head* may deposit, mill, weld, place, sense, heat, cool, stitch, or expose. A *cell* is the local controlled environment in which one or more heads operate. A *facility* is an arrangement of cells with transfer logistics. This separation accommodates five-axis stages, multi-head gantries, six-axis arms, fixture changers, and clean, vacuum, inert, or high-temperature chambers. Toolchanging need not be limited to one head at a time.

Concurrent operations must require explicit mutual exclusion on shared space, fixtures, power budgets, thermal zones, optical paths, and materials. If two heads touch the same workpiece simultaneously, the compiler must account for both trajectories, time-dependent deformation, force balance, and interaction with incomplete geometry.

### 4.2 The agent–fabricator boundary

The **Forge Agent** proposes designs, reasoning steps, simulations and process choices. The **Forge compiler** validates declarative constraints and transforms the authorized process graph into device-specific procedures. **Local machine controllers** perform motion and process control deterministically with independent interlocks. AI should not directly author an unchecked heating, laser emission, machining, pressure, or motion command to a live machine.

### 4.3 Material, feature and interface semantics

A product representation should record not only material identity but spatial variation and relationships. Relevant interface types include bonded, brazed/welded, cold-pressure-joined, mechanically interlocked, sliding, separated, stitched, woven, laminated, embedded, and temporarily supported. Interfaces can also have electrical, optical, magnetic, thermal, chemical, and moisture-transport properties. A *free-moving region* must remain free after manufacturing and post-processing; a *selectively bonded region* must not accidentally fuse during a later thermal stage.

A continuous fiber or conductive trace is better represented as a **path with tangent, tension and connection semantics** than merely as colored voxels. A printed circuit might be represented using a connectivity graph in addition to geometry; a flexible textile requires stitch, crossing, and anchor relationships. The same finished geometry may be manufacturable through different processes with different performance and cost.

## 5. Forge Intermediate Representation (Forge IR)

The proposed Forge IR is a typed, versioned, machine-independent intermediate representation for *artifact intent* plus a separate, lower-level *fabrication operation graph*. These should be independently inspectable and linked by traceability references.

**Design IR:** coordinate frames, parametric/mesh/voxel geometry, region IDs, material definitions and batch provenance, oriented fibers, graded compositions, conductor nets, optical fields, flexible/rigid constraints, interface graph, behavioral requirements, uncertainty, units, and tolerances.

**Process IR:** operation ID, inputs/outputs, capability requirements, tool pose/trajectory or abstract procedure, start conditions, fixtures, consumables, energy and atmosphere requirements, expected transformed state, process guards, dependencies, resources, verification and human approval.

**Machine capability manifest:** supported processes; axes and reachable workspace; tool transforms; loads, temperatures, wavelengths, optical power and beam quality; atmosphere; metrology resolution; supported material/feedstock classes; operational safety class; firmware/adapter version; confidence/calibration status.

Illustrative schema fragment (non-executable):

```yaml
forge_ir: "oblivion.forge.design/v0-proposal"
artifact:
  geometry: model://example/wing-shell
  regions:
    - id: shell
      material: carbon_fiber_composite
      orientation_field: field://load-aligned-tows
    - id: hinge
      material: flexible_polymer
      interfaces: [selective_bond_to_shell]
    - id: circuit
      material: copper
      connections: netlist://sensors
  requirements:
    - {kind: bending_compliance, region: hinge}
    - {kind: electrical_continuity, region: circuit}
process_graph:
  - {id: a, kind: fiber_place, produces: shell}
  - {id: b, kind: polymer_deposit, after: [a], produces: hinge}
  - {id: c, kind: conductor_deposit_or_insert, after: [b], produces: circuit}
  - {id: d, kind: inspect, after: [c], verifies: [hinge, circuit]}
policy:
  actuation: human_authorization_required
  safety: independent_local_interlocks
```

A useful compiler should **refuse** plans whose material/operation pair lacks a validated compatibility claim, rather than fabricate unsupported assumptions. It should emit a machine program only if all required safety and capability preconditions can be established. Unknown is not equivalent to safe.

## 6. Material and process research portfolio

### 6.1 Recycled aluminum and copper

Soda cans offer a compelling recycled-feedstock case study, but used beverage containers contain coatings, mixed alloys, and potential contaminants. Recycling into suitable casting stock is different from producing qualified wire or laser powder. Wire-arc additive manufacturing, molten-metal jetting, casting, and AFSD each require different feedstock specifications, atmospheres and quality controls. For copper, electrical/thermal conductivity, oxidation and optical reflectivity are relevant; green-wavelength laser processing has been researched as an alternative to near-infrared for copper.

A crucial hazard constraint: **do not attempt to atomize molten aluminum with ordinary compressed air to make printing powder.** Fine aluminum dust can form combustible/explosible atmospheres. Powder-based metal manufacturing requires specialized powder handling, containment, fire protection and qualified operators. The platform can research or model powder-bed processes without making unsafe home powder generation part of its reference implementation.

### 6.2 Softened rather than fully molten metals

Hot forming and AFSD demonstrate that a metal may be plastically deformed without complete melting [1, 2]. Semi-solid metal processing exploits an alloy-specific solid-plus-liquid temperature range; pure elements do not have the same broad mushy interval under ordinary equilibrium conditions. A proposed head must specify applied load, strain rate, contact material, heating mechanism, oxidation control and microstructural acceptance criteria—not just nozzle temperature.

### 6.3 Cold joining, vacuum and controlled atmospheres

Cold welding is a solid-state bond under favorable surface cleanliness and intimate contact/pressure conditions. Vacuum can help preserve clean surfaces, but **vacuum alone does not reliably weld typical oxidized aluminum parts**. Friction, ultrasonic and pressure-based joining may be more appropriate for different pairs of materials. Vacuum also changes heat transfer and complicates mechanisms, feedthroughs and outgassing; it belongs in a dedicated capability definition.

### 6.4 Insertion and graded structures

Some components should be fabricated in place, others inserted: copper conductors, magnets, bearings, ceramics, synthetic diamond thermal spreaders, optical chips, sensors or fully prefabricated dies. Diamond is a heat-spreading material under suitable interfaces, not a stand-alone cooler. Non-fused regions enable joints, chains, bearings, hinges, cloth, and interlocking metamaterials. Graded material regions should include composition gradients *and* validated process/interface assumptions.

### 6.5 Organic and bio-derived materials

Wood, cellulose, bamboo fibers, proteins, bone-derived composites, and biodegradable polymers extend the design space. Each adds moisture sensitivity, anisotropy, degradation, temperature limits, and possible contamination or ethical sourcing concerns. Biological and medical applications require their own biocompatibility/sterility and regulatory validation; a process acceptable for craft fiber is not automatically appropriate for implanted material. The existing cellulose-orientation research [6] offers a grounded example of programmed shape response.

## 7. Optical material engineering: wavelength, depth and selectivity

This section addresses the novel research idea most clearly raised in the current discussion: **can a deposited or embedded optical structure alter, route or gate incident light so that a later beam selectively processes a buried region?**

### 7.1 What a printed optical layer can and cannot do

A passive linear layer can transmit, reflect, absorb, scatter, polarize, refract, or diffract light. It can filter wavelengths or change beam phase and direction. It does **not** ordinarily change the optical frequency merely by refraction. Actual frequency conversion requires processes such as fluorescence, phosphor emission, stimulated emission, nonlinear mixing, harmonic generation, or other matter–light interactions with appropriate energy supply and efficiencies.

A compact research model should account for attenuation in a simple absorbing medium, e.g. `I(z) = I(0) exp(-αz)`, while acknowledging that a multilayer, scattering, nonlinear, anisotropic or high-intensity material needs a richer electromagnetic/thermal model. Spatial targeting further requires beam focusing, index matching, aberration control, dispersion, scattering estimates, and knowledge of the already-printed geometry.

### 7.2 Candidate process families

- **Spectral transmission/filter layers:** select which incoming wavelengths reach the interior; established optics, but no inherent frequency conversion.
- **Embedded wavelength-converting particles:** absorb excitation and emit a different spectrum; demonstrated in photopolymerization/upconversion contexts [13, 14]. Conversion is finite and often isotropic, not automatically a perfectly localized replacement laser beam.
- **Nonlinear photonic regions/metasurfaces:** engineered structures generate harmonics or mixed frequencies under appropriate illumination [12]; typically demanding fabrication, pump, efficiency and phase-matching conditions.
- **Two-color or multiphoton activation:** exploit nonlinear/threshold photochemistry to confine polymerization in 3D; material- and resin-specific [13, 14].
- **Waveguides, diffractive layers, microlenses:** route/focus photons but require optically suitable materials and tolerances.

### 7.3 Falsifiable optical research hypothesis

**H-O1:** For a specified transparent or partially transparent printed stack, a compiler can choose source wavelength, optical layer composition, geometry and exposure parameters to activate a buried photoreactive target while preserving surrounding regions within measured damage limits.

Independent variables: stack thickness, absorption/scattering, excitation wavelength, nanoparticle concentration or engineered optical geometry, exposure dose, thermal environment and target depth. Outcomes: conversion spectrum and efficiency, delivered dose profile, lateral/axial localization, unintended cure/damage, heat generation, repeatability and aging. Required baseline: direct illumination without the conversion layer. **Failure criteria:** insufficient dose contrast, unacceptable collateral heating, poor reproducibility, incompatible processing temperatures, or inability to characterize internal conversion. This is not a claim of general-purpose subsurface metal welding.

### 7.4 Multi-wavelength processing architecture

Rather than demanding a single infinitely tunable laser, define independent optical modules by wavelength range, CW/pulsed operation, pulse width, power, beam delivery, spot quality, focus and calibrated output. Tunable sources can be integrated where appropriate, but feasible wavelength ranges depend on the source and nonlinear conversion system. High-power optical equipment requires engineering controls (enclosure, interlocks, beam dumps, exposure prevention and process fumes management); a spectrum selection request cannot bypass them.

## 8. AI and physics foundation-model layer

There are useful existing scientific models, including from university groups and research labs. They do **not** remove the need for specialist solvers, measured parameters, or experiments.

- **MatterGen (Microsoft Research):** a generative model proposing candidate *inorganic material structures*; useful for inverse design research, not a manufacturing-process simulator [15].
- **MatterSim (Microsoft Research):** machine-learned atomistic energies/forces/stresses and materials behavior across elements, pressure and temperature ranges; its model card warns about accuracy limitations for organic polymeric systems, interfaces and long-range effects [16].
- **MACE (academic collaboration):** open-source equivariant machine-learned interatomic potentials and foundation-model checkpoints; different checkpoints target distinct chemical regimes and carry model-specific licenses [17].
- **FAIR Chemistry / UMA:** pretrained atomistic systems models spanning inorganic materials, molecules and catalysts, but each domain/task has its own data assumptions [18].
- **Meep:** open-source finite-difference time-domain electromagnetics, relevant to light propagation and some nonlinear optical modeling [19].

These can be combined with classical finite-element thermal/structural solvers, computational fluid dynamics, electromagnetic simulation, kinetic chemistry, materials databases and empirical calibration, provided **model scope and uncertainty** are declared. A model predicting atomic forces does not automatically predict the strength of a macroscopic printed weld, optical transparency of a printed polymer, or lifetime of a composite hinge.

Proposed inference sequence: identify the physical phenomenon; select candidate model(s) by validated scope; determine missing measurements; simulate; attach uncertainty; reject unsupported extrapolations; compare with independent solver or data when possible; acquire real experimental evidence only through approved workflows; update the evidence registry. The agent can synthesize conclusions, but every claim must retain its source model and test conditions.

## 9. Open-source integration candidate register

The table is a **discovery register**, not an imported dependency tree. Before code reuse, verify the current upstream revision, license including dependencies and weights, API/version, reproducibility, maintenance status and export-control or process limits if relevant.

| Domain | Candidate | Proposed adapter or contribution |
|---|---|---|
| CAD / geometric modeling | [FreeCAD](https://github.com/FreeCAD/FreeCAD) | solids, parameters and machining geometry |
| Programmable paths | [FullControl](https://github.com/FullControlXYZ/fullcontrol) | explicit nonstandard deposition paths |
| Polymer slicing | [PrusaSlicer](https://github.com/prusa3d/PrusaSlicer) | slicer and multi-material toolpath research |
| CNC / 5-axis | [LinuxCNC](https://github.com/LinuxCNC/linuxcnc) | kinematics and machine controller adapter |
| Motion planning | [MoveIt 2](https://github.com/moveit/moveit2) | robot trajectories and collision planning |
| Picking / assembly | [OpenPnP](https://github.com/openpnp/openpnp) | component placement jobs |
| Lithography | [openMLA](https://github.com/openMLA) / [Codeberg](https://codeberg.org/openMLA) | projection pattern alignment and exposure |
| Circuit CAD | [KiCad](https://github.com/KiCad/kicad-source-mirror) | layouts, connections, manufacturing exports |
| Silicon physical design | [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) | RTL to physical layout interfaces |
| Silicon design flow | [LibreLane](https://github.com/librelane/librelane) | reproducible EDA tool orchestration |
| SRAM design | [OpenRAM](https://github.com/VLSIDA/OpenRAM) | parametrized memory-macro workflows |
| Machine-neutral knitting | [Knitout](https://github.com/textiles-lab/knitout) | low-level textile IR precedent |
| Fiber winding | [FiberPath](https://github.com/fiberpath/fiberpath) | winding paths and machine simulator |
| EM simulation | [Meep](https://github.com/NanoComp/meep) | optical/EM simulation |
| Atomistic simulations | [MACE](https://github.com/ACEsuit/mace) | pretrained force fields / physics inference |
| Atomistic simulations | [MatterSim](https://github.com/microsoft/mattersim) | scientific materials inference |
| Material generation | [MatterGen](https://github.com/microsoft/mattergen) | proposed crystal structure search |
| General atomistic models | [FAIR Chemistry](https://github.com/facebookresearch/fairchem) | task-conditioned universal atomistic model |

**Integration policy:** prefer invoking each upstream tool as an independent service or process with a documented adapter and pinned revision. Do not conflate software licenses with data/model-weight licenses. Adapters should not automatically import or copy a codebase into Forge. A GPL/AGPL module, a permissively licensed plugin, and a proprietary process-design kit can have very different redistributability consequences. A public GitHub repository is not proof of an open-source license.

## 10. Existing Oblivion Forge: continuity rather than replacement

The present proposal is an **extension**, not a declaration that existing Forge capabilities are completed. Available historical project material documents a backend-neutral `oblivion.forge.session/v1` design covering **Model**, **Render**, and **Fabrication** Forge; a proposed/partially deployed F6 Go API and MCP bridge; sixteen typed MCP tools in one October 2026 acceptance record; and separate physical fabrication commissioning. The sources also describe subsequent Rust 2024 toolchain/dependency preparation; these records should be reconciled against the current canonical source and runtime before changing code.

The historical session design specifies:

- **DRAGON:** workflow ordering, approval transitions and audit/policy decisions.
- **AETHER:** durable task/session state, machine leases and recovery policy.
- **Forge Agent:** bounded specialization planning and execution within an authorized session.
- **Kubernetes:** compute/resource scheduling (not real-time hardware actuation).
- **Local equipment safety:** independently enforced protections, with no implicit authorization from an agent or Kubernetes state.

This new research proposes additional design/compilation layers **above** the current specialized Forge backends and can preserve prior API semantics through versioned adapters. Physical actuation, device calibration, heating, laser emission, tooling, and writes remain operation-specific, human-gated activities. The ongoing work's exact head/commit, readiness and test results must be verified before publication of implementation claims.

## 11. Research questions and experimental hypotheses

**RQ1 — Representation.** Can one versioned IR encode an artifact containing a metal support, compliant woven region, conductor network, mechanically movable interfaces and optical behavior without flattening away essential information?

**RQ2 — Compilation.** Can the same design IR compile to at least two independent, capability-distinct manufacturing process graphs, with equivalent declared artifact requirements and explicit limitations?

**RQ3 — Multi-head scheduling.** Can a planner improve throughput with concurrent operations while showing collision-free trajectories, resource isolation, consistent workpiece-state handoffs and stable real-time control?

**RQ4 — Cross-scale registration.** Can a facility maintain traceable coordinate transforms and tolerances when a part passes from millimeter-scale assembly to microfabrication?

**RQ5 — Materials and interfaces.** Can the system accurately distinguish a required bond from a sliding, interlocked, woven or insulated interface, and predict when a later step destroys that intended relation?

**RQ6 — Optical layer processing.** Can known photoactive materials and engineered optical structures support verified, depth-selective transformation beneath previously fabricated layers without unacceptable collateral effects (H-O1)?

**RQ7 — Physics model selection.** Does a domain-aware ensemble of specialist solvers plus foundation models outperform a single general model in well-defined out-of-distribution material/process tests?

**RQ8 — Process reproducibility.** Can complete provenance (inputs, tool calibrations, model weights, assumptions, approvals, measurements) enable repeatable comparative manufacturing studies across laboratories?

**RQ9 — Automation boundary.** Can independent safety policies reliably prevent simulation or agent instructions from becoming unauthorized physical operations, even under stale network state, failed tools and retried tasks?

**RQ10 — Accessibility.** Can the software be useful to researchers and hobbyists operating only simulators or low-cost polymer equipment, before expensive metal or microfabrication facilities become available?

## 12. Validation strategy, metrics and negative controls

A research program must define success and failure before selecting impressive demonstrations. Proposed benchmark families:

| Benchmark | What is measured | Negative or baseline control |
|---|---|---|
| IR expressiveness | percentage of required material/interface/connectivity assertions retained | STL/mesh plus conventional slicer |
| Multi-backend planning | accepted operation graphs; missing-capability detection; auditability | independent manual tool chains |
| Multi-head scheduling | collision incidents (target zero), makespan, utilization, schedule recovery | sequential single-head plan |
| Cross-cell registration | positional, angular and surface error after transfers | no metrology corrections |
| Material compatibility | measured bond strength, conductivity, modulus, porosity, damage | unvalidated material pairing |
| Fiber/4D structure | target deformation error, cycles-to-damage, directionality | isotropic or randomly oriented fiber |
| Optical buried activation | 3D dose localization, conversion efficiency, parasitic heat/damage | direct light without converting layer |
| Model reliability | prediction error, calibration, out-of-distribution error, abstention rate | single-model or generic surrogate |
| Workflow evidence | percent of results reproducible using pinned inputs, logs and models | undocumented interactive workflow |
| Safety admission | unauthorized actuation blocked, interlock effectiveness | deliberate simulated rejected commands |

The **DOOM optimization loop** can optimize candidate implementations on time, material, energy, quality, and older-hardware compatibility, but **only within approved constraints**. Safety and material validity are hard feasibility gates rather than scalar metrics to trade against speed. Computational improvements should be benchmarked separately from physical improvements to prevent circular claims.

At the current conceptual stage, **no integrated benchmark results are claimed**. The paper's contribution is the proposed research design and testable architecture.

## 13. Major limitations and honest feasibility assessment

1. **Physics coverage is incomplete.** No known single open model adequately captures chemistry, bulk mechanics, light propagation, heat, flow, fatigue and manufacturing quality for arbitrary materials/processes.
2. **Material interactions are path-dependent.** Deposition order, residual stress, contaminants, humidity, oxidation, thermal cycles, and curing affect outcomes.
3. **Scale conflicts are severe.** Welding or metal cutting and micron-scale lithography have fundamentally different vibration, contamination, thermal and safety needs.
4. **Optical conversion has bounds.** Absorption, scattering, phase matching, conversion quantum yield and optical damage restrict depth and spatial precision.
5. **Semiconductor manufacturing cannot be reduced to low-resolution lithography alone.** Devices require functioning materials, contacts, process control and metrology.
6. **Metal powder and vacuum processes introduce hazards.** Flammable dust, inert-gas asphyxiation, moisture explosions, high-power radiation, energetic equipment and pressure boundaries require specialist controls.
7. **Manufacturing quality must be measured.** A visually good part can be mechanically or electrically defective. A foundation-model prediction is not a certification.
8. **Multi-head throughput is not automatically better.** Tool interference, calibration and process waiting time can negate concurrency benefits.
9. **Licenses and patents matter.** Open-source dependencies cannot simply be copied or relicensed; physical processes may have patent constraints.
10. **Economic universality is unrealistic.** An accessible shared specification is plausible; an affordable device for every fabrication process is not an initial claim.

## 14. Publication and collaboration program

This project can be published without building a house-sized facility. The first research contribution would be **a written specification and interoperable software prototypes**, followed by opt-in simulation and independent process experiments. The paper is intentionally not a purchase list or immediate construction tutorial.

Possible independent deliverables:

- A requirements/novelty review with a dated prior-art register.
- Forge Design IR and Process IR schemas, type checker and conformance fixtures.
- Capability manifests for simulated additive, subtractive, textile, optical and electronic operations.
- A planner/compiler prototype running entirely on synthetic or simulated machinery.
- Adapter specifications for upstream tools, with license and revision provenance.
- Model-selection and verification services with clear validity ranges.
- Benchmark datasets containing **negative cases**, not just successes.
- A safety case describing non-bypassable local physical controls.
- Later peer-reviewed process-specific experiments by appropriately equipped collaborators.

**Community design:** clear separation of stable interfaces from experimental branches; reproducible fixtures; documented constraints; explicit citation and contribution policy; research-issue tags for feasible/unknown/refuted concepts; and permission to publish negative results. An open repository should link to upstreams rather than claiming their prior inventions as Forge's own.

### Possible dedicated repository layout (future)

```text
oblivion-forge-research/
  README.md
  paper/oblivion-forge-research-program.md
  research/questions.md
  specifications/forge-ir-proposal.md
  specifications/capability-manifest-proposal.md
  references/open-source-candidates.csv
  benchmarks/README.md
  governance/safety-and-human-authorization.md
  LICENSE-RESEARCH.md
```

A future release should clearly distinguish **proposal**, **prototype**, **measured result**, and **qualified capability**. Suggested indicators: `CONCEPT`, `SIMULATED`, `EXPERIMENTAL`, `VALIDATED`, `REJECTED`.

## 15. Conclusion

The strongest plausible form of Oblivion Forge is not an impossibly capable printhead. It is a coherent *research and software ecosystem* that describes functional artifacts across materials and scales, chooses from physically constrained fabrication operations, coordinates multiple heads and specialized cells, and verifies outcomes without confusing intelligent reasoning with deterministic equipment control. Recycled metals, solid-state joining, optical wavelength conversion, selective interior curing, lithography, printed electronics, continuous fibers, wood-derived responsive structures, and integrated assemblies all have relevant scientific precedents—but extending and combining them remains an open research effort.

The proposed novelty is therefore an **interoperable, typed, evidence-aware manufacturing representation and planner** spanning processes usually isolated from one another. Its success should be judged not by promises of universal manufacturing, but by whether independent backends can faithfully implement the same requirements, refuse invalid combinations, preserve intended interfaces, and produce reproducible results. This is a defensible, potentially publishable open-source agenda even before the project owns expensive fabrication equipment.

---

## References and source register

These links were checked for relevance in October 2026; this is an initial research bibliography, **not a systematic literature review**. References to the existing Oblivion AOS source in §10 summarize supplied project materials and require reconciliation with the canonical repository before public implementation claims.

1. Kincaid, J., et al. (2023). *Hybrid Manufacturing: Combining Additive Friction Stir Deposition, Metrology, and Machining*. ORNL / Springer. https://doi.org/10.1007/978-3-031-22661-8_1
2. Kincaid, J., et al. (2023). *Process planning for hybrid manufacturing using additive friction stir deposition*. ORNL. https://www.ornl.gov/publication/process-planning-hybrid-manufacturing-using-additive-friction-stir-deposition
3. LinuxCNC Documentation. *5-Axis Kinematics*. https://www.linuxcnc.org/docs/html/motion/5-axis-kinematics.html
4. Toray Composite Materials. *Carbon fiber manufacturing: weaving, braiding, multiaxial reinforcement*. https://www.toraycma.com/applications/carbon-fiber-applications/
5. Wang, Y., et al. (2024). *Electrothermally controlled origami fabricated by 4D printing of continuous fiber-reinforced composites*. Nature Communications. https://doi.org/10.1038/s41467-024-46591-3
6. Wyss Institute, Harvard. *4D Printing of Shapeshifting Devices*. https://wyss.harvard.edu/technology/4d-printing/
7. OpenPnP Project. *Open-source SMT pick and place*. https://github.com/openpnp/openpnp
8. OpenROAD Project. *OpenROAD*. https://github.com/The-OpenROAD-Project/OpenROAD
9. LibreLane Project. *ASIC implementation flow infrastructure*. https://github.com/librelane/librelane
10. OpenRAM Project. *OpenRAM*. https://github.com/VLSIDA/OpenRAM
11. openMLA Project. *Open-hardware maskless lithography aligners*. https://github.com/openMLA ; current development: https://codeberg.org/openMLA
12. Gao, J., et al. (2021). *Near-infrared to ultra-violet frequency conversion in chalcogenide metasurfaces*. Nature Communications. https://doi.org/10.1038/s41467-021-26094-1
13. Sanders, S. N., et al. (2022). *Triplet fusion upconversion nanocapsules for volumetric 3D printing*. Nature. https://doi.org/10.1038/s41586-022-04485-8
14. *Upconversion 3D printing enables single-immersion multi-material stereolithography* (2023). ScienceDirect record. https://www.sciencedirect.com/science/article/pii/S2352940723001245
15. Zeni, C., et al. (2025). *A generative model for inorganic materials design* (MatterGen). Nature. https://doi.org/10.1038/s41586-025-08628-5 ; https://github.com/microsoft/mattergen
16. Microsoft Research. *MatterSim model card and repository*. https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md
17. ACEsuit. *MACE foundation models and code*. https://github.com/ACEsuit/mace ; https://github.com/ACEsuit/mace-foundations
18. FAIR Chemistry. *Open data and universal models for atomic systems*. https://fair-chem.github.io/ ; https://github.com/facebookresearch/fairchem
19. Meep Project. *Open-source FDTD electromagnetics*. https://github.com/NanoComp/meep
20. FullControl Project. *Programmable toolpath design*. https://github.com/FullControlXYZ/fullcontrol
21. CMU Textiles Lab. *Knitout machine-independent knitting instructions*. https://github.com/textiles-lab/knitout
22. FiberPath Project. *Composite winding, planning and simulation*. https://github.com/fiberpath/fiberpath
23. University/industrial research. *Light-sheet 3D microprinting via two-colour two-step absorption*. Nature Photonics (2022). https://www.nature.com/articles/s41566-022-01081-0
24. Review. *Nanoparticle-enhanced vat photopolymerization in additive manufacturing* (2026). https://doi.org/10.1016/j.cis.2025.103690
25. Microsoft Research. *Materials research program (MatterGen and MatterSim)*. https://www.microsoft.com/en-us/research/project/materials/
26. FreeCAD Project. *FreeCAD source and license*. https://github.com/FreeCAD/FreeCAD
27. Open-source robotics. *MoveIt 2*. https://github.com/moveit/moveit2
28. KiCad Project. *KiCad source*. https://github.com/KiCad/kicad-source-mirror
29. Prusa Research. *PrusaSlicer*. https://github.com/prusa3d/PrusaSlicer
30. FAIR Chemistry. *Pretrained model scope and the UMA recommendation*. https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/models.md

### Internal project records consulted (not public citations)

- Draft `oblivion.forge.session/v1` session contract: separation of DRAGON, AETHER and Forge, operation-specific authorization, durable evidence and leases.
- `Fabrication Forge v2.5.2` mission/readiness artifact: OctoPrint/camera commissioning constraints and prohibition on unapproved actuation.
- October 2026 F6/MCP bridge notes: 16-tool bridge, authentication tests and previously blocked client-registration/commissioning issues.
- Conversation history describing F6.0–F6.2, Rust 2024 preparation, fabrication/model/render split, and DOOM optimization goals.

---

*Public release note: This began as an informal late-night thought experiment and is published to invite critique and collaboration. It contains no claimed original experimental results, no borrowed upstream source code, and no authorization to operate machinery. A document/software license has not yet been selected; no reuse rights beyond those granted by applicable law should be assumed.*