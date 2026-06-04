---
title: Quantum Gates
date: 2026-06-03
tags: [quantum-computing, algorithms]
---

# Quantum Gates

**Summary**: Mathematical operators represented by unitary matrices that transform the state of qubits in a quantum circuit.

**Sources**: [quantum-mechanics-basics.ipynb](../raw/quantum-mechanics-basics.ipynb), [build-and-run-your-first-quantum-program.ipynb](../raw/build-and-run-your-first-quantum-program.ipynb)

---

## 1. Mathematical Foundation: Unitary Matrices

In quantum mechanics, all physical state transformations (excluding measurement) must preserve the total probability of 1. Therefore, quantum gates are represented by **unitary matrices**.

A matrix $U$ is unitary if its conjugate transpose (adjoint) $U^\dagger$ is also its inverse:
$$U^\dagger U = U U^\dagger = I$$

This mathematical property guarantees that all quantum gates are:
- **Probability-preserving**: The length of the state vector remains 1.
- **Reversible**: Any gate operation can be undone by applying its inverse gate $U^\dagger$.

---

## 2. Common Single-Qubit Gates

Single-qubit gates act on a 2D state vector.

### A. The Hadamard Gate ($H$)
The Hadamard gate creates a superposition by mapping basis states to equal-probability mixtures. It corresponds to a $180^\circ$ rotation around the $X+Z$ diagonal axis of the Bloch Sphere.
$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

**Action on basis states:**
$$H \vert 0 \rangle = \frac{1}{\sqrt{2}} (\vert 0 \rangle + \vert 1 \rangle) = \vert + \rangle$$
$$H \vert 1 \rangle = \frac{1}{\sqrt{2}} (\vert 0 \rangle - \vert 1 \rangle) = \vert - \rangle$$

### B. The Pauli-X Gate ($X$)
Often called the quantum NOT gate, it swaps the amplitudes of the $\vert 0 \rangle$ and $\vert 1 \rangle$ states (rotation of $180^\circ$ around the $X$-axis).
$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

**Action on basis states:**
$$X \vert 0 \rangle = \vert 1 \rangle, \qquad X \vert 1 \rangle = \vert 0 \rangle$$

### C. The Pauli-Y Gate ($Y$)
A rotation of $180^\circ$ around the $Y$-axis.
$$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$$

**Action on basis states:**
$$Y \vert 0 \rangle = i \vert 1 \rangle, \qquad Y \vert 1 \rangle = -i \vert 0 \rangle$$

### D. The Pauli-Z Gate ($Z$)
Also called the Phase Flip gate, it leaves the state $\vert 0 \rangle$ unchanged, but flips the sign of the state $\vert 1 \rangle$.
$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Action on basis states:**
$$Z \vert 0 \rangle = \vert 0 \rangle, \qquad Z \vert 1 \rangle = -\vert 1 \rangle$$

---

## 3. Common Multi-Qubit Gates

Multi-qubit gates act on multi-qubit state vectors. For two qubits, vectors are 4D (representing coefficients of $\vert 00 \rangle, \vert 01 \rangle, \vert 10 \rangle, \vert 11 \rangle$).

### The Controlled-NOT (CNOT / $CX$) Gate
The CNOT gate operates on two qubits: a **control qubit** (qubit 0) and a **target qubit** (qubit 1). It flips the target qubit state if and only if the control qubit is in state $\vert 1 \rangle$.
$$CX = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

**Action on basis states:**
- $CX \vert 00 \rangle = \vert 00 \rangle$
- $CX \vert 01 \rangle = \vert 01 \rangle$
- $CX \vert 10 \rangle = \vert 11 \rangle$ (control is 1, target flips $0 \rightarrow 1$)
- $CX \vert 11 \rangle = \vert 10 \rangle$ (control is 1, target flips $1 \rightarrow 0$)

---

## 4. Qiskit Implementation Example

Here is how to create a simple circuit in Python using IBM's Qiskit library to apply these gates:

```python
from qiskit import QuantumCircuit

# 1. Initialize a 2-qubit circuit with 2 classical measurement bits
qc = QuantumCircuit(2, 2)

# 2. Apply Hadamard gate on qubit 0 (puts it in superposition)
qc.h(0)

# 3. Apply CNOT (CX) gate with control=0, target=1 (entangles them)
qc.cx(0, 1)

# 4. Measure both qubits into the classical bits
qc.measure([0, 1], [0, 1])

# 5. Draw the circuit
print(qc.draw(output="text"))
```

## Related Concepts
- [[qubits]]
- [[entanglement]]
- [[ibm-quantum-learning]]
