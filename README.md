 From Efficiency Tool to System Enabler: An Evolutionary Study of AI-Driven Transformation in Smart Manufacturing Systems

This repository contains the complete NetLogo source code, data, figures, and documentation for the spatially embedded agent-based model developed in the paper:

From Efficiency Tool to System Enabler: An Evolutionary Study of AI-Driven Transformation in Smart Manufacturing Systems  
International Journal of Production Economics (under review / forthcoming).

The model implements a Technology–Institution–System (TIS) co-evolutionary framework grounded in complex adaptive systems (CAS) theory. It explores how artificial intelligence (AI) evolves from a firm-level efficiency tool into a genuine system enabler, driving the emergence of self-organizing, resilient, and sustainable smart manufacturing ecosystems.

 Overview

The simulation features four interacting components:
- Manufacturers and Suppliers as heterogeneous adaptive agents
- Government implementing dynamic fiscal and policy mechanisms
- Geographic Environment on a 33×33 toroidal grid (scaled to real-world clusters such as the G60 Sci-Tech Corridor)

Key mechanisms include:
- AI capability evolution across generations (G1–G3)
- Distance-decaying knowledge spillovers
- Green zone diffusion and certification
- Counter-cyclical transformation funds with phased subsidy attenuation
- Nonlinear market demand driven by the emergent System Value Index (SVI)

The model reproduces five macro-patterns validated against Chinese smart manufacturing clusters: S-curve adoption, spatial clustering, nonlinear demand takeoff, triple-buffer resilience, and boundary stagnation under weak conditions.

This repository ensures full transparency and reproducibility of the published research.

 Repository Contents

- `code/`  
  Main NetLogo model file (`TIS_ABM.nlogo`)
- `data/`  
  Initialization parameters, sample outputs, and validation datasets
- `figures/`  
  Simulation visualizations (spatial evolution, trajectory plots, policy comparisons)
- `docs/`  
  Supplementary materials aligned with paper appendices

 Getting Started

 Prerequisites
- NetLogo 6.4.0 or higher[](https://ccl.northwestern.edu/netlogo/)

 Installation & Running
1. Clone the repository:
   ```bash
   git clone https://github.com/wsmlxqa/TIE-ABM-AI-Driven-Smart-Green-Manufacturing-system-Simulation.git
   Open code/TIS_ABM.nlogo in NetLogo.
2.Press Setup to initialize:
    50 manufacturers, 100 suppliers
    33×33 grid with initial green patches
    Baseline parameters (see Table 2 in the paper)
4.Press Go to run for 500 ticks (~40 years, 1 tick = 1 month).
5.Monitor key indicators or export data via BehaviorSpace for analysis.

Key Scenarios (Section 4 of the paper)

  Baseline: Natural co-evolution with dynamic governance
  Policy comparison: Static subsidies vs. pure dynamic fund vs. hybrid regime
  External shock: 25% competitiveness loss at t=200 to test resilience
  Spatial evolution: Point → cluster → network diffusion of green zones

Adjust sliders (e.g., green-subsidy, carbon-tax, demand-svi-elasticity-β) to replicate scenarios.

Validation & Real-World Cases
Simulation patterns are validated through pattern-oriented modelling against:
  Haier COSMOPlat (Haier Smart Home Co., Ltd., China) – S-curve platform growth
  Yangtze River Delta EV cluster & G60 Sci-Tech Corridor – Point-to-cluster-to-network spatial diffusion
  CATL (Contemporary Amperex Technology Co., Limited, China) – Nonlinear demand takeoff
  Sany Heavy Industry Changsha Lighthouse Factory (Sany Heavy Industry Co., Ltd., China) – Triple-buffer resilience during 2020–2022 pandemic

Robustness & Sensitivity
Model robustness was assessed via multiple runs with varied random seeds and ±10% parameter perturbations (see Appendix: Sensitivity Analysis). All five macro-patterns remain qualitatively stable.
