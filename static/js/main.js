/**
 * Main Site Script
 * ---------------------------------------------------------------------------
 * Handles global, site-wide interactive behavior that isn't specific to a
 * single page:
 * 1. Mobile navbar toggle (hamburger menu open/close)
 * 2. Auto-closing mobile menu when a nav link is clicked
 * 3. Auto-dismissing success/info messages after a few seconds
 */
(function () {
    'use strict';

    /* ------------------------------------------------------------------
       1 & 2. Mobile Navbar Toggle
       ------------------------------------------------------------------ */
    const navbarToggle = document.getElementById('navbar-toggle');
    const navbarLinks = document.getElementById('navbar-links');

    if (navbarToggle && navbarLinks) {
        navbarToggle.addEventListener('click', function () {
            navbarLinks.classList.toggle('open');
            navbarToggle.classList.toggle('active');
        });

        // Close the mobile menu automatically once a link is tapped,
        // so users aren't stuck looking at an open menu after navigating.
        const navLinks = navbarLinks.querySelectorAll('.nav-link');
        navLinks.forEach(function (link) {
            link.addEventListener('click', function () {
                navbarLinks.classList.remove('open');
                navbarToggle.classList.remove('active');
            });
        });

        // Close the mobile menu if the user clicks/taps outside of it.
        document.addEventListener('click', function (event) {
            const isClickInsideMenu = navbarLinks.contains(event.target);
            const isClickOnToggle = navbarToggle.contains(event.target);
            if (!isClickInsideMenu && !isClickOnToggle && navbarLinks.classList.contains('open')) {
                navbarLinks.classList.remove('open');
                navbarToggle.classList.remove('active');
            }
        });
    }

    /* ------------------------------------------------------------------
       3. Auto-dismiss success/info toast messages after 5 seconds
       ------------------------------------------------------------------ */
    const autoDismissAlerts = document.querySelectorAll('.alert-success, .alert-info');
    autoDismissAlerts.forEach(function (alertEl) {
        setTimeout(function () {
            alertEl.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            alertEl.style.opacity = '0';
            alertEl.style.transform = 'translateX(40px)';
            setTimeout(function () {
                alertEl.remove();
            }, 500);
        }, 5000);
    });
})();