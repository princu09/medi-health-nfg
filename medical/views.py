# Page Redirect , Request Page , Response Page
from django.shortcuts import render, HttpResponse, redirect
# Showing Message alert on Main Page
from django.contrib import messages
# Create account
from django.contrib.auth.models import User
# import Tables
from medical.models import HelpContact, Client
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
    if request.method == 'POST':
        client_fname = request.POST['client_fname']
        client_mname = request.POST['client_mname']
        client_lname = request.POST['client_lname']
        client_mobile = request.POST['client_mobile']
        client_email = request.POST['client_email']
        client_dob = request.POST['client_dob']
        client_sex = request.POST['client_sex']
        client_status = request.POST['client_status']
        client_referance = request.POST['client_referance']
        client_addr1 = request.POST['client_addr1']
        client_addr2 = request.POST['client_addr2']
        client_city = request.POST['client_city']
        client_state = request.POST['client_state']
        client_zip = request.POST['client_zip']
        client_diagnosis_1 = request.POST['client_diagnosis_1']
        client_diagnosis_2 = request.POST['client_diagnosis_2']
        client_diagnosis_3 = request.POST['client_diagnosis_3']
        client_diagnosis_4 = request.POST['client_diagnosis_4']
        client_diagnosis_5 = request.POST['client_diagnosis_5']
        client_diagnosis_6 = request.POST['client_diagnosis_6']

        client = Client(
            client_First_Name=client_fname,
            client_Middle_Name=client_mname,
            client_Last_Name=client_lname,
            client_Mobile=client_mobile,
            client_Email=client_email,
            client_Date_Of_Birth=client_dob,
            client_Sex=client_sex,
            client_Status=client_status,
            client_Referance=client_referance,
            client_Address_1=client_addr1,
            client_Address_2=client_addr2,
            client_City=client_city,
            client_State=client_state,
            client_Zip=client_zip,
            client_Diagnosis_1=client_diagnosis_1,
            client_Diagnosis_2=client_diagnosis_2,
            client_Diagnosis_3=client_diagnosis_3,
            client_Diagnosis_4=client_diagnosis_4,
            client_Diagnosis_5=client_diagnosis_5,
            client_Diagnosis_6=client_diagnosis_6)
        client.save()
        messages.success(request, "New Client Added Successfully !!")
        return redirect('/clients')

    client = Client.objects.all()
    context = {'client': client}
    return render(request, 'clients.html', context)


def clientsDetails(request, slug):
    clients = Client.objects.filter(client_ID=slug).first()
    context = {'clients': clients}
    return render(request, 'clientsDetails.html', context)

    # return HttpResponse(f"Hello {clients.client_Date_Of_Birth}")

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
