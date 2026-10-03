# 📚 ARI CRT - Corso Radioamatori 2025

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/raythekool/ari-crt-corso-2025)
[![Cloudflare Pages](https://img.shields.io/badge/Cloudflare-Pages-F38020?logo=cloudflare)](https://pages.cloudflare.com/)
[![Astro](https://img.shields.io/badge/Astro-Sito-FF5D01?logo=astro)](https://astro.build/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Sito del corso basato su **Astro** + Starlight, pubblicato su GitHub Pages e Cloudflare Pages.

---

## 🚀 Quick Start

### Clona il repository
```bash
git clone https://github.com/raythekool/ari-crt-corso-2025.git
cd ari-crt-corso-2025
```

---

## 🏗️ Struttura del Progetto

```
ari-crt-corso-2025/
├── README.md             # Questa documentazione
├── site/                 # Codice sorgente del sito Astro
│   ├── astro.config.mjs  # Configurazione Astro
│   ├── package.json      # Dipendenze Node.js
│   ├── public/           # Asset statici
│   ├── scripts/          # Script di build (og.mjs)
│   └── src/              # Pagine, contenuti (lezioni) e stili
├── scripts/              # Estrazione slide dai PDF
├── slides 2026/          # Slide PDF delle lezioni
└── transcripts/          # Trascrizioni delle lezioni
```

---

## 🔧 Build e Deploy

GitHub Pages: workflow [`deploy.yml`](.github/workflows/deploy.yml) su push a `main`.

### Cloudflare Pages

| Impostazione               | Valore          |
| -------------------------- | --------------- |
| Production branch          | `main`          |
| Root directory             | `site`          |
| Build command              | `npm run build` |
| Build output directory     | `dist`          |
| `NODE_VERSION` (opzionale) | `22.19.0`       |

---

## 📦 Installazione Locale

### Prerequisiti
- 🟢 **Node.js 22.12+** (per Astro)
- 📦 **npm** (incluso con Node.js)

Per usare `scripts/extract_slides.py`, installare le dipendenze Python con `pip install -r requirements.txt` e i programmi `pdftotext` e `pdftocairo` del pacchetto **Poppler** (su Debian/Ubuntu: `sudo apt install poppler-utils`).

### Sviluppo locale

```bash
cd site
npm ci
npm run dev
```

Il sito sarà disponibile su: `http://localhost:4321`

### Build di produzione

```bash
cd site
npm ci
npm run build
```

L'output sarà in: `site/dist/`

Per verificare i componenti Astro e i tipi TypeScript, esegui `npm run check` dalla cartella `site/`.

---

## 📖 Studiare su iPad

Nelle pagine delle lezioni, premi **Modalità lettura** per nascondere la navigazione del sito e leggere a colonna singola, come un libro. Il layout si adatta sia all'orientamento verticale sia a quello orizzontale, incluso l'iPad 2017 da **9,7″** (768 × 1024 punti CSS).

- **Testo**, direttamente sulla pagina in modalità lettura, regola dimensione dei caratteri (18–26 px) e interlinea (1,4 / 1,6 / 1,75 / 2). Le modifiche sono visibili subito.
- **Menu** apre un pannello a scomparsa con indice della pagina, elenco delle lezioni e le stesse impostazioni del testo.
- **Esci dalla lettura** ripristina il layout normale. Modalità, dimensione del testo e interlinea vengono ricordate sul dispositivo, se il browser consente il salvataggio.
- **Schermo intero**, nel menu, usa la funzione del browser quando disponibile. Se il browser la rifiuta, il pannello mostra un messaggio.
- Su Safari per iPad, se lo schermo intero non è disponibile, apri una lezione e scegli **Condividi → Aggiungi alla schermata Home**. Avviando il sito dall'icona, le barre del browser non vengono mostrate e la modalità lettura si attiva inizialmente.
- Il **Reader di Safari** è una funzione distinta, gestita dal browser e non attivabile dal sito. Il contenuto usa un elemento semantico `article` per agevolarne il riconoscimento, senza garantirne la disponibilità. Per conservare navigazione e contenuti originali, usa la modalità lettura del sito.

La modalità lettura non scarica le lezioni per l'uso offline e mantiene il tema chiaro/scuro selezionato nel sito. Il menu funziona senza dipendere dalle API Popover o Dialog, non disponibili in alcune versioni di Safari sui vecchi iPad.

---

## 📝 Contenuti

### 🎓 Materiale didattico
- **Slide delle lezioni**: integrate nelle guide di studio
- **Registrazioni video**: link disponibili in [`site/risorse.md`](site/risorse.md)
- **Appunti collaborativi**: contribuisci con PR!

### 📋 Preparazione all'esame
- [Domande d'esame](site/domande-esame.md) - Banca domande aggiornata
- [Glossario](site/glossario.md) - Terminologia tecnica
- [Guide di studio](site/guide-studio/) - Percorsi di apprendimento

---

## 🤝 Come Contribuire

I contributi sono benvenuti! Questo ramo è in **sviluppo attivo**.

1. **Forka** il repository
2. Crea un branch per la tua feature: `git checkout -b feature/nuova-guida`
3. **Commita** le modifiche: `git commit -m "Aggiungi guida su..."`
4. **Pusha** il branch: `git push origin feature/nuova-guida`
5. Apri una **Pull Request** su `main`

### Linee guida
- ✍️ Usa Markdown per i contenuti
- 🔗 Includi fonti attendibili per informazioni tecniche
- 🎨 Mantieni lo stile coerente con il resto del sito
- ✅ Testa localmente prima di submittere
- 🧪 Verifica che la build Astro funzioni: `npm run build`

---

## 📬 Contatti

- **ARI CRT**: [Sito ufficiale](https://www.ari.it/)
- **GitHub Issues**: [Segnala problemi](https://github.com/raythekool/ari-crt-corso-2025/issues)
- **Email**: [vedi sito ARI](https://www.ari.it/contatti)

---

## 📄 Licenza

Questo progetto è distribuito con licenza **MIT**. Vedi il file [LICENSE](LICENSE) per i dettagli.

---

<div align="center">

**Buono studio e 73 de ARI CRT!** 📻

[⬆️ Torna su](#-ari-crt---corso-radioamatori-2025)

</div>
