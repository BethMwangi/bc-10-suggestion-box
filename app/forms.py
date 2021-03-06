from flask.ext.wtf import Form 
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, SubmitField, ValidationError 
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from .models import User
from flask.ext.pagedown.fields import PageDownField

class LoginForm(Form):
	email = StringField('Email', validators=[Required(),
		Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('')
	submit = SubmitField('Log In')

class RegistrationForm(Form):
	email = StringField('Email', validators=[Required(), Length(1,64),
		Email()])
	username = StringField('Username', validators=[Required(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
		'Usernames must have only letters, '
		'numbers, dots or underscores')])
	password = PasswordField('Password', validators=[
		Required(), EqualTo('password2', message='Passwords must match')])
	password2 = PasswordField('Confirm password', validators=[Required()])
	submit = SubmitField('Register')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered')


	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already registered')


class EditProfileForm(Form):
	username = StringField('Real name', validators=[Length(0, 64)])
	gender = StringField('Gender', validators=[Length(0, 64)])
	about_me = TextAreaField('About me')
	submit = SubmitField('Submit')

class PostForm(Form):
	title = StringField('Title', validators=[Required()])
	body = PageDownField('Suggestion', validators=[Required()])
	submit = SubmitField('Submit')

class VoteForm(Form):
	post_id = StringField('post_id')
	votes = StringField('votes')

class CommentForm(Form):
	body = StringField('comment', validators=[Required()])
	submit = SubmitField('Submit')























