from django.shortcuts import render
from django.http import HttpResponse


def faille_1(request):
    return render(request, 'faille_1/index.html')

# def lancerMachine(request):
#     # return render('http://localhost:8080')

# def set_immortal(self, request):
#     return HttpResponseRedirect("../")
