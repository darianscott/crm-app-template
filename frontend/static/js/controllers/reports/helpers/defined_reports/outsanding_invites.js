/**
 * Object representing the configuration for fetching outstanding invites and testimonials for users.
 *
 * @constant {Object} outstandingInvitesVsTestimonials
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

export async function outstandingInvitesVsTestimonials() {
    const payload = {
        resource: 'user',
        fields: [ 
            'last_name',
            'invites_sent', 
            'outstanding_invites',
            'testimonials_received',
            'testimonial_rating'
        ],
        filters: [],
        joins: [],
        sort_by: 'last_name',
        sort_order: 'asc',
        format: 'csv',
        page: 1,
        page_size: 30
    };

     return await getPredefinedReport(payload);
    
};