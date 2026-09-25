# 📚 ARI CRT - Corso Radioamatori 2025

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/raythekool/ari-crt-corso-2025)
[![Cloudflare Pages](https://img.shields.io/badge/Cloudflare-Pages-F38020?logo=cloudflare)](https://pages.cloudflare.com/)
[![Jekyll](https://img.shields.io/badge/Jekyll-Site-CC0000?logo=jekyll)](https://jekyllrb.com/)
[![Astro](https://img.shields.io/badge/Astro-Preview-FF5D01?logo=astro)](https://astro.build/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Materiale didattico ufficiale per il **corso radioamatori ARI CRT 2025**. Questo repository contiene slide, appunti, guide e risorse per preparare l'esame di radioamatore.

---

## 🚀 Quick Start

### Per gli studenti
- 🌐 **Sito web**: [ari-crt.github.io](https://ari-crt.github.io/) (produzione)
- 📖 **Guide di studio**: disponibili nella sezione [`site/guide-studio/`](site/guide-studio/)
- ❓ **Domande d'esame**: [`site/domande-esame.md`](site/domande-esame.md)
- 📚 **Risorse utili**: [`site/risorse.md`](site/risorse.md)

### Per i contributori
```bash
git clone https://github.com/raythekool/ari-crt-corso-2025.git
cd ari-crt-corso-2025
```

---

## 🏗️ Struttura del Progetto

```
ari-crt-corso-2025/
├── build.sh              # Script di build per Cloudflare Pages
├── README.md             # Questa documentazione
├── site/                 # Codice sorgente del sito
│   ├── _config.yml       # Configurazione Jekyll (main)
│   ├── _config.cloudflare.yml  # Config specifica per Cloudflare
│   ├── Gemfile           # Dipendenze Ruby/Jekyll
│   ├── package.json      # Dipendenze Node/Astro (update-guide-studio-2026)
│   ├── astro.config.mjs  # Configurazione Astro
│   ├── index.md          # Homepage
│   ├── guide-studio/     # Guide di studio
│   ├── domande-esame.md  # Banca domande
│   ├── glossario.md      # Glossario tecnico
│   └── risorse.md        # Risorse esterne
└── ...
```

### 🌿 Rami principali

| Ramo | Framework | Stato | Descrizione |
|------|-----------|-------|-------------|
| [`main`](https://github.com/raythekool/ari-crt-corso-2025/tree/main) | **Jekyll** | 🟢 Produzione | Sito principale deployato su Cloudflare Pages |
| [`update-guide-studio-2026`](https://github.com/raythekool/ari-crt-corso-2025/tree/update-guide-studio-2026) | **Astro** | 🟡 Preview | Nuova versione del sito in sviluppo |

---

## 🔧 Build e Deploy

Il progetto utilizza **Cloudflare Pages** per il deploy automatico. La build è gestita dallo script [`build.sh`](build.sh) che rileva automaticamente il ramo corrente e usa il framework appropriato.

### Comandi di build

| Ramo | Framework | Comando | Output |
|------|-----------|---------|--------|
| `main` | Jekyll | `bundle exec jekyll build --destination ../dist` | `dist/` |
| `update-guide-studio-2026` | Astro | `npm run build` | `site/dist/` |

### Configurazione Cloudflare Pages

1. **Connetti il repository** su [Cloudflare Pages](https://pages.cloudflare.com/)
2. **Build command**: `./build.sh`
3. **Build directory**: `dist`
4. **Production branch**: `main`

#### Variabili d'ambiente consigliate

| Variabile | Valore | Descrizione |
|-----------|--------|-------------|
| `RUBY_VERSION` | `3.2` | Versione Ruby per Jekyll |
| `NODE_VERSION` | `20` | Versione Node per Astro |

---

## 📦 Installazione Locale

### Prerequisiti
- 💎 **Ruby 3.2+** (per Jekyll)
- 🟢 **Node.js 20+** (per Astro)
- 📦 **Bundler** (`gem install bundler`)

### Build Jekyll (ramo `main`)

```bash
cd site
bundle install
bundle exec jekyll serve --drafts
```

Il sito sarà disponibile su: `http://localhost:4000`

### Build Astro (ramo `update-guide-studio-2026`)

```bash
cd site
npm ci
npm run dev
```

Il sito sarà disponibile su: `http://localhost:4321`

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

I contributi sono benvenuti! Segui questi passaggi:

1. **Forka** il repository
2. Crea un branch per la tua feature: `git checkout -b feature/nuova-guida`
3. **Commita** le modifiche: `git commit -m "Aggiungi guida su..."`
4. **Pusha** il branch: `git push origin feature/nuova-guida`
5. Apri una **Pull Request**

### Linee guida
- ✍️ Usa Markdown per i contenuti
- 🔗 Includi fonti attendibili per informazioni tecniche
- 🎨 Mantieni lo stile coerente con il resto del sito
- ✅ Testa localmente prima di submittere

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
