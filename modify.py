import re

with open('/data/repos/ari-crt-corso-2025/site/guide-studio/lezione_02.md', 'r') as f:
    text = f.read()

# Date update
text = text.replace('12/03/2025', '12/03/2026')

# Insert slide-02 and slide-03
text = text.replace(
    'Collegando il generatore a un **carico** tramite cavi elettrici, scorre una corrente.',
    '<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-02.jpg" alt="Circuito base" width="50%"></div><br>\n\n<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-03.jpg" alt="Grandezze fondamentali" width="50%"></div><br>\n\nCollegando il generatore a un **carico** tramite cavi elettrici, scorre una corrente.'
)

# Insert slide-05
text = text.replace(
    '> **Definizione:**',
    '<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-05.jpg" alt="La resistenza elettrica" width="50%"></div><br>\n\n> **Definizione:**'
)

# Insert slide-06 and 07
text = text.replace(
    '> - $S$ = sezione del conduttore (in mm²)\n\nLa **resistività**',
    '> - $S$ = sezione del conduttore (in mm²)\n\n<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-06.jpg" alt="Fattori da cui dipende la resistenza" width="50%"></div><br>\n\n<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-07.jpg" alt="Resistenza, lunghezza e sezione" width="50%"></div><br>\n\nLa **resistività**'
)

# Insert slide-14
text = text.replace(
    '1. **Leggere bene la domanda** e capire cosa viene chiesto',
    '<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-14.jpg" alt="Metodo di risoluzione" width="50%"></div><br>\n\n1. **Leggere bene la domanda** e capire cosa viene chiesto'
)

# Insert slide-15 and 16
text = text.replace(
    '**Esempio 1** (⏱ 28:08):',
    '<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-15.jpg" alt="Esempio Legge di Ohm 1" width="50%"></div><br>\n\n**Esempio 1** (⏱ 28:08):'
)

text = text.replace(
    '**Esempio 2** (⏱ 29:29):',
    '<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-16.jpg" alt="Esempio Legge di Ohm 2" width="50%"></div><br>\n\n**Esempio 2** (⏱ 29:29):'
)

# Insert slide-22 and 23
text = text.replace(
    'Il resistore ha un **simbolo elettrico** a zigzag',
    '<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-23.jpg" alt="Simbolo elettrico" width="50%"></div><br>\n\n<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-22.jpg" alt="Funzione del resistore" width="50%"></div><br>\n\nIl resistore ha un **simbolo elettrico** a zigzag'
)

# Insert slide-24 and 25
text = text.replace(
    'La formula $P = \\frac{V^2}{R}$ è particolarmente usata',
    '<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-24.jpg" alt="Esempio potenza 1" width="50%"></div><br>\n\n<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-25.jpg" alt="Esempio potenza 2" width="50%"></div><br>\n\nLa formula $P = \\frac{V^2}{R}$ è particolarmente usata'
)

# Insert slide-26
text = text.replace(
    '- **PTC** (Positive Temperature Coefficient, coefficiente di temperatura positivo) — quando la temperatura **aumenta**, il valore della resistenza **aumenta**.',
    '- **PTC** (Positive Temperature Coefficient, coefficiente di temperatura positivo) — quando la temperatura **aumenta**, il valore della resistenza **aumenta**.\n\n<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-26.jpg" alt="Resistori NTC e PTC" width="50%"></div><br>'
)

# Insert slide-27
text = text.replace(
    '- La **temperatura** di esercizio\n\nI resistori reali',
    '- La **temperatura** di esercizio\n\n<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-27.jpg" alt="Il resistore ideale" width="50%"></div><br>\n\nI resistori reali'
)

# Insert slide-30
text = text.replace(
    'In realtà, generatori ideali non esistono.',
    'In realtà, generatori ideali non esistono.\n\n<div align="center"><img src="../assets/images/lezioni/lezione_02/slide-30.jpg" alt="Il generatore ideale" width="50%"></div><br>'
)


with open('/data/repos/ari-crt-corso-2025/site/guide-studio/lezione_02.md', 'w') as f:
    f.write(text)

