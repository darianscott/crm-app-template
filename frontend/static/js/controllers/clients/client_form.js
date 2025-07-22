import AppUtils from '.app_utils'


async function init() {
  document.addEventListener('DOMContentLoaded', () => {
    setDefaultFocus()
    document.addEventListener('click', (event) => {
      AppUtils.clearFields();
      AppUtils.disableAllFields();

      const btn = event.target.closest('[data-target-class]');
      if (!btn) return;

      const targetClass = btn.dataset.targetClass;

      // Dispatch the correct function
      switch (targetClass) {
        case 'add-client':
        case 'update-client':
        case 'send-invite':
        case 'delete-client':
        case 'schedule-email':
        case 'save-testimonial':
        case 'log-interaction':
        case 'schedule-appointment':
          AppUtils.exposeFieldsByClass(targetClass);
          break;

        case 'saveButton':
          AppUtils.getDataByClass(event.target);
          AppUtils.sendToRoute(data, event.target);
          break;
        case 'close-modal':
          AppUtils.removeForm();
          AppUtils.toggleModalVisibility();
          break;
        default:
          console.warn("Unhandled client action:", targetClass);
          break;
      }
    });
  });
}
