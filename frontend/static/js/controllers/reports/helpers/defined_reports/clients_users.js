
import { getPredefinedReport } from '/helpers/getPredefinedReport.js'

export async function clientsUsers() {
    
    const payload = {
        resource: 'clients',
        fields: [
            'first_name',
            'last_name',
            'street_address',
            'zip_code',
            'phone_number'
        ],
        filters: [],
        joins: ['user'],
        sort_by: 'user.last_name',
        sort_order: 'asc',
        format: 'csv',
        page: 1,
        page_size: 30

    };

    return await getPredefinedReport(payload);

}