from django.urls import path

from . import views

urlpatterns = [
    path('', views.faille_1, name='faille_1'),

<<<<<<< HEAD
<<<<<<< HEAD
    # path('demarageChallenge/', views.lancerMachine),
=======
    path('demarageChallenge/', views.lancerMachine),
>>>>>>> 37490fcfc9b9789a29ca4709225c286298a7f7bb
=======
    path('demarageChallenge/', views.lancerMachine),
>>>>>>> refs/remotes/origin/master
]
