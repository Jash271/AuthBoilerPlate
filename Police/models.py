from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Police(models.Model):
    Ref=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Photo=models.ImageField(upload_to='media')
    Chowki=models.CharField(max_length=100)


class  Crime(models.Model):
    Name=models.CharField(max_length=100)
    
    Description=models.TextField()
    Criminal_ID=models.CharField(max_length=10)






  