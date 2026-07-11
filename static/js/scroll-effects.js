/**
 * Scroll Effects Controller
 * ---------------------------------------------------------------------------
 * Handles:
 * 1. Sticky navbar background/shrink on scroll
 * 2. Scroll-to-top button visibility + click behavior
 * 3. Scroll-reveal animations for elements with the "reveal-on-scroll" class
 *    (used across home, about, menu, gallery pages for fade-up entrances)
 */
(function () {
    'use strict';

    const navbar = document.getElementById('navbar');
    const scrollTopBtn = document.getElementById('scroll-top-btn');
    const SCROLL_THRESHOLD = 60;

    function handleScroll() {
        const scrollY = window.scrollY || window.pageYOffset;

        // Navbar background on scroll
        if (navbar) {
            if (scrollY > SCROLL_THRESHOLD) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }

        // Scroll-to-top button visibility
        if (scrollTopBtn) {
            if (scrollY > 400) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        }
    }

    // Throttle scroll handling using requestAnimationFrame for smooth,
    // performant behavior even on lower-powered devices.
    let ticking = false;
    window.addEventListener('scroll', function () {
        if (!ticking) {
            window.requestAnimationFrame(function () {
                handleScroll();
                ticking = false;
            });
            ticking = true;
        }
    });

    // Run once on initial load in case the page loads already scrolled
    // (e.g. anchor link navigation or browser scroll restoration).
    handleScroll();

    // Scroll-to-top button click behavior
    if (scrollTopBtn) {
        scrollTopBtn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Scroll-reveal animations using IntersectionObserver.
    // Any element with class "reveal-on-scroll" fades/slides into view
    // the first time it enters the viewport, then stops observing it
    // (one-time reveal, not a repeating effect).
    const revealElements = document.querySelectorAll('.reveal-on-scroll');

    if ('IntersectionObserver' in window && revealElements.length > 0) {
        const revealObserver = new IntersectionObserver(function (entries, observer) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -50px 0px',
        });

        revealElements.forEach(function (el) {
            revealObserver.observe(el);
        });
    } else {
        // Fallback for browsers without IntersectionObserver support:
        // simply reveal everything immediately.
        revealElements.forEach(function (el) {
            el.classList.add('revealed');
        });
    }
})();