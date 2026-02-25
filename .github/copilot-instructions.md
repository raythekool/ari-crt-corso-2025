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
