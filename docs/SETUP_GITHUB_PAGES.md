# 🚀 Setup GitHub Pages e Cloudflare Pages

Questa guida descrive la configurazione attuale del portale del corso e come mantenerla operativa.

## 📋 Architettura di pubblicazione

Il branch autorevole resta `main`, ma i sorgenti pubblicati del sito risiedono ora interamente nella cartella [`site/`](../site/).

La workflow [`.github/workflows/sync-gh-pages.yml`](../.github/workflows/sync-gh-pages.yml) legge direttamente da `site/` e genera due siti statici separati:

- branch `gh-pages` per GitHub Pages
- branch `cf-pages` per Cloudflare Pages

## 📦 Contenuti effettivamente pubblicati

La pipeline pubblica i contenuti presenti in `site/`, in particolare:

- `site/index.md`
- `site/glossario.md`
- `site/domande-esame.md`
- `site/risorse.md`
- `site/guide-studio/`
- `site/_config.yml`
- `site/_config.cloudflare.yml`
- `site/_layouts/default.html`

Non vengono pubblicati:

- `transcripts/`
- `transcripts (vtt)/`
- `docs/`
- `README.md`
- `LICENSE`
- `requirements.txt`
- file di test o artefatti locali

## 🔧 GitHub Pages

### Configurazione richiesta

1. Vai in **Settings → Pages** del repository.
2. Imposta come sorgente il branch `gh-pages`.
3. Imposta la cartella pubblicata su `/ (root)`.

### URL atteso

- `https://raythekool.github.io/ari-crt-corso-2025/`

### Configurazione Jekyll usata

Il build GitHub Pages usa [`site/_config.yml`](../site/_config.yml) con:

- `url: "https://raythekool.github.io"`
- `baseurl: "/ari-crt-corso-2025"`

## ☁️ Cloudflare Pages

### Configurazione richiesta

1. Vai in **Cloudflare Dashboard → Workers & Pages**.
2. Crea o apri il progetto Pages collegato al repository.
3. Imposta come branch di produzione `cf-pages`.
4. Usa queste impostazioni:
   - **Framework preset**: `None`
   - **Build command**: vuoto
   - **Build output directory**: `.`

### URL atteso

- `https://ari-crt-corso-2025.pages.dev/`

### Configurazione Jekyll usata

Il build Cloudflare Pages crea una copia temporanea dei sorgenti di `site/` e sostituisce `site/_config.yml` con [`site/_config.cloudflare.yml`](../site/_config.cloudflare.yml), che usa:

- `url: "https://ari-crt-corso-2025.pages.dev"`
- `baseurl: ""`

Quindi su Cloudflare gli URL sono pubblicati alla root, senza il prefisso `/ari-crt-corso-2025/`.

## 🔄 Flusso di deploy

Ogni push su `main` esegue questa sequenza:

1. checkout del branch `main`
2. build Jekyll GitHub Pages da `site/` in `.site-gh/`
3. deploy del risultato nel branch `gh-pages`
4. creazione di una copia temporanea di `site/` per la variante Cloudflare
5. sostituzione della config con `site/_config.cloudflare.yml` nella copia temporanea
6. build Jekyll Cloudflare Pages in `.site-cf/`
7. deploy del risultato nel branch `cf-pages`

È possibile rilanciare manualmente la workflow con `workflow_dispatch` dalla tab Actions.

## ✅ Verifiche consigliate dopo ogni deploy

Controlla almeno:

- home del sito GitHub Pages
- home del sito Cloudflare Pages
- indice guide di studio
- una o due lezioni campione
- assenza di link a `transcripts/` nel sito pubblico
- corretto caricamento del layout e della navigazione

Per la modifica recente dei video YouTube, verifica che i link video si aprano in una nuova scheda.

## 🧪 Test locale opzionale

Per provare Jekyll localmente:

```powershell
gem install bundler jekyll

@"
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
"@ | Out-File -FilePath Gemfile

bundle install
bundle exec jekyll serve --source site
```

Per simulare il sito GitHub Pages, usa `site/_config.yml`.
Per simulare la variante Cloudflare, usa `site/_config.cloudflare.yml`.

## 🐛 Troubleshooting

### Il sito non si aggiorna

- verifica che la workflow su `main` sia partita
- controlla se `gh-pages` e `cf-pages` puntano al commit di deploy più recente
- se necessario, rilancia la workflow manualmente

### GitHub Pages aggiornato ma Cloudflare no

- verifica che Cloudflare Pages stia leggendo davvero il branch `cf-pages`
- controlla che Cloudflare non stia servendo una cache vecchia
- confronta l'HTML pubblicato su `cf-pages` con quello atteso dal layout corrente

### Link interni errati

- GitHub Pages usa `baseurl: /ari-crt-corso-2025`
- Cloudflare usa `baseurl: ""`
- i link interni devono sempre passare da `relative_url` o essere relativi al contenuto Markdown

### Modifiche fatte nel posto sbagliato

- i file del sito pubblico vivono in `site/`
- modificare i file omologhi nella root non ha più effetto sulla pubblicazione
- `gh-pages` e `cf-pages` restano branch generati automaticamente dalla workflow

## 📚 Documentazione correlata

- [Panoramica implementazione sito](WEBSITE_IMPLEMENTATION_SUMMARY.md)
- [README del repository](../README.md)
