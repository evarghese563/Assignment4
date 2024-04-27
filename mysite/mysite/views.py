from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import requests


def home(request):
    return render(request,"main.html")

def checkout(request):
    return render(request, "checkout.html")