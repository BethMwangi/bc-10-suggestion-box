from flask import render_template, redirect, request, url_for, flash, g, json
from app import app, db
from flask_login import login_required , login_user, logout_user, current_user
from .models import User, Post, login_manager
from .forms import LoginForm, RegistrationForm, PostForm, EditProfileForm, CommentForm, VoteForm
from datetime import datetime

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
			username=form.username.data,
			password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('You can now login.')
		return redirect(url_for('index'))
	return render_template('register.html', form=form)



# @app.before_request
# def before_request():
#     g.user = current_user
#     if g.user.is_authenticated:
#         g.user.last_seen = datetime.utcnow()
#         db.session.add(g.user)
#         db.session.commit()

@app.route('/user')
@login_required
def user():
	return render_template('user.html')

@app.route('/vote', methods=['POST'])
@login_required
def vote():
	votes = request.form['votes']
	post_id = request.form['post_id']
	update = db.session.query(Post).filter_by(id=int(post_id)).update({'votes':int(votes)})
	db.session.commit()
	get_votes = db.session.query(Post).filter_by(id=int(post_id)).one()
	print(get_votes.votes)
	votes = get_votes.votes
	return json.dumps({'status':'OK','votes':votes, 'id':post_id})

@app.route('/stream')
@login_required
def stream():
	return render_template('welcome.html')

@app.route('/current_user')
@login_required
def curre_user():
	return render_template('user.html')



@app.route('/welcome')
@login_required
def welcome():
	posts = Post.query.order_by(Post.timestamp.desc()).all()
	return render_template('welcome.html', posts=posts, current_user = current_user.username)


@app.route('/edit-profile',methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.about_me = form.about_me.data
		current_user.gender = form.gender.data
		db.session.add(current_user)
		db.session.commit()
		flash('Your profle has been submitted')
		return redirect(url_for('user', username = current_user.username))
	form.username.data = current_user.username
	form.about_me.data = current_user.about_me
	form.gender.data = current_user.gender
	return render_template('edit_profile.html', about_me = current_user.about_me, form=form)
		

 
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

@app.route('/post', methods=['GET','POST'])
@login_required
def post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, 
	    	body = form.body.data,
	    	author = current_user._get_current_object())
		db.session.add(post)
		db.session.commit()
		flash('Post successfully created')
		return redirect(url_for('welcome'))
	return render_template('post.html', form = form)


@app.route('/post_comment', methods=['GET','POST'])
@login_required
def post_comment():
	post_comment= Post.query.get_or_404(id)
	form = CommentForm()
	if form.validate_on_submit():
		comment = Comment(
	    	body = form.body.data,
	    	author = current_user._get_current_object())
		db.session.add(comment)
		db.session.commit()
		return redirect(url_for('welcome', id =post.id))
	return render_template('post.html',posts=[post], form = form)



