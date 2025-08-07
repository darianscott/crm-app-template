/**
 * Object representing the configuration for fetching users and new clients they have in the past
 * 30, 60, and 90 days.
 * @constant {Object} newClients
 * @property {Object} payload - The payload defining query parameters.
 * @property {string} payload.resource - The type of resource to query; in this case, "user".
 * @property {string[]} payload.fields - An array of field names to retrieve.
 * @property {Array} payload.filters - An array of filters to apply to the query (currently empty).
 * @property {Array} payload.joins - An array of join operations for related data (currently empty).
 * @property {string} payload.sort_by - The field name used to sort the data; here, "last_name".
 * @property {string} payload.sort_order - The order of sorting; "asc" for ascending.
 * @property {string} payload.format - The format in which to return data; "json".
 */

import { getPredefinedReport } from '/helpers/getPredefinedReport.js'

export async function newClients() {
    const payload = {
        resource: 'clients',
        fields: [
            'last_name',
            'created_at',
            'status',
            'zip_code',
        ],
        filters: [],
        joins: ['user'],
        sort_by: 'user.last_name',
        sort_order: 'asc',
        format: 'json',
        page: 1,
        page_size: 30,
    };

    return await getPredefinedReport(payload);
    
}
