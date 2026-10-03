---
layout: default
title: "3 - Circuiti Elettrici e Onde Radio"
permalink: /guide-studio/lezione_03.html
---

# 📘 Lezione 03 - Circuiti Elettrici e Onde Radio

> 🎓 **Esame ridotto: lezione non necessaria.** Questa lezione riguarda la Parte A (questioni di natura tecnica, A.1 Elettricità, elettromagnetismo e radiotecnica) del programma d'esame, da cui è esonerato chi ha un titolo previsto dall'art. 5 dell'Allegato 26. Serve per l'esame completo.

## 📌 Panoramica

- **Materia e argomento**: Elettrotecnica e Onde Radio — la corrente alternata: sinusoide, frequenza, periodo, valori caratteristici della tensione alternata, fase. Onde elettromagnetiche, lunghezza d'onda, frequenza, bande.
- **Tempo di studio stimato**: 90–120 minuti
- **Prerequisiti**: Aver studiato le Lezioni 01 e 02 sulla corrente continua.
- **Obiettivi di apprendimento**:
  - Comprendere la differenza tra corrente continua e corrente alternata
  - Conoscere il concetto di sinusoide e i suoi parametri
  - Padroneggiare le grandezze frequenza e periodo e la relazione $f = \frac{1}{T}$
  - Distinguere i diversi modi di esprimere il valore di una tensione alternata: istantanea, efficace, di picco, picco-picco, valor medio
  - Comprendere il concetto di fase, controfase e quadratura tra sinusoidi
  - Comprendere cos'è un'onda radio e un'antenna
  - Applicare la formula per calcolare la lunghezza d'onda ($\lambda = \frac{300}{f}$) e la frequenza
  - Conoscere la suddivisione delle frequenze in bande (LF, MF, HF, VHF, UHF, ecc.)

---

## 📖 Contenuti Teorici

## ⚡ 1. La corrente alternata

La **corrente continua** (CC o DC) è un flusso di cariche elettriche (elettroni) che scorre sempre nello stesso verso, dal polo negativo al polo positivo di un generatore (pila, batteria).

La **corrente alternata** (CA o AC) è una corrente che **inverte il senso di scorrimento** un certo numero di volte nell'unità di tempo. Il generatore non ha un polo fisso positivo e uno fisso negativo.


La corrente alternata è generata da una **tensione alternata** ed è prodotta da dispositivi chiamati **alternatori**.
> 💡 **Nota per i neofiti:** Immaginate un magnete che ruota all'interno di una bobina di filo di rame. Un giro completo del magnete (360°) produce esattamente un ciclo completo della sinusoide. Ecco perché la frequenza è spesso intuitivamente associata ai "giri al secondo".

<div align="center">
  <img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_03/slide-03.jpg" alt="Grafico Corrente Alternata" style="width: 75%;">
</div><br>

### 🔹 L'andamento sinusoidale e non sinusoidale

La **corrente alternata sinusoidale** ha una forma "sinuosa": parte da zero, sale a un picco massimo, scende con continuità fino a un minimo (negativo), poi risale.

Esistono anche forme d'onda **non sinusoidali**, come l'onda quadra o l'onda triangolare, ma le sinusoidi sono fondamentali in ambito radio.

<div align="center">
  <img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_03/slide-07.jpg" alt="Sinusoide e non sinusoidale" style="width: 75%;">
</div><br>

---

## 📈 2. Frequenza e periodo

### 🔹 Frequenza

La **frequenza** — simbolo $f$ — è il numero di cicli completi che un'onda compie in un secondo. Si misura in **hertz** (Hz).


### 🔹 Periodo

Il **periodo** — simbolo $T$ — è il tempo necessario perché la sinusoide compia un ciclo completo. Si misura in **secondi** (s).


### 🔹 Relazione tra frequenza e periodo

Frequenza e periodo sono **l'inverso** l'uno dell'altro:

$$f = \frac{1}{T} \qquad\qquad T = \frac{1}{f}$$


---

## 📊 3. I valori della tensione alternata

Con la corrente alternata, dato che la tensione varia continuamente, servono **più parametri** per descriverla:


1. **Tensione istantanea**: il valore in un preciso istante di tempo.
2. **Tensione efficace (RMS)**: il valore che, applicato a un carico, produce lo **stesso lavoro** di una tensione continua equivalente. Matematicamente si calcola come: $V_{eff} = \frac{V_p}{\sqrt{2}} \approx 0{,}707 \times V_p$.
> 💡 **Esempio Pratico:** Quando diciamo che la tensione della presa di casa è "230V", stiamo parlando del valore *efficace*. In realtà, la tensione di *picco* raggiunge circa i 325V!


3. **Tensione di picco ($V_p$)**: il valore massimo raggiunto dalla sinusoide. $V_p = 1{,}41 \times V_{eff}$
4. **Tensione picco-picco ($V_{pp}$)**: l'escursione totale, dal minimo al massimo. $V_{pp} = 2 \times V_p$
5. **Valor medio ($V_m$)**: media in un semiperiodo. $V_m = 0{,}9 \times V_{eff}$

<div align="center">
  <img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_03/slide-17.jpg" alt="Riepilogo Valori" style="width: 75%;">
</div><br>

---

## 🔄 4. La fase tra sinusoidi

Ogni punto del ciclo di una sinusoide può essere identificato con un **angolo in gradi**.
> 💡 **Analogia della Pista di Atletica:** Immagina due corridori che fanno giri continui su una pista di atletica. Se partono insieme e corrono alla stessa velocità, sono "in fase" (0° di distanza). Se uno parte quando l'altro è esattamente a metà pista (mezzo giro di ritardo, ovvero 180°), sono in "controfase". Se uno ha un quarto di giro di vantaggio (90°), sono "in quadratura".

<div align="center">
  <img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_03/slide-18.jpg" alt="Punti notevoli" style="width: 75%;">
</div><br>

- **In fase**: raggiungono simultaneamente picchi e zeri. Sfasamento = 0°.
- **In controfase**: sfasamento di **180°**. Se si sommano, si annullano.
- **In quadratura**: sfasamento di **90°**.

<div align="center">
  <img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_03/slide-19.jpg" alt="Fase" style="width: 75%;">
</div><br>

---

## 📡 5. Onde Radio e Propagazione

### 🔹 Cos'è un'onda radio

Un'onda è una perturbazione che si propaga nello spazio (come un sasso in uno stagno).

<div align="center">
  <img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_03/slide-22.jpg" alt="Onde" style="width: 75%;">
</div><br>

Una tensione sinusoidale su un conduttore di forma e dimensioni adeguate, comunica energia allo spazio circostante sotto forma di **onde elettromagnetiche**. Questo conduttore è l'**antenna**.

<div align="center">
  <img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_03/slide-23.jpg" alt="Antenna" style="width: 75%;">
</div><br>

### 🔹 Lunghezza d'onda e Frequenza

La **lunghezza d'onda ($\lambda$)** è la distanza fisica fra due punti omologhi dell'onda elettromagnetica. Dipende dalla velocità di propagazione (la velocità della luce: 300.000 km/s nel vuoto).

$$\lambda = \frac{300.000}{F\text{ (in kHz)}} = \frac{300}{F\text{ (in MHz)}}$$


Esempio:
Frequenza = 14,200 MHz $\rightarrow \lambda = \frac{300}{14,2} = 21,12$ m.


### 🔹 Bande di Frequenza

Le frequenze radio sono suddivise in **bande**: LF, MF, HF, VHF, UHF, ecc. 
Ad esempio, le **HF** (High Frequency) vanno da 3 a 30 MHz (onde corte), le **VHF** (Very High Frequency) da 30 a 300 MHz (onde ultracorte).

<div align="center">
  <img src="/ari-crt-corso-2025/assets/images/lezioni/lezione_03/slide-28.jpg" alt="Bande" style="width: 75%;">
</div><br>

---

## 🔗 Mappa Concettuale

- Tensione alternata → genera → corrente alternata che inverte periodicamente il verso.
- Alternatore → produce → tensione alternata, spesso descritta con una sinusoide.
- Ciclo della sinusoide → determina → periodo $T$; numero di cicli al secondo → determina → frequenza $f$.
- Frequenza e periodo → sono inversi → $f = \frac{1}{T}$.
- Tensione di picco → determina → tensione efficace e tensione picco-picco della sinusoide.
- Sfasamento tra sinusoidi → distingue → segnali in fase, in quadratura e in controfase.
- Tensione sinusoidale applicata a un'antenna → irradia → onde elettromagnetiche.
- Frequenza dell'onda → determina inversamente → lunghezza d'onda; intervalli di frequenze → costituiscono → bande radio.

---

## 📝 Punti Chiave

1. La **corrente alternata** inverte periodicamente il senso di scorrimento.
2. **Frequenza** ($f$) e **periodo** ($T$) sono inversamente proporzionali: $f = 1/T$.
3. I valori della tensione alternata includono: **efficace** (usato nei calcoli pratici), **di picco**, e **picco-picco**.
4. Due segnali possono avere una **differenza di fase** (in fase, quadratura, controfase).
5. Un'antenna trasforma la corrente alternata in **onde elettromagnetiche**.
6. La **lunghezza d'onda** ($\lambda$) e la **frequenza** ($f$) sono legate dalla velocità della luce: $\lambda = 300 / f$ (con f in MHz).
7. Lo spettro radio è suddiviso in bande (MF, HF, VHF, UHF, ecc.).

---

## 📝 Quiz di Verifica

<details>
<summary><b>1. Se una radio trasmette a 144 MHz, qual è la lunghezza d'onda approssimativa?</b></summary>
Circa 2 metri. (Applica la formula $\lambda = 300 / 144 \approx 2{,}08$ m).
</details>

<details>
<summary><b>2. La tensione di rete è 230V (efficaci). Qual è la tensione di picco approssimativa?</b></summary>
Circa 325V ($230 \times 1{,}41$).
</details>

<details>
<summary><b>3. Se due segnali sono sfasati di 180° e hanno la stessa ampiezza, cosa succede se vengono sommati?</b></summary>
Si annullano a vicenda (sono in controfase, quindi quando uno è al suo picco positivo, l'altro è al suo picco negativo).
</details>

---

## ❓ Domande di Comprensione

1. Perché una batteria mantiene un verso di scorrimento della corrente, mentre una tensione alternata ne provoca l'inversione?
2. Se il periodo di una sinusoide si dimezza, come cambia la sua frequenza e quale relazione permette di spiegarlo?
3. Perché il solo valore istantaneo non basta a descrivere una tensione alternata e quando è utile conoscerne il valore efficace?
4. Come ricaveresti il valore di picco e quello picco-picco conoscendo la tensione efficace di una sinusoide?
5. In che modo lo sfasamento distingue due sinusoidi in fase, in quadratura e in controfase? Che cosa accade sommando due segnali uguali in controfase?
6. Quale ruolo svolge l'antenna nel passaggio dalla tensione alternata alle onde elettromagnetiche?
7. Perché una frequenza maggiore corrisponde a una lunghezza d'onda minore e come useresti questa relazione per confrontare un segnale HF con uno VHF?

---

## 📚 Glossario

- **Alternatore** — Dispositivo che produce tensione alternata.
- **Antenna** — Conduttore di forma e dimensioni adeguate che comunica energia allo spazio circostante sotto forma di onde elettromagnetiche.
- **Banda di frequenza** — Intervallo dello spettro radio identificato da una denominazione come HF o VHF.
- **Controfase** — Relazione tra due sinusoidi sfasate di 180°; se uguali e sommate, si annullano.
- **Corrente alternata (CA)** — Corrente che inverte periodicamente il proprio verso di scorrimento.
- **Corrente continua (CC)** — Corrente che scorre sempre nello stesso verso.
- **Fase** — Posizione di una sinusoide nel suo ciclo, esprimibile mediante un angolo.
- **Frequenza** — Numero di cicli completi di un'onda in un secondo, misurato in hertz.
- **Hertz (Hz)** — Unità di misura della frequenza.
- **Lunghezza d'onda ($\lambda$)** — Distanza fisica tra due punti omologhi di un'onda elettromagnetica.
- **Onda elettromagnetica** — Forma di energia che si propaga nello spazio quando un'antenna è alimentata da una tensione sinusoidale.
- **Periodo ($T$)** — Tempo necessario a compiere un ciclo completo di una sinusoide.
- **Quadratura** — Relazione tra due sinusoidi sfasate di 90°.
- **Sinusoide** — Forma d'onda che varia con continuità tra un massimo e un minimo.
- **Tensione alternata** — Tensione il cui verso cambia periodicamente e che genera corrente alternata.
- **Tensione di picco ($V_p$)** — Valore massimo raggiunto dalla sinusoide.
- **Tensione efficace (RMS)** — Valore di tensione alternata che produce su un carico lo stesso lavoro di una tensione continua equivalente.
- **Tensione istantanea** — Valore della tensione alternata in un preciso istante.
- **Tensione picco-picco ($V_{pp}$)** — Escursione totale della tensione dal minimo al massimo.
- **Valor medio ($V_m$)** — Media della tensione alternata in un semiperiodo.

---

## 👥 Partecipanti

- 👨‍🏫 **Relatore**: Paolo (Paolo Cavecchioli, docente del corso)

---

## 📅 Informazioni Lezione

- **Numero Lezione**: 03
- **Data**: 01/04/2026
- **Keywords**: corrente alternata, sinusoide, frequenza, periodo, hertz, tensione efficace, fase, onde radio, lunghezza d'onda, bande HF VHF UHF, antenna.
