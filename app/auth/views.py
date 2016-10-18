from flask import render_template, redirect, request, url_for, flash 
from . import auth
from flask.ext.login import login_required , login_user
from ..models import User
from .forms import LoginForm




@app.route('/secret')
@login_required
def secret():
	return 'Only authenticated users are allowed!'

@auth.route('/login')
def login():
	return render_template('auth/login.html')


@app.route('/login', methods =['GET', 'POST'])
def login():
	# error = None
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('index'))
		flash('Invalid username or password.')
	return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('main.index'))

