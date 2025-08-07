async function compilePayload(method) {
    const form = document.getElementById(form);
    const fields = [];
    let resource = '';
    const resource_id = document.getElementById('hidden').value.trim();

    // Select only input, select, and textarea elements inside the form
    form.querySelectorAll('input, select, textarea').forEach(el => {
        // Skip disabled or empty fields
        if (!el.disabled && el.value.trim() !== '') {
            fields[el.name] = el.value.trim();
            // Capture resource if defined
            if (el.dataset.resource) {
                resource = el.dataset.resource;
            }
        }
    });

    // Validate: Make sure we have at least one field to send
    if (Object.keys(fields).length === 0) {
        console.error('No fields provided for payload.');
        alert('Please fill out at least one field before submitting.');
        return;
    }


    // Build payload based on method
    const payload = {};
    if (method === 'update') {
        Object.assign(payload, {
            resource_id: resource_id || null,
            resource: resource,
            fields: fields
        });
    } else {
        Object.assign(payload, {
            resource: resource,
            fields: fields
        });
    }

    console.log('Payload being sent:', payload);
    console.log('Payload being sent:', payload);

    // Determine which request to send
    if (method === 'update') {
        await patchRequest(payload);
    } else if (method === 'create') {
        await postRequest(payload);
    } else {
        console.error('Invalid method specified.');
    }
    // Reset the form after submission
    form.reset();
}
