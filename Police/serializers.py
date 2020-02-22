from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import  serializers
from django.contrib.auth.models import User
from . models import Crime

class NewCrimeserializer(serializers.ModelSerializer):
    class Meta:
        model=Crime
        fields=['Name','Description','Criminal_ID']
