from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(UserMixin, db.Model):
	"""docstring for User"""
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(120))
	password_hash = db.Column(db.String(128))
	joined_at=db.Column(db.DateTime, default=datetime.datetime.now)
	is_admin=db.Column(db.Boolean, default=False)
	posts = db.relationship('Post', backref='author', lazy='dynamic')
		

	def __repr__(self):
		return '<User %r' %(self.username)

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)


class Post(db.Model):
	__tablename__ = "posts"
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(64))
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id  = db.Column(db.Integer, db.ForeignKey('users.id'))
	# user = db.ForeignKey(User)

	def __repr__(self):
		return '<Post %r>' % (self.body)
