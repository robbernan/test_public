from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	date = models.CharField(max_length=50)
	description = models.CharField(max_length=250)
