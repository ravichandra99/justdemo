from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class UserType(models.Model):
	usertype = models.CharField(max_length = 50)

	def __str__(self):
		return self.usertype

class Company(models.Model):
	company = models.CharField(max_length = 50)

	def __str__(self):
		return self.company

	class Meta:
		verbose_name = 'Company'
		verbose_name_plural = 'Companies'

class State(models.Model):
	state = models.CharField(max_length = 50)

	def __str__(self):
		return self.state

class Place(models.Model):
	state = models.ForeignKey(State,on_delete = models.CASCADE)
	place = models.CharField(max_length = 50)

	def __str__(self):
		return self.place

class UserMaster(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	full_name = models.CharField(max_length = 100)
	usertype = models.ForeignKey(UserType,on_delete = models.CASCADE)
	company = models.ForeignKey(Company,on_delete = models.CASCADE)
	#state = models.ForeignKey(State,on_delete = models.CASCADE)
	place = models.ForeignKey(Place,on_delete = models.CASCADE)
	address = models.TextField()
	email = models.EmailField()
	phone = PhoneNumberField()

	def __str__(self):
		return self.full_name

class UserInfo(models.Model):
	user = models.ForeignKey(UserMaster,on_delete = models.CASCADE)
	invoice = models.FileField(upload_to = '')
	total = models.IntegerField()
	sold = models.IntegerField(null = True,blank = True)
	remaining = models.IntegerField(null = True,blank = True)

	def __str__(self):
		return str(self.user)




