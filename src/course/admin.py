from django.contrib import admin

# Register your models here.
from .models import course

class courseAdmin(admin.ModelAdmin):
	list_display = ['title', 'body']
	class Meta:
		model = course

admin.site.register(course, courseAdmin)