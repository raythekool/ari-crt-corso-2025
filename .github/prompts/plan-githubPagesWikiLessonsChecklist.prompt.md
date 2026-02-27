## Checklist operativa: GitHub Pages wiki lezioni (gh-pages)

### 1) Scope pubblico
- [ ] Pubblicare solo: `guide-studio/` + pagine root selezionate (`index.md`, `glossario.md`, `domande-esame.md`, `risorse.md`)
- [ ] Escludere dal sito: `transcripts/`, `transcripts (vtt)/`, documentazione tecnica interna

### 2) Struttura Jekyll corretta
- [ ] Spostare/rinominare `_layouts.default.html` in `_layouts/default.html`
- [ ] Verificare che i file Markdown usino `layout: default` dove necessario

### 3) Configurazione sito
- [ ] Aggiornare `_config.yml` con `url` reale del repo owner
- [ ] Confermare `baseurl: /ari-crt-corso-2025`
- [ ] Mantenere `exclude` esplicito per transcript e contenuti non pubblici

### 4) Navigazione wiki
- [ ] Rimuovere link a transcript da `index.md`
- [ ] Verificare menu principale nel layout (solo pagine pubbliche)
- [ ] Controllare i link incrociati root ↔ `guide-studio/`

### 5) Link integrity
- [ ] Risolvere link rotti noti (es. `formule.md` in `glossario.md`)
- [ ] Eseguire controllo link interni su home, indice guide, 3 lezioni campione

### 6) Deploy branch dedicato
- [ ] Preparare branch `gh-pages` con root del sito pubblicabile
- [ ] Configurare GitHub Pages: Source `gh-pages` / root
- [ ] Verificare pubblicazione su URL finale

### 7) Validazione finale
- [ ] Confermare assenza totale di URL `transcripts/*` nel sito
- [ ] Verificare rendering layout, menu, breadcrumb/link
- [ ] Smoke test finale su: home, guide index, glossario, domande-esame, risorse

### Deliverable attesi
- Sito wiki navigabile per studio lezioni
- Nessuna pubblicazione transcript nel sito Pages
- Setup documentato e ripetibile
