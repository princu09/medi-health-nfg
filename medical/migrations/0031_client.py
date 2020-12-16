# Generated by Django 3.1.3 on 2020-12-16 22:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0030_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_ID', models.AutoField(primary_key=True, serialize=False)),
                ('client_First_Name', models.CharField(max_length=1000)),
                ('client_Middle_Name', models.CharField(max_length=1000)),
                ('client_Last_Name', models.CharField(max_length=1000)),
                ('client_Mobile', models.CharField(max_length=1000)),
                ('client_Email', models.CharField(max_length=1000)),
                ('client_Date_Of_Birth', models.DateField()),
                ('client_Sex', models.CharField(max_length=1000)),
                ('client_Status', models.CharField(max_length=1000)),
                ('client_Referance', models.CharField(blank=True, default='None', max_length=1000)),
                ('client_Address_1', models.CharField(max_length=1000)),
                ('client_Address_2', models.CharField(max_length=1000)),
                ('client_City', models.CharField(max_length=1000)),
                ('client_State', models.CharField(max_length=1000)),
                ('client_Zip', models.CharField(max_length=1000)),
                ('client_Disease_1', models.CharField(blank=True, default='None', max_length=1000)),
                ('client_Disease_2', models.CharField(blank=True, default='None', max_length=1000)),
                ('client_Disease_3', models.CharField(blank=True, default='None', max_length=1000)),
                ('client_Disease_4', models.CharField(blank=True, default='None', max_length=1000)),
                ('client_Disease_5', models.CharField(blank=True, default='None', max_length=1000)),
                ('client_Disease_6', models.CharField(blank=True, default='None', max_length=1000)),
                ('timestamp', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
