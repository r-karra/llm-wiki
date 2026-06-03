# Welcome to your LLM Wiki

This is your personal "Second Brain" for tracking daily learning across **LLMs**, **Quantum Computing**, **DSA**, and **English**. Optimized for LLM processing and interlinked research.

## 🚀 "Auto-Mode" Workflow

The wiki is designed to grow automatically as you learn. Use these primary methods to keep it updated:

### 1. Unified Resource Sync
The wiki tracks your two main hubs:
- **Google Doc**: [Daily Learning Notes](https://docs.google.com/document/d/1RSezpbxa5_VNKxc4tARunh34F83lU8si50qgosN0fbk/edit)
- **GitHub Repo**: [learn-quantum-AI](https://github.com/learn-quantum-AI)

**To trigger a full sync**, simply ask me: 
> *"Sync my resources and update the wiki."*

I will then fetch the latest notes from your Google Doc, pull updates from GitHub, and automatically create/update your topic and concept pages.

### 2. The Build Engine
You can run the automation script manually to sync your local GitHub repo and prepare the site for publishing:
```bash
python3 ~/llm-wiki/scripts/build.py
```

### 3. Manual Content
- **Raw Materials**: Drop PDFs or `.ipynb` notebooks into `~/llm-wiki/raw/`.
- **Quick Snippets**: Paste code/text in this chat and say *"Save this to my wiki."*

## 🌐 Publishing to GitHub Pages

Your wiki is live at: **[https://r-karra.github.io/llm-wiki/](https://r-karra.github.io/llm-wiki/)**

To push your latest local changes to the web:
```bash
cd ~/llm-wiki && git add . && git commit -m "Update wiki" && git push
```

## 📂 Wiki Directory

### Daily Learning Paths
- [Hands-on LLMs](wiki/topics/hands-on-llms.md)
- [IBM Quantum Learning](wiki/topics/ibm-quantum-learning.md)
- [DSA in Python](wiki/topics/dsa-in-python.md)
- [Learn English](wiki/topics/learn-english.md)
- [Neural Networks: Zero to Hero](wiki/topics/neural-networks-zero-to-hero.md)

### Core Concepts
- [Tokenization](wiki/tokenization.md) | [Embeddings](wiki/embeddings.md)
- [Qubits](wiki/qubits.md) | [Quantum Gates](wiki/quantum-gates.md) | [Entanglement](wiki/entanglement.md)
- [Binary Search](wiki/binary-search.md) | [Complexity Analysis](wiki/complexity-analysis.md)

### Tracking
- [Daily Learning Log](wiki/log.md)
- [Wiki Index (Homepage)](index.md)
