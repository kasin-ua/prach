from django.shortcuts import render
from course.models import course
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from course.forms import courseForm
from django.core.context_processors import csrf

# Create your views here.

def Courses(request):
	return render(request,'course/courses.html',{'courses':course.objects.all()},'')

def Course(request, course_id=1):
	return render(request,'course/course.html',{'course':course.objects.get(id=course_id)},'')

def create(request):
	if request.POST:
		form = courseForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/courses/all')

	else:
		form = courseForm()

	args = {}
	args['form'] = form

	return render(request, 'course/create_course.html',args)

# def create_lesson(request):
	