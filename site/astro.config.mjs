import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// Lesson markdown hardcodes this prefix in <img src>, so the base stays the same on every host.
const base = '/ari-crt-corso-2025';
const site = process.env.CF_PAGES
  ? (process.env.CF_PAGES_URL ?? 'https://ari-crt-corso-2025.pages.dev')
  : 'https://raythekool.github.io';

export default defineConfig({
  site,
  base,
  integrations: [
    starlight({
      title: 'Corso ARI Toscana CRT 2026',
      defaultLocale: 'root',
      locales: { root: { label: 'Italiano', lang: 'it' } },
      favicon: '/favicon.svg',
      head: [
        { tag: 'meta', attrs: { property: 'og:image', content: `${site}${base}/og.png` } },
      ],
      customCss: ['./src/styles/custom.css'],
      components: {
        Head: './src/components/StudyHead.astro',
        PageFrame: './src/components/StudyFrame.astro',
        MarkdownContent: './src/components/StudyContent.astro',
      },
      sidebar: [
        {
          label: 'Materiale Didattico',
          items: [{ autogenerate: { directory: 'lezioni' } }],
        }
      ],
    }),
  ],
});
