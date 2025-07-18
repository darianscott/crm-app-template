import AppUtils from '/app_utils'

document.addEventListener('DOMContentLoaded', () => {
  setDefaultFocus()
  document.addEventListener('click', (event) => {
    clearFields();
    disableAllFields();

    const btn = event.target.closest('data-class');
    if (!btn) return;

    const handler = btn.dataset.handler;
    const targetClass = btn.dataset.targetClass;

    // Dispatch the correct function
    switch (targetClass) {
      case 'add-user':
        exposeFieldsByClass(targetClass); // currentGuid passed from context
        break;
      case 'update-user':
        exposeFieldsByClass(targetClass);
        break;
      case 'reset-password':
        exposeFieldsByClass(targetClass);
        break;
      case 'enter-training':
        exposeFieldsByClass(targetClass);
        break;
      case 'set-reminders':
        exposeFieldsByClass(targetClass);
        break;
      case 'enter-license':
        exposeFieldsByClass(targetClass);
        break;
      case 'audit-login':
        exposeFieldsByClass(targetClass);
        break;
      case 'delete-user':
        exposeFieldsByClass(targetClass);
        break;
      case 'saveButton':
        getDataByClass(event.target);
        giveToRoute(data, event.target);
        break;
      case 'close-modal':
        removeForm();
        toggleModalVisibility();
      default:
        console.warn("Unhandled user action:", handler);
        break;
    }
  });
});
