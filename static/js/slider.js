/**
 * Hero Slider Controller
 * ---------------------------------------------------------------------------
 * Powers the home page hero image slider (matching the reference design's
 * left/right arrow navigation). Auto-advances every 6 seconds and pauses
 * auto-advance temporarily whenever the user manually navigates, so manual
 * interaction always feels responsive rather than fighting the timer.
 */
(function () {
    'use strict';

    const slider = document.getElementById('hero-slider');
    if (!slider) return;

    const slides = slider.querySelectorAll('.hero-slide');
    const prevBtn = document.getElementById('hero-prev');
    const nextBtn = document.getElementById('hero-next');
    const dotsContainer = document.getElementById('hero-dots');

    if (slides.length === 0) return;

    let currentIndex = 0;
    let autoAdvanceTimer = null;
    const AUTO_ADVANCE_INTERVAL = 6000;

    // Build navigation dots dynamically based on how many slides exist.
    if (dotsContainer) {
        slides.forEach(function (_, index) {
            const dot = document.createElement('button');
            dot.classList.add('hero-dot');
            dot.setAttribute('aria-label', 'Go to slide ' + (index + 1));
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', function () {
                goToSlide(index);
                restartAutoAdvance();
            });
            dotsContainer.appendChild(dot);
        });
    }

    const dots = dotsContainer ? dotsContainer.querySelectorAll('.hero-dot') : [];

    function goToSlide(index) {
        slides[currentIndex].classList.remove('active');
        if (dots[currentIndex]) dots[currentIndex].classList.remove('active');

        currentIndex = (index + slides.length) % slides.length;

        slides[currentIndex].classList.add('active');
        if (dots[currentIndex]) dots[currentIndex].classList.add('active');
    }

    function nextSlide() {
        goToSlide(currentIndex + 1);
    }

    function prevSlide() {
        goToSlide(currentIndex - 1);
    }

    function startAutoAdvance() {
        autoAdvanceTimer = setInterval(nextSlide, AUTO_ADVANCE_INTERVAL);
    }

    function restartAutoAdvance() {
        clearInterval(autoAdvanceTimer);
        startAutoAdvance();
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function () {
            nextSlide();
            restartAutoAdvance();
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', function () {
            prevSlide();
            restartAutoAdvance();
        });
    }

    // Pause auto-advance while the user hovers over the slider, resume
    // when they move away — a small UX touch matching premium sites.
    slider.addEventListener('mouseenter', function () {
        clearInterval(autoAdvanceTimer);
    });
    slider.addEventListener('mouseleave', function () {
        startAutoAdvance();
    });

    startAutoAdvance();
})();