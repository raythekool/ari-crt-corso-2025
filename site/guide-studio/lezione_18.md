---
layout: default
---

# 📘 Lezione 18 - Interferenze e EMC

## 📌 Overview

- **Materia**: Propagazione delle onde radio
- **Tempo di studio stimato**: 2 ore e 30 minuti
- **Prerequisiti**: Concetti base di elettromagnetismo, nozioni sullo spettro elettromagnetico, unità di misura (frequenza, lunghezza d'onda, potenza in dB)
- **Obiettivi di apprendimento**:
  - Comprendere la natura del campo elettromagnetico e le sue proprietà fondamentali
  - Conoscere i quattro meccanismi di propagazione delle onde radio
  - Capire la struttura della ionosfera e il ruolo dei suoi strati nella propagazione HF
  - Padroneggiare i concetti di frequenza critica, MUF, LUF e FOT
  - Comprendere l'influenza del ciclo solare sulla propagazione
  - Conoscere i meccanismi avanzati: riflessioni multiple, duct mode, chordal mode
  - Comprendere il ruolo dell'attenuazione nelle riflessioni a terra e la differenza tra percorsi su mare e su terra

---

## 📖 Core Content

### 1. 🔍 Introduzione e contesto storico (⏱ 00:00–12:00)

La lezione si apre con una breve correzione del quiz della lezione precedente (Lezione 16 — Strumenti di misura), poi il nuovo docente Paolo si presenta e annuncia che terrà quattro lezioni: la prima sulla **propagazione**, la seconda sulle **linee di trasmissione** e le ultime due sulle **antenne**.

Paolo introduce l'argomento della propagazione partendo dalla storia delle telecomunicazioni radio:

- **1873 — James Clerk Maxwell** pubblica le equazioni che dimostrano che campo elettrico e campo magnetico sono concatenati e formano un **campo elettromagnetico** capace di propagarsi nello spazio. Maxwell teorizza che la luce stessa è un'onda elettromagnetica.
- **1901 — Guglielmo Marconi** realizza il primo collegamento radiotelegrafico transoceanico tra Poldhu (Cornovaglia) e San Giovanni di Terranova (Canada), dimostrando che le onde radio possono seguire la curvatura terrestre.
- **1923 — Schnell e Delois** realizzano il primo **QSO transoceanico in onde corte** (circa 3 MHz, 103 m di lunghezza d'onda), dimostrando che anche con potenze modeste le onde corte permettono comunicazioni a grande distanza.

> Il docente sottolinea come la scoperta delle onde corte sia stata fondamentale per i radioamatori e per le comunicazioni a lunga distanza con potenze ridotte.

---

### 2. 📡 Il campo elettromagnetico (⏱ 12:00–20:00)

Il **campo elettromagnetico** è costituito da due componenti inscindibili:

- **Campo elettrico (E)** — misurato in Volt/metro (V/m)
- **Campo magnetico (H)** — misurato in Ampere/metro (A/m)

I due campi sono **perpendicolari** tra loro e **perpendicolari alla direzione di propagazione**. Si sostengono a vicenda: la variazione di uno genera l'altro, permettendo all'onda di propagarsi indefinitamente nello spazio.

**Impedenza dello spazio libero** — Il rapporto tra il campo elettrico e il campo magnetico nel vuoto è una costante fondamentale:

$$Z_0 = \frac{E}{H} = 377 \, \Omega$$

> ⚠️ **Domanda d'esame!** L'impedenza dello spazio libero è pari a **377 Ω**. Questo valore è una costante fisica e compare frequentemente nelle domande d'esame.

**Velocità di propagazione** — Nel vuoto, le onde elettromagnetiche si propagano alla velocità della luce:

$$c = 300.000 \, \text{km/s} = 3 \times 10^8 \, \text{m/s}$$

In mezzi diversi dal vuoto, la velocità di propagazione diminuisce in funzione delle caratteristiche dielettriche del mezzo.

---

### 3. 📐 Polarizzazione (⏱ 20:00–25:00)

La **polarizzazione** di un'onda elettromagnetica è definita dal **piano del campo elettrico** rispetto al suolo:

- **Polarizzazione verticale** — il campo elettrico è perpendicolare al suolo (tipica delle antenne verticali)
- **Polarizzazione orizzontale** — il campo elettrico è parallelo al suolo (tipica dei dipoli orizzontali)

> ⚠️ **Domanda d'esame!** La polarizzazione è determinata dall'orientamento del campo **elettrico**, non del campo magnetico.

Per ottimizzare la ricezione, l'antenna ricevente dovrebbe avere la stessa polarizzazione dell'onda trasmessa. Un disallineamento di polarizzazione causa una significativa perdita di segnale.

---

### 4. 📊 Spettro elettromagnetico e lunghezza d'onda (⏱ 25:00–32:00)

Le **onde radio** occupano la porzione dello spettro elettromagnetico compresa tra **3 kHz e 300 GHz**. La suddivisione in bande segue una nomenclatura standardizzata:

| Sigla | Nome              | Frequenza     | Lunghezza d'onda |
| ----- | ----------------- | ------------- | ---------------- |
| VLF   | Very Low Freq.    | 3–30 kHz      | 100–10 km        |
| LF    | Low Frequency     | 30–300 kHz    | 10–1 km          |
| MF    | Medium Frequency  | 300 kHz–3 MHz | 1 km–100 m       |
| HF    | High Frequency    | 3–30 MHz      | 100–10 m         |
| VHF   | Very High Freq.   | 30–300 MHz    | 10–1 m           |
| UHF   | Ultra High Freq.  | 300 MHz–3 GHz | 1 m–10 cm        |
| SHF   | Super High Freq.  | 3–30 GHz      | 10–1 cm          |
| EHF   | Extremely High F. | 30–300 GHz    | 1 cm–1 mm        |

La **lunghezza d'onda** (λ) è lo spazio percorso dall'onda in un'oscillazione completa ed è legata alla frequenza dalla relazione:

$$\lambda = \frac{300}{f_{(\text{MHz})}} \quad [\text{metri}]$$

oppure in forma più generale:

$$\lambda = \frac{c}{f}$$

dove $c$ è la velocità della luce e $f$ la frequenza in Hz.

**Esempio**: la banda dei 40 m corrisponde a $f = 300/40 = 7{,}5$ MHz (approssimativamente i 7 MHz della banda amatoriale).

---

### 5. 📉 Attenuazione del segnale (⏱ 32:00–37:00)

L'**attenuazione** di un segnale radio in spazio libero aumenta con la distanza e con la frequenza. La relazione fondamentale è:

$$\text{Attenuazione} \propto d^2 \times f^2$$

Ciò significa che:

- **Raddoppiando la distanza**, l'attenuazione aumenta di **4 volte** (6 dB)
- **Raddoppiando la frequenza**, l'attenuazione aumenta di **4 volte** (6 dB)

> ⚠️ **Domanda d'esame!** L'attenuazione in spazio libero è proporzionale al quadrato della distanza e al quadrato della frequenza.

Questo spiega perché le frequenze più basse (HF) sono preferite per comunicazioni a lunga distanza, mentre le frequenze più alte (UHF, SHF) sono utilizzate per comunicazioni a breve raggio o con antenne ad alto guadagno.

---

### 6. 🌐 I quattro tipi di propagazione (⏱ 37:00–50:00)

Esistono quattro modalità principali di propagazione delle onde radio:

#### 🔹 1. Propagazione in spazio libero (portata ottica)

Si verifica quando trasmettitore e ricevitore sono in **visibilità diretta** (line of sight). Tipica delle frequenze VHF e superiori. La portata è limitata dalla curvatura terrestre e dall'altezza delle antenne. Utilizzata nelle comunicazioni satellitari e nei ponti radio.

#### 🔹 2. Propagazione per onda di terra

L'onda si propaga seguendo la superficie terrestre, "aggrappandosi" al suolo grazie alla sua conducibilità. È efficace solo alle **frequenze molto basse** (VLF, LF, parte delle MF). La **polarizzazione verticale** è fortemente preferita perché il campo elettrico verticale interagisce meglio con il suolo conduttivo. L'attenuazione dipende dalla conducibilità del terreno: il mare salato è il miglior conduttore, il terreno asciutto e roccioso il peggiore.

#### 🔹 3. Propagazione troposferica

Sfrutta i fenomeni di **rifrazione** e **diffusione** nella troposfera (0–15 km di altitudine). La troposfera contiene il 90% dei gas atmosferici ed è un mezzo neutro (non ionizzato). Le variazioni di temperatura, pressione e umidità creano gradienti dell'indice di rifrazione che curvano i raggi radio oltre l'orizzonte ottico.

- **Frequenze tipiche**: VHF e UHF
- **Portata massima**: circa 800–1000 km (in condizioni favorevoli)
- **Scatter troposferico (tropo-scatter)**: tecnica utilizzata dalla NATO e dall'Enel (collegamento Toscana–Sardegna a 470 MHz con parabole da 11 m e 150 W di potenza trasmessa) per comunicazioni oltre l'orizzonte sfruttando la diffusione nella troposfera

#### 🔹 4. Propagazione ionosferica

Sfrutta la **riflessione e rifrazione** delle onde radio da parte degli strati ionizzati della ionosfera (80–400 km). È il meccanismo fondamentale per le comunicazioni a lunga distanza in **onde corte (HF)**. Le caratteristiche di questo tipo di propagazione dipendono fortemente dallo stato della ionosfera, che a sua volta è influenzata dall'attività solare.

---

### 7. 🌍 L'atmosfera terrestre e la ionosfera (⏱ 50:00–58:00)

#### 🔹 La troposfera

Si estende dal suolo fino a circa **15 km** di altitudine. Contiene il 90% della massa gassosa dell'atmosfera. È un **mezzo neutro** (non ionizzato) e causa fenomeni di rifrazione sulle onde radio a causa dei gradienti di temperatura e umidità.

#### 🔹 La ionosfera

Si estende da circa **80 km a 400 km** di altitudine. È costituita da **plasma ionosferico**: gas rarefatto le cui molecole sono ionizzate dalla radiazione solare (raggi UV, raggi X, raggi gamma). Il livello di ionizzazione varia con l'altitudine, l'ora del giorno, la stagione e il ciclo solare.

La ionosfera è suddivisa in **strati** con caratteristiche diverse:

| Strato | Altitudine | Caratteristiche principali                                                                                                                                                                                                                                             |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **D**  | 60–90 km   | Solo diurno (scompare dopo il tramonto). Causa **assorbimento** delle frequenze sotto 5–6 MHz. Effetto **dannoso** per la propagazione HF.                                                                                                                             |
| **E**  | 100–140 km | Variabile giorno/notte. Decadimento più graduale rispetto a D. Può contribuire alla propagazione.                                                                                                                                                                      |
| **F**  | 150–400 km | Strato principale per la propagazione HF. Sempre presente. Di **giorno** si divide in **F1** (più basso, meno ionizzato) e **F2** (più alto, massima ionizzazione). Di **notte** si ricombina in un unico strato **F** a quota più alta ma con ionizzazione inferiore. |

> Lo **strato D** è particolarmente importante da ricordare: è presente solo di giorno e causa assorbimento, non riflessione. Per questo le bande basse HF (sotto i 5–6 MHz) funzionano meglio di notte, quando lo strato D scompare.

---

### 8. 📈 Frequenza critica, zona d'ombra, MUF, LUF e FOT (⏱ 58:00–74:00)

#### 🔹 Frequenza critica (f₀)

La **frequenza critica** è la massima frequenza che viene riflessa dalla ionosfera con incidenza verticale (perpendicolare). I suoi valori variano enormemente:

- **Minimo solare, notte**: circa **2 MHz**
- **Massimo solare, giorno**: fino a **12–13 MHz**

La f₀ è monitorata costantemente dall'**INGV di Roma** con ionosonde che effettuano misurazioni ogni 15 minuti.

**Tre comportamenti fondamentali a seconda della frequenza**:

1. **f < f₀** → **Riflessione totale**: l'onda viene completamente riflessa dalla ionosfera. Si forma una cavità tra suolo e ionosfera (fenomeno sfruttato dalle frequenze VLF/LF).
2. **f > f₀** → **Rifrazione angolo-dipendente**: l'onda penetra nella ionosfera ma viene piegata e può tornare a terra. L'angolo di incidenza determina se l'onda viene riflessa o attraversa lo strato. Possibilità di **zona d'ombra**.
3. **f >> f₀** → **Trasparenza**: l'onda attraversa la ionosfera senza essere deviata. Condizione sfruttata per le comunicazioni satellitari.

#### 🔹 Zona d'ombra

Quando $f > f_0$, i fasci con angolo di incidenza troppo verticale "bucano" la ionosfera e si perdono nello spazio. Solo i fasci con angoli più radenti vengono rifratti a sufficienza per tornare a terra. Questo crea una **zona d'ombra**: un'area circolare intorno al trasmettitore che non può essere raggiunta né dall'onda di terra (troppo lontana) né dall'onda ionosferica (troppo vicina). La zona d'ombra si estende tipicamente da alcune decine fino a centinaia di chilometri.

#### 🔹 MUF — Maximum Usable Frequency

La **MUF** è la massima frequenza utilizzabile per un collegamento ionosferico su un determinato percorso. Approssimativamente:

$$\text{MUF} \approx 3 \times f_0$$

La MUF varia con la posizione geografica, l'ora del giorno e lo stato del ciclo solare. Per realizzare un collegamento, la MUF deve essere superiore alla frequenza operativa **lungo tutta la tratta**.

#### 🔹 LUF — Lowest Usable Frequency

La **LUF** è la minima frequenza utilizzabile, determinata principalmente dall'**assorbimento dello strato D**. Le frequenze troppo basse subiscono un'attenuazione eccessiva attraversando gli strati bassi della ionosfera.

#### 🔹 FOT — Frequenza Ottimale di Traffico

La **FOT** è la frequenza operativa consigliata per ottenere le migliori condizioni di collegamento:

$$\text{FOT} = 80\text{–}90\% \times \text{MUF}$$

> ⚠️ **Domanda d'esame!** La FOT è l'80–90% della MUF e rappresenta la frequenza ottimale di lavoro per garantire collegamenti affidabili.

---

### 9. 🌏 Distanza massima e riflessioni multiple (⏱ 74:50–78:32)

#### 🔹 Distanza massima per singolo salto

Con una singola riflessione ionosferica, la distanza massima raggiungibile è di circa **3.500 km**. Questo valore si calcola per semplice geometria considerando:

- Raggio terrestre: **6.370 km**
- Altezza dello strato riflettente: circa **250 km**
- Angolo minimo: fascio radente all'orizzonte

#### 🔹 Riflessioni multiple

Per superare i 3.500 km sono necessarie **riflessioni multiple** (multi-hop). Il segnale riflesso dalla ionosfera torna a terra, viene riflesso dal suolo e risale verso la ionosfera, compiendo più "salti". L'attenuazione è molto elevata perché ad ogni salto il segnale attraversa gli strati bassi (specialmente lo strato D).

#### 🔹 Duct mode (modalità condotto)

In condizioni particolari, il segnale rimbalza nello spazio compreso tra lo **strato F e lo strato E**, senza toccare terra. Questo comporta un'**attenuazione molto inferiore** perché si evitano sia le riflessioni a terra sia l'attraversamento dello strato D.

#### 🔹 Chordal mode (modalità cordale)

Il fascio, una volta raggiunto lo strato F, prosegue **pressoché orizzontalmente** all'interno dello strato ionizzato fino a raggiungere terra a grande distanza. Anche questa modalità presenta attenuazione ridotta.

> Sia il duct mode che il chordal mode sono **rari** e si verificano in condizioni particolari, ma producono segnali molto più forti rispetto alle riflessioni multiple tradizionali. La **scarsissima prevedibilità** della propagazione ionosferica deriva proprio dalla molteplicità di questi meccanismi.

---

### 10. ☀️ Il ciclo solare e l'influenza sulla propagazione (⏱ 79:20–96:17)

Il livello di ionizzazione della ionosfera è direttamente dipendente dall'**attività solare**. Esistono quattro cicli fondamentali:

#### 🔹 1. Ciclo undecennale delle macchie solari

Il ciclo più importante, con durata di circa **11 anni**. Il **SSN** (Sunspot Number — numero di macchie solari) varia da zero a oltre 200–300.

**Dati storici dei cicli solari**:

- **1958**: record storico con SSN = 350
- Cicli successivi: 1969–70, 1980, 1991, 2003–2004, 2014 (ciclo 24, pessimo)
- **Ciclo 25 (attuale)**: massimo raggiunto a cavallo tra fine 2024 e inizio 2025, SSN intorno a 150 (buono). La discesa è appena iniziata; ancora circa 2 anni di buone condizioni.

Il **SFI** (Solar Flux Intensity — intensità del flusso solare) è un altro indicatore correlato al numero di macchie solari.

Oltre al ciclo regolare, esistono fenomeni improvvisi (**SID** — Sudden Ionospheric Disturbances): **brillamenti**, **buchi coronali**, **eruzioni solari**, **tempeste magnetiche**. Questi sono più frequenti nei periodi di massima attività.

#### 🔹 2. Ciclo di rotazione solare (~27 giorni)

Il Sole ruota sul proprio asse in circa 25 giorni, ma dal punto di vista di un osservatore terrestre la stessa zona della superficie solare riappare dopo circa **27 giorni** (perché la Terra nel frattempo si è spostata sulla propria orbita).

Poiché le macchie non sono distribuite uniformemente, il livello di radiazione varia con ciclicità di 27 giorni. **Regola pratica**: se si verificano ottime condizioni di propagazione, è probabile che si ripresentino dopo circa **26–27 giorni**.

#### 🔹 3. Ciclo orbitale terrestre (stagionale)

L'inclinazione dell'asse terrestre di **23,5°** rispetto al piano dell'eclittica causa l'alternanza delle stagioni. Questo influenza:

- Le ore di insolazione (e quindi di ionizzazione)
- L'angolo di incidenza delle radiazioni solari
- Il comportamento prevalentemente degli strati bassi (D, E) ma anche di F

#### 🔹 4. Ciclo di rotazione terrestre (giorno/notte)

L'alternanza giorno/notte ha effetti molto importanti sugli strati ionosferici:

- **Strato D**: scompare **pressoché immediatamente** dopo il tramonto, ricompare all'alba
- **Strato E**: decade **gradualmente** dopo il tramonto (tempi molto più lunghi)
- **Strato F**: di notte si ricombina in uno strato unico a quota maggiore, con ionizzazione inferiore ma comunque significativa

#### 🔹 Effetti pratici sulla propagazione

**Durante massimo solare** (come ora): la differenza tra giorno e notte per le bande alte HF (sopra i 40 m) è ridotta. Le bande rimangono aperte anche di notte.

**Durante minimo solare**: le bande sopra i 40 m si aprono solo nelle ore centrali del giorno. Di notte la MUF scende sotto i 10 MHz, rendendo inutilizzabili le bande alte.

**Grey line (linea grigia)** — Il periodo immediatamente dopo il tramonto offre condizioni eccellenti: lo strato D scompare rapidamente (eliminando l'assorbimento sulle bande basse) mentre lo strato F mantiene ancora un'elevata ionizzazione. I valori di MUF restano elevati per diverse ore dopo il tramonto.

---

### 11. 🌊 Attenuazione nelle riflessioni a terra (⏱ Q&A)

Nelle riflessioni multiple, ogni "rimbalzo" a terra introduce un'attenuazione che dipende fortemente dalla natura del suolo:

| Superficie        | Attenuazione per salto |
| ----------------- | ---------------------- |
| **Acqua di mare** | < 1 dB (media 0,5 dB)  |
| **Terreno**       | 2–5 dB                 |
| **Neve/ghiaccio** | fino a 5 dB (peggiore) |

Questo spiega importanti fenomeni pratici:

- **Il Sud America è il DX più forte dall'Italia**: il percorso è quasi interamente su mare (Tirreno → Mediterraneo → Atlantico). Anche con 5–6 salti, l'attenuazione totale è solo 5–6 dB.
- **Il Giappone è più debole**: alla stessa distanza (~18.000 km), il percorso attraversa la steppa asiatica e la Siberia (spesso innevata). Con 4–5 salti su terra, l'attenuazione è 15–20 dB.
- **Stazioni vicino al mare**: hanno un vantaggio significativo. Marconi scelse Coltano proprio perché era una palude salmastra, ottima per la conducibilità del terreno.

---

### 12. 🔄 Via corta e via lunga (⏱ Q&A)

Per raggiungere una destinazione agli antipodi, esistono due percorsi possibili:

- **Via corta (short path)**: il percorso più breve sulla superficie terrestre
- **Via lunga (long path)**: il percorso nella direzione opposta, più lungo ma talvolta preferibile

La scelta dipende dalla MUF lungo l'intero percorso. A volte la via lunga funziona quando la via corta non lo consente, perché le condizioni di ionizzazione sono favorevoli su quel percorso alternativo.

#### Esempio classico: Italia → Australia/Nuova Zelanda

- **Via corta**: quasi tutto su terra → attenuazione elevata (15–20 dB da riflessioni a terra)
- **Via lunga**: passa sopra Caraibi/Atlantico → quasi tutto su mare → attenuazione molto inferiore

Nonostante la distanza maggiore (e uno o due salti in più), la via lunga può produrre segnali più forti grazie alla minore attenuazione nelle riflessioni a terra.

---

### 13. 📡 Propagazione transequatoriale — TEP (⏱ Q&A)

Il **TEP** (Trans-Equatorial Propagation) è un fenomeno di propagazione che permette collegamenti a lunghissima distanza attraverso l'equatore.

#### 🔹 Meccanismo

L'**Anomalia di Ionizzazione Equatoriale (EIA)** crea due "creste" di altissima ionizzazione a circa **10–12°** a nord e sud dell'**equatore magnetico**. Il segnale sfrutta un **chordal mode**: sale nella prima cresta, prosegue orizzontalmente nello strato ionizzato, e scende attraverso la seconda cresta.

#### 🔹 Condizioni necessarie

- Le due creste devono avere livelli di ionizzazione **simmetrici**, condizione che si verifica soprattutto durante gli **equinozi** (settembre e marzo)
- Il percorso deve essere orientato **lungo i meridiani** (direzione nord-sud), perché le creste sono allineate parallelamente all'equatore
- Finestra temporale ristretta: tra le **20:00 e le 21:00** ora locale
- Il picco si presenta poco dopo mezzogiorno locale (12:00–15:00) in termini di massima ionizzazione

#### 🔹 Frequenze e prestazioni

- **TEP tradizionale (HF, 50 MHz)**: angolo utilizzabile più ampio, si riesce a lavorare anche in leggera diagonale
- **TEP in VHF (144 MHz)**: angolo molto stretto, solo lungo i meridiani. Test recenti Italia–Namibia hanno permesso collegamenti di circa **7.000 km in 2 m** utilizzando modi digitali
- **TEP in UHF (430 MHz)**: test in corso tra Giappone e Australia

> Il fenomeno è stato scoperto e studiato approfonditamente grazie alle anomalie riscontrate nei sistemi **GPS** nelle aree equatoriali.

---

### 14. 🔻 Angolo di radiazione e propagazione (⏱ Q&A)

Anticipando i temi delle lezioni sulle antenne, il docente sottolinea che l'**angolo di radiazione** dell'antenna è un fattore cruciale per la propagazione a lunga distanza:

- L'angolo di radiazione è determinato per l'**80% dalla posizione** in cui si installa l'antenna, non dal tipo di antenna
- Un **angolo basso** significa meno salti, quindi meno attenuazione
- Quando la propagazione cala, si perdono prima gli **angoli alti** (corrispondenti vicini). Gli angoli bassi sono gli ultimi a chiudersi

> Questo argomento sarà trattato in dettaglio nelle lezioni sulle antenne.

---

### 15. 🔬 Effetti della ionizzazione sulle distanze (⏱ Q&A)

Un concetto apparentemente controintuitivo: quando la ionizzazione è **più elevata** (ad esempio d'estate), la zona d'ombra si **riduce** e si possono collegare corrispondenti **più vicini**. Quando la ionizzazione cala, si perdono prima i corrispondenti più vicini (quelli raggiunti con angoli alti), non quelli lontani (raggiunti con angoli bassi).

Questo spiega perché d'estate la propagazione sugli 11 m e 10 m appare "più corta": la maggiore ionizzazione consente riflessione con angoli di incidenza più ripidi, riducendo la distanza minima raggiungibile.

> ⚠️ Questo comportamento è una tendenza statistica, non una regola assoluta, perché la radiazione solare non è costante.

---

## 🔗 Concept Map (testuale)

- **Campo elettrico E** + **Campo magnetico H** → formano → **Campo elettromagnetico**
- **Campo EM** → si propaga alla → **Velocità della luce (300.000 km/s)**
- **Impedenza spazio libero (377 Ω)** = rapporto tra → E e H
- **Polarizzazione** → determinata da → piano del campo **E** rispetto al suolo
- **Lunghezza d'onda λ** → inversamente proporzionale a → **frequenza f**
- **Attenuazione** → proporzionale a → **d² × f²**
- **Propagazione ionosferica** → dipende da → **strati D, E, F** della ionosfera
- **Strato D** → causa → **assorbimento** (presente solo di giorno)
- **Strato F** → responsabile della → **riflessione/rifrazione** HF principale
- **Frequenza critica f₀** → determina il → **comportamento della ionosfera** (riflessione/rifrazione/trasparenza)
- **MUF** ≈ 3 × f₀ → limita → massima frequenza utilizzabile
- **FOT** = 80–90% MUF → è la → frequenza ottimale operativa
- **LUF** → limitata da → assorbimento dello strato D
- **Ciclo solare 11 anni** → influenza → livello di ionizzazione → influenza → MUF
- **Rotazione solare 27 giorni** → causa → periodicità nelle condizioni di propagazione
- **Riflessioni multiple** → necessarie per → distanze > 3.500 km
- **Duct mode / Chordal mode** → sono casi speciali di → propagazione ionosferica con minore attenuazione
- **Attenuazione riflessione a terra** → dipende da → tipo di superficie (mare < terra < ghiaccio)
- **TEP** → sfrutta → Anomalia Ionizzazione Equatoriale → allineata → lungo i meridiani

---

## 📝 Key Takeaways

1. **L'impedenza dello spazio libero è 377 Ω**, costante fisica data dal rapporto E/H nel vuoto. Concetto ricorrente nelle domande d'esame.

2. **La polarizzazione è definita dal piano del campo elettrico**: verticale se E è perpendicolare al suolo, orizzontale se parallelo.

3. **La lunghezza d'onda si calcola con λ = 300/f(MHz)**, formula fondamentale per tutti i calcoli in radiofrequenza.

4. **L'attenuazione in spazio libero è proporzionale a d² × f²**: raddoppiando distanza o frequenza, l'attenuazione quadruplica (6 dB).

5. **La ionosfera ha tre strati principali**: D (solo diurno, causa assorbimento), E (variabile), F (strato principale per la propagazione HF, sempre presente).

6. **La FOT (80–90% della MUF) è la frequenza ottimale per i collegamenti**, non la MUF stessa, per garantire un margine di sicurezza.

7. **La distanza massima con un singolo salto ionosferico è circa 3.500 km**; distanze maggiori richiedono riflessioni multiple, duct mode o chordal mode.

8. **Il ciclo solare di 11 anni è il fattore più importante per la propagazione HF**: in massimo solare le bande alte sono aperte anche di notte, in minimo solare solo durante il giorno.

9. **Le riflessioni sul mare attenuano 0,5 dB per salto contro 2–5 dB su terra**: questo spiega perché il Sud America dall'Italia è il DX più forte a parità di distanza.

10. **La grey line (subito dopo il tramonto) offre condizioni eccellenti**: strato D scompare (meno assorbimento) mentre strato F mantiene alta ionizzazione.

---

## ❓ Comprehension Questions

1. Perché l'impedenza dello spazio libero è una costante e quale relazione lega campo E e campo H? In che modo questo concetto si applica al dimensionamento delle antenne?

2. Spiegare perché lo strato D è considerato "dannoso" per la propagazione HF e come la sua presenza/assenza influenza la scelta delle bande operative nelle diverse ore del giorno.

3. Se la frequenza critica f₀ è di 8 MHz in un dato momento, quale sarebbe approssimativamente la MUF e la FOT? Quale banda amatoriale risulterebbe ottimale?

4. Descrivere il meccanismo del duct mode e spiegare perché produce segnali più forti rispetto alle riflessioni multiple tradizionali.

5. Come si spiega che il Sud America sia costantemente il "miglior DX" dall'Italia, nonostante non sia la destinazione più vicina? Utilizzare i dati sull'attenuazione per salto nella risposta.

6. Perché durante i periodi di elevata ionizzazione la distanza minima raggiungibile (skip distance) si riduce? Questo fenomeno è controintuitivo: spiegare il meccanismo geometrico sottostante.

7. Quali sono i quattro cicli che influenzano la ionizzazione terrestre e quale tra questi è il più rilevante per la pianificazione dei collegamenti HF a lunga distanza?

8. Spiegare le condizioni necessarie perché si verifichi la propagazione transequatoriale (TEP) e il motivo per cui funziona prevalentemente lungo i meridiani.

9. Un radioamatore nota che 27 giorni dopo un'ottima apertura in 10 m, le condizioni sono nuovamente favorevoli. Quale ciclo solare spiega questo fenomeno?

10. Confrontare i vantaggi e svantaggi della via corta e della via lunga per un collegamento Italia–Nuova Zelanda, considerando sia la MUF sia l'attenuazione per riflessione a terra.

---

## 📚 Glossary

- **Attenuazione** — Riduzione della potenza del segnale durante la propagazione, espressa in dB. In spazio libero è proporzionale a d² × f².
- **Campo elettromagnetico** — Campo composto da una componente elettrica (E) e una magnetica (H) perpendicolari tra loro, capace di propagarsi nello spazio.
- **Chordal mode** — Modalità di propagazione in cui il segnale percorre orizzontalmente l'interno di uno strato ionizzato senza toccare terra.
- **Ciclo solare undecennale** — Ciclo di circa 11 anni dell'attività solare, caratterizzato dalla variazione del numero di macchie solari (SSN).
- **Duct mode (modalità condotto)** — Propagazione in cui il segnale rimbalza tra strato F e strato E senza riflessione a terra, con attenuazione ridotta.
- **EIA (Equatorial Ionization Anomaly)** — Anomalia di ionizzazione equatoriale che crea creste di alta ionizzazione a ±10–12° dall'equatore magnetico.
- **f₀ (frequenza critica)** — Massima frequenza riflessa dalla ionosfera con incidenza verticale. Varia da 2 MHz (notte, minimo solare) a 12–13 MHz (giorno, massimo solare).
- **FOT (Frequenza Ottimale di Traffico)** — Frequenza operativa consigliata, pari all'80–90% della MUF.
- **Grey line (linea grigia)** — Linea di passaggio tra giorno e notte sulla superficie terrestre; offre condizioni di propagazione eccellenti.
- **Impedenza dello spazio libero** — Rapporto E/H nel vuoto, pari a 377 Ω.
- **Ionosfera** — Regione dell'atmosfera (80–400 km) costituita da plasma ionizzato dalla radiazione solare, suddivisa in strati D, E, F.
- **LUF (Lowest Usable Frequency)** — Minima frequenza utilizzabile per un collegamento ionosferico, limitata dall'assorbimento dello strato D.
- **Lunghezza d'onda (λ)** — Distanza percorsa dall'onda in un'oscillazione completa: λ = 300/f(MHz) in metri.
- **MUF (Maximum Usable Frequency)** — Massima frequenza utilizzabile per un collegamento ionosferico su un dato percorso. Approssimativamente 3 × f₀.
- **Onda di terra** — Propagazione in cui l'onda segue la superficie terrestre; efficace solo a frequenze molto basse.
- **Plasma ionosferico** — Gas rarefatto le cui molecole sono ionizzate dalla radiazione solare.
- **Polarizzazione** — Orientamento del piano del campo elettrico rispetto al suolo (verticale o orizzontale).
- **Propagazione troposferica** — Propagazione che sfrutta rifrazione e diffusione nella troposfera (0–15 km); tipica di VHF/UHF.
- **SFI (Solar Flux Intensity)** — Intensità del flusso solare, indicatore dell'attività solare correlato al numero di macchie.
- **SID (Sudden Ionospheric Disturbance)** — Disturbo ionosferico improvviso causato da brillamenti o eruzioni solari.
- **SSN (Sunspot Number)** — Numero di macchie solari, indicatore principale del ciclo solare undecennale.
- **Strato D** — Strato ionosferico (60–90 km) presente solo di giorno, causa assorbimento delle frequenze sotto 5–6 MHz.
- **Strato E** — Strato ionosferico (100–140 km) variabile tra giorno e notte, con decadimento graduale.
- **Strato F (F1, F2)** — Strato ionosferico principale (150–400 km) per la propagazione HF. Di giorno si divide in F1 e F2.
- **TEP (Trans-Equatorial Propagation)** — Propagazione a lunga distanza attraverso l'equatore, sfruttando le creste di ionizzazione equatoriale.
- **Tropo-scatter** — Tecnica di comunicazione oltre l'orizzonte che sfrutta la diffusione del segnale nella troposfera.
- **Via corta / Via lunga (Short path / Long path)** — Percorsi alternativi per raggiungere una stessa destinazione seguendo rispettivamente il tragitto più breve o più lungo sulla superficie terrestre.
- **Zona d'ombra** — Area circolare intorno al trasmettitore non raggiungibile né dall'onda di terra né dall'onda ionosferica.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo (radioamatore dal 1977, 40 anni di esperienza professionale nel settore RF)
- 🎓 **Coordinatore**: Fabrizio (coordina la sessione, gestisce le domande)

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                                                                                                  |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Numero lezione**   | 18                                                                                                                                                                                                                                                                                                                      |
| **Data**             | 03/09/2025 (mercoledì)                                                                                                                                                                                                                                                                                                  |
| **Durata**           | ~2 ore e 28 minuti                                                                                                                                                                                                                                                                                                      |
| **Numero argomenti** | 15                                                                                                                                                                                                                                                                                                                      |
| **Parole chiave**    | propagazione, campo elettromagnetico, impedenza 377 Ω, polarizzazione, spettro EM, lunghezza d'onda, attenuazione, ionosfera, strato D, strato E, strato F, frequenza critica, MUF, LUF, FOT, zona d'ombra, ciclo solare, SSN, SFI, riflessioni multiple, duct mode, chordal mode, grey line, TEP, via corta, via lunga |
