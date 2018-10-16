from django.db import models

from django.conf import settings 
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField
import datetime
import pytz

# Create your models here.
class Researchers(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, default=None)
	surname = models.CharField(max_length=30, default="user")
	firstname = models.CharField(max_length=30, default="broken")
	number_of_coversheets = models.IntegerField(default=0)
	email = models.EmailField(default="def@gmail.com")
	def __str__(self):
		return str(self.firstname)

class CoverSheetFormModel(models.Model):
	creator = models.ForeignKey(Researchers, on_delete=models.PROTECT, default=None)
	all_data = PickledObjectField(blank=True, null=True)
	created_at = models.DateTimeField(default=datetime.datetime.now(tz=pytz.timezone('Australia/Perth')))
	updated_at = models.DateTimeField(default=datetime.datetime.now(tz=pytz.timezone('Australia/Perth')))
	name = models.CharField(max_length=30, default="{}_#{}".format("coversheetform","test"))
	approved = models.BooleanField(default=False)
	request_lodged = models.BooleanField(default=False)

	def __str__(self):
		return str(self.name) 

class Message(models.Model):
	message = models.TextField(default="Ignore message")
	date = models.DateTimeField(default=datetime.datetime.now(tz=pytz.timezone('Australia/Perth')))
	coversheet = models.ForeignKey(CoverSheetFormModel, on_delete=models.PROTECT, default=None) #BAD PRACATICEEC
	author = models.CharField(max_length=30, default="admin") 


class CriteriaTemplateFormModel(models.Model):
	is_general = models.BooleanField()
	name = models.CharField(max_length=100)
	data = models.TextField(default=" @ @ @ ")
	creator = models.ForeignKey(Researchers, on_delete=models.PROTECT, default=None)
	#zero_descriptor = models.ForeignKey(ZeroDescriptor, on_delete=models.PROTECT,)

class Species(models.Model):
	#
	name = models.CharField(max_length=100)

