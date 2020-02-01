from django.shortcuts import render
from django.http import HttpResponse
from site_owasp import bdd
# from pages.models import MyUser

def home_view(request, *args, **kwargs): # *args, **kwargs
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "pages/home.html", {})

def profil(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") # string of can only concatenate str (not "SimpleLazyObject") to strHTML code
    if request.user.is_authenticated:
        return render(request,"pages/profil.html",{})

    else:
        return render(request, "pages/home.html", {})

def flag(request):
    # print(request)
    # for i in request:
        # print(i)
    if request.user.is_authenticated:
        if 'flag' in request.POST:
            database = bdd.DB('www-data','www-data','owasp')
            valid = database.validFlag(request.POST.get('flag'))
            if valid:
                database_check_if_already_validate= bdd.DB('www-data','www-data','owasp')
                print(request.user)
                print(request.POST.get('flag'))
                a = database_check_if_already_validate.already_validate(request.POST.get('flag'),request.user)
                print(a)
                if a == True or a == None:
                    valid = "NO"
                elif a == False:
                    valid = "YES"
                    database_addp = bdd.DB('www-data','www-data','owasp')
                    database_addp.addPoint(request.user,10)
                    database_addp.add_to_flagged(request.POST.get('flag'),request.user)

            else:
                valid = "NO"
            return render(request,'base.html',{"flag":valid})
    return render(request,'base.html',{})
