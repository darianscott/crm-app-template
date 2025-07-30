export function license_payload() {
    return{
        resources: {
            user: {
                last_name: true
            },
            license: {
                license_type: false,
                license_number: false,
                expiration_date: true,
                days_remaining: true,
                is_complient: true,
                updated_at: true
            }
        },
        joins: true,
        sort_by: user.last_name,
        format: 'json'
    };
}