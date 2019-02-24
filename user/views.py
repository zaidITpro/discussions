from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'app/discussions/signup-simple.html')

def signin(request):
    return render(request,'app/discussions/signin-simple.html')