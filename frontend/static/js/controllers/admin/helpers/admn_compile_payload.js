export async function compilePayload(method, formId) {
    const element = 'Input';
    let fields = {};
    let resource = '';
    let payload = {};

    for (element of formId.elements) {
        if (element === document.activeElement && element.innerText.value !== '')
            
            fields = [element.name, element.innerText.value];

            if (element.data-resource) {
                resource = element.data-resource;
            }

        if (element.innerText.value.trim() === '') {
            error
        }
    }


    payload.resource = resource;
    payload.fields = fields;    
    
    if (method === 'update')
        patchRequest(payload);

    if (method === 'delete')
        deleteRequest(payload);
    
    postRequest(payload);

    resetForm();
    
}