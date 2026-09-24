import re

with open('site/guide-studio/lezione_04.md', 'r') as f:
    content = f.read()

# Revert previous incorrect changes to year if needed, actually it replaced 2025 with 2026 correctly but we need to run it clean. Let's start fresh just in case.
with open('site/guide-studio/lezione_04.md', 'r') as f:
    content = f.read()

replacements = {
    "### 🔹 I magneti permanenti": "### 🔹 I magneti permanenti\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-02.jpg\" alt=\"I magneti\" width=\"50%\"></div><br>",
    "### 🔹 Campo magnetico generato dalla corrente": "### 🔹 Campo magnetico generato dalla corrente\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-03.jpg\" alt=\"Esperimento Oersted\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-04.jpg\" alt=\"Campo radiale\" width=\"50%\"></div><br>",
    "### 🔹 Induzione elettromagnetica (Faraday, 1830)": "### 🔹 Induzione elettromagnetica (Faraday, 1830)\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-05.jpg\" alt=\"Induzione Faraday\" width=\"50%\"></div><br>",
    "### 🔹 Struttura e funzionamento": "### 🔹 Struttura e funzionamento\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-06.jpg\" alt=\"Simbolo induttore\" width=\"50%\"></div><br>",
    "### 🔹 L'induttanza e la sua unità di misura": "### 🔹 L'induttanza e la sua unità di misura\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-07.jpg\" alt=\"Induttanza\" width=\"50%\"></div><br>",
    "### 🔹 Fattori che influenzano l'induttanza": "### 🔹 Fattori che influenzano l'induttanza\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-08.jpg\" alt=\"Fattori induttanza\" width=\"50%\"></div><br>",
    "### 🔹 Permeabilità magnetica (µ)": "### 🔹 Permeabilità magnetica (µ)\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-09.jpg\" alt=\"Permeabilità magnetica\" width=\"50%\"></div><br>",
    "### 🔹 Tipologie di induttori": "### 🔹 Tipologie di induttori\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-10.jpg\" alt=\"Nucleo ferromagnetico\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-11.jpg\" alt=\"Induttore variabile\" width=\"50%\"></div><br>",
    "### 🔹 Collegamento in serie": "### 🔹 Collegamento in serie\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-12.jpg\" alt=\"Serie e Parallelo\" width=\"50%\"></div><br>",
    "### 🔹 Collegamento in parallelo": "### 🔹 Collegamento in parallelo\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-13.jpg\" alt=\"Domande serie parallelo\" width=\"50%\"></div><br>",
    "### 🔹 Comportamento transitorio": "### 🔹 Comportamento transitorio\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-14.jpg\" alt=\"Transitorio CC\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-15.jpg\" alt=\"Costante di tempo\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-16.jpg\" alt=\"Grafico transitorio\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-17.jpg\" alt=\"Legge di Faraday-Lenz\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-18.jpg\" alt=\"Energia accumulata\" width=\"50%\"></div><br>",
    "### 🔹 La corrente è in ritardo di 90°": "### 🔹 La corrente è in ritardo di 90°\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-22.jpg\" alt=\"Sfasamento 90\" width=\"50%\"></div><br>",
    "### 🔹 Reattanza induttiva ($X_L$)": "### 🔹 Reattanza induttiva ($X_L$)\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-19.jpg\" alt=\"Reattanza Induttiva\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-20.jpg\" alt=\"Grafico Reattanza\" width=\"50%\"></div><br>",
    "### 🔹 Esercizio svolto: calcolo reattanza": "### 🔹 Esercizio svolto: calcolo reattanza\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-21.jpg\" alt=\"Esercizio XL\" width=\"50%\"></div><br>",
    "### 🔹 Distribuzione della corrente ad alta frequenza": "### 🔹 Distribuzione della corrente ad alta frequenza\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-23.jpg\" alt=\"Effetto Pelle\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-24.jpg\" alt=\"Immagine effetto pelle\" width=\"50%\"></div><br>",
    "## ⚡ 7. Il trasformatore (⏱ 96:51)": "## ⚡ 7. Il trasformatore (⏱ 96:51)\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-25.jpg\" alt=\"Trasformatore\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-26.jpg\" alt=\"Simbolo Trasformatore\" width=\"50%\"></div><br>",
    "### 🔹 Principio di funzionamento": "### 🔹 Principio di funzionamento\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-27.jpg\" alt=\"Mutua induzione\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-28.jpg\" alt=\"Primario e secondario\" width=\"50%\"></div><br>",
    "### 🔹 Rapporto di trasformazione": "### 🔹 Rapporto di trasformazione\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-29.jpg\" alt=\"Rapporto K\" width=\"50%\"></div><br>",
    "### 🔹 Esercizio svolto": "### 🔹 Esercizio svolto\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-30.jpg\" alt=\"Esercizio K\" width=\"50%\"></div><br>\n\n<div align=\"center\"><img src=\"../assets/images/lezioni/lezione_04/slide-31.jpg\" alt=\"Esercizio corrente\" width=\"50%\"></div><br>"
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open('site/guide-studio/lezione_04.md', 'w') as f:
    f.write(content)

