---
description: 'Documentation and content creation standards'
applyTo: '**/*.md'
---

## Markdown Content Rules

The following markdown content rules apply to all documentation files in this repository:

1. **Headings**: Use appropriate heading levels (H2, H3, etc.) to structure your content. Do not use more than one H1 per file.
2. **Lists**: Use bullet points or numbered lists for lists. Ensure proper indentation and spacing.
3. **Code Blocks**: Use fenced code blocks for code snippets. Specify the language for syntax highlighting. **Never** use code blocks for mathematical formulas.
4. **Links**: Use proper markdown syntax for links. Ensure that links are valid and accessible.
5. **Images**: Use proper markdown syntax for images. Include alt text for accessibility.
6. **Tables**: Use markdown tables for tabular data. Ensure proper formatting and alignment.
7. **Line Length**: Limit line length to 400 characters for readability.
8. **Whitespace**: Use appropriate whitespace to separate sections and improve readability.

## Formatting and Structure

- **Headings**: Use `##` for H2 and `###` for H3. Ensure headings are used in a hierarchical manner.
- **Lists**: Use `-` for bullet points and `1.` for numbered lists. Indent nested lists with two spaces.
- **Code Blocks**: Use triple backticks to create fenced code blocks. Specify the language after the opening backticks (e.g., ` ```python `).
- **Links**: Use `[link text](URL)` for links. Ensure that the link text is descriptive and the URL is valid.
- **Images**: Use `![alt text](image URL)` for images. Include a brief description in the alt text.
- **Tables**: Use `|` to create tables. Ensure columns are properly aligned and headers are included.
- **Whitespace**: Use blank lines to separate sections. Avoid excessive whitespace.

## Math Formula Rules (MathJax v3)

This site renders math via **MathJax v3**. Always use LaTeX math notation — never write formulas as plain text or inside code blocks.

- **Inline formulas** (within a sentence): wrap with single `$...$`
  - ✅ `La reattanza induttiva è $X_L = 2\pi f L$`
  - ❌ `La reattanza induttiva è X_L = 2*pi*f*L`
- **Display formulas** (standalone, centered): wrap with `$$...$$` on its own line
  - ✅
    ```
    $$
    \lambda = \frac{c}{f}
    $$
    ```
  - ❌ `\[...\]` (avoid — causes rendering issues in some Jekyll configurations)
  - ❌ plain code block with the formula inside
- Use standard LaTeX commands: `\frac{}{}`, `\cdot`, `\pi`, `\sqrt{}`, `^{}`, `_{}`, `\text{}`, `\Omega`, `\mu`, `\lambda`, `\Delta`, etc.
- For units inside formulas use `\text{}`: e.g., `$1\,\text{H} = \frac{1\,\text{Wb}}{1\,\text{A}}$`
- Always verify that every `$` is paired and LaTeX braces `{}` are balanced.
