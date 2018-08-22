from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
from django.contrib import messages


# login pages displays login_registration.html 
def index(request):
	return(render(request, 'wall/login_registration.html'))

# adds a new user to the model from the login page
def register(request):
	if request.method == 'POST':
		errors = User.objects.register_validation(request.POST)
		if len(errors) == 0:
			# hashpw= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
			user = User.objects.create_user(request.POST)
			request.session['id'] = user.id
			return redirect('/welcome')
		for error in errors:
			messages.error(request, error)
		return redirect('/')

# validates the person logging in as someone who already registered
def validate(request):
	errors = User.objects.login_validation(request.POST)
	print(errors, '//////')
	if len(errors) == 0:
		user = User.objects.filter(email=request.POST['email'])
		request.session['id'] = user[0].id
		return redirect('/welcome')
	for error in errors:
		messages.error(request, error)
	return redirect('/')


# welcome page/ main wall page
def welcome(request):
	context = {
		'user': User.objects.get(id=request.session['id']),
		'wall_messages': Wall_message.objects.all(),
		'comments': Comment.objects.all()
	}
	return(render(request, 'wall/index.html', context))

# takes message and inserts into the model
def message(request):
	if request.method == 'POST':
		errors = Wall_message.objects.wall_validation(request.POST)
		if len(errors) == 0:
			wall_message = Wall_message.objects.create(message=request.POST['message'], user_id=request.session['id'])
			return redirect('/welcome')
		for error in errors:
			messages.error(request, error)
		return redirect('/welcome')

# inserts comments into the messages
def comment(request, id):
	if request.method == 'POST':
		errors = Comment.objects.comment_validation(request.POST)
		if len(errors) == 0:
			comment = Comment.objects.create(comment=request.POST['comment'], user_id=request.session['id'], wall_message_id=int(id))
		for error in errors:
			messages.error(request, error)
	return redirect('/welcome')

def logout(request):
	if 'id' in request.session:
		request.session.pop('id')
	return redirect('/')

