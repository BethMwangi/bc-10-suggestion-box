from flask import render_template, redirect, request, url_for, flash 
from app import app, db
from flask_login import login_required , login_user, logout_user, current_user
from .models import User, login_manager
from .forms import LoginForm, RegistrationForm


@app.route('/secret')
@login_required
def secret():
	return 'Only authenticated users are allowed!'

@app.route('/')
def index():
	return "hello"


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


# import ipdb; ipdb.set_trace()

@app.route('/login', methods =['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			flash("You've been looged in.Success!")
			return redirect(url_for('index'))
		flash('Invalid username or password.')
	return render_template('login.html', form=form, current_user=current_user)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('welcome'))