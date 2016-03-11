from django.conf.urls import patterns,include,url

urlpatterns = [
	url(r'^all/$','course.views.Courses'),
	url(r'^get/(?P<course_id>\d+)/$','course.views.Course'),
	url(r'^create/$','course.views.create'),
	# url(r'^create_lesson/$','course.views.create_lesson'),

	]