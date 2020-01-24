from django.shortcuts import render

# Create your views here.

def Error_view(request):
    return render(request,"index.html",{})
