from os import name
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import LoginTable

# Create your views here.
def login(request):
    return render(request, 'index.html')

def sign_in(request):
    mail = request.POST['mail']
    pswd = request.POST['pswd']
    name = 'Name'
    return render(request, 'home.html', {'name': name})

def register(request):
    return render(request, 'register.html')

def sign_up(request):

    new_user = LoginTable()

    new_user.name = request.POST['name']
    new_user.mail = request.POST['mail']
    if request.POST['pswd1'] == request.POST['pswd2']:
        new_user.password = request.POST['pswd1']
        new_user.save()
        return render(request, 'registration.html')
    return HttpResponse('<h1>Passwords Not Matching</h1>')