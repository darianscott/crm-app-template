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
            // Clear everything first
            if (!field.hasAttribute('data-preserve')) {
                field.value = '';
            }

            // Then apply enable/disable logic
            if (field.classList.contains(targetClass)) {
                field.disabled = false;
                field.classList.add('active');
            } else {
                field.disabled = true;
                field.classList.remove('active');
            }
        });
    },


    async getDataByClass(targetClass) {
        const fields = document.querySelectorAll(targetClass);
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
    },



    async sendToRoute(targetClass, data) {
        const [action, resource] = targetClass.split('-');
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


    async saveFormData() {
        const data = AppUtils.getDataByClass(`.${targetClass}`);
                  
        try {
            await AppUtils.sendToRoute(targetClass, data);
        } catch (error) {
            console.error('Save failed:', error);
        }
        break;
    }



}
