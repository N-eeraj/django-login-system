from os import name
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import LoginTable

# Create your views here.
def login(request):
    return render(request, 'index.html')

def sign_in(request):

    try:
        obj = LoginTable.objects.get(mail=request.POST['mail'])

        if obj.password == request.POST['pswd']:
            user = obj.name
            return render(request, 'home.html', {'name': user})
        
        return HttpResponse('<h1>Invalid Credentials</h1><a href="..">Back</a>')
    
    except:
        return HttpResponse('<h1>Invalid Credentials</h1><a href="..">Back</a>')

def register(request):
    return render(request, 'register.html')

def sign_up(request):

    h1 = 'Passwords Not Matching'
    success = False

    new_user = LoginTable()
    new_user.name = request.POST['name']
    new_user.mail = request.POST['mail']

    if request.POST['pswd1'] == request.POST['pswd2']:
        new_user.password = request.POST['pswd1']
        new_user.save()

        h1 = 'Registration Successful'
        success = True

    return render(request, 'registration.html', {'heading': h1, 'success': success})