---
layout: default
---

# 📘 Lezione 09 - Modulazione

## 📌 Overview

- **Materia**: Normativa radioamatoriale — Alfabeto fonetico, indicativi di chiamata, abbreviazioni telegrafiche, codice Q, rapporto RST e locatore
- **Tempo di studio stimato**: 2 ore e 30 minuti
- **Prerequisiti**: Conoscenze base di matematica (lezione 08), nozioni generali sul radioamatore
- **Obiettivi di apprendimento**:
  - Correggere e consolidare gli esercizi di matematica della lezione precedente
  - Conoscere l'alfabeto fonetico NATO/ICAO/ITU e la sua importanza nelle comunicazioni radio
  - Comprendere la struttura degli indicativi di chiamata italiani e internazionali
  - Memorizzare le abbreviazioni telegrafiche previste dal tema d'esame
  - Padroneggiare il codice Q nelle sue forme di domanda e risposta
  - Comprendere il sistema RST (Readability, Strength, Tone)
  - Conoscere il Maidenhead Locator System per l'identificazione geografica

---

## 📖 Core Content

### 1. 📝 Correzione quiz Lezione 08 — Ripasso matematica

La prima parte della lezione è dedicata alla correzione degli esercizi assegnati da Lucia nella lezione 08. Questa sessione di verifica serve a consolidare le competenze matematiche necessarie per il resto del corso e per l'esame.

#### 🔹 Esercizi di notazione scientifica e conversione di unità

Gli esercizi corretti includono diverse tipologie:

- **Conversione in notazione scientifica**: ad esempio $160 \times 10^9$ deve essere scritto come $1{,}6 \times 10^{11}$.
- **Esponenti negativi**: $14 \times 10^{-3} = 0{,}014$.
- **Resistenze in parallelo**: usando la formula $R = \frac{R_1 \times R_2}{R_1 + R_2}$ con attenzione alla conversione delle unità (es. $k\Omega$ e $\Omega$).
- **Resistenze in serie** con unità miste: somma di valori espressi in $\Omega$ e $k\Omega$.
- **Conversioni tra multipli e sottomultipli**: picofarad in nanofarad, MHz in Hz ($100 \text{ MHz} = 10^8 \text{ Hz}$), GHz in THz ($1 \text{ GHz} = 10^{-3} \text{ THz}$).
- **Regole degli esponenti**: moltiplicazione di potenze con la stessa base.
- **Logaritmi**: $\log 2 \approx 0{,}3$, calcolo di $20 \times \log 3 \approx 9{,}54$.

I risultati dei corsisti sono stati nel complesso positivi.

#### 🔹 Discussione sull'uso della calcolatrice all'esame

Un punto importante emerso dalla discussione riguarda l'uso della **calcolatrice durante l'esame**. Non è certo se sarà consentita, poiché dipende dal decreto ministeriale vigente al momento dell'esame. In ogni caso, se la calcolatrice non fosse ammessa, i calcoli richiesti saranno sufficientemente semplici da poter essere eseguiti a mente. Gli esercizi proposti da Lucia sono stati volutamente più difficili rispetto a quelli d'esame, come una sorta di "palestra" per allenare le competenze matematiche.

> "Se non fosse consentita la calcolatrice, i calcoli saranno sufficientemente semplici da poter essere eseguiti a mente."

I logaritmi verranno utilizzati nel prosieguo del corso per il calcolo dei **decibel**.

---

### 2. 📡 Alfabeto fonetico NATO/ICAO/ITU

Con l'inizio della parte di **normativa**, il docente Silvio (IZ5DIY) introduce il primo dei quattro argomenti fondamentali della serata. L'alfabeto fonetico è uno standard internazionale sviluppato dall'**ICAO** (International Civil Aviation Organization) e adottato dall'**ITU** (International Telecommunication Union).

#### 🔹 Scopo e caratteristiche

L'**alfabeto fonetico** — detto anche NATO phonetic alphabet — nasce per eliminare le ambiguità nello spelling delle lettere durante le comunicazioni radio. In condizioni di segnale debole o disturbato, lettere come P, B e T possono essere facilmente confuse. Usando le parole convenzionali (Papa, Bravo, Tango), l'ambiguità viene eliminata.

**Caratteristiche delle parole scelte**:

- Non confondibili tra loro, anche in condizioni di ascolto difficili
- Riconoscibili a livello internazionale
- Provenienti da culture diverse per favorire la comprensione universale

**Esempio pratico**: la lettera "P" può essere confusa con "B" o "T" nel parlato normale. Usando "Papa", "Bravo" e "Tango" non vi è possibilità di confusione.

**Nota sul numero 9**: si pronuncia "**Niner**" (e non semplicemente "Nine") per evitare confusione con "Five".

> **Consiglio pratico**: esercitarsi leggendo le targhe delle automobili usando l'alfabeto fonetico.

#### 🔹 Uso corretto vs. uso gergale

Silvio sottolinea con forza l'importanza di usare le parole **corrette** dell'alfabeto fonetico, non varianti gergali. Ad esempio:

- **R** = **Romeo** (NON "Radio")
- **S** = **Sierra** (NON "Santiago")

L'uso di "Radio" per R e "Santiago" per S è tipico della **CB (Citizen Band)** e non è corretto nelle comunicazioni radioamatoriali. In condizioni di segnale debole, la controparte si aspetta di sentire le parole standard; usare varianti non standard crea confusione e può impedire la comprensione, specialmente con interlocutori stranieri.

⚠️ _Tema d'esame: l'alfabeto fonetico ICAO/ITU è materia d'esame._

---

### 3. 📋 Indicativi di chiamata (Nominativi)

L'**indicativo di chiamata** (call sign) è il "nome" unico di ogni radioamatore, paragonabile a una targa automobilistica. È composto da tre elementi fondamentali.

#### 🔹 Struttura dell'indicativo

| Elemento     | Descrizione                  | Esempio           |
| ------------ | ---------------------------- | ----------------- |
| **Prefisso** | Identifica il Paese          | I, IK, IZ, IU, IW |
| **Numero**   | Identifica l'area geografica | 5 = Toscana       |
| **Suffisso** | Assegnato in sequenza        | AA, AB, AC...     |

**Prefisso** — Il prefisso italiano è **I**. Nel tempo, con l'esaurimento dei suffissi disponibili, sono stati introdotti prefissi aggiuntivi: **IK**, **IZ**, **IU**, **IW**, corrispondenti a diverse epoche o classi di patente. L'allocazione dei prefissi a livello mondiale è gestita dall'**ITU**.

**Numero d'area** — In Italia il numero indica l'area geografica, basata sulla suddivisione dei codici postali:

- **5** = Toscana
- Ogni regione/area ha il proprio numero identificativo

**Suffisso** — Viene assegnato sequenzialmente (AA, AB, AC, ...) ed è unico per ciascun radioamatore.

#### 🔹 Regole d'uso dell'indicativo

L'indicativo di chiamata deve essere pronunciato:

- All'**inizio** di ogni trasmissione
- Alla **fine** di ogni trasmissione
- Ogni **10 minuti** durante la trasmissione

#### 🔹 Prefissi internazionali

Ogni nazione ha uno o più prefissi assegnati dall'ITU. Esempi:

| Prefisso     | Paese       |
| ------------ | ----------- |
| **F**        | Francia     |
| **DL**       | Germania    |
| **EA**       | Spagna      |
| **K**, **W** | Stati Uniti |
| **JA**       | Giappone    |

Esistono anche prefissi speciali per:

- **Isole italiane** e regioni autonome
- **Stazioni di club** (prefisso **IQ**)
- **Stazioni da contest** con prefissi temporanei

⚠️ _Tema d'esame: la struttura degli indicativi e i prefissi italiani sono materia d'esame._

---

### 4. 📨 Abbreviazioni telegrafiche

Le **abbreviazioni telegrafiche** nascono nell'epoca della telegrafia, quando la velocità di trasmissione era limitata e ogni carattere richiedeva tempo. Queste sigle, pur essendo nate per il CW (Continuous Wave / telegrafia), sono entrate nell'uso comune anche in **fonia** e nelle **comunicazioni digitali** moderne.

#### 🔹 Abbreviazioni fondamentali da esame

| Sigla   | Significato                                                                      |
| ------- | -------------------------------------------------------------------------------- |
| **TX**  | Trasmettitore                                                                    |
| **RX**  | Ricevitore                                                                       |
| **RTX** | Ricetrasmettitore                                                                |
| **CQ**  | Chiamata generale ("I seek you" — cerco qualcuno)                                |
| **AR**  | Fine del messaggio (in CW si trasmette come un unico carattere: $\overline{AR}$) |
| **R**   | Ricevuto (Roger)                                                                 |
| **K**   | Invito a trasmettere                                                             |
| **SK**  | Fine delle trasmissioni (Silent Key)                                             |
| **RST** | Rapporto di ricezione (Readability, Strength, Tone)                              |
| **73**  | Saluti cordiali                                                                  |

#### 🔹 CQ — La chiamata generale

**CQ** è l'abbreviazione più iconica del mondo radioamatoriale. Deriva foneticamente dall'inglese "**I seek you**" (ti cerco). Quando un radioamatore si sintonizza su una frequenza e vuole stabilire un contatto, trasmette:

> "CQ CQ CQ chiama India Zulu 5 Delta India Yankee..."

#### 🔹 SK — Silent Key

**SK** significa letteralmente "tasto silente" (Silent Key). Oltre al significato tecnico di "fine delle trasmissioni", nel gergo radioamatoriale ha assunto anche il significato di **radioamatore deceduto**: un "OM morto" viene chiamato un "SK". Questo è un esempio di come le abbreviazioni telegrafiche si carichino di significati aggiuntivi nel tempo.

#### 🔹 Evoluzione dall'uso telegrafico all'uso moderno

Queste abbreviazioni, nate per la telegrafia, si ritrovano oggi:

- In **fonia** (es. "il mio RX", "il mio QTH")
- Nelle **comunicazioni digitali** (PSK31, FT8, ecc.)
- Sulle **cartoline QSL** (es. "CFM our QSO")

Il linguaggio abbreviato costituisce un vero e proprio **metalinguaggio** comprensibile da tutti i radioamatori del mondo, indipendentemente dalla lingua madre.

#### 🔹 Formato delle domande d'esame

Le domande d'esame sulle abbreviazioni telegrafiche hanno tipicamente due forme:

1. "Qual è la sigla per [significato]?" → scegliere la sigla corretta
2. "[Sigla] che cosa significa?" → scegliere il significato corretto

Le abbreviazioni da sapere per l'esame sono circa **12**, un numero gestibile con qualche esercizio ripetuto.

⚠️ _Tema d'esame: le abbreviazioni telegrafiche indicate dal ministero sono materia d'esame obbligatoria._

---

### 5. 🔤 Codice Q

Il **codice Q** è una raccolta standardizzata di **messaggi codificati di tre lettere**, tutte inizianti con la lettera **Q**. Sviluppato inizialmente per le comunicazioni commerciali via telegrafo, è stato successivamente adottato dalla Marina, dall'Aeronautica e dai radioamatori.

#### 🔹 Funzionamento del codice Q

Ogni codice Q può essere usato in due modi:

1. **Come domanda**: seguito da un **punto interrogativo** (?)
   - Es. QRA? = "Come ti chiami?" / "Qual è il nome della tua stazione?"
2. **Come risposta/affermazione**: seguito dall'informazione richiesta
   - Es. QRA è IZ5DIY = "Il nome della mia stazione è IZ5DIY"
3. **Come comando**: alcuni codici hanno senso da soli, senza necessità di ulteriori dettagli
   - Es. QRS = "Trasmetti più lentamente" (è un'istruzione diretta)

#### 🔹 Codici Q da esame

I codici Q richiesti per l'esame sono in numero limitato. Silvio sottolinea che sono quelli evidenziati nelle slide ministeriali. Alcuni codici Q importanti:

| Codice  | Significato (domanda)                          | Significato (risposta/comando)           |
| ------- | ---------------------------------------------- | ---------------------------------------- |
| **QRA** | Qual è il nome della tua stazione?             | Il nome della mia stazione è...          |
| **QRG** | Qual è la mia frequenza esatta?                | La tua frequenza esatta è...             |
| **QRK** | Qual è l'intelligibilità dei miei segnali?     | L'intelligibilità dei tuoi segnali è...  |
| **QRL** | Sei occupato?                                  | Sono occupato                            |
| **QRM** | Sei disturbato?                                | Sono disturbato                          |
| **QRN** | Sei disturbato da scariche atmosferiche?       | Sono disturbato da scariche atmosferiche |
| **QRO** | Devo aumentare la potenza?                     | Aumenta la potenza                       |
| **QRP** | Devo diminuire la potenza?                     | Diminuisci la potenza                    |
| **QRS** | Devo trasmettere più lentamente?               | Trasmetti più lentamente                 |
| **QRT** | Devo cessare la trasmissione?                  | Cessa la trasmissione                    |
| **QRZ** | Da chi sono chiamato?                          | Sei chiamato da...                       |
| **QSL** | Puoi dare ricevuta?                            | Do ricevuta                              |
| **QSO** | Puoi comunicare con...?                        | Posso comunicare con...                  |
| **QSY** | Devo passare a trasmettere su altra frequenza? | Passa a trasmettere su...                |
| **QTH** | Qual è la tua posizione?                       | La mia posizione è...                    |

#### 🔹 Uso pratico e metalinguaggio

Il codice Q rappresenta un **metalinguaggio universale**: indipendentemente dalla lingua madre, tutti i radioamatori comprendono lo stesso significato. Se un operatore dice "QTH?" a un radioamatore russo, giapponese o brasiliano, tutti capiscono che sta chiedendo la posizione. Questo supera la barriera linguistica.

**Esempio pratico**: "QTH è San Marcello Pistoiese" — in un'unica sigla di tre lettere si esprime "il mio posto è", evitando lunghe frasi in qualsiasi lingua.

#### 🔹 Differenza tra uso ministeriale e uso reale

Silvio segnala una discrepanza tra le definizioni ministeriali dei codici Q e il loro uso effettivo nella pratica radioamatoriale. I testi ministeriali possono contenere definizioni "arcaiche" che non vengono aggiornate da decenni, mentre l'uso pratico si è evoluto. Tuttavia, per l'esame è necessario conoscere i codici **come definiti dal ministero**, anche se nella pratica l'uso è leggermente diverso.

> "Ingoliamo la pasticca piccolina invece di prendere il suostone" — ovvero meglio imparare poche definizioni ministeriali che dover conoscere l'intero formulario Q.

#### 🔹 Nota sulla revisione dei temi d'esame

Viene evidenziato come in altri Paesi (es. Stati Uniti) i temi d'esame vengano rivisti ogni 5 anni per mantenerli attuali (eliminando argomenti obsoleti e aggiungendone di nuovi). In Italia, il processo di revisione è molto più lento, per cui alcune domande d'esame riguardano argomenti ormai poco usati nella pratica.

⚠️ _Tema d'esame: i codici Q evidenziati dal ministero sono materia d'esame. È molto probabile che almeno 2-3 domande riguardino il codice Q._

---

### 6. 📊 Rapporto RST (Readability, Strength, Tone)

Il **rapporto RST** è il sistema standardizzato per comunicare la qualità del segnale ricevuto. Si compone di tre parametri, ciascuno espresso con un numero.

#### 🔹 R — Readability (Leggibilità)

La **R** indica quanto il messaggio è **comprensibile**, indipendentemente dalla potenza del segnale. Scala da 1 a 5:

| Valore | Significato                                                                     |
| ------ | ------------------------------------------------------------------------------- |
| **R1** | Illeggibile — si percepisce la presenza di un segnale ma non si comprende nulla |
| **R2** | Appena leggibile — si capisce qualche parola a tratti                           |
| **R3** | Leggibile con notevole difficoltà                                               |
| **R4** | Leggibile con qualche difficoltà — si perde qualche parola ma il senso è chiaro |
| **R5** | Perfettamente leggibile — comprensione totale                                   |

**Distinzione fondamentale**: un segnale può arrivare **forte** ma essere **incomprensibile** (es. modulazione distorta, microfono difettoso). Readability e Strength sono parametri indipendenti.

> "Se io parlo col microfono infilato dentro una lattina di Coca-Cola mentre fa le bollicine, non mi capisce nessuno, anche se il segnale è molto forte."

#### 🔹 S — Strength (Intensità del segnale)

La **S** indica con quanta **intensità** il segnale arriva al ricevitore. È una misura prevalentemente **strumentale**, letta sullo **S-meter** del ricevitore. Scala da S1 a S9, dove:

- **S1** = segnale appena percepibile
- **S9** = segnale molto forte (corrisponde a un livello di tensione standardizzato in $\mu V$)
- Oltre S9 si parla di **dB oltre S9** (es. "S9 +20 dB"), indicando segnali estremamente forti

Lo S-meter è un indicatore presente sulla maggior parte dei ricevitori, con un ago che si posiziona sulla scala da S1 a S9 e oltre.

#### 🔹 T — Tone (Tono della nota telegrafica)

La **T** riguarda specificamente la **qualità della nota in telegrafia**. Scala da 1 a 9:

- **T9** = nota perfettamente pura e cristallina (standard attuale)
- **T1** = nota estremamente ronzante, con gravi difetti

I difetti nella nota telegrafica erano storicamente **indicatori di problemi circuitali**: un ronzio poteva indicare un problema di rettificazione della corrente alternata, un rientro di radiofrequenza o altri malfunzionamenti del trasmettitore.

**Nota**: nelle apparecchiature moderne, quasi tutte le note telegrafiche sono di qualità T9. Questa scala mantiene rilevanza come retaggio storico e per casi eccezionali con apparecchiature vecchie.

**In fonia**: il parametro T non viene utilizzato. Il rapporto diventa semplicemente **RS** (es. "59" = R5 S9, ovvero perfettamente comprensibile e molto forte).

⚠️ _Tema d'esame: il sistema RST e la sua interpretazione sono materia d'esame._

---

### 7. 🗺️ Maidenhead Locator System (Locatore)

Il **locatore** (Maidenhead Locator System) è un sistema per identificare la posizione geografica mediante una sigla alfanumerica compatta, alternativa alle coordinate di latitudine e longitudine.

#### 🔹 Come funziona

Il sistema funziona per **suddivisioni successive** (come una matriosca):

1. **Primo livello** (2 lettere): il mondo viene diviso in grandi quadrati, identificati da due lettere (es. **JN**). Questa è una macroarea molto ampia.

2. **Secondo livello** (2 numeri): ogni quadrato del primo livello viene suddiviso in sotto-quadrati identificati da due numeri (es. JN**54**). Si ottiene un'area più ristretta.

3. **Terzo livello** (2 lettere): ogni sotto-quadrato viene ulteriormente diviso, identificato da due lettere minuscole (es. JN54**ja**). Si arriva a un'area di pochi chilometri quadrati.

Il locatore completo a 6 caratteri (es. **JN54ja**) identifica un'area di alcuni chilometri quadrati, sufficiente per distinguere paesi vicini.

#### 🔹 Utilità pratica

- Permette di comunicare la propria posizione in modo **compatto** (6 caratteri invece di coordinate lunghe)
- Consente il **calcolo della distanza** tra due stazioni tramite software
- Viene utilizzato nei **log** di stazione e nei **contest**
- È calcolato automaticamente dai programmi, dal GPS e da servizi come Google Maps

**Esempio**: JN54ja identifica un'area nella montagna pistoiese. Ogni diversa posizione nel mondo avrà un locatore diverso.

> "Con questi tre passaggi arrivo a definire un quadratotto di qualche chilometro quadrato [...] già sufficiente per dire e differenziare un quartiere di Firenze piuttosto che l'altro."

⚠️ _Il locatore NON è materia d'esame, ma è una conoscenza essenziale per l'attività pratica del radioamatore._

---

## 🔗 Concept Map (testuale)

- **Alfabeto fonetico ICAO/ITU** → elimina ambiguità → **comunicazioni radio**
- **Indicativo di chiamata** → è composto da → **Prefisso + Numero + Suffisso**
- **Prefisso** → identifica → **Nazione** (assegnato dall'ITU)
- **Numero d'area** → identifica → **Regione geografica** (5 = Toscana)
- **Abbreviazioni telegrafiche** → sono il DNA del → **linguaggio radioamatoriale**
- **CQ** → è la chiamata generale → deriva da "I seek you"
- **Codice Q** → è un metalinguaggio → universale indipendente dalla lingua
- **Codice Q + ?** → assume forma di → **domanda**
- **Codice Q senza ?** → assume forma di → **risposta o comando**
- **Rapporto RST** → misura la qualità del → **collegamento radio**
- **R (Readability)** → misura la → **comprensibilità** (scala 1-5)
- **S (Strength)** → misura l'→ **intensità del segnale** (scala S1-S9+)
- **T (Tone)** → misura la qualità della → **nota telegrafica** (scala 1-9)
- **Readability** → è indipendente da → **Strength** (segnale forte ≠ comprensibile)
- **Locatore Maidenhead** → codifica → **posizione geografica** in 6 caratteri
- **Abbreviazioni telegrafiche** → sono nate per → **CW/telegrafia**
- **Abbreviazioni telegrafiche** → sono migrate in → **fonia e digitale**
- **Tutte le sigle e codici** → formano un → **metalinguaggio universale**

---

## 📝 Key Takeaways

1. **L'alfabeto fonetico NATO/ICAO/ITU** è uno standard internazionale che elimina l'ambiguità nello spelling durante le comunicazioni radio. Le parole scelte sono studiate per essere non confondibili tra loro, anche in condizioni di ascolto difficili.

2. **L'indicativo di chiamata** è unico e personale, strutturato come Prefisso (nazione) + Numero (area) + Suffisso (sequenziale). In Italia il prefisso è I (e varianti IK, IZ, IU, IW) e il numero 5 indica la Toscana.

3. **L'indicativo deve essere pronunciato** all'inizio e alla fine di ogni trasmissione e ogni 10 minuti durante la trasmissione stessa.

4. **Le abbreviazioni telegrafiche** (circa 12 per l'esame) costituiscono un metalinguaggio universale nato dalla telegrafia e ancora in uso in fonia e comunicazioni digitali. Le più importanti sono CQ, TX, RX, RST, SK, AR, R, K, 73.

5. **Il codice Q** è un sistema di messaggi codificati di tre lettere che iniziano con Q. Seguito da punto interrogativo è una domanda, altrimenti è una risposta o un comando. I codici Q ministeriali sono circa 15 e vanno saputi a memoria per l'esame.

6. **Il rapporto RST** esprime la qualità del segnale ricevuto: R (comprensibilità, 1-5), S (intensità, S1-S9+), T (qualità della nota telegrafica, 1-9). In fonia si usa solo RS, senza il parametro T.

7. **Readability e Strength sono indipendenti**: un segnale può arrivare forte ma essere incomprensibile, o debole ma perfettamente leggibile.

8. **Il locatore Maidenhead** codifica la posizione geografica in una sigla di 6 caratteri (lettere-numeri-lettere) con precisione di alcuni chilometri quadrati. Non è materia d'esame ma è indispensabile nella pratica.

9. **Usare sempre le parole corrette dell'alfabeto fonetico** (Romeo, Sierra) e non varianti gergali da CB (Radio, Santiago), per garantire la comprensione internazionale.

10. **Per l'esame**, le domande su abbreviazioni telegrafiche e codice Q hanno una struttura a risposta chiusa (3 opzioni): conoscere bene le sigle ministeriali permette spesso di escludere le risposte errate per deduzione.

---

## ❓ Comprehension Questions

1. Perché l'alfabeto fonetico ICAO/ITU prevede parole specifiche come "Papa", "Bravo" e "Tango" invece di lasciare libertà di scelta al radioamatore? Quali problemi potrebbe causare l'uso di parole non standard?

2. Spiega la struttura completa di un indicativo di chiamata italiano, facendo un esempio concreto. Qual è il significato di ciascuna parte?

3. Qual è la differenza tra un codice Q seguito da punto interrogativo e lo stesso codice Q senza punto interrogativo? Fai almeno due esempi.

4. Perché il parametro R (Readability) e il parametro S (Strength) del rapporto RST sono considerati indipendenti? Descrivi una situazione in cui un segnale ha R basso ma S alto.

5. Le abbreviazioni telegrafiche sono nate per la telegrafia (CW). Spiega come e perché sono migrate nell'uso in fonia e nelle comunicazioni digitali, facendo almeno due esempi concreti.

6. Come funziona il Maidenhead Locator System? Descrivi i tre livelli di suddivisione e spiega perché un locatore a 6 caratteri è sufficiente per la maggior parte delle comunicazioni.

7. Un radioamatore trasmette "CQ CQ CQ chiama IZ5DIY": cosa sta facendo esattamente? Come dovrebbe rispondere un altro radioamatore che lo sente?

8. Quali informazioni si possono ricavare dall'indicativo di chiamata IK5ABC? Identifica prefisso, area e suffisso, e spiega cosa indicano.

9. Un radioamatore riceve un rapporto "59": cosa significa in dettaglio ciascun numero? E se il rapporto fosse "31"?

10. Perché Silvio afferma che i temi d'esame italiani non sono sempre aggiornati? Qual è la differenza con il sistema americano, e perché questo ha un impatto sulla preparazione del candidato?

---

## 📚 Glossary

- **73** — Abbreviazione telegrafica che significa "saluti cordiali". È un saluto universale tra radioamatori.
- **Alfabeto fonetico (NATO/ICAO/ITU)** — Standard internazionale che assegna una parola univoca a ciascuna lettera dell'alfabeto per eliminare ambiguità nelle comunicazioni radio.
- **AR** — Abbreviazione telegrafica per "fine del messaggio". In CW si trasmette come carattere unico.
- **Call sign** — Vedi "Indicativo di chiamata".
- **CB (Citizen Band)** — Banda radio per uso civile non amatoriale, con regole e convenzioni diverse da quelle radioamatoriali.
- **Codice Q** — Raccolta standardizzata di messaggi codificati di tre lettere che iniziano con Q, usati nelle comunicazioni radio per sintetizzare domande e risposte.
- **CQ** — Chiamata generale; un radioamatore che trasmette CQ cerca qualcuno con cui stabilire un collegamento.
- **CW (Continuous Wave)** — Telegrafia, trasmissione mediante codice Morse.
- **DX** — Collegamento a lunga distanza (da "Distance").
- **ICAO** — International Civil Aviation Organization, ente che ha sviluppato l'alfabeto fonetico poi adottato dall'ITU.
- **Indicativo di chiamata** — Sigla unica assegnata a ogni radioamatore, composta da prefisso (Paese), numero (area) e suffisso (sequenziale).
- **ITU** — International Telecommunication Union, organizzazione internazionale per le telecomunicazioni che assegna i prefissi nazionali.
- **K** — Abbreviazione telegrafica per "invito a trasmettere".
- **Locatore (Maidenhead)** — Sistema di codifica della posizione geografica in una sigla alfanumerica di 6+ caratteri.
- **Metalinguaggio** — Linguaggio convenzionale (sigle, abbreviazioni, codici Q) comprensibile da tutti i radioamatori del mondo indipendentemente dalla lingua madre.
- **Niner** — Pronuncia fonetica del numero 9, per evitare confusione con "Five".
- **OM (Old Man)** — Termine affettuoso per indicare un radioamatore.
- **Prefisso** — Prima parte dell'indicativo di chiamata, identifica il Paese di appartenenza (es. I = Italia).
- **QRA** — Codice Q: nome della stazione.
- **QRZ** — Codice Q: "Da chi sono chiamato?"
- **QSL** — Codice Q: conferma di ricezione. "QSL Card" = cartolina di conferma del collegamento.
- **QSO** — Codice Q: comunicazione/collegamento tra due stazioni.
- **QTH** — Codice Q: posizione (luogo da dove si trasmette).
- **R** — Abbreviazione telegrafica per "ricevuto" (Roger). Anche: parametro di Readability nel rapporto RST.
- **Readability** — Parametro R del rapporto RST: misura la comprensibilità del segnale (scala 1-5).
- **RST** — Sistema di rapporto sulla qualità del segnale: Readability (comprensibilità), Strength (intensità), Tone (tono della nota telegrafica).
- **RTX** — Ricetrasmettitore (abbreviazione di RX + TX).
- **RX** — Ricevitore (abbreviazione telegrafica).
- **S-meter** — Strumento indicatore presente nei ricevitori che mostra l'intensità del segnale ricevuto su scala S1-S9+.
- **SK (Silent Key)** — Abbreviazione telegrafica per "fine delle trasmissioni". Nel gergo radioamatoriale indica anche un radioamatore deceduto.
- **S (Strength)** — Parametro del rapporto RST: misura l'intensità del segnale ricevuto (scala S1-S9 e oltre in dB).
- **Suffisso** — Ultima parte dell'indicativo di chiamata, assegnato sequenzialmente (AA, AB, AC...).
- **T (Tone)** — Parametro del rapporto RST: misura la qualità della nota telegrafica (scala 1-9).
- **TX** — Trasmettitore (abbreviazione telegrafica).

---

## 👥 Partecipanti

- 👨‍🏫 **Relatori**: Lucia (correzione quiz matematica), Silvio IZ5DIY (normativa — lezione principale)
- 🎙️ **Coordinamento**: Fabrizio, Alessio

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Lezione**          | 09                                                                                                                                                                                                                 |
| **Data**             | 07 maggio 2025                                                                                                                                                                                                     |
| **Durata**           | ~2 ore e 40 minuti                                                                                                                                                                                                 |
| **Numero argomenti** | 7 (correzione quiz + 6 argomenti normativi)                                                                                                                                                                        |
| **Parole chiave**    | Alfabeto fonetico, ICAO, ITU, NATO, indicativi di chiamata, prefissi, call sign, abbreviazioni telegrafiche, CQ, SK, codice Q, QTH, QSL, QSO, QRZ, RST, Readability, Strength, Tone, S-meter, locatore, Maidenhead |
