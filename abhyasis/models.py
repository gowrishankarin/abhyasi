import datetime 

from django.db import models
from django.utils import timezone
from datetime import datetime


class Abhyasi(models.Model):
	name = models.CharField(max_length=50)
	id_card_number = models.CharField(max_length=12)
	date_of_birth = models.DateField('Date of Birth')
	date_of_join = models.DateField('Date of Join')
	address = models.CharField(max_length=200)
	email = models.EmailField(blank=True, default='abhyasi@abhyasi.com')
	biography = models.TextField(max_length=100, default="Short Bio")
	def __str__(self):
		return self.name


class Sitting(models.Model):
	name = models.ForeignKey(Abhyasi)
	date = models.DateTimeField('Date and time of individual sitting')
	findings = models.TextField(max_length=300)
	experiences = models.TextField(max_length=300)
	def sitting_since(self):
		no_days = (timezone.now() - self.date).days
		return no_days
	def __str__(self):
		return self.findings