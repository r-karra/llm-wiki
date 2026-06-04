---
title: Large Language Models
date: 2026-06-04
tags: [llm, transformers, gemma, deep-learning, model-training]
---

# Large Language Models (LLMs)

**Summary**: Advanced transformer-based neural networks trained on massive datasets to process, understand, and generate natural language or other sequential data.

**Resource**: [Attention Is All You Need Paper](https://arxiv.org/abs/1706.03762) | [Gemma Model Family](https://ai.google.dev/gemma)

---

LLMs are built on the Transformer architecture, utilizing attention mechanisms to process sequences in parallel and capture long-range semantic dependencies.

## 1. Transformer Architecture & Attention

- **Self-Attention**: Calculates mathematical scores between every word/token in a sentence to capture context (e.g., resolving what "it" refers to).
- **Encoder-Decoder**: Standard sequence-to-sequence structure. Many modern LLMs are decoder-only (e.g., GPT, Gemma, Llama), focused on predicting the next token.
- **Key-Value Caching (KV Cache)**: Optimizes inference speeds by storing key-value pairs of past tokens instead of recomputing them.

## 2. Gemma Model Architecture

Gemma is Google’s open-weights model family (available in 2B, 7B, 9B, and 27B parameters). It implements several key updates to the vanilla Transformer:

- **Rotary Positional Embeddings (RoPE)**: Replaces absolute positional encodings with relative, rotary ones, improving length extrapolation.
- **GeGLU Activations**: Employs gated linear units with GeLU activation instead of standard ReLU in its Feed-Forward Networks.
- **Multi-Query Attention (MQA) / Grouped-Query Attention (GQA)**: Accelerates inference memory operations by sharing key/value attention heads across query heads.

## 3. Adaptation & Fine-Tuning

- **Parameter-Efficient Fine-Tuning (PEFT)**: Adapts a model without modifying all parameters.
- **Low-Rank Adaptation (LoRA)**: Injects trainable rank-decomposition matrices into attention layers, reducing parameter tuning overhead by >99%.
- **Reinforcement Learning from Human Feedback (RLHF)**: Aligns models with human preferences using reward models and optimization algorithms (e.g., PPO).

## 4. Sequential Modeling Beyond Text

The principles of language modeling extend beyond human speech. By representing other sequential structures as tokens, the same transformer techniques are applied to:
- **Biology**: Modeling protein sequences to predict folds (e.g., AlphaFold).
- **Climate Science**: Sequential weather grid modeling (e.g., GraphCast).
