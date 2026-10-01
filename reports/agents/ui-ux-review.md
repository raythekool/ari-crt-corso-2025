# Report Review UI/UX: ari-crt-corso-2025

Questo documento contiene l'analisi dell'interfaccia utente (UI) e dell'esperienza utente (UX) del sito, basata sul file `site/_layouts/default.html` e sui fogli di stile in `site/styles/`.

## 1. Analisi e implementazione della Dark Mode
Attualmente il file `tokens.css` definisce una serie di variabili sotto il selettore `[data-theme="dark"]`, ma la Dark Mode non è completamente operativa per i seguenti motivi:
- **Tema hardcoded nell'HTML:** Nel file `default.html`, il tag radice è `<html lang="it" data-theme="light">`.
- **Assenza di toggle o rilevamento:** Non c'è un meccanismo JavaScript che rilevi la preferenza di sistema (`prefers-color-scheme: dark`) né un bottone per far scegliere all'utente.
- **Colori non tokenizzati:** Molti file CSS contengono colori *hardcoded* (es. `#f8f4ec`, `rgba(255, 253, 248, 0.74)`, `#f5f7f8`) che non si adatteranno al cambio di tema.

### 🛠️ Azioni suggerite:
- **Script per tema dinamico in `default.html`:**
  Aggiungere un piccolo script in `<head>` per leggere le preferenze dell'utente:
  ```html
  <script>
    const savedTheme = localStorage.getItem('theme');
    const systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (savedTheme === 'dark' || (!savedTheme && systemDark)) {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.setAttribute('data-theme', 'light');
    }
  </script>
  ```
- **Aggiungere un pulsante** (Theme Switcher) nell'header o nav per permettere il toggle.

## 2. Uso delle Variabili CSS (Tokenizzazione)
Il sistema di design adotta nativamente la sintassi moderna `@layer` ed esporta buoni design token in `tokens.css`. Tuttavia, l'uso di questi token non è consistente. 

### 🛠️ Azioni suggerite:
- In `base.css`:
  Il background del `body` utilizza colori statici sfumati:
  ```css
  linear-gradient(180deg, #f8f4ec 0%, var(--color-surface-base) 42%, #ece5d6 100%)
  ```
  Sostituire i colori statici con nuove variabili aggiunte in `tokens.css` (es. `var(--color-surface-gradient-start)`, `var(--color-surface-gradient-end)`).
- In `layout.css`:
  Il footer usa `background: rgba(255, 253, 248, 0.74);`. In dark mode diventerà un blocco bianco accecante. Utilizzare `var(--glass-bg)` o un nuovo token dedicato.
- In `components.css`:
  I tag `<pre>` usano `background: #f5f7f8;`. Sostituirlo con `var(--color-surface-card)` o una variabile `--color-surface-code`. Stessa cosa per i bordi e gli sfondi delle tabelle.

## 3. Tipografia e Spacing (Readability)
La fluid typography usata con le funzioni `clamp()` è un'ottima scelta per la responsiveness. 

### 🛠️ Azioni suggerite:
- **Line Length (Misura):** La classe `.course-prose` si espande su tutta la larghezza disponibile (`minmax(0, 1fr)` del main), che su container da 1280px porta a righe di testo troppo lunghe (oltre i 100-120 caratteri). L'ideale per la leggibilità è tra i 60 e gli 80 caratteri.
  *Modifica consigliata:*
  ```css
  .course-prose {
    max-width: 70ch; /* o 800px */
    margin-inline: auto; /* per centrare il contenuto se lo si desidera */
  }
  ```
- **Focus Rings:** Migliorare l'accessibilità visiva per la navigazione da tastiera. Aggiungere uno stile globale per lo stato di `:focus-visible` in `base.css`:
  ```css
  :focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 4px;
  }
  ```

## 4. Modernizzazione, Accessibilità e UI
- **Scrollbar Personalizzata:** La scrollbar in `base.css` ha colori come `rgba(9, 56, 74, 0.28)`. In Dark Mode, una scrollbar scura su sfondo scuro potrebbe essere invisibile o un elemento di stacco strano. Considerare l'uso della proprietà CSS standard `scrollbar-color: var(--color-primary) transparent;` che è più moderna e accessibile.
- **Transizioni UI:** Gli elementi usano bene `prefers-reduced-motion: reduce`, dimostrando già un'ottima cura per l'accessibilità.
- **Link Accessibilità:** I contrasti sui testi "muted" andrebbero verificati con strumenti WCAG, specialmente quando resi su gradienti di background complessi.

## Conclusione
L'architettura CSS basata su `@layer` è eccellente e rende il codice pulito e modulare. Il passo principale per rendere il progetto "production-ready" e moderno è estirpare tutti i valori statici nei file `layout.css`, `components.css` e `base.css`, portandoli all'interno di `tokens.css`. Così facendo, la Dark Mode si attiverà quasi magicamente e la manutenzione diventerà molto più rapida.
