from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name=models.CharField(max_length=50)
	description=models.TextField()
	openening_time=models.DateTimeField()
	closing_time=models.DateTimeField()
	def __str__(self):
		return self.name