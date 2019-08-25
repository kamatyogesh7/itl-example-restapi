from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Supplier(models.Model):
	sname			= models.CharField(max_length=255, unique=True)
	contact			= models.CharField(max_length=255)
	address			= models.TextField(max_length=255)

	def __str__(self):
		return self.sname

class Inventory(models.Model):
	pname			= models.CharField(max_length=255)
	quantity		= models.PositiveIntegerField()
	measurement		= models.CharField(max_length=255)
	orginal_price	= models.PositiveIntegerField()
	profit			= models.PositiveIntegerField()
	selling_price	= models.PositiveIntegerField()
	supplier 		= models.ForeignKey(Supplier, on_delete=models.CASCADE)

	def __str__(self):
		return self.pname