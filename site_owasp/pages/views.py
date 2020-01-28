from django.shortcuts import render
from django.http import HttpResponse
from site_owasp import bdd
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

def flag(request):
    print(request)
    for i in request:
        print(i)
    if request.user.is_authenticated:
        if 'flag' in request.POST:
            database = bdd.DB('www-data','www-data','owasp')
            valid = database.validFlag(request.POST.get('flag'))
            if valid:
                valid = "YES"
                database2 = bdd.DB('www-data','www-data','owasp')
                database2.addPoint(request.user)
            else:
                valid = "NO"
            return render(request,'base.html',{"flag":valid})
    return render(request,'base.html',{})
