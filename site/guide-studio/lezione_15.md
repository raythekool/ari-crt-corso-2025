---
layout: default
---

# 📘 Lezione 15 - Linee di Trasmissione

## 📌 Overview

- **Materia**: Elettronica e tecnica dei ricevitori radio
- **Argomento principale**: I ricevitori radioamatoriali — architettura supereterodina, tipi di rivelatori, AGC, frequenza immagine e problemi dei ricevitori
- **Tempo di studio stimato**: 2 ore e 30 minuti
- **Prerequisiti**: Conoscenza dei filtri e circuiti risonanti (Lezione 06), modulazioni AM/SSB/FM (Lezione 07), decibel (Lezione 13), trasmettitori e miscelatori (Lezione 14)
- **Obiettivi di apprendimento**:
  - Comprendere l'architettura del ricevitore supereterodina a singola e doppia conversione
  - Conoscere i rivelatori specifici per CW, SSB, AM e FM
  - Capire il funzionamento dell'AGC e dell'S-meter
  - Comprendere il problema della frequenza immagine e le sue soluzioni
  - Conoscere i problemi dei ricevitori: bloccaggio, modulazione incrociata e intermodulazione

---

## 📖 Core Content

### 1. 📝 Correzione quiz Lezione 14 (⏱ 00:02)

La lezione si apre con la correzione dei quiz della settimana precedente, riguardanti i trasmettitori. Vengono riviste le seguenti domande chiave:

**Moltiplicatori di frequenza in FM**: nei trasmettitori FM, per aumentare la **deviazione di frequenza** prodotta dal modulatore si utilizzano i **moltiplicatori di frequenza**, non i filtri passa-basso né i modulatori bilanciati. I moltiplicatori moltiplicano sia la frequenza sia la deviazione per lo stesso fattore.

**Filtro passabanda in SSB**: all'uscita del modulatore bilanciato è presente un filtro passabanda per eliminare una delle due bande laterali (o equivalentemente per selezionare la banda laterale voluta). Il modulatore bilanciato produce un segnale DSB (doppia banda laterale), e il filtro ne lascia passare una sola.

**Filtro passa-basso in uscita al trasmettitore**: se si trasmette a 14 MHz, la frequenza di taglio del filtro deve essere **poco superiore** alla frequenza di trasmissione, ma **inferiore alla seconda armonica** (2 × 14 = 28 MHz). Un filtro troppo alto (es. 50 MHz) lascerebbe passare armoniche pericolose.

**Calcolo della deviazione di frequenza**: viene svolto un esercizio dettagliato. Un oscillatore a 12,21 MHz modulato a reattanza deve produrre una trasmissione a 146,52 MHz con deviazione di 5 kHz. Il fattore di moltiplicazione è 146,52 / 12,21 = **12**. Quindi la deviazione all'oscillatore dev'essere 5000 / 12 ≈ **417 Hz**. Il fattore di moltiplicazione si applica identicamente sia alla frequenza sia alla deviazione.

**Mixer**: un segnale a 5,3 MHz non può diventare 14,3 MHz per moltiplicazione (×2 = 10,6; ×3 = 15,9). L'unico circuito che può fare questa traslazione è il **mixer** (miscelatore/convertitore): 5,3 + 9,0 = 14,3 MHz.

---

### 2. 📡 Introduzione ai ricevitori (⏱ 13:52)

Il ricevitore è il componente che **caratterizza maggiormente** una stazione radioamatoriale. A differenza dei trasmettitori, che sono sostanzialmente identici tra radio economiche e costose (un trasmettitore da 100 W ha sempre lo stesso costo industriale), il **ricevitore fa la differenza** nel prezzo.

Le radio possono essere classificate per fascia di prezzo:

- **Entry-level** (€500-1000): fanno il loro lavoro in condizioni normali, ma hanno limiti intrinseci con bande affollate
- **Fascia intermedia** (€1000-2000): prestazioni discrete
- **Top di gamma** (€5000-10000): ricevitori "macchine da guerra", robustissimi, raramente perdono il controllo della situazione

La differenza sostanziale sta nella **componentistica** del ricevitore: circuiti risonanti, filtri e dispositivi di alta qualità costano molto. Un ricevitore di fascia alta deve continuare a funzionare anche con bande strapiene durante i contest, dove segnali fortissimi potrebbero far "imbarcare" un ricevitore economico.

---

### 3. 🔍 Le tre caratteristiche fondamentali del ricevitore (⏱ 19:15)

Un buon ricevitore deve possedere tre caratteristiche essenziali:

#### 🔹 Sensibilità

La **sensibilità** — è la capacità di ascoltare segnali deboli, discriminando il segnale utile dal rumore. Un collegamento si fa non quando un segnale arriva forte, ma quando il **rapporto segnale/rumore (S/N)** è adeguato. Si può avere un segnale forte, ma se il rumore è più forte, il segnale non è comprensibile.

La sensibilità si ottiene attraverso l'**amplificazione**: un ricevitore deve amplificare il segnale dall'antenna da **1 milione a 10 milioni di volte**. Un'antenna può captare segnali da 1-5-10 µV (microvolts), che devono essere portati a circa 10 V per pilotare l'altoparlante. Questa amplificazione è realizzata da una **catena di amplificatori** in successione.

#### 🔹 Selettività

La **selettività** — è la capacità di far ascoltare solo il segnale su cui si è sintonizzati, senza interferenze dai canali adiacenti. Si realizza con **filtri**: circuiti risonanti LC o filtri a cristallo di quarzo.

Il problema è che avere un filtro per ogni canale sarebbe costosissimo, e un singolo circuito risonante LC non è sufficiente per separare canali vicini (ne servirebbero almeno 5 in cascata). Sintonizzare manualmente 5 filtri in serie sarebbe impraticabile.

#### 🔹 Stabilità

La **stabilità** — è la caratteristica meccanica ed elettrica per cui, una volta sintonizzato su una certa frequenza, il ricevitore deve restare lì senza derive.

---

### 4. 📻 Il ricevitore supereterodina (⏱ 25:03)

Per risolvere il problema della selettività, verso il **1910-1915** fu inventata l'architettura dei ricevitori **supereterodina** (ricevitori a conversione). Il termine "eterodinaggio" indica il processo di battimento tra due segnali per ottenere una terza frequenza.

#### 🔹 Principio di funzionamento

Il cuore del sistema è un **filtro a frequenza fissa** (tipicamente a cristallo di quarzo), ad esempio a **9 MHz** o **455 kHz**. Questo filtro non può essere spostato in frequenza poiché i cristalli hanno frequenza determinata dal taglio e dalle dimensioni fisiche.

La soluzione geniale è: invece di spostare il filtro, si **porta il segnale desiderato alla frequenza del filtro**. Questo avviene tramite un **convertitore** (mixer) e un **oscillatore locale** (VFO).

**Esempio con la banda cittadina (27 MHz)**:

- Voglio ricevere il Canale 1 a 27,000 MHz
- Il filtro è fisso a 9 MHz
- L'oscillatore locale genera 18,000 MHz
- Il mixer calcola: 27,000 − 18,000 = **9,000 MHz** → il segnale passa il filtro
- Per ricevere il Canale 2 (27,010 MHz): sposto l'oscillatore locale a 18,010 MHz
- 27,010 − 18,010 = 9,000 MHz → sempre alla frequenza del filtro

La **frequenza intermedia** (IF — Intermediate Frequency) è la frequenza fissa a cui il segnale viene convertito. La manopola di sintonia varia la frequenza dell'oscillatore locale.

#### 🔹 Schema a blocchi della supereterodina

```
Antenna → Amplificatore RF → Convertitore/Mixer → Filtro IF → Amplificatore IF → Rivelatore → Amplificatore BF → Altoparlante
                                    ↑
                            Oscillatore Locale (VFO)
```

Il ricevitore supereterodina è essenzialmente un **ricevitore a frequenza fissa** (dal filtro in poi) preceduto da un convertitore che, con un oscillatore locale di frequenza opportuna, converte volta per volta la frequenza desiderata alla frequenza intermedia.

> "La manopola della sintonia in queste radio mi varia la frequenza del mio oscillatore locale. Variando la frequenza dell'oscillatore locale io di volta in volta converto il canale che voglio ricevere alla mia frequenza intermedia."

#### 🔹 Oscillatore locale: tipologie

L'oscillatore locale può essere:

- Un **oscillatore libero**: usato nelle radio AM economiche (Rai 1, Rai 2, Rai 3)
- Un **PLL** (Phase-Locked Loop): usato dalla banda cittadina in poi, molto più stabile perché agganciato a un quarzo di riferimento
- Nei primi CB a 24 canali: le frequenze erano ottenute mescolando 6 quarzi con altri 4 quarzi (6 × 4 = 24 canali)

---

### 5. 🔄 Supereterodina a doppia conversione (⏱ 44:30)

In molti ricevitori si effettua una **doppia conversione**:

```
Antenna → Amp RF → 1° Mixer → Filtro 1ª IF (9 MHz) → 2° Mixer → Filtro 2ª IF (455 kHz) → Amp IF → Rivelatore → Amp BF → Altoparlante
                      ↑                                    ↑
              Oscillatore Locale                   Oscillatore Fisso
              (variabile - VFO)
```

La prima conversione usa un **oscillatore variabile** (VFO) per portare il segnale alla prima IF (es. 9 MHz). La seconda conversione usa un **oscillatore fisso** per riconvertire a una IF più bassa (es. 455 kHz).

Motivi per la doppia conversione:

- I filtri a frequenza più bassa costano meno
- Permette di avere una prima IF alta (buona reiezione della frequenza immagine) e una seconda IF bassa (filtri economici e performanti)
- Esistono anche ricevitori a **tripla conversione**

---

### 6. 🔊 Tre tipi di amplificatori nel ricevitore (⏱ 46:51)

In un ricevitore sono presenti tre categorie di amplificatori:

| Tipo                                        | Frequenza di lavoro            | Funzione                                                                     |
| ------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------- |
| **Amplificatore RF** (radiofrequenza)       | Frequenza dei segnali ricevuti | Amplifica segnali deboli dall'antenna; a volte chiamato **preamplificatore** |
| **Amplificatore IF** (frequenza intermedia) | Frequenza fissa (es. 9 MHz)    | Fornisce il grosso del guadagno (×1000 - ×10000); stadi in cascata           |
| **Amplificatore BF** (bassa frequenza)      | Frequenze audio                | Amplifica il segnale audio e pilota l'altoparlante                           |

L'amplificatore RF è spesso dotato di più modalità:

- **Preamplificatore alto guadagno**: +12/14/18 dB
- **Preamplificatore basso guadagno**: +6 dB
- **Through** (diretto): nessuna amplificazione, antenna collegata direttamente al mixer
- **Attenuatore**: −6, −12, −18 dB per evitare la saturazione con segnali forti in ingresso

---

### 7. 📶 Ricevitore per CW — Telegrafia (⏱ 48:46)

#### 🔹 Caratteristiche del filtro

Il segnale telegrafico è una **portante accesa e spenta** (on/off keying), quindi è molto stretto in frequenza. Si usa un filtro a **500 Hz** di larghezza di banda. Questo è un valore standard: nelle domande d'esame, se chiedono la larghezza di banda per CW, la risposta è **500 Hz**.

#### 🔹 Esempio numerico — Banda 80 m

- Banda: 3,5 − 4 MHz
- Oscillatore locale: 5 − 5,5 MHz
- Verifica: 3,5 + 5,5 = 9 MHz ✓ e 4,0 + 5,0 = 9 MHz ✓
- Frequenza intermedia: **9 MHz**

#### 🔹 Il BFO — Oscillatore di battimento

**BFO** — Beat Frequency Oscillator (oscillatore della frequenza di battimento). È un oscillatore, generalmente a quarzo, la cui frequenza è leggermente spostata rispetto alla frequenza intermedia.

Il problema della telegrafia è che una portante pura accesa/spenta non produce alcun suono udibile. Per renderla udibile si usa un **rivelatore a prodotto** (che funziona come un mixer):

- Il segnale CW arriva a 9 MHz (dalla catena IF)
- Il BFO genera 9 MHz + 700 Hz = 9,0007 MHz
- Il rivelatore a prodotto calcola: somma (18 MHz → inaudibile) e differenza (**700 Hz** → tono audio!)
- I tre puntini della lettera S diventano: **"ti-ti-ti"** a 700 Hz

**Perché 700 Hz?** È una frequenza a cui l'orecchio umano è particolarmente sensibile. Nelle radio più costose c'è una manopola di **pitch** che permette di regolare la frequenza del tono.

---

### 8. 📡 Ricevitore per SSB (⏱ 61:20)

#### 🔹 Caratteristiche del filtro

Il filtro per SSB ha una larghezza di banda di **2,5 kHz** (2 kHz e mezzo), corrispondente alla banda vocale utile (200 Hz − 2500 Hz).

#### 🔹 Rivelazione SSB

Il meccanismo è identico a quello della telegrafia: si usa un **rivelatore a prodotto** con un **BFO**. Il BFO "rimette la portante" che era stata soppressa in trasmissione, rigenerando così il segnale audio.

La differenza è che il BFO ha **due quarzi commutabili**:

- Quarzo per **USB** (Upper Side Band): BFO a 9 MHz + 2500 Hz
- Quarzo per **LSB** (Lower Side Band): BFO a 9 MHz − 2500 Hz = 8,9975 MHz

Si usa **un solo filtro** per entrambe le bande laterali e si commuta il quarzo del BFO. Usare due filtri separati sarebbe possibile ma molto più costoso (un filtro costa circa 10 volte un quarzo).

#### 🔹 Sintonia del ricevitore SSB

Nello schema del ricevitore SSB:

- **C3** = condensatore dell'oscillatore locale (**sintonia** = VFO)
- **C1, C2** = condensatori del preamplificatore sintonizzato (nelle radio vintage hanno manopole esterne; nelle radio moderne si sintonizzano automaticamente)

---

### 9. 📻 Ricevitore per AM (⏱ 71:51)

#### 🔹 Caratteristiche del filtro

L'AM richiede entrambe le bande laterali, quindi il filtro è largo il **doppio** rispetto all'SSB: tipicamente **5-6 kHz**.

#### 🔹 Rivelatore AM — diodo e condensatore

Il rivelatore AM è il circuito più semplice, identico alla storica **radio a galena**:

```
Segnale AM → Diodo → Condensatore → Uscita audio
```

1. Il **diodo** rettifica il segnale, tagliando la semionda negativa (lascia passare la corrente solo in un verso)
2. Il **condensatore** livella i picchi della portante a radiofrequenza
3. Sul condensatore resta l'**inviluppo** del segnale modulato = il segnale audio originale

È un circuito economicissimo e senza alternative pratiche per la demodulazione AM.

---

### 10. 📡 Ricevitore per FM (⏱ 76:28)

#### 🔹 Caratteristiche del filtro

L'FM è il modo di emissione più largo; si usano filtri a **10 kHz** di larghezza di banda (standard di canalizzazione attuale). La frequenza intermedia tipica è **10,7 MHz** (standard industriale adottato dalla maggior parte dei costruttori).

#### 🔹 Il limitatore

Nella catena di media frequenza FM compare uno stadio chiamato **limitatore** — un amplificatore che lavora in **saturazione** e taglia ("tosa") i picchi del segnale al di sopra di un certo livello, rendendo costante l'ampiezza del segnale.

In FM l'informazione è contenuta nella **variazione di frequenza**, non nell'ampiezza. Quindi si può limitare brutalmente l'ampiezza senza perdere informazione, eliminando tutti i **disturbi in modulazione di ampiezza** (scariche elettriche, fulmini, amplificatori switching). Questo è il motivo per cui l'FM ha una riproduzione **particolarmente pulita** rispetto all'AM.

#### 🔹 Discriminatore a pendenza

Il discriminatore più semplice usa un **circuito risonante** sintonizzato non esattamente sulla frequenza intermedia, ma **leggermente più in alto** (es. a 10,8 MHz anziché 10,7 MHz):

- Quando la frequenza FM si sposta **verso la risonanza** → l'ampiezza in uscita **aumenta** (V₀ + ΔV)
- Quando la frequenza si sposta **lontano dalla risonanza** → l'ampiezza **diminuisce** (V₀ − ΔV)

In questo modo la **modulazione di frequenza viene convertita in modulazione di ampiezza**, che poi viene rivelata con un semplice diodo + condensatore.

⚠️ _Il discriminatore a pendenza non è perfetto: la curva del circuito risonante (campana) non è lineare, quindi la conversione FM→AM introduce distorsione. È un discriminatore economico ma di qualità limitata._

#### 🔹 Discriminatore Foster-Seeley

Il **discriminatore Foster-Seeley** — è un discriminatore molto più **lineare**, usato in tutte le radio FM di qualità, inclusa l'alta fedeltà. Non è richiesto conoscerne il funzionamento nel dettaglio, ma bisogna sapere che si chiama **discriminatore di Foster-Seeley** e che è il discriminatore standard per l'FM.

> Il termine **discriminatore** si usa esclusivamente per i ricevitori FM. Per l'AM si parla di **rivelatore**.

#### 🔹 Squelch (silenziatore)

Lo **squelch** — è un circuito presente nei ricevitori FM che silenzia l'audio in assenza di segnale utile. Si regola con una manopola:

- Si posiziona la soglia appena sopra il livello di fruscio/rumore di fondo
- Segnali sotto soglia (= rumore) → audio silenziato
- Segnali sopra soglia (= trasmissione in corso) → audio riprodotto ("apre lo squelch")

Funzione pratica: evita lo stress di ascoltare fruscio continuo quando nessuno trasmette.

---

### 11. 🎛️ AGC — Controllo Automatico di Guadagno (⏱ 92:13)

Il **Controllo Automatico di Guadagno** è uno dei circuiti più importanti di un ricevitore. Può essere indicato con diverse sigle:

- **CAG** — Controllo Automatico di Guadagno
- **CAV** — Controllo Automatico di Volume
- **AGC** — Automatic Gain Control

Tutte e tre le sigle possono comparire nelle domande d'esame.

#### 🔹 Funzionamento

Il ricevitore può avere in ingresso segnali da 1 µV fino a 10 mV (un fattore di 10.000). Senza AGC, si dovrebbe regolare continuamente il volume, rischiando "urlate" nell'altoparlante.

L'AGC è un **circuito di retroazione**: preleva un campione del segnale dall'uscita del rivelatore e, in base alla sua ampiezza, **regola il guadagno dell'amplificatore IF** (e talvolta anche del preamplificatore RF):

- Segnale in ingresso forte → guadagno IF basso
- Segnale in ingresso debole → guadagno IF alto

Risultato: l'audio in uscita rimane a livello pressoché costante.

#### 🔹 RF Gain

Oltre alla regolazione automatica, esiste una **regolazione manuale** tramite la manopola **RF Gain** che permette di controllare il guadagno complessivo della catena di amplificazione. Utile per:

- Tecniche di ascolto specifiche
- Ridurre il guadagno in presenza di segnali molto forti
- Evitare saturazione del ricevitore

#### 🔹 S-meter

La stessa tensione proporzionale all'intensità del segnale ricevuto viene usata per pilotare lo **S-meter** (misuratore di livello del segnale):

| Scala        | Significato                                               |
| ------------ | --------------------------------------------------------- |
| **S0 — S9**  | Ogni punto S = **6 dB** = **×4 in potenza**               |
| **S9**       | Corrisponde a **50 µV** in antenna (taratura di fabbrica) |
| **Oltre S9** | Scala logaritmica: S9+10, S9+20, S9+30, S9+40, S9+50 dB   |

La "S" dello S-meter deriva dal sistema **RST**: R = Readability (leggibilità), **S = Strength** (forza del segnale), T = Tone (tono, solo per telegrafia).

---

### 12. 🔀 Frequenza immagine (⏱ 102:32)

La **frequenza immagine** — è un problema intrinseco di tutti i ricevitori supereterodina. Nasce dal fatto che il mixer genera sia la somma sia la differenza dei segnali in ingresso.

#### 🔹 Esempio pratico

Ricevitore AM casalingo con IF a 455 kHz:

- Voglio ascoltare Rai 1 a **900 kHz**
- VFO a **1355 kHz**
- 1355 − 900 = **455 kHz** ✓ (segnale desiderato)
- Ma anche: 1810 − 1355 = **455 kHz** ⚠️ (frequenza immagine!)

Se esiste un segnale a 1810 kHz, viene convertito alla stessa IF e viene ascoltato **sovrapposto** al segnale desiderato.

#### 🔹 Regola fondamentale

> La frequenza immagine dista sempre **2 × IF** dal segnale ricevuto.

| IF del ricevitore | Distanza della freq. immagine |
| ----------------- | ----------------------------- |
| 455 kHz           | 910 kHz                       |
| 9 MHz             | 18 MHz                        |
| 10,7 MHz          | 21,4 MHz                      |

#### 🔹 Soluzioni

1. **Circuiti selettivi prima del mixer**: filtri che lasciano passare la frequenza desiderata e bloccano la frequenza immagine
2. **IF alta**: più è alta la IF, più la frequenza immagine è lontana e più è facile filtrarla
3. **Doppia conversione**: permette di avere una prima IF molto alta (40-70 MHz) per eccellente reiezione dell'immagine, e una seconda IF bassa (9 MHz) dove è facile realizzare filtri stretti

---

### 13. ⚠️ Problemi dei ricevitori (⏱ 112:03)

I ricevitori supereterodina possono soffrire di tre problemi principali:

#### 🔹 Bloccaggio

Il **bloccaggio** — si verifica quando un segnale molto forte (anche una portante) vicino alla frequenza che si sta ascoltando **silenzia il ricevitore**. Il segnale forte varia il punto di lavoro dei transistor del preamplificatore, causando una perdita di sensibilità. L'effetto è che il ricevitore sembra "ammutolirsi".

#### 🔹 Modulazione incrociata

La **modulazione incrociata** — avviene quando la modulazione di un segnale forte si **trasferisce su un segnale debole**. Si ascolta il segnale debole con una doppia modulazione (es. giornale radio + musica sovrapposta). Il segnale interferente è così forte da creare un processo di modulazione di ampiezza negli stadi del ricevitore.

#### 🔹 Intermodulazione

L'**intermodulazione** — è il problema più comune e grave. Quando segnali in ingresso forti portano gli amplificatori del ricevitore in **regime non lineare**, tutti i segnali presenti in banda vengono "mescolati" generando una grande quantità di segnali spuri, armoniche e prodotti di intermodulazione.

A differenza del trasmettitore (dove i segnali da mescolare sono pochi — la propria voce), nel ricevitore i segnali sono **molti** (tutti i canali attivi in banda). Nei casi limite, l'intermodulazione può saturare l'intera banda rendendo impossibile l'uso del ricevitore.

**Esempio tipico**: la banda dei **40 m** (7 MHz) con stazioni di broadcasting (radiodiffusione a 100 kW) subito sopra e sotto la banda RadioAmatoriale, che con propagazione favorevole arrivano fortissime e mandano in intermodulazione i ricevitori meno robusti.

---

### 14. 📊 Sensibilità e rapporto segnale/rumore (⏱ 117:42)

La **sensibilità** è la minima tensione in ingresso che produce un segnale d'uscita distinguibile dal rumore. Si esprime normalmente così:

> **0,5 µV per 10 dB di rapporto segnale/rumore (S/N)**

Significa che con 0,5 µV in antenna, il segnale ha una potenza 10 volte superiore a quella del rumore (10 dB = ×10 in potenza).

Un collegamento si fa non perché il segnale è forte, ma perché il **rapporto S/N è favorevole**.

#### 🔹 Influenza della larghezza di banda

La larghezza di banda del ricevitore è come una "finestra aperta": più è larga, più rumore entra. Di conseguenza:

| Modo    | Filtro  | Sensibilità                             |
| ------- | ------- | --------------------------------------- |
| **CW**  | 500 Hz  | **Migliore** (finestrella strettissima) |
| **SSB** | 2,5 kHz | Buona                                   |
| **AM**  | 5-6 kHz | Discreta                                |
| **FM**  | 10 kHz  | **Peggiore** (finestra spalancata)      |

Per questo motivo molti radioamatori continuano a usare la telegrafia: in CW si fanno **collegamenti più distanti con meno potenza** perché i ricevitori sono intrinsecamente più sensibili.

La sensibilità dipende anche dal **rumore dei primi stadi** del ricevitore (preamplificatore). Usare transistor e FET molto silenziosi ai primi stadi è fondamentale per tenere basso il livello di rumore intrinseco.

---

### 15. 🔧 Filtro notch (⏱ 125:18)

Il **filtro notch** — lavora in media frequenza, subito dopo il filtro principale, nell'ambito della banda passante del ricevitore. Serve per eliminare un singolo segnale interferente (es. una portante disturbante) all'interno del canale che si sta ascoltando.

---

## 🔗 Concept Map (testuale)

- Ricevitore supereterodina → utilizza → conversione di frequenza
- Oscillatore locale (VFO) → determina → frequenza ricevuta
- Mixer/convertitore → genera → frequenza intermedia (IF)
- Filtro IF → realizza → selettività del ricevitore
- IF fissa → richiede → conversione di frequenza tramite mixer
- Amplificatore IF → fornisce → il grosso del guadagno
- BFO → permette → rivelazione CW e SSB tramite battimento
- BFO + rivelatore a prodotto → genera → tono audio (CW) o voce (SSB)
- Diodo + condensatore → rivela → modulazione di ampiezza (AM)
- Limitatore → elimina → disturbi AM nel ricevitore FM
- Discriminatore → rivela → modulazione di frequenza (FM)
- Foster-Seeley → è tipo di → discriminatore (lineare, FM)
- AGC → mantiene costante → livello audio in uscita
- AGC → pilota → S-meter
- Frequenza immagine → è problema di → supereterodina
- Frequenza immagine → dista → 2 × IF dal segnale ricevuto
- IF alta → migliora → reiezione frequenza immagine
- Segnali forti in ingresso → causano → intermodulazione nel ricevitore
- Larghezza di banda filtro → influisce su → sensibilità (banda stretta = più sensibile)

---

## 📝 Key Takeaways

1. Il **ricevitore supereterodina** converte il segnale ricevuto a una frequenza intermedia fissa tramite un mixer e un oscillatore locale variabile; la manopola di sintonia varia la frequenza dell'oscillatore locale.

2. La **frequenza intermedia (IF)** è una frequenza fissa tipica: 455 kHz, 9 MHz, 10,7 MHz. A questa frequenza vengono realizzati il filtro principale e la catena di amplificazione.

3. La **doppia conversione** usa una prima IF alta (per reiezione dell'immagine) e una seconda IF bassa (per filtri economici e performanti).

4. Per la **telegrafia (CW)**: filtro 500 Hz, rivelatore a prodotto + BFO a IF + 700 Hz → tono audio a 700 Hz.

5. Per l'**SSB**: filtro 2,5 kHz, rivelatore a prodotto + BFO con due quarzi commutabili (USB/LSB). Si usa un solo filtro + 2 quarzi anziché 2 filtri separati per ragioni di costo.

6. Per l'**AM**: filtro 5-6 kHz, rivelatore a diodo + condensatore (stile radio a galena).

7. Per l'**FM**: filtro 10 kHz, IF = 10,7 MHz, **limitatore** (taglia picchi di ampiezza per eliminare disturbi AM), discriminatore (a pendenza o Foster-Seeley), squelch (silenziatore).

8. L'**AGC** (CAG/CAV) regola automaticamente il guadagno dell'amplificatore IF per mantenere costante il livello audio in uscita. La stessa tensione pilota lo **S-meter**.

9. Nello **S-meter**: ogni punto S = 6 dB (×4 in potenza), S9 = 50 µV, oltre S9 scala in dB.

10. La **frequenza immagine** dista sempre 2 × IF dal segnale ricevuto; si contrasta con circuiti selettivi in ingresso, IF alta e doppia conversione.

11. I tre problemi principali del ricevitore sono: **bloccaggio** (silenziamento), **modulazione incrociata** (modulazione del forte sul debole), **intermodulazione** (il più grave — segnali forti portano amplificatori in regime non lineare, mescolando tutti i segnali in banda).

12. La **sensibilità** dipende dalla larghezza di banda del filtro e dal rumore dei primi stadi: CW è il modo più sensibile (500 Hz), FM il meno (10 kHz).

---

## ❓ Comprehension Questions

1. Perché, in un ricevitore supereterodina, la manopola di sintonia non agisce direttamente sul filtro ma sull'oscillatore locale? Quali problemi risolve questa architettura?

2. Se un ricevitore ha una frequenza intermedia di 9 MHz e si sta ascoltando la frequenza di 14,200 MHz, quale sarà la frequenza dell'oscillatore locale e quale sarà la frequenza immagine? Come si può ridurre il rischio di interferenza dalla frequenza immagine?

3. Spiega perché in un ricevitore SSB si usano due quarzi per il BFO anziché due filtri separati per USB e LSB. Quali sono i vantaggi economici di questa scelta?

4. In FM, perché il limitatore può tagliare i picchi di ampiezza senza perdere informazione utile? Quale tipo di disturbi viene eliminato e perché?

5. Chi dei due discriminatori FM (a pendenza e Foster-Seeley) è più lineare e perché? In quali applicazioni viene preferito ciascuno?

6. Un ricevitore in CW con filtro a 500 Hz è più sensibile di uno FM con filtro a 10 kHz. Spiega il motivo e le implicazioni pratiche per i collegamenti a lunga distanza.

7. Descrivi il funzionamento dell'AGC: da dove preleva il segnale di controllo, su quali stadi agisce, e perché è essenziale in un ricevitore radioamatoriale.

8. Qual è la differenza tra bloccaggio, modulazione incrociata e intermodulazione nel ricevitore? Quale di questi è il problema più comune e perché?

9. In un ricevitore a doppia conversione con prima IF a 70 MHz e seconda IF a 9 MHz, spiega i vantaggi di ciascuna scelta di frequenza e perché la doppia conversione è necessaria.

10. Perché lo S-meter non misura direttamente la potenza del segnale ma sfrutta la tensione dell'AGC? Come è organizzata la sua scala?

---

## 📚 Glossary

- **AGC (Automatic Gain Control)** — Controllo automatico di guadagno; circuito di retroazione che mantiene costante il livello dell'audio in uscita regolando il guadagno degli amplificatori IF
- **Amplificatore BF** — Amplificatore di bassa frequenza; amplifica il segnale audio per pilotare l'altoparlante
- **Amplificatore IF** — Amplificatore a frequenza intermedia; fornisce il grosso del guadagno nel ricevitore, lavora a frequenza fissa
- **Amplificatore RF** — Amplificatore a radiofrequenza; primo stadio del ricevitore, detto anche preamplificatore
- **Attenuatore** — Dispositivo che riduce il livello del segnale in ingresso per evitare la saturazione del ricevitore
- **BFO (Beat Frequency Oscillator)** — Oscillatore di battimento; genera un segnale leggermente spostato rispetto alla IF per produrre un tono audio (CW) o rigenerare la portante (SSB)
- **Bloccaggio** — Fenomeno in cui un segnale forte silenzia il ricevitore variando il punto di lavoro dei transistor
- **CAG / CAV** — Sigle italiane per Controllo Automatico di Guadagno / Volume; equivalente dell'AGC
- **Conversione di frequenza** — Processo per cui un segnale viene traslato in frequenza tramite un mixer
- **Discriminatore** — Rivelatore specifico per FM; converte variazioni di frequenza in variazioni di ampiezza
- **Discriminatore a pendenza** — Discriminatore FM semplice basato su un circuito risonante disaccordato; non lineare
- **Discriminatore Foster-Seeley** — Discriminatore FM ad alta linearità, usato nelle radio FM di qualità
- **Doppia conversione** — Architettura che usa due stadi di conversione: prima IF alta, seconda IF bassa
- **Eterodinaggio** — Processo di battimento tra due segnali per generare frequenze somma e differenza
- **Frequenza immagine** — Frequenza spuria che produce la stessa IF del segnale desiderato, distante 2×IF
- **Frequenza intermedia (IF)** — Frequenza fissa a cui il segnale ricevuto viene convertito nel ricevitore supereterodina
- **Intermodulazione (nel ricevitore)** — Mescolamento di segnali in ingresso forti causato dalla perdita di linearità degli amplificatori; il problema più grave dei ricevitori
- **Limitatore** — Amplificatore in saturazione usato nei ricevitori FM per eliminare variazioni di ampiezza e disturbi AM
- **Modulazione incrociata** — Fenomeno in cui la modulazione di un segnale forte si trasferisce su un segnale debole nel ricevitore
- **Oscillatore locale** — Oscillatore a frequenza variabile (VFO) o fisso che alimenta il mixer nel ricevitore supereterodina
- **Pitch** — Regolazione della frequenza del tono del BFO nei ricevitori CW
- **Preamplificatore** — Altro nome dell'amplificatore RF; primo stadio di amplificazione del ricevitore
- **RF Gain** — Controllo manuale del guadagno a radiofrequenza della catena di ricezione
- **Radio a galena** — Ricevitore AM primitivo che usava un cristallo di galena come rivelatore
- **Rapporto segnale/rumore (S/N)** — Rapporto tra la potenza del segnale utile e la potenza del rumore; determina la qualità della ricezione
- **Rivelatore** — Circuito che estrae il segnale audio dalla portante modulata
- **Rivelatore a prodotto** — Rivelatore basato su un mixer, usato per CW e SSB, che fa battere il segnale IF con il BFO
- **S-meter** — Strumento che indica la forza del segnale ricevuto; scala S0-S9 poi dB sopra S9
- **Selettività** — Capacità del ricevitore di isolare il segnale desiderato dai canali adiacenti
- **Sensibilità** — Minima tensione in ingresso che produce un segnale d'uscita distinguibile dal rumore
- **Squelch** — Silenziatore; circuito nei ricevitori FM che blocca l'audio quando non c'è segnale utile
- **Stabilità** — Capacità del ricevitore di mantenere costante la frequenza sintonizzata
- **Supereterodina** — Architettura di ricevitore a conversione di frequenza, con filtro a frequenza fissa e oscillatore locale variabile

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo
- 🎙️ **Moderatore**: Fabrizio

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione**          | 15                                                                                                                                                                                                                                                                                                                            |
| **Data**             | 18 giugno 2025                                                                                                                                                                                                                                                                                                                |
| **Durata**           | ~2 ore e 7 minuti                                                                                                                                                                                                                                                                                                             |
| **Numero argomenti** | 15                                                                                                                                                                                                                                                                                                                            |
| **Parole chiave**    | Ricevitore, supereterodina, conversione di frequenza, frequenza intermedia, IF, oscillatore locale, VFO, BFO, rivelatore a prodotto, discriminatore, Foster-Seeley, limitatore, squelch, AGC, S-meter, frequenza immagine, doppia conversione, sensibilità, selettività, intermodulazione, bloccaggio, modulazione incrociata |
