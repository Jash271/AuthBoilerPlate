# Generated by Django 2.2.8 on 2020-02-22 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Police', '0002_crime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crime',
            name='Photo',
        ),
    ]
