# 📘 Lezione 12 - Corso Radioamatori

## 📌 Overview

- **Materia**: Radiotecnica — Transistor, FET, MOSFET e Valvole Termoioniche
- **Tempo di studio stimato**: 2 ore e 30 minuti
- **Prerequisiti**: Semiconduttori, giunzione P-N, diodi e loro tipologie, alimentatori lineari (Lezione 11), concetti di corrente e tensione, legge di Ohm e di Kirchhoff (Lezioni 02-03)
- **Obiettivi di apprendimento**:
  - Comprendere il funzionamento del transistor bipolare (NPN e PNP) come amplificatore di corrente
  - Conoscere i tre terminali del transistor (base, collettore, emettitore) e il fattore di amplificazione beta
  - Distinguere le tre configurazioni di amplificazione: emettitore comune, base comune, collettore comune
  - Comprendere il funzionamento dei transistor a effetto di campo (FET) e MOSFET
  - Conoscere le valvole termoioniche: diodo, triodo, tetrodo e pentodo
  - Saper confrontare i dispositivi a stato solido con le valvole termoioniche

---

## 📖 Core Content

### 1. 🔍 Correzione Quiz Lezione 11 (⏱ 00:02)

La lezione inizia con la correzione del quiz della settimana precedente sugli argomenti dei diodi e degli alimentatori. I risultati sono molto buoni, con quasi tutti vicini al 100%. Le domande più critiche sono state la L e la P.

Punti chiave dalle risposte:

- **Caduta di tensione del diodo al silicio**: 0,7 V. Questa tensione si genera intrinsecamente nella giunzione P-N del silicio e si ritrova ai capi del diodo quando conduce.
- **Diodo Zener**: è uno stabilizzatore di tensione (centrata da tutti).
- **Diodo hot carrier (Schottky)**: ha la giunzione fra metallo e semiconduttore (non P-N).
- **Diodo Varicap**: è un diodo a capacità variabile.
- **LED**: è un diodo che emette luce.
- **Condensatori in parallelo all'uscita del raddrizzatore**: servono per il filtraggio, non per alzare o abbassare la tensione.
- **Trasformatore in alimentatore lineare**: serve ad abbassare la tensione in ingresso.
- **Raddrizzatore**: è formato da diodi (non transistor, che servono per la stabilizzazione).
- **Filtri di alimentazione**: usano condensatori e induttanze.
- **Raddrizzatore a singola semionda**: conduce per 180° di ciascun ciclo (metà sinusoide). A doppia semionda: 360°.
- **Condensatori nei filtri alimentatori**: si usano **elettrolitici** perché servono grandi capacità (10.000 µF e oltre).
- **Ponte di diodi**: è un raddrizzatore ad onda intera (doppia semionda), tensione pulsante a 100 Hz.
- **Rapporto spire trasformatore**: un rapporto di 10 significa 220 V → 22 V.

---

### 2. 📡 Il Transistor Bipolare (⏱ 10:07)

#### 🔹 Struttura del Transistor

Il **transistor** è un dispositivo **semiconduttore a tre strati drogati**, a differenza del diodo che ne ha due. Esistono due tipi fondamentali:

- **NPN**: strato N - strato P - strato N
- **PNP**: strato P - strato N - strato P

I tre terminali del transistor sono:

- **Base** (B): lo strato centrale, **molto sottile** — è il terminale di controllo
- **Collettore** (C): uno degli strati esterni — terminale di uscita
- **Emettitore** (E): l'altro strato esterno — identificato dal simbolo con la freccia

> **Regola per il simbolo**: nel transistor **NPN** la freccia dell'emettitore punta verso l'**esterno**; nel **PNP** la freccia punta verso l'**interno**. Il simbolo può essere ruotato a seconda dello schema elettrico.

Nel transistor ci sono **due giunzioni**:

- Giunzione **base-collettore**
- Giunzione **base-emettitore**

È come se fossero due diodi messi in serie con polarità opposte.

#### 🔹 Funzionamento del Transistor

Quando il transistor non è polarizzato (base non alimentata), si formano **due zone di svuotamento** alle giunzioni, esattamente come nel diodo. Queste zone impediscono il passaggio di corrente: il transistor si comporta come un **interruttore aperto**.

Quando si applica una corrente alla **base** (polarizzazione diretta della giunzione base-emettitore), le cariche elettriche iniettate nella base sottilissima **abbattono le zone di svuotamento**, permettendo il flusso di una corrente **molto maggiore** fra emettitore e collettore. La base, essendo molto sottile, richiede pochissima corrente per controllare un flusso molto più grande.

> **Il transistor è un amplificatore di corrente**: una piccola corrente di base produce una corrente di collettore 100-200 volte maggiore.

#### 🔹 Distribuzione delle Correnti (Legge di Kirchhoff)

Per la legge dei nodi di Kirchhoff, la corrente che entra nel transistor deve uscire:

$$I_E = I_B + I_C$$

Dove:

- $I_E$ = corrente di emettitore
- $I_B$ = corrente di base (molto piccola)
- $I_C$ = corrente di collettore (grande)

Poiché $I_B \ll I_C$, le correnti di emettitore e collettore sono praticamente uguali:

$$I_E \approx I_C$$

> **Esempio**: se $I_E = 100$ mA e $I_B = 1$ mA, allora $I_C = 99$ mA. Dal punto di vista ingegneristico, 99 ≈ 100.

#### 🔹 Il Fattore di Amplificazione Beta (β)

Il **guadagno** o **fattore di amplificazione** del transistor è il rapporto tra la corrente di collettore e la corrente di base:

$$\beta = H_{FE} = \frac{I_C}{I_B}$$

> **Esempio**: se $I_B = 1$ mA e $I_C = 150$ mA, allora $\beta = 150$. Il transistor amplifica 150 volte la corrente di base.

La sigla tecnica è **$H_{FE}$**, ma comunemente si parla di **beta** del transistor. Non sono richiesti calcoli numerici all'esame, ma si deve conoscere la definizione.

---

### 3. ⚡ Il Transistor come Amplificatore (⏱ 31:30)

#### 🔹 Schema di Amplificazione Base

Per usare il transistor come amplificatore servono:

1. **Polarizzazione di base**: una tensione/corrente continua che porta il transistor in conduzione (supera la soglia di 0,7 V della giunzione base-emettitore)
2. **Segnale di ingresso**: sovrapposto alla polarizzazione di base (es. segnale microfonico, segnale d'antenna)
3. **Alimentazione di collettore**: una tensione più alta (es. 12 V) attraverso una **resistenza di carico** $R_C$

Il funzionamento: la corrente modulata di base ($I_B$ costante + segnale) viene amplificata dal transistor ($I_C = \beta \times I_B$). La corrente di collettore, attraversando la resistenza di carico, genera per la legge di Ohm ($V = R \times I$) una **tensione di uscita** che riproduce il segnale di ingresso ma amplificato.

> Il transistor amplifica la **corrente**. La resistenza di carico **trasforma** l'amplificazione di corrente in amplificazione di **tensione**.

In pratica si usa un unico alimentatore ($V_{CC}$) da cui si ricavano sia l'alimentazione del collettore sia la polarizzazione di base tramite un **partitore resistivo** ($R_1$, $R_2$).

---

### 4. 🔧 Le Tre Configurazioni di Amplificazione (⏱ 46:06)

#### 🔹 Emettitore Comune (la più usata)

L'**emettitore** è il terminale **comune** ai circuiti di ingresso (base → emettitore) e di uscita (collettore → emettitore).

| Caratteristica | Valore |
|---|---|
| Amplificazione di tensione | Alta |
| Amplificazione di corrente | Alta (β) |
| Amplificazione di potenza | Alta |
| Impedenza di ingresso | Medio-bassa |
| Impedenza di uscita | Media |

È la configurazione **classica** e più usata per amplificatori di ogni tipo.

#### 🔹 Base Comune (rara, alta frequenza)

La **base** è messa a massa; il segnale entra dall'**emettitore** e l'uscita è sul **collettore**.

| Caratteristica | Valore |
|---|---|
| Amplificazione di tensione | Alta |
| Amplificazione di corrente | < 1 |
| Amplificazione di potenza | Media |
| Impedenza di ingresso | Molto bassa |
| Impedenza di uscita | Medio-alta |

Usata raramente, ma utile per **amplificazione ad alta frequenza** perché la base, interposta fisicamente fra collettore ed emettitore e messa a massa, funge da **schermo** che previene le autooscillazioni (effetto Larsen).

#### 🔹 Collettore Comune — Buffer (⏱ 50:06)

Il **collettore** è il terminale comune; il segnale entra in **base** e l'uscita si preleva dall'**emettitore**.

| Caratteristica | Valore |
|---|---|
| Amplificazione di tensione | ≈ 1 (leggermente attenuata) |
| Amplificazione di corrente | Molto alta |
| Amplificazione di potenza | Media |
| Impedenza di ingresso | **Molto alta** |
| Impedenza di uscita | **Molto bassa** |

Questo circuito è detto **buffer** o **separatore**. Non amplifica in tensione ma è fondamentale come interfaccia: l'alta impedenza di ingresso **non disturba** il circuito a monte, mentre la bassa impedenza di uscita permette di **pilotare carichi forti** (relè, linee di trasmissione).

> **Domanda d'esame tipica**: "Qual è la caratteristica ottimale per un amplificatore che deve disturbare poco il circuito a monte?" → Impedenza di ingresso alta → collettore comune (buffer).

---

### 5. 📊 Polarizzazione del Transistor (EXTRA) (⏱ 59:00)

> ⚠️ Questa sezione è **EXTRA** — non fa parte del programma d'esame.

Ogni transistor ha delle **curve caratteristiche** che mostrano come la corrente di uscita varia in funzione delle grandezze di ingresso. La **polarizzazione** consiste nel calcolare i valori delle resistenze del circuito per far lavorare il transistor nel **punto di lavoro ottimale**.

Nelle curve caratteristiche di uscita si distingue:

- Una zona iniziale **non lineare** (curva a gobba)
- Una zona centrale **lineare** (dove il segnale viene amplificato fedelmente)

Il punto di lavoro deve essere scelto **al centro della zona lineare** per permettere l'amplificazione corretta sia delle semionde positive che negative del segnale. Se il punto è troppo vicino alla zona non lineare, le semionde negative vengono distorte.

---

### 6. 📈 Transistor a Effetto di Campo — FET (⏱ 63:54)

#### 🔹 Struttura e Funzionamento

Il **FET** (Field Effect Transistor) ha un funzionamento diverso dal transistor bipolare. I tre terminali si chiamano:

- **Gate** (G): terminale di controllo (equivalente della base)
- **Drain** (D): terminale di uscita (equivalente del collettore)
- **Source** (S): terminale di riferimento (equivalente dell'emettitore)

La struttura è una **barretta di materiale drogato** (canale) che va dal drain al source, avvolta da una giunzione di materiale drogato opposto che forma il gate. La regione di svuotamento attorno al canale funziona come "rubinetto":

- **Aumento della tensione di gate** (in polarizzazione inversa) → la regione di svuotamento si allarga → il canale si restringe → meno corrente
- **Diminuzione della tensione di gate** → la regione si riduce → il canale si allarga → più corrente

> **Differenza fondamentale**: il transistor bipolare si pilota in **corrente** (la base assorbe corrente), il FET si pilota in **tensione** (il gate **non assorbe corrente** perché è sempre in polarizzazione inversa).

Come i transistor bipolari, esistono FET a **canale N** e a **canale P**.

#### 🔹 Transconduttanza

Il guadagno del FET non è il beta (che è un rapporto di correnti) ma la **transconduttanza** ($g_m$):

$$g_m = \frac{\Delta I_D}{\Delta V_G}$$

Dove $\Delta I_D$ è la variazione della corrente di drain e $\Delta V_G$ è la variazione della tensione di gate.

#### 🔹 Vantaggio Principale

L'**impedenza di ingresso molto alta** è il principale vantaggio dei FET. Sono usati come **stadio di ingresso** nelle catene di amplificazione per non caricare il circuito sorgente (es. microfono, ricevitore a cristallo con segnali debolissimi).

---

### 7. 🔌 MOSFET (⏱ 71:00)

Il **MOSFET** (Metal Oxide Semiconductor Field Effect Transistor) è una variazione del FET in cui il gate non è realizzato con una giunzione P-N ma con una **superficie metallica isolata dal canale mediante uno strato di ossido** (metal oxide), simile al principio dei diodi Schottky (hot carrier).

Il funzionamento è analogo al FET: la tensione di gate modula la larghezza del canale controllando il flusso di corrente. La differenza è puramente tecnologica (metallizzazione anziché giunzione).

---

### 8. 📻 Valvole Termoioniche — Tubi a Vuoto (⏱ 73:09)

> ⚠️ Le valvole termoioniche **fanno ancora parte del programma d'esame** del Ministero, anche se è incerto se continueranno a essere oggetto di domande.

#### 🔹 Principio di Funzionamento

Le valvole operano nel **vuoto** all'interno di un bulbo di vetro. Il principio base è l'**emissione termoionica**: un filamento portato all'incandescenza emette elettroni per eccitazione termica.

#### 🔹 Il Diodo Termoionico (⏱ 74:16)

**A riscaldamento diretto**: il filamento incandescente emette elettroni. Se una **placca** (anodo) vicina ha tensione positiva, attira gli elettroni → scorre corrente. Se l'anodo è negativo, respinge gli elettroni → non scorre corrente. Funzionamento identico al diodo a semiconduttore.

**A riscaldamento indiretto**: il filamento riscalda un **catodo** separato, realizzato con materiali ad alta **emissività** (che emettono facilmente molti elettroni). Vantaggio: minore energia per ottenere maggiore emissione di elettroni.

#### 🔹 Il Triodo (⏱ 78:40)

Il **triodo** ha tre terminali: **catodo**, **griglia** e **placca** (anodo). Una griglia di filo sottile posta vicino al catodo controlla il flusso di elettroni:

- Griglia molto negativa → respinge gli elettroni verso il catodo → non scorre corrente
- Griglia poco negativa → gli elettroni filtrano attraverso e raggiungono la placca → scorre corrente

Il triodo è il **primo dispositivo amplificatore** mai inventato (anni 1920). La griglia funziona esattamente come la base del transistor: una tensione di polarizzazione sulla quale si sovrappone il segnale da amplificare. Il segnale amplificato si ritrova sulla placca.

> L'analogia è immediata: la valvola è come un tubo dell'acqua, la griglia è il rubinetto che regola il flusso.

#### 🔹 Il Tetrodo (⏱ 81:12)

Il tetrodo aggiunge una **seconda griglia** chiamata **griglia schermo**:

- **Griglia controllo**: identica alla griglia del triodo, controlla il flusso di corrente
- **Griglia schermo**: posta tra griglia controllo e anodo, a potenziale positivo (ma inferiore all'anodo)

La griglia schermo risolve il problema del triodo: ad alta amplificazione, la capacità parassita tra griglia e placca riporta parte del segnale amplificato verso la griglia, causando **oscillazioni indesiderate**. La griglia schermo **scherma** la griglia controllo dalla placca, eliminando questo accoppiamento capacitivo e aumentando ulteriormente l'amplificazione.

#### 🔹 Il Pentodo (⏱ 84:54)

Il pentodo ha **cinque terminali**: catodo, anodo e tre griglie:

1. **Griglia controllo**: regola il flusso di corrente
2. **Griglia schermo**: scherma la griglia dall'anodo
3. **Griglia soppressore**: sopprme l'emissione di **elettroni secondari** dall'anodo

Il problema che risolve: gli elettroni che impattano ad alta velocità sull'anodo possono far uscire altri elettroni (emissione secondaria), disturbando il flusso di corrente e distorcendo le curve caratteristiche. La griglia soppressore li rimanda verso l'anodo, rendendo la curva **più lineare** e migliorando la fedeltà dell'amplificazione.

---

### 9. 📡 Discussione Pratica — Interferenze e Potenza (⏱ 97:00)

Nella parte finale della lezione si discute di aspetti pratici dell'attività radioamatoriale:

- **Limite legale di potenza**: 500 W (con riduzioni su bande specifiche). Il limite si misura sulla **potenza di uscita** dalla radio/amplificatore, non sulla potenza effettivamente irradiata dall'antenna.
- **Disturbi alle TV condominiali**: quasi sempre risolvibili. Le cause principali sono centralini TV economici senza filtraggio in ingresso e decoder di bassa qualità. I problemi si risolvono con filtri passa-basso sull'uscita del trasmettitore e sostituzione/miglioramento degli impianti TV.
- **Polizza assicurativa ARI**: l'iscrizione all'ARI include una polizza di copertura per le antenne installate. Sul sito ARI è disponibile la documentazione completa.
- **Rubrica legale su Radio Rivista**: l'avvocato Michele tratta mensilmente aspetti normativi (installazione antenne, assicurazioni, regolamenti condominiali).

---

## 🔗 Concept Map (testuale)

- **Transistor bipolare** → ha tre strati drogati → **NPN** o **PNP**
- **Base** (sottilissima) → terminale di controllo → piccola corrente abilita → grande corrente **collettore-emettitore**
- **Beta (β)** = $I_C / I_B$ → fattore di amplificazione → tipicamente 100-200
- **Emettitore comune** → amplifica tensione, corrente e potenza → configurazione più usata
- **Base comune** → bassa amplificazione corrente → usata ad alta frequenza → base funge da schermo
- **Collettore comune** → guadagno tensione ≈ 1 → buffer/separatore → impedenza ingresso alta, uscita bassa
- **FET** → pilotato in tensione → gate non assorbe corrente → impedenza ingresso molto alta
- **Transconduttanza** ($g_m$) → guadagno del FET → $\Delta I_D / \Delta V_G$
- **MOSFET** → variante del FET → gate isolato con ossido metallico
- **Valvola termoionica** → emissione termoionica nel vuoto → filamento emette elettroni
- **Triodo** → griglia controlla il flusso → primo amplificatore della storia
- **Tetrodo** → aggiunge griglia schermo → riduce accoppiamento capacitivo → meno oscillazioni
- **Pentodo** → aggiunge griglia soppressore → sopprime emissione secondaria → maggiore linearità

---

## 📝 Key Takeaways

1. Il **transistor bipolare** è un amplificatore di corrente con tre terminali: base (controllo), collettore (uscita) e emettitore. Una piccola corrente in base abilita una corrente molto maggiore fra collettore ed emettitore.

2. Il **fattore di amplificazione β** (beta o $H_{FE}$) è il rapporto $I_C / I_B$, tipicamente tra 100 e 200. L'amplificazione di corrente viene convertita in amplificazione di tensione tramite una resistenza di carico.

3. Le **tre configurazioni** di amplificazione a transistor sono: emettitore comune (la più usata, amplifica tutto), base comune (alta frequenza, anti-oscillazione), collettore comune (buffer, impedenza ingresso alta).

4. Il **FET** (transistor a effetto di campo) si pilota in **tensione** anziché in corrente: il gate non assorbe corrente, risultando in un'impedenza di ingresso molto alta. Il guadagno è espresso dalla transconduttanza.

5. Il **MOSFET** è una variante del FET con gate isolato da uno strato di ossido metallico; il funzionamento è analogo ma la tecnologia costruttiva è diversa.

6. Le **valvole termoioniche** funzionano per emissione termoionica nel vuoto. I quattro tipi (diodo, triodo, tetrodo, pentodo) differiscono per il numero di griglie: il triodo ne ha una (controllo), il tetrodo due (controllo + schermo), il pentodo tre (controllo + schermo + soppressore).

7. Il **triodo** è il primo amplificatore della storia: la griglia controlla il flusso di elettroni tra catodo e placca, come un rubinetto controlla il flusso d'acqua.

8. L'**impedenza di ingresso alta** è fondamentale per non disturbare il circuito a monte. Il collettore comune (buffer) e il FET hanno questa caratteristica e vengono usati come stadi di ingresso.

9. Il limite legale di potenza per i radioamatori è **500 W**, misurato all'uscita della radio/amplificatore. Con una buona antenna e 100 W si collegano praticamente tutte le stazioni.

10. I disturbi alla TV condominiale sono quasi sempre risolvibili con filtri, schermature e miglioramento dell'impianto TV. L'ARI fornisce supporto e polizza assicurativa per le antenne.

---

## ❓ Comprehension Questions

1. In che modo il funzionamento del transistor bipolare è collegato a quello del diodo? Quali analogie ci sono tra la giunzione P-N del diodo e le giunzioni del transistor?

2. Perché la base del transistor deve essere molto sottile? Cosa succederebbe se fosse spessa quanto gli altri strati?

3. Spiega perché il transistor è definito un "amplificatore di corrente" e come si ottiene da esso un amplificatore di tensione.

4. In quale situazione pratica sceglieresti un amplificatore a collettore comune anziché uno ad emettitore comune? Quali caratteristiche lo rendono adatto a quel compito?

5. Qual è la differenza fondamentale tra il pilotaggio di un transistor bipolare e quello di un FET? Quali conseguenze ha questa differenza sull'impedenza di ingresso?

6. Perché la configurazione a base comune è preferita per l'amplificazione ad alta frequenza? Qual è il ruolo fisico della base in questa configurazione?

7. Descrivi l'evoluzione dalle valvole diodo al pentodo: quale problema risolve ciascun tipo rispetto al precedente?

8. Perché il gate di un FET non assorbe corrente? Spiega il meccanismo legato alla regione di svuotamento.

9. Confronta il fattore di amplificazione β del transistor bipolare con la transconduttanza $g_m$ del FET: cosa misurano e perché hanno unità di misura diverse?

10. Un tuo vicino lamenta disturbi alla TV quando trasmetti. Sulla base di quanto appreso in questa lezione, quali potrebbero essere le cause e come le risolveresti?

---

## 📚 Glossary

- **Amplificatore a base comune** — Configurazione del transistor con base a massa; usata ad alta frequenza per prevenire oscillazioni. Bassa amplificazione di corrente, alta di tensione.
- **Amplificatore a collettore comune (buffer)** — Configurazione del transistor con collettore comune a ingresso e uscita; guadagno in tensione ≈ 1, impedenza di ingresso alta, impedenza di uscita bassa. Usato come separatore.
- **Amplificatore a emettitore comune** — Configurazione classica del transistor; amplifica tensione, corrente e potenza. La più usata.
- **Base** — Terminale di controllo del transistor bipolare; strato centrale molto sottile. Una piccola corrente di base controlla una grande corrente di collettore.
- **Beta (β) / $H_{FE}$** — Fattore di amplificazione in corrente del transistor bipolare; rapporto tra corrente di collettore e corrente di base ($\beta = I_C / I_B$).
- **Buffer (separatore)** — Circuito con alta impedenza di ingresso e bassa impedenza di uscita che non amplifica in tensione ma isola i circuiti.
- **Catodo** — Nelle valvole: terminale che emette elettroni per effetto termoionico.
- **Collettore** — Terminale di uscita del transistor bipolare; raccoglie la corrente amplificata.
- **Drain** — Terminale di uscita del FET, equivalente del collettore nel transistor bipolare.
- **Emettitore** — Terminale del transistor bipolare collegato alla massa nel circuito più comune; identificato dalla freccia nel simbolo.
- **Emissione termoionica** — Emissione di elettroni da un materiale portato all'incandescenza; principio di funzionamento delle valvole.
- **FET (Field Effect Transistor)** — Transistor a effetto di campo, pilotato in tensione tramite il gate. Impedenza di ingresso molto alta.
- **Gate** — Terminale di controllo del FET/MOSFET, equivalente della base nel transistor bipolare. Non assorbe corrente.
- **Griglia controllo** — Nelle valvole: griglia che controlla il flusso di elettroni tra catodo e placca, equivalente della base/gate.
- **Griglia schermo** — Nel tetrodo/pentodo: griglia che scherma la griglia controllo dall'anodo, prevenendo oscillazioni.
- **Griglia soppressore** — Nel pentodo: griglia che sopprime l'emissione secondaria di elettroni dall'anodo.
- **Impedenza di ingresso** — Resistenza equivalente che un circuito presenta al segnale in ingresso. Alta = disturba poco il circuito a monte.
- **MOSFET** — Metal Oxide Semiconductor FET; variante del FET con gate isolato da ossido metallico.
- **NPN / PNP** — I due tipi di transistor bipolare, distinti dall'ordine degli strati drogati. NPN: freccia emettitore verso l'esterno. PNP: freccia verso l'interno.
- **Pentodo** — Valvola con cinque terminali (catodo, anodo, tre griglie) che offre la maggiore linearità di amplificazione.
- **Placca (anodo)** — Nelle valvole: terminale positivo che raccoglie gli elettroni emessi dal catodo.
- **Polarizzazione** — Impostazione delle condizioni di lavoro del transistor tramite tensioni e correnti continue che definiscono il punto di funzionamento.
- **Punto di lavoro** — Punto sulle curve caratteristiche del transistor dove è polarizzato; deve stare nella zona lineare per amplificazione fedele.
- **Resistenza di carico ($R_C$)** — Resistenza sul collettore che trasforma le variazioni di corrente in variazioni di tensione (uscita dell'amplificatore).
- **Source** — Terminale di riferimento del FET, equivalente dell'emettitore nel transistor bipolare.
- **Tetrodo** — Valvola con quattro terminali; aggiunge la griglia schermo al triodo per ridurre le oscillazioni.
- **Transconduttanza ($g_m$)** — Guadagno del FET; rapporto tra variazione della corrente di drain e variazione della tensione di gate.
- **Transistor bipolare** — Dispositivo semiconduttore a tre giunzioni (NPN o PNP) che amplifica la corrente. Pilotato in corrente.
- **Triodo** — Valvola con tre terminali (catodo, griglia, placca); primo dispositivo amplificatore della storia.
- **Valvola termoionica (tubo a vuoto)** — Dispositivo elettronico basato sull'emissione di elettroni da un catodo incandescente nel vuoto; precursore del transistor.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore principale**: Paolo (radiotecnica — transistor, FET, MOSFET, valvole)
- 👨‍🏫 **Relatore**: Silvio IZ5DIY (correzione quiz e coordinamento)
- 👨‍🏫 **Interventi**: Sauro (valvole, amplificatori), Fabrizio (coordinamento, filtri ATX)
- 🎓 **Partecipanti**: Marco, Luigi, David, Claudio, Vincenzo, Nicola, Alessandro, Federico, Salvatore, Roberto e altri

---

## ⏱️ Evidenze Temporali

| Intervallo | Argomento |
|---|---|
| 00:02 - 09:00 | Correzione quiz Lezione 11 (diodi, alimentatori, raddrizzatori) |
| 09:10 - 25:00 | Transistor bipolare: struttura NPN/PNP, terminali, zone di svuotamento, amplificazione |
| 25:00 - 29:00 | Beta del transistor: definizione e formula |
| 29:00 - 45:00 | Schema di amplificazione: polarizzazione, resistenza di carico, uscita al collettore, domande |
| 45:00 - 56:00 | Tre configurazioni: emettitore comune, base comune, collettore comune (buffer) |
| 56:00 - 63:00 | Domande su attenuazione, impedenza, tabella riassuntiva |
| 63:00 - 63:30 | Polarizzazione del transistor (EXTRA): curve caratteristiche e punto di lavoro |
| 63:30 - 70:00 | FET: struttura, gate, drain, source, canale, transconduttanza |
| 70:00 - 73:00 | MOSFET: gate isolato con ossido metallico |
| 73:00 - 86:00 | Valvole termoioniche: diodo, triodo, tetrodo, pentodo |
| 86:00 - 116:00 | Discussione pratica: esibizione valvole, interferenze TV, limiti di potenza, polizza ARI |

---

## 📅 Informazioni Lezione

| Campo | Valore |
|---|---|
| **Numero lezione** | 12 |
| **Data** | 28 maggio 2025 |
| **Durata** | ~2 ore |
| **Numero argomenti** | 6 (Quiz, Transistor bipolare, Configurazioni amplificazione, FET/MOSFET, Valvole, Discussione pratica) |
| **Parole chiave** | Transistor, NPN, PNP, base, collettore, emettitore, beta, amplificazione, emettitore comune, base comune, collettore comune, buffer, FET, MOSFET, gate, drain, source, transconduttanza, valvola termoionica, triodo, tetrodo, pentodo, griglia, impedenza di ingresso |
