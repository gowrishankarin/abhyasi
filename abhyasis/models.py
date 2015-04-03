import datetime 

from django.db import models
from django.utils import timezone


class Abhyasi(models.Model):
	name = models.CharField(max_length=50)
	id_card_number = models.CharField(max_length=12)
	date_of_birth = models.DateField('Date of Birth')
	date_of_join = models.DateField('Date of Join')
	address = models.CharField(max_length=200)
	def __str__(self):
		return self.name


class Sitting(models.Model):
	name = models.ForeignKey(Abhyasi)
	date_and_time = models.DateTimeField('Date and Time of Individual Sitting')
	findings = models.CharField(max_length=300)
	experiences = models.CharField(max_length=300)
	def __str__(self):
		return self.findings