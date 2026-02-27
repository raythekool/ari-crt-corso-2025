# 📘 Lezione 16 - Misure e Strumenti

## 📌 Overview

- **Materia**: Strumenti di misura per elettronica e radioamatori
- **Argomento principale**: Strumenti analogici a bobina mobile (amperometro, voltmetro, ohmetro), multimetro, carico fittizio, wattmetri, frequenzimetro, grid-dip meter, oscilloscopio e analizzatore di spettro
- **Tempo di studio stimato**: 2 ore
- **Prerequisiti**: Legge di Ohm e grandezze elettriche fondamentali (Lezioni 01-03), decibel e dBm (Lezione 13), trasmettitori (Lezione 14), ricevitori (Lezione 15)
- **Obiettivi di apprendimento**:
  - Comprendere il funzionamento dello strumento a bobina mobile
  - Sapere come estendere la portata di amperometri e voltmetri
  - Conoscere il collegamento corretto degli strumenti (serie/parallelo)
  - Distinguere strumenti ideali e reali, voltmetri elettronici
  - Conoscere gli strumenti specifici per radioamatori: carico fittizio, wattmetro, ROSmetro, frequenzimetro, grid-dip meter
  - Comprendere la differenza tra oscilloscopio (dominio del tempo) e analizzatore di spettro (dominio della frequenza)

---

## 📖 Core Content

### 1. 📝 Correzione quiz Lezione 15 (⏱ 00:03)

La lezione si apre con la correzione dei quiz sui ricevitori. Punti chiave rivisti:

- Il **BFO** (oscillatore della frequenza di battimento) serve nei ricevitori **SSB** (e CW): è l'oscillatore che rigenera l'audio nel demodulatore. Non serve per l'AM, che usa un rivelatore a diodo + condensatore (rivelatore a inviluppo).
- Nella **supereterodina**, il segnale ricevuto viene **convertito di frequenza** una o più volte prima di essere demodulato.
- **Frequenza immagine**: con IF = 9 MHz e segnale a 51 MHz → 2 × 9 = 18 MHz di distanza → 51 − 18 = **33 MHz** (la frequenza immagine). Il metodo: calcolare 2 × IF, poi provare somma e sottrazione dal segnale ricevuto; una delle due è la risposta.
- Il **discriminatore** demodula l'FM; il **rivelatore a prodotto** demodula SSB.
- La **sensibilità** è la minima tensione in ingresso distinguibile dal rumore. Dipende da due fattori: **larghezza di banda** e **cifra di rumore** (noise figure, traduzione corretta dall'inglese, non "figura di rumore"). La cifra di rumore dipende dalla rumorosità dei primi stadi del ricevitore (transistor, FET, MOSFET).
- Il **miscelatore/mixer** riceve i segnali dall'amplificatore RF e dall'oscillatore locale, inviandoli al filtro IF.
- La banda passante degli stadi IF deve essere **appena più larga** della larghezza di banda del segnale ricevuto.
- La sensibilità si misura in **microvolts**.

---

### 2. 🔧 Lo strumento a bobina mobile (⏱ 15:34)

Tutti gli strumenti analogici di base funzionano con il meccanismo della **bobina mobile**, lo stesso principio dell'altoparlante (interazione tra campi magnetici).

#### 🔹 Principio di funzionamento

Lo strumento contiene:

- Un **magnete permanente** (calamita) che genera un campo magnetico fisso
- Una **bobina** avvolta su un telaietto circolare, libera di ruotare su due perni
- Una **molla a spirale** che tiene lo strumento in posizione zero
- Un **indice** (ago) collegato meccanicamente alla bobina

Quando una corrente scorre nella bobina, essa genera un proprio campo magnetico. L'interazione tra il campo fisso del magnete e quello variabile della bobina produce una **forza** che fa ruotare la bobina. La molla antagonista produce un equilibrio: l'ago si ferma in un punto proporzionale alla corrente che scorre.

> Tutti gli strumenti a bobina mobile sono fondamentalmente **amperometri** (o microamperometri), perché misurano la corrente. È la corrente nella bobina che genera il campo magnetico, non la tensione.

---

### 3. ⚡ L'amperometro e la resistenza di shunt (⏱ 20:27)

#### 🔹 Tre valori caratteristici di uno strumento

Ogni strumento a bobina mobile è definito da tre valori legati dalla legge di Ohm ($V = R \times I$):

| Parametro               | Simbolo  | Esempio |
| ----------------------- | -------- | ------- |
| Corrente di fondo scala | $I_{FS}$ | 50 µA   |
| Resistenza interna      | $R_i$    | 100 Ω   |
| Tensione di fondo scala | $V_{FS}$ | 5 mV    |

Verifica: $50 \times 10^{-6} \times 100 = 5 \times 10^{-3}$ V = 5 mV ✓

#### 🔹 Estensione della portata — resistenza di shunt

Per misurare correnti più alte del fondo scala nativo, si aggiunge una **resistenza in parallelo** (detta **resistenza di shunt**). Questa resistenza devia la corrente in eccesso, lasciando passare nello strumento solo la sua corrente di fondo scala.

**Formula della resistenza di shunt**:

$$R_S = \frac{R_i \times I_{FS}}{I_{desiderata} - I_{FS}} = \frac{V_{FS}}{I_{desiderata} - I_{FS}}$$

**Principio**: la resistenza di shunt è in parallelo allo strumento, quindi ha ai suoi capi la stessa tensione (5 mV nell'esempio). La corrente che la attraversa è la differenza tra la corrente totale e quella dello strumento.

| Fondo scala desiderato | Resistenza di shunt | Nota                              |
| ---------------------- | ------------------- | --------------------------------- |
| 0,3 mA                 | 20 Ω                | Corrente bassa → shunt alto       |
| 3 mA                   | 1,6 Ω               |                                   |
| 30 mA                  | 0,16 Ω              |                                   |
| 300 mA                 | 0,016 Ω             | Corrente alta → shunt molto basso |

> **Regola**: più è elevata la corrente da misurare, più **bassa** deve essere la resistenza di shunt.

---

### 4. 🔌 Il voltmetro (⏱ 29:48)

Per misurare tensioni si usa lo stesso microamperometro con una **resistenza in serie** (detta resistenza moltiplicatrice).

#### 🔹 Principio

Si calcola quale resistenza serve affinché, con la tensione di fondo scala desiderata ai capi dell'insieme strumento + resistenza, scorra esattamente la corrente di fondo scala dello strumento.

**Formula della resistenza serie**:

$$R_S = \frac{V_{desiderata}}{I_{FS}} - R_i$$

| Fondo scala desiderato | Resistenza serie    | Nota                |
| ---------------------- | ------------------- | ------------------- |
| 1 V                    | 19.900 Ω            |                     |
| 10 V                   | 199.000 Ω           | ×10 rispetto a 1 V  |
| 100 V                  | 1.999.900 Ω (~2 MΩ) | ×10 rispetto a 10 V |

> **Regola**: più è alta la tensione da misurare, più **grande** deve essere la resistenza in serie.

⚠️ _I valori non sono "tondi" (es. 19.900 anziché 20.000) perché bisogna sottrarre la resistenza interna dello strumento, già presente._

---

### 5. 🔗 Collegamento degli strumenti nel circuito (⏱ 36:02)

| Strumento       | Collegamento     | Motivo                                                                            |
| --------------- | ---------------- | --------------------------------------------------------------------------------- |
| **Amperometro** | In **serie**     | Si interrompe il circuito e si inserisce lo strumento nel percorso della corrente |
| **Voltmetro**   | In **parallelo** | Si collega ai due punti tra cui si vuole misurare la differenza di potenziale     |

---

### 6. ⚖️ Strumenti ideali e reali (⏱ 37:46)

L'inserimento di uno strumento nel circuito può **perturbare** la misura:

- L'**amperometro** ha una resistenza interna che, essendo in serie, fa diminuire leggermente la corrente misurata
- Il **voltmetro** assorbe una piccola corrente che può far calare la tensione del generatore, specie se il generatore ha resistenza interna alta

**Strumenti ideali**:

- **Amperometro ideale**: resistenza interna **nulla** (R = 0)
- **Voltmetro ideale**: resistenza interna **infinita** (R → ∞)

#### 🔹 Voltmetri elettronici

Per avvicinarsi al voltmetro ideale esistono i **voltmetri elettronici**, caratterizzati da un'impedenza di ingresso molto alta, tipicamente **superiore a 10 MΩ**.

Sono realizzati con circuiti a **FET** (Field Effect Transistor) in configurazione a ponte: due FET identici, polarizzati per avere stesse correnti a riposo; la tensione da misurare, applicata al gate di un FET, squilibra il ponte e fa deviare lo strumento.

Il vantaggio del FET: il terminale di gate è una giunzione polarizzata inversamente, quindi **non assorbe corrente**.

| Tipo di strumento                | Impedenza tipica                |
| -------------------------------- | ------------------------------- |
| Voltmetro analogico tradizionale | ~20.000 Ω/V (es. 200 kΩ a 10 V) |
| Voltmetro elettronico            | >10 MΩ                          |

⚠️ _I multimetri digitali, pur avendo elettronica sofisticata, NON sono voltmetri elettronici: hanno un'impedenza di ingresso simile a quella degli strumenti tradizionali._

---

### 7. Ω L'ohmetro (⏱ 44:20)

L'**ohmetro** misura la resistenza sfruttando la legge di Ohm. Contiene:

- Una **batteria interna** di tensione nota (es. 1,5 V)
- Il solito strumento a bobina mobile
- Morsetti per collegare la resistenza incognita ($R_X$)

Chiudendo il circuito batteria-strumento-resistenza incognita, scorre una corrente inversamente proporzionale a $R_X$. La scala è graduata direttamente in ohm. Il fondo scala è modificabile tramite un commutatore.

---

### 8. 🛠️ Il multimetro (⏱ 46:08)

Il **multimetro** — è lo strumento che riunisce in un unico scatolotto voltmetro, amperometro e ohmetro. Tramite un selettore rotativo si sceglie la grandezza da misurare e il fondo scala.

I multimetri moderni sono di tipo **digitale** con display numerico. Possono misurare anche tensioni alternate (AC), frequenza, e testare componenti (transistor, diodi). Tuttavia, i multimetri digitali economici **non** sono voltmetri elettronici e hanno impedenze di ingresso paragonabili agli strumenti tradizionali.

---

### 9. 🔴 Carico fittizio (Dummy Load) (⏱ 58:03)

Il **carico fittizio** — è una terminazione resistiva che fa le veci dell'antenna, usata per prove e tarature del trasmettitore senza irradiare segnali nell'etere.

Costruttivamente è una **resistenza ad alta potenza** immersa in olio per trasformatori (per dissipare il calore). Un tipico carico fittizio in un bidoncino da ~15 cm può gestire fino a ~1000 W.

**Misura della potenza**: sul carico è montato un rivelatore che fornisce una tensione continua proporzionale alla tensione RF. Collegando un voltmetro, si calcola:

$$P = \frac{V^2}{R}$$

> Il carico fittizio va usato **sempre** per prove, tarature e collaudi, per non inquinare l'etere con trasmissioni spurie.

---

### 10. 📊 Wattmetri passanti (⏱ 60:22)

I **wattmetri passanti** — hanno due connettori (ingresso dal trasmettitore, uscita verso l'antenna) e misurano la **potenza in transito**.

I wattmetri professionali (es. Bird) hanno **elementi intercambiabili** che si inseriscono per selezionare la banda di frequenza e il fondo scala di potenza (es. "25 W, 100-250 MHz").

Oltre alla potenza diretta (dal trasmettitore all'antenna), possono misurare anche la **potenza riflessa** (dall'antenna indietro), nel caso l'antenna non sia perfettamente adattata.

---

### 11. 📐 ROSmetro (⏱ 62:12)

Il **ROSmetro** — misura il **ROS** (Rapporto Onde Stazionarie), che indica quanto l'antenna è in grado di assorbire la potenza inviata dal trasmettitore. È uno strumento molto comune nelle stazioni radioamatoriali e nella banda cittadina. L'argomento sarà approfondito nelle lezioni sulle antenne.

---

### 12. 🔢 Frequenzimetro (⏱ 64:28)

Il **frequenzimetro** — è uno strumento molto semplice. Funziona così:

1. Una **porta** si apre per esattamente **1 secondo**
2. Un **contatore** conta il numero di cicli completi della sinusoide durante quel secondo
3. A porta chiusa, il contatore mostra il risultato = frequenza in Hz

Per questo motivo il frequenzimetro viene spesso chiamato anche **contatore**.

Per misurare trasmettitori potenti basta un'antennina vicina; per segnali deboli serve un collegamento diretto con sonda.

---

### 13. 🔍 Grid-dip meter (⏱ 65:26)

Il **grid-dip meter** — è uno strumento che misura la **frequenza di risonanza** di circuiti LC. Contiene un oscillatore sintonizzabile con una **bobina esterna** visibile.

#### 🔹 Modalità DIP (misura di risonanza)

1. Si avvicina la bobina del grid-dip al circuito LC da misurare
2. Si sintonizza l'oscillatore interno ruotando la manopola
3. Quando la frequenza dell'oscillatore coincide con quella del circuito → **assorbimento di potenza** → l'indicatore mostra un **dip** (calo, picco negativo)
4. Si legge la frequenza sulla scala di sintonia

**Dip** — dall'inglese, significa picco negativo, calo. **Grid** — griglia, perché originariamente costruito con valvole termoioniche (misurava il dip della corrente di griglia).

#### 🔹 Modalità ondametro

Spegnendo l'oscillatore e usando il transistor come amplificatore, la bobina funziona da **antenna**. Lo strumento diventa un **misuratore selettivo** (ondametro): sintonizzandolo si cerca il **massimo** dell'indicatore per determinare la frequenza di un segnale esterno. Misura più grossolana del frequenzimetro, ma utile sul campo.

---

### 14. 📺 Oscilloscopio (⏱ 72:24)

L'**oscilloscopio** — è lo strumento che mostra le **forme d'onda** dei segnali. Lavora nel **dominio del tempo**.

- **Asse X** (orizzontale): **tempo** (secondi, millisecondi, microsecondi per divisione)
- **Asse Y** (verticale): **ampiezza** (volt per divisione)

Lo schermo è diviso da un reticolo in "divisioni" (quadratini).

#### 🔹 Misura di ampiezza

Si contano le divisioni verticali occupate dal segnale e si moltiplica per il valore della manopola "Volt/div":

$$V_{pp} = \text{divisioni verticali} \times \text{volt/divisione}$$

**Esempio**: sinusoide alta 4 divisioni × 2 V/div = **8 V picco-picco**

#### 🔹 Misura del periodo e della frequenza

Si contano le divisioni orizzontali di un ciclo completo e si moltiplica per il valore della manopola "Tempo/div" (base dei tempi):

$$T = \text{divisioni orizzontali} \times \text{tempo/divisione}$$
$$f = \frac{1}{T}$$

**Esempio**: sinusoide larga 4 divisioni × 0,1 ms/div = 0,4 ms → $f = 1/0{,}0004 = 2500$ Hz

Tipicamente un oscilloscopio ha **due canali** per confrontare due segnali (es. ingresso e uscita di un amplificatore).

⚠️ _L'oscilloscopio non nasce come strumento di precisione per misure di tensione o frequenza; serve principalmente per **visualizzare** le forme d'onda._

---

### 15. 📈 Analizzatore di spettro (⏱ 80:06)

L'**analizzatore di spettro** — è lo strumento che mostra la composizione in frequenza di un segnale. Lavora nel **dominio della frequenza**.

- **Asse X** (orizzontale): **frequenza**
- **Asse Y** (verticale): **potenza**, espressa in **dBm** (decibel rispetto a 1 mW)

| Confronto | Oscilloscopio          | Analizzatore di spettro  |
| --------- | ---------------------- | ------------------------ |
| Dominio   | Tempo                  | Frequenza                |
| Asse X    | Tempo (s, ms, µs)      | Frequenza (Hz, kHz, MHz) |
| Asse Y    | Ampiezza (V)           | Potenza (dBm)            |
| Mostra    | Forma d'onda nel tempo | Composizione spettrale   |

#### 🔹 Funzionamento interno

Internamente è come un **ricevitore** seguito da un display tipo oscilloscopio. L'operatore imposta la **frequenza centrale** e lo **span** (apertura della finestra di osservazione). Lo strumento "scansiona" lo span mostrando l'ampiezza di ogni componente di frequenza.

#### 🔹 Applicazioni pratiche

- Visualizzare la **portante** e le **bande laterali** di un segnale AM
- Verificare la **pulizia spettrale** di un trasmettitore: si vedono le armoniche (2ª, 3ª, ecc.) e il loro livello rispetto alla fondamentale
- Determinare il livello di **armoniche** e **segnali spuri**

#### 🔹 Scala logaritmica (dBm)

La scala in dBm è essenziale perché consente di visualizzare segnali con dinamica enorme. Su una scala lineare, un segnale 1000 volte più debole scompare; su scala logaritmica è visibile e misurabile.

| dBm     | Potenza   |
| ------- | --------- |
| 0 dBm   | 1 mW      |
| −10 dBm | 0,1 mW    |
| −20 dBm | 0,01 mW   |
| −30 dBm | 0,001 mW  |
| −40 dBm | 0,0001 mW |

Il **waterfall** (cascata) dei ricevitori digitali moderni è una forma di analizzatore di spettro, anche se fornisce indicazioni solo indicative (non calibrate).

---

## 🔗 Concept Map (testuale)

- Strumento a bobina mobile → è fondamentalmente → amperometro
- Magnete permanente + bobina → generano → interazione campi magnetici → muovono → ago indicatore
- Amperometro + resistenza in parallelo (shunt) → estende → portata in corrente
- Amperometro + resistenza in serie → diventa → voltmetro
- Amperometro → si collega → in serie al circuito
- Voltmetro → si collega → in parallelo al circuito
- Amperometro ideale → ha → resistenza interna nulla
- Voltmetro ideale → ha → resistenza interna infinita
- Voltmetro elettronico → usa → FET → per avere → alta impedenza di ingresso
- Ohmetro → misura resistenza → tramite → legge di Ohm con batteria interna
- Multimetro → combina → voltmetro + amperometro + ohmetro
- Carico fittizio → sostituisce → antenna → per misurare → potenza trasmettitore
- Wattmetro passante → misura → potenza in transito → tra TX e antenna
- ROSmetro → misura → adattamento antenna
- Frequenzimetro → conta → cicli in 1 secondo → determina → frequenza
- Grid-dip meter → misura → frequenza risonanza circuiti LC → tramite → assorbimento di potenza
- Grid-dip in modo ondametro → misura → frequenza segnale esterno
- Oscilloscopio → lavora in → dominio del tempo → mostra → forme d'onda
- Analizzatore di spettro → lavora in → dominio della frequenza → mostra → composizione spettrale
- Scala dBm → è logaritmica → permette → visualizzare segnali con grande dinamica

---

## 📝 Key Takeaways

1. Tutti gli strumenti analogici a bobina mobile sono fondamentalmente **amperometri**: misurano la corrente tramite l'interazione tra il campo magnetico fisso di un magnete permanente e quello variabile generato dalla bobina.

2. La portata di un amperometro si estende con una **resistenza in parallelo** (shunt): più corrente si vuole misurare, più piccola dev'essere la resistenza di shunt.

3. Un microamperometro diventa voltmetro con una **resistenza in serie**: più alta è la tensione da misurare, più grande dev'essere la resistenza.

4. L'amperometro si collega **in serie**, il voltmetro **in parallelo**. L'amperometro ideale ha resistenza nulla, il voltmetro ideale ha resistenza infinita.

5. I **voltmetri elettronici** (basati su FET) hanno impedenza di ingresso >10 MΩ, molto superiore ai voltmetri tradizionali (~20.000 Ω/V). I multimetri digitali economici NON sono voltmetri elettronici.

6. Il **carico fittizio** è una resistenza che simula l'antenna per prove senza irradiare segnali. La potenza si calcola con $P = V^2/R$.

7. I **wattmetri passanti** misurano la potenza in transito tra trasmettitore e antenna; possono misurare anche la potenza riflessa.

8. Il **frequenzimetro** conta i cicli di una sinusoide in un secondo.

9. Il **grid-dip meter** misura la frequenza di risonanza di circuiti LC (dip = assorbimento di potenza) e può funzionare anche come **ondametro** (misuratore selettivo di frequenza).

10. L'**oscilloscopio** lavora nel dominio del tempo (asse X = tempo, asse Y = ampiezza in volt); l'**analizzatore di spettro** lavora nel dominio della frequenza (asse X = frequenza, asse Y = potenza in dBm).

11. L'analizzatore di spettro è lo strumento ideale per verificare la **pulizia spettrale** del trasmettitore, visualizzando armoniche e segnali spuri. La scala logaritmica in dBm è essenziale per gestire l'enorme dinamica dei segnali.

---

## ❓ Comprehension Questions

1. Perché uno strumento a bobina mobile è fondamentalmente un amperometro? Spiega il ruolo del magnete permanente, della bobina e della molla nel determinare la posizione dell'ago.

2. Se hai un microamperometro da 100 µA con resistenza interna di 50 Ω e vuoi realizzare un amperometro con fondo scala di 1 A, calcola il valore della resistenza di shunt necessaria. Spiega il ragionamento.

3. Perché il voltmetro si collega in parallelo e l'amperometro in serie? Cosa succede se si collegano al contrario?

4. In quali situazioni un voltmetro tradizionale può dare letture errate e perché un voltmetro elettronico risolve il problema? Qual è il ruolo del FET?

5. Spiega la differenza tra misurare la potenza del trasmettitore con un carico fittizio e con un wattmetro passante. Quando si deve usare l'uno e quando l'altro?

6. Come funziona il grid-dip meter nelle sue due modalità (dip e ondametro)? Cosa si osserva in ciascun caso?

7. Un oscilloscopio mostra una sinusoide alta 3 divisioni con la manopola a 5 V/div e larga 2 divisioni con la base tempi a 0,5 ms/div. Calcola l'ampiezza picco-picco e la frequenza del segnale.

8. Perché l'analizzatore di spettro usa una scala logaritmica in dBm anziché una scala lineare in volt? Fai un esempio che mostri il vantaggio.

9. Come si può usare un analizzatore di spettro per verificare se un trasmettitore ha problemi di armoniche? Cosa si vedrebbe sullo schermo?

10. Il waterfall di un ricevitore digitale è a tutti gli effetti un analizzatore di spettro? Quali sono le differenze rispetto a uno strumento professionale?

---

## 📚 Glossary

- **Amperometro** — Strumento che misura la corrente elettrica; si collega in serie al circuito
- **Analizzatore di spettro** — Strumento che visualizza la composizione in frequenza di un segnale (dominio della frequenza); asse X = frequenza, asse Y = potenza in dBm
- **Base dei tempi** — Manopola dell'oscilloscopio che regola la velocità di scorrimento orizzontale (tempo per divisione)
- **Bobina mobile** — Principio costruttivo degli strumenti analogici: bobina immersa in campo magnetico fisso, la cui rotazione è proporzionale alla corrente
- **Carico fittizio (Dummy load)** — Resistenza che simula l'antenna per prove del trasmettitore senza irradiare
- **Cifra di rumore (Noise figure)** — Parametro che descrive la rumorosità intrinseca dei primi stadi di un ricevitore; dipende dai componenti (transistor, FET, MOSFET)
- **Contatore** — Altro nome del frequenzimetro
- **Dip** — Dall'inglese: picco negativo, calo; nel grid-dip meter indica l'assorbimento di potenza alla frequenza di risonanza
- **Divisione** — Unità di misura sullo schermo dell'oscilloscopio/analizzatore, corrisponde a un quadratino del reticolo
- **Dominio del tempo** — Rappresentazione di un segnale in funzione del tempo (oscilloscopio)
- **Dominio della frequenza** — Rappresentazione di un segnale in funzione della frequenza (analizzatore di spettro)
- **Frequenzimetro** — Strumento che misura la frequenza contando i cicli in un secondo
- **Grid-dip meter** — Strumento per misurare la frequenza di risonanza di circuiti LC e funzionare come ondametro
- **Impedenza di ingresso** — Resistenza "vista" dal circuito in cui si inserisce lo strumento
- **Multimetro** — Strumento che combina voltmetro, amperometro e ohmetro
- **Ohmetro** — Strumento che misura la resistenza; utilizza batteria interna e legge di Ohm
- **Ondametro** — Strumento che misura la frequenza di un segnale in modo selettivo; funzione secondaria del grid-dip meter
- **Oscilloscopio** — Strumento che mostra le forme d'onda nel dominio del tempo
- **Resistenza di shunt** — Resistenza posta in parallelo all'amperometro per estenderne la portata
- **Resistenza interna** — Resistenza propria dello strumento, dovuta al filo della bobina
- **Resistenza moltiplicatrice** — Resistenza posta in serie al microamperometro per trasformarlo in voltmetro
- **ROS (Rapporto Onde Stazionarie)** — Parametro che indica l'adattamento tra trasmettitore e antenna
- **ROSmetro** — Strumento che misura il ROS
- **Span** — Nell'analizzatore di spettro: apertura della finestra di osservazione attorno alla frequenza centrale
- **Strumento RMS** — Strumento che misura il valore efficace vero, indipendente dalla forma d'onda
- **Voltmetro** — Strumento che misura la tensione; si collega in parallelo al circuito
- **Voltmetro elettronico** — Voltmetro con impedenza di ingresso molto alta (>10 MΩ), realizzato con FET
- **Wattmetro passante** — Strumento che misura la potenza in transito tra trasmettitore e antenna

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione**          | 16                                                                                                                                                                                                                                                                                                                                                   |
| **Data**             | 25 giugno 2025                                                                                                                                                                                                                                                                                                                                       |
| **Durata**           | ~1 ora e 40 minuti                                                                                                                                                                                                                                                                                                                                   |
| **Numero argomenti** | 15                                                                                                                                                                                                                                                                                                                                                   |
| **Parole chiave**    | Strumenti di misura, bobina mobile, amperometro, voltmetro, ohmetro, multimetro, shunt, resistenza serie, strumenti ideali, voltmetro elettronico, FET, carico fittizio, wattmetro passante, ROSmetro, frequenzimetro, contatore, grid-dip meter, ondametro, oscilloscopio, analizzatore di spettro, dominio del tempo, dominio della frequenza, dBm |
