from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from allauth.socialaccount.models import SocialApp
from .models import User

admin.site.register(User, UserAdmin)
#admin.site.register(SocialApp)