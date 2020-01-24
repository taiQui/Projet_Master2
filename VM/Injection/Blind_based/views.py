from django.shortcuts import render

# Create your views here.

def Blind_view(request):
    return render(request,"index.html",{})
