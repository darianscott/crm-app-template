import AppUtils from './app_utils.js'


async function init() {

    document.addEventListener('DOMContentLoaded', () => {

    let method = '';
    AppUtils.setDefaultFocus();

    document.addEventListener('click', async (event) => {


      const btn = event.target.closest('[data-target-class]');
      if (!btn) return;

      const targetClass = btn.dataset.targetClass;

      switch (targetClass) {
        case 'update-user':
          toggleClientName();
           break;

        case 'add=usert':
        case 'add-training':
        case 'add-license':
        case 'delete-user':
        case 'delete-client':

        case 'saveButton':
          AppUtils.saveFormData();
          break;

       case 'getButton':
          AppUtils.getClientData();
          AppUtils.exposeSecionsByClass();
          showClientData();
          break;

        case 'updateButton':
          AppUtils.saveFormData();
          break;

        case 'save-exit':
          AppUtils.saveFormData();
          AppUtils.removeForm();
          AppUtils.toggleModalVisibility('modal-id', false);
          break;
        default:
          console.warn("Unhandled user action:", targetClass);
          break;
      };
    })
  })
}  
  
export { init };
