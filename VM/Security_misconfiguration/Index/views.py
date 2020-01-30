from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    if "username" in request.POST and "password" in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "admin" and password=="dfad37d1d67f40b64cbb5d2228d27fbe":
            return render(request,"login.html",{})
        else:
            return render(request,"index.html",{"error":True})
    return render(request,"index.html",{})


# def login(request):
