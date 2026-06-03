---
title: Embeddings
date: 2026-06-03
tags: [llm, machine-learning, vectors]
---

# Embeddings

**Summary**: High-dimensional vector representations of tokens that capture semantic meaning and relationships.

**Sources**: [Chapter_2_Tokens_and_Token_Embeddings.ipynb](../raw/Chapter_2_Tokens_and_Token_Embeddings.ipynb)

---

Embeddings map discrete tokens to continuous vector space. Tokens with similar meanings are positioned closer together in this space.

## Properties
- **Semantic Similarity**: Captures how related two pieces of text are.
- **Dimensionality**: Typically hundreds or thousands of dimensions.

## Key Libraries
- `sentence-transformers`
- `gensim`
- `scikit-learn` (for dimensionality reduction/visualization)

## Related Concepts
- [[tokenization]]
- [[large-language-models]]
