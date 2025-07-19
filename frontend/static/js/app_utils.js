window.AppUtils = {


    clearFormInputs(formId) {
        const form = document.getElementById(formId);
        if (!form) {
            console.warn(`Form with ID "${formId}" not found.`);
            return;
        };
        form.reset();
    },


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


    async injectForm(formPath, formId) {
        const modalContent = document.getElementById(formId)
        fetch(formPath)
            .then(response => response.text())
            .then(html => {
                modalContent.innerHTML = html;
            })
            .catch(error => console.error('Error fetching form content:', error));
    },


    toggleModalVisibility(elementId, show) {
        if (elementId) {
            if (show) {
                modal.showModal();
            } else {
                modal.close();
            }
        };
    },


    exposeFieldsByClass(targetClass) {
        const allFields = document.querySelectorAll('input, select, textarea');

        allFields.forEach(field => {
            const fieldClasses = field.classList;

            if (fieldClasses.contains(targetClass)) {
                field.classList.add('active');
                field.disabled = false; // Optional: enable the input
            };
        });
    },

    async getDataByClass(targetClass) {
        const fields = document.querySelectorAll(targetClass);
        const data = {};
        const missingFields = [];

    // Check for blanks before extracting
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
            // Focus the first empty field
            missingFields[0]?.focus();
            return null;
        }

            // Optional: fill with placeholder
        missingFields.forEach(field => {
            field.value = field.getAttribute('data-default') || '[blank]';
        });

        // Now build clean data payload
        fields.forEach(field => {
            const name = field.name;
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

            if (name) data[name] = value;
            });

            return data;
        };
    },


    async  giveToRoute(targetClass, data) {
        const [action, resource] = target.split('-');
        const methodMap = {
            add: 'POST',
            update: 'PUT',
            assign: 'POST',
            enter: 'POST'
            
        };

        const method = methodMap[action] || 'POST';
        const endpoint = `/api/${resource}/${action}`;

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
    },


    async logAction(entry) {
        await fetch('/api/logs/write', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(entry)
        });
    },


    clearFields() {
        resetForm();
    },


    disableAllFields() {
        let element = document.querySelectorAll('input, select, textarea, checkbox, radio')
        element.forEach(el => {
            el.disabled = true;
        });
    },
}
