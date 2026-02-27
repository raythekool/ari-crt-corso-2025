# 📘 Lezione 06 - Semiconduttori

## 📌 Overview

- **Materia e argomento**: Radiotecnica — filtri, circuiti risonanti e cristalli di quarzo. Prima lezione della sezione "radiotecnica" del corso, con un approccio più qualitativo e meno formule rispetto alle lezioni precedenti di elettrotecnica.
- **Tempo di studio stimato**: 90–110 minuti
- **Prerequisiti**: Reattanza induttiva $X_L = 2\pi fL$ e capacitiva $X_C = 1/(2\pi fC)$ (Lezioni 04–05), impedenza (Lezione 05), condensatori e induttori in serie/parallelo.
- **Obiettivi di apprendimento**:
  - Comprendere il principio di funzionamento dei filtri basati su componenti reattivi (LC, RC)
  - Distinguere i quattro tipi fondamentali di filtro: passa basso, passa alto, passa banda, elimina banda
  - Definire la frequenza di taglio (metà potenza oppure $0{,}707$ in tensione)
  - Comprendere la risonanza in circuiti LC parallelo e serie
  - Usare la formula del fattore di merito $Q = f_0 / B$
  - Conoscere i cristalli di quarzo e il principio piezoelettrico

---

## 📖 Core Content

## 🔍 1. Revisione quiz Lezione 05 (⏱ 00:04 – 22:14)

La lezione si apre con la correzione del quiz della Lezione 05. Le risposte sono riepilogate brevemente:

- **Scopo del condensatore**: bloccare la corrente continua e lasciar passare la corrente alternata (non il contrario)
- **Unità di misura della capacità**: Farad (con sottomultipli µF, nF, pF)
- **Fattori che determinano la capacità**: materiale dielettrico (ε), superficie delle armature, numero di piastre, distanza fra le piastre
- **Condensatori in parallelo**: le capacità si sommano ($C_{tot} = C_1 + C_2$)
- **Aumento distanza fra le piastre**: la capacità diminuisce (D al denominatore in $C = \varepsilon \cdot S/D$)
- **Conversione**: 500.000 µF = 0,5 F (spostarsi di 6 posizioni decimali)
- **Reattanza capacitiva e frequenza**: $X_C$ aumenta al diminuire della frequenza (F al denominatore)
- **Due condensatori uguali da 8 pF in serie**: $C_{tot} = 4$ pF (metà)
- **Tre condensatori uguali in serie**: capacità totale minore di ogni singolo condensatore
- **Formula della reattanza**: $X_C = 1/(2\pi fC)$
- **Unità di misura dell'impedenza**: ohm (Ω)
- **Impedenza**: grandezza che si oppone allo scorrere della corrente alternata in qualsiasi circuito
- **Legge di Ohm per le impedenze**: $V = Z \times I$
- **Potenza dissipata dalla parte reale dell'impedenza**: potenza attiva

---

## 📡 2. Introduzione ai filtri (⏱ 22:14 – 27:25)

### 🔹 Cos'è un filtro

Un **filtro** è una combinazione di circuiti composti da induttori e condensatori (circuiti LC) che sfrutta la variazione della reattanza induttiva e capacitiva in funzione della frequenza per attenuare o far passare determinate bande di frequenza.

Il principio fondamentale è:

- **Reattanza induttiva** ($X_L$): vale 0 a frequenza zero (cortocircuito per la DC), cresce linearmente con la frequenza
- **Reattanza capacitiva** ($X_C$): vale infinito a frequenza zero (circuito aperto per la DC), decresce con la frequenza

Queste caratteristiche complementari permettono di discriminare i segnali in base alla frequenza.

---

## 📉 3. Filtro passa basso (⏱ 27:25 – 46:16)

### 🔹 Definizione

Il **filtro passa basso** attenua i segnali con frequenza superiore alla **frequenza di taglio** e lascia passare inalterati quelli con frequenza inferiore.

### 🔹 Frequenza di taglio

La **frequenza di taglio** è definita in due modi equivalenti:

1. La frequenza alla quale la **potenza** del segnale di uscita si dimezza rispetto alla banda passante
2. La frequenza alla quale l'**ampiezza** (tensione) del segnale di uscita si riduce a $\frac{1}{\sqrt{2}} \approx 0{,}707$ rispetto al valore in banda passante

> Perché $0{,}707$ equivale a metà potenza? Poiché $P \propto V^2$: $(0{,}707)^2 = (1/\sqrt{2})^2 = 1/2 = 0{,}5$

⚠️ _Questa definizione si applica a tutti i tipi di filtro e può essere oggetto di domande d'esame._

### 🔹 Schema circuitale RC

Nella versione più semplice, il filtro passa basso è costituito da:

- Una **resistenza** in serie (valore costante con la frequenza)
- Un **condensatore** verso massa

A **frequenze basse**: la reattanza del condensatore è molto alta → il condensatore è "come se non esistesse" → il segnale passa inalterato in uscita.

A **frequenze alte**: la reattanza del condensatore diventa bassa → il condensatore cortocircuita il segnale verso massa → la tensione di uscita si azzera.

### 🔹 Schema circuitale LC (migliore)

Sostituendo la resistenza con un **induttore**:

- L'induttore a frequenze alte ha reattanza alta → ostacola il passaggio
- Il condensatore a frequenze alte ha reattanza bassa → cortocircuita verso massa

Due componenti reattivi lavorano insieme, ottenendo un filtraggio **più ripido** (selettivo).

### 🔹 Concetto di poli

Ogni componente reattivo (condensatore o induttore) inserito nel filtro aggiunge un **polo**. Più poli ha il filtro, più la sua curva di attenuazione è ripida oltre la frequenza di taglio, avvicinandosi al comportamento di un filtro ideale.

### 🔹 Applicazioni pratiche

- **Controlli di tono** negli amplificatori audio (stereo, autoradio, TV)
- **Filtri crossover** nelle casse acustiche: il passa basso manda i bassi al woofer
- **Uscita dei trasmettitori radio**: per eliminare le armoniche (es. trasmettitore a 27 MHz genera armoniche a 54, 81 MHz… che interferivano con la TV)
- **Filtri commerciali** (es. Drake): reggono fino a 1 kW, passano sotto 30 MHz, attenuazione 80 dB a 41 MHz

---

## 📈 4. Filtro passa alto (⏱ 60:20 – 66:46)

### 🔹 Definizione

Il **filtro passa alto** è speculare al passa basso: attenua le frequenze inferiori alla frequenza di taglio e lascia passare quelle superiori.

### 🔹 Schema circuitale

Si invertono le posizioni dei componenti rispetto al passa basso:

- Il **condensatore** è in serie: a frequenze basse ha reattanza altissima → blocca il segnale; a frequenze alte ha reattanza bassissima → lascia passare tutto
- L'**induttore** (o resistore) è verso massa: a frequenze basse ha reattanza bassa → cortocircuita verso massa anche ciò che riuscisse a passare

### 🔹 Varianti

Un filtro passa alto può essere costruito con diverse combinazioni: C+R, C+L, oppure L+R (come osservato durante la lezione).

---

## 📊 5. Filtro passa banda (⏱ 66:46 – 75:02)

### 🔹 Definizione

Il **filtro passa banda** fa passare le frequenze comprese tra una **frequenza di taglio inferiore** e una **frequenza di taglio superiore**, attenuando tutto ciò che sta al di fuori.

### 🔹 Composizione

Può essere realizzato come **combinazione** di un filtro passa alto (che taglia il sotto) e un filtro passa basso (che taglia il sopra).

### 🔹 Applicazione principale

I filtri passa banda sono fondamentali nei **ricevitori radio**: permettono la **selettività**, cioè la capacità di ascoltare un solo segnale per volta. Un segnale FM commerciale è largo circa 100 kHz; il filtro passa banda del ricevitore è dimensionato per far passare esattamente quella larghezza di banda.

---

## 🚫 6. Filtro elimina banda (notch) (⏱ 70:55 – 75:02)

### 🔹 Definizione

Il **filtro elimina banda** (o **notch**) attenua i segnali con frequenza compresa tra le due frequenze di taglio e lascia passare tutto il resto. È il funzionamento speculare del passa banda.

### 🔹 Applicazione pratica

Usato per eliminare le interferenze della **banda FM commerciale** (88–108 MHz) nei ricevitori radioamatoriali. I segnali FM sono molto forti e possono "sovraccaricare" un ricevitore sensibile, impedendone il funzionamento.

### 🔹 Riepilogo dei quattro tipi di filtro

| Tipo di filtro    | Cosa lascia passare                  | Cosa blocca                          |
| ----------------- | ------------------------------------ | ------------------------------------ |
| **Passa basso**   | Frequenze sotto la freq. di taglio   | Frequenze sopra la freq. di taglio   |
| **Passa alto**    | Frequenze sopra la freq. di taglio   | Frequenze sotto la freq. di taglio   |
| **Passa banda**   | Frequenze tra le due freq. di taglio | Frequenze fuori dalla banda          |
| **Elimina banda** | Frequenze fuori dalla banda          | Frequenze tra le due freq. di taglio |

⚠️ _Le domande d'esame sui filtri sono tipicamente formulate come: "Cosa lascia passare un filtro passa banda?" con tre risposte a scelta multipla._

---

## 🔄 7. Circuiti risonanti (⏱ 78:31 – 96:05)

### 🔹 Definizione di risonanza

Un **circuito risonante** si ottiene collegando un condensatore e un induttore in **serie** o in **parallelo**. Esiste una frequenza specifica, la **frequenza di risonanza** ($f_0$), alla quale la reattanza induttiva e quella capacitiva sono uguali ($X_L = X_C$) e si annullano a vicenda.

### 🔹 Formula della frequenza di risonanza

> $$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

Dove:

- $L$ = induttanza in Henry
- $C$ = capacità in Farad

### 🔹 Circuito risonante parallelo

In un circuito LC parallelo alla frequenza di risonanza:

1. La tensione è **la stessa** ai capi di L e C (sono in parallelo)
2. Le reattanze sono uguali → le correnti che scorrono in L e C sono uguali in ampiezza
3. La corrente nell'induttore è in **ritardo** di 90° rispetto alla tensione; la corrente nel condensatore è in **anticipo** di 90°
4. Le due correnti sono quindi **sfasate di 180°** (in opposizione di fase) → si annullano
5. Il circuito esterno non vede scorrere corrente → **impedenza infinita** (circuito aperto)

> Il condensatore e l'induttore si "palleggiano" l'energia: il condensatore si scarica sull'induttore (campo elettrico → campo magnetico) e viceversa, senza assorbire energia dall'esterno.

### 🔹 Circuito risonante serie

In un circuito LC serie alla frequenza di risonanza:

1. La corrente è **la stessa** in L e C (sono in serie)
2. Le reattanze sono uguali → le tensioni ai capi di L e C sono uguali in ampiezza
3. La tensione sull'induttore è in **anticipo** di 90° rispetto alla corrente; la tensione sul condensatore è in **ritardo** di 90°
4. Le due tensioni sono **sfasate di 180°** → si annullano
5. Fra i punti A e B non c'è differenza di potenziale → **impedenza nulla** (cortocircuito)

### 🔹 Confronto risonanza serie vs parallelo

| Proprietà                   | Parallelo                      | Serie                     |
| --------------------------- | ------------------------------ | ------------------------- |
| Alla risonanza si annullano | Le correnti                    | Le tensioni               |
| Impedenza alla risonanza    | **Infinita** (circuito aperto) | **Nulla** (cortocircuito) |
| Curva della corrente        | Minimo a $f_0$                 | Massimo a $f_0$           |

I circuiti risonanti sono il meccanismo base della **selettività** nei ricevitori radio.

---

## 📐 8. Fattore di merito Q e larghezza di banda (⏱ 96:05 – 109:23)

### 🔹 Componenti reali e perdite

Nel mondo reale, i componenti hanno **perdite** (rappresentate da una resistenza parassita):

- I **condensatori** hanno perdite molto basse (campo elettrico confinato tra le armature)
- Gli **induttori** hanno perdite significative (campo magnetico non confinato, si propaga nello spazio)

Per un buon funzionamento:

- Circuito risonante **parallelo**: la resistenza parassita deve essere **alta** (per non cortocircuitare)
- Circuito risonante **serie**: la resistenza parassita deve essere **bassa** (per non bloccare la corrente)

### 🔹 Fattore di merito Q

Il **fattore di merito** (o **fattore di qualità**) **Q** indica quanto è "buono" un circuito risonante. Un Q alto significa basse perdite e curva di risonanza stretta (selettiva). La relazione con la larghezza di banda è:

> $$Q = \frac{f_0}{B}$$

Dove:

- $f_0$ = frequenza di risonanza
- $B$ = larghezza di banda (distanza tra le due frequenze di taglio a −3 dB)

### 🔹 Relazione Q – selettività

| Q              | Curva di risonanza  | Selettività |
| -------------- | ------------------- | ----------- |
| Basso (5–10)   | Ampia, "spampanata" | Bassa       |
| Alto (50–100+) | Stretta, ripida     | Alta        |

Q e B sono **inversamente proporzionali**: aumentando Q, diminuisce la larghezza di banda.

### 🔹 Esercizi svolti

**Esercizio 1**: Un filtro passa banda risuona a 20 MHz con larghezza di banda di 2 kHz. Qual è il fattore Q?

$$Q = \frac{f_0}{B} = \frac{20.000.000 \text{ Hz}}{2.000 \text{ Hz}} = 10.000$$

> ⚠️ Convertire sempre alla stessa unità di misura prima di calcolare!

**Esercizio 2**: Un filtro passa banda risuona a 5 MHz con Q = 100. Qual è la larghezza di banda?

$$B = \frac{f_0}{Q} = \frac{5.000 \text{ kHz}}{100} = 50 \text{ kHz}$$

---

## 💎 9. Cristalli di quarzo (⏱ 114:18 – 122:02)

### 🔹 Piezoelettricità

Il quarzo è un materiale **piezoelettrico**: se compresso meccanicamente, genera una tensione sulle sue facce. Il fenomeno è anche **inverso**: applicando una corrente alternata, il quarzo vibra alla sua frequenza di risonanza meccanica.

**Esempio pratico**: l'accendino a scintilla da cucina contiene un quarzo; premendo il pulsante si comprime il cristallo, generando una tensione sufficientemente alta da produrre una scintilla.

### 🔹 Risonanza meccanica

A differenza dei circuiti LC (risonanza elettrica), i quarzi funzionano per **risonanza meccanica**. Il principio è analogo a una **corda di chitarra** o a un **bicchiere di cristallo** colpito con l'unghia: il materiale oscilla a una frequenza determinata dalle sue dimensioni fisiche.

### 🔹 Vantaggi dei quarzi rispetto ai circuiti LC

| Caratteristica         | Circuito LC                           | Quarzo                |
| ---------------------- | ------------------------------------- | --------------------- |
| Fattore di merito Q    | 10 – 100                              | Fino a **10.000**     |
| Stabilità in frequenza | Moderata                              | **Estremamente alta** |
| Perdite                | Significative (soprattutto induttore) | **Minime**            |

La frequenza di risonanza dipende dalle **dimensioni fisiche** del cristallo: i quarzi vengono tagliati per risuonare alla frequenza desiderata. La fondamentale arriva fino a circa **20 MHz**; per frequenze superiori si utilizzano le **armoniche** del quarzo.

### 🔹 Aspetto fisico

I quarzi si presentano come piccoli contenitori metallici con due piedini. All'interno c'è una sottilissima lamina di quarzo con due metallizzazioni collegate ai piedini esterni. Dimensioni variabili: nei vecchi baracchini CB (Midland, Tokai) si trovavano quarzi più grandi; i quarzi moderni sono molto più compatti.

---

## 🔗 Concept Map (testuale)

- **Filtri** → sfruttano → **Variazione di reattanza con la frequenza**
- **Filtro passa basso** → è speculare a → **Filtro passa alto**
- **Filtro passa banda** → è combinazione di → **Filtro passa basso + filtro passa alto**
- **Filtro elimina banda** → è speculare a → **Filtro passa banda**
- **Frequenza di taglio** → corrisponde a → **Metà potenza** oppure **0,707 in tensione**
- **Poli del filtro** → determinano → **Ripidità della curva di attenuazione**
- **Circuito LC** → entra in → **Risonanza a $f_0 = 1/(2\pi\sqrt{LC})$**
- **Risonanza parallelo** → produce → **Impedenza infinita (circuito aperto)**
- **Risonanza serie** → produce → **Impedenza nulla (cortocircuito)**
- **Fattore di merito Q** → è inversamente proporzionale a → **Larghezza di banda B**
- **Quarzo** → usa → **Risonanza meccanica (piezoelettricità)**
- **Quarzo** → ha → **Q molto alto (~10.000), grande stabilità**

---

## 📝 Key Takeaways

1. I **filtri** sono combinazioni di induttori e condensatori che attenuano o lasciano passare determinate bande di frequenza. Esistono quattro tipi: passa basso, passa alto, passa banda, elimina banda.
2. La **frequenza di taglio** è il punto in cui la potenza si dimezza (−3 dB) oppure la tensione si riduce a $1/\sqrt{2} \approx 0{,}707$. Questi due valori sono equivalenti.
3. Un **circuito risonante parallelo** alla frequenza di risonanza ha impedenza infinita (circuito aperto); un **circuito risonante serie** ha impedenza nulla (cortocircuito). Sono speculari.
4. La **frequenza di risonanza** è $f_0 = 1/(2\pi\sqrt{LC})$, cioè la frequenza dove $X_L = X_C$.
5. Il **fattore di merito Q** indica la qualità/selettività di un circuito risonante: $Q = f_0/B$. Più alto è Q, più stretta è la curva di risonanza.
6. Gli **induttori reali** hanno perdite maggiori dei condensatori perché il campo magnetico non è confinato. Questo limita il Q dei circuiti LC.
7. I **cristalli di quarzo** sfruttano la piezoelettricità per ottenere risonanze meccaniche con Q fino a 10.000, permettendo oscillatori estremamente stabili.

---

## ❓ Comprehension Questions

1. Perché un filtro LC passa basso ha una curva di attenuazione più ripida rispetto a un filtro RC? Cosa si intende per "poli" di un filtro?
2. Spiegare perché la definizione di frequenza di taglio "metà potenza" è equivalente a "tensione pari a $0{,}707$".
3. In un circuito risonante parallelo, le correnti in L e C si annullano alla risonanza. Perché l'impedenza vista dall'esterno diventa infinita e non nulla?
4. Un circuito risonante serie ha $f_0$ = 7 MHz e $Q$ = 200. Qual è la larghezza di banda? Come cambierebbe il comportamento se Q fosse 20?
5. Perché le perdite degli induttori sono molto maggiori di quelle dei condensatori? In che modo questo influisce sul fattore Q?
6. Un radioamatore abita vicino a un trasmettitore FM commerciale e la sua radio non funziona. Quale tipo di filtro dovrebbe usare e perché?
7. Spiegare l'analogia tra la risonanza meccanica di una corda di chitarra e la risonanza di un cristallo di quarzo.

---

## 📚 Glossary

- **Banda passante** — intervallo di frequenze che un filtro lascia passare con attenuazione trascurabile
- **Circuito risonante** — circuito LC in cui a una specifica frequenza ($f_0$) le reattanze si annullano, producendo impedenza massima (parallelo) o minima (serie)
- **Fattore di merito (Q)** — parametro che indica la qualità di un circuito risonante; $Q = f_0/B$; valori alti indicano basse perdite e alta selettività
- **Filtro elimina banda (notch)** — filtro che attenua le frequenze comprese tra due frequenze di taglio
- **Filtro passa alto** — filtro che lascia passare le frequenze superiori alla frequenza di taglio
- **Filtro passa banda** — filtro che lascia passare le frequenze comprese tra due frequenze di taglio
- **Filtro passa basso** — filtro che lascia passare le frequenze inferiori alla frequenza di taglio
- **Frequenza di risonanza ($f_0$)** — frequenza alla quale $X_L = X_C$ in un circuito LC; $f_0 = 1/(2\pi\sqrt{LC})$
- **Frequenza di taglio** — frequenza alla quale la potenza di uscita di un filtro si dimezza (−3 dB) o la tensione scende a $0{,}707$ del valore in banda passante
- **Larghezza di banda (B)** — ampiezza dell'intervallo di frequenze entro il quale un circuito risonante o un filtro opera efficacemente
- **Piezoelettricità** — proprietà di materiali cristallini di generare tensione quando compressi meccanicamente (e viceversa)
- **Polo** — in un filtro, ogni componente reattivo aggiunge un polo; più poli → curva di attenuazione più ripida
- **Quadripolo** — dispositivo con due terminali di ingresso e due di uscita (es. un filtro)
- **Quarzo** — cristallo piezoelettrico usato come risonatore meccanico ad altissimo Q per oscillatori stabili
- **Resistenza parassita** — resistenza intrinseca non desiderata di un componente reale, che rappresenta le perdite di energia
- **Selettività** — capacità di un ricevitore di discriminare un segnale rispetto ad altri di frequenza diversa

---

## 👥 Partecipanti

- 👨‍🏫 **Relatori**: Paolo (lezione principale su filtri, risonanza e quarzi), Sauro (quiz e ripasso lezione 05)
- 📋 **Coordinamento**: Fabrizio, Alessio
- 🎓 **Partecipanti**: aspiranti radioamatori ARI Toscana CRT 2025 (interventi di Claudio, Marco, Luigi, Antonio, Nicola, Massimo, Giovanni, Sebastian, Leonardo, Maria, Franco, Alessandro, Salvatore, Matteo)

---

## ⏱️ Evidenze Temporali

| Intervallo      | Argomento                                                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 00:04 – 22:14   | Revisione quiz Lezione 05: condensatori, reattanza capacitiva, impedenza, legge di Ohm                                           |
| 22:14 – 27:25   | Introduzione ai filtri: concetto, reattanza variabile con la frequenza                                                           |
| 27:25 – 46:16   | Filtro passa basso: funzionamento, frequenza di taglio (0,707 / metà potenza), schemi RC e LC, poli, applicazioni pratiche       |
| 46:16 – 60:20   | Domande e discussione: quadripoli, massa, filtri nelle casse acustiche, bobine perpendicolari per evitare mutua induzione        |
| 60:20 – 66:46   | Filtro passa alto: funzionamento speculare, schema con C in serie                                                                |
| 66:46 – 75:02   | Filtro passa banda e filtro elimina banda: definizioni, due frequenze di taglio, applicazioni (ricevitori radio, filtro anti-FM) |
| 75:02 – 78:31   | Riepilogo visivo dei quattro tipi di filtro (curve ideali)                                                                       |
| 78:31 – 93:57   | Circuiti risonanti: frequ. di risonanza $f_0$, risonanza parallelo (Z infinita), risonanza serie (Z nulla)                       |
| 93:57 – 109:23  | Fattore di merito Q, larghezza di banda, esercizi ($Q = f_0/B$), componenti reali e perdite                                      |
| 109:23 – 122:02 | Cristalli di quarzo: piezoelettricità, risonanza meccanica, Q altissimo, applicazioni                                            |
| 122:02 – fine   | Organizzazione: iscrizioni ARI, sezioni, quiz prossima lezione                                                                   |

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Lezione**          | 06                                                                                                                                                                                                                                                                                               |
| **Data**             | 9 aprile 2025                                                                                                                                                                                                                                                                                    |
| **Durata**           | ~2 ore e 30 minuti                                                                                                                                                                                                                                                                               |
| **Numero argomenti** | 9                                                                                                                                                                                                                                                                                                |
| **Parole chiave**    | filtri, passa basso, passa alto, passa banda, elimina banda, frequenza di taglio, $0{,}707$, $-3$ dB, circuito risonante, risonanza, $f_0 = 1/(2\pi\sqrt{LC})$, impedenza infinita, impedenza nulla, fattore di merito Q, $Q = f_0/B$, larghezza di banda, quarzo, piezoelettricità, selettività |
