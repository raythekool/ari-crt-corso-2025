---
layout: default
title: "11 - I Transistor e i Tubi a Vuoto"
permalink: /guide-studio/lezione_11.html
---

# 📘 Lezione 11 - Il Transistor, gli Amplificatori e i Tubi a Vuoto

## 📌 Panoramica

- **Materia**: Radiotecnica — Dispositivi Attivi e Amplificazione
- **Tempo di studio stimato**: 2 ore
- **Prerequisiti**: Semiconduttori e drogaggio, tensione e corrente.
- **Obiettivi di apprendimento**:
  - Comprendere la struttura e il funzionamento del transistor BJT (NPN e PNP).
  - Imparare il concetto di amplificazione e il fattore Hfe (Beta).
  - Distinguere le tre configurazioni degli amplificatori (emettitore, base e collettore comune).
  - Conoscere i principi dei FET e MOSFET.
  - Comprendere il funzionamento base dei tubi a vuoto (diodo, triodo, tetrodo, pentodo).

---

## 📖 Contenuti Teorici

### 1. 📡 Il Transistor BJT (Bipolar Junction Transistor)

Il transistor è un dispositivo a semiconduttore fondamentale, costituito da tre strati drogati, usato principalmente per **amplificare** segnali elettrici. A seconda della disposizione degli strati, può essere di tipo **NPN** o **PNP**.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_11/slide-02.jpg" alt="Transistor NPN e PNP" style="width: 75%;"></div><br>

#### 🔹 Struttura e Terminali
Ha tre reofori (terminali), ciascuno collegato a uno strato drogato:
- **Base (B)**: strato centrale, molto sottile, agisce da terminale di controllo.
- **Collettore (C)**: riceve la maggior parte della corrente.
- **Emettitore (E)**: emette i portatori di carica verso il collettore.

I contatti fra le parti drogate formano due **giunzioni**: la giunzione Base-Collettore (BC) e la giunzione Base-Emettitore (BE).

#### 🔹 Principio di Amplificazione
Il transistor è un dispositivo **attivo** controllato in corrente: una minima variazione della corrente di base ($I_B$) provoca una notevole variazione della corrente di collettore ($I_C$). La corrente di base è molto minore della corrente di collettore, quindi le correnti di collettore ed emettitore sono quasi uguali.

Il rapporto tra la corrente di collettore e la corrente di pilotaggio alla base si chiama **Guadagno in Corrente** e si indica con **Hfe** o **Beta ($\beta$)**. Può valere 100-200 o più.

---

### 2. 🎛️ Configurazioni degli Amplificatori

Per amplificare i segnali, i transistor BJT possono essere configurati in tre modi principali:

#### 🔹 Emettitore Comune
- L'emettitore è in comune tra l'ingresso e l'uscita.
- **Amplifica sia la tensione che la corrente**.
- È la configurazione classica e più diffusa degli amplificatori generici.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_11/slide-11.jpg" alt="Emettitore Comune" style="width: 75%;"></div><br>

#### 🔹 Base Comune
- La base separa i circuiti di ingresso e uscita.
- Il guadagno in corrente è circa 1 (non amplifica la corrente), ma **amplifica la tensione**.
- Offre alta stabilità ed è molto usato in **alta frequenza**.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_11/slide-12.jpg" alt="Base Comune" style="width: 75%;"></div><br>

#### 🔹 Collettore Comune (Inseguitore di Emettitore)
- Il guadagno in tensione è circa 1, ma **amplifica la corrente**.
- È usato come separatore di stadi (buffer) e per pilotare carichi a bassa impedenza.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_11/slide-13.jpg" alt="Collettore Comune" style="width: 75%;"></div><br>

#### 🔹 Polarizzazione
Affinché il transistor amplifichi correttamente senza distorcere il segnale, deve essere **polarizzato**, ossia devono essere impostate tensioni e correnti continue "a riposo" (in assenza di segnale) tramite resistenze. Questo fa lavorare il dispositivo nel tratto lineare delle sue curve caratteristiche.

---

### 3. 🔌 FET e MOSFET

I transistor a effetto di campo (FET) operano diversamente dai BJT.

#### 🔹 FET (Field Effect Transistor)
È un dispositivo controllato in **tensione**, non in corrente, presentando un'**altissima impedenza di ingresso**. I terminali sono:
- **Gate (G)**: controlla il passaggio di cariche (analogo alla Base).
- **Drain (D)**: analogo al Collettore.
- **Source (S)**: analogo all'Emettitore.

Il suo guadagno è chiamato **Transconduttanza (Gm)**, ed è il rapporto tra la variazione di corrente nel Drain e la variazione di tensione applicata al Gate ($\Delta I_D / \Delta V_G$).

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_11/slide-19.jpg" alt="Struttura del FET" style="width: 75%;"></div><br>

#### 🔹 MOSFET
Ha una struttura simile al FET, ma il terminale di Gate è realizzato con una superficie metallica **isolata** dal canale mediante un sottile strato di ossido di silicio. Questo garantisce un'impedenza d'ingresso ancora più elevata.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_11/slide-22.jpg" alt="MOSFET" style="width: 75%;"></div><br>

---

### 4. 💡 I Tubi a Vuoto (Valvole Termoioniche)

Prima dei transistor, le amplificazioni venivano fatte tramite i tubi a vuoto (o valvole). Sono formati da bulbi di vetro al cui interno è praticato il vuoto. Operano riscaldando un filamento, causando l'emissione di elettroni (effetto termoionico).

#### 🔹 Il Diodo a Vuoto
Ha due elettrodi principali: **catodo** e **anodo**. Il filamento riscaldatore porta all'incandescenza il catodo, che emette elettroni. 
- Se l'anodo è positivo rispetto al catodo, attira gli elettroni e scorre corrente.
- Se è negativo, li respinge e non scorre corrente.
Funge da raddrizzatore.

#### 🔹 Il Triodo
Aggiunge un terzo elettrodo, la **griglia di controllo**, a forma di spirale, posta tra catodo e anodo.
- Una piccola tensione negativa sulla griglia respinge in parte gli elettroni, controllando il flusso di corrente verso l'anodo.
- In questo modo, la valvola **amplifica** i segnali, analogamente a un transistor.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_11/slide-27.jpg" alt="Triodo" style="width: 75%;"></div><br>

#### 🔹 Il Tetrodo
Aggiunge una seconda griglia (la **griglia schermo**) tra la griglia di controllo e l'anodo.
- Riduce la capacità parassita tra anodo e griglia di controllo, evitando auto-oscillazioni ad alta frequenza.
- Polarizzata positivamente, favorisce l'accelerazione degli elettroni e offre maggiore amplificazione.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_11/slide-28.jpg" alt="Tetrodo" style="width: 75%;"></div><br>

#### 🔹 Il Pentodo
Inserisce una terza griglia (la **griglia soppressore**) tra la griglia schermo e l'anodo.
- Viene collegata spesso al catodo e serve a respingere verso l'anodo gli "elettroni secondari" rimbalzati dall'anodo stesso a causa del forte impatto.
- Questo rende la curva caratteristica più lineare e migliora ulteriormente il guadagno.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_11/slide-29.jpg" alt="Pentodo" style="width: 75%;"></div><br>

---

## 🔗 Mappa Concettuale

- **Transistor BJT** → controllato in corrente → NPN / PNP
  - Terminali: **Base, Collettore, Emettitore**
  - **Beta (Hfe)** → fattore di amplificazione di corrente
  - **Emettitore comune** → amplifica V e I
  - **Base comune** → amplifica V, alta frequenza
  - **Collettore comune** → amplifica I, separatore
- **FET / MOSFET** → controllati in tensione, alta impedenza d'ingresso
  - Terminali: **Gate, Drain, Source**
- **Tubi a Vuoto**
  - **Diodo**: catodo, anodo → raddrizzatore
  - **Triodo**: + griglia controllo → amplificatore
  - **Tetrodo**: + griglia schermo → evita oscillazioni e aumenta guadagno
  - **Pentodo**: + griglia soppressore → elimina emissione secondaria e migliora linearità

---

## 📝 Punti Chiave

1. Il **BJT** (Bipolar Junction Transistor) ha tre terminali: Base, Emettitore e Collettore. Funziona da amplificatore di corrente (la debole corrente di base regola la forte corrente tra collettore ed emettitore).
2. Il **Beta (Hfe)** è il parametro che indica il guadagno di corrente (Ic / Ib).
3. L'**Emettitore Comune** è la configurazione più usata per ottenere guadagno sia di tensione che di corrente.
4. I **FET** e i **MOSFET** hanno tre terminali (Gate, Drain, Source) e si differenziano dai BJT perché sono **controllati in tensione** e offrono altissima impedenza d'ingresso.
5. I **Tubi a vuoto** basano il funzionamento sull'emissione termoionica da un catodo riscaldato. Il **Triodo** amplifica grazie alla griglia di controllo; le griglie aggiuntive nel **Tetrodo** e nel **Pentodo** ne migliorano le prestazioni, specialmente alle alte frequenze e in termini di linearità.

---

## ❓ Domande di Comprensione

1. Qual è la relazione tra la corrente di base, di collettore e di emettitore in un BJT?
2. A cosa serve la polarizzazione in un circuito a transistor?
3. In quale configurazione del BJT non si ha amplificazione di tensione ma solo di corrente?
4. Qual è la differenza principale tra il controllo di un transistor BJT e un transistor FET?
5. Qual è lo scopo della "griglia schermo" nel tetrodo rispetto al semplice triodo?
6. Che funzione svolge la griglia soppressore nel pentodo?

---

## 📚 Glossario

- **BJT (Transistor a Giunzione Bipolare)**: Transistor basato su due giunzioni PN, controllato in corrente.
- **Beta (Hfe)**: Guadagno di corrente in continua di un transistor a emettitore comune.
- **FET (Field Effect Transistor)**: Transistor a effetto di campo, controllato in tensione, con alta impedenza di ingresso.
- **MOSFET**: FET in cui il gate è isolato dal canale tramite un sottile strato di ossido.
- **Transconduttanza ($G_m$)**: Nei FET, è il rapporto tra la variazione di corrente di Drain e la variazione di tensione di Gate.
- **Triodo**: Tubo a vuoto con tre elettrodi (catodo, anodo, griglia di controllo), usato per amplificare segnali.
- **Tetrodo**: Tubo a vuoto con quattro elettrodi (aggiunge la griglia schermo per migliorare l'amplificazione ad alta frequenza).
- **Pentodo**: Tubo a vuoto con cinque elettrodi (aggiunge la griglia soppressore per abbattere le emissioni secondarie dell'anodo).

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------- |
| **Numero lezione**   | 11                                                                                                        |
| **Data**             | 27 maggio 2026                                                                                            |
| **Durata**           | ~2 ore                                                                                                    |
| **Numero argomenti** | 4 (BJT, Configurazioni Amplificatori, FET/MOSFET, Tubi a vuoto)                                           |
| **Parole chiave**    | Transistor, NPN, PNP, Base, Collettore, Emettitore, FET, MOSFET, Triodo, Tetrodo, Pentodo, Amplificazione |
