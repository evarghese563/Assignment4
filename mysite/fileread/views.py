from django.shortcuts import render, loader

from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def home(request):
    return render(request,"main.html")

def checkout(request):
    return render(request,"checkout.html")
