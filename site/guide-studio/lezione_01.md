---
layout: default
---

# 📘 Lezione 01 - Introduzione al Corso

## 📌 Overview

- **Materia e argomento**: Elettrotecnica di base — corrente continua. Vengono introdotti i concetti fondamentali di tensione, corrente, potenza, energia, i generatori di corrente continua e gli effetti della corrente elettrica.
- **Tempo di studio stimato**: 90–120 minuti
- **Prerequisiti**: Nessuno. Il corso è pensato per tutti e non richiede titoli di studio particolari né conoscenze pregresse di elettronica o matematica.
- **Obiettivi di apprendimento**:
  - Comprendere la struttura dell'atomo e il ruolo degli elettroni nei fenomeni elettrici
  - Distinguere materiali conduttori e isolanti
  - Definire e saper utilizzare le grandezze elettriche fondamentali: carica (coulomb), corrente (ampere), tensione (volt), potenza (watt), energia (wattora)
  - Applicare la formula $P = V \times I$ e le sue inverse
  - Conoscere i tre tipi di generatori: pile, batterie/accumulatori, alternatori
  - Comprendere il collegamento in serie e in parallelo dei generatori
  - Riconoscere i quattro effetti della corrente elettrica: fisiologico, termico, chimico, magnetico

---

## 📖 Core Content

## 🔬 1. Struttura dell'atomo e cariche elettriche (⏱ 03:10)

### 🔹 L'atomo e le sue particelle

L'**atomo** — la particella più piccola che mantiene le caratteristiche della materia a cui appartiene — è il punto di partenza per comprendere tutti i fenomeni elettrici. Un atomo di oro, per esempio, possiede tutte le caratteristiche dell'oro, anche se è una singola particella.

L'atomo è composto da tre tipi di particelle. Al centro si trova il **nucleo**, paragonabile al Sole nel sistema solare, che contiene due tipi di particelle: i **neutroni** — particelle elettricamente neutre che contribuiscono alla massa dell'atomo ma non alla carica elettrica — e i **protoni** — particelle dotate di carica elettrica convenzionalmente definita **positiva**. Attorno al nucleo, come pianeti attorno al Sole, orbitano gli **elettroni** — particelle portatrici di carica elettrica convenzionalmente definita **negativa**.

In condizioni normali, ogni atomo è **elettricamente neutro**: il numero di protoni è uguale al numero di elettroni, e le rispettive cariche si bilanciano esattamente. Quando un atomo cede o acquista elettroni, diventa uno **ione**: se perde un elettrone diventa uno **ione positivo** (avendo perso una carica negativa, resta con un eccesso di carica positiva); se ne acquista uno, diventa uno **ione negativo**.

### 🔹 Conduttori e isolanti (⏱ 05:51)

Non tutti i materiali si comportano allo stesso modo rispetto agli elettroni. Esistono materiali in cui gli elettroni sono **fortemente vincolati** all'atomo: anche applicando energia, è molto difficile estrarre un elettrone. Questi sono i **materiali isolanti** — ad esempio plastica, gomma, ceramica, aria.

Vi sono invece altri materiali, tipicamente i **metalli** (oro, argento, rame, alluminio, ferro), dove gli elettroni non sono agganciati saldamente al nucleo e con poca energia possono essere estratti e messi in movimento. Questi sono i **materiali conduttori**, fondamentali per la corrente elettrica. Tra i migliori conduttori troviamo oro e argento; il rame conduce bene ed è il materiale più usato per i cavi elettrici; il ferro conduce un po' meno bene, ma resta comunque un buon conduttore.

> "L'acqua di per sé è isolante. L'acqua conduce se ci sono degli additivi, ad esempio il sale."

---

## ⚡ 2. La carica elettrica e il coulomb (⏱ 08:51)

### 🔹 Definizione di carica elettrica

Se da un materiale conduttore si riesce a estrarre un certo numero di elettroni, si costituisce una **carica elettrica**. La carica elettrica negativa non è altro che un insieme di elettroni; la carica elettrica positiva "pura" non esiste in natura — è in realtà uno **ione**, ovvero un atomo che ha perso un elettrone (i protoni sono molto difficili da sganciarsi dal nucleo, richiederebbero energie elevatissime).

L'unità di misura della carica elettrica è il **coulomb** (simbolo: **C**). Un coulomb corrisponde a circa $6{,}25 \times 10^{18}$ elettroni, ovvero 6,25 miliardi di miliardi di elettroni.

> **Formula fondamentale:**
>
> $$1 \text{ C} = 6{,}25 \times 10^{18} \text{ elettroni}$$

### 🔹 Attrazione e repulsione tra cariche

Le cariche elettriche interagiscono tra loro secondo una legge fondamentale:

- **Cariche uguali si respingono** (positivo–positivo o negativo–negativo)
- **Cariche diverse si attraggono** (positivo–negativo)

Questa proprietà è analoga a quanto accade con le calamite e il magnetismo.

---

## 🧲 3. Il campo elettrico (⏱ 11:26)

### 🔹 Concetto di campo e linee di forza

Ogni carica elettrica genera attorno a sé un **campo elettrico** — una zona di spazio in cui si avvertono gli effetti generati dalla carica stessa. I campi elettrici si rappresentano graficamente mediante le **linee di forza**, che indicano la direzione secondo la quale agiscono le forze di attrazione e repulsione.

Per comprendere le linee di forza, si immagina di posizionare una piccola carica positiva "di prova" in vari punti dello spazio attorno alla carica. Se la carica centrale è positiva, la carica di prova viene respinta radialmente verso l'esterno (le frecce puntano verso l'esterno). Se la carica centrale è negativa, la carica di prova viene attratta verso il centro (le frecce puntano verso l'interno).

Quando sono presenti due cariche, il campo risultante è la combinazione dei campi generati da ciascuna. Ad esempio, due cariche positive generano linee di forza antagoniste, che si respingono a vicenda. Una carica positiva e una negativa generano linee che vanno dalla positiva alla negativa, mostrando l'attrazione reciproca.

Il concetto di campo è fondamentale per il radioamatore: quando si trasmette, l'antenna genera un **campo elettromagnetico**, che verrà studiato in dettaglio nelle lezioni successive.

---

## 🔌 4. La corrente elettrica (⏱ 15:08)

### 🔹 Definizione e natura della corrente

La **corrente elettrica** — spostamento ordinato di cariche elettriche (nel 99,9% dei casi, elettroni) — si genera quando in un punto dello spazio vi è un eccesso di elettroni e in un altro punto una carenza. Se questi due punti sono collegati da un conduttore, gli elettroni fluiscono dalla zona con eccesso (polo negativo) verso la zona con carenza (polo positivo).

### 🔹 Corrente continua vs corrente alternata (⏱ 20:34)

La **corrente continua** (CC o DC) scorre sempre in un solo senso, dal polo negativo al polo positivo. Questo non significa che il suo valore sia costante nel tempo: la corrente può variare in ampiezza, ma non cambia mai direzione. Viene prodotta da pile e batterie.

La **corrente alternata** (CA o AC), che sarà oggetto della lezione 3, scorre a volte in un senso e a volte nell'altro, invertendo periodicamente la direzione.

⚠️ *Attenzione a un errore comune*: "continua" non significa "flusso costante". Significa che il verso della corrente non cambia mai.

### 🔹 L'ampere: unità di misura della corrente (⏱ 24:11)

L'intensità della corrente elettrica si misura in **ampere** (simbolo dell'unità di misura: **A**; simbolo nelle formule: **I**, lettera maiuscola). L'ampere prende il nome dal fisico francese André-Marie Ampère.

> **Definizione:**
>
> $$1 \text{ A} = 1 \text{ C/s}$$
>
> Un ampere corrisponde al passaggio di un
> coulomb di carica al secondo attraverso
> un conduttore.

Se in un filo in un secondo passano $6{,}25 \times 10^{18}$ elettroni, in quel filo scorre una corrente di 1 ampere.

---

## 🔋 5. La tensione e la differenza di potenziale (⏱ 26:06)

### 🔹 Concetto di potenziale e analogia idraulica

La corrente elettrica scorre perché esiste una **differenza di potenziale** tra due punti. Il docente utilizza un'efficace analogia: immaginate due secchi d'acqua, uno pieno e uno quasi vuoto, collegati da un tubo. L'acqua fluisce naturalmente dal secchio più pieno a quello meno pieno, fino a livellare i livelli. Lo stesso accade con le cariche elettriche: gli elettroni si spostano da dove ce ne sono di più a dove ce ne sono di meno, finché non si livellano, oppure continuano a fluire se un generatore mantiene la differenza di potenziale.

La differenza di potenziale, detta comunemente **tensione**, si misura in **volt** (simbolo dell'unità di misura: **V**; simbolo nelle formule: **V**). Prende il nome da Alessandro Volta, il fisico italiano che nel 1799 inventò la pila.

> **Definizione formale:**
>
> 1 volt è la differenza di potenziale tra due
> punti A e B di un circuito tale che per
> trasportare 1 coulomb dal punto A al punto B
> occorre compiere un lavoro di 1 joule.

⚠️ *Nota*: Ai fini dell'esame, tensione e differenza di potenziale possono essere considerati sinonimi, anche se tecnicamente non sono esattamente identici.

---

## ⚙️ 6. Energia e potenza elettrica (⏱ 30:33)

### 🔹 L'energia elettrica

L'**energia** — la capacità di compiere un lavoro — è un concetto che il docente spiega con l'analogia dell'automobile. Il serbatoio di un'auto contiene energia (chimica nella benzina, elettrica nelle auto elettriche). Questa energia viene trasformata dal motore in **energia cinetica** (energia associata al movimento).

Allo stesso modo, in una radio portatile il pacco batterie contiene energia chimica che la radio trasforma in energia del **campo elettromagnetico** irradiato dall'antenna.

L'energia elettrica si misura in **wattora** (simbolo: **Wh**) o **kilowattora** (kWh). È ciò che l'Enel ci fornisce e che i contatori domestici misurano.

> $$1 \text{ Wh} = \text{consumo di 1 watt per 1 ora}$$

### 🔹 La potenza elettrica (⏱ 34:05)

La **potenza** — la quantità di energia che si trasforma nell'unità di tempo — è ciò che determina "quanta" energia viene utilizzata in un dato momento. Tornando all'analogia dell'automobile: premendo poco l'acceleratore si trasforma poca energia (bassa potenza), premendo molto si trasforma molta energia (alta potenza), consumando più benzina.

L'unità di misura della potenza è il **watt** (simbolo dell'unità di misura: **W**; simbolo nelle formule: **P**).

> **Definizione:**
>
> $$1 \text{ W} = 1 \text{ J/s}$$
>
> Un watt corrisponde a un joule di lavoro
> compiuto in un secondo.

**Analogia con la radio**: un palmare radioamatoriale può essere regolato su diverse potenze di uscita (es. 0,5 W, 1 W, 5 W). A 0,5 W preleva poca energia dalla batteria e irradia un campo elettromagnetico debole. A 5 W preleva dieci volte tanta energia e genera un campo dieci volte più intenso.

> **Riepilogo fondamentale per l'esame:**
>
> - L'energia si misura in **wattora** (Wh) o **kilowattora** (kWh)
> - La potenza si misura in **watt** (W)

---

## 📐 7. La formula della potenza e le formule inverse (⏱ 45:33)

### 🔹 Formula principale

La formula fondamentale per il calcolo della potenza elettrica nei circuiti è:

> $$P = V \times I$$
>
> La potenza (P, in watt) è uguale al prodotto
> della tensione (V, in volt) per la corrente
> (I, in ampere).

**Esempio pratico**: una radio alimentata a 12 V che consuma 0,1 A assorbe una potenza di $12 \times 0{,}1 = 1{,}2$ W.

### 🔹 Formule inverse (⏱ 47:25)

Dalla formula principale si ricavano due formule inverse, utili quando i dati a disposizione sono diversi:

> $$I = \frac{P}{V}$$
>
> $$V = \frac{P}{I}$$

Il procedimento matematico è semplice: si divide entrambi i membri dell'equazione per la stessa grandezza. Ad esempio, dividendo $P = V \times I$ per $V$, si ottiene $\frac{P}{V} = I$.

**Esempio pratico — calcolo del fusibile** (⏱ 53:27): una radio da 100 W alimentata a 12 V assorbe una corrente $I = \frac{100}{12} \approx 8{,}3$ A. Si può quindi scegliere un fusibile da 10 A per proteggere il circuito.

**Esempio pratico — calcolo della potenza** (⏱ 52:35): una radio alimentata a 12 V che consuma 10 A assorbe $P = 12 \times 10 = 120$ W.

**Esempio dalla discussione con un corsista** (⏱ 56:28): una radio che eroga 120 W verso l'antenna ne consuma almeno il doppio dall'alimentatore (~250 W). Con alimentatore a 12 V: $I = \frac{250}{12} \approx 20$ A. Ecco perché gli alimentatori radioamatoriali tipici sono da 20–30 ampere.

⚠️ *Consiglio d'esame*: è molto probabile che nelle 30 domande della parte tecnica ci sia almeno una domanda che richiede l'uso di queste formule. È fondamentale memorizzare tutte e tre le versioni.

---

## 🔋 8. I generatori di corrente elettrica (⏱ 61:54)

### 🔹 Le pile (⏱ 62:37)

La **pila** è un generatore in cui la corrente elettrica viene prodotta da una **reazione chimica irreversibile**. All'interno della pila, sostanze chimiche si combinano spostando elettroni verso il polo negativo, lasciando il polo positivo carente di elettroni. Quando la pila è inserita in un circuito, gli elettroni scorrono dal polo negativo al polo positivo attraverso il circuito esterno. Le pile si scaricano e **non possono essere ricaricate**.

Le pile comuni hanno tensione di 1,5 V (stilo) o 9 V (il classico "pacchettino").

### 🔹 Le batterie / accumulatori (⏱ 64:28)

Le **batterie** (o **accumulatori**) funzionano in modo simile alle pile, ma la reazione chimica è **reversibile**: possono essere **ricaricate**. Questo le distingue fondamentalmente dalle pile, anche se commercialmente si trovano "pile ricaricabili" che tecnicamente appartengono alla categoria delle batterie.

Le batterie sono caratterizzate da due valori:

1. **Tensione** di uscita (es. 6 V, 12 V)
2. **Capacità**, espressa in **amperora** (simbolo: **Ah**) — la quantità di energia che contengono

> **Calcolo della durata di una batteria:**
>
> $$t = \frac{C}{I}$$
>
> dove $t$ = tempo in ore, $C$ = capacità in Ah,
> $I$ = corrente assorbita in ampere.

**Esempio**: una batteria da 10 Ah che eroga 2 A si scarica in $\frac{10}{2} = 5$ ore. La stessa batteria con un carico da 0,25 A dura $\frac{10}{0{,}25} = 40$ ore.

Le pile di piccole dimensioni hanno capacità molto inferiore, espressa in **milliamperora** (mAh). Le batterie ricaricabili si sono evolute dal nichel-cadmio (NiCd, con il problema dell'**effetto memoria** — la batteria risente del modo in cui è stata ricaricata in precedenza) agli **ioni di litio** (Li-ion), che nello stesso peso e volume possono contenere fino a 10 volte più energia.

### 🔹 Gli alternatori (⏱ 68:31)

L'**alternatore** è un generatore che produce corrente elettrica tramite il **moto meccanico**, sfruttando l'interazione di due campi magnetici. A differenza di pile e batterie, l'alternatore genera **corrente alternata**.

Nell'automobile, la batteria fornisce energia per l'avviamento, poi l'alternatore — azionato dal motore — mantiene la batteria carica e alimenta l'impianto elettrico. La tensione alternata in uscita dall'alternatore viene **raddrizzata** (trasformata in continua) tramite componenti elettronici chiamati **diodi**. La batteria funge anche da elemento **stabilizzatore** della tensione dell'impianto.

> "Le batterie erogano tensione continua e quindi corrente continua. L'alternatore genera corrente alternata."

---

## 📊 9. Il generatore ideale e collegamenti serie/parallelo (⏱ 75:53)

### 🔹 Generatore ideale

Un **generatore ideale** è un generatore che mantiene la **tensione di uscita costante** al variare della corrente assorbita dal carico. Se genera 12 V, mantiene 12 V sia con 1 A che con 100 A di carico. Il generatore ideale **non esiste** nella realtà: tutti i generatori reali subiscono un leggero calo di tensione quando la corrente assorbita aumenta. È tuttavia un concetto teorico importante e possibile domanda d'esame.

### 🔹 Collegamento in parallelo (⏱ 77:03)

Mettendo generatori **in parallelo** (tutti devono avere la **stessa tensione**):

- La **tensione di uscita** resta **uguale** a quella del singolo generatore
- La **corrente erogabile** è la **somma** delle correnti dei singoli generatori

Esempio: tre batterie da 1,5 V in parallelo erogano 1,5 V, ma con corrente tripla rispetto a una sola batteria.

⚠️ *Attenzione*: non si possono mettere in parallelo generatori con tensioni diverse, pena il rischio di guasto.

### 🔹 Collegamento in serie (⏱ 78:43)

Mettendo generatori **in serie**:

- La **tensione di uscita** è la **somma** delle tensioni dei singoli generatori
- La **corrente erogabile** resta **uguale** a quella del singolo generatore

> $$V_{totale} = V_1 + V_2 + \ldots + V_n$$

Esempio: due batterie da 1,5 V in serie erogano $1{,}5 + 1{,}5 = 3$ V. In pratica si usano generatori uguali per bilanciare lo sforzo.

### 🔹 Riepilogo serie vs parallelo

| Collegamento  | Tensione             | Corrente             |
| ------------- | -------------------- | -------------------- |
| **Serie**     | Somma delle tensioni | Uguale al singolo    |
| **Parallelo** | Uguale al singolo    | Somma delle correnti |

---

## 🛡️ 10. Effetti della corrente elettrica (⏱ 103:01)

### 🔹 Effetto fisiologico

La corrente elettrica attraversa il corpo umano causando la **scossa elettrica**. Il cervello comanda la muscolatura tramite impulsi elettrici dell'ordine dei millesimi di volt. Una corrente esterna di tensione elevata può provocare:

- **Ustioni** se la corrente è elevata
- **Contrazioni muscolari** involontarie, particolarmente pericolose quando coinvolgono il **miocardio** (muscolo cardiaco)
- **Fibrillazione ventricolare** — il cuore può fermarsi
- **Paralisi respiratoria**

Il rischio elettrico sarà approfondito in una lezione dedicata (14ª–15ª lezione).

### 🔹 Effetto termico — Effetto Joule (⏱ 105:17)

La corrente elettrica che scorre in un conduttore lo **scalda** sempre, producendo calore. Questo fenomeno è detto **effetto Joule**. Applicazioni pratiche:

- **Stufette elettriche**: l'energia elettrica si trasforma in energia termica
- **Lampadine a incandescenza** (ormai poco usate per il basso rendimento): un filamento percorso da corrente diventa incandescente ed emette luce

Nella prossima lezione si imparerà a calcolare quanto scalda un conduttore.

### 🔹 Effetto chimico — Elettrolisi (⏱ 107:01)

L'**elettrolisi** si verifica quando la corrente elettrica scorre in un liquido (es. acqua salata). La corrente ha il potere di **scindere le sostanze chimiche**: il sale (cloruro di sodio, NaCl) si divide in ioni sodio (Na⁺) e ioni cloro (Cl⁻), attratti dai rispettivi poli di segno opposto.

⚠️ *Nota per l'esame*: l'effetto chimico non ha applicazione diretta nelle radio, ma il programma richiede che si conosca.

### 🔹 Effetto magnetico (⏱ 108:46)

Un cavo elettrico percorso da corrente **genera un campo magnetico**. Questo fu scoperto da **Hans Christian Ørsted** nel 1800 circa, che notò come un ago di bussola deviasse in prossimità di un filo percorso da corrente. L'effetto magnetico è alla base del funzionamento di componenti elettronici come gli **induttori** (o **bobine**), che saranno oggetto di lezioni future.

---

## 🔗 Concept Map (testuale)

- Atomo → contiene → Protoni (carica +), Neutroni (neutri), Elettroni (carica −)
- Elettroni liberi → costituiscono → Carica elettrica (misurata in coulomb)
- Cariche uguali → si respingono; Cariche diverse → si attraggono
- Carica elettrica → genera → Campo elettrico (rappresentato da linee di forza)
- Differenza di potenziale (volt) → causa → Flusso di elettroni
- Flusso di elettroni → è → Corrente elettrica (misurata in ampere)
- Corrente continua → scorre → sempre nello stesso verso
- Corrente alternata → inverte → periodicamente il verso
- Potenza (watt) → è il prodotto di → Tensione (volt) × Corrente (ampere)
- Energia (wattora) → è → Potenza × Tempo
- Pile → generano corrente tramite → Reazione chimica irreversibile
- Batterie/Accumulatori → generano corrente tramite → Reazione chimica reversibile
- Alternatori → generano corrente tramite → Moto meccanico
- Generatori in serie → aumentano → la tensione totale
- Generatori in parallelo → aumentano → la corrente erogabile
- Generatore ideale → mantiene → tensione costante al variare del carico
- Corrente elettrica → produce → Effetto fisiologico, termico (Joule), chimico (elettrolisi), magnetico

---

## 📝 Key Takeaways

1. **L'atomo** è composto da protoni (carica positiva), neutroni (neutri) ed elettroni (carica negativa). Un atomo neutro ha ugual numero di protoni ed elettroni.

2. **I materiali conduttori** (metalli: rame, oro, argento, alluminio, ferro) permettono il flusso di elettroni; i **materiali isolanti** (plastica, gomma, ceramica, aria) lo impediscono.

3. **Un coulomb** è l'unità di misura della carica elettrica e corrisponde a $6{,}25 \times 10^{18}$ elettroni.

4. **La corrente elettrica** è un flusso ordinato di elettroni, si misura in **ampere** (A), e 1 A = 1 C/s.

5. **La corrente continua** scorre sempre nello stesso verso (dal polo negativo al positivo), ma la sua ampiezza può variare.

6. **La tensione** (differenza di potenziale) si misura in **volt** (V) ed è la causa che fa scorrere la corrente.

7. **La potenza elettrica** si calcola con $P = V \times I$ e si misura in **watt** (W). Le formule inverse sono $I = \frac{P}{V}$ e $V = \frac{P}{I}$.

8. **L'energia** si misura in **wattora** (Wh) o kilowattora (kWh); la potenza indica quanta energia si trasforma per unità di tempo.

9. Le **pile** (non ricaricabili) e le **batterie/accumulatori** (ricaricabili) generano corrente continua; gli **alternatori** generano corrente alternata.

10. La **capacità** di una batteria si esprime in **amperora** (Ah): una batteria da 10 Ah eroga 1 A per 10 ore, oppure 2 A per 5 ore.

11. **Generatori in serie**: la tensione si somma, la corrente resta invariata. **In parallelo**: la corrente si somma, la tensione resta invariata.

12. La corrente elettrica ha quattro effetti: **fisiologico** (scossa, rischio cardiaco), **termico** (effetto Joule), **chimico** (elettrolisi), **magnetico** (generazione di campo magnetico).

---

## ❓ Comprehension Questions

1. Perché la corrente continua viene definita "continua" anche se la sua ampiezza può variare nel tempo? In che modo si distingue dalla corrente alternata?

2. Spiega l'analogia idraulica utilizzata per descrivere la differenza di potenziale. Come si comportano gli elettroni in modo analogo all'acqua tra due recipienti a diverso livello?

3. Una radio portatile da 5 W è alimentata con una batteria da 12 V e 10 Ah. Quanta corrente assorbe la radio? Per quanto tempo la batteria può alimentarla prima di scaricarsi? Giustifica ogni passaggio con le formule appropriate.

4. Perché non è possibile collegare in parallelo generatori con tensioni diverse, mentre è possibile collegarli in serie? Quali grandezze si sommano in ciascun tipo di collegamento?

5. Un radioamatore possiede una radio che eroga 120 W in antenna ma ne consuma circa il doppio dall'alimentatore. Se l'alimentatore fornisce 12 V, perché è consigliabile un alimentatore da almeno 25–30 A anziché uno da 20 A?

6. Qual è la differenza fondamentale tra una pila e un accumulatore? Perché le batterie al litio hanno rappresentato un progresso enorme rispetto a quelle al nichel-cadmio?

7. Descrivi i quattro effetti della corrente elettrica. Quale di questi è alla base del funzionamento delle stufette? E quale è alla base del funzionamento degli induttori?

8. In che modo l'effetto Joule è correlato al funzionamento delle vecchie lampadine a incandescenza? Perché queste lampadine hanno un rendimento basso?

9. Che cos'è un generatore ideale? Perché nella realtà non esiste? Qual è la sua importanza come concetto teorico?

10. Nell'automobile, la batteria e l'alternatore lavorano insieme. Spiega il ruolo di ciascuno e perché l'alternatore deve essere seguito da un circuito raddrizzatore.

---

## 📚 Glossary

- **Accumulatore (batteria)** — Generatore elettrochimico con reazione chimica reversibile, ricaricabile. Caratterizzato da tensione e capacità (Ah).
- **Alternatore** — Generatore di corrente alternata basato sul moto meccanico e l'interazione di campi magnetici.
- **Amperora (Ah)** — Unità di misura della capacità di una batteria. Indica quanta corrente può fornire per quanto tempo prima di scaricarsi.
- **Ampere (A)** — Unità di misura dell'intensità di corrente elettrica. 1 A = 1 C/s.
- **Atomo** — Particella fondamentale della materia, composta da protoni, neutroni ed elettroni.
- **Campo elettrico** — Zona di spazio in cui si avvertono gli effetti di una o più cariche elettriche.
- **Campo elettromagnetico** — Campo generato dall'antenna di una radio durante la trasmissione.
- **Carica elettrica** — Proprietà fondamentale delle particelle subatomiche; si misura in coulomb.
- **Conduttore** — Materiale in cui gli elettroni possono muoversi facilmente (es. rame, oro, argento, alluminio, ferro).
- **Corrente alternata (CA)** — Corrente che inverte periodicamente il verso di scorrimento.
- **Corrente continua (CC)** — Corrente che scorre sempre nello stesso verso, dal polo negativo al positivo.
- **Corrente elettrica** — Spostamento ordinato di cariche elettriche (elettroni).
- **Coulomb (C)** — Unità di misura della carica elettrica. 1 C = $6{,}25 \times 10^{18}$ elettroni.
- **Diodo** — Componente elettronico usato per raddrizzare la corrente alternata in corrente continua.
- **Differenza di potenziale** — Differenza di "livello" elettrico fra due punti; sinonimo pratico di tensione.
- **Effetto Joule** — Riscaldamento di un conduttore causato dal passaggio di corrente elettrica.
- **Elettrolisi** — Scissione di sostanze chimiche in un liquido per effetto della corrente elettrica.
- **Elettrone** — Particella subatomica con carica negativa; il suo movimento costituisce la corrente elettrica.
- **Energia elettrica** — Capacità di compiere un lavoro; si misura in wattora (Wh) o kilowattora (kWh).
- **Fusibile** — Dispositivo di protezione che fonde quando la corrente supera un valore limite.
- **Generatore ideale** — Generatore teorico che mantiene la tensione di uscita costante indipendentemente dalla corrente assorbita.
- **Induttore (bobina)** — Componente elettronico che sfrutta l'effetto magnetico della corrente.
- **Ione** — Atomo che ha perso o acquisito elettroni, diventando carico positivamente o negativamente.
- **Isolante** — Materiale in cui gli elettroni sono fortemente vincolati e non possono muoversi (es. plastica, gomma, ceramica, aria).
- **Joule (J)** — Unità di misura del lavoro e dell'energia.
- **Kilowattora (kWh)** — Unità di misura dell'energia; 1 kWh = 1000 Wh.
- **Linee di forza** — Rappresentazione grafica del campo elettrico che mostra la direzione delle forze.
- **Milliamperora (mAh)** — Sottomultiplo dell'amperora; usato per pile e piccole batterie.
- **Neutrone** — Particella subatomica elettricamente neutra, presente nel nucleo dell'atomo.
- **Nucleo** — Parte centrale dell'atomo, contenente protoni e neutroni.
- **Pila** — Generatore elettrochimico con reazione chimica irreversibile, non ricaricabile.
- **Potenza elettrica (P)** — Quantità di energia trasformata nell'unità di tempo; si misura in watt (W). $P = V \times I$.
- **Protone** — Particella subatomica con carica positiva, presente nel nucleo dell'atomo.
- **Tensione (V)** — Differenza di potenziale fra due punti; si misura in volt (V). È la forza che fa scorrere la corrente.
- **Volt (V)** — Unità di misura della tensione. Prende il nome da Alessandro Volta.
- **Watt (W)** — Unità di misura della potenza. 1 W = 1 J/s.
- **Wattora (Wh)** — Unità di misura dell'energia. 1 Wh = consumo di 1 W per 1 ora.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo — docente del corso, esperto radioamatore

---

## 📅 Informazioni Lezione

- **Numero Lezione**: 01
- **Data**: 05/03/2025
- **Durata**: Circa 2 ore (incluse pause e Q&A)
- **Argomenti Trattati**: 10 (atomo, carica, campo elettrico, corrente, tensione, energia, potenza, formule, generatori, effetti della corrente)
- **Keywords**: corrente continua, tensione, volt, ampere, watt, potenza, energia, coulomb, atomo, elettrone, protone, conduttore, isolante, pila, batteria, accumulatore, alternatore, serie, parallelo, generatore ideale, effetto Joule, elettrolisi, campo magnetico, campo elettrico, formula $P = V \times I$
