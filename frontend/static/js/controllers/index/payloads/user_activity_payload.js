export function user_activity_payload() {
    return{
        resources: {
            user: {
                last_name: true,
                invites_sent: false,
                invites_archived: false,
                outstanding_invites: false,
                new_clients: false,
                active_clients: false,
                archived_clients: false,
                testimonials_recieved: false,
                testimonail_rating: false,
                updated_at: true
            }
        },
        joins: true,
        sort_by: user.last_name,
        format: 'json'
    };
}