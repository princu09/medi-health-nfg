from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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
        return str("Send Mail On") + " " + str(self.timestamp.strftime ("%d/%m/%y")) + " From " + self.mail_From