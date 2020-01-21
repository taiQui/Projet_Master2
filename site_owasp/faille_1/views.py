from django.shortcuts import render
from django.http import HttpResponse


def faille_1(request):
    return render(request, 'faille_1/index.html')

def lancerMachine(request):
    return HttpResponse("faille_1 prete voici l'ip")

# def set_immortal(self, request):
#     return HttpResponseRedirect("../")
