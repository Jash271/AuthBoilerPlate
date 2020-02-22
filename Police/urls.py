from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('NewCrime',views.NewCrime.as_view(),name='NewCrime'),
    path('records',views.records,name='records'),
    
]
