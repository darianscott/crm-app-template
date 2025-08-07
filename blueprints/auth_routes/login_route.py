'''
This blueprint handles user login.
'''

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from models import User

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    '''
    This route handles user login.
    '''
    if request.method == 'POST':
        # Validate credentials
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('frontend.home'))
        else:
            flash('Invalid credentials')
    return render_template('login.js')
