export async function sendRecordRequest(payload) {
    try {
        const response = await fetch('/api/record/custom', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
        });

        if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error || 'Report request failed');
        };

        return await response.text()
        } catch (err) {
        console.error('Report error:', err.message);
        throw err;
    };
}
