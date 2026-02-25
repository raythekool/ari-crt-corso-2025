#!/usr/bin/env python3
"""
Script per scaricare i transcript delle lezioni del corso
Aspiranti Radioamatori ARI Toscana CRT 2025.

Uso:
    pip install -r requirements.txt
    python download_transcripts.py

I transcript verranno salvati nella cartella ./transcripts/
"""

import re
import os
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

# Cartella di output
OUTPUT_DIR = "transcripts"

# Lista delle lezioni
LEZIONI = [
    ("Lezione_01", "05-03-2025", "https://youtu.be/ZliWEcTEQhw"),
    ("Lezione_02", "12-03-2025", "https://youtu.be/Rb0OC1pjHzQ"),
    ("Lezione_03", "19-03-2025", "https://youtu.be/XofmUruCxdk"),
    ("Lezione_04", "26-03-2025", "https://youtu.be/kAcblCn2XtI"),
    ("Lezione_05", "02-04-2025", "https://youtu.be/8ZwIbOkQ2jw"),
    ("Lezione_06", "09-04-2025", "https://youtu.be/qXZjlGC6OzM"),
    ("Lezione_07", "16-04-2025", "https://youtu.be/x_ArVY_hELo"),
    ("Lezione_08", "23-04-2025", "https://youtu.be/0iuDGQIka6M"),
    ("Lezione_09", "07-05-2025", "https://youtu.be/lW79RYE_7ds"),
    ("Lezione_10", "14-05-2025", "https://youtu.be/c0SRE-zw1Q4"),
    ("Lezione_11", "21-05-2025", "https://youtu.be/2fBbfPQQVts"),
    ("Lezione_12", "28-05-2025", "https://youtu.be/yuNAN72b7tc"),
    ("Lezione_13", "04-06-2025", "https://youtu.be/a6RmrP8iwFs"),
    ("Lezione_14", "11-06-2025", "https://youtu.be/YM5H3Y6G-4I"),
    ("Lezione_15", "18-06-2025", "https://youtu.be/UaDGhyB0T5I"),
    ("Lezione_16", "25-06-2025", "https://youtu.be/pGOycXhTISI"),
    ("Serata_Speciale", "02-07-2025", "https://youtu.be/iTg4BaclXYs"),
    ("Lezione_18", "03-09-2025", "https://youtu.be/b2DfH0QReZM"),
    ("Lezione_19", "10-09-2025", "https://www.youtube.com/watch?v=WzYG_u0xn2k"),
    ("Lezione_20", "17-09-2025", "https://youtu.be/tf9stbW989w"),
    ("Lezione_21", "24-09-2025", "https://youtu.be/rlzS2xD51GY"),
    ("Lezione_22", "01-10-2025", "https://youtu.be/Ei0UzSfS-SM"),
    ("Lezione_23", "08-10-2025", "https://youtu.be/KA3ORkjTle4"),
    ("Simulazione_Esame", "22-10-2025", "https://youtu.be/NviNlhPfp9E"),
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


def fetch_transcript(video_id: str) -> tuple[str, str]:
    """
    Scarica il transcript del video.
    Ritorna (testo, lingua) oppure (None, messaggio_errore).
    """
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.list(video_id)

    # Priorità: italiano > italiano auto-generato > qualsiasi lingua
    for lang_codes in [["it"], ["it-IT"]]:
        try:
            t = transcript_list.find_transcript(lang_codes)
            fetched = t.fetch()
            text = "\n".join(e.text for e in fetched)
            return text, fetched.language
        except Exception:
            pass

    # Prova auto-generato in italiano
    try:
        t = transcript_list.find_generated_transcript(["it", "it-IT"])
        fetched = t.fetch()
        text = "\n".join(e.text for e in fetched)
        return text, f"{fetched.language} (auto-generato)"
    except Exception:
        pass

    # Prendi la prima lingua disponibile
    for t in transcript_list:
        fetched = t.fetch()
        text = "\n".join(e.text for e in fetched)
        return text, f"{fetched.language} (prima disponibile)"

    return None, "Nessun transcript disponibile"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\n📁 Output nella cartella: ./{OUTPUT_DIR}/\n")
    print("-" * 60)

    ok, skipped, errors = 0, 0, 0

    for nome, data, url in LEZIONI:
        filename = f"{OUTPUT_DIR}/{nome}_{data}.txt"
        video_id = extract_video_id(url)

        if not video_id:
            print(f"❌ {nome}: URL non valido")
            errors += 1
            continue

        # Skip se il file esiste già
        if os.path.exists(filename):
            print(f"⏭️  {nome}: già presente, skip")
            skipped += 1
            continue

        try:
            text, lang = fetch_transcript(video_id)

            if text:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"# {nome.replace('_', ' ')} - {data}\n")
                    f.write(f"# URL: {url}\n")
                    f.write(f"# Lingua: {lang}\n")
                    f.write(f"# Video ID: {video_id}\n\n")
                    f.write(text)
                print(f"✅ {nome}: salvato ({lang})")
                ok += 1
            else:
                print(f"⚠️  {nome}: {lang}")
                errors += 1

        except TranscriptsDisabled:
            print(f"🔒 {nome}: transcript disabilitati dal proprietario")
            errors += 1
        except NoTranscriptFound:
            print(f"🔍 {nome}: nessun transcript trovato")
            errors += 1
        except Exception as e:
            print(f"❌ {nome}: errore - {e}")
            errors += 1

        time.sleep(2)  # Evita rate limiting di YouTube

    print("-" * 60)
    print(f"\n✅ Completati: {ok} | ⏭️  Saltati: {skipped} | ❌ Errori: {errors}\n")


if __name__ == "__main__":
    main()
