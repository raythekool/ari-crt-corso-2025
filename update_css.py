import re

with open('site/src/styles/custom.css', 'r') as f:
    content = f.read()

new_block = """/* Effetto Bento Box per le Sidebar (Desktop) come nel Mockup */
@media (min-width: 50rem) {
  .sidebar-pane {
    margin: 2rem 1rem 2rem 2rem !important;
    top: calc(var(--sl-nav-height) + 2rem) !important;
    height: calc(100vh - var(--sl-nav-height) - 4rem) !important;
    border-radius: 16px !important;
    background-color: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4) !important;
    background-image: linear-gradient(135deg, rgba(56, 189, 248, 0.06) 0%, transparent 60%) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    overflow-y: auto !important;
    box-sizing: border-box !important;
  }
}

@media (min-width: 72rem) {
  .right-sidebar-panel {
    margin: 2rem 2rem 2rem 1rem !important;
    padding: 1.5rem !important;
    top: calc(var(--sl-nav-height) + 2rem) !important;
    height: calc(100vh - var(--sl-nav-height) - 4rem) !important;
    max-height: calc(100vh - var(--sl-nav-height) - 4rem) !important;
    border-radius: 16px !important;
    background-color: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4) !important;
    background-image: linear-gradient(225deg, rgba(56, 189, 248, 0.06) 0%, transparent 60%) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    overflow-y: auto !important;
    box-sizing: border-box !important;
  }
}

/* Fix per l'intestazione dell'indice a destra per farla matchare */
.right-sidebar-panel h2 {
  margin-top: 0 !important;
}"""

# Replace everything from "/* Effetto Bento Box" to the end
content = re.sub(r'/\* Effetto Bento Box.*', new_block, content, flags=re.DOTALL)

with open('site/src/styles/custom.css', 'w') as f:
    f.write(content)
