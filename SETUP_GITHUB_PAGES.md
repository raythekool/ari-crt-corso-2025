# 🚀 Setup GitHub Pages

Questa guida spiega come attivare il sito web del corso su GitHub Pages.

## 📋 Prerequisiti

- Repository GitHub pubblico o account Pro/Education
- Accesso alle impostazioni del repository

## 🔧 Configurazione GitHub Pages

### 1. Attiva GitHub Pages

1. Vai su **Settings** del repository
2. Scorri fino a **Pages** nella barra laterale
3. In **Source**, seleziona `main` (o il branch principale)
4. Seleziona la cartella **/ (root)**
5. Clicca **Save**

### 2. Aggiorna _config.yml

Modifica il file `_config.yml` e aggiorna:

```yaml
url: "https://TUO_USERNAME.github.io"
baseurl: "/ari-crt-corso-2025"
```

Sostituisci `TUO_USERNAME` con il tuo username GitHub.

### 3. Attendi la Build

- GitHub Pages costruirà automaticamente il sito (ci vogliono 2-5 minuti)
- Puoi vedere lo stato nella tab **Actions** del repository
- Il sito sarà disponibile all'indirizzo mostrato nelle impostazioni Pages

## 🌐 Struttura del Sito

Il sito include:

- **Home page** (`index.md`) — Panoramica del corso e indice lezioni
- **Guide di Studio** (`guide-studio/`) — 22 guide complete
- **Glossario** (`glossario.md`) — Termini tecnici
- **Risorse** (`risorse.md`) — Link e materiali aggiuntivi
- **Domande d'Esame** (`domande-esame.md`) — Quiz e preparazione esame

## 🎨 Personalizzazione

### Cambiare Tema

Nel file `_config.yml`, modifica:

```yaml
theme: jekyll-theme-cayman  # Cambia con altro tema
```

Temi disponibili: `minima`, `cayman`, `slate`, `architect`, `leap-day`, `minimal`, `modernist`, `tactile`, `dinky`, `hacker`

### Modificare Stili

Gli stili CSS inline sono in `_layouts/default.html`. Puoi:
- Cambiare colori del gradiente dell'header
- Modificare font
- Aggiustare spaziature

## 📱 Funzionalità

### Navigazione

- **Menu principale** in tutte le pagine
- **Link incrociati** tra lezioni, glossario e risorse
- **Indice completo** delle guide di studio

### Responsive Design

Il sito è ottimizzato per:
- Desktop
- Tablet
- Mobile

### SEO

Il sito include:
- Meta tags appropriati
- Struttura semantica HTML
- Plugin SEO di Jekyll

## 🔍 Test Locale (Opzionale)

Per testare il sito localmente prima di pubblicare:

### Windows

```powershell
# Installa Ruby (https://rubyinstaller.org/)
gem install bundler jekyll

# Crea Gemfile
@"
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
"@ | Out-File -FilePath Gemfile

# Installa dipendenze
bundle install

# Avvia server locale
bundle exec jekyll serve
```

Visita `http://localhost:4000/ari-crt-corso-2025/`

### Linux/Mac

```bash
# Installa Ruby
sudo apt-get install ruby-full build-essential zlib1g-dev  # Ubuntu/Debian
# oppure
brew install ruby  # macOS

# Installa bundler
gem install bundler

# Crea Gemfile
cat > Gemfile << EOF
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
EOF

# Installa dipendenze
bundle install

# Avvia server locale
bundle exec jekyll serve
```

## 🐛 Troubleshooting

### Il sito non si carica

1. Verifica che GitHub Pages sia attivo nelle impostazioni
2. Controlla la tab **Actions** per errori di build
3. Assicurati che `_config.yml` sia valido (usa validator YAML online)

### Link rotti

- Verifica che `baseurl` in `_config.yml` sia corretto
- Tutti i link interni usano `| relative_url` filter

### Stili non applicati

- Cancella la cache del browser
- Attendi che GitHub Pages completi la build
- Verifica che `_layouts/default.html` esista

## 📊 Analytics (Opzionale)

Per aggiungere Google Analytics, modifica `_layouts/default.html` e aggiungi prima di `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🔐 Custom Domain (Opzionale)

Per usare un dominio personalizzato:

1. Crea file `CNAME` nella root con il tuo dominio:
   ```
   corso.tuodominio.it
   ```

2. Configura i DNS del dominio:
   ```
   Type: CNAME
   Name: corso (o @)
   Value: TUO_USERNAME.github.io
   ```

3. Abilita HTTPS nelle impostazioni Pages

## 📚 Risorse Aggiuntive

- [Documentazione Jekyll](https://jekyllrb.com/docs/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [Jekyll Themes](https://jekyllthemes.io/)

---

**Domande?** Apri una issue nel repository!
