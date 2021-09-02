from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'index.html')

def sign_in(request):
    mail = request.POST['mail']
    pswd = request.POST['pswd']

    print('*'*25)
    print(mail, pswd)
    print('*'*25)
    return HttpResponse('<h1>Login Success</h1>')