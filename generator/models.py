from django.db import models

# Create your models here.
class Trait(models.Model):
	name=models.CharField(max_length=30)
	description=models.CharField(max_length=300)

	def __str__(self):
		return self.name



class Name(models.Model):

	name=models.CharField(max_length=100)
	species=models.CharField(max_length=100)


	def __str__(self):

		return self.name




class Job(models.Model):

	name=models.CharField(max_length=100)
	base_salary=models.IntegerField()



	def __str__(self):

		return self.name