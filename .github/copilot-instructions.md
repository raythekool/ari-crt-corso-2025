# Copilot Instructions — ARI CRT Corso 2025–2026

## Project Overview

This repository contains the Astro + Starlight site for the **Corso Aspiranti Radioamatori ARI Toscana CRT**. The published contents are **notes extracted from the lessons of the Tuscany amateur radio course**, not the official course text. The current site organizes 22 lesson guides, supporting transcripts, and recap pages for the 2026 course edition.

## Repository Structure

- `site/` — Astro + Starlight application
- `site/src/content/docs/lezioni/` — Markdown lesson guides (`lezione_XX.md`) and lessons index
- `site/src/pages/index.astro` — Site home page
- `docs/lezioni-2026.md` — Verified table of lesson dates, titles, and recordings
- `transcripts/2025/` and `transcripts/2026/` — Plain-text transcripts (`.txt`) with timestamps, one folder per course edition
- `transcripts (vtt)/2026/` — WebVTT subtitle files (`.vtt`)
- `slides 2026/` — PDF slide decks
- `download_transcripts_2026.py` — Python utility to download available transcripts
- `README.md` — Repository overview and local usage instructions

## Public content rules

- The repository is **private**: published pages (home, lessons, README, docs) must never link to GitHub or mention the repository, cloning, forks, pull requests or issues. Mentions of GitHub Pages/Cloudflare Pages as hosting are the only exception.
- The site states that its contents are notes extracted from the lessons of the ARI Toscana course, **editions 2025 and 2026**. Keep this wording consistent in the home, lessons index, README and social preview.
- Each lesson opens with a `🎓 Esame ridotto` block (needed / partly needed / not needed for the exam with partial exemption, i.e. only Parts B and C of the official programme). Official-source additions that are not in the lesson must stay in a Starlight `:::note[… — contenuto non proveniente dalla lezione]` box, never in the lesson prose.

## Linting

Markdown is linted with **markdownlint** using the rules in `.markdownlint.json`. To lint all files:

```sh
npx markdownlint-cli2 "**/*.md"
```

To lint a single file:

```sh
npx markdownlint-cli2 site/src/content/docs/lezioni/lezione_01.md
```

Key rules enabled: MD013 (line length) is **disabled**. MD024 (duplicate headings), MD028 (blank line in blockquote), MD029 (ordered list prefix), MD036 (emphasis as heading), MD040 (fenced code language) are also disabled.

## Python Transcript Tool

Transcripts can be refreshed with the repository script [`download_transcripts_2026.py`](../download_transcripts_2026.py). Install dependencies and run:

```sh
pip install -r requirements.txt
python download_transcripts_2026.py
```

The `requirements.txt` requires `youtube-transcript-api>=1.0.3`. Transcripts are saved to:

- `transcripts/2026/` — plain-text with timestamps
- `transcripts (vtt)/2026/` — WebVTT subtitle files

## Deployment Pipeline

The CI workflow [`deploy.yml`](../.github/workflows/deploy.yml) runs on push to `main`, builds the Astro site from `site/`, and publishes `site/dist/` to GitHub Pages with base URL `/ari-crt-corso-2025`.

The site also supports Cloudflare Pages through environment detection in [`site/astro.config.mjs`](../site/astro.config.mjs), but the repository automation currently deploys GitHub Pages only.

The prebuild step runs [`site/scripts/og.mjs`](../site/scripts/og.mjs), which regenerates `site/public/og.png` from `site/public/og.svg`.

## Rendering Notes

Lesson guides still contain LaTeX-style `$...$` and `$$...$$` formulas, but the current Astro site does **not** have a math renderer wired in. Treat raw formula rendering on the site as a presentation defect to report; do not silently rewrite lesson content to work around it.

## File Naming Conventions

- Study guides: `site/src/content/docs/lezioni/lezione_XX.md` — `XX` is always **zero-padded two digits** (e.g., `lezione_01.md`, `lezione_22.md`)
- Transcripts: `transcripts/2026/ARI Toscana Formazione Corso 2026 Lezione XX DD MM YYYY.txt`
- VTT files: `transcripts (vtt)/2026/ARI Toscana Formazione Corso 2026 Lezione XX DD MM YYYY.vtt`

## Scoped Instruction Files

More specific rules are in `.github/instructions/`:

- `markdown.instructions.md` — applies to `**/*.md`: full markdown + MathJax formatting rules
- `study-guide.instructions.md` — contains the complete lesson-guide structure and quality rules used for the guides in `site/src/content/docs/lezioni/`

## Repository Usage

- For the commits, always follow instructions from: [ConventionalCommits](https://www.conventionalcommits.org/en/v1.0.0/#specification)

## Custom Agents

The site contents are **notes extracted from the lessons of the Tuscany amateur radio course** (ARI Toscana CRT), not the official course text. Three agents are defined in `.github/agents/`:

- `redattore-lezioni` — creates and updates the lesson guides in `site/src/content/docs/lezioni/`.
- `redattore-pagine` — keeps the generic and summary pages (home, lessons index, README, recordings list, navigation) consistent with the lessons.
- `qa-tester` — read-only QA: always checks that every recap page matches the current lessons and that every link is correct and leads to the right place, then layout and reading mode. Run it after any change to lessons, titles, navigation or assets.

## Language and Domain

- All transcripts and study guides are in **Italian**.
- The domain is **amateur radio (radioamatorismo)**: electronics, RF propagation, antennas, modulation, regulations, and exam preparation for the Italian amateur radio license.
- When generating or editing content, use Italian unless explicitly asked otherwise.
- Use correct Italian technical terminology for radio/electronics concepts (e.g., "impedenza", "modulazione", "propagazione", "antenna", "frequenza", "potenza").

## Transcript Conventions

- Transcripts are auto-generated from YouTube and may contain transcription errors, missing punctuation, or garbled technical terms.
- Each `.txt` transcript line starts with a timestamp (e.g., `00:02`, `01:23:45`).
- `.vtt` files follow the standard WebVTT format with timed cues.
- When working with transcripts, be aware of common Italian speech-to-text errors (e.g., "ertz" instead of "hertz", words merged or split incorrectly).

## Study Guide Generation Instructions

Study guides are stored in `site/src/content/docs/lezioni/`. When asked to generate a study guide from a transcript, follow these instructions exactly.

### Role

Act as an expert academic note-taker and study guide author. Transform the raw lecture transcript into an exhaustive, self-contained study document that a student can use to learn the subject without needing to watch the original video.

### Input

A full text transcript of a lecture or educational video. Timestamps may be included in the transcript.

### Pre-Analysis

Before writing, silently identify:

- The **main subject** and academic discipline
- The **target audience** (beginner / intermediate / advanced)
- The **core thesis or learning objective** of the lecture
- The **language** of the transcript — output the study guide in the SAME language
- Flag any content relevant to Italian/CEPT amateur radio licensing exam (regulations, band plans, technical formulas)

### Required Study Guide Structure

Generate the study guide using the following fixed structure:

#### Title

Use: `# 📘 Lezione XX - Titolo della Lezione` (where XX is the lesson number and "Titolo della Lezione" is the title of the lesson).

#### 📌 Overview

- Subject and topic
- Estimated study time for this guide
- Prerequisites: what the student should already know
- Learning objectives: what the student will know after studying

#### 📖 Core Content

Organize content into numbered sections and subsections following the logical flow of the lecture. Use emoji-prefixed headings for sections (`## 🔍`, `## 📈`, `## 📡`, etc.) and `### 🔹` for sub-sections ("Concetti di Base", "Dettagli Tecnici"). Do not put info on the timing of the transcription.S

For each section:

- Write a **conceptual explanation** in full prose (2–5 paragraphs), not just bullet points
- Define every **technical term** the first time it appears, formatted as: **Term** — definition
- Include **formulas, rules, or principles** in a dedicated block, clearly labeled
- Add **examples or analogies** where the lecturer provides them, or infer one if a concept is complex
- Note any **common mistakes or misconceptions** mentioned

#### 🔗 Concept Map (textual)

List the key concepts and how they relate to each other using short relational statements:

- Example: "Concept A → causes → Concept B"
- Example: "Concept C is a special case of → Concept D"

#### 📝 Key Takeaways

A numbered list of the most important facts, rules, or principles from the lecture. Each item should be a complete, standalone statement (2–3 sentences max).

#### ❓ Comprehension Questions

Generate 5–10 open-ended questions (NOT flashcards) that test deep understanding of the material. Questions should require reasoning, not just recall. Do NOT provide answers — these are for self-testing.

#### 📚 Glossary

Alphabetically sorted list of all defined technical terms with their definitions.

#### 👥 Partecipanti

List the speaker/instructor and audience (e.g., 👨‍🏫 **Relatore**: ...).

#### 📅 Informazioni Lezione

Metadata footer with: lesson number, date, duration, argument count, and keywords.

### Formatting Rules

- Use Markdown formatting throughout
- Use headers (`##`, `###`) to create clear hierarchy
- Bold (`**`) for terms, key concepts, and warnings
- Use `>` blockquotes for direct quotes from the speaker
- Use code blocks (` ``` `) ONLY for non-mathematical structured data (tables of values, pseudocode, signal formats); NEVER for math formulas
- If timestamps are present in the transcript, add (⏱ mm:ss) next to the relevant section header

#### Math Formula Rules

Write formulas in LaTeX/MathJax-style notation even though the current Astro site does not yet render them. This keeps the source material consistent until a math renderer is added. Never rewrite formulas as plain text or inside code blocks.

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

  - ❌ `\[...\]` (avoid — causes rendering issues in some site configurations)
  - ❌ plain code block with the formula inside
- Use standard LaTeX commands: `\frac{}{}`, `\cdot`, `\pi`, `\sqrt{}`, `^{}`, `_{}`, `\text{}`, `\Omega`, `\mu`, `\lambda`, `\Delta`, etc.
- For units inside formulas use `\text{}`: e.g., `$1\,\text{H} = \frac{1\,\text{Wb}}{1\,\text{A}}$`
- Always test that every `$` is paired and LaTeX braces `{}` are balanced

### Content Rules

- Extract and organize the actual technical content discussed
- Correct obvious transcription errors in study guides (but keep transcripts as-is)
- Reference specific exam topics ("domande d'esame") when the transcript mentions them
- Preserve the chronological flow of the lecture while grouping related topics

### Quality Rules

- The guide must be **EXHAUSTIVE**: a student who reads it should not need to re-watch the video
- Do NOT skip or summarize sections because they seem minor
- If the transcript is unclear or incomplete on a topic, add a note: ⚠️ _This section may be incomplete in the source transcript._
- Do NOT add information not present in the transcript
- Maintain a neutral, academic tone throughout

### Output

Return ONLY the study guide in Markdown. No preamble, no meta-commentary about what was done.
