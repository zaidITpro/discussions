from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse('This is gonna be our new homepage')
    return render(request,'app/discussions/index.html')