from django.shortcuts import render
from Injection import bdd
# Create your views here.

def Error_attack(request):
    if 'search' in request.GET:
        requete = request.GET.get('search')
        database = bdd.DB("www-data","www-data","sql_injection")
        err,cmd = database.error_getUser(requete)
        if cmd == None:
            return render(request,"base_VM.html",{"error_user_projet":err})
        else:
            return render(request,"base_VM.html",{"error_user_projet":err,"error_cmd":cmd})

        # if len(user) == 0:
        #     return render(request,"base_VM.html",{"blind_nouser"::":No result."})
    # return HttpReponse("YOLO")
    return render(request,"base_VM.html")
