from django import forms
from course.models import course

class courseForm(forms.ModelForm):
	class Meta:
		model = course
		fields = '__all__'