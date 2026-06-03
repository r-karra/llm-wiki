# Welcome to your LLM Wiki

This is your personal "Second Brain" for tracking daily learning across LLMs, Quantum Computing, DSA, and English.

## 🚀 How to Add Content

To keep your wiki updated, follow these steps:

### 1. Ingesting from Primary Resources
The wiki is configured to track two main resources:
- **Google Doc**: [Daily Learning Notes](https://docs.google.com/document/d/1RSezpbxa5_VNKxc4tARunh34F83lU8si50qgosN0fbk/edit)
- **GitHub Repo**: [learn-quantum-AI](https://github.com/learn-quantum-AI)

**To trigger an update**:
Simply ask me: *"Update my wiki from my main resources."* I will then:
1. Pull the latest text from your Google Doc.
2. Scan your local `learn-quantum-AI` folder for new notebooks or changes.
3. Automatically create/update concept pages and topic logs.

### 2. Manual Additions
- **Raw Files**: Drop PDFs or notes into the `raw/` directory.
- **Quick Snippets**: Paste code or text directly in our chat and say *"Save this to my wiki."*

## 🛠 How to Update the Wiki Structure

- **Navigation**: Modify `config.yaml` to change the sidebar or header links.
- **Rules**: Check `CLAUDE.md` for the standards on how pages should be formatted.
- **Build**: Run the build script to refresh the distributed version:
  ```bash
  cd ~/llm-wiki && python3 scripts/build.py
  ```

## 📂 Current Topics
- [Hands-on LLMs](wiki/topics/hands-on-llms.md)
- [IBM Quantum Learning](wiki/topics/ibm-quantum-learning.md)
- [DSA in Python](wiki/topics/dsa-in-python.md)
- [Learn English](wiki/topics/learn-english.md)
- [Neural Networks: Zero to Hero](wiki/topics/neural-networks-zero-to-hero.md)
- [Wiki Index](index.md)
