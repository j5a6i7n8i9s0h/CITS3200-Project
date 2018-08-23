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
