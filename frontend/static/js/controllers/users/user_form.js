import AppUtils from './app_utils.js'


async function init() {

    document.addEventListener('DOMContentLoaded', () => {
    },
      AppUtils.setDefaultFocus());

    document.addEventListener('click', async (event) => {


      const btn = event.target.closest('[data-target-class]');
      if (!btn) return;

      const targetClass = btn.dataset.targetClass;

      switch (targetClass) {
        case 'add-user':
        case 'update-user':
        case 'reset-password':
        case 'enter-training':
        case 'set-reminders':
        case 'enter-license':
        case 'audit-login':
        case 'delete-user':
          AppUtils.exposeFieldsByClass(targetClass);
          break;

        case 'saveButton':
          AppUtils.saveFormData();
        

        case 'save-exit':
          AppUtils.saveFormData();
          AppUtils.removeForm();
          AppUtils.toggleModalVisibility('modal-id', false);
          break;
        default:
          console.warn("Unhandled user action:", targetClass);
          break;
      }
    });
}

export { init };
