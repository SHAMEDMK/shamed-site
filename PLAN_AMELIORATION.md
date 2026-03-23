# Plan d'amélioration – Site Shamed (shamed.ma)

**Projet** : Distributeur Kerox Dental Maroc  
**Type** : Site vitrine HTML statique  
**Dernière mise à jour** : Mars 2026

---

## Vue d'ensemble

Ce document liste les améliorations à effectuer pour :

1. **Site vitrine** (www.shamed.ma) : préparer la mise en production et améliorer l'expérience utilisateur.
2. **ERP** (erp.shamed.ma) : créer un back-office de gestion pour les commandes, le stock, les clients et la facturation.

---

## Phase 1 – Bloquants (avant mise en production)

### 1.1 Menu mobile
**Priorité** : critique  
**Effort** : ~1h  
**Statut** : ✅ Fait (mars 2026)

Le menu disparaît sur mobile (`display: none` à 768px) sans alternative.

- [x] Ajouter un bouton hamburger (≡) visible sur mobile
- [x] Créer un menu déroulant / drawer avec les liens (Accueil, Produits + sous-menu, À propos, Contact)
- [ ] Tester sur différentes tailles d'écran

---

### 1.2 Images
**Priorité** : critique  
**Effort** : ~30 min

Fichiers référencés à vérifier ou créer :

| Fichier | Pages concernées |
|---------|------------------|
| `images/zircostar-3dml-bg.png` | index, zircone |
| `images/zircostar-html-bg.png` | zircone |
| `images/zircostar-utml-bg.png` | zircone |
| `images/zircostar-ht-bg.png` | zircone |
| `images/zircostar-hs-bg.png` | zircone |
| `images/zircostar-uht-bg.png` | zircone |
| `images/pmma.webp` | index, pmma |
| `images/castable-resin-for-dental_Green1.png` | index, resine-3d |
| `images/wax.png` | index |
| `images/our-products-zirconia.png` | a-propos |
| `images/Moder-resine.png` | resine-3d |

- [ ] Créer le dossier `images/` si absent
- [ ] Vérifier que chaque image existe et est correcte
- [ ] Optimiser les images (compression, format WebP si pertinent)
- [ ] Ajouter `loading="lazy"` sur les images hors viewport initial

---

### 1.3 Contact et WhatsApp
**Priorité** : haute  
**Effort** : ~20 min

- [ ] Remplacer `212600000000` par le vrai numéro WhatsApp (voir AVANT_PRODUCTION.txt)
- [x] Formulaire contact prêt pour Formspree : remplacer YOUR_FORM_ID dans contact.html

---

## Phase 2 – UX / Interface

### 2.1 Navigation
**Priorité** : haute  
**Effort** : ~30 min  
**Statut** : ✅ Fait

- [x] Sur les sous-pages, faire pointer "Produits" vers `index.html#produits`
- [x] Indicateur visuel de la page active dans le dropdown
- [x] Dropdown ouvrable au clic sur appareils tactiles (hover: none)

---

### 2.2 Accessibilité (a11y)
**Priorité** : moyenne  
**Effort** : ~45 min  
**Statut** : ✅ Fait

- [x] `aria-label` sur hamburger (Ouvrir/Fermer) et lien WhatsApp
- [x] Lien d'évitement "Aller au contenu" (navigation clavier)
- [x] `:focus-visible` pour les éléments interactifs

---

### 2.3 Footer
**Priorité** : moyenne  
**Effort** : ~20 min  
**Statut** : ✅ Fait

- [x] Lien "Mentions légales" (mentions-legales.html)
- [x] Lien "Politique de confidentialité" (politique-confidentialite.html)
- [x] Numéro de téléphone cliquable dans le footer
- [x] Lien WhatsApp cliquable dans le footer

---

## Phase 3 – Performance et SEO

### 3.1 SEO
**Priorité** : haute  
**Effort** : ~30 min  
**Statut** : ✅ Fait

- [x] Meta description sur toutes les pages
- [x] Balises Open Graph (`og:title`, `og:description`, `og:image`, `og:url`, `og:locale`)
- [x] Sitemap `sitemap.xml`
- [x] Fichier `robots.txt`

---

### 3.2 Performance
**Priorité** : moyenne  
**Effort** : ~45 min  
**Statut** : ✅ Fait

- [x] Lazy loading sur images : `loading="lazy"`
- [x] Preconnect pour Google Fonts (toutes les pages)
- [ ] Tester avec [PageSpeed Insights](https://pagespeed.web.dev/)

---

## Phase 4 – Contenu et structure

### 4.1 Contenu
**Priorité** : moyenne  
**Effort** : variable

- [ ] Harmoniser le ton avec le site WordPress actuel (ex. "9 ans d'expérience" si pertinent)
- [ ] Ajouter une section "Nos marques" ou "Partenaires" si souhaité
- [ ] Vérifier les textes produits (Zircone, PMMA, Résines 3D) avec les fiches Kerox
- [ ] Corriger le lien "Consommables Divers" (actuellement pointe vers Contact au lieu d'une page dédiée)

---

### 4.2 Page Consommables
**Priorité** : faible  
**Effort** : ~1h

- [ ] Créer `consommables.html` ou section dédiée
- [ ] Lister les principaux consommables (cire, fraises, etc.)
- [ ] Mettre à jour le lien dans le menu et les cartes produits

---

## Phase 5 – Préparation production

### 5.1 Avant le déploiement
**Priorité** : critique  
**Effort** : ~20 min

- [ ] Vérifier tous les liens internes (pas de 404)
- [ ] Tester en local : ouvrir chaque page et vérifier l'affichage
- [ ] Tester sur mobile (Chrome DevTools ou appareil réel)
- [ ] Remplacer les placeholders (WhatsApp, email si besoin)
- [ ] Vérifier que le formulaire envoie bien (avec Formspree ou équivalent)

---

### 5.2 Hébergement et domaine
**Priorité** : critique  
**Effort** : variable

- [ ] Choisir la méthode : FTP OVH, Netlify, Vercel, autre
- [ ] Configurer le domaine `shamed.ma` ou sous-domaine de test
- [ ] Activer HTTPS (généralement inclus)
- [ ] Si remplacement du WordPress : sauvegarder l'ancien site et prévoir une redirection

---

## Phase 6 – erp.shamed.ma (Back-office / ERP)

**Objectif** : Créer un espace de gestion interne accessible via **erp.shamed.ma** pour gérer les commandes, le stock, les clients et la facturation.

### 6.1 Choix de la solution
**Priorité** : haute  
**Effort** : décision + cadrage

Options à évaluer :

| Option | Description | Avantages | Inconvénients |
|--------|-------------|-----------|---------------|
| **A. ERP custom** | Développement sur mesure (Next.js, React, etc.) | Adapté 100 % aux besoins, contrôle total | Temps de dev important |
| **B. Adapter TacTac/DOUMA** | Réutiliser le projet dental manager existant (tactac) | Base déjà prête, rôles Admin/Comptable/Magasiner | Adaptation au contexte Shamed (Kerox, produits) |
| **C. Odoo / solution existante** | ERP open source ou SaaS | Fonctionnel rapidement, communauté | Moins flexible, licence éventuelle |
| **D. Hybride** | Site vitrine + modules ciblés (commandes, devis) | Progressif, MVP rapide | Risque de dispersion |

- [ ] Définir le périmètre minimal (MVP) : commandes ? stock ? facturation ? clients ?
- [ ] Choisir l'option (A, B, C ou D)
- [ ] Lister les rôles utilisateurs (admin, commercial, magasinier, etc.)

---

### 6.2 Fonctionnalités cibles (MVP proposé)
**Priorité** : haute  
**Effort** : selon option retenue

| Module | Description | Priorité |
|--------|-------------|----------|
| **Authentification** | Connexion sécurisée, gestion des comptes | Obligatoire |
| **Gestion des produits** | Catalogue Kerox (Zircone, PMMA, Résines 3D, consommables) | Obligatoire |
| **Gestion des clients** | Laboratoires, prothésistes, contacts | Obligatoire |
| **Commandes / Devis** | Création, suivi, statuts | Obligatoire |
| **Stock** | Suivi des entrées/sorties (optionnel en MVP) | Moyenne |
| **Facturation** | Édition factures, PDF | Haute |
| **Tableau de bord** | Vue synthèse (CA, commandes en cours, alertes) | Haute |
| **Livraisons** | Suivi des livraisons, bons de livraison | Moyenne |

- [ ] Valider la liste des modules pour le MVP
- [ ] Définir les champs métier (numéros de commande, formats, etc.)

---

### 6.3 Infrastructure technique
**Priorité** : haute  
**Effort** : ~2–4 h selon stack

- [ ] Base de données (PostgreSQL recommandé, ou hébergeur type Vercel/Supabase)
- [ ] Hébergement dédié pour l'ERP (Vercel, OVH VPS, Railway, etc.)
- [ ] Configuration DNS : sous-domaine **erp.shamed.ma** → application ERP
- [ ] Certificat SSL (HTTPS) pour erp.shamed.ma
- [ ] Environnement de développement / staging (ex. erp-dev.shamed.ma ou localhost)
- [ ] Sauvegardes automatiques (DB + fichiers)

---

### 6.4 Sécurité et accès
**Priorité** : critique  
**Effort** : ~1–2 h

- [ ] Accès restreint : pas d'indexation dans Google (`robots.txt`, `<meta name="robots" content="noindex, nofollow">`)
- [ ] Authentification robuste (JWT, sessions sécurisées)
- [ ] HTTPS obligatoire
- [ ] Limitation des tentatives de connexion (rate limiting)
- [ ] Politique de mots de passe (complexité, expiration si besoin)
- [ ] Séparation nette : site vitrine (public) vs ERP (privé, authentifié)

---

### 6.5 Intégration site vitrine ↔ ERP
**Priorité** : moyenne  
**Effort** : variable

- [ ] Lien discret "Espace pro" ou "Connexion" sur www.shamed.ma → erp.shamed.ma (réservé aux clients connectés ou internes selon choix)
- [ ] Ou : formulaire de contact / demande de devis qui crée une entrée dans l'ERP
- [ ] Cohérence visuelle (charte Shamed : navy, cuivre) entre site vitrine et ERP

---

### 6.6 Planning ERP (indicatif)

| Étape | Délai estimé |
|-------|--------------|
| Décision + cadrage (6.1, 6.2) | 1–2 semaines |
| Choix technique + infra (6.3, 6.4) | 1 semaine |
| Développement MVP (selon option) | 4–12 semaines |
| Tests + mise en production | 1–2 semaines |

**Note** : Si option B (adapter TacTac), le délai peut être réduit grâce au code existant.

---

## Priorisation recommandée

### Site vitrine (www.shamed.ma)

| Ordre | Tâche | Phase |
|-------|-------|-------|
| 1 | Menu mobile (hamburger) | 1.1 |
| 2 | Images (dossier + vérification) | 1.2 |
| 3 | Numéro WhatsApp + formulaire contact | 1.3 |
| 4 | Meta descriptions + SEO de base | 3.1 |
| 5 | Corrections navigation (liens dropdown) | 2.1 |
| 6 | Footer (mentions légales, téléphone) | 2.2 |
| 7 | Lazy loading images | 3.2 |
| 8 | Accessibilité de base | 2.2 |
| 9 | Page Consommables (optionnel) | 4.2 |

### ERP (erp.shamed.ma)

| Ordre | Tâche | Phase |
|-------|-------|-------|
| 10 | Choix solution (custom / TacTac / Odoo) | 6.1 |
| 11 | Définition MVP (modules, rôles) | 6.2 |
| 12 | Infrastructure (DB, hébergement, DNS) | 6.3 |
| 13 | Sécurité (auth, HTTPS, noindex) | 6.4 |
| 14 | Développement / adaptation | 6.2 |
| 15 | Intégration site vitrine ↔ ERP | 6.5 |

---

## Estimation totale

### Site vitrine (Phases 1–5)

- **Phase 1** (bloquants) : ~2–3 h  
- **Phase 2** (UX) : ~1,5–2 h  
- **Phase 3** (SEO/Perf) : ~1–1,5 h  
- **Phase 4** (Contenu) : variable  
- **Phase 5** (Production) : ~1 h + config hébergement  

**Total minimum pour un site prêt à publier** : ~5–7 heures

### ERP erp.shamed.ma (Phase 6)

- **Cadrage + choix** : 1–2 semaines  
- **Infra + sécurité** : ~3–6 h  
- **Développement MVP** : 4–12 semaines (selon option : custom, TacTac, Odoo)  
- **Mise en production** : 1–2 semaines  

**Total ERP** : ~2–4 mois (ou moins si adaptation de TacTac)

---

## Architecture cible

```
shamed.ma
├── www.shamed.ma (ou shamed.ma)     → Site vitrine (HTML statique)
└── erp.shamed.ma                    → Back-office / ERP (app métier)
```

- **Site vitrine** : présentation, catalogue produits, contact, devis.
- **ERP** : gestion interne, commandes, stock, clients, facturation (accès authentifié).

---

## Notes

- Le design actuel (glassmorphism, palette navy/cuivre) est cohérent et professionnel.
- Le site est adapté à un déploiement statique (HTML/CSS/JS).
- Une fois la Phase 1 terminée, le site peut être mis en ligne sur un sous-domaine pour tests.
- L'ERP peut être développé en parallèle du site vitrine ; le sous-domaine erp.shamed.ma reste indépendant.
