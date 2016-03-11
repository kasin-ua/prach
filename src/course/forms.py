from django import forms
from course.models import course
# from course.models import lesson

class courseForm(forms.ModelForm):
	class Meta:
		model = course
		fields = '__all__'

# class lessonForm(forms.ModelForm):
# 	class Meta:
# 		model = lesson
# 		fields = ['title','body']
