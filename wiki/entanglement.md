---
title: Entanglement
date: 2026-06-03
tags: [quantum-computing, physics]
---

# Quantum Entanglement

**Summary**: A quantum phenomenon where the states of two or more qubits are correlated such that the state of one qubit cannot be described independently of the others, even when separated by large distances.

**Sources**: [quantum-mechanics-basics.ipynb](../raw/quantum-mechanics-basics.ipynb), [build-and-run-your-first-quantum-program.ipynb](../raw/build-and-run-your-first-quantum-program.ipynb)

---

## 1. What is Quantum Entanglement?

Entanglement is a key resource in quantum computing. When two qubits are entangled, a measurement on one qubit immediately collapses its state and *instantaneously* determines the state of the other qubit, regardless of how far apart they are. This correlation has no classical equivalent and violates **Local Realism** (as proven by Bell's Theorem).

---

## 2. The Four Bell States (The Bell Basis)

The **Bell Basis** consists of four specific, maximally entangled two-qubit quantum states. They represent the building blocks of quantum communication protocols like Superdense Coding and Quantum Teleportation.

1. **Phi-Plus ($\vert\Phi^+\rangle$):**
   $$\vert \Phi^+ \rangle = \frac{1}{\sqrt{2}} (\vert 00 \rangle + \vert 11 \rangle)$$
2. **Phi-Minus ($\vert\Phi^-\rangle$):**
   $$\vert \Phi^- \rangle = \frac{1}{\sqrt{2}} (\vert 00 \rangle - \vert 11 \rangle)$$
3. **Psi-Plus ($\vert\Psi^+\rangle$):**
   $$\vert \Psi^+ \rangle = \frac{1}{\sqrt{2}} (\vert 01 \rangle + \vert 10 \rangle)$$
4. **Psi-Minus ($\vert\Psi^-\rangle$):**
   $$\vert \Psi^- \rangle = \frac{1}{\sqrt{2}} (\vert 01 \rangle - \vert 10 \rangle)$$

---

## 3. Mathematical State Evolution of $\vert\Phi^+\rangle$

Let's trace how the Hadamard ($H$) and CNOT ($CX$) gates combine to generate the entangled state $\vert\Phi^+\rangle$.

### Step 1: Initial State
We start with both qubits in the ground state:
$$\vert \psi_0 \rangle = \vert 00 \rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}$$

### Step 2: Apply Hadamard to Qubit 0
Applying $H$ to qubit 0 (written as $H \otimes I$) puts it into superposition while leaving qubit 1 in state $\vert0\rangle$:
$$\vert \psi_1 \rangle = (H \otimes I)\vert 00 \rangle = (H\vert0\rangle) \otimes \vert 0 \rangle = \frac{1}{\sqrt{2}}(\vert 0 \rangle + \vert 1 \rangle) \otimes \vert 0 \rangle = \frac{1}{\sqrt{2}}(\vert 00 \rangle + \vert 10 \rangle)$$

In vector form:
$$\vert \psi_1 \rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix}$$

### Step 3: Apply CNOT (Control=0, Target=1)
The CNOT gate flips the target (qubit 1) if the control (qubit 0) is $\vert1\rangle$.
$$\vert \psi_2 \rangle = CX \vert \psi_1 \rangle = CX \left( \frac{1}{\sqrt{2}}(\vert 00 \rangle + \vert 10 \rangle) \right) = \frac{1}{\sqrt{2}} (CX\vert 00 \rangle + CX\vert 10 \rangle)$$

Since $CX\vert 00 \rangle = \vert 00 \rangle$ and $CX\vert 10 \rangle = \vert 11 \rangle$, we get:
$$\vert \psi_2 \rangle = \frac{1}{\sqrt{2}}(\vert 00 \rangle + \vert 11 \rangle) = \vert \Phi^+ \rangle$$

In vector form:
$$\vert \psi_2 \rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix}$$

---

## 4. Simulation vs. Real QPU Noise

- **Simulator (Perfect World)**: Running $\vert\Phi^+\rangle$ on a simulator for 1000 shots produces exactly $\approx 500$ occurrences of $\vert00\rangle$ and $\approx 500$ occurrences of $\vert11\rangle$. The states $\vert01\rangle$ and $\vert10\rangle$ never occur.
- **Physical QPU (Real World)**: Real quantum computers are prone to environmental noise, thermal fluctuations, and gate calibration drifts. Consequently, a histogram from a real QPU will show minor occurrences of $\vert01\rangle$ and $\vert10\rangle$ (e.g. 2-5% of counts) representing measurement and gate errors.

---

## 5. Qiskit Code for Generating the Bell State

Here is the Python script to build the circuit, run it on a simulator, and visualize the counts:

```python
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

# 1. Create a 2-qubit circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# 2. Get local simulator backend
backend = Aer.get_backend('qasm_simulator')

# 3. Execute the circuit for 1000 shots
result = backend.run(qc, shots=1000).result()

# 4. Extract measurement counts
counts = result.get_counts(qc)
print("Measurement counts:", counts)
# Output will be approximately: {'00': 503, '11': 497}

# 5. Optional: Plot the histogram
# plot_histogram(counts)
```

## Related Concepts
- [[qubits]]
- [[quantum-gates]]
- [[ibm-quantum-learning]]
