# 📘 Lezione 03 - Circuiti Elettrici

## 📌 Overview

- **Materia e argomento**: Elettrotecnica — la corrente alternata: sinusoide, frequenza, periodo, valori caratteristici della tensione alternata, fase, potenza in corrente alternata (potenza reale, apparente, reattiva), fattore di potenza (cos φ).
- **Tempo di studio stimato**: 90–120 minuti
- **Prerequisiti**: Aver studiato le Lezioni 01 e 02: concetti di tensione (volt), corrente (ampere), potenza (watt), energia, legge di Ohm nelle tre formulazioni ($V = R \cdot I$, $I = \frac{V}{R}$, $R = \frac{V}{I}$), resistenze in serie e in parallelo, calcolo della potenza dissipata ($P = V \cdot I$, $P = \frac{V^2}{R}$, $P = I^2 \cdot R$).
- **Obiettivi di apprendimento**:
  - Comprendere la differenza tra corrente continua e corrente alternata
  - Conoscere il concetto di sinusoide e come viene generata (sviluppo circolare)
  - Padroneggiare le grandezze frequenza e periodo e la relazione $f = \frac{1}{T}$
  - Comprendere il principio di funzionamento di un alternatore
  - Distinguere i diversi modi di esprimere il valore di una tensione alternata: istantanea, efficace, di picco, picco-picco, valor medio
  - Applicare le relazioni tra tensione efficace, di picco e picco-picco ($V_p = 1{,}41 \cdot V_{eff}$, $V_{pp} = 2 \cdot V_p$)
  - Comprendere il concetto di fase, controfase e quadratura tra sinusoidi
  - Calcolare la potenza in corrente alternata su carico resistivo e su carico reattivo
  - Conoscere la potenza reale (attiva), la potenza apparente e la potenza reattiva
  - Comprendere il significato del fattore di potenza $\cos\varphi$

---

## 📖 Core Content

## 🔍 1. Riepilogo e correzione quiz della Lezione 02 (⏱ 00:01)

### 🔹 Risultati del quiz

La lezione si apre con la revisione dei risultati del quiz della Lezione 02, dedicata alla legge di Ohm. Il docente mostra un istogramma dei risultati: la soglia di successo all'esame è fissata al **60%**, e il gruppo è risultato sempre superiore all'**80%**, tranne che nelle domande P e Q (relative alla potenza). Il docente sottolinea che si tratta di una prestazione brillantissima.

### 🔹 Revisione delle risposte

Vengono ripercorse le risposte corrette:

- **Domanda A**: La legge di Ohm dice che $I = \frac{V}{R}$. Le formulazioni errate presentate nel quiz invertivano le relazioni ($V = \frac{R}{I}$ è sbagliata, $I = R \cdot V$ è sbagliata). (⏱ 01:22)
- **Domanda B**: Una resistenza attraversata da 2 A con tensione di 12 V → $R = \frac{V}{I} = \frac{12}{2} = 6\;\Omega$. Il metodo consigliato: individuare i dati del problema, trovare la formula adatta, sostituire. (⏱ 01:41)
- **Domanda C**: Un generatore reale di tensione si modella come un generatore ideale con in serie una **resistenza interna**. Più corrente si assorbe, più la tensione di uscita cala. (⏱ 02:22)
- **Domanda D**: Resistenza di due resistori in serie → $R_{tot} = R_1 + R_2$. (⏱ 02:53)
- **Domanda E**: Resistenza totale di tre resistenze in parallelo → $\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$, equivalentemente $R = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}}$. (⏱ 03:04)
- **Domanda F**: Due resistori in serie da 1 Ω e 2 Ω → $R = 1 + 2 = 3\;\Omega$. (⏱ 04:18)
- **Domanda G**: Se si raddoppia la corrente attraverso una resistenza, la tensione raddoppia, poiché $V = R \cdot I$ e la tensione è direttamente proporzionale alla corrente. (⏱ 04:31)
- **Domanda H**: La resistenza si oppone al flusso di elettroni — come dice il nome, "resiste". (⏱ 05:14)
- **Domanda I**: 500 Ω in serie a 200 Ω → $R = 500 + 200 = 700\;\Omega$. (⏱ 05:28)

### 🔹 Il parallelo di tre resistenze: calcolo e metodo "a occhio" (⏱ 05:41)

La domanda J chiede il valore del parallelo di tre resistenze da 15, 24 e 37 Ω. Il docente illustra due approcci:

**Approccio con la formula:**

$$R = \frac{1}{\frac{1}{15} + \frac{1}{24} + \frac{1}{37}} \approx 7{,}38\;\Omega$$

**Approccio "a occhio" (stima ragionata):**

1. Il valore del parallelo è **sempre più basso** della resistenza più piccola → si scarta qualunque risposta ≥ 15 Ω.
2. Si approssimano 24 Ω e 37 Ω entrambe a circa 30 Ω → il parallelo di 30 e 30 dà 15 Ω.
3. 15 Ω in parallelo con l'altra resistenza da 15 Ω → circa 7,5 Ω → risposta: **7,38 Ω**.

> "Quando si mettono resistenze in parallelo, il valore di un parallelo è sempre più basso di ogni singola resistenza."

Il docente suggerisce fortemente di procurarsi una **calcolatrice** per l'esame (non lo smartphone). Si menziona che il risultato esatto sarebbe 7,39 Ω ma il quiz ministeriale riporta 7,38 Ω per arrotondamento; il docente avverte che i quiz ministeriali non sono perfetti e bisogna scegliere la *risposta migliore*.

### 🔹 Metodo alternativo per il parallelo (intervento di Sauro) (⏱ 09:30)

**Sauro** suggerisce un metodo alternativo per tre resistenze in parallelo: usare la formula semplificata per due resistenze $R = \frac{R_1 \cdot R_2}{R_1 + R_2}$ applicandola in due passaggi:

1. Calcolare il parallelo delle prime due resistenze.
2. Usare il risultato come nuova resistenza e calcolare il parallelo con la terza.

### 🔹 Altre domande del quiz (⏱ 12:27)

- **Domanda M**: 1 kΩ in serie a 3 kΩ → $R = 1 + 3 = 4$ kΩ. (⏱ 12:34)
- **Domanda N**: 30 kΩ in parallelo a 15 kΩ → $R = \frac{30 \times 15}{30 + 15} = \frac{450}{45} = 10$ kΩ. Il docente ribadisce: scartare il valore 45 kΩ perché il parallelo è sempre inferiore alla resistenza più piccola. (⏱ 12:45)
- **Domanda O**: In parallelo, la resistenza totale di due resistori è sempre **minore** del valore di ciascun singolo resistore. (⏱ 16:36)

### 🔹 Domande sulla potenza (⏱ 16:54)

- **Domanda P**: Potenza erogata con $V = 10$ V e $R = 5$ Ω → formula da scegliere: $P = \frac{V^2}{R}$, perché i dati sono tensione e resistenza. Calcolo: $P = \frac{10^2}{5} = \frac{100}{5} = 20$ W. (⏱ 17:01)
- **Domanda Q**: Resistore da 200 Ω attraversato da 3 A → formula $P = I^2 \cdot R$, perché i dati sono corrente e resistenza. Calcolo: $P = 3^2 \times 200 = 9 \times 200 = 1800$ W. (⏱ 19:14)

### 🔹 Metodo generale per le domande con calcoli

Il docente ribadisce il metodo universale per affrontare le domande d'esame con calcoli:

1. **Leggere bene la domanda**
2. **Identificare i due dati** forniti (tensione e resistenza, corrente e resistenza, tensione e corrente…)
3. **Scegliere la formula giusta** tra le tre formulazioni della legge di Ohm o le tre formulazioni della potenza
4. **Eseguire il calcolo**

> "Il metodo alla fine è sempre lo stesso: leggete bene la domanda, capite i dati che la domanda vi dà — saranno sempre due numeri — e trovate la formula giusta."

---

## ⚡ 2. La corrente alternata (⏱ 21:04)

### 🔹 Posizione nel programma del corso

Questa è la terza lezione. Dopo le grandezze elettriche di base (Lezione 01) e la corrente continua con resistore e legge di Ohm (Lezione 02), si entra nel tema della **corrente alternata**. Nelle prossime due lezioni (4 e 5) si parlerà di condensatore e induttore (tenute da Sauro), completando la parte di elettronica. Seguirà poi la radiotecnica: filtri, trasmettitori, ricevitori.

### 🔹 Corrente continua vs corrente alternata (⏱ 28:05)

La **corrente continua** (CC o DC) è un flusso di cariche elettriche (elettroni) che scorre sempre nello stesso verso, dal polo negativo al polo positivo di un generatore (pila, batteria, alimentatore). La tensione che la genera ha un polo positivo che resta sempre positivo e un polo negativo che resta sempre negativo.

La **corrente alternata** (CA o AC) è una corrente che **inverte il senso di scorrimento** un certo numero di volte nell'unità di tempo. Il generatore non ha più un polo fisso positivo e uno fisso negativo, ma due poli la cui polarità si alterna nel tempo. Quando un polo è positivo, l'altro è negativo; l'istante successivo si scambiano. Di conseguenza la corrente "va e torna" rispetto al generatore.

La corrente alternata è generata da una **tensione alternata** ed è prodotta da dispositivi chiamati **alternatori**.

In corrente continua la tensione si indica semplicemente con $V$ (es. 12 V costanti). In corrente alternata la tensione varia col tempo, quindi si scrive $V(t)$: il valore può cambiare istante per istante.

### 🔹 L'andamento sinusoidale (⏱ 30:33)

Osservando su un grafico (asse orizzontale = tempo, asse verticale = tensione o corrente):

- La **corrente continua** appare come una linea orizzontale con valore costante (es. 1 A).
- La **corrente alternata sinusoidale** ha una forma "sinuosa": parte da zero, sale a un picco massimo, scende con continuità fino a un minimo (negativo), poi risale. Non presenta spigoli: è una curva liscia.

La **sinusoide** — dal latino *sinus* — è la forma d'onda fondamentale in campo elettronico. Possiede moltissime proprietà che verranno esplorate nel corso.

---

## 📈 3. Frequenza e periodo (⏱ 32:02)

### 🔹 Frequenza

La **frequenza** — simbolo $f$ — è il numero di cicli completi che un'onda compie in un secondo. Si misura in **hertz** (Hz).

Un ciclo completo corrisponde al percorso: da zero → al massimo positivo → ritorno a zero → al minimo negativo → ritorno a zero.

**Esempio pratico:** la rete elettrica ENEL fornisce una tensione con frequenza di **50 Hz**, ovvero la sinusoide compie 50 cicli completi al secondo. Se la si osservasse con un **oscilloscopio**, si vedrebbe una forma sinusoidale che si ripete 50 volte al secondo.

In campo radio le frequenze sono molto più elevate: si parla di **megahertz** (MHz), cioè milioni di hertz. Un trasmettitore a 10 MHz produce 10 milioni di cicli al secondo.

### 🔹 Periodo

Il **periodo** — simbolo $T$ — è il tempo necessario perché la sinusoide compia un ciclo completo. Si misura in **secondi** (s), ma per segnali veloci si usano sottomultipli: millisecondi (ms), microsecondi (μs), nanosecondi (ns).

Si misura l'intervallo di tempo tra due punti omologhi (corrispondenti) della sinusoide, tipicamente tra due massimi consecutivi.

### 🔹 Relazione tra frequenza e periodo (⏱ 35:56)

Frequenza e periodo sono **l'inverso** l'uno dell'altro:

$$f = \frac{1}{T} \qquad\qquad T = \frac{1}{f}$$

Dove:

- $f$ = frequenza in hertz (Hz)
- $T$ = periodo in secondi (s)

**Esempio con la rete ENEL (50 Hz):**

$$T = \frac{1}{f} = \frac{1}{50} = 0{,}02\;\text{s} = 20\;\text{ms}$$

**Verifica inversa:**

$$f = \frac{1}{T} = \frac{1}{0{,}02} = 50\;\text{Hz}$$

Dire che un'onda ha frequenza 50 Hz **o** periodo 20 ms è esattamente la stessa cosa: si descrive la stessa onda, una volta dicendo quanti cicli compie al secondo, l'altra dicendo quanto tempo impiega per un ciclo.

> "Dire che un'onda ha una frequenza di 50 Hz o un periodo di 20 millisecondi è esattamente la stessa cosa."

**Esempio con 1 MHz:**

$$T = \frac{1}{1\;000\;000} = 0{,}000\;001\;\text{s} = 1\;\mu\text{s}$$

### 🔹 Attenzione ai multipli e sottomultipli (⏱ 63:22)

Il docente e un corsista (Marco) ribadiscono un punto fondamentale: nelle formule **bisogna usare sempre le stesse unità di misura**. Se si lavora con la frequenza, questa deve essere espressa in hertz (non in MHz); se si lavora con la resistenza, deve essere in ohm (non in kΩ). Come regola: riportare tutto alle unità di misura fondamentali prima di fare i calcoli.

> "Si sommano mele con mele, pere con pere."

---

## 📡 4. Generazione della sinusoide: il cerchio e il raggio rotante (⏱ 45:57)

### 🔹 Sviluppo geometrico della sinusoide

La sinusoide si ottiene geometricamente da un **moto circolare uniforme**. Si consideri una circonferenza con un raggio che ruota attorno al centro a **velocità angolare costante**:

1. Man mano che il raggio ruota, il suo estremo descrive punti sulla circonferenza.
2. Si proietta l'altezza del punto (la distanza verticale dall'asse orizzontale) su un grafico dove l'asse orizzontale rappresenta l'angolo percorso (in gradi) o il tempo.
3. La curva risultante è una **sinusoide**.

**Corrispondenza angolo-sinusoide:**

| Angolo | Posizione sulla sinusoide   |
| ------ | --------------------------- |
| 0°     | Zero (passaggio per l'asse) |
| 90°    | Massimo positivo (picco)    |
| 180°   | Zero (passaggio per l'asse) |
| 270°   | Minimo negativo (valle)     |
| 360°   | Zero (ciclo completo)       |

Ogni **360°** (angolo giro) la sinusoide compie un ciclo completo.

### 🔹 Velocità di rotazione e frequenza

Se il raggio ruota più velocemente, la sinusoide ha una **frequenza più alta** (periodo più breve, forma più compressa). Se il raggio ruota più lentamente, la sinusoide ha una frequenza più bassa (periodo più lungo). Se il raggio ruota a velocità non costante (a volte più veloce, a volte più lento), si ottiene una sinusoide con periodo variabile — è il principio della **modulazione di frequenza**. (⏱ 82:54)

---

## 🔧 5. L'alternatore (⏱ 54:46)

### 🔹 Principio di funzionamento

L'alternatore è il dispositivo che produce corrente alternata sinusoidale. Il suo funzionamento si basa sulle scoperte di **Ørsted** e di **Faraday**: quando una **spira** di filo conduttore si muove in un **campo magnetico**, in modo che la quantità di campo magnetico intercettata dalla spira vari, su quella spira nasce una **tensione** (e di conseguenza può scorrere una corrente).

> ⚠️ *Il funzionamento dettagliato dell'alternatore non è materia di esame, ma viene spiegato per completezza culturale.*

### 🔹 Struttura dell'alternatore

- Un **asse di rotazione** (albero meccanico) attorno a cui può girare una **spira** (o un avvolgimento) di filo conduttore metallico.
- La spira è immersa in un **campo magnetico** generato da un magnete permanente (o da elettromagneti), con polo Nord (N) e polo Sud (S).
- La spira viene fatta **ruotare** attorno all'asse.

### 🔹 Perché produce una sinusoide

Durante la rotazione:

- Quando la spira è **parallela** alle linee di forza del campo magnetico, intercetta **pochissimo** campo → tensione minima.
- Quando la spira è **perpendicolare** alle linee di forza (parallela alle facce del magnete), intercetta il **massimo** campo → tensione massima.

Siccome il moto è circolare, l'intercettazione del campo segue la stessa legge dello sviluppo geometrico del cerchio → la tensione generata è **sinusoidale**.

La parte che ruota si chiama **rotore**. Il rotore contiene le spire di filo elettrico. Il campo magnetico può essere generato da magneti permanenti o da elettromagneti.

---

## 📊 6. I valori della tensione alternata (⏱ 65:05)

### 🔹 Premessa: molteplicità di parametri

Con la corrente continua, basta un solo numero per descrivere la tensione (es. "batteria da 9 V"). Con la corrente alternata, dato che la tensione varia continuamente, servono **più parametri** per descriverla. Ce ne sono cinque principali.

### 🔹 Tensione istantanea (⏱ 65:37)

La **tensione istantanea** è il valore della tensione in un preciso istante di tempo. Come una "fotografia" della sinusoide in un dato momento: può assumere qualsiasi valore tra il picco positivo e il picco negativo. Non è oggetto di domande d'esame, ma è importante conoscerne il concetto.

### 🔹 Tensione efficace (valore efficace, RMS) (⏱ 66:18)

La **tensione efficace** (in inglese **RMS** — Root Mean Square) è il valore di tensione alternata che, applicato a un carico, produce lo **stesso lavoro** (stessa dissipazione di calore) di una tensione continua di pari valore.

**Esempio:** se l'ENEL fornisce 220 V (efficaci) e si collega una stufetta elettrica, il calore prodotto è identico a quello che si otterrebbe con una tensione continua di 220 V.

Quando si indica un valore di tensione alternata senza ulteriori specificazioni, **si intende sempre il valore efficace**. L'ENEL dice "220 V" e sottintende "efficaci".

### 🔹 Tensione di picco ($V_p$) (⏱ 67:38)

La **tensione di picco** è il valore massimo raggiunto dalla sinusoide, corrispondente alla cresta dell'onda. È il massimo valore istantaneo.

$$V_p = 1{,}41 \times V_{eff} = \sqrt{2} \times V_{eff}$$

Il fattore 1,41 corrisponde a $\sqrt{2} \approx 1{,}4142$.

### 🔹 Tensione picco-picco ($V_{pp}$) (⏱ 68:16)

La **tensione picco-picco** rappresenta l'escursione totale della sinusoide, dal minimo negativo al massimo positivo:

$$V_{pp} = 2 \times V_p$$

### 🔹 Valor medio ($V_m$) (⏱ 68:41)

Il **valor medio** si calcola come l'altezza di un rettangolo che ha la stessa base di un semiperiodo della sinusoide e **la stessa area** sotto la curva del semiperiodo. In pratica è la media di tutti i valori della sinusoide in un semiperiodo.

$$V_m = 0{,}9 \times V_{eff} = 0{,}637 \times V_p$$

### 🔹 Riepilogo delle relazioni

| Grandezza                       | Formula                       | Esempio (ENEL) |
| ------------------------------- | ----------------------------- | -------------- |
| Tensione efficace ($V_{eff}$)   | dato di riferimento           | **220 V**      |
| Tensione di picco ($V_p$)       | $V_p = 1{,}41 \times V_{eff}$ | **311 V**      |
| Tensione picco-picco ($V_{pp}$) | $V_{pp} = 2 \times V_p$       | **622 V**      |
| Valor medio ($V_m$)             | $V_m = 0{,}9 \times V_{eff}$  | **198 V**      |

> Nella presa elettrica di casa, l'ENEL dichiara 220 V efficaci, ma l'escursione picco-picco reale è di **622 V** (da −311 V a +311 V).

### 🔹 Utilità pratica dei diversi valori (⏱ 72:22)

- La **tensione efficace** serve per calcolare il lavoro prodotto (potenza, calore, movimento). Tutti i generatori commerciali indicano la tensione efficace.
- La **tensione di picco** serve per dimensionare gli **isolamenti**: non basta un isolante che regga 230 V se la tensione di picco raggiunge 311 V. Bisogna dimensionare gli isolanti almeno per la tensione di picco (350–400 V o più nel caso della rete ENEL).

---

## 🔄 7. La fase tra sinusoidi (⏱ 73:44)

### 🔹 Concetto di fase

Ogni punto del ciclo di una sinusoide può essere identificato con un **angolo in gradi** (da 0° a 360°):

- 0° → passaggio per lo zero (in salita)
- 90° → picco positivo
- 180° → passaggio per lo zero (in discesa)
- 270° → picco negativo
- 360° → fine del ciclo (coincide con 0° del ciclo successivo)

Quando si confrontano **due sinusoidi**, si può misurare la loro **differenza di fase**: quanto una è "anticipata" o "ritardata" rispetto all'altra.

### 🔹 Sinusoidi in fase

Due sinusoidi sono **in fase** quando raggiungono simultaneamente i picchi, gli zeri e le valli. Lo sfasamento è **0°**. Se si sommano, il risultato è una sinusoide con ampiezza pari alla somma delle due ampiezze (esattamente come batterie in serie nello stesso verso).

### 🔹 Sinusoidi in controfase (sfasamento di 180°) (⏱ 74:48)

Due sinusoidi sono **in controfase** quando una raggiunge il massimo nell'istante in cui l'altra raggiunge il minimo. Lo sfasamento è di **180°**. Le sinusoidi si muovono in modo opposto.

Se si sommano due sinusoidi di uguale ampiezza in controfase, si **annullano** completamente punto per punto (analogia: batterie collegate in verso opposto che si sottraggono).

### 🔹 Sinusoidi in quadratura (sfasamento di 90°) (⏱ 75:55)

Due sinusoidi sono **in quadratura** quando lo sfasamento tra di esse è di **90°**: quando una è al massimo, l'altra passa per lo zero.

### 🔹 Effetto del verso di rotazione sulla fase (⏱ 59:52)

Se il raggio generatore ruota in senso antiorario, la sinusoide parte verso l'alto (picco positivo per primo). Se ruota in senso orario, la sinusoide parte verso il basso. Le due sinusoidi risultanti sono identiche ma sfasate di **180°**.

### 🔹 Modulazione di ampiezza e di frequenza (cenni) (⏱ 41:10)

Il docente anticipa, a partire da una domanda del corsista Mattia, che:

- Se l'**ampiezza** della sinusoide varia da un ciclo all'altro (a volte più alta, a volte più bassa), si parla di **modulazione di ampiezza** (AM), un modo di trasmettere segnali radio.
- Se la **frequenza** (periodo) della sinusoide varia (alcuni periodi più lunghi, altri più corti), si parla di **modulazione di frequenza** (FM), un altro modo di trasmissione radio.

Questi argomenti saranno approfonditi nelle lezioni successive.

---

## ⚡ 8. Potenza in corrente alternata (⏱ 84:54)

### 🔹 Richiamo: energia e potenza (⏱ 85:02)

- **Energia** — capacità di un sistema di compiere un lavoro; si misura in **joule** (J) o in **wattora** (Wh).
- **Potenza** — capacità di svolgere un lavoro nell'unità di tempo; si misura in **watt** (W).

**Esempi:**

- Lampadina da 20 W accesa per 3 ore → consuma $20 \times 3 = 60$ Wh di energia.
- Stufetta da 1000 W accesa per 30 minuti (0,5 ore) → consuma $1000 \times 0{,}5 = 500$ Wh.

### 🔹 Carico resistivo: tensione e corrente in fase (⏱ 86:27)

Quando la tensione alternata alimenta un **carico resistivo** (una resistenza pura), la sinusoide della tensione e la sinusoide della corrente sono perfettamente **in fase**: raggiungono massimi, zeri e minimi contemporaneamente.

In questo caso le formule della potenza sono **identiche** a quelle viste in corrente continua, purché si usino i **valori efficaci**:

$$P_{eff} = V_{eff} \times I_{eff}$$

$$P_{eff} = \frac{V_{eff}^2}{R}$$

$$P_{eff} = I_{eff}^2 \times R$$

> "Non cambia assolutamente niente rispetto a quello che abbiamo visto con la corrente continua."

### 🔹 Carico reattivo: sfasamento tra tensione e corrente (⏱ 88:39)

A volte il carico non è puramente resistivo: può avere una **componente induttiva** (bobina/induttore) o una **componente capacitiva** (condensatore). In questi casi tensione e corrente **non sono più in fase**: si forma un **angolo di sfasamento** tra le due sinusoidi, indicato con la lettera greca **φ** (phi, in italiano "fi").

Lo sfasamento φ è espresso in gradi e può assumere qualsiasi valore tra 0° e 90°.

### 🔹 Potenza apparente, potenza reale e potenza reattiva (⏱ 90:17)

Quando tensione e corrente sono sfasate, non tutta la potenza si trasforma in lavoro utile.

**Potenza apparente** ($S$) — è il prodotto semplice della tensione efficace per la corrente efficace:

$$S = V_{eff} \times I_{eff}$$

Si misura in **voltampere** (VA).

**Potenza reale** (o **potenza attiva**, $P$) — è la parte della potenza che effettivamente produce lavoro (calore, movimento, luce):

$$\boxed{P = V_{eff} \times I_{eff} \times \cos\varphi = S \times \cos\varphi}$$

Si misura in **watt** (W).

**Potenza reattiva** ($Q$) — è la parte di potenza che **non produce lavoro**: è associata alla componente di corrente sfasata di 90° rispetto alla tensione. Si misura in **voltampere reattivi** (VAR).

> Il docente precisa che "potenza reale" e "potenza attiva" sono **sinonimi perfetti**.

### 🔹 Il coseno di φ (fattore di potenza) (⏱ 90:49)

Il **coseno** è un'operazione trigonometrica che associa un numero a un angolo. Due casi particolari fondamentali:

| Angolo φ | cos φ | Significato                                             |
| -------- | ----- | ------------------------------------------------------- |
| **0°**   | **1** | Tensione e corrente in fase → tutta la potenza è reale  |
| **90°**  | **0** | Tensione e corrente in quadratura → potenza reale nulla |

Quando $\cos\varphi = 1$ (carico resistivo puro), la potenza reale coincide con la potenza apparente: $P = V \times I$.
Quando $\cos\varphi = 0$ (carico totalmente reattivo), la potenza reale è zero: nessun lavoro utile viene prodotto.

### 🔹 Scomposizione vettoriale della corrente (⏱ 96:56)

Su un diagramma vettoriale, si rappresenta la tensione $V$ sull'asse orizzontale e la corrente $I$ come un vettore che forma un angolo φ con essa. La corrente può essere scomposta in due componenti:

- **Componente in fase** con la tensione (proiezione sull'asse orizzontale) → produce lavoro → genera la **potenza reale**.
- **Componente in quadratura** (proiezione sull'asse verticale, a 90° dalla tensione) → non produce lavoro → genera la **potenza reattiva**.

La somma vettoriale delle due componenti ricostruisce la corrente totale.

Più l'angolo φ è grande (corrente più sfasata), più la componente in fase diminuisce e quindi meno potenza reale si ottiene. Più l'angolo φ è piccolo (corrente quasi in fase), maggiore è il rendimento.

### 🔹 L'analogia della birra 🍺 (⏱ 100:24)

Il docente propone un'analogia efficace:

- **Potenza reale** = la **birra** nel boccale → è quella che toglie la sete (produce lavoro).
- **Potenza reattiva** = la **schiuma** sopra la birra → occupa spazio ma non toglie la sete (non produce lavoro).
- **Potenza apparente** = l'**altezza totale** del boccale (birra + schiuma) → è la combinazione delle due.

### 🔹 Il rifasamento (cenni) (⏱ 112:09)

L'**ENEL** esige che i carichi industriali (motori, ecc.) siano il più possibile "rifasati", cioè che l'angolo φ sia il più piccolo possibile. Quando i carichi sono troppo sfasati, c'è un "girare a vuoto" di energia apparente sulle linee elettriche che non produce lavoro utile ma crea disturbi.

Il **rifasamento** è un'operazione tecnica (mediante condensatori o dispositivi appositi detti **rifasatori**) che riduce l'angolo di sfasamento tra tensione e corrente, avvicinando $\cos\varphi$ a 1. Questo argomento sarà approfondito nelle prossime lezioni su condensatore e induttore.

---

## 🔗 Concept Map (testuale)

- Corrente continua → scorre in un solo verso → generata da tensione costante
- Corrente alternata → inverte ciclicamente il verso → generata da tensione alternata (alternatore)
- Alternatore → basato su scoperte di Faraday → spira rotante in campo magnetico → produce sinusoide
- Sinusoide → ottenuta da moto circolare uniforme → sviluppo del raggio rotante su cerchio
- Frequenza ($f$) → numero di cicli al secondo → inverso del periodo → $f = \frac{1}{T}$
- Periodo ($T$) → durata di un ciclo completo → inverso della frequenza → $T = \frac{1}{f}$
- Tensione alternata → caratterizzata da: valore efficace, di picco, picco-picco, valor medio
- Tensione di picco → $V_p = \sqrt{2} \times V_{eff} \approx 1{,}41 \times V_{eff}$
- Tensione picco-picco → $V_{pp} = 2 \times V_p$
- Valor medio → $V_m = 0{,}9 \times V_{eff}$
- Tensione efficace → produce lavoro equivalente alla tensione continua di pari valore
- Fase → posizione angolare sulla sinusoide (0°–360°)
- In fase (0°) → sinusoidi si sommano
- In controfase (180°) → sinusoidi si annullano
- In quadratura (90°) → caso intermedio
- Carico resistivo → tensione e corrente in fase → $P = V \times I$ (come in CC)
- Carico reattivo → tensione e corrente sfasate di angolo φ
- Potenza apparente ($S$) → $S = V \times I$ → somma di potenza reale + reattiva
- Potenza reale/attiva ($P$) → $P = S \times \cos\varphi$ → produce lavoro
- Potenza reattiva ($Q$) → non produce lavoro → associata alla componente di corrente in quadratura
- $\cos\varphi = 1$ → carico resistivo → massimo rendimento
- $\cos\varphi = 0$ → carico totalmente reattivo → nessun lavoro utile
- Modulazione di ampiezza (AM) → ampiezza della sinusoide varia
- Modulazione di frequenza (FM) → frequenza della sinusoide varia
- Rifasamento → avvicinare $\cos\varphi$ a 1 → richiesto dall'ENEL per i carichi industriali

---

## 📝 Key Takeaways

1. La **corrente alternata** è una corrente che inverte periodicamente il senso di scorrimento, generata da una tensione alternata sinusoidale prodotta da un alternatore.
2. La **sinusoide** si ottiene geometricamente dalla proiezione di un punto che ruota a velocità angolare costante su una circonferenza: ogni 360° si completa un ciclo.
3. **Frequenza** ($f$) e **periodo** ($T$) sono grandezze inverse: $f = \frac{1}{T}$ e $T = \frac{1}{f}$. La frequenza indica quanti cicli al secondo, il periodo quanto dura ogni ciclo.
4. Un **alternatore** genera corrente sinusoidale facendo ruotare una spira in un campo magnetico (principio di Faraday): la variazione ciclica del campo intercettato genera una tensione sinusoidale.
5. La tensione alternata ha molteplici valori: **efficace** (usato nei calcoli di potenza, è il valore sottinteso), **di picco** ($V_p = 1{,}41 \times V_{eff}$), **picco-picco** ($V_{pp} = 2 \times V_p$) e **valor medio** ($V_m = 0{,}9 \times V_{eff}$).
6. I 220 V dell'ENEL sono un valore **efficace**; la tensione di picco nella presa è circa 311 V e l'escursione picco-picco è di 622 V.
7. Due sinusoidi possono essere **in fase** (0°, si sommano), **in quadratura** (90°), o **in controfase** (180°, si annullano se di uguale ampiezza).
8. Su **carico resistivo**, tensione e corrente sono in fase e la potenza si calcola come in corrente continua usando i valori efficaci: $P = V_{eff} \times I_{eff}$.
9. Su **carico reattivo**, tensione e corrente si sfasano di un angolo φ; la potenza reale (attiva) è $P = V \times I \times \cos\varphi$, dove $\cos\varphi$ è il **fattore di potenza**.
10. La **potenza apparente** ($S = V \times I$) comprende sia la parte reale (che produce lavoro, la "birra") sia la parte reattiva (che non produce lavoro, la "schiuma"). L'ENEL richiede il rifasamento dei carichi industriali per portare $\cos\varphi$ il più vicino possibile a 1.
11. Nei calcoli, occorre sempre verificare che le grandezze siano espresse nelle **stesse unità di misura** (Hz, non MHz; Ω, non kΩ) prima di applicare le formule.

---

## ❓ Comprehension Questions

1. Spiega la differenza fondamentale tra corrente continua e corrente alternata in termini di comportamento del generatore e della corrente nel circuito. Perché un generatore in corrente continua ha poli fissi positivo e negativo, mentre un alternatore no?

2. Descrivi il processo geometrico con cui una sinusoide viene generata a partire da un raggio che ruota su una circonferenza. Cosa succede alla forma d'onda se la velocità di rotazione del raggio non è costante?

3. Un segnale radio ha una frequenza di 145 MHz. Qual è il suo periodo? Spiega il procedimento e le conversioni di unità necessarie per arrivare al risultato.

4. Perché la tensione efficace dell'ENEL è di 220 V, ma per dimensionare gli isolamenti è necessario considerare la tensione di picco (311 V)? Fornisci un ragionamento basato sulle relazioni tra i valori caratteristici della tensione alternata.

5. Due sinusoidi di uguale ampiezza vengono sommate. Descrivi cosa accade al segnale risultante nei tre casi: sinusoidi in fase, in quadratura e in controfase. Qual è l'analogia con le batterie in serie?

6. Spiega perché, in un circuito con carico reattivo, non tutta la potenza apparente si traduce in lavoro utile. Utilizza la scomposizione vettoriale della corrente per giustificare la formula $P = V \times I \times \cos\varphi$.

7. Nell'analogia della birra proposta dal docente, cosa rappresentano rispettivamente la birra, la schiuma e l'altezza totale del boccale? Perché questa analogia è utile per comprendere il concetto di fattore di potenza?

8. Un carico industriale ha $\cos\varphi = 0{,}5$. Questo significa che il carico è più vicino a un carico resistivo o a un carico totalmente reattivo? Quale percentuale della potenza apparente viene effettivamente convertita in lavoro? Perché l'ENEL richiede il rifasamento?

9. Qual è la relazione tra il funzionamento di un alternatore e lo sviluppo geometrico della sinusoide? Spiega perché un alternatore produce naturalmente una corrente sinusoidale collegando la rotazione della spira al concetto di raggio rotante.

10. Il docente menziona brevemente la modulazione di ampiezza (AM) e la modulazione di frequenza (FM). Con riferimento alla sinusoide "pura" (ampiezza e frequenza costanti), spiega cosa cambia in ciascuno dei due tipi di modulazione e perché si adottano.

---

## 📚 Glossary

- **Alternatore** — Macchina elettrica rotante che produce corrente alternata sinusoidale, basata sulla rotazione di una spira in un campo magnetico.
- **Angolo di sfasamento (φ)** — Angolo in gradi che misura la differenza di fase tra la sinusoide della tensione e quella della corrente in un circuito in corrente alternata.
- **Angolo giro** — Angolo di 360°, corrispondente a un ciclo completo della sinusoide.
- **Campo magnetico** — Regione di spazio in cui si manifestano forze magnetiche, generato da magneti permanenti o elettromagneti.
- **Carico reattivo** — Carico elettrico che presenta una componente capacitiva o induttiva, causando sfasamento tra tensione e corrente.
- **Carico resistivo** — Carico elettrico costituito da sola resistenza, dove tensione e corrente sono in fase.
- **Controfase** — Condizione di due sinusoidi sfasate di 180°: quando una è al massimo, l'altra è al minimo.
- **Corrente alternata (CA/AC)** — Corrente elettrica che inverte periodicamente il senso di scorrimento.
- **Corrente continua (CC/DC)** — Corrente elettrica che scorre sempre nello stesso verso.
- **Coseno di φ (cos φ)** — Fattore di potenza; rapporto tra potenza reale e potenza apparente. Vale 1 se tensione e corrente sono in fase, 0 se sono in quadratura.
- **Fattore di potenza** — Valore numerico $\cos\varphi$ che indica quale frazione della potenza apparente produce lavoro utile.
- **Frequenza ($f$)** — Numero di cicli completi di un'onda nell'unità di tempo (un secondo). Si misura in hertz (Hz).
- **Hertz (Hz)** — Unità di misura della frequenza; 1 Hz = 1 ciclo al secondo.
- **In fase** — Condizione di due sinusoidi con sfasamento nullo (0°): raggiungono i massimi e i minimi simultaneamente.
- **Megahertz (MHz)** — Multiplo dell'hertz, pari a un milione di hertz (10⁶ Hz).
- **Modulazione di ampiezza (AM)** — Tecnica di trasmissione radio in cui l'ampiezza della sinusoide portante varia nel tempo.
- **Modulazione di frequenza (FM)** — Tecnica di trasmissione radio in cui la frequenza della sinusoide portante varia nel tempo.
- **Oscilloscopio** — Strumento elettronico in grado di visualizzare forme d'onda (sinusoidi, ecc.) su uno schermo.
- **Periodo ($T$)** — Intervallo di tempo necessario a completare un ciclo della sinusoide. Si misura in secondi (s).
- **Potenza apparente ($S$)** — Prodotto $V_{eff} \times I_{eff}$ in corrente alternata; comprende sia la potenza reale sia la potenza reattiva. Si misura in voltampere (VA).
- **Potenza reale (o attiva, $P$)** — Parte della potenza che produce effettivamente lavoro; vale $P = S \times \cos\varphi$. Si misura in watt (W).
- **Potenza reattiva ($Q$)** — Parte della potenza che non produce lavoro utile, associata alla componente di corrente in quadratura rispetto alla tensione. Si misura in voltampere reattivi (VAR).
- **Quadratura** — Condizione di due sinusoidi sfasate di 90°.
- **Rifasamento** — Operazione tecnica per ridurre l'angolo di sfasamento φ tra tensione e corrente, avvicinando $\cos\varphi$ a 1.
- **Rotore** — Parte rotante di un alternatore o motore elettrico, che contiene le spire di filo conduttore.
- **Sinusoide** — Forma d'onda fondamentale, ottenuta dalla funzione seno; è la curva che descrive l'andamento di una tensione o corrente alternata generata da un alternatore.
- **Spira** — Avvolgimento rettangolare o circolare di filo conduttore; elemento base di un alternatore.
- **Tensione di picco ($V_p$)** — Valore massimo raggiunto dalla sinusoide; $V_p = \sqrt{2} \times V_{eff} \approx 1{,}41 \times V_{eff}$.
- **Tensione efficace ($V_{eff}$ o RMS)** — Valore della tensione alternata equivalente, in termini di lavoro prodotto, a una tensione continua dello stesso valore.
- **Tensione istantanea** — Valore della tensione in un dato istante preciso.
- **Tensione picco-picco ($V_{pp}$)** — Escursione totale della sinusoide, dal minimo al massimo; $V_{pp} = 2 \times V_p$.
- **Valor medio ($V_m$)** — Media dei valori istantanei di una sinusoide in un semiperiodo; $V_m \approx 0{,}9 \times V_{eff}$.
- **Velocità angolare** — Rapidità con cui il raggio generatore della sinusoide ruota attorno al centro della circonferenza; determina la frequenza.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore principale**: Paolo (docente del corso)
- 👨‍🏫 **Co-docente / interventi**: Sauro (suggerimento sul metodo alternativo per il parallelo di tre resistenze; curerà le lezioni su condensatore e induttore)

---

## 📅 Informazioni Lezione

- **Numero Lezione**: 03
- **Data**: 19/03/2025
- **Durata**: circa 2 ore (121 minuti)
- **Numero di argomenti principali**: 8
- **Keywords**: corrente alternata, sinusoide, frequenza, periodo, hertz, alternatore, Faraday, spira, campo magnetico, tensione efficace, tensione di picco, tensione picco-picco, valor medio, RMS, fase, controfase, quadratura, sfasamento, potenza apparente, potenza reale, potenza attiva, potenza reattiva, coseno di φ, fattore di potenza, rifasamento, modulazione di ampiezza, modulazione di frequenza, oscilloscopio, ENEL
