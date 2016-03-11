from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	Student = 'Student'
	Instructor = 'Instructor' 
	usertype_choice = (
    (Student, 'Student'),
    (Instructor, 'Instructor'),
    )
	firstname = forms.CharField(required = True)
	lastname = forms.CharField(required = True)
	usertype = forms.ChoiceField(choices=usertype_choice)
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('firstname','lastname','email','username','password1','password2','usertype')

	def save(self, commit = True):
		user = super(MyRegistrationForm,self).save(commit=False)
		user.first_name = self.cleaned_data['firstname']
		user.last_name = self.cleaned_data['lastname']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

# class signupform(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput)
# 	class Meta:
# 		model = signup
		
# 		fields = ['email','password','firstname','lastname']