from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Main Page"),
    path('medicine/', views.medicine, name="Medicine Page"),
    path('payments/', views.payments, name="Payments Page"),
    path('bills/', views.bills, name="Bills Page"),
    path('clients/', views.clients, name="Clients Page"),
    path('clientsDetails/<str:slug>/', views.clientsDetails , name="Clients Details Page"),
    path('about/', views.about, name="About Page"),
    path('notfound/', views.notfound, name="Page Not Found"),
    path('handleLogin/', views.handleLogin, name="Login Page"),
    path('handleLogout/', views.handleLogout, name="Login Page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
