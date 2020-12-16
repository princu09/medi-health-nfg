from django.contrib import admin
from .models import Profile , HelpContact , Client , MedicalShop

# Register your models here.

admin.site.register(MedicalShop)
admin.site.register(Profile)
admin.site.register(HelpContact)
admin.site.register(Client)