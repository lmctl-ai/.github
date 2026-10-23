# lmctl-ai

Scientific computing you can run from one command: write a short [lmscript](https://lmctl.com/tools/lmscript/skill.html) program, and a static host binary computes, simulates and draws. Every picture below was made by the example it links to.

|  |  |  |
| :---: | :---: | :---: |
| <a href="https://github.com/lmctl-ai/lmplot"><img src="https://raw.githubusercontent.com/lmctl-ai/lmplot/main/docs/images/blackbody_planck.png" width="280" alt="Stellar spectra and the visible band"></a><br><b>lmplot</b> · plots and surfaces (gnuplot) | <a href="https://github.com/lmctl-ai/lmnum"><img src="https://raw.githubusercontent.com/lmctl-ai/lmnum/main/docs/images/lorenz.gif" width="280" alt="A Lorenz trajectory, animated"></a><br><b>lmnum</b> · numerical computing (Eigen, SUNDIALS) | <a href="https://github.com/lmctl-ai/lmfinance"><img src="https://raw.githubusercontent.com/lmctl-ai/lmfinance/main/docs/images/vol_surface.png" width="280" alt="A Heston implied-volatility surface"></a><br><b>lmfinance</b> · financial models (QuantLib) |
| <a href="https://github.com/lmctl-ai/lmspace"><img src="https://raw.githubusercontent.com/lmctl-ai/lmspace/main/docs/images/halley.png" width="280" alt="Halley's orbit and changing speed"></a><br><b>lmspace</b> · orbital dynamics (N-body, SPICE) | <a href="https://github.com/lmctl-ai/lmphysics"><img src="https://raw.githubusercontent.com/lmctl-ai/lmphysics/main/docs/images/incline_forces.png" width="280" alt="A measured force balance on a ramp"></a><br><b>lmphysics</b> · rigid-body mechanics (Project Chrono) | <a href="https://github.com/lmctl-ai/lmbio"><img src="https://raw.githubusercontent.com/lmctl-ai/lmbio/main/docs/images/repressilator.png" width="280" alt="Three repressors become a biological clock"></a><br><b>lmbio</b> · reaction networks (CVODE, SSA, SBML) |
| <a href="https://github.com/lmctl-ai/lmfluid"><img src="https://raw.githubusercontent.com/lmctl-ai/lmfluid/main/docs/images/cylinder_wake.png" width="280" alt="A vortex street sheds behind a cylinder"></a><br><b>lmfluid</b> · fluids and finite elements (MFEM, LBM) | <a href="https://github.com/lmctl-ai/lmmolecule"><img src="https://raw.githubusercontent.com/lmctl-ai/lmmolecule/main/docs/images/water_box_render.png" width="280" alt="216 TIP3P waters, rendered ball-and-stick"></a><br><b>lmmolecule</b> · molecular dynamics (OpenMM) | <a href="https://github.com/lmctl-ai/lmcell"><img src="https://raw.githubusercontent.com/lmctl-ai/lmcell/main/docs/images/wound_closure.png" width="280" alt="Migration and division close a scratch"></a><br><b>lmcell</b> · agent-based cell biology (PhysiCell) |
| <a href="https://github.com/lmctl-ai/lmparticle"><img src="https://raw.githubusercontent.com/lmctl-ai/lmparticle/main/docs/images/material_attenuation.png" width="280" alt="Photon attenuation in lead, aluminium and water"></a><br><b>lmparticle</b> · photon transport (NIST XCOM) | <a href="https://github.com/lmctl-ai/lmweather"><img src="https://raw.githubusercontent.com/lmctl-ai/lmweather/main/docs/images/planetary_jets.png" width="280" alt="Planetary rotation shapes zonal winds"></a><br><b>lmweather</b> · atmospheric dynamics (shallow water) | <a href="https://github.com/lmctl-ai/lmdraw"><img src="https://raw.githubusercontent.com/lmctl-ai/lmdraw/main/docs/images/lens-ray-diagram.png" width="280" alt="Real and virtual images through one lens"></a><br><b>lmdraw</b> · annotated 2D diagrams |
| <a href="https://github.com/lmctl-ai/lmcad"><img src="https://raw.githubusercontent.com/lmctl-ai/lmcad/main/docs/images/buckyball.png" width="280" alt="The carbon cage of a buckyball"></a><br><b>lmcad</b> · parametric 3D solids (OpenCASCADE) | <a href="https://github.com/lmctl-ai/lmblender"><img src="https://raw.githubusercontent.com/lmctl-ai/lmblender/main/docs/images/caffeine-molecule.png" width="280" alt="Caffeine rendered in atom colours"></a><br><b>lmblender</b> · path-traced scenes (Cycles) | <a href="https://github.com/lmctl-ai/lmimg"><img src="https://raw.githubusercontent.com/lmctl-ai/lmimg/main/docs/images/thumbnail_grid.png" width="280" alt="Procedural colour and image transforms"></a><br><b>lmimg</b> · image editing (ImageMagick core) |
| <a href="https://github.com/lmctl-ai/lmaudio"><img src="https://raw.githubusercontent.com/lmctl-ai/lmaudio/main/docs/images/chirp_spectrogram.png" width="280" alt="Linear and exponential chirp spectrograms"></a><br><b>lmaudio</b> · audio synthesis and analysis | <a href="https://github.com/lmctl-ai/lmshark"><img src="https://raw.githubusercontent.com/lmctl-ai/lmshark/main/docs/images/protocol_sequence_ladder.png" width="280" alt="From ARP to HTTP in a packet sequence"></a><br><b>lmshark</b> · packet and protocol analysis | <a href="https://github.com/lmctl-ai/lmgallery"><img src="https://raw.githubusercontent.com/lmctl-ai/lmgallery/main/docs/images/showcase-01-oscillator.png" width="280" alt="Damped oscillator dashboard: lmnum feeding lmplot"></a><br><b>lmgallery</b> · compositions that chain hosts |

## Hosts

- [lmplot](https://github.com/lmctl-ai/lmplot): 2D/3D plots, heatmaps, polar and GIF animation on a static gnuplot.
- [lmnum](https://github.com/lmctl-ai/lmnum): linear algebra, ODEs, integration, root finding, optimization and fitting.
- [lmfinance](https://github.com/lmctl-ai/lmfinance): yield curves, bonds, swaps, options, Greeks, risk and calibration.
- [lmspace](https://github.com/lmctl-ai/lmspace): N-body integration, Kepler, Lambert and Hohmann transfers, SPICE frames.
- [lmphysics](https://github.com/lmctl-ai/lmphysics): rigid bodies, joints, contact and friction with Project Chrono.
- [lmbio](https://github.com/lmctl-ai/lmbio): gene circuits, enzymes, drugs and epidemics as stiff ODEs or Gillespie runs.
- [lmfluid](https://github.com/lmctl-ai/lmfluid): finite elements and lattice-Boltzmann flow with known-answer problems.
- [lmmolecule](https://github.com/lmctl-ai/lmmolecule): molecular dynamics with OpenMM, from argon to water boxes.
- [lmcell](https://github.com/lmctl-ai/lmcell): tumours, wounds and chemotaxis as PhysiCell agent simulations.
- [lmparticle](https://github.com/lmctl-ai/lmparticle): seeded Monte Carlo photon transport for shielding, detectors and dose.
- [lmweather](https://github.com/lmctl-ai/lmweather): rotating shallow water on the sphere and the beta-plane.
- [lmdraw](https://github.com/lmctl-ai/lmdraw): computed 2D diagrams, free-body sketches and numbered-frame GIFs.
- [lmcad](https://github.com/lmctl-ai/lmcad): OpenCASCADE B-rep solids with a built-in renderer; PNG, APNG, STL.
- [lmblender](https://github.com/lmctl-ai/lmblender): Blender's Cycles path tracer as one executable, no Blender install.
- [lmimg](https://github.com/lmctl-ai/lmimg): layers, masks, curves, healing and LUTs on a static ImageMagick core.
- [lmaudio](https://github.com/lmctl-ai/lmaudio): synthesis, FFT/STFT analysis, EQ, pitch and WAVE I/O.
- [lmshark](https://github.com/lmctl-ai/lmshark): read, build, dissect and filter pcap/pcapng captures.
- [lmgallery](https://github.com/lmctl-ai/lmgallery): fifteen compositions that chain several hosts into one picture.

## Quickstart

Install the runner once, then run any example straight from its URL in an empty directory. The picture lands in `images/`.

```sh
npm install -g @lmctl-ai/lmctl

# Planck spectra of three stars with the visible band marked (lmplot)
lmctl autorun https://raw.githubusercontent.com/lmctl-ai/lmplot/main/examples/blackbody_planck.lms

# Von Karman vortex street behind a cylinder (lmfluid, drawn by lmplot)
lmctl autorun https://raw.githubusercontent.com/lmctl-ai/lmfluid/main/examples/cylinder_wake.lms

# Damped oscillator dashboard: lmnum integrates, lmplot draws (lmgallery)
lmctl autorun https://raw.githubusercontent.com/lmctl-ai/lmgallery/main/examples/01-oscillator-ode-plot.lms
```

## How it works

- An lmscript program binds a host in a `_dsl_` block: `p = _dsl_ cli="lmplot" install="github:lmctl-ai/lmplot@latest";`. The block's body is compiled against the schema embedded in the host binary (`lmplot --dsl-schema`), so mistakes are reported before anything runs.
- Each host is one static executable per platform (linux-x64, linux-arm64, macos-arm64, macos-x64, windows-x64) with nothing to install beside it; `install="…@latest"` fetches the newest release on first use.
- One program can bind several hosts, so a simulation host computes and a drawing host (lmplot, lmdraw, lmcad, lmblender) turns the result into a picture. [lmgallery](https://github.com/lmctl-ai/lmgallery) collects such compositions and runs every one of them in CI.

Every host is MIT licensed except lmblender (GPL-3.0-or-later, as Blender is); each release carries its third-party notices.
