from flask import render_template, redirect, request, url_for, flash 
from app import app, db
from flask_login import login_required , login_user, logout_user, current_user
from .models import User, Post, login_manager
from .forms import LoginForm, RegistrationForm, PostForm


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



@app.route('/user')
@login_required
def user():
	return render_template('user.html')

# @app.route('/welcome')
# @login_required
# def user():
# 	return render_template('user.html')

 
@app.route('/', methods =['GET', 'POST'])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(url_for('user'))
		flash("Invalid Username or Password")
	return render_template('index.html', form=form, current_user=current_user)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('index'))

#creating a Post route	

@app.route('/post', methods=('GET','POST'))
@login_required
def post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(form.data.title, 
			form.data.body)
		db.session.add(post)
		db.session.commit()
		flash('Post successfuly created')
		return redirect(url_for('index'))
	return render_template('post.html', form=form, post=post)


# post streams

# @app.route('/stream')
# @app.route('/stream/<username>')
# def stream():
# 	template = 'stream.html'
# 	if username and username != current_user.username:
# 		user = Post.query.filter_by(username=form.username.data).all()
# 		stream = Post.user.query.all()
# 	else:
# 		stream = 
# 	return render_template('stream.html', stream=stream)

# @app.route('/user/<username>')
# @login_required
# def user(username):
# 	user = User.query.filter_by(username=username).first()
# 	if user is None:
# 		abort(404)
# 	return render_template('user.html', user=user, posts=posts)








