---
description: "Framework-agnostic styling standards covering token architecture, CSS custom properties, typography, surfaces, motion, layout, and accessibility. Includes framework-specific guidance for React/Fluent UI v9, React/Tailwind, Vue, and Angular."
applyTo: "*.{tsx,ts,jsx,js,css,vue,scss}"
---

# Styling Standards

This file defines universal styling principles applicable to any web project, regardless of framework.
Framework-specific conventions are collected at the end of the document.
Follow the universal rules first; then apply the framework addendum that matches your stack (if you use one of the indicated frameworks).

---

## Part A — Universal Standards (framework-agnostic)

These rules apply to every project, every technology, and every team member.

---

### A1. Token Architecture

Every project's color system is built in three layers. Never skip a layer.

```
Brand palette  →  CSS custom properties (:root)  →  Framework theme / utility classes
  (source of           (tokens.css or                  (optional — see Part B)
    truth)              equivalent)
```

#### Layer 1 — Brand palette (source of truth)

A curated set of brand colors is defined by the design system or design team.
All other colors are derived from or mapped to this palette.
New colors must come from the palette — never invent ad-hoc hex values.

#### Layer 2 — CSS custom properties

Brand values are declared as `--` CSS variables on `:root`.
The token set must cover:

- **Color roles** — named by purpose, not by value: `--color-primary`, `--color-primary-dark`, `--color-primary-light`, `--color-success`, `--color-warning`, `--color-error`, `--color-info`.
- **Surface scale** — background levels ordered by elevation: `--color-surface-base`, `--color-surface-card`, `--color-surface-overlay`.
- **Text roles** — `--color-text`, `--color-text-muted`, `--color-text-inverted`.
- **Border** — `--color-border`, `--color-border-strong`.
- **Layout constants** — `--sidebar-width`, `--sidebar-collapsed`, `--topbar-height` (adjust names to the project shell).
- **Radius scale** — `--radius-xs`, `--radius-sm`, `--radius-md`, `--radius-lg`, `--radius-xl`, `--radius-full`.
- **Shadow scale** — `--shadow-xs` through `--shadow-xl`.
- **Glass surface presets** — `--glass-bg`, `--glass-border`, `--glass-blur`.
- **Transition presets** — `--transition-fast`, `--transition-normal`, `--transition-slow` (see A5).

**Rule**: Components reference `var(--color-*)` tokens, never raw hex or `rgb()` literals.

#### Layer 3 — Framework theme (optional)

Some frameworks or component libraries accept a theme object (Design tokens as JS objects, Tailwind config, CSS-in-JS theme, etc.).
When present, this layer must be generated from Layer 2 values, not defined independently.

---

### A2. Typography Scale

Declare the font family once, globally (`:root` or `body`). Components must not override it.

| Level          | CSS / token                    | Typical usage                   |
| -------------- | ------------------------------ | ------------------------------- |
| Display / Hero | `clamp(28px, 3vw, 40px)`       | Full-page hero headline         |
| Heading 1      | `--font-size-xl` or equivalent | Main section title              |
| Heading 2      | `--font-size-lg`               | Card title, panel header        |
| Body large     | `--font-size-md`               | Primary content                 |
| Body           | `--font-size-base`             | Default text, form labels       |
| Caption        | `--font-size-sm`               | Timestamps, footnotes, metadata |

- Use `clamp()` for headings that must respond to viewport width.
- Never set `font-family` per component — it is declared globally.
- Prefer named weight tokens (`--font-weight-bold`, `--font-weight-semibold`) over numeric values.

---

### A3. Surfaces and Elevation

Use a **depth metaphor**: lower surfaces are more opaque; elevated surfaces are lighter or translucent.

| Depth              | Token                                               | When                  |
| ------------------ | --------------------------------------------------- | --------------------- |
| Page background    | `body` gradient or `--color-surface-base`           | Behind everything     |
| Shell / containers | `--color-surface-base`                              | Sidebar, shell panels |
| Cards / panels     | `--color-surface-card` + `--color-border`           | Content cards         |
| Floating           | `--glass-bg` + `backdrop-filter: var(--glass-blur)` | Modals, popovers      |

Every card component must have:

- `border-radius: var(--radius-lg)` at default; deviate only with explicit justification.
- `box-shadow: var(--shadow-sm)` at rest.
- On hover: `box-shadow: var(--shadow-md)` + `transform: translateY(-2px)` animated with `var(--transition-normal)`.

---

### A4. Semantic Status Colors

Domain statuses (record status, priority, risk, etc.) must always be rendered through a shared **semantic badge / status chip component**.
This component maps domain values to semantic color tokens (`--color-success`, `--color-warning`, `--color-error`, `--color-info`, plus muted/brand variants).

**Never hard-code a status color in a page or card.** Extend the shared mapping and use the component everywhere.
Color is never the only differentiator — always pair it with a text label.

---

### A5. Motion and Transitions

Define three transition presets using a single shared easing function:

```css
:root {
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --transition-fast: 0.15s var(--ease-out-expo);
  --transition-normal: 0.22s var(--ease-out-expo);
  --transition-slow: 0.35s var(--ease-out-expo);
}
```

| Preset                | Use                                         |
| --------------------- | ------------------------------------------- |
| `--transition-fast`   | Micro-interactions: color change, icon swap |
| `--transition-normal` | Card hover, panel expand/collapse           |
| `--transition-slow`   | Page-level entry, drawer / sheet open       |

Rules:

- Do not use `linear` easing.
- Do not use arbitrary duration values outside these presets.
- Do not use `transition: all` — list specific CSS properties.
- Respect `prefers-reduced-motion`: wrap all transitions in:

```css
@media (prefers-reduced-motion: no-preference) {
  .animated-element {
    transition: transform var(--transition-normal);
  }
}
```

---

### A6. Layout and Responsiveness

- Use **CSS Grid** and **Flexbox** for all layout. No floats, no absolute-position hacks.
- Multi-column grids use `repeat(N, minmax(0, 1fr))`.
- At narrow viewports (≤ 900 px), collapse to `grid-template-columns: 1fr`.
- Define breakpoints in plain `@media` rules — no external breakpoint library required.
- Shell layout constants (`--sidebar-width`, `--topbar-height`) are CSS variables so layout adjustments cascade automatically.

---

### A7. Global Base Stylesheet

A single global CSS file (e.g., `index.css`, `global.css`, `base.css`) loaded once at the app entry point covers:

- `:root` — the complete CSS variable token set.
- `body` — full-viewport background, `background-attachment: fixed`.
- `body::before` — decorative overlay/texture (pointer-events disabled).
- Reset: `box-sizing: border-box`, `font: inherit` on form elements.
- Custom scrollbar styling (`-webkit-scrollbar`).

Do not add component-level or page-level styles here.

---

### A8. CSS Naming Convention (page-level stylesheets)

Use BEM-like, domain-prefixed naming for utility and layout classes:

```
.{domain}-{block}
.{domain}-{block}__{element}
.{domain}-{block}--{modifier}
```

Examples: `.dash-kpi-grid`, `.dash-kpi-card`, `.dash-kpi-card--highlighted`.

---

### A9. Iconography

- Use a **single, consistent icon library** per project. Do not mix multiple libraries.
- Import individual icons by name, never the entire package.
- Set icon size via `font-size` or `width`/`height` using a token value, not a hardcoded pixel.
- Icon-only interactive elements must carry `aria-label`.

---

### A10. Accessibility (WCAG 2.1 AA)

- Color contrast: **4.5 : 1** for body text, **3 : 1** for large text and UI component boundaries.
- Heading levels (`h1` → `h2` → `h3` …) must not skip.
- Color is never the sole differentiator for status or meaning.
- All interactive elements are keyboard-navigable (Tab, Enter, Space, Escape).
- Dynamic content uses `aria-live` regions.
- Images and icon-only controls have accessible text (`alt`, `aria-label`, `aria-labelledby`).

---

### A11. Dark Mode Readiness

- Surface and text colors must always reference semantic CSS variables, never light-specific hex values.
- When dark mode is required, add a `[data-theme="dark"]` selector (or equivalent) that overrides the color role variables. The component markup stays unchanged.
- Component stylesheets using CSS variables adapt automatically without any changes.

---

### A12. Universal Anti-Patterns

| Anti-pattern                                                          | Required approach                                     |
| --------------------------------------------------------------------- | ----------------------------------------------------- |
| Raw hex or `rgb()` in any component style                             | Use CSS custom property token                         |
| Inventing a new color for a status                                    | Extend the shared status mapping                      |
| `transition: all`                                                     | List specific properties with a preset variable       |
| Overriding the global font family per component                       | Font is global; do not override                       |
| Skipping heading levels for visual sizing                             | Use font-size tokens; preserve semantic heading level |
| Breakpoints via JS media-query libraries                              | Use `@media` in CSS                                   |
| Setting layout dimensions as literal pixels                           | Use layout constant tokens                            |
| Side-effect styles on global selectors (`.card`) from component files | Scope to component or use a page-level sheet          |

---

## Part B — Framework-Specific Addenda

Apply the addendum that matches the project's UI stack on top of Part A.
Only one addendum applies per project; do not mix patterns from different addenda.

---

### B1. React + Fluent UI v9 (Griffel)

**Stack**: React, TypeScript, `@fluentui/react-components`, `@fluentui/react-icons`.

#### Component styling — `makeStyles` first

All component styles use `makeStyles()`. Plain CSS class names and inline `style={}` are not permitted for component-level styling.

```tsx
import { makeStyles, mergeClasses, tokens } from "@fluentui/react-components";

const useStyles = makeStyles({
  root: {
    display: "flex",
    gap: tokens.spacingVerticalM,
    padding: `${tokens.spacingVerticalL} ${tokens.spacingHorizontalL}`,
    backgroundColor: tokens.colorNeutralBackground1,
    borderRadius: tokens.borderRadiusMedium,
  },
  rootActive: { boxShadow: tokens.shadow8 },
});

export function MyComponent({ isActive }: { isActive: boolean }) {
  const styles = useStyles();
  return (
    <div className={mergeClasses(styles.root, isActive && styles.rootActive)} />
  );
}
```

#### Token mapping inside `makeStyles`

| Need          | Token                                                    |
| ------------- | -------------------------------------------------------- |
| Spacing       | `tokens.spacingVertical*` / `tokens.spacingHorizontal*`  |
| Color         | `tokens.colorNeutral*` or `var(--color-*)` CSS variables |
| Shadow        | `tokens.shadow*` or `var(--shadow-*)`                    |
| Border radius | `tokens.borderRadius*` or `var(--radius-*)`              |
| Font size     | `tokens.fontSizeBase*`                                   |
| Font weight   | `tokens.fontWeightSemibold` / `tokens.fontWeightBold`    |
| Transition    | `var(--transition-*)` CSS variables                      |

#### Brand theme

Generate `illyLightTheme` (or equivalent) with `createLightTheme(brandVariants)` once.
Apply it at root: `<FluentProvider theme={brandLightTheme}>`.
For dark mode, generate `createDarkTheme(brandVariants)` from the same palette and swap at runtime.

#### Icons

```tsx
// Correct — individual import
import { CalendarRegular, PersonRegular } from "@fluentui/react-icons";

// Wrong — never import the whole package
import * as Icons from "@fluentui/react-icons";
```

Use `tokens.iconSizeSmall` / `tokens.iconSizeMedium` for icon size.

#### JS token constants

A TypeScript mirror of CSS variables (e.g., `tokens.ts`) is used **only** for non-CSS contexts:
Recharts/D3 fills, canvas drawing, chart axis colors.
Do not use JS constants inside `makeStyles` or `className` strings.

#### Fluent-UI-specific anti-patterns

| Anti-pattern                            | Required approach                       |
| --------------------------------------- | --------------------------------------- |
| Raw hex inside `makeStyles`             | Use `tokens.color*` or `var(--color-*)` |
| Overriding `.fui-*` internal classes    | Use `makeStyles` slot/override API      |
| Hardcoded pixel spacing in `makeStyles` | Use `tokens.spacing*`                   |
| Inline `style={}` for visual properties | Use `makeStyles`                        |

---

### B2. React + Tailwind CSS

**Stack**: React (or Next.js), TypeScript, Tailwind CSS v3/v4.

#### Token integration

Define brand tokens in `tailwind.config` under `theme.extend`. Do not add one-off arbitrary values with `[]` — extend the config instead.

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: "var(--color-primary)",
        "primary-dark": "var(--color-primary-dark)",
        surface: "var(--color-surface-card)",
        border: "var(--color-border)",
      },
      borderRadius: {
        lg: "var(--radius-lg)",
        xl: "var(--radius-xl)",
      },
      boxShadow: {
        card: "var(--shadow-sm)",
        "card-hover": "var(--shadow-md)",
      },
    },
  },
};
```

CSS variables are still the source of truth; Tailwind classes simply alias them.

#### Class composition

Use `clsx` (or `cn`) to conditionally compose classes. Do not build class strings with string concatenation.

```tsx
import clsx from "clsx";

<div
  className={clsx(
    "rounded-lg bg-surface shadow-card",
    isActive && "shadow-card-hover",
  )}
/>;
```

#### Avoid

- Arbitrary values like `text-[#d31217]` or `p-[14px]` — use token-mapped utilities.
- Long one-line class strings without extraction into a `@layer components` rule when reused in ≥ 3 places.
- Mixing Tailwind utility classes with plain CSS class names on the same element.

#### Dark mode

Use Tailwind's `dark:` variant tied to `class` strategy. Toggle the `dark` class on `<html>`. CSS variables in `:root` / `.dark` handle the color swap.

---

### B3. Vue (Vue 3 + `<style scoped>`)

**Stack**: Vue 3, TypeScript or JavaScript, single-file components (SFC).

#### Component styling

Use `<style scoped>` in every SFC. Global unscoped styles are only allowed in the app entry stylesheet.

```vue
<template>
  <div :class="['card', { 'card--active': isActive }]">…</div>
</template>

<style scoped>
.card {
  background: var(--color-surface-card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  transition:
    box-shadow var(--transition-normal),
    transform var(--transition-normal);
}
.card--active,
.card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}
</style>
```

#### CSS variables inside SFC

Always use `var(--*)` for colors, spacing, radii, and shadows — never raw literals.
You can also use `:deep()` to override child component styles when a library does not expose a token API.

#### Class binding

Use `:class` with an object or array binding. Do not build class strings dynamically via JavaScript string concatenation.

#### Dark mode

Add a `[data-theme="dark"]` attribute on `<html>` and override CSS variable values in the global stylesheet. SFC styles adapt automatically.

---

### B4. Angular (Angular 17+ with standalone components)

**Stack**: Angular 17+, TypeScript, component-scoped styles.

#### Component styling

Use the `styles` or `styleUrl` metadata of `@Component`. Angular applies View Encapsulation (Emulated by default), which scopes styles to the component automatically — analogous to Vue's `scoped`.

```ts
@Component({
  selector: "app-card",
  template: `<div class="card" [class.card--active]="isActive">…</div>`,
  styles: [
    `
      .card {
        background: var(--color-surface-card);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-sm);
        transition:
          box-shadow var(--transition-normal),
          transform var(--transition-normal);
      }
      .card:hover {
        box-shadow: var(--shadow-md);
        transform: translateY(-2px);
      }
    `,
  ],
})
export class CardComponent {
  isActive = false;
}
```

#### Global styles

Global CSS variable tokens go in `src/styles.css` (the Angular project's root stylesheet). Do not declare tokens inside component stylesheets.

#### Class binding

Use Angular's `[class.modifier]="condition"` or `[ngClass]` binding. Do not build class strings via TypeScript string concatenation.

#### CSS custom properties

All colors, radii, and shadows are referenced as `var(--*)` inside component styles.
Use `::ng-deep` sparingly and only to pierce View Encapsulation for third-party library overrides; scope it inside a host selector.

#### Dark mode

Toggle a `data-theme` attribute on `<html>` from an Angular service. CSS variables in `styles.css` handle the swap; component styles adapt without changes.

---

### B5. Plain HTML + CSS (no framework)

**Stack**: Static sites, server-rendered HTML (any language), no component framework.

#### File structure

```
styles/
  tokens.css      ← CSS custom properties (the full token set)
  base.css        ← reset, body, scrollbar
  layout.css      ← shell, grid, sidebar, topbar
  components.css  ← reusable UI patterns: card, badge, button
  pages/
    dashboard.css ← page-specific overrides
```

Import order in `<head>`: `tokens.css` → `base.css` → `layout.css` → `components.css` → page CSS.

#### Naming

Follow the BEM convention described in A8. Keep specificity flat — one class, no nesting via descended selectors unless unavoidable.

#### No build step

To avoid specificity conflicts without a bundler, use the `@layer` rule:

```css
@layer reset, tokens, base, components, utilities;
```

Declare each file's rules inside the matching layer.
