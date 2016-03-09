from django.db import models

# Create your models here.
class course(models.Model):
	title = models.TextField(max_length = 100)
	body = models.TextField()