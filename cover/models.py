from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	cellphone = models.IntegerField(default=0)
	phone = models.IntegerField(default=0)
	address = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)
	profession = models.CharField(max_length = 100)








	