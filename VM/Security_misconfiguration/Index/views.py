from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    if "username" in request.POST and "password" in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "admin" and password=="Fl4g4d05_F0ll0w_U5":
            return render(request,"login.html",{})
        else:
            return render(request,"index.html",{"error":True})
    return render(request,"index.html",{})


# def login(request):
