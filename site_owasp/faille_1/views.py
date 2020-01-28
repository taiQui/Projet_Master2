from django.shortcuts import render
from django.http import HttpResponse


def faille_1(request):
    return render(request, 'faille_1/index.html')

<<<<<<< HEAD
<<<<<<< HEAD
# def lancerMachine(request):
#     # return render('http://localhost:8080')
=======
def lancerMachine(request):
    return HttpResponse("faille_1 prete voici l'ip")
>>>>>>> 37490fcfc9b9789a29ca4709225c286298a7f7bb
=======
def lancerMachine(request):
    return HttpResponse("faille_1 prete voici l'ip")
>>>>>>> refs/remotes/origin/master

# def set_immortal(self, request):
#     return HttpResponseRedirect("../")
