'''
This route is for logging users in and out of the app.
When a user tried to view a protected view (anything with
@ogin_required at the top) if they are not logged in 
it will promp them to login. It also allows the use of 
current user to get the user id.
'''

# routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import User
from extensions import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    '''
    this is the logic for logging the user in
    '''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Replace with hashing
            login_user(user)
            return redirect(url_for('dashboard'))  # Where to go after login
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    '''
    this is the logic for logging the user out
    '''
    logout_user()
    return redirect(url_for('auth.login'))
