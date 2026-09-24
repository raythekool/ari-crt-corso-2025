import re

with open('site/guide-studio/lezione_14_temp.md', 'r') as f:
    text = f.read()

# Update Frontmatter and Title
text = text.replace('title: "Tecnica dei Ricevitori"', 'title: "I Ricevitori"')
text = text.replace('permalink: /guide-studio/lezione_15.html', 'permalink: /guide-studio/lezione_14.html')
text = text.replace('# 📘 Lezione 15 - Tecnica dei Ricevitori', '# 📘 Lezione 14 - I Ricevitori')

# Insert Slide 2
slide2 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-02.jpg" alt="Sensibilità, Selettività, Stabilità" width="50%"></div><br>\n'
text = text.replace('### 3. 🔍 Le tre caratteristiche fondamentali del ricevitore (⏱ 19:15)\n\nUn buon ricevitore deve possedere tre caratteristiche essenziali:', 
                    '### 3. 🔍 Le tre caratteristiche fondamentali del ricevitore\n\n' + slide2 + 'Un buon ricevitore deve possedere tre caratteristiche essenziali:')

# Insert Slide 3
slide3 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-03.jpg" alt="Schema a blocchi supereterodina" width="50%"></div><br>\n'
text = text.replace('#### 🔹 Schema a blocchi della supereterodina\n\n```',
                    '#### 🔹 Schema a blocchi della supereterodina\n\n' + slide3 + '```')

# Insert Slide 4
slide4 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-04.jpg" alt="Ricevitore a doppia conversione" width="50%"></div><br>\n'
text = text.replace('### 5. 🔄 Supereterodina a doppia conversione (⏱ 44:30)\n\nIn molti ricevitori si effettua una **doppia conversione**:',
                    '### 5. 🔄 Supereterodina a doppia conversione\n\n' + slide4 + 'In molti ricevitori si effettua una **doppia conversione**:')

# Insert Slide 5
slide5 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-05.jpg" alt="Tipi di amplificatori" width="50%"></div><br>\n'
text = text.replace('### 6. 🔊 Tre tipi di amplificatori nel ricevitore (⏱ 46:51)\n\nIn un ricevitore sono presenti tre categorie di amplificatori:',
                    '### 6. 🔊 Tre tipi di amplificatori nel ricevitore\n\n' + slide5 + 'In un ricevitore sono presenti tre categorie di amplificatori:')

# Insert Slide 8
slide8 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-08.jpg" alt="Ricevitore CW" width="50%"></div><br>\n'
text = text.replace('### 7. 📶 Ricevitore per CW — Telegrafia (⏱ 48:46)\n\n#### 🔹 Caratteristiche del filtro',
                    '### 7. 📶 Ricevitore per CW — Telegrafia\n\n' + slide8 + '#### 🔹 Caratteristiche del filtro')

# Insert Slide 10
slide10 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-10.jpg" alt="Ricevitore SSB" width="50%"></div><br>\n'
text = text.replace('### 8. 📡 Ricevitore per SSB (⏱ 61:20)\n\n#### 🔹 Caratteristiche del filtro',
                    '### 8. 📡 Ricevitore per SSB\n\n' + slide10 + '#### 🔹 Caratteristiche del filtro')

# Insert Slide 12
slide12 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-12.jpg" alt="Ricevitore AM" width="50%"></div><br>\n'
text = text.replace('### 9. 📻 Ricevitore per AM (⏱ 71:51)\n\n#### 🔹 Caratteristiche del filtro',
                    '### 9. 📻 Ricevitore per AM\n\n' + slide12 + '#### 🔹 Caratteristiche del filtro')

# Insert Slide 14 & 15
slide14_15 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-14.jpg" alt="Ricevitore FM" width="50%"></div><br>\n<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-15.jpg" alt="Componenti ricevitore FM" width="50%"></div><br>\n'
text = text.replace('### 10. 📡 Ricevitore per FM (⏱ 76:28)\n\n#### 🔹 Caratteristiche del filtro',
                    '### 10. 📡 Ricevitore per FM\n\n' + slide14_15 + '#### 🔹 Caratteristiche del filtro')

# Insert Slide 16
slide16 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-16.jpg" alt="AGC" width="50%"></div><br>\n'
text = text.replace('### 11. 🎛️ AGC — Controllo Automatico di Guadagno (⏱ 92:13)\n\nIl **Controllo Automatico di Guadagno**',
                    '### 11. 🎛️ AGC — Controllo Automatico di Guadagno\n\n' + slide16 + 'Il **Controllo Automatico di Guadagno**')

# Insert Slide 17
slide17 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-17.jpg" alt="S-meter" width="50%"></div><br>\n'
text = text.replace('#### 🔹 S-meter\n\nLa stessa tensione proporzionale all\'intensità del segnale ricevuto viene usata per pilotare lo **S-meter**',
                    '#### 🔹 S-meter\n\n' + slide17 + 'La stessa tensione proporzionale all\'intensità del segnale ricevuto viene usata per pilotare lo **S-meter**')

# Insert Slide 18 & 19
slide18_19 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-18.jpg" alt="Frequenza immagine" width="50%"></div><br>\n<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-19.jpg" alt="Esempio frequenza immagine" width="50%"></div><br>\n'
text = text.replace('### 12. 🔀 Frequenza immagine (⏱ 102:32)\n\nLa **frequenza immagine**',
                    '### 12. 🔀 Frequenza immagine\n\n' + slide18_19 + 'La **frequenza immagine**')

# Insert Slide 20
slide20 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-20.jpg" alt="Soluzioni frequenza immagine" width="50%"></div><br>\n'
text = text.replace('#### 🔹 Soluzioni\n\n1. **Circuiti selettivi prima del mixer**',
                    '#### 🔹 Soluzioni\n\n' + slide20 + '1. **Circuiti selettivi prima del mixer**')

# Insert Slide 21
slide21 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-21.jpg" alt="Problemi ricevitori" width="50%"></div><br>\n'
text = text.replace('### 13. ⚠️ Problemi dei ricevitori (⏱ 112:03)\n\nI ricevitori supereterodina possono soffrire',
                    '### 13. ⚠️ Problemi dei ricevitori\n\n' + slide21 + 'I ricevitori supereterodina possono soffrire')

# Insert Slide 22 & 23
slide22_23 = '<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-22.jpg" alt="Sensibilità" width="50%"></div><br>\n<div align="center"><img src="../assets/images/lezioni/lezione_14/slide-23.jpg" alt="Formula del rumore" width="50%"></div><br>\n'
text = text.replace('### 14. 📊 Sensibilità e rapporto segnale/rumore (⏱ 117:42)\n\nLa **sensibilità**',
                    '### 14. 📊 Sensibilità e rapporto segnale/rumore\n\n' + slide22_23 + 'La **sensibilità**')

# Fix Footers
text = text.replace('| **Lezione**          | 15', '| **Lezione**          | 14')
text = text.replace('| **Data**             | 18 giugno 2025', '| **Data**             | 17 giugno 2026')
text = text.replace('14 (⏱ 00:02)', '13')
text = text.replace(' (⏱ 13:52)', '')
text = text.replace(' (⏱ 25:03)', '')
text = text.replace(' (⏱ 125:18)', '')

# Also remove other timing texts just in case (the regex way)
text = re.sub(r' \(⏱ \d{2}:\d{2}\)', '', text)

with open('site/guide-studio/lezione_14.md', 'w') as f:
    f.write(text)

print("Done")
