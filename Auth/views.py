from django.shortcuts import render
from . serializers import Signupserializer

from rest_framework import generics

from rest_framework.decorators import api_view
import json
from django.http import JsonResponse,HttpResponse
import requests

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
import json
# Create your views here.
class SignupUser(generics.CreateAPIView):
    serializer_class=Signupserializer
    queryset=User.objects.all()
    def create(self,request):
        
        u_name=request.data['username']
        f_name=request.data['first_name']
        l_name=request.data['last_name']
        passw=request.data['password']
        e_mail=request.data['email']
        print(u_name)
        try: 
            User.objects.get(username=u_name)

            return JsonResponse('Username Already exists',safe=False)
        except:
            
            
            u=User(username=u_name,first_name=f_name,last_name=l_name,email=e_mail)
            u.set_password(passw)
            u.save()
            n_user=User.objects.get(username=u_name)
            login(request,n_user)
            return JsonResponse('loggedIn',safe=False)
            



                

            

