from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# from login.models import the_user

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class the_userInline(admin.StackedInline):
#     model = the_user 
#     can_delete = False
#     verbose_name_plural = 'the user'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (the_userInline, )

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# Register your models here.
# from .models import signup
# from .forms import signupform

# class signupadmin(admin.ModelAdmin):
# 	list_display = ["__str__", "firstname","lastname"]
# 	form = signupform
# 	#class Meta:
# 		#model = signup

# admin.site.register(signup, signupadmin)