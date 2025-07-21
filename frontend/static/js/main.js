import AppUtils from '/app_utils.js'
import { init as initUserForm } from '/form_controllers/users/user_form.js'
import { init as initIndex } from '/page_controllers/index/index.js'
import { init as initClientForm } from '/form_controllers/clients/client_form.js'

document.addEventListener('DOMContentLoaded', () => {
    initIndex();
    AppUtils.restoreFocus();

    document.addEventListener('click', async (event) => {

        const btn = event.target.closest('[data-form-id]');
        if (!btn) return;

        const formId = btn.dataset.formId;
        const formPath = btn.dataset.formPath;

        if (formId === user-form) {
            AppUtils.saveFocus();
            AppUtils.injectForm(formPath, formId);
            initUserForm();
            AppUtils.toggleModalVisibility('modal-id', true); 
        } else if (formId === client-form) {
            AppUtils.saveFocus();
            AppUtils.injectForm(formPath, formId);
            initClientForm();
            AppUtils.toggleModalVisibility('modal-id', true);
        }
    });
});
