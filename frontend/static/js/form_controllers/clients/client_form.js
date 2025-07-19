import AppUtils from '.app_utils'

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
        AppUtils.exposeFieldsByClass(targetClass);
        break;
      case 'update-client':
        AppUtils.exposeFieldsByClass(targetClass);
        break;
      case 'send-invite':
        AppUtils.exposeFieldsByClass(targetClass);
        break;
      case 'delete-client':
        AppUtils.exposeFieldsByClass(targetClass);
        break;
      case 'schedule-email':
        AppUtils.exposeFieldsByClass(targetClass);
        break;
      case 'save-testimonial':
        AppUtils.exposeFieldsByClass(targetClass);
        break;
      case 'log-interaction':
        AppUtils.exposeFieldsByClass(targetClass);
        break;
      case 'schedule-appointment':
        AppUtils.exposeFieldsByClass(targetClass);
        break;
      case 'saveButton':
        AppUtils.getDataByClass(event.target);
        AppUtils.giveToRoute(data, event.target);
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
