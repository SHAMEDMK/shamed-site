# CONVENTIONS – Projet Antigravity (Shamed)

**Projet** : Site vitrine Shamed – Distributeur Kerox Dental Maroc  
**Objectifs** : Migrer vers Vercel · Améliorer le site avant migration  
**Dernière mise à jour** : Mars 2026

---

## 1. Charte graphique

| Élément | Valeur |
|--------|--------|
| **Couleur principale (Navy)** | `#233C67` (`--clr-navy`) |
| **Couleur accent (Cuivre)** | `#CD9A50` (`--clr-copper`) |
| **Cuivre survol** | `#B58444` (`--clr-copper-hover`) |
| **Typographie titres** | `Playfair Display` |
| **Typographie corps** | `Inter` |
| **Navigation** | Fond doré glassmorphism `rgba(205, 154, 80, 0.92)`, `backdrop-filter: blur(10px)` |
| **Cartes produits (survol)** | Fond cuivre, texte navy |
| **Boutons primaires** | Fond cuivre, texte blanc, survol cuivre plus foncé |

---

## 2. Structure HTML des pages

### Obligatoire sur chaque page

- Skip link : `<a href="#main" class="skip-link">Aller au contenu</a>` en début de `body`
- Nav `glass-nav` avec logo `S`hamed. et dropdown Produits
- Menu mobile `#mobileMenu` avec tous les liens
- Contenu principal avec `id="main"` sur le hero
- Footer avec marque, contact, réseaux sociaux, liens légaux
- Bouton WhatsApp flottant avec `aria-label="Contact WhatsApp"`

### Composants réutilisables

| Composant | Classes / structure |
|-----------|----------------------|
| Hero accueil | `header.hero-section` + `hero-content` + `hero-shape` |
| Page hero (sous-pages) | `header.page-hero` + `page-hero-content` + `subtitle-slogan` |
| Section produits | `section.products-section` + `product-grid` |
| CTA | `section.cta-section` + `cta-content` + `btn-primary` |

---

## 3. Ajout d’un nouveau produit (carte sur l’accueil)

```html
<div class="product-card fade-in delay-X">
  <div class="card-image [zircone|pmma|resine-3d|equipement]">
    <img src="images/XXXX.png" alt="Nom produit" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
  </div>
  <div class="card-content">
    <h3>Nom du produit</h3>
    <p>Description courte (1–2 phrases).</p>
    <a href="page-dediee.html" class="btn-primary">Texte CTA <span>→</span></a>
  </div>
</div>
```

**À faire systématiquement :**
- Ajouter le lien dans le dropdown Produits (nav + menu mobile)
- Créer la page dédiée ou étendre une page existante
- Placer l’image dans `images/`
- Mettre à jour `sitemap.xml` si nouvelle page

---

## 4. Ajout d’un produit détaillé (page gamme type Zircone)

| Bloc | Structure |
|------|-----------|
| Page hero | `header.page-hero` + `subtitle-slogan` + `h1` + `p` |
| Section | `section.zirconia-detail-section` |
| Grille | `div.zirconia-grid` |
| Carte produit | `div.zirc-card` (+ `zirc-card-premium` si premium) |
| Image | `img.zirc-img` |
| Specs | `div.zirc-specs` avec `ul` et `li` (`<strong>Indications:</strong>`, etc.) |
| Tags | `div.zirc-tags` avec `span.tag` |
| Badge premium | `div.zirc-badge` (optionnel) |
| Animations | Classes `fade-in`, `delay-1`, `delay-2` |

---

## 5. SEO (chaque nouvelle page)

- Meta `description` unique
- Balises Open Graph : `og:title`, `og:description`, `og:type`, `og:url`, `og:image`, `og:locale`
- Titre `title` cohérent
- Images : `loading="lazy"` et `alt` descriptif

---

## 6. Accessibilité (a11y)

- Skip link pour la navigation clavier
- Bouton menu : `aria-label`, `aria-expanded`
- Lien WhatsApp : `aria-label="Contact WhatsApp"`
- Liens et boutons avec libellés explicites
- `:focus-visible` (déjà dans `styles.css`)

---

## 7. Images

- Dossier : `images/`
- Formats : PNG, WebP
- Attributs : `loading="lazy"`, `alt` descriptif
- Optimiser (compression) avant mise en ligne

---

## 8. Avant production

| Tâche | Fichier(s) concerné(s) |
|-------|-------------------------|
| Remplacer le numéro WhatsApp | `index.html`, `contact.html`, `a-propos.html`, `pmma.html`, `zircone.html`, `resine-3d.html` |
| Formspree | `contact.html` → remplacer `YOUR_FORM_ID` |
| Réseaux sociaux | Facebook, Instagram (placeholders actuels) |
| Pages légales | `mentions-legales.html`, `politique-confidentialite.html` |
| Sitemap / robots | `sitemap.xml`, `robots.txt` si domaine différent |

---

## 9. Liens et URLs

- Liens internes : chemins relatifs (ex. `zircone.html`, `index.html#produits`)
- Domaine cible : `https://www.shamed.ma`
- Dropdown Produits : lien vers `index.html#produits` sur les sous-pages

---

## 10. Structure du projet

```
projet antigravity/
├── index.html
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
├── sitemap.xml
├── robots.txt
├── images/
├── CONVENTIONS.md (ce fichier)
├── PLAN_AMELIORATION.md
└── AVANT_PRODUCTION.txt
```

---

## Références

- **PLAN_AMELIORATION.md** : plan d’évolution, phases, ERP
- **AVANT_PRODUCTION.txt** : checklist avant mise en ligne
