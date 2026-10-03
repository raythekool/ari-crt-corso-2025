# 📚 ARI Toscana CRT — Appunti di studio

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/raythekool/ari-crt-corso-2025)
[![Cloudflare Pages](https://img.shields.io/badge/Cloudflare-Pages-F38020?logo=cloudflare)](https://pages.cloudflare.com/)
[![Astro](https://img.shields.io/badge/Astro-Sito-FF5D01?logo=astro)](https://astro.build/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Questo repository contiene il sito Astro + Starlight del corso ARI Toscana CRT e raccoglie **appunti estratti dalle lezioni del corso per radioamatori della Toscana**. Non è il testo ufficiale del corso: serve per ripassare le 22 lezioni, consultare rapidamente formule, definizioni e riferimenti normativi, e ritrovare le registrazioni disponibili.

---

## 🚀 Quick start

```bash
git clone https://github.com/raythekool/ari-crt-corso-2025.git
cd ari-crt-corso-2025/site
npm ci
npm run dev
```

Il sito locale sarà disponibile su `http://localhost:4321`.

---

## 🏗️ Struttura del repository

- [README.md](README.md) — panoramica del progetto
- [site/](site/) — sorgenti del sito Astro + Starlight
- [site/src/content/docs/lezioni/](site/src/content/docs/lezioni/) — 22 guide di studio e indice lezioni
- [site/src/pages/index.astro](site/src/pages/index.astro) — home del sito
- [docs/lezioni-2026.md](docs/lezioni-2026.md) — date, titoli e registrazioni verificabili
- [transcripts/2026/](transcripts/2026/) — trascrizioni testuali con timestamp
- [transcripts (vtt)/2026/](<transcripts (vtt)/2026/>) — sottotitoli WebVTT
- [slides 2026/](<slides 2026/>) — PDF delle slide
- [download_transcripts_2026.py](download_transcripts_2026.py) — utility per scaricare i transcript disponibili

---

## 🧭 Contenuti principali

- [Indice delle lezioni](site/src/content/docs/lezioni/index.md) — panoramica completa delle guide, percorsi 1–9 / 10–15 / 16–22 e ricerca per concetto
- [Calendario e registrazioni 2026](docs/lezioni-2026.md) — stato verificato di date e video presenti nel repo
- [Guide di studio](site/src/content/docs/lezioni/) — una pagina per ciascuna lezione
- [Trascrizioni TXT](transcripts/2026/) e [VTT](<transcripts (vtt)/2026/>) — materiale di partenza per le guide

Ogni guida include glossario e domande di autoverifica nella stessa pagina. Al momento il repository **non** contiene pagine separate per glossario generale, domande d'esame o risorse.

---

## 🔧 Sviluppo locale e verifica

### Prerequisiti

- **Node.js 22.12+**
- **npm**
- Facoltativo: **Python 3** per [download_transcripts_2026.py](download_transcripts_2026.py)

Per usare gli script di estrazione slide in [scripts/](scripts/), installare anche `pdftotext` e `pdftocairo` dal pacchetto **Poppler** (su Debian/Ubuntu: `sudo apt install poppler-utils`).

### Comandi utili

```bash
cd site
npm ci
npm run check
npm run build
```

- `npm run check` verifica componenti Astro e tipi TypeScript
- `npm run build` genera l'output statico in [site/dist/](site/dist/)
- la prebuild rigenera [site/public/og.png](site/public/og.png) a partire da [site/public/og.svg](site/public/og.svg) tramite [site/scripts/og.mjs](site/scripts/og.mjs)

---

## 📖 Studiare su iPad

Nelle pagine delle lezioni, **Modalità lettura** nasconde la navigazione del sito e porta il testo in colonna singola. Il layout è pensato anche per iPad 2017 da 9,7″.

- **Testo** regola dimensione dei caratteri e interlinea direttamente nella pagina
- **Menu** apre indice della pagina, elenco delle lezioni e impostazioni di lettura
- **Esci dalla lettura** ripristina il layout normale, mantenendo le preferenze salvate dal browser
- **Schermo intero** usa la funzione del browser quando disponibile
- su Safari per iPad, se il full screen non è disponibile, il sito può essere avviato da **Condividi → Aggiungi alla schermata Home**

La modalità lettura non rende il sito disponibile offline da sola: per studiare senza rete è necessario clonare il repository e avviare il sito in locale.

---

## 🌐 Build e pubblicazione

La pubblicazione su GitHub Pages è gestita dal workflow [deploy.yml](.github/workflows/deploy.yml), che costruisce il sito partendo da [site/](site/) e pubblica [site/dist/](site/dist/).

La configurazione Astro è in [site/astro.config.mjs](site/astro.config.mjs) e usa la base `/ari-crt-corso-2025`, compatibile sia con GitHub Pages sia con Cloudflare Pages.

---

## 🤝 Come contribuire

I contributi sono benvenuti.

1. Crea un branch dedicato
2. Apporta la modifica
3. Verifica localmente con `npm run check` e `npm run build`
4. Usa messaggi di commit in stile [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
5. Apri una pull request

Se segnali un errore nei contenuti, indica sempre la lezione e il passaggio interessato.

---

## 📄 Licenza

Questo progetto è distribuito con licenza **MIT**. Vedi [LICENSE](LICENSE) per i dettagli.
