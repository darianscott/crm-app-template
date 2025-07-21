import AppUtils from './app_utils.js'


function init() {

  document.addEventListener('DOMContentLoaded', () => {
    AppUtils.setDefaultFocus();

    document.addEventListener('click', async (event) => {
      AppUtils.clearFormInputs('yourFormId'); // Optional
      AppUtils.disableAllFields();

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
          const data = AppUtils.getDataByClass(`.${targetClass}`);
          await AppUtils.giveToRoute(`${targetClass}`, data);
          break;

        case 'close-modal':
          AppUtils.removeForm();
          AppUtils.toggleModalVisibility('modal-id', false);
          break;

        default:
          console.warn("Unhandled user action:", targetClass);
          break;
      }
    });
  });
}

export { init };
