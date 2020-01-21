from django.urls import path

from . import views

urlpatterns = [
    path('', views.faille_1, name='faille_1'),

    path('demarageChallenge/', views.lancerMachine),
]
