# Page Redirect , Request Page , Response Page
from django.shortcuts import render, HttpResponse, redirect
# Showing Message alert on Main Page
from django.contrib import messages
# Create account
from django.contrib.auth.models import User
# import Tables
from medical.models import HelpContact
# Login account
from django.contrib.auth import authenticate, login, logout
# Gmail Request Add
import smtplib


def index(request):
    return render(request, 'index.html')


def medicine(request):
    return render(request, 'medicine.html')


def payments(request):
    return render(request, 'payments.html')


def bills(request):
    return render(request, 'bills.html')


def clients(request):
    return render(request, 'clients.html')


def about(request):

    Email_ID = 'pmkvyprince@gmail.com'  # Your Email
    Email_PSWD = 'nfg$786#07#132*'  # Your Password

    if request.method == 'POST':
        from_company = request.POST['email']
        sub = request.POST['subject']
        tel = request.POST['tel']
        msg = request.POST['message']
        to = "northfoxgroup@hotmail.com"

        # print(f"Email to {to} send with Subject : {sub} and massage {msg}")

        # ======================== Gmail SMTP Server ========================
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # ======================== STMP Server Connect or Start =============
        s.starttls()

        # ======================== Login to Email ===========================
        s.login(Email_ID, Email_PSWD)

        # ======================== Send Mail to User ========================
        s.sendmail(
            Email_ID, to, f"Subject : {sub} \n\n From : {from_company} \n Phone : {tel} \n\n {msg} ")

        # ======================== Mail Quit ================================
        s.quit()

        helpContact = HelpContact(
            mail_From=from_company, subject=sub, message=msg, telephone=tel)
        helpContact.save()

    helpContact = HelpContact.objects.all()
    context = {'helpContact': helpContact}
    return render(request, 'about.html', context)


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
