/**
 * Gallery Filter & Lightbox Controller
 * ---------------------------------------------------------------------------
 * 1. Client-side category filtering: clicking a tab shows/hides gallery
 *    items based on their data-category attribute, with no page reload
 *    (all images are already rendered server-side; JS just toggles a
 *    "hidden" class for a smooth, instant filtering experience).
 * 2. Lightbox: clicking any gallery image opens a full-screen preview
 *    overlay with the enlarged photo and its caption.
 */
(function () {
    'use strict';

    /* ------------------------------------------------------------------
       1. Category Filtering
       ------------------------------------------------------------------ */
    const filterTabs = document.querySelectorAll('.gallery-tab');
    const galleryItems = document.querySelectorAll('.gallery-item');

    filterTabs.forEach(function (tab) {
        tab.addEventListener('click', function () {
            const targetCategory = tab.getAttribute('data-category');

            filterTabs.forEach(function (t) { t.classList.remove('active'); });
            tab.classList.add('active');

            galleryItems.forEach(function (item) {
                const itemCategory = item.getAttribute('data-category');
                if (targetCategory === 'all' || itemCategory === targetCategory) {
                    item.classList.remove('hidden');
                } else {
                    item.classList.add('hidden');
                }
            });
        });
    });

    /* ------------------------------------------------------------------
       2. Lightbox
       ------------------------------------------------------------------ */
    const lightboxOverlay = document.getElementById('lightbox-overlay');
    const lightboxImage = document.getElementById('lightbox-image');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const lightboxClose = document.getElementById('lightbox-close');

    if (lightboxOverlay && lightboxImage) {
        galleryItems.forEach(function (item) {
            item.addEventListener('click', function () {
                const img = item.querySelector('img');
                if (!img) return;

                lightboxImage.setAttribute('src', img.getAttribute('src'));
                lightboxImage.setAttribute('alt', img.getAttribute('alt') || '');
                if (lightboxCaption) {
                    lightboxCaption.textContent = img.getAttribute('alt') || '';
                }
                lightboxOverlay.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });

        function closeLightbox() {
            lightboxOverlay.classList.remove('active');
            document.body.style.overflow = '';
        }

        if (lightboxClose) {
            lightboxClose.addEventListener('click', closeLightbox);
        }

        lightboxOverlay.addEventListener('click', function (event) {
            if (event.target === lightboxOverlay) {
                closeLightbox();
            }
        });

        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && lightboxOverlay.classList.contains('active')) {
                closeLightbox();
            }
        });
    }
})();