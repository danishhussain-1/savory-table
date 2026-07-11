/**
 * Custom Select Dropdown
 * ---------------------------------------------------------------------------
 * Progressively enhances every <select class="form-control"> on the page
 * with a fully custom-styled dropdown that matches the dark, gold-accented
 * Savory Table theme — including the OPEN state, which native <select>
 * elements cannot be styled for consistently across browsers.
 *
 * The original <select> element is kept in the DOM (visually hidden) so
 * the form still submits its value normally; this script only builds a
 * visual layer on top and keeps it in sync.
 */
(function () {
    'use strict';

    function enhanceSelect(originalSelect) {
        // Avoid double-enhancing the same select if this script runs twice.
        if (originalSelect.dataset.enhanced === 'true') return;
        originalSelect.dataset.enhanced = 'true';

        // Wrapper that will contain both the hidden native select and the
        // custom visual dropdown.
        const wrapper = document.createElement('div');
        wrapper.className = 'custom-select-wrapper';

        // Insert the wrapper right before the select, then move the select
        // inside it and visually hide it (but keep it functional/focusable
        // for accessibility and native form submission).
        originalSelect.parentNode.insertBefore(wrapper, originalSelect);
        wrapper.appendChild(originalSelect);
        originalSelect.classList.add('custom-select-native');

        // Build the visible trigger button showing the current selection.
        const trigger = document.createElement('div');
        trigger.className = 'custom-select-trigger';
        trigger.setAttribute('tabindex', '0');
        trigger.setAttribute('role', 'button');
        trigger.setAttribute('aria-haspopup', 'listbox');

        const triggerText = document.createElement('span');
        triggerText.className = 'custom-select-trigger-text';

        const triggerArrow = document.createElement('span');
        triggerArrow.className = 'custom-select-arrow';
        triggerArrow.innerHTML = '&#9662;';

        trigger.appendChild(triggerText);
        trigger.appendChild(triggerArrow);
        wrapper.appendChild(trigger);

        // Build the custom options list.
        const optionsList = document.createElement('div');
        optionsList.className = 'custom-select-options';
        optionsList.setAttribute('role', 'listbox');

        const optionEls = [];

        Array.from(originalSelect.options).forEach(function (option) {
            const optionEl = document.createElement('div');
            optionEl.className = 'custom-select-option';
            optionEl.textContent = option.textContent;
            optionEl.setAttribute('data-value', option.value);
            optionEl.setAttribute('role', 'option');

            if (option.selected) {
                optionEl.classList.add('selected');
            }

            optionEl.addEventListener('click', function () {
                originalSelect.value = option.value;
                updateTriggerText();
                optionEls.forEach(function (el) { el.classList.remove('selected'); });
                optionEl.classList.add('selected');
                closeDropdown();
                // Fire a native change event so any other listeners
                // (e.g. form validation scripts) still work as expected.
                originalSelect.dispatchEvent(new Event('change', { bubbles: true }));
            });

            optionEls.push(optionEl);
            optionsList.appendChild(optionEl);
        });

        wrapper.appendChild(optionsList);

        function updateTriggerText() {
            const selectedOption = originalSelect.options[originalSelect.selectedIndex];
            triggerText.textContent = selectedOption ? selectedOption.textContent : '';
        }

        function openDropdown() {
            closeAllDropdowns();
            wrapper.classList.add('open');
        }

        function closeDropdown() {
            wrapper.classList.remove('open');
        }

        trigger.addEventListener('click', function () {
            if (wrapper.classList.contains('open')) {
                closeDropdown();
            } else {
                openDropdown();
            }
        });

        // Keyboard accessibility: open/close with Enter or Space.
        trigger.addEventListener('keydown', function (event) {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                trigger.click();
            } else if (event.key === 'Escape') {
                closeDropdown();
            }
        });

        updateTriggerText();
    }

    function closeAllDropdowns() {
        document.querySelectorAll('.custom-select-wrapper.open').forEach(function (wrapper) {
            wrapper.classList.remove('open');
        });
    }

    // Close any open dropdown when clicking outside of it.
    document.addEventListener('click', function (event) {
        if (!event.target.closest('.custom-select-wrapper')) {
            closeAllDropdowns();
        }
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            closeAllDropdowns();
        }
    });

    // Enhance every matching select currently on the page.
    document.querySelectorAll('select.form-control').forEach(enhanceSelect);
})();