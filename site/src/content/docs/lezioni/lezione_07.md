---
layout: default
title: "Modi di Emissione: AM, SSB e FM"
permalink: /guide-studio/lezione_07.html
---

# 📘 Lezione 07 - Modi di Emissione: AM, SSB e FM

## 📌 Panoramica

- **Materia**: Elettronica e Radiotecnica per la licenza di radioamatore
- **Argomento**: Modi di emissione (AM, SSB, FM), introduzione ai Decibel
- **Tempo di studio stimato**: 90–110 minuti
- **Prerequisiti**: Conoscenza dei filtri, circuiti risonanti, fattore Q (Lezione 06); concetti base di corrente alternata, frequenza, periodo, sinusoidi (Lezioni 03-05)
- **Obiettivi di apprendimento**:
  - Comprendere i tre principali tipi di modulazione: AM, FM, PM
  - Calcolare l'indice di modulazione AM e riconoscere i casi di sotto-modulazione, modulazione piena e sovra-modulazione
  - Descrivere lo spettro AM con portante e bande laterali, e calcolarne la distribuzione di potenza
  - Comprendere il principio della SSB e i suoi vantaggi rispetto all'AM
  - Distinguere splatter da armoniche
  - Comprendere la modulazione FM, deviazione, indice di modulazione FM
  - Confrontare FM a banda larga (broadcast) e FM a banda stretta (radioamatoriale)
  - Conoscere la formula della lunghezza d'onda $\lambda = 300 / f_{MHz}$
  - Conoscere e saper usare il dBm

---

## 📖 Contenuti Teorici

### 1. 🔍 Ripasso Quiz Lezione 06

La lezione si apre con la correzione dei quiz assegnati nella lezione precedente, dedicata a filtri e circuiti risonanti. Vengono rivisti i seguenti concetti chiave:

- **Filtro elimina banda**: è un filtro che attenua una certa banda di frequenze, lasciando passare quelle al di sotto e al di sopra. Si può realizzare mettendo in parallelo un filtro passa basso e un filtro passa alto.
- **Filtro passa basso**: lascia passare le frequenze al di sotto della frequenza di taglio e attenua quelle superiori. La **frequenza di taglio** è il punto in cui la tensione di uscita scende a **0,707** della tensione massima (corrispondente a metà potenza, cioè −3 dB).
- **Circuito risonante parallelo**: alla frequenza di risonanza, l'impedenza è **massima** (teoricamente infinita). È selettivo: si comporta come un filtro passa banda.
- **Circuito risonante serie**: alla frequenza di risonanza, l'impedenza è **minima** e uguale alla sola resistenza $R$ del circuito, poiché la reattanza induttiva e quella capacitiva si annullano ($X_L = X_C$).
- **Fattore di qualità Q** nel circuito risonante serie: è dato dalla formula $Q = \frac{X_L}{R}$ (o equivalentemente $Q = \frac{X_C}{R}$). Maggiore è $Q$, più il circuito è selettivo e la banda passante più stretta.
- **Filtri in serie (cascata)**: collegando più filtri dello stesso tipo in serie, l'attenuazione complessiva aumenta e la curva di risposta diventa più ripida, migliorando la selettività.
- **Impedenza di un circuito LRC serie alla risonanza**: alla frequenza di risonanza, $Z = R$, poiché le reattanze si cancellano.

---

### 2. 📡 Introduzione ai Modi di Emissione e alla Modulazione

#### 🔹 Il concetto di modulazione

Per trasmettere informazione via radio è necessario un segnale ad alta frequenza chiamato **portante** (carrier). La portante, da sola, non trasporta alcuna informazione: è una sinusoide pura a frequenza costante. L'operazione che permette di "attaccare" l'informazione (voce, musica, dati) alla portante si chiama **modulazione**.

**Modulazione** — Processo mediante il quale un segnale a bassa frequenza (il segnale modulante, ad esempio la voce) modifica una o più caratteristiche della portante ad alta frequenza per trasportare informazione.

La portante è una sinusoide descritta da tre parametri fondamentali:

- **Ampiezza**
- **Frequenza**
- **Fase**

Ciascuno di questi parametri può essere variato dal segnale modulante, dando origine ai tre tipi fondamentali di modulazione:

| Tipo   | Parametro variato | Codice ITU | Denominazione            |
| ------ | ----------------- | ---------- | ------------------------ |
| **AM** | Ampiezza          | **A3E**    | Modulazione di ampiezza  |
| **FM** | Frequenza         | **F3E**    | Modulazione di frequenza |
| **PM** | Fase              | —          | Modulazione di fase      |

La **modulazione di fase (PM)** è meno utilizzata nell'uso vocale radioamatoriale ed è tipica delle trasmissioni dati. Le due modulazioni principali nell'ambito radioamatoriale sono AM e FM.

> "La portante da sola non trasporta alcuna informazione. È come un treno vuoto: deve essere caricato con qualcosa per essere utile."

---

### 3. 📈 Modulazione di Ampiezza (AM) in Dettaglio

#### 🔹 Principio di funzionamento

Nella modulazione di ampiezza, il **segnale modulante** (la voce, ad esempio) varia l'**ampiezza** della portante. Quando si parla nel microfono, l'ampiezza della portante cresce e decresce seguendo l'andamento del segnale audio. La frequenza della portante rimane costante.

L'**inviluppo** del segnale modulato riproduce la forma d'onda del segnale modulante. Se il segnale modulante è una sinusoide, l'inviluppo sarà sinusoidale; se è la voce, seguirà le variazioni della voce.

#### 🔹 Indice di modulazione AM

L'**indice di modulazione** (indicato con $m$) quantifica il rapporto tra l'ampiezza del segnale modulante e l'ampiezza della portante:

$$m = \frac{V_m}{V_p}$$

dove:

- $V_m$ = ampiezza del segnale modulante
- $V_p$ = ampiezza della portante

Si distinguono tre casi fondamentali:

1. **$m < 1$ (sotto-modulazione, es. $m = 0{,}5$ ovvero 50%)**: La portante è modulata solo parzialmente. Il segnale trasmesso è corretto ma **inefficiente**, perché molta potenza resta nella portante che non trasporta informazione. Il segnale ricevuto sarà più debole rispetto al caso ottimale.

2. **$m = 1$ (100%, modulazione piena)**: Caso ottimale. L'ampiezza della portante varia dal doppio del suo valore a zero. Tutta la capacità di modulazione è sfruttata, massimizzando l'efficienza nella trasmissione dell'informazione.

3. **$m > 1$ (sovra-modulazione, es. $m > 100\%$)**: Situazione da evitare assolutamente. L'ampiezza dell'inviluppo dovrebbe andare sotto lo zero, il che è fisicamente impossibile. Il segnale viene **tagliato** (clipping), producendo una distorsione grave che genera componenti spurie note come **splatter**.

> **⚠️ Errore comune**: Confondere splatter con armoniche. Sono due fenomeni distinti (vedi sezione dedicata più avanti).

#### 🔹 Controllo del guadagno microfonico

Nei trasmettitori AM e SSB è presente una manopola chiamata **guadagno microfonico** (mic gain) che permette di regolare l'ampiezza del segnale modulante. Va regolata con attenzione:

- Troppo basso → sotto-modulazione, segnale debole
- Troppo alto → sovra-modulazione, distorsione e splatter
- Il valore ideale si raggiunge osservando un indicatore (strumento di misura o LED) presente sul trasmettitore

#### 🔹 Lo splatter

Lo **splatter** è un fenomeno di distorsione causato dalla sovra-modulazione ($m > 1$). Quando il segnale modulato viene "tagliato", si generano componenti spettrali spurie che si estendono sui canali adiacenti, disturbando le comunicazioni di altri operatori.

Lo splatter si manifesta come un **allargamento del segnale** nella banda, che fuoriesce dal canale assegnato e interferisce con i canali vicini.

#### 🔹 Spettro del segnale AM — Dominio della frequenza

Un segnale AM nel **dominio della frequenza** è composto da tre componenti:

1. **Portante** ($f_c$): al centro, alla frequenza del trasmettitore
2. **Banda laterale superiore (USB — Upper Side Band)**: a frequenza $f_c + f_m$
3. **Banda laterale inferiore (LSB — Lower Side Band)**: a frequenza $f_c - f_m$

dove $f_m$ è la frequenza del segnale modulante.

La **larghezza di banda** occupata da un segnale AM è:

$$B_{AM} = 2 \times f_{m_{max}}$$

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-10.jpg" alt="Larghezza di banda AM" style="width: 75%;"></div><br>

Per la voce umana ($f_{m_{max}} \approx 3{-}3{,}5$ kHz), la banda occupata è circa **6–7 kHz**. Esempio pratico: nella CB (Citizens Band) i canali sono distanziati di 10 kHz.

#### 🔹 Distribuzione della potenza in AM

A modulazione piena ($m = 1$, 100%), la potenza si distribuisce come segue:

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-12.jpg" alt="Distribuzione della potenza in AM" style="width: 75%;"></div><br>

| Componente                     | Quota di potenza  |
| ------------------------------ | ----------------- |
| Portante                       | **2/3** (≈ 66,7%) |
| Banda laterale superiore (USB) | **1/6** (≈ 16,7%) |
| Banda laterale inferiore (LSB) | **1/6** (≈ 16,7%) |

Questo evidenzia il grande svantaggio dell'AM: **due terzi della potenza** sono impiegati per la portante, che **non contiene alcuna informazione**. Solo un terzo della potenza trasporta effettivamente il messaggio, distribuito equamente tra le due bande laterali.

> "In AM, due terzi della potenza se ne vanno nella portante, che è come mandare un treno pieno di vagoni vuoti."

---

### 4. 📡 SSB — Banda Laterale Unica (Single Side Band)

#### 🔹 Il principio della SSB

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-13.jpg" alt="Principio della SSB" style="width: 75%;"></div><br>

La SSB nasce dall'osservazione che:

- La **portante** non trasporta informazione (spreco di 2/3 della potenza)
- Le due **bande laterali** contengono la stessa informazione (sono simmetriche)

La soluzione è eliminare la portante **e** una delle due bande laterali, trasmettendo solo la banda laterale rimanente:

- **USB (Upper Side Band)**: si trasmette solo la banda laterale superiore. Codice ITU: **J3E**.
- **LSB (Lower Side Band)**: si trasmette solo la banda laterale inferiore.

Per convenzione radioamatoriale:

- Sulle **onde corte HF sotto i 10 MHz** si usa prevalentemente la **LSB**
- Sulle **onde corte HF sopra i 10 MHz** e in **VHF** si usa prevalentemente la **USB**

#### 🔹 Vantaggi della SSB rispetto all'AM

1. **Efficienza di potenza**: tutta la potenza trasmessa contiene informazione (niente spreco nella portante). A parità di potenza totale, il segnale utile è molto più forte.
2. **Larghezza di banda dimezzata**: la banda occupata è circa **3 kHz** (la metà rispetto ai 6–7 kHz dell'AM). In un dato spazio di spettro ci stanno il doppio dei canali.
3. **Nessuna emissione in silenzio**: quando l'operatore non parla, il trasmettitore non emette potenza (non c'è portante), a differenza dell'AM dove la portante è sempre presente. Questo riduce il consumo energetico e l'interferenza.
4. **Migliore sensibilità in ricezione**: meno rumore nella banda più stretta.

#### 🔹 Svantaggi della SSB

1. **Apparecchiatura più complessa e costosa**: il ricevitore deve rigenerare la portante localmente tramite un oscillatore (BFO — Beat Frequency Oscillator).
2. **Sintonia più critica**: in SSB è necessario sintonizzarsi con precisione. Uno spostamento anche piccolo della frequenza del ricevitore altera il tono della voce ricevuta, fino a renderla incomprensibile. In AM, una leggera imprecisione nella sintonia non altera significativamente la qualità audio.

#### 🔹 Portante residua in SSB

Anche in un trasmettitore SSB rimane una minima portante residua. In un trasmettitore da 100 W, la portante residua è tipicamente dell'ordine di **10–100 mW**, trascurabile in pratica.

---

### 5. ⚡ Splatter vs Armoniche: Distinzione Fondamentale

Un chiarimento importante emerso durante la lezione riguarda la distinzione tra **splatter** e **armoniche**, due fenomeni diversi spesso confusi:

| Caratteristica          | Splatter                           | Armoniche                                               |
| ----------------------- | ---------------------------------- | ------------------------------------------------------- |
| **Causa**               | Sovra-modulazione ($m > 1$)        | Saturazione dell'amplificatore (non linearità)          |
| **Dove si manifestano** | **In banda** (canali adiacenti)    | **Fuori banda** (multipli della frequenza fondamentale) |
| **Frequenze coinvolte** | Vicine alla frequenza di emissione | $2f$, $3f$, $4f$, ...                                   |
| **Effetto**             | Disturba le stazioni adiacenti     | Può interferire con altri servizi radio                 |
| **Rimedio**             | Ridurre il guadagno microfonico    | Filtri armonici in uscita                               |

Lo **splatter** è un fenomeno **in banda**: il segnale si allarga e invade i canali adiacenti. Le **armoniche** sono un fenomeno **fuori banda**: si generano segnali a frequenze multiple della fondamentale (se trasmetto a 7 MHz, le armoniche sono a 14 MHz, 21 MHz, 28 MHz, ecc.).

---

### 6. 📻 Modulazione di Frequenza (FM)

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-17.jpg" alt="Modulazione di Frequenza" style="width: 75%;"></div><br>

#### 🔹 Principio di funzionamento

Nella modulazione di frequenza, l'ampiezza della portante **resta costante**, mentre è la **frequenza** della portante a variare in funzione del segnale modulante. Quando si parla, la frequenza della portante aumenta e diminuisce seguendo l'andamento del segnale audio.

#### 🔹 Deviazione e indice di modulazione FM

La **deviazione di frequenza** ($\Delta f$) è lo spostamento massimo della frequenza della portante rispetto al suo valore nominale.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-18.jpg" alt="Deviazione di frequenza" style="width: 75%;"></div><br>

L'**indice di modulazione FM** è definito come:

$$m_{FM} = \frac{\Delta f}{f_m}$$

dove:

- $\Delta f$ = deviazione massima di frequenza
- $f_m$ = frequenza del segnale modulante

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-19.jpg" alt="Indice di modulazione FM" style="width: 75%;"></div><br>

A differenza dell'AM, l'indice di modulazione FM **non ha un limite superiore intrinseco** (può superare 1 senza distorsione). Tuttavia, un indice più alto produce un segnale più largo in frequenza, quindi deve essere regolato per rispettare le norme sull'occupazione di banda.

#### 🔹 FM Broadcast vs FM Radioamatoriale (Narrowband)

| Parametro                 | FM Broadcast (radio commerciale) | FM Radioamatoriale (narrowband) |
| ------------------------- | -------------------------------- | ------------------------------- |
| **Indice di modulazione** | ~5                               | ~1                              |
| **Deviazione**            | ±75 kHz                          | ±4–5 kHz                        |
| **Banda audio massima**   | 15 kHz                           | ~3 kHz                          |
| **Spaziatura canali**     | ~300 kHz                         | 12,5–25 kHz                     |

La FM radioamatoriale è detta **a banda stretta** (narrowband FM, NBFM).

#### 🔹 Vantaggi della FM

1. **Insensibilità ai disturbi di ampiezza**: poiché l'informazione è nella frequenza e non nell'ampiezza, i disturbi atmosferici, le scariche elettriche e i rumori artificiali (che variano l'ampiezza del segnale) non influenzano la ricezione FM. Il ricevitore FM ha un **limitatore** che taglia le variazioni di ampiezza.
2. **Efficienza del trasmettitore**: un trasmettitore FM può raggiungere un'efficienza dell'**80%** (assorbe 200 W dalla rete e genera 160 W RF), contro il 50% tipico di un trasmettitore AM/SSB.
3. **Potenza costante**: la potenza trasmessa non varia con la modulazione (a differenza dell'AM, dove la potenza aumenta con la modulazione).
4. **Sintonia non critica**: non richiede precisione nella sintonia come la SSB. Alcuni ricevitori FM hanno persino la ricerca automatica della frequenza.
5. **Nessun controllo manuale della deviazione**: a differenza dell'AM/SSB, i trasmettitori FM regolano automaticamente la deviazione, senza necessità della manopola di guadagno microfonico.

#### 🔹 Svantaggio principale della FM

La FM occupa una **banda molto più larga** rispetto alla SSB. Per questo motivo:

- La FM è usata principalmente nelle bande **VHF e UHF** (144 MHz, 430 MHz, ecc.) dove c'è ampio spazio
- La FM **non è ammessa** nelle bande delle onde corte (HF) a livello internazionale, dove lo spazio è limitato e si usa prevalentemente la SSB

---

### 7. 🔍 Regolazione della Banda del Ricevitore

Durante la sessione di domande, viene trattato il tema della **regolazione della larghezza di banda** del ricevitore. Il ricevitore è paragonato a una **finestra aperta sul mondo**: più la finestra è ampia, più rumore entra; più è stretta, più il segnale desiderato può emergere dal rumore.

- **Uso normale**: la regolazione di banda non è necessaria
- **Ricerca di segnali deboli**: si restringe la banda al minimo indispensabile per ricevere il segnale, eliminando il più possibile il rumore e i segnali adiacenti. Questo è utile quando si cercano collegamenti difficili (DX) o segnali deboli immersi nei disturbi

---

### 8. 🔊 I Decibel (dB)

Il decibel (dB) è un'unità di misura logaritmica ampiamente usata in radiotecnica. Consente di gestire facilmente grandezze con dinamiche molto ampie.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-24.jpg" alt="Decibel e potenza" style="width: 75%;"></div><br>

#### 🔹 Unità di misura relativa
Il decibel è un'unità di misura **relativa**. Tipicamente confronta i livelli di potenza tra l'uscita e l'ingresso di un amplificatore o di un attenuatore.
Il vantaggio principale dell'uso dei logaritmi è che **moltiplicazioni e divisioni si trasformano in addizioni e sottrazioni**. Questo rende molto più semplice calcolare i livelli di potenza lungo una catena di trasmissione o ricezione.

#### 🔹 Calcolo del Guadagno
Il guadagno di potenza ($G$) di un amplificatore è definito come:
$$G = 10 \log_{10} \left(\frac{P_{out}}{P_{in}}\right) \text{ dB}$$

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-25.jpg" alt="Raddoppio di potenza" style="width: 75%;"></div><br>

**Regola pratica fondamentale**:
- **+3 dB** equivale a un **raddoppio** della potenza ($P_{out} = 2 \times P_{in}$)
- **-3 dB** equivale a un **dimezzamento** della potenza ($P_{out} = P_{in} / 2$)
- **+10 dB** equivale a moltiplicare la potenza per **10**
- **-10 dB** equivale a dividere la potenza per **10** (attenuazione)

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-26.jpg" alt="Attenuatore" style="width: 75%;"></div><br>

#### 🔹 Catene di amplificazione
Quando si mettono in cascata più amplificatori o attenuatori, il guadagno totale in dB è semplicemente la **somma algebrica** dei guadagni in dB di ogni singolo stadio.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-27.jpg" alt="Amplificatori in cascata" style="width: 75%;"></div><br>

*Esempio*: Un amplificatore con $G_1 = 10$ dB in cascata con uno da $G_2 = 20$ dB produce un guadagno totale di $30$ dB.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-28.jpg" alt="Esempio 5W a 100W" style="width: 75%;"></div><br>
<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-29.jpg" alt="Esempio raddoppio a 200W" style="width: 75%;"></div><br>

#### 🔹 Il dBm (Decibel-milliwatt)
Se si fissa un livello di riferimento assoluto, il decibel diventa un'unità di misura **assoluta**. In radiotecnica si usa comunemente il **dBm**, dove il livello di riferimento è **1 milliwatt (1 mW)**.

- **0 dBm = 1 mW**
- **+30 dBm = 1 W** (1000 mW, ovvero $+10$ dB per tre volte)
- **+50 dBm = 100 W**

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_07/slide-32.jpg" alt="Tabella dBm" style="width: 75%;"></div><br>

---

## 📝 Punti Chiave

1. La **modulazione** è il processo che permette di trasportare informazione su una portante radio. I tre tipi fondamentali sono AM (ampiezza), FM (frequenza) e PM (fase), classificati con codici ITU: AM = A3E, FM = F3E, SSB = J3E.

2. In **AM**, l'indice di modulazione $m = V_m / V_p$ deve idealmente essere pari a 1 (100%). Se $m > 1$, si produce **splatter** — allargamento del segnale che disturba i canali adiacenti.

3. Lo **spettro AM** è composto dalla portante e da due bande laterali (USB e LSB). A modulazione piena, **2/3 della potenza** sta nella portante (che non trasporta informazione) e solo **1/3** nelle bande laterali.

4. La **SSB** elimina portante e una banda laterale, ottenendo: tutta la potenza utile, metà della banda occupata, nessuna emissione in silenzio. Per contro, richiede apparecchiatura più complessa e sintonia precisa.

5. Lo **splatter** (in banda, da sovra-modulazione) è concettualmente diverso dalle **armoniche** (fuori banda, da saturazione dell'amplificatore). Rimedi diversi: mic gain per lo splatter, filtri armonici per le armoniche.

6. In **FM**, la potenza trasmessa è costante, l'indice di modulazione $m_{FM} = \Delta f / f_m$ può superare 1, e i disturbi di ampiezza non influenzano la ricezione. L'efficienza del trasmettitore può raggiungere l'80%.

7. La FM radioamatoriale è **a banda stretta** (NBFM): deviazione ±4–5 kHz, indice ~1. La FM broadcast ha indice ~5 e deviazione ±75 kHz.

8. La FM è usata in **VHF/UHF** (dove c'è spazio), non è ammessa in **HF** (onde corte) a livello internazionale per la sua eccessiva occupazione di banda.

9. Il **decibel (dB)** è un'unità relativa che esprime il rapporto tra due potenze.

10. **+3 dB** significa raddoppiare la potenza, mentre **+10 dB** significa decuplicarla. L'unità assoluta **dBm** usa 1 mW come riferimento (es. 0 dBm = 1 mW, 30 dBm = 1 W).

---


## ❓ Domande di Comprensione

1. Perché in AM la portante rappresenta uno spreco di potenza? Come si risolve questo problema nella SSB?

2. Un trasmettitore AM da 150 W opera con modulazione piena ($m = 1$). Quanta potenza è effettivamente impiegata per trasmettere informazione e quanta è "sprecata" nella portante?

3. Spiega la differenza tra splatter e armoniche: da cosa sono causati, dove si manifestano nello spettro e quali sono i rimedi per ciascun fenomeno.

4. Perché la modulazione di frequenza non è ammessa sulle bande delle onde corte (HF) a livello internazionale? Qual è il vantaggio compensato da questo svantaggio?

5. Un operatore radioamatore trasmette a 14,2 MHz in SSB. Qual è la larghezza di banda approssimativa del suo segnale? E se trasmettesse in AM, quanto sarebbe larga la banda occupata?

6. Calcola la lunghezza d'onda di un segnale a 145 MHz. A quale banda radioamatoriale corrisponde? Che tipo di modulazione si usa tipicamente su questa banda?

7. Perché un trasmettitore FM ha un'efficienza maggiore di un trasmettitore AM? Cosa c'entra la costanza della potenza nel segnale FM?

8. L'indice di modulazione in AM non può superare 1 senza conseguenze negative, mentre in FM può essere maggiore di 1 senza distorsione. Spiega il motivo di questa differenza e cosa limita comunque l'indice FM.

9. In che modo la regolazione della larghezza di banda del ricevitore aiuta nella ricezione di segnali deboli? Usa l'analogia della finestra.

10. Un radioamatore vuole operare sulla banda dei 20 m. A quale frequenza approssimativa corrisponde? Userà LSB o USB? Perché?

---

## 📚 Glossario

- **A3E** — Codice ITU per la modulazione di ampiezza (AM) con emissione a doppia banda laterale e portante completa.
- **AM (Modulazione di Ampiezza)** — Tipo di modulazione in cui l'informazione è trasmessa variando l'ampiezza della portante.
- **Banda laterale (Sideband)** — Componente dello spettro di un segnale modulato, situata sopra (USB) o sotto (LSB) la frequenza della portante.
- **BFO (Beat Frequency Oscillator)** — Oscillatore locale nel ricevitore SSB che rigenera la portante soppressa per demodulare il segnale.
- **Deviazione di frequenza ($\Delta f$)** — Spostamento massimo della frequenza della portante rispetto al valore nominale in modulazione FM.
- **F3E** — Codice ITU per la modulazione di frequenza (FM) con emissione in fonia.
- **FM (Modulazione di Frequenza)** — Tipo di modulazione in cui l'informazione è trasmessa variando la frequenza della portante, mantenendo costante l'ampiezza.
- **HF (High Frequency)** — Banda di frequenza da 3 a 30 MHz, corrispondente alle onde corte.
- **Indice di modulazione AM ($m$)** — Rapporto tra l'ampiezza del segnale modulante e l'ampiezza della portante: $m = V_m / V_p$.
- **Indice di modulazione FM ($m_{FM}$)** — Rapporto tra la deviazione massima di frequenza e la frequenza del segnale modulante: $m_{FM} = \Delta f / f_m$.
- **Inviluppo** — Curva che descrive l'andamento dell'ampiezza massima (e minima) del segnale modulato nel tempo.
- **J3E** — Codice ITU per la SSB (Single Side Band), emissione a banda laterale unica con portante soppressa.
- **Lambda ($\lambda$)** — Simbolo della lunghezza d'onda, espressa in metri.
- **LSB (Lower Side Band)** — Banda laterale inferiore, usata convenzionalmente sotto i 10 MHz in HF.
- **Lunghezza d'onda ($\lambda$)** — Distanza percorsa da un'onda elettromagnetica durante un ciclo completo. Si calcola con $\lambda = 300 / f_{MHz}$ [m].
- **MF (Medium Frequency)** — Banda di frequenza da 300 kHz a 3 MHz, corrispondente alle onde medie.
- **Modulazione** — Processo mediante il quale un segnale a bassa frequenza modifica le caratteristiche di una portante per trasportare informazione.
- **NBFM (Narrowband FM)** — FM a banda stretta, tipica dell'uso radioamatoriale, con deviazione di ±4–5 kHz.
- **Onda elettromagnetica** — Perturbazione dei campi elettrico e magnetico che si propaga nello spazio alla velocità della luce.
- **PM (Modulazione di Fase)** — Tipo di modulazione in cui l'informazione è trasmessa variando la fase della portante.
- **Portante (Carrier)** — Segnale sinusoidale ad alta frequenza sul quale viene sovrapposta l'informazione tramite modulazione.
- **Segnale modulante** — Segnale a bassa frequenza (voce, musica, dati) che contiene l'informazione da trasmettere.
- **Sovra-modulazione** — Condizione in cui l'indice di modulazione AM supera 1, causando distorsione e splatter.
- **Splatter** — Distorsione in banda causata dalla sovra-modulazione AM, che produce allargamento del segnale verso i canali adiacenti.
- **SSB (Single Side Band)** — Tecnica di modulazione derivata dall'AM in cui la portante e una banda laterale vengono soppresse, trasmettendo solo una banda laterale.
- **UHF (Ultra High Frequency)** — Banda di frequenza da 300 MHz a 3 GHz.
- **USB (Upper Side Band)** — Banda laterale superiore, usata convenzionalmente sopra i 10 MHz e in VHF.
- **Velocità della luce ($c$)** — Velocità di propagazione delle onde elettromagnetiche nel vuoto: circa 300.000 km/s ($3 \times 10^8$ m/s).
- **VHF (Very High Frequency)** — Banda di frequenza da 30 a 300 MHz, corrispondente alle onde ultracorte.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore principale**: Paolo — docente del corso, esperto di radiotecnica e modulazioni
- 👨‍🏫 **Co-docente**: Alessio — presente in aula, prende il coordinamento al termine della parte tecnica
- 👨‍🏫 **Partecipante attivo**: Giovanni — interviene con domande e precisazioni (denominazioni delle bande, quiz ministeriali)

---

## 📅 Informazioni Lezione

| Campo                  | Valore                                                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Numero lezione**     | 07                                                                                                                                                                                    |
| **Data**               | 29 aprile 2026                                                                                                                                                                        |
| **Durata**             | ~110 minuti                                                                                                                                                                           |
| **Argomenti trattati** | 4 (Modi di emissione AM/SSB/FM, Decibel)                                                                                                                                           |
| **Parole chiave**      | Modulazione, AM, FM, SSB, portante, bande laterali, indice di modulazione, splatter, armoniche, deviazione, narrowband, decibel, dB, dBm, guadagno, attenuazione |
| **Prossima lezione**   | 6 maggio 2026                                                                                                                              |
