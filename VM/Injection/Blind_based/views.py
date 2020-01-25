from django.shortcuts import render
from Injection import bdd
# Create your views here.

def Blind_attack(request):
    if 'search' in request.GET:
        requete = request.GET.get('search')
        database = bdd.DB("www-data","www-data","sql_injection")
        user = database.blind_getUser(requete)
        print(user)
        # if len(user) == 0:
        #     return render(request,"base_VM.html",{"blind_nouser":"No result."})
        return render(request,"base_VM.html",{"blind_user_projet":user})
    # return HttpReponse("YOLO")
    return render(request,"base_VM.html")
