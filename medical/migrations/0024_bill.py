# Generated by Django 3.1.3 on 2020-12-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0023_auto_20201216_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
