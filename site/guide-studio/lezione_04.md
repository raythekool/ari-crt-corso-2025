---
layout: default
permalink: /guide-studio/lezione_04.html
---

# 📘 Lezione 04 - Corrente Alternata

## 📌 Overview

- **Materia e argomento**: Elettrotecnica — induttori, reattanza induttiva e trasformatori. Vengono introdotti il campo magnetico, l'induzione elettromagnetica, l'induttore come componente, la reattanza induttiva e il trasformatore.
- **Tempo di studio stimato**: 90–120 minuti
- **Prerequisiti**: Conoscenza della corrente alternata (sinusoide, valore efficace, periodo, frequenza), legge di Ohm, resistenze in serie e parallelo (Lezioni 01–03).
- **Obiettivi di apprendimento**:
  - Comprendere il campo magnetico generato da un conduttore percorso da corrente
  - Conoscere il principio dell'induzione elettromagnetica (Faraday/Ørsted)
  - Definire l'induttanza e la sua unità di misura (Henry) con i sottomultipli
  - Calcolare induttori in serie e in parallelo
  - Comprendere lo sfasamento di 90° tra tensione e corrente in un induttore
  - Calcolare la reattanza induttiva con la formula $X_L = 2\pi f L$
  - Comprendere il funzionamento del trasformatore e il rapporto di trasformazione

---

## 📖 Core Content

## 🧲 1. Magneti e campo magnetico (⏱ 21:18)

### 🔹 I magneti permanenti

I **magneti** sono elementi presenti in natura che sviluppano un **campo magnetico** nel loro intorno. Le calamite (magneti permanenti) presentano sempre due poli: un **polo nord** e un **polo sud**. Il magnete permanente più grande e conosciuto è la Terra stessa, con il suo polo nord e polo sud geografici, su cui si basa il funzionamento delle bussole.

A livello molecolare, i magneti possiedono una struttura in cui ogni particella forma un piccolo **dipolo** (polo sud e polo nord). Questa polarizzazione interna è una caratteristica intrinseca di alcuni materiali.

Le interazioni tra poli magnetici seguono una regola fondamentale:

- **Poli di uguale segno si respingono**
- **Poli di segno opposto si attraggono**

### 🔹 Campo magnetico generato dalla corrente

Un conduttore percorso da corrente genera un campo magnetico nel suo intorno. Le **linee di forza** di questo campo sono concentriche e coassiali all'asse del conduttore, formando cerchi attorno al filo. Questo fenomeno è visualizzabile con il classico esperimento della limatura di ferro su un foglio di carta attraversato da un filo.

L'intensità del campo magnetico è **direttamente proporzionale** alla corrente che scorre nel conduttore: più corrente transita, più forte è il campo magnetico generato.

### 🔹 Induzione elettromagnetica (Faraday, 1830)

Il fenomeno è **perfettamente reversibile**:

1. **Corrente → Campo magnetico**: un conduttore percorso da corrente genera un campo magnetico
2. **Campo magnetico → Corrente**: muovendo un magnete vicino a una spira conduttrice, si genera una tensione (e quindi una corrente) nella spira stessa

La tensione indotta è tanto maggiore quanto più è veloce il moto relativo tra il magnete e la spira. Questo principio, scoperto da **Faraday** e **Ørsted**, è alla base di generatori, alternatori e trasformatori.

---

## 📡 2. L'induttore (bobina, solenoide) (⏱ 29:10)

### 🔹 Struttura e funzionamento

Un **induttore** (detto anche **bobina** o **solenoide**) si ottiene avvolgendo un conduttore a spirale, con più spire una accanto all'altra, su un supporto. Rispetto al filo rettilineo, l'avvolgimento a più spire **rinforza** la capacità di produrre campo magnetico.

Quando attraversato da corrente:

- **Corrente continua**: si forma un campo magnetico stazionario nell'intorno, ma senza ulteriori effetti dinamici
- **Corrente alternata**: la corrente viene **ostacolata** nel suo passaggio. L'induttore genera una **forza controelettromotrice** che si oppone alla variazione di corrente

### 🔹 L'induttanza e la sua unità di misura

L'**induttanza** — grandezza che esprime la capacità di un induttore di generare campo magnetico — si indica con la lettera **L** e si misura in **Henry** (simbolo: **H**).

> **Definizione**: Un Henry corrisponde a un flusso magnetico di 1 Weber quando l'induttore è attraversato da 1 Ampere di corrente.
>
> $$1 \text{ H} = \frac{1 \text{ Wb}}{1 \text{ A}}$$

L'Henry è un'unità di misura **molto grande**; nella pratica si utilizzano i sottomultipli:

| Sottomultiplo | Simbolo | Valore        | Notazione esponenziale |
| ------------- | ------- | ------------- | ---------------------- |
| millihenry    | mH      | 0,001 H       | $10^{-3}$ H            |
| microhenry    | µH      | 0,000001 H    | $10^{-6}$ H            |
| nanohenry     | nH      | 0,000000001 H | $10^{-9}$ H            |

### 🔹 Fattori che influenzano l'induttanza

L'induttanza di una bobina dipende dalle sue caratteristiche costruttive secondo la formula:

> $$L = \mu \cdot \frac{N^2 \cdot S}{l}$$

Dove:

- **L** = induttanza in Henry
- **µ (mu)** = permeabilità magnetica del nucleo
- **N** = numero di spire
- **S** = sezione (diametro) su cui sono avvolte le spire
- **l** = lunghezza totale dell'avvolgimento

Relazioni di proporzionalità:

- L è **proporzionale al quadrato** del numero di spire ($N^2$)
- L è **direttamente proporzionale** alla sezione S
- L è **direttamente proporzionale** alla permeabilità magnetica µ del nucleo
- L è **inversamente proporzionale** alla lunghezza l dell'avvolgimento

⚠️ _Queste relazioni di proporzionalità sono frequentemente oggetto di domande d'esame._

### 🔹 Permeabilità magnetica (µ)

La **permeabilità magnetica** (µ) è la proprietà di un materiale di magnetizzarsi più o meno intensamente in un campo magnetico. I materiali **ferromagnetici** (magnetite, ferro, nichel, leghe ferrose) hanno permeabilità elevata e concentrano il flusso magnetico, aumentando l'induttanza.

La permeabilità del vuoto (o dell'aria) è indicata con **µ₀** e viene usata come riferimento per esprimere la **permeabilità relativa** di tutti gli altri materiali.

### 🔹 Tipologie di induttori

- **Induttori con nucleo assiale**: bobina avvolta su supporto cilindrico con nucleo ferromagnetico inserito assialmente. Le linee di flusso si estendono all'esterno, con possibili effetti di accoppiamento con bobine vicine.
- **Induttori toroidali**: bobina avvolta su un nucleo ad anello (toroide). Il flusso magnetico circola interamente all'interno del nucleo, con minor dispersione e minor accoppiamento indesiderato.
- **Induttore variabile**: dotato di nucleo avvitabile; ruotando il nucleo si varia l'induttanza. Il simbolo elettrico è quello dell'induttore con una freccia diagonale. Si trovano nelle vecchie radio AM/FM per la taratura dei circuiti.

---

## 🔗 3. Induttori in serie e in parallelo (⏱ 46:29)

### 🔹 Collegamento in serie

In un collegamento in serie la stessa corrente attraversa tutti gli induttori. L'induttanza totale è la **somma** dei singoli valori:

> $$L_{tot} = L_1 + L_2 + L_3 + \ldots$$

### 🔹 Collegamento in parallelo

In un collegamento in parallelo la stessa tensione è applicata a tutti gli induttori. L'induttanza totale si calcola come:

> $$\frac{1}{L_{tot}} = \frac{1}{L_1} + \frac{1}{L_2} + \frac{1}{L_3} + \ldots$$

Le formule sono **identiche** a quelle delle resistenze in serie e in parallelo, sostituendo R con L.

> **Suggerimento per l'esame**: con la calcolatrice, per il parallelo si calcola $1/L_1$, si somma a $1/L_2$, poi a $1/L_3$, e alla fine si fa $1/x$ del totale per ottenere $L_{tot}$.

---

## ⏱️ 4. Costante di tempo τ = L/R (⏱ 60:03)

### 🔹 Comportamento transitorio

Quando si collega un induttore a una tensione continua (o al primo istante di una tensione alternata), la corrente **non sale istantaneamente** ma cresce con un andamento **esponenziale** fino a raggiungere il valore di regime (100%).

La **costante di tempo** (τ, tau) è definita come il tempo impiegato dalla corrente per raggiungere il **63%** del suo valore di regime:

> $$\tau = \frac{L}{R}$$

Dove:

- **τ** = costante di tempo in secondi
- **L** = induttanza in Henry
- **R** = resistenza in serie in Ohm

Il valore di regime (100%) viene raggiunto dopo circa **4–5 costanti di tempo**.

> Il 63% deriva dalla formula esponenziale: $i(t) = I_{max}(1 - e^{-t/\tau})$; per $t = \tau$ si ottiene $i = I_{max}(1 - e^{-1}) \approx 0{,}63 \cdot I_{max}$.

---

## 📐 5. Sfasamento e reattanza induttiva (⏱ 71:01)

### 🔹 La corrente è in ritardo di 90°

In un induttore alimentato in corrente alternata, la **corrente è in ritardo di 90°** rispetto alla tensione (oppure equivalentemente: la tensione è in anticipo di 90° rispetto alla corrente). Tensione e corrente si dicono **in quadratura**.

Questo avviene perché la tensione applicata genera un campo magnetico che produce una **forza controelettromotrice**, ostacolando l'instaurarsi immediato della corrente.

### 🔹 Reattanza induttiva ($X_L$)

L'opposizione offerta dall'induttore al passaggio della corrente alternata si chiama **reattanza induttiva** e si misura in **ohm**, analogamente alla resistenza.

> **Formula:**
> $$X_L = 2\pi f L$$

Dove:

- **$X_L$** = reattanza induttiva in ohm (Ω)
- **$f$** = frequenza in Hertz (Hz)
- **$L$** = induttanza in Henry (H)
- **$2\pi f$** = pulsazione angolare (quanti giri al secondo fa la sinusoide)

Proprietà fondamentali:

- $X_L$ è **direttamente proporzionale** alla frequenza: aumentando $f$, aumenta $X_L$
- $X_L$ è **direttamente proporzionale** all'induttanza: aumentando $L$, aumenta $X_L$
- L'andamento è **lineare**: il grafico $X_L$ vs $f$ è una retta

### 🔹 Esercizio svolto: calcolo reattanza

Induttore da 10 mH alimentato a diverse frequenze:

| Frequenza | Calcolo                                                        | Reattanza $X_L$ |
| --------- | -------------------------------------------------------------- | --------------- |
| 100 kHz   | $2\pi \times 100.000 \times 0{,}01 = 6{,}28 \times 1000$       | **6.280 Ω**     |
| 1 MHz     | $2\pi \times 1.000.000 \times 0{,}01 = 6{,}28 \times 10.000$   | **62.800 Ω**    |
| 10 MHz    | $2\pi \times 10.000.000 \times 0{,}01 = 6{,}28 \times 100.000$ | **628.000 Ω**   |

> **Importante per l'esame**: nelle formule bisogna sempre convertire i valori nei loro multipli/sottomultipli canonici (Hz, H, Ω) prima di eseguire i calcoli. Per semplificare, si possono usare le notazioni esponenziali: ad esempio $10 \text{ mH} = 10 \times 10^{-3}$ e $100 \text{ kHz} = 100 \times 10^{3}$, semplificando $10^{3}$ con $10^{-3}$.

---

## 🌀 6. Effetto pelle (⏱ 78:07)

### 🔹 Distribuzione della corrente ad alta frequenza

L'**effetto pelle** (skin effect) è il fenomeno per cui, a frequenze elevate, la corrente alternata tende a scorrere prevalentemente sulla **superficie esterna** del conduttore, anziché distribuirsi uniformemente sulla sezione.

Questo avviene perché al centro del conduttore si ha una maggiore concentrazione di linee di campo magnetico, che oppone maggiore reattanza al passaggio della corrente. La corrente "cerca" il percorso con meno opposizione, ovvero la superficie.

Per questo motivo, nelle applicazioni ad alta frequenza si usano **fili di rame argentato**: lo strato di argento all'esterno, essendo un conduttore migliore del rame, riduce ulteriormente la resistenza al passaggio della corrente sulla superficie.

⚠️ _Non ci sono domande d'esame sul calcolo della profondità dell'effetto pelle, ma è un concetto da conoscere._

---

## ⚡ 7. Il trasformatore (⏱ 96:51)

### 🔹 Principio di funzionamento

Il **trasformatore** è un dispositivo elettrico formato da **due induttori** (avvolgimento primario e secondario) accoppiati magneticamente attraverso un **nucleo ferromagnetico**. Funziona **esclusivamente in corrente alternata**.

Il principio è la **mutua induzione**: la corrente alternata che scorre nel primario genera un campo magnetico variabile che si concatena con il secondario attraverso il nucleo, inducendo una tensione (e quindi una corrente) nel secondario.

> **Attenzione**: se un trasformatore viene alimentato in corrente continua, l'avvolgimento primario presenta quasi solo la resistenza del filo (molto bassa), comportandosi come un quasi-cortocircuito. Non si ha trasferimento di energia al secondario e il trasformatore può danneggiarsi.

### 🔹 Rapporto di trasformazione

Il **rapporto di trasformazione** (K) è il rapporto tra il numero di spire del primario e del secondario:

> $$K = \frac{N_P}{N_S} = \frac{V_P}{V_S}$$

La tensione in uscita dal secondario vale:

> $$V_S = \frac{V_P}{K}$$

Dove:

- **$N_P$**, **$N_S$** = numero di spire primario e secondario
- **$V_P$**, **$V_S$** = tensione primario e secondario (valori efficaci)

### 🔹 Conservazione della potenza

Il rendimento di un trasformatore è **prossimo al 100%**: la potenza trasferita dal primario si ritrova quasi identica sul secondario, ma con parametri diversi di tensione e corrente.

> $$P_P = V_P \times I_P \approx P_S = V_S \times I_S$$

Se il trasformatore abbassa la tensione (riduttore), la corrente disponibile sul secondario **aumenta** proporzionalmente, e viceversa.

### 🔹 Esercizio svolto

Un trasformatore con primario di 500 spire e secondario di 25 spire:

- Rapporto di trasformazione: $K = 500/25 = 20$
- Alimentato a 220 V sul primario: $V_S = 220/20 = 11$ V sul secondario

Un trasformatore 220 V / 22 V (K = 10) con 1 A sul primario:

- Potenza primario: $P = 220 \times 1 = 220$ W
- Corrente secondario: $I_S = P/V_S = 220/22 = 10$ A
- Verifica: $P_S = 22 \times 10 = 220$ W ✓

### 🔹 Trasformatore elevatore e riduttore

Il trasformatore è **perfettamente reversibile**:

- **Riduttore**: alimentato dal primario (più spire), abbassa la tensione sul secondario. Uso tipico: alimentatori domestici (da 220 V a 12 V).
- **Elevatore**: alimentato dal secondario (meno spire), eleva la tensione sul primario. Uso tipico: linee elettriche ad alta tensione.

Le linee ad alta tensione usano trasformatori elevatori per trasportare l'energia a grandi distanze: aumentando la tensione si riduce la corrente, e quindi si riducono le perdite per effetto termico ($P = R \times I^2$) nei cavi.

> Nota storica: la disputa tra Edison (corrente continua) e Tesla (corrente alternata) si risolse a favore di Tesla proprio grazie alla possibilità di usare il trasformatore per il trasporto efficiente dell'energia elettrica.

---

## 🔗 Concept Map (testuale)

- **Corrente in un conduttore** → genera → **Campo magnetico**
- **Campo magnetico variabile** → induce → **Tensione in una spira** (Faraday)
- **Spire avvolte** → formano → **Induttore (bobina)**
- **Induttore** → ha proprietà → **Induttanza (L, Henry)**
- **Induttanza** → dipende da → **N² (spire), S (sezione), µ (permeabilità), 1/l (lunghezza)**
- **Permeabilità magnetica** → aumenta con → **Materiali ferromagnetici (ferro, nichel)**
- **Induttore in corrente alternata** → produce → **Sfasamento 90° (corrente in ritardo)**
- **Sfasamento** → determina → **Reattanza induttiva ($X_L = 2\pi fL$)**
- **Reattanza induttiva** → aumenta con → **Frequenza e induttanza**
- **Due induttori accoppiati** → formano → **Trasformatore**
- **Trasformatore** → trasforma → **Tensione e corrente (conservando la potenza)**
- **Rapporto di trasformazione** → è dato da → **$K = N_P/N_S = V_P/V_S$**

---

## 📝 Key Takeaways

1. Un conduttore percorso da corrente genera un campo magnetico; il fenomeno è reversibile (induzione elettromagnetica di Faraday).
2. L'induttanza si misura in **Henry** (H), ma nella pratica si usano millihenry (mH), microhenry (µH) e nanohenry (nH). L'induttanza cresce con $N^2$, con la sezione S e con la permeabilità µ, mentre diminuisce con la lunghezza dell'avvolgimento.
3. In un induttore alimentato in corrente alternata, la **corrente è in ritardo di 90°** rispetto alla tensione.
4. La **reattanza induttiva** $X_L = 2\pi fL$ è l'opposizione dell'induttore al passaggio di corrente alternata. Aumenta linearmente con la frequenza e con l'induttanza.
5. Gli induttori in serie si sommano ($L_{tot} = L_1 + L_2 + ...$); in parallelo si usa la formula del reciproco, identica alle resistenze.
6. Il trasformatore funziona **solo in corrente alternata** e trasforma tensione e corrente secondo il rapporto $K = N_P/N_S$, conservando la potenza.
7. Nelle formule bisogna sempre usare le unità di misura canoniche (H, Hz, Ω), convertendo da multipli/sottomultipli prima del calcolo.

---

## ❓ Comprehension Questions

1. Perché un induttore oppone resistenza al passaggio della corrente alternata ma non della corrente continua?
2. Come cambia l'induttanza di una bobina se si raddoppia il numero di spire mantenendo invariati tutti gli altri parametri?
3. Un induttore da 5 mH viene alimentato a 200 kHz. Qual è la sua reattanza induttiva? Spiegare il procedimento di conversione delle unità.
4. Perché il trasformatore non funziona con la corrente continua? Cosa succederebbe collegando una batteria al primario?
5. Un trasformatore ha un rapporto di trasformazione di 15. Se la tensione sul primario è 300 V e la corrente è 2 A, quali sono tensione e corrente sul secondario?
6. Spiegare perché le linee elettriche ad alta tensione utilizzano trasformatori elevatori e in che modo questo riduce le perdite di energia.
7. Qual è la differenza tra un induttore toroidale e uno con nucleo assiale in termini di dispersione del campo magnetico?
8. Perché l'effetto pelle è rilevante nelle applicazioni ad alta frequenza e come si mitiga nella pratica?

---

## 📚 Glossary

- **Bobina** — sinonimo di induttore; conduttore avvolto in più spire
- **Costante di tempo (τ)** — tempo impiegato dalla corrente per raggiungere il 63% del valore di regime; per un circuito RL vale $\tau = L/R$
- **Effetto pelle (skin effect)** — fenomeno per cui la corrente alternata ad alta frequenza scorre prevalentemente sulla superficie esterna del conduttore
- **Henry (H)** — unità di misura dell'induttanza; 1 H = 1 Wb / 1 A
- **Induttanza (L)** — grandezza che esprime la capacità di un induttore di generare campo magnetico; si misura in Henry
- **Induttore** — componente elettronico costituito da un conduttore avvolto in spire, che immagazzina energia sotto forma di campo magnetico
- **Induttore variabile** — induttore il cui valore può essere regolato inserendo più o meno un nucleo ferromagnetico
- **Mutua induzione** — fenomeno per cui un campo magnetico variabile in un avvolgimento induce una tensione in un avvolgimento vicino
- **Permeabilità magnetica (µ)** — proprietà di un materiale che esprime la capacità di magnetizzarsi; µ₀ è la permeabilità del vuoto/aria
- **Rapporto di trasformazione (K)** — rapporto tra spire primario e secondario di un trasformatore; $K = N_P/N_S$
- **Reattanza induttiva ($X_L$)** — opposizione offerta da un induttore al passaggio di corrente alternata; $X_L = 2\pi fL$, misurata in ohm
- **Solenoide** — sinonimo di induttore; avvolgimento di forma cilindrica
- **Toroide** — nucleo ad anello su cui si avvolgono le spire di un induttore; consente di contenere il campo magnetico all'interno
- **Trasformatore** — dispositivo a due avvolgimenti accoppiati magneticamente che trasforma tensione e corrente alternata mantenendo la potenza costante
- **Weber (Wb)** — unità di misura del flusso magnetico

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo (IZ5 — sezione ARI Prato) e Sauro (sezione ARI Prato, licenza dal 1984)
- 📋 **Coordinamento**: Alessio (mappa interattiva sezioni), Fabrizio, Federico

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                  |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione**          | 04                                                                                                                                                                                                                      |
| **Data**             | 26 marzo 2025                                                                                                                                                                                                           |
| **Durata**           | ~2 ore e 20 minuti                                                                                                                                                                                                      |
| **Numero argomenti** | 7                                                                                                                                                                                                                       |
| **Parole chiave**    | induttore, induttanza, Henry, campo magnetico, induzione elettromagnetica, Faraday, reattanza induttiva, $X_L = 2\pi fL$, trasformatore, rapporto di trasformazione, effetto pelle, serie, parallelo, costante di tempo |
