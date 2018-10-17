from django.shortcuts import render, redirect
# will improve later down the line
from .forms import *
from .models import *
from django.db.models import Q
from django.urls import reverse

# user authentication
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm

# downloading files
from django.http import FileResponse
import subprocess
import json
# Create your views here.

from .additional_func import standardise_keys


def index(request):
    if request.user.is_authenticated and (
            request.user.is_superuser or Researchers.objects.filter(user=request.user).exists()):
        context = {
            'isResearcher': not request.user.is_superuser,
            'user': request.user if request.user.is_superuser else Researchers.objects.get(user=request.user),
            'templates': CoverSheetFormModel.objects.all() if request.user.is_superuser else CoverSheetFormModel.objects.filter(
                creator=Researchers.objects.get(user=request.user))
        }
    return redirect('/awb/accounts/login') if not request.user.is_authenticated else render(request,
                                                                                            'animalwellbeing/welcome.html',
                                                                                            context)


def logout_view(request):
    logout(request)
    return redirect('/awb/')


@login_required
def view_coversheet(request, coversheet_id):
    coversheetmodel = None
    try:
        # improve this later on
        coversheetmodel = CoverSheetFormModel.objects.get(pk=coversheet_id)
        return render(request, 'animalwellbeing/view_coversheet.html', coversheetmodel.all_data)
    except CoverSheetFormModel.DoesNotExist:
        return redirect('/awb/')


def password_validators(password):
    if len(password) < 6 or \
            all(char.isdigit() for char in password) or \
            all(char.isalpha() for char in password) or \
            all(char.islower() for char in password):
        return True


def create_researcher(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            email = form.cleaned_data['Email']
            surname = form.cleaned_data['Surname']
            firstname = form.cleaned_data['First_Name']
            input_question = form.cleaned_data['Question']
            input_answer = form.cleaned_data['Answer']
            a = password_validators(password)
            if a:
                data = {'first': "Your password must contain at least 6 characters",
                        'second': "Your password must contain at least 1 uppercase letter",
                        'third': "Your password must contain at least 1 number and 1 letter"}
                return render(request, 'animalwellbeing/signup.html', data)
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    is_active=False
                )
                user.save()
                new_researcher = Researchers.objects.create(
                    user=user,
                    surname=surname,
                    firstname=firstname
                )
                new_researcher.save()
                question = Question.objects.create(
                    user_Q=username,
                    Question=input_question,
                    Answer=input_answer
                )
                question.save()
                print('Successfully created researcher')
                return redirect('/awb/')
            except:
                data = {'user_exist': True, 'existed_username': username}
                return render(request, 'animalwellbeing/signup.html', data)
    return render(request, 'animalwellbeing/signup.html')


def user_activation(request):
    context = {
        'is_active': User.objects.filter(is_active=False)
    }
    return render(request, 'animalwellbeing/activation.html', context)


def activate(request, name):
    if request.user.is_superuser:
        user_need_activation = User.objects.get(username=name)
        user_need_activation.is_active = True
        user_need_activation.save()
        context = {
            'is_active': User.objects.filter(is_active=False)
        }
        return render(request, 'animalwellbeing/activation.html', context)
    else:
        return redirect('animalwellbeing/activation.html')


@login_required
def view_profile(request):
    user = request.user
    args = {'user': user}
    context = {'researchers_infor': Researchers.objects.get(user=user),
               'user': request.user if request.user.is_superuser else Researchers.objects.get(user=request.user)}
    return render(request, 'animalwellbeing/profile.html', context, args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            First_Name = form.cleaned_data['First_Name']
            Surname = form.cleaned_data['Surname']
            email = form.cleaned_data['Email']
            r = Researchers.objects.get(user=request.user)
            r.firstname = First_Name
            r.surname = Surname
            r.save()
            u = User.objects.get(username=request.user)
            u.email = email
            u.save()
            return redirect(reverse('awb:view_profile'))
    else:
        data = {'First_Name': Researchers.objects.get(user=request.user).firstname,
                'Surname': Researchers.objects.get(user=request.user).surname,
                'Email': User.objects.get(username=request.user).email}
        form = EditProfileForm(initial=data)
        args = {'form': form,
                'user': request.user if request.user.is_superuser else Researchers.objects.get(user=request.user)}
        return render(request, 'animalwellbeing/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('awb:view_profile'))

    else:
        form = PasswordChangeForm(user=request.user)

    args = {'form': form}
    return render(request, 'animalwellbeing/change_password.html', args)


def get_username(request):
    if request.method == 'POST':
        username = request.POST.get('search_name')
        exist = User.objects.filter(username=username)
        if exist and username:
            data = {'Question': Question.objects.get(user_Q=username).Question,
                    'Username': username}
            form = QuestionForm(initial=data)
            args = {'form': form}
            return render(request, 'animalwellbeing/validate_question.html', args)
        elif not exist:
            return render(request, 'animalwellbeing/get_username.html', {'attempt': True})
    return render(request, 'animalwellbeing/get_username.html')

def validate_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            answer = form.cleaned_data['Answer']
            password = form.cleaned_data['Password']
            a = password_validators(password)
            if a:
                data = {'Question': Question.objects.get(user_Q=username).Question,
                        'Username': username}
                form = QuestionForm(initial=data)
                data = {'first': "Your password must contain at least 6 characters",
                        'second': "Your password must contain at least 1 uppercase letter",
                        'third': "Your password must contain at least 1 number and 1 letter",
                        'form': form}
                return render(request, 'animalwellbeing/validate_question.html', data)

            if answer == Question.objects.get(user_Q=username).Answer:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                return redirect('/awb/accounts/login')
            else:
                data = {'Question': Question.objects.get(user_Q=username).Question,
                        'Username': username}
                form = QuestionForm(initial=data)
                args = {'form': form, 'answer_wrong': "Your answer was incorrect, please try again"}
                return render(request, 'animalwellbeing/validate_question.html', args)
    return redirect('awb:get_username')


@login_required
def edit_form(request, coversheet_id):
    coversheetmodel = None
    try:
        if request.user.is_superuser:
            coversheetmodel = CoverSheetFormModel.objects.get(pk=coversheet_id)
        else:
            coversheetmodel = CoverSheetFormModel.objects.get(pk=coversheet_id,
                                                              creator=Researchers.objects.get(user=request.user))
    except CoverSheetFormModel.DoesNotExist:
        return redirect('/awb/')

    if request.method == 'POST':
        form = CoverSheetForm(request.POST)
        dictionary_data = {
            'contact_details': {
                'Protocol Title :': '' or form['protocol_title'].value(),
                'Monitoring Start Date :': '' or form['start_date'].value(),
                'Chief Investigator :': [form['cheif_investigator'].value(), form['cheif_investigator_phone'].value()],
                'Emergency Contact :': [form['emergency_investigator'].value(),
                                        form['emergency_investigator_phone'].value()],
                'Monitor 1 :': [form['monitor_1'].value(), form['monitor_1_phone'].value()],
                'Monitor 2 :': [form['monitor_2'].value(), form['monitor_2_phone'].value()],
                'Monitor 3 :': [form['monitor_3'].value(), form['monitor_3_phone'].value()],
                'Supervisor :': form['supervision'].value(),
                'Person responsible for euthanasia :': [form['euthanasia_person'].value(),
                                                        form['euthanasia_phone'].value()],
                'Other experts :': [form['other_experts'].value(), form['other_experts_phone'].value()],
            },
            'species_phenotype_issues': {
                'Species': form['species_phenotype_issues'].value()
            },
            'monitoring_criteria': {},
            'monitoring_frequency': {},
            'type_of_recording_sheet': {},
            'actions_and_interventions': {}
        }
        coversheetmodel.name = form['protocol_title'].value() or coversheetmodel.name
        coversheetmodel.all_data = dictionary_data
        coversheetmodel.save()
        return redirect('/awb/')
    else:
        if coversheetmodel.approved:
            return redirect('/awb/')
        else:
            return render(request, 'animalwellbeing/createcoversheet.html',
                          {'dictionary_data': standardise_keys(coversheetmodel.all_data)})


@login_required
def form_creation(request):
    if request.method == 'POST':
        form = CoverSheetForm(request.POST)
        # print(form)
        # if form.is_valid():
        # 	print("GOT EHRE")
        print(form.data)
        print(form['protocol_title'].value())
        dictionary_data = {
            'contact_details': {
                'Protocol Title :': '' or form['protocol_title'].value(),
                'Monitoring Start Date :': '' or form['start_date'].value(),
                'Chief Investigator :': [form['cheif_investigator'].value(), form['cheif_investigator_phone'].value()],
                'Emergency Contact :': [form['emergency_investigator'].value(),
                                        form['emergency_investigator_phone'].value()],
                'Monitor 1 :': [form['monitor_1'].value(), form['monitor_1_phone'].value()],
                'Monitor 2 :': [form['monitor_2'].value(), form['monitor_2_phone'].value()],
                'Monitor 3 :': [form['monitor_3'].value(), form['monitor_3_phone'].value()],
                'Supervisor :': form['supervision'].value(),
                'Person responsible for euthanasia :': [form['euthanasia_person'].value(),
                                                        form['euthanasia_phone'].value()],
                'Other experts :': [form['other_experts'].value(), form['other_experts_phone'].value()],
            },
            'species_phenotype_issues': {
                'Species': form['species_phenotype_issues'].value()
            },
            'monitoring_criteria': {},
            'monitoring_frequency': {},
            'type_of_recording_sheet': {},
            'actions_and_interventions': {}
        }
        creator_ = Researchers.objects.get(user=request.user)
        csfm = CoverSheetFormModel.objects.create(
            creator=creator_,
            all_data=dictionary_data,
            created_at=datetime.datetime.now(),
            name=form['protocol_title'].value() or "{}_{}_form#{}".format(creator_.firstname, creator_.surname,
                                                                          creator_.number_of_coversheets)
        )
        creator_.number_of_coversheets += 1
        creator_.save()
        csfm.save()
        return redirect('/awb/')
    return render(request, 'animalwellbeing/createcoversheet.html')


@login_required
def download_cs(request, coversheet_id):
    coversheetmodel = None
    try:
        if request.user.is_superuser:
            coversheetmodel = CoverSheetFormModel.objects.get(pk=coversheet_id)
        else:
            coversheetmodel = CoverSheetFormModel.objects.get(pk=coversheet_id,
                                                              creator=Researchers.objects.get(user=request.user))
        script = ["python2.7", "animalwellbeing/handlers.py", json.dumps(coversheetmodel.all_data),
                  coversheetmodel.name]
        process = subprocess.Popen(script, stdout=subprocess.PIPE)
        output, error = process.communicate()
        response = FileResponse(
            open('animalwellbeing/static/animalwellbeing/coversheets/{}.docx'.format(coversheetmodel.name), 'rb'),
            as_attachment=True)
        return response
    except CoverSheetFormModel.DoesNotExist:
        return redirect('/awb/')


def login_view(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        try:
            if form.is_valid() and not User.objects.get(username=form.cleaned_data['Username']).is_active:
                return render(request, 'animalwellbeing/login.html', {'activation': True})
            elif form.is_valid():
                username = form.cleaned_data['Username']
                password = form.cleaned_data['Password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('/awb/')
        except:
            return render(request, 'animalwellbeing/login.html', {'has_attempted': True})
    return render(request, 'animalwellbeing/login.html', {'has_attempted': False})


def search(request):
    template = 'animalwellbeing/welcome.html'
    author = request.GET['author']
    projectName = request.GET['projectName']
    date = request.GET['date']
    if author and projectName and date:
        try:
            match = CoverSheetFormModel.objects.filter(
                Q(created_at=date) &
                Q(creator=Researchers.objects.get(firstname__icontains=author)) &
                Q(name__icontains=projectName))
            if match:
                return render(request, template, {'results': match})
            else:
                return render(request, template, {'Message': "Cant find the matching Query"})
        except:
            return render(request, template, {'Message': "Cant find the matching Query"})
    elif author and projectName:
        try:
            match = CoverSheetFormModel.objects.filter(
                Q(creator=Researchers.objects.get(firstname__icontains=author)) &
                Q(name__icontains=projectName))
            if match:
                return render(request, template, {'results': match})
            else:
                return render(request, template, {'Message': "Cant find the matching Query"})
        except:
            return render(request, template, {'Message': "Cant find the matching Query"})
    elif author and date:
        try:
            match = CoverSheetFormModel.objects.filter(Q(created_at=date) &
                                                       Q(creator=Researchers.objects.get(firstname__icontains=author)))
            if match:
                return render(request, template, {'results': match})
            else:
                return render(request, template, {'Message': "Cant find the matching Query"})
        except:
            return render(request, template, {'Message': "Cant find the matching Query"})
    elif projectName and date:
        try:
            match = CoverSheetFormModel.objects.filter(
                Q(created_at=date) &
                Q(name__icontains=projectName))
            if match:
                return render(request, template, {'results': match})
            else:
                return render(request, template, {'Message': "Cant find the matching Query"})
        except:
            context = {'results': CoverSheetFormModel.objects.all()}
            return render(request, template, context)
    elif author:
        try:
            context = {'results': CoverSheetFormModel.objects.filter(
                creator=Researchers.objects.get(firstname__icontains=author))}
            return render(request, template, context)
        except:
            if author is "":
                context = {'results': CoverSheetFormModel.objects.all()}
                return render(request, template, context)
            else:
                return render(request, template, {'Message': "Cant find the matching Query"})
    elif projectName:
        match = CoverSheetFormModel.objects.filter(name__icontains=projectName)
        if match:
            return render(request, template, {'results': match})
        else:
            return render(request, template, {'Message': "Cant find the matching Query"})
    elif date:
        try:
            match = CoverSheetFormModel.objects.filter(created_at=date)
            if match:
                return render(request, template, {'results': match})
            else:
                return render(request, template, {'Message': "Cant find the matching Query"})
        except:
            context = {'results': CoverSheetFormModel.objects.all()}
            return render(request, template, context)
    else:
        context = {'results': CoverSheetFormModel.objects.all()}
        return render(request, template, context)
