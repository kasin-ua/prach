from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from login.forms import MyRegistrationForm
from django.contrib.auth.models import Group

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			data = request.POST.get('usertype')
			user = form.save()
			if data == 'Student':
				user.groups.add(Group.objects.get(name='Student'))
			else:
				user.groups.add(Group.objects.get(name='Instructor'))
			return HttpResponseRedirect('/accounts/register_success')
			
	args={}
	args['form'] = MyRegistrationForm()
	
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
	# m = Member.objects.get(username=request.POST['username'])
  #    if m.password == request.POST['password']:
  #        request.session['member_id'] = m.id
  #        return HttpResponse("You're logged in.")
  #    else:
  #        return HttpResponse("Your username and password didn't match.")

def loggedin_student(request):
	return render(request,'authsystem/loggedin_student.html','')

def loggedin_instructor(request):
	return render(request,'authsystem/loggedin_instructor.html','')

def invalid_login(request):
	return render(request,'authsystem/invalid_login.html','')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
