from django.db import models

# Create your models here.
from wagtail.models import Page
from django.http import HttpResponseRedirect

class ProfileRedirectPage(Page):
    """A simple page that redirects users to their profile page."""

    def serve(self, request):
        return HttpResponseRedirect('/profile/')