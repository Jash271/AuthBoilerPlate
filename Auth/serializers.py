
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import  serializers
from django.contrib.auth.models import User

class Signupserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password']

class LoginSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username','password']