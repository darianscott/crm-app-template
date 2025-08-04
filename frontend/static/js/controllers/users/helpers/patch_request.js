export async function patchRequest(payload) {

    const response = await fetch('/api/patch/update', {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)/c
    });

    const data = await response.json();
    console.log('Update Respnse:', data);
}
