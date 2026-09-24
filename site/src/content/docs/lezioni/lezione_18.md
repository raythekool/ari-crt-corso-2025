---
layout: default
title: "Antenne - Parte prima"
permalink: /guide-studio/lezione_18.html
---

# 📘 Lezione 18 - Antenne - Parte prima

## 📌 Panoramica

- **Materia**: Antenne e Linee di Trasmissione
- **Tempo di studio stimato**: 2 ore e 30 minuti
- **Prerequisiti**: Corrente alternata, circuiti risonanti, onde elettromagnetiche.
- **Obiettivi di apprendimento**:
  - Comprendere cos'è un'antenna e il suo principio di funzionamento.
  - Conoscere le aree di propagazione del campo elettromagnetico.
  - Comprendere la resistenza di radiazione.
  - Capire il funzionamento delle antenne caricate e multibanda.
  - Analizzare il lobo di radiazione in spazio libero e con effetto del terreno.

---

## 📖 Contenuti Teorici

### 1. 🔍 Elementi fondamentali dell'antenna

L'antenna è un "trasduttore", ovvero un dispositivo che ha la funzione di trasferire l'energia elettrica ad alta frequenza (generata dal TX e che percorre la linea di trasmissione) in un campo elettromagnetico che si propaga nello spazio circostante, e viceversa in ricezione.

Un conduttore percorso da una corrente variabile genera nel suo intorno un campo elettromagnetico. Analogamente, un conduttore immerso in un campo elettromagnetico variabile è sede di una corrente indotta proporzionale all'intensità del campo.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-03.jpg" alt="Elementi fondamentali dell'antenna" style="width: 75%;"></div><br>

Esistono 3 diverse aree in funzione della distanza dall'antenna:
1. **Campo Vicino Reattivo (Reactive Near Field)**: Fino a 0,1 λ - 0,4 λ. I campi E e H non sono correlati e il comportamento è reattivo.
> ⚠️ **In Pratica:** È fondamentale non avere ostacoli metallici (ringhiere, cavi, esseri umani) in questa zona, perché interagiscono con l'antenna comportandosi come elementi reattivi che ne cambiano la sintonizzazione, ed espongono a forti campi magnetici!

2. **Campo Vicino Radiativo (Fresnel Region)**: Fino a 0,5 λ - 1,5 λ. I campi E e H iniziano a correlarsi, ci sono fluttuazioni di fase.
3. **Campo Lontano Radiativo (Fraunhofer Region)**: Oltre la regione di Fresnel fino all'infinito. I campi sono totalmente correlati e formano un'onda sferica.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-05.jpg" alt="Aree di campo dell'antenna" style="width: 75%;"></div><br>

Un'antenna è assimilabile ad un **circuito risonante serie** dove L e C dipendono dalle dimensioni fisiche e determinano la frequenza di risonanza. R, in assenza di perdite, coincide con la resistenza di radiazione.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-06.jpg" alt="Antenna come circuito risonante" style="width: 75%;"></div><br>

### 2. ⚡ Resistenza di radiazione e Risonanza

La teoria definisce "Resistenza di Radiazione" ($R_{rad}$) di un'antenna il rapporto tra la potenza totale irradiata e il quadrato della corrente.
$$ P_{ir} = R_{rad} \cdot I^2 $$
> 💡 **Nota Concettuale:** Questa **non** è una vera resistenza fisica che scalda dissipando energia in calore! È un parametro fittizio matematico che usiamo per quantificare l'energia "utile" che si sgancia dall'antenna diventando un'onda radio. Un'antenna efficiente deve avere una $R_{rad}$ alta rispetto alla vera resistenza ohmica dei materiali.

A parità di potenza irradiata, un'antenna di dimensioni minori avrà una $R_{rad}$ minore e necessiterà di una corrente maggiore. Antenne più corte di $1/10 \lambda$ hanno una resistenza di radiazione così bassa da avere un'efficienza bassissima.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-08.jpg" alt="Resistenza di radiazione" style="width: 75%;"></div><br>

La dimensione dell'elemento radiante è legata alla frequenza di risonanza: aumentando la lunghezza, la frequenza diminuisce; accorciandolo, la frequenza aumenta.
A causa del **fattore di velocità (Fv)** del materiale, le lunghezze reali dell'antenna sono sempre leggermente inferiori (circa 0,95 - 0,98) rispetto a quelle teoriche.

Se l'antenna non lavora alla frequenza di risonanza $f_0$, presenterà un'impedenza complessa $Z_0 = R \pm jX$:
- Capacitiva ($-jX$) per $f < f_0$
- Induttiva ($+jX$) per $f > f_0$

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-13.jpg" alt="Impedenza e Carta di Smith" style="width: 75%;"></div><br>

### 3. 🛠️ Antenne caricate e multibanda

Per annullare la reattanza di un'antenna fuori risonanza si utilizzano "carichi", come una **bobina di carico** o un **cappello capacitivo**. 
L'adattamento di impedenza può avvenire anche con uno **Stub** o **Hairpin** (forcella), ponendo in parallelo al punto di alimentazione una reattanza induttiva di opportuno valore.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-14.jpg" alt="Antenne caricate" style="width: 75%;"></div><br>

Le **antenne multibanda** utilizzano delle **trappole** (circuiti risonanti LC in parallelo) per interrompere elettricamente l'antenna a determinate frequenze.
In alternativa si sfrutta la risonanza in armonica: le stesse antenne risuonano non solo alla fondamentale $F_0$, ma anche alle sue armoniche dispari ($3F_0, 5F_0...$).
Un esempio è il dipolo OCF (Off-Center Fed), che alimenta l'antenna in un punto decentrato per avere un'impedenza adatta su più bande.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-16.jpg" alt="Antenne con trappole" style="width: 75%;"></div><br>

### 4. 🌐 Il Lobo di Radiazione

Il comportamento teorico di un'antenna si riferisce al **radiatore isotropico** (sorgente puntiforme che irradia in tutte le direzioni in modo uniforme) nello spazio libero.
> 💡 **Attenzione:** Il radiatore isotropico non esiste in natura! È una finzione matematica usata come "metro di misura" base per confrontare il guadagno delle antenne reali.

Nella realtà, l'intensità del campo varia con la direzione. Il grafico tridimensionale è detto **lobo di radiazione**, spesso diviso in:
- **Azimuth Plot** (lobo orizzontale)
- **Elevation Plot** (lobo verticale)

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-20.jpg" alt="Lobo di radiazione" style="width: 75%;"></div><br>

Il campo emesso presenta una polarizzazione legata all'orientamento dell'elemento radiante:
- **Orizzontale**: il campo elettrico E è parallelo al terreno.
- **Verticale**: il campo elettrico E è perpendicolare al terreno.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-21.jpg" alt="Polarizzazione dell'antenna" style="width: 75%;"></div><br>

Un dipolo nello spazio libero ha un guadagno di **2,1 dBi** rispetto all'isotropico.
Nella pratica, il segnale al ricevitore è la somma di un fascio diretto e un fascio riflesso dal terreno. La differenza di fase tra i due (dovuta alla differenza di percorso dipendente dall'altezza $h$ e dall'angolo di take-off) può generare un "Ground Gain" fino a +6 dB, o un'attenuazione profonda (fino a -20 dB).

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-23.jpg" alt="Riflessione dal terreno e fascio diretto" style="width: 75%;"></div><br>

Per antenne a **polarizzazione orizzontale**, si ha inversione di fase nella riflessione a terra, per cui le componenti si sommano quando la differenza di percorso è $\lambda/2$. Il lobo dipende fortemente dall'altezza da terra.
> 📏 **Regola pratica (Rule of Thumb):** Per avere un buon angolo di take-off basso (utile per i collegamenti a lunga distanza / DX), un'antenna orizzontale andrebbe montata ad almeno $\lambda/2$ di altezza dal suolo!

Per antenne a **polarizzazione verticale**, non c'è inversione di fase; l'angolo di radiazione è basso anche quando poste vicino al terreno, ma sono molto influenzate dalle caratteristiche dielettriche di questo (perdite).

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_18/slide-26.jpg" alt="Lobo antenna verticale" style="width: 75%;"></div><br>

---

## 🔗 Mappa Concettuale

- **Antenna** → Trasduttore RF ↔ Campo EM
- **Campi attorno all'antenna** → Reattivo, Fresnel, Fraunhofer (Lontano)
- **Resistenza di Radiazione ($R_{rad}$)** → Diminuisce con antenne più corte
- **Fattore di velocità** → Lunghezza reale < Lunghezza teorica
- **Antenne fuori risonanza** → Reattive (Capacitive per f < f0, Induttive per f > f0)
- **Antenne Caricate** → Uso di bobine / cappelli capacitivi
- **Antenne Multibanda** → Uso di trappole / Armoniche dispari
- **Lobo di radiazione** → Rappresentazione del campo irradiato (Azimuth e Elevation)
- **Ground Gain** → Somma di onda diretta e riflessa dal suolo (fino a +6dB)
- **Polarizzazione** → Verticale (senza inversione di fase al suolo) / Orizzontale (con inversione di fase)

---

## 📝 Punti Chiave

1. L'antenna converte energia elettrica RF in campi EM irradiati e viceversa.
2. Si assimila a un circuito risonante serie. La Resistenza di Radiazione $R_{rad}$ lega potenza e corrente.
3. Un'antenna corta rispetto a $\lambda$ ha $R_{rad}$ più bassa, richiedendo correnti maggiori per pari potenza.
4. L'impedenza fuori risonanza include reattanza. Per le antenne si usano sistemi di carico (bobine) o adattamento (stub).
5. Antenne multibanda si ottengono con circuiti trappola o sfruttando risonanze su armoniche dispari.
6. Il lobo di radiazione descrive la direttività rispetto all'ipotetica antenna isotropica.
7. L'altezza da terra modifica enormemente il lobo (Elevation) di un'antenna orizzontale per l'inversione di fase dell'onda riflessa.
8. Un'antenna verticale irradia ad angoli bassi ed è soggetta a perdite del suolo se vicina ad esso.

---

## 📝 Quiz e Domande di Comprensione

<details>
<summary><b>1. Qual è la funzione principale di un'antenna?</b></summary>
Fungere da trasduttore per trasferire energia elettrica a radiofrequenza in un campo elettromagnetico irradiato nello spazio (in trasmissione) e viceversa (in ricezione).
</details>

<details>
<summary><b>2. Se un'antenna viene accorciata molto rispetto alla sua dimensione di risonanza naturale, cosa succede alla sua resistenza di radiazione?</b></summary>
La sua resistenza di radiazione diminuisce drasticamente. Di conseguenza l'efficienza scende, poiché una porzione maggiore della potenza viene dissipata in calore dalle resistenze ohmiche (perdite) invece di essere irradiata.
</details>

<details>
<summary><b>3. Qual è lo scopo primario di una "trappola" (circuito LC) in un'antenna?</b></summary>
Interrompere elettricamente l'elemento radiante a determinate frequenze per permettere all'antenna di risuonare (funzionare in modo ottimale) su più bande diverse.
</details>

<details>
<summary><b>4. Perché per i collegamenti a lunga distanza (DX) è desiderabile un lobo di radiazione con un "angolo di take-off" basso?</b></summary>
Perché un'onda emessa quasi parallelamente al terreno andrà a colpire la ionosfera molto più lontano rispetto a un'onda sparata verso l'alto, coprendo distanze maggiori con ogni "salto" (hop) riflessivo.
</details>

---

## 📚 Glossario

- **Antenna Isotropica** — Antenna teorica puntiforme che irradia uniformemente in tutte le direzioni.
- **Cappello Capacitivo** — Struttura posta all'estremità dell'antenna per compensare reattanze.
- **Fattore di Velocità ($F_v$)** — Coefficiente che indica quanto la lunghezza d'onda in un conduttore è minore rispetto allo spazio libero.
- **Fraunhofer Region (Campo Lontano)** — Zona a distanza sufficiente in cui i campi E e H diventano onde sferiche perfettamente in fase.
- **Ground Gain** — Incremento del segnale (fino a 6dB) dovuto all'interferenza costruttiva tra onda diretta e riflessa dal suolo.
- **Resistenza di Radiazione** — Parametro fittizio che rappresenta la potenza irradiata in rapporto alla corrente che fluisce.
- **Trappola** — Circuito LC risonante inserito nell'elemento radiante per interromperlo a precise frequenze, per antenne multibanda.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo (i5WHC)
- 🎓 **Coordinatore**: Fabrizio (coordina la sessione, gestisce le domande)

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                                                                                                  |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Numero lezione**   | 18                                                                                                                                                                                                                                                                                                                      |
| **Data**             | 16/09/2026 (mercoledì)                                                                                                                                                                                                                                                                                                  |
| **Durata**           | ~2 ore e 30 minuti                                                                                                                                                                                                                                                                                                      |
| **Parole chiave**    | antenne, trasduttore, campo elettromagnetico, reattivo, radiativo, resistenza di radiazione, risonanza, antenne caricate, multibanda, lobo di radiazione, ground gain, spazio libero, polarizzazione |
