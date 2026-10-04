---
layout: default
title: "16 - Linee di Trasmissione RF"
permalink: /guide-studio/lezione_16.html
---

# 📘 Lezione 16 - Linee di Trasmissione RF

## 📌 Panoramica

- **Materia**: Antenne, propagazioni, linee di trasmissione
- **Argomento principale**: La teoria delle linee RF, linee in regime di Onde Stazionarie, adattamento di impedenza e misure sulle linee.
- **Relatore**: Paolo (i5WHC)
- **Data**: 2 Settembre 2026

---

## 📖 Contenuti Teorici

### 1. La teoria delle linee RF

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-03.jpg" alt="Teoria linee RF" style="width: 75%;"></div><br>

In generale si definisce **"Linea di Trasmissione"** la coppia di conduttori che collegano il generatore al carico.
Se la lunghezza della linea è trascurabile rispetto alla lunghezza d'onda del segnale elettrico, la distribuzione delle tensioni e correnti è uniforme e si applicano le regole dei circuiti classici.
Tuttavia, quando le dimensioni del circuito non sono trascurabili rispetto alla lunghezza d'onda, la distribuzione non è uniforme, e occorre applicare la "Teoria delle Linee di Trasmissione".

La formula della lunghezza d'onda è:
$$\lambda(m) = \frac{300}{F(MHz)}$$

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-04.jpg" alt="Lunghezza onda" style="width: 75%;"></div><br>

Ciascun conduttore della linea presenta un'**induttanza distribuita** e tra i conduttori vi è una **capacità distribuita**. Pertanto, la linea si assimila ad un **circuito LC a costanti distribuite**.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-06.jpg" alt="Circuito LC a costanti distribuite" style="width: 75%;"></div><br>

Se consideriamo una linea di lunghezza infinita, essa presenta al generatore un'impedenza $Z_0$ (Impedenza Caratteristica) pari a:
$$Z_0 = \sqrt{\frac{L}{C}}$$
dove L è l'induttanza per unità di lunghezza e C la capacità per unità di lunghezza.
> 💡 **Nota Pratica:** Se misuriamo un cavo coassiale con un tester in corrente continua (CC), leggeremo un circuito aperto (resistenza infinita tra centrale e calza). Invece, per il segnale RF (corrente alternata ad alta frequenza), il cavo presenta un "carico" dinamico di 50 $\Omega$ determinato dalla sua geometria (capacità e induttanza), non dalla resistenza elettrica del rame!

Se chiudiamo una linea reale con un carico $Z = Z_0$, essa si comporta come se fosse infinita, in regime di sola **onda progressiva**.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-07.jpg" alt="Impedenza caratteristica" style="width: 75%;"></div><br>

#### Cavi Coassiali vs Linee Bifilari
I **cavi coassiali** hanno il conduttore esterno che scherma i campi EM, impedendo interferenze con l'esterno, ma presentano maggiore attenuazione rispetto alle linee bifilari. Si usano per collegare generatori e carichi **sbilanciati** (con un terminale a terra). 
Le linee bifilari si usano per carichi **bilanciati**. Per passare da sbilanciato a bilanciato si utilizza un **Balun**.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-10.jpg" alt="Cavi coassiali e bifilari" style="width: 75%;"></div><br>

#### Parametri della linea:
- **Impedenza caratteristica ($Z_0$)**: 50-75 $\Omega$ per coax, 200-300 $\Omega$ per bifilari.
- **Attenuazione**: espressa in dB/m.
- **Fattore di velocità ($F_v$)**: La velocità in linea è inferiore a quella nel vuoto. 
La lunghezza d'onda fisica è minore: 
*Lunghezza Fisica* = *Lunghezza Elettrica* ($\lambda$) $\times$ *Fattore di velocità*

---

### 2. Linee in regime di Onde Stazionarie

Se un carico $Z_L$ è diverso da $Z_0$, parte dell'energia viene riflessa, creando un regime di **Onde Stazionarie**.
> 💡 **Analogia Idraulica:** Immagina un'onda d'acqua in un canale stretto. Se alla fine del canale c'è uno scivolo (carico adattato), l'onda prosegue e cede la sua energia. Se invece c'è un muro (disadattamento), l'onda sbatte e torna indietro. L'onda di ritorno si sovrappone a quella in arrivo creando punti in cui l'acqua è sempre ferma (nodi) e punti in cui oscilla col doppio della forza (ventri). Queste sono le "Onde Stazionarie".

La composizione del flusso diretto e riflesso genera massimi e minimi di tensione e corrente che si ripetono ogni $\lambda/2$.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-16.jpg" alt="ROS Onde stazionarie" style="width: 75%;"></div><br>

Si definisce **ROS** (Rapporto di Onde Stazionarie) o SWR:
$$ROS = \frac{V_{max}}{V_{min}}$$
Se $Z_L < Z_0$, $ROS = \frac{Z_0}{Z_L}$. Se $Z_L > Z_0$, $ROS = \frac{Z_L}{Z_0}$.
Il valore del ROS varia tra 1 e infinito.

Lungo la linea in onde stazionarie, l'impedenza vista varia al variare della lunghezza elettrica. 

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-19.jpg" alt="Impedenza lungo la linea" style="width: 75%;"></div><br>

---

### 3. Il trasformatore $\lambda/4$ e i tronchi di linea

Un tronco di linea lungo $\lambda/4$ si comporta da **trasformatore di impedenza**. Per adattare $Z_1$ e $Z_2$, occorre una linea a $\lambda/4$ con impedenza:
$$Z_0 = \sqrt{Z_1 \times Z_2}$$

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-21.jpg" alt="Trasformatore quarto d onda" style="width: 75%;"></div><br>

- Linea aperta a $\lambda/4$ si comporta come un **circuito risonante serie**.
- Linea in corto circuito a $\lambda/4$ si comporta come un **circuito risonante parallelo**.

---

### 4. Adattamento di impedenza e misure

#### Legge di Jacobi
Il teorema del massimo trasferimento di potenza stabilisce che la massima potenza si trasferisce quando l'impedenza del carico è pari al **complesso coniugato** dell'impedenza interna del generatore (stessa parte resistiva, parte reattiva opposta).

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-25.jpg" alt="Legge di Jacobi" style="width: 75%;"></div><br>

#### Accordatore (ATU)
Utilizzato per adattare i valori di impedenza. La condizione ottimale è piazzarlo vicino all'antenna. Se piazzato al trasmettitore, protegge il TX ma la linea resta disadattata e con alta attenuazione e sollecitazioni.

#### Misura del ROS
Tra Potenza Diretta ($P_d$) e Potenza Riflessa ($P_r$):
$$ROS = \frac{1 + \sqrt{P_r / P_d}}{1 - \sqrt{P_r / P_d}}$$

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-27.jpg" alt="Misura del ROS" style="width: 75%;"></div><br>

**Attenzione all'attenuazione del cavo**: se si misura il ROS all'uscita del TX e il cavo ha elevata attenuazione, il ROS misurato sarà **più basso** del ROS reale all'antenna (perché sia la potenza diretta in arrivo, sia quella riflessa di ritorno, vengono attenuate dal cavo).
> ⚠️ **Importante:** Un cavo molto lungo o scadente può nascondere un'antenna rotta! Se il ROS reale all'antenna è altissimo, ma il cavo perde molta potenza, l'onda riflessa arriverà al trasmettitore così attenuata che il rosmetro segnerà un innocuo 1,5:1. Misurate sempre il ROS il più vicino possibile all'antenna quando fate dei test.

<div align="center"><img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_16/slide-29.jpg" alt="Attenuazione del cavo" style="width: 75%;"></div><br>

#### Attenuazione in decibel (dB)
Usare i dB semplifica i calcoli perché permette di sommare i guadagni e sottrarre le attenuazioni.
$$A(dB) = 10 \log_{10} \frac{P_{uscita}}{P_{ingresso}}$$

---

## 📝 Come presentare la domanda d'esame

All'inizio della serata, prima di passare alla parte tecnica, il coordinatore del corso dedica una decina di minuti alla **domanda di partecipazione all'esame**. La scadenza indicata a lezione è il **10 ottobre**; il consiglio è di presentare la domanda nella prima quindicina di settembre, così che eventuali problemi tecnici o di altra natura si possano risolvere senza arrivare a ridosso del termine. Chi ha già inviato la domanda con la vecchia procedura non deve rifarla: la domanda resta valida.

### 🔹 La nuova versione del portale

Il **portale** del MIMIT per la richiesta di patente è stato aggiornato il 28 luglio con una nuova versione, operativa dalla prima settimana di agosto, che semplifica la procedura. Non servono più le **marche da bollo** da acquistare in anticipo né il versamento preventivo di 25 € sulla piattaforma dei pagamenti: tutto si fa dentro il portale, pagamento compreso, in pochi minuti. Nelle linee guida in PDF predisposte da un collega di Catania, che vengono mostrate a lezione e inviate agli allievi il giorno dopo, le parti sull'acquisto delle marche e sul versamento iniziale non sono quindi più valide; il resto resta com'è. L'indirizzo del portale è cambiato: chi ha usato quello vecchio non deve preoccuparsi, perché la domanda è stata comunque registrata, mentre su Internet possono restare indicazioni obsolete.

> ⚠️ *Questa sezione potrebbe essere incompleta nella trascrizione di origine.* L'indirizzo del portale e i dettagli della schermata non sono leggibili nella trascrizione automatica.

### 🔹 Accesso e scelta del tipo di richiesta

Per entrare nel portale ci si autentica con **SPID** o **CIE** (nella trascrizione automatica compaiono come «Speed» e «CE»): i dati personali presenti nel sistema di autenticazione vengono importati automaticamente. Dalla schermata iniziale si sceglie la voce **richiesta patente**, si accetta l'informativa sulla privacy e si entra nella richiesta di esame, dove bisogna scegliere con attenzione tra **tre tipi di richiesta**:

- **esame con esonero parziale**, per chi possiede un titolo di studio che consente di non sostenere le domande sulla parte tecnica del programma; il titolo va dichiarato e allegato;
- **esame senza esonero parziale** (esame completo);
- **richiesta di ammissione all'esame per un minore**.

In basso a sinistra c'è un tasto **Salva**, da usare ogni volta che si raggiunge un punto soddisfacente: rientrando, la procedura riprende da lì senza ripartire dall'inizio.

### 🔹 Dati richiesti

La prima informazione da indicare è l'**ispettorato territoriale** presso cui si farà l'esame (Toscana per i toscani, Liguria per i liguri), che porta con sé le informazioni relative. Occorre poi completare i **dati anagrafici**, compresi i campi e-mail e **PEC**. La **PEC non è obbligatoria**: chi non la possiede può indicare nel campo il normale indirizzo di posta elettronica. Nella parte dichiarativa chi avesse già pagato i 25 € con la vecchia procedura può dichiarare di avere assolto l'adempimento (in tal caso il portale chiederà di allegare la ricevuta); chi non l'ha fatto non lo dichiara.

### 🔹 Invio, pagamento e allegati

Raggiunta la parte finale, si entra nella sezione per l'invio di domande e documenti e si invia la domanda. Rientrando nel portale, che conserva anche la storia radioamatoriale dell'utente (patente, licenza, rinnovi), la richiesta di partecipazione all'esame compare come primo rigo e risulta **incompleta**. Tramite i tre pallini a destra del rigo si apre la maschera di completamento, dove si effettua il **pagamento unico**: i 25 € del contributo più i 16 € della marca da bollo richiesta in tutte le istanze alla pubblica amministrazione, in totale **41 €**, tramite **pagoPA** con i consueti metodi di pagamento. Il versamento avviene dentro il sistema, che lo riconosce da solo: la ricevuta non va allegata e la si conserva soltanto per sé. A questo punto la pratica passa all'ispettorato territoriale del MIMIT competente, che invita all'esame.

Nella fase finale c'è una sezione per caricare gli **allegati**, preferibilmente in **PDF** (anche una scansione o una foto). Vi si può caricare:

- il **titolo di studio**, per chi chiede l'esonero parziale;
- le **certificazioni** di condizioni (per esempio di salute) che giustificano un esame diverso o non in presenza;
- la certificazione di una condizione come l'ipovisione, che dà diritto al **40% di tempo in più** per l'esame.

I casi particolari che possono dar luogo a un allegato si trovano descritti nelle linee guida.

### 🔹 Domande dei corsisti

- **Autocertificazione del diploma**: a una domanda sulla possibilità di autocertificare il diploma, il coordinatore risponde che l'ispettorato richiede di contattare l'istituto in cui si è conseguito il titolo e di farsi rilasciare una **certificazione**; «è sempre stato così finora».
- **Domanda già presentata in passato**: chi ha presentato la domanda in anni precedenti (a lezione si cita il 2024) e non ha potuto sostenere l'esame resta in coda, nella lista di attesa; non deve rifare la domanda. Il consiglio è di scrivere o telefonare al MIMIT nella prima decade di ottobre per confermare la propria partecipazione.
- **Diploma già in possesso**: chi ha il diploma (per esempio di elettrotecnica) lo allega come foto o, meglio, come PDF.

> ⚠️ *Questa sezione potrebbe essere incompleta nella trascrizione di origine.* Le cifre (25 €, 16 €, 41 €, 40%) e le date (28 luglio, 10 ottobre) sono riportate come dette a lezione; nella trascrizione automatica alcuni passaggi sono confusi (per esempio sull'anno della domanda citata da un corsista e sulla distinzione tra titoli di studio e altre certificazioni). Per le condizioni valide e i dettagli aggiornati fa fede il portale.

---

## 🔗 Mappa Concettuale

- Linea di trasmissione → unisce TX e antenna
- Modello linea → Circuito LC a costanti distribuite
- Impedenza caratteristica $Z_0$ → per linea adatta, potenza si trasferisce integralmente (onda progressiva)
- Cavo coassiale → sbilanciato, schermato
- Linea bifilare → bilanciata (serve un Balun per TX sbilanciato)
- Onde stazionarie → generate dal disadattamento $Z_L \neq Z_0$
- ROS = Rapporto tra Vmax e Vmin lungo la linea
- Trasformatore $\lambda/4$ → adatta impedenze
- Legge di Jacobi → massimo trasferimento di potenza se $Z_{carico}$ è complesso coniugato di $Z_{generatore}$
- SWR Meter → rileva potenza diretta e riflessa per calcolare il ROS
- Attenuazione cavo → falsa la misura del ROS facendola apparire inferiore se effettuata dal lato TX

---

## 📝 Quiz di Verifica

<details>
<summary><b>1. Perché il tester (multimetro in CC) non può misurare l'impedenza caratteristica di 50 $\Omega$ di un cavo coassiale?</b></summary>
Perché l'impedenza caratteristica è un parametro dinamico in Radiofrequenza (Corrente Alternata), dipendente dalla capacità e induttanza distribuite nel cavo. Il tester in Corrente Continua misurerà solo la resistenza resistiva, indicando circuito aperto.
</details>

<details>
<summary><b>2. Se misuro un ROS di 1:1 all'uscita della radio, posso essere certo che l'antenna sia perfettamente accordata?</b></summary>
No. Se il cavo coassiale ha molta attenuazione, gran parte dell'energia riflessa da un'antenna disadattata verrebbe dissipata prima di tornare alla radio, mostrando un falso basso ROS.
</details>

---

## 📅 Informazioni Lezione

| Campo                | Valore                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lezione**          | 16                                                                                                                                                                                                                                    |
| **Data**             | 2 Settembre 2026                                                                                                                                                                                                                      |
| **Parole chiave**    | Linee di trasmissione, impedenza caratteristica, ROS, onde stazionarie, cavo coassiale, Balun, trasformatore quarto d'onda, attenuazione, decibel, legge di Jacobi. |

