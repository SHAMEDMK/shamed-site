# Shamed – Site vitrine

Site vitrine de **Shamed**, distributeur Kerox Dental au Maroc. Solutions dentaires premium : Zircone Zircostar®, PMMA, Résines 3D, Consommables.

## Stack

- HTML5, CSS3, JavaScript
- Site statique (aucun framework)

## Structure

```
├── index.html          # Accueil
├── zircone.html
├── pmma.html
├── resine-3d.html
├── consommables.html
├── a-propos.html
├── contact.html
├── mentions-legales.html
├── politique-confidentialite.html
├── styles.css
├── script.js
├── images/
├── sitemap.xml
├── robots.txt
├── CONVENTIONS.md
└── PLAN_AMELIORATION.md
```

## Déploiement

Prévu pour déploiement sur **Vercel** (site statique).

### URL Vercel (preview)

L’URL du projet sur Vercel correspond au **nom du projet** dans le tableau de bord Vercel :

| URL qui fonctionne | Remarque |
|--------------------|----------|
| `https://shamed-vtrine.vercel.app` | Nom du projet : **shamed-vtrine** (sans **i** dans « vitrine ») |

Si vous tapez `shamed-vitrine.vercel.app` (avec **i**), vous obtenez une **404** : ce n’est pas le même sous-domaine.

**Pour corriger** : dans Vercel → projet → **Settings** → **General** → **Project Name**, renommer en `shamed-vitrine` (orthographe correcte). L’URL deviendra alors `https://shamed-vitrine.vercel.app` (l’ancienne `shamed-vtrine` peut rediriger un temps selon Vercel).

## Prérequis avant production

Voir `AVANT_PRODUCTION.txt` : WhatsApp, Formspree, réseaux sociaux, pages légales.

## Conventions

Voir `CONVENTIONS.md` pour les règles de design, structure et ajout de contenu.
