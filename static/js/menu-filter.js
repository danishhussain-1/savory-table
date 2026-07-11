/**
 * Menu Search Box Enhancement
 * ---------------------------------------------------------------------------
 * The category filter tabs and pagination on the Menu page are handled
 * server-side (via query parameters ?category=slug&q=term&page=n) so that
 * search engines can crawl and index every filtered view with a real URL.
 *
 * This script only adds small client-side conveniences on top of that:
 * 1. Auto-submits the search form when the user presses Enter (already
 *    default browser behavior, but we also debounce a "live typing"
 *    visual cue so the UI feels responsive).
 * 2. Highlights the active category tab based on the current URL,
 *    as a defensive fallback in case template-side "active" logic
 *    doesn't catch an edge case.
 */
(function () {
    'use strict';

    const searchInput = document.getElementById('menu-search-input');
    const searchForm = document.getElementById('menu-search-form');

    if (searchInput && searchForm) {
        // Small visual feedback: add a subtle "searching" class while
        // the user types, removed once they pause (purely cosmetic).
        let typingTimer;
        searchInput.addEventListener('input', function () {
            searchForm.classList.add('is-typing');
            clearTimeout(typingTimer);
            typingTimer = setTimeout(function () {
                searchForm.classList.remove('is-typing');
            }, 600);
        });
    }

    // Defensive active-tab highlighting based on the current query string.
    const params = new URLSearchParams(window.location.search);
    const activeCategory = params.get('category') || '';
    const categoryTabs = document.querySelectorAll('.category-tab');

    categoryTabs.forEach(function (tab) {
        const tabCategory = tab.getAttribute('data-category') || '';
        if (tabCategory === activeCategory) {
            tab.classList.add('active');
        }
    });
})();