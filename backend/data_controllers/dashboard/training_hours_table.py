from models.training_hours_model import TrainingHours
from models.user_model import User
from app import db
from datetime import datetime

def get_training_hours_table():
    results = db.session.query(
        TrainingHours.required_hours,
        TrainingHours.competed_hours,
        TrainingHours.courses,
        TrainingHours.date_due,
        TrainingHours.progress,
        User.name.label("user_name")
    ).join(User, User.id == TrainingHours.user_id).all()
    
    table_data = []
    for row in results:
        days_remaining = (row.expiration_date - datetime.utznow().date()).days
        is_compliant = days_remaining > 0  # or whatever your logic is
        table_data.append({
            "userName": row.user_name,
            "requiredHours": row.required_hours,
            "completedHours": row.completed_hours,
            "courses": row.courses,
            "dateDue": row.date_due,
            "progress": row.progress,
            "daysRemaining": row.days_remaining,
            "isCompliant": row.is_compliant
        })
    return table_data 
