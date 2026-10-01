import os
import re
import glob

files = glob.glob('site/src/content/docs/lezioni/lezione_*.md')
for fpath in files:
    filename = os.path.basename(fpath)
    # Extract number from 'lezione_03.md'
    m = re.search(r'lezione_(\d+)\.md', filename)
    if not m:
        continue
    
    num_str = m.group(1)
    num = int(num_str) # 03 -> 3
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace title: "..." with title: "3 - ..."
    # We must match exactly the title line in the frontmatter.
    def title_repl(match):
        old_title = match.group(1)
        # Avoid prepending multiple times if the script runs twice
        if re.match(r'^\d+\s*-', old_title):
            return f'title: "{old_title}"'
        return f'title: "{num} - {old_title}"'
        
    new_content = re.sub(r'^title:\s*"(.*?)"', title_repl, content, count=1, flags=re.MULTILINE)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Titles updated.")
