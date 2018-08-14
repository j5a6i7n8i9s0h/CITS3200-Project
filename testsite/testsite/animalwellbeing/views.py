from django.shortcuts import render, redirect
# will improve later down the line
from .forms import * 
from .models import * 

#user authentication
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

# Create your views here.

def index(request):
		return redirect('/awb/accounts/index') if not request.user.is_authenticated else render(request, 'animalwellbeing/index.html',{'user':request.user})
	

def login_view(request):
	context = {}
	if request.method=='POST':
		form = LoginForm(request.POST)
		if form.is_valid(): 
			username = form.cleaned_data['Username']
			password = form.cleaned_data['Password']
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
				return index(request)
				#success 
	return render(request, 'animalwellbeing/login.html')



def profile(request, user):

	return render(request,'animalwellbeing/index.html')
