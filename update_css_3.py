import re

with open('site/src/styles/custom.css', 'r') as f:
    content = f.read()

# Remove the broken bento box block
content = re.sub(r'/\* Effetto Bento Box.*?(?=/\* Custom UI/UX)', '', content, flags=re.DOTALL)

# Create the new safe bento box block
new_block = """/* Effetto Bento Box Sicuro (Non rompe il Grid di Starlight) */
@media (min-width: 50rem) {
  /* Rimuovi bordi nativi di Starlight */
  .sidebar-pane, .right-sidebar-panel {
    border: none !important;
    background: transparent !important;
  }
  
  /* Applica lo stile alla nav interna a sinistra */
  .sidebar-pane .sidebar-content {
    margin: 2rem 1rem 2rem 1.5rem !important;
    height: calc(100vh - var(--sl-nav-height) - 4rem) !important;
    border-radius: 16px !important;
    background-color: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    backdrop-filter: blur(12px);
  }
}

@media (min-width: 72rem) {
  /* Applica lo stile al TOC interno a destra */
  .right-sidebar-panel .right-sidebar-container {
    margin: 2rem 1.5rem 2rem 1rem !important;
    padding: 1rem !important;
    height: max-content !important;
    max-height: calc(100vh - var(--sl-nav-height) - 4rem) !important;
    border-radius: 16px !important;
    background-color: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    backdrop-filter: blur(12px);
    overflow-y: auto !important;
  }
}

"""

# Insert the new block before the UI agent's block
content = content.replace('/* Custom UI/UX', new_block + '/* Custom UI/UX')

with open('site/src/styles/custom.css', 'w') as f:
    f.write(content)
