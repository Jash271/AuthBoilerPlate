from django.shortcuts import render


from rest_framework import generics

from rest_framework.decorators import api_view
import json
from django.http import JsonResponse,HttpResponse
import requests

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from . serializers import NewCrimeserializer
from . models import Crime
from django.core.mail import send_mail

# Create your views here.
class NewCrime(generics.CreateAPIView):
    serializer_class=NewCrimeserializer
    queryset=Crime.objects.all()


@api_view(['POST'])
def records(request):
    crim_name=request.data['Criminal_ID']
    data=Crime.objects.filter(Name=crim_name)
    li=[]
    for x in data:
        li.append(x.Description)
    d=json.dumps(li)
    return JsonResponse(d,safe=False)

@api_view(['POST'])
def sendmail(request):
    Name=request.data['Name']
    location=request.data['Location']
    Timestamp=request.data['Timestamp']
    send_mail('Loan','{} located at {} on this time {}'.format(Name,location,Timestamp),'hrishikesh2pv@gmail.com',['shahjash271@gmail.com'],fail_silently=False)
    return JsonResponse("Done",safe=False)