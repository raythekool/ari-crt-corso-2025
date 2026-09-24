import re

with open('site/src/styles/custom.css', 'r') as f:
    content = f.read()

# Remove my previous attempt
content = re.sub(r'/\* Restringi la Right Sidebar.*?\n}\n', '', content, flags=re.DOTALL)

new_css = """
/* Restringi drasticamente la Right Sidebar */
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
}
"""

with open('site/src/styles/custom.css', 'w') as f:
    f.write(content + new_css)
