---
title: Neural Networks
date: 2026-06-04
tags: [neural-networks, deep-learning, machine-learning]
---

# Neural Networks

**Summary**: The foundational architecture of deep learning, consisting of layers of nodes (neurons) that process inputs to perform classification, regression, or generation tasks.

**Resource**: [Andrej Karpathy - Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | [Google Developers ML Crash Course](https://developers.google.com/machine-learning/crash-course)

---

Neural networks are mathematical models loosely inspired by biological brains. By stacking linear transformations and non-linear activation functions, neural networks can approximate arbitrary complex functions.

## 1. Core Architecture

- **Input Layer**: Receives the raw feature vectors (e.g., token IDs, image pixels).
- **Hidden Layers**: Perform intermediate computations where weights and biases extract features.
- **Output Layer**: Produces the final prediction (e.g., class probabilities, predicted values).
- **Activation Functions**: Introduce non-linearities, enabling the network to learn non-linear patterns (e.g., ReLU, GeGLU, Softmax).

## 2. Training Loop

1. **Forward Propagation**: Input passes through the layers to compute the output and the loss value (discrepancy between prediction and target).
2. **Backward Propagation (Backprop)**: The chain rule of calculus is used to calculate the gradient of the loss function with respect to every weight and bias in the network.
3. **Weight Update**: An optimizer (e.g., Adam, SGD) updates the parameters using the calculated gradients to reduce the loss in subsequent iterations.

## 3. Related Concepts
- [[tokenization]]
- [[embeddings]]
- [[large-language-models]]
