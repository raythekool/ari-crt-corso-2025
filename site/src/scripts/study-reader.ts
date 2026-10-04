export {};

const root = document.documentElement;
const toolbar = document.querySelector<HTMLElement>('.study-toolbar');
const toolbarSpacer = document.querySelector<HTMLElement>('#study-toolbar-spacer');
const menu = document.querySelector<HTMLElement>('#study-menu');
const backdrop = document.querySelector<HTMLElement>('#study-backdrop');
const menuToggle = document.querySelector<HTMLButtonElement>('#study-menu-toggle');
const closeButton = document.querySelector<HTMLButtonElement>('#study-menu-close');
const readingToggle = document.querySelector<HTMLButtonElement>('#study-reading-toggle');
const fullscreenButton = document.querySelector<HTMLButtonElement>('#study-fullscreen');
const fullscreenHelp = document.querySelector<HTMLElement>('#study-fullscreen-help');
const fontSize = document.querySelector<HTMLSelectElement>('#study-font-size');
const lineHeight = document.querySelector<HTMLSelectElement>('#study-line-height');
const textSettings = document.querySelector<HTMLDetailsElement>('.study-text-settings');
const textSettingsSummary = textSettings?.querySelector<HTMLElement>('summary');
const status = document.querySelector<HTMLElement>('#study-status');

if (!toolbar || !toolbarSpacer || !menu || !backdrop || !menuToggle || !closeButton ||
    !readingToggle || !fullscreenButton || !fullscreenHelp || !fontSize || !lineHeight ||
    !textSettings || !textSettingsSummary || !status) {
  throw new Error('Gli strumenti di studio non sono disponibili nella pagina.');
}

type BackgroundElementState = { element: HTMLElement; ariaHidden: string | null; inert: boolean };
type ElementAnchorState = { kind: 'element'; element: HTMLElement; sampleY: number; ratio: number };
type MarkerAnchorState = { kind: 'marker'; marker: HTMLSpanElement; sampleY: number };
type AnchorState = ElementAnchorState | MarkerAnchorState;
type DocumentWithCaretApis = Document & {
  caretPositionFromPoint?: (x: number, y: number) => CaretPosition | null;
  caretRangeFromPoint?: (x: number, y: number) => Range | null;
};

const controls = {
  toolbar,
  toolbarSpacer,
  menu,
  backdrop,
  menuToggle,
  closeButton,
  readingToggle,
  fullscreenButton,
  fullscreenHelp,
  fontSize,
  lineHeight,
  textSettings,
  textSettingsSummary,
  status,
};
const storageKey = 'ari-study-reader';
const focusableSelector = 'button:not([disabled]):not([hidden]), select:not([disabled]), a[href], [tabindex]:not([tabindex="-1"])';
const currentLessonSelector = '[data-study-current-lesson]';
let previousFocus: HTMLElement | null = null;
let backgroundElements: BackgroundElementState[] = [];
let resizeFrame = 0;

function report(message: string, error?: unknown) {
  controls.status.textContent = message;
  if (error) console.warn(message, error);
}

function getCaretRange(x: number, y: number) {
  const caretDocument = document as DocumentWithCaretApis;
  if (caretDocument.caretPositionFromPoint) {
    const position = caretDocument.caretPositionFromPoint(x, y);
    if (!position) return null;
    const range = document.createRange();
    range.setStart(position.offsetNode, position.offset);
    range.collapse(true);
    return range;
  }

  return caretDocument.caretRangeFromPoint ? caretDocument.caretRangeFromPoint(x, y) : null;
}

function captureViewportAnchor(): AnchorState | null {
  const article = document.querySelector<HTMLElement>('main article, .sl-markdown-content');
  if (!article) return null;

  const articleRect = article.getBoundingClientRect();
  const x = Math.round(
    Math.max(24, Math.min(window.innerWidth - 24, articleRect.left + Math.min(articleRect.width / 2, 320))),
  );
  const candidateYs = [0.28, 0.42, 0.58].map((ratio) => Math.round(window.innerHeight * ratio));
  const anchorSelector = 'h1, h2, h3, p, li, blockquote, pre, table, figure, .pagination-links a';

  for (const y of candidateYs) {
    const range = getCaretRange(x, y);
    if (range && article.contains(range.startContainer)) {
      const marker = document.createElement('span');
      marker.setAttribute('aria-hidden', 'true');
      marker.dataset.studyScrollAnchor = '';
      marker.style.display = 'inline-block';
      marker.style.inlineSize = '0';
      marker.style.blockSize = '0';
      marker.style.overflow = 'hidden';
      const markerRange = range.cloneRange();
      markerRange.collapse(true);
      markerRange.insertNode(marker);
      return { kind: 'marker', marker, sampleY: y };
    }

    const target = document.elementFromPoint(x, y);
    const anchor = target instanceof Element ? target.closest<HTMLElement>(anchorSelector) : null;
    if (anchor && article.contains(anchor) && !controls.toolbar.contains(anchor) && !controls.menu.contains(anchor)) {
      const anchorRect = anchor.getBoundingClientRect();
      const ratio = anchorRect.height > 0 ? (y - anchorRect.top) / anchorRect.height : 0;
      return { kind: 'element', element: anchor, sampleY: y, ratio: Math.max(0, Math.min(1, ratio)) };
    }
  }

  const fallback = article.querySelector<HTMLElement>(anchorSelector);
  return fallback ? { kind: 'element', element: fallback, sampleY: Math.round(window.innerHeight * 0.42), ratio: 0 } : null;
}

function restoreViewportAnchor(anchor: AnchorState | null) {
  if (!anchor) return;

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      if (anchor.kind === 'marker') {
        if (!anchor.marker.isConnected) return;
        const markerRect = anchor.marker.getBoundingClientRect();
        if (Number.isFinite(markerRect.top)) {
          window.scrollBy(0, markerRect.top - anchor.sampleY);
        }
        const parent = anchor.marker.parentElement;
        anchor.marker.remove();
        parent?.normalize();
        return;
      }

      if (!anchor.element.isConnected) return;
      const anchorRect = anchor.element.getBoundingClientRect();
      const samplePoint = anchorRect.top + (anchorRect.height * anchor.ratio);
      if (!Number.isFinite(samplePoint)) return;
      window.scrollBy(0, samplePoint - anchor.sampleY);
    });
  });
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

function isCompactToolbar() {
  return window.innerWidth <= 1024 || window.innerHeight <= 820;
}

function updateToolbarLabels() {
  const compact = isCompactToolbar();
  const reading = root.hasAttribute('data-study-reading');

  controls.menuToggle.textContent = compact ? 'Indice' : 'Apri indice';
  controls.menuToggle.setAttribute('aria-label', 'Apri indice e lezioni');

  const readingLabel = reading
    ? (compact ? 'Esci' : 'Esci dalla lettura')
    : (compact ? 'Leggi' : 'Attiva lettura');
  controls.readingToggle.textContent = readingLabel;
  controls.readingToggle.setAttribute('aria-label', reading ? 'Esci dalla lettura' : 'Attiva lettura');
  controls.readingToggle.setAttribute('aria-pressed', String(reading));

  controls.textSettingsSummary.textContent = compact ? 'Aa' : 'Testo';
  controls.textSettingsSummary.setAttribute('aria-label', 'Apri le impostazioni del testo');
}

function updateToolbarSpacer() {
  if (root.hasAttribute('data-study-reading')) {
    controls.toolbarSpacer.hidden = true;
    controls.toolbarSpacer.style.height = '0px';
    return;
  }

  const reserve = Math.ceil(controls.toolbar.getBoundingClientRect().height + 16);
  controls.toolbarSpacer.hidden = false;
  controls.toolbarSpacer.style.height = `${reserve}px`;
}

function closeTextSettings(restoreFocus = false) {
  if (!controls.textSettings.open) return;
  controls.textSettings.open = false;
  if (restoreFocus) controls.textSettingsSummary.focus();
}

function setReading(reading: boolean, preserveViewport = false) {
  const anchor = preserveViewport ? captureViewportAnchor() : null;
  closeTextSettings();
  root.toggleAttribute('data-study-reading', reading);
  updateToolbarLabels();
  updateToolbarSpacer();
  savePreferences();
  restoreViewportAnchor(anchor);
}

function scrollCurrentLessonIntoView() {
  const currentLesson = controls.menu.querySelector<HTMLElement>(currentLessonSelector);
  if (!currentLesson) return;

  const currentRect = currentLesson.getBoundingClientRect();
  const menuRect = controls.menu.getBoundingClientRect();
  if (currentRect.top < menuRect.top || currentRect.bottom > menuRect.bottom) {
    const targetScrollTop = controls.menu.scrollTop + currentRect.top - menuRect.top
      - Math.max(0, (menuRect.height - currentRect.height) / 2);
    controls.menu.scrollTop = Math.max(0, targetScrollTop);
  }
}

function setMenu(open: boolean, restoreFocus = true) {
  if (open === !controls.menu.hidden) return;

  controls.menu.hidden = !open;
  controls.backdrop.hidden = !open;
  controls.menuToggle.setAttribute('aria-expanded', String(open));
  root.toggleAttribute('data-study-menu-open', open);

  if (open) {
    closeTextSettings();
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
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        scrollCurrentLessonIntoView();
        controls.closeButton.focus({ preventScroll: true });
      });
    });
    return;
  }

  backgroundElements.forEach(({ element, ariaHidden, inert }) => {
    element.inert = inert;
    if (ariaHidden === null) element.removeAttribute('aria-hidden');
    else element.setAttribute('aria-hidden', ariaHidden);
  });
  backgroundElements = [];
  if (restoreFocus) previousFocus?.focus();
}

controls.toolbar.hidden = false;
controls.toolbar.style.inlineSize = 'max-content';
controls.toolbar.style.maxInlineSize = 'calc(100vw - 1.5rem)';
const restoredSize = parseInt(root.style.getPropertyValue('--study-font-size'), 10);
controls.fontSize.value = String([14, 16, 18, 20, 22].includes(restoredSize) ? restoredSize : 20);
const restoredLineHeight = Number(root.style.getPropertyValue('--study-line-height'));
controls.lineHeight.value = String([1, 1.2, 1.4, 1.6, 1.8].includes(restoredLineHeight) ? restoredLineHeight : 1.8);
const fontSelects = [...document.querySelectorAll<HTMLSelectElement>('[data-study-font-size]')];
const lineSelects = [...document.querySelectorAll<HTMLSelectElement>('[data-study-line-height]')];
fontSelects.forEach((select) => { select.value = controls.fontSize.value; });
lineSelects.forEach((select) => { select.value = controls.lineHeight.value; });
updateToolbarLabels();
updateToolbarSpacer();
if (root.hasAttribute('data-study-storage-error')) {
  report('Le preferenze salvate non sono disponibili. Puoi comunque usare la modalità lettura.');
}

controls.menuToggle.addEventListener('click', () => setMenu(controls.menu.hidden !== false));
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
      heading.addEventListener('blur', () => heading.removeAttribute('tabindex'), { once: true });
      heading.focus({ preventScroll: true });
    }
  }
});
document.addEventListener('click', (event) => {
  if (!controls.textSettings.open) return;
  if (event.target instanceof Node && !controls.textSettings.contains(event.target)) {
    closeTextSettings();
  }
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && controls.textSettings.open) {
    event.preventDefault();
    closeTextSettings(true);
  }
  if (controls.menu.hidden) return;
  if (event.key === 'Escape') {
    event.preventDefault();
    setMenu(false);
  } else if (event.key === 'Tab') {
    const focusable = [...controls.menu.querySelectorAll<HTMLElement>(focusableSelector)];
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
  setReading(reading, true);
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
    const anchor = captureViewportAnchor();
    fontSelects.forEach((other) => { other.value = select.value; });
    root.style.setProperty('--study-font-size', `${select.value}px`);
    savePreferences();
    restoreViewportAnchor(anchor);
  });
});
lineSelects.forEach((select) => {
  select.addEventListener('change', () => {
    const anchor = captureViewportAnchor();
    lineSelects.forEach((other) => { other.value = select.value; });
    root.style.setProperty('--study-line-height', select.value);
    savePreferences();
    restoreViewportAnchor(anchor);
  });
});

const canFullscreen = Boolean(document.fullscreenEnabled && root.requestFullscreen);
controls.fullscreenButton.hidden = !canFullscreen;
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
      setReading(true, true);
    }
    setMenu(false);
  } catch (error) {
    report('Il browser non ha consentito lo schermo intero. Usa la modalità lettura o aggiungi il sito alla schermata Home.', error);
  }
});

window.addEventListener('orientationchange', () => {
  const anchor = captureViewportAnchor();
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      updateToolbarLabels();
      updateToolbarSpacer();
      if (!controls.menu.hidden) scrollCurrentLessonIntoView();
      if (anchor?.kind === 'marker') {
        if (anchor.marker.isConnected) {
          const markerRect = anchor.marker.getBoundingClientRect();
          if (Number.isFinite(markerRect.top)) {
            window.scrollBy(0, markerRect.top - anchor.sampleY);
          }
        }
        const parent = anchor.marker.parentElement;
        anchor.marker.remove();
        parent?.normalize();
      } else if (anchor && anchor.element.isConnected) {
        const anchorRect = anchor.element.getBoundingClientRect();
        const samplePoint = anchorRect.top + (anchorRect.height * anchor.ratio);
        if (Number.isFinite(samplePoint)) {
          window.scrollBy(0, samplePoint - anchor.sampleY);
        }
      }
    });
  });
});
window.addEventListener('resize', () => {
  if (resizeFrame) cancelAnimationFrame(resizeFrame);
  resizeFrame = requestAnimationFrame(() => {
    updateToolbarLabels();
    updateToolbarSpacer();
    if (!controls.menu.hidden) scrollCurrentLessonIntoView();
  });
});

updateFullscreenButton();
