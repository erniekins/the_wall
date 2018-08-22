from __future__ import unicode_literals
from django.db import models
import re, bcrypt

# Create your models here.
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
class UserManager(models.Manager):
	def register_validation(self, input):
		error = []
		if (len(input["first_name"])<3):
			error.append('First name should be more than two characers')
		if (len(input["last_name"])<3):
			error.append('Last name should be more than two characers')
		if not EMAIL_REGEX.match(input['email']):
			error.append('Email should have the proper format')
		if (len(input['password'])<3):
			error.append('Password should be longer than two characters')
		if input['password'] != input['password_confirm']:
			error.append('Passwords must match')
		print('*****', error)
		return error

	def login_validation(self, input):
		error = []
		user = User.objects.filter(email=input['email'])
		if len(user) == 0:
			error.append('Email does not exist')
			return error
		if bcrypt.checkpw(input['password'].encode(), user[0].password.encode()):
			print("passwords match!")
		else:
			error.append("Not a valid password")
		return error

	def create_user(self, input):
		hashpw= bcrypt.hashpw(input['password'].encode(), bcrypt.gensalt())
		user = self.create(
				first_name = input['first_name'],
				last_name = input['last_name'],
				email = input['email'],
				password = hashpw
			)
		return user


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Wall_messageManager(models.Manager):
	def wall_validation(self, input):
		error = []
		if len(input['message'])<2:
			error.append('Message must be more than one character')
		return error

class Wall_message(models.Model):
	message = models.CharField(max_length=255)
	user = models.ForeignKey(User, related_name='wall_messages')
	# created_at = models.DateTimeField(auto_now_add=True)
	# updated_at = models.DateTimeField(auto_now=True)
	objects = Wall_messageManager()

class CommentManager(models.Manager):
	def comment_validation(self, input):
		error = []
		if len(input['comment'])<2:
			error.append('Comments must be more than one character')
		return error

class Comment(models.Model):
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, related_name='comments')
	wall_message = models.ForeignKey(Wall_message, related_name='comments')
	objects = CommentManager()


