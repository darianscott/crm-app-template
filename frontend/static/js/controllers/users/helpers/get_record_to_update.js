export async function getRecordToUpdate() {
const form = document.getElementById(form);
    const fields = {};
    let resource = 'clients';

    // Select only input, select, and textarea elements inside the form
    form.querySelectorAll('input').forEach(el => {
        // Skip disabled or empty fields
        if (!el.disabled && el.value.trim() !== '') {
            fields[el.name] = el.value.trim();
            // Capture resource if defined
        }
    });

    // Validate: Make sure we have at least one field to send
    if (Object.keys(fields).length === 0) {
        console.error('No fields provided for payload.');
        alert('Please fill out at least one field before submitting.');
        return;
    }

    // Build payload
    const payload = {
        resource: resource,
        fields: fields
    };

    console.log('Payload being sent:', payload);

    sendRecordRequest(payload); 

}