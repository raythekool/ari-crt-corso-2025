#!/usr/bin/env python3
import sys
import os
import subprocess
import pymupdf

def process_lesson(lesson_num_str, pdf_path):
    lesson_num = int(lesson_num_str)
    output_dir = f"site/assets/images/lezioni/lezione_{lesson_num:02d}"
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Elaborazione PDF: {pdf_path}")
    print(f"Cartella destinazione: {output_dir}")
    
    txt_output_path = os.path.join(output_dir, f"lezione_{lesson_num:02d}_testo.txt")
    print("Estrazione testo...")
    subprocess.run(["pdftotext", pdf_path, txt_output_path], check=True)
    
    # Analyze with PyMuPDF
    doc = pymupdf.open(pdf_path)
    slides_to_keep = []
    
    print("Analisi intelligente delle slide...")
    for i in range(len(doc)):
        page = doc[i]
        image_list = page.get_images(full=True)
        paths = page.get_drawings()
        
        has_raster = len(image_list) > 0
        has_complex_vector = len(paths) > 10 # More than just the background template
        
        if has_raster or has_complex_vector:
            slides_to_keep.append(i + 1)
            print(f"  Slide {i+1:02d}: MANTENUTA (contiene grafica)")
        else:
            print(f"  Slide {i+1:02d}: SCARTATA (solo testo/template)")
            
    print("Estrazione slide come immagini JPEG...")
    prefix = os.path.join(output_dir, "slide")
    cmd = [
        "pdftocairo", 
        "-jpeg", 
        "-jpegopt", "quality=75", 
        "-scale-to", "1024", 
        pdf_path, 
        prefix
    ]
    subprocess.run(cmd, check=True)
    
    # Remove discarded slides to save space and avoid confusing the subagent
    for i in range(1, len(doc) + 1):
        if i not in slides_to_keep:
            img_path = f"{prefix}-{i:02d}.jpg"
            if os.path.exists(img_path):
                os.remove(img_path)
    
    print("✅ Completato!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python extract_slides.py <numero_lezione> <percorso_pdf>")
        sys.exit(1)
    
    process_lesson(sys.argv[1], sys.argv[2])
