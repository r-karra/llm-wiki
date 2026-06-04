---
title: Embeddings
date: 2026-06-03
tags: [llm, machine-learning, vectors]
---

# Embeddings

**Summary**: Continuous high-dimensional vector representations of text tokens that capture semantic meaning, relationships, and contextual usage.

**Sources**: [Chapter_2_Tokens_and_Token_Embeddings.ipynb](../raw/Chapter_2_Tokens_and_Token_Embeddings.ipynb)

---

## 1. What are Embeddings?

An **Embedding** maps a discrete Token ID to a continuous vector of numbers in a high-dimensional space (e.g., 3,072 dimensions for Phi-3-mini, 4,096 dimensions for Llama-2-7B). 

In this space:
- Semantic relationships are represented as distances.
- **Cosine Similarity** is commonly used to measure the angle between two vectors $\mathbf{u}$ and $\mathbf{v}$:
  $$\text{Cosine Similarity} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$
- Linear algebraic relationships emerge:
  $$\vec{v}_{\text{King}} - \vec{v}_{\text{Man}} + \vec{v}_{\text{Woman}} \approx \vec{v}_{\text{Queen}}$$

---

## 2. Static vs. Contextualized Embeddings

Embedding technology has evolved from static representations to dynamic, context-aware representations:

### Static Embeddings (Word2Vec, GloVe)
- **Concept**: Each word in the vocabulary is mapped to a single, fixed vector.
- **Limitation**: Cannot handle polysemy (homographs). The word "bank" in *"river bank"* has the exact same vector as in *"savings bank"*.

### Contextualized Embeddings (BERT, GPT, Transformers)
- **Concept**: The vector representation of a word changes depending on its context (surrounding words).
- **How it works**: The model starts with a static token embedding, then passes it through **Self-Attention Layers** which dynamically update the token's vector by mixing information from other tokens in the sequence.

---

## 3. Sentence and Document Embeddings

To compare entire sentences or documents (e.g., for semantic search or RAG), we must pool token-level embeddings into a single vector.

### Pooling Techniques
1. **Mean Pooling**: Average the embedding vectors of all tokens in the sentence.
2. **CLS Token**: Use the vector of the special classification token (like `[CLS]` in BERT) which is pre-trained to capture sequence-level meaning.

### Implementing Sentence Embeddings
Using the Hugging Face `sentence-transformers` library:

```python
from sentence_transformers import SentenceTransformer, util

# 1. Load a pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Encode sentences into vectors
sentences = [
    "Large Language Models require GPUs for training.",
    "AI models need graphics cards to train.",
    "The weather is lovely today in Seattle."
]
embeddings = model.encode(sentences, convert_to_tensor=True)

# 3. Calculate cosine similarity
sim_1_2 = util.cos_sim(embeddings[0], embeddings[1])
sim_1_3 = util.cos_sim(embeddings[0], embeddings[2])

print(f"Similarity (1 vs 2): {sim_1_2.item():.4f}") # High similarity (~0.75+)
print(f"Similarity (1 vs 3): {sim_1_3.item():.4f}") # Low similarity (~0.10)
```

---

## 4. Word Embeddings Beyond LLMs: Recommendation Systems

Embeddings are widely used in collaborative filtering and recommendation engines. By treating a user's session of interacted items (e.g., songs listened to in sequence) as a "sentence" and individual items as "words", we can train algorithms like Word2Vec to learn item embeddings.

### Song Recommendation with `gensim`
Here is a Python code snippet demonstrating how to train item embeddings for songs:

```python
from gensim.models import Word2Vec

# 1. Prepare user sessions (lists of songs listened to sequentially)
sessions = [
    ["Song_A", "Song_B", "Song_C"],
    ["Song_B", "Song_C", "Song_D", "Song_E"],
    ["Song_A", "Song_C", "Song_F"],
    ["Song_D", "Song_E", "Song_F"]
]

# 2. Train Word2Vec model
# vector_size: dimension of embedding, window: context frame, min_count: discard rare items
model = Word2Vec(sentences=sessions, vector_size=50, window=3, min_count=1, workers=4)

# 3. Recommend similar songs based on vector cosine similarity
similar_songs = model.wv.most_similar("Song_B", topn=3)
print("Songs similar to Song_B:")
for song, similarity in similar_songs:
    print(f" - {song}: {similarity:.4f}")
```

## Related Concepts
- [[tokenization]]
- [[large-language-models]]
- [[hands-on-llms]]
