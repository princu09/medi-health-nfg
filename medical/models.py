from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class MedicalShop(models.Model):
    name = models.CharField(max_length=100 , null=False)
    address_1 = models.CharField(max_length=100 , null=False)
    address_2 = models.CharField(max_length=100 , null=False)
    city = models.CharField(max_length=100 , null=False)
    state = models.CharField(max_length=100 , null=False)
    zip = models.CharField(max_length=100 , null=False)
    logo = models.ImageField(upload_to="medical")
    email = models.CharField(max_length=100 , null=False)
    mobile = models.CharField(max_length=100 , null=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images')


class HelpContact(models.Model):
    sno = models.AutoField(primary_key=True)
    mail_From = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    telephone = models.CharField(max_length=13)
    message = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str("Send Mail On") + " " + str(self.timestamp.strftime("%d/%m/%y")) + " From " + self.mail_From


class Client(models.Model):
    client_ID = models.AutoField(primary_key=True)
    client_First_Name = models.CharField(max_length=1000)
    client_Middle_Name = models.CharField(max_length=1000)
    client_Last_Name = models.CharField(max_length=1000)
    client_Mobile = models.CharField(max_length=1000)
    client_Email = models.CharField(max_length=1000)
    client_Date_Of_Birth = models.DateField(auto_now=False, auto_now_add=False)
    client_Sex = models.CharField(max_length=1000)
    client_Status = models.CharField(max_length=1000)
    client_Referance = models.CharField(max_length=1000, blank=True , default="None")
    client_Address_1 = models.CharField(max_length=1000)
    client_Address_2 = models.CharField(max_length=1000)
    client_City = models.CharField(max_length=1000)
    client_State = models.CharField(max_length=1000)
    client_Zip = models.CharField(max_length=1000)
    client_Disease_1 = models.CharField(max_length=1000, blank=True , default="None")
    client_Disease_2 = models.CharField(max_length=1000, blank=True , default="None")
    client_Disease_3 = models.CharField(max_length=1000, blank=True , default="None")
    client_Disease_4 = models.CharField(max_length=1000, blank=True , default="None")
    client_Disease_5 = models.CharField(max_length=1000, blank=True , default="None")
    client_Disease_6 = models.CharField(max_length=1000, blank=True , default="None")
    timestamp = models.TimeField(default=now)

    def __str__(self):
        return f"Client {self.client_ID} {self.client_First_Name} {self.client_Last_Name}"