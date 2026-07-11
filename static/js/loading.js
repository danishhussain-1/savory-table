/**
 * Loading Screen Controller
 * ---------------------------------------------------------------------------
 * Fades out the full-screen loading overlay once the window has fully
 * loaded (all images, fonts, etc). A small minimum-display delay is added
 * so the animation doesn't feel like a jarring flash on fast connections.
 */
(function () {
    'use strict';

    const MIN_DISPLAY_TIME = 900; // milliseconds
    const startTime = Date.now();

    function hideLoadingScreen() {
        const loadingScreen = document.getElementById('loading-screen');
        if (!loadingScreen) return;

        const elapsed = Date.now() - startTime;
        const remainingTime = Math.max(MIN_DISPLAY_TIME - elapsed, 0);

        setTimeout(function () {
            loadingScreen.classList.add('loaded');
            // Remove from DOM after the fade transition finishes to free up
            // memory and avoid it intercepting clicks if something goes wrong
            // with the opacity/visibility transition.
            setTimeout(function () {
                loadingScreen.style.display = 'none';
            }, 650);
        }, remainingTime);
    }

    window.addEventListener('load', hideLoadingScreen);

    // Fallback: if the load event is unusually slow (e.g. slow assets),
    // force-hide the loading screen after 4 seconds so users are never
    // stuck staring at it.
    setTimeout(hideLoadingScreen, 4000);
})();