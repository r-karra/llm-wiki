---
title: IBM Quantum Learning
date: 2026-06-03
tags: [quantum-computing, ibm, learning-path]
---

# IBM Quantum Learning

This learning path focuses on practical quantum computation, circuit building, and quantum mechanics, using IBM Quantum Learning resources and the Qiskit software development kit.

---

## 📅 Progress & Lesson Summaries

### Lesson 1: Build and Run Your First Quantum Program
- **Summary**: Transitioning from visual circuit design on IBM Composer to programmatic circuit creation in Qiskit.
- **Core Concepts**:
  - **IBM Composer**: Dragging and dropping gates on a visual timeline (circuit diagram) to explore state changes.
  - **The Hello World Circuit**: Creating the $\vert\Phi^+\rangle$ Bell state using a Hadamard ($H$) gate on qubit 0 followed by a Controlled-NOT ($CX$) gate with qubit 0 as control and qubit 1 as target.
  - **Simulators vs. QPUs**: Running job executions on a perfect local simulator vs. a real physical IBM Quantum Processing Unit (QPU) affected by environmental decoherence, read-out errors, and noise.
- **Concept Links**:
  - [[quantum-gates]]
  - [[entanglement]]

---

### Lesson 2: Quantum Mechanics Basics
- **Summary**: Exploring the mathematical foundations of quantum systems and state transitions.
- **Core Concepts**:
  - **State Vector Representation**: Describing qubit states using Dirac notation (ket vectors $\vert \psi \rangle$) and matrices.
  - **Superposition Math**: Restricting state amplitudes to the normalization condition $\vert\alpha\vert^2 + \vert\beta\vert^2 = 1$.
  - **Bloch Sphere Coordinates**: Parameterizing the state vector using polar ($\theta$) and azimuthal ($\phi$) angles.
  - **Measurement Collapse**: Explaining why a quantum state collapses to classical eigenvalues upon physical measurement.
- **Concept Links**:
  - [[qubits]]
  - [[entanglement]]

---

## 🛠️ Resources & Environment Setup

- **Platform**: [IBM Quantum Learning](https://learning.quantum.ibm.com/)
- **Software**: Qiskit SDK (`qiskit`, `qiskit-aer` for simulation, `qiskit-ibmq-provider` for cloud QPUs).
- **Notebooks**:
  - [Build and Run your First Quantum Program Notebook](../../raw/build-and-run-your-first-quantum-program.ipynb)
  - [Quantum Mechanics Basics Notebook](../../raw/quantum-mechanics-basics.ipynb)
