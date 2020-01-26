from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    if "calcul" in request.POST:
        magique = "Bien joué ! "
        get_calcul = request.POST.get('calcul')
        if ".." in get_calcul or "cd" in get_calcul or '/' in get_calcul or '//' in get_calcul or "bin" in get_calcul or "bash" in get_calcul or "sh" in get_calcul or "dash" in get_calcul:
            return render(request,'index.html',{"calcul":"error"})
        try:
            calcul = eval(get_calcul)
            return render(request,'index.html',{"calcul":calcul})
        except Exception as e:
            print("erreur : ")
            print(e)
            return render(request,'index.html',{"calcul":e})

    return render(request,'index.html',{})
