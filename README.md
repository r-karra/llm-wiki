# LLM Wiki

A structured knowledge base for daily learning paths and technical research, optimized for LLM processing.

## Structure

- `wiki/`: Main content directory.
  - `index.md`: Wiki entry point.
  - `topics/`: Specific learning paths and subjects.
- `scripts/`: Automation and build tools.
- `config.yaml`: Site configuration and navigation.

## Usage

Content is written in Markdown with YAML frontmatter. Internal links use relative paths or wiki-link syntax.

## Build

To build the wiki (simulated):
```bash
python3 scripts/build.py
```
