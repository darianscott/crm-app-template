export async function deleteRequest(payload) {

    const response = await fetch('api/delete/delete', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)/c
    });

    const data = await response.json();
    console.log('Delete Respnse:', data);
}
