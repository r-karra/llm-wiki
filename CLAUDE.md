# LLM Wiki

A personal knowledge base for daily learning paths and technical research, optimized for LLM processing.

## Purpose

This wiki is a structured, interlinked knowledge base for tracking learning progress in fields like LLMs, Quantum Computing, DSA, and more.
The CLI agent maintains the wiki. The user curates sources, tracks progress, and guides the analysis.

## Folder structure

```
raw/          -- source documents (immutable -- never modify these)
wiki/         -- markdown pages for core concepts
wiki/topics/  -- specific learning paths and daily progress
wiki/index.md -- table of contents for the entire wiki
scripts/      -- automation and build tools
```

## Ingest workflow

When adding a new learning resource:

1. Create a summary page in `wiki/topics/` named after the resource.
2. Link the resource in `wiki/index.md`.
3. Extract key concepts into individual pages in `wiki/`.
4. Use wiki-links ([[page-name]]) to interlink concepts and topics.

## Page format

Every wiki page should follow this structure:

```markdown
---
title: Page Title
date: YYYY-MM-DD
tags: [tag1, tag2]
---

# Page Title

**Summary**: One to two sentences describing this page.

**Resource**: Link to the original learning material.

---

Main content goes here. Use clear headings and short paragraphs.

## Key Concepts
- [[concept-1]]
- [[concept-2]]
```

## Rules

- Never modify anything in the `raw/` folder.
- Always update `wiki/index.md` after adding new topics.
- Keep page names lowercase with hyphens (e.g. `neural-networks.md`).
- Use YAML frontmatter for metadata.
