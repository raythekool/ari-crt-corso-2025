---
layout: default
---

# 📘 Lezione 22 - Procedure Operative

## 📌 Overview

- **Materia**: Legislazione radioamatoriale — Parte 1: Struttura normativa, D.Lgs. 259/2003, articoli 134-145, CEPT e reciprocità internazionale
- **Tempo di studio stimato**: 2 ore
- **Prerequisiti**: Nozioni di base sull'attività radioamatoriale, nominativi di chiamata, bande di frequenza (lezioni precedenti)
- **Obiettivi di apprendimento**:
  - Conoscere la struttura gerarchica della normativa (ITU → CEPT → legislazione nazionale)
  - Comprendere il D.Lgs. 259/2003 e gli articoli 134-145 relativi ai radioamatori
  - Distinguere tra patente (non scade) e autorizzazione (10 anni)
  - Conoscere le raccomandazioni CEPT TR 61-01 e TR 61-02
  - Comprendere le norme sulle stazioni ripetitrici e le autorizzazioni speciali

---

## 📖 Core Content

### 1. 📝 Correzione Quiz sulle Antenne

La lezione si apre con la correzione dei quiz relativi alla lezione precedente (antenne). Il relatore Paolo evidenzia che tutti i partecipanti hanno superato la soglia del 60% (richiesta all'esame), con punteggi mediamente tra il 70% e il 100%.

Vengono riepilogati i concetti chiave verificati nel quiz:

- **Aumentare la frequenza di risonanza** di un'antenna → accorciarla (frequenza e lunghezza d'onda sono inversamente proporzionali)
- **Polarizzazione** → definita dal piano in cui si propaga il **campo elettrico**
- **Antenna direttiva** → il **riflettore parabolico** (l'isotropica e la ground plane irradiano a 360°)
- **Resistenza di radiazione** di un dipolo a mezz'onda → **73 Ω**
- **Calcolo ERP**: 100 W trasmettitore + 4 dB guadagno antenna − 1 dB attenuazione cavo = +3 dB = raddoppio → **200 W** di potenza effettiva irradiata
- **Formula dipolo**: $150 \times 0{,}953 / f \approx 143 / f$
- **Antenna isotropica** → teorica, non realizzabile, usata come riferimento
- **Balun** → va inserito tra il cavo coassiale e l'antenna
- **Antenna artificiale** = carico fittizio (non irradiante)
- **Guadagno dipolo vs isotropica** → **2,1 dB**
- **Trappole** → rendono l'antenna multibanda
- **Lobo principale Yagi** → direzione di massima irradiazione

> ⚠️ **Concetto d'esame ribadito**: Nella Yagi, il **riflettore è più lungo** del radiatore, i **direttori sono più corti**. Il radiatore è un dipolo a **mezz'onda**. Non esiste un rapporto numerico fisso tra le lunghezze, poiché dipende dalla progettazione specifica dell'antenna.

---

### 2. 🔑 Parole Chiave della Normativa

Prima di entrare nella legislazione, vengono presentate le parole chiave fondamentali che ricorrono nella normativa radioamatoriale:

| Acronimo  | Significato                                                           | Ruolo                                                                          |
| --------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **ITU**   | International Telecommunication Union                                 | Agenzia ONU per le telecomunicazioni, definisce il servizio di radioamatore    |
| **IARU**  | International Amateur Radio Union                                     | Rappresenta i radioamatori nella ITU; organizzata con associazioni nazionali   |
| **CEPT**  | Conferenza Europea delle Amministrazioni di Poste e Telecomunicazioni | Standardizzazione e reciprocità tra stati europei (e non solo)                 |
| **MIMIT** | Ministero delle Imprese e del Made in Italy                           | Ente regolatore italiano di riferimento per i radioamatori                     |
| **WRC**   | World Radiocommunication Conference                                   | Conferenze preparatorie per le riunioni ITU sulle attribuzioni di frequenza    |
| **PNRF**  | Piano Nazionale di Ripartizione delle Frequenze                       | Elenco delle frequenze e dei servizi a cui sono attribuite in ambito nazionale |

L'**IARU** rappresenta le istanze dei radioamatori nella sede ITU, difendendo le bande di frequenza attribuite al servizio di radioamatore dalle pressioni di altri servizi commerciali e governativi.

---

### 3. 🏛️ Gerarchia Normativa

La normativa radioamatoriale si inserisce in una struttura piramidale:

```
Costituzione / Codice civile e penale
        ↓
Standard internazionali (ITU, IARU)
        ↓
Raccomandazioni CEPT
        ↓
Leggi nazionali (D.Lgs. 259/2003)
        ↓
Decreti attuativi
        ↓
Circolari ministeriali
```

Le **leggi** definiscono il quadro generale. I **decreti** dettagliano aspetti specifici. Le **circolari** chiariscono aspetti interpretativi e pratici (es. date degli esami, modalità di presentazione della domanda).

---

### 4. 📜 Il Decreto Legislativo 259/2003

Il **D.Lgs. 259/2003** (1° agosto 2003) è il **Codice delle comunicazioni elettroniche**, la legge fondamentale che governa tutte le comunicazioni elettroniche in Italia — dalla radiodiffusione alla TV satellitare, dai gestori internet ai radioamatori.

#### Struttura della parte radioamatoriale

La parte che riguarda specificamente i radioamatori è contenuta in:

- **Titolo III, Capo VII**: circa **10-11 articoli** (dal 134 al 145) — quadro generale dell'attività radioamatoriale
- **Allegato 25**: contributi economici (importi e modalità di pagamento — attualmente 50 € una tantum)
- **Allegato 26**: norme attuative dettagliate — potenze, procedure, moduli, programma d'esame, suballegati con codice Q, abbreviazioni, ecc.

> ⚠️ **Attenzione**: Il D.Lgs. 259/2003 ha subito **successive modifiche di legge**, l'ultima significativa il **24 marzo 2024**. Non tutte le versioni reperibili in rete sono aggiornate. È fondamentale studiare sulla **versione vigente consolidata**.

#### Rapporto legge-allegato

La legge (articoli) enuncia i principi generali; l'allegato 26 dettaglia come si applicano. Tuttavia, le modifiche del 2024 alla legge non sono ancora state tutte recepite nell'allegato 26. Esempio: la legge prevede la **classe N** (radioamatore novizio), ma l'allegato 26 non contiene ancora le specifiche operative.

---

### 5. 🌐 Normativa Internazionale ITU — Articolo 25

Il servizio di radioamatore è definito nel **regolamento delle radiocomunicazioni dell'ITU** (articolo 25):

> *"Un servizio di radiocomunicazioni per lo scopo di autoformazione, intercomunicazione e indagini tecniche svolte da radioamatori, persone debitamente autorizzate, interessate alla tecnica radio, esclusivamente a scopo personale e senza interesse pecuniario."*

Questo articolo stabilisce:

- La **definizione** del servizio di radioamatore
- Le **limitazioni**: comunicazioni relative all'oggetto del servizio + osservazioni di carattere personale
- La delega a ogni **amministrazione nazionale** per stabilire le potenze e le specifiche normative

> ⚠️ **Concetto d'esame**: L'articolo 25 ITU può essere oggetto di domande d'esame.

---

### 6. 🇪🇺 CEPT e Raccomandazioni TR 61-01 e TR 61-02

La **CEPT** non si limita all'Europa: alcune direttive sono recepite anche da paesi extraeuropei. Per i radioamatori, le due raccomandazioni fondamentali sono:

#### TR 61-01 — Operare all'estero

Stabilisce le regole per cui un radioamatore può operare fuori dal proprio stato. Analogia: come la patente di guida vale in altri paesi europei, la licenza radioamatoriale viene riconosciuta nei paesi aderenti alla CEPT.

**Esempio pratico**: Un radioamatore italiano che si sposta in Danimarca usa il prefisso "OZ/" davanti al proprio nominativo.

> **Regola fondamentale**: All'estero si devono seguire le **normative del paese ospitante**, non quelle del proprio paese di origine. (Es. se la banda dei 6 m non è consentita nel paese visitato, non si può usare anche se è permessa in Italia.)

#### TR 61-02 — HAREC (Harmonized Amateur Radio Examination Certificate)

Stabilisce la corrispondenza delle patenti e degli esami tra i paesi aderenti. Un esame superato in Italia, conforme alla HAREC, è riconosciuto da tutti i paesi CEPT, senza necessità di ridare l'esame.

> ⚠️ **Concetto d'esame**: Possono essere chieste domande su cosa riguardino la TR 61-01 (operare all'estero) e la TR 61-02 (reciprocità patenti/esami).

---

### 7. 📋 Articolo 134 — Definizione dell'attività di radioamatore

L'articolo 134 del D.Lgs. 259/2003 definisce l'attività di radioamatore come:

> *"L'espletamento di un servizio svolto in linguaggio chiaro o con l'uso di codici internazionalmente ammessi, esclusivamente su mezzo radioelettrico, anche via satellite, di istruzione individuale, di intercomunicazione e di studio tecnico effettuato da persone che abbiano conseguito la relativa autorizzazione generale, che si interessano alla tecnica della radioelettricità a titolo esclusivamente personale senza alcun interesse di natura economica."*

Questo articolo è l'ampliamento nazionale della definizione ITU. Stabilisce inoltre che l'attività di radioamatore è disciplinata dagli articoli del presente capo **e dall'allegato 26**.

---

### 8. 📋 Articolo 135 — Riferimento alle normative CEPT

L'articolo 135 fa riferimento alle raccomandazioni della CEPT, ne richiama l'applicabilità e stabilisce il collegamento tra la normativa nazionale e quella europea.

---

### 9. 📋 Articolo 136 — Patente e Classi di Autorizzazione

L'articolo 136 è particolarmente ricco di informazioni richieste all'esame:

#### Classi di autorizzazione

- **Classe A**: autorizzazione standard per radioamatori
- **Classe N** (novità 2024): radioamatore novizio, in addestramento, corrisponde alla classe CEPT novizio. Dettagli operativi ancora non definiti nell'allegato 26.

#### Patente vs Autorizzazione

|                     | Patente                                           | Autorizzazione                                                |
| ------------------- | ------------------------------------------------- | ------------------------------------------------------------- |
| **Cos'è**           | Certificato che attesta il superamento dell'esame | Permesso di installare e operare una stazione radioamatoriale |
| **Scadenza**        | **Non scade mai**                                 | **10 anni** (rinnovabile)                                     |
| **Come si ottiene** | Superando l'esame                                 | Richiedendola dopo aver ottenuto la patente                   |

> ⚠️ **Concetto d'esame molto frequente**: La **patente non scade**, l'**autorizzazione dura 10 anni**. Domanda a trabocchetto classica.

#### Esame ed esoneri

L'esame è obbligatorio per tutti. Esiste un **esonero parziale** per chi possiede un titolo di studio che certifica le conoscenze tecniche: in tal caso si sostiene solo la parte relativa alla **normativa** (non la parte tecnica). Non esiste titolo di studio che esoneri dalla parte normativa.

---

### 10. 📋 Articolo 137 — Requisiti per diventare radioamatore

Chi può ottenere l'autorizzazione:

- **Cittadini UE** o dello **Spazio Economico Europeo**
- Cittadini di paesi con **accordi di reciprocità**
- Età minimum: **14 anni** (l'esame può essere sostenuto prima, ma l'autorizzazione non viene rilasciata fino ai 14 anni)
- **Assenza di condanne penali** specifiche

> ⚠️ **Concetto d'esame**: L'età minima per ottenere l'autorizzazione è **14 anni**.

---

### 11. 📋 Articolo 139 — Nominativo di Chiamata

Il nominativo di chiamata:

- **Identifica** la stazione radioamatoriale
- È **assegnato dal Ministero** (MIMIT)
- Le novità del 2024 (evidenziate in giallo) includono la possibilità di **scelta del nominativo** e la possibilità di **riprendere un nominativo scaduto** o di un **familiare defunto**. Tuttavia, le modalità operative non sono ancora definite nell'allegato 26.

---

### 12. 📋 Articolo 140 — Attività all'estero

Ribadisce il principio che nel momento in cui un radioamatore opera all'estero, deve seguire la **normativa del paese ospitante**, non quella italiana. Si rimanda alle raccomandazioni CEPT (TR 61-01).

---

### 13. 📋 Articoli 141-142 — Emergenze e Assistenza

#### Articolo 141 — Comunicazioni di emergenza

In situazioni di **calamità** o contingenze particolari, il radioamatore può essere autorizzato a effettuare comunicazioni che vanno oltre i limiti normali dell'attività radioamatoriale (es. comunicazioni di soccorso, richieste d'aiuto).

#### Articolo 142 — Assistenza a manifestazioni sportive

I radioamatori possono fornire supporto di comunicazione durante manifestazioni sportive, previa comunicazione agli organi periferici del Ministero. Questa norma risale a tempi in cui non esistevano altri mezzi di comunicazione diffusi, ma è ancora in vigore.

---

### 14. 📋 Articolo 143 — Stazioni Ripetitrici (Ponti)

Le stazioni ripetitrici sono un argomento ricorrente nelle domande d'esame:

- **Uso collettivo**: le stazioni ripetitrici sono ad uso libero per tutti i radioamatori. Non possono esistere ripetitori "privati".
- **Stazioni non presidiate**: sono remote, senza controllo diretto dell'operatore.

**Regole tecniche fondamentali:**

| Parametro                       | Valore                                               |
| ------------------------------- | ---------------------------------------------------- |
| Portante dopo fine trasmissione | Max **10 secondi**                                   |
| Ripetizione del nominativo      | Ogni **10 minuti**                                   |
| Potenza massima                 | **10 W EIRP**                                        |
| Interlacciamento                | Permesso tra bande/frequenze diverse (es. VHF ↔ UHF) |

> ⚠️ **Concetto d'esame**: La potenza massima delle stazioni ripetitrici (10 W EIRP), il tempo massimo della portante (10 secondi), la frequenza di ripetizione del nominativo (10 minuti).

---

### 15. 📋 Articolo 144 — Autorizzazioni Speciali

Oltre alle persone fisiche, possono ottenere autorizzazioni radioamatoriali speciali:

- **Università** ed enti di ricerca
- **Scuole**
- Corsi militari
- **Associazioni di radioamatori** (es. nominativi IQ per le sezioni ARI)

Queste stazioni hanno un **operatore responsabile** ma il nominativo non è personale.

**Novità 2024**: È stata introdotta la possibilità legale di far operare persone **non ancora radioamatori** presso stazioni speciali (es. sezioni ARI), a scopo di formazione e avvicinamento all'attività. Le modalità operative non sono ancora dettagliate nell'allegato 26.

---

### 16. 📂 Allegato 26 — Contenuto e Importanza

L'**allegato 26** è la parte più pratica della normativa e contiene:

- Norme dettagliate sulle potenze consentite
- Procedure per ottenere nominativo e autorizzazione
- Moduli per le domande
- **Programma d'esame** (suballegato D) con:
  - Lista del **codice Q** richiesto all'esame
  - **Abbreviazioni** da conoscere
  - Riferimenti a normative IARU (band plan)
  - Articolo 25 del regolamento ITU
  - Regioni ITU (1, 2, 3)
  - Raccomandazioni CEPT
- Regole sulle stazioni ripetitrici (art. 9 dell'allegato)
- Certificazione HAREC
- Norme sulle emissioni (da trattare nella lezione successiva)

> **Nota del relatore**: Le domande d'esame sulla normativa sono spesso generate direttamente dal contenuto dell'allegato 26 e dei suoi suballegati, perché il testo è preciso e non ambiguo, rendendo facile la formulazione di domande incontestabili.

---

### 17. ❓ Sessione Domande e Risposte

#### Domande su date e leggi

Nelle domande d'esame si può trovare la richiesta di identificare quale legge governa i radioamatori (D.Lgs. 259/2003, che abroga la normativa precedente del 1992/93). Le risposte errate tipiche fanno riferimento a leggi obsolete o a normative CEI non pertinenti.

#### Shift dei ponti VHF/UHF

Lo shift delle stazioni ripetitrici (differenza tra frequenza di ricezione e trasmissione) è normato dalla normativa tecnica IARU e sarà trattato nella lezione successiva.

#### Modi di emissione

I codici dei modi di emissione (es. J3E, A1A, F3E) saranno affrontati nella prossima lezione. Il relatore avverte che, pur essendo di scarsa utilità pratica nell'attività quotidiana, sono argomento frequentissimo d'esame perché la tabelline dei modi permette di generare facilmente centinaia di domande.

---

## 🔗 Concept Map (testuale)

- ITU → definisce → servizio di radioamatore (art. 25)
- IARU → rappresenta i radioamatori → nella ITU
- CEPT → stabilisce → reciprocità tra stati europei
- TR 61-01 → regola → operatività all'estero
- TR 61-02 (HAREC) → regola → reciprocità patenti/esami
- D.Lgs. 259/2003 → è la legge italiana → sulle comunicazioni elettroniche
- Art. 134 → definisce → l'attività di radioamatore
- Art. 136 → stabilisce → classi A e N, patente e autorizzazione
- Patente → non scade | Autorizzazione → dura 10 anni
- Art. 137 → requisiti → cittadinanza UE/EEA, età ≥ 14 anni, no condanne penali
- Art. 139 → disciplina → assegnazione del nominativo
- Art. 140 → stabilisce → si seguono le norme del paese ospitante
- Art. 141 → permette → comunicazioni di emergenza oltre i limiti
- Art. 143 → disciplina → stazioni ripetitrici (uso collettivo, 10 W EIRP)
- Art. 144 → autorizzazioni speciali → per enti, scuole, associazioni
- Allegato 25 → contributi economici (50 €)
- Allegato 26 → norme attuative dettagliate + programma d'esame

---

## 📝 Key Takeaways

1. **D.Lgs. 259/2003**: La legge fondamentale per i radioamatori italiani è il Decreto Legislativo 259/2003 (Codice delle comunicazioni elettroniche). Solo ~10 articoli (134-145) riguardano specificamente i radioamatori.

2. **Patente vs Autorizzazione**: La patente (certificato d'esame) **non scade mai**. L'autorizzazione (permesso operativo) ha durata di **10 anni** ed è rinnovabile. Domanda d'esame frequentissima.

3. **Età minima**: Per ottenere l'autorizzazione di radioamatore servono almeno **14 anni**. L'esame può essere sostenuto prima.

4. **Classe A e Classe N**: La Classe A è l'autorizzazione standard; la Classe N (novizio) è stata introdotta nel 2024 ma non è ancora operativa (allegato 26 non aggiornato).

5. **CEPT TR 61-01**: Raccomandazione che regola l'operatività dei radioamatori all'estero (reciprocità). All'estero si seguono le normative del paese ospitante.

6. **CEPT TR 61-02 (HAREC)**: Certificazione armonizzata degli esami — la patente italiana è riconosciuta nei paesi CEPT senza necessità di ridare l'esame.

7. **Stazioni ripetitrici**: Ad uso collettivo (non private), potenza max 10 W EIRP, portante max 10 secondi dopo la trasmissione, nominativo ripetuto ogni 10 minuti, interlacciamento tra bande consentito.

8. **Autorizzazioni speciali (art. 144)**: Concesse a università, scuole, associazioni. Novità 2024: possibilità di far operare non-radioamatori a scopo formativo.

9. **Gerarchia normativa**: ITU (internazionale) → CEPT (europea) → D.Lgs. 259/2003 + allegati (nazionale) → decreti e circolari (attuativo).

10. **Allegato 26**: Contiene le norme pratiche e il programma d'esame. È la fonte principale delle domande d'esame sulla normativa e va letto con attenzione nella versione aggiornata/vigente.

---

## ❓ Comprehension Questions

1. Qual è la differenza fondamentale tra patente e autorizzazione radioamatoriale in termini di durata? Perché questa distinzione è rilevante per l'esame?

2. Spiega il rapporto tra gli articoli del D.Lgs. 259/2003 e l'allegato 26. Perché la legge e l'allegato possono non essere allineati temporalmente?

3. Un radioamatore italiano si reca in vacanza in un paese CEPT dove la banda dei 6 m non è consentita. Può utilizzarla? Quale principio normativo si applica?

4. A cosa servono le raccomandazioni CEPT TR 61-01 e TR 61-02? In che cosa differiscono?

5. Quali sono i requisiti per ottenere l'autorizzazione di radioamatore in Italia? Esistono esoneri per l'esame?

6. Perché le stazioni ripetitrici hanno limiti più restrittivi rispetto alle stazioni personali? Elenca almeno tre parametri regolamentati.

7. Che cos'è la classe N introdotta dalla modifica del 2024? Perché non è ancora operativa?

8. Spiega il ruolo dell'ITU, della IARU e della CEPT nella regolamentazione dell'attività radioamatoriale. Come si collegano tra loro?

9. Che cosa sono le autorizzazioni speciali (art. 144) e a quali enti possono essere concesse? Quale novità è stata introdotta nel 2024?

10. Perché il relatore consiglia di studiare solo dalla versione consolidata/aggiornata della legge? Cosa potrebbe accadere studiando da una versione non aggiornata?

---

## 📚 Glossary

- **Allegato 25** — Parte del D.Lgs. 259/2003 che disciplina i contributi economici (pagamento di 50 € per l'autorizzazione).
- **Allegato 26** — Parte del D.Lgs. 259/2003 che contiene le norme attuative dettagliate: potenze, procedure, moduli, programma d'esame, regole sulle ripetitrici.
- **Antenna artificiale** — Sinonimo di carico fittizio (dummy load), carico non irradiante per test sui trasmettitori.
- **Autorizzazione generale** — Permesso operativo per installare e utilizzare una stazione radioamatoriale. Dura 10 anni.
- **CEPT** — Conferenza Europea delle Amministrazioni di Poste e Telecomunicazioni. Organismo che definisce standard e reciprocità.
- **Classe A** — Autorizzazione radioamatoriale standard.
- **Classe N** — Autorizzazione per radioamatore novizio, prevista dalla modifica 2024. Corrisponde alla classe novizio CEPT. Dettagli operativi non ancora definiti.
- **D.Lgs. 259/2003** — Decreto Legislativo del 1° agosto 2003, Codice delle comunicazioni elettroniche. Legge fondamentale che regola i radioamatori in Italia.
- **HAREC** — Harmonized Amateur Radio Examination Certificate. Certificazione CEPT che garantisce il riconoscimento reciproco delle patenti radioamatoriali.
- **IARU** — International Amateur Radio Union. Unione internazionale che rappresenta i radioamatori nella ITU.
- **Interlacciamento** — Collegamento tra stazioni ripetitrici su bande/frequenze diverse (es. VHF ↔ UHF).
- **ITU** — International Telecommunication Union. Agenzia ONU per le telecomunicazioni.
- **MIMIT** — Ministero delle Imprese e del Made in Italy. Ente regolatore italiano per le comunicazioni elettroniche e i radioamatori (ex Ministero dello Sviluppo Economico, ex Ministero delle Poste).
- **Patente di radioamatore** — Certificato che attesta il superamento dell'esame. Non scade mai.
- **PNRF** — Piano Nazionale di Ripartizione delle Frequenze. Documento che elenca tutte le frequenze e i servizi a cui sono attribuite in Italia.
- **Stazione ripetitrice (ponte)** — Stazione automatica non presidiata che riceve e ritrasmette i segnali, posta in posizione vantaggiosa per estendere la copertura. Ad uso collettivo, max 10 W EIRP.
- **TR 61-01** — Raccomandazione CEPT che regola le modalità per operare all'estero come radioamatore.
- **TR 61-02** — Raccomandazione CEPT relativa alla HAREC (corrispondenza patenti/esami tra paesi).
- **WRC** — World Radiocommunication Conference. Conferenza mondiale sulle radiocomunicazioni, preparatoria alle riunioni ITU.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatori**:
  - **Paolo** — Coordinatore del corso. Introduce la serata e corregge i quiz sulle antenne (~13 minuti).
  - **Silvio** (IW5EDI) — Radioamatore dalla montagna pistoiese. Tiene la parte principale sulla legislazione radioamatoriale.
- 🎙️ **Moderatore**: Alessandro (Ale) — Gestisce la sessione tecnica.

---

## 📅 Informazioni Lezione

| Campo                  | Valore                                                                                                                                                                                                      |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione**            | 22                                                                                                                                                                                                          |
| **Data**               | 1 ottobre 2025                                                                                                                                                                                              |
| **Durata**             | ≈ 1 ora e 51 minuti                                                                                                                                                                                         |
| **Argomenti trattati** | 17                                                                                                                                                                                                          |
| **Parole chiave**      | Legislazione, D.Lgs. 259/2003, ITU, IARU, CEPT, MIMIT, patente, autorizzazione, classe A, classe N, TR 61-01, TR 61-02, HAREC, PNRF, stazioni ripetitrici, allegato 26, programma d'esame, articoli 134-145 |
