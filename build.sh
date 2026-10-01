#!/usr/bin/env bash
set -euo pipefail

# Cloudflare Pages build script per ari-crt-corso-2025
# - main                 -> Jekyll (con _config.cloudflare.yml)
# - update-guide-studio-2026 -> Astro

BRANCH="${CF_PAGES_BRANCH:-}"

echo "🔧 Build in corso per ramo: ${BRANCH}"

case "${BRANCH}" in
  main)
    echo "📦 Configurazione build: Jekyll (ramo main)"
    cd site
    bundle install
    # Uso il config specifico per Cloudflare
    bundle exec jekyll build \
      --config _config.yml,_config.cloudflare.yml \
      --destination ../dist
    ;;

  update-guide-studio-2026)
    echo "📦 Configurazione build: Astro (ramo update-guide-studio-2026)"
    cd site
    npm ci
    npm run build
    # Astro scrive in site/dist, Cloudflare userà site/dist come publish dir
    ;;

  *)
    echo "❌ Ramo non gestito: ${BRANCH}"
    echo "   Rami supportati: main (Jekyll), update-guide-studio-2026 (Astro)"
    exit 1
    ;;
esac

echo "✅ Build completata per ramo: ${BRANCH}"
