from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField
import datetime

# Create your models here.
class Researchers(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, default=None)
	surname = models.CharField(max_length=30, default="user")
	firstname = models.CharField(max_length=30, default="broken")
	number_of_coversheets = models.IntegerField(default=0)
	def __str__(self):
		return str(self.user)

class CoverSheetFormModel(models.Model):
	creator = models.ForeignKey(Researchers, on_delete=models.PROTECT, default=None)
	all_data = PickledObjectField(blank=True, null=True)
	created_at = models.DateField(default=datetime.datetime.now())
	name = models.CharField(max_length=30, default="{}_#{}".format("coversheetform","test"))
	approved = models.BooleanField(default=False)

	'''dictionary ={
		'contact details' : {Protocol Title :' : 'ironman',
			'Monitoring Start Date :' : 'today' , 
			'Chief Investigator :' : ['kanye_west' , '123123'],
			'Emergency Contact :' : ['thor', ' 123123141342'],
			'Monitor 1 :' : ['captainamerica', ' 123123141342'],
			'Monitor 2 :' : ['lilpump', ' 123123141342'],
			'Monitor 3 :' : ['thanos ', ' 12342'],
			'Person responsible for euthanasia :' : ['h3h3', ' 12'],
			'Other experts :' : ['voldemort', ' 2'],
			},
	} '''

class Criteria(models.Model):
	is_general = models.BooleanField()
	name = models.CharField(max_length=100)
	#zero_descriptor = models.ForeignKey(ZeroDescriptor, on_delete=models.PROTECT,)

class Species(models.Model):
	#
	name = models.CharField(max_length=100)