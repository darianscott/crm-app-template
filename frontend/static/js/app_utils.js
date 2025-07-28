window.AppUtils = {


    /*** --------------------------------------------------------------------- *
     *    This Section is focused on setting, restoring, or saving user focus. *
     *    -------------------------------------------------------------------- *
    */

    setDefaultFocus() {
        const selector = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
        const interactive = document.querySelector(selector);
        if (interactive && typeof interactive.focus === 'function') {
            interactive.focus();
        }
    },


    restoreFocus() {
        const lastId = localStorage.getItem('lastFocusedId');
        if (lastId) {
            const el = document.getElementById(lastId);
        if (el && typeof el.focus === 'function') {
            el.focus();
        } else {
            AppUtils.setDefaultFocus();
        }}
    },


    saveFocus() {
        const active = document.activeElement;
        if (active && active.id) {
            localStorage.setItem('lastFocusedId', active.id);
        }
    },


    /*** --------------------------------------------------------------------- *
     *    This Section is focused injecting the form and showing Modal.        *
     *    -------------------------------------------------------------------- *
    */

    async injectForm(formPath, formId) {
        const modalContent = document.getElementById(formId)
        fetch(formPath)
            .then(response => response.text())
            .then(html => {
                modalContent.innerHTML = html;
            })
          .catch(error => console.error('Error fetching form content:', error));
        },
    },


    function toggleModalVisibility(elementId, show) {
        if (elementId) {
            if (show) {
                modal.showModal();
            } else {
                modal.close();
            }
        };
    }



    /*** --------------------------------------------------------------------- *
     *    This Section is focused form specific logic                        . *
     *    -------------------------------------------------------------------- *
    */

    function exposeSectionsByClass(targetClass) {
        const allFields = document.querySelectorAll('section');

        AppUtils.clearFields();

        // Then apply enable/disable logic
        allFields.forEach(section => {
            const controls = section.querySelectorAll('input, select, textarea, button');
                if (secton.classList.contains(targetClass)) {
                    controls.forEach(control => {
                     control.disabled = false;
                    section.classlist.add('active')})                    
                 } else {
                    section.disabled = true;
                    section.classList.remove('active');
                };
        });
    }


    async function getDataIfActive() {
       async function getDataIfActive(targetClass) {
    const fields = document.querySelectorAll(`section.${targetClass}.active input, section.${targetClass}.active textarea`);
        const data = {};
        const missingFields = [];

        fields.forEach(field => {
            if (
                field.type !== 'checkbox' &&
                !field.value?.trim() &&
                !field.hasAttribute('data-optional')
            ) {
                missingFields.push(field);
                field.classList.add('validation-error');
            }
        });

        if (missingFields.length > 0) {
            const fieldNames = missingFields.map(f => f.name || f.id || '[unnamed]');
            const result = await Swal.fire({
                title: 'Incomplete Fields',
                html: `You left these blank:<br><strong>${fieldNames.join(', ')}</strong><br>Do you want to leave them empty?`,
                icon: 'question',
                showCancelButton: true,
                confirmButtonText: 'Yes, continue',
                cancelButtonText: 'No, I’ll fix them'
            });

            if (!result.isConfirmed) {
                missingFields[0]?.focus();
                return null; // Exit early
            }

            // Fill missing fields with placeholder or data-default
            missingFields.forEach(field => {
                field.value = field.getAttribute('data-default') || '[blank]';
            });
        }

        // Build clean data payload
        fields.forEach(field => {
            const name = field.name;
            if (!name) return;

            let value;
            switch (field.type) {
                case 'checkbox':
                    value = field.checked;
                    break;
                case 'number':
                    value = field.value ? Number(field.value) : null;
                    break;
                case 'date':
                    value = field.value ? new Date(field.value).toISOString() : null;
                    break;
                default:
                    value = field.value.trim();
            }

            data[name] = value;
            });

            return data;
        };
    }



    async function sendToRoute(targetClass, data) {
        const [action, resource] = targetClass.split('-');
        const methodMap = {
            post: 'POST',
            update: 'UPDATE'
        };

        const method = methodMap[action] || 'POST';
        const endpoint = `/api/${resource}`;

        try {
            const response = await fetch(endpoint, {
            method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
            });

            const result = await response.json();
            return result; // Or logAction here, or trigger toast, etc.
        } catch (err) {
            console.error('Route dispatch failed:', err);
        }
    };

async function saveFormData() {
    const data = AppUtils.getDataIfActive('active'); // Already validated

    try {
        await AppUtils.sendToRoute(targetClass, data);
        notify('Saved successfully'); // SweetAlert toast
        AppUtils.clearFields();
        AppUtils.disableAllSectionns();
    } catch (error) {
        console.error('Save failed:', error);
        notify('Save failed', 'error');
    }
}

    /*** --------------------------------------------------------------------- *
     *    This Section is focused misc form functions.                         *
     *    -------------------------------------------------------------------- *
    */

    async function logAction(entry) {
        await fetch('/api/logs/write', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(entry)
        });
    };


    function clearFields() {
        resetForm();
    };


    function disableAllSectionns() {
        let element = document.querySelectorAll('section input, section select, section textarea;')
        element.forEach(el => {
            el.disabled = true;
        });
        document.querySelectorAll('section').forEach(section => {
        section.classList.remove('active');
        });
    }



