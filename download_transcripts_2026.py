#!/usr/bin/env python3
"""
Script per scaricare i transcript delle lezioni del Corso ARI CRT 2026.
Salva:
- formato testo con timestamp (MM:SS testo) in transcripts/
- formato WebVTT in 'transcripts (vtt)/'
"""

import os
import re
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

OUTPUT_DIR_TXT = os.path.join("transcripts", "2026")
OUTPUT_DIR_VTT = os.path.join("transcripts (vtt)", "2026")

LEZIONI_2026 = [
    # num, date_str (DD MM YYYY), url, title
    (3, "01 04 2026", "https://www.youtube.com/watch?v=C_19T6kHGI8", "Lezione 03"),
    (4, "08 04 2026", "https://youtu.be/oMHiAE6ckzo", "Lezione 04"),
    (5, "15 04 2026", "https://youtu.be/pxnhOJFaxoU", "Lezione 05"),
    (6, "22 04 2026", "https://youtu.be/XZU93COksIo", "Lezione 06"),
    (7, "29 04 2026", "https://youtu.be/mflme_j99Fs", "Lezione 07"),
    (8, "05 05 2026", "https://youtu.be/-q9u3xRE7E8", "Lezione 08"),
    (9, "13 05 2026", "https://youtu.be/ATsOd6giY08", "Lezione 09"),
    (10, "20 05 2026", "https://youtu.be/p5A-77jjy2c", "Lezione 10"),
    (11, "27 05 2026", "https://youtu.be/wTMDxppgASw", "Lezione 11"),
    (12, "03 06 2026", "https://youtu.be/pmU82oVcYLM", "Lezione 12"),
    (13, "10 06 2026", "https://youtu.be/L4qM7Rpn0Js", "Lezione 13"),
    (14, "17 06 2026", "https://youtu.be/2GVGKXY-h68", "Lezione 14"),
    (15, "24 06 2026", "https://youtu.be/VepbJqd5s5o", "Lezione 15"),
    (16, "02 09 2026", "https://youtu.be/I88higsfbUk", "Lezione 16 Linee di trasmissione"),
    (17, "09 09 2026", "https://youtu.be/MY72-6kiK2I", "Lezione 17 Propagazione"),
    (18, "16 09 2026", "https://youtu.be/XXliNcZlkMA", "Lezione 18 Antenne parte 1"),
    (19, "23 09 2026", "https://youtu.be/j8PrbhUYPmE", "Lezione 19 Antenne parte 2"),
]


def extract_video_id(url: str) -> str | None:
    patterns = [
        r"youtu\.be/([a-zA-Z0-9_-]+)",
        r"youtube\.com/watch\?v=([a-zA-Z0-9_-]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def format_seconds_to_vtt(seconds: float) -> str:
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    return f"{hrs:02d}:{mins:02d}:{secs:02d}.{millis:03d}"


def build_vtt(entries) -> str:
    lines = ["WEBVTT\n"]
    for i, e in enumerate(entries, 1):
        start_str = format_seconds_to_vtt(e.start)
        end_str = format_seconds_to_vtt(e.start + e.duration)
        lines.append(f"{i}\n{start_str} --> {end_str}\n{e.text}\n")
    return "\n".join(lines)


def build_txt(entries) -> str:
    lines = []
    for e in entries:
        mins = int(e.start // 60)
        secs = int(e.start % 60)
        lines.append(f"{mins:02d}:{secs:02d} {e.text}")
    return "\n".join(lines) + "\n"


def main():
    os.makedirs(OUTPUT_DIR_TXT, exist_ok=True)
    os.makedirs(OUTPUT_DIR_VTT, exist_ok=True)
    api = YouTubeTranscriptApi()

    print("Inizio download transcript Corso 2026...")
    print("-" * 60)

    success = 0
    failed = 0

    for num, date_str, url, _ in LEZIONI_2026:
        base_name = f"ARI Toscana Formazione Corso 2026 Lezione {num:02d} {date_str}"
        txt_path = os.path.join(OUTPUT_DIR_TXT, f"{base_name}.txt")
        vtt_path = os.path.join(OUTPUT_DIR_VTT, f"{base_name}.vtt")

        vid = extract_video_id(url)
        if not vid:
            print(f"❌ Lezione {num:02d}: URL non valido ({url})")
            failed += 1
            continue

        try:
            transcript_list = api.list(vid)
            # Cerca prima italiano manuale o auto-generato
            try:
                t = transcript_list.find_transcript(["it", "it-IT"])
            except Exception:
                # Seleziona la prima lingua disponibile
                t = next(iter(transcript_list))

            entries = t.fetch()

            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(build_txt(entries))

            with open(vtt_path, "w", encoding="utf-8") as f:
                f.write(build_vtt(entries))

            print(f"✅ Lezione {num:02d} ({date_str}): salvata ({len(entries)} segmenti, lingua: {t.language})")
            success += 1

        except TranscriptsDisabled:
            print(f"🔒 Lezione {num:02d}: sottotitoli disabilitati per il video {vid}")
            failed += 1
        except NoTranscriptFound:
            print(f"🔍 Lezione {num:02d}: nessun transcript trovato per {vid}")
            failed += 1
        except Exception as ex:
            print(f"❌ Lezione {num:02d}: errore ({ex})")
            failed += 1

        time.sleep(1.5)

    print("-" * 60)
    print(f"Completato: {success} scaricati con successo, {failed} non disponibili/falliti.")


if __name__ == "__main__":
    main()
