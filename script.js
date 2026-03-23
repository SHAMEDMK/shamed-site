// Intersection Observer for fade-in animations
document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('appear');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach(el => observer.observe(el));

    // Simple sticky nav effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Mobile menu (hamburger)
    const navToggle = document.querySelector('.nav-toggle');
    const mobileMenu = document.getElementById('mobileMenu');
    const closeMobileMenu = () => {
        mobileMenu.classList.remove('is-open');
        if (navToggle) {
            navToggle.setAttribute('aria-expanded', 'false');
            navToggle.setAttribute('aria-label', 'Ouvrir le menu');
        }
        document.body.style.overflow = '';
    };
    if (navToggle && mobileMenu) {
        navToggle.addEventListener('click', () => {
            const isOpen = mobileMenu.classList.toggle('is-open');
            navToggle.setAttribute('aria-expanded', isOpen);
            navToggle.setAttribute('aria-label', isOpen ? 'Fermer le menu' : 'Ouvrir le menu');
            document.body.style.overflow = isOpen ? 'hidden' : '';
        });
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMobileMenu);
        });
        /* Fermer en cliquant sur le fond (overlay) */
        mobileMenu.addEventListener('click', (e) => {
            if (e.target === mobileMenu) closeMobileMenu();
        });
    }

    // Dropdown Produits : ouverture au clic sur appareils tactiles (hover non disponible)
    const navItem = document.querySelector('.nav-item');
    if (navItem) {
        const prodLink = navItem.querySelector('a');
        const dropdown = navItem.querySelector('.dropdown');
        const isTouch = window.matchMedia('(hover: none)').matches;
        if (isTouch && prodLink && dropdown) {
            prodLink.addEventListener('click', (e) => {
                e.preventDefault();
                navItem.classList.toggle('is-open');
            });
            document.addEventListener('click', (e) => {
                if (!navItem.contains(e.target)) navItem.classList.remove('is-open');
            });
        }
    }

    // Indicateur page active dans le dropdown (basé sur l'URL courante)
    const path = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.dropdown a').forEach(a => {
        const href = (a.getAttribute('href') || '').split('#')[0].trim();
        const linkPath = href ? href.split('/').pop() : '';
        if (path && linkPath && path === linkPath) a.classList.add('active');
    });
});
