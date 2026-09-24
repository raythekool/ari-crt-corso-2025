import re

with open('site/src/styles/custom.css', 'r') as f:
    content = f.read()

content = content.replace('overflow-y: auto !important;', 'overflow-y: auto !important;\n    position: sticky !important;')

with open('site/src/styles/custom.css', 'w') as f:
    f.write(content)
