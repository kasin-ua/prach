"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^posts/$', include("posts.urls")),
    url(r'^$', include("homepage.urls")),
    url(r'^login/', include("login.urls")),
    
    #user auth
    url(r'^accounts/login/$',  'login.views.login'),
    url(r'^accounts/auth/$',  'login.views.auth_view'),    
    url(r'^accounts/logout/$', 'login.views.logout'),
    url(r'^accounts/loggedin_student/$', 'login.views.loggedin_student'),
    url(r'^accounts/loggedin_instructor/$', 'login.views.loggedin_instructor'),
    url(r'^accounts/invalid/$', 'login.views.invalid_login'),  
    url(r'^accounts/register/$', 'login.views.register'),
    url(r'^accounts/register_success$', 'login.views.register_success'),  
     #url(r'^posts/', "<appname>.view.<function_name"),

     #course
    url(r'^courses/', include('course.urls')),
]
