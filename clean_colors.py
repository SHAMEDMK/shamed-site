import os
import re

css_path = r"c:\projet antigravity\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Contraintes de variables CSS - on lie les "anciennes" variables aux 3 seules couleurs autorisées
css = re.sub(r'--clr-navy-light:\s*#[a-zA-Z0-9]{6};', '--clr-navy-light: var(--clr-navy);', css)
css = re.sub(r'--clr-gray:\s*#[a-zA-Z0-9]{6};', '--clr-gray: rgba(45, 55, 72, 0.6); /* Transparence de Navy */', css)

# Couleurs écrites en dur (notamment les arrière-plans PMMA ou Zircone et textes gris)
css = css.replace('background-color: #E2E8F0;', 'background-color: var(--clr-gray-light);')
css = css.replace('background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);', 'background: var(--clr-gray-light);')
css = css.replace('background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);', 'background: var(--clr-copper);') # La carte PMMA s'alignera avec le bleu électrique
css = css.replace('background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);', 'background: var(--clr-gray-light);')

css = css.replace('color: #666;', 'color: var(--clr-navy); opacity: 0.7;')
css = css.replace('color: #555;', 'color: var(--clr-navy); opacity: 0.8;')

css = css.replace('background: #f8faff;', 'background: var(--clr-white);')
css = css.replace('border: 1px solid #e1e7f0;', 'border: 1px solid var(--clr-gray-light);')
css = css.replace('color: #cbd5e1;', 'color: var(--clr-gray-light);')
css = css.replace('background-color: #e2e8f0;', 'background-color: var(--clr-gray-light);')

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Nettoyage des couleurs aléatoires terminé.")
