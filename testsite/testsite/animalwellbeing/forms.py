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

class ReviewForm(forms.Form):
	comment = forms.CharField(max_length=300,widget=forms.Textarea)

class CoverSheetForm(forms.Form):
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
	scrit = forms.CharField()
	pcrit = forms.CharField()
	
	#monitory frequency
	monitoring_frequency = forms.CharField(max_length=200,widget=forms.Textarea)
	#type of recording sheet
	general = forms.BooleanField()	
	anasthesia = forms.BooleanField()
	post_proc = forms.BooleanField()
	other = forms.BooleanField()
	other_description = forms.CharField()

class CriteriaTemplateForm(forms.Form):
	name = forms.CharField()
	scrit = forms.CharField()