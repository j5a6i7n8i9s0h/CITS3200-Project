from django import forms


class LoginForm(forms.Form):
    Username = forms.CharField(max_length=30)
    Password = forms.CharField(max_length=30)


class SignUpForm(forms.Form):
    Username = forms.CharField(max_length=30)
    Password = forms.CharField(max_length=30)
    First_Name = forms.CharField(max_length=30)
    Surname = forms.CharField(max_length=30)
    Email = forms.EmailField(max_length=100)
    Question = forms.CharField(max_length=150)
    Answer = forms.CharField(max_length=50)


class ReviewForm(forms.Form):
	comment = forms.CharField(max_length=300,widget=forms.Textarea)

class CoverSheetForm(forms.Form):
    protocol_title = forms.CharField(max_length=200, strip=False)
    start_date = forms.DateField()
    cheif_investigator = forms.CharField(max_length=30)
    cheif_investigator_phone = forms.CharField(max_length=10)
    emergency_investigator = forms.CharField(max_length=30)
    emergency_investigator_phone = forms.CharField(max_length=10)
    monitor_1 = forms.CharField(max_length=30)
    monitor_1_phone = forms.CharField(max_length=10)
    monitor_2 = forms.CharField(max_length=30)
    monitor_2_phone = forms.CharField(max_length=10)
    monitor_3 = forms.CharField(max_length=30)
    monitor_3_phone = forms.CharField(max_length=10)
    supervision = forms.BooleanField()
    euthanasia_person = forms.CharField(max_length=30)
    euthanasia_phone = forms.CharField(max_length=10)
    other_experts = forms.CharField(max_length=30)
    other_experts_phone = forms.CharField(max_length=10)
    # species/phenotype/issues
    species_phenotype_issues = forms.CharField(max_length=30)
    # MONITORING CRITERIA AND SCORING
    scrit = forms.CharField()
    pcrit = forms.CharField()

    # monitory frequency
    monitoring_frequency = forms.CharField(max_length=200)
    # type of recording sheet
    typeofsheet = forms.ChoiceField()
    other_description = forms.CharField()
    protocol_title = forms.CharField(max_length=200, strip=False)
    start_date = forms.DateTimeField()
    cheif_investigator = forms.CharField(max_length=30)
    cheif_investigator_phone = forms.CharField(max_length=10)
    emergency_investigator = forms.CharField(max_length=30)
    emergency_investigator_phone = forms.CharField(max_length=10)
    monitor_1 = forms.CharField(max_length=30)
    monitor_1_phone = forms.CharField(max_length=10)
    monitor_2 = forms.CharField(max_length=30)
    monitor_2_phone = forms.CharField(max_length=10)
    monitor_3 = forms.CharField(max_length=30)
    monitor_3_phone = forms.CharField(max_length=10)
    supervision = forms.BooleanField()
    euthanasia_person = forms.CharField(max_length=30)
    euthanasia_phone = forms.CharField(max_length=10)
    other_experts = forms.CharField(max_length=30)
    other_experts_phone = forms.CharField(max_length=10)
    #species/phenotype/issues
    species_phenotype_issues = forms.CharField(max_length=30)
    #MONITORING CRITERIA AND SCORING
    actions1a = forms.CharField()
    actions1b = forms.CharField()
    actions2a = forms.CharField()
    actions2b = forms.CharField()
    actions3a = forms.CharField()#test
    actions3b = forms.CharField()
    actions4a = forms.CharField()
    actions4b = forms.CharField()
    additional = forms.CharField()
    #AEC interventions
    aec1 = forms.CharField()
    aec2 = forms.CharField()
    aec3 = forms.CharField()
    aec4 = forms.CharField()
    aec5 = forms.CharField()
    aec6 = forms.CharField()
    aec7 = forms.CharField()
    aec8 = forms.CharField()
    #monitory frequency
    monitoring_frequency = forms.CharField(max_length=200,widget=forms.Textarea)
    #type of recording sheet
    general = forms.BooleanField()	
    anasthesia = forms.BooleanField()
    post_proc = forms.BooleanField()
    other = forms.BooleanField()
    other_description = forms.CharField()


class EditProfileForm(forms.Form):
    First_Name = forms.CharField(max_length=30)
    Surname = forms.CharField(max_length=30)
    Email = forms.EmailField(max_length=100)


class QuestionForm(forms.Form):
    Username = forms.CharField(max_length=30,  widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    Question = forms.CharField(max_length=150,  widget=forms.TextInput(attrs={'readonly': 'readonly', 'size': 80}))
    Answer = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=30)

class CriteriaTemplateForm(forms.Form):
    name = forms.CharField()
    scrit = forms.CharField()
