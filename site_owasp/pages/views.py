from django.shortcuts import render
from django.http import HttpResponse

# from pages.models import MyUser

def home_view(request, *args, **kwargs): # *args, **kwargs
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "pages/home.html", {})

def profil(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.user.is_authenticated:
        return render(request,"pages/profil.html",{})

    else:
        return render(request, "pages/home.html", {})
