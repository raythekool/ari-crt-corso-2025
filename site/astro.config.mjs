import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://raythekool.github.io',
  base: '/ari-crt-corso-2025',
  integrations: [
    starlight({
      title: 'Corso ARI Toscana CRT 2026',
      customCss: [],
      sidebar: [
        {
          label: 'Materiale Didattico',
          items: [{ autogenerate: { directory: 'lezioni' } }],
        }
      ],
    }),
  ],
});
