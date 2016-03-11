from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

# class the_user(models.Model):
# 	Student = 'Student'
# 	Instructor = 'Instructor'
# 	usertype_choice = (
# 		(Student,'Student'),
# 		(Instructor,'Instructor'),

# 		)
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	usertype = models.CharField(max_length = 100, choices=usertype_choice,default=Student)
    # usertype = forms.ChoiceField(choices=usertype_choice)
	# Student = 'Student'
	# Instructor = 'Instructor' 
	# usertype_choice = (
 #    (Student, 'Student'),
 #    (Instructor, 'Instructor'),
 #    )
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # usertype = forms.ChoiceField(choices=usertype_choice)
# class signup(models.Model):
# 	email = models.EmailField(max_length = 100, blank = False, null = False)
# 	firstname = models.CharField(max_length = 100, null = False)
# 	lastname = models.CharField(max_length = 100, null = False)
# 	password = models.CharField(max_length = 100,null = False,blank = False)


# 	def __str__(self):
# 		return self.email