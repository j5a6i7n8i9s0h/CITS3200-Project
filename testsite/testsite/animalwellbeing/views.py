from django.shortcuts import render
from .forms import *

#user authentication
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

# Create your views here.

def index(request):
	context = {}
	if request.method=='POST':
		form = LoginForm(request.POST)
		#if form.is_valid(): 
		username = form['Username']
		password = form['Password']

	return render(request,'animalwellbeing/index.html')
