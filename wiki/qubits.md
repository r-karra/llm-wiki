---
title: Qubits
date: 2026-06-03
tags: [quantum-computing, physics]
---

# Qubits

**Summary**: The fundamental unit of quantum information, capable of existing in superpositions of 0 and 1, represented mathematically as vectors in a two-dimensional Hilbert space.

**Sources**: [quantum-mechanics-basics.ipynb](../raw/quantum-mechanics-basics.ipynb)

---

## 1. Classical Bits vs. Quantum Qubits

A classical bit represents a switch that is either completely open (`0`) or closed (`1`). In contrast, a **qubit** (quantum bit) can represent `0`, `1`, or any **superposition** of both simultaneously. This enables quantum computers to explore massive computational state spaces in parallel.

---

## 2. Mathematical State Representation

We represent the state of a qubit using **Dirac notation** (also called bra-ket notation). 

### The Basis States
The two computational basis states are denoted as kets:
- $\vert 0 \rangle$ (representing the ground state)
- $\vert 1 \rangle$ (representing the excited state)

In vector form, these form an orthonormal basis:
$$\vert 0 \rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad \vert 1 \rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

### Superposition State
Any pure state of a single qubit, $\vert \psi \rangle$, is a linear combination of the basis states:
$$\vert \psi \rangle = \alpha \vert 0 \rangle + \beta \vert 1 \rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$$

Here, $\alpha$ and $\beta$ are complex numbers representing **probability amplitudes**.

### Normalization Condition
Since the total probability of measurement outcomes must equal 1, the state vector must be normalized:
$$\vert \alpha \vert^2 + \vert \beta \vert^2 = 1$$
- $\vert \alpha \vert^2$: Probability of measuring state $\vert 0 \rangle$.
- $\vert \beta \vert^2$: Probability of measuring state $\vert 1 \rangle$.

---

## 3. The Bloch Sphere

The state of a single qubit can be visualized as a point on the surface of a three-dimensional unit sphere, known as the **Bloch Sphere**.

Any normalized qubit state can be written using spherical coordinates:
$$\vert \psi \rangle = \cos\left(\frac{\theta}{2}\right) \vert 0 \rangle + e^{i\phi}\sin\left(\frac{\theta}{2}\right) \vert 1 \rangle$$

- $\theta$ ($0 \le \theta \le \pi$): Determines the polar angle (latitude), controlling the balance of superposition. 
  - $\theta = 0$ corresponds to the north pole: $\vert 0 \rangle$.
  - $\theta = \pi$ corresponds to the south pole: $\vert 1 \rangle$.
- $\phi$ ($0 \le \phi \le 2\pi$): Determines the azimuthal angle (longitude), representing the **relative phase** of the qubit.

---

## 4. Measurement & State Collapse

Measurement is a destructive process in quantum mechanics:
1. **Superposition**: Before measurement, the qubit is in a superposition $\alpha \vert 0 \rangle + \beta \vert 1 \rangle$.
2. **Collapse**: Upon measurement, the qubit's state **collapses** to either the classical state $\vert 0 \rangle$ (with probability $\vert\alpha\vert^2$) or $\vert 1 \rangle$ (with probability $\vert\beta\vert^2$).
3. **Repeated Sampling**: Running a quantum circuit once only returns a single classical bit. To estimate the probability amplitudes $\alpha$ and $\beta$, we must execute the circuit multiple times (referred to as **shots**) and count the frequency of results.

## Related Concepts
- [[quantum-gates]]
- [[entanglement]]
- [[ibm-quantum-learning]]
