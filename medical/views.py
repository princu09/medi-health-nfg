# Page Redirect , Request Page , Response Page
from django.shortcuts import render, HttpResponse, redirect
# Showing Message alert on Main Page
from django.contrib import messages
# Create account
from django.contrib.auth.models import User
# Login account
from django.contrib.auth import authenticate, login, logout
# Gmail Request Add
import smtplib


def index(request):
    return render(request, 'index.html')

def notfound(request):
    return render(request, '404.html')

# ======== Authentication APIs ========

def handleLogin(request):
    if request.method == 'POST':
        loginUsername = request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']

        user = authenticate(username=loginUsername, password=loginPassword)

        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, "login.html")


def handleLogout(request):
    logout(request)
    return redirect('/')
