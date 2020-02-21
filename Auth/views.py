from django.shortcuts import render
from . serializers import Signupserializer,LoginSerilaizer

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
# Create your views here.
@csrf_exempt
def SignupUser(request):
    
        if request.method == 'POST':

            u_name=request.POST['username']
            f_name=request.POST['first_name']
            l_name=request.POST['last_name']
            passw=request.POST['password']
            e_mail=request.POST['email']
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
                print(request.user)
                return JsonResponse('loggedIn',safe=False)


 
class  LoginUser(generics.CreateAPIView):
    serializer_class=LoginSerilaizer
    queryset=User.objects.all()
    def create(self, request):
        
        u_name=request.data['username']
        p=request.data['password']
        user = authenticate(username=u_name, password=p)

        if user is not None:
            user=User.objects.get(username=u_name)
            login(request,user)
            return JsonResponse('Done',safe=False)
        else:
            return JsonResponse('None',safe=False)


                

            

