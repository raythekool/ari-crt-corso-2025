with open('site/guide-studio/lezione_04.md', 'r') as f:
    content = f.read()

# Fix the specific string that was badly replaced
bad_string = """### 🔹 Esercizio svolto

<div align="center"><img src="../assets/images/lezioni/lezione_04/slide-30.jpg" alt="Esercizio K" width="50%"></div><br>

<div align="center"><img src="../assets/images/lezioni/lezione_04/slide-31.jpg" alt="Esercizio corrente" width="50%"></div><br>: calcolo reattanza

<div align="center"><img src="../assets/images/lezioni/lezione_04/slide-21.jpg" alt="Esercizio XL" width="50%"></div><br>"""

good_string = """### 🔹 Esercizio svolto: calcolo reattanza

<div align="center"><img src="../assets/images/lezioni/lezione_04/slide-21.jpg" alt="Esercizio XL" width="50%"></div><br>"""

content = content.replace(bad_string, good_string)

with open('site/guide-studio/lezione_04.md', 'w') as f:
    f.write(content)

