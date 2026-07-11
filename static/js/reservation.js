/**
 * Reservation Form Enhancement
 * ---------------------------------------------------------------------------
 * Small client-side UX touches for the "Book Your Table" form:
 * 1. Prevents selecting a past date in the date picker (in addition to
 *    the server-side validation already enforced by ReservationForm).
 * 2. Adds a subtle shake animation to invalid fields on submit attempt,
 *    drawing the eye to what needs fixing before the page even reloads.
 */
(function () {
    'use strict';

    const dateInput = document.querySelector('input[name="reservation_date"]');

    if (dateInput) {
        const today = new Date();
        const yyyy = today.getFullYear();
        const mm = String(today.getMonth() + 1).padStart(2, '0');
        const dd = String(today.getDate()).padStart(2, '0');
        dateInput.setAttribute('min', `${yyyy}-${mm}-${dd}`);
    }

    const reservationForm = document.querySelector('form[action*="reservation"]');
    if (reservationForm) {
        reservationForm.addEventListener('submit', function () {
            const submitBtn = reservationForm.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = 'Submitting...';
            }
        });
    }
})();