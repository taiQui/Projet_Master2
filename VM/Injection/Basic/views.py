from django.shortcuts import render
from django.http import HttpResponse
from Injection import bdd

# Create your views here.

# def index(request):
#     # return HttpResponse("Hello world !")
#     return render('','')

def Basic_view(request):
    return render(request,"base_VM.html",{})


def Basic_attack(request):
    if 'search' in request.GET:
        requete = request.GET.get('search')
        database = bdd.DB("www-data","www-data","sql_injection")
        user = database.getUser(requete)
        print(user)
        if len(user) == 0:
            return render(request,"base_VM.html",{"basic_nouser":"No result."})
        return render(request,"base_VM.html",{"basic_user_projet":user})
    # return HttpReponse("YOLO")
    return render(request,"base_VM.html")
