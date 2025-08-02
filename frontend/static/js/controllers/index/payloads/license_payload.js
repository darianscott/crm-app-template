export function license_payload() {
    return{
        resources: {
            user: {
                last_name: true
            },
            license: {
                license_type: false,
                license_number: false,
                license_expiration_date: true,
                license_days_remaining: true,
                license_is_complient: true,
                updated_at: true
            }
        }
    };
}