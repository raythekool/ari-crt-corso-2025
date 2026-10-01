import re

with open('site/src/styles/custom.css', 'r') as f:
    content = f.read()

# Update content width to 100ch
content = content.replace('--sl-content-width: 90ch !important;', '--sl-content-width: 100ch !important;')

# Update right sidebar CSS block
old_sidebar_css = """/* Restringi drasticamente la Right Sidebar */
@media (min-width: 72rem) {
  .right-sidebar-panel {
    width: 12rem !important;
    min-width: 12rem !important;
    max-width: 12rem !important;
    flex: 0 0 12rem !important;
  }
  .right-sidebar-panel .right-sidebar-container {
    margin: 2rem 1rem 2rem 0 !important;
  }
}"""

new_sidebar_css = """/* Restringi la Right Sidebar e fai espandere il contenuto centrale */
@media (min-width: 72rem) {
  .right-sidebar-panel {
    width: 14rem !important;
    min-width: 14rem !important;
    max-width: 14rem !important;
    flex: 0 0 14rem !important;
  }
  .right-sidebar-panel .right-sidebar-container {
    margin: 2rem 1rem 2rem 0 !important;
  }
  .main-pane {
    flex: 1 1 auto !important;
    width: calc(100% - 14rem) !important;
    max-width: none !important;
  }
}"""

if old_sidebar_css in content:
    content = content.replace(old_sidebar_css, new_sidebar_css)
else:
    # Just in case the exact match fails
    content += "\\n" + new_sidebar_css

with open('site/src/styles/custom.css', 'w') as f:
    f.write(content)
