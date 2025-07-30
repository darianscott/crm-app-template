export function training_payload() {
    return{
        resources: {
            user: {
                last_name: true
            },
            training_hours: {
                required_hours: false,
                completed_hours: true,
                date_due: true,
                days_remaining: false,
                is_complient: true,
                updated_at: true
            }
        },
        joins: true,
        sort_by: user.last_name,
        format: 'json'
    };
}