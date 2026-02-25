# Copilot Instructions — ARI CRT Corso 2025

## Project Overview

This repository contains materials for the **Corso Aspiranti Radioamatori ARI Toscana CRT 2025** (Italian amateur radio licensing course). It includes YouTube lecture transcripts, study guides, and a Python utility to download transcripts.

## Repository Structure

- `transcripts/` — Plain-text transcripts (`.txt`) of each lecture, with timestamps
- `transcripts (vtt)/` — WebVTT subtitle files (`.vtt`) for each lecture
- `guide_studio/` — Markdown study guides summarizing lecture content
- `requirements.txt` — Python dependencies
- `README.md` — Lecture index with YouTube links

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

## Study Guide Format (`guide-studio/`)

Study guides follow this structure:

- **Title**: `# 📘 Lezione XX - Corso Radioamatori`
- **Sections**: Organized by topic with emoji-prefixed headings (`## 🔍`, `## 📈`, `## 📡`, etc.)
- **Sub-sections**: Use `### 🔹` for "Concetti di Base" and "Dettagli Tecnici"
- **Metadata footer**: Includes lesson number, date, duration, argument count, and keywords
- **Participants section**: Lists speaker/instructor and audience
- **Timestamps section**: Key time ranges from the lecture

## Content Generation Guidelines

- When creating study guides from transcripts, extract and organize the actual technical content discussed.
- Correct obvious transcription errors in generated study guides (but keep transcripts as-is).
- Include relevant formulas using proper notation when applicable (e.g., $\lambda = \frac{c}{f}$).
- Reference specific exam topics ("domande d'esame") when the transcript mentions them.
- Preserve the chronological flow of the lecture while grouping related topics.

---

## Study Guide Generation Prompt

Use the following prompt when asked to generate a study guide from a transcript. Paste it into any capable LLM (ChatGPT, Claude, Gemini, Copilot) followed by the transcript text.

````
# ROLE
You are an expert academic note-taker and study guide author.
Your goal is to transform a raw lecture transcript into an
exhaustive, self-contained study document that a student
can use to learn the subject without needing to watch
the original video.

# INPUT
A full text transcript of a lecture or educational video.
[Optional: timestamps may be included in the transcript]

# INSTRUCTIONS

## 1. Pre-Analysis
Before writing, silently identify:
- The **main subject** and academic discipline
- The **target audience** (beginner / intermediate / advanced)
- The **core thesis or learning objective** of the lecture
- The **language** of the transcript → output the study guide
  in the SAME language
- Flag any content relevant to Italian/CEPT amateur radio
  licensing exam (regulations, band plans, technical formulas)

## 2. Study Guide Structure
Generate the study guide using the following fixed structure:

### 📌 Overview
- Subject and topic
- Estimated study time for this guide
- Prerequisites: what the student should already know
- Learning objectives: what the student will know after studying

### 📖 Core Content
Organize content into numbered sections and subsections
following the logical flow of the lecture.

For each section:
- Write a **conceptual explanation** in full prose
  (2–5 paragraphs), not just bullet points
- Define every **technical term** the first time it appears,
  formatted as: **Term** — definition
- Include **formulas, rules, or principles** in a dedicated
  block, clearly labeled
- Add **examples or analogies** where the lecturer provides
  them, or infer one if a concept is complex
- Note any **common mistakes or misconceptions** mentioned

### 🔗 Concept Map (textual)
List the key concepts and how they relate to each other
using short relational statements:
Example: "Concept A → causes → Concept B"
Example: "Concept C is a special case of → Concept D"

### 📝 Key Takeaways
A numbered list of the most important facts, rules,
or principles from the lecture. Each item should be
a complete, standalone statement (2–3 sentences max).

### ❓ Comprehension Questions
Generate 5–10 open-ended questions (NOT flashcards)
that test deep understanding of the material.
Questions should require reasoning, not just recall.
Do NOT provide answers — these are for self-testing.

### 📚 Glossary
Alphabetically sorted list of all defined technical terms
with their definitions.

## 3. Formatting Rules
- Use Markdown formatting throughout
- Use headers (##, ###) to create clear hierarchy
- Bold (**) for terms, key concepts, and warnings
- Use > blockquotes for direct quotes from the speaker
- Use code blocks for formulas or structured data
- If timestamps are present in the transcript,
  add (⏱ mm:ss) next to the relevant section header

## 4. Quality Rules
- The guide must be EXHAUSTIVE: a student who reads it
  should not need to re-watch the video
- Do NOT skip or summarize sections because they seem minor
- If the transcript is unclear or incomplete on a topic,
  add a note: ⚠️ *This section may be incomplete
  in the source transcript.*
- Do NOT add information not present in the transcript
- Maintain a neutral, academic tone throughout

# OUTPUT
Return ONLY the study guide in Markdown.
No preamble, no meta-commentary about what you did.
````
