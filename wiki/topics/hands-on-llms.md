---
title: Hands-on LLMs
date: 2026-06-03
tags: [llm, machine-learning, learning-path]
---

# Hands-on LLMs

This learning path focuses on practical implementation, architecture, and deployment of Large Language Models, following the textbook *Hands-On Large Language Models* by Jay Alammar and Maarten Grootendorst.

---

## 📅 Progress & Chapter Summaries

### Chapter 1: Introduction to Language Models
- **Summary**: High-level overview of language models, history, and applications (translation, summarization, chatbots, classification).
- **Core Concepts**:
  - Loading models using the Hugging Face `pipeline` abstraction.
  - Interfacing with local pre-trained weights (e.g., `microsoft/Phi-3-mini-4k-instruct`).
  - Configuring GPUs (CUDA) for model inference.
- **Concept Links**:
  - [[large-language-models]]

---

### Chapter 2: Tokens and Token Embeddings
- **Summary**: Deep-dive into how text is converted into numbers and subsequently mapped to continuous vector spaces.
- **Core Concepts**:
  - **Tokenization**: Breaking words into subword pieces using BPE, WordPiece, or SentencePiece. Comparing tokenizers across model generations (e.g., GPT's `tiktoken` vs. Llama vs. Phi-3).
  - **Word Embeddings**: Static embeddings (Word2Vec) vs. contextualized embeddings (BERT, GPT, Phi-3).
  - **Sentence Embeddings**: Computing semantic similarity between entire sentences using pooling mechanisms and `sentence-transformers`.
  - **Beyond Text**: Using item sequence embeddings (e.g., songs in user sessions) to train custom recommendation algorithms with `gensim`.
- **Concept Links**:
  - [[tokenization]]
  - [[embeddings]]

---

## 🛠️ Resources & Environment Setup

- **Book**: [Hands-On Large Language Models (Amazon)](https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961)
- **Hugging Face Suite**: `transformers`, `datasets`, `accelerate`, and `sentence-transformers`.
- **Notebooks**:
  - [Chapter 1 Notebook](../../raw/Chapter_1_Introduction_to_Language_Models.ipynb)
  - [Chapter 2 Notebook](../../raw/Chapter_2_Tokens_and_Token_Embeddings.ipynb)
