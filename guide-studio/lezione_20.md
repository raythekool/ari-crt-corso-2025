# 📘 Lezione 20 - Normative Nazionali

## 📌 Overview

- **Materia**: Antenne — Parte 1: Fondamenti teorici, antenne caricate/multibanda, lobo di radiazione
- **Tempo di studio stimato**: 2 ore
- **Prerequisiti**: Concetti di impedenza, risonanza nei circuiti LC, linee di trasmissione (Lezione 19), propagazione ionosferica (Lezione 18), decibel
- **Obiettivi di apprendimento**:
  - Comprendere il funzionamento dell'antenna come trasduttore
  - Distinguere le regioni di campo vicino e campo lontano
  - Padroneggiare il concetto di resistenza di radiazione e impedenza nel punto di alimentazione
  - Comprendere il funzionamento delle antenne caricate e multibanda (trappole, OCF)
  - Conoscere la formazione e le caratteristiche del lobo di radiazione
  - Comprendere l'effetto del terreno (ground gain) sull'irradiazione e l'impedenza

---

## 📖 Core Content

### 1. 🔍 Correzione quiz e note di servizio (⏱ 00:00–15:08)

La lezione si apre con una nota organizzativa sull'iscrizione all'esame di patente: il Ministero (MIMIT) ha un portale online; servono due marche da bollo e un contributo di 25 €, pagabile con PagoPA.

Segue la correzione del quiz della Lezione 18 (propagazione). La domanda più problematica riguarda il **wattmetro direzionale**:

> Se un wattmetro direzionale indica 90 W di potenza diretta e 10 W di potenza riflessa, qual è la potenza in uscita dal trasmettitore?

La risposta corretta è **90 W**, non 100 W né 80 W. Per definizione, la **potenza diretta** è la potenza in uscita dal trasmettitore verso l'antenna. Gli 80 W sono la potenza effettivamente irradiata dall'antenna (90 − 10 = 80), ma la domanda chiede la potenza in uscita dal trasmettitore, che coincide con la potenza diretta.

> ⚠️ Alcuni database di quiz online riportano erroneamente 80 W come risposta corretta. Inoltre, 100 W è fisicamente impossibile: il trasmettitore non può generare più energia di quella che eroga.

Altra domanda discussa: un cavo coassiale di qualità scadente **dissipa l'energia in calore** al suo interno (effetto Joule), non la riflette verso il trasmettitore.

---

### 2. 📡 L'antenna come trasduttore (⏱ 15:08–19:30)

L'**antenna** è un **trasduttore**: un dispositivo che trasferisce l'energia elettrica ad alta frequenza proveniente dal trasmettitore (attraverso la linea di trasmissione) in un **campo elettromagnetico** che si propaga nello spazio, e viceversa.

Il processo è **completamente reversibile**:

- **In trasmissione**: energia elettrica RF → campo elettromagnetico
- **In ricezione**: campo elettromagnetico → tensione RF ai capi dell'antenna

L'analogia proposta è quella di un **altoparlante/microfono**: trasformano energia elettrica in onde acustiche e viceversa.

Un conduttore percorso da una **corrente variabile** genera al suo intorno un campo elettromagnetico (equazioni di Maxwell). Analogamente, un conduttore immerso in un campo EM è sede di una **corrente indotta** proporzionale all'intensità del campo.

---

### 3. 🔬 Regioni di campo: vicino e lontano (⏱ 19:30–27:10)

Intorno ad un'antenna esistono **tre regioni** distinte:

#### 🔹 1. Regione di campo vicino reattivo

- **Distanza**: pochi decimi di lunghezza d'onda (λ/10 circa)
- Il campo è **puramente reattivo**: non c'è dissipazione di potenza né radiazione. Le correnti servono solo a sostenere i campi (come in un condensatore o un'induttanza).
- L'intensità del campo è molto **fluttuante**

#### 🔹 2. Regione di campo vicino radiativo

- **Distanza**: da circa λ/2 a 1,5λ
- Zona di transizione: il campo comincia a mostrare correlazione tra componente E e H, ma non ha ancora le caratteristiche di un'onda piana
- Significative fluttuazioni nel livello del campo

#### 🔹 3. Regione di campo lontano (radiativo)

- **Distanza**: oltre 1,5λ fino all'infinito
- L'antenna può essere considerata una **sorgente puntiforme**
- Il campo assume le caratteristiche di un'**onda piana** che si propaga linearmente
- L'intensità degrada gradualmente con la distanza
- **Tutte le misure e i dati delle antenne si riferiscono a questa regione**

> Questa classificazione, pur non essendo materia d'esame, è fondamentale per comprendere il comportamento reale delle antenne e i fenomeni di accoppiamento nelle antenne direttive.

---

### 4. ⚡ Risonanza e analogia con le linee di trasmissione (⏱ 27:10–30:10)

Un'antenna (tipicamente un dipolo) è assimilabile a un **circuito risonante serie** (L, C, R) dove:

- **L** e **C** dipendono dalle dimensioni fisiche dell'elemento radiante
- **R** (in assenza di perdite) coincide con la **resistenza di radiazione**

L'analogia con le linee di trasmissione è diretta: un **tronco di linea lungo λ/4 aperto** all'estremità si comporta come un circuito risonante serie. "Aprendo" i due conduttori della linea fino a farli diventare allineati si ottiene un **dipolo a mezza lunghezza d'onda**.

**Alla risonanza**:

- La **corrente è massima** e la **tensione è minima** nel punto di alimentazione (al centro)
- Agli estremi: corrente zero, tensione massima
- L'impedenza nel punto di alimentazione è **puramente resistiva**

Valori di impedenza alla risonanza:

- **Dipolo aperto λ/2**: **73 Ω** (alimentato al centro)
- **Dipolo ripiegato (folded)**: **300 Ω**

---

### 5. 📐 Resistenza di radiazione (⏱ 30:10–39:00)

La **resistenza di radiazione** è definita come:

$$R_{rad} = \frac{P_{irradiata}}{I^2}$$

dove $P_{irradiata}$ è la potenza irradiata dall'antenna e $I$ è la corrente che la percorre.

> ⚠️ La resistenza di radiazione **non è una resistenza fisica** misurabile con un tester. Non dipende dalle caratteristiche elettriche dei materiali, ma rappresenta la **capacità dell'antenna di irradiare energia**.

**Relazione fondamentale**: la potenza irradiata è proporzionale alle **dimensioni** dell'antenna e alla **corrente** che la percorre, e inversamente proporzionale al quadrato della lunghezza d'onda:

$$P_{irr} \propto \frac{L \times I^2}{\lambda^2}$$

**Conseguenza cruciale**: a parità di potenza irradiata, un'antenna di **dimensioni minori** deve essere percorsa da una **corrente maggiore** → la resistenza di radiazione deve essere **minore**.

La resistenza di radiazione **diminuisce drasticamente** con il diminuire delle dimensioni:

- **Verticale λ/4 full-size**: R_rad = **36 Ω**
- **Verticale 0,125λ caricata in testa**: R_rad ≈ **20 Ω**
- **Verticale 0,125λ caricata alla base**: R_rad ≈ **7 Ω**

Antenne con dimensioni inferiori a circa **1/10 di lunghezza d'onda** hanno una resistenza di radiazione così bassa da renderle praticamente **inutilizzabili** per la bassissima efficienza.

> Questo dato smentisce le pubblicità di "antenne miracolose" di dimensioni minime.

---

### 6. 🔄 Resistenza di radiazione vs impedenza di alimentazione (⏱ 39:00–43:00)

I due concetti sono correlati ma **non identici**:

- **Resistenza di radiazione**: rapporto tra potenza irradiata e corrente² — è una proprietà intrinseca dell'antenna
- **Impedenza nel punto di alimentazione**: rapporto V/I nel punto specifico dove si collega il cavo — dipende dalla **posizione** del punto di alimentazione

**Esempio**: un dipolo OCF (Off Center Feed), alimentato a 1/3 della lunghezza, presenta un'impedenza di circa **200 Ω** nel punto di alimentazione, molto diversa dai 73 Ω al centro.

Le due grandezze coincidono **solo** quando:

1. L'antenna è **alla risonanza**
2. Il punto di alimentazione è nel **punto di massima corrente**
3. L'antenna è **priva di perdite** (caso teorico)

---

### 7. 📏 Dimensioni, frequenza di risonanza e fattore di velocità (⏱ 43:00–48:00)

Essendo un circuito risonante serie, l'antenna ha efficienza massima alla **risonanza**, dove l'impedenza è puramente resistiva e la corrente è massima.

> ⚠️ **Domanda d'esame!** Aumentando la lunghezza dell'elemento radiante, la frequenza di risonanza **diminuisce**. Accorciandolo, la frequenza di risonanza **aumenta**.

**Formule teoriche**:

$$L_{dipolo} = \frac{150}{f_{(MHz)}} \quad [\text{m}]$$

$$L_{verticale} = \frac{75}{f_{(MHz)}} \quad [\text{m}]$$

**Formule reali** (con fattore di velocità):

$$L_{reale} = L_{teorica} \times FV$$

Il **fattore di velocità (FV)** tiene conto del materiale e del **rapporto di finezza** (rapporto lunghezza/diametro dell'elemento). Valori tipici: **0,95–0,98**.

Un filo sottile avrà una lunghezza diversa rispetto a un tubo di diametro maggiore per la stessa frequenza di risonanza.

---

### 8. ⚙️ Comportamento fuori risonanza e antenne caricate (⏱ 48:00–55:30)

Fuori dalla frequenza di risonanza, l'impedenza dell'antenna presenta componenti **reattive**:

- **Sotto la risonanza** → componente **capacitiva**
- **Sopra la risonanza** → componente **induttiva**

Anche la componente resistiva varia: aumenta per frequenze superiori e diminuisce per frequenze inferiori.

**Antenne caricate** — Per ridurre le dimensioni dell'antenna mantenendo la risonanza sulla frequenza desiderata:

1. **Bobina di carico (induttiva)**: compensa il comportamento capacitivo dell'elemento accorciato. La posizione della bobina è cruciale: è preferibile porla **il più lontano possibile dal punto di alimentazione** (verso gli estremi), perché la zona centrale è quella dove le correnti sono massime e la radiazione è maggiore.
2. **Carico capacitivo in testa (cappello capacitivo)**: da preferire alla bobina alla base, perché garantisce maggiore efficienza.

Lo scotto da pagare: la resistenza di radiazione **diminuisce** e potrebbe essere necessario un **dispositivo di adattamento** (ad esempio uno **shunt pin**: induttanza in parallelo al punto di alimentazione per adattare impedenze inferiori a quella della linea).

---

### 9. 🔀 Antenne multibanda (⏱ 55:30–65:00)

#### 🔹 Trappole (circuiti risonanti parallelo)

Una **trappola** è un circuito risonante parallelo inserito lungo l'elemento radiante. Alla sua frequenza di risonanza presenta **impedenza infinita**, isolando elettricamente il resto dell'antenna. Su altre frequenze, l'impedenza residua della trappola si combina con il resto dell'elemento per creare una seconda risonanza.

Si possono inserire più trappole in serie per ottenere antenne funzionanti su 2, 3 o anche 4 bande. Sulla frequenza più alta l'antenna è full-size; sulle frequenze inferiori si comporta come un'antenna **caricata**.

#### 🔹 Risonanza in armonica

Un dipolo risuona non solo sulla frequenza fondamentale ma anche sui suoi **multipli dispari** (3ª, 5ª, 7ª armonica). Questo perché l'andamento di tensione e corrente si ripete ogni multiplo dispari di λ/2, mantenendo gli stessi valori nel punto di alimentazione.

#### 🔹 Dipolo OCF (Off Center Feed)

Il dipolo OCF è alimentato a **1/3 della lunghezza** totale, con un braccio di 1/3λ e uno di 2/3λ. L'impedenza in questo punto è circa **200 Ω** (si usa un trasformatore 4:1 a larga banda per adattare a 50 Ω).

La caratteristica unica dell'OCF è che, per la relazione armonica e la distribuzione delle correnti, il valore di impedenza resta **sostanzialmente costante** su molte bande: 80 m, 40 m, 20 m, 17 m, 12 m, 10 m. Mancano i **30 m e i 15 m** perché non presentano lo stesso valore di corrente in quel punto.

---

### 10. 📊 Il lobo di radiazione (⏱ 65:00–77:50)

#### 🔹 Antenna isotropica (riferimento teorico)

L'**antenna isotropica** è un'antenna teorica che emette con uguale intensità in tutte le direzioni. Non esiste nella realtà ma serve come **riferimento** per misurare il guadagno delle antenne reali.

> ⚠️ **Domanda d'esame!** L'antenna isotropica è un'antenna teorica con campo uniforme in tutte le direzioni, usata come riferimento per il guadagno.

**Spazio libero** — Ambiente teorico in cui l'antenna non ha alcuna influenza elettromagnetica da oggetti circostanti (nemmeno il terreno). Nella realtà non esiste mai.

> I dati di guadagno e lobo di radiazione forniti dai produttori sono sempre riferiti al **radiatore isotropico** e allo **spazio libero**.

#### 🔹 Lobo di radiazione del dipolo

Anche nello spazio libero, il dipolo non irradia uniformemente. Il suo lobo è un **toroide**: l'intensità è **massima sul piano perpendicolare all'asse** del dipolo e **nulla lungo l'asse**.

Il dipolo ha un guadagno massimo di **2,1 dBi** (decibel rispetto all'antenna isotropica) nello spazio libero.

> ⚠️ **Domanda d'esame!** Il guadagno di un dipolo nello spazio libero è **2,1 dBi**. La "i" sta per "isotropico".

#### 🔹 Rappresentazione del lobo

Il lobo tridimensionale viene rappresentato in sezione:

- **Lobo orizzontale**: sezione sul piano orizzontale (mostra la direttività azimutale)
- **Lobo verticale**: sezione sul piano verticale (mostra gli angoli di radiazione)

---

### 11. 🌍 Effetto del terreno: ground gain (⏱ 77:50–92:00)

Nella realtà, un corrispondente lontano riceve sempre la **composizione** di almeno due fasci:

1. **Fascio diretto** dall'antenna
2. **Fascio riflesso** dal terreno

La differenza di percorso tra i due fasci dipende da:

- **Altezza da terra dell'antenna (H)**
- **Angolo di radiazione (β)**

I due fasci possono **sommarsi** (fino a +6 dB) o **sottrarsi** (fino a −20 dB o più) a seconda della fase relativa.

#### 🔹 Polarizzazione orizzontale

Nella riflessione a terra si ha un'**inversione di fase**. Le componenti si sommano quando la differenza di percorso è pari a λ/2. L'angolo di massima radiazione è:

$$\beta_{max} = f(H, \lambda)$$

**Regola fondamentale**: più l'antenna è **alta**, più basso è l'angolo di massima radiazione → più favorevole per la propagazione a lunga distanza (DX).

Il lobo di radiazione si modifica **significativamente** con l'altezza da terra:

- Da λ/8 a 2λ le forme dei lobi sono completamente diverse
- Sotto **0,2λ** da terra, le perdite del terreno diventano significative e l'efficienza crolla rapidamente (la resistenza di radiazione va verso zero)

**Implicazione pratica**: un dipolo degli 80 m (λ = 80 m) sotto 16 m di altezza (cioè 0,2λ) comincia a soffrire di perdite significative.

> Paolo sottolinea che il comportamento dell'antenna dipende per l'**80% da dove la si installa**, non dal tipo di antenna. L'angolo di radiazione è determinato principalmente dall'altezza da terra, non dalle caratteristiche intrinseche dell'antenna.

#### 🔹 Polarizzazione verticale

A differenza della polarizzazione orizzontale:

- **Non c'è inversione di fase** nella riflessione a terra
- Il lobo ha un angolo di radiazione **naturalmente basso** anche con antenna vicino a terra
- L'irradiazione è **uniforme** sul piano orizzontale
- La radiazione è **pressoché nulla** per angoli > 50–60°

**Svantaggio**: l'efficienza dipende fortemente dalle **caratteristiche elettriche del terreno**:

- Acqua salata → coefficiente di riflessione elevato → ottima efficienza
- Terreno buono → discreta efficienza
- Area urbana/terreno scarso → efficienza significativamente ridotta

#### 🔹 Antenna immagine

Il fascio riflesso dal terreno è equivalente a quello che sarebbe generato da un'**antenna immagine** posta simmetricamente sotto il piano di terra. Questo concetto è alla base del funzionamento delle antenne direttive (argomento della lezione successiva).

---

## 🔗 Concept Map (testuale)

- **Antenna** → è un → **trasduttore** (energia RF ↔ campo EM)
- **Antenna** → si comporta come un → **circuito risonante serie** (L, C, R)
- **Frequenza di risonanza** → dipende da → **dimensioni fisiche** dell'elemento radiante
- **Aumentare lunghezza** → causa → **diminuzione** della frequenza di risonanza
- **Resistenza di radiazione** → dipende da → **dimensioni** dell'antenna (più piccola → R_rad minore)
- **Resistenza di radiazione** ≠ **impedenza nel punto di alimentazione** (coincidono solo in condizioni ideali)
- **Antenna caricata** → usa → **bobina di carico** o **cappello capacitivo** per ridurre le dimensioni
- **Bobina di carico** → è preferibile → **lontano dal punto di alimentazione** (verso gli estremi)
- **Trappola** → è un → **circuito risonante parallelo** → impedenza infinita alla risonanza → isola elettricamente parti dell'antenna
- **Dipolo OCF** → alimentato a **1/3** → impedenza ~200 Ω → multibanda senza trappole
- **Dipolo** → risuona sui → **multipli dispari** della frequenza fondamentale
- **Antenna isotropica** → è il → **riferimento teorico** per il guadagno (dBi)
- **Dipolo nello spazio libero** → guadagno = **2,1 dBi** → lobo a toroide
- **Lobo di radiazione** → dipende da → **altezza da terra** dell'antenna (ground gain)
- **Ground gain** → composizione di → **fascio diretto + fascio riflesso** dal terreno
- **Altezza maggiore** → **angolo di radiazione più basso** → migliore per DX
- **Polarizzazione verticale** → lobo naturalmente basso → ma sensibile alle **caratteristiche del terreno**
- **Polarizzazione orizzontale** → lobo dipende molto dall'**altezza** → sotto 0,2λ l'efficienza crolla

---

## 📝 Key Takeaways

1. **L'antenna è un trasduttore reversibile** che converte energia RF in campo EM e viceversa, analogamente a un altoparlante/microfono.

2. **Un dipolo a mezza lunghezza d'onda ha un'impedenza di 73 Ω** al centro alla risonanza. Un dipolo ripiegato ha 300 Ω.

3. **La resistenza di radiazione diminuisce drasticamente** con la riduzione delle dimensioni dell'antenna. Antenne inferiori a λ/10 sono praticamente inutilizzabili.

4. **Aumentando la lunghezza dell'elemento, la frequenza di risonanza diminuisce** (e viceversa). La lunghezza reale è il 95–98% di quella teorica per il fattore di velocità.

5. **Sotto la risonanza l'impedenza è capacitiva, sopra è induttiva**. Le antenne caricate usano bobine per compensare il comportamento capacitivo di elementi accorciati.

6. **La posizione della bobina di carico è cruciale**: meglio verso gli estremi dell'antenna (lontano dal punto di alimentazione) per mantenere massima la radiazione nella zona di corrente elevata.

7. **Il dipolo ha un guadagno di 2,1 dBi** nello spazio libero, con lobo a forma di toroide. L'antenna isotropica (campo uniforme) è il riferimento teorico.

8. **L'altezza da terra determina il lobo di radiazione** più di qualsiasi altra caratteristica dell'antenna. Più alta è l'antenna, più basso è l'angolo di massima radiazione.

9. **Le antenne verticali hanno un lobo naturalmente basso** anche vicino a terra, ma la loro efficienza dipende fortemente dalla conducibilità del terreno.

10. **Sotto 0,2λ di altezza**, un dipolo orizzontale subisce perdite significative per effetto del terreno: la resistenza di radiazione si avvicina allo zero.

---

## ❓ Comprehension Questions

1. Spiegare perché la resistenza di radiazione non è una resistenza fisica misurabile con un tester e come si differenzia dall'impedenza nel punto di alimentazione.

2. Un dipolo per gli 80 m è installato a 10 m di altezza. Calcolarne l'altezza in frazioni di lunghezza d'onda e valutare se l'efficienza ne risente significativamente.

3. Perché la posizione ideale della bobina di carico in un'antenna accorciata è verso gli estremi e non al centro? Collegare la risposta alla distribuzione della corrente lungo l'elemento.

4. Descrivere il meccanismo con cui un dipolo OCF può funzionare su più bande senza trappole. Quali bande HF copre e quali mancano?

5. Un'antenna verticale al suolo presenta un lobo a basso angolo di radiazione anche senza essere sollevata. Spiegare perché, facendo riferimento al diverso comportamento della riflessione a terra rispetto alla polarizzazione orizzontale.

6. Qual è la differenza tra il guadagno in dBi e il guadagno in dBd? Come si converte dall'uno all'altro?

7. Spiegare il concetto di ground gain: come può il terreno aggiungere fino a 6 dB di guadagno al segnale irradiato da un'antenna?

8. Perché le trappole in un'antenna multibanda sono circuiti risonanti parallelo e non serie? Cosa succederebbe con circuiti serie?

---

## 📚 Glossary

- **Antenna immagine** — Antenna virtuale posta simmetricamente sotto il piano di terra, utilizzata per modellare l'effetto della riflessione del terreno.
- **Antenna isotropica** — Antenna teorica che irradia con uguale intensità in tutte le direzioni. Usata come riferimento per il guadagno (dBi).
- **Cappello capacitivo** — Carico capacitivo posto in cima a un'antenna accorciata per compensarne il comportamento reattivo.
- **dBi** — Decibel riferiti all'antenna isotropica. Il dipolo ha 2,1 dBi nello spazio libero.
- **Dipolo OCF (Off Center Feed)** — Dipolo alimentato a 1/3 della lunghezza totale, con impedenza ~200 Ω, funzionante su multiple bande HF.
- **Dipolo ripiegato (folded dipole)** — Dipolo la cui impedenza alla risonanza è circa 300 Ω.
- **Fattore di velocità (FV)** — Fattore correttivo (0,95–0,98) che tiene conto del materiale e del rapporto di finezza, usato per calcolare la lunghezza reale dell'antenna.
- **Ground gain** — Guadagno (o perdita) causato dalla composizione del fascio diretto e del fascio riflesso dal terreno.
- **Lobo di radiazione** — Rappresentazione grafica tridimensionale (o in sezione) dell'intensità del campo emesso da un'antenna nelle varie direzioni.
- **Rapporto di finezza** — Rapporto tra la lunghezza e il diametro dell'elemento radiante, influenza la lunghezza reale dell'antenna.
- **Regione di campo lontano** — Zona oltre 1,5λ dall'antenna dove il campo si comporta come un'onda piana. Le specifiche delle antenne si riferiscono a questa regione.
- **Regione di campo vicino reattivo** — Zona entro pochi decimi di λ dall'antenna, dove il campo è puramente reattivo (nessuna radiazione).
- **Resistenza di radiazione** — Rapporto P_irradiata/I², rappresenta la capacità dell'antenna di irradiare. Non è una resistenza fisica.
- **Shunt pin** — Induttanza posta in parallelo al punto di alimentazione per adattare impedenze inferiori a quella della linea.
- **Spazio libero** — Ambiente teorico senza influenze elettromagnetiche esterne (nemmeno il terreno).
- **Trappola** — Circuito risonante parallelo inserito in un'antenna per isolare elettricamente porzioni dell'elemento a determinate frequenze, permettendo il funzionamento multibanda.
- **Trasduttore** — Dispositivo che converte un tipo di energia in un altro. L'antenna converte energia RF in campo EM e viceversa.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo (radioamatore dal 1977, esperto di propagazione e antenne)
- 🎓 **Coordinatore**: Fabrizio (note di servizio sull'iscrizione all'esame)

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Numero lezione**   | 20                                                                                                                                                                                                                                                                                                                                                            |
| **Data**             | 17/09/2025 (mercoledì)                                                                                                                                                                                                                                                                                                                                        |
| **Durata**           | ~1 ora e 36 minuti                                                                                                                                                                                                                                                                                                                                            |
| **Numero argomenti** | 11                                                                                                                                                                                                                                                                                                                                                            |
| **Parole chiave**    | antenna, trasduttore, campo vicino, campo lontano, risonanza, resistenza di radiazione, impedenza alimentazione, dipolo 73 Ω, fattore di velocità, antenne caricate, bobina di carico, cappello capacitivo, trappola, OCF, multibanda, armoniche dispari, antenna isotropica, lobo di radiazione, dBi, ground gain, altezza da terra, polarizzazione, terreno |
