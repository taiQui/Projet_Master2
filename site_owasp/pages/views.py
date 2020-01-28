from django.shortcuts import render
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> refs/remotes/origin/master

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", {})
<<<<<<< HEAD
>>>>>>> 37490fcfc9b9789a29ca4709225c286298a7f7bb
=======
>>>>>>> refs/remotes/origin/master
