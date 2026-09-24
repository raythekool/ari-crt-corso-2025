import re

with open("/tmp/original_lezione_14.md", "r", encoding="utf-8") as f:
    text = f.read()

# Update frontmatter and titles
text = text.replace("title: \"Trasduttori, Mixer e Trasmettitori\"", "title: \"Trasduttori, Miscelatori e Trasmettitori\"")
text = text.replace("permalink: /guide-studio/lezione_14.html", "permalink: /guide-studio/lezione_13.html")
text = text.replace("# 📘 Lezione 14 - Trasduttori, Mixer e Trasmettitori", "# 📘 Lezione 13 - Trasduttori, Miscelatori e Trasmettitori")
text = text.replace("**Lezione**            | 14", "**Lezione**            | 13")
text = text.replace("11 giugno 2025", "10 giugno 2026")

# Update prerequisiti numbers
text = text.replace("Lezione 13", "Lezione 12")
text = text.replace("Correzione Quiz Lezione 13", "Correzione Quiz Lezione 12")

def insert_after(text, search_str, image_filename, alt_text):
    image_html = f'\n<div align="center"><img src="../assets/images/lezioni/lezione_13/{image_filename}" alt="{alt_text}" width="50%"></div><br>\n'
    return text.replace(search_str, search_str + image_html)

text = insert_after(text, "#### 🔹 Il Microfono", "slide-02.jpg", "Microfono")
text = insert_after(text, "#### 🔹 L'Altoparlante", "slide-03.jpg", "Altoparlante")
text = insert_after(text, "#### 🔹 Funzionamento", "slide-05.jpg", "Miscelatore")
text = insert_after(text, "### 4. 📡 Schema Generale del Trasmettitore (⏱ 35:30–40:00)", "slide-09.jpg", "Blocchi base del trasmettitore")
text = insert_after(text, "#### 🔹 Schema CW a Singola Frequenza", "slide-12.jpg", "Trasmettitore CW semplice")
text = insert_after(text, "#### 🔹 Schema CW Multibanda con Conversione di Frequenza", "slide-13.jpg", "Trasmettitore multibanda con miscelatore")
text = insert_after(text, "#### 🔹 Circuito di Accordo (Pi-Greco)", "slide-15.jpg", "Circuito Pi-greco")
text = insert_after(text, "#### 🔹 Click di Manipolazione", "slide-16.jpg", "Click di manipolazione")
text = insert_after(text, "### 7. 📻 Trasmettitore AM (⏱ 97:00–99:40)", "slide-17.jpg", "Generazione Modulazione di Ampiezza")
text = insert_after(text, "variando la tensione di alimentazione dello stadio finale.", "slide-18.jpg", "Generazione AM schema")
text = insert_after(text, "1. **Modulatore Bilanciato**: Riceve il segnale", "slide-19.jpg", "Modulatore bilanciato per DSB")
text = insert_after(text, "### 6. 📻 Trasmettitore SSB (⏱ 58:30–88:00)", "slide-21.jpg", "Schema a blocchi trasmettitore SSB")
text = insert_after(text, "#### 🔹 Armoniche e Distorsione", "slide-28.jpg", "Armoniche flat topping")
text = insert_after(text, "il segnale si taglia (flat-topping)", "slide-29.jpg", "Flat-topping e armoniche dispari")
text = insert_after(text, "L'intermodulazione si verifica quando", "slide-31.jpg", "Intermodulazione con due segnali")
text = insert_after(text, "La formula generica è $2f_1 - f_2$ e $2f_2 - f_1$.", "slide-32.jpg", "Intermodulazione di ordine superiore")

with open("/data/repos/ari-crt-corso-2025/site/guide-studio/lezione_13.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
