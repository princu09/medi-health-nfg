from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Main Page"),
    path('notfound/' , views.notfound , name="Page Not Found"),
    path('handleLogin/', views.handleLogin, name="Login Page"),
    path('handleLogout/' , views.handleLogout , name="Login Page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
