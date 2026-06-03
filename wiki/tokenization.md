---
title: Tokenization
date: 2026-06-03
tags: [llm, nlp, preprocessing]
---

# Tokenization

**Summary**: The process of breaking down text into smaller units called tokens, which can be characters, words, or subwords.

**Sources**: [Chapter_2_Tokens_and_Token_Embeddings.ipynb](../raw/Chapter_2_Tokens_and_Token_Embeddings.ipynb)

---

Tokenization is the first step in the LLM pipeline. It converts raw text into a format that the model can understand.

## Types of Tokenization
- **Character-level**: Treating each character as a token.
- **Word-level**: Splitting text by whitespace and punctuation.
- **Subword-level**: (Most common) Breaking words into meaningful pieces (e.g., Byte Pair Encoding or WordPiece).

## Key Libraries
- `transformers` (Hugging Face)
- `sentence-transformers`

## Related Concepts
- [[embeddings]]
- [[large-language-models]]
