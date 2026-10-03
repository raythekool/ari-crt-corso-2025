# 📚 ARI Toscana CRT — Appunti di studio

[![Cloudflare Pages](https://img.shields.io/badge/Cloudflare-Pages-F38020?logo=cloudflare)](https://pages.cloudflare.com/)
[![Astro](https://img.shields.io/badge/Astro-Sito-FF5D01?logo=astro)](https://astro.build/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Questo progetto contiene il sito Astro + Starlight del corso ARI Toscana CRT e raccoglie **appunti estratti dalle lezioni del corso per radioamatori della Toscana (edizioni 2025 e 2026)**, a partire da trascrizioni e slide di entrambe le edizioni. Non è il testo ufficiale del corso: serve per ripassare le 22 lezioni, consultare rapidamente formule, definizioni e riferimenti normativi, e ritrovare le registrazioni disponibili.

---

## 🚀 Avvio locale

```bash
cd site
npm ci
npm run dev
```

Il sito locale sarà disponibile su `http://localhost:4321`.

---

## 🏗️ Struttura del progetto

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
- [Calendario e registrazioni 2026](docs/lezioni-2026.md) — stato verificato di date e video
- [Guide di studio](site/src/content/docs/lezioni/) — una pagina per ciascuna lezione
- [Trascrizioni TXT](transcripts/2026/) e [VTT](<transcripts (vtt)/2026/>) — materiale di partenza per le guide

La maggior parte delle guide include mappa concettuale, punti chiave, domande di autoverifica e glossario nella stessa pagina. Al momento il progetto **non** contiene pagine separate per glossario generale, domande d'esame o risorse.

---

## 🎓 Esame completo ed esame ridotto

- **Esame completo**: Parti A, B e C; 50 domande a 3 opzioni (30 tecniche e 20 su procedure e normativa); 2 ore; superato con 30 risposte corrette, di cui almeno 18 tecniche e 12 normative.
- **Esame ridotto**: esonero parziale dalla sola Parte A; 20 domande sulle Parti B e C; superato con 12 risposte corrette. Nessun titolo esonera dalle Parti B e C.
- I numeri sono quelli del decreto direttoriale MIMIT del 6 marzo 2024, applicato anche al 2026.
- Per l'esame ridotto servono solo le lezioni [08](site/src/content/docs/lezioni/lezione_08.md), [09](site/src/content/docs/lezioni/lezione_09.md) e [22](site/src/content/docs/lezioni/lezione_22.md); le altre 19 sono la Parte A.
- Alcuni punti ufficiali B e C (segnali di soccorso e catastrofi, registro di stazione, regioni radio UIT) non sono negli appunti. Gli elenchi completi dei 15 codici Q (B.2) e delle 13 abbreviazioni operative (B.3) sono riportati solo in parte nella lezione 08. Da studiare sul Sub allegato D del DM 1 marzo 2021.
- Titoli di esonero, punti del programma e fonti ufficiali sono nella sezione «Gli esami» della home ([site/src/pages/index.astro](site/src/pages/index.astro)). Per l'esame fanno fede i testi ufficiali.

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

- **Indice** apre il pannello con indice della pagina, elenco delle lezioni e impostazioni di lettura
- **Leggi** attiva la lettura; **Esci** la disattiva e ripristina il layout normale, mantenendo le preferenze salvate dal browser (su schermi larghi i pulsanti si chiamano **Attiva lettura** ed **Esci dalla lettura**)
- **Testo** regola dimensione dei caratteri e interlinea direttamente nella pagina
- **Schermo intero**, nel pannello Indice, usa la funzione del browser quando disponibile
- su Safari per iPad, se il full screen non è disponibile, il sito può essere avviato da **Condividi → Aggiungi alla schermata Home**

La modalità lettura non rende il sito disponibile offline da sola: il sito va consultato online.

---

## 🌐 Build e pubblicazione

Il sito statico si costruisce da [site/](site/) e produce [site/dist/](site/dist/). L’hosting è GitHub Pages o Cloudflare Pages.

La configurazione Astro è in [site/astro.config.mjs](site/astro.config.mjs) e usa la base `/ari-crt-corso-2025`, compatibile con entrambi.

---

## 📄 Licenza

Questo progetto è distribuito con licenza **MIT**. Vedi [LICENSE](LICENSE) per i dettagli.
