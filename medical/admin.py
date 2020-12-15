from django.contrib import admin
from .models import Profile , HelpContact , Client

# Register your models here.

admin.site.register(Profile)
admin.site.register(HelpContact)
admin.site.register(Client)