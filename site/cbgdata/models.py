from django.db import models

# Create your models here.

class Snippets(models.Model):
	uid = models.CharField(max_length=30,primary_key=True)
	price = models.IntegerField(default=0)
	url = models.URLField(max_length=250)



	def __str__(self):
		return self.uid