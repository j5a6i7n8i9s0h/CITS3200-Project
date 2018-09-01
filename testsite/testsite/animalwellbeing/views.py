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
		return redirect('/awb/accounts/login') if not request.user.is_authenticated else render(request, 'animalwellbeing/welcome.html',{'user':request.user if request.user.is_superuser else Researchers.objects.get(user=request.user) })
	
def logout_view(request):
	logout(request)
	return redirect('/awb/')
	
def create_researcher(request):
	if request.method=='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['Username']
			password = form.cleaned_data['Password']
			email = form.cleaned_data['Email']
			surname = form.cleaned_data['Surname']
			firstname = form.cleaned_data['First_Name']
			user = User.objects.create_user(
				username=username,
				password=password,
				email=email
				)
			user.save() 
			new_researcher = Researchers.objects.create(
				user=user,
				surname=surname,
				firstname=firstname
				)
			new_researcher.save()
			print('Successfully created researcher')
			return redirect('/awb/')
	return render(request, 'animalwellbeing/signup.html')

@login_required
def form_creation(request):
	return render(request, 'animalwellbeing/createcoversheet.html', 
	{
		'general_criterea':{
		'1':' Activity – i.e. movement around the cageBright, Alert, Responsive (BAR)', 
		'2':'Body Posture',
		'3':'Social Behaviour (only relevant for group housed animals)', 
		}	
	})

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
				return redirect('/awb/')
		return render(request, 'animalwellbeing/login.html',{'has_attempted':True})
	return render(request, 'animalwellbeing/login.html',{'has_attempted':False})

