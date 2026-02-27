# 📘 Lezione 08 - Oscillatori

## 📌 Overview

- **Materia**: Matematica applicata alla radiotecnica
- **Argomento**: Notazione scientifica, equivalenze tra unità di misura, equazioni di primo grado, logaritmi in base 10
- **Tempo di studio stimato**: 60–80 minuti
- **Prerequisiti**: Concetti base di algebra (potenze, frazioni), legge di Ohm e formula della potenza (Lezioni 01-02), unità di misura usate in elettronica (Henry, Farad, Ohm, Ampere, Volt, Watt)
- **Obiettivi di apprendimento**:
  - Saper convertire numeri da notazione scientifica a notazione decimale e viceversa
  - Padroneggiare le equivalenze tra multipli e sottomultipli delle unità di misura (da pico a giga)
  - Risolvere equazioni di primo grado per ricavare formule inverse (es. legge di Ohm)
  - Comprendere la definizione di logaritmo in base 10
  - Applicare le proprietà dei logaritmi per risolvere semplici equazioni logaritmiche

---

## 📖 Core Content

### 1. 🔢 Notazione Scientifica (⏱ 05:04–15:52)

#### 🔹 Concetti di base

La **notazione scientifica** è un modo per rappresentare numeri molto grandi o molto piccoli usando le potenze del 10. Un numero in notazione scientifica è composto da:

- Una **parte numerica** (parte intera e decimale)
- Una **potenza del 10** che indica l'ordine di grandezza

Ad esempio: $17{,}5 \times 10^3 = 17.500$

**Potenza del 10 positiva** — Indica che si aggiungono zeri a destra: il numero diventa più grande. Si sposta la virgola verso **destra** di tante posizioni quante indicate dall'esponente.

**Potenza del 10 negativa** — Indica che si aggiungono zeri a sinistra: il numero diventa più piccolo (più vicino a zero, ma sempre positivo). Si sposta la virgola verso **sinistra** di tante posizioni quante indicate dal valore assoluto dell'esponente.

> ⚠️ **Errore comune**: "Numeri molto piccoli" non significa "numeri negativi". Significa numeri positivi che si avvicinano a zero (es. $0{,}0118$).

#### 🔹 Regole di conversione

- **Da notazione scientifica a decimale**: partire dalla posizione della virgola. Se l'esponente è **positivo**, spostare la virgola verso destra; se **negativo**, verso sinistra.
  - Esempio: $17{,}5 \times 10^3 = 17.500$ (virgola spostata di 3 posizioni a destra)
  - Esempio: $1{,}18 \times 10^{-2} = 0{,}0118$ (virgola spostata di 2 posizioni a sinistra)

- **Cambio di esponente**: è possibile passare da una rappresentazione esponenziale a un'altra spostando la virgola e modificando l'esponente di conseguenza.
  - Esempio: $59{,}1 \times 10^{-3} = 5{,}91 \times 10^{-2}$ (virgola a sinistra di 1 → esponente aumenta di 1)
  - Attenzione al **segno** dell'esponente: se l'esponente è negativo, diminuirlo ulteriormente (renderlo più negativo) corrisponde a spostare la virgola a **destra**, non a sinistra.

> ⚠️ **Attenzione**: nella notazione anglosassone la virgola separa le migliaia e il punto separa i decimali — l'opposto della notazione italiana. Se si consultano risorse online in inglese, prestare attenzione a questa differenza.

---

### 2. 📐 Equivalenze tra Unità di Misura (⏱ 15:59–39:04)

#### 🔹 Multipli e sottomultipli

Nella radiotecnica si usano frequentemente grandezze espresse in multipli o sottomultipli delle unità di misura fondamentali. La tabella seguente riporta quelli più rilevanti:

| Prefisso     | Simbolo      | Potenza del 10 | Valore            |
| ------------ | ------------ | -------------- | ----------------- |
| Tera         | T            | $10^{12}$      | 1.000.000.000.000 |
| Giga         | G            | $10^{9}$       | 1.000.000.000     |
| Mega         | M            | $10^{6}$       | 1.000.000         |
| Kilo         | k            | $10^{3}$       | 1.000             |
| (unità base) | —            | $10^{0}$       | 1                 |
| Milli        | m            | $10^{-3}$      | 0,001             |
| Micro        | µ (mu greca) | $10^{-6}$      | 0,000001          |
| Nano         | n            | $10^{-9}$      | 0,000000001       |
| Pico         | p            | $10^{-12}$     | 0,000000000001    |

Dai kilo in su, le grandezze scalano di **1000 in 1000** (cioè di $10^3$ in $10^3$). Stessa cosa dal milli in giù. Tra unità base, deca, etto e kilo la scala è di 10 in 10.

#### 🔹 Unità di misura comuni in radiotecnica

- **Farad**: spesso espresso in nano e picofarad (nF, pF)
- **Henry**: spesso espresso in millihenry e microhenry (mH, µH)
- **Ohm**: può trovarsi in micro e milliohm, ma anche in kilohm e megaohm
- **Ampere**: spesso in milliampere (mA) e a volte microampere (µA)
- **Hertz**: le frequenze si esprimono in kilohertz (kHz), megahertz (MHz), gigahertz (GHz)
- **Watt**: spesso in milliwatt (mW) e microwatt (µW)

#### 🔹 Regola fondamentale per le equivalenze

Per convertire tra unità di misura diverse della stessa grandezza:

- **Da unità più grande a più piccola** → si **moltiplica** per la potenza di 10 corrispondente (il numero diventa più grande)
- **Da unità più piccola a più grande** → si **divide** per la potenza di 10 corrispondente (il numero diventa più piccolo)

In pratica, si conta quanti "scaloni" separano le due unità (ogni scalino = $\times 10^3$):

| Da → A        | Operazione                                               |
| ------------- | -------------------------------------------------------- |
| milli → micro | $\times 10^3$ (1 scalino verso il basso)                 |
| micro → milli | $\div 10^3$ (1 scalino verso l'alto)                     |
| milli → Henry | $\times 10^{-3}$ (1 scalino verso l'alto all'unità base) |
| MHz → Hz      | $\times 10^6$ (2 scalini verso il basso)                 |

#### 🔹 Esempio pratico: conversione di induttanza

$0{,}012 \text{ mH} = ?\ \mu\text{H}$

Da milli a micro si scende di uno scalino → si moltiplica per $10^3$:

$$0{,}012 \times 10^3 = 12\ \mu\text{H}$$

#### 🔹 Importanza dell'omogeneità

Quando si devono combinare grandezze in una formula (somma, sottrazione, ecc.), è **indispensabile** che siano espresse nella stessa unità di misura. Ad esempio, per sommare tre resistenze in serie:

- $R_1 = 0{,}2\ \Omega$, $R_2 = 20\ \text{m}\Omega$, $R_3 = 2000\ \mu\Omega$

Convertendo tutto in milliohm:

- $R_1 = 200\ \text{m}\Omega$
- $R_2 = 20\ \text{m}\Omega$
- $R_3 = 2\ \text{m}\Omega$

$$R_{tot} = 200 + 20 + 2 = 222\ \text{m}\Omega$$

> ⚠️ **Errore da evitare all'esame**: sommare numeri in unità diverse senza prima convertirli. Ad esempio, $0{,}2 + 2000 = 2000{,}2$ non ha alcun significato se le unità non sono omogenee.

---

### 3. ➗ Equazioni di Primo Grado e Formule Inverse (⏱ 39:43–60:23)

#### 🔹 Principio fondamentale delle equazioni

Un'**equazione** è una dichiarazione di equivalenza: ciò che sta a sinistra del simbolo $=$ ha lo stesso valore di ciò che sta a destra. Se si esegue la **stessa operazione** (somma, sottrazione, moltiplicazione, divisione) su **entrambi i membri**, l'uguaglianza resta valida.

Questo principio permette di **isolare l'incognita**: si spostano tutti i termini noti da una parte e l'incognita dall'altra.

#### 🔹 Esempio algebrico

$$3x + 6 = 12$$

1. Sottrarre 6 da entrambi i membri: $3x = 6$
2. Dividere per 3 entrambi i membri: $x = 2$

#### 🔹 Applicazione alla legge di Ohm

La legge di Ohm è:

$$I = \frac{V}{R}$$

Da questa **unica formula** si ricavano tutte le altre per semplice manipolazione algebrica:

- Per trovare $R$: moltiplicare entrambi i membri per $R$, poi dividere per $I$:

$$R = \frac{V}{I}$$

- Per trovare $V$: moltiplicare entrambi i membri per $R$:

$$V = I \times R$$

> **Consiglio pratico**: non è necessario memorizzare tutte le formule inverse. Basta ricordare **una sola formula** (ad es. $V = I \times R$) e ricavare le altre isolando l'incognita desiderata. In caso di dubbio, si può anche verificare con numeri: se $V = I \times R$ e $10 = 5 \times 2$, allora $R = V/I = 10/5 = 2$.

#### 🔹 Esercizio svolto: trovare la resistenza

Dati: $V = 20$ V, $I = 200$ mA

1. Convertire $I$ in ampere: $200\ \text{mA} = 0{,}2$ A
2. Applicare $R = V / I = 20 / 0{,}2 = 100\ \Omega$

> ⚠️ L'unità di misura dell'ohm è volt/ampere. Bisogna prima convertire i milliampere in ampere per avere il risultato in ohm.

#### 🔹 Applicazione alla formula della potenza

La potenza dissipata è:

$$P = V \times I$$

Se non si conosce la corrente ma si conoscono $V$ e $R$, si può sostituire $I = V/R$ nella formula della potenza:

$$P = V \times \frac{V}{R} = \frac{V^2}{R}$$

Esempio: $V = 20$ V, $R = 50\ \Omega$

$$P = \frac{20^2}{50} = \frac{400}{50} = 8\ \text{W}$$

Questo mostra la tecnica della **sostituzione**: in un'equazione si può sostituire a una grandezza l'espressione equivalente derivata da un'altra formula.

---

### 4. 📊 I Logaritmi (⏱ 70:07–120:07)

#### 🔹 Definizione

Il **logaritmo in base $z$ dell'argomento $y$** è l'esponente $x$ che si deve dare alla base $z$ per ottenere $y$:

$$\log_z y = x \iff z^x = y$$

I due logaritmi più comuni sono:

- **Logaritmo in base 10** (logaritmo comune): si scrive $\log$ o $\log_{10}$. La base 10 spesso si omette.
- **Logaritmo naturale**: si scrive $\ln$ (base $e \approx 2{,}718$). Non serve per gli esercizi radioamatoriali.

#### 🔹 Interpretazione pratica

Il logaritmo in base 10 risponde alla domanda: **"Qual è l'esponente da dare a 10 per ottenere quel numero?"**

Esempi immediati:

- $\log 1000 = 3$ perché $10^3 = 1000$
- $\log 100 = 2$ perché $10^2 = 100$
- $\log 10 = 1$ perché $10^1 = 10$
- $\log 1 = 0$ perché $10^0 = 1$ (vale per qualunque base)

Per valori non interi (es. $\log 12$), si usa la calcolatrice: scrivere l'argomento, poi premere il tasto **LOG**.

#### 🔹 Proprietà delle potenze (rilevanti per i logaritmi)

Poiché il logaritmo è essenzialmente un esponente, le regole delle potenze si riflettono sulle proprietà dei logaritmi:

| Proprietà delle potenze   | Formula                     |
| ------------------------- | --------------------------- |
| Prodotto con stessa base  | $a^x \times a^y = a^{x+y}$  |
| Esponente negativo        | $a^{-x} = \frac{1}{a^x}$    |
| Potenza di potenza        | $(a^x)^y = a^{x \cdot y}$   |
| Quoziente con stessa base | $\frac{a^x}{a^y} = a^{x-y}$ |
| Casi particolari          | $a^1 = a$; $a^0 = 1$        |

#### 🔹 Proprietà dei logaritmi

| Proprietà                 | Formula                              | Esempio                              |
| ------------------------- | ------------------------------------ | ------------------------------------ |
| Definizione               | $10^{\log y} = y$                    | $10^{\log 25} = 25$                  |
| Logaritmo di un prodotto  | $\log(a \times b) = \log a + \log b$ | $\log(2 \times 3) = \log 2 + \log 3$ |
| Logaritmo di un quoziente | $\log\frac{a}{b} = \log a - \log b$  | $\log\frac{3}{2} = \log 3 - \log 2$  |
| Logaritmo di una potenza  | $\log(a^n) = n \times \log a$        | $\log(2^3) = 3 \times \log 2$        |

Queste proprietà sono fondamentali per risolvere equazioni logaritmiche e saranno usate nel calcolo dei decibel.

#### 🔹 Risoluzione di equazioni con logaritmi

Il metodo consiste nell'**isolare il logaritmo con l'incognita** da un lato dell'equazione, poi applicare la definizione di logaritmo per trovare il valore.

**Esempio 1**: $20 \times \log\left(\frac{x}{50}\right) = 1{,}5$

1. Dividere entrambi i membri per 20: $\log\left(\frac{x}{50}\right) = 0{,}075$
2. Applicare la proprietà del quoziente: $\log x - \log 50 = 0{,}075$
3. Sommare $\log 50$ a entrambi i membri: $\log x = 0{,}075 + \log 50 = 0{,}075 + 1{,}699 = 1{,}774$
4. Applicare la definizione: $x = 10^{1{,}774} \approx 59{,}4$

**Esempio 2**: $10 \times \log\left(\frac{100}{x}\right) = 3$

1. Dividere per 10: $\log\left(\frac{100}{x}\right) = 0{,}3$
2. Scomporre: $\log 100 - \log x = 0{,}3$, quindi $2 - \log x = 0{,}3$
3. Isolare: $\log x = 1{,}7$
4. Risolvere: $x = 10^{1{,}7} \approx 50{,}1$

> **Nota**: il docente ha accennato che i logaritmi saranno usati nel calcolo dei **decibel** (dB), argomento che sarà trattato nelle lezioni successive da Paolo. La struttura tipica delle equazioni logaritmiche d'esame è proprio della forma $N \times \log\left(\frac{x}{y}\right) = k$ o $N \times \log\left(\frac{y}{x}\right) = k$, dove $N$ è tipicamente 10 o 20.

#### 🔹 Consigli per l'esame

- La calcolatrice è molto utile per i logaritmi, ma non è sempre ammessa all'esame (dipende dalla commissione e dal decreto ministeriale in vigore).
- Se la calcolatrice non è ammessa, i calcoli saranno sufficientemente semplici da farsi a mente.
- All'esame le domande sono a **risposta multipla** (di solito 3 opzioni): una è chiaramente errata, le altre due richiedono ragionamento.
- Pochi valori di logaritmo ricorrono frequentemente: $\log 2 \approx 0{,}301$, $\log 3 \approx 0{,}477$, $\log 10 = 1$, $\log 100 = 2$.

---

## 🔗 Concept Map (testuale)

- **Notazione scientifica** → usa → **Potenze del 10** per rappresentare numeri grandi e piccoli
- **Multipli e sottomultipli** → sono espressi come → **Potenze del 10** (kilo = $10^3$, milli = $10^{-3}$, micro = $10^{-6}$, ecc.)
- **Equivalenze** → richiedono → **Omogeneità** delle unità di misura prima di combinare grandezze
- **Equazioni di primo grado** → usano il principio di → **Uguaglianza** (stessa operazione su entrambi i membri)
- **Formule inverse** → si ricavano da → **Equazioni di primo grado** isolando l'incognita
- **Legge di Ohm** ($I = V/R$) → consente di ricavare → $R = V/I$ e $V = I \times R$
- **Formula della potenza** ($P = V \times I$) → combinata con la legge di Ohm → $P = V^2/R$
- **Logaritmo in base 10** → è definito come → l'**Esponente** da dare a 10 per ottenere l'argomento
- **Proprietà dei logaritmi** → derivano dalle → **Proprietà delle potenze**
- **Logaritmo di un prodotto** → è uguale alla → **Somma dei logaritmi** dei fattori
- **Logaritmo di un quoziente** → è uguale alla → **Differenza dei logaritmi** (numeratore meno denominatore)
- **Decibel** → utilizzerà → **Logaritmi in base 10** (argomento futuro)

---

## 📝 Key Takeaways

1. La **notazione scientifica** rappresenta un numero come parte numerica × potenza del 10. Esponente positivo → numero grande (virgola a destra); esponente negativo → numero piccolo (virgola a sinistra), mai negativo.

2. Le grandezze in radiotecnica usano prefissi standard: dal **pico** ($10^{-12}$) al **tera** ($10^{12}$), passando per nano, micro, milli, kilo, mega, giga. Da milli in giù e da kilo in su, si scala di $10^3$ alla volta.

3. Per convertire tra unità di misura: da unità **più grande a più piccola** si **moltiplica**; da **più piccola a più grande** si **divide**. Ad esempio: 0,012 mH × 1000 = 12 µH.

4. Prima di combinare grandezze in una formula, esse devono essere **omogenee** (stessa unità di misura). Questo è un trabocchetto frequente all'esame.

5. Le **equazioni di primo grado** si risolvono applicando la stessa operazione a entrambi i membri per isolare l'incognita. Non serve memorizzare tutte le formule inverse: basta conoscerne una e ricavare le altre.

6. Il **logaritmo in base 10** di un numero $y$ è l'esponente da dare a 10 per ottenere $y$. Esempi fondamentali: $\log 10 = 1$, $\log 100 = 2$, $\log 1000 = 3$, $\log 1 = 0$.

7. Le proprietà chiave dei logaritmi: il logaritmo di un **prodotto** è la somma dei logaritmi; il logaritmo di un **quoziente** è la differenza; il logaritmo di una **potenza** è l'esponente per il logaritmo della base.

8. Per risolvere un'equazione logaritmica: isolare il logaritmo con l'incognita, poi applicare la definizione ($\log x = k \Rightarrow x = 10^k$). La struttura tipica all'esame è $N \times \log(x/y) = k$.

---

## ❓ Comprehension Questions

1. Come si converte il numero $4{,}7 \times 10^{-5}$ in notazione decimale? Spiega il procedimento passo per passo.

2. Se hai una capacità di 4700 pF e un'altra di 0,0047 µF, sono la stessa grandezza? Come verifichi che siano omogenee per poterle sommare?

3. Partendo dalla formula della potenza $P = V \times I$ e dalla legge di Ohm $I = V/R$, ricava la formula $P = I^2 \times R$. Mostra tutti i passaggi.

4. Spiega con parole tue cosa significa $\log 500 \approx 2{,}7$ e come verificheresti questo risultato.

5. Perché il logaritmo in base 10 di 1 è sempre uguale a 0? Come si collega alla proprietà delle potenze?

6. Un circuito è alimentato da una batteria da 12 V. Se passa una corrente di 250 mA, qual è la resistenza? Mostra tutti i passaggi, inclusa la conversione delle unità.

7. All'esame trovi tre resistenze da sommare: $0{,}5$ Ω, $500$ mΩ e $500.000$ µΩ. Un candidato ha risposto 500.501 Ω. Dov'è l'errore e qual è il risultato corretto?

8. Risolvi l'equazione $10 \times \log\left(\frac{x}{5}\right) = 7$ mostrando tutti i passaggi. Qual è la proprietà dei logaritmi che usi per semplificare?

---

## 📚 Glossary

- **Equivalenza (di unità di misura)** — Espressione di una stessa grandezza fisica in un multiplo o sottomultiplo diverso ma di uguale valore (es. 12 µH = 0,012 mH).
- **Equazione di primo grado** — Equazione algebrica in cui l'incognita compare con esponente 1 e si risolve isolando l'incognita mediante operazioni inverse.
- **Formula inversa** — Riscrittura di una formula per esprimere una grandezza diversa come incognita (es. da $I = V/R$ si ricava $R = V/I$).
- **Giga (G)** — Prefisso per $10^9$ (un miliardo).
- **Kilo (k)** — Prefisso per $10^3$ (mille).
- **Logaritmo** — L'esponente da dare alla base per ottenere un dato argomento. Il logaritmo in base 10 di $y$ è il numero $x$ tale che $10^x = y$.
- **Logaritmo in base 10 (log)** — Logaritmo comune, usato nella definizione dei decibel. Il 10 è spesso omesso: $\log y \equiv \log_{10} y$.
- **Logaritmo naturale (ln)** — Logaritmo in base $e \approx 2{,}718$. Non usato negli esercizi radioamatoriali.
- **Mega (M)** — Prefisso per $10^6$ (un milione).
- **Micro (µ)** — Prefisso per $10^{-6}$ (un milionesimo). Simbolo: lettera greca mu.
- **Milli (m)** — Prefisso per $10^{-3}$ (un millesimo).
- **Nano (n)** — Prefisso per $10^{-9}$ (un miliardesimo).
- **Notazione scientifica** — Rappresentazione di un numero come prodotto di una parte numerica e una potenza del 10.
- **Omogeneità delle unità** — Condizione necessaria per combinare grandezze: devono essere espresse nella stessa unità di misura.
- **Pico (p)** — Prefisso per $10^{-12}$ (un bilionesimo).
- **Potenza del 10** — Numero espresso come $10^n$; l'esponente $n$ indica quanti zeri seguono l'1 (se positivo) o quante posizioni decimali prima della cifra significativa (se negativo).
- **Sostituzione** — Tecnica algebrica che consiste nel sostituire a una grandezza la sua espressione equivalente ricavata da un'altra formula.
- **Tera (T)** — Prefisso per $10^{12}$ (mille miliardi).

---

## 👥 Partecipanti

- 👨‍🏫 **Relatrice principale**: Lucia — docente della lezione di matematica applicata alla radiotecnica
- 👨‍🏫 **Co-docenti/coordinatori**: Fabrizio (coordinamento corso), Alessio (informazioni esame, esperienza anni precedenti)
- 🎓 **Partecipanti**: Marco, Roberto (nuovo iscritto), Alessandro, Giovanni, Claudio e altri corsisti del Corso Aspiranti Radioamatori ARI Toscana CRT 2025

---

## ⏱️ Evidenze Temporali

| Intervallo    | Contenuto                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| 00:02–05:04   | Presentazione della docente Lucia, introduzione alla lezione di matematica                                    |
| 05:04–15:52   | Notazione scientifica: conversione tra notazione esponenziale e decimale, esercizi con errori da individuare  |
| 15:59–30:10   | Tabella dei multipli/sottomultipli, equivalenze tra unità di misura (milli, micro, nano, pico)                |
| 30:10–39:04   | Esercizi pratici di equivalenze con unità miste (Ω, mΩ, µΩ), frequenze (MHz → Hz), corrente (mA → A)          |
| 39:43–56:23   | Equazioni di primo grado, isolamento dell'incognita, formule inverse di Ohm ($R = V/I$, $V = I \times R$)     |
| 56:23–60:23   | Formula della potenza $P = V^2/R$ (per sostituzione), calcolo corrente dal circuito                           |
| 60:55–70:07   | Pausa e discussione informale: importanza dell'esercizio, rassicurazioni sull'esame                           |
| 70:07–82:03   | Definizione di logaritmo, proprietà delle potenze, proprietà dei logaritmi (prodotto, quoziente, potenza)     |
| 82:03–95:01   | Esercizi con logaritmi: calcoli diretti ($3 \log 2 + \log 3$), equazioni logaritmiche con incognita           |
| 95:01–120:07  | Secondo esercizio logaritmico (incognita al denominatore), esercizio libero più complesso                     |
| 120:07–130:05 | Consigli per l'esame: calcolatrice, risposta multipla, difficoltà dei calcoli, programmazione esercizi futuri |

---

## 📅 Informazioni Lezione

| Campo                  | Valore                                                                                                                                                                                                     |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Numero lezione**     | 08                                                                                                                                                                                                         |
| **Data**               | 23 aprile 2025                                                                                                                                                                                             |
| **Durata**             | ~130 minuti                                                                                                                                                                                                |
| **Argomenti trattati** | 4 (Notazione scientifica, Equivalenze unità, Equazioni di primo grado, Logaritmi)                                                                                                                          |
| **Parole chiave**      | Notazione scientifica, potenze del 10, multipli, sottomultipli, milli, micro, nano, pico, equivalenze, equazioni, formule inverse, legge di Ohm, potenza, logaritmo, base 10, proprietà logaritmi, decibel |
| **Prossima lezione**   | 7 maggio 2025                                                                                                                                                                                              |
