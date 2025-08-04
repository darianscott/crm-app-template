export async function postRequest(payload) {

    const response = await fetch('/api/post/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)/c
    });

    const data = await response.json();
    console.log('Create Respnse:', data);
}
