from models.license_model import License
from models.user_model import User
from app import db
from datetime import datetime






def get_license_table():
    results = db.session.query(
        License.license_type,
        License.license_number,  # FIXED: was license_id_number
        License.expiration_date,
        License.reminder_days,  # renewal_link not in model, use reminder_days if relevant
        License.is_compliant,
        User.name.label("user_name")
    ).join(User, User.id == License.user_id).all()

    table_data = []
    for row in results:
        days_remaining = (row.expiration_date.date() - datetime.now().date()).days
        is_compliant = days_remaining > 0
        table_data.append({
            "userName": row.user_name,
            "licenseType": row.license_type,
            "licenseIdNumber": row.license_number,
            "expirationDate": row.expiration_date.strftime("%Y-%m-%d"),
            "daysRemaining": days_remaining,
            "reminderDays": row.reminder_days,
            "isCompliant": is_compliant
        })

    return table_data
