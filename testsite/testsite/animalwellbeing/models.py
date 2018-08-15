from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User


# Create your models here.
class Researchers(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, default=None)
	
	def __str__(self):
		return str(self.user)

class Supervisors(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, default=None)
	def __str__(self):
		return str(self.user)

class CoverSheetForm(models.Model):
	pass
class Species(models.Model):
	#
	name = models.CharField(max_length=100)