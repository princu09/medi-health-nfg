from django.contrib import admin
from django.urls import path, include
from medical import urls

admin.site.site_header = "Medi Health NFG"
admin.site.site_title = "Medi Health NFG"
admin.site.index_title = "Welcome to Medi Health NFG"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medical.urls')),
]