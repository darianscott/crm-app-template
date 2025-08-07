import AppUtils from './app_utils.js'


async function init() {

    document.addEventListener('DOMContentLoaded', () => {

    AppUtils.setDefaultFocus();

    document.addEventListener('click', async (event) => {
    const btn = event.target.closest('[class]');
    if (!btn) return;
        const target  = btn.class;
    let resource = target

    switch (target) {
        
        case 'user':
        
            break;

        case 'client':
            
            break;

        case 'predefined':
            break;

        case 'get-report':
            await buildPayload(resource);
            break;

        case 'get-exit':
            break;



    }  
  
export { init };
  
  
  
  
  
