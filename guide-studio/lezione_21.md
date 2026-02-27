# 📘 Lezione 21 - Normative Internazionali

## 📌 Overview

- **Materia**: Antenne — Parte 2: Antenne direttive, efficienza di radiazione, misure e aspetti pratici
- **Tempo di studio stimato**: 2 ore e 30 minuti
- **Prerequisiti**: Concetti di base sulle antenne (Lezione 20), propagazione ionosferica (Lezione 18), linee di trasmissione, impedenza, ROS, carta di Smith
- **Obiettivi di apprendimento**:
  - Comprendere i principi delle antenne direttive (parabola, Yagi-Uda, array)
  - Padroneggiare i concetti di guadagno (dBi vs dBd), ERP e efficienza di radiazione
  - Conoscere le problematiche delle correnti di modo comune e l'uso dei balun
  - Valutare criticamente le misure sulle antenne (analizzatore, VNA)
  - Distinguere le esigenze diverse tra antenna in trasmissione e in ricezione

---

## 📖 Core Content

### 1. 🔄 Riepilogo: Relazione tra Propagazione e Angolo di Radiazione

La lezione si apre con un riepilogo fondamentale che collega la propagazione ionosferica (trattata nella Lezione 18) alle caratteristiche delle antenne. L'**angolo di radiazione** dell'antenna deve coincidere con l'angolo ottimale per la riflessione ionosferica, altrimenti l'energia viene dispersa in direzioni inutili.

Per i collegamenti a lunga distanza (**DX**), gli angoli bassi di radiazione — compresi tra 0° e 20° di elevazione — sono quelli ottimali, poiché consentono una riflessione ionosferica efficiente e il raggiungimento di stazioni lontane. Se il lobo di radiazione dell'antenna non si sovrappone alla fascia angolare ideale per la riflessione, gran parte dell'energia viene irradiata in direzioni non utili, riducendo drasticamente l'efficacia del collegamento.

> **Principio chiave**: L'efficacia di un collegamento in HF dipende dalla corrispondenza tra il lobo di radiazione dell'antenna e l'angolo di riflessione della ionosfera.

---

### 2. 📡 Antenne Direttive: Metodi per Ottenere la Direttività

Esistono tre metodi principali per concentrare l'energia irradiata in una direzione preferenziale, ottenendo così un'antenna direttiva.

#### 🔹 Riflettore Parabolico

Il **riflettore parabolico** sfrutta le proprietà geometriche della parabola: qualsiasi onda emessa dal fuoco viene riflessa in raggi paralleli, tutti in fase tra loro. Questo produce un fascio estremamente concentrato di energia. Il principio è lo stesso delle antenne paraboliche usate per le telecomunicazioni satellitari e per i radar. L'efficienza dipende dalla precisione della superficie riflettente e dal corretto posizionamento della sorgente nel fuoco geometrico.

#### 🔹 Antenna Yagi-Uda

L'**antenna Yagi-Uda** (comunemente detta Yagi) è il sistema direttivo più diffuso in ambito radioamatoriale. Fu sviluppata dai professori giapponesi Yagi e Uda alla fine degli anni '40. Il suo funzionamento si basa sul principio della **mutua induzione**: un elemento attivo (il **radiatore**, o **dipolo pilotato**) irradia energia che induce correnti negli elementi passivi (o **parassiti**) vicini.

La fase della corrente indotta negli elementi parassiti dipende dalla loro **lunghezza** e dalla **distanza** dal radiatore:

- Il **riflettore** è posizionato dietro il radiatore (nella direzione opposta alla radiazione) ed è leggermente **più lungo** del radiatore (qualche percento, es. se il radiatore è 10 m → riflettore ≈ 10,5 m). La componente reattiva induttiva genera uno sfasamento tale da sommare il campo nella direzione desiderata.
- I **direttori** sono posizionati davanti al radiatore e sono leggermente **più corti** (es. radiatore 10 m → direttori ≈ 9,5 m). La componente reattiva capacitiva produce lo sfasamento opposto.

La combinazione costruttiva/distruttiva dei campi prodotti da tutti gli elementi genera un lobo di radiazione direzionale.

> ⚠️ **Concetto d'esame**: Il riflettore è più lungo del radiatore, i direttori sono più corti. Il radiatore è sempre circa mezza lunghezza d'onda ($\lambda/2$). Non esiste una formula esatta per le differenze di lunghezza, poiché dipendono anche dalla distanza fra gli elementi e dal diametro dei conduttori.

**Guadagno tipico delle Yagi:**

- 2 elementi: ≈ 4 dBd
- 3 elementi: ≈ 6,5 dBd
- L'incremento di guadagno per ogni elemento aggiunto diminuisce progressivamente
- Oltre un certo numero di elementi, la complicazione meccanica non giustifica il guadagno ottenuto

**Nota sulla progettazione moderna**: Con i software di simulazione attuali, si è scoperto che il guadagno dipende più dalla **lunghezza totale** dell'antenna (espressa in lunghezze d'onda) che dal numero di elementi. Un'antenna Yagi lunga due lunghezze d'onda produce circa lo stesso guadagno sia con 5, 6 o 7 elementi nello stesso spazio.

#### 🔹 Array di Antenne (Collineari e ad Elementi Pilotati)

Il terzo metodo consiste nell'utilizzare **più elementi alimentati** (non parassiti) con fase controllata. Esempi includono:

- **Array collineari**: più dipoli allineati verticalmente, alimentati in fase, per concentrare il lobo in azimut.
- **Array a fase controllata (phased arrays)**: sistemi come il **four-square** (quattro verticali disposte a quadrato) in cui la fase di alimentazione di ciascun elemento è controllata (es. 0°, 90°, 90°, 180°) per dirigere il lobo di radiazione in una direzione specifica.

L'**antenna log-periodica** è una variante che offre direttività su una banda molto larga, a differenza della Yagi che è intrinsecamente a banda stretta.

> **Importante**: La direttività dell'antenna si combina sempre con l'effetto del terreno sottostante (**ground gain**). Il diagramma di radiazione reale è il prodotto dell'interazione tra il pattern dell'antenna e le riflessioni dal suolo.

---

### 3. 📊 Guadagno: dBi vs dBd

Il **guadagno** di un'antenna è definito come il rapporto tra l'intensità del campo elettromagnetico prodotto nella direzione di massima radiazione rispetto a quello che produrrebbe un'antenna di **riferimento** a parità di potenza applicata.

I due riferimenti standard sono:

| Unità | Riferimento | Descrizione |
|-------|-------------|-------------|
| **dBi** | Antenna isotropica | Sorgente puntiforme ideale che irradia uniformemente in tutte le direzioni |
| **dBd** | Dipolo a mezz'onda | Antenna reale di riferimento |

La relazione tra le due unità è costante:

$$G_{dBi} = G_{dBd} + 2{,}1 \text{ dB}$$

**Esempio**: un'antenna con guadagno di 10 dBd equivale a 12,1 dBi.

> ⚠️ **Concetto d'esame**: La differenza tra dBi e dBd è sempre 2,1 dB. Quando si confrontano antenne, verificare sempre quale riferimento è utilizzato.

---

### 4. ⚡ ERP — Potenza Effettiva Irradiata

L'**ERP** (Effective Radiated Power, o **Potenza Effettiva Irradiata**) rappresenta la potenza che bisognerebbe applicare a un'antenna isotropica per produrre la stessa intensità di campo nella direzione di massima radiazione dell'antenna in esame.

$$\text{ERP} = P_{TX} \times G$$

dove $P_{TX}$ è la potenza fornita dal trasmettitore e $G$ è il guadagno dell'antenna (in valore lineare, non in dB).

**Esempio pratico**: un trasmettitore da 100 W collegato a un'antenna con guadagno 10 dB (= ×10) produce un ERP di:

$$\text{ERP} = 100 \times 10 = 1000 \text{ W}$$

> ⚠️ **Concetto d'esame**: l'ERP è il prodotto della potenza del trasmettitore per il guadagno dell'antenna.

---

### 5. 🔬 Efficienza di Radiazione

Non tutta la potenza applicata a un'antenna viene effettivamente irradiata. L'**efficienza di radiazione** è il rapporto tra la potenza irradiata e la potenza applicata, ed è sempre inferiore al 100%.

$$\eta = \frac{P_{irradiata}}{P_{applicata}} = \frac{R_{rad}}{R_{rad} + R_{perdita}}$$

dove:

- **$R_{rad}$** — Resistenza di radiazione: la componente dell'impedenza responsabile dell'effettiva irradiazione
- **$R_{perdita}$** — Resistenza di perdita: la somma di tutte le perdite dissipative

Le componenti della resistenza di perdita sono:

1. **Perdite nel conduttore** (effetto pelle / skin effect): la corrente RF scorre solo sulla superficie del conduttore. Lo **spessore di penetrazione** ($\sigma$) nel rame è circa 20 µm a 10 MHz e circa 4-5 µm a 100 MHz. Un dipolo per 160 m in filo da 1 mm può avere circa 10 Ω di resistenza del conduttore (contro milliohm in corrente continua). Conduttori di diametro maggiore hanno resistenza RF minore.
2. **Perdite nel dielettrico**: dovute agli isolatori e ai materiali che sostengono l'antenna.
3. **Perdite nel terreno**: particolarmente significative per antenne orizzontali poste a meno di $\lambda/4$ da terra, e sempre presenti per le antenne verticali.

> **Principio fondamentale**: A parità di perdite, un'antenna con bassa resistenza di radiazione avrà un'efficienza minore. Le **antenne caricate** (più corte della dimensione risonante) hanno intrinsecamente una $R_{rad}$ minore e quindi efficienza inferiore rispetto alle corrispondenti antenne full-size, a meno di adottare strategie specifiche per minimizzare le perdite.

> **Conseguenza pratica**: Antenne di dimensioni molto ridotte (es. grandi come una bottiglia d'acqua minerale) non possono avere buona efficienza. Nella maggior parte dei casi, è il cavo di alimentazione che irradia, non l'antenna stessa.

---

### 6. 🔢 Esempi Pratici di Calcolo dell'Efficienza

Tre casi reali analizzati in dettaglio durante la lezione:

#### Caso 1: Dipolo orizzontale 40 m a λ/4 da terra

| Parametro | Valore |
|-----------|--------|
| Banda | 40 m (7 MHz) |
| Altezza | 10 m (= λ/4) |
| Conduttore | Ø 1,5 mm |
| $R_{rad}$ | 85 Ω |
| $R_{perdita}$ (conduttore + terreno) | 4 Ω |
| Impedenza al punto di alimentazione | 89 Ω |
| ROS (su 50 Ω) | 1,78 |
| **Efficienza** | **95%** |

#### Caso 2: Dipolo orizzontale 80 m a λ/8 da terra

| Parametro | Valore |
|-----------|--------|
| Banda | 80 m (3,5 MHz) |
| Altezza | 10 m (= λ/8) |
| Conduttore | Ø 1,5 mm |
| $R_{rad}$ | 45 Ω |
| $R_{perdita}$ (conduttore + terreno significativo) | 7 Ω |
| Impedenza al punto di alimentazione | 52 Ω |
| ROS (su 50 Ω) | 1,04 |
| **Efficienza** | **≈ 87%** |

#### Caso 3: Verticale caricata λ/8 a terra con 16 radiali

| Parametro | Valore |
|-----------|--------|
| Tipo | Verticale caricata in testa |
| Lunghezza | λ/8 |
| Installazione | A terra, 16 radiali interrati lunghi ~λ |
| $R_{rad}$ | 20 Ω |
| $R_{perdita}$ (principalmente terreno) | 18 Ω |
| Impedenza al punto di alimentazione | 38 Ω |
| ROS (su 50 Ω) | 1,3 |
| **Efficienza** | **52%** |

#### Lezioni apprese dai tre casi

Il confronto tra i casi è estremamente istruttivo:

- Il **Caso 2** ha il ROS migliore (quasi 1:1) ma un'efficienza inferiore al Caso 1 che ha ROS 1,8. Il ROS non è indicatore di efficienza.
- Il **Caso 3** ha un ROS accettabile (1,3) ma **metà della potenza** viene dissipata in perdite nel terreno.

> **Citazione**: Il famoso autore **John Devolder** (ON4UN, scomparso recentemente) scrive: *"L'antenna con il miglior valore di ROS è un buon carico fittizio (dummy load)."*

> ⚠️ **Concetto d'esame**: Il **carico fittizio** è chiamato anche **antenna artificiale** nelle domande d'esame. È una resistenza pura che presenta ROS perfetto ma efficienza di radiazione nulla.

**Conclusione fondamentale**: Un buon valore di ROS indica un buon adattamento di impedenza ma **non fornisce alcuna indicazione attendibile circa l'efficienza di radiazione** dell'antenna. Misurare il ROS è semplice; valutare l'efficienza di radiazione non lo è affatto.

---

### 7. 🌐 Antenne Verticali e Radiali

Le antenne verticali, anche se montate a terra, devono sempre essere dotate di un **adeguato numero di radiali**. Senza radiali:

- Tutta la corrente d'antenna deve richiudersi attraverso il terreno → perdite elevate
- Se montata su un tetto o altra struttura, la corrente si richiude attraverso qualsiasi percorso conduttivo disponibile (impianti elettrici, strutture metalliche), causando perdite imprevedibili, interferenze e disturbi

**Strategie per i radiali:**

| Installazione | Caratteristiche |
|---------------|----------------|
| Radiali interrati | Buona efficienza, la corrente li attraversa preferenzialmente rispetto al terreno |
| Radiali appoggiati a terra/tetto | Funzionano sufficientemente bene perché la loro conducibilità è molto superiore a quella del terreno |
| Radiali sollevati | Condizione ottimale per antenne montate in quota |

**Anche con i radiali**, è necessario un dispositivo di blocco (**RF choke**) per evitare che correnti di modo comune scorrano sulla calza esterna del cavo coassiale. Per l'**effetto pelle**, la superficie esterna e quella interna della calza si comportano come due conduttori separati.

> **Regola pratica**: L'andamento della corrente è massimo in prossimità del punto di alimentazione e decresce allontanandosi. Anche radiali relativamente corti sono meglio di nessun radiale. L'ideale sarebbero radiali risonanti (λ/4), ma qualsiasi lunghezza apporta un beneficio.

---

### 8. 🔌 Correnti di Modo Comune e Balun

Al punto di alimentazione di un'antenna si presentano tre esigenze fondamentali:

1. **Bilanciamento** (passaggio bilanciato/sbilanciato — BALanced/UNbalanced = **BALUN**)
2. **Adattamento di impedenza** (rapporto di trasformazione 1:1, 4:1, ecc.)
3. **Blocco delle correnti di modo comune** (RF choke)

Esistono due tipi principali di balun:

#### Balun di corrente (Guanella / Choke balun)

Il **balun di corrente** è la soluzione preferita perché svolge contemporaneamente tutte e tre le funzioni sopra elencate. Funziona come un **Transmission Line Transformer (TLT)** e può essere realizzato:

- Avvolgendo il cavo coassiale in spire (formando un'induttanza sulla calza esterna)
- Utilizzando avvolgimenti su nuclei di ferrite

È dimostrabile matematicamente che, qualsiasi sia il rapporto delle tensioni al lato bilanciato rispetto a massa, le correnti dall'altro lato rimangono sostanzialmente inalterate. Questo garantisce un eccellente bilanciamento.

Lo stesso principio è utilizzato nei moderni finali di potenza in push-pull, dove l'accoppiamento bilanciato-sbilanciato in uscita è realizzato con un TLT.

#### Balun di tensione

Il **balun di tensione** utilizza avvolgimenti multipli (bifilari, trifilari) su nuclei di ferrite. Funziona correttamente solo con carichi perfettamente bilanciati. È meno versatile del balun di corrente.

#### Considerazioni pratiche sul choke in cavo coassiale

Quando si realizza un choke avvolgendo il cavo coassiale in spire, si formano **capacità parassite tra le spire** che portano l'insieme in risonanza a una certa frequenza. È opinione condivisa che il choke debba operare **sotto la sua frequenza di autorisonanza**, dove l'attenuazione di modo comune è maggiore. Sopra la risonanza, l'impedenza cala drasticamente.

Si possono ottimizzare le prestazioni giocando sul rapporto lunghezza/diametro dell'avvolgimento: un avvolgimento più allungato (rapporto lunghezza/diametro maggiore) sposta la frequenza di autorisonanza. Per un'antenna ben bilanciata come una Yagi, un'attenuazione di modo comune di **20-25 dB** è già sufficiente.

In alternativa al choke in cavo, si possono usare **manicotti di ferrite** infilati sull'esterno del cavo.

> ⚠️ **Attenzione**: Se un'antenna verticale senza radiali viene dotata di un choke efficiente, l'antenna smette di funzionare perché il choke blocca la corrente sia per gli effetti negativi sia per quelli positivi (il ritorno della corrente attraverso la calza).

---

### 9. 📏 Misure sulle Antenne: Analizzatore e VNA

I moderni strumenti (analizzatori d'antenna, VNA — Vector Network Analyzer) sono accessibili ed economici, ma richiedono una corretta interpretazione dei dati.

#### Misure di impedenza con analizzatore d'antenna

La misura dell'impedenza eseguita all'estremità del cavo coassiale (e non direttamente sull'antenna) **può non essere attendibile** se la lunghezza del cavo non è un multiplo intero di $\lambda/2$.

> **Regola fondamentale**: Solo con una lunghezza elettrica del cavo pari a un multiplo intero di $\lambda/2$ l'impedenza misurata all'estremità del cavo corrisponde esattamente a quella presente al punto di alimentazione dell'antenna.

**Esempio numerico 1**:

- Antenna con impedenza reale: 31,5 Ω (puramente resistiva), ROS = 1,58
- Misurato attraverso cavo di lunghezza arbitraria: 52 − j25 Ω (componente capacitiva spuria!)
- Valore completamente diverso dalla realtà

**Esempio numerico 2**:

- Antenna con impedenza reale: 75 Ω, cavo 50 Ω, ROS = 1,5, lunghezza cavo 0,3 λ
- Misurato: 35 + j8 Ω (componente induttiva spuria!)

#### Misure con VNA e carta di Smith

Un errore comune con il VNA è identificare la **frequenza di risonanza** dell'antenna come il punto in cui la curva sulla carta di Smith attraversa l'asse orizzontale (impedenza puramente resistiva). Questa lettura è corretta **solo** se lo strumento è stato configurato per compensare la lunghezza del cavo.

Senza la compensazione del cavo, il punto di minimo ROS (punto più vicino al centro della carta di Smith) è un indicatore più affidabile della frequenza di risonanza rispetto all'attraversamento dell'asse reale.

---

### 10. 📡 Differenze tra Antenna in Trasmissione e in Ricezione

Questa sezione tratta un aspetto avanzato ma importante, spesso trascurato.

**In trasmissione** l'obiettivo è:

- Massimizzare l'energia irradiata nella fascia angolare ottimale (0°-20° per DX)
- Ottenere il massimo guadagno nella direzione desiderata

**In ricezione** l'obiettivo è:

- Massimizzare il **rapporto segnale-rumore** (SNR), che è una cosa diversa dal massimizzare il segnale ricevuto

In HF, e soprattutto sulle bande basse, il **rumore prevalente è quello esterno** (atmosferico, attività umane), che può superare il rumore interno del ricevitore anche di 50-60 dB. Questo rumore esterno è distribuito mediamente in tutte le direzioni.

Di conseguenza, un aumento generalizzato del guadagno dell'antenna incrementa sia il segnale utile sia il rumore esterno, **senza migliorare il rapporto segnale-rumore**.

> **Strategia corretta in ricezione**: L'unico modo per migliorare l'SNR è disporre di un'antenna con massimo nella direzione del segnale utile e **marcata attenuazione in tutte le altre direzioni**, indipendentemente dal valore assoluto del guadagno.

Esistono antenne specializzate per la ricezione che hanno guadagni molto bassi o addirittura negativi, ma offrono vantaggi in termini di SNR grazie alla selettività direzionale del loro lobo. Il **loop magnetico** è un esempio: si comporta molto bene in ricezione ma non altrettanto in trasmissione.

---

### 11. ❓ Sessione Domande e Risposte

#### Vicinanza tra antenne verticali

Una domanda riguarda due antenne verticali distanti solo 40 cm, una multibanda e una Gy Master per i 27 MHz. Paolo spiega che 40 cm è una distanza significativa solo a frequenze molto elevate (es. 3 GHz), ma a 10 MHz si è abbondantemente nel **campo vicino** e gli effetti di **mutuo accoppiamento** sono significativi, anche con l'antenna inutilizzata scollegata. Senza radiali, la corrente di ritorno scorre sulla calza del cavo → rischio interferenze. Consiglio: aggiungere anche pochi radiali corti, appoggiati al tetto, è sempre meglio di niente.

#### Domanda d'esame sulla Yagi a 14 MHz

Viene discussa una domanda d'esame: *"Quanto è lungo approssimativamente l'elemento attivo di un'antenna Yagi per i 14 MHz?"*

Il calcolo: $150 / 14 = 10{,}71$ m. Tra le risposte disponibili (10,7 m e 10 m), la risposta considerata corretta è **10 m** per via della parola "approssimativamente" e del fatto che l'elemento radiante di una Yagi è in realtà leggermente più corto della mezzonda teorica (fattore di velocità tipico per il diametro dell'elemento). La questione è considerata discutibile nella sua formulazione.

#### Choke balun: aspetti pratici

Discussione dettagliata sulla realizzazione pratica di un choke con cavo coassiale avvolto in spire. Viene confermato che:

- Il choke va fatto lavorare **sotto** la sua frequenza di autorisonanza
- Esistono risonanza serie e antirisonanza (parallelo), relativamente vicine tra loro
- Si può ottimizzare agendo sul rapporto lunghezza/diametro dell'avvolgimento
- Per antenne ben bilanciate, 20-25 dB di attenuazione di modo comune sono sufficienti
- Alternativa: manicotti di ferrite sull'esterno del cavo

#### Riflessione lunare (EME)

Viene menzionata un'esperienza di riflessione lunare (EME — Earth-Moon-Earth) sui 2 m con due Yagi a 12 elementi accoppiate con polarizzazione incrociata (orizzontale + verticale) per ottenere **polarizzazione circolare**, molto utile nelle comunicazioni EME poiché la riflessione lunare altera la polarizzazione del segnale.

---

## 🔗 Concept Map (testuale)

- Angolo di radiazione → deve coincidere con → angolo di riflessione ionosferica per DX
- Antenne direttive → concentrano energia → in una direzione preferenziale
- Yagi-Uda → utilizza → mutua induzione tra elementi parassiti
- Riflettore → è leggermente più lungo di → radiatore → è leggermente più lungo di → direttori
- Guadagno (dBi) = Guadagno (dBd) + 2,1 dB
- ERP = Potenza TX × Guadagno antenna
- Efficienza di radiazione → dipende da → rapporto $R_{rad} / (R_{rad} + R_{perdita})$
- Antenne caricate → hanno $R_{rad}$ minore → efficienza minore a parità di perdite
- Perdite nel conduttore → causate da → effetto pelle (skin effect)
- Perdite nel terreno → significative per → antenne basse e verticali senza radiali
- Radiali → riducono → perdite nel terreno → migliorano → efficienza di radiazione
- ROS basso → indica → buon adattamento → ma NON indica → buona efficienza
- Carico fittizio = antenna artificiale → ROS perfetto → efficienza zero
- Balun di corrente → svolge → bilanciamento + adattamento + blocco modo comune
- Misura impedenza attraverso cavo → attendibile solo se → lunghezza cavo = n × λ/2
- Guadagno TX → concentra energia → nella direzione desiderata
- Guadagno RX → aumenta → sia segnale sia rumore → SNR non migliora
- SNR migliora solo con → attenuazione marcata in → direzioni diverse da quella utile

---

## 📝 Key Takeaways

1. **Angolo di radiazione e propagazione**: Per i collegamenti DX in HF, l'angolo di radiazione ottimale è compreso tra 0° e 20°. L'antenna deve concentrare la massima energia in questa fascia.

2. **Tre metodi per la direttività**: Riflettore parabolico (focalizzazione geometrica), Yagi-Uda (elementi parassiti per mutua induzione) e array ad elementi pilotati (controllo elettronico della fase).

3. **Yagi — regola degli elementi**: Il riflettore è leggermente più lungo del radiatore, i direttori leggermente più corti. Il riferimento è sempre il dipolo a mezza lunghezza d'onda.

4. **dBi vs dBd**: La differenza è costante e pari a 2,1 dB. Un guadagno di X dBd equivale a (X + 2,1) dBi.

5. **ERP**: La potenza effettiva irradiata è il prodotto della potenza del trasmettitore per il guadagno dell'antenna. 100 W con guadagno 10 dB (×10) → ERP = 1000 W.

6. **Efficienza di radiazione**: $\eta = R_{rad} / (R_{rad} + R_{perdita})$. Un'antenna con bassa resistenza di radiazione (es. antenne caricate o molto piccole) avrà sempre efficienza inferiore rispetto a un'antenna full-size, a parità di perdite.

7. **ROS ≠ Efficienza**: Un buon ROS indica solo un buon adattamento di impedenza. Il carico fittizio (antenna artificiale) ha ROS perfetto ma efficienza di radiazione nulla.

8. **Radiali sempre necessari**: Le antenne verticali richiedono sempre radiali per minimizzare le perdite nel terreno e controllare il percorso della corrente di ritorno. Anche radiali corti sono meglio di nessun radiale.

9. **Balun di corrente preferibile**: Il balun di corrente (Guanella/choke) è il tipo migliore perché svolge contemporaneamente bilanciamento, adattamento e blocco delle correnti di modo comune.

10. **Misure attraverso il cavo**: L'impedenza misurata all'estremità del cavo è attendibile solo se la lunghezza elettrica del cavo è un multiplo intero di λ/2. Il punto di minimo ROS è un indicatore di risonanza più affidabile dell'attraversamento dell'asse reale sulla carta di Smith.

11. **TX vs RX**: In trasmissione si cerca il massimo guadagno nella direzione desiderata; in ricezione si cerca il massimo rapporto segnale-rumore, ottenibile con forte attenuazione nelle direzioni indesiderate, non semplicemente aumentando il guadagno.

---

## ❓ Comprehension Questions

1. Perché un'antenna con ROS prossimo a 1:1 potrebbe comunque avere un'efficienza di radiazione molto bassa? Spiega con un esempio numerico.

2. Un dipolo in banda 40 m a λ/4 da terra ha efficienza del 95%, mentre una verticale caricata λ/8 con 16 radiali ha efficienza del 52%. Quali sono le cause principali di questa differenza?

3. Spiega perché l'effetto pelle rende la resistenza di un conduttore alle radiofrequenze molto maggiore rispetto alla corrente continua. Come varia lo spessore di penetrazione con la frequenza?

4. Perché misurare l'impedenza di un'antenna all'estremità del cavo coassiale può dare risultati errati? In quale caso specifico la misura è attendibile?

5. In che modo il balun di corrente differisce dal balun di tensione? Perché il primo è generalmente preferito?

6. Spiega il funzionamento di una Yagi a tre elementi: qual è il ruolo del riflettore, del radiatore e del direttore? Come si determina la fase relativa delle correnti indotte?

7. Perché in ricezione HF sulle bande basse un aumento del guadagno dell'antenna non migliora necessariamente il rapporto segnale-rumore? Quale strategia è più efficace?

8. Un'antenna ha un'efficienza di radiazione del 52%. Se il trasmettitore eroga 100 W e l'antenna ha guadagno 6 dBi, qual è l'ERP effettivo considerando le perdite?

9. Perché le antenne verticali necessitano sempre di radiali, anche quando il ROS misurato è accettabile? Cosa succede alla corrente di ritorno in assenza di radiali?

10. Discuti il paradosso per cui antenne miniaturizzate possono mostrare un buon ROS pur avendo un'efficienza di radiazione trascurabile. Qual è l'elemento che effettivamente irradia in questi casi?

---

## 📚 Glossary

- **Antenna artificiale** — Sinonimo di carico fittizio (dummy load). Resistenza pura usata per prove di trasmettitori senza irradiare. Termine usato nelle domande d'esame.
- **Antenna isotropica** — Sorgente puntiforme ideale che irradia uniformemente in tutte le direzioni. Esiste solo come riferimento teorico.
- **Array (collineare / phased)** — Sistema di più antenne alimentate con fase controllata per ottenere direttività.
- **Balun** — Dispositivo che realizza la transizione tra una linea sbilanciata (coassiale) e un carico bilanciato (dipolo). Da BALanced-UNbalanced.
- **Balun di corrente (Guanella)** — Tipo di balun che mantiene uguali le correnti nei due conduttori. Svolge bilanciamento, adattamento e blocco delle correnti di modo comune.
- **Balun di tensione** — Tipo di balun con avvolgimenti bifilari/trifilari su ferrite. Efficace solo con carichi perfettamente bilanciati.
- **Carico fittizio (Dummy load)** — Resistenza pura (50 Ω) non radiante, usata per test. Presenta ROS perfetto ma efficienza di radiazione nulla.
- **Correnti di modo comune** — Correnti indesiderate che scorrono sulla superficie esterna della calza del coassiale, causando irradiazione spuria e interferenze.
- **dBd** — Unità di guadagno riferita al dipolo a mezza lunghezza d'onda.
- **dBi** — Unità di guadagno riferita all'antenna isotropica. $G_{dBi} = G_{dBd} + 2{,}1$.
- **Direttore** — Elemento parassita della Yagi, più corto del radiatore, posto nella direzione di massima radiazione.
- **Effetto pelle (Skin effect)** — Fenomeno per cui la corrente RF scorre solo sulla superficie del conduttore, aumentando la resistenza effettiva. Spessore di penetrazione: ~20 µm a 10 MHz nel rame.
- **Efficienza di radiazione** — Rapporto tra potenza irradiata e potenza applicata: $\eta = R_{rad}/(R_{rad}+R_{perdita})$.
- **EME (Earth-Moon-Earth)** — Tecnica di comunicazione radio che utilizza la Luna come riflettore passivo.
- **ERP (Effective Radiated Power)** — Potenza effettiva irradiata: $\text{ERP} = P_{TX} \times G$.
- **Four-square** — Array di quattro antenne verticali disposte a quadrato con alimentazione a fase controllata (0°/90°/90°/180°).
- **Log-periodica** — Antenna direttiva a banda larga, alternativa alla Yagi quando serve copertura su ampio range di frequenze.
- **Loop magnetico** — Antenna di piccole dimensioni con buone prestazioni in ricezione (alto SNR) ma bassa efficienza in trasmissione.
- **Mutua induzione** — Fenomeno per cui un elemento radiante induce corrente in un elemento parassita vicino. Principio di funzionamento della Yagi.
- **Radiali** — Conduttori disposti radialmente alla base di un'antenna verticale, necessari per fornire un percorso a bassa impedenza alla corrente di ritorno e minimizzare le perdite nel terreno.
- **Rapporto segnale-rumore (SNR)** — Rapporto tra l'intensità del segnale utile e il rumore. In ricezione HF, il rumore esterno è dominante.
- **Resistenza di perdita ($R_{perdita}$)** — Componente resistiva che dissipa potenza senza irradiarla (conduttore, dielettrico, terreno).
- **Resistenza di radiazione ($R_{rad}$)** — Componente dell'impedenza dell'antenna responsabile dell'effettiva irradiazione elettromagnetica.
- **RF Choke** — Dispositivo (induttanza o manicotti di ferrite) che blocca le correnti di modo comune sulla calza esterna del cavo coassiale.
- **Riflettore (Yagi)** — Elemento parassita della Yagi, leggermente più lungo del radiatore, posto nella direzione opposta alla radiazione.
- **TLT (Transmission Line Transformer)** — Trasformatore realizzato con tratti di linea di trasmissione, utilizzato nei balun di corrente e negli stadi finali di potenza.
- **VNA (Vector Network Analyzer)** — Strumento di misura che analizza impedenze e parametri di scattering in ampiezza e fase.
- **Yagi-Uda** — Antenna direttiva composta da un radiatore (dipolo alimentato) e uno o più elementi parassiti (riflettore e direttori). Inventata da Yagi e Uda alla fine degli anni '40.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo — Radioamatore dal 1977 con oltre 40 anni di esperienza professionale nel settore RF. Conclude il suo ciclo di lezioni sulle antenne con questa sessione.
- 🎙️ **Moderatore**: Alessandro (Ale) — Gestisce la sessione e le domande.
- 🎓 **Partecipanti**: Aspiranti radioamatori del corso ARI Toscana CRT 2025. Intervengono con domande: Claudio (problemi di installazione antenne verticali), Marco (domande d'esame sulla Yagi), Sauro (aspetti tecnici del choke balun e correnti di modo comune).

---

## ⏱️ Evidenze Temporali

| Intervallo | Argomento |
|------------|-----------|
| 00:00 – 05:20 | Riepilogo propagazione e angolo di radiazione |
| 05:20 – 17:00 | Metodi per ottenere la direttività (parabola, Yagi, array) |
| 07:00 – 10:57 | Guadagno: dBi vs dBd, differenza di 2,1 dB |
| 37:20 – 41:30 | ERP — Potenza Effettiva Irradiata, esempi di calcolo |
| 41:36 – 55:00 | Efficienza di radiazione: formula, componenti di perdita |
| 42:00 – 53:00 | Correnti di modo comune, balun di corrente vs tensione |
| 59:00 – 66:00 | Effetto pelle: spessore di penetrazione, resistenza RF |
| 66:16 – 71:05 | Antenne verticali, radiali, correnti sulla calza del cavo |
| 71:11 – 74:16 | Formula efficienza di radiazione, antenne caricate e piccole |
| 74:16 – 82:56 | Tre esempi pratici di calcolo efficienza (40m, 80m, verticale) |
| 82:56 – 83:03 | ROS vs efficienza: citazione di John Devolder, carico fittizio |
| 83:03 – 90:52 | Misure con analizzatore d'antenna e VNA, errori comuni |
| 91:00 – 97:39 | TX vs RX: guadagno, SNR, antenne specializzate per ricezione |
| 97:39 – 98:22 | Letture consigliate, conclusione del ciclo di lezioni di Paolo |
| 98:34 – 105:20 | Q&A: Claudio — antenne verticali vicine, radiali, installazione |
| 105:27 – 109:18 | Q&A: Marco — domanda d'esame Yagi 14 MHz |
| 109:26 – 119:38 | Q&A: Sauro — choke balun, risonanza, attenuazione modo comune |
| 119:44 – 130:10 | Q&A: Marco — elementi Yagi (riflettore/direttore), guadagno, EME |

---

## 📅 Informazioni Lezione

| Campo | Valore |
|-------|--------|
| **Lezione** | 21 |
| **Data** | 24 settembre 2025 |
| **Durata** | ≈ 2 ore e 10 minuti |
| **Argomenti trattati** | 11 |
| **Parole chiave** | Antenne direttive, Yagi-Uda, guadagno dBi dBd, ERP, efficienza di radiazione, skin effect, radiali, balun di corrente, correnti modo comune, misure antenna, VNA, SNR ricezione, carico fittizio |
