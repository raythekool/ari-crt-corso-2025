---
layout: default
title: "10 - I Diodi e gli Alimentatori"
permalink: /guide-studio/lezione_10.html
---

# 📘 Lezione 10 - I Diodi e gli Alimentatori

> 🎓 **Esame ridotto: lezione non necessaria.** Questa lezione riguarda la Parte A (questioni di natura tecnica, A.2 Componenti) del programma d'esame, da cui è esonerato chi ha un titolo previsto dall'art. 5 dell'Allegato 26. Serve per l'esame completo.

## 📌 Panoramica

- **Materia**: Elettronica — Diodi, alimentatori lineari, alimentatori switching
- **Tempo di studio stimato**: 2 ore
- **Prerequisiti**: Nozioni base di corrente, tensione, componenti passivi (resistori, condensatori)
- **Obiettivi di apprendimento**:
  - Comprendere il funzionamento e la struttura dei diodi
  - Conoscere i vari tipi di diodi (raddrizzatore, LED, Zener, Varicap, Schottky)
  - Capire il funzionamento degli alimentatori lineari e le loro sezioni
  - Comprendere i principi degli alimentatori switching, i loro pregi e difetti

---

## 📖 Contenuti Teorici

### 1. 🔀 I Diodi

Il **diodo** è un dispositivo a semiconduttore che consente il passaggio di corrente in un solo senso.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-02.jpg" alt="Diodo" style="width: 75%;"></div><br>

#### 🔹 Materiali Semiconduttori e Drogaggio
È composto da due parti di semiconduttore (tipicamente **silicio** che ha 4 elettroni di valenza), che vengono "drogati" per modificarne le proprietà elettriche:
- **Drogaggio P** (es. Indio, 3 elettroni di valenza): Si formano "lacune" positive.
- **Drogaggio N** (es. Arsenico, 5 elettroni di valenza): Si formano elettroni liberi.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-03.jpg" alt="Struttura diodo" style="width: 75%;"></div><br>

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-04.jpg" alt="Drogaggio" style="width: 75%;"></div><br>
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-06.jpg" alt="Giunzione PN" style="width: 75%;"></div><br>

Quando polarizzato direttamente, la soglia di conduzione dei diodi al silicio è di **0,7 V**. Questo significa che quando è attraversato da corrente (polarizzazione diretta), ai suoi capi cadono 0,7 V.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-07.jpg" alt="Soglia 0,7V" style="width: 75%;"></div><br>
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-11.jpg" alt="Caduta di tensione" style="width: 75%;"></div><br>

#### 🔹 Funzioni Principali
- **Raddrizzamento**: Serve a rendere *pulsante* una corrente alternata (cioè a trasformare CA in CC).
- **Rivelazione (Demodulazione)**: Serve a *estrarre* un segnale a frequenza audio (BF) da un segnale a radiofrequenza (RF) modulato.

#### 🔹 Parametri Limite
Un diodo ha dei limiti fisici che non possono essere superati senza danneggiarlo:
- **Massima tensione inversa**: massimo valore di tensione applicabile in senso inverso.
- **Massima corrente**: massimo valore di corrente applicabile in polarizzazione diretta.
- **Massima potenza**: massimo prodotto tra corrente e caduta di tensione (0,7V) in polarizzazione diretta.

#### 🔹 Tipi di Diodi
- **Diodo raddrizzatore**: trasforma CA in CC.
- **Diodo LED**: in grado di emettere luce. Lavora in polarizzazione diretta.
  <div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-12.jpg" alt="Diodo LED" style="width: 75%;"></div><br>
- **Diodo Zener**: in grado di stabilizzare la tensione ai suoi capi. Lavora in polarizzazione *inversa*.
  <div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-13.jpg" alt="Diodo Zener" style="width: 75%;"></div><br>
- **Diodo Varicap**: cambia la capacità al variare della tensione applicata (funziona come un condensatore variabile). Lavora in polarizzazione *inversa*.
- **Diodo Hot-Carrier (Schottky)**: ha una giunzione metallo-semiconduttore. È un diodo molto veloce, impiegato in UHF e SHF.

---

### 2. 🔌 Gli Alimentatori Lineari

Un alimentatore lineare trasforma la tensione di rete (220 V CA) in una tensione continua stabile necessaria per i dispositivi elettronici (es. 13,8 V CC per le radio). 

#### 🔹 Il Trasformatore
Serve per due scopi principali:
1. **Trasformazione**: abbassa la tensione di rete (220 V) a una tensione vicina a quella di uscita desiderata.
2. **Isolamento galvanico**: garantisce la separazione elettrica tra la rete e il circuito, impedendo il passaggio di corrente diretta per sicurezza.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-18.jpg" alt="Trasformatore" style="width: 75%;"></div><br>
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-20.jpg" alt="Alimentatore lineare" style="width: 75%;"></div><br>

#### 🔹 Raddrizzamento
- **Raddrizzatore a singola semionda**: usa 1 diodo. Fornisce una tensione pulsante alla stessa frequenza della rete (50 Hz).
  <div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-21.jpg" alt="Raddrizzatore singola semionda" style="width: 75%;"></div><br>
- **Raddrizzatore a doppia semionda (2 diodi + trasformatore con presa centrale)**: fornisce una tensione pulsante a frequenza doppia (100 Hz).
  <div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-22.jpg" alt="Doppia semionda 2 diodi" style="width: 75%;"></div><br>
- **Ponte di Graetz (4 diodi)**: fornisce tensione pulsante a frequenza doppia senza necessitare del secondario doppio sul trasformatore.
  <div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-23.jpg" alt="Ponte a 4 diodi" style="width: 75%;"></div><br>

#### 🔹 Spianamento (Condensatore di Filtro)
Si usano condensatori di alta capacità (elettrolitici) per "spianare" l'andamento pulsante e fornire una tensione continua (seppur con un leggero ripple).
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-24.jpg" alt="Filtro" style="width: 75%;"></div><br>

#### 🔹 Stabilizzazione
I circuiti stabilizzatori rendono costante la tensione di uscita indipendentemente dal carico. Utilizzano un transistor di regolazione, pilotato in base alla "tensione di errore" (la differenza tra l'uscita e una tensione di riferimento nota).
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-25.jpg" alt="Stabilizzazione" style="width: 75%;"></div><br>
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-26.jpg" alt="Transistor di regolazione" style="width: 75%;"></div><br>

---

### 3. ⚡ Gli Alimentatori a Commutazione (Switching)

Negli alimentatori switching, la tensione di rete viene prima raddrizzata (diventando circa 310 V CC) e poi un oscillatore la trasforma in una tensione alternata ad altissima frequenza (es. 30-60 kHz). Questo permette di usare trasformatori piccolissimi per abbassare la tensione, che viene poi nuovamente raddrizzata e livellata.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-28.jpg" alt="Schema Switching" style="width: 75%;"></div><br>

#### 🔹 Isolamento con Optoisolatore
L'isolamento galvanico della retroazione (feedback) è affidato a un **optoisolatore**: un componente formato da un LED e un fototransistor nello stesso contenitore. Questo garantisce la sicurezza elettrica separando la parte ad alta tensione da quella in uscita.
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_10/slide-29.jpg" alt="Optoisolatore" style="width: 75%;"></div><br>

#### 🔹 Pro e Contro
**Pregi:**
- Più piccoli e leggeri (trasformatore minuscolo e meno dissipatori necessari).
- Rendimento molto elevato (70-90%).
- Costo più basso.

**Difetti:**
- Generano interferenze a Radiofrequenza (RF).
- Tempi di risposta al transitorio più lenti.
- Segnale di uscita non perfettamente livellato.

---

## 🔗 Mappa Concettuale

- Drogaggio P e N → formano → giunzione del diodo.
- Polarizzazione diretta → permette → conduzione del diodo al silicio oltre la soglia.
- Diodi raddrizzatori → trasformano → tensione alternata in tensione pulsante.
- Condensatore di filtro → spiana → tensione pulsante; stabilizzatore → mantiene → tensione di uscita costante.
- Alimentatore lineare → usa → trasformatore di rete e raddrizzatore.
- Alimentatore switching → usa → commutazione ad alta frequenza e un trasformatore più piccolo.
- Optoisolatore → separa elettricamente → retroazione e sezione ad alta tensione.

## 📝 Punti Chiave

1. Il diodo al silicio conduce prevalentemente in un verso; in polarizzazione diretta presenta una caduta di tensione di circa 0,7 V.
2. Le specifiche di massima tensione inversa, corrente diretta e potenza non devono essere superate.
3. Il raddrizzamento a doppia semionda produce una tensione pulsante a 100 Hz con una rete a 50 Hz, mentre quello a singola semionda conserva la frequenza di 50 Hz.
4. Nell'alimentatore lineare il trasformatore abbassa la tensione e isola dalla rete; il condensatore filtra e lo stabilizzatore regola l'uscita.
5. L'alimentatore switching usa una frequenza di commutazione elevata per ridurre le dimensioni del trasformatore, ma può generare interferenze radio.

## ❓ Domande di Comprensione

1. Perché il drogaggio di tipo P e quello di tipo N permettono a una giunzione di comportarsi da diodo?
2. In che modo la soglia di conduzione del silicio influisce sulla tensione disponibile a valle di un diodo polarizzato direttamente?
3. Perché un ponte di Graetz fornisce impulsi a frequenza doppia rispetto alla rete senza richiedere un trasformatore con presa centrale?
4. Quali funzioni diverse svolgono il condensatore di filtro e lo stabilizzatore in un alimentatore lineare?
5. Perché la frequenza di commutazione elevata consente di ridurre il trasformatore, ma può creare problemi a un ricevitore radio?
6. Quale ruolo svolge l'optoisolatore nella retroazione di un alimentatore switching e perché è importante l'isolamento galvanico?

## 📚 Glossario

- **Alimentatore lineare** — circuito che abbassa, raddrizza, filtra e stabilizza la tensione di rete.
- **Alimentatore switching** — alimentatore che converte la tensione tramite commutazione ad alta frequenza prima del raddrizzamento finale.
- **Diodo** — componente a semiconduttore che conduce prevalentemente in un solo verso.
- **Drogaggio N** — aggiunta di impurità che forniscono elettroni liberi a un semiconduttore.
- **Drogaggio P** — aggiunta di impurità che creano lacune in un semiconduttore.
- **Isolamento galvanico** — separazione elettrica tra due circuiti senza passaggio diretto di corrente.
- **Optoisolatore** — componente che trasferisce un segnale tramite luce mantenendo separate elettricamente le due sezioni.
- **Ponte di Graetz** — raddrizzatore a quattro diodi che sfrutta entrambe le semionde.
- **Raddrizzamento** — conversione della tensione alternata in tensione pulsante unidirezionale.
- **Ripple** — variazione residua della tensione continua dopo il filtraggio.
- **Stabilizzazione** — regolazione che mantiene costante la tensione d'uscita al variare del carico.

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: non indicato nella fonte.

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                   |
| -------------------- | ---------------------------------------------------------------------------------------- |
| **Lezione**          | 10                                                                                       |
| **Data**             | 20 maggio 2026                                                                           |
| **Durata**           | ~2 ore                                                                                   |
| **Numero argomenti** | 3 (Diodi, Alimentatori Lineari, Alimentatori Switching)                                  |
| **Parole chiave**    | Diodo, Silicio, LED, Zener, Trasformatore, Raddrizzatore, Switching, Optoisolatore       |
