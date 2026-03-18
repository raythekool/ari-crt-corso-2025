# 📻 Portale del Corso - Stato Implementazione

## Stato attuale

Il repository pubblica un portale statico Jekyll derivato da un sottoinsieme dei contenuti presenti in `main`.

La pubblicazione è automatica su due destinazioni:

- GitHub Pages tramite branch `gh-pages`
- Cloudflare Pages tramite branch `cf-pages`

La pipeline attiva è [`.github/workflows/sync-gh-pages.yml`](../.github/workflows/sync-gh-pages.yml).

## Componenti del sito

### Contenuti sorgente pubblici

- [`index.md`](../index.md) — home del portale
- [`guide-studio/index.md`](../guide-studio/index.md) — indice guide
- `guide-studio/lezione_XX.md` — guide delle singole lezioni
- [`glossario.md`](../glossario.md)
- [`domande-esame.md`](../domande-esame.md)
- [`risorse.md`](../risorse.md)

### Configurazioni di build

- [`_config.yml`](../_config.yml) — configurazione GitHub Pages
- [`_config.cloudflare.yml`](../_config.cloudflare.yml) — configurazione Cloudflare Pages

### Layout attivo

- [`_layouts/default.html`](../_layouts/default.html) — layout effettivamente usato dal sito

Il file `/_layouts.default.html` in root non fa parte della build pubblicata ed è solo un residuo storico.

## Cosa fa la pipeline

La workflow esegue questi passaggi:

1. copia in `.publish/` soltanto i contenuti pubblicabili
2. genera una build Jekyll per GitHub Pages in `.site-gh/`
3. pubblica il risultato su `gh-pages`
4. sostituisce la configurazione con quella Cloudflare
5. genera una build Jekyll per Cloudflare in `.site-cf/`
6. pubblica il risultato su `cf-pages`

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
- `gh-pages` e `cf-pages` sono branch di output generati dalla workflow
- eventuali modifiche al sito vanno fatte nei file sorgente di `main`, non nei branch pubblicati

## Documentazione utile

- [Guida setup GitHub/Cloudflare Pages](SETUP_GITHUB_PAGES.md)
- [README del repository](../README.md)

## Stato documentazione

Questo documento sostituisce il precedente riepilogo iniziale, che conteneva istruzioni ormai superate, ad esempio:

- riferimento a layout non più correnti
- task ancora segnati come pendenti ma già completati
- indicazioni di setup non allineate alla pipeline automatica attuale
