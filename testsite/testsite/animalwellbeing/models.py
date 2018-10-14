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


class Criteria(models.Model):
	species = models.ForeignKey("Species", default=1, on_delete=models.CASCADE)
	name = models.CharField("Criteria Name", max_length=100)
	zero_descriptor = models.TextField("Score 0", default="" , max_length=1000)
	one_descriptor = models.TextField("Score 1", default="", max_length=1000)
	two_descriptor = models.TextField("Score 2", default="", max_length=1000)
	is_general = models.BooleanField(default=True)
	created_at = models.DateTimeField(default=datetime.datetime.now(tz=pytz.timezone('Australia/Perth')))
	#zero_descriptor = models.ForeignKey(ZeroDescriptor, on_delete=models.PROTECT,)
	class Meta:
		verbose_name_plural = "criteria"
	def __str__(self):
		return self.name

class Species(models.Model):
	name = models.CharField("Species", max_length=100, unique=True, default="species") 
	class Meta:
		verbose_name_plural = "species"
	def __str__(self):
		return self.name

