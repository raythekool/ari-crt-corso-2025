# 📘 Lezione 02 - Fondamenti di Elettrotecnica

## 📌 Overview

- **Materia e argomento**: Elettrotecnica di base — la resistenza elettrica, la legge di Ohm, il resistore, le resistenze in serie e in parallelo, le leggi di Kirchhoff.
- **Tempo di studio stimato**: 90–120 minuti
- **Prerequisiti**: Aver studiato la Lezione 01: concetti di tensione (volt), corrente (ampere), potenza (watt), energia, generatori in serie e in parallelo, formula $P = V \times I$.
- **Obiettivi di apprendimento**:
  - Comprendere il concetto di resistenza elettrica e la sua unità di misura (ohm)
  - Conoscere la formula della resistenza di un conduttore ($R = \rho \cdot \frac{L}{S}$) e il significato di resistività
  - Padroneggiare la legge di Ohm nelle sue tre formulazioni ($V = R \cdot I$, $I = \frac{V}{R}$, $R = \frac{V}{I}$)
  - Calcolare la potenza dissipata da un resistore con le tre formule equivalenti
  - Conoscere i resistori NTC e PTC e le loro applicazioni
  - Comprendere il concetto di generatore reale e resistenza interna
  - Applicare le leggi di Kirchhoff (nodi e maglie)
  - Calcolare la resistenza equivalente di resistori in serie e in parallelo
  - Saper usare multipli e sottomultipli delle unità di misura (kilo, mega, giga, milli, micro, nano, pico)

---

## 📖 Core Content

## 🔍 1. Riepilogo e correzione quiz della Lezione 01 (⏱ 00:02)

### 🔹 Risultati del quiz

La lezione si apre con la revisione dei risultati del quiz della Lezione 01. Il docente mostra un istogramma con i punteggi ottenuti per ciascuna delle 15 domande (dalla A alla Q). L'asse verticale rappresenta il 100% delle risposte corrette, e la soglia di successo all'esame è fissata al **60%**. Il gruppo risulta complessivamente molto al di sopra della soglia per tutte le domande, tranne la domanda L, leggermente più debole.

### 🔹 Revisione delle risposte

Vengono ripercorse le risposte corrette:

- **Domanda A**: Quale grandezza non si misura in volt? → La **potenza** (si misura in watt). La differenza di potenziale e la caduta di tensione si misurano entrambe in volt.
- **Domanda B**: Tre accumulatori da 2 V in serie → $2 + 2 + 2 = 6$ V.
- **Domanda C**: La quantità di carica Q si misura in **coulomb** (il volt misura la differenza di potenziale, il joule misura il lavoro).
- **Domanda D**: La corrente elettrica è un **flusso di elettroni**. Gli atomi difficilmente si muovono; nei conduttori (rame, alluminio, oro, argento) alcuni elettroni sono "liberi" e si muovono con facilità sotto l'effetto di una differenza di potenziale.
- **Domanda E**: $P = V \times I = 220 \times 2 = 440$ W.
- **Domanda F**: Una batteria da 10 Ah eroga 1 ampere per 10 ore ($1 \times 10 = 10$ Ah).
- **Domanda G**: Tre pile da 1,5 V in parallelo → 1,5 V (in parallelo la tensione non aumenta, aumenta la corrente erogabile).
- **Domanda H**: L'intensità di corrente si misura in **ampere**.
- **Domanda I**: $I = \frac{P}{V} = \frac{220}{220} = 1$ A.
- **Domanda L**: Quale grandezza esprime la velocità con cui viene impiegata l'energia elettrica? → La **potenza**. L'energia è il "serbatoio" (si misura in kilowattora), la potenza indica quanta energia si usa nell'unità di tempo (si misura in watt).
- **Domanda M**: Corrente che scorre in un solo verso → corrente **continua**.
- **Domanda N**: $P = V \times I = 12 \times 0{,}2 = 2{,}4$ W.
- **Domanda O**: Due generatori di tensione in serie equivalgono a un unico generatore il cui valore è la somma dei due.
- **Domanda P**: L'unità di misura della capacità delle batterie → **amperora** (Ah).
- **Domanda Q**: $P = V \times I = 1{,}5 \times 2 = 3$ W.

### 🔹 Osservazione sulla formulazione delle domande ministeriali

Il docente segnala che le domande del Ministero a volte usano un linguaggio gergale o inusuale (ad esempio "si dissipano" anziché "quale potenza viene usata"). È importante saper leggere e interpretare con attenzione la formulazione delle domande, poiché sono state scritte da persone diverse con stili variabili. L'allenamento costante aiuta a familiarizzare con queste formulazioni.

> "Molte domande del ministero, ma veramente molte, hanno delle forme su cui bisogna un attimo lavorare."

---

## ⚡ 2. La resistenza elettrica (⏱ 14:36)

### 🔹 Concetti di base

Nella lezione precedente si era visto che un **generatore** (ad esempio un accumulatore da 12 V) possiede due poli: al polo negativo vi è un'alta densità di elettroni, al polo positivo vi è una carenza di elettroni (gli atomi diventano ioni positivi). Questa differenza crea una **differenza di potenziale** tra i due poli.

Collegando il generatore a un **carico** tramite cavi elettrici, scorre una corrente. Il generatore è caratterizzato dalla sua tensione in volt; nei cavi passa la corrente misurata in ampere. Tuttavia, quanta corrente passa **lo decide il carico**, perché il carico presenta una sua **resistenza**.

La **resistenza elettrica** — l'opposizione che un materiale oppone al passaggio della corrente — è la grandezza fondamentale introdotta in questa lezione. I materiali conduttori hanno una resistenza bassa (frazioni di ohm, ad esempio 0,001 Ω); i materiali isolanti hanno resistenze molto alte (10.000, 20.000, 100.000 Ω e oltre).

> La resistenza è proprio un'opposizione nel senso vero del termine: la corrente vuole scorrere e il materiale oppone una resistenza fisica al passaggio degli elettroni.

### 🔹 L'ohm come unità di misura

La resistenza si misura in **ohm** (simbolo: **Ω**). Un ohm è la resistenza di un conduttore che viene attraversato da 1 ampere quando ai suoi capi si applica una differenza di potenziale di 1 volt.

> **Definizione:**
>
> $$1\;\Omega = \frac{1\;\text{V}}{1\;\text{A}}$$

---

## 📐 3. La resistenza di un conduttore (⏱ 19:28)

### 🔹 La formula della resistenza del conduttore

La resistenza di un pezzo di filo elettrico (conduttore) si può calcolare con la seguente formula:

> **Formula della resistenza di un conduttore:**
>
> $$R = \rho \cdot \frac{L}{S}$$
>
> dove:
>
> - $R$ = resistenza del conduttore (in ohm, Ω)
> - $\rho$ (rho) = **resistività** del materiale (costante specifica del materiale)
> - $L$ = lunghezza del conduttore (in metri)
> - $S$ = sezione del conduttore (in mm²)

La **resistività** ($\rho$) — valore tipico di ogni materiale che indica quanto esso si oppone al passaggio della corrente — è una costante: per il rame ha un certo valore, per l'argento un altro, per il ferro un altro ancora. Si trova nelle tabelle di riferimento. I materiali conduttori hanno un $\rho$ molto basso; i materiali isolanti hanno un $\rho$ molto alto.

### 🔹 Proporzionalità diretta e inversa

Dalla formula emergono due relazioni fondamentali:

1. **La resistenza è direttamente proporzionale alla lunghezza**: se la lunghezza raddoppia, la resistenza raddoppia. Questo perché $L$ è al numeratore della frazione.
2. **La resistenza è inversamente proporzionale alla sezione**: se la sezione aumenta, la resistenza diminuisce. Questo perché $S$ è al denominatore della frazione.

### 🔹 L'analogia del tubo d'acqua

Il docente utilizza l'analogia idraulica per rendere intuitiva la formula:

- Un **tubo lungo** oppone più resistenza al passaggio dell'acqua rispetto a un tubo corto → più lungo il conduttore, maggiore la resistenza.
- Un **tubo di grande diametro** lascia passare più acqua rispetto a un tubicino capillare → maggiore la sezione, minore la resistenza.

> "Pensate proprio al tubo d'acqua: è l'esempio classico."

### 🔹 Errori comuni e suggerimenti per l'esame

Nelle domande d'esame può essere chiesto se la resistenza di un conduttore "cresce al crescere della lunghezza" oppure "cresce al crescere della sezione". Bisogna ricordare:

- Cresce al crescere della **lunghezza** (direttamente proporzionale) ✅
- Diminuisce al crescere della **sezione** (inversamente proporzionale) ✅
- NON cresce al crescere della sezione ❌

---

## 📏 4. La legge di Ohm (⏱ 24:30)

### 🔹 Le tre grandezze fondamentali

A questo punto della lezione si hanno tre grandezze:

- **Tensione** ($V$), misurata in volt
- **Corrente** ($I$), misurata in ampere
- **Resistenza** ($R$), misurata in ohm

Queste tre grandezze sono legate dalla **legge di Ohm**, scoperta dal fisico tedesco Georg Simon Ohm nel XIX secolo.

### 🔹 Formulazione principale e formule inverse

> **Legge di Ohm — Formulazione principale:**
>
> $$V = R \cdot I$$
>
> La tensione ai capi di una resistenza è direttamente proporzionale alla corrente che la attraversa.

Da questa si ricavano le **formule inverse**:

> **Formula 2 — Corrente:**
>
> $$I = \frac{V}{R}$$
>
> (si ottiene dividendo entrambi i membri per $R$)

> **Formula 3 — Resistenza:**
>
> $$R = \frac{V}{I}$$
>
> (si ottiene dividendo entrambi i membri per $I$)

Queste tre formule vanno memorizzate oppure, ricordandone una, si possono ricavare le altre due con semplici passaggi algebrici.

### 🔹 Esempi di applicazione

**Esempio 1** (⏱ 28:08): 10 V applicati a una resistenza di 5 Ω. Quanta corrente scorre?

- Dato: $V = 10$ V, $R = 5$ Ω. Incognita: $I$.
- Formula: $I = \frac{V}{R} = \frac{10}{5} = 2$ A.

**Esempio 2** (⏱ 29:29): 15 V ai capi di un circuito in cui scorrono 5 A. Che resistenza presenta?

- Dato: $V = 15$ V, $I = 5$ A. Incognita: $R$.
- Formula: $R = \frac{V}{I} = \frac{15}{5} = 3$ Ω.

**Esempio 3** (⏱ 30:17): In una resistenza di 4 Ω scorrono 3 A. Che tensione è applicata?

- Dato: $R = 4$ Ω, $I = 3$ A. Incognita: $V$.
- Formula: $V = R \cdot I = 4 \times 3 = 12$ V.

### 🔹 Metodo per affrontare i problemi

Il docente suggerisce un percorso in tre passi per affrontare le domande d'esame:

1. **Leggere bene la domanda** e capire cosa viene chiesto (alcune domande sono "scivolose").
2. **Scegliere la formula giusta** in base ai dati forniti.
3. **Inserire i numeri nella formula** e svolgere il calcolo (è permesso usare una calcolatrice all'esame).

---

## 📊 5. Multipli e sottomultipli (⏱ 31:44)

### 🔹 Multipli

Nel mondo dell'elettronica si usano frequentemente i **multipli** delle unità di misura, poiché i valori reali sono spesso molto grandi o molto piccoli. I multipli seguono la **notazione ingegneristica** (potenze di 10 a passi di 3):

| Prefisso | Simbolo | Valore        | Potenza di 10 |
| -------- | ------- | ------------- | ------------- |
| **Kilo** | k       | 1.000         | $10^3$        |
| **Mega** | M       | 1.000.000     | $10^6$        |
| **Giga** | G       | 1.000.000.000 | $10^9$        |

Per le resistenze si usano tipicamente **kilohm** (kΩ) e **megaohm** (MΩ), perché 1 Ω è già una resistenza molto bassa. Nei circuiti radio si usano comunemente resistenze da 100 Ω, 1.000 Ω (1 kΩ), 10.000 Ω (10 kΩ), 100.000 Ω (100 kΩ).

Per le frequenze elevate si usano i **gigahertz** (GHz), come nella banda dei telefoni cellulari.

### 🔹 Sottomultipli

| Prefisso  | Simbolo | Valore                                         | Potenza di 10 |
| --------- | ------- | ---------------------------------------------- | ------------- |
| **Milli** | m       | 0,001 (un millesimo)                           | $10^{-3}$     |
| **Micro** | μ       | 0,000001 (un milionesimo)                      | $10^{-6}$     |
| **Nano**  | n       | 0,000000001 (un miliardesimo)                  | $10^{-9}$     |
| **Pico**  | p       | 0,000000000001 (un milionesimo di milionesimo) | $10^{-12}$    |

I sottomultipli sono tipici, ad esempio, dei **condensatori**, che si esprimono in microfarad (μF), nanofarad (nF) o picofarad (pF). Un farad è un'unità molto grande; si usano sempre sottomultipli.

### 🔹 Nota importante per i calcoli

Quando si inseriscono i valori nelle formule, è importante usare sempre le **unità di misura canoniche** (ampere, non milliampere; ohm, non kilohm; volt, non millivolt) per evitare errori nei calcoli. Convertire prima i valori nelle unità base, poi applicare la formula.

---

## 🔧 6. Il resistore (⏱ 44:13)

### 🔹 Cos'è un resistore

Il **resistore** — componente elettronico costruito appositamente per avere un determinato valore di resistenza — è l'elemento su cui tipicamente si applica la legge di Ohm nei circuiti reali. Anche un conduttore normale ha una resistenza, ma per un conduttore la resistenza è un **parametro parassita** (si vorrebbe che fosse zero). Il resistore, invece, è progettato per ostacolare parzialmente il passaggio della corrente.

Il resistore ha un **simbolo elettrico** a zigzag che intuitivamente suggerisce la difficoltà della corrente nell'attraversarlo.

### 🔹 A cosa serve un resistore

In un circuito complesso (ad esempio una radio alimentata a 12 V), ci possono essere parti che necessitano di tensioni inferiori (ad esempio 3 V). Tramite opportune resistenze, calcolate con la legge di Ohm, si può ridurre la tensione al valore desiderato. I resistori si trovano in amplificatori, oscillatori e in tutti i circuiti elettronici.

### 🔹 Il codice dei colori

Nelle resistenze più piccole, il valore è indicato tramite un **codice di colori**: bande colorate dipinte sul corpo del resistore. Ogni colore corrisponde a un numero (ad esempio rosso = 2, arancione = 3, blu = 6). Le prime bande indicano le cifre significative, una banda indica il moltiplicatore (numero di zeri), e l'ultima banda indica la **tolleranza** (ad esempio, oro = 5%). Nelle resistenze più grandi, il valore è scritto direttamente sul corpo (es. "120 Ω 5 W"). Questo argomento non è materia d'esame.

### 🔹 Potenza dissipata dal resistore

Ogni resistore, nel farsi attraversare dalla corrente, ostacola una parte dell'energia e la **dissipa in calore** (effetto Joule, visto nella Lezione 01). Tutte le resistenze, chi più chi meno, scaldano.

La potenza dissipata si può calcolare con tre formule equivalenti:

> **Formule della potenza dissipata da un resistore:**
>
> $$P = V \times I$$
>
> $$P = R \times I^2$$
>
> $$P = \frac{V^2}{R}$$

La seconda formula ($P = R \cdot I^2$) si ottiene sostituendo $V = R \cdot I$ nella formula generale:
$$P = V \cdot I = (R \cdot I) \cdot I = R \cdot I^2$$

La terza formula ($P = \frac{V^2}{R}$) si ottiene sostituendo $I = \frac{V}{R}$:
$$P = V \cdot I = V \cdot \frac{V}{R} = \frac{V^2}{R}$$

La scelta della formula dipende dai dati disponibili:

- Se si conoscono $V$ e $I$ → usare $P = V \cdot I$
- Se si conoscono $R$ e $I$ → usare $P = R \cdot I^2$
- Se si conoscono $V$ e $R$ → usare $P = \frac{V^2}{R}$

La formula $P = \frac{V^2}{R}$ è particolarmente usata anche per misurare la potenza di un trasmettitore radio: si misura la tensione su un carico noto di 50 Ω.

---

## 🌡️ 7. Resistori NTC e PTC (⏱ 53:15)

### 🔹 Definizioni

Esistono resistori speciali il cui valore in ohm **non è costante**, ma varia con la temperatura:

- **NTC** (Negative Temperature Coefficient, coefficiente di temperatura negativo) — quando la temperatura **aumenta**, il valore della resistenza **diminuisce**.
- **PTC** (Positive Temperature Coefficient, coefficiente di temperatura positivo) — quando la temperatura **aumenta**, il valore della resistenza **aumenta**.

### 🔹 Applicazioni

1. **Termometri e sensori di temperatura**: conoscendo la legge con cui la resistenza varia al variare della temperatura, si costruiscono termometri elettronici. Le sonde PTC al platino (PT100, PT300) sono state per decenni lo standard professionale per la loro elevata precisione e linearità.

2. **Controllo di temperatura**: nei frigoriferi, congelatori e termostati, i resistori NTC o PTC rilevano la temperatura e comandano l'accensione e lo spegnimento dei motori.

3. **Protezione dei circuiti all'accensione**: i resistori NTC/PTC proteggono i circuiti elettronici nel momento critico dell'accensione, quando le correnti iniziali possono essere elevate.

4. **Stabilizzazione del punto di lavoro negli amplificatori**: negli amplificatori ad alta fedeltà, i transistor di potenza scaldano e il loro **punto di lavoro** — la condizione operativa ottimale del dispositivo — tende a spostarsi, aumentando la distorsione. Resistori NTC/PTC inseriti nel circuito compensano questa deriva termica, mantenendo stabile il punto di lavoro.

5. **Controllo delle ventole nei computer**: resistori PTC nelle schede madri e nei chip rilevano la temperatura e regolano i giri delle ventole di raffreddamento.

Un partecipante racconta un'applicazione pratica ingegnosa: l'uso di un resistore PTC in serie a un elettromagnete per un distributore automatico di cibo per acquario, dove il PTC aumentava la sua resistenza dopo un certo tempo, interrompendo di fatto l'alimentazione dell'elettromagnete e proteggendolo dalla bruciatura.

---

## 🔋 8. Il resistore ideale e il generatore reale (⏱ 60:47)

### 🔹 Il resistore ideale

Il **resistore ideale** — un modello teorico — è un resistore il cui valore in ohm resta costante al variare di:

- La **frequenza** della corrente che lo attraversa
- La **temperatura** di esercizio

I resistori reali hanno sempre una certa variazione con la temperatura e la frequenza, ma il modello ideale è utile per i calcoli.

### 🔹 Il generatore ideale vs. il generatore reale

Il **generatore ideale** mantiene la tensione costante al variare della corrente assorbita dal carico. In realtà, generatori ideali non esistono.

Il **generatore reale** si schematizza come un generatore ideale seguito da una **resistenza interna** ($R_i$), di valore molto piccolo (ad esempio 0,01 Ω o 0,1 Ω).

A causa della resistenza interna, la tensione ai morsetti di uscita **diminuisce** all'aumentare della corrente assorbita, perché sulla resistenza interna vale la legge di Ohm:

> **Caduta di tensione sulla resistenza interna:**
>
> $$V_{uscita} = V_{generatore} - R_i \cdot I$$

**Esempio**: Un generatore ideale da 12 V con resistenza interna di 1 Ω:

- Con assorbimento di 1 A: $V_{uscita} = 12 - 1 \times 1 = 11$ V
- Con assorbimento di 2 A: $V_{uscita} = 12 - 1 \times 2 = 10$ V
- Con assorbimento di 3 A: $V_{uscita} = 12 - 1 \times 3 = 9$ V

La curva tensione-corrente del generatore reale è **decrescente**: parte dalla tensione nominale a vuoto e cala progressivamente all'aumentare della corrente. In gergo si dice che l'alimentatore "si inginocchia".

La resistenza interna è una caratteristica costruttiva: più il generatore è potente e "grosso", più la resistenza interna sarà bassa. Un piccolo caricabatterie per cellulari avrà una resistenza interna relativamente alta, perché è progettato per erogare poca corrente.

---

## 🔀 9. Le leggi di Kirchhoff (⏱ 67:32)

### 🔹 Prima legge di Kirchhoff (legge dei nodi)

> **Enunciato**: La somma algebrica delle correnti che confluiscono in un **nodo** di un circuito elettrico è uguale a zero.

Un **nodo** — punto di un circuito in cui confluiscono due o più rami — è il luogo dove si applica questa legge. In termini semplici: tutta la corrente che entra in un nodo deve uscirne (gli elettroni non possono accumularsi indefinitamente in un punto).

> **Formulazione matematica:**
>
> $$I_T - I_1 - I_2 = 0 \quad \Rightarrow \quad I_T = I_1 + I_2$$

**Esempio**: Se in un nodo entra una corrente $I_T = 3$ A, e questa si divide in due rami, potrebbe essere $I_1 = 1$ A e $I_2 = 2$ A, con $1 + 2 = 3$.

Per convenzione, la corrente che entra è positiva, quella che esce è negativa.

### 🔹 Seconda legge di Kirchhoff (legge delle maglie)

> **Enunciato**: La somma algebrica delle tensioni in una **maglia** chiusa di un circuito elettrico è uguale a zero.

Una **maglia** — un percorso chiuso che si può individuare all'interno di un circuito, partendo da un punto e tornandovi — è la struttura su cui si applica questa legge. In termini semplici: la tensione del generatore si ripartisce interamente sulle resistenze del circuito.

> **Formulazione matematica (esempio con 2 resistenze):**
>
> $$V_{generatore} - V_{R1} - V_{R2} = 0 \quad \Rightarrow \quad V_{generatore} = V_{R1} + V_{R2}$$

**Esempio**: Con un generatore da 12 V, se sulla prima resistenza ci sono 9 V e sulla seconda 3 V:
$$12 - 9 - 3 = 0$$

I 12 V del generatore possono ripartirsi in qualsiasi combinazione (9+3, 6+6, 8+4...) purché la somma torni a 12 V.

---

## 🔗 10. Resistori in serie (⏱ 72:11)

### 🔹 Regole fondamentali

In un circuito con resistori in **serie**, valgono tre regole:

1. **La resistenza totale** è data dalla **somma** delle singole resistenze:

> $$R_{totale} = R_1 + R_2 + R_3 + \ldots$$

2. **La corrente** ha lo **stesso valore** in qualsiasi punto del circuito (prima legge di Kirchhoff).

3. **La somma delle cadute di tensione** su ciascuna resistenza corrisponde alla tensione totale del generatore (seconda legge di Kirchhoff).

### 🔹 Esempio numerico

Tre resistenze in serie: $R_1 = 1$ kΩ, $R_2 = 2$ kΩ, $R_3 = 3$ kΩ, alimentate da un generatore da 12 V.

- $R_{totale} = 1000 + 2000 + 3000 = 6000$ Ω = 6 kΩ
- $I = \frac{V}{R_{totale}} = \frac{12}{6000} = 0{,}002$ A = 2 mA (uguale in tutto il circuito)
- Cadute di tensione:
  - $V_{R1} = R_1 \cdot I = 1000 \times 0{,}002 = 2$ V
  - $V_{R2} = R_2 \cdot I = 2000 \times 0{,}002 = 4$ V
  - $V_{R3} = R_3 \cdot I = 3000 \times 0{,}002 = 6$ V
- Verifica: $2 + 4 + 6 = 12$ V ✅

### 🔹 Ripartizione della tensione

In un circuito serie, la resistenza **più grande** si "prende" la fetta maggiore di tensione. Nell'esempio, la resistenza da 3 kΩ ha ai suoi capi 6 V (la metà della tensione del generatore), mentre la resistenza da 1 kΩ ha solo 2 V.

### 🔹 Calcolo della potenza dissipata in serie

Usando $P = V \cdot I$ (dato che $I$ è uguale per tutte e $V$ è noto per ciascuna):

- $P_{R1} = 2 \times 0{,}002 = 4$ mW
- $P_{R2} = 4 \times 0{,}002 = 8$ mW
- $P_{R3} = 6 \times 0{,}002 = 12$ mW

La resistenza **più grande** dissipa la potenza **maggiore** nel circuito serie.

### 🔹 Trucco per l'esame

Il valore della resistenza totale in serie è **sempre più grande** di ogni singola resistenza. Se tra le risposte c'è un valore inferiore a una delle resistenze date, è sicuramente sbagliato. Questo permette di escludere risposte errate "a colpo d'occhio".

---

## 🔀 11. Resistori in parallelo (⏱ 75:40)

### 🔹 Regole fondamentali

In un circuito con resistori in **parallelo**, valgono tre regole:

1. **La tensione** è la **stessa** ai capi di ogni ramo del parallelo.

2. **La corrente totale** è uguale alla **somma delle correnti** di ciascun ramo (prima legge di Kirchhoff).

3. **La resistenza equivalente** è sempre **minore** della resistenza più piccola del parallelo.

### 🔹 Formula generale della resistenza equivalente

> **Formula per n resistori in parallelo:**
>
> $$\frac{1}{R_{totale}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \ldots$$
>
> ovvero:
>
> $$R_{totale} = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \ldots}$$

### 🔹 Formula semplificata per due resistori

Quando i resistori in parallelo sono solo **due**, la formula si semplifica:

> **Formula per due resistori in parallelo:**
>
> $$R_{totale} = \frac{R_1 \times R_2}{R_1 + R_2}$$

### 🔹 Esempio numerico: parallelo di tre resistenze

Tre resistenze in parallelo: $R_1 = 100$ Ω, $R_2 = 200$ Ω, $R_3 = 500$ Ω, alimentate da un generatore da 100 V.

- Tensione su ciascuna resistenza: 100 V (uguale per tutte)
- Correnti:
  - $I_1 = \frac{100}{100} = 1$ A
  - $I_2 = \frac{100}{200} = 0{,}5$ A
  - $I_3 = \frac{100}{500} = 0{,}2$ A
- $I_{totale} = 1 + 0{,}5 + 0{,}2 = 1{,}7$ A (verifica con Kirchhoff ✅)

La resistenza **più piccola** lascia passare **più corrente**.

### 🔹 Esempio numerico: parallelo di due resistenze

$R_1 = 1000$ Ω, $R_2 = 2000$ Ω:

$$R_{totale} = \frac{1000 \times 2000}{1000 + 2000} = \frac{2.000.000}{3000} = 666{,}7\;\Omega$$

Il risultato (666,7 Ω) è inferiore a entrambe le resistenze, e in particolare è inferiore alla più piccola (1000 Ω) ✅.

### 🔹 Casi particolari

- **Due resistenze uguali** in parallelo: il risultato è la **metà** del valore di una singola resistenza.
  - Esempio: due resistenze da 1000 Ω → $R_{totale} = 500$ Ω.
  - Esempio: due resistenze da 5000 Ω → $R_{totale} = 2500$ Ω.

- **n resistenze uguali** in parallelo: il risultato è il valore di una singola resistenza diviso per $n$.
  - Esempio: tre resistenze da 1000 Ω → $R_{totale} = \frac{1000}{3} = 333{,}3$ Ω.

### 🔹 Potenza dissipata in parallelo

Usando $P = \frac{V^2}{R}$ (dato che $V$ è uguale per tutte e $R$ è noto per ciascuna):

- $P_{R1} = \frac{100^2}{100} = \frac{10.000}{100} = 100$ W
- $P_{R2} = \frac{100^2}{200} = \frac{10.000}{200} = 50$ W
- $P_{R3} = \frac{100^2}{500} = \frac{10.000}{500} = 20$ W

La resistenza **più piccola** dissipa la potenza **maggiore** nel circuito parallelo (perché lascia passare più corrente).

### 🔹 Simmetria tra serie e parallelo

I circuiti serie e parallelo si comportano in modo **speculare**:

| Caratteristica                      | Serie                                    | Parallelo                                 |
| ----------------------------------- | ---------------------------------------- | ----------------------------------------- |
| Corrente                            | Uguale in tutte le resistenze            | Si ripartisce tra i rami                  |
| Tensione                            | Si ripartisce tra le resistenze          | Uguale ai capi di tutte le resistenze     |
| $R_{totale}$                        | Somma delle resistenze                   | Minore della più piccola                  |
| Fetta maggiore di tensione/corrente | La resistenza più grande ha più tensione | La resistenza più piccola ha più corrente |
| Dissipazione maggiore               | La resistenza più grande (in serie)      | La resistenza più piccola (in parallelo)  |

### 🔹 Trucco per l'esame

Il valore della resistenza totale in parallelo è **sempre più piccolo** della resistenza più piccola. Se tra le risposte c'è un valore superiore a una delle resistenze date, è sicuramente sbagliato. Questo permette di escludere risposte errate "a colpo d'occhio", anche senza fare calcoli.

> "Nel parallelo la resistenza deve venire sempre più piccola della più piccola."

### 🔹 Come misurare le tensioni in un circuito serie

Un partecipante chiede come misurare le tensioni sulle singole resistenze in un circuito serie. Il docente spiega che bisogna posizionare i puntali del tester **all'ingresso e all'uscita** di ciascuna resistenza, senza interrompere il circuito (altrimenti il circuito si apre e le tensioni misurate non sono più quelle reali).

---

## 🔗 Concept Map (testuale)

- Resistenza elettrica → si misura in → ohm (Ω)
- Resistenza di un conduttore → dipende da → resistività ($\rho$), lunghezza ($L$), sezione ($S$)
- Resistenza → è direttamente proporzionale a → lunghezza
- Resistenza → è inversamente proporzionale a → sezione
- Resistività → è una costante specifica di → ogni materiale
- Legge di Ohm → lega → tensione ($V$), corrente ($I$), resistenza ($R$)
- $V = R \cdot I$ → formula inversa per la corrente → $I = \frac{V}{R}$
- $V = R \cdot I$ → formula inversa per la resistenza → $R = \frac{V}{I}$
- Resistore → è un componente che → oppone resistenza al passaggio della corrente
- Resistore attraversato da corrente → dissipa energia in → calore (effetto Joule)
- Potenza dissipata → si calcola con → $P = V \cdot I$, $P = R \cdot I^2$, $P = \frac{V^2}{R}$
- NTC → temperatura aumenta → resistenza diminuisce
- PTC → temperatura aumenta → resistenza aumenta
- NTC/PTC → si usano come → sensori di temperatura, protezione circuiti, stabilizzazione punto di lavoro
- Generatore reale → si modella come → generatore ideale + resistenza interna
- Resistenza interna → causa → caduta di tensione all'aumentare della corrente
- Kirchhoff (1ª legge, nodi) → la somma delle correnti in un nodo → è uguale a zero
- Kirchhoff (2ª legge, maglie) → la somma delle tensioni in una maglia → è uguale a zero
- Resistori in serie → resistenza totale → somma delle singole resistenze
- Resistori in serie → la corrente → è uguale ovunque
- Resistori in serie → la tensione → si ripartisce sulle resistenze
- Resistori in parallelo → resistenza totale → minore della più piccola
- Resistori in parallelo → la tensione → è uguale su tutti i rami
- Resistori in parallelo → la corrente → si ripartisce tra i rami

---

## 📝 Key Takeaways

1. La **resistenza elettrica** è l'opposizione che un materiale offre al passaggio della corrente e si misura in **ohm** (Ω). 1 Ω = 1 V / 1 A.

2. La resistenza di un conduttore dipende da tre fattori: la **resistività** del materiale ($\rho$, costante), la **lunghezza** (direttamente proporzionale) e la **sezione** (inversamente proporzionale): $R = \rho \cdot \frac{L}{S}$.

3. La **legge di Ohm** si esprime in tre formulazioni equivalenti: $V = R \cdot I$, $I = \frac{V}{R}$, $R = \frac{V}{I}$. Bisogna scegliere la formula giusta in base ai dati forniti dalla domanda.

4. La **potenza dissipata** da un resistore si calcola con tre formule equivalenti: $P = V \cdot I$, $P = R \cdot I^2$, $P = \frac{V^2}{R}$.

5. I resistori **NTC** diminuiscono la resistenza all'aumentare della temperatura; i **PTC** la aumentano. Si usano come sensori di temperatura e per la stabilizzazione dei circuiti.

6. Un **generatore reale** si schematizza come un generatore ideale più una resistenza interna: la tensione di uscita cala all'aumentare della corrente assorbita.

7. La **prima legge di Kirchhoff** (nodi) stabilisce che la somma delle correnti entranti in un nodo è uguale alla somma delle correnti uscenti.

8. La **seconda legge di Kirchhoff** (maglie) stabilisce che la somma algebrica delle tensioni lungo una maglia chiusa è zero.

9. In un circuito **serie**, la resistenza totale è la **somma** delle singole resistenze, la corrente è uguale ovunque, e la tensione si ripartisce proporzionalmente ai valori delle resistenze.

10. In un circuito **parallelo**, la resistenza totale è sempre **inferiore** alla più piccola delle resistenze, la tensione è uguale su ogni ramo, e la corrente si ripartisce. Per due resistori: $R_{totale} = \frac{R_1 \cdot R_2}{R_1 + R_2}$.

11. Nelle formule vanno sempre usate le **unità di misura canoniche** (ampere, volt, ohm) e non i multipli/sottomultipli, per evitare errori di calcolo.

---

## ❓ Comprehension Questions

1. Un conduttore in rame lungo 10 m ha una certa resistenza. Se raddoppio la lunghezza a 20 m mantenendo la stessa sezione, come cambia la resistenza? E se invece raddoppio la sezione mantenendo la stessa lunghezza?

2. Spiega perché un resistore dissipa energia in calore quando viene attraversato dalla corrente. Quale effetto fisico è coinvolto?

3. Un generatore ideale da 12 V con resistenza interna di 0,5 Ω eroga una corrente di 4 A. Qual è la tensione ai morsetti di uscita? Descrivi il ragionamento.

4. In un circuito serie con tre resistenze alimentate da un generatore, la resistenza più grande "si prende" la fetta maggiore di tensione. Spiega perché, utilizzando la legge di Ohm.

5. In un circuito parallelo, invece, la resistenza più piccola "si prende" la fetta maggiore di corrente. Perché questa situazione è speculare rispetto al circuito serie?

6. Se metto in parallelo due resistenze da 4700 Ω ciascuna, qual è la resistenza equivalente? E se le metto in serie? Come si distinguono le due situazioni a colpo d'occhio?

7. Un resistore NTC viene utilizzato nel termostato di un frigorifero. Spiega come funziona il meccanismo: cosa succede alla resistenza quando la temperatura nel frigorifero sale? Come viene usata questa informazione per controllare il compressore?

8. Per quale motivo le domande d'esame del Ministero possono risultare "scivolose"? Qual è il metodo suggerito dal docente per affrontarle?

9. Un circuito parallelo con tre resistenze da 100 Ω, 200 Ω e 500 Ω è alimentato da 100 V. Calcola la potenza dissipata da ciascuna resistenza. Quale resistenza scalda di più e perché?

10. Perché nelle formule è importante convertire sempre i valori nelle unità di misura canoniche (ohm, ampere, volt) prima di eseguire i calcoli? Fai un esempio pratico con i milliampere.

---

## 📚 Glossary

- **Amperora (Ah)** — Unità di misura della capacità delle batterie; indica quanta corrente una batteria può erogare per quanto tempo.
- **Caduta di tensione** — Riduzione della tensione che si verifica ai capi di un componente attraversato da corrente.
- **Codice dei colori** — Sistema di bande colorate dipinte sui resistori per indicarne il valore e la tolleranza.
- **Differenza di potenziale** — Differenza di livello elettrico tra due punti; si misura in volt.
- **Effetto Joule** — Fenomeno per cui la corrente che attraversa una resistenza produce calore.
- **Generatore ideale** — Modello teorico di generatore che mantiene la tensione costante indipendentemente dalla corrente assorbita.
- **Generatore reale** — Generatore che si modellizza come un generatore ideale in serie con una resistenza interna.
- **Giga (G)** — Prefisso che indica il miliardo ($10^9$).
- **Kilo (k)** — Prefisso che indica il migliaio ($10^3$).
- **Kirchhoff (prima legge, legge dei nodi)** — La somma algebrica delle correnti in un nodo è uguale a zero.
- **Kirchhoff (seconda legge, legge delle maglie)** — La somma algebrica delle tensioni in una maglia chiusa è uguale a zero.
- **Legge di Ohm** — Legge che lega tensione, corrente e resistenza: $V = R \cdot I$.
- **Maglia** — Percorso chiuso individuabile all'interno di un circuito elettrico.
- **Mega (M)** — Prefisso che indica il milione ($10^6$).
- **Micro (μ)** — Prefisso che indica il milionesimo ($10^{-6}$).
- **Milli (m)** — Prefisso che indica il millesimo ($10^{-3}$).
- **Nano (n)** — Prefisso che indica il miliardesimo ($10^{-9}$).
- **Nodo** — Punto di un circuito in cui confluiscono due o più rami.
- **Notazione ingegneristica** — Sistema di rappresentazione dei numeri con potenze di 10 a passi di 3 (kilo, mega, giga, milli, micro, nano...).
- **NTC (Negative Temperature Coefficient)** — Tipo di resistore la cui resistenza diminuisce all'aumentare della temperatura.
- **Ohm (Ω)** — Unità di misura della resistenza elettrica.
- **Parametro parassita** — Caratteristica indesiderata di un componente (es. la resistenza di un conduttore ideale dovrebbe essere zero).
- **Pico (p)** — Prefisso che indica $10^{-12}$.
- **PTC (Positive Temperature Coefficient)** — Tipo di resistore la cui resistenza aumenta all'aumentare della temperatura.
- **Punto di lavoro** — Condizione operativa ottimale di un dispositivo elettronico (es. transistor), che può variare con la temperatura.
- **Resistenza elettrica** — Opposizione che un materiale oppone al passaggio della corrente elettrica; si misura in ohm.
- **Resistenza interna** — Resistenza propria di un generatore reale, che causa una caduta di tensione all'aumentare della corrente erogata.
- **Resistività (ρ)** — Costante specifica di ogni materiale che esprime la sua attitudine a opporsi al passaggio della corrente.
- **Resistore** — Componente elettronico progettato per avere un determinato valore di resistenza.
- **Resistore ideale** — Modello teorico di resistore il cui valore resta costante al variare della frequenza e della temperatura.
- **Tolleranza** — Margine di variazione accettabile del valore nominale di un resistore, espressa in percentuale.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore principale**: Paolo (Paolo Cavecchioli, docente del corso)
- 👨‍🏫 **Co-relatore**: Sauro (Fabrizio/Sauro, collaboratore e membro della sezione ARI)
- 👨‍🏫 **Collaboratore**: Alessio (membro della sezione ARI, assiste nell'organizzazione)
- 🎓 **Partecipanti**: Aspiranti radioamatori del corso ARI Toscana CRT 2025, tra cui: Marco, Giancarlo, Matteo, Manuel, Antonio/Antonino, Luigi, Claudio, Vasco, Simone e altri.

---

## ⏱️ Evidenze Temporali

| Intervallo      | Argomento                                                                     |
| --------------- | ----------------------------------------------------------------------------- |
| 00:02 – 10:00   | Revisione risultati quiz Lezione 01 e correzione risposte                     |
| 10:00 – 14:30   | Discussioni organizzative e domande dei partecipanti                          |
| 14:36 – 19:00   | Introduzione alla resistenza elettrica e definizione di ohm                   |
| 19:28 – 24:00   | Formula della resistenza di un conduttore ($R = \rho \cdot L / S$)            |
| 24:30 – 31:40   | Legge di Ohm: tre formulazioni e esempi pratici                               |
| 31:44 – 35:15   | Multipli (kilo, mega, giga) e sottomultipli (milli, micro, nano, pico)        |
| 35:15 – 44:00   | Domande dei partecipanti e chiarimenti                                        |
| 44:13 – 53:10   | Il resistore: funzione, simbolo, codice colori, potenza dissipata             |
| 53:15 – 60:45   | Resistori NTC e PTC: definizioni e applicazioni pratiche                      |
| 60:47 – 67:30   | Resistore ideale, generatore ideale e generatore reale (resistenza interna)   |
| 67:32 – 72:10   | Leggi di Kirchhoff: legge dei nodi e legge delle maglie                       |
| 72:11 – 75:40   | Resistori in serie: regole, calcoli, esempi                                   |
| 75:40 – 86:40   | Resistori in parallelo: regole, formule, casi particolari, esempi             |
| 86:40 – 105:10  | Esercitazioni pratiche interattive: calcoli di potenza, corrente e resistenze |
| 105:10 – 117:59 | Informazioni organizzative: iscrizione ARI, libro di testo, chiusura          |

---

## 📅 Informazioni Lezione

- **Numero Lezione**: 02
- **Data**: 12/03/2025
- **Durata stimata**: circa 2 ore
- **Numero argomenti trattati**: 11
- **Keywords**: resistenza elettrica, ohm, legge di Ohm, resistore, resistività, NTC, PTC, generatore reale, resistenza interna, leggi di Kirchhoff, nodo, maglia, resistori in serie, resistori in parallelo, multipli, sottomultipli, potenza dissipata, effetto Joule, codice colori, kilohm, megaohm
