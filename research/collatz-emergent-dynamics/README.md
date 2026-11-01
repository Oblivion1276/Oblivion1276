# Collatz Emergent Dynamics — working research project

**Status:** Exploratory computational research. **No proof or disproof of Collatz.**

Research direction and questions by **Oblivion1276**. Calculations, scripts, explorer, and writing prepared with **OpenAI GPT-6** (AI assistance). Established mathematical work is attributed to the original authors in the [paper](paper/collatz_emergent_dynamics.md).

## Findings at a glance

The exact accelerated map is `T(n)=n/2` for even `n`, `(3n+1)/2` for odd `n`. This work examines binary parity histories, inverse trees, residue-class first-drop certificates, base-dependent raster maps, complex phases, and quantum-inspired mathematical visualizations. All finite experiments reported here preserve the original Collatz rule.

- At depth 16: **2,114** unresolved residue classes out of `2^16` (3.225708%).
- Tracking their descendants exactly to depth 24: **286,581** unresolved classes out of `2^24` (1.708156%).
- The count rises even as the *fraction* falls. A finite unresolved prefix does not mean infinite divergence.
- A fixed-depth universal first-drop certificate is impossible because `2^k-1` has `k` consecutive odd accelerated steps.
- Rotations and changes of numeral base change *pictures*, not the arithmetic; no special rotation or physical quantum mechanism is established.

## Contents

- [`paper/collatz_emergent_dynamics.md`](paper/collatz_emergent_dynamics.md): full mathematical working paper with proofs, limitations, and bibliography.
- [`explorer/index.html`](explorer/index.html): **standalone interactive explorer** with base-to-base overlays, nonstandard angles, user-selected centers, complex phase controls, Gaussian radix `-1+i`, and selected normalized physics-constant presets. Open in a browser; no server needed.
- [`src/track_residues.py`](src/track_residues.py): exact-integer level-by-level residue tracking.
- [`tests/test_residues.py`](tests/test_residues.py): independent brute-force and algebraic regression checks.
- [`data/residue_levels.csv`](data/residue_levels.csv): all measured depth-16-to-24 counts and proportions.
- [`data/residue_transitions.csv`](data/residue_transitions.csv): 0/1/2 surviving-child counts by level.
- [`figures/`](figures/): charts used in the paper.

## Reproduce

```bash
python3 src/track_residues.py --max-depth 24 --out data
python3 tests/test_residues.py
```

The tests print a `PASS` line if the exact count comparisons succeed. For this reproduction, Python 3 standard library is sufficient; charts and the PDF version were created with Matplotlib/Pandoc.

## Technical limitations

The residue certificate is *uniform for all `n=r+j*2^t` with `j>=1`* when verified using the smallest representative `2^t+r`. It is not a claim about all positive integers in the residue class below `2^t`, and failure of the certificate is not evidence of divergence.

The exploratory visual encoding choices, custom real bases, dimensionless normalizations of physical constants, and the toy free-Schrödinger center sampler are explicitly **not known physics of the Collatz map**. The paper documents the more rigorous arithmetic results separately.

## Credit and prior art

This investigation builds on results of Collatz, Terras, Lagarias, Bernstein, Tao, Barina, Rozier, Terracol and researchers in Sturmian/symbolic dynamics. Scholarly citations and URLs are collected in the working paper. No original proof of the unsolved conjecture is claimed.