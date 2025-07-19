import AppUtils from '/app_utils.js'

document.addEventListener('DOMContentLoaded', () => {
    AppUtils.restoreFocus();

    document.addEventListener('click', async (event) => {

        const btn = event.target.closest('[data-form-id]');
        if (!btn) return;

        const formId = btn.dataset.formId;
        const formPath = btn.dataset.formPath;

        if (formId === user-form) {
            AppUtils.saveFocus();
            AppUtils.injectForm(formPath, formId);
            AppUtils.toggleModalVisibility('modal-id', true); 
        } else if (formId === client-form) {
            AppUtils.saveFocus();
            AppUtils.injectForm(formPath, formId);
            AppUtils.toggleModalVisibility('modal-id', true);
        }
    });
});
