From Efficiency Tool to System Enabler: An Evolutionary Study of AI-Driven Transformation in Smart Manufacturing Systems

The repository contains a comprehensive and well-documented agent-based model implemented in NetLogo. It studies how artificial intelligence evolves from a simple efficiency tool at the firm level into a core enabler of smart, green, and resilient manufacturing ecosystems. The work is grounded in the Technology–Institution–System (TIS) co-evolutionary framework and complex adaptive systems theory.
Here are the main highlights of the model and repository:

Main components of the simulation

1.Heterogeneous adaptive agents: 50 manufacturers + 100 suppliers

2.Government with dynamic fiscal and policy instruments

3.33×33 toroidal spatial grid (inspired by real clusters like G60 Sci-Tech Corridor)

4.AI capability develops across three generations (G1 → G2 → G3)

Core mechanisms

1.Distance-decaying knowledge spillovers

2.Green zone certification and diffusion

3.Counter-cyclical transformation fund with phased subsidy reduction

4.Emergent System Value Index (SVI) that drives nonlinear market demand

Five validated macro-patterns (P1–P4 + boundary condition)

1.S-curve adoption of AI and green technologies

2.Spatial evolution: point → cluster → network

3.Nonlinear takeoff of market demand after SVI threshold

4.Triple-buffer resilience against external shocks

5.Stagnation / low-level equilibrium when key conditions are weak

Real-world alignment

The model reproduces patterns observed in leading Chinese smart manufacturing cases:

1.Haier COSMOPlat (S-curve adoption)

2.G60 Sci-Tech Corridor & Yangtze River Delta EV cluster (spatial clustering)

3.CATL (nonlinear demand surge)

4.Sany Heavy Industry Lighthouse Factory (pandemic resilience)

5.Legacy regions without strong anchor firms or spillovers (stagnation)

How to run the model

Install NetLogo 6.4.0 or newer
Clone the repository:
git clone https://github.com/wsmlxqa/TIS-ABM-AI-Driven-Smart-Green-Manufacturing-System-Simulation.git
Open code/TIS_ABM.nlogo
Press Setup (uses baseline parameters from Table 2)
Press Go (runs 500 ticks ≈ 40 years, 1 tick = 1 month)

Key experiments you can easily replicate

1.Baseline run (dynamic governance enabled) → shows Pathway 1, 2, 3

2.Adjust spillover-radius or spillover-intensity → test spatial clustering strength

3.Change demand-svi-elasticity-β → compare linear vs. nonlinear demand growth

4.Switch between static subsidies, pure dynamic fund, or hybrid policy regime

5.Apply external shock (25% competitiveness drop at tick 200) → test resilience

Repository contents summary

1.All figures (1–10) with data (.csv) and Python plotting scripts

2.Sensitivity analysis (Appendix A.1–A.3 .xlsx)

3.Parameter and result tables (Table 1–8, D.12 .xlsx)

4.Graphical abstract & highlights documents

5.Pseudocode and algorithm description (PDF)

6.video (vedio.mp4)

This model provides a solid, reproducible platform for studying AI-driven industrial transformation, especially in the context of smart and green manufacturing clusters. It is particularly valuable for researchers interested in co-evolutionary dynamics, spatial economics, industrial policy design, and resilience under uncertainty.

If you have specific questions about running experiments, interpreting certain parameters, modifying the model, or comparing results with real cases, feel free to ask!
