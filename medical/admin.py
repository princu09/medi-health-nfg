from django.contrib import admin
from .models import Profile , HelpContact , MedicalShop ,Bill , Client

# Register your models here.

admin.site.register(MedicalShop)
admin.site.register(Profile)
admin.site.register(HelpContact)
admin.site.register(Client)
admin.site.register(Bill)