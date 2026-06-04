---
title: Tokenization
date: 2026-06-03
tags: [llm, nlp, preprocessing]
---

# Tokenization

**Summary**: The process of breaking down raw text into integer tokens (Token IDs) that a Large Language Model can process.

**Sources**: [Chapter_2_Tokens_and_Token_Embeddings.ipynb](../raw/Chapter_2_Tokens_and_Token_Embeddings.ipynb)

---

## 1. What is Tokenization?

Large Language Models do not read text directly. Instead, they process sequences of numbers called **Token IDs**. A **Tokenizer** is a standalone preprocessing tool that maps raw characters or words to these integer IDs.

```
Raw Text: "Tokenization is awesome"
   ↓ (Tokenization)
Tokens:   ["Token", "ization", " is", " awesome"]
   ↓ (Numerical Mapping)
Token IDs: [47352, 1943, 318, 7234]
```

### The Trade-off of Vocabulary Size
- **Small Vocabulary**: Smaller model parameters (smaller embedding weight matrix), but text is split into many small tokens, resulting in longer sequence lengths (higher computational cost during self-attention).
- **Large Vocabulary**: Shorter sequences (faster attention), but requires a large embedding weight matrix which takes up substantial memory. E.g., Llama 3 uses a 128,256 vocabulary, while Phi-3 uses 32,064.

---

## 2. Subword Tokenization Algorithms

To avoid the issue of *Out-of-Vocabulary (OOV)* words (e.g., encountering new names or typos), modern LLMs use **subword tokenization**. The three major algorithms are:

### A. Byte Pair Encoding (BPE)
- **Concept**: Starts with character-level vocabulary and iteratively merges the most frequent adjacent byte or character pairs in the training corpus.
- **Used by**: GPT-4 (`tiktoken`), Llama, RoBERTa.
- **Example**: If "token" and "ization" are frequent but "tokenization" is rare, BPE stores them separately and represents the word as two tokens: `["token", "ization"]`.

### B. WordPiece
- **Concept**: Similar to BPE, but instead of choosing the most frequent pair, it selects the pair that maximizes the likelihood of the training data according to a unigram language model (maximizing mutual information).
- **Used by**: BERT, DistilBERT.

### C. SentencePiece
- **Concept**: Treats the input as a raw byte stream, including whitespaces (represented as a special character like `_` or ` `). This removes the need for language-specific rule-based pre-tokenizers.
- **Used by**: Llama-2, T5, ALBERT.

---

## 3. Practical Implementation with Hugging Face

Here is how you load and run the tokenizer for `Phi-3` using the Hugging Face `transformers` library:

```python
from transformers import AutoTokenizer

# 1. Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

# 2. Tokenize text into subword string tokens
text = "Tokenization is key for LLMs."
tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)
# Output: [' Token', 'ization', ' is', ' key', ' for', ' L', 'L', 'Ms', '.']

# 3. Convert string tokens to numerical Token IDs
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print("Token IDs:", token_ids)
# Output: [47352, 1943, 318, 1729, 367, 362, 381, 14233, 29889]

# 4. End-to-end encoding (text directly to IDs)
inputs = tokenizer(text)
print("Encoded Input IDs:", inputs["input_ids"])

# 5. Decode back to human text
decoded_text = tokenizer.decode(token_ids)
print("Decoded Text:", decoded_text)
```

---

## 4. Special Tokens

Tokenizers use reserved **special tokens** to structure inputs and control generation. Common examples:
- `<s>` or `<|bos|>`: Beginning of Sequence.
- `</s>` or `<|eos|>`: End of Sequence (tells the model to stop generating).
- `<|pad|>`: Padding token to align batch sequences to the same length.
- `<|user|>` / `<|assistant|>`: Chat template markers used to separate user prompts and model responses.

## Related Concepts
- [[embeddings]]
- [[large-language-models]]
- [[hands-on-llms]]
