# Generated by Django 2.2.8 on 2020-02-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Police', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Photo', models.ImageField(upload_to='criminals')),
                ('Description', models.TextField()),
                ('Criminal_ID', models.CharField(max_length=10)),
            ],
        ),
    ]
