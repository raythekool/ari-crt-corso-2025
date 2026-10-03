export {};

const root = document.documentElement;
const toolbar = document.querySelector<HTMLElement>('.study-toolbar');
const menu = document.querySelector<HTMLElement>('#study-menu');
const backdrop = document.querySelector<HTMLElement>('#study-backdrop');
const menuToggle = document.querySelector<HTMLButtonElement>('#study-menu-toggle');
const closeButton = document.querySelector<HTMLButtonElement>('#study-menu-close');
const readingToggle = document.querySelector<HTMLButtonElement>('#study-reading-toggle');
const fullscreenButton = document.querySelector<HTMLButtonElement>('#study-fullscreen');
const fontSize = document.querySelector<HTMLSelectElement>('#study-font-size');
const lineHeight = document.querySelector<HTMLSelectElement>('#study-line-height');
const textSettings = document.querySelector<HTMLDetailsElement>('.study-text-settings');
const status = document.querySelector<HTMLElement>('#study-status');

if (!toolbar || !menu || !backdrop || !menuToggle || !closeButton ||
    !readingToggle || !fullscreenButton || !fontSize || !lineHeight || !textSettings || !status) {
  throw new Error('Gli strumenti di studio non sono disponibili nella pagina.');
}

// Narrowed references remain available inside event callbacks.
const controls = { toolbar, menu, backdrop, menuToggle, closeButton, readingToggle, fullscreenButton, fontSize, lineHeight, textSettings, status };
const storageKey = 'ari-study-reader';
let previousFocus: HTMLElement | null = null;
let backgroundElements: { element: HTMLElement; ariaHidden: string | null; inert: boolean }[] = [];

function report(message: string, error?: unknown) {
  controls.status.textContent = message;
  if (error) console.warn(message, error);
}

function savePreferences() {
  try {
    localStorage.setItem(storageKey, JSON.stringify({
      reading: root.hasAttribute('data-study-reading'),
      fontSize: Number(controls.fontSize.value),
      lineHeight: Number(controls.lineHeight.value),
    }));
  } catch (error) {
    report('Le preferenze non possono essere salvate. Restano attive per questa pagina.', error);
  }
}

function updateReadingButton() {
  const reading = root.hasAttribute('data-study-reading');
  controls.readingToggle.setAttribute('aria-pressed', String(reading));
  controls.readingToggle.textContent = reading ? 'Esci dalla lettura' : 'Modalità lettura';
}

function setReading(reading: boolean) {
  controls.textSettings.open = false;
  root.toggleAttribute('data-study-reading', reading);
  updateReadingButton();
  savePreferences();
}

function setMenu(open: boolean, restoreFocus = true) {
  if (open === !controls.menu.hidden) return;
  controls.menu.hidden = !open;
  controls.backdrop.hidden = !open;
  controls.menuToggle.setAttribute('aria-expanded', String(open));
  root.toggleAttribute('data-study-menu-open', open);
  if (open) {
    controls.textSettings.open = false;
    previousFocus = document.activeElement instanceof HTMLElement && document.activeElement !== document.body
      ? document.activeElement
      : controls.menuToggle;
    backgroundElements = [...document.querySelectorAll<HTMLElement>('.page, .study-toolbar, .sl-skip-link')].map((element) => ({
      element,
      ariaHidden: element.getAttribute('aria-hidden'),
      inert: element.inert,
    }));
    backgroundElements.forEach(({ element }) => {
      element.inert = true;
      element.setAttribute('aria-hidden', 'true');
    });
    controls.closeButton.focus();
  } else {
    backgroundElements.forEach(({ element, ariaHidden, inert }) => {
      element.inert = inert;
      if (ariaHidden === null) element.removeAttribute('aria-hidden');
      else element.setAttribute('aria-hidden', ariaHidden);
    });
    backgroundElements = [];
    if (restoreFocus) previousFocus?.focus();
  }
}

controls.toolbar.hidden = false;
const restoredSize = parseInt(root.style.getPropertyValue('--study-font-size'), 10);
controls.fontSize.value = String([18, 20, 22, 24, 26].includes(restoredSize) ? restoredSize : 20);
const restoredLineHeight = Number(root.style.getPropertyValue('--study-line-height'));
controls.lineHeight.value = String([1.4, 1.6, 1.75, 2].includes(restoredLineHeight) ? restoredLineHeight : 1.75);
const fontSelects = [...document.querySelectorAll<HTMLSelectElement>('[data-study-font-size]')];
const lineSelects = [...document.querySelectorAll<HTMLSelectElement>('[data-study-line-height]')];
fontSelects.forEach((select) => { select.value = controls.fontSize.value; });
lineSelects.forEach((select) => { select.value = controls.lineHeight.value; });
updateReadingButton();
if (root.hasAttribute('data-study-storage-error')) {
  report('Le preferenze salvate non sono disponibili. Puoi comunque usare la modalità lettura.');
}

controls.menuToggle.addEventListener('click', () => setMenu(true));
controls.closeButton.addEventListener('click', () => setMenu(false));
controls.backdrop.addEventListener('click', () => setMenu(false));
controls.menu.addEventListener('click', (event) => {
  const link = event.target instanceof Element ? event.target.closest('a') : null;
  if (!link) return;
  setMenu(false, false);
  if (link.hash && link.pathname === location.pathname) {
    const heading = document.getElementById(decodeURIComponent(link.hash.slice(1)));
    if (heading) {
      heading.setAttribute('tabindex', '-1');
      heading.focus({ preventScroll: true });
    }
  }
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && controls.textSettings.open) {
    controls.textSettings.open = false;
    controls.textSettings.querySelector('summary')?.focus();
  }
  if (controls.menu.hidden) return;
  if (event.key === 'Escape') {
    event.preventDefault();
    setMenu(false);
  } else if (event.key === 'Tab') {
    const focusable = [...controls.menu.querySelectorAll<HTMLElement>('button:not([disabled]), select, a[href]')];
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (event.shiftKey && (document.activeElement === first || document.activeElement === controls.menu)) {
      event.preventDefault();
      last?.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first?.focus();
    }
  }
});
document.addEventListener('focusin', (event) => {
  if (!controls.menu.hidden && event.target instanceof Node && !controls.menu.contains(event.target)) {
    controls.closeButton.focus();
  }
});

controls.readingToggle.addEventListener('click', async () => {
  const reading = !root.hasAttribute('data-study-reading');
  setReading(reading);
  if (!reading && document.fullscreenElement) {
    try {
      await document.exitFullscreen();
    } catch (error) {
      setMenu(true);
      report('Impossibile uscire dallo schermo intero. Usa il comando del browser.', error);
    }
  }
});
fontSelects.forEach((select) => {
  select.addEventListener('change', () => {
    fontSelects.forEach((other) => { other.value = select.value; });
    root.style.setProperty('--study-font-size', `${select.value}px`);
    savePreferences();
  });
});
lineSelects.forEach((select) => {
  select.addEventListener('change', () => {
    lineSelects.forEach((other) => { other.value = select.value; });
    root.style.setProperty('--study-line-height', select.value);
    savePreferences();
  });
});

const canFullscreen = Boolean(document.fullscreenEnabled && root.requestFullscreen);
controls.fullscreenButton.disabled = !canFullscreen;
if (!canFullscreen) {
  controls.fullscreenButton.textContent = 'Schermo intero non disponibile nel browser';
}
function updateFullscreenButton() {
  if (canFullscreen) {
    controls.fullscreenButton.textContent = document.fullscreenElement ? 'Esci dallo schermo intero' : 'Schermo intero';
  }
}
document.addEventListener('fullscreenchange', updateFullscreenButton);
controls.fullscreenButton.addEventListener('click', async () => {
  try {
    if (document.fullscreenElement) {
      await document.exitFullscreen();
    } else {
      await root.requestFullscreen();
      setReading(true);
    }
    setMenu(false);
  } catch (error) {
    report('Il browser non ha consentito lo schermo intero. Usa la modalità lettura o aggiungi il sito alla schermata Home.', error);
  }
});
