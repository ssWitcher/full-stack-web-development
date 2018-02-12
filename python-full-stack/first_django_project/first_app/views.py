from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Saurabh Shrivastava !! You are the most amazing person in the world")
