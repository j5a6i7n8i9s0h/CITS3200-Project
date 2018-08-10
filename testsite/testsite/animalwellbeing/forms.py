from django import forms 

class LoginForm(forms.Form): 
	Username = forms.CharField(max_length=30) 
	Password = forms.CharField(max_length=30)
	