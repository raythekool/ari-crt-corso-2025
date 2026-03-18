---
layout: default
permalink: /guide-studio/lezione_05.html
---

# 📘 Lezione 05 - Componenti Elettronici

## 📌 Overview

- **Materia e argomento**: Elettrotecnica — il condensatore, la reattanza capacitiva e l'impedenza. Viene completata la trattazione dei tre componenti fondamentali (resistore, induttore, condensatore) e introdotto il concetto unificante di impedenza.
- **Tempo di studio stimato**: 90–120 minuti
- **Prerequisiti**: Legge di Ohm, resistenze in serie/parallelo (Lezione 02), corrente alternata e valore efficace (Lezione 03), induttore e reattanza induttiva (Lezione 04).
- **Obiettivi di apprendimento**:
  - Comprendere struttura e funzionamento del condensatore
  - Definire la capacità e la sua unità di misura (Farad) con i sottomultipli
  - Calcolare condensatori in serie e in parallelo (regole invertite rispetto alle resistenze)
  - Comprendere lo sfasamento di 90° (corrente in anticipo sulla tensione) nei condensatori
  - Calcolare la reattanza capacitiva con $X_C = \frac{1}{2\pi fC}$
  - Definire e calcolare l'impedenza $Z = \sqrt{R^2 + (X_L - X_C)^2}$
  - Distinguere potenza apparente, attiva e reattiva in corrente alternata

---

## 📖 Core Content

## 🔋 1. Il condensatore: struttura e funzionamento (⏱ 39:20)

### 🔹 Cos'è un condensatore

Il **condensatore** è un componente elettronico che accumula carica elettrica quando è connesso a un generatore di tensione. È formato da **due piastre conduttive** (chiamate **armature**) separate da un materiale isolante detto **dielettrico**. Il dielettrico può essere aria, plastica, mica, ceramica o un elettrolita.

Il simbolo elettrico del condensatore è costituito da due barrette parallele con i terminali.

### 🔹 Campo elettrico e carica

Quando si applica una tensione ai capi del condensatore, le cariche elettriche si accumulano sulle armature: cariche positive su un lato e cariche negative sull'altro, in funzione della polarità del generatore. Fra le armature si sviluppa un **campo elettrico** che rappresenta l'energia immagazzinata.

### 🔹 Il ruolo del dielettrico

L'interposizione di un materiale isolante (dielettrico) fra le armature ha due effetti:

1. **Aumenta la capacità** del condensatore, perché si formano ulteriori superfici affacciate fra armature e dielettrico
2. **Impone una tensione massima di lavoro**: ogni dielettrico ha una **rigidità dielettrica** — la tensione massima applicabile prima che l'isolante si perfori ("si buchi"). Anche l'aria ha una sua rigidità dielettrica.

### 🔹 Comportamento con corrente continua e alternata

- **Corrente continua**: il condensatore si comporta come un **circuito aperto** — la corrente non può attraversare il dielettrico isolante
- **Corrente alternata**: il condensatore presenta una **reattanza capacitiva** che permette alla corrente alternata di attraversarlo

> Questo è l'**opposto** dell'induttore, che lascia passare la corrente continua e ostacola l'alternata.

### 🔹 Tipologie di condensatori

| Tipo                    | Caratteristiche                             | Valori tipici            |
| ----------------------- | ------------------------------------------- | ------------------------ |
| **A mica**              | Alta stabilità, capacità indicata in pF     | es. 500 pF, 500 V        |
| **A film plastico**     | Parallelepipedo, capacità in nF             | es. 22 nF                |
| **Elettrolitici**       | Nastro avvolto in cilindro, grandi capacità | centinaia/migliaia di µF |
| **Ad aria (variabili)** | Lamelle rotanti, usati per sintonia radio   | variabili                |

I **condensatori variabili** ad aria sono formati da lamelle fisse (statore) e lamelle rotanti (rotore); girando la manopola si varia la superficie affacciata e quindi la capacità. Il simbolo elettrico è il condensatore con una freccia sopra.

---

## 📐 2. La capacità e la sua unità di misura (⏱ 46:00)

### 🔹 Definizione

La **capacità** (C) esprime quanta carica elettrica può immagazzinare un condensatore per ogni volt di tensione applicata:

> $$C = \frac{Q}{V}$$

Dove:

- **C** = capacità in Farad (F)
- **Q** = carica elettrica in Coulomb (C)
- **V** = tensione ai capi in Volt (V)

L'unità di misura è il **Farad** (F): 1 Farad = 1 Coulomb / 1 Volt.

### 🔹 Sottomultipli del Farad

Il Farad è un'unità molto grande; nella pratica si usano solo sottomultipli:

| Sottomultiplo | Simbolo | Valore       | Notazione                     |
| ------------- | ------- | ------------ | ----------------------------- |
| microfarad    | µF      | $10^{-6}$ F  | un milionesimo                |
| nanofarad     | nF      | $10^{-9}$ F  | un millesimo di milionesimo   |
| picofarad     | pF      | $10^{-12}$ F | un milionesimo di milionesimo |

### 🔹 Formula costruttiva della capacità

La capacità dipende dalle caratteristiche fisiche del condensatore:

> $$C = \varepsilon \cdot \frac{S}{D}$$

Dove:

- **ε (epsilon)** = costante dielettrica del materiale isolante
- **S** = superficie delle armature affacciate
- **D** = distanza fra le armature

Relazioni di proporzionalità:

- C è **direttamente proporzionale** alla costante dielettrica ε
- C è **direttamente proporzionale** alla superficie S delle armature
- C è **inversamente proporzionale** alla distanza D fra le armature

⚠️ _Queste relazioni sono frequente oggetto di domande d'esame._

---

## 🔗 3. Condensatori in serie e in parallelo (⏱ 57:36)

### 🔹 Regola fondamentale: l'opposto delle resistenze

Le formule per condensatori in serie e in parallelo sono **invertite** rispetto a resistenze e induttori:

### 🔹 Condensatori in parallelo — si sommano

> $$C_{tot} = C_1 + C_2 + C_3 + \ldots$$

In parallelo la superficie affacciata aumenta, quindi la capacità totale **aumenta**.

### 🔹 Condensatori in serie — formula del reciproco

> $$\frac{1}{C_{tot}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \ldots$$

Casi particolari:

- Due condensatori **uguali** in serie: $C_{tot} = C/2$ (metà del valore di ciascuno)
- N condensatori **uguali** in serie: $C_{tot} = C/N$
- Il risultato è sempre **minore del condensatore più piccolo**

> **Tabella riassuntiva serie/parallelo:**
>
> | Componente | Serie | Parallelo |
> |---|---|---|
> | Resistenze | Si sommano | Formula reciproco |
> | Induttori | Si sommano | Formula reciproco |
> | Condensatori | Formula reciproco | **Si sommano** |

---

## ⏱️ 4. Costante di tempo τ = R × C (⏱ 62:07)

### 🔹 Carica e scarica del condensatore

Quando si applica una tensione a un condensatore tramite una resistenza in serie:

- La **corrente** scorre subito (è in anticipo)
- La **tensione** ai capi del condensatore cresce con andamento **esponenziale** fino al valore di regime

La **costante di tempo** è il tempo impiegato dalla tensione per raggiungere il **63%** del valore finale:

> $$\tau = R \times C$$

Dove:

- **τ** = costante di tempo in secondi
- **R** = resistenza in Ohm
- **C** = capacità in Farad

La tensione raggiunge il valore di regime dopo circa **5 costanti di tempo**. La scarica avviene con la stessa legge esponenziale.

> Confronto con l'induttore: nell'induttore la costante di tempo è $\tau = L/R$; nel condensatore è $\tau = R \times C$.

---

## ⚡ 5. Sfasamento nei condensatori: corrente in anticipo di 90° (⏱ 66:08)

### 🔹 Corrente e tensione nel condensatore

In un condensatore alimentato in corrente alternata, la **corrente è in anticipo di 90°** rispetto alla tensione (oppure equivalentemente: la tensione è in ritardo di 90° rispetto alla corrente).

> **Analogia del secchiello**: il condensatore è come un secchio da riempire d'acqua. L'acqua (la corrente) scorre subito; il livello del secchio (la tensione) sale gradualmente. La corrente precede la tensione.

### 🔹 Riepilogo sfasamenti

| Componente       | Sfasamento V–I       | Descrizione                                      |
| ---------------- | -------------------- | ------------------------------------------------ |
| **Resistore**    | 0° (in fase)         | V e I partono e raggiungono i massimi insieme    |
| **Induttore**    | I in ritardo di 90°  | La corrente è ostacolata dalla reattanza         |
| **Condensatore** | I in anticipo di 90° | La corrente scorre subito, la tensione sale dopo |

---

## 📉 6. Reattanza capacitiva $X_C$ (⏱ 67:18)

### 🔹 Definizione e formula

La **reattanza capacitiva** è l'opposizione che un condensatore offre al passaggio della corrente alternata. Si misura in **ohm** e si indica con **$X_C$**:

> $$X_C = \frac{1}{2\pi f C}$$

Dove:

- **$X_C$** = reattanza capacitiva in ohm (Ω)
- **$f$** = frequenza in Hertz (Hz)
- **$C$** = capacità in Farad (F)

### 🔹 Andamento con la frequenza

A differenza della reattanza induttiva (che cresce linearmente), la reattanza capacitiva ha un andamento **iperbolico decrescente**:

- A **frequenza zero** (corrente continua): $X_C = \infty$ → circuito aperto
- All'**aumentare della frequenza**: $X_C$ diminuisce → il condensatore "lascia passare" meglio la corrente
- A **frequenze molto alte**: $X_C \to 0$ → quasi un cortocircuito

> **Confronto**: $X_L$ cresce con la frequenza (retta), $X_C$ diminuisce con la frequenza (iperbole). Il punto dove $X_L = X_C$ si chiama **risonanza**.

### 🔹 Esercizio svolto

Condensatore da 39 pF a diverse frequenze:

| Frequenza | Reattanza $X_C$                                                                                                        |
| --------- | ---------------------------------------------------------------------------------------------------------------------- |
| 1 MHz     | $\frac{1}{2\pi \times 10^6 \times 39 \times 10^{-12}} = \frac{1}{6{,}28 \times 39 \times 10^{-6}} \approx$ **4.083 Ω** |
| 10 MHz    | **408,3 Ω** (10 volte meno)                                                                                            |
| 100 MHz   | **40,8 Ω** (100 volte meno)                                                                                            |

> **Suggerimento per semplificare i calcoli**: con 39 pF ($10^{-12}$) e 1 MHz ($10^{6}$), si semplifica $10^{6}$ con $10^{-12}$ ottenendo $10^{-6}$, evitando numeri troppo grandi o piccoli nella calcolatrice.

---

## 🔧 7. Legge di Ohm generalizzata con le reattanze (⏱ 75:21)

### 🔹 Analogia tra R, $X_L$ e $X_C$

La legge di Ohm si applica identicamente ai tre componenti, sostituendo R con la reattanza appropriata:

| Circuito          | Formula            |
| ----------------- | ------------------ |
| Solo resistenza   | $V = R \times I$   |
| Solo induttore    | $V = X_L \times I$ |
| Solo condensatore | $V = X_C \times I$ |

Le formule inverse ($I = V/X$ e $X = V/I$) funzionano allo stesso modo.

---

## 🔺 8. L'impedenza Z (⏱ 79:15)

### 🔹 Definizione

L'**impedenza** (Z) è la grandezza che tiene conto dell'effetto combinato di resistenza, reattanza induttiva e reattanza capacitiva in un circuito in corrente alternata. Si misura in **ohm** e si indica con la lettera **Z**.

### 🔹 Formula dell'impedenza (Teorema di Pitagora)

> $$Z = \sqrt{R^2 + (X_L - X_C)^2}$$

Questa formula è esattamente il **teorema di Pitagora** applicato alla rappresentazione vettoriale dove:

- **R** (resistenza) sta sull'asse X orizzontale
- **$X_L - X_C$** (reattanza netta) sta sull'asse Y verticale
- **Z** (impedenza) è l'ipotenusa

Casi particolari:

- Solo R → $Z = R$ (legge di Ohm classica)
- Solo $X_L$ → $Z = X_L$
- Solo $X_C$ → $Z = X_C$
- $X_L = X_C$ → $Z = R$ (risonanza)

### 🔹 Rappresentazione come numero complesso

L'impedenza si può esprimere anche come **numero complesso**:

> $$Z = R + jX$$

Dove:

- **R** = parte reale (resistenza)
- **jX** = parte immaginaria (reattanza)
- **+jX** indica reattanza induttiva
- **−jX** indica reattanza capacitiva

Esempio: $Z = 50 + j15$ Ω → 50 Ω resistivi e 15 Ω di reattanza induttiva.

### 🔹 Legge di Ohm con l'impedenza

Usando l'impedenza Z, la legge di Ohm vale **sempre**, sia in corrente continua che alternata:

> $$V = Z \times I \qquad I = \frac{V}{Z} \qquad Z = \frac{V}{I}$$

---

## 📊 9. Potenza in corrente alternata (⏱ 95:09)

### 🔹 Tre tipi di potenza

In un circuito con resistenze e reattanze, tensione e corrente non sono in fase, e la potenza si esprime in tre forme:

| Tipo                       | Formula                                            | Unità                     | Descrizione                              |
| -------------------------- | -------------------------------------------------- | ------------------------- | ---------------------------------------- |
| **Potenza apparente**      | $S = V \times I$                                   | VA (voltampere)           | Tutto ciò che il generatore eroga        |
| **Potenza attiva (reale)** | $P = R \times I^2 = V \times I \times \cos\varphi$ | W (watt)                  | Produce lavoro utile (calore, movimento) |
| **Potenza reattiva**       | $Q = X \times I^2$                                 | VAR (voltampere reattivi) | Circola senza produrre lavoro            |

### 🔹 Rappresentazione vettoriale della potenza

Le tre potenze formano un **triangolo rettangolo** (analogo a quello dell'impedenza):

- Potenza attiva sull'asse X
- Potenza reattiva sull'asse Y
- Potenza apparente come ipotenusa

L'angolo φ è lo sfasamento tra tensione e corrente; il **cos φ** (fattore di potenza) lega potenza attiva e apparente:

> $$P = S \times \cos\varphi$$

### 🔹 Applicazione pratica: rifasamento

L'Enel impone alle utenze industriali un **cos φ ≥ 0,8** (rifasamento). I carichi industriali sono spesso induttivi (motori, trasformatori), causando correnti reattive elevate che occupano le linee senza produrre lavoro. Il rifasamento consiste nel ridurre l'angolo φ, tipicamente aggiungendo condensatori.

---

## 🔗 Concept Map (testuale)

- **Condensatore** → è composto da → **Due armature + dielettrico**
- **Dielettrico** → determina → **Capacità (ε) e tensione massima (rigidità dielettrica)**
- **Capacità (C)** → si misura in → **Farad (F), sottomultipli: µF, nF, pF**
- **Capacità** → dipende da → **ε (dielettrico), S (superficie), 1/D (distanza)**
- **Condensatore in AC** → produce → **Sfasamento 90° (corrente in anticipo)**
- **Condensatore** → oppone → **Reattanza capacitiva $X_C = 1/(2\pi fC)$**
- **$X_C$** → diminuisce con → **Frequenza (andamento iperbolico)**
- **Resistenza + Reattanze** → si combinano in → **Impedenza $Z = \sqrt{R^2 + (X_L - X_C)^2}$**
- **Impedenza** → sostituisce R in → **Legge di Ohm generalizzata ($V = ZI$)**
- **Sfasamento V–I** → determina → **Cos φ (fattore di potenza)**
- **Potenza apparente** → si divide in → **Potenza attiva (lavoro utile) + Potenza reattiva**

---

## 📝 Key Takeaways

1. Il condensatore accumula carica elettrica sotto forma di campo elettrico. Blocca la corrente continua e lascia passare la corrente alternata — l'opposto dell'induttore.
2. La capacità si misura in **Farad** (F), con sottomultipli µF, nF, pF. Dipende dalla superficie delle armature (S), dalla costante dielettrica (ε) e inversamente dalla distanza (D).
3. I condensatori in **parallelo** si sommano; in **serie** si usa la formula del reciproco — regole **invertite** rispetto a resistenze e induttori.
4. In un condensatore, la **corrente è in anticipo di 90°** rispetto alla tensione. Nell'induttore accade l'opposto.
5. La reattanza capacitiva $X_C = 1/(2\pi fC)$ **diminuisce** all'aumentare della frequenza (l'inverso della reattanza induttiva).
6. L'**impedenza** $Z = \sqrt{R^2 + (X_L - X_C)^2}$ è il parametro universale che combina R, $X_L$ e $X_C$. Si usa nella legge di Ohm al posto di R per qualsiasi circuito.
7. In corrente alternata la potenza si divide in **attiva** (produce lavoro, W), **reattiva** (circola inutilmente, VAR) e **apparente** (totale, VA), legate dal fattore di potenza cos φ.

---

## ❓ Comprehension Questions

1. Perché il condensatore blocca la corrente continua ma lascia passare la corrente alternata? In cosa differisce dall'induttore?
2. Come varia la capacità di un condensatore se si raddoppia la distanza fra le armature mantenendo invariati gli altri parametri?
3. Tre condensatori da 30 µF ciascuno sono collegati in serie. Qual è la capacità totale? E se fossero in parallelo?
4. Calcolare la reattanza capacitiva di un condensatore da 100 pF a 10 MHz. Spiegare il procedimento di semplificazione degli esponenti.
5. In un circuito sono presenti una resistenza di 30 Ω e una reattanza induttiva di 40 Ω (nessuna capacità). Qual è l'impedenza totale?
6. Spiegare perché la formula dell'impedenza è un'applicazione del teorema di Pitagora. Cosa rappresentano i due cateti e l'ipotenusa?
7. Un circuito ha cos φ = 0,5. Qual è la percentuale di potenza attiva rispetto alla potenza apparente? Perché l'Enel richiede il rifasamento?
8. Descrivere un'applicazione pratica in cui un induttore viene usato per bloccare la corrente alternata lasciando passare la continua.

---

## 📚 Glossary

- **Armatura** — ciascuna delle due piastre conduttive che compongono un condensatore
- **Capacità (C)** — grandezza che esprime quanta carica elettrica un condensatore può immagazzinare per unità di tensione; si misura in Farad
- **Condensatore** — componente elettronico formato da due armature separate da un dielettrico, che immagazzina energia sotto forma di campo elettrico
- **Condensatore variabile** — condensatore la cui capacità può essere regolata (es. ruotando lamelle); usato per la sintonia radio
- **Costante dielettrica (ε)** — proprietà del materiale isolante che esprime la sua capacità di aumentare la capacità del condensatore
- **Dielettrico** — materiale isolante interposto fra le armature di un condensatore
- **Farad (F)** — unità di misura della capacità; 1 F = 1 C / 1 V
- **Impedenza (Z)** — grandezza che combina resistenza e reattanze in un circuito AC; $Z = \sqrt{R^2 + (X_L - X_C)^2}$, misurata in ohm
- **Numero complesso** — forma di rappresentazione dell'impedenza: $Z = R + jX$, con parte reale (R) e immaginaria (X)
- **Picofarad (pF)** — un milionesimo di milionesimo di Farad ($10^{-12}$ F)
- **Potenza apparente (S)** — potenza totale erogata dal generatore: $S = V \times I$, misurata in VA
- **Potenza attiva (P)** — potenza che produce lavoro utile: $P = V \times I \times \cos\varphi$, misurata in W
- **Potenza reattiva (Q)** — potenza che circola nel circuito senza produrre lavoro, misurata in VAR
- **Reattanza capacitiva ($X_C$)** — opposizione del condensatore al passaggio della corrente alternata; $X_C = 1/(2\pi fC)$
- **Rifasamento** — correzione del fattore di potenza per ridurre la potenza reattiva nelle utenze industriali
- **Rigidità dielettrica** — tensione massima applicabile a un dielettrico prima che si perfori
- **Teorema di Pitagora** — relazione geometrica usata per calcolare l'impedenza dalla rappresentazione vettoriale di R e X

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Sauro (sezione ARI Prato, licenza dal 1984)
- 📋 **Coordinamento**: Fabrizio, Alessio

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione**          | 05                                                                                                                                                                                                                                    |
| **Data**             | 2 aprile 2025                                                                                                                                                                                                                         |
| **Durata**           | ~2 ore                                                                                                                                                                                                                                |
| **Numero argomenti** | 9                                                                                                                                                                                                                                     |
| **Parole chiave**    | condensatore, capacità, Farad, dielettrico, reattanza capacitiva, $X_C = 1/(2\pi fC)$, impedenza, $Z = \sqrt{R^2 + (X_L - X_C)^2}$, teorema di Pitagora, potenza apparente, potenza attiva, potenza reattiva, cos φ, serie, parallelo |
