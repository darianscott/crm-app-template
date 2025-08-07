/**
 * Sends a POST request to the server endpoint for fetching a predefined report.
 *
 * @param {Object} payload - The payload containing the necessary report parameters.
 * @returns {Awaiting the return} Awaiting the response to the server's request.
 */
export async function getPredefinedReportPayload(payload) {
    return await fetch(`/api/reports/defined`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    });
}