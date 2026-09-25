# 📚 ARI CRT - Corso Radioamatori 2025 (Ramo Astro)

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/raythekool/ari-crt-corso-2025)
[![Cloudflare Pages](https://img.shields.io/badge/Cloudflare-Pages-F38020?logo=cloudflare)](https://pages.cloudflare.com/)
[![Astro](https://img.shields.io/badge/Astro-Sito-FF5D01?logo=astro)](https://astro.build/)
[![Jekyll](https://img.shields.io/badge/Jekyll-Main-CC0000?logo=jekyll)](https://jekyllrb.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**Ramo di sviluppo** per la nuova versione del sito ARI CRT basata su **Astro**. Questo ramo contiene la preview del sito che sarà eventualmente fusa in `main` dopo testing.

---

## 🚀 Quick Start

### Per gli sviluppatori
- 🔭 **Preview**: deployata automaticamente su Cloudflare Pages
- 📖 **Guide di studio**: [`site/guide-studio/`](site/guide-studio/)
- 🏠 **Homepage**: [`site/index.md`](site/index.md)

### Clona il repository
```bash
git clone https://github.com/raythekool/ari-crt-corso-2025.git
cd ari-crt-corso-2025
git checkout update-guide-studio-2026
```

---

## 🏗️ Struttura del Progetto

```
ari-crt-corso-2025/
├── build.sh              # Script di build per Cloudflare Pages
├── README.md             # Questa documentazione
├── site/                 # Codice sorgente del sito Astro
│   ├── astro.config.mjs  # Configurazione Astro
│   ├── package.json      # Dipendenze Node.js
│   ├── package-lock.json # Lock file npm
│   ├── tsconfig.json     # Configurazione TypeScript
│   ├── public/           # Asset statici
│   ├── src/              # Sorgenti Astro
│   │   ├── components/   # Componenti Astro
│   │   ├── layouts/      # Layout
│   │   └── pages/        # Pagine
│   ├── guide-studio/     # Guide di studio
│   ├── index.md          # Homepage
│   └── ...               # Altri contenuti
└── ...
```

### 🌿 Rami principali

| Ramo | Framework | Stato | Descrizione |
|------|-----------|-------|-------------|
| [`main`](https://github.com/raythekool/ari-crt-corso-2025/tree/main) | **Jekyll** | 🟢 Produzione | Sito principale deployato su Cloudflare Pages |
| [`update-guide-studio-2026`](https://github.com/raythekool/ari-crt-corso-2025/tree/update-guide-studio-2026) | **Astro** | 🟡 Sviluppo | Nuova versione del sito in preview |

---

## 🔧 Build e Deploy

Il progetto utilizza **Cloudflare Pages** per il deploy automatico. La build è gestita dallo script [`build.sh`](build.sh) che rileva automaticamente il ramo corrente.

### Comandi di build

| Ramo | Framework | Comando | Output |
|------|-----------|---------|--------|
| `main` | Jekyll | `bundle exec jekyll build --destination ../dist` | `dist/` |
| `update-guide-studio-2026` | **Astro** | `npm run build` | `site/dist/` |

### Configurazione Cloudflare Pages

1. **Connetti il repository** su [Cloudflare Pages](https://pages.cloudflare.com/)
2. **Build command**: `./build.sh`
3. **Build directory**: `site/dist` (per questo ramo)
4. **Production branch**: `main` (per Jekyll)

#### Variabili d'ambiente consigliate

| Variabile | Valore | Descrizione |
|-----------|--------|-------------|
| `NODE_VERSION` | `20` | Versione Node per Astro |
| `RUBY_VERSION` | `3.2` | Versione Ruby per Jekyll (main) |

---

## 📦 Installazione Locale

### Prerequisiti
- 🟢 **Node.js 20+** (per Astro)
- 💎 **Ruby 3.2+** (per Jekyll, ramo `main`)
- 📦 **npm** (incluso con Node.js)

### Build Astro (questo ramo)

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

### Build Jekyll (ramo `main`)

```bash
git checkout main
cd site
bundle install
bundle exec jekyll serve --drafts
```

Il sito sarà disponibile su: `http://localhost:4000`

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
5. Apri una **Pull Request** su `update-guide-studio-2026`

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

[⬆️ Torna su](#-ari-crt---corso-radioamatori-2025-ramo-astro)

</div>
