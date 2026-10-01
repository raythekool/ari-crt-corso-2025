import os
import glob
import subprocess

pdf_dir = "slides 2026"
pdfs = os.listdir(pdf_dir)

for i in range(1, 20):
    if i == 3:
        continue # Already done
        
    # Find the pdf for lesson i
    pdf_path = None
    for pdf in pdfs:
        # Check if "Lezione X." or "Lezione_X." or "Lezione X " etc is in the filename
        # A simple check:
        import re
        if re.search(rf'Lezione[ _]?{i}\b', pdf, re.IGNORECASE):
            pdf_path = os.path.join(pdf_dir, pdf)
            break
            
    if pdf_path:
        print(f"\n================ Processing Lesson {i:02d} ================")
        subprocess.run([".venv/bin/python", "scripts/extract_slides.py", str(i), pdf_path])
    else:
        print(f"Warning: Could not find PDF for lesson {i}")

