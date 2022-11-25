from django.db import models
from django.urls import reverse
#Django by defaults handles authentication
from django.contrib.auth.models import User

# Create your models here.
#basically we define tables here


# we are here creating tables with one to amny relationship as one user will have multiple entry
class Task(models.Model):
	user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	
	title = models.CharField(max_length=200)
	
	description = models.TextField(null=True, blank=True) 
	
	complete =models.BooleanField(default=False)
	
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return (self.title)
	
class Meta:
	ordering = ['complete']	
