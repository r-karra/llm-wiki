---
title: Large Language Models
date: 2026-06-04
tags: [llm, transformers, gemma, deep-learning, model-training]
---

# Large Language Models (LLMs)

**Summary**: Advanced transformer-based neural networks trained on massive datasets to process, understand, and generate natural language.

**Resource**: [Attention Is All You Need Paper](https://arxiv.org/abs/1706.03762) | [Gemma Model Family](https://ai.google.dev/gemma)

---

## 1. Transformer Architecture & Attention

LLMs are built on the Transformer architecture, utilizing attention mechanisms to process sequences in parallel and capture long-range semantic dependencies.

- **Self-Attention**: Calculates mathematical scores between every word/token in a sentence to capture context (e.g., resolving what "it" refers to).
- **Encoder-Decoder**: Standard sequence-to-sequence structure. Many modern LLMs are decoder-only (e.g., GPT, Gemma, Llama, Phi-3), focused on predicting the next token.
- **Key-Value Caching (KV Cache)**: Optimizes inference speeds by storing key-value pairs of past tokens instead of recomputing them.

---

## 2. Navigating the Hugging Face Ecosystem

Hugging Face is the central hub for machine learning, especially for natural language processing. It provides:

- **🤗 Hub**: A registry containing hundreds of thousands of open-source models, datasets, and interactive demos (Spaces).
- **🤗 Transformers**: The core library used to download, initialize, and run model architectures (PyTorch, TensorFlow, and JAX supported).
- **🤗 Datasets**: A library for loading and processing large datasets in memory-mapped format.
- **🤗 Accelerate**: A library that simplifies distributed multi-GPU or TPU training and inference.

---

## 3. Running LLMs Locally: Pipelines & Manual Loading

There are two primary ways to run an LLM using the Hugging Face `transformers` library:

### Method A: The `pipeline` Abstraction (Recommended for Inference)
The `pipeline` wraps tokenization, model inference, and text decoding into a simple, high-level function call.

```python
import torch
from transformers import pipeline

# 1. Create a text-generation pipeline
# This automatically downloads, configures, and moves the model to GPU (if cuda is available)
generator = pipeline(
    "text-generation", 
    model="microsoft/Phi-3-mini-4k-instruct",
    device_map="auto",
    torch_dtype=torch.float16,
    trust_remote_code=True
)

# 2. Define chat template prompt structure
prompt = [
    {"role": "system", "content": "You are a helpful physics co-pilot."},
    {"role": "user", "content": "Explain quantum superposition in one sentence."}
]

# 3. Generate content
outputs = generator(
    prompt,
    max_new_tokens=100,
    return_full_text=False,
    temperature=0.0
)

print(outputs[0]['generated_text'])
```

### Method B: Manual Tokenizer and Model Loading (For customization)
If you need to access raw logits or perform parameter-efficient fine-tuning (PEFT), load the tokenizer and model components separately.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 1. Load tokenizer and model separately
model_id = "microsoft/Phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16,
    trust_remote_code=True
)

# 2. Encode inputs to Token IDs
text = "What is Accelerated Linear Algebra (XLA)?"
inputs = tokenizer(text, return_tensors="pt").to("cuda")

# 3. Generate token sequences
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=150)

# 4. Decode output tokens to text
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

---

## 4. Gemma Model Architecture

Gemma is Google’s open-weights model family (available in 2B, 7B, 9B, and 27B parameters). It implements several key updates to the vanilla Transformer:

- **Rotary Positional Embeddings (RoPE)**: Replaces absolute positional encodings with relative, rotary ones, improving length extrapolation.
- **GeGLU Activations**: Employs gated linear units with GeLU activation instead of standard ReLU in its Feed-Forward Networks.
- **Multi-Query Attention (MQA) / Grouped-Query Attention (GQA)**: Accelerates inference memory operations by sharing key/value attention heads across query heads.

---

## 5. Adaptation & Fine-Tuning

- **Parameter-Efficient Fine-Tuning (PEFT)**: Adapts a model without modifying all parameters.
- **Low-Rank Adaptation (LoRA)**: Injects trainable rank-decomposition matrices into attention layers, reducing parameter tuning overhead by >99%.
- **Reinforcement Learning from Human Feedback (RLHF)**: Aligns models with human preferences using reward models and optimization algorithms (e.g., PPO).

## Related Concepts
- [[tokenization]]
- [[embeddings]]
- [[jax-ecosystem]]
- [[hands-on-llms]]
