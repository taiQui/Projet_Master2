from django.shortcuts import render
from django.http import HttpResponse
import pickle,base64
# Create your views here.
def home(request):
    if "data" in request.POST:
        data = request.POST.get('data')
        try:
            d = pickle.loads(base64.b64decode(data))
        except:
            d = "Erreur dans le decodage. Verifier si les données sont bien donnée en base64 !"
        return render(request,"index.html",{"data":d})

    return render(request,'index.html',{})
