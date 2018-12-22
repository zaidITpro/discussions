from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(reqeust):
    return HttpResponse('This is going to be our signup page ! Got it ?')