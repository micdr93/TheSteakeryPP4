from django.shortcuts import render
from django.http import HttpResponse

def my_restaurant(request):
    return HttpResponse("restaurant")

def home(request):
    return HttpResponse("Welcome to the Steakery!")

