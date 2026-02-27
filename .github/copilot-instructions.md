# Copilot Instructions — ARI CRT Corso 2025

## Project Overview

This repository contains materials for the **Corso Aspiranti Radioamatori ARI Toscana CRT 2025** (Italian amateur radio licensing course). It includes YouTube lecture transcripts, study guides, and a Python utility to download transcripts.

## Repository Structure

- `transcripts/` — Plain-text transcripts (`.txt`) of each lecture, with timestamps
- `transcripts (vtt)/` — WebVTT subtitle files (`.vtt`) for each lecture
- `guide-studio/` — Markdown study guides summarizing lecture content
- `requirements.txt` — Python dependencies
- `README.md` — Lecture index with YouTube links

## Repository Usage

- For the commits, always follow instructions from: [ConventionalCommits](https://www.conventionalcommits.org/en/v1.0.0/#specification)

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

Study guides are stored in `guide-studio/`. When asked to generate a study guide from a transcript, follow these instructions exactly.

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

#### Math Formula Rules (MathJax v3)

The site renders math via **MathJax v3**. Always use LaTeX math notation — never write formulas as plain text or inside code blocks.

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
