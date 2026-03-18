---
layout: default
permalink: /guide-studio/lezione_17.html
---

# 📘 Lezione 17 - Serata Speciale

## 📌 Overview

- **Materia**: Sicurezza elettrica e protezione contro i fulmini
- **Tempo di studio stimato**: 60–75 minuti
- **Prerequisiti**: Legge di Ohm, concetti base di corrente alternata e continua, conoscenza di base degli impianti elettrici domestici, strumenti di misura (lezione 16)
- **Obiettivi di apprendimento**:
  - Comprendere perché la corrente alternata è più pericolosa della corrente continua
  - Conoscere gli effetti della corrente elettrica sul corpo umano (soglie di percezione, tetanizzazione, fibrillazione)
  - Capire il funzionamento del sistema di protezione combinato (messa a terra + interruttore differenziale)
  - Comprendere i contatti diretti e indiretti e le relative protezioni
  - Conoscere il doppio isolamento e la separazione elettrica
  - Comprendere il rischio di fulminazione e la valutazione del rischio secondo le norme CEI 81
  - Conoscere i sistemi di protezione contro i fulmini (LPS, SPD)
  - Sapere come realizzare un corretto impianto di messa a terra per la stazione radio

---

## 📖 Core Content

### 1. 🔍 Correzione quiz Lezione 16 (⏱ 00:02–09:11)

La lezione inizia con la correzione delle domande relative alla lezione precedente sugli strumenti di misura. I risultati sono molto positivi: la maggior parte dei partecipanti ha ottenuto punteggi superiori al 90%.

Vengono riepilogate le risposte corrette principali:

- La portata di un **voltmetro** si aumenta aggiungendo una **resistenza in serie**
- L'asse orizzontale dell'**analizzatore di spettro** visualizza la **frequenza**
- L'**amperometro** si inserisce **in serie** al circuito
- Quando si commuta un voltmetro a una portata più alta, viene **aggiunta una resistenza in serie**
- L'**oscilloscopio** visualizza l'andamento nel **dominio del tempo**
- Un **wattmetro direzionale** misura la potenza diretta e quella riflessa
- Un **multimetro** misura tensione, corrente e resistenza
- La **resistenza di shunt** serve ad aumentare la portata di un **amperometro**
- Per controllare le **emissioni spurie** di un trasmettitore si usa l'**analizzatore di spettro**
- Durante le riparazioni, il trasmettitore va collegato a un **carico artificiale**

**Esercizio sul calcolo dello shunt**: un amperometro con portata 1 A e resistenza interna 10 Ω deve raggiungere una portata di 11 A. La corrente che deve passare nella resistenza di shunt è $I_{shunt} = 11 - 1 = 10$ A. Per la legge di Ohm, la resistenza di shunt è:

$$R_s = \frac{R_i \times I_{fs}}{I_{nuova} - I_{fs}} = \frac{10 \times 1}{11 - 1} = 1 \, \Omega$$

---

### 2. ⚡ Sicurezza elettrica: corrente alternata vs corrente continua (⏱ 12:15–17:27)

Il relatore **Fabrizio Badiani (IU5QUO)**, esperto di sicurezza elettrica, introduce il tema ponendo una domanda fondamentale: è più pericolosa la corrente alternata o la continua?

**La corrente alternata (AC) è molto più pericolosa della corrente continua (DC)** a parità di tensione. Questo è un fatto oggettivo supportato dalle norme CEI (Comitato Elettrotecnico Italiano).

Perché allora si usa la corrente alternata? Perché è **molto più economica da trasportare** a distanza. Se si inviano 220 V in continua su un lungo tratto di cavo, all'arrivo si misurano valori prossimi a zero; con l'alternata, la tensione si conserva praticamente intatta (es. 219 V dopo chilometri).

> Viene citata la storica diatriba tra **Edison** (sostenitore della corrente continua) e **Tesla** (inventore della corrente alternata). Edison conduceva esperimenti macabri con l'alternata per dimostrarne la pericolosità, ma Tesla vinse la "guerra delle correnti" grazie alla superiorità nel trasporto.

La ragione principale della maggiore pericolosità dell'alternata è la **frequenza di 50 Hz**: il cuore umano batte a circa 60–70 battiti al minuto (circa 1 Hz), e il corpo non riesce ad adattarsi a cambiamenti di stato così rapidi. La corrente alternata a 50 Hz può portare il cuore in **fibrillazione ventricolare**.

---

### 3. 📈 Effetti della corrente sul corpo umano (⏱ 19:52–26:06)

Il grafico tempo-corrente (scale logaritmiche) degli effetti della corrente alternata sulle persone si divide in **quattro zone**:

| Zona       | Corrente     | Effetto                                                                                                                                                     |
| ---------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zona 1** | < 0,5 mA     | Nessuna percezione — il corpo non sente nulla                                                                                                               |
| **Zona 2** | 0,5–10 mA    | Corrente percepita ma senza problematiche gravi                                                                                                             |
| **Zona 3** | 10–300 mA    | **Tetanizzazione** — i muscoli si bloccano, impossibile rilasciare la presa; possibile blocco del **diaframma** (muscolo semivolontario della respirazione) |
| **Zona 4** | > 100–300 mA | **Fibrillazione ventricolare** — il cuore batte in modo caotico, non pompa più sangue, crollo della pressione, rischio morte in circa 1 minuto              |

**Tetanizzazione** — quando la corrente alternata attraversa il corpo, i muscoli si contraggono e non si riesce a "staccarsi" dalla parte sotto tensione. La soglia di tetanizzazione è circa **10–15 mA**.

**Fibrillazione ventricolare** — il cuore, che è essenzialmente una pompa elettrica, inizia a battere in modo completamente disordinato. Il segnale ECG diventa caotico. La conseguenza è il crollo della pressione sanguigna e la mancata irrorazione del cervello. Senza intervento immediato (defibrillatore), si può morire in 1–1,5 minuti.

Il **periodo di refrattarietà** è il tempo che il sangue impiega a entrare e uscire dal cuore. Se la corrente attraversa il cuore per un tempo superiore a questo periodo, la fibrillazione è probabile.

---

### 4. 🔢 Calcolo della corrente sul corpo umano (⏱ 34:34–37:02)

Applicando la legge di Ohm si può calcolare la corrente che attraversa il corpo:

$$I = \frac{V}{R}$$

Dove:

- $V = 230$ V (tensione di rete)
- $R = 500 \div 1000$ Ω (resistenza del corpo umano secondo le norme)

> ⚠️ **La resistenza del corpo umano** varia tra **500 e 1000 Ω** secondo le norme. I bambini, avendo la pelle molto idratata, possono avere resistenza ancora più bassa.

Con $R = 1000$ Ω:

$$I = \frac{230}{1000} = 230 \, \text{mA}$$

Questo valore ricade ampiamente nella **zona di fibrillazione ventricolare** sul grafico.

---

### 5. 🛡️ Sistemi di protezione: differenziale e messa a terra (⏱ 30:00–34:06)

Il sistema di protezione dai **contatti indiretti** è un **sistema combinato** composto da:

1. **Impianto di messa a terra** — devia la corrente di guasto verso terra
2. **Interruttore differenziale** (detto anche "salvavita") — rileva la differenza tra corrente in ingresso e in uscita

**Interruttore differenziale** — contiene un toroide con tre bobine. Quando una parte della corrente "scappa" verso terra (tramite un guasto), la corrente entrante non è più uguale a quella uscente. Il differenziale rileva questa differenza e **scatta** (apre il circuito).

> Il differenziale **non è un limitatore di corrente**, è un **limitatore di tempo**: riduce il tempo di esposizione alla corrente.

Caratteristiche del differenziale ad alta sensibilità:

- Soglia di intervento: **30 mA** (0,03 A)
- Tempo di sgancio ideale: **27–28 millisecondi**
- Inventato nel **1965**

⚠️ **Manutenzione fondamentale**: premere il **tasto T** (test) almeno **una volta al mese**. Le lamelle interne di rame si ossidano nel tempo e possono "cementarsi", ritardando o impedendo lo sgancio.

---

### 6. 📡 Confronto soglie AC vs DC (⏱ 39:25–41:35)

| Parametro                                               | Corrente Alternata (AC) | Corrente Continua (DC)                           |
| ------------------------------------------------------- | ----------------------- | ------------------------------------------------ |
| Soglia di percezione                                    | 0,5 mA                  | 2 mA (4× superiore)                              |
| Soglia di tetanizzazione                                | 10–15 mA                | Non esiste vera soglia di rilascio fino a 300 mA |
| Soglia di fibrillazione (contatto > 1 periodo cardiaco) | Relativamente bassa     | Molte volte maggiore rispetto ad AC              |
| Soglia di fibrillazione (contatto < 200 ms)             | Circa uguale            | Circa uguale                                     |

> Con la corrente continua, paradossalmente, "conviene rimanerci attaccati" perché per contatti prolungati la soglia di fibrillazione è molto più alta rispetto all'alternata.

---

### 7. 🔌 Contatti diretti, indiretti e arco elettrico (⏱ 41:46–50:06)

#### Contatto indiretto

Si verifica quando si tocca una **massa metallica** (carcassa di un elettrodomestico, di una radio) che normalmente non è sotto tensione ma lo diventa a causa di un guasto. La protezione è il **sistema combinato** (messa a terra + differenziale).

**Anello di guasto** — è il percorso che la corrente compie quando si verifica un guasto: dalla carcassa, attraverso il corpo, fino al secondario del trasformatore in cabina, il cui centro stella è collegato a terra.

#### Contatto diretto

Si verifica toccando direttamente una parte sotto tensione (es. inserire le dita nella presa). In questo caso:

- Il **differenziale** se ne accorge **solo se** parte della corrente va verso terra (es. piedi scalzi)
- L'**interruttore magnetotermico** interviene: la **parte termica** protegge dai sovraccarichi, la **parte magnetica** dai cortocircuiti

#### Arco elettrico

Un rischio spesso sottovalutato. Con un trifase (380–400 V) e cortocircuiti si possono raggiungere temperature di **3000–4000 °C**. Anche a 220 V si possono superare i **1000 °C** per frazioni di secondo. Le batterie in corrente continua possono anch'esse provocare archi elettrici se maneggiate scorrettamente.

---

### 8. 🔒 Doppio isolamento e separazione elettrica (⏱ 59:00–61:23)

#### Doppio isolamento

Il costruttore garantisce che non è possibile toccare le parti sotto tensione. I dispositivi in doppio isolamento:

- Non hanno il collegamento di terra (solo 2 poli nella spina)
- È **vietato** collegarli a terra (norma CEI 64-8)
- Simbolo: quadrato dentro un quadrato
- Esempi: caricatori di cellulare, asciugacapelli (phon)

#### Separazione elettrica

Utilizza un **trasformatore di isolamento**: non c'è contatto elettrico tra primario e secondario. L'anello di guasto non si può chiudere, quindi anche toccando un'attrezzatura guasta non si prende la scossa perché la corrente non può circolare.

---

### 9. ⚡ Fulmini: fenomeno e classificazione (⏱ 65:01–69:01)

Il secondo relatore, **Gabriele (IZ5JLW)**, progettista impiantistico, introduce il tema dei fulmini.

**Fulmine** — fenomeno legato all'**elettricità atmosferica**. La parte pericolosa è la corrente elettrica generata, che si misura in **kiloampere** (migliaia di ampere).

Tipi di fulmini:

- **Nuvola → suolo** (il più comune e pericoloso per le strutture)
- **Suolo → nuvola**
- **Nuvola → nuvola**
- **Fulmini globulari** (fenomeno raro e spettacolare)

Le condizioni per lo sviluppo dei fulmini sono i **cumulonembi** — nubi a sviluppo verticale che generano temporali. Dalla nuvola si forma un **canale ionizzato** nel quale si genera la scarica elettrica. Tipicamente non si osserva un singolo fulmine ma una **serie di scariche** nello stesso punto. La seconda scarica (**scarica di ritorno**) è solitamente più luminosa della prima.

> La scarica si propaga verso la nube con una velocità di circa 1/3 della velocità della luce, ed è per questo che vediamo l'effetto luminoso.

---

### 10. 📊 Valutazione del rischio di fulminazione (⏱ 70:11–76:13)

La normativa di riferimento è la **CEI 81**, redatta dal **Comitato 81** del CEI (Comitato Elettrotecnico Italiano), associazione di diritto privato senza scopo di lucro dedicata alla normazione in ambito elettrotecnico.

#### Sorgenti di rischio

Il fulmine può essere pericoloso per:

1. La **struttura** stessa
2. Le **vicinanze** della struttura
3. Le **linee** (elettriche o dati) collegate
4. Le **vicinanze delle linee**

#### Tipi di danno e perdita

- **Danno per esseri viventi** (elettrocuzione)
- **Danno materiale**
- **Guasto impianti elettrici**

Tipi di perdita:

- Perdita di vite umane o danni permanenti
- Perdita di servizio pubblico
- Perdita di patrimonio culturale insostituibile
- Perdita economica

#### Rischio tollerabile (perdita media annua)

| Tipo di perdita               | Rischio tollerabile   |
| ----------------------------- | --------------------- |
| Vite umane / danni permanenti | $10^{-5}$ anni$^{-1}$ |
| Servizio pubblico             | $10^{-3}$ anni$^{-1}$ |
| Patrimonio culturale          | $10^{-4}$ anni$^{-1}$ |

> **Non esiste il rischio zero**, esiste solo il **rischio tollerabile**. Una struttura "autoprotetta" non significa sicura al 100%.

#### Procedura di valutazione

1. Identificare la struttura da proteggere
2. Identificare i tipi di perdita
3. Per ciascun tipo, calcolare il rischio R1
4. Confrontare R1 con il rischio tollerabile RT
5. Se R1 > RT → servono protezioni
6. Se R1 ≤ RT → struttura **autoprotetta**

---

### 11. 🏠 Fattori che influenzano la valutazione (⏱ 76:38–83:52)

#### Densità di fulminazione (Ng)

Il dato fondamentale è il numero di fulmini che cadono a terra **per anno per km²** nella zona oggetto della valutazione. Questo valore:

- Va **ricontrollato ogni 5 anni**
- Tende ad **aumentare** nel tempo a causa dei cambiamenti climatici e della tropicalizzazione

#### Tipo di ambiente

| Ambiente           | Caratteristiche                             | Livello di protezione |
| ------------------ | ------------------------------------------- | --------------------- |
| **Urbano**         | Edifici di altezza uguale o superiore       | Più protetto          |
| **Suburbano**      | Zone periferiche, edifici di altezza simile | Protezione media      |
| **Rurale/isolato** | Collina, campagna, edificio isolato         | Più pericoloso        |

#### Caratteristiche dell'edificio

- Struttura metallica, cemento armato, tetto metallico
- **H minima** = altezza del tetto/terrazza
- **H massima** = punta dell'antenna (fondamentale per i radioamatori!)

#### Valutazione prima e dopo l'antenna

La valutazione del rischio va fatta **due volte**: prima e dopo l'installazione dell'antenna. È raro che un edificio autoprotetto diventi non autoprotetto dopo l'installazione di un'antenna, a meno che non ci si trovi già "a cavallo" del limite (es. collina isolata con alta densità di fulminazione).

---

### 12. 🔧 LPS — Lightning Protection System (⏱ 85:51–87:33)

L'**LPS** (sistema di protezione esterno contro i fulmini) è composto da:

- **Captatori** — elementi metallici posti sulla sommità dell'edificio che "catturano" il fulmine
- **Maglia equipotenziale** — collega i captatori tra loro con la medesima sezione
- **Discese** (calate) — conducono la corrente dai captatori ai dispersori
- **Dispersori di terra** — scaricano la corrente nel terreno

> Le discese devono avere **tutte la stessa sezione** per scaricare l'energia in modo equo. Se c'è una sola calata, l'energia passante può strapparla dal muro.

Il collegamento tra dispersori verso il basso può essere ridondante (collegamento dispersore-dispersore nel terreno) per garantire continuità in caso di ossidazione delle giunzioni.

---

### 13. ⚙️ SPD — Scaricatori di sovratensione (⏱ 87:33–98:01)

Gli **SPD** (Surge Protection Device) proteggono gli impianti elettrici dalle sovratensioni causate dai fulmini (anche indiretti). Si dividono in **tre classi**:

| Tipo       | Posizione                              | Protezione         | Corrente max     |
| ---------- | -------------------------------------- | ------------------ | ---------------- |
| **Tipo 1** | Al contatore (gruppo di misura)        | Scariche dirette   | Fino a **50 kA** |
| **Tipo 2** | Centralino di casa, ripetuto ogni 20 m | Scariche indirette | Fino a **20 kA** |
| **Tipo 3** | Sull'utenza finale (schede, ciabatte)  | Protezione fine    | Correnti minori  |

> La cosa fondamentale degli SPD è la **vicinanza con il dispersore**. Lo scaricatore deve essere collegato a un dispersore il più vicino possibile.

Ogni SPD protegge fino a **20 m di linea**. Se la distanza tra contatore e centralino supera 20 m, la protezione va ripetuta.

Negli ambienti urbani e suburbani della Toscana (escludendo zone appenniniche e colline) è sufficiente il **tipo 2**. Gli SPD andrebbero installati **sempre e ovunque**, non solo dove obbligatorio.

Riferimenti normativi: legge 46/90 (in vigore dal 5 marzo 1990 al 22 gennaio 2008), sostituita dal **DM 37/08** (Decreto Ministro Sviluppo Economico n. 37).

---

### 14. 📡 Impianto di messa a terra per la stazione radio (⏱ 98:51–104:05)

L'impianto di messa a terra nella sala radio è fondamentale sia per la **sicurezza** sia per il **buon funzionamento** della stazione.

#### Collettore (barra equipotenziale)

Tutti i dispositivi con morsetto **GND** devono essere collegati a una **barra equipotenziale** posta nella sala radio. Questa barra si collega poi al dispersore di terra e all'impianto di terra di casa.

#### Sezioni dei conduttori

| Tipo conduttore                    | Sezione minima                                 |
| ---------------------------------- | ---------------------------------------------- |
| Conduttore di protezione (isolato) | **16 mm²**                                     |
| Conduttore di protezione (nudo)    | **25 mm²**                                     |
| Conduttore equipotenziale          | Uguale alla sezione di fase (min. **2,5 mm²**) |
| Consigliato per sala radio         | **6 mm²**                                      |

> I dispositivi in **doppio isolamento** (simbolo: quadrato nel quadrato) **non devono** essere collegati a terra: si rischierebbe di reintrodurre un potenziale di terra dove non serve.

#### Correnti di modo comune

Una buona **equipotenzialità** nella stazione radio elimina le **correnti di modo comune**, che causano:

- Spegnimento o sfarfallio del computer quando si trasmette
- Blocco del software per modi digitali
- Interferenze e rumore elettrico

> L'impianto equipotenziale è importante non solo per la protezione dai fulmini, ma anche per il **buon funzionamento complessivo** della stazione, specialmente per i modi digitali.

---

### 15. 🏗️ Consigli pratici per i radioamatori (⏱ 105:08–134:53)

Dalla sessione di domande e risposte emergono importanti consigli pratici:

#### Traliccio e messa a terra

- **Non collegare il traliccio/palo dell'antenna al dispersore di terra** in ambiente domestico: si creerebbe una "strada privilegiata" per il fulmine verso l'interno dell'abitazione
- L'impianto di messa a terra deve essere **unico**: la terra della sala radio deve essere collegata alla terra dell'impianto di casa
- Se la barra equipotenziale della sala radio è collegata a un dispersore **diverso** da quello dell'impianto domestico, si crea una situazione **pericolosa** (due impianti di terra separati)

#### Eccezione: edifici con LPS

Se l'edificio è protetto da un LPS (parafulmine), le norme CEI 81 **obbligano** la messa a terra dei supporti delle antenne. In questo caso il conduttore di terra del palo va fatto passare **all'esterno** dell'edificio (es. in tubazione PVC esterna) per evitare campi elettromagnetici nelle condutture interne.

#### Comportamento durante i temporali

- **Scollegare sempre i bocchettoni** dell'antenna durante il temporale
- Lasciarli **penzoloni e lontani** dalla radio e da tutte le superfici metalliche

#### Le antenne come captatori

- Tutte le antenne, specialmente quelle verticali, sono potenziali **captatori di fulmini**
- In ambiente urbano con edifici di altezza simile o superiore, il rischio è ridotto
- La presenza di strutture più alte nelle vicinanze (es. campanile con parafulmine) offre una protezione naturale

#### Resistenza di terra e differenziale

Con un interruttore differenziale da 0,03 A (30 mA), la resistenza di terra massima accettabile è:

$$R_T \leq \frac{50}{I_{dn}} = \frac{50}{0,03} \approx 1600 \, \Omega$$

Senza differenziale, si richiedevano valori non superiori a **20 Ω**.

---

## 🔗 Concept Map (testuale)

- **Corrente alternata 50 Hz** → è più pericolosa di → **corrente continua** (a parità di tensione)
- **50 Hz** → può provocare → **fibrillazione ventricolare** (cuore batte a ~1 Hz, non può adattarsi)
- **Corrente > 10–15 mA** → provoca → **tetanizzazione** (muscoli bloccati, non ci si stacca)
- **Corrente > 100–300 mA** → provoca → **fibrillazione ventricolare** → causa → **morte per arresto cardiaco**
- **Legge di Ohm** $I = V/R$ → determina → **corrente sul corpo** (230V/1000Ω = 230 mA)
- **Sistema combinato** = **messa a terra** + **interruttore differenziale** → protegge da → **contatti indiretti**
- **Differenziale** → misura differenza corrente ingresso/uscita → è un **limitatore di tempo**
- **Magnetotermico** → parte termica protegge da **sovraccarichi**, parte magnetica da **cortocircuiti**
- **Doppio isolamento** → elimina necessità di → **messa a terra** (vietato collegare a terra!)
- **Trasformatore di isolamento** → impedisce → **chiusura anello di guasto**
- **Fulmine** → genera corrente in → **kiloampere** → richiede → **valutazione rischio CEI 81**
- **Ng (densità fulminazione)** → influenza → **rischio calcolato R1** → confrontato con → **rischio tollerabile RT**
- **R1 > RT** → richiede → **protezioni (LPS, SPD)** ; **R1 ≤ RT** → struttura **autoprotetta**
- **LPS** = captatori + maglia + discese + dispersori → protegge → **struttura** esternamente
- **SPD** (tipo 1, 2, 3) → protegge → **impianti elettrici** dalle sovratensioni
- **Barra equipotenziale** nella sala radio → elimina → **correnti di modo comune** → migliora → **funzionamento stazione**
- **Antenna** in ambiente urbano → è un **captatore** ma → rischio ridotto se edifici circostanti sono di altezza simile o superiore

---

## 📝 Key Takeaways

1. **La corrente alternata a 50 Hz è molto più pericolosa della corrente continua** a parità di tensione, perché può indurre fibrillazione ventricolare nel cuore umano. La soglia di percezione AC è 0,5 mA contro i 2 mA della DC.

2. **La resistenza del corpo umano è compresa fra 500 e 1000 Ω** secondo le norme. Con 230 V di rete, la corrente che attraversa il corpo può raggiungere 230–460 mA, ben oltre la soglia di fibrillazione.

3. **Il sistema di protezione combinato** (messa a terra + interruttore differenziale da 30 mA) è la difesa fondamentale contro i contatti indiretti. L'interruttore differenziale non limita la corrente ma il tempo di esposizione.

4. **Il tasto test del differenziale va premuto almeno una volta al mese** per evitare che le lamelle si ossidino e si cementino, impedendo lo sgancio in caso di guasto.

5. **I dispositivi in doppio isolamento non devono essere collegati a terra** (è vietato). Il trasformatore di isolamento impedisce la chiusura dell'anello di guasto.

6. **Il rischio di fulminazione si valuta secondo la CEI 81**, confrontando il rischio calcolato R1 con il rischio tollerabile RT ($10^{-5}$ anni$^{-1}$ per perdita di vite umane). Se R1 ≤ RT la struttura è autoprotetta.

7. **La densità di fulminazione (Ng)** aumenta nel tempo a causa dei cambiamenti climatici. L'ambiente (urbano, suburbano, rurale) influenza significativamente il livello di rischio.

8. **Gli SPD (scaricatori di sovratensione)** andrebbero installati sempre: tipo 1 al contatore (50 kA), tipo 2 al centralino (20 kA, ripetuto ogni 20 m), tipo 3 sulle utenze finali.

9. **L'impianto di messa a terra deve essere unico**: la terra della stazione radio e la terra dell'impianto domestico devono essere collegate. Avere due impianti di terra separati è pericoloso.

10. **Non collegare il traliccio/palo antenna al dispersore di terra** in ambiente domestico: si crea un percorso privilegiato per il fulmine. Scollegare sempre i bocchettoni dell'antenna durante i temporali.

---

## ❓ Comprehension Questions

1. Perché la corrente alternata a 50 Hz è più pericolosa della corrente continua a parità di tensione? Quali sono le differenze nelle soglie di percezione, tetanizzazione e fibrillazione?

2. Un radioamatore tocca accidentalmente la carcassa metallica di un amplificatore lineare andato in dispersione. Descrivi cosa succede se: (a) c'è il sistema combinato messa a terra + differenziale, (b) c'è solo la messa a terra senza differenziale, (c) non c'è né messa a terra né differenziale.

3. Perché il differenziale viene definito "limitatore di tempo" e non "limitatore di corrente"? Qual è la differenza pratica?

4. Spiega perché è vietato collegare a terra un dispositivo in doppio isolamento. Cosa potrebbe accadere?

5. In che modo l'installazione di un'antenna può modificare la valutazione del rischio di fulminazione di un edificio? Quali parametri cambiano?

6. Qual è la differenza tra uno scaricatore di sovratensione di tipo 1, tipo 2 e tipo 3? In quali posizioni dell'impianto vanno installati?

7. Perché è importante che l'impianto di messa a terra sia unico e non si abbiano due impianti separati (uno per la stazione radio e uno per la casa)?

8. In base alla legge di Ohm, calcola la corrente che attraversa il corpo di una persona che tocca una fase a 230 V, considerando una resistenza corporea di 700 Ω. In quale zona del grafico tempo-corrente ricade questo valore?

9. Come funziona il collegamento equipotenziale nella sala radio e perché è importante anche per il buon funzionamento della stazione (non solo per la sicurezza)?

10. Perché si consiglia di scollegare i bocchettoni dell'antenna durante un temporale piuttosto che collegare il palo antenna a terra?

---

## 📚 Glossary

- **Anello di guasto** — percorso completo che la corrente compie in caso di guasto, dalla massa attraverso il corpo e il terreno fino al centro stella del trasformatore
- **Arco elettrico** — scarica luminosa ad altissima temperatura (fino a 3000–4000 °C) che si verifica durante cortocircuiti
- **Barra equipotenziale** — elemento conduttore al quale si collegano tutte le masse della stazione radio per portarle allo stesso potenziale
- **Captatore** — elemento metallico posto sulla sommità di un edificio che intercetta il fulmine nell'ambito di un LPS
- **CEI** — Comitato Elettrotecnico Italiano, associazione di diritto privato senza scopo di lucro per la normazione elettrotecnica
- **Cenelec** — organismo europeo di normazione elettrotecnica
- **Contatto diretto** — contatto con una parte normalmente sotto tensione
- **Contatto indiretto** — contatto con una massa metallica che diventa sotto tensione a causa di un guasto
- **Corrente di modo comune** — corrente parassita che causa interferenze tra dispositivi non correttamente equipotenzializzati
- **Cumulonembo** — nube a sviluppo verticale che genera temporali e fulmini
- **Differenziale (interruttore)** — dispositivo di protezione che rileva la differenza tra corrente entrante e uscente e sgancia il circuito; contiene un toroide con tre bobine
- **Dispersore** — elemento metallico (palina, rete elettrosaldata) interrato che scarica la corrente nel terreno
- **Dispersore di fatto** — dispersore costituito dai ferri del cemento armato, non intenzionalmente installato per la messa a terra
- **DM 37/08** — Decreto Ministeriale che ha sostituito la legge 46/90 per la regolamentazione degli impianti
- **Doppio isolamento** — sistema di protezione in cui il costruttore garantisce l'impossibilità di contatto con parti sotto tensione; simbolo: quadrato dentro quadrato
- **ECG (Elettrocardiogramma)** — registrazione del segnale elettrico del cuore
- **Fibrillazione ventricolare** — condizione in cui il cuore batte in modo caotico e non pompa più sangue; potenzialmente letale in 1–1,5 minuti
- **GND** — morsetto di messa a terra presente sugli apparati radio
- **IEC** — International Electrotechnical Commission, organismo internazionale di normazione
- **Legge 46/90** — prima legge italiana sulla sicurezza degli impianti elettrici (1990–2008)
- **LPS (Lightning Protection System)** — sistema di protezione esterno contro i fulmini (captatori + maglia + discese + dispersori)
- **Magnetotermico** — interruttore con protezione magnetica (cortocircuiti) e termica (sovraccarichi)
- **Massa estranea** — elemento conduttore normalmente non in tensione che può andare in tensione per guasto di isolamento
- **Messa a terra** — collegamento elettrico intenzionale al terreno tramite dispersori
- **Ng** — densità di fulminazione, numero di fulmini per km² per anno in una zona
- **PES/PAV** — Persona Esperta / Persona Avvertita in ambito sicurezza elettrica
- **Periodo di refrattarietà** — tempo che il sangue impiega a entrare e uscire dal cuore
- **Rischio tollerabile** — livello di rischio considerato accettabile dalla normativa
- **Separazione elettrica** — protezione tramite trasformatore di isolamento che impedisce la chiusura dell'anello di guasto
- **Sistema TT** — sistema di distribuzione elettrica "Terra-Terra" dove la messa a terra è a carico dell'utente
- **Sistema TN** — sistema di distribuzione con messa a terra fornita dal distributore
- **SPD (Surge Protection Device)** — scaricatore di sovratensione; tipo 1 (50 kA), tipo 2 (20 kA), tipo 3 (protezione fine)
- **Struttura autoprotetta** — struttura il cui rischio calcolato è inferiore al rischio tollerabile
- **Tetanizzazione** — contrazione involontaria e persistente dei muscoli causata dal passaggio di corrente alternata (soglia: 10–15 mA)

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore 1**: Fabrizio Badiani (IU5QUO) — esperto di sicurezza elettrica, formatore PES/PAV
- 👨‍🏫 **Relatore 2**: Gabriele (IZ5JLW) — progettista impiantistico e acustico, radioamatore (telegrafia con tasti meccanici)
- 👨‍🏫 **Moderatore**: Paolo — coordinatore del corso

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione numero**   | 17                                                                                                                                                                                                                                                                                                            |
| **Data**             | 02/07/2025                                                                                                                                                                                                                                                                                                    |
| **Durata stimata**   | ~2 ore 15 minuti                                                                                                                                                                                                                                                                                              |
| **Numero argomenti** | 15                                                                                                                                                                                                                                                                                                            |
| **Parole chiave**    | sicurezza elettrica, corrente alternata, corrente continua, fibrillazione ventricolare, tetanizzazione, differenziale, messa a terra, contatto diretto, contatto indiretto, doppio isolamento, fulmini, CEI 81, LPS, SPD, scaricatore di sovratensione, barra equipotenziale, dispersore, rischio tollerabile |
