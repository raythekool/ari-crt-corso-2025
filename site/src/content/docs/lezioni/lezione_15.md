---
layout: default
title: "15 - Strumenti di Misura"
permalink: /guide-studio/lezione_15.html
---

# 📘 Lezione 15 - Strumenti di Misura

## 📌 Panoramica

- **Materia**: Strumentazione e Misure Elettriche/Radio
- **Argomento principale**: Principi e utilizzo degli strumenti di misura: galvanometro, amperometro, voltmetro, ohmmetro, multimetro, wattmetro, rosmetro, frequenzimetro, grid-dip meter, oscilloscopio, analizzatore di spettro
- **Tempo di studio stimato**: 2 ore
- **Prerequisiti**: Legge di Ohm e potenza elettrica (Lezioni iniziali), circuiti risonanti LC (Lezione 06)
- **Obiettivi di apprendimento**:
  - Conoscere il principio di funzionamento del galvanometro a bobina mobile
  - Saper calcolare la resistenza di shunt per amperometri e la resistenza addizionale per voltmetri
  - Comprendere come si inseriscono gli strumenti in un circuito
  - Distinguere tra strumenti nel dominio del tempo e della frequenza
  - Conoscere il funzionamento di wattmetri, rosmetri e frequenzimetri

---

## 📖 Contenuti Teorici

### 1. 🧭 Galvanometro a Bobina Mobile

Lo strumento di misura analogico fondamentale è il **galvanometro a bobina mobile**.
È dotato di una bobina mobile inserita dentro un magnete e collegata meccanicamente all'ago indicatore. La misura viene effettuata dall'interazione del campo magnetico fisso con il campo magnetico generato dalla bobina attraversata da corrente, che fa muovere lo strumento.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-02.jpg" alt="Galvanometro" style="width: 75%;"></div><br>

---

### 2. ⚡ Amperometro e Resistenza di Shunt

Un amperometro misura la corrente in un circuito e **deve essere inserito in serie**. 
Per aumentarne la portata (cioè la corrente massima misurabile), si inserisce una resistenza in **parallelo** allo strumento, detta **resistenza di shunt**.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-04.jpg" alt="Circuito Amperometro" style="width: 75%;"></div><br>

#### Calcolo della Resistenza di Shunt
La formula per calcolare la resistenza di shunt è:
**Rs = (r * i) / Is**

Dove:
- **Rs** = resistenza di shunt
- **Is** = corrente che deve scorrere nella resistenza di shunt
- **r** = resistenza interna dello strumento
- **i** = corrente di fondo scala dello strumento

*Esempio*: Un amperometro ha una portata di 1 A fondo scala e una resistenza interna di 1 ohm. Di quale valore deve essere la resistenza di shunt da porre in parallelo allo strumento per portarlo a 5 A fondo scala? 
(Risposta: scorrereanno 4 A nello shunt, quindi Rs = (1 * 1) / 4 = 0,25 ohm).

---

### 3. 🔋 Voltmetro e Resistenza Addizionale

Un voltmetro serve per misurare la tensione (differenza di potenziale) e **deve essere inserito in parallelo** al circuito. 
Costruttivamente, è un micro-amperometro in cui scorrono pochi µA, con all'interno una resistenza in serie di alto valore. Per aumentarne la portata, bisogna mettere **un'ulteriore resistenza in serie** di adeguato valore.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-06.jpg" alt="Voltmetro" style="width: 75%;"></div><br>
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-07.jpg" alt="Circuito Voltmetro" style="width: 75%;"></div><br>

#### Calcolo della Resistenza in Serie
La formula è:
**Rv = (V / i) - r**

Dove:
- **Rv** = resistenza da mettere in serie
- **V** = tensione di fondo scala desiderata
- **r** = resistenza interna dello strumento
- **i** = corrente di fondo scala dello strumento

---

### 4. 🔌 Inserzione degli Strumenti e Strumento Ideale

- **Misura della corrente**: lo strumento (amperometro) si posiziona in **serie** al circuito.
- **Misura della tensione**: lo strumento (voltmetro) si posiziona in **parallelo** al circuito.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-09.jpg" alt="Inserzione" style="width: 75%;"></div><br>

Uno strumento **ideale** non perturba il circuito su cui effettua la misura:
- **Amperometro ideale**: ha una resistenza interna *nulla* (0 Ω).
- **Voltmetro ideale**: ha una resistenza interna *infinita* (∞ Ω).

---

### 5. 💡 Voltmetro Elettronico

Un voltmetro elettronico è progettato per perturbare il meno possibile il circuito:
- Ha un'impedenza di ingresso altissima (maggiore di 10 MΩ), ottenuta mediante l'uso di FET e resistori di alto valore.
- Presenta spesso una configurazione "a ponte": il segnale in ingresso sbilancia il ponte e genera la lettura.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-11.jpg" alt="Voltmetro Elettronico" style="width: 75%;"></div><br>

---

### 6. 🧲 Ohmmetro e Multimetro

#### Ohmmetro
Una resistenza si misura collegandola a una batteria di tensione nota all'interno dello strumento, e misurando la corrente che la attraversa tramite la legge di Ohm (R = V / I).
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-12.jpg" alt="Ohmmetro" style="width: 75%;"></div><br>

#### Multimetro (Tester)
Consente misure di tensione, corrente e resistenza nello stesso dispositivo. 
*Attenzione*: un normale multimetro passivo a lancetta non è un voltmetro elettronico, quindi la sua resistenza interna potrebbe non essere abbastanza alta per alcune misurazioni delicate.
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-13.jpg" alt="Multimetro" style="width: 75%;"></div><br>

---

### 7. 📏 Wattmetro e Rosmetro

#### Wattmetro per radiofrequenza
Per misurare la potenza emessa da un trasmettitore:
- Si collega il TX a un **carico fittizio** (dummy load, tipicamente 50 Ω).
- Si misura la tensione sul carico.
- Si applica la legge di Joule: **P = V² / R**
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-14.jpg" alt="Wattmetro" style="width: 75%;"></div><br>

#### Rosmetro (Misuratore di Onde Stazionarie)
I rosmetri leggono il **ROS** (Rapporto di Onde Stazionarie) presente su una linea di trasmissione.
Sfruttano il fatto che lungo la linea disadattata esistono due componenti di corrente (onda diretta e onda riflessa) che viaggiano in direzioni opposte.
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-15.jpg" alt="Rosmetro" style="width: 75%;"></div><br>
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-16.jpg" alt="Rosmetro Interno" style="width: 75%;"></div><br>

---

### 8. ⏱️ Frequenzimetro e Grid-Dip Meter

#### Frequenzimetro
Conta quanti cicli (oscillazioni) fa il segnale in ingresso in un secondo (Hertz).
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-17.jpg" alt="Frequenzimetro" style="width: 75%;"></div><br>

#### Grid-Dip Meter
Misura la **frequenza di risonanza** di un circuito LC passivo (non alimentato).
- Contiene un oscillatore a radiofrequenza sintonizzabile.
- Se la frequenza dell'oscillatore e quella del circuito LC esterno in esame sono uguali, il circuito LC assorbe per induzione un po' di potenza.
- Lo strumento rileva questo assorbimento tramite un calo ("dip") della corrente di griglia (o base).
- Può funzionare anche come "ondametro" (rivelatore a diodo) se l'oscillatore interno viene spento.
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-18.jpg" alt="Grid-Dip Meter" style="width: 75%;"></div><br>

---

### 9. 📈 Oscilloscopio

Consente di visualizzare l'andamento nel tempo di un segnale. 
Lavora nel **dominio del tempo**:
- Sull'asse X (orizzontale) è riportato il **tempo**.
- Sull'asse Y (verticale) è riportata l'**ampiezza** del segnale (di solito in Volt).
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-19.jpg" alt="Oscilloscopio" style="width: 75%;"></div><br>
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-21.jpg" alt="Traccia Oscilloscopio" style="width: 75%;"></div><br>

---

### 10. 📻 Analizzatore di Spettro

Consente di visualizzare le frequenze che compongono un segnale.
Mostra una curva che rappresenta la composizione dello **spettro di frequenza**.
Lavora nel **dominio della frequenza**:
- Sull'asse X (orizzontale) è riportata la **frequenza**.
- Sull'asse Y (verticale) è riportata la **potenza** del segnale (di solito in dBm o dB).

Dal punto di vista funzionale, è costituito dall'abbinamento di un **ricevitore a scansione** e un display (oscilloscopio).
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_15/slide-23.jpg" alt="Analizzatore di Spettro" style="width: 75%;"></div><br>

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione**          | 15                                                                                                                                                                                                                                                                                                                            |
| **Data**             | 24 giugno 2026                                                                                                                                                                                                                                                                                                                |
| **Durata**           | ~2 ore                                                                                                                                                                                                                                                                                                                        |
| **Numero argomenti** | 10                                                                                                                                                                                                                                                                                                                            |
| **Parole chiave**    | Strumenti di misura, galvanometro, amperometro, voltmetro, shunt, wattmetro, rosmetro, frequenzimetro, grid-dip meter, oscilloscopio, analizzatore di spettro, dominio del tempo, dominio della frequenza |
