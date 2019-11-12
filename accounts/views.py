from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserLoginForm,UserRegistrationForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = UserLoginForm(request.POST)

        if form.is_valid():
            return render(request,'accounts/login.htm',{'form':form})
    else:
        form = UserLoginForm()
        return render(request,'accounts/login.htm',{'form':form})
    

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            return render(request,'accounts/register.htm',{'form':form})
    else:
        form = UserRegistrationForm()
        return render(request,'accounts/register.htm',{'form':form})