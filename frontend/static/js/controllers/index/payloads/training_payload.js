export function training_payload() {
    return{
            user: {
                last_name,
                training_required_hours,
                training_completed_hours,
                training_date_due,
                training_days_remaining,
                training_is_complient
            },
        joins: '',
        sort_by: '',
        format: 'json'
    };
}