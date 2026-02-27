# 📘 Lezione 11 - Trasmettitori

## 📌 Overview

- **Materia**: Radiotecnica — Il Diodo e gli Alimentatori
- **Tempo di studio stimato**: 2 ore e 30 minuti
- **Prerequisiti**: Concetti di tensione alternata e continua, trasformatori, condensatori, resistenza e impedenza (Lezioni 04-06), bande radioamatoriali e normativa (Lezioni 09-10)
- **Obiettivi di apprendimento**:
  - Comprendere il funzionamento dei semiconduttori e della giunzione P-N
  - Conoscere i cinque tipi di diodi e le loro applicazioni
  - Capire lo schema a blocchi di un alimentatore lineare (trasformatore, raddrizzatore, filtro, stabilizzatore)
  - Distinguere raddrizzamento a singola e doppia semionda
  - Comprendere il principio dell'isolamento galvanico e la sua importanza per la sicurezza
  - Conoscere i vantaggi e svantaggi degli alimentatori a commutazione (switching) rispetto ai lineari

---

## 📖 Core Content

### 1. 🔍 Correzione Quiz Lezione 10 (⏱ 00:02)

La lezione si apre con la correzione del quiz della settimana precedente (Lezione 10), condotta da Silvio IZ5DIY. I risultati sono complessivamente buoni, con la maggior parte degli studenti che ha risposto correttamente.

Le domande più significative riguardano:

- **88 metri non è una banda radioamatoriale**: la risposta corretta è che 88 m non è una banda assegnata ai radioamatori. È fondamentale conoscere le bande assegnate (160 m, 80 m, 40 m, 20 m, ecc.) e riconoscere quelle che non lo sono.
- **VHF = 30-300 MHz**: le gamme di frequenza procedono per fattori di 10: HF va da 3 a 30 MHz, VHF da 30 a 300 MHz, UHF da 300 a 3000 MHz. Basta ricordare la progressione moltiplicativa per 10.
- **L'America appartiene alla Regione 2 ITU**: l'Italia è nella Regione 1, l'America nella Regione 2 e l'Asia/Oceania nella Regione 3.
- **La patente di radioamatore non scade**: questo è un concetto ricorrente all'esame. La patente non ha scadenza, a differenza dell'**autorizzazione generale** che scade ogni 10 anni.
- **145 MHz è la frequenza centrale della banda dei 2 metri**: la banda VHF dei 2 m va da 144 a 146 MHz, quindi il centro è a 145 MHz.

---

### 2. 📡 Il Diodo — Semiconduttori e Giunzione P-N (⏱ 09:00)

#### 🔹 Introduzione ai Semiconduttori

Il diodo è un componente elettronico fondamentale costruito a partire da materiali **semiconduttori**. Per comprenderne il funzionamento, Paolo introduce il concetto di resistività dei materiali:

- **Conduttori** (es. rame): resistività molto bassa, dell'ordine dei milliohm
- **Isolanti** (es. vetro, ceramica): resistività elevatissima, dell'ordine di centinaia di milioni di ohm
- **Semiconduttori** (es. silicio, germanio): resistività intermedia, tra 100.000 e 1.000.000 di ohm

Il **silicio** è il semiconduttore più utilizzato nell'industria elettronica. Allo stato puro (intrinseco) il silicio ha quattro elettroni di valenza che formano legami covalenti con gli atomi adiacenti, creando una struttura cristallina stabile.

#### 🔹 Il Drogaggio (EXTRA — non materia d'esame)

Paolo approfondisce, a titolo didattico, il processo di **drogaggio** (**doping**) che rende il silicio utile per l'elettronica:

- **Drogaggio di tipo P**: si introducono atomi con 3 elettroni di valenza (es. **indio**). La mancanza di un elettrone nel reticolo cristallino crea una **lacuna** (hole), cioè una "buca" che si comporta come una carica positiva mobile.
- **Drogaggio di tipo N**: si introducono atomi con 5 elettroni di valenza (es. **arsenico**). L'elettrone in eccesso è libero di muoversi, creando portatori di carica negativi.

Quando si uniscono una regione P e una regione N si forma la **giunzione P-N**. All'interfaccia si crea una **regione di svuotamento** (depletion region), priva di portatori di carica, che agisce come un isolante naturale.

#### 🔹 Polarizzazione del Diodo

Il diodo ha due terminali:

- **Anodo** (A): terminale positivo
- **Catodo** (K): terminale negativo (contrassegnato da una banda sul corpo del componente)

Il simbolo circuitale del diodo è un triangolo che punta verso una barra; la corrente convenzionale scorre nella direzione della freccia (dall'anodo al catodo).

- **Polarizzazione diretta** (forward bias): si applica tensione positiva all'anodo rispetto al catodo. La regione di svuotamento si assottiglia e, superata la **tensione di soglia** di circa **0,7 V** per il silicio (0,3 V per il germanio), il diodo conduce come un interruttore chiuso.
- **Polarizzazione inversa** (reverse bias): si applica tensione positiva al catodo rispetto all'anodo. La regione di svuotamento si allarga e il diodo non conduce, comportandosi come un interruttore aperto.

> **Regola pratica**: il diodo si fa attraversare dalla corrente solo quando l'anodo è positivo rispetto al catodo.

---

### 3. 🔧 I Cinque Tipi di Diodi (⏱ 30:00)

Questa sezione è **materia d'esame**. Paolo elenca e descrive cinque tipologie fondamentali di diodi:

#### 🔹 1. Diodo Raddrizzatore

Il diodo raddrizzatore è il tipo più comune e viene utilizzato per trasformare la corrente alternata (AC) in corrente continua (DC). Quando è in conduzione, presenta una caduta di tensione tipica di **0,7 V**. Le sue caratteristiche principali sono:

- **Tensione inversa massima**: la massima tensione che può sopportare in polarizzazione inversa senza danneggiarsi
- **Corrente massima**: la massima corrente che può attraversarlo

> **Esempio**: il diodo **1N4007** ha una tensione inversa massima di 1000 V e una corrente massima di 1 A.

#### 🔹 2. LED (Light Emitting Diode)

Il **LED** — **diodo a emissione luminosa** — emette luce quando è polarizzato direttamente. Il meccanismo fisico è il seguente: gli elettroni energizzati che attraversano la giunzione, quando si ricombinano con le lacune, rilasciano energia sotto forma di **fotoni** (luce). Il colore della luce dipende dal materiale semiconduttore utilizzato e dalla larghezza della banda proibita (band gap).

#### 🔹 3. Diodo Zener

Il diodo **Zener** è progettato per funzionare in **polarizzazione inversa**. Quando la tensione inversa raggiunge un valore specifico chiamato **tensione di Zener**, il diodo inizia a condurre mantenendo la tensione ai suoi capi costante a quel valore. Questa proprietà lo rende ideale come **stabilizzatore di tensione**.

> **Esempio**: uno Zener da 12 V mantiene costantemente 12 V ai suoi terminali indipendentemente dalle variazioni del carico, compensando le variazioni di corrente secondo la legge di Kirchhoff.

Nello schema tipico, lo Zener è collegato al circuito di stabilizzazione degli alimentatori per fornire una tensione di riferimento fissa.

#### 🔹 4. Diodo Varicap

Il diodo **Varicap** (o **varactor**) funziona in **polarizzazione inversa** e si comporta come un **condensatore variabile**. La regione di svuotamento della giunzione P-N agisce come il dielettrico tra le "armature" del condensatore: variando la tensione inversa applicata, si modifica la larghezza della regione di svuotamento e quindi la capacità.

Questo lo rende ideale per l'**accordo elettronico** dei circuiti risonanti (es. sintonizzazione radio senza componenti meccanici).

#### 🔹 5. Diodo Schottky (Hot Carrier)

Il diodo **Schottky** (detto anche **hot carrier**) ha una giunzione **metallo-semiconduttore** anziché la classica P-N. Questo gli conferisce una velocità di commutazione molto elevata, rendendolo adatto a lavorare ad **alte frequenze** (UHF, SHF, dell'ordine dei GHz). Nel simbolo circuitale, il catodo presenta una forma a "S".

---

### 4. ⚡ Alimentatori Lineari — Schema a Blocchi (⏱ 63:00)

L'alimentatore lineare trasforma la tensione alternata della rete elettrica (220-230 V AC a 50 Hz) in una tensione continua stabile (tipicamente 12 V DC) per alimentare apparecchiature elettroniche come le radio. Lo **schema a blocchi** è composto da quattro stadi in cascata:

$$\text{Rete AC 220V} \rightarrow \boxed{\text{Trasformatore}} \rightarrow \boxed{\text{Raddrizzatore}} \rightarrow \boxed{\text{Filtro}} \rightarrow \boxed{\text{Stabilizzatore}} \rightarrow \text{12V DC}$$

#### 🔹 Stadio 1: Trasformatore (⏱ 64:44)

Il trasformatore svolge due funzioni fondamentali:

1. **Abbassamento della tensione**: trasforma i 220 V AC della rete in una tensione più vicina a quella desiderata in uscita (es. da 220 V a 18 V AC per ottenere poi 12 V DC in uscita).

2. **Isolamento galvanico**: garantisce la separazione elettrica tra il circuito primario (rete 220 V) e il circuito secondario (apparecchiatura). Tra primario e secondario di un trasformatore non c'è passaggio di elettroni: l'energia si trasferisce tramite **campi magnetici**. Questo impedisce che un operatore, toccando i terminali di uscita dell'alimentatore, possa chiudere un circuito elettrico con il suolo e subire una scarica elettrica.

> **Isolamento galvanico** — separazione elettrica completa tra due circuiti, che impedisce il passaggio di corrente tra essi. È uno dei principi fondamentali della **sicurezza elettrica**.

Paolo illustra il pericolo della mancanza di isolamento galvanico: se un carico è collegato direttamente alla rete (fase + neutro), una persona che tocca un conduttore può chiudere un circuito attraverso il proprio corpo e il suolo verso la presa di terra della centrale Enel, subendo una scarica potenzialmente mortale. Anche il filo del neutro, che è messo a terra nella centrale Enel, può presentare una tensione significativa rispetto a terra quando arriva nelle abitazioni, a causa delle cadute di tensione lungo centinaia di metri di cavo e delle utenze intermedie.

> ⚠️ Gli **autotrasformatori**, usati in passato per motivi economici, non realizzano l'isolamento galvanico e sono oggi fuori legge per ragioni di sicurezza.

#### 🔹 Stadio 2: Raddrizzatore (⏱ 73:07)

Il raddrizzatore trasforma la tensione alternata in uscita dal trasformatore in una **tensione continua pulsante**, utilizzando diodi.

> **Tensione continua** — tensione in cui la corrente scorre sempre nello stesso verso (non necessariamente a valore costante).

**Raddrizzatore a singola semionda**: utilizza un singolo diodo che lascia passare solo le semionde positive della sinusoide. In uscita si ottiene una tensione pulsante alla stessa frequenza dell'ingresso (50 Hz), con lunghi intervalli a tensione zero tra un impulso e l'altro.

**Raddrizzatore a doppia semionda**: recupera anche le semionde negative invertendole, producendo una tensione pulsante a **frequenza doppia** rispetto all'ingresso (100 Hz con ingresso a 50 Hz). Questo riduce significativamente i "buchi" nella tensione di uscita, avvicinandola a una tensione costante.

Due realizzazioni circuitali principali:

1. **Con trasformatore a presa centrale**: usa un trasformatore con secondario doppio e due diodi che lavorano in alternanza. Il diodo superiore conduce durante le semionde dispari, il diodo inferiore durante le semionde pari.

2. **Ponte di Graetz** (raddrizzatore a ponte): usa quattro diodi disposti a forma di "ponte" quadrato e un trasformatore con secondario singolo. In ogni semionda, una coppia di diodi conduce (D2+D4 nella semionda positiva, D1+D3 nella semionda negativa). Questo è il metodo più comunemente usato e si trova spesso come componente integrato.

#### 🔹 Stadio 3: Filtro di Livellamento (⏱ 87:18)

Il filtro di livellamento utilizza **condensatori elettrolitici di grande capacità** che funzionano come serbatoi di energia:

- Quando la tensione pulsante è in fase crescente, il condensatore si carica
- Quando la tensione pulsante è in fase calante o assente, il condensatore si scarica lentamente fornendo energia al circuito a valle
- Il risultato è una tensione quasi costante con una piccola **ondulazione residua** (ripple)

L'alimentatore può essere concettualmente diviso in due parti separate dal condensatore di filtro: la parte a monte ha il compito di mantenere il condensatore ben carico, la parte a valle preleva l'energia e la regola al valore desiderato.

#### 🔹 Stadio 4: Stabilizzatore (⏱ 90:17)

Lo stabilizzatore esegue il livellamento finale e regola la tensione al valore preciso desiderato. Esistono due tipologie:

**1. Stabilizzazione con diodo Zener**: uno Zener collegato insieme a un transistor blocca la tensione di uscita al valore di Zener. Schema semplice ma con tensione di uscita fissa e non regolabile, adatto solo a piccole potenze.

**2. Stabilizzazione a retroazione (feedback)**: è il metodo più diffuso. Il cuore è un **amplificatore di errore** che confronta continuamente due tensioni:

- Una **tensione di riferimento fissa** $V_Z$ (ottenuta da un diodo Zener)
- Un campione della **tensione di uscita** (prelevata tramite un partitore resistivo)

Se la tensione di uscita cala (per esempio per un aumento del carico), si genera una **tensione di errore** che modifica la polarizzazione del transistor di regolazione, compensando la variazione. Questo **anello di controllo** (loop di retroazione) mantiene la tensione costante indipendentemente dalle variazioni di carico.

In molti alimentatori è presente un **trimmer** o **potenziometro** nel circuito di retroazione che permette di regolare la tensione di uscita (es. da 8 a 18 V) variando la quantità di segnale di uscita che arriva all'amplificatore di errore.

---

### 5. 🔌 Alimentatori a Commutazione (Switching) (⏱ 99:32)

> ⚠️ Gli alimentatori a commutazione **non fanno attualmente parte del programma d'esame**, ma sono trattati perché presenti in tutte le stazioni radioamatoriali moderne.

#### 🔹 Principio di Funzionamento

A differenza degli alimentatori lineari dove il trasformatore è il primo elemento, negli alimentatori switching la sequenza è diversa:

$$\text{230V AC} \rightarrow \boxed{\text{Raddrizzatore}} \rightarrow \boxed{\text{Filtro}} \rightarrow \boxed{\text{Chopper}} \rightarrow \boxed{\text{Trasformatore HF}} \rightarrow \boxed{\text{Raddrizzatore}} \rightarrow \boxed{\text{Filtro}} \rightarrow \text{DC}$$

1. La tensione di rete (230 V AC, 50 Hz) viene **raddrizzata direttamente** senza trasformatore, ottenendo circa **310 V DC** (tensione di picco)
2. Un circuito **chopper** ("affettatore") trasforma i 310 V DC in una tensione alternata ad **alta frequenza** (20-40 kHz), cioè almeno 400-800 volte superiore ai 50 Hz della rete
3. Questa tensione ad alta frequenza attraversa un **trasformatore** di dimensioni molto ridotte
4. In uscita dal trasformatore, la tensione viene nuovamente raddrizzata e filtrata

#### 🔹 Il Segreto: il Trasformatore ad Alta Frequenza

Il vantaggio fondamentale sta nella fisica dell'induzione elettromagnetica: l'energia trasferita per induzione **cresce con la frequenza**. Ricordando le esperienze di Faraday, più rapidamente si varia il flusso magnetico, più energia viene indotta. Un trasformatore che lavora a 20-40 kHz è enormemente più efficiente di uno a 50 Hz.

> **Dato pratico**: un trasformatore switching per 250 W pesa circa **100 grammi** con nucleo in ferrite, contro i **2-3 kg** di un trasformatore lineare equivalente a 50 Hz. Le dimensioni si riducono di circa **un decimo**.

#### 🔹 Stabilizzazione negli Switching

La stabilizzazione avviene tramite retroazione sul **duty cycle** del chopper (la larghezza delle "fette" di tensione). Il circuito di controllo misura la tensione di uscita e regola per quanto tempo il chopper conduce in ogni ciclo: fette più larghe = più energia trasferita = tensione più alta.

La separazione galvanica nel circuito di retroazione è garantita da un **optoisolatore** (optocoupler): un componente che contiene un LED e un **fototransistor** separati otticamente. Il segnale di controllo viene trasmesso tramite **luce**, mantenendo l'isolamento elettrico tra la parte collegata alla rete e la parte sicura.

#### 🔹 Sicurezza negli Alimentatori Switching

> ⚠️ **ATTENZIONE**: negli alimentatori switching, una parte consistente del circuito è collegata **direttamente alla rete 220 V senza isolamento galvanico**. L'isolamento è garantito solo dal trasformatore HF e dall'optoisolatore. **Non aprire mai un alimentatore switching acceso**; anche da spento, il condensatore di filtro può mantenere cariche a 310 V.

Negli alimentatori lineari invece, grazie al trasformatore in ingresso, tutta la parte a valle è sicura e si può intervenire senza pericolo (a alimentatore spento).

#### 🔹 Confronto Lineari vs Switching

| Caratteristica        | Alimentatore Lineare                             | Alimentatore Switching              |
| --------------------- | ------------------------------------------------ | ----------------------------------- |
| **Peso**              | Pesante (2-3 kg solo il trasformatore per 250 W) | Leggero (1,5-2 kg totali per 250 W) |
| **Dimensioni**        | Ingombrante                                      | Compatto                            |
| **Costo**             | Più costoso                                      | Più economico                       |
| **Rendimento**        | Più basso (più calore da dissipare)              | 70-90%                              |
| **Dissipatori**       | Grandi alette di alluminio                       | Molto ridotte                       |
| **Rumore RF**         | Praticamente assente                             | Può generare interferenze           |
| **Sicurezza interna** | Facile da manipolare                             | Pericoloso (alta tensione interna)  |

#### 🔹 Il Problema delle Interferenze RF

Il principale difetto degli alimentatori switching è che il chopper interno è un **generatore di interferenze** naturale. Se l'alimentatore non è ben schermato, può disturbare i ricevitori radio. Il problema è più evidente negli alimentatori economici (spesso di produzione cinese) che risparmiano sulle schermature.

Alcuni alimentatori economici hanno un potenziometro etichettato "**noise offset**" che permette di spostare la frequenza dell'oscillatore del chopper per allontanare le armoniche dalla banda radio in uso. Questa soluzione **non risolve il problema** ma lo sposta: l'interferenza può scomparire su una frequenza ma apparire su un'altra.

> **Consiglio pratico**: le fonti di interferenza in una stazione radio possono provenire non solo dall'alimentatore della radio ma da qualsiasi dispositivo switching della casa: alimentatori di telefoni, ripetitori Wi-Fi, strisce LED, plafoniere LED. Il metodo efficace è identificarle una per una, spegnendo i dispositivi e verificando la riduzione del rumore. Possibili soluzioni: filtri di rete in ingresso agli alimentatori, nuclei di ferrite sui cavi, filtri recuperati da vecchi alimentatori ATX per PC.

---

## 🔗 Concept Map (testuale)

- **Semiconduttore** (silicio) → con drogaggio diventa → **tipo P** (lacune) o **tipo N** (elettroni liberi)
- **Giunzione P-N** → crea → **regione di svuotamento** (isolante naturale)
- **Polarizzazione diretta** → riduce la regione di svuotamento → **diodo conduce** (sopra 0,7 V)
- **Polarizzazione inversa** → allarga la regione di svuotamento → **diodo non conduce**
- **Diodo raddrizzatore** → è usato in → **raddrizzatore** (stadio dell'alimentatore)
- **Diodo Zener** → è usato in → **stabilizzatore** (stadio dell'alimentatore)
- **Diodo Varicap** → si comporta come → **condensatore variabile** (per accordo elettronico)
- **Diodo Schottky** → è adatto a → **alte frequenze** (UHF, SHF)
- **Alimentatore lineare** → schema: Trasformatore → Raddrizzatore → Filtro → Stabilizzatore
- **Trasformatore** → realizza → **isolamento galvanico** (sicurezza elettrica)
- **Condensatore elettrolitico** → realizza → **livellamento** della tensione pulsante
- **Amplificatore di errore** → confronta tensione uscita con riferimento → **retroazione** → stabilizzazione
- **Alimentatore switching** → usa → **chopper** ad alta frequenza → trasformatore piccolo e leggero
- **Chopper** → genera → **interferenze RF** (difetto principale degli switching)
- **Optoisolatore** → realizza → **isolamento galvanico** nel circuito di retroazione degli switching

---

## 📝 Key Takeaways

1. Il **diodo** è un componente a semiconduttore che consente il passaggio di corrente in una sola direzione: dall'anodo al catodo quando è in polarizzazione diretta (soglia ~0,7 V per il silicio).

2. I **cinque tipi di diodi** da conoscere per l'esame sono: raddrizzatore (AC→DC), LED (emette luce), Zener (stabilizza tensione in polarizzazione inversa), Varicap (condensatore variabile), Schottky (alte frequenze, giunzione metallo-semiconduttore).

3. Un **alimentatore lineare** è composto da quattro stadi in serie: trasformatore (abbassa tensione + isolamento galvanico), raddrizzatore (AC→DC pulsante), filtro di livellamento (condensatore elettrolitico), stabilizzatore (tensione costante e precisa).

4. L'**isolamento galvanico** è fondamentale per la sicurezza: il trasformatore impedisce il contatto elettrico diretto tra la rete 220 V e l'utilizzatore, trasferendo energia solo tramite campi magnetici.

5. Il **raddrizzatore a doppia semionda** (ponte di Graetz con 4 diodi) produce una tensione pulsante a frequenza doppia (100 Hz) rispetto all'ingresso, risultando più efficiente del raddrizzamento a singola semionda.

6. La **stabilizzazione a retroazione** è il metodo più diffuso: un amplificatore di errore confronta la tensione di uscita con un riferimento Zener e corregge automaticamente le variazioni tramite un anello di controllo.

7. Gli **alimentatori switching** sono più leggeri, compatti, economici e efficienti (70-90%) grazie al trasformatore ad alta frequenza (20-40 kHz), ma possono generare **interferenze RF** che disturbano i ricevitori radio.

8. Negli alimentatori switching, una parte del circuito è collegata direttamente alla rete 220 V senza isolamento galvanico: sono **potenzialmente pericolosi** da aprire e manipolare, a differenza dei lineari.

9. La **patente di radioamatore non scade mai**; l'autorizzazione generale scade ogni 10 anni. Questo concetto è ricorrente nelle domande d'esame.

10. Le **interferenze RF** in una stazione radio possono provenire da qualsiasi alimentatore switching presente in casa (Wi-Fi, LED, caricabatterie), non solo da quello della radio. La soluzione è identificarle una per una e applicare filtri di rete o nuclei di ferrite.

---

## ❓ Comprehension Questions

1. Perché un semiconduttore come il silicio ha bisogno del processo di drogaggio per diventare utile nell'elettronica? Cosa cambia tra il drogaggio di tipo P e quello di tipo N?

2. Spiega perché il diodo conduce solo in polarizzazione diretta, facendo riferimento al comportamento della regione di svuotamento.

3. Un diodo Zener e un diodo Varicap funzionano entrambi in polarizzazione inversa, ma svolgono funzioni completamente diverse. Quali sono queste funzioni e in quali contesti applicativi vengono impiegati?

4. Perché il raddrizzatore a doppia semionda produce un risultato migliore di quello a singola semionda per alimentare un'apparecchiatura elettronica? Quali sono le implicazioni sulla frequenza del segnale in uscita?

5. Descrivi il percorso completo attraverso cui la tensione di rete (220 V AC) diventa 12 V DC stabili in un alimentatore lineare, indicando la funzione di ciascuno stadio.

6. Perché l'isolamento galvanico è così importante per la sicurezza? Cosa potrebbe accadere a un operatore se un dispositivo fosse collegato direttamente alla rete senza trasformatore?

7. Nel circuito di stabilizzazione a retroazione, come reagisce il sistema quando la tensione di uscita cala a causa di un aumento del carico? Descrivi il meccanismo dell'anello di controllo.

8. Perché il trasformatore di un alimentatore switching può essere così piccolo e leggero rispetto a quello di un alimentatore lineare? Quale principio fisico viene sfruttato?

9. In che modo un alimentatore switching può disturbare la ricezione radio? Perché il potenziometro "noise offset" non è una vera soluzione al problema?

10. Se dovessi scegliere un alimentatore per la tua stazione radioamatoriale, quali fattori considereresti nella scelta tra un lineare e uno switching? Qual è il compromesso principale?

---

## 📚 Glossary

- **Alimentatore a commutazione (switching)** — Alimentatore che converte la tensione di rete in DC tramite un chopper ad alta frequenza e un trasformatore HF, risultando leggero e compatto ma potenzialmente rumoroso in RF.
- **Alimentatore lineare** — Alimentatore che usa un trasformatore a 50 Hz, un raddrizzatore, un filtro capacitivo e uno stabilizzatore per produrre tensione continua stabile. Pesante ma privo di interferenze RF.
- **Amplificatore di errore** — Circuito che confronta la tensione di uscita con una tensione di riferimento per generare un segnale di correzione nel loop di retroazione.
- **Anodo** — Terminale positivo del diodo, da cui la corrente convenzionale entra nel componente.
- **Catodo** — Terminale negativo del diodo, da cui la corrente convenzionale esce; contrassegnato da una banda sul corpo del componente.
- **Chopper** — Circuito che "affetta" una tensione continua trasformandola in alternata ad alta frequenza (20-40 kHz) negli alimentatori switching.
- **Diodo** — Componente a semiconduttore con due terminali che consente il passaggio di corrente in una sola direzione.
- **Diodo LED** — Diodo a emissione luminosa che emette fotoni quando è in polarizzazione diretta.
- **Diodo raddrizzatore** — Diodo utilizzato per convertire tensione alternata in tensione continua pulsante.
- **Diodo Schottky (Hot Carrier)** — Diodo con giunzione metallo-semiconduttore, adatto ad alte frequenze (UHF/SHF).
- **Diodo Varicap** — Diodo che in polarizzazione inversa si comporta come un condensatore variabile, usato per l'accordo elettronico dei circuiti risonanti.
- **Diodo Zener** — Diodo progettato per operare in polarizzazione inversa a una tensione costante (tensione di Zener), usato come stabilizzatore di tensione.
- **Drogaggio (doping)** — Processo di inserimento controllato di impurità in un semiconduttore per modificarne le proprietà elettriche.
- **Duty cycle** — Rapporto tra il tempo di conduzione e il periodo totale di un segnale pulsato; negli switching regola la tensione di uscita.
- **Filtro di livellamento** — Stadio dell'alimentatore che usa condensatori elettrolitici per trasformare la tensione pulsante in tensione quasi costante.
- **Giunzione P-N** — Interfaccia tra una regione drogata P e una regione drogata N di un semiconduttore; è la struttura fondamentale del diodo.
- **Isolamento galvanico** — Separazione elettrica completa tra due circuiti che impedisce il passaggio di corrente tra essi, fondamentale per la sicurezza elettrica.
- **Optoisolatore (optocoupler)** — Componente che trasmette un segnale elettrico tramite luce (LED + fototransistor), realizzando l'isolamento galvanico.
- **Polarizzazione diretta** — Condizione in cui si applica tensione positiva all'anodo rispetto al catodo, permettendo la conduzione del diodo.
- **Polarizzazione inversa** — Condizione in cui si applica tensione positiva al catodo rispetto all'anodo, bloccando la conduzione del diodo.
- **Ponte di Graetz** — Configurazione a ponte con quattro diodi per il raddrizzamento a doppia semionda, la più comune negli alimentatori.
- **Raddrizzatore** — Circuito che converte tensione alternata in tensione continua pulsante mediante diodi.
- **Regione di svuotamento (depletion region)** — Zona priva di portatori di carica all'interfaccia della giunzione P-N, che agisce come isolante.
- **Retroazione (feedback)** — Principio di controllo in cui una parte del segnale di uscita viene riportata all'ingresso per correggere automaticamente le variazioni.
- **Semiconduttore** — Materiale con resistività intermedia tra conduttori e isolanti (es. silicio, germanio), base dell'elettronica moderna.
- **Stabilizzatore** — Stadio finale dell'alimentatore che regola la tensione di uscita al valore preciso desiderato.
- **Tensione di soglia** — Tensione minima necessaria per portare un diodo in conduzione (~0,7 V per il silicio, ~0,3 V per il germanio).
- **Tensione pulsante** — Tensione continua che varia periodicamente in ampiezza ma mantiene sempre la stessa polarità.
- **Trasformatore** — Componente che trasferisce energia elettrica tra due circuiti tramite induzione magnetica, modificando il rapporto di tensione e realizzando l'isolamento galvanico.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore principale**: Paolo (radiotecnica — diodi e alimentatori)
- 👨‍🏫 **Relatore**: Silvio IZ5DIY (correzione quiz e coordinamento)
- 👨‍🏫 **Coordinamento**: Fabrizio (organizzazione lezione in presenza)
- 🎓 **Partecipanti**: Aspiranti radioamatori del corso ARI Toscana CRT 2025 (Marco, Maurizio, Claudio, Andrea, Leonardo e altri)

---

## ⏱️ Evidenze Temporali

| Intervallo      | Argomento                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------- |
| 00:02 - 08:30   | Correzione quiz Lezione 10 e annuncio lezione in presenza                                         |
| 09:00 - 28:00   | Introduzione al diodo: semiconduttori, drogaggio P-N, giunzione, polarizzazione diretta e inversa |
| 28:00 - 53:00   | I cinque tipi di diodi: raddrizzatore, LED, Zener, Varicap, Schottky                              |
| 53:00 - 63:00   | Domande e transizione agli alimentatori                                                           |
| 63:00 - 72:30   | Alimentatori lineari: trasformatore e isolamento galvanico                                        |
| 72:30 - 84:00   | Raddrizzatore: singola semionda, doppia semionda, ponte di Graetz                                 |
| 84:00 - 90:00   | Filtro di livellamento con condensatori elettrolitici                                             |
| 90:00 - 98:00   | Stabilizzatore: Zener e circuito a retroazione, domande su trimmer                                |
| 99:30 - 112:00  | Alimentatori a commutazione (switching): funzionamento, vantaggi, sicurezza                       |
| 112:00 - 126:00 | Confronto lineari vs switching, discussione interferenze RF e soluzioni pratiche                  |

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Numero lezione**   | 11                                                                                                                                                                                                                                                                  |
| **Data**             | 21 maggio 2025                                                                                                                                                                                                                                                      |
| **Durata**           | ~2 ore e 10 minuti                                                                                                                                                                                                                                                  |
| **Numero argomenti** | 5 (Quiz, Diodi, Alimentatori lineari, Alimentatori switching, Interferenze RF)                                                                                                                                                                                      |
| **Parole chiave**    | Diodo, semiconduttore, giunzione P-N, polarizzazione, Zener, Varicap, Schottky, LED, alimentatore lineare, alimentatore switching, raddrizzatore, ponte di Graetz, filtro capacitivo, stabilizzatore, isolamento galvanico, chopper, optoisolatore, interferenze RF |
