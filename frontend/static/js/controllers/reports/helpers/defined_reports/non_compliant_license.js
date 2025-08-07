/**
 * Object representing the configuration for fetching users that are about to be non-compliant with  
 * licensing requirements.
 * @constant {Object} nonCompliantLicense
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

export async function nonCompliantLicense() {
    const payload = {
        resource: 'user',
        fields: [
            'last_name',
            'license_type',
            'license_expiration_date',
            'license_days_remaining'
        ],
        filters: [],
        joins: [],
        sort_by: 'license_days_remaining',
        sort_order: 'asc',
        format: 'json',
        page: 1,
        page_size: 30,
    };

    return await getPredefinedReport(payload);
    
}
