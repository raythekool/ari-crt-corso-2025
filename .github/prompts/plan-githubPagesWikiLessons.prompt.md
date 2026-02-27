## Plan: Wiki lezioni su GitHub Pages (branch dedicato)

Impostiamo un sito Jekyll “wiki-style” pubblicato da branch `gh-pages` con **solo contenuti studio**: lezioni in [guide-studio](guide-studio), più pagine root selezionate ([glossario.md](glossario.md), [domande-esame.md](domande-esame.md), [risorse.md](risorse.md), [index.md](index.md)).  
Dalla review, la base è già presente ma con incoerenze da correggere: layout non in percorso Jekyll standard ([\_layouts.default.html](_layouts.default.html)), link a transcript ancora esposti ([index.md](index.md#L33)), documentazione di deploy non allineata ([SETUP_GITHUB_PAGES.md](SETUP_GITHUB_PAGES.md#L16-L18), [WEBSITE_IMPLEMENTATION_SUMMARY.md](WEBSITE_IMPLEMENTATION_SUMMARY.md#L68-L87)).  
Obiettivo: separazione netta del sito pubblico dai materiali completi del repo, evitando pubblicazione dei transcript.

**Steps**
1. Definire il perimetro “pubblicabile” e creare la struttura target del branch `gh-pages` (root del branch):  
   [index.md](index.md), [glossario.md](glossario.md), [domande-esame.md](domande-esame.md), [risorse.md](risorse.md), [guide-studio/index.md](guide-studio/index.md) + tutte le `lezione_XX.md`, [_config.yml](_config.yml), `_layouts/default.html`.
2. Correggere la struttura layout Jekyll spostando/rinominando [\_layouts.default.html](_layouts.default.html) in `_layouts/default.html`, poi validare che i front matter `layout: default` risolvano correttamente.
3. Aggiornare [_config.yml](_config.yml#L1-L38) per ambiente Pages del branch dedicato: valorizzare `url`, confermare `baseurl`, mantenere/esplcitare `exclude` per transcript e file non sito.
4. Ripulire la navigazione “wiki” rimuovendo riferimenti a transcript e percorsi non pubblicati: home [index.md](index.md#L29-L35) e menu layout [\_layouts.default.html](_layouts.default.html#L100-L103) (dopo migrazione del file).
5. Verificare e sistemare collegamenti interni tra pagine studio (root ↔ guide-studio), includendo il link rotto a `formule.md` in [glossario.md](glossario.md) (rimozione o sostituzione con destinazione esistente).
6. Allineare la documentazione operativa di deploy alla nuova strategia branch dedicato: aggiornare [SETUP_GITHUB_PAGES.md](SETUP_GITHUB_PAGES.md) e [WEBSITE_IMPLEMENTATION_SUMMARY.md](WEBSITE_IMPLEMENTATION_SUMMARY.md) eliminando istruzioni obsolete.
7. Configurare GitHub Pages in repository settings su `gh-pages` / root e definire il flusso di aggiornamento contenuti (manuale o automatizzato) da `main` a `gh-pages`.
8. Eseguire smoke test finale su URL Pages: home, indice guide, 3 lezioni campione, glossario/domande/risorse, assenza totale di URL transcript.

**Verification**
- Build locale Jekyll del contenuto pubblicabile e controllo link interni.
- Controllo post-deploy su Pages:
  - nessun riferimento navigabile a `transcripts/` o `transcripts (vtt)/`
  - layout applicato correttamente
  - URL canonici coerenti con `baseurl`.
- Verifica regressioni su pagine chiave: [index.md](index.md), [guide-studio/index.md](guide-studio/index.md), [glossario.md](glossario.md), [domande-esame.md](domande-esame.md), [risorse.md](risorse.md).

**Decisions**
- Strategia scelta: branch `gh-pages` dedicato (separazione forte tra sito pubblico e repository completo).
- Scope pubblico: `guide-studio` + alcune pagine root di supporto, con esclusione totale dei transcript dal sito.
