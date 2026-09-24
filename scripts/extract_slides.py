#!/usr/bin/env python3
import sys
import os
import subprocess

def process_lesson(lesson_num_str, pdf_path):
    lesson_num = int(lesson_num_str)
    output_dir = f"site/assets/images/lezioni/lezione_{lesson_num:02d}"
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Elaborazione PDF: {pdf_path}")
    print(f"Cartella destinazione: {output_dir}")
    
    # 1. Estrazione del testo usando pdftotext
    txt_output_path = os.path.join(output_dir, f"lezione_{lesson_num:02d}_testo.txt")
    print("Estrazione testo...")
    subprocess.run(["pdftotext", pdf_path, txt_output_path], check=True)
    
    # 2. Estrazione immagini usando pdftocairo
    # Genera immagini con pattern: slide-01.jpg, slide-02.jpg, ecc.
    print("Estrazione slide come immagini JPEG...")
    prefix = os.path.join(output_dir, "slide")
    # pdftocairo -jpeg -jpegopt quality=75 -scale-to 1024
    cmd = [
        "pdftocairo", 
        "-jpeg", 
        "-jpegopt", "quality=75", 
        "-scale-to", "1024", 
        pdf_path, 
        prefix
    ]
    subprocess.run(cmd, check=True)
    
    # Rinomina i file da slide-01.jpg a slide-01.jpg (pdftocairo aggiunge '-01', '-02', ma senza zeri per i numeri brevi, aspettate. 
    # pdftocairo usa %d o zeri in base al numero di pagine. Es: slide-01.jpg, slide-02.jpg).
    
    print("✅ Completato!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python extract_slides.py <numero_lezione> <percorso_pdf>")
        sys.exit(1)
    
    process_lesson(sys.argv[1], sys.argv[2])
