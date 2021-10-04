from flask import Blueprint, render_template, redirect, request, flash, url_for
from app.forms import signInForm, signUpForm, updateUser
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

from app.models import db, User

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form= signUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(form.username.data, form.email.data, form.password.data, form.first_name.data, form.last_name.data)

            try:
                db.session.add(new_user)
                db.session.commit()
            except:
                flash('Someone beat you to it. Username or email already exists, please try again.', category='alert-danger')
                return redirect(url_for('auth.signup'))

            flash(f'You have successfully signed up with the username {form.username.data}. You are now signed in.', category='alert-success')
            login_user(new_user)
            return redirect(url_for('home'))
        else:
            flash('Nop, invalid input, please try again.', category='alert-danger')
            return redirect(url_for('auth.signup'))
    return render_template('signup.html', form=form)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = signInForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            usernamedata = form.username.data
            passworddata = form.password.data

            user = User.query.filter_by(username=usernamedata).first()
            if user is None or not check_password_hash(user.password, passworddata):
                flash('Incorrect username or password. Please try again.', category='alert-danger')
                return redirect(url_for('auth.signin'))

            login_user(user)
            flash(f'You are now logged in! Welcome { usernamedata}.', category='alert-success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password. Please try again.', category='alert-danger')
            return redirect(url_for('auth.signin'))
    return render_template('signin.html', form=form)

@auth.route('/signout')
def signout():
    logout_user()
    flash('You are now signed out.', category='alert-info')
    return redirect(url_for('auth.signin'))

@auth.route('/profile')
@login_required
def profile():
    context = current_user.to_dict()
    print(context)
    return render_template('profile.html', **context)
    
@auth.route('/updateuser', methods=['GET', 'POST'])
@login_required
def updateuser():
    form = updateUser
    if request.method == 'POST':
        if form.validate_on_submit() and check_password_hash(current_user.password, form.oldpassword.data):
            if form.newpassword.data and form.newusername.data:
                current_user.password = generate_password_hash(form.newpassword.data)
                current_user.username = form.newusername.data
                db.session.commit()

            elif form.newusername.data:
                current_user.username =  form.newusername.data
                db.session.commit()
            elif form.newpassword.data:
                current_user.password = generate_password_hash(form.newpassword.data)
                db.session.commit()
            flash('User information updated!', category='alert-info')
            return redirect(url_for('auth.profile' ))
        else:
            flash('Nop, invalid input. Please try again.', category='alert-danger')
            return redirect(url_for('auth.profile'))

    return render_template('updateuser.html', form=form)