# 📘 Lezione 19 - Sicurezza Elettrica

## 📌 Overview

- **Materia**: Linee di trasmissione radiofrequenza, onde stazionarie, adattamento di impedenza e decibel
- **Tempo di studio stimato**: 90–110 minuti
- **Prerequisiti**: Concetti di base di elettrotecnica (legge di Ohm, impedenza, reattanza), propagazione ionosferica (lezione precedente), concetto di lunghezza d'onda e frequenza
- **Obiettivi di apprendimento**:
  - Comprendere la teoria delle linee di trasmissione RF e il concetto di impedenza caratteristica
  - Distinguere tra regime di onda progressiva e regime di onde stazionarie
  - Calcolare e interpretare il ROS (Rapporto di Onde Stazionarie / SWR)
  - Conoscere le differenze tra cavo coassiale e linea bifilare
  - Comprendere il fattore di velocità e la differenza tra lunghezza fisica e lunghezza elettrica
  - Utilizzare il decibel per calcoli di guadagno e attenuazione in una catena RF
  - Comprendere il corretto posizionamento degli strumenti di misura del ROS

---

## 📖 Core Content

### 1. 🔍 Revisione del Test Precedente (⏱ 00:05–08:17)

La lezione si apre con la revisione dei risultati del test sulla propagazione. La maggior parte degli studenti ha ottenuto risultati superiori all'80%, ma due domande hanno presentato difficoltà significative.

#### 🔹 Domanda sulla MOF/MUF e Lunghezza d'Onda

La domanda chiedeva: "Se la massima frequenza utilizzabile (MOF) per un dato collegamento è 24 MHz, quale banda offre la migliore possibilità di collegamento?"

Il trabocchetto risiede nel passaggio da **frequenza** a **lunghezza d'onda**: la frequenza ottimale è circa l'80–90% della MUF, quindi circa 20 MHz. La banda corrispondente è quella dei **15 m** (21 MHz), non dei 20 m. L'errore comune è confondere il valore numerico della frequenza in MHz con la lunghezza d'onda in metri.

#### 🔹 Domanda sull'Attenuazione in Troposfera

La domanda chiedeva come varia l'attenuazione nella troposfera al variare della frequenza. La risposta corretta è che **l'attenuazione cresce sempre all'aumentare della frequenza**, indipendentemente dal tipo di propagazione (troposferica, ionosferica o in portata ottica). L'attenuazione di un campo elettromagnetico dipende sostanzialmente dalla **distanza** e dalla **frequenza**: a parità di distanza, aumenta con la frequenza.

> **Nota**: durante la revisione è emerso un problema di indicizzazione delle domande (alfabeto italiano vs. versione con J e K), che ha causato confusione tra le versioni del questionario.

---

### 2. 📡 Teoria delle Linee di Trasmissione RF (⏱ 08:44–19:35)

#### 🔹 Definizione di Linea di Trasmissione

**Linea di trasmissione** — coppia di conduttori che collegano un generatore a un carico. Quando la lunghezza della linea è **trascurabile** rispetto alla lunghezza d'onda del segnale che la percorre, tensioni e correnti lungo la linea possono essere considerate uniformi e si applicano le regole dell'elettrotecnica classica.

L'esempio della prolunga domestica è illuminante: a 50 Hz la lunghezza d'onda è circa 6.000 km, quindi qualsiasi prolunga è enormemente più corta e il comportamento è quello di un circuito a parametri concentrati.

Quando invece la dimensione della linea diventa **comparabile** con la lunghezza d'onda (tipicamente una linea a radiofrequenza che alimenta un'antenna), la distribuzione di tensioni e correnti non è più uniforme e si deve ricorrere alla **teoria delle linee di trasmissione**.

#### 🔹 Modello a Costanti Distribuite (Circuito LC)

Ogni conduttore della linea presenta un'**induttanza distribuita** (dipendente da diametro, lunghezza, presenza di dielettrico) e tra i due conduttori esiste una **capacità distribuita** (funzione delle dimensioni dei conduttori, della loro distanza e del dielettrico). Pertanto una linea può essere assimilata a un **circuito LC a costanti distribuite**: dividendo la linea in tanti segmenti, ciascuno presenta un valore costante di L e C per unità di lunghezza.

#### 🔹 Impedenza Caratteristica

La teoria delle linee dimostra che, per una linea di lunghezza infinita, il segnale si propaga in regime di **onda progressiva** e la linea presenta al generatore un'impedenza chiamata **impedenza caratteristica** ($Z_0$):

$$Z_0 = \sqrt{\frac{L}{C}}$$

dove $L$ è l'induttanza per unità di lunghezza e $C$ la capacità per unità di lunghezza.

Se una linea di lunghezza finita viene chiusa su un'impedenza pari a $Z_0$, essa si comporta come una linea di lunghezza infinita: il segnale si propaga in modo esclusivamente progressivo e **tutta l'energia** erogata dal generatore viene trasferita al carico.

L'impedenza caratteristica dipende unicamente dalle **caratteristiche fisiche** della linea: rapporto tra le dimensioni dei due conduttori, distanza tra essi e proprietà del dielettrico.

> **Valori tipici commerciali**:
>
> - **Linea bifilare** (piattina): 200–300 Ω
> - **Cavo coassiale**: 50–75 Ω

---

### 3. 📐 Cavo Coassiale vs. Linea Bifilare (⏱ 19:41–23:28)

#### 🔹 Vantaggi del Cavo Coassiale

Il campo elettromagnetico nel cavo coassiale rimane **confinato** all'interno del conduttore esterno, a differenza della linea bifilare nella quale una quota parte si propaga anche a distanza dai conduttori. Questo comporta che:

- Il cavo coassiale può essere posato **in qualsiasi ambiente** senza subire interferenze da masse metalliche circostanti
- La linea bifilare, se posata in prossimità di altri cavi o canalizzazioni metalliche, subisce interferenze e può a sua volta disturbare i conduttori vicini

Per contro, a parità di lunghezza, il cavo coassiale ha generalmente **maggiore attenuazione** rispetto alla linea bifilare.

#### 🔹 Carichi Bilanciati e Sbilanciati

**Carico sbilanciato** — un carico (o generatore) in cui uno dei due terminali è riferito a terra. Il cavo coassiale è impiegabile quasi esclusivamente per la connessione tra generatori e carichi sbilanciati.

**Carico bilanciato** — un carico i cui terminali non hanno alcun riferimento a terra (es. la maggior parte delle antenne). Per alimentare un carico bilanciato con un cavo coassiale è necessario un dispositivo di adattamento chiamato **balun** (balanced-unbalanced).

Poiché la totalità degli apparati ricetrasmittenti moderni ha un'uscita di tipo sbilanciato, l'impiego del cavo coassiale è praticamente universale. L'uso della linea bifilare è limitato a casi particolari, come l'adattamento di impedenza tramite tronchi di linea.

---

### 4. ⚡ Parametri Caratteristici di una Linea Reale (⏱ 23:53–34:07)

Una linea reale, a differenza della linea ideale teorica, presenta sempre una certa **attenuazione**. I tre parametri fondamentali che definiscono una linea sono:

#### 🔹 Impedenza Caratteristica

Valori tipici: 50–75 Ω per cavi coassiali, 200–300 Ω per linee bifilari.

#### 🔹 Attenuazione

Espressa in **dB per metro** (o dB per 100 m). L'attenuazione di una linea reale **aumenta sempre con la frequenza**. A parità di frequenza, dipende dalle caratteristiche dei conduttori e del dielettrico:

- Cavi coassiali di **maggior diametro** hanno minore attenuazione
- Cavi con dielettrico **foam** (spugnoso) hanno minore attenuazione rispetto al dielettrico compatto, perché il dielettrico spugnoso contiene aria e ha una costante dielettrica diversa
- I cavi da TV, pur avendo ottima attenuazione, non sono adatti a supportare potenze elevate in trasmissione
- Cavi professionali con dielettrico spugnoso hanno il conduttore esterno in tubo di rame rigido e corrugato per evitare schiacciamenti

#### 🔹 Fattore di Velocità

La velocità di propagazione del segnale lungo una linea è **inferiore** a quella nello spazio libero ($c$ ≈ 300.000 km/s). Il fattore di velocità ($v_f$) indica di quanto si riduce la velocità di propagazione rispetto al vuoto.

**Lunghezza fisica** — la lunghezza misurata materialmente col metro.
**Lunghezza elettrica** — la lunghezza riferita al segnale che percorre la linea.

La relazione è:

$$L_{fisica} = L_{elettrica} \times v_f = \lambda \times v_f$$

> **Esempio**: a 30 MHz ($\lambda$ = 10 m) con un cavo a $v_f$ = 0,66, uno spezzone lungo una lunghezza d'onda non misura 10 m, bensì **6,60 m** (lunghezza fisica). La lunghezza elettrica rimane 10 m.

Valori tipici del fattore di velocità:

| Tipo dielettrico            | $v_f$     |
| --------------------------- | --------- |
| Polietilene compatto        | 0,66      |
| PTFE (Teflon)               | 0,70      |
| Dielettrico spugnoso (foam) | 0,80–0,85 |

Nella tabella di cavi comuni presentata nella lezione figurano RG58, RG213, RG214 e altri, con impedenze di 50 o 75 Ω, attenuazioni dell'ordine di frazioni di dB al metro e fattori di velocità coerenti con il tipo di dielettrico.

---

### 5. 🌊 Regime di Onde Stazionarie (⏱ 34:07–52:56)

#### 🔹 Cosa Accade con Impedenza Diversa da Z₀

Quando la linea è chiusa su un'impedenza **diversa** dall'impedenza caratteristica, non tutta l'energia raggiunge il carico: una parte viene **riflessa** verso il generatore, creando un **regime di onde stazionarie**.

Il carico può essere pensato come la serie di due impedenze: una pari a $Z_0$ (che assorbe energia in regime progressivo) e una pari alla differenza (che rappresenta la potenza riflessa). I due flussi — diretto (dal generatore al carico) e riflesso (dal carico al generatore) — si compongono generando un'**onda stazionaria**: un'onda che non scorre lungo la linea ma presenta **massimi e minimi fissi** in posizioni determinate, che si ripetono con periodicità di $\lambda/2$.

#### 🔹 Definizione di ROS (SWR)

**ROS** (Rapporto di Onde Stazionarie) o **SWR** (Standing Wave Ratio) — il rapporto tra la tensione (o corrente) massima e minima lungo una linea in regime di onde stazionarie:

$$ROS = \frac{V_{max}}{V_{min}} = \frac{I_{max}}{I_{min}}$$

Il ROS è anche uguale al rapporto tra impedenza caratteristica della linea e impedenza del carico (o viceversa, prendendo sempre il rapporto maggiore):

$$ROS = \frac{Z_L}{Z_0} \quad \text{oppure} \quad ROS = \frac{Z_0}{Z_L}$$

> **Attenzione (domande d'esame)**: il ROS varia da un **minimo di 1** (perfetto adattamento, assenza di onde stazionarie) a un **massimo di infinito** (riflessione totale). Il valore minimo NON è zero.

#### 🔹 Variazione dell'Impedenza lungo la Linea

In regime di onde stazionarie, l'impedenza vista dal generatore **varia da punto a punto** lungo la linea con ciclicità $\lambda/2$. I valori estremi sono:

$$Z_{min} = \frac{Z_0}{ROS} \qquad Z_{max} = Z_0 \times ROS$$

> **Esempio numerico**: cavo da 50 Ω, ROS = 2 → l'impedenza varia da **25 Ω** (50/2) a **100 Ω** (50×2).

Nei punti intermedi (diversi da multipli di $\lambda/4$), l'impedenza presenta anche **componenti reattive** (induttive o capacitive), anche quando il carico è puramente resistivo. Solo a distanze pari a multipli interi di $\lambda/4$ si trovano valori puramente resistivi.

#### 🔹 Il ROS è Costante lungo la Linea

Concetto fondamentale: sebbene tensioni, correnti e impedenza varino da punto a punto, il **valore del ROS è costante in ogni punto della linea**. È un errore credere che allungando o accorciando il cavo si possa "aggiustare" il valore del ROS. Questa credenza errata è alimentata dal fatto che alcuni strumenti di misura, in determinate condizioni, forniscono letture diverse a seconda della posizione lungo la linea (per limiti dello strumento, non per variazione reale del ROS).

---

### 6. 🔧 Applicazioni delle Onde Stazionarie: Trasformatore λ/4 (⏱ 61:26–67:23)

#### 🔹 Trasformatore di Impedenza a Quarto d'Onda

Una linea lunga esattamente $\lambda/4$, chiusa su un'impedenza diversa dalla propria, presenta dall'altro capo un'impedenza puramente resistiva (se il carico è resistivo). Questo comportamento viene sfruttato come **trasformatore di impedenza**.

Per adattare due impedenze $Z_1$ e $Z_2$, si interpone un tronco di linea lungo $\lambda/4$ con impedenza caratteristica:

$$Z_{linea} = \sqrt{Z_1 \times Z_2}$$

> **Esempio**: per adattare un carico da 100 Ω a un generatore da 50 Ω → $Z_{linea} = \sqrt{50 \times 100} = \sqrt{5000} \approx 70{,}7 \approx 75 \; \Omega$. Un tronco di cavo da 75 Ω lungo $\lambda/4$ realizza l'adattamento.

Questa tecnica è molto utilizzata in **VHF** e per accoppiare più antenne.

#### 🔹 Linee λ/4 Aperte e in Cortocircuito

- **Linea λ/4 in cortocircuito**: presenta impedenza **infinita** dall'altro lato. Per lunghezze < λ/4 si comporta come **induttanza pura**, per lunghezze tra λ/4 e λ/2 come **capacità pura** → equivalente a un **circuito risonante parallelo**
- **Linea λ/4 aperta**: comportamento opposto → equivalente a un **circuito risonante serie**

Questo principio è utilizzato in alta frequenza per realizzare **risonatori coassiali** e filtri ad elevato fattore di merito Q.

---

### 7. ⚠️ Conseguenze del Disadattamento (⏱ 67:31–76:18)

#### 🔹 Potenza Riflessa in Funzione del ROS

| ROS | Potenza riflessa (%) | Perdita (dB) |
| --- | -------------------- | ------------ |
| 1,0 | 0%                   | 0 dB         |
| 1,5 | ~4%                  | ~0,2 dB      |
| 2,0 | ~11%                 | ~0,5 dB      |
| 3,0 | 25%                  | ~1,25 dB     |
| ∞   | 100%                 | totale       |

Fino a ROS = 2, la percentuale di potenza riflessa è inferiore al 10–11%. Sale al 25% con ROS = 3, poi cresce drasticamente.

#### 🔹 Effetti Dannosi del Disadattamento

1. **Aumento dell'attenuazione del cavo**: l'attenuazione nominale è relativa al perfetto adattamento; in regime di onde stazionarie il cavo è sottoposto a tensioni e correnti più elevate e l'attenuazione aumenta
2. **Danneggiamento di cavo e trasmettitore** con potenze elevate
3. **Riduzione della potenza erogata dal trasmettitore**: per il **teorema del massimo trasferimento di potenza**, la massima potenza si ottiene quando l'impedenza del carico è pari al complesso coniugato dell'impedenza interna del generatore. In pratica, il trasmettitore eroga la potenza nominale solo se vede un carico di **50 Ω puramente resistivi**

> Con ROS = 2, la potenza riflessa è solo ~10%, ma l'impedenza vista dal trasmettitore può variare da 25 a 100 Ω: il trasmettitore non riesce a lavorare in condizioni ottimali, e le due condizioni (perdita riflessa + mancato adattamento al TX) si sommano.

#### 🔹 Uso dell'Accordatore (Tuner)

**Accordatore** — dispositivo in grado di adattare due valori di impedenza differenti.

- **Posizione ottimale**: in prossimità dell'antenna, in modo che sia la linea sia il trasmettitore lavorino in perfetto adattamento
- **Posizione comune**: all'uscita del trasmettitore. Questo protegge i finali e permette l'erogazione della massima potenza, ma **non elimina il disadattamento lungo la linea**: il ROS in linea rimane elevato, causando un'attenuazione superiore a quella nominale e quindi poca potenza effettiva all'antenna

---

### 8. 📏 Misura del ROS (⏱ 76:18–83:39)

#### 🔹 Strumenti di Misura

Il ROS si misura tramite un **wattmetro direzionale** (o accoppiatore direzionale) in grado di rilevare separatamente la potenza diretta ($P_d$) e la potenza riflessa ($P_r$). Il ROS si calcola come:

$$ROS = \frac{1 + \sqrt{P_r / P_d}}{1 - \sqrt{P_r / P_d}}$$

#### 🔹 Tipologie di Sensori

- **Accoppiatore direzionale**: il più affidabile
- **Ponti di misura** (Wheatstone Bridge, Tandem Bridge): utilizzati negli strumenti di basso costo, possono dare letture non attendibili in funzione della posizione lungo la linea

#### 🔹 Effetto dell'Attenuazione del Cavo sulla Misura

La misura andrebbe fatta idealmente **al punto di connessione con l'antenna**. Misurando lato trasmettitore, l'attenuazione del cavo "maschera" il vero valore di ROS.

> **Esempio numerico dettagliato**:
>
> - Trasmettitore: 100 W, cavo con attenuazione totale di 2 dB, antenna con ROS = 3 (25% di riflessione)
> - **Misura lato antenna**: $P_d$ = 63 W (100 W − 2 dB), $P_r$ = 16 W (25% di 63) → **ROS letto = 3** ✓
> - **Misura lato trasmettitore**: $P_d$ = 100 W, $P_r$ = 10 W (i 16 W riflessi subiscono 2 dB di attenuazione percorrendo il cavo a ritroso) → **ROS letto = 1,9** ✗
>
> In regime di onde stazionarie, l'attenuazione reale del cavo è addirittura superiore a quella nominale, peggiorando ulteriormente la discrepanza.

---

### 9. 📊 Il Decibel (dB) (⏱ 83:39–95:30)

#### 🔹 Definizione

Il **decibel** (dB) è un'unità di misura **logaritmica** che esprime il rapporto tra due potenze:

$$G_{dB} = 10 \cdot \log_{10}\left(\frac{P_{out}}{P_{in}}\right)$$

#### 🔹 Valori Notevoli

| Rapporto lineare | Valore in dB |
| ---------------- | ------------ |
| 2 (doppio)       | +3 dB        |
| 4 (quadruplo)    | +6 dB        |
| 10               | +10 dB       |
| 100              | +20 dB       |
| 1.000            | +30 dB       |
| 1/2 (metà)       | −3 dB        |
| 1/4              | −6 dB        |
| 1/10             | −10 dB       |
| 1/100            | −20 dB       |
| 1/1.000          | −30 dB       |

- **Guadagno**: valori positivi
- **Attenuazione**: valori negativi

> Per le domande d'esame è sufficiente ricordare: **3 dB = doppio/metà**, **6 dB = quadruplo/quarto**, **10 dB = 10 volte/un decimo**.

#### 🔹 Vantaggio dell'Uso dei Decibel

In una catena con più elementi (cavo + antenna, amplificatore + cavo + filtro, ecc.), guadagni e attenuazioni espressi in dB possono essere **semplicemente sommati algebricamente** per ottenere il risultato complessivo.

> **Esempio pratico**:
>
> - Trasmettitore: 100 W
> - Cavo: −3 dB di attenuazione
> - Antenna: +6 dB di guadagno
> - Guadagno totale = +6 − 3 = **+3 dB** → potenza irradiata = 100 × 2 = **200 W**

#### 🔹 Calcolo dell'Attenuazione di un Cavo

L'attenuazione complessiva di una linea si ottiene **moltiplicando** il valore di attenuazione per metro (fornito dal costruttore alla frequenza di utilizzo) per la lunghezza del cavo.

> **Esempio**: cavo con 0,2 dB/m, lungo 15 m → attenuazione totale = 0,2 × 15 = **3 dB**.

Attenzione: l'attenuazione dipende dalla frequenza, quindi per antenne multibanda lo stesso cavo avrà attenuazioni diverse su bande diverse.

---

### 10. 🛠️ Aspetti Pratici e Discussione (⏱ 95:36–125:44)

#### 🔹 Posizionamento del Rosmetro

In risposta alla domanda di Marco sul posizionamento del rosmetro rispetto a un commutatore d'antenna: se il commutatore è di buona qualità e adeguato alla frequenza di utilizzo, la posizione (prima o dopo il commutatore) è praticamente **indifferente**, purché il ROS sia basso. Con ROS elevati e strumenti di basso costo, si possono avere letture diverse a seconda della posizione — problema dello strumento, non del ROS reale.

#### 🔹 Cavi con Dielettrico Spugnoso — RG8 Mini

Claudio chiede informazioni sull'RG8 Mini (fattore di velocità 0,82, attenuazione 2,5 dB per 30 m a 50 MHz). Il fattore di velocità elevato (0,82 anziché 0,66) tradisce il dielettrico **spugnoso** (foam). Questi cavi offrono ottima attenuazione per le dimensioni, ma sono **delicati**: occorre evitare pieghe marcate, schiacciamenti e torsioni che possono alterare il dielettrico e le caratteristiche del cavo.

#### 🔹 Misure con VNA e Impedenza dell'Antenna

La misura di impedenza dell'antenna andrebbe fatta il più vicino possibile all'antenna stessa. Misurando alla base del cavo si rischia di leggere valori falsati dalla trasformazione di impedenza della linea. In particolare, se il cavo non ha lunghezza elettrica pari a un multiplo intero di $\lambda/2$, un'antenna risonante (impedenza puramente resistiva) può apparire con componenti reattive dall'altro capo del cavo, inducendo a modifiche errate dell'antenna.

> **Errore comune**: cercare il punto di impedenza puramente resistiva alla base del cavo e pensare di non essere in risonanza a causa di componenti reattive, quando in realtà è il cavo a introdurle per effetto della trasformazione di impedenza.

Soluzioni pratiche: utilizzare uno **spezzone di cavo calibrato** di lunghezza nota, oppure accoppiatori direzionali con **interfaccia wireless** da posizionare direttamente all'antenna.

#### 🔹 Consigli sui Cavi

Segnalazione del marchio **Messi & Paoloni** come produttore di cavi professionali di alta qualità (serie Ultraflex da 7, 10, 13 mm) con specifiche dettagliate di attenuazione per frequenza.

#### 🔹 Ripasso di Propagazione Ionosferica

In risposta alla domanda corretta del quiz: lo strato **F** è l'unico che rimane presente anche di notte. Durante la notte, il livello di ionizzazione dello strato F diminuisce progressivamente e raggiunge il **minimo poco prima dell'alba**, per poi risalire con la nuova radiazione solare. Subito dopo il tramonto, lo strato F mantiene ancora per un po' i livelli diurni.

#### 🔹 Cenni sulla Rete Troposcatter NATO/USAF

Breve digressione storica sulla rete troposcatter che passava per Coltano (Pisa): sistemi USAF a **400 MHz** (tratte su mare) e **800 MHz** (tratte su terra), potenze da **1 a 10 kW**, sistemi multicanale da 100 canali. Impianto attivato nel 1963 e smantellato alla fine degli anni '80.

---

## 🔗 Concept Map (testuale)

- **Linea di trasmissione** → è caratterizzata da → **impedenza caratteristica** $Z_0$
- **Impedenza caratteristica** → dipende da → **rapporto dimensioni conduttori** e **dielettrico**
- **Linea chiusa su $Z_0$** → determina → **regime di onda progressiva** (trasferimento totale di energia)
- **Linea chiusa su impedenza ≠ $Z_0$** → genera → **regime di onde stazionarie**
- **Regime di onde stazionarie** → è quantificato dal → **ROS (SWR)**
- **ROS** → è costante lungo la linea → ma **impedenza** varia ciclicamente ogni λ/2
- **Disadattamento** → causa → **potenza riflessa**, **aumento attenuazione cavo**, **riduzione potenza erogata dal TX**
- **Accordatore** → compensa il disadattamento → ma idealmente va posto **all'antenna**
- **Tronco λ/4** → può funzionare come → **trasformatore di impedenza**
- **Fattore di velocità** → determina la differenza tra → **lunghezza fisica** e **lunghezza elettrica**
- **Cavo coassiale** → ha campo confinato → preferito rispetto a **linea bifilare**
- **Linea bifilare** → necessaria per → **carichi bilanciati** (con balun nel caso di coassiale)
- **Decibel** → esprime rapporti di potenza in scala logaritmica → permette di **sommare** guadagni e attenuazioni
- **Attenuazione del cavo** → dipende da → **frequenza**, **lunghezza**, **tipo di dielettrico**
- **Misura del ROS** → influenzata da → **attenuazione del cavo** e **tipo di strumento**

---

## 📝 Key Takeaways

1. L'**impedenza caratteristica** $Z_0$ di una linea dipende dalle sue caratteristiche fisiche ($Z_0 = \sqrt{L/C}$) e non dalla lunghezza; valori tipici sono 50–75 Ω per cavi coassiali, 200–300 Ω per linee bifilari.

2. Una linea chiusa su un'impedenza pari alla propria impedenza caratteristica è in **regime di onda progressiva**: tutta l'energia viene trasferita al carico. Ogni disadattamento genera un regime di **onde stazionarie** con energia riflessa.

3. Il **ROS** (SWR) varia da **1** (perfetto adattamento) a **infinito** (riflessione totale). Il valore minimo NON è zero — un errore frequente nelle domande d'esame.

4. Il valore del ROS è **costante in ogni punto della linea**: cambiare la lunghezza del cavo NON modifica il ROS. L'**impedenza** vista lungo la linea, invece, varia ciclicamente ogni λ/2.

5. Il **fattore di velocità** determina la differenza tra lunghezza fisica e lunghezza elettrica di un cavo: $L_{fisica} = \lambda \times v_f$. Non tenerne conto porta a errori grossolani nelle misure e nel dimensionamento.

6. Il cavo coassiale è preferito alla linea bifilare perché il campo elettromagnetico rimane **confinato** all'interno, rendendo il cavo immune da interferenze ambientali.

7. Un tronco di linea lungo **λ/4** può funzionare come trasformatore di impedenza: l'impedenza della linea deve essere $Z = \sqrt{Z_1 \times Z_2}$.

8. L'**accordatore** posizionato al trasmettitore protegge i finali e permette l'erogazione della massima potenza, ma NON elimina le onde stazionarie lungo il cavo: la posizione ideale è all'antenna.

9. Il **decibel** è una scala logaritmica: +3 dB = doppio, +6 dB = quadruplo, +10 dB = 10 volte. In una catena RF, guadagni e attenuazioni in dB si sommano algebricamente.

10. La misura del ROS effettuata alla base del cavo (lato TX) anziché all'antenna può fornire valori **significativamente inferiori** a quelli reali a causa dell'attenuazione del cavo che maschera la potenza riflessa.

---

## ❓ Comprehension Questions

1. Perché una prolunga elettrica domestica a 220 V/50 Hz può essere studiata con le regole dell'elettrotecnica classica, mentre una linea a radiofrequenza che alimenta un'antenna no?

2. Un cavo coassiale da 50 Ω è chiuso su un'antenna con impedenza di 150 Ω. Qual è il valore del ROS? Quali sono i valori minimo e massimo di impedenza che si possono trovare lungo la linea?

3. Spiega perché il ROS rimane costante in ogni punto della linea, mentre l'impedenza vista varia ciclicamente. Come si conciliano queste due affermazioni?

4. Un radioamatore misura un ROS di 1,8 alla base del cavo e conclude che l'antenna è ragionevolmente adattata. Quali fattori potrebbero rendere questa conclusione errata?

5. Perché l'accordatore posizionato all'uscita del trasmettitore risolve solo parzialmente il problema del disadattamento? Qual è la posizione ottimale?

6. Descrivi come un tronco di linea lungo λ/4 può essere utilizzato per adattare un'impedenza di 200 Ω a un sistema a 50 Ω. Quale impedenza caratteristica deve avere il tronco?

7. Un cavo con fattore di velocità 0,66 deve essere tagliato a una lunghezza elettrica di mezza lunghezza d'onda per la frequenza di 14 MHz. Quale sarà la lunghezza fisica del cavo?

8. Perché il valore minimo del ROS è 1 e non 0? Cosa significherebbe fisicamente un ROS pari a 0?

9. Trasmettitore da 50 W, cavo con perdita di 6 dB, antenna con guadagno di 9 dB. Quanta potenza viene effettivamente irradiata? Mostra il calcolo in dB.

10. In una misura di impedenza alla base del cavo, un'antenna in risonanza appare con componenti reattive. Spiega il meccanismo fisico alla base di questa apparente anomalia.

---

## 📚 Glossary

- **Accordatore (Tuner)** — dispositivo che adatta impedenze diverse tra loro, compensando il disadattamento tra trasmettitore, linea e antenna
- **Accoppiatore direzionale** — dispositivo che separa i flussi di potenza diretta e riflessa in una linea, utilizzato per la misura del ROS
- **Attenuazione** — perdita di potenza del segnale lungo la linea, espressa in dB per metro o dB per 100 m; cresce con la frequenza
- **Balun** — dispositivo di adattamento tra un circuito bilanciato e uno sbilanciato (balanced-unbalanced)
- **Carico bilanciato** — carico i cui terminali non hanno riferimento a terra (es. dipolo)
- **Carico sbilanciato** — carico in cui uno dei terminali è riferito a terra
- **Carta di Smith** — diagramma polare che permette di calcolare graficamente i valori di impedenza lungo una linea in regime di onde stazionarie
- **Costanti distribuite** — modello circuitale in cui induttanza e capacità sono distribuite uniformemente lungo la linea
- **Decibel (dB)** — unità di misura logaritmica per rapporti di potenza: $dB = 10 \cdot \log_{10}(P_2/P_1)$
- **Dielettrico foam (spugnoso)** — isolante contenente aria che riduce l'attenuazione del cavo ma ne aumenta la fragilità meccanica
- **Fattore di velocità ($v_f$)** — rapporto tra la velocità di propagazione nel cavo e quella nello spazio libero; valori tipici 0,66–0,85
- **Impedenza caratteristica ($Z_0$)** — impedenza propria della linea, dipendente dalle sue caratteristiche fisiche; $Z_0 = \sqrt{L/C}$
- **Linea bifilare (piattina)** — linea di trasmissione formata da due conduttori paralleli; impedenza tipica 200–300 Ω
- **Lunghezza elettrica** — lunghezza della linea espressa in funzione della lunghezza d'onda del segnale che la percorre
- **Lunghezza fisica** — lunghezza materiale della linea, misurata col metro
- **MOF / MUF** — Maximum Observable / Usable Frequency: massima frequenza utilizzabile per un collegamento ionosferico
- **Onda progressiva** — regime in cui il segnale si propaga in un'unica direzione lungo la linea, con trasferimento completo di energia
- **Onde stazionarie** — regime in cui l'interferenza tra onda diretta e riflessa genera massimi e minimi fissi lungo la linea
- **ROS (SWR)** — Rapporto di Onde Stazionarie (Standing Wave Ratio): rapporto tra tensione massima e minima lungo la linea; valori da 1 (adattamento perfetto) a ∞ (riflessione totale)
- **Teorema del massimo trasferimento di potenza** — la potenza massima si trasferisce quando l'impedenza del carico è pari al complesso coniugato dell'impedenza interna del generatore
- **Trasformatore λ/4** — tronco di linea lungo un quarto d'onda utilizzato per adattare impedenze; $Z_{linea} = \sqrt{Z_1 \times Z_2}$
- **Wattmetro direzionale** — strumento che misura separatamente potenza diretta e riflessa in una linea

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo (docente principale della serata, esperto di linee di trasmissione e RF)
- 👨‍💼 **Moderatore/Organizzatore**: Fabrizio
- 👨‍💻 **Gestione quiz**: Alessio

---

## 📅 Informazioni Lezione

| Campo                    | Valore                                                                                                                                                                                                                  |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Numero lezione**       | 19                                                                                                                                                                                                                      |
| **Data**                 | 10 settembre 2025                                                                                                                                                                                                       |
| **Durata**               | ~2 ore e 5 minuti                                                                                                                                                                                                       |
| **Argomenti principali** | 6 (revisione test, teoria linee RF, onde stazionarie, adattamento impedenza, decibel, aspetti pratici)                                                                                                                  |
| **Parole chiave**        | Linea di trasmissione, impedenza caratteristica, onde stazionarie, ROS, SWR, cavo coassiale, linea bifilare, fattore di velocità, trasformatore λ/4, decibel, accordatore, wattmetro direzionale, balun, carta di Smith |
