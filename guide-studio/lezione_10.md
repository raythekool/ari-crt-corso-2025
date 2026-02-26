# 📘 Lezione 10 - Corso Radioamatori

## 📌 Overview

- **Materia**: Normativa radioamatoriale — Bande radioamatoriali, frequenze, band plan, ITU, IARU, ARI, legislazione
- **Tempo di studio stimato**: 2 ore e 30 minuti
- **Prerequisiti**: Lezione 09 (alfabeto fonetico, indicativi, codice Q, RST), nozioni di base su onde elettromagnetiche e frequenza
- **Obiettivi di apprendimento**:
  - Comprendere la relazione tra lunghezza d'onda e frequenza
  - Conoscere la suddivisione dello spettro radio (HF, VHF, UHF, ecc.)
  - Memorizzare le bande radioamatoriali e i relativi intervalli di frequenza
  - Comprendere i concetti di uso esclusivo, primario e secondario delle frequenze
  - Capire la funzione e la struttura del band plan
  - Conoscere il ruolo di ITU, IARU, CEPT, ARI e MIMIT
  - Distinguere tra patente di radioamatore e autorizzazione generale

---

## 📖 Core Content

### 1. 📝 Correzione quiz Lezione 09 — Ripasso normativa

La lezione si apre con la correzione del questionario relativo alla lezione 09. I risultati sono largamente positivi, con due picchi negativi su domande specifiche.

#### 🔹 Domande chiave analizzate

- **Domanda C (Santiago)**: la domanda era volutamente ironica. Santiago **non è** la parola corretta dell'alfabeto fonetico per la lettera S (la parola corretta è **Sierra**). Santiago è una città della Galizia, meta di pellegrinaggi. L'intento era far riflettere sull'uso canonico dell'alfabeto fonetico.

- **Domanda D (Nominativo)**: quale di queste è una stazione italiana? La risposta corretta era **IU2FQW**. Un nominativo come IS0HL5P non può esistere perché, nella parte di suffisso, non possono comparire numeri — solo lettere.

- **Domanda H (RST)**: la **R** del codice RST indica la **readability** (leggibilità/comprensibilità), non la forza del segnale (che è la **S**, Strength) e non la quantità di rumore.

- **Domanda I (Locatore)**: domanda fuori esame sul QTH Locator. La struttura è: 2 lettere (quadratone) + 2 numeri (sotto-quadrato) + 2 lettere (ulteriore dettaglio). Le altre opzioni erano un nominativo e un'abbreviazione telegrafica (73 = saluti).

- **Domanda P (QRT)**: il codice **QRT** indica la cessazione/fine delle trasmissioni.

#### 🔹 Nota sulle abbreviazioni 73, 51

Le abbreviazioni numeriche come **73** (saluti) e **51** non rientrano nella tabella delle abbreviazioni telegrafiche da esame. Tuttavia, 73 è una conoscenza che ogni radioamatore non può non avere, anche se formalmente non è nelle 12 abbreviazioni ministeriali.

---

### 2. 📡 Onde elettromagnetiche e lunghezza d'onda

Silvio introduce il tema delle bande radioamatoriali partendo da un'analogia fondamentale: le **onde elettromagnetiche** sono il **mezzo di trasporto** per le nostre comunicazioni, proprio come un'automobile, un treno o un aereo sono mezzi per spostarsi fisicamente.

#### 🔹 L'analogia del mezzo di trasporto

La scelta della frequenza (e quindi della **lunghezza d'onda**) determina dove e come possiamo comunicare:

- Per andare a Firenze dalla Toscana → automobile (distanza breve)
- Per andare negli Stati Uniti → aereo (lunga distanza)
- Non si va a fare la spesa in paese con un Boeing 320

Allo stesso modo, frequenze diverse hanno **caratteristiche di propagazione** diverse:

- Il **Wi-Fi** (frequenze alte, lunghezza d'onda corta) non supera le pareti di casa
- La **radio FM** si perde appena si cambia versante di montagna
- Le **onde medie** (AM) si possono ascoltare anche dal seminterrato

#### 🔹 Lunghezza d'onda e frequenza

La **lunghezza d'onda** ($\lambda$) è la distanza percorsa dall'onda nel compimento di un ciclo completo. È legata alla frequenza ($f$) dalla relazione inversa:

$$\lambda = \frac{c}{f} = \frac{300}{f_{MHz}} \text{ (in metri)}$$

- **Maggiore è la frequenza** → **minore è la lunghezza d'onda** (e viceversa)
- A 100 MHz → $\lambda$ = 3 m
- A 1 MHz → $\lambda$ = 300 m
- A 14 MHz → $\lambda$ = circa 20 m

#### 🔹 Analogia del passo

La lunghezza d'onda è paragonabile al "passo" con cui l'onda si muove:

- **Onde lunghe** (passo grande) = come un gigante → superano facilmente ostacoli (sassi, muri, montagne)
- **Onde corte** (passo piccolo) = come una formica → già un sasso è un ostacolo insormontabile

Questo spiega perché il Wi-Fi (lunghezza d'onda centimetrica) non passa attraverso un muro, mentre le onde medie (lunghezza d'onda di centinaia di metri) si ricevono anche nel seminterrato.

---

### 3. 📊 Spettro elettromagnetico e spettro radio

Lo **spettro elettromagnetico** comprende tutte le onde elettromagnetiche: dalle onde radio alla luce visibile, dai raggi X ai raggi gamma. Lo **spettro radio** è solo una porzione di esso, compresa indicativamente tra 10 kHz e diversi GHz.

#### 🔹 Suddivisione dello spettro radio

Lo spettro radio è suddiviso in bande designate con sigle internazionali. La nomenclatura nasce storicamente: prima si usavano solo basse frequenze, poi man mano si scoprivano frequenze più alte.

| Sigla   | Nome                     | Frequenza       | Lunghezza d'onda   | Denominazione |
| ------- | ------------------------ | --------------- | ------------------ | ------------- |
| **VLF** | Very Low Frequency       | 3 – 30 kHz      | Onde miriametriche |               |
| **LF**  | Low Frequency            | 30 – 300 kHz    | Onde chilometriche |               |
| **MF**  | Medium Frequency         | 300 – 3.000 kHz | Onde ettometriche  |               |
| **HF**  | High Frequency           | 3 – 30 MHz      | Onde decametriche  |               |
| **VHF** | Very High Frequency      | 30 – 300 MHz    | Onde metriche      |               |
| **UHF** | Ultra High Frequency     | 300 – 3.000 MHz | Onde decimetriche  |               |
| **SHF** | Super High Frequency     | 3 – 30 GHz      | Onde centimetriche |               |
| **EHF** | Extremely High Frequency | 30 – 300 GHz    | Onde millimetriche |               |

> Il pattern ricorrente è il fattore **3**: ogni banda va da 3 a 30 (o da 30 a 300, ecc.), cioè un fattore 10 per ogni salto.

L'attività radioamatoriale si concentra prevalentemente in **HF**, **VHF** e **UHF**, che coprono il 95-99% dell'uso.

⚠️ _Tema d'esame: conoscere le sigle (HF, VHF, UHF...) e i corrispondenti intervalli di frequenza. Le bande più rilevanti sono quelle attribuite ai radioamatori._

---

### 4. 📻 Bande radioamatoriali

Le bande radioamatoriali sono porzioni ("fettine") dello spettro radio attribuite al servizio di radioamatore. Sono disseminate lungo lo spettro e vengono identificate per **lunghezza d'onda**.

#### 🔹 Le bande principali

| Banda (lunghezza d'onda) | Frequenza (MHz)   | Categoria spettro |
| ------------------------ | ----------------- | ----------------- |
| 160 m                    | 1,810 – 2,000     | MF                |
| 80 m                     | 3,500 – 3,800     | HF                |
| 40 m                     | 7,000 – 7,200     | HF                |
| 30 m                     | 10,100 – 10,150   | HF                |
| 20 m                     | 14,000 – 14,350   | HF                |
| 17 m                     | 18,068 – 18,168   | HF                |
| 15 m                     | 21,000 – 21,450   | HF                |
| 12 m                     | 24,890 – 24,990   | HF                |
| 10 m                     | 28,000 – 29,700   | HF                |
| 6 m                      | 50,000 – 52,000   | VHF               |
| 2 m                      | 144,000 – 146,000 | VHF               |
| 70 cm                    | 430,000 – 440,000 | UHF               |
| 23 cm                    | 1.240 – 1.300     | UHF               |

Quando un radioamatore dice "ho fatto un collegamento in 20 m", intende che ha usato la banda 14 – 14,350 MHz. La denominazione per lunghezza d'onda è il modo di comunicazione standard tra radioamatori.

#### 🔹 Tipi di attribuzione

Le bande possono essere attribuite ai radioamatori con tre livelli diversi:

**Uso esclusivo** — La banda è utilizzata **solo** dai radioamatori. Nessun altro servizio è ammesso. Sono tipicamente le bande più storiche.

**Uso primario** — La banda è condivisa con altri servizi, ma il radioamatore ha **priorità**. In caso di interferenza, l'altro servizio deve cedere.

**Uso secondario** — La banda è condivisa con altri servizi, ma il radioamatore **non ha priorità**. Se la banda è già in uso da un servizio primario (es. militare), il radioamatore deve cessare la trasmissione.

> **Esempio**: la banda dei 70 cm (433 MHz) è condivisa con altri servizi come i telecomandi delle automobili.

⚠️ _Tema d'esame: la differenza tra uso esclusivo, primario e secondario è materia d'esame ricorrente._

---

### 5. 🗺️ Band Plan — Il piano di banda

Il **band plan** (piano di banda) è l'insieme delle regole che i radioamatori si sono dati per l'utilizzo organizzato delle bande loro attribuite. È paragonabile al regolamento di un condominio.

#### 🔹 Perché serve il band plan

All'interno di una banda attribuita ai radioamatori, coesistono **tipi di emissione diversi** con **larghezze di banda** molto differenti:

| Tipo di emissione       | Larghezza di banda tipica    |
| ----------------------- | ---------------------------- |
| Telegrafia (CW)         | ~300 Hz                      |
| Modi digitali (es. FT8) | ~50 Hz                       |
| Fonia SSB               | ~2.700 Hz (2,7 kHz)          |
| Fonia FM                | 5.000 – 15.000 Hz (5-15 kHz) |

**Analogia del parcheggio**: dove ci sta una trasmissione FM (un "camion"), ci starebbero 10 trasmissioni SSB (10 "automobili") o 50 trasmissioni CW (50 "biciclette"). Senza regole, l'uso sarebbe inefficiente.

#### 🔹 Struttura del band plan

Il band plan suddivide ogni banda in segmenti destinati a specifici tipi di trasmissione:

- Un segmento per la telegrafia (segnali con larghezza ≤ 200 Hz o ≤ 500 Hz)
- Un segmento per la fonia SSB (larghezza ≤ 2,7 kHz)
- Un segmento per i modi digitali
- Eventuali segmenti per FM (solo in certe bande, es. 10 m e 2 m)
- Frequenze di ritrovo per attività specifiche (es. QRP a 3560 kHz, DX, ecc.)

**Esempio banda 20 m** (14 – 14,350 MHz): non è possibile fare FM perché lo spazio è troppo limitato. In soli 350 kHz, poche trasmissioni FM occuperebbero tutta la banda.

**Esempio banda 10 m** (28 – 29,7 MHz): essendo più ampia, include un segmento FM (sopra 29 MHz) con canali da 10 kHz.

#### 🔹 Come conoscere il band plan

I band plan sono pubblicati dalla **IARU Regione 1** e vengono periodicamente aggiornati. L'ultima versione citata è del 16 ottobre 2020. Non sono statici: evolvono con le esigenze (nuovi modi digitali, nuove attività).

> "Il band plan non è scolpito sulla pietra [...] sono frutto di continui aggiustamenti e compromessi raggiunti in ambito internazionale."

#### 🔹 Cosa sapere per l'esame

Non è richiesto memorizzare ogni dettaglio di ogni band plan. È necessario sapere:

- **Che cosa è** un band plan e a cosa serve
- Che la banda è suddivisa per **tipo di emissione** e **larghezza di banda**
- Che esiste una regolamentazione a cui sottostare
- Il concetto generale di utilizzo efficiente dello spettro

⚠️ _Tema d'esame: il concetto di band plan e la sua funzione possono essere oggetto di domanda._

---

### 6. 🏛️ Organizzazioni internazionali: ITU, IARU, CEPT

La regolamentazione delle frequenze richiede coordinamento internazionale perché le onde radio non si fermano ai confini nazionali.

#### 🔹 ITU — International Telecommunication Union

L'**ITU** (Unione Internazionale delle Telecomunicazioni) è l'agenzia delle **Nazioni Unite** che sovraintende alle telecomunicazioni mondiali. È una sorta di "Ministero delle Comunicazioni del mondo intero".

All'interno della ITU viene definito il **servizio di radioamatore**:

> "Un servizio di radiocomunicazione a scopo non commerciale svolto da appassionati di radiocomunicazione che utilizzano e sperimentano le proprie stazioni radio per comunicazioni personali, autoistruzione tecnica, interconnessione di stazione, ricerca scientifica e altri scopi simili."

L'ITU opera per **regioni geografiche**:

| Regione       | Area geografica                       |
| ------------- | ------------------------------------- |
| **Regione 1** | Europa, Africa, Medio Oriente, Russia |
| **Regione 2** | Americhe                              |
| **Regione 3** | Asia e Oceania                        |

**L'Italia appartiene alla Regione 1 dell'ITU.**

Le attribuzioni di frequenza possono variare tra regioni diverse (es. la banda 900 MHz: in Europa è per la telefonia mobile, in USA è di uso libero a bassa potenza).

⚠️ _Tema d'esame: a quale Regione ITU appartiene l'Italia (Regione 1), quante sono le regioni ITU (3)._

#### 🔹 IARU — International Amateur Radio Union

La **IARU** è l'Unione Internazionale dei Radioamatori, fondata nel 1925. È l'organizzazione che:

- **Rappresenta** i radioamatori nell'ITU (come un sindacato internazionale)
- **Coordina** l'uso delle bande a livello internazionale (band plan)
- **Protegge** lo spettro attribuito ai radioamatori dalla pressione di servizi commerciali
- È riconosciuta dall'ONU come **ente non governativo**

Ogni nazione ha **una sola associazione** membro della IARU, in modo da garantire rappresentanza unitaria.

> "Se non si proteggono le nostre bande, un servizio commerciale di connessione via satellite potrebbe voler acquisire le nostre frequenze 144-146 MHz per costruirci un servizio a pagamento."

#### 🔹 CEPT — Conferenza Europea delle Amministrazioni Postali e delle Telecomunicazioni

La **CEPT** è un coordinamento europeo che si occupa di standardizzazione in ambito postale e delle telecomunicazioni. In ambito radioamatoriale, la CEPT è importante perché stabilisce accordi di **reciprocità**: un radioamatore italiano autorizzato secondo gli standard CEPT può operare anche in Spagna o in altri Paesi membri, essendo riconosciuto come operatore autorizzato.

---

### 7. 🇮🇹 Organizzazioni nazionali: ARI e MIMIT

#### 🔹 ARI — Associazione Radioamatori Italiani

L'**ARI** è l'associazione nazionale che rappresenta i radioamatori italiani. In ambito nazionale svolge il ruolo che la IARU svolge a livello internazionale:

- Si rapporta con l'ente regolatore (MIMIT)
- Rappresenta le istanze dei radioamatori presso il Ministero
- Riceve e diffonde comunicazioni dal Ministero
- È l'**unica** associazione italiana membro della IARU

#### 🔹 MIMIT — Ministero delle Imprese e del Made in Italy

Il **MIMIT** (già Ministero dello Sviluppo Economico, Ministero delle Poste e Telecomunicazioni, ecc.) è l'ente regolatore italiano per le telecomunicazioni. Ha cambiato nome molte volte nel tempo; per questo Silvio preferisce chiamarlo genericamente "ente regolatore".

All'interno del MIMIT opera la **Direzione Generale per i Servizi di Comunicazione Elettronica, Radiodiffusione e Postali**, che ha uffici teritoriali detti **ispettorati** (quello di riferimento per la Toscana ha sede a Firenze).

La normativa di riferimento è il **Codice delle Comunicazioni Elettroniche** (D.Lgs. 259/2003 e successive modifiche), che contiene circa **10 articoli** specifici per i radioamatori, più un allegato (Allegato 26) che elenca i **temi d'esame**.

#### 🔹 Regole fondamentali dall'Articolo 25 ITU

Le comunicazioni radioamatoriali devono essere:

- **Non commerciali** — non si può fare lucro
- **Aperte e non segrete** — non si possono usare codici o trasmissioni criptate
- **Non destinate a terzi** — salvo in caso di emergenza e calamità naturali

> "Nella virtù del fatto che non ci facciamo lucro [...] e offriamo un servizio in situazioni di emergenza, queste frequenze sono una sorta di concessione filantropica che lo Stato fa nei confronti della comunità radioamatoriale."

---

### 8. 📋 Patente e Autorizzazione Generale

Silvio conclude con due concetti fondamentali per l'iter di accesso all'attività radioamatoriale.

#### 🔹 Patente di radioamatore

La **patente** è il documento che attesta la qualifica di radioamatore. Si ottiene superando un esame che verifica conoscenze tecniche e competenze operative.

Caratteristiche fondamentali:

- **Non scade MAI** — una volta ottenuta, resta valida per tutta la vita
- Certifica che il titolare possiede le conoscenze teoriche e pratiche necessarie
- È paragonabile alla patente automobilistica (ma quella automobilistica ha scadenza)
- Avere la patente non obbliga a svolgere attività radioamatoriale

#### 🔹 Autorizzazione Generale

L'**autorizzazione generale** (in passato chiamata "licenza") è il documento che:

- Assegna un **nominativo** (indicativo di chiamata) al radioamatore
- Autorizza effettivamente l'esercizio dell'attività radioamatoriale
- **Scade ogni 10 anni** e deve essere rinnovata
- Richiede il pagamento di un **canone annuale** (importo simbolico, pochi euro)
- Può essere personale o attribuita a una sezione (nominativo collettivo)

**Analogia automobilistica**:

- **Patente** = so guidare (abilitazione) → non scade
- **Autorizzazione generale** = ho l'automobile e la targa (mezzo + nominativo) → scade ogni 10 anni

**Iter procedurale**:

1. Superare l'**esame** → ottenere la **patente** (non scade)
2. Richiedere un **nominativo** → ottenere l'**autorizzazione generale** (scade ogni 10 anni)
3. Pagare il **canone** annuale
4. Iniziare l'attività radioamatoriale

L'autorizzazione generale può essere **sospesa o revocata** in caso di comportamenti irregolari, analogamente alle sanzioni previste per la patente automobilistica. La patente invece, attestando una conoscenza, non viene ritirata.

⚠️ _Tema d'esame: la distinzione tra patente (non scade) e autorizzazione generale (scade ogni 10 anni) è una domanda ricorrente._

---

## 🔗 Concept Map (testuale)

- **Onda elettromagnetica** → è il mezzo di trasporto per → **comunicazione radio**
- **Lunghezza d'onda ($\lambda$)** → è inversamente proporzionale a → **frequenza ($f$)**
- **Spettro radio** → è suddiviso in → **VLF, LF, MF, HF, VHF, UHF, SHF, EHF**
- **HF (3-30 MHz)** → contiene la maggior parte delle → **bande radioamatoriali**
- **Bande radioamatoriali** → sono identificate per → **lunghezza d'onda** (es. 20 m, 2 m)
- **Attribuzione di banda** → può essere → **esclusiva, primaria o secondaria**
- **Band plan** → regola l'uso interno delle → **bande radioamatoriali**
- **Larghezza di banda dell'emissione** → determina il → **segmento di band plan**
- **CW (300 Hz)** → occupa molto meno spazio di → **FM (15 kHz)**
- **ITU** → è l'agenzia ONU che regola → **telecomunicazioni mondiali**
- **ITU** → è suddivisa in → **3 regioni** (Italia = Regione 1)
- **IARU** → rappresenta i radioamatori dentro → **ITU**
- **IARU** → coordina → **band plan** a livello regionale
- **ARI** → rappresenta i radioamatori italiani in → **IARU**
- **ARI** → si rapporta con → **MIMIT** (ente regolatore italiano)
- **CEPT** → standardizza in ambito europeo → **riconoscimento reciproco radioamatori**
- **Patente** → attesta la qualifica → **non scade mai**
- **Autorizzazione generale** → abilita l'esercizio → **scade ogni 10 anni**
- **Patente** → precede → **autorizzazione generale** nell'iter

---

## 📝 Key Takeaways

1. **Le onde elettromagnetiche** sono il mezzo di trasporto delle comunicazioni radio. La scelta della frequenza determina le caratteristiche di propagazione, analogamente alla scelta del mezzo di trasporto per uno spostamento fisico.

2. **Lunghezza d'onda e frequenza sono inversamente proporzionali**: $\lambda = 300/f_{MHz}$. A frequenza più alta corrisponde lunghezza d'onda più corta, e viceversa.

3. **Lo spettro radio** è suddiviso in bande (HF, VHF, UHF, ecc.) con intervalli che seguono il fattore 3 (3-30, 30-300, 300-3000 MHz). L'attività radioamatoriale si svolge prevalentemente in HF, VHF e UHF.

4. **Le bande radioamatoriali** sono porzioni dello spettro, disseminate al suo interno, identificate per lunghezza d'onda (20 m, 2 m, 70 cm, ecc.) e possono essere in uso esclusivo, primario o secondario.

5. **Il band plan** è il regolamento interno delle bande radioamatoriali che suddivide ogni banda per tipo di emissione e larghezza di banda, garantendo la coesistenza efficiente di servizi diversi (CW, SSB, FM, digitale).

6. **L'ITU** è l'agenzia delle Nazioni Unite per le telecomunicazioni, suddivisa in 3 regioni: l'Italia appartiene alla **Regione 1** (Europa, Africa, Medio Oriente, Russia).

7. **La IARU** è il "sindacato internazionale" dei radioamatori che siede nell'ITU, coordina i band plan e protegge lo spettro attribuito ai radioamatori dalla pressione commerciale.

8. **L'ARI** è l'unica associazione italiana membro della IARU e si rapporta con il MIMIT (ente regolatore) per le questioni nazionali.

9. **La patente di radioamatore non scade mai**; l'**autorizzazione generale scade ogni 10 anni** e richiede rinnovo e pagamento di un canone annuale simbolico.

10. **Lo spettro radio è un bene finito e pubblico**: la regolamentazione delle frequenze esiste per garantire la coesistenza di servizi diversi (radioamatori, aeronautica, telefonia, ecc.) senza interferenze reciproche.

---

## ❓ Comprehension Questions

1. Spiega la relazione tra lunghezza d'onda e frequenza utilizzando la formula $\lambda = 300/f$. Perché a frequenze più alte corrispondono lunghezze d'onda più corte?

2. Qual è la differenza tra uso esclusivo, primario e secondario di una banda di frequenze? Fai un esempio pratico per ciascun tipo.

3. Perché non è possibile (o non è opportuno) trasmettere in FM nella banda dei 20 m? Ragiona in termini di larghezza di banda e numero di canali disponibili.

4. Descrivi la struttura gerarchica delle organizzazioni radioamatoriali: ITU → IARU → ARI. Qual è il ruolo di ciascuna?

5. In che modo il band plan garantisce l'utilizzo efficiente delle bande radioamatoriali? Perché è paragonato al "regolamento condominiale"?

6. Un radioamatore ha superato l'esame e ottenuto la patente. Può iniziare immediatamente a trasmettere? Perché?

7. Perché lo spettro radio viene definito un "bene finito e pubblico"? Quali conseguenze ha questa definizione sulla regolamentazione?

8. L'Italia appartiene alla Regione ITU 1. Quali altri Paesi o aree geografiche fanno parte della stessa regione? Perché è importante questa suddivisione?

9. Spiega perché le comunicazioni radioamatoriali devono essere "aperte e non segrete". Da quale norma internazionale deriva questo principio?

10. Cosa succederebbe se non esistessero regole di convivenza (band plan) all'interno delle bande radioamatoriali? Descrivi uno scenario di utilizzo non regolamentato.

---

## 📚 Glossary

- **Allegato 26** — Allegato al Codice delle Comunicazioni Elettroniche che elenca i temi d'esame per la patente di radioamatore.
- **ARI** — Associazione Radioamatori Italiani, unica associazione nazionale membro della IARU.
- **Autorizzazione generale** — Documento che abilita l'esercizio dell'attività radioamatoriale, assegna un nominativo, ha durata di 10 anni e richiede il pagamento di un canone.
- **Band plan** — Piano di banda; regolamentazione interna delle bande radioamatoriali che stabilisce quali tipi di emissione sono ammessi in ciascun segmento di frequenza.
- **CEPT** — Conferenza Europea delle Amministrazioni delle Poste e delle Telecomunicazioni; standardizza le regole in ambito europeo, inclusa la reciprocità delle patenti radioamatoriali.
- **Codice delle Comunicazioni Elettroniche** — D.Lgs. 259/2003; legge italiana che regola tutte le comunicazioni elettroniche, inclusa l'attività radioamatoriale (circa 10 articoli specifici).
- **EHF** — Extremely High Frequency, 30-300 GHz, onde millimetriche.
- **HF** — High Frequency, 3-30 MHz, onde decametriche. Contiene la maggior parte delle bande radioamatoriali storiche.
- **IARU** — International Amateur Radio Union; organizzazione internazionale che rappresenta i radioamatori nell'ITU e coordina i band plan.
- **Ispettorato territoriale** — Ufficio locale del MIMIT; quello di riferimento per la Toscana ha sede a Firenze.
- **ITU** — International Telecommunication Union; agenzia delle Nazioni Unite per le telecomunicazioni, suddivisa in 3 regioni.
- **Ionosfera** — Strato dell'atmosfera che riflette alcune frequenze radio (tipicamente HF), permettendo comunicazioni oltre l'orizzonte.
- **Larghezza di banda** — Porzione di spettro occupata da un segnale; varia da ~50 Hz (modi digitali) a ~15 kHz (FM).
- **LF** — Low Frequency, 30-300 kHz, onde chilometriche.
- **Lunghezza d'onda ($\lambda$)** — Distanza percorsa dall'onda in un ciclo completo; inversamente proporzionale alla frequenza.
- **MF** — Medium Frequency, 300-3000 kHz, onde ettometriche. Le "onde medie" della radio tradizionale.
- **MIMIT** — Ministero delle Imprese e del Made in Italy; l'attuale ente regolatore italiano per le telecomunicazioni.
- **Patente di radioamatore** — Documento che attesta la qualifica tecnica e operativa del radioamatore; non ha scadenza.
- **Piano nazionale di ripartizione delle frequenze** — Documento che assegna le diverse porzioni dello spettro radio ai vari servizi (radioamatori, aeronautica, telefonia, ecc.).
- **Propagazione** — Modalità con cui le onde elettromagnetiche si diffondono nello spazio; dipende dalla frequenza.
- **Regione ITU** — Suddivisione geografica dell'ITU: Regione 1 (Europa, Africa, Medio Oriente, Russia), Regione 2 (Americhe), Regione 3 (Asia, Oceania).
- **SHF** — Super High Frequency, 3-30 GHz, onde centimetriche.
- **Spettro radio** — Porzione dello spettro elettromagnetico utilizzata per le radiocomunicazioni.
- **UHF** — Ultra High Frequency, 300-3000 MHz, onde decimetriche.
- **Uso esclusivo** — Attribuzione di una banda al solo servizio di radioamatore.
- **Uso primario** — Attribuzione condivisa in cui il radioamatore ha priorità sugli altri servizi.
- **Uso secondario** — Attribuzione condivisa in cui il radioamatore deve cedere in caso di conflitto con un servizio primario.
- **VHF** — Very High Frequency, 30-300 MHz, onde metriche. Include la banda dei 2 m.
- **VLF** — Very Low Frequency, 3-30 kHz, onde miriametriche.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Silvio IZ5DIY (normativa e bande radioamatoriali)
- 🎓 **Partecipanti**: Corsisti ARI Toscana CRT 2025 (tra cui Marco, Massimo, Giovanni, Roberto, Claudio, Alberto)
- 🎙️ **Coordinamento**: Fabrizio, Alessio

---

## ⏱️ Evidenze Temporali

| Intervallo      | Argomento                                                                        |
| --------------- | -------------------------------------------------------------------------------- |
| 00:03 – 10:03   | Correzione quiz lezione 09: Santiago, nominativi, RST, locatore, QRT             |
| 10:16 – 13:08   | Introduzione argomenti della serata                                              |
| 13:08 – 26:04   | Onde elettromagnetiche: analogia mezzi di trasporto, lunghezza d'onda, frequenza |
| 26:04 – 39:00   | Spettro elettromagnetico, suddivisione HF/VHF/UHF/SHF, tabella frequenze         |
| 39:00 – 55:00   | Bande radioamatoriali: elenco, attribuzione esclusiva/primaria/secondaria        |
| 55:00 – 78:00   | Band plan: concetto, larghezza di banda emissioni, suddivisione interna          |
| 78:00 – 98:00   | Band plan dettagliato: 20 m, 2 m, regole condominiali, domande e risposte        |
| 98:00 – 113:00  | ITU e IARU: definizione, ruolo, regioni, servizio di radioamatore                |
| 113:00 – 122:00 | CEPT, ARI, MIMIT: organizzazioni europee e nazionali                             |
| 122:00 – 132:00 | Codice delle Comunicazioni Elettroniche, patente e autorizzazione generale       |
| 132:00 – 150:00 | Domande finali su patente/autorizzazione, sanzioni, frequenze, approfondimenti   |

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                               |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione**          | 10                                                                                                                                                                                                                                                   |
| **Data**             | 14 maggio 2025                                                                                                                                                                                                                                       |
| **Durata**           | ~2 ore e 30 minuti                                                                                                                                                                                                                                   |
| **Numero argomenti** | 8 (correzione quiz + 7 argomenti normativi)                                                                                                                                                                                                          |
| **Parole chiave**    | Bande radioamatoriali, lunghezza d'onda, frequenza, spettro radio, HF, VHF, UHF, band plan, uso esclusivo, uso primario, uso secondario, ITU, IARU, CEPT, ARI, MIMIT, Regione 1, patente, autorizzazione generale, Codice Comunicazioni Elettroniche |
