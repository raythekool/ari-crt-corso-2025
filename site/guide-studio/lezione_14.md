---
layout: default
---

# 📘 Lezione 14 - Antenne - Parte 2

## 📌 Overview

- **Materia**: Radiotecnica — Trasduttori, Miscelatori, Trasmettitori e Intermodulazione
- **Tempo di studio stimato**: 100–120 minuti
- **Prerequisiti**: Oscillatori e PLL (Lezione 13); classi di amplificazione e decibel (Lezione 13); modulazione AM/SSB/FM (Lezione 07); circuiti risonanti e filtri (Lezione 06); diodi varicap (Lezione 11)
- **Obiettivi di apprendimento**:
  - Conoscere i tipi di trasduttori: microfoni (carbone, cristallo, condensatore, dinamico) e altoparlanti
  - Comprendere il funzionamento del miscelatore (mixer): frequenza somma e differenza
  - Conoscere lo schema a blocchi dei trasmettitori in CW, SSB, AM e FM
  - Capire la conversione di frequenza e il suo ruolo nei trasmettitori multibanda
  - Comprendere il problema dell'intermodulazione e degli splatter

---

## 📖 Core Content

### 1. 🔍 Correzione Quiz Lezione 13 (⏱ 00:03–12:30)

Paolo apre la lezione con la correzione del quiz precedente, dedicato ad amplificatori, oscillatori e decibel. Risultati molto buoni, con qualche difficoltà solo sulla domanda relativa ai −6 dB.

#### 🔹 Risposte Chiave e Chiarimenti

- **Maggior rendimento**: amplificatore in **classe C** (70–75%). Se assorbe 100 W dall'alimentatore, 75 W diventano RF e solo 25 W in calore.
- **Primo stadio BF** in un trasmettitore per amplificare il segnale microfonico: funziona in **classe A** (totale fedeltà). Regola generale: tutti gli stadi a basso livello (bassa potenza) lavorano in classe A.
- **Alto rendimento senza vincoli sulla distorsione**: **classe C**. Adatta per telegrafia (CW) dove il segnale è una sinusoide pura on/off.
- **Distorsione minore**: **classe A** (mnemonica: A = Alta fedeltà).
- **PLL**: circuito che confronta la frequenza del VCO con un riferimento a quarzo e produce una tensione di correzione.
- **Cosa distingue le classi**: l'**angolo di conduzione** del segnale in uscita (360° classe A, ~180° classe B, <180° classe C).
- **Push-pull**: alto rendimento e bassa distorsione (due dispositivi in classe B che ricostruiscono il segnale completo).
- **1 W + 13 dB**: 13 = 10 + 3 → ×10 = 10 W, ×2 = **20 W**.
- **100 W + antenna (+4 dB) − cavo (−1 dB)**: guadagno netto = +3 dB → **200 W**.
- **100 W − cavo (−6 dB)**: −6 = −3 −3 → 100 × 0,5 = 50, × 0,5 = **25 W** (situazione classica — investire in un buon cavo!).
- **Modifica frequenza oscillatore variabile**: **diodo varicap** (condensatore variabile elettronico, polarizzazione inversa).

---

### 2. 🎙️ Trasduttori: Microfoni e Altoparlanti (⏱ 15:00–30:00)

I trasduttori sono i componenti che interfacciano il mondo esterno (onde acustiche) con il mondo elettrico (segnali elettrici della radio).

#### 🔹 Il Microfono

**Microfono** — trasduttore che trasforma un'onda acustica (vibrazione meccanica) in un segnale elettrico.

Esistono quattro tipi principali di microfoni:

**Microfono a carbone** — sfrutta la variazione di conduttività di granuli di carbone compressi. La voce fa vibrare una lamina metallica che comprime e dilata i granuli, variandone la resistenza. Molto storico, usato nei vecchi telefoni (SIP). Adatto alla voce ma non ad alta fedeltà, non sale particolarmente in frequenza. Oggi raramente usato se non in apparati vintage.

**Microfono a cristallo (ceramico)** — sfrutta l'**effetto piezoelettrico** del quarzo. La voce fa vibrare una lamina che comprime un piccolo cristallo, che genera una tensione proporzionale all'intensità del suono. Molto adatto all'uso radio perché enfatizza i toni acuti della voce, rendendo il segnale più comprensibile in condizioni di disturbo e segnali deboli. Non è alta fedeltà, ma eccelle nelle comunicazioni.

**Microfono a condensatore** — contiene un condensatore con un'armatura fissa e una mobile (membrana). La voce fa vibrare la membrana, variando la distanza tra le armature e quindi la capacità. Un circuito converte la variazione di capacità in tensione. È il microfono di **migliore qualità** (alta fedeltà). Richiede **alimentazione** (Phantom power) per il circuito interno.

**Microfono dinamico** — funziona come un altoparlante al contrario: la voce fa vibrare una membrana collegata a una bobina mobile immersa nel campo magnetico di un magnete permanente. Il movimento della bobina genera una tensione. Buona fedeltà, secondo solo al condensatore. Molto usato per il canto e applicazioni generiche.

⚠️ Attenzione alla distinzione: i microfoni **preamplificati** (con batteria interna) usano spesso capsule ceramiche o dinamiche — la batteria alimenta il preamplificatore, non il microfono. Nei microfoni a condensatore, invece, l'alimentazione serve al microfono stesso oltre che al preamplificatore.

#### 🔹 L'Altoparlante

**Altoparlante** — trasduttore che trasforma un segnale elettrico in un'onda acustica (funzione reciproca del microfono).

Funzionamento basato sull'interazione tra due campi magnetici:

1. Un **magnete permanente** crea un campo magnetico costante
2. Una **bobina mobile** inserita nella cavità del magnete permanente riceve il segnale elettrico
3. La corrente nella bobina genera un campo magnetico variabile
4. L'interazione tra i due campi (attrazione/repulsione) muove la bobina
5. La bobina è collegata a un **cono** che riproduce le vibrazioni nell'aria → suono

Il microfono dinamico è essenzialmente un altoparlante usato al rovescio.

---

### 3. 🔄 Miscelatori (Mixer) (⏱ 30:48–35:30)

**Miscelatore (mescolatore, mixer)** — componente con **due ingressi e un'uscita** che combina due segnali a frequenze diverse producendo in uscita la frequenza somma e la frequenza differenza.

I tre termini (miscelatore, mescolatore, mixer) sono sinonimi e compaiono tutti nelle domande d'esame.

#### 🔹 Funzionamento

Se i due segnali in ingresso hanno frequenza $f_1$ e $f_2$, in uscita si trovano **contemporaneamente**:

- **Frequenza somma**: $f_1 + f_2$
- **Frequenza differenza**: $f_1 - f_2$

> **Esempio**: $f_1 = 10$ MHz, $f_2 = 2$ MHz → in uscita: 12 MHz (somma) e 8 MHz (differenza).

Il miscelatore è fondamentale per la **conversione di frequenza** sia nei trasmettitori che nei ricevitori. Si seleziona poi il segnale desiderato (somma o differenza) mediante un filtro passa-banda con circuiti risonanti.

Dal punto di vista pratico, un **MOSFET a doppio gate** funziona già come miscelatore: iniettando i due segnali nei due gate, in uscita (drain) si ottengono somma e differenza.

---

### 4. 📡 Schema Generale del Trasmettitore (⏱ 35:30–40:00)

Il trasmettitore è un dispositivo che trasforma l'informazione (voce, dati, immagini) in un segnale irradiabile da un'antenna. Lo schema a blocchi generale comprende:

1. **Oscillatore** — genera un segnale RF (es. 14 MHz), potenza molto bassa (pochi milliwatt)
2. **Driver (pilota)** — catena di amplificatori in **classe A** che amplifica il segnale dell'oscillatore fino alla potenza necessaria per pilotare il finale (es. ~10 W)
3. **Amplificatore finale** — tipicamente **push-pull in classe AB**, amplifica fino alla potenza di uscita desiderata (es. 100 W)
4. **Accordatore d'antenna** — adatta l'impedenza di uscita dell'amplificatore a quella dell'antenna (standard **50 Ω**) per il massimo trasferimento di potenza
5. **Modulatore** — riceve il segnale microfonico amplificato e lo applica alla catena in un punto appropriato (diverso a seconda del tipo di modulazione)
6. **Alimentatore** — fornisce corrente a tutti i blocchi

---

### 5. 📻 Trasmettitore in Telegrafia (CW) (⏱ 40:49–54:00)

#### 🔹 Schema CW a Singola Frequenza

Il trasmettitore CW più semplice:

- **Oscillatore a cristallo** (Xtal) → frequenza fissa (es. 14 MHz)
- **Amplificatore di potenza**
- **Tasto telegrafico** → interruttore che accende/spegne uno stadio a basso livello

Schema didattico; limite: trasmette su una sola frequenza.

#### 🔹 Schema CW Multibanda con Conversione di Frequenza

Per trasmettere su più bande si usa la **conversione di frequenza**:

- **VFO** (oscillatore a frequenza variabile) a bassa frequenza (es. 5–5,5 MHz) → più stabile che ad alta frequenza
- **Oscillatore a cristallo** fisso → fornisce la frequenza di "battimento"
- **Mixer** → combina VFO + cristallo per ottenere la frequenza desiderata

> **Esempio**: VFO a 5 MHz + cristallo a 23 MHz → uscita a 28 MHz (banda 10 m). VFO a 5,5 MHz + cristallo a 9 MHz → uscita a 3,5 MHz (banda 80 m). Un unico VFO con diversi cristalli copre tutte le bande.

#### 🔹 Circuito di Accordo (Pi-Greco)

**Circuito pi-greco (π)** — circuito di adattamento d'impedenza formato da 2 condensatori variabili e 1 induttore, con forma che ricorda la lettera greca π. Adatta l'impedenza di uscita del trasmettitore ai 50 Ω dell'antenna.

Quando le impedenze sono uguali → **massimo trasferimento di potenza**.

#### 🔹 Click di Manipolazione

**Click di manipolazione** — disturbo causato dai fronti troppo ripidi dell'accensione/spegnimento del segnale CW. L'interruzione brusca (on/off istantaneo) allarga la banda del segnale, disturbando i canali adiacenti.

**Soluzione**: circuito di **smussamento** (shaping) che rende graduali le transizioni di potenza:

- **Salita progressiva** all'inizio di ogni punto/linea (rise time)
- **Discesa progressiva** alla fine (fall time)

Il segnale "smussato" non genera click. Questo circuito opera a basso livello (pochi mW), dove è più facile da realizzare.

---

### 6. 📻 Trasmettitore SSB (⏱ 58:30–88:00)

Il trasmettitore **SSB (Single Side Band)** è più complesso del CW ma segue una logica chiara.

#### 🔹 Generazione del Segnale SSB

1. **Oscillatore a cristallo** — genera la portante a frequenza fissa (tradizionalmente 9 MHz)
2. **Amplificatore BF** — amplifica il segnale microfonico
3. **Modulatore bilanciato** — riceve portante + segnale audio:
   - Genera un segnale a **doppia banda laterale (DSB)**
   - **Sopprime la portante**: quando non si parla, non esce niente
4. **Filtro a cristallo (2,5 kHz)** — filtro passa-banda strettissimo che lascia passare **una sola banda laterale**, sopprimendo l'altra → **SSB**

**Modulatore bilanciato** — circuito simile a un mixer che produce somma e differenza delle frequenze di ingresso, ma con la caratteristica aggiuntiva di sopprimere il segnale dell'oscillatore (portante) quando non c'è modulazione.

#### 🔹 Selezione USB/LSB

Poiché il filtro a cristallo è costoso, si usa un **unico filtro** e si commutano **due quarzi** nell'oscillatore (distanziati di circa 3 kHz):

- **Per USB**: il quarzo genera una frequenza appena **sotto** la banda passante del filtro → la banda laterale superiore passa, l'inferiore viene bloccata
- **Per LSB**: il quarzo genera una frequenza appena **sopra** la banda passante del filtro → la banda laterale inferiore passa, la superiore viene bloccata

La levetta USB/LSB sulla radio semplicemente commuta tra i due quarzi.

#### 🔹 Doppia Conversione di Frequenza

Il segnale SSB è generato a **frequenza fissa** (9 MHz) perché vincolato al filtro a cristallo. Per trasmettere su qualsiasi banda:

1. **Prima conversione** — mixer + **VFO** (es. 5–5,5 MHz): fornisce la copertura di 500 kHz (su questa agisce la manopola di sintonia)
2. **Seconda conversione** — mixer + **oscillatore a cristallo** commutabile: trasla la banda di 500 kHz sulla banda radioamatoriale desiderata (il selettore di banda commuta i cristalli)
3. **Amplificatore lineare** finale

---

### 7. 📻 Trasmettitore AM (⏱ 97:00–99:40)

La modulazione d'ampiezza è la più semplice da realizzare. Il modulatore agisce direttamente sull'**amplificatore finale**, variandone la **tensione di alimentazione** in funzione del segnale microfonico.

- Tensione più alta → più potenza in uscita (picco della modulazione)
- Tensione più bassa → meno potenza in uscita (minimo della modulazione)

> **Esempio**: amplificatore alimentato nominalmente a 12 V. Con modulazione, la tensione varia da 6 V a 18 V seguendo la voce, e la potenza d'uscita varia di conseguenza.

I blocchi dello schema sono gli stessi del trasmettitore generico, con la modulazione applicata allo stadio finale.

---

### 8. 📻 Trasmettitore FM (⏱ 88:53–95:40)

#### 🔹 Schema a Blocchi

1. **Microfono** + **Amplificatore BF**
2. **Filtro limitatore**: limita i picchi del parlato (evita eccessiva deviazione) e inserisce la **pre-enfasi** (compensazione preventiva della distorsione del rivelatore FM che attenua gli acuti)
3. **Modulatore a reattanza** — tipicamente un **diodo varicap** che modifica leggermente la capacità in parallelo al quarzo dell'oscillatore, spostando la frequenza di risonanza in funzione del segnale audio → **modulazione di frequenza**
4. **Catena di moltiplicatori** — amplificatori non lineari che generano armoniche, con prelievo dell'armonica desiderata (×2, ×3, ×5)
5. **Amplificatore finale** (può essere in **classe C** per FM, dato che l'ampiezza è costante)

**Modulatore a reattanza** — circuito che modula un componente reattivo (tipicamente un varicap = reattanza capacitiva) per variare la frequenza dell'oscillatore.

#### 🔹 Moltiplicatori e Deviazione di Frequenza

I moltiplicatori moltiplicano sia la frequenza **sia la deviazione** per lo stesso fattore:

$$\text{Se } f_{osc} \times N = f_{uscita}, \quad \text{allora } \Delta f_{osc} \times N = \Delta f_{uscita}$$

> **Esempio**: oscillatore a 14 MHz con deviazione 600 Hz. Moltiplicazione ×10 → uscita a 140 MHz con deviazione 6 kHz.

Questo spiega perché in FM l'oscillatore lavora a frequenza bassa: la deviazione iniziale è piccola e viene poi amplificata dalla catena di moltiplicatori.

#### 🔹 Filtri per Tipo di Emissione

| Tipo di emissione | Larghezza filtro tipica |
| ----------------- | ----------------------- |
| CW (telegrafia)   | ~500 Hz                 |
| SSB               | ~2,5 kHz                |
| AM                | ~6 kHz                  |
| FM                | ~10 kHz                 |

---

### 9. 📊 Caratteristiche del Trasmettitore

Un trasmettitore è specificato da:

- **Stabilità di frequenza** — deve restare sulla frequenza impostata
- **Larghezza di banda** — deve stare entro la banda assegnata (10 kHz per FM, 2,5 kHz per SSB)
- **Potenza di uscita** — tipicamente 100 W per le radio amatoriali
- **Rendimento** — rapporto tra potenza RF e potenza assorbita
- **Deviazione di frequenza** (FM) o **indice di modulazione** (AM)

---

### 10. ⚠️ Intermodulazione e Splatter (⏱ 100:00–121:00)

#### 🔹 Armoniche e Distorsione

Quando un amplificatore è **sovrapilotato** (pilotato oltre la potenza che può erogare), il segnale sinusoidale viene "appiattito" in cima (**flat-topping**). Questa deformazione genera **armoniche**.

**Armonica** — segnale a frequenza multipla della fondamentale. Un segnale a 27 MHz sovrapilotato genera: 2ª armonica (54 MHz), 3ª armonica (81 MHz), ecc.

Caratteristiche dei diversi segnali:

- **Sinusoide pura** → una sola riga in frequenza, **nessuna armonica**
- **Onda triangolare** → tutte le armoniche (pari e dispari)
- **Onda quadra** → solo armoniche **dispari** (3ª, 5ª, 7ª)
- **Sinusoide con flat-topping** → prevalentemente armoniche **dispari**

Le armoniche singole **non sono un problema** perché sono molto lontane dalla fondamentale → facilmente eliminabili con circuiti risonanti o filtri passa-basso in uscita.

#### 🔹 L'Intermodulazione

**Intermodulazione** — comparsa di frequenze indesiderate in uscita dal trasmettitore, non presenti all'ingresso. Si verifica quando sono presenti **contemporaneamente due condizioni**:

1. L'amplificatore è **sovrapilotato** (va in distorsione/flat-topping)
2. In ingresso ci sono **più segnali** a frequenze diverse (come accade parlando in SSB o AM)

Quando l'amplificatore distorce con più segnali in ingresso ($f_1$ e $f_2$), si comporta come un miscelatore e genera:

- **Somma e differenza** ($f_1 + f_2$, $f_1 - f_2$) → lontane, non problematiche
- **Prodotti del 3° ordine**: $2f_1 - f_2$ e $2f_2 - f_1$ → **molto vicini** alla frequenza di trasmissione!
- **Prodotti del 5° ordine**: $3f_1 - 2f_2$, $3f_2 - 2f_1$ → ancora più vicini
- **Ordini superiori** (7°, 9°…): sempre più componenti indesiderate

> Il "3° ordine" si chiama così perché la somma dei coefficienti è 3 (es. 2+1=3).

#### 🔹 Splatter

**Splatter** — termine usato dai radioamatori per indicare l'allargamento del canale di trasmissione causato dall'intermodulazione. Il segnale "deborda" nei canali adiacenti, disturbando le stazioni vicine in frequenza.

**Dove si verifica**: principalmente in **SSB e AM** (segnali multi-frequenza). **Non** in CW e FM:

- **CW**: una sola frequenza → niente mescolazione tra segnali diversi
- **FM**: ampiezza costante → la distorsione non produce intermodulazione significativa

**Soluzione**: **non sovrapilotare** l'amplificatore finale. Restare entro l'80–90% della potenza massima. Non amplificare eccessivamente il microfono. Se serve più potenza, usare un amplificatore lineare dimensionato adeguatamente piuttosto che "tirare il collo" a uno sottodimensionato.

> Paolo sottolinea: "È molto meglio avere 300 W puliti che non danno noia a nessuno che 100 W sporchissimi che disturbano a 50 km di distanza."

---

## 🔗 Concept Map (testuale)

- **Trasduttore** → si divide in → **microfono** (acustico→elettrico) e **altoparlante** (elettrico→acustico)
- **Microfono dinamico** → funziona come → **altoparlante al contrario**
- **Miscelatore** → produce → **frequenza somma** ($f_1+f_2$) e **frequenza differenza** ($f_1-f_2$)
- **Miscelatore** → è usato per → **conversione di frequenza** nei trasmettitori
- **Trasmettitore** → schema generale → oscillatore → driver (classe A) → finale (classe AB) → accordatore
- **Conversione di frequenza** → permette → copertura **multibanda** con un unico VFO
- **Trasmettitore CW** → usa → tasto telegrafico + circuito anti-click
- **Trasmettitore SSB** → genera segnale con → modulatore bilanciato (sopprime portante) + filtro a cristallo (sopprime banda laterale)
- **Selezione USB/LSB** → avviene cambiando → **quarzo nell'oscillatore** (non il filtro)
- **Trasmettitore FM** → modula con → modulatore a reattanza (varicap) + catena moltiplicatori
- **Moltiplicatore** → moltiplica → sia frequenza sia deviazione per lo stesso fattore
- **Trasmettitore AM** → modula variando → **tensione di alimentazione** del finale
- **Sovrapilotaggio** → genera → **armoniche** (lontane, filtrabili)
- **Sovrapilotaggio + segnali multipli** → genera → **intermodulazione** (vicina, non filtrabile!)
- **Intermodulazione** → causa → **splatter** (allargamento canale, disturbo adiacenti)

---

## 📝 Key Takeaways

1. I **microfoni** trasformano onde acustiche in segnali elettrici; i quattro tipi sono: carbone (storico), cristallo/ceramico (ottimo per radio, enfatizza acuti), condensatore (migliore qualità, richiede alimentazione) e dinamico (buona fedeltà, funziona come altoparlante al contrario).

2. Il **miscelatore** (mixer/mescolatore) ha 2 ingressi e 1 uscita: produce contemporaneamente la frequenza somma e la frequenza differenza dei due segnali in ingresso. È il componente chiave per la conversione di frequenza.

3. Lo schema generale del trasmettitore prevede: oscillatore → catena amplificazione (driver classe A) → amplificatore finale (push-pull classe AB) → accordatore d'antenna (adatta a 50 Ω).

4. In CW multibanda, un **VFO a bassa frequenza** + **mixer** + cristalli diversi permette di coprire tutte le bande con un unico oscillatore variabile. I **click di manipolazione** si evitano smussando i transitori on/off.

5. Nel trasmettitore SSB, il **modulatore bilanciato** sopprime la portante e il **filtro a cristallo** (2,5 kHz) sopprime la banda laterale indesiderata. La selezione USB/LSB avviene commutando il quarzo dell'oscillatore, non cambiando filtro.

6. La **doppia conversione** nell'SSB è necessaria perché il filtro lavora a frequenza fissa (9 MHz): la prima conversione fornisce la copertura di 500 kHz (sintonia), la seconda trasla sulla banda desiderata.

7. Nell'FM, il **modulatore a reattanza** (varicap) sposta la frequenza dell'oscillatore; i **moltiplicatori** aumentano sia la frequenza sia la deviazione per lo stesso fattore. L'amplificatore finale può essere in classe C.

8. L'**intermodulazione** nasce quando l'amplificatore è sovrapilotato E amplifica più segnali contemporaneamente: i prodotti del 3° ordine ($2f_1 - f_2$, $2f_2 - f_1$) cadono vicino alla frequenza di trasmissione e non sono filtrabili.

9. Lo **splatter** è l'allargamento indesiderato del canale causato dall'intermodulazione; si verifica in SSB/AM, non in CW/FM. La soluzione è non sovrapilotare il trasmettitore.

10. L'AM si ottiene nel modo più semplice: variando la **tensione di alimentazione** dell'amplificatore finale in funzione del segnale microfonico.

---

## ❓ Comprehension Questions

1. Qual è la differenza fondamentale tra un microfono a condensatore e uno dinamico, sia nel principio di funzionamento sia nella necessità di alimentazione?

2. Un miscelatore riceve in ingresso un segnale a 7 MHz e uno a 5 MHz. Quali frequenze sono presenti in uscita? Come si seleziona solo quella desiderata?

3. Perché nei trasmettitori CW multibanda l'oscillatore variabile lavora a frequenza bassa (es. 5 MHz) invece che direttamente alla frequenza di trasmissione?

4. Spiega il meccanismo completo della generazione SSB: dal microfono fino al segnale a banda laterale unica. Qual è il ruolo di ciascun blocco?

5. Perché il trasmettitore SSB necessita di doppia conversione di frequenza? Cosa limita la possibilità di generare l'SSB direttamente alla frequenza di trasmissione?

6. Come si seleziona USB o LSB in un trasmettitore SSB con un unico filtro a cristallo? Descrivi il meccanismo dei due quarzi commutabili.

7. In un trasmettitore FM, l'oscillatore lavora a 12 MHz con deviazione 500 Hz. Dopo una catena di moltiplicatori ×12, quale sarà la frequenza e la deviazione in uscita?

8. Perché l'intermodulazione è un problema per SSB e AM ma non per CW e FM? Quali sono le due condizioni che devono coesistere?

9. Cosa sono i prodotti di intermodulazione del 3° ordine e perché sono particolarmente problematici rispetto alle armoniche semplici?

10. Perché è preferibile usare un amplificatore lineare da 300 W "tranquillo" piuttosto che un trasmettitore da 100 W "col collo tirato"?

---

## 📚 Glossary

- **Accordatore d'antenna (pi-greco)** — circuito con 2 condensatori variabili e 1 induttore che adatta l'impedenza di uscita del TX a 50 Ω dell'antenna
- **Altoparlante** — trasduttore che converte segnale elettrico in onda acustica tramite interazione tra magnete permanente e bobina mobile
- **Armonica** — segnale a frequenza multipla intera della fondamentale (2ª, 3ª, 4ª…)
- **Click di manipolazione** — disturbi sui canali adiacenti causati da transizioni troppo rapide on/off del segnale CW
- **Conversione di frequenza** — processo di traslazione di un segnale da una frequenza a un'altra tramite miscelatore
- **Driver (pilota)** — stadi di amplificazione intermedia (classe A) tra oscillatore e finale
- **DSB (Double Side Band)** — segnale a doppia banda laterale, passo intermedio nella generazione SSB
- **Flat-topping** — appiattimento della sinusoide quando l'amplificatore è sovrapilotato
- **Fondamentale** — frequenza principale di un segnale, rispetto alla quale si definiscono le armoniche
- **Intermodulazione** — generazione di frequenze spurie per mescolamento di segnali multipli in un amplificatore distorto
- **Microfono** — trasduttore che converte un'onda acustica in un segnale elettrico
- **Microfono a carbone** — microfono che sfrutta la variazione di resistività di granuli di carbone compressi
- **Microfono a condensatore** — microfono basato sulla variazione di capacità tra armatura fissa e membrana mobile; richiede alimentazione
- **Microfono a cristallo (ceramico)** — microfono basato sull'effetto piezoelettrico del quarzo; enfatizza le frequenze acute
- **Microfono dinamico** — microfono basato su bobina mobile in campo magnetico; funziona come altoparlante al contrario
- **Miscelatore (mixer, mescolatore)** — componente con 2 ingressi e 1 uscita che produce le frequenze somma e differenza dei segnali in ingresso
- **Modulatore a reattanza** — circuito (tipicamente varicap) che modula la frequenza di un oscillatore variando una reattanza capacitiva
- **Modulatore bilanciato** — circuito che genera DSB sopprimendo la portante; quando non si parla, non esce niente
- **Moltiplicatore di frequenza** — amplificatore non lineare che genera armoniche; moltiplica sia frequenza sia deviazione FM
- **Phantom power** — alimentazione fornita attraverso il cavo del microfono a condensatore
- **Pi-greco (π)** — topologia di circuito di adattamento d'impedenza a forma di lettera π
- **Pre-enfasi** — amplificazione preventiva dei toni bassi nel TX FM per compensare la distorsione del rivelatore
- **Prodotti del 3° ordine** — componenti di intermodulazione ($2f_1-f_2$, $2f_2-f_1$) che cadono vicino alla frequenza di trasmissione
- **Splatter** — allargamento del canale di trasmissione causato da intermodulazione, disturba i canali adiacenti
- **Trasduttore** — dispositivo che converte un tipo di energia in un altro (acustica ↔ elettrica)

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo (radiotecnica — trasduttori, miscelatori, trasmettitori, intermodulazione)

---

## 📅 Informazioni Lezione

| Campo                  | Valore                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione**            | 14                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Data**               | 11 giugno 2025                                                                                                                                                                                                                                                                                                                                                                                           |
| **Durata**             | circa 2 ore e 15 minuti                                                                                                                                                                                                                                                                                                                                                                                  |
| **Argomenti trattati** | 6 (quiz, trasduttori, miscelatori, trasmettitori CW/SSB/AM/FM, intermodulazione)                                                                                                                                                                                                                                                                                                                         |
| **Parole chiave**      | trasduttore, microfono, altoparlante, carbone, cristallo, condensatore, dinamico, miscelatore, mixer, frequenza somma, frequenza differenza, conversione di frequenza, trasmettitore, CW, SSB, AM, FM, modulatore bilanciato, filtro a cristallo, doppia conversione, modulatore a reattanza, moltiplicatore, varicap, pi-greco, click manipolazione, armonica, intermodulazione, splatter, flat-topping |
