from flask import render_template, redirect, request, url_for, flash 
from app import app, db
from flask.ext.login import login_required , login_user, logout_user, current_user
from .models import User, login_manager
from .forms import LoginForm, RegistrationForm

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



# @auth.route('/secret')
# @login_required
# def secret():
# 	return 'Only authenticated users are allowed!'


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
			username=form.username.data,
			password=form.password.data)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		flash('You can now login.')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)


@app.route('/', methods =['GET', 'POST'])
def index():
	# error = None
	form = LoginForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User.query.filter_by(email=request.form['email']).first()
			if user is not None and user.verify_password(form.password.data):
				login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('welcome'))
		flash('Invalid username or password.')
	return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('welcome'))





