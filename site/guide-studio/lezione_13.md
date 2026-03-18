---
layout: default
permalink: /guide-studio/lezione_13.html
---

# 📘 Lezione 13 - Antenne - Parte 1

## 📌 Overview

- **Materia**: Radiotecnica — Amplificatori, Oscillatori e Decibel
- **Tempo di studio stimato**: 90–110 minuti
- **Prerequisiti**: Conoscenza di transistor, FET, MOSFET, valvole termoioniche (Lezione 12); circuiti risonanti e quarzi (Lezione 06); diodi e alimentatori (Lezione 11)
- **Obiettivi di apprendimento**:
  - Distinguere amplificatori a bassa frequenza (BF) e ad alta frequenza (AF)
  - Comprendere guadagno, rendimento e le quattro classi di amplificazione (A, B, C, AB)
  - Capire il principio di funzionamento degli oscillatori (retroazione positiva)
  - Conoscere le tre tipologie di oscillatori: libero (VFO), a quarzo, ad aggancio di fase (PLL)
  - Padroneggiare l'uso pratico dei decibel con i "mattoncini" +3 dB e +10 dB
  - Comprendere la differenza tra dB (misura relativa) e dBm (misura assoluta)

---

## 📖 Core Content

### 1. 🔍 Correzione Quiz Lezione 12 (⏱ 00:02–18:00)

Paolo e Silvio IZ5DIY aprono la lezione con la correzione del quiz della settimana precedente, dedicato a transistor, FET e valvole termoioniche. I risultati sono generalmente buoni, con la maggior parte dei partecipanti tra l'80% e il 100%.

#### 🔹 Risposte Chiave e Chiarimenti

- **Transistor bipolare**: ha **2 giunzioni** (non 1 come il diodo). Il diodo ha una sola giunzione P-N, il transistor ne ha due (N-P-N o P-N-P).
- **FET**: l'impedenza di ingresso è **alta** perché è pilotato in tensione e non richiede corrente al gate.
- **Diodo Zener**: è un **diodo**, non un transistor. Lavora in polarizzazione inversa per stabilizzare la tensione.
- **Valvola termoionica**: necessita di **tensioni elevate** (centinaia di volt) per funzionare, a differenza dei transistor.
- **Impedenza d'ingresso di un amplificatore**: deve essere **alta** per non "caricare" lo stadio precedente, cioè per non assorbire troppa corrente dal circuito che lo alimenta.
- **Emettitore comune**: configurazione con impedenza d'ingresso **media** (non alta come il collettore comune).
- **Filamento** nelle valvole: ha il compito di **scaldare il catodo** (nel riscaldamento indiretto).
- **Tetrodo**: possiede **2 griglie** (griglia controllo + griglia schermo).
- **Pentodo**: la griglia soppressore serve a **sopprimere la corrente inversa** (emissione secondaria dall'anodo).
- **Griglia di controllo**: controlla il flusso di corrente tra catodo e anodo.
- **Pentodo**: ha **5 elettrodi** (catodo, griglia controllo, griglia schermo, griglia soppressore, anodo) + **2 terminali per il filamento** = **7 terminali** totali.

---

### 2. 📡 Amplificatori: Concetti Generali (⏱ 18:45–32:00)

Paolo introduce gli amplificatori ricordando che all'esame è richiesta la conoscenza a livello di **schema a blocchi** (scatolette nere), non a livello di singoli componenti. L'amplificatore è un dispositivo che riceve un segnale debole in ingresso e produce un segnale più forte in uscita.

#### 🔹 Amplificatori BF e AF

Esistono due grandi categorie di amplificatori, distinte per la banda di frequenza operativa:

**Amplificatore BF (Bassa Frequenza)** — amplificatore che opera nella banda audio (circa 20 Hz – 18.000 Hz). Non utilizza circuiti risonanti perché deve amplificare uniformemente tutte le frequenze della banda audio. Tipico impiego: stadi finali di ricevitori, impianti Hi-Fi.

**Amplificatore AF/RF (Alta Frequenza)** — amplificatore che opera a frequenze radio elevate. Utilizza **circuiti risonanti** in ingresso e/o in uscita per ottenere **selettività**, cioè per amplificare solo una banda stretta di frequenze centrata sulla frequenza di risonanza. La **curva di risposta** mostra un picco alla frequenza di risonanza e un'attenuazione via via maggiore allontanandosi da essa.

⚠️ La distinzione fondamentale: gli amplificatori BF amplificano un'ampia gamma di frequenze in modo uniforme, quelli AF amplificano selettivamente grazie ai circuiti risonanti.

#### 🔹 Fattore di Amplificazione o Guadagno

**Guadagno (o fattore di amplificazione)** — rapporto tra il segnale in uscita e il segnale in ingresso di un amplificatore. I termini "guadagno" e "fattore di amplificazione" sono sinonimi.

Il guadagno può essere espresso:

- **In potenza**: $G_P = \frac{P_{out}}{P_{in}}$
- **In tensione**: $G_V = \frac{V_{out}}{V_{in}}$

> Esempio: un amplificatore che con 1 W in ingresso produce 15 W in uscita ha un guadagno di 15 volte (in potenza).

Il guadagno viene spesso espresso in **decibel** (dB) come vedremo più avanti nella lezione.

#### 🔹 Rendimento

**Rendimento (η)** — rapporto percentuale tra la potenza utile in uscita e la potenza totale assorbita dall'alimentazione.

$$\eta = \frac{P_{uscita}}{P_{alimentazione}} \times 100\%$$

La differenza tra la potenza assorbita dall'alimentatore e la potenza effettivamente presente in uscita si trasforma in **calore**. Ecco perché gli amplificatori con rendimento basso necessitano di dissipatori (radiatori) o ventole per smaltire il calore.

> Esempio: se un amplificatore eroga 100 W in uscita e assorbe 200 W dall'alimentatore, il rendimento è 50%. I restanti 100 W vengono dissipati in calore — l'amplificatore "diventa una stufetta".

---

### 3. 📊 Classi di Amplificazione (⏱ 32:00–66:00)

Le classi di amplificazione definiscono per quale porzione del ciclo del segnale il dispositivo attivo conduce corrente. Si distinguono per la posizione del **punto di lavoro** (punto di polarizzazione) sulla curva caratteristica del dispositivo.

#### 🔹 Classe A

**Classe A** — classe di amplificazione in cui la corrente nel dispositivo scorre per **l'intero periodo** (360°) del segnale.

Il punto di lavoro è posizionato nella **zona lineare** della curva caratteristica, ben lontano sia dalla zona di saturazione che da quella di interdizione. Il segnale viene amplificato in modo **molto fedele**, con distorsione minima.

- **Angolo di conduzione**: 360° (intero ciclo)
- **Rendimento**: molto basso, tipicamente **5–20%**
- **Linearità**: eccellente, riproduzione molto fedele del segnale
- **Applicazioni**: amplificatori per piccoli segnali, ricevitori, apparecchiature Hi-Fi, amplificatori per cuffia
- **Svantaggio principale**: la maggior parte della potenza assorbita si trasforma in calore

> Paolo racconta che in Hi-Fi esistono splendidi amplificatori in classe A per cuffia (2-3 W), dove il basso rendimento non è un problema perché le potenze sono molto ridotte. Per potenze maggiori, il calore diventa critico.

#### 🔹 Classe B

**Classe B** — classe di amplificazione in cui la corrente nel dispositivo scorre solo per **metà periodo** (180°) del segnale.

Il punto di lavoro è posizionato vicino alla zona di **interdizione** (cut-off). Il dispositivo conduce solo durante un semiperiodo; durante l'altro semiperiodo è spento. Il segnale in uscita è una **mezza sinusoide** — fortemente distorto se usato singolarmente.

- **Angolo di conduzione**: 180° (mezzo ciclo)
- **Rendimento**: circa **60%**
- **Linearità**: segnale distorto (solo metà dell'onda)
- **Soluzione**: configurazione **push-pull** (o **controfase**)

**Push-pull (controfase)** — configurazione circuitale che utilizza **due dispositivi in classe B** complementari: uno amplifica la semionda positiva, l'altro la semionda negativa. I due segnali vengono poi ricombinati per ricostruire la **sinusoide completa**.

⚠️ **Distorsione di crossover** — nel punto di raccordo tra le due semionde amplificate dai due dispositivi si può verificare una piccola distorsione dovuta alla non perfetta giunzione dei due segnali. Questo è il principale svantaggio del push-pull in classe B.

#### 🔹 Classe C

**Classe C** — classe di amplificazione in cui la corrente scorre per **meno di metà periodo** (tipicamente 70°–80°).

Il dispositivo conduce solo per una piccola frazione del ciclo, amplificando solo i "picchi" del segnale. Il segnale in uscita è **molto distorto**.

- **Angolo di conduzione**: < 180° (tipicamente 70°–80°)
- **Rendimento**: **70–75%** (il più alto tra le classi tradizionali)
- **Linearità**: pessima — segnale molto distorto
- **Applicazioni**: **solo FM e CW (telegrafia)** dove non serve linearità in ampiezza
- **Funzionamento**: si utilizza un **circuito risonante (carico risonante)** in uscita che "rigenera" la sinusoide completa a partire dagli impulsi amplificati

> La classe C non può essere usata per SSB o AM perché queste modulazioni richiedono la conservazione delle variazioni di ampiezza.

#### 🔹 Classe AB

**Classe AB** — classe di amplificazione intermedia tra A e B, in cui la corrente scorre per **più di metà periodo** ma non per tutto il ciclo.

- **Angolo di conduzione**: circa **220°–240°**
- **Rendimento**: **50–60%**
- **Linearità**: buon compromesso, abbastanza fedele
- **Applicazioni**: **amplificatori finali dei trasmettitori** sia a valvole che a stato solido (MOSFET, LDMOS)

Paolo spiega che nei tipici amplificatori a MOSFET o LDMOS, il dispositivo viene polarizzato con una **corrente di riposo (bias)** pari a circa il **10–15%** della corrente massima di trasmissione. Ad esempio, se in trasmissione il MOSFET consuma 5 A, la corrente di bias sarà di 500–700 mA.

#### 🔹 Tabella Riassuntiva delle Classi

| Classe | Angolo di conduzione  | Fedeltà riproduzione       | Rendimento | Impiego tipico                       |
| ------ | --------------------- | -------------------------- | ---------- | ------------------------------------ |
| **A**  | 360° (intero periodo) | Molto fedele               | 5–20%      | Ricevitori, Hi-Fi, piccoli segnali   |
| **AB** | ~220°–240°            | Abbastanza fedele          | 50–60%     | Finali TX valvolari e a stato solido |
| **B**  | 180° (mezzo periodo)  | Lineare solo con push-pull | ~60%       | Push-pull, controfase                |
| **C**  | < 180° (~70°–80°)     | Non lineare                | 70–75%     | Solo FM e CW, con carico risonante   |

---

### 4. 📻 Oscillatori (⏱ 66:28–83:42)

L'oscillatore è un altro dei "blocchi funzionali" (scatolette nere) fondamentali, presente sia nei trasmettitori che nei ricevitori. Il suo compito è **generare un segnale** a una determinata frequenza.

#### 🔹 Principio di Funzionamento: la Retroazione

**Retroazione (feedback)** — meccanismo per cui una parte del segnale di uscita viene riportata all'ingresso dell'amplificatore.

Tutti gli oscillatori funzionano sul principio della **retroazione positiva**:

1. All'accensione, il dispositivo amplificatore (FET, transistor) raccoglie il **rumore intrinseco** presente in ingresso
2. Questo piccolo segnale di rumore viene **amplificato** e si ritrova in uscita
3. Una parte del segnale di uscita viene **riportata all'ingresso** tramite un circuito di retroazione
4. Il segnale ritorna all'ingresso leggermente più forte, viene riamplificato, torna in uscita ancora più forte…
5. Il processo continua finché non si raggiunge una **condizione di oscillazione stabile** con ampiezza costante

Per ottenere una **frequenza precisa**, nel percorso di retroazione si inserisce un **circuito risonante LC** o un **quarzo**, che fa sì che il meccanismo funzioni efficacemente solo alla frequenza di risonanza.

#### 🔹 Tre Tipologie di Oscillatori

##### Oscillatore Libero (VFO)

**VFO (Variable Frequency Oscillator)** — oscillatore a frequenza variabile, che utilizza un circuito LC (bobina + condensatore) nel percorso di retroazione.

- **Vantaggio**: la frequenza può essere variata modificando il condensatore variabile → utile per la sintonia
- **Svantaggio**: **stabilità limitata** — la frequenza può variare con la temperatura, le vibrazioni meccaniche e altri fattori
- **Esempio**: schema con FET dove il segnale dal gate viene amplificato, esce sul drain, e tramite un condensatore e una bobina (circuito LC) viene riportato al gate
- Se si progetta un circuito LC che risuona a 9 MHz, l'oscillatore genera un segnale di uscita a 9 MHz

##### Oscillatore a Quarzo

**Oscillatore a quarzo** — oscillatore che utilizza un cristallo di quarzo nel percorso di retroazione, al posto del circuito LC.

- **Vantaggio**: **stabilità altissima** — il quarzo ha un fattore di qualità Q di circa 10.000 (rispetto ai 100–150 di un circuito LC normale), quindi tiene l'oscillatore molto "fermo" sulla frequenza
- **Svantaggio**: opera a **frequenza fissa** (la frequenza del quarzo)
- **Armoniche**: è possibile far oscillare un quarzo non solo alla frequenza fondamentale, ma anche alle **armoniche dispari** (3ª, 5ª, 7ª armonica). Es.: da un quarzo a 9 MHz si possono generare 27 MHz (3ª armonica), 45 MHz (5ª armonica), ecc.

##### Oscillatore ad Aggancio di Fase (PLL)

**PLL (Phase Locked Loop)** — circuito oscillatore che combina la **variabilità** di un oscillatore libero con la **stabilità** di un riferimento a quarzo.

Il PLL è la tipologia usata nella quasi totalità dei ricetrasmettitori moderni. All'interno contiene **due oscillatori**:

1. **VCO (Voltage Controlled Oscillator)** — oscillatore controllato in tensione che genera il segnale di uscita. La frequenza è regolata tramite **diodi varicap** (condensatori variabili elettronici) al posto della manopola meccanica.
2. **Oscillatore di riferimento a quarzo** — fornisce la frequenza stabile di riferimento.

**Funzionamento del PLL**:

1. Il VCO genera il segnale alla frequenza desiderata
2. Il segnale di uscita viene prelevato e inviato a un **comparatore di fase**
3. Il comparatore confronta la fase del segnale del VCO con quella dell'oscillatore di riferimento
4. Se il VCO si allontana dalla frequenza corretta, il comparatore genera una **tensione di errore**
5. Questa tensione, dopo un **filtro passa-basso** (per ottenere una tensione continua priva di ondulazioni), va a modificare la polarizzazione dei varicap del VCO
6. I varicap correggono la frequenza del VCO → **anello di retroazione chiuso**

**Filtro passa-basso nel PLL**: serve a ottenere una tensione continua perfettamente piatta. Se il segnale di errore avesse un'ondulazione residua, questa si trasformerebbe in **modulazione di frequenza indesiderata** del VCO.

> Paolo usa l'espressione "botte piena e moglie ubriaca" per descrivere il PLL: si ottiene contemporaneamente la stabilità del quarzo e la variabilità in frequenza dell'oscillatore libero.

#### 🔹 Confronto tra le Tipologie

| Caratteristica  | VFO (Libero)               | Quarzo                   | PLL                         |
| --------------- | -------------------------- | ------------------------ | --------------------------- |
| **Frequenza**   | Variabile                  | Fissa                    | Variabile                   |
| **Stabilità**   | Bassa                      | Altissima                | Alta (agganciata al quarzo) |
| **Impiego**     | Sintonia vecchi ricevitori | Riferimenti di frequenza | Ricetrasmettitori moderni   |
| **Complessità** | Semplice                   | Semplice                 | Complesso                   |

---

### 5. 📈 I Decibel (dB) (⏱ 83:48–110:14)

L'ultimo argomento della lezione è il **decibel**, un'unità di misura fondamentale nell'elettronica e nella radiotecnica. Paolo lo introduce come un concetto che "sembra complicato ma in pratica è di una banalità estrema".

#### 🔹 Cos'è il Decibel

**Decibel (dB)** — unità di misura logaritmica usata per esprimere rapporti tra grandezze (potenze, tensioni). Il simbolo è **dB** (d minuscola, B maiuscola). Il nome significa "un decimo di Bell", dal cognome di Alexander Graham Bell.

Il decibel è usato ovunque in radiotecnica:

- **Guadagno delle antenne**: es. "antenna direzionale da 5 dB di guadagno"
- **Attenuazione dei cavi coassiali**: es. "1,2 dB di attenuazione ogni 10 m"
- **Guadagno degli amplificatori**: es. "amplificatore da 13 dB"
- **Scale S-meter dei ricevitori**: S1, S2, … S9, S9+10 dB, S9+20 dB, S9+30 dB

#### 🔹 Perché i Logaritmi

Paolo offre una parentesi storica: i **logaritmi** furono inventati nel 1600 per semplificare i calcoli. Prima delle calcolatrici, fare moltiplicazioni come 10.327 × 4.322 era un "bagno di sangue". Il logaritmo ha la proprietà fondamentale di **trasformare le moltiplicazioni in somme** e le **divisioni in sottrazioni**, rendendo i calcoli enormemente più semplici.

**Logaritmo in base 10** — il logaritmo in base 10 di un numero è l'esponente a cui va elevato 10 per ottenere quel numero:

- $\log_{10}(10) = 1$ perché $10^1 = 10$
- $\log_{10}(100) = 2$ perché $10^2 = 100$
- $\log_{10}(1000) = 3$ perché $10^3 = 1000$

La formula completa del guadagno in decibel è:

$$G_{dB} = 10 \cdot \log_{10}\left(\frac{P_{out}}{P_{in}}\right)$$

⚠️ Ai fini dell'esame **non è necessario** conoscere la formula matematica né saper calcolare logaritmi. Basta padroneggiare i "mattoncini" fondamentali.

#### 🔹 I Due Mattoncini Fondamentali

Per risolvere **tutti** i problemi d'esame servono solo **4 valori** da memorizzare (2 coppie):

| dB         | Rapporto in potenza | Significato                 |
| ---------- | ------------------- | --------------------------- |
| **+3 dB**  | ×2                  | Raddoppio della potenza     |
| **+10 dB** | ×10                 | Potenza moltiplicata per 10 |
| **−3 dB**  | ×0,5                | Dimezzamento della potenza  |
| **−10 dB** | ×0,1                | Potenza ridotta a un decimo |

Con questi mattoncini si costruiscono tutti gli altri valori:

- **+6 dB** = +3 +3 → ×2 × 2 = **×4**
- **+20 dB** = +10 +10 → ×10 × 10 = **×100**
- **+30 dB** = +10 +10 +10 → ×10 × 10 × 10 = **×1.000**
- **−6 dB** = −3 −3 → ×0,5 × 0,5 = **×0,25**
- **−20 dB** = −10 −10 → ×0,1 × 0,1 = **×0,01 (un centesimo)**
- **−30 dB** = −10 −10 −10 → **×0,001 (un millesimo)**

> **Regola pratica**: ogni +10 dB aggiunge uno zero (moltiplica per 10), ogni −10 dB toglie uno zero (divide per 10); +3 dB raddoppia, −3 dB dimezza.

#### 🔹 Il Segno del Decibel

- **dB positivo** (+dB) → si riferisce a un **guadagno** (amplificazione): il segnale in uscita è più forte di quello in ingresso
- **dB negativo** (−dB) → si riferisce a un'**attenuazione**: il segnale in uscita è più debole di quello in ingresso

#### 🔹 Amplificatori in Cascata: Somma dei dB

Quando più amplificatori (o attenuatori) sono collegati **in cascata** (in serie), il guadagno totale in dB è semplicemente la **somma** dei guadagni dei singoli stadi:

$$G_{totale} = G_1 + G_2 + G_3 + \ldots$$

> **Esempio 1**: Amplificatore 1 guadagna +10 dB, Amplificatore 2 guadagna +20 dB. Guadagno totale = 10 + 20 = **+30 dB**. Se entrano 1 W: dopo il primo stadio → 10 W; dopo il secondo stadio → 10 × 10 × 10 = 1.000 W.

> **Esempio 2**: 7 W in ingresso a un amplificatore da +30 dB. Risultato: 7 → 70 → 700 → 7.000 W.

#### 🔹 Esempio Pratico d'Esame: da 5 W a 100 W

Problema: un amplificatore di potenza deve fornire 100 W all'antenna a partire dai 5 W del trasmettitore. Quale guadagno in dB è necessario?

**Soluzione** usando i mattoncini:

1. 5 W → **+3 dB** (raddoppio) → 10 W
2. 10 W → **+10 dB** (×10) → 100 W
3. Guadagno totale: 3 + 10 = **13 dB**

Per raddoppiare ulteriormente a 200 W: basta aggiungere **+3 dB** → totale **16 dB**.

#### 🔹 Esempio con Catena di Trasmissione

Problema tipico d'esame: trasmettitore da 100 W, cavo coassiale che attenua −6 dB, antenna con guadagno +9 dB. Quale potenza viene effettivamente irradiata?

**Soluzione**:

1. Guadagno totale della catena: +9 dB (antenna) − 6 dB (cavo) = **+3 dB**
2. Potenza irradiata: 100 W × 2 = **200 W** effettivamente irradiati (ERP)

#### 🔹 Decibel come Misura Relativa vs Assoluta

Il decibel è per natura una **misura relativa**: esprime un rapporto tra due grandezze, non un livello assoluto. Dire "3 dB" non indica una potenza specifica, ma che un segnale è il doppio di un altro.

Per trasformare il dB in **misura assoluta** si usa un riferimento fisso.

**dBm (decibel riferiti al milliwatt)** — unità di misura assoluta in cui **0 dBm = 1 mW** per definizione.

| dBm     | Potenza corrispondente |
| ------- | ---------------------- |
| −10 dBm | 0,1 mW                 |
| −3 dBm  | 0,5 mW                 |
| 0 dBm   | 1 mW (definizione)     |
| +3 dBm  | 2 mW                   |
| +10 dBm | 10 mW                  |
| +13 dBm | 20 mW                  |
| +20 dBm | 100 mW                 |
| +30 dBm | 1.000 mW = 1 W         |
| +50 dBm | 100 W                  |

> Esempio: +13 dBm = +10 +3 → 1 mW × 10 = 10 mW, poi × 2 = 20 mW. Oppure: +3 +10 → 1 mW × 2 = 2 mW, poi × 10 = 20 mW. Il risultato è identico.

I dBm sono molto usati nella strumentazione radio, ad esempio nei **VNA** (Vector Network Analyzer) e nelle misure sulle antenne.

---

### 6. 💬 Discussioni e Aneddoti Pratici

#### 🔹 Amplificatori Hi-Fi e Classi

Un partecipante chiede perché in alta fedeltà vengano spesso pubblicizzati amplificatori "classe AB" quando la classe A sarebbe superiore per fedeltà. Paolo conferma che per l'alta fedeltà la classe A è effettivamente migliore, ma il suo basso rendimento ne limita l'uso a potenze ridotte (es. amplificatori per cuffia da 2-3 W). Il marketing di amplificatori "classe AB" va preso con cautela.

#### 🔹 MOSFET in Classe AB e Corrente di Bias

Marco Morelli conferma di possedere un amplificatore a MOSFET che lavora in classe AB. Paolo spiega che la maggior parte degli amplificatori MOSFET e LDMOS lavorano effettivamente in AB con una corrente di riposo (bias) del 10-15% della corrente massima. Marco racconta un aneddoto: spolverando la radio ha accidentalmente aumentato il bias al 70-80%, rischiando di bruciare l'amplificatore.

#### 🔹 Transistor Falsi e Riparazione Amplificatori

Un partecipante racconta la sua esperienza con transistor 2N3055 contraffatti acquistati online: misurati col tester risultavano buoni, ma una volta installati andavano in cortocircuito e prendevano fuoco. Aprendo i contenitori, si scopriva che all'interno c'era una microgiunzione da mezzo ampere invece del dispositivo originale. Dopo tre tentativi falliti, ha rinunciato alla riparazione dell'amplificatore NAD.

---

## 🔗 Concept Map (testuale)

- **Amplificatore** → si classifica in → **BF** (senza circuiti risonanti) o **AF** (con circuiti risonanti)
- **Guadagno** → è il rapporto → $P_{out}/P_{in}$
- **Rendimento** → è il rapporto → $P_{out}/P_{alimentazione}$ × 100%
- **Potenza non convertita** → si trasforma in → **calore**
- **Classe A** → ha come caratteristica → **massima linearità, minimo rendimento**
- **Classe B** → necessita di → **push-pull** per ricostruire il segnale completo
- **Classe C** → richiede → **circuito risonante** in uscita + solo per **FM/CW**
- **Classe AB** → rappresenta un compromesso tra → **Classe A** e **Classe B**
- **Oscillatore** → funziona tramite → **retroazione positiva**
- **Retroazione** → utilizza → **circuito LC** o **quarzo** per determinare la frequenza
- **VFO** → è → variabile ma poco stabile
- **Oscillatore a quarzo** → è → stabile ma a frequenza fissa
- **PLL** → combina → variabilità del VFO + stabilità del quarzo
- **PLL** → contiene → **VCO** + **oscillatore riferimento a quarzo** + **comparatore di fase**
- **VCO** → utilizza → **diodi varicap** per variare la frequenza
- **Decibel** → trasforma → moltiplicazioni in somme
- **+3 dB** → corrisponde a → raddoppio della potenza
- **+10 dB** → corrisponde a → potenza × 10
- **dB** → è misura → relativa
- **dBm** → è misura → assoluta (riferita a 1 mW)

---

## 📝 Key Takeaways

1. Gli amplificatori si dividono in **BF** (bassa frequenza, senza circuiti risonanti, banda larga) e **AF** (alta frequenza, con circuiti risonanti, selettivi su una frequenza specifica).

2. Il **guadagno** è il rapporto tra potenza di uscita e potenza di ingresso; il **rendimento** è il rapporto tra potenza di uscita e potenza totale assorbita dall'alimentatore — la differenza diventa calore.

3. Esistono quattro classi di amplificazione: **A** (360°, lineare, rendimento 5–20%), **B** (180°, push-pull necessario, rendimento ~60%), **C** (< 180°, solo FM/CW con carico risonante, rendimento 70–75%), **AB** (220–240°, compromesso, rendimento 50–60%).

4. La classe C non può essere usata con modulazioni che richiedono linearità d'ampiezza (AM, SSB) perché distorce fortemente il segnale — va bene solo per FM e CW che non portano informazione nell'ampiezza.

5. Tutti gli oscillatori funzionano per **retroazione positiva**: parte del segnale d'uscita viene riportata all'ingresso e riamplificata fino a raggiungere un'oscillazione stabile.

6. Le tre tipologie di oscillatori sono: **VFO** (variabile, poco stabile), **a quarzo** (stabile, frequenza fissa, armoniche possibili), **PLL** (variabile e stabile grazie all'aggancio del VCO a un riferimento a quarzo).

7. Il **PLL** è usato nella quasi totalità dei ricetrasmettitori moderni e combina un VCO controllato da varicap con un oscillatore di riferimento a quarzo tramite un comparatore di fase.

8. Il **decibel** è un'unità logaritmica che trasforma le moltiplicazioni in somme: **+3 dB = ×2**, **+10 dB = ×10**, **−3 dB = ×0,5**, **−10 dB = ×0,1**. Con questi quattro valori si risolvono tutti i problemi d'esame.

9. Il guadagno totale di una catena (amplificatori, cavi, antenne) si calcola **sommando i dB** dei singoli stadi: se un trasmettitore eroga 100 W, il cavo attenua −6 dB e l'antenna guadagna +9 dB, il guadagno netto è +3 dB → 200 W irradiati.

10. Il **dBm** è la versione assoluta del decibel, riferita a 1 mW: **0 dBm = 1 mW**. Si usa nella strumentazione (es. VNA) e segue le stesse regole dei mattoncini +3/+10.

---

## ❓ Comprehension Questions

1. Perché un amplificatore BF non utilizza circuiti risonanti, mentre un amplificatore AF sì? Quale implicazione ha questa differenza sulla curva di risposta in frequenza?

2. Un amplificatore assorbe 300 W dall'alimentatore ed eroga 120 W in uscita. Calcola il rendimento e spiega dove finisce l'energia rimanente.

3. Perché la classe C non può essere utilizzata per amplificare segnali SSB o AM? Quale tipo di modulazione è compatibile e perché?

4. Spiega il funzionamento del push-pull in classe B: perché sono necessari due dispositivi e qual è il principale difetto di questa configurazione?

5. Descrivi il meccanismo di retroazione positiva che sta alla base del funzionamento degli oscillatori. Cosa succederebbe se mancasse il circuito risonante?

6. Confronta i tre tipi di oscillatori (VFO, quarzo, PLL) in termini di stabilità e variabilità di frequenza. Perché il PLL ha quasi completamente sostituito gli altri nei ricetrasmettitori moderni?

7. Un trasmettitore eroga 10 W. Il segnale passa attraverso un amplificatore da +10 dB, poi un cavo che attenua −3 dB, e infine un'antenna con guadagno +6 dB. Qual è la potenza effettivamente irradiata?

8. Spiega la differenza concettuale tra dB (misura relativa) e dBm (misura assoluta). Perché 0 dBm corrisponde esattamente a 1 mW?

9. Nel PLL, qual è il ruolo del filtro passa-basso posto tra il comparatore di fase e il VCO? Cosa accadrebbe senza di esso?

10. Perché all'esame le domande sui decibel sono risolvibili con soli quattro valori (+3, +10, −3, −10 dB) senza bisogno di calcolatrice?

---

## 📚 Glossary

- **Amplificatore AF (Alta Frequenza)** — amplificatore con circuiti risonanti per amplificare selettivamente una banda stretta di frequenze radio
- **Amplificatore BF (Bassa Frequenza)** — amplificatore senza circuiti risonanti per amplificare uniformemente la banda audio (20–18.000 Hz)
- **Angolo di conduzione** — porzione del ciclo del segnale durante la quale il dispositivo attivo conduce corrente, espressa in gradi
- **Armoniche** — frequenze multiple intere della frequenza fondamentale (2ª, 3ª, 5ª, 7ª…)
- **Bias (corrente di)** — corrente di polarizzazione a riposo del dispositivo attivo, tipicamente 10–15% della corrente massima in classe AB
- **Carico risonante** — circuito LC in uscita a un amplificatore in classe C che rigenera la sinusoide a partire da impulsi
- **Classe A** — classe di amplificazione con conduzione per l'intero ciclo (360°), massima linearità, rendimento 5–20%
- **Classe AB** — classe intermedia con conduzione per circa 220°–240°, buon compromesso linearità/rendimento (50–60%)
- **Classe B** — classe di amplificazione con conduzione per mezzo ciclo (180°), rendimento ~60%, richiede push-pull
- **Classe C** — classe di amplificazione con conduzione per meno di mezzo ciclo, rendimento 70–75%, solo FM/CW
- **Comparatore di fase** — circuito che confronta la fase di due segnali e produce una tensione di errore proporzionale alla differenza
- **Controfase** — termine italiano per push-pull, configurazione con due dispositivi che amplificano semionde alternate
- **Corrente di riposo** — corrente che scorre nel dispositivo in assenza di segnale; sinonimo di corrente di bias
- **Curva di risposta** — grafico che mostra il guadagno dell'amplificatore in funzione della frequenza
- **dB (decibel)** — unità di misura logaritmica relativa per rapporti di potenza; +3 dB = ×2, +10 dB = ×10
- **dBm** — unità di misura assoluta di potenza riferita a 1 milliwatt; 0 dBm = 1 mW
- **Distorsione di crossover** — distorsione nel punto di raccordo tra le due semionde in un amplificatore push-pull
- **Fattore di amplificazione** — sinonimo di guadagno; rapporto tra segnale in uscita e segnale in ingresso
- **Guadagno** — rapporto tra potenza (o tensione) in uscita e in ingresso di un amplificatore
- **Logaritmo** — operatore matematico che trasforma moltiplicazioni in somme; il logaritmo in base 10 di N è l'esponente a cui va elevato 10 per ottenere N
- **Oscillatore** — circuito che genera un segnale a frequenza determinata tramite retroazione positiva
- **PLL (Phase Locked Loop)** — oscillatore ad aggancio di fase che combina un VCO con un oscillatore di riferimento a quarzo tramite comparatore di fase
- **Punto di lavoro** — condizione operativa statica (in assenza di segnale) del dispositivo attivo sulla sua curva caratteristica
- **Push-pull** — configurazione con due dispositivi complementari che amplificano semionde alternate per ricostruire il segnale completo
- **Rendimento (η)** — rapporto percentuale tra potenza utile in uscita e potenza totale assorbita dall'alimentazione
- **Retroazione (feedback)** — meccanismo per cui parte del segnale di uscita viene riportata all'ingresso
- **S-meter** — strumento del ricevitore che indica l'intensità del segnale ricevuto, con scala in unità S e dB
- **Varicap (diodo)** — diodo a capacità variabile usato nei VCO per variare la frequenza tramite tensione di polarizzazione
- **VCO (Voltage Controlled Oscillator)** — oscillatore la cui frequenza è controllata da una tensione applicata ai diodi varicap
- **VFO (Variable Frequency Oscillator)** — oscillatore libero a frequenza variabile con circuito LC
- **VNA (Vector Network Analyzer)** — strumento di misura che analizza le reti elettriche misurando parametri in dBm

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo (radiotecnica — amplificatori, oscillatori, decibel)
- 👨‍🏫 **Relatore**: Silvio IZ5DIY (correzione quiz lezione 12)

---

## 📅 Informazioni Lezione

| Campo                  | Valore                                                                                                                                                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione**            | 13                                                                                                                                                                                                                            |
| **Data**               | 04 giugno 2025                                                                                                                                                                                                                |
| **Durata**             | circa 2 ore                                                                                                                                                                                                                   |
| **Argomenti trattati** | 4 (correzione quiz, amplificatori e classi, oscillatori, decibel)                                                                                                                                                             |
| **Parole chiave**      | amplificatore, guadagno, rendimento, classe A, classe B, push-pull, classe C, classe AB, oscillatore, retroazione, VFO, quarzo, PLL, VCO, varicap, comparatore di fase, decibel, dB, dBm, logaritmo, mattoncini, attenuazione |
