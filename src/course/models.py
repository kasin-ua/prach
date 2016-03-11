from django.db import models

# Create your models here.
class course(models.Model):
	# courseid = models.PositiveIntegerField(blank = False)
	title = models.TextField(max_length = 100)
	body = models.TextField()

# class lesson(models.Model):
# 	courseid = models.PositiveIntegerField(blank = False)
# 	title = models.TextField(max_length = 100)
# 	body = models.TextField()