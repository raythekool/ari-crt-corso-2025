---
layout: default
title: "Antenne - Parte Seconda"
permalink: /guide-studio/lezione_19.html
---

# 📘 Lezione 19 - Antenne (Parte Seconda)

## 📌 Panoramica

- **Materia**: Antenne direttive, Efficienza di radiazione, Balun, Misure sulle antenne
- **Tempo di studio stimato**: 90–110 minuti
- **Prerequisiti**: Concetti base sulle antenne (Lezione precedente), propagazione elettromagnetica
- **Obiettivi di apprendimento**:
  - Comprendere i principi delle antenne direttive (Yagi, Array, Parabole) e calcolare l'ERP
  - Valutare l'efficienza di radiazione, la resistenza di radiazione e le perdite (effetto pelle, perdite nel terreno)
  - Imparare il ruolo essenziale del Balun / RF Choke
  - Interpretare correttamente le misure strumentali (Analizzatori e VNA) tenendo conto delle linee di alimentazione
  - Distinguere le esigenze di un sistema d'antenna tra trasmissione e ricezione

---

## 📖 Contenuti Teorici

### 1. 📡 Antenne Direttive (Guadagno ed ERP)

La modifica del lobo di radiazione di un’antenna non è solo un effetto indesiderato dovuto all'ambiente, ma può essere sfruttato per concentrare l'energia irradiata in una determinata direzione. Questo aumenta le probabilità di collegamento verso il nostro corrispondente.

<div align="center"><img src="../assets/images/lezioni/lezione_19/slide-04.jpg" alt="Lobo di radiazione antenne direttive" width="50%"></div><br>

**Il Guadagno di un'antenna:**
Si definisce guadagno il rapporto tra l’intensità del campo emesso nella direzione del lobo principale e quella di un'antenna di riferimento (radiatore isotropico o dipolo ideale). 
- Viene espresso in **dBi** (riferito al radiatore isotropico puntiforme)
- Può essere espresso in **dBd** (riferito al dipolo ideale) 
> *Nota: la differenza tra i due valori è pari a 2,1 dB (0 dBd = 2,1 dBi).*

<div align="center"><img src="../assets/images/lezioni/lezione_19/slide-05.jpg" alt="Guadagno di un'antenna" width="50%"></div><br>

**Metodi per ottenere la direttività:**
1. **Specchio parabolico**: Una superficie riflettente pone l'elemento radiante nel suo fuoco, concentrando l'energia in un fascio parallelo all'asse.
2. **Antenna Yagi-Uda**: Utilizza elementi "parassiti" passivi accoppiati per mutua induzione. Regolando le distanze e le lunghezze si sfasano le correnti per sommare i campi in una precisa direzione.
3. **Array / Collineari**: Più elementi attivi alimentati con la giusta fase per sommare i fasci emessi. Un esempio sono le antenne Log-Periodiche.

<div align="center"><img src="../assets/images/lezioni/lezione_19/slide-08.jpg" alt="Antenna Yagi Uda e mutua induzione" width="50%"></div><br>

#### 🔹 ERP (Effective Radiated Power)
L'ERP indica la potenza che andrebbe applicata a un radiatore isotropico ideale per ottenere lo stesso campo generato dalla nostra antenna direttiva:
$$ERP(W) = P_{tx}(W) \times Guadagno$$
*(Se il guadagno è in dB, il moltiplicatore è $10^{\frac{G(dB)}{10}}$)*

---

### 2. ⚡ Efficienza di Radiazione e Perdite

Affinché le cariche elettriche circolino correttamente, è necessario un "percorso di ritorno". Nelle antenne sbilanciate serve un contrappeso, ma anche in quelle bilanciate (come il dipolo) accoppiamenti parassiti possono far fluire la RF sulla calza del cavo coassiale (correnti di modo comune). 

<div align="center"><img src="../assets/images/lezioni/lezione_19/slide-13.jpg" alt="Correnti di modo comune e necessità di blocco RF" width="50%"></div><br>

**Cos'è l'efficienza di radiazione?**
Nessuna antenna reale irradia il 100% della potenza fornita. L'efficienza $\eta_r$ è il rapporto percentuale tra la potenza effettivamente irradiata ($P_{ir}$) e quella fornita al punto di alimentazione ($P_{Tx}$). 

$$ \eta_r = \frac{R_{rad}}{R_{rad} + R_{loss}} $$

<div align="center"><img src="../assets/images/lezioni/lezione_19/slide-17.jpg" alt="Resistenza di radiazione e di perdita" width="50%"></div><br>

Dove:
- **$R_{rad}$ (Resistenza di radiazione)**: la componente utile, rappresenta la potenza irradiata.
- **$R_{loss}$ (Resistenza di perdita)**: la somma delle perdite ohmiche e nel terreno.

Le cause principali di $R_{loss}$ includono:
- **Effetto pelle (Skin effect)**: Aumentando la frequenza, la corrente RF scorre solo sulla superficie esterna del conduttore, riducendo la sezione utile e aumentando la resistenza elettrica ($R_c$). Filari sottili sono più colpiti rispetto ai tubi in alluminio.
- **Perdite nel terreno ($R_g$)**: Antenne posizionate basse (sotto $\lambda/4$) inducono correnti in un terreno dissipativo. Le verticali necessitano sempre di molti radiali per limitare questa perdita.

---

### 3. 🔌 L'Uso del Balun

Per interfacciare un'antenna bilanciata e una linea sbilanciata (cavo coassiale), si usa il **BALUN** (Balanced to Unbalanced).

Un Balun svolge spesso tre funzioni chiave (specialmente il *Balun di Corrente* o *Guanella Choke*):
1. **Adattare l'equilibrio**: Bilanciato verso sbilanciato.
2. **Adattamento di impedenza**: Trasformare l'impedenza dell'antenna verso quella del cavo (es. 4:1, 9:1).
3. **Blocco RF (Choke)**: Impedire alle correnti RF di viaggiare sulla guaina esterna del cavo coassiale, evitando di irradiare in stazione (RFI) e migliorando il diagramma di radiazione.

<div align="center"><img src="../assets/images/lezioni/lezione_19/slide-15.jpg" alt="Funzioni del Balun" width="50%"></div><br>

---

### 4. 🎛️ SWR e Misure sulle Antenne

**SWR non è sinonimo di efficienza!**
Come disse John Devoldere (ON4UN): *"L'antenna con il miglior SWR è un buon carico fittizio"*. Un basso ROS assicura solo il corretto trasferimento di potenza alla linea senza onde riflesse al generatore, ma se tale potenza viene dissipata in calore (alte perdite $R_{loss}$ e bassa $R_{rad}$), l'antenna non irradierà quasi nulla. 

<div align="center"><img src="../assets/images/lezioni/lezione_19/slide-24.jpg" alt="SWR e carico fittizio" width="50%"></div><br>

#### 🔹 Misurazione con Analizzatori d'Antenna e VNA
Quando misuriamo l'impedenza dal fondo di un cavo coassiale, la lunghezza della linea trasforma l'impedenza. Se l'antenna non presenta esattamente 50 $\Omega$ puri e la linea non è un esatto multiplo di $\lambda/2$, lo strumento (analizzatore o VNA) misurerà valori **diversi** dall'impedenza reale ai morsetti dell'antenna, introducendo reattanze fittizie. Strumenti avanzati (VNA) permettono di impostare il "delay" o la lunghezza elettrica del cavo per spostare il piano di calibrazione matematicamente fino all'antenna.

<div align="center"><img src="../assets/images/lezioni/lezione_19/slide-29.jpg" alt="Misurazione attraverso linea sbilanciata" width="50%"></div><br>

---

### 5. 📉 Ottimizzazione TX vs RX

Spesso si crede che un'antenna ottima in trasmissione lo sia anche in ricezione, ma non sempre è così (soprattutto nelle bande HF inferiori).
- **In TX (Trasmissione)**: L'obiettivo è massimizzare l'energia irradiata utile, quindi l'efficienza e il guadagno puntato ad angoli bassi (0°-20° per il DX).
- **In RX (Ricezione)**: L'obiettivo è migliorare il **Rapporto Segnale/Rumore (S/N)**. Un guadagno elevato in RX amplifica anche il forte rumore ambientale HF (che spesso supera il limite di sensibilità). L'approccio migliore è ottimizzare la *direttività spaziale* per minimizzare i segnali da angoli non voluti (attenuazione dei disturbi), a prescindere dal guadagno assoluto.

<div align="center"><img src="../assets/images/lezioni/lezione_19/slide-31.jpg" alt="Antenne TX vs RX e S/N" width="50%"></div><br>
