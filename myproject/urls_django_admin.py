# myproject/myproject/urls_django_admin.py

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', admin.site.urls),
]