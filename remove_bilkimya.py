import codecs

file_path = r"c:\projet antigravity\index.html"
with codecs.open(file_path, "r", "utf-8") as f:
    html = f.read()

html = html.replace('<h3>PMMA Bilkimya</h3>', '<h3>Gamme PMMA</h3>')
html = html.replace("d'usinage turque", "d'usinage")
html = html.replace('<h2>Les Solutions PMMA Bilkimya</h2>', '<h2>Les Solutions PMMA</h2>')
html = html.replace(' (Bilkim)', '')
html = html.replace('<h3>Bilkimya PMMA', '<h3>PMMA')

with codecs.open(file_path, "w", "utf-8") as f:
    f.write(html)

print("Bilkimya a ete retire avec succes")
