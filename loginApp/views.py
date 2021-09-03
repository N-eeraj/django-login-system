from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'index.html')

def sign_in(request):
    mail = request.POST['mail']
    pswd = request.POST['pswd']
    return HttpResponse('<h1>Login Success</h1>')

def register(request):
    return render(request, 'register.html')

def sign_up(request):
    name = request.POST['name']
    mail = request.POST['mail']
    pswd1 = request.POST['pswd1']
    pswd2 = request.POST['pswd2']
    return HttpResponse('<h1>Registration Success</h1>')