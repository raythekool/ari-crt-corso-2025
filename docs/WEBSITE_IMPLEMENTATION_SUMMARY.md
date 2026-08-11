# 📻 Portale del Corso - Stato Implementazione

## Stato attuale

Il repository pubblica un portale statico Jekyll i cui sorgenti pubblicati sono raccolti nella cartella [`site/`](../site/).

La pubblicazione automatica del sito avviene direttamente da `main` verso GitHub Pages tramite GitHub Actions, senza branch di output dedicati.

La pipeline attiva è [`.github/workflows/sync-gh-pages.yml`](../.github/workflows/sync-gh-pages.yml).

## Componenti del sito

### Contenuti sorgente pubblici

- [`site/index.md`](../site/index.md) — home del portale
- [`site/guide-studio/index.md`](../site/guide-studio/index.md) — indice guide
- `site/guide-studio/lezione_XX.md` — guide delle singole lezioni
- [`site/glossario.md`](../site/glossario.md)
- [`site/domande-esame.md`](../site/domande-esame.md)
- [`site/risorse.md`](../site/risorse.md)

### Configurazioni di build

- [`site/_config.yml`](../site/_config.yml) — configurazione GitHub Pages
- [`site/_config.cloudflare.yml`](../site/_config.cloudflare.yml) — configurazione disponibile per build Cloudflare esterne alla workflow GitHub

### Layout attivo

- [`site/_layouts/default.html`](../site/_layouts/default.html) — layout effettivamente usato dal sito

Il file `/_layouts.default.html` in root non fa parte della build pubblicata ed è un residuo storico da rimuovere.

## Cosa fa la pipeline

La workflow esegue questi passaggi:

1. legge direttamente i sorgenti da `site/`
2. genera una build Jekyll per GitHub Pages in `.site/`
3. carica l'artefatto della build
4. pubblica direttamente l'artefatto su GitHub Pages

## Funzionalità già presenti nel portale

- layout comune per tutte le pagine pubbliche
- menu di navigazione globale
- navigazione rapida tra lezioni nelle guide di studio
- ricerca lato client tra le lezioni pubblicate
- rendering formule tramite MathJax
- apertura dei link YouTube in una nuova scheda
- supporto responsive desktop/mobile

## Contenuti esclusi dalla pubblicazione

Questi contenuti restano nel repository ma non entrano nel sito finale:

- `transcripts/`
- `transcripts (vtt)/`
- `docs/`
- documentazione tecnica interna
- file di supporto locale e artefatti di test

## Note operative

- il branch autorevole rimane `main`
- `gh-pages` e `cf-pages` non sono piu necessari
- eventuali modifiche al sito vanno fatte nei file sotto `site/` su `main`, non nei branch pubblicati

## Documentazione utile

- [Guida setup GitHub/Cloudflare Pages](SETUP_GITHUB_PAGES.md)
- [README del repository](../README.md)

## Stato documentazione

Questo documento sostituisce il precedente riepilogo iniziale, che conteneva istruzioni ormai superate, ad esempio:

- riferimento a layout non più correnti
- task ancora segnati come pendenti ma già completati
- indicazioni di setup non allineate alla pipeline automatica attuale
