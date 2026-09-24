import os

content = r"""---
layout: default
title: "La Propagazione delle Onde Radio"
permalink: /guide-studio/lezione_17.html
---

# 📘 Lezione 17 - La Propagazione delle Onde Radio

<div align="center"><img src="../assets/images/lezioni/lezione_17/slide-01.jpg" alt="Copertina" width="50%"></div><br>

## 📌 Panoramica

- **Materia**: Radiotecnica e Propagazione
- **Tempo di studio stimato**: 60–75 minuti
- **Prerequisiti**: Fondamenti sulle onde elettromagnetiche, frequenza e lunghezza d'onda
- **Obiettivi di apprendimento**:
  - Comprendere i campi elettromagnetici e le loro proprietà.
  - Conoscere lo spettro elettromagnetico e le onde radio.
  - Comprendere i meccanismi di propagazione delle onde radio.
  - Comprendere la propagazione ionosferica e i vari strati (D, E, F1, F2).
  - Conoscere il ruolo del ciclo solare, MUF, LUF e FOT.

---

## 📖 Appunti della Lezione

### 1. I Campi Elettromagnetici - Un po' di storia

I primi studi sull'elettromagnetismo risalgono all'Ottocento, con figure illustri come:
- **Michael Faraday** (Induzione elettromagnetica)
- **André-Marie Ampère** (Relazione tra corrente e campo magnetico)
- **Heinrich Lenz** e **Carl Friedrich Gauss** (Legge di Lenz e Teorema di Gauss)
- **Heinrich Rudolf Hertz** (Esistenza delle onde elettromagnetiche)

<div align="center"><img src="../assets/images/lezioni/lezione_17/slide-03.jpg" alt="Storia dei campi elettromagnetici" width="50%"></div><br>

La svolta epocale avvenne con **James Clerk Maxwell**, che elaborò le famose *Equazioni di Maxwell*, dimostrando che i campi elettrici e magnetici in variazione si sostengono a vicenda e si propagano nello spazio sotto forma di onde alla velocità della luce.
**Guglielmo Marconi**, nel 1901, dimostrò la possibilità di usare queste onde per comunicazioni a lunga distanza.
Successivamente, nel 1923, i radioamatori **Fred Schnell** e **Léon Deloy** dimostrarono la superiorità delle "onde corte" (HF) per i collegamenti transoceanici con debole potenza.

### 2. I Fondamentali del Campo Elettromagnetico

Il campo elettromagnetico è costituito da un campo elettrico (E) e un campo magnetico (H) concatenati.
- Nello spazio libero, il rapporto tra le loro intensità è costante: $E/H = 377 \Omega$ (impedenza dello spazio libero).
- I due campi sono sempre perpendicolari tra loro.
- La **polarizzazione** dell'onda è definita dal piano su cui giace il campo elettrico E rispetto a terra.

<div align="center"><img src="../assets/images/lezioni/lezione_17/slide-06.jpg" alt="Campi Elettrico e Magnetico" width="50%"></div><br>

La velocità di propagazione nel vuoto è pari a quella della luce ($V \approx 3 \cdot 10^5$ km/s).
La **lunghezza d'onda** ($\lambda$) e la frequenza ($f$) sono inversamente proporzionali: $\lambda(m) = 300 / f(MHz)$.

### 3. Lo Spettro Elettromagnetico e le Onde Radio

Lo spettro elettromagnetico include onde radio, radiazione termica, luce visibile, raggi X e gamma. Le **Onde Radio** occupano la porzione di spettro con frequenza compresa tra $3$ kHz e $300$ GHz.

<div align="center"><img src="../assets/images/lezioni/lezione_17/slide-09.jpg" alt="Spettro Elettromagnetico" width="50%"></div><br>

La propagazione nello spazio libero avviene in linea retta in modo sferico, con l'intensità del segnale che si riduce proporzionalmente al quadrato della distanza.

### 4. Propagazione Ionosferica e Ciclo Solare

La ionosfera è la parte alta dell'atmosfera terrestre, ionizzata dalle radiazioni solari (raggi UV e X). I principali strati riflettenti sono:
- **Strato D**: attivo di giorno, attenua le frequenze basse. Scompare di notte.
- **Strato E**: attivo di giorno, attenua ma riflette in determinate condizioni.
- **Strato F**: principale responsabile delle riflessioni a lunga distanza. Di giorno si divide in F1 e F2, di notte si ricompone.

**MUF, LUF e FOT**
- **MUF (Maximum Usable Frequency)**: la massima frequenza utilizzabile per la riflessione (circa 3 volte la frequenza critica $f_0$).
- **LUF (Lower Usable Frequency)**: la minima frequenza utilizzabile (sotto di essa l'attenuazione è eccessiva).
- **FOT (Frequency of Optimum Traffic)**: frequenza ottimale, circa l'80-90% della MUF.

<div align="center"><img src="../assets/images/lezioni/lezione_17/slide-30.jpg" alt="MUF LUF FOT" width="50%"></div><br>

**Riflessioni Multiple (Multihop)**
I segnali possono subire riflessioni multiple tra la ionosfera e il suolo, o modalità come il *Duct Mode* e *Chordal Mode* che riducono l'attenuazione (particolarmente alle latitudini equatoriali o lungo la *gray line*).

<div align="center"><img src="../assets/images/lezioni/lezione_17/slide-33.jpg" alt="Multihop path" width="50%"></div><br>

### 5. Il Ciclo Solare

L'attività della ionosfera dipende direttamente dall'attività solare, influenzata da:
- **Ciclo undecennale (Sunspot cycle)**: la quantità di macchie solari varia ciclicamente in periodi di circa 11 anni, influenzando notevolmente le condizioni di propagazione sulle onde corte.
- **Ciclo di rotazione solare (27 giorni)**: il numero di macchie esposte verso la Terra varia durante la rotazione del Sole.
- **Ciclo orbitale (Stagioni)**: cambia l'inclinazione dei raggi solari e quindi l'intensità della ionizzazione.
- **Ciclo giornaliero**: l'alternanza giorno/notte causa l'apparizione e scomparsa degli strati inferiori e la variazione della MUF.

<div align="center"><img src="../assets/images/lezioni/lezione_17/slide-36.jpg" alt="Ciclo undecennale" width="50%"></div><br>

---

## 📚 Glossario

- **Campo elettromagnetico** — combinazione di un campo elettrico e un campo magnetico variabili, che si propagano nello spazio.
- **FOT (Frequency of Optimum Traffic)** — frequenza ottimale per stabilire un collegamento, solitamente l'80-90% della MUF.
- **Ionosfera** — strato superiore dell'atmosfera terrestre contenente plasma (gas ionizzato).
- **LUF (Lower Usable Frequency)** — frequenza minima utilizzabile per un dato collegamento ionosferico.
- **Macchie solari** — regioni della fotosfera solare con intensa attività magnetica, collegate all'emissione di radiazioni ionizzanti.
- **MUF (Maximum Usable Frequency)** — frequenza massima che può essere riflessa dalla ionosfera tra due punti dati.
- **Onde corte (HF)** — frequenze comprese tra 3 e 30 MHz.
- **Polarizzazione** — orientamento del campo elettrico dell'onda elettromagnetica rispetto al terreno.

---

## 👥 Partecipanti

- 👨‍🏫 **Moderatore**: Paolo
- 👨‍🏫 **Relatore**: i5WHC

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione numero**   | 17                                                                                                                                                                                                                                                                                                            |
| **Data**             | 09/09/2026                                                                                                                                                                                                                                                                                                    |
| **Durata stimata**   | ~2 ore                                                                                                                                                                                                                                                                                                        |
| **Numero argomenti** | 3                                                                                                                                                                                                                                                                                                             |
| **Parole chiave**    | radiotecnica, campi elettromagnetici, onde radio, propagazione, ionosfera, MUF, LUF, FOT, ciclo solare, macchie solari, strati ionosferici                                                                                                                                                                    |
"""

with open('/data/repos/ari-crt-corso-2025/site/guide-studio/lezione_17.md', 'w') as f:
    f.write(content)
