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
	
class ZeroDescriptor(models.Model):
	pass

class Criteria(models.Model):
	is_general = models.BooleanField()
	name = models.CharField(max_length=100)
	zero_descriptor = models.ForeignKey(ZeroDescriptor, on_delete=models.PROTECT,)

class Species(models.Model):
	#
	name = models.CharField(max_length=100)