import sys
import pymupdf

def analyze_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    for i in range(len(doc)):
        page = doc[i]
        image_list = page.get_images(full=True)
        paths = page.get_drawings()
        
        has_raster = len(image_list) > 0
        has_complex_vector = len(paths) > 10
        
        if has_raster or has_complex_vector:
            print(f"Slide {i+1:02d}: KEEP (Images: {len(image_list)}, Vectors: {len(paths)})")
        else:
            print(f"Slide {i+1:02d}: DISCARD (Text-only template)")

if __name__ == "__main__":
    analyze_pdf(sys.argv[1])
