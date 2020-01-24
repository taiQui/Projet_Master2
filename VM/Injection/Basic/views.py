from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     # return HttpResponse("Hello world !")
#     return render('','')

def Basic_view(request):
    return render(request,"base_VM.html",{})

def Basic_php(request):
    return render(request,"action.php",{})

def Basic_attack(request):
    print(request.GET)
    if 'search' in request.GET:
        return HttpResponse("SEXE")
    return render(request,"base_VM.html")
