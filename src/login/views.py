from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')
	else:
		form = UserCreationForm()
	args={}
	args['form'] = form
	
	return render(request,'authsystem/register.html',args)
	
def register_success(request):
	return render(request,'authsystem/register_success.html','')
def login(request):
	return render(request,'authsystem/login.html','')
def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username,password=password)

	if user is not None:
		auth.login(request, user)
		if request.user.groups.filter(name="Student").exists():
			return HttpResponseRedirect('/accounts/loggedin_student')
		else:
			return HttpResponseRedirect('/accounts/loggedin_instructor')

	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin_student(request):
	return render(request,'authsystem/loggedin_student.html','')

def loggedin_instructor(request):
	return render(request,'authsystem/loggedin_instructor.html','')

def invalid_login(request):
	return render(request,'authsystem/invalid_login.html','')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
