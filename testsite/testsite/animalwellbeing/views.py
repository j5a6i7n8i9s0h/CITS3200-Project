from django.shortcuts import render, redirect
# will improve later down the line
from .forms import *
from .models import *


#user authentication
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

#downloading files
from django.http import FileResponse
# Create your views here.

def index(request):
	if request.user.is_authenticated and (request.user.is_superuser or Researchers.objects.filter(user=request.user).exists()):
		context = {
			'isResearcher': not request.user.is_superuser,
			'user':request.user if request.user.is_superuser else Researchers.objects.get(user=request.user),
			'templates':  CoverSheetFormModel.objects.all() if request.user.is_superuser else CoverSheetFormModel.objects.filter(creator=Researchers.objects.get(user=request.user))
			}
	return redirect('/awb/accounts/login') if not request.user.is_authenticated else render(request, 'animalwellbeing/welcome.html', context)

def logout_view(request):
	logout(request)
	return redirect('/awb/')

@login_required
def view_coversheet(request, coversheet_id):
	coversheetmodel = None
	try:
		coversheetmodel = CoverSheetFormModel.objects.get(pk=coversheet_id)
		return render(request, 'animalwellbeing/view_coversheet.html', coversheetmodel.all_data)
	except CoverSheetFormModel.DoesNotExist:
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
	if request.method == 'POST':
		form = CoverSheetForm(request.POST)
		# print(form)
		# if form.is_valid():
		# 	print("GOT EHRE")
		print(form.data)
		print(form['protocol_title'].value())
		dictionary_data={
			'contact_details':{
				'Protocol Title :' : '' or form['protocol_title'].value(),
				'Monitoring Start Date :':'' or form['start_date'].value(),
				'Chief Investigator :' :[form['cheif_investigator'].value(), form['cheif_investigator_phone'].value()],
				'Emergency Contact :': [form['emergency_investigator'].value(), form['emergency_investigator_phone'].value()],
				'Monitor 1 :': [form['monitor_1'].value(), form['monitor_1_phone'].value()],
				'Monitor 2 :': [form['monitor_2'].value(), form['monitor_2_phone'].value()],
				'Monitor 3 :': [form['monitor_3'].value(), form['monitor_3_phone'].value()],
				'Supervisor :': form['supervision'].value(),
				'Person responsible for euthanasia :': [form['euthanasia_person'].value(), form['euthanasia_phone'].value()],
				'Other experts :': [form['other_experts'].value(), form['other_experts_phone'].value()],
			},
			'species_phenotype_issues':{
				'Species' : form['species_phenotype_issues'].value()
			},
			'monitoring_criteria':{},
			'monitoring_frequency':{},
			'type_of_recording_sheet':{},
			'actions_and_interventions':{}
		}
		creator_ = Researchers.objects.get(user=request.user)
		csfm = CoverSheetFormModel.objects.create(
			creator = creator_,
			all_data = dictionary_data,
			created_at = datetime.datetime.now(),
			name = "{}_{}_form#{}".format(creator_.firstname, creator_.surname , creator_.number_of_coversheets)
		)
		creator_.number_of_coversheets+=1
		creator_.save()
		csfm.save()
		return redirect('/awb/')
	return render(request, 'animalwellbeing/createcoversheet.html')

import subprocess
import json
@login_required
def download_cs(request, coversheet_id):
	coversheetmodel = None
	try:
		if request.user.is_superuser:
			coversheetmodel = CoverSheetFormModel.objects.get(pk=coversheet_id)
		else:
			coversheetmodel = CoverSheetFormModel.objects.get(pk=coversheet_id, creator=Researchers.objects.get(user=request.user))
		script = ["python2.7", "animalwellbeing/handlers.py", json.dumps(coversheetmodel.all_data), coversheetmodel.name] 
		process = subprocess.Popen(script, stdout=subprocess.PIPE)
		output,error = process.communicate()
		response = FileResponse(open('animalwellbeing/static/animalwellbeing/coversheets/{}.docx'.format(coversheetmodel.name), 'rb'), as_attachment=True)
		return response
	except CoverSheetFormModel.DoesNotExist:
		return redirect('/awb/')

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


def search(request):
    template = 'animalwellbeing/welcome.html'
    if request.method == 'GET':
        query = request.GET.get('q')
        try:
            context = {'results':  CoverSheetFormModel.objects.filter(creator=Researchers.objects.get(firstname__icontains=query))}
            return render(request, template, context)
        except:
            return render(request, template)
    else:
        return render(request, template)